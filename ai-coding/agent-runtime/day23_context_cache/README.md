# Day 23：Context Cache

## 目标

把昂贵或重复的上下文/模型请求结果暂存起来，减少重复计算和 LLM 调用：

```text
请求 → 生成稳定的 cache key → Redis 查询
                         ├─ 命中：直接返回
                         └─ 未命中：执行请求 → 写入 Redis（TTL）→ 返回
```

```
用户提问
  ↓
应用收到 messages
  ↓
POST /context
  ↓
redis_client() 注入 Redis
  ↓
根据 messages 生成缓存 key
  ↓
Redis 查询
  ├─ 命中 → 直接返回缓存上下文
  └─ 未命中
       ↓
     trim_context()
       ↓
     compress_context()
       ↓
     写入 Redis，TTL 300 秒
       ↓
     返回处理后的 messages
```

这里的缓存是“响应缓存”，不是模型本身的 prompt caching。它缓存的是应用或 LiteLLM 已经得到的结果。

## 参考资料

- [Redis with FastAPI](https://redis.io/docs/latest/integrate/fastapi/)
- [FastAPI and Redis Tutorial](https://redis.io/tutorials/develop/python/fastapi/)
- [fastapi-redis-sdk](https://github.com/redis/fastapi-redis-sdk)
- [Building a REST API with FastAPI and Redis Caching](https://medium.com/@suganthi2496/building-a-rest-api-with-fastapi-and-redis-caching-278c4dc07d70)
- [LiteLLM Caching](https://docs.litellm.ai/docs/caching)

## 一、FastAPI + Redis 的缓存模式

### Redis 适合做什么

- Redis 是独立的内存型 key-value 服务，读写延迟低。
- 适合作为多个 FastAPI worker 共享的缓存；进程内 dict 只能被单个 worker 使用。
- 缓存通常设置 TTL，避免旧数据永久存在。
- Redis 既可以本地通过 Docker 运行，也可以使用托管服务。

### FastAPI 中的基本职责

FastAPI 负责 HTTP 层，Redis 客户端负责缓存层。应用通常需要：

1. 创建 Redis 连接或连接池。
2. 在应用启动时建立连接，在关闭时释放连接。
3. 请求进入后先查缓存。
4. 未命中时执行原本的业务逻辑。
5. 将可序列化的结果写入 Redis，并设置 TTL。

Redis 官方的推荐落点是把连接管理放进 FastAPI 的 `lifespan`：应用启动时建立连接池，关闭时释放连接；请求处理函数通过依赖注入拿到异步 Redis 客户端。这样连接池是应用级共享资源，不需要每个请求重复创建连接。

如果使用 Redis 官方的 `fastapi-redis-sdk`，安装名和导入名不同：

```bash
pip install fastapi-redis-sdk
```

```python
from fastapi import FastAPI
from redis_fastapi import AsyncRedisDep, FastAPIRedis

app = FastAPI()
FastAPIRedis(app).lifespan()

@app.get("/items")
async def get_items(redis: AsyncRedisDep):
    return {"items": await redis.get("items")}
```

连接配置可以使用 `REDIS_URL`，也可以拆成 `REDIS_HOST`、`REDIS_PORT`、`REDIS_PASSWORD` 等环境变量。实际项目中应通过环境变量或密钥管理系统提供凭据，不要把密码写入代码。

伪代码：

```python
async def endpoint(key: str):
    cached = await redis.get(key)
    if cached is not None:
        return decode(cached)

    result = await expensive_operation(key)
    await redis.set(key, encode(result), ex=60)
    return result
```

### Key 设计

缓存 key 必须能唯一表示会影响结果的输入。建议包含：

- 业务前缀，例如 `answer:` 或 `user-profile:`
- 资源标识或请求参数
- 必要的版本号，例如 `v1`

不要把未经处理的长文本、秘密信息或不稳定的对象字符串直接当作 key。结构化参数应先规范化，确保参数顺序不会导致同一请求产生不同 key。

### 失效与一致性

TTL 只能处理“过期”，不能自动理解业务数据何时改变。数据更新后如果旧缓存不可接受，应主动删除相关 key，或者提高 key 版本：

```text
更新源数据 → 删除对应缓存 → 下次请求重新计算
```

缓存应被视为可丢失的派生数据，不能把唯一的业务数据只放在 Redis 中。

Redis SDK 将常用缓存操作拆成三类：

- `cache()`：读取时缓存响应。
- `cache_evict()`：写入或删除后清理相关缓存。
- `cache_put()`：写入后同时刷新缓存。

这些操作可以通过 FastAPI 的 `Depends` 挂到路由上，并共享同一个 key builder 和 eviction group，避免 GET、PUT、DELETE 使用不同 key 导致失效失败。需要条件缓存、动态 TTL 或级联失效时，再直接使用 `CacheBackend` 的 `get`、`set`、`delete` 等方法。

### HTTP 层缓存

应用层 Redis 缓存之外，还可以利用 HTTP 缓存协议：

- `Cache-Control` 告诉客户端或代理缓存多久。
- `ETag` 标识响应版本。
- 客户端带 `If-None-Match` 重新请求时，如果内容没变，服务端返回 `304 Not Modified`，不重复传输响应体。

因此一次请求可能同时涉及两层缓存：Redis 避免服务端重复计算，HTTP 缓存避免客户端和网络重复传输。

### 观察命中情况

缓存接入后，不能只假设它会生效。至少应能区分 MISS 和 HIT，并记录延迟、TTL、缓存大小以及失效事件。官方 SDK 会通过 `X-Redis-Cache: HIT/MISS` 响应头帮助验证缓存是否生效；需要更完整指标时可以启用 OpenTelemetry。

- MISS：缓存里没有数据，需要执行原本的计算或调用 LLM，然后写入缓存。
- HIT：缓存里已有数据，直接返回缓存结果，没有重新计算或调用 LLM。

HIT 全称是 Cache Hit，中文叫“缓存命中”。
- Cache Hit：缓存命中，直接拿到缓存数据
- Cache Miss：缓存未命中，需要重新计算或请求 LLM

## 二、LiteLLM Caching

### 核心机制

LiteLLM 可以缓存 `completion()`、`embedding()` 等调用的结果。相同请求再次到达时，直接返回缓存结果，从而降低延迟和模型成本。

SDK 模式的最小示例：

```python
import litellm
from litellm import completion
from litellm.caching.caching import Cache

litellm.cache = Cache()

first = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a joke."}],
    caching=True,
)
second = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a joke."}],
    caching=True,
)
```

LiteLLM 的 exact-match cache 会根据完整请求计算 key；模型、消息内容或其他影响请求的字段发生变化，都可能导致 miss。因此，agent 的每一轮上下文变化通常都会产生新的缓存项。

### 缓存后端

常见后端包括：

| 后端 | 适用场景 |
| --- | --- |
| `local` / in-memory | 本地开发、单进程验证 |
| `disk` | 本机开发，需要跨进程保留一部分缓存 |
| `redis` | 多 worker、多副本或生产环境 |
| `redis-semantic`、`qdrant-semantic` | 按语义相似度命中，而不是严格相同请求 |
| `s3`、`gcs` | 对象存储型缓存 |

生产环境优先使用 Redis：进程内缓存不会在 worker 或副本之间共享。LiteLLM 文档也将 Redis 作为多 worker 场景的默认选择。

### Proxy 配置思路

LiteLLM Proxy 可以在配置中开启缓存，并通过环境变量提供 Redis 连接信息：

```yaml
litellm_settings:
  cache: true
  cache_params:
    type: redis
```

```env
REDIS_URL=redis://username:password@hostname:6379/0
```

也可以限制只缓存指定的调用类型，或者在请求级别显式开启缓存。缓存命中时，LiteLLM 会返回 `x-litellm-cache-key` 响应头，可用于定位或删除缓存项。

### Exact-match 与 semantic cache 的取舍

- Exact-match：结果可预测，只在完整请求相同或 key 相同的时候命中；适合 agent、多轮对话和需要严格一致的请求。
- Semantic cache：相似问题也可能命中；适合单轮、重复性高的问题，但不适合上下文细微变化就会改变答案的 agent 流程。

## 三、和 Day 22 Harness 的关系

Day 22 的调用链可以加入缓存层：

```text
Harness.run_agent
        ↓
      Model
        ↓
   LiteLLM / LLM API
        ↓
Redis response cache
```

推荐先缓存 Model 的最终响应，而不是在 Harness 中复制一套 Redis 逻辑：

- Harness 继续只负责流程、工具调用和预算控制。
- Model 或 LiteLLM 层负责响应缓存。
- Messages 仍然是 cache key 的重要输入。
- Tool 调用结果一般不应盲目缓存，除非工具是幂等的且缓存不会造成业务错误。

## 四、实践清单

- 先确认重复请求确实存在，再引入缓存。
- 为 key 设计版本和命名空间。
- 设置 TTL，并明确更新时的失效策略。
- 不缓存密码、token、个人隐私或不可公开复用的响应。
- 生产环境使用共享 Redis，不依赖单 worker 的内存缓存。
- 记录 hit/miss、延迟、缓存大小和失效情况。
- 对 agent 请求默认采用 exact-match；semantic cache 需要单独验证错误命中风险。
- 缓存不可用时，应用应能回退到正常请求路径，不能丢失业务数据。

## 一句话总结

FastAPI 负责把 Redis 接入应用的请求生命周期；LiteLLM 负责把 LLM 响应缓存封装起来；对 Day 22 来说，最小改动是让 `Model` 层缓存，保持 Harness 的流程控制职责不变。

## 五、Demo

### 1. 无依赖版本

`demo_stdlib.py` 只使用 Python 标准库，用内存字典模拟 Redis，包含：

- `trim_context()`：按字符预算保留系统消息和最近消息。
- `compress_context()`：将较早消息合并成摘要。
- `progressive_load()`：默认返回摘要，需要详情时返回完整上下文。
- `cached_llm()` / `cached_embedding()`：使用稳定 hash key 做缓存。

运行：

```bash
python day23_context_cache/demo_stdlib.py
```

### 2. 依赖版本

`demo_dependencies.py` 展示真实依赖接入：

- FastAPI + `redis.asyncio`：Redis 连接和依赖注入。
- Redis TTL：缓存上下文接口结果。
- LiteLLM：通过 `caching=True` 缓存 LLM 和 Embedding 请求。
- `trim_context()` / `compress_context()`：请求进入模型前处理上下文。

安装依赖：

```bash
pip install fastapi redis litellm uvicorn
```

启动 Redis 和 API：

```bash
export REDIS_URL=redis://localhost:6379/0
export LITELLM_MODEL=openai/gpt-4o-mini
export LITELLM_EMBEDDING_MODEL=openai/text-embedding-3-small
uvicorn day23_context_cache.demo_dependencies:app --reload
```

这个依赖版是接入示例，不包含完整的鉴权、生产级 key 规范化、并发 single-flight 或缓存失效策略；需要上线时再补。

# QA

## `from __future__ import annotations`

```python
from __future__ import annotations
```

表示：让当前文件使用“延迟类型注解”。

例如：

```python
def trim_context(
    messages: list[dict[str, str]],
) -> list[dict[str, str]]:
    ...
```

这些类型不会在函数定义时立即求值，而是延迟处理。

主要作用：

- 支持较新的类型写法，例如 `list[str]`
- 支持函数返回自身类型、前向引用等写法
- 避免类型注解中某些名称尚未定义的问题
- 不影响程序的实际运行逻辑

它只影响类型注解，不是导入某个库，也不会执行缓存或 FastAPI 相关功能。

“延迟”指的是：函数定义时不立刻计算类型表达式，而是先保存成字符串。

没有它：

```python
class User:
    pass

def get_user() -> User:
    ...
```

Python 定义 `get_user` 时就要找到 `User`。

有它：

```python
from __future__ import annotations

def get_user() -> User:
    ...
```

定义函数时，`User` 可以暂时还不存在；类型注解会先以类似字符串的形式保存，之后类型检查器或 `typing.get_type_hints()` 需要时再解析。

可以观察：

```python
from __future__ import annotations

def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)
```

结果类似：

```python
{'a': 'int', 'b': 'int', 'return': 'int'}
```

所以它延迟的是“类型注解的解析”，不是函数执行，也不是把整个程序异步化。
