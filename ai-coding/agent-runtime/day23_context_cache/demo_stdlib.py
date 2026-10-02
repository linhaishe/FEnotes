"""No-dependency context and LLM cache demo."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass


Message = dict[str, str]


@dataclass
class MemoryCache:
    values: dict[str, object]

    def __init__(self) -> None:
        self.values = {}
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> object | None:
        value = self.values.get(key)
        if value is None:
            self.misses += 1
        else:
            self.hits += 1
        return value

    def set(self, key: str, value: object) -> None:
        self.values[key] = value


def trim_context(messages: list[Message], max_chars: int) -> list[Message]:
    """Keep the system message and the newest messages within a character budget."""
    system = [message for message in messages if message["role"] == "system"][:1]
    rest = [message for message in messages if message["role"] != "system"]
    kept: list[Message] = []
    used = sum(len(message["content"]) for message in system)
    for message in reversed(rest):
        size = len(message["content"])
        if used + size > max_chars:
            break
        kept.append(message)
        used += size
    return system + list(reversed(kept))


def compress_context(messages: list[Message], keep_last: int = 2) -> list[Message]:
    """Replace old messages with a compact deterministic summary."""
    system = [message for message in messages if message["role"] == "system"][:1]
    rest = [message for message in messages if message["role"] != "system"]
    if len(rest) <= keep_last:
        return messages
    summary = " | ".join(f'{m["role"]}: {m["content"]}' for m in rest[:-keep_last])
    return system + [{"role": "summary", "content": summary}] + rest[-keep_last:]


def progressive_load(messages: list[Message], detail: bool = False) -> list[Message]:
    """Return a cheap summary first, then full detail when requested."""
    if detail:
        return messages
    return compress_context(messages, keep_last=1)


def stable_key(namespace: str, payload: object) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
    return f"{namespace}:{hashlib.sha256(encoded).hexdigest()}"


def cached_llm(messages: list[Message], cache: MemoryCache) -> str:
    key = stable_key("llm", messages)
    cached = cache.get(key)
    if cached is not None:
        return str(cached)
    result = f"LLM response for {len(messages)} messages"
    cache.set(key, result)
    return result


def cached_embedding(text: str, cache: MemoryCache) -> tuple[float, ...]:
    key = stable_key("embedding", text)
    cached = cache.get(key)
    if cached is not None:
        return tuple(cached)  # type: ignore[arg-type]
    result = tuple(round(byte / 255, 3) for byte in hashlib.sha256(text.encode()).digest()[:4])
    cache.set(key, result)
    return result


def demo() -> None:
    messages = [
        {"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "old question"},
        {"role": "assistant", "content": "old answer"},
        {"role": "user", "content": "latest question"},
    ]
    cache = MemoryCache()
    assert len(trim_context(messages, 35)) == 2
    assert compress_context(messages)[1]["role"] == "summary"
    assert progressive_load(messages)[-1]["content"] == "latest question"
    assert cached_llm(messages, cache) == cached_llm(messages, cache)
    assert cached_embedding("hello", cache) == cached_embedding("hello", cache)
    assert cache.hits == 2
    print("stdlib demo passed", {"hits": cache.hits, "misses": cache.misses})


if __name__ == "__main__":
    demo()
