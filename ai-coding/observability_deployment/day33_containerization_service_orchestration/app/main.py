"""Day 33：可容器化的最小 FastAPI Agent 服务。"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest
from pydantic import BaseModel
from redis.asyncio import Redis
from starlette.responses import Response

app = FastAPI(title="Containerized Agent Demo")
TASKS = Counter("agent_tasks_total", "Total demo Agent tasks")
REDIS_RETRIES = Counter("agent_redis_retries_total", "Redis retry attempts")
STATE_PATH = Path(os.getenv("AGENT_STATE_PATH", "/data/approvals.json"))
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
MAX_RETRIES = int(os.getenv("REDIS_MAX_RETRIES", "3"))


class TaskRequest(BaseModel):
    """创建演示任务的请求体。"""

    prompt: str


class ApprovalRequest(BaseModel):
    """创建审批状态的请求体。"""

    task_id: str


def read_secret() -> str:
    """从运行时 Secret 文件读取 API Key，不把密钥写入镜像。

    Returns:
        Secret 内容；未配置时返回空字符串。
    """
    secret_path = os.getenv("DEEPSEEK_API_KEY_FILE", "/run/secrets/deepseek_api_key")
    path = Path(secret_path)
    return path.read_text(encoding="utf-8").strip() if path.exists() else ""


async def redis_ping_with_retry() -> bool:
    """使用有限次数重试检查 Redis 是否可用。

    Returns:
        Redis 可用返回 ``True``，重试耗尽返回 ``False``。
    """
    for attempt in range(MAX_RETRIES):
        try:
            client = Redis.from_url(REDIS_URL, socket_connect_timeout=1)
            try:
                return bool(await client.ping())
            finally:
                await client.aclose()
        except Exception:
            if attempt < MAX_RETRIES - 1:
                REDIS_RETRIES.inc()
                await asyncio.sleep(0.2 * (attempt + 1))
    return False


def load_state() -> dict[str, Any]:
    """从 Volume 加载审批状态，容器重启后继续使用。"""
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict[str, Any]) -> None:
    """把审批状态写入 Volume。

    Args:
        state: 要持久化的审批状态。
    """
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state), encoding="utf-8")


@app.get("/health/live")
async def liveness() -> dict[str, str]:
    """检查进程是否存活，不检查外部依赖。"""
    return {"status": "alive"}


@app.get("/health/ready")
async def readiness() -> dict[str, str]:
    """检查 Redis 和运行时 Secret，决定服务是否接收流量。"""
    if not await redis_ping_with_retry():
        raise HTTPException(status_code=503, detail="redis unavailable")
    if not read_secret():
        raise HTTPException(status_code=503, detail="DeepSeek secret unavailable")
    return {"status": "ready"}


@app.get("/metrics")
async def metrics() -> Response:
    """暴露 Prometheus 指标。"""
    return Response(generate_latest(), media_type="text/plain")


@app.post("/tasks")
async def create_task(request: TaskRequest) -> dict[str, str]:
    """创建一个演示任务并记录到 Redis。

    Args:
        request: 包含 Agent prompt 的请求体。
    """
    if not await redis_ping_with_retry():
        raise HTTPException(status_code=503, detail="redis unavailable")
    client = Redis.from_url(REDIS_URL)
    try:
        task_id = str(await client.incr("agent:task:id"))
        await client.hset(f"agent:task:{task_id}", mapping={"prompt": request.prompt})
    finally:
        await client.aclose()
    TASKS.inc()
    return {"task_id": task_id, "status": "accepted"}


@app.post("/approvals")
async def create_approval(request: ApprovalRequest) -> dict[str, str]:
    """创建 pending_approval 状态并持久化到 Volume。

    Args:
        request: 需要人工审批的任务。
    """
    state = load_state()
    state[request.task_id] = "pending_approval"
    save_state(state)
    return {"task_id": request.task_id, "status": state[request.task_id]}


@app.get("/approvals/{task_id}")
async def get_approval(task_id: str) -> dict[str, str]:
    """读取审批状态，用于验证容器重启后的恢复。"""
    status = load_state().get(task_id)
    if status is None:
        raise HTTPException(status_code=404, detail="approval not found")
    return {"task_id": task_id, "status": status}
