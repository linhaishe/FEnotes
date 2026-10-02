"""Dependency-based FastAPI + Redis + LiteLLM cache demo.

Requires: fastapi, redis, litellm, uvicorn.
Redis must be available at REDIS_URL (default: redis://localhost:6379/0).
"""

from __future__ import annotations

import os
from typing import Any

from fastapi import Depends, FastAPI
from litellm import acompletion, aembedding
import litellm
from redis.asyncio import Redis


app = FastAPI(title="Context cache demo")
redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
litellm.cache = litellm.Cache()


async def redis_client() -> Redis:
    return redis


def trim_context(messages: list[dict[str, str]], max_chars: int) -> list[dict[str, str]]:
    system = [message for message in messages if message["role"] == "system"][:1]
    rest = [message for message in messages if message["role"] != "system"]
    kept: list[dict[str, str]] = []
    used = sum(len(message["content"]) for message in system)
    for message in reversed(rest):
        if used + len(message["content"]) > max_chars:
            break
        kept.append(message)
        used += len(message["content"])
    return system + list(reversed(kept))


def compress_context(messages: list[dict[str, str]], keep_last: int = 2) -> list[dict[str, str]]:
    if len(messages) <= keep_last:
        return messages
    summary = " | ".join(message["content"] for message in messages[:-keep_last])
    return [{"role": "summary", "content": summary}] + messages[-keep_last:]


@app.post("/context")
async def context(
    messages: list[dict[str, str]],
    detail: bool = False,
    client: Redis = Depends(redis_client),
) -> dict[str, Any]:
    key = "context:" + str(hash(str(messages)))
    cached = await client.get(key)
    if cached is not None:
        return {"source": "redis", "messages": cached}
    result = messages if detail else compress_context(trim_context(messages, 120))
    await client.set(key, str(result), ex=300)
    return {"source": "computed", "messages": result}


async def call_llm(messages: list[dict[str, str]]) -> Any:
    return await acompletion(
        model=os.environ["LITELLM_MODEL"], messages=messages, caching=True
    )


async def call_embedding(text: str) -> Any:
    return await aembedding(
        model=os.environ["LITELLM_EMBEDDING_MODEL"], input=[text], caching=True
    )
