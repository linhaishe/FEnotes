"""为 FastAPI Agent 请求、模型和工具调用输出 JSON 运行日志。"""

from __future__ import annotations

import json
import logging
import os
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Iterator
from uuid import uuid4
from rich.console import Console
from rich.logging import RichHandler

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI(title="Agent JSON Logging Demo")
logger = logging.getLogger("day34.agent")
logger.setLevel(logging.INFO)
logger.propagate = False
LOG_FORMAT = os.getenv("LOG_FORMAT", "json")
if LOG_FORMAT == "console":
    handler = RichHandler(
        console=Console(file=sys.stdout), show_time=False, show_path=False
    )
else:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)


class AgentRequest(BaseModel):
    """Agent 请求体；Prompt 只用于处理，不写入日志。"""

    prompt: str


def log_event(event: str, request_id: str, **fields: object) -> None:
    """按配置输出人类可读日志或单行 JSON 日志。

    Args:
        event: 稳定的事件名称。
        request_id: 当前请求的关联 ID。
        fields: 状态码、耗时或错误类型等非敏感字段。
    """
    level = "error" if event.endswith("_failed") else "info"
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "event": event,
        "request_id": request_id,
        **fields,
    }
    message = (
        f"{event}  req={request_id[:8]}"
        + "".join(f"  {key}={value}" for key, value in fields.items())
        if LOG_FORMAT == "console"
        else json.dumps(record, ensure_ascii=False)
    )
    logger.log(
        logging.ERROR if level == "error" else logging.INFO,
        message,
    )


@contextmanager
def logged_call(stage: str, request_id: str) -> Iterator[None]:
    """记录模型或工具调用的开始、结果、耗时及错误分类。

    Args:
        stage: ``model`` 或 ``tool``。
        request_id: 当前请求的关联 ID。

    Yields:
        被测调用的执行位置。
    """
    started = time.perf_counter()
    log_event(f"{stage}_call_started", request_id)
    try:
        yield
    except Exception as exc:
        log_event(
            f"{stage}_call_failed",
            request_id,
            duration_ms=round((time.perf_counter() - started) * 1000, 2),
            error_type="timeout" if isinstance(exc, TimeoutError) else "error",
        )
        raise
    else:
        log_event(
            f"{stage}_call_finished",
            request_id,
            duration_ms=round((time.perf_counter() - started) * 1000, 2),
        )


def mock_model(prompt: str) -> str:
    """根据请求决定是否调用天气工具。

    Args:
        prompt: 用户输入，仅在内存中处理。

    Returns:
        ``weather`` 或 ``general`` 决策。
    """
    return "weather" if prompt.startswith("查询天气:") else "general"


def mock_weather(city: str) -> str:
    """返回固定天气结果。

    Args:
        city: 查询城市，仅在内存中处理。

    Returns:
        固定天气文本。
    """
    return {"上海": "sunny", "北京": "cloudy"}.get(city, "unknown")


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
    log_event(
        "agent_request_finished",
        request_id,
        status_code=response.status_code,
        duration_ms=round((time.perf_counter() - started) * 1000, 2),
    )
    return response


@app.post("/agent")
async def run_agent(body: AgentRequest, request: Request) -> dict[str, str]:
    """运行 Mock Agent，记录模型和工具调用事件。

    Args:
        body: 用户的 Agent 请求。
        request: 包含当前 ``request_id`` 的 HTTP 请求。

    Returns:
        Mock Agent 答案和请求 ID。
    """
    request_id = request.state.request_id
    try:
        with logged_call("model", request_id):
            decision = mock_model(body.prompt)
        if decision == "weather":
            city = body.prompt.split(":", 1)[1].strip()
            with logged_call("tool", request_id):
                answer = mock_weather(city)
        else:
            answer = "请求已处理"
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Agent dependency failed") from exc
    return {"request_id": request_id, "answer": answer}
