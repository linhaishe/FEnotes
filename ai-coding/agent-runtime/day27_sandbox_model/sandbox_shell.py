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
    """在受限 Docker 容器中运行允许的检查命令。

    工作区以只读方式挂载到容器的 `/workspace`，容器禁用网络、提权和
    全部 Linux capabilities，并限制资源、执行时间和输出大小。命令名
    必须经过 `command_for` 的白名单校验，不能直接传入任意 Shell 字符串。

    参数:
        workspace: 已创建的独立工作区目录。
        name: 策略中允许的检查命令名称，例如 `"list"` 或 `"syntax"`。

    返回:
        检查命令的标准输出。

    异常:
        ValueError: `name` 不在允许的命令白名单中。
        ShellUnavailable: Docker 不可用、命令超时、输出超限或执行失败。
    """
    inner = command_for(name)
    if os.geteuid() == 0: # 这行用于检查当前进程是否以 root 用户运行 用户 ID 为 0：表示当前是 root Worker 必须以普通用户运行，不能以 root 身份启动。
        raise ShellUnavailable("run worker as non-root")
    container = f"day27-{uuid.uuid4().hex}" # 这行代码生成一个临时 Docker 容器名称
    """
    各部分含义：
- day27-：固定前缀，方便识别这是本任务创建的容器。
- uuid.uuid4()：生成随机 UUID。
- .hex：把 UUID 转成不带连字符的字符串。
- f"..."：格式化字符串，把随机 ID 拼接进名称。
这样做可以保证每次运行的容器名称基本不会重复，后续超时或异常时可以准确清理
    """
    command = [
        "docker", "run", "--rm", "--name", container,
        "--network", "none", "--read-only", "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges", "--pids-limit", "64",
        "--memory", "256m", "--cpus", "0.5", "--user", f"{os.getuid()}:{os.getgid()}",
        "--tmpfs", "/tmp:rw,noexec,nosuid,size=16m",
        "--mount", f"type=bind,src={workspace.resolve()},dst=/workspace,readonly",
        "--workdir", "/workspace", "python:3.12-slim", *inner,
    ]
    """
    这段代码是在拼接一条 Docker 命令，用受限容器运行检查程序：

```python
command = [
    "docker", "run",
    "--rm",
    "--name", container,
    "--network", "none",
    "--read-only",
    "--cap-drop", "ALL",
    "--security-opt", "no-new-privileges",
    "--pids-limit", "64",
    "--memory", "256m",
    "--cpus", "0.5",
    "--user", f"{os.getuid()}:{os.getgid()}",
    "--tmpfs", "/tmp:rw,noexec,nosuid,size=16m",
    "--mount", f"type=bind,src={workspace.resolve()},dst=/workspace,readonly",
    "--workdir", "/workspace",
    "python:3.12-slim",
    *inner,
]
```

它最终大致相当于：

```bash
docker run --rm --name day27-xxx \
  --network none \
  --read-only \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 64 \
  --memory 256m \
  --cpus 0.5 \
  --user 当前用户UID:当前用户GID \
  --tmpfs /tmp:rw,noexec,nosuid,size=16m \
  --mount type=bind,src=workspace路径,dst=/workspace,readonly \
  --workdir /workspace \
  python:3.12-slim \
  检查命令
```

主要参数含义：

- `docker run`：创建并运行容器。
- `--rm`：容器退出后自动删除。
- `--name`：设置容器名称。
- `--network none`：完全禁用网络。
- `--read-only`：容器根文件系统只读。
- `--cap-drop ALL`：删除所有 Linux 权限能力。
- `--security-opt no-new-privileges`：禁止进程获得更高权限。
- `--pids-limit 64`：最多创建 64 个进程。
- `--memory 256m`：最多使用 256 MB 内存。
- `--cpus 0.5`：最多使用半个 CPU。
- `--user ...`：使用当前普通用户运行，避免容器内以 root 身份运行。
- `--tmpfs /tmp:rw,noexec,nosuid,size=16m`：提供一个最多 16 MB 的临时目录：
  - 可读写；
  - 禁止执行其中的文件；
  - 禁止 setuid 提权。
- `--mount ...`：把 workspace 以只读方式挂载到容器的 `/workspace`。
- `--workdir /workspace`：设置容器内的当前工作目录。
- `python:3.12-slim`：使用的 Docker 镜像。
- `*inner`：展开实际检查命令，例如 `syntax` 对应的 Python 命令。

因此，这段代码的整体目的就是：

> 在没有网络、没有特权、资源受限、只能读取 workspace 的 Docker 容器中运行固定检查命令。
    """
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except OSError:
        raise ShellUnavailable("container runtime unavailable") from None
    
    """
这段代码的作用是：启动一个外部命令，并在启动失败时抛出自定义异常。
具体来说：
1. subprocess.Popen(command)
   启动 command 指定的系统命令，并立即返回一个进程对象。
2. stdout=subprocess.PIPE
   捕获命令的标准输出，之后可以通过 process.stdout 或 communicate() 读取。
3. stderr=subprocess.STDOUT
   将错误输出合并到标准输出中，因此两类输出会进入同一个管道。
4. except OSError
   如果命令不存在、无法执行，或系统资源不可用，就捕获操作系统错误。
5. raise ShellUnavailable(...) from None
   将底层错误转换成更符合业务含义的 ShellUnavailable 异常，并隐藏原始异常链。
简单说：它尝试启动一个容器运行时或 Shell 命令；如果启动不了，就报告“容器运行时不可用”。
    """
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
