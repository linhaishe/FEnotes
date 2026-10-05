# Day 29：LangSmith 链路追踪 Demo

这个 Demo 使用 LangChain Agent 调用一个天气工具，并通过 LangSmith 记录完整链路：

```text
Agent
  ├── 模型调用
  ├── get_weather 工具调用
  └── 最终回答
```

## 配置

```bash
export DEEPSEEK_API_KEY="你的 DeepSeek API key"
export LANGSMITH_API_KEY="你的 LangSmith API key"
export LANGSMITH_TRACING=true
export LANGSMITH_PROJECT=day29-langsmith-demo
```

可选配置：

```bash
export DEEPSEEK_MODEL=deepseek-chat
```

Demo 为 DeepSeek 请求设置 60 秒超时并关闭自动重试，避免模型请求异常时 Trace 长时间停留在 `Pending`。

## 运行

```bash
cd observability_deployment/day29_langsmith_tracing
python demo.py --task "查询上海天气并用一句话回答"
```

在 LangSmith 中打开 `day29-langsmith-demo` 项目，可以看到：

- Agent 总耗时
- 模型调用输入和输出
- 工具调用参数和结果
- 各个子调用的耗时
- Token 使用量（模型返回 usage metadata 时）
- 错误和重试信息

终端输出的是本地摘要；链路明细以 LangSmith 中的 Trace 为准。

## 验收

1. 终端输出 `success: True`；
2. `tool_call_count` 通常为 `1`；
3. LangSmith 项目中出现新的根 Trace；
4. 根 Trace 下能展开模型调用和 `get_weather` 工具调用。

如果终端成功但 LangSmith 没有新 Trace，检查 `LANGSMITH_TRACING=true`、`LANGSMITH_API_KEY` 和项目名称。

`LANGSMITH_TRACING` 不是代码里的函数，而是 LangChain 读取的环境变量开关。

在运行前设置：

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="你的 LangSmith API key"
export LANGSMITH_PROJECT="langsmith-demo"
```

然后代码正常调用 LangChain Agent：

```python
result = agent.invoke({
    "messages": [
        {"role": "user", "content": task}
    ]
})
```

LangChain 会自动把这次调用记录到 LangSmith，包括：

```text
Agent
 ├── 模型调用
 ├── get_weather 工具调用
 └── 最终结果
```

因此，`demo.py` 中真正触发追踪的是：

```python
agent.invoke(...)
```

而这段代码只是检查你是否开启了追踪：

```python
if os.getenv("LANGSMITH_TRACING", "").lower() not in {"true", "1", "yes"}:
    raise RuntimeError(...)
```

完整关系是：

```text
LANGSMITH_TRACING=true
        ↓
LangChain 自动启用 tracing
        ↓
agent.invoke(...)
        ↓
发送 Trace 到 LangSmith
```

注意：

- `LANGSMITH_TRACING=true`：开启追踪
- `LANGSMITH_API_KEY`：身份认证
- `LANGSMITH_PROJECT`：指定数据进入哪个项目
- `DEEPSEEK_API_KEY`：调用 DeepSeek 模型，不是 LangSmith 的密钥

也就是说，代码不需要手动调用 `langsmith.trace()`，因为 LangChain 已经集成了 LangSmith 的自动追踪机制。
