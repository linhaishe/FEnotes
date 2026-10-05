"""Minimal RAG retrieval cache demo backed by Redis.

参数说明：
    --redis-url：Redis 服务地址，默认是 redis://localhost:6379/0。
    --rounds：每个查询重复执行的轮数，默认是 20；轮数越多，缓存命中效果越明显。

Run:
    redis-server
    python rag_redis_demo.py --rounds 20
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import time
from dataclasses import dataclass

from redis.asyncio import Redis


@dataclass(frozen=True)
class Document:
    doc_id: str
    text: str


DOCUMENTS = (
    Document("redis", "Redis is an in-memory key-value store with low latency."),
    Document(
        "rag", "RAG retrieves relevant documents before the model writes an answer."
    ),
    Document("fastapi", "FastAPI supports async endpoints for non-blocking I/O."),
)


def cache_key(query: str) -> str:
    """根据查询内容生成稳定的 Redis 缓存键。

    Args:
        query: 用户输入的查询文本。

    Returns:
        包含版本号和 SHA-256 摘要的 Redis key。
    """
    digest = hashlib.sha256(query.strip().lower().encode()).hexdigest()
    return f"rag:retrieval:v1:{digest}"


async def retrieve(query: str) -> list[Document]:
    """模拟耗时的文档检索步骤。

    Args:
        query: 用于匹配文档内容的用户查询。

    Returns:
        按匹配程度排序后的最多两篇文档。
    """
    await asyncio.sleep(0.01)
    words = set(query.lower().split())
    ranked = sorted(
        DOCUMENTS,
        key=lambda document: sum(word in document.text.lower() for word in words),
        reverse=True,
    )
    return ranked[:2]


async def answer(query: str, documents: list[Document]) -> str:
    """根据查询和检索结果生成回答。

    Args:
        query: 用户输入的查询文本。
        documents: 提供给生成步骤的相关文档。

    Returns:
        包含查询和上下文的回答文本。
    """
    context = " ".join(document.text for document in documents)
    return f"Q: {query}\nA: {context}"


async def rag_query(
    query: str, redis: Redis | None = None, ttl_seconds: int = 300
) -> tuple[str, bool]:
    """执行一次 RAG 查询，并返回回答和缓存命中状态。

    Args:
        query: 用户输入的查询文本。
        redis: 可选的异步 Redis 客户端；为 None 时不读写缓存。
        ttl_seconds: 检索结果写入 Redis 后的过期时间，单位为秒。

    Returns:
        二元组 ``(answer, cache_hit)``，分别表示回答文本和是否命中缓存。
    """
    key = cache_key(query)
    if redis is not None:
        cached = await redis.get(key)
        if cached is not None:
            documents = [Document(**item) for item in json.loads(cached)]
            return await answer(query, documents), True

    documents = await retrieve(query)
    if redis is not None:
        await redis.set(
            key,
            json.dumps([document.__dict__ for document in documents]),
            ex=ttl_seconds,
        )
    return await answer(query, documents), False


async def benchmark(
    queries: list[str], rounds: int, redis: Redis | None
) -> dict[str, float]:
    """测量一组查询在指定缓存配置下的性能。

    Args:
        queries: 要重复执行的用户查询列表。
        rounds: 每个查询重复执行的轮数。
        redis: Redis 客户端；为 None 时作为无缓存基线运行。

    Returns:
        包含请求数、总耗时、平均延迟、命中数和命中率的指标字典。
    """
    started = time.perf_counter()
    hits = 0
    for _ in range(rounds):
        for query in queries:
            _, hit = await rag_query(query, redis)
            hits += int(hit)
    elapsed_ms = (time.perf_counter() - started) * 1000
    total = rounds * len(queries)
    return {
        "requests": total,
        "elapsed_ms": round(elapsed_ms, 3),
        "avg_latency_ms": round(elapsed_ms / total, 3),
        "cache_hits": hits,
        "hit_rate": round(hits / total, 3),
    }


async def main(redis_url: str, rounds: int) -> None:
    """连接 Redis 并运行无缓存与有缓存的对比实验。

    Args:
        redis_url: Redis 服务连接地址。
        rounds: 每个查询重复执行的轮数。
    """
    queries = ["What is Redis?", "How does RAG work?", "What supports async I/O?"]
    client = Redis.from_url(redis_url, decode_responses=True)
    await client.ping()
    try:
        for query in queries:
            await client.delete(cache_key(query))

        before = await benchmark(queries, rounds, redis=None)
        after = await benchmark(queries, rounds, redis=client)
        print(
            json.dumps({"without_cache": before, "with_redis_cache": after}, indent=2)
        )
    finally:
        await client.aclose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--redis-url",
        default="redis://localhost:6379/0",
        help="Redis 服务地址（默认：redis://localhost:6379/0）",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=20,
        help="每个查询的重复次数；默认：20",
    )
    args = parser.parse_args()
    if args.rounds < 1:
        parser.error("--rounds must be positive")
    asyncio.run(main(args.redis_url, args.rounds))
