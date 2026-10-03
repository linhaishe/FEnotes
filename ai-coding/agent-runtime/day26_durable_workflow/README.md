# Day 26：Durable Workflow

参考：[LangGraph Durable Execution](https://langchain-ai.github.io/langgraph/concepts/durable_execution/)

## 为什么 Agent 需要 Durable Execution

普通 Agent 调用通常是一次性的：进程退出、网络断开或用户暂时离开后，运行状态就丢失。Durable Execution 把 Agent 工作流变成可持久化、可恢复的执行过程：即使中断，也能从已经保存的状态继续，而不是从头开始。

典型场景：

- 长时间运行的研究、审批、订单和客服工作流
- 用户需要几小时或几天后再回复的人工确认
- Worker 崩溃、部署重启或请求超时后的恢复
- 外部工具调用完成，但应用还没来得及返回结果的故障恢复

## 核心概念

### Checkpoint

LangGraph 在图执行过程中保存 checkpoint。checkpoint 包含当前线程的状态、下一步要执行的节点以及恢复所需的元数据。生产环境应使用持久化 checkpointer；Demo 使用 `InMemorySaver` 只为方便运行。

### Thread ID

每次调用都要传稳定的 `configurable.thread_id`。它是一次对话或业务流程的恢复键：相同 `thread_id` 才会读到同一条执行记录，换一个 ID 就是新的运行。

### 节点边界与重放

恢复通常从保存的节点边界继续。节点中已经完成的 Python 代码不等于外部世界已经幂等，因此节点应尽量小，并把网络请求、扣款、发邮件等副作用隔离成可安全重放的步骤。

### 中断与恢复

`interrupt()` 可以暂停图并保存状态，等待用户输入。恢复时使用相同的 `thread_id`，通过 `Command(resume=...)` 提供答案，工作流从暂停点继续。

### 副作用与确定性

节点在恢复或重放时可能再次运行。副作用操作应使用稳定的幂等键、外部状态查询或事务/补偿机制；不要依赖随机数、当前时间或不可重复的外部状态来决定恢复路径。需要非确定性结果时，将结果写入状态后复用。

### 持久化模式

持久化速度与可靠性存在取舍。异步写入适合减少执行等待；需要更强确认时可以使用同步写入；只关心流程结束结果时可以选择退出时写入。具体模式取决于允许丢失多少最近进度。

## 最小 Demo

运行：

```bash
python agent-runtime/day26_durable_workflow/demo.py
```

Demo 模拟一个退款 Agent：先生成退款申请，在人工审批处暂停；随后使用同一个 `thread_id` 恢复并完成退款。它验证了：

1. `interrupt()` 会暂停工作流并保存状态。
2. 使用不同的 `thread_id` 不会误恢复别人的流程。
3. 使用原来的 `thread_id` 和 `Command(resume=...)` 可以继续执行。
4. `InMemorySaver` 只适合演示；多进程和生产环境应换成持久化 checkpointer。

## 故障恢复 Demo

运行：

```bash
python agent-runtime/day26_durable_workflow/demo_fault_recovery.py
```

[demo_fault_recovery.py](./demo_fault_recovery.py) 专门验证“状态机 + 任务队列 + 持久化状态 + 故障恢复”：

- LangGraph `StateGraph` 表达 `queued → running → completed` 状态机。
- `asyncio.Queue(maxsize=2)` 作为有界任务队列，避免任务无限堆积。
- SQLite 保存 workflow checkpoint 和任务结果；重启后通过相同 `job_id` 恢复。
- 第一个任务产生副作用后模拟 Worker 崩溃，第二次运行重新读取状态。
- 已完成但尚未推进 checkpoint 的任务通过稳定 task ID 幂等返回，不重复执行副作用。
- 未完成任务继续执行，最终断言三个任务全部完成。

## Agent 中的设计清单

- 为每个会话、订单或任务生成稳定的 `thread_id`。
- 把长流程拆成有意义的节点，让 checkpoint 足够频繁且便于观察。
- 对外部副作用使用幂等键，恢复时先查询状态再决定是否执行。
- 给每个节点区分可重试错误、需要用户输入的错误和不可预期错误。
- 不把 prompt 模板、连接对象等不可持久化对象直接放进状态；状态保存原始、可序列化的数据。
- 选择适合业务风险的 checkpointer 和持久化模式。
