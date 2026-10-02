# Day 22：最小 Agent Loop 与 Harness

本练习参考 [OpenAI Agents SDK 的运行循环](https://openai.github.io/openai-agents-python/running_agents/) 和 [Harness Engineering](https://openai.com/index/harness-engineering/)。

## 学习目标

实现一个不依赖 Agent 框架的最小运行时：

1. 调用模型。
2. 判断模型是否请求工具。
3. 调度工具并把结果追加到消息历史。
4. 再次调用模型，直到模型返回最终文本。
5. 通过轮数、时间和成本预算停止运行。


展示 Agent 的最小闭环

- Model：model.complete(messages) 生成下一步决策
- Harness：run_agent() 决定何时调用 Model、何时执行 Tool、何时停止
- Tool：tool(**call.arguments) 执行动作
- Messages：messages 列表保存上下文
- Budget：budget 控制超时、轮数和成本

所以，Harness 不是某个单独的类，而是 run_agent() 这段编排和控制逻辑。


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

Agents SDK 是一个 Python-first、轻量的 Agent 运行时，核心原语包括：

- `Agent`：带有 instructions 和 tools 的模型。
- `Runner`：负责运行 Agent，管理多轮调用和工具执行。
- `Handoffs` / agents as tools：让 Agent 把任务委托给其他 Agent。
- `Guardrails`：在输入、输出或运行过程中做校验和安全检查。
- `Sessions`：跨轮次保存工作上下文。
- `Tracing`：记录、可视化和调试 Agent 工作流。

SDK 默认使用 Responses API，但在模型调用之上增加了工具执行、循环、handoff、guardrail、session 和 tracing 等运行时能力。

可以这样选择：

- 直接使用 Responses API：希望自己管理循环、工具分发和状态，或者流程很短。
- 使用 Agents SDK：希望运行时管理多轮任务、工具、guardrails、handoffs、sessions，或需要工作区和可恢复执行。

本练习刻意只实现 SDK 中最小的核心机制，用来理解 Harness 如何管理模型、工具、消息历史和停止条件；生产系统应优先复用 SDK 已提供的能力。

## Harness Engineering 的启发

Harness 不是让模型“更努力”，而是为 Agent 建立一个可理解、可执行、可验证的工作环境。参考文章中的关键原则是：

1. **人负责设定目标，Agent 负责执行**：工程师的重点从手写每一行代码，转向设计环境、明确意图和建立反馈循环。
2. **让应用对 Agent 可理解**：代码、文档、计划、日志、指标、trace 和可运行的 UI 都应能被 Agent 直接访问和验证。
3. **仓库是知识的事实来源**：`AGENTS.md` 应像目录一样简短，指向结构化的架构文档、设计文档、产品规格、执行计划和技术债记录，而不是堆积成一份百科全书。
4. **渐进式披露上下文**：先给 Agent 一张地图，再让它按任务需要查找细节，避免过大的上下文淹没真正的约束。
5. **把规则写成可执行约束**：重要的架构边界、依赖方向、数据边界、日志规范和质量要求，应通过 lint、结构化测试和 CI 强制，而不只写在文档里。
6. **反馈循环比一次性生成更重要**：运行、测试、审查、修复、再次验证构成闭环；错误暴露的是 Harness 缺少的能力或约束。
7. **吞吐量提高后要管理熵**：Agent 产出越快，越需要文档维护、架构检查、技术债跟踪和定期清理，防止代码库逐渐失去一致性。

映射到本练习：`Model` 是能力提供者，`run_agent` 是 Harness。它通过消息历史、工具注册表、预算和停止原因，把“模型能做什么”变成“模型能在边界内可靠完成什么”。

## 最小 Harness 的运行流程

```text
用户输入
   ↓
调用 Model.complete(messages)
   ↓
有工具调用？ ── 否 ──→ 返回最终文本
   │
  是
   ↓
查找工具 → 执行工具 → 将结果写回消息历史
   ↓
检查轮数 / 时间 / 成本预算
   ↓
继续调用模型
```

这个循环对应 Agents SDK 的基本运行思想，但省略了 sessions、handoffs、guardrails、tracing、流式输出和真实模型适配等生产能力，便于先掌握最小闭环。

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
