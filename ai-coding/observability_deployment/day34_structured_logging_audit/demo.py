"""为 FastAPI Agent 请求生成 request_id 和单行 JSON 运行日志。"""

from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI(title="Agent JSON Logging Demo")
logger = logging.getLogger("day34.agent")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)


class AgentRequest(BaseModel):
    """Agent 请求体；Prompt 只用于处理，不写入日志。"""

    prompt: str


@app.middleware("http")
async def log_request(request: Request, call_next):
    """给请求分配 ID，并在响应完成时写一行 JSON 日志。

    Args:
        request: 当前 HTTP 请求。
        call_next: 调用下一个中间件或路由的函数。

    Returns:
        含 ``X-Request-ID`` 响应头的 HTTP 响应。
    """
    request_id = uuid4().hex
    request.state.request_id = request_id
    started = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    logger.info(
        json.dumps(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "level": "info",
                "event": "agent_request_finished",
                "request_id": request_id,
                "status_code": response.status_code,
                "duration_ms": round((time.perf_counter() - started) * 1000, 2),
            },
            ensure_ascii=False,
        )
    )
    return response


@app.post("/agent")
async def run_agent(body: AgentRequest, request: Request) -> dict[str, str]:
    """运行固定响应的 Mock Agent，演示请求与日志关联。

    Args:
        body: 用户的 Agent 请求。
        request: 包含当前 ``request_id`` 的 HTTP 请求。

    Returns:
        Mock Agent 答案和请求 ID。
    """
    return {"request_id": request.state.request_id, "answer": "请求已处理"}
