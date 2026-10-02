"""Dependency-based FastAPI + Redis + LiteLLM cache demo.

Requires: fastapi, redis, litellm, uvicorn.
Redis must be available at REDIS_URL (default: redis://localhost:6379/0).
"""

from __future__ import annotations  # 让当前文件使用“延迟类型注解”

import os
from typing import Any

from fastapi import Depends, FastAPI
from litellm import acompletion, aembedding
import litellm
from redis.asyncio import Redis

# Redis 客户端在应用进程内复用连接池；不要在每个请求中重新创建客户端。
app = FastAPI(title="Context cache demo")
redis = Redis.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True
)
# LiteLLM 开启缓存后，会根据完整请求生成 key；相同请求可直接复用响应。
litellm.cache = litellm.Cache()


async def redis_client() -> Redis:
    """FastAPI 依赖：向路由注入共享的异步 Redis 客户端。"""
    return redis


def trim_context(
    messages: list[dict[str, str]], max_chars: int
) -> list[dict[str, str]]:
    """按字符预算裁剪上下文，保留系统消息和尽可能新的消息。

    Args:
        messages: 按对话顺序排列的消息列表，每项包含 role 和 content。
        max_chars: 允许保留的 content 总字符数上限。

    Returns:
        裁剪后的消息列表。
    """
    system = [message for message in messages if message["role"] == "system"][
        :1
    ]  # 最多保留第一条
    rest = [message for message in messages if message["role"] != "system"]
    kept: list[dict[str, str]] = []
    used = sum(
        len(message["content"]) for message in system
    )  # 计算 system 中所有系统消息的内容总字符数
    for message in reversed(rest):  # 从后往前遍历 rest，但不会立刻创建一个新的列表
        if used + len(message["content"]) > max_chars:
            break
        kept.append(message)
        used += len(message["content"])
    return system + list(reversed(kept))


def compress_context(
    messages: list[dict[str, str]], keep_last: int = 2
) -> list[dict[str, str]]:
    """把较早消息合并成摘要，并保留最近的若干条消息。

    Args:
        messages: 原始上下文消息。
        keep_last: 原样保留的最新消息数量。

    Returns:
        包含摘要消息和最近消息的新上下文。
    """
    if len(messages) <= keep_last:
        return messages
    summary = " | ".join(message["content"] for message in messages[:-keep_last])
    return [{"role": "summary", "content": summary}] + messages[-keep_last:]


"""
messages[:-2]  # 除最后两条外的所有消息
messages[-2:]  # 最后两条消息
"""


@app.post("/context")
async def context(
    messages: list[dict[str, str]],
    detail: bool = False,
    client: Redis = Depends(redis_client),
) -> dict[str, Any]:
    """返回处理后的上下文，并把结果缓存到 Redis。

    Args:
        messages: 请求携带的完整上下文。
        detail: 为 True 时跳过裁剪和压缩，返回完整上下文；默认为 False。
        client: 由 FastAPI 注入的 Redis 客户端。

    Returns:
        包含数据来源（computed 或 redis）和上下文消息的 JSON 对象。
    """
    # Demo 使用请求内容生成 key；生产环境应使用稳定的 hash，而不是 Python 的 hash()。
    key = "context:" + str(hash(str(messages)))
    cached = await client.get(key)
    if cached is not None:
        # HIT：跳过上下文处理，直接返回 Redis 中的结果。
        return {"source": "redis", "messages": cached}
    # MISS：先裁剪/压缩，再把结果写入 Redis，TTL 为 5 分钟。Time To Live
    result = messages if detail else compress_context(trim_context(messages, 120))
    await client.set(key, str(result), ex=300)
    return {"source": "computed", "messages": result}


async def call_llm(messages: list[dict[str, str]]) -> Any:
    """调用 LiteLLM，并开启 exact-match 响应缓存。

    Args:
        messages: 传给模型的上下文消息。

    Returns:
        LiteLLM 的异步响应对象。
    """
    return await acompletion(
        model=os.environ["LITELLM_MODEL"], messages=messages, caching=True
    )


async def call_embedding(text: str) -> Any:
    """生成文本向量，并开启 Embedding 响应缓存。

    Args:
        text: 需要转换为向量的文本。

    Returns:
        LiteLLM 的异步 Embedding 响应对象。
    """
    return await aembedding(
        model=os.environ["LITELLM_EMBEDDING_MODEL"], input=[text], caching=True
    )
