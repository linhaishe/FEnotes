"""在受限 Docker 容器里执行固定的代码检查。"""

import os
import selectors
import subprocess
import time
import uuid
from pathlib import Path

from policy import POLICY


class ShellUnavailable(RuntimeError):
    """容器运行失败、超时或输出超过上限。"""


def command_for(name: str) -> list[str]:
    """将外部名字映射到固定参数列表，绝不拼接模型输出。"""
    if name not in POLICY.commands:
        raise ValueError("command not allowed")
    if name == "list":
        return ["python", "-c", "import os; print('\\n'.join(sorted(os.listdir('/workspace'))))"]
    # ast.parse 只解析语法，不导入或执行用户源码，也无需写入 __pycache__。
    return ["python", "-c", "import ast,pathlib; [ast.parse(p.read_text()) for p in pathlib.Path('/workspace').rglob('*.py')]"]


def run_check(workspace: Path, name: str) -> str:
    """挂载只读工作区、禁网络/提权，限时限量读取容器输出。

    参数:
        workspace: 已创建的独立工作区。
        name: 策略中允许的检查命令名。

    返回:
        命令的标准输出，非零退出抛出 ShellUnavailable。
    """
    inner = command_for(name)
    if os.geteuid() == 0:
        raise ShellUnavailable("run worker as non-root")
    container = f"day27-{uuid.uuid4().hex}"
    command = [
        "docker", "run", "--rm", "--name", container,
        "--network", "none", "--read-only", "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges", "--pids-limit", "64",
        "--memory", "256m", "--cpus", "0.5", "--user", f"{os.getuid()}:{os.getgid()}",
        "--tmpfs", "/tmp:rw,noexec,nosuid,size=16m",
        "--mount", f"type=bind,src={workspace.resolve()},dst=/workspace,readonly",
        "--workdir", "/workspace", "python:3.12-slim", *inner,
    ]
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except OSError:
        raise ShellUnavailable("container runtime unavailable") from None
    output = bytearray()
    deadline = time.monotonic() + POLICY.shell_timeout_seconds
    selector = selectors.DefaultSelector()
    assert process.stdout is not None
    selector.register(process.stdout, selectors.EVENT_READ)
    try:
        while selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ShellUnavailable("check timed out")
            for key, _ in selector.select(remaining):
                chunk = os.read(key.fd, 4096)
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                output.extend(chunk)
                if len(output) > POLICY.max_output_bytes:
                    raise ShellUnavailable("check output too large")
        if process.wait(timeout=max(0.1, deadline - time.monotonic())) != 0:
            raise ShellUnavailable("check failed")
        return output.decode("utf-8", errors="replace")
    except (subprocess.TimeoutExpired, ShellUnavailable):
        # docker 客户端退出不保证容器退出；按唯一名称强制删除容器。
        process.kill()
        subprocess.run(["docker", "rm", "-f", container], capture_output=True, timeout=5, check=False)
        raise ShellUnavailable("check interrupted") from None
    finally:
        selector.close()
        process.stdout.close()
        process.wait()
