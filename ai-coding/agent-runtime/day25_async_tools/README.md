结论：仓库里确实提到了“异步、并发、超时、工具 I/O”，但“结构化并发、真正的取消传播、Backpressure 控制”目前没有完整落地。

| 主题 | 命中内容 | 判断 |
|---|---|---|
| 结构化并发 | LangGraph 的并行节点、`Send` 动态扇出、SuperStep、并行任务汇合 | 有并发编排，但没有明确使用 Python `TaskGroup` 或系统化介绍 structured concurrency |
| 超时 | `agent-runtime/day22_harness/agent_loop.py`：时间预算；LangGraph 节点级 `TimeoutPolicy`；模型、工具、整图三层超时 | 已有较完整说明 |
| 取消 | LangGraph 的 `interrupt()`、人工审批、暂停/恢复；超时导致异步节点失败 | 有“中断/暂停”，但没有 `asyncio.CancelledError`、取消传播、取消清理等真正 cancellation 教程 |
| Backpressure | LangGraph 流式输出使用同步/异步队列，由调用方迭代消费 | 只描述了队列和消费模型，没有队列容量、生产者限速、阻塞/丢弃策略等 Backpressure 控制 |
| I/O 工具 | `LangChain/05-Tools.md` 明确说明异步工具适用于 API、数据库、文件等 I/O 密集型任务 | 已有直接内容 |

重点位置：

- [LangChain/05-Tools.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangChain/05-Tools.md:2450>)：同步工具 vs 异步工具，明确覆盖 API、数据库、文件 I/O。
- [LangChain/07-agent-智能体.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangChain/07-agent-智能体.md:256>)：`ainvoke`、`astream`、`abatch` 等异步/批量调用。
- [LangGraph/02-LangGraph控制流与节点执行.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/02-LangGraph控制流与节点执行.md:400>)：静态并行节点。
- 同文件 [1392](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/02-LangGraph控制流与节点执行.md:1392>)、[1811](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/02-LangGraph控制流与节点执行.md:1811>)：`Send` 动态并发任务、Map-Reduce。
- 同文件 [3866](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/02-LangGraph控制流与节点执行.md:3866>)：异步节点超时、`run_timeout`、`idle_timeout`。
- [LangGraph/04-LangGraph中断与工具与部署.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/04-LangGraph中断与工具与部署.md:4375>)：模型、工具、整图三层超时；[4390](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/04-LangGraph中断与工具与部署.md:4390>)：敏感工具通过 `interrupt()` 审批。
- [LangGraph/05-LangGraph高级特性.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/LangGraph/05-LangGraph高级特性.md:47>)：异步流式队列与调用方消费。

另外，[agent-runtime/readme.md](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/readme.md:34>) 规划过 `day25_async_tools`，目录名声称包含“异步、超时、取消、背压”，但该目录及对应代码当前并不存在。

- 异步 I/O：有覆盖
- 并发：有覆盖，但偏 LangGraph 编排，不是完整结构化并发
- 超时：有覆盖
- 取消：只有中断/暂停，缺少真正的取消传播
- Backpressure：基本没有系统覆盖，只提到了流式队列

所以更准确地说：覆盖了基础概念，但“取消”和“Backpressure”还不完整。


## 异步工具调度补充大纲

当前仓库已有异步调用、并行节点、流式队列和超时的基础介绍，但以下主题仍需要系统补充。`day25_async_tools` 目前是学习路径中的规划目录，相关实现尚未提交。

### 1. 结构化并发（Structured Concurrency）

- 使用 `asyncio.TaskGroup` 管理一组有明确生命周期的子任务。
- 父任务结束时，子任务不能继续失控地运行。
- 一个子任务失败时，如何取消同组任务并统一收集异常。
- 区分“并发执行”与“结构化管理”：`gather()` 能并发，但不自动表达任务的层级和生命周期。
- 工具批次、Agent 回合、整条请求分别作为不同的并发作用域。
- 并发任务写入共享状态时，使用结果聚合而不是隐式修改全局变量。

### 2. 超时边界（Timeouts）

- 单个模型调用超时。
- 单个工具调用超时。
- 一批并发工具的整体超时。
- Agent 请求的总预算超时。
- 使用 `asyncio.timeout()` 或客户端自身的 `timeout` 参数。
- 超时后的任务清理、连接释放和状态标记。
- 读操作可以有限重试；写入、扣款、删除等副作用操作超时后，先确认远端状态再决定是否重试。

### 3. 取消传播（Cancellation）

- 请求断开、用户停止生成、上层超时时触发取消。
- 正确处理 `asyncio.CancelledError`，不要无意中吞掉取消信号。
- 取消从 Agent 请求传播到工具批次，再传播到具体 I/O 操作。
- 在 `finally` 中关闭连接、释放 Semaphore、清理临时文件和队列任务。
- 区分可取消的查询工具与不可随意中断的副作用工具。
- 对不可取消的副作用使用幂等键、状态查询和补偿流程。
- 区分“取消运行中的任务”和 LangGraph 的 `interrupt()`：前者是运行时控制，后者是工作流暂停/恢复。

### 4. Backpressure 与资源上限

- 使用有界 `asyncio.Queue`，避免生产者无限生成工具任务。
- 使用 `Semaphore` 限制同时运行的模型、HTTP、数据库工具数量。
- 当队列已满时让生产者等待，而不是继续堆积内存。
- 明确队列满时的策略：等待、拒绝、丢弃低优先级任务或返回降级结果。
- 为不同类型的 I/O 设置独立并发上限，避免一种工具耗尽全部资源。
- 设置队列等待超时、任务执行超时和整体请求超时。
- 监控队列长度、等待时间、活动任务数、拒绝数和超时数。

### 5. I/O 工具调度

- HTTP API、数据库、Redis、文件和 MCP 工具优先使用异步客户端。
- 不要在事件循环中直接执行阻塞式 I/O 或长时间 CPU 计算。
- 复用连接池，不要为每次工具调用重复创建客户端。
- 为工具定义统一的输入、输出、错误和超时边界。
- 让工具层负责 I/O 细节，让调度层负责并发、取消、超时和重试策略。
- 对外部服务错误进行分类：可重试、不可重试、需要人工确认。

### 6. 组合调度模式

推荐按以下顺序设计一次工具批次：

```text
接收请求
  → 创建结构化并发作用域
  → 将工具任务放入有界队列
  → Semaphore 控制 I/O 并发
  → 为单任务和整批任务设置超时
  → 请求结束或超时时传播取消
  → finally 释放资源
  → 聚合成功、失败、取消和降级结果
```

需要重点验证的组合场景：

- 一个工具超时，其他并行工具是否继续或一起取消。
- 用户断开连接后，后台 I/O 是否真的停止。
- 队列已满时，系统是否有明确的拒绝或降级行为。
- 工具被取消后，连接、锁、Semaphore 和临时资源是否释放。
- 重试是否会突破并发上限，或重复执行非幂等副作用。

### 7. 最小验收清单

- 能限制同时运行的工具数量。
- 能限制队列长度并观察队列满的行为。
- 单个工具超时后不会遗留后台任务。
- 父任务取消后，子任务和 I/O 操作都能收到取消信号。
- 任务组中一个任务失败时，其他任务的行为符合预期。
- 取消、超时、拒绝、重试和降级结果可以区分。
- 副作用工具具备幂等或状态确认机制。


可以把它们理解成“多人同时干活时，怎么保证不失控”。

### 1. 异步 I/O：等待外部服务时使用

适合：

- 调用 OpenAI、Gemini、搜索 API
- 查询数据库、Redis
- 读取文件
- 调用 MCP 工具

例子：Agent 调用搜索 API 时，不要占住整个程序，可以去处理其他请求。

---

### 2. 并发：多个任务互不依赖时使用

例子：用户问：

> “帮我查天气、查汇率、查新闻。”

这三个任务互不依赖，可以同时执行，而不是：

```text
查天气 → 查完后查汇率 → 查完后查新闻
```

这样能节省总等待时间。

---

### 3. 结构化并发：并发任务需要一起管理时使用

例子：

```text
一次请求
├── 查天气
├── 查汇率
└── 查新闻
```

如果用户中途关闭页面，应该把下面三个任务一起取消，而不是它们继续偷偷运行。

所以：

- 并发：让多个任务同时执行
- 结构化并发：保证这些任务有明确的开始、结束和归属

---

### 4. 超时：外部服务可能卡住时使用

例子：

- 搜索 API 30 秒没响应
- 数据库连接一直等待
- 某个工具服务挂死

应该设置：

```text
单个工具最多等 10 秒
整次 Agent 请求最多等 60 秒
```

否则一个请求可能永远不返回。

---

### 5. 取消：用户不想继续时使用

例子：

- 用户点击“停止生成”
- 用户关闭浏览器
- 请求超时
- Agent 已经得到答案，不需要继续执行其他工具

这时需要取消正在运行的任务，释放连接和资源。

注意：查询天气可以直接取消，但“扣款、发邮件、删除数据”不能随便中断，必须确认远端到底有没有执行成功。

---

### 6. Backpressure：任务太多时使用

例子：用户上传了 10 万条数据，每条都要调用一个 API。

如果一次创建 10 万个任务，会导致：

- 内存暴涨
- API 被打爆
- 数据库连接耗尽
- 服务整体变慢

Backpressure 的意思就是“让生产速度适应处理速度”：

```text
最多同时处理 10 个任务
队列最多排 100 个
超过后等待、拒绝或降级
```

---

### 7. 这些功能通常一起使用

一个典型 Agent 请求可能是：

```text
用户请求
  → 并发调用多个工具
  → Semaphore 限制同时运行数量
  → Queue 防止任务无限堆积
  → 每个工具设置超时
  → 用户取消时取消全部子任务
  → 最后统一整理结果
```

最简单的判断方式：

- 只有一个简单 API 调用：异步 I/O + 超时通常够了
- 多个工具同时调用：加并发
- 并发任务属于同一次请求：加结构化并发和取消
- 任务数量可能很多：加 Backpressure
- 涉及扣款、写入、删除：再加幂等和执行状态确认

跳过：现在不需要马上实现所有机制；先理解“任务多、会卡住、用户会取消”这三个现实问题即可。