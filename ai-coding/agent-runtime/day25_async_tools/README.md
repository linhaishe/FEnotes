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


# 异步工具调度补充大纲

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

# ---- here----

看过了。现在这份 README 更像“知识盘点 + 零散解释”，还不是一个可以照着做的项目计划。

建议把整个学习项目定义成：

> 实现一个可靠的异步工具调度器：接收一批工具调用，控制并发、超时、取消和队列压力，最后返回每个任务的执行结果。

不要一开始接真实 OpenAI 或数据库，先用“可控的模拟工具”学习，这样更容易观察问题。

## 项目最终效果

输入 10 个工具任务：

```text
search("天气")
fetch_url("...")
query_database("...")
send_email("...")
```

调度器负责：

```text
最多同时执行 3 个
每个任务最多 5 秒
整个批次最多 20 秒
队列最多等待 10 个
用户取消时取消所有查询任务
失败任务不影响其他任务
最终区分成功、失败、超时、取消、拒绝
```

---

## 阶段一：异步 I/O 基础

file: `agent-runtime/day25_async_tools/phase1_demo.py`

run: `python agent-runtime/day25_async_tools/phase1_demo.py`

`python 文件.py`：直接运行一个文件。
`python -m 模块名`：把某个模块当作程序运行。

`python -m agent_runtime.day25_async_tools.phase1_demo`

因为目录名使用了连字符 -，不能直接写成标准模块路径。若以后改成 Python 包结构，通常更推荐下划线

### 项目目标

实现 3 个模拟 I/O 工具：

```python
async def search(...)
async def fetch_weather(...)
async def query_database(...)
```

每个工具内部使用 `asyncio.sleep()` 模拟网络等待。

先实现两种执行方式：

```text
串行执行：A → B → C
并发执行：A、B、C 同时执行
```

结果

```
串行: 0.60s
并发: 0.30s
```

### 学习内容

- `async def`
- `await`
- `asyncio.run`
- `asyncio.gather`
- 为什么 `time.sleep()` 会阻塞事件循环
- I/O 密集型任务为什么适合异步

### 验收标准

- 并发执行耗时明显低于串行执行。
- 一个任务等待时，其他任务仍能执行。
- 能区分异步 I/O 和 CPU 密集型任务。

---

## 阶段二：统一工具接口

Demo：`phase2_scheduler.ipynb`

在 Jupyter 中打开后运行全部单元格。这个 Demo 对应最终项目结构中的 `scheduler.py`，同时提前演示 `models.py` 中的 `ToolCall` 和 `ToolResult`。

### 项目目标

不要让调度器认识每个工具的内部实现，只认识统一的工具任务。

```python
ToolCall(
    name="search",
    arguments={"query": "..."},
    timeout=5,
    kind="read",
)
```

每个结果统一为：

```python
ToolResult(
    status="success",
    value=...,
    error=None,
)
```

### 学习内容

- 工具注册表
- 工具输入和输出
- 工具错误分类
- 查询工具和副作用工具的区别
- 用 `ToolCall` 描述“调用哪个工具以及传什么参数”
- 用 `ToolResult` 统一表示成功和失败
- 用一个 `execute_tool()` 入口执行不同工具
- 用 `dict[str, Tool]` 解耦调度器和工具实现
- 用关键字参数把 `ToolCall.arguments` 传给具体工具

### Demo 中的方法

| 方法 | 作用 |
| --- | --- |
| `search(query)` | 模拟搜索工具，参数是搜索关键词 |
| `fetch_weather(city)` | 模拟天气工具，参数是城市名 |
| `register_tool(registry, name, tool)` | 把工具加入注册表 |
| `execute_tool(registry, call)` | 根据统一的 `ToolCall` 找到并执行工具，返回 `ToolResult` |
| `main()` | 注册工具、构造调用并执行验收 |

### 验收标准

调度器可以执行任意注册工具，不需要为每个工具写一套特殊逻辑。

运行 Demo 后应能看到两个成功结果和一个未知工具错误：

```text
search -> ToolResult(status='success', ...)
fetch_weather -> ToolResult(status='success', ...)
missing -> ToolResult(status='failed', ...)
```

本阶段刻意不加入并发、超时、取消、Semaphore 和 Queue；这些机制会在后续阶段围绕同一个统一工具接口继续添加。

---

## 阶段三：结构化并发

Demo：`phase3_structured_concurrency.ipynb`

在 Jupyter 中打开后运行全部单元格。

### 项目目标

使用标准库 `asyncio.TaskGroup` 管理一批工具任务：

```text
一次批次
├── search
├── weather
└── database
```

`TaskGroup` 是一个结构化并发作用域。进入作用域时创建子任务，离开作用域前等待它们结束；如果一个任务失败，仍在运行的同批任务会被取消，异常会在作用域退出时统一传播。

### 学习内容

- `asyncio.TaskGroup` 的创建和退出。
- 父任务与子任务的生命周期关系。
- 一个子任务失败时，其他子任务如何被取消。
- 使用 `asyncio.CancelledError` 做清理并重新抛出取消信号。
- `TaskGroup` 和 `asyncio.gather()` 的区别：前者明确表达任务层级和生命周期。

### Demo 中的方法

| 方法 | 作用 |
| --- | --- |
| `fake_tool(name, delay, should_fail)` | 模拟一个可成功、失败或被取消的异步工具；参数分别是名称、等待时间和是否失败 |
| `run_batch(task_refs)` | 在一个 `TaskGroup` 中创建并管理工具任务；`task_refs` 记录本批次的子任务以便检查生命周期 |
| `main()` | 捕获批次异常并验证没有遗留后台任务 |

### 验收标准

- 一个工具失败后，仍在运行的同批工具会收到取消信号。
- `TaskGroup` 退出后没有遗留后台任务。
- 失败以异常组传播，而不是被静默吞掉。

运行后可以看到类似输出：

```text
weather: cancelled
batch failed with 1 exception(s)
batch finished without background tasks
```

本阶段只演示结构化并发；单工具超时、整批超时、队列和 Semaphore 在后续阶段加入。

### 项目目标

用 `asyncio.TaskGroup` 管理一批工具任务。

```text
一次批次
├── 工具 A
├── 工具 B
└── 工具 C
```

当批次结束时，不能残留后台任务。

### 学习内容

- `asyncio.TaskGroup`
- 父任务和子任务
- 子任务异常如何传播
- 一个任务失败时，其他任务是否取消
- `TaskGroup` 和 `gather()` 的区别

### 推荐实验

设计三种策略进行比较：

```text
策略 A：任何任务失败，整批取消
策略 B：单个任务失败，其他任务继续
策略 C：查询任务继续，关键任务失败时整批取消
```

### 验收标准

- 批次结束后没有遗留任务。
- 能明确选择“单任务失败”还是“整批失败”。
- 不使用全局列表偷偷保存任务。

---

## 阶段四：超时

### 项目目标

给工具调度器增加三层超时：

```text
单个工具超时：5 秒
单批工具超时：15 秒
整次请求超时：30 秒
```

### 学习内容

- `asyncio.timeout()`
- 单任务超时和整批超时
- 超时后的取消行为
- `finally` 清理资源
- 外部 HTTP 客户端自身的 timeout

### 推荐实验

准备三个模拟工具：

```text
fast_tool：1 秒返回
slow_tool：一直等待
flaky_tool：有时成功，有时超时
```

### 验收标准

- 慢工具不会让整次请求永久卡住。
- 单个任务超时后能返回 `timeout`。
- 超时后没有残留后台任务。
- 超时不会自动重试非幂等工具。

---

## 阶段四 Demo：超时边界

Demo：`phase4_timeouts.ipynb`

使用 `asyncio.timeout()` 演示三层超时中的前两层：单个工具超时和整批工具超时；整次请求超时可以在 Agent 入口继续包住整个批次。

### Demo 中的方法

| 方法 | 作用 |
| --- | --- |
| `fake_tool(name, delay)` | 模拟外部 I/O；参数是工具名称和等待秒数，并在 `finally` 中清理 |
| `run_with_timeout(name, delay, timeout)` | 执行单个工具；参数包含名称、运行时间和超时时间，超时返回 `timeout` |
| `run_batch(timeout)` | 并发执行快、慢两个工具，并给每个工具设置独立超时 |
| `run_request(tool_timeout, batch_timeout)` | 给整个批次增加总超时；参数分别是单工具和整批超时时间 |
| `main()` | 验证单工具超时、整批超时和清理行为 |

### 关键知识

- 单个工具超时后，其他工具仍可以继续完成。
- 整批超时会取消尚未完成的工具，并等待取消清理结束。
- `finally` 中的清理逻辑会在成功、失败和超时后执行。
- 对扣款、发邮件等副作用操作，超时后不能直接重试，应先确认远端状态。

### 验收标准

- 慢工具不会让请求永久阻塞。
- 单工具超时返回 `slow_tool: timeout`。
- 整批超时返回空列表，并取消未完成任务。
- 输出清理信息，且 notebook 执行结束后没有遗留任务。

### LangChain Async 对照

4 个阶段的 notebook 都额外包含一个 LangChain Async 小例子：

- `phase1`：`RunnableLambda.abatch()` 并发执行异步 I/O。
- `phase2`：`RunnableLambda.ainvoke()` 调用统一工具入口。
- `phase3`：把 LangChain Runnable 放进 `asyncio.TaskGroup`。
- `phase4`：给 Runnable 的 `ainvoke()` 增加 `asyncio.timeout()`。

LangChain Runnable 的异步入口主要是 `ainvoke()`；批量异步调用使用 `abatch()`。详见[官方 LangChain Async 文档](https://python.langchain.com/docs/how_to/async/)。

### FastAPI 对照

4 个阶段的 notebook 也各自包含一个 FastAPI 路由示例。路由只负责接收 HTTP 请求并 `await` 已有的异步函数，不把调度、并发和超时逻辑重复写在 Web 层。Demo 只注册路由，不启动端口；实际运行时可使用：

```bash
uvicorn module:app --reload
```

## 阶段五：取消传播

### 项目目标

模拟用户点击“停止生成”：

```text
用户请求
  → 工具批次
    → 多个工具任务
      → 具体 I/O
```

取消必须从最上层传递到底层。

### 学习内容

- `asyncio.Task.cancel()`
- `asyncio.CancelledError`
- `try/finally`
- 取消时释放连接、锁和 Semaphore
- 取消查询任务和取消副作用任务的区别

### 推荐实验

启动 5 个工具，然后在第 2 秒取消整个批次。

观察：

```text
哪些任务收到取消
哪些任务已经完成
哪些资源被释放
是否还有任务继续运行
```

### 验收标准

- 父任务取消后，子任务也能停止。
- 不吞掉 `CancelledError`。
- `finally` 一定执行。
- 查询工具可以取消。
- 邮件、扣款、删除等副作用工具不会因为取消而进入未知状态。

---

## 阶段五 Demo：取消传播

Demo：`phase5_cancellation.ipynb`

这个 Demo 使用同一个可取消工具，分别展示原生 Python、LangChain Async 和 FastAPI 入口。

### Demo 中的方法

| 方法 | 作用 |
| --- | --- |
| `cancellable_tool(name, delay, cleaned)` | 模拟可取消工具；参数是名称、等待时间和清理记录列表 |
| `run_cancellable_batch(names, delay)` | 并发运行一批工具；参数是名称列表和等待时间，并传播父任务取消 |
| `native_cancel_example()` | 使用原生 `Task.cancel()` 取消批次 |
| `langchain_async_example()` | 使用 LangChain Runnable 的 `ainvoke()`，再取消其任务 |
| `run_phase5_cancel()` | FastAPI 路由示例，运行并取消一个异步批次 |
| `main()` | 验证原生 Python 和 LangChain Async 的取消传播 |

### 关键知识

- `task.cancel()` 会向任务注入 `asyncio.CancelledError`。
- 捕获 `CancelledError` 后通常必须重新抛出，不能吞掉取消信号。
- `finally` 无论成功、失败还是取消都会执行，适合释放连接、锁和 Semaphore。
- 查询任务通常可以取消；扣款、发邮件、删除等副作用操作需要幂等键和远端状态确认。
- FastAPI 路由只是异步入口；真实客户端断开时，ASGI 服务器负责取消请求任务。

### 验收标准

- 父任务取消后，子工具收到取消信号。
- 原生 Python、LangChain Async 和 FastAPI 示例都保留清理逻辑。
- 不吞掉 `CancelledError`。
- notebook 执行结束后没有遗留批次任务。

## 阶段六：Backpressure

### 项目目标

让调度器处理 100 个任务，但不能一次启动 100 个网络请求。

设置：

```text
队列容量：10
最大并发数：3
```

### 学习内容

- `asyncio.Queue(maxsize=...)`
- 生产者和消费者
- `asyncio.Semaphore`
- 队列满时等待
- 队列满时拒绝或降级
- 并发上限和吞吐量

### 推荐实验

```text
生产者：快速生成 100 个任务
消费者：最多同时执行 3 个
```

记录：

```text
队列长度
排队时间
执行时间
拒绝数量
当前活动任务数
```

### 验收标准

- 同时运行的任务永远不超过 3 个。
- 队列长度永远不超过 10。
- 任务太多时不会无限增长内存。
- 能选择队列满时的行为：

```text
等待
拒绝
丢弃低优先级任务
返回降级结果
```

---

## 阶段七：失败、重试和幂等

### 项目目标

给工具增加不同类型的失败：

```text
网络临时失败
参数错误
权限错误
超时
未知错误
```

### 学习内容

- 哪些错误可以重试
- 指数退避
- 重试是否受并发上限控制
- 查询工具和写入工具的区别
- 幂等键
- 远端执行状态确认

### 推荐规则

```text
查询失败：可以有限重试
模型调用失败：可以有限重试
发送邮件超时：先查询是否已发送
扣款超时：不能直接重试
删除数据失败：需要人工确认
```

### 验收标准

- 重试不会突破并发上限。
- 非幂等操作不会盲目重试。
- 每次任务都能说明最终状态。
- 状态至少区分：

```text
success
failed
timeout
cancelled
rejected
unknown
```

---

## 阶段八：接入真实 I/O

前面都稳定后，再替换模拟工具：

```text
模拟 HTTP → httpx.AsyncClient
模拟数据库 → 异步数据库客户端
模拟 Redis → redis.asyncio
模拟 MCP → MCP 异步客户端
```

重点不是“会调用 API”，而是保证：

- 连接池复用
- 客户端正确关闭
- timeout 参数生效
- 取消能够传到底层
- 不把同步阻塞库放进事件循环

---

## 最终项目结构

```text
day25_async_tools/
├── README.md
├── models.py          # ToolCall、ToolResult、状态
├── fake_tools.py      # 可控的模拟工具
├── scheduler.py       # 调度器
├── concurrency.py     # TaskGroup、Semaphore
├── cancellation.py    # 取消传播
├── backpressure.py    # Queue、生产者、消费者
├── retry.py           # 重试与退避
├── demo.py            # 可运行演示
└── test_async_tools.py
```

但建议按阶段逐步创建文件，不要一开始把这些文件全部建出来。

## 最推荐的学习顺序

```text
模拟异步 I/O
  → 串行和并发
  → 统一工具接口
  → TaskGroup
  → 单任务和整体超时
  → 取消传播
  → Queue + Semaphore
  → 重试和幂等
  → 真实 HTTP / 数据库 / MCP
```

每个阶段只加一个新问题。这样你学到的不是 API，而是：

> 当 Agent 同时调用很多外部工具时，如何让它不会卡死、失控、泄漏资源或重复执行危险操作。
