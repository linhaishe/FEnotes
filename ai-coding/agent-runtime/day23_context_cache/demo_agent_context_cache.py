"""Standalone Agent flow demo: context cache first, model call second."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from fastapi import Depends, FastAPI
from redis.asyncio import Redis

from .demo_dependencies import (
    call_llm,
    compress_context,
    redis_client,
    trim_context,
)

app = FastAPI(title="Agent context cache flow demo")


async def cached_context(
    messages: list[dict[str, str]], client: Redis
) -> dict[str, Any]:
    payload = json.dumps(messages, ensure_ascii=False, sort_keys=True).encode()
    key = "agent-context:" + hashlib.sha256(payload).hexdigest()
    cached = await client.get(key)
    if cached is not None:
        return {"source": "redis", "messages": json.loads(cached)}

    result = compress_context(trim_context(messages, 120))
    await client.set(key, json.dumps(result, ensure_ascii=False), ex=300)
    return {"source": "computed", "messages": result}


@app.post("/chat")
async def chat(
    messages: list[dict[str, str]],
    client: Redis = Depends(redis_client),
) -> dict[str, Any]:
    context = await cached_context(messages, client)
    response = await call_llm(context["messages"])
    return {
        "context_source": context["source"],
        "messages": context["messages"],
        "answer": response.choices[0].message.content,
    }
