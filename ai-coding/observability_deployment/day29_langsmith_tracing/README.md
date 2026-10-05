# Day 29：LangSmith 链路追踪 Demo

这个 Demo 使用 LangChain Agent 调用一个天气工具，并通过 LangSmith 记录完整链路：

```text
Agent
  ├── 模型调用
  ├── get_weather 工具调用
  └── 最终回答
```

## LangSmith、OpenTelemetry 与 Langfuse 的区别

| 工具 | 定位 | 接入方式 | 收费模式 | 优势 | 适合场景 |
| --- | --- | --- | --- | --- | --- |
| [LangSmith](https://docs.smith.langchain.com/) | 面向 LangChain/LangGraph 的 Agent 可观测平台 | 环境变量、LangChain 集成、`@traceable` | 有免费开发者使用范围；付费方案和额度、保留期等以[官方定价](https://www.langchain.com/pricing)为准 | 自动展示 Agent、模型、工具和图节点的嵌套 Trace，并支持评估、反馈和监控 | 主要使用 LangChain/LangGraph，希望快速查看 Agent 链路 |
| [OpenTelemetry](https://opentelemetry.io/docs/languages/python/) | 厂商中立的 traces、metrics、logs 标准与 SDK | SDK、自动埋点、Exporter | OpenTelemetry 本身是开源标准和 SDK，通常免费；实际费用来自你选择的采集器、存储和观测后端 | 不绑定单一观测平台，能统一应用和基础设施指标 | 已有 Prometheus、Jaeger、Grafana 或云观测体系 |
| [Langfuse](https://langfuse.com/) | 面向 LLM/Agent 的开源或托管可观测平台 | Langfuse SDK、OpenTelemetry 或框架集成 | 可免费自托管 OSS；Cloud 有 Hobby 免费额度，付费按方案和用量计费，具体以[官方定价](https://langfuse.com/pricing)为准 | 支持自托管、Prompt 管理、Token/成本分析和评估 | 需要开源、自托管或希望控制 LLM 数据存储 |

三者不一定只能选一个：可以用 OpenTelemetry 采集通用基础设施指标，同时用 LangSmith 或 Langfuse 查看更丰富的 LLM/Agent 语义链路。

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
