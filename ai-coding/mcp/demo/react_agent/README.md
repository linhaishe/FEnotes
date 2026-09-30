# LangChain ReAct Agent Demo

这个 Demo 根据 LangChain 官方的 custom tool Agent 示例改写，使用仓库已有的 Gemini 依赖和一个本地天气工具。

## ReAct 是什么

ReAct（Reasoning + Acting）把模型推理和外部行动交替起来：

```text
用户问题
  → Thought：判断是否需要工具
  → Action：选择 get_weather 并生成 city 参数
  → Observation：得到工具返回的天气结果
  → Thought：判断是否还需要继续行动
  → Final Answer：生成最终回答
```

工具调用让模型能够访问训练数据之外的信息或能力。ReAct 的关键不是固定调用某个工具，而是让模型根据当前观察结果决定下一步。

## 代码对应关系

[`agent.py`](agent.py) 中的 `get_weather` 是工具，`create_agent` 创建 Agent：

```python
agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
    system_prompt="You are a helpful assistant. Use tools when they are useful.",
)
```

调用 `agent.invoke()` 后，LangChain 负责模型与工具之间的循环。新版本的 Agent API 不要求应用手动拼接 `Thought/Action/Observation` 文本，也不会默认把模型隐藏推理过程直接打印出来；可以观察最终消息以及工具调用消息来确认流程。

## 运行

```bash
export GEMINI_API_KEY="你的 Gemini API Key"
python demo/react_agent/agent.py
```

预期会看到模型基于 `get_weather("Beijing")` 的工具结果生成最终回答。这个工具返回的是固定字符串，目的是隔离 Agent 流程；真实天气查询可以替换为仓库的 `shared.weather.get_weather` 或 MCP 工具。

## 与仓库其他 Demo 的关系

```text
本 Demo：LangChain Agent → Python 工具
langchain_host.py：LangChain Agent → MCPAdapter → MCP Server → weather
langchain_multi_tool_host.py：LangChain Agent → MCPAdapter → 多个 MCP 工具
```

MCP 负责工具发现和跨进程通信；LangChain Agent 负责根据模型输出决定是否调用工具以及是否继续循环。

## 参考资料

- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [LangChain Agents 官方文档](https://python.langchain.com/v0.1/docs/modules/agents/)
