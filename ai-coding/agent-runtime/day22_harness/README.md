# Day 22：最小 Agent Loop 与 Harness

本练习参考 [OpenAI Agents SDK 的运行循环](https://openai.github.io/openai-agents-python/running_agents/) 和 [Harness Engineering](https://openai.com/index/harness-engineering/)。

## 学习目标

实现一个不依赖 Agent 框架的最小运行时：

1. 调用模型。
2. 判断模型是否请求工具。
3. 调度工具并把结果追加到消息历史。
4. 再次调用模型，直到模型返回最终文本。
5. 通过轮数、时间和成本预算停止运行。
   
“不依赖 Agent 框架”意思是：这个最小运行时不绑定 LangChain、AutoGen、CrewAI 之类的现成 Agent 框架。
它只依赖基础能力，例如：
- 调用模型 API
- 管理消息和上下文
- 执行工具/函数
- 维护简单状态
- 实现基本循环：思考 → 调用工具 → 继续 → 返回结果
也就是说，Agent 的核心机制自己实现，框架只是可选适配层。
区别可以理解为：
- Agent 框架：提供完整的 Agent 抽象、工具系统、记忆、编排、插件等。
- 最小运行时：只提供让一个 Agent 跑起来所必需的底层循环和接口。
所以“不依赖 agent”通常不是说完全没有 Agent，而是说：
不依赖某个现成的 Agent 框架；Agent 能力由这个运行时自己完成。

## 目录

```text
day22/
├── agent_loop.py  # Agent Loop、预算、工具注册与 ScriptedModel
└── README.md
```

## 运行

```bash
python agent-runtime/day22/agent_loop.py
```

预期输出：

```text
结果是 5
```

## 核心设计

`Model` 只负责产生 `ModelResponse`，不负责执行工具；`run_agent` 是 Harness，负责循环、消息历史、工具调度和停止条件。工具使用普通 Python 函数注册：

```python
result = run_agent(
    model=model,
    user_input="计算 2 + 3",
    tools={"add": lambda a, b: a + b},
    budget=Budget(max_turns=4, timeout_seconds=10, max_cost=0.05),
)
```

## 停止条件

- `completed`：模型返回文本且没有工具调用。
- `max_turns`：达到最大模型调用次数。
- `timeout`：超过运行时间预算。
- `cost_budget`：累计模型成本超过预算。

成本不是由 Harness 猜测，而是由模型适配器在每次响应中提供 `ModelResponse.cost`。真实模型接入时，只需实现 `Model.complete()`，不需要修改循环。

## 与 Agents SDK 的边界

Agents SDK 已经提供 Runner、工具调用、`max_turns`、sessions、guardrails 和 tracing 等运行时能力。本练习刻意只保留最小机制，用来理解 Harness 如何管理模型、工具和运行状态；生产系统不应重复实现 SDK 已经覆盖的能力。

## 下一步

第 23 天再加入上下文裁剪和缓存；第 24 天再加入 checkpoint/resume。当前版本不提前引入 Redis、异步队列或持久化，避免把学习重点分散。


# QA

## ToolCall("add", {"a": 2, "b": 3}) 这个会生成实例，使用ToolCall生成实例在这里有什么好处

`ToolCall("add", {"a": 2, "b": 3})` 会创建一个 `ToolCall` 实例。它的好处取决于 `ToolCall` 的定义，通常包括：

- **语义更清晰**：明确表示“这是一次工具调用”，而不是普通元组。
- **可用属性访问**：

  ```python
  call.name
  call.arguments
  ```

- **集中校验**：构造时可以检查工具名和参数是否合法。
- **统一行为**：可以添加序列化、日志、比较、执行等方法。
- **类型检查更可靠**：代码可以判断：

  ```python
  isinstance(call, ToolCall)
  ```

普通元组：

```python
("add", {"a": 2, "b": 3})
```

只是约定俗成的数据结构，容易写错，也不表达明确语义。

如果这个数据只在很小范围内临时传递，元组就够了；如果要跨模块传递、校验或处理，使用 `ToolCall` 更合适。

## result = run_agent(model, "计算 2 + 3", {"add": lambda a, b: a + b}) 这里的tools参数为啥长这样

`tools` 参数通常是一个字典：

```python
tools = {
    "工具名": 可调用对象
}
```

所以：

```python
{"add": lambda a, b: a + b}
```

表示注册一个名为 `"add"` 的工具，实际执行时调用这个函数：

```python
tools["add"](2, 3)  # 5
```

完整写法：

```python
result = run_agent(
    model,
    "计算 2 + 3",
    {"add": lambda a, b: a + b},
)
```

Agent 可能会生成工具调用：

```python
ToolCall("add", {"a": 2, "b": 3})
```

运行器再执行：

```python
tools["add"](**{"a": 2, "b": 3})
```

也就是：

```python
lambda a, b: a + b
```

你写的：

```python
lambda *a*, *b*: a + b
```

如果星号是代码本身，这是无效语法。若想接收任意位置参数，应写：

```python
lambda *args: sum(args)
```

但这里最简单、最合适的是 `lambda a, b: a + b`。