# Day 24：Run State、Checkpoint/Resume 与幂等工具

参考：[OpenAI Agents SDK - Running Agents](https://openai.github.io/openai-agents-python/running_agents/)

> 幂等工具: 就是同一个操作执行一次或执行多次，最终效果都一样，不会重复产生副作用。

## 参考资料总结

一次 Agent Run 可以包含多个模型调用、工具调用、handoff，最后才产生一个逻辑回合的结果。应用通常只把最终输出展示给用户，但要想支持恢复，就需要保存运行过程中的状态。

资料中介绍的状态管理方式主要有四类：

| 方式 | 状态保存位置 | 适用场景 |
| --- | --- | --- |
| `result.to_input_list()` | 应用内存或自有存储 | 小型对话、手动管理完整历史 |
| `session` | 应用存储，由 SDK 读写 | 持久化对话、可恢复运行 |
| `conversation_id` | OpenAI Conversations API | 跨 worker 或服务共享对话 |
| `previous_response_id` | OpenAI Responses API | 轻量的服务端连续对话 |

一个项目通常应选择一种状态策略。不要同时把本地完整历史和服务端 conversation state 当作同一份历史传入，否则可能重复上下文。

### Run State

Run State 是一次运行的可恢复快照，至少应包含：

- `run_id`：标识一次运行；
- 当前步骤或待执行动作；
- 输入、消息和业务中间结果；
- 已完成的工具调用及其结果；
- 恢复后继续运行所需的元数据。

SDK 的 `RunResult` 可以转换为下一轮输入；应用如果需要跨进程恢复，则还需要把自己的业务状态和工具结果持久化。

### Checkpoint/Resume

Checkpoint 是在安全边界保存的运行快照。恢复时读取最近一次 checkpoint，从保存的步骤继续，而不是重新从用户输入开始执行。实际系统通常还要考虑：

- checkpoint 写入要尽量原子，避免进程中断留下半个文件；
- 工具执行前后要明确状态边界；
- 恢复可能重新收到同一个工具调用，因此不能假设每个工具只会被调用一次。

### 有副作用工具的幂等保护

发送邮件、扣款、创建订单等工具会改变外部系统。Run 恢复时，模型或 Runner 可能再次提交同一个工具调用。工具应使用稳定的幂等键（本 Demo 使用 `run_id + tool_call_id`）：

1. 第一次调用前检查幂等记录；
2. 没有记录时执行副作用；
3. 将工具结果和幂等键持久化；
4. 重复调用时直接返回原结果，不再次执行副作用。

幂等记录和真实副作用最好由同一个支持幂等语义的外部系统保证。这里用 JSON 文件只是为了让机制可以零依赖运行。

## Demo

`demo.py` 使用 Python 标准库实现三个部分：

- `RunState`：保存当前步骤、输入和工具结果；
- `CheckpointStore`：用临时文件替换实现简单的原子 checkpoint；
- `IdempotentOrderTool`：用 `run_id:create_order` 防止重复创建订单。

运行：

```bash
python day24_state_resume/demo.py
```

运行过程：

```text
保存初始 Run State
  ↓
创建订单（副作用成功）
  ↓
模拟进程中断，还没把运行步骤推进到 complete
  ↓
读取 checkpoint 并 resume
  ↓
再次遇到同一个 tool_call_id
  ↓
命中幂等记录，返回 order-1，不重复创建
```

Demo 运行时会生成 `day24_state_resume/.demo-data/`，其中保存 checkpoint 和幂等账本；再次运行前会清理这两个 Demo 文件。

## LangChain + Gemini Demo

`demo_langchain_gemini.py` 使用 LangGraph（LangChain 生态的状态图与 checkpoint 组件）实现同一个流程：

- `State`：Run State，保存 `run_id`、商品和模型计划；
- `MemorySaver`：按 `thread_id` 保存图执行 checkpoint；
- `ChatGoogleGenerativeAI`：接入 Gemini，执行 Agent 的计划节点；
- `IdempotentOrderTool`：用 `run_id:create_order` 防止恢复时重复创建订单。

安装并运行：

```bash
pip install -U langchain langchain-google-genai langgraph
GEMINI_API_KEY=你的_key python day24_state_resume/demo_langchain_gemini.py
```

Demo 会故意在订单创建成功后抛出一次异常，然后用相同的 `thread_id` resume。`create_order` 节点会重跑，但幂等账本会返回已有的 `order-1`，不会再次创建订单。
