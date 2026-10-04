"""把受控文件、Shell 与模型调用串成一个代码分析任务。"""

import asyncio
import json
import os
from pathlib import Path

from credentials import CredentialBroker
from model_client import ModelClient, ModelUnavailable
from sandbox_fs import Workspace
from sandbox_shell import run_check


def record_audit(path: Path, status: str) -> None:
    """只记录状态，不记录源码、模型内容、URL 或凭据。"""
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"event": "analysis", "status": status}) + "\n")


async def analyze_project(
    workspace: Workspace, relative_file: str, model: ModelClient, audit_path: Path
) -> dict[str, str]:
    """分析工作区内一个文件，返回静态检查与模型报告。

    参数:
        workspace: 已创建并装入项目文件的独立工作区。
        relative_file: 用户选择的工作区内相对路径。
        model: 指向固定模型服务的客户端。
        audit_path: 宿主侧审计日志文件；仅写入状态，不包含原始输入。
    """
    try:
        source = workspace.read(relative_file)
        # 同步容器管理放在线程里，避免阻塞 Agent 的异步事件循环。
        check = await asyncio.to_thread(run_check, workspace.root, "syntax")
        try:
            report = await model.analyze(source)
            status = "ok"
        except ModelUnavailable:
            # 静态检查已完成，模型故障时返回明确降级结果。
            report, status = "模型服务不可用；已保留静态检查结果。", "degraded"
    except Exception:
        record_audit(audit_path, "failed")
        raise
    record_audit(audit_path, status)
    return {"status": status, "check": check or "syntax ok", "report": report}


async def demo() -> None:
    """用环境变量配置本地 OpenAI-compatible 模型服务。"""
    url = os.environ.get("DAY27_MODEL_URL", "http://127.0.0.1:8000/v1")
    allowed_host = os.environ.get("DAY27_MODEL_HOST", "127.0.0.1")
    model = ModelClient(
        url,
        os.environ.get("DAY27_MODEL_NAME", "local-model"),
        allowed_host,
        CredentialBroker(),
        allow_loopback=allowed_host in ("127.0.0.1", "localhost"),
    )
    try:
        with Workspace() as workspace:
            workspace.add("sample.py", b"print('hello')\n")
            audit_path = Path(os.environ.get("DAY27_AUDIT_LOG", "day27_audit.jsonl"))
            print(await analyze_project(workspace, "sample.py", model, audit_path))
    finally:
        await model.close()


if __name__ == "__main__":
    asyncio.run(demo())
