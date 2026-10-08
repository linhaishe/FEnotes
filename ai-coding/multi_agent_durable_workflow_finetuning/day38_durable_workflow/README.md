# Day 38：Durable Workflow

本日目标：在一个模拟退款任务上加入任务队列、持久化状态、人工审批节点和 Checkpoint，演练暂停、进程重启与失败恢复。本目录包含学习大纲、可运行 Demo 与自动化测试。

## 一、先弄清边界

- **工作流状态**：订单号、拟执行动作、审批决定、执行结果等业务数据，以及当前走到哪个节点。
- **Checkpoint / Checkpointer**：按 `thread_id` 保存图的状态快照，使同一条工作流可在中断或失败后继续。内存 Checkpointer 无法跨进程重启；本地练习可选持久化的 SQLite Checkpointer。
- **任务队列**：保存待执行任务，交给 Worker 消费；它解决调度与投递问题，不能代替 Checkpoint。反过来，Checkpoint 也不会自动替应用提供队列。
- **审批节点**：在高风险操作前调用 `interrupt()` 暂停；审批系统提交批准或拒绝后，用相同 `thread_id` 与 `Command(resume=...)` 恢复。恢复时被中断的节点会从头执行，因此中断前不要放不可重复的外部副作用。
- **幂等性**：Worker 崩溃或任务重复投递可能导致节点重跑。真实写操作必须用业务幂等键/执行记录防重，不能把“有 Checkpoint”等同于“只执行一次”。

阅读顺序：[Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) → [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers)（重点查状态与快照）→ [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)。实现时以官方文档的当前 API 为准。

## 二、项目：可审批、可恢复的模拟退款流程

沿用假订单与退款规则，不连接真实支付系统。输入一个退款请求后，由 Worker 消费队列任务，工作流读取订单与规则、生成拟退款决定；需要退款时暂停等待人工审批；批准后调用 Mock 退款工具，拒绝则结束且不调用工具。

建议的主路径：`queued → running → pending_approval → approved/rejected → executing → completed/failed`。队列中的 `task_id` 标识投递，图的 `thread_id` 标识同一工作流，审批记录引用二者；不要用一次 Worker 运行 ID 代替稳定的 `thread_id`。

## 三、Task / Project 学习路线

### Task 1：画状态机并定义最小状态

- 列出节点、状态转移、终止状态和可重试错误；明确批准、拒绝、超时、工具失败各走哪条边。
- 定义最小状态字段：`task_id`、`thread_id`、`order_id`、`approval_status`、`result`、`error_type`。敏感信息不放进状态快照。
- **产出/验收**：状态图及状态字段表；不存在绕过审批直达退款工具的路径。

### Task 2：加入持久化 Checkpoint

- 用持久化 Checkpointer 编译 LangGraph；每个任务使用稳定的 `thread_id`，记录并读取当前状态/快照。
- 对比内存与持久化 Checkpointer：分别重启进程，观察哪些状态保留。
- **产出/验收**：重启后仍可用同一 `thread_id` 找到暂停的任务；换新 `thread_id` 不会意外接续旧任务。

### Task 3：加入审批节点

- 在 Mock 写操作前触发 `interrupt()`，展示待审批动作及必要的非敏感参数。
- 分别用批准、拒绝恢复；只在批准分支执行 Mock 退款。审批决定与操作结果分别持久化。
- **产出/验收**：暂停时写工具调用数为 0；拒绝后仍为 0；批准后执行一次。验证恢复时审批节点重跑不会产生副作用。

### Task 4：加入任务队列与 Worker

- 请求入口只负责创建任务并入队；Worker 按 `task_id` 取任务、用对应 `thread_id` 推进图，暂停或结束后更新任务状态。
- 明确入队、消费、确认、失败重投的时机；队列本身也要有持久化方案，不能只用进程内列表来验证跨重启恢复。
- **产出/验收**：重复投递同一 `task_id` 不会创建第二笔退款；队列和 Checkpoint 的记录可相互定位。

### Task 5：演练暂停与重启恢复

- 运行到 `pending_approval` 后停止 API/Worker 进程，重新启动并查询任务与待审批信息。
- 用原 `thread_id` 提交审批，观察图从已保存状态继续；检查重启前的只读步骤是否被无谓重做。
- **产出/验收**：重启前后的任务状态和审批请求一致，完成结果可查询，未批准前没有写入。

### Task 6：演练失败、重试与重复投递

- 注入一次工具超时、一次 Worker 崩溃和一次重复队列投递，记录每次恢复从哪个节点开始。
- 为 Mock 写操作加业务幂等键，区分“工具实际成功但确认前崩溃”和“工具未执行成功”；限制自动重试次数，耗尽后落入明确失败状态。
- **产出/验收**：可解释每次重试/恢复路径；最终不会重复写入，失败任务不会无限重试。

## 四、最小验证矩阵

| 场景 | 期望结果 |
| --- | --- |
| 正常请求并批准 | 一次 Mock 退款，任务完成 |
| 审批拒绝 | 任务结束，无 Mock 退款 |
| 等待审批时重启 | 待审批状态保留，可继续审批 |
| 工具超时 | 有界重试或明确失败，错误可查询 |
| Worker 崩溃 / 重复投递 | 可恢复，同一业务动作不重复执行 |

## 五、完成标准与产物

- 提供状态图、状态字段与队列/Checkpoint 的职责说明。
- 提供可运行 Demo、启动与重启步骤、自动化测试和一份恢复演练记录。
- 上述验证矩阵全部通过；能指出 `task_id`、`thread_id`、审批 ID 如何关联。
- 清楚说明本地 Demo 的边界：Mock 写操作不等于真实支付安全；生产环境还需要数据库事务/幂等约束、可靠队列、访问控制和审计。

## 六、运行 Demo

在本目录执行：

```bash
python -m pip install -r requirements.txt
python -m unittest test_demo.py -v
python demo.py --state-dir .day38-state submit order-1
python demo.py --state-dir .day38-state work
python demo.py --state-dir .day38-state status <task_id>
python demo.py --state-dir .day38-state approve <task_id>
python demo.py --state-dir .day38-state work
python demo.py --state-dir .day38-state status <task_id>
```

将 `approve` 换成 `reject` 可验证拒绝分支。每条命令都是独立进程，故自然演练了跨进程状态恢复。`status` 展示 `task_id`、`thread_id`、`approval_id`、图快照、任务状态和 Mock 退款写入数。提交只入队；`work` 消费一条投递；审批后必须再运行一次 `work` 才会继续执行。

故障演练（先完成 `submit → work → approve`；以下两组分别使用新任务）：

```bash
python demo.py --state-dir .day38-state work --fail before_write
python demo.py --state-dir .day38-state work

# 新建并批准另一任务后，再演练写入成功但确认丢失：
python demo.py --state-dir .day38-state work --fail after_write
python demo.py --state-dir .day38-state recover
python demo.py --state-dir .day38-state work
```

`before_write` 模拟写前超时，最多尝试 2 次；`after_write` 模拟写入成功、确认前 Worker 崩溃。后者需先运行 `recover` 重投，再运行 `work`，幂等表保证不会产生第二笔 Mock 退款。`work --fail worker_crash` 可在任意待消费任务上模拟取到任务后崩溃，同样通过 `recover` 恢复。状态数据位于 `.day38-state/queue.db` 与 `.day38-state/checkpoints.db`；前者保存队列/审批/幂等记录，后者保存 LangGraph Checkpoint。不要把演练数据或真实凭据提交到仓库。

本 Demo 是单 Worker、本地 SQLite、固定假订单和 Mock 工具的教学实现，没有接模型或真实支付接口。`recover` 仅适用于确认旧 Worker 已停止之后；多 Worker、并发审批及真实支付需要更严格的租约、事务和幂等设计。

自动化恢复演练记录：`python -m unittest test_demo.py -v` 覆盖批准/拒绝、内存与 SQLite Checkpointer 对比、跨连接重启、写前超时、写后崩溃、Worker 崩溃及重复投递；预期 7 个测试全部通过。若环境使用 Python 3.14，LangChain 依赖可能打印 Pydantic V1 兼容性警告，该警告不影响本 Demo 的测试结果。
