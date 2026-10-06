# Day 34：结构化日志与审计

本阶段为 Agent 应用输出可检索的 JSON 日志和审计事件，同时避免记录凭据、个人信息（PII）和敏感上下文。

参考资料：

- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)：logger、日志级别、handler、filter 和 formatter。
- [structlog 文档](https://www.structlog.org/en/stable/)：结构化事件、上下文字段与 JSON 输出。

## 学习目标

完成后，应能回答：一次 Agent 任务失败时，如何通过 `request_id` 找到模型与工具调用？谁批准了一次高风险操作？日志里是否可能泄露 API Key、用户数据或完整 Prompt？

## 一、区分运行日志与审计事件

| 类型 | 回答的问题 | 典型事件 |
| --- | --- | --- |
| 运行日志 | 服务发生了什么、哪里失败、耗时多久 | `task_started`、`model_failed`、`tool_timed_out` |
| 审计事件 | 谁在何时请求、批准、拒绝或执行了什么操作 | `approval_requested`、`approval_rejected`、`tool_executed` |

运行日志用于排障；审计事件用于还原权限决策和有副作用的操作。审计记录不能只依赖普通 `DEBUG` 日志：日志级别变化、采样或轮转都不应使关键审批事件消失。

## 二、JSON 日志的最小字段

每行输出一个 JSON 对象（JSON Lines），字段名称保持稳定：

```json
{"timestamp":"2026-10-06T08:00:00Z","level":"info","event":"tool_call_finished","request_id":"req-123","task_id":"task-456","tool":"weather","status":"success","duration_ms":42}
```

建议字段：

- `timestamp`：使用带时区的时间，统一采用 UTC。
- `level`、`event`：严重程度和稳定的事件名称。
- `request_id`、`task_id`：关联同一请求和任务的事件；不要记录原始 Prompt 作为关联键。
- `tool`、`status`、`duration_ms`：定位工具故障与性能问题。
- `error_type`：稳定的错误分类；避免直接记录含敏感内容的异常消息。

按需增加 `trace_id`，将日志与 Day 29 的链路追踪关联。日志用于查看单次事件，指标用于看总量与趋势，两者不要互相替代。

## 三、Python Logging 基础

学习 `logging.getLogger(__name__)`、`DEBUG/INFO/WARNING/ERROR`、handler、filter 和 formatter：

1. 用 logger 记录事件，避免用 `print()` 作为服务日志。
2. 将日志输出到标准输出，由容器平台收集。
3. 用 formatter 转为一行 JSON；用 filter 或统一处理器在输出前检查敏感字段。
4. 对异常记录错误类型和关联 ID；审慎处理堆栈，因为堆栈或异常消息可能包含原始请求。

## 四、structlog 的结构化上下文

学习如何使用事件名和命名字段，而不是拼接不可检索的字符串：

```python
log.info("task_finished", task_id="task-456", status="success", duration_ms=42)
```

重点练习：JSON renderer、时间戳、日志级别、`request_id` 绑定与清理，以及与标准库 `logging` 的集成。并发请求之间的上下文不能串用；进入请求时绑定，完成后清理。

## 五、敏感信息边界

采用“允许记录的字段清单”设计事件。默认只记录操作类型、结果、耗时和不含敏感信息的 ID；不要把整个请求、响应、工具参数或异常对象直接序列化。

禁止直接记录：

- `DEEPSEEK_API_KEY`、Authorization Header、Cookie、数据库密码。
- 邮箱、手机号、身份证号等 PII。
- 完整用户 Prompt、检索文档、模型原始响应和工具返回的敏感内容。
- 审批备注或工具参数中可能包含的凭据。

如果排障确实需要部分上下文，应先定义明确的保留字段和脱敏规则，并限制访问与保留期限。记录哈希 ID 也应评估能否重新识别用户。

## 六、Agent 生命周期中的埋点位置

```text
请求进入 → 输入校验 → Agent 开始 → 模型调用 → 工具调用
     → 审批请求/决定 → 最终结果或异常 → 请求结束
```

为每个关键阶段设计成功、失败事件。尤其关注：

- 模型和工具失败的不同 `error_type`。
- 超时、重试次数与最终结果。
- 高风险工具在审批前不能执行；审批拒绝后记录拒绝事件，不记录执行成功。
- 审批通过后记录审批人与时间，并在真正执行时单独记录 `tool_executed`。

## 七、审计事件设计

审计事件至少包含：`event`、`timestamp`、`actor_id`、`request_id`、`resource_id`、`decision`、`reason_code`。使用稳定的状态名，例如 `requested`、`approved`、`rejected`、`executed`、`failed`。

不要将“模型建议执行”当作“已执行”。审计记录应由权限检查、审批服务和工具执行层写入，而不是由模型输出生成。生产系统还需考虑持久化、访问控制、保留期限与防篡改策略。

## 八、练习顺序

1. 给一个 FastAPI Agent 请求增加 `request_id`，输出一行 JSON 运行日志。
2. 在模型调用和工具调用处记录开始、结束、耗时与错误分类。
3. 将同一请求的日志与 `trace_id` 关联。
4. 复用 Day 32 的审批请求、批准、拒绝和工具执行写独立审计事件。
5. 构造包含 API Key、邮箱、手机号和完整 Prompt 的输入，验证日志与审计事件均不会泄露。
6. 模拟模型超时、工具失败、审批拒绝，按 `request_id` 还原处理过程。
7. 在 Day 33 容器中从标准输出读取 JSON 日志；重启服务后确认审计事件仍可查询。

## 九、完成标准

- 每条运行日志是可解析的单行 JSON，并带时间、级别、事件名和关联 ID。
- 同一任务的模型、工具与最终结果能按 `request_id` 或 `trace_id` 关联。
- 高风险操作的请求、审批决定与实际执行分别有审计记录。
- 不记录凭据、PII、完整 Prompt 和敏感工具结果。
- 正常、失败、重试和拒绝路径都有测试；日志内容可用于定位问题而不泄露敏感上下文。
- 容器重启后，按设计持久化的审计事件仍可查询。

## Demo

`demo.py` 默认运行 FastAPI Mock Agent，也可选用 DeepSeek LangChain Agent。中间件给每次请求生成 `request_id`，并创建一个 LangSmith 根 Trace。两个 ID 都写入日志和响应；Mock 模型和工具调用分别记录开始、成功结束或失败事件，最后记录请求完成事件。每个事件占一行 JSON，不记录 Prompt、工具参数或异常原文。

```bash
cd observability_deployment/day34_structured_logging_audit
pip install -r requirements.txt
uvicorn demo:app --port 8000 --no-access-log
```

本地需要更易读的彩色输出时，用 Rich 模式启动：

```bash
LOG_FORMAT=console uvicorn demo:app --port 8000 --no-access-log
```

Rich 模式显示事件、请求 ID 前 8 位、耗时和错误分类。默认 `LOG_FORMAT=json`，继续输出供日志系统采集的单行 JSON。两种模式都不输出 Prompt、工具参数或异常原文。

另开终端发起请求：

```bash
curl -i -X POST http://127.0.0.1:8000/agent \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"查询上海天气"}'
```

响应中的 `X-Request-ID`、`request_id` 与日志中的 `request_id` 应一致；`X-Trace-ID`、响应体与日志中的 `trace_id` 也应一致。天气请求会依次产生 `model_call_started`、`model_call_finished`、`tool_call_started`、`tool_call_finished` 和 `agent_request_finished`。结束事件包含 `duration_ms`；失败事件另外包含 `error_type`，值为 `timeout` 或 `error`。

运行验证：

```
python -m unittest test_demo.py -v
```

将同一请求的日志与 Day 29 `trace_id` 关联：

若要像 Day 29 一样将根 Trace 发送到 LangSmith，启动前设置：

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="你的 LangSmith API key"
export LANGSMITH_PROJECT=day29-langsmith-demo
uvicorn demo:app --port 8000 --no-access-log
```

在 LangSmith 的同一项目中按响应头 `X-Trace-ID` 查找该请求的根 Trace，再用日志的 `trace_id` 关联事件。未开启 tracing 时仍会生成本地 Trace ID，但不会上传到 LangSmith。

默认 Mock 路径只输出模型、工具 JSON 日志，不产生对应 LangSmith 子 Trace。要观察真实 Agent 的子调用，另起服务并设置：

```bash
export DEEPSEEK_API_KEY="你的 DeepSeek API key"
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="你的 LangSmith API key"
export LANGSMITH_PROJECT=day29-langsmith-demo
AGENT_BACKEND=deepseek uvicorn demo:app --port 8000 --no-access-log
```

用上面的 `curl` 请求天气后，Day 34 的请求根 Trace 下应展开 LangChain Agent、DeepSeek 模型和 `get_weather` 工具调用；`get_weather` 返回固定天气数据，不依赖天气服务。FastAPI 的中间件与路由可能跨异步任务，因此代码在 Agent 入口显式把根 Trace 设为父上下文。JSON 日志仍通过 `request_id` 和 `trace_id` 关联，但真实路径当前只记录 Agent 整体开始/结束，不逐个输出模型、工具 JSON 事件。LangSmith 子 Trace 可能包含完整 Prompt 和模型/工具内容，请只用非敏感测试数据，并按项目策略限制访问与保留时间。

`AGENT_BACKEND=deepseek`

这行是在**启动服务时，临时选择真实 Agent**：

- `AGENT_BACKEND=deepseek`：只对这次启动生效，让 Demo 使用 DeepSeek LangChain Agent；不设置时使用默认的 Mock Agent。
- `uvicorn demo:app`：启动 `demo.py` 里的 FastAPI `app`。
- `--port 8000`：监听 8000 端口。
- `--no-access-log`：关闭 Uvicorn 自带的请求访问日志，保留 Demo 输出的结构化日志。

它不会设置 API Key。运行前仍需配置 `DEEPSEEK_API_KEY`；如果还想在 LangSmith 查看 Trace，也要配置 `LANGSMITH_TRACING` 和 `LANGSMITH_API_KEY`。

## 审批审计 Demo：复用 Day 32

> 审计事件:
>
> 审计事件是用来回答：**谁在什么时候，对什么操作做了什么决定，以及操作最终有没有执行。**
>
> 以刚做的删除审批为例：
>
> ```
> approval_requested → approval_approved → tool_executed
> ```
>
> 这表示有人提出删除请求、审批通过、工具随后实际执行。若是拒绝，记录会是 `approval_requested → approval_rejected`，不应出现 `tool_executed`。因此审计记录能区分“批准了”和“真的执行了”，用于事后核查和追责。
>
> 它与普通运行日志的侧重点不同：运行日志帮助排查超时、报错和耗时；审计事件帮助还原权限与操作决策。当前 Demo 已记录事件、时间和审批请求 ID，但还没有记录经过可信身份验证的申请人、审批人，也没有防篡改保障，所以它是学习示例，不是完整的生产审计系统。

==从仓库的 `ai-coding` 目录运行（无需调用 DeepSeek）：==

```python
python -m observability_deployment.day34_structured_logging_audit.audit_demo \
  --state-dir observability_deployment/day34_structured_logging_audit/.audit_state
```

在仓库的 `ai-coding` 目录执行这两行即可。末尾的 `\` 表示命令换行；也可以写成一行：

```
python -m observability_deployment.day34_structured_logging_audit.audit_demo --state-dir /tmp/day34-audit-demo
```

它会模拟“一次删除请求被拒绝、另一次获批并执行”，然后把审计事件写入 `/tmp/day34-audit-demo/audit.jsonl`。查看结果：

```
cat /tmp/day34-audit-demo/audit.jsonl
```

这个演示不调用 DeepSeek，也不会删除真实资源。

查看 `/tmp/day34-audit-demo/audit.jsonl`。演示先请求删除并拒绝，再请求另一项删除、批准并执行。审计文件依次出现 `approval_requested`、`approval_rejected`、`approval_requested`、`approval_approved`、`tool_executed`；被拒绝的请求没有执行事件。Day 32 的审批存储和工具执行层写入这些事件，每条含 UTC `timestamp`，不写资源 ID、Prompt 或工具参数；审批状态另存于 `approvals.json`。

`audit.jsonl` 是独立的持久化审计文件，不受运行日志 `LOG_FORMAT` 影响。这里的 `request_id` 是 Day 32 的审批请求 ID，不是 FastAPI `/agent` 的 HTTP 请求 ID；当前演示尚未关联两者，也没有实现审批人身份或生产级防篡改存储。

```bash
python -m unittest observability_deployment.day34_structured_logging_audit.test_audit_demo -v
```

## 敏感输入验证

在 `ai-coding` 目录运行 Day 34 测试：

```bash
python -m unittest discover -s observability_deployment/day34_structured_logging_audit -p 'test_*.py' -v
```

测试只使用假的 API Key、邮箱和手机号，并构造完整 Prompt 及含敏感内容的工具结果/异常。它们分别经过 Mock Agent 的正常与失败路径、模拟真实 Agent 的入口、Day 32 的审批拒绝与批准执行路径；断言运行日志和 `audit.jsonl` 均不包含这些原文。此处验证的是**日志与审计事件**，不是对响应体、LangSmith Trace 或 `approvals.json` 的脱敏保证；不要在真实请求中放入凭据。

### LangSmith 的脱敏配置 VS 现在的字段白名单

方便脱敏的主要是 **LangSmith 的 Trace API**，不是让 LangChain 自动替你处理所有日志。

| 方法                 | 保护的对象                                   | Day 34 中的作用                                              |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| 现在的字段白名单     | 应用自己写出的 JSON 运行日志、审计事件       | 只写事件名、时间、关联 ID、耗时等字段，根本不把 Prompt 和工具结果交给日志 |
| LangSmith 的脱敏配置 | 发送到 LangSmith 的 Trace 输入、输出、元数据 | 防止模型和工具子 Trace 上传完整 Prompt 或敏感结果            |

LangSmith 提供最直接的全隐藏配置：

```
LANGSMITH_HIDE_INPUTS=true
LANGSMITH_HIDE_OUTPUTS=true
```

如果还需要保留部分内容用于排查，可以用 `Client(anonymizer=...)` 按规则遮盖邮箱等字段；也可以用 `hide_inputs`、`hide_outputs`、`hide_metadata` 分别控制。[LangSmith 官方文档](https://docs.langchain.com/langsmith/mask-inputs-outputs)

两种方法应当**叠加，而不是二选一**：LangSmith 的设置不会清理我们写入的 `audit.jsonl` 或控制台日志；Day 34 现有的日志测试也没有证明 LangSmith Trace 已脱敏。另一个区别是，全隐藏更稳妥但会失去 Trace 中的输入输出排障信息；规则脱敏保留信息更多，却可能漏掉没覆盖到的敏感格式。

验证 LangSmith 脱敏，最直接的方法是用**假的敏感数据发一次真实 Agent 请求，然后检查上传后的子 Trace**。Day 34 现有单元测试只验证 JSON 日志和审计文件，不验证 LangSmith 收到的内容。

在 Day 34 目录的 `.env` 中加入：

```
LANGSMITH_TRACING=true
LANGSMITH_HIDE_INPUTS=true
LANGSMITH_HIDE_OUTPUTS=true
```

确认原有的 `LANGSMITH_API_KEY`、`DEEPSEEK_API_KEY` 已配置，然后重启服务：

```
AGENT_BACKEND=deepseek uvicorn demo:app --port 8000 --no-access-log
```

另开终端发请求，只使用虚构数据：

```
curl -i -X POST http://127.0.0.1:8000/agent \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"查询天气: 上海。测试标记 sk-test-not-real、alice@example.test、13800138000"}'
```

从响应头复制 `X-Trace-ID`，在 LangSmith 对应项目中找到这条 Trace，**展开 DeepSeek 模型和工具的子调用**。通过标准是：能看到调用结构和关联 ID，但各级 Trace 的输入、输出中看不到测试 Prompt、假 Key、邮箱和手机号。只看根 Trace 不够，因为敏感内容可能在模型子 Trace 中。[LangSmith 官方说明](https://docs.langchain.com/langsmith/mask-inputs-outputs)

同时检查控制台 JSON 日志；它们由 Day 34 自己控制，不受上述两个 LangSmith 开关保护。注意这两个开关只是防止输入输出写入 LangSmith，**不会阻止 Prompt 发给 DeepSeek，也不会清理 `approvals.json`**。

`LANGSMITH_HIDE_INPUTS=true
LANGSMITH_HIDE_OUTPUTS=true`

这两个开关控制的是：**上传到 LangSmith 的 Trace 要不要包含调用内容**。

- `LANGSMITH_HIDE_INPUTS=true`：隐藏 Trace 的输入，比如用户 Prompt、模型收到的消息、工具调用参数。
- `LANGSMITH_HIDE_OUTPUTS=true`：隐藏 Trace 的输出，比如模型回答、工具返回结果。

开启后，你仍可在 LangSmith 看调用链、耗时和错误，但看不到这些输入输出内容。它们**不会修改发给 DeepSeek 的内容**，也不会替你脱敏 Day 34 的控制台日志或审计文件。

### 按我的理解就是 通过这些参数进行隐藏了？那我写的脱敏方法是做什么的？

你写的那套方法保护的是**另一份数据**——Day 34 自己输出的 JSON 运行日志和审计事件。它采用“只记录允许的字段”的方式：记录事件名、时间、`request_id`、`trace_id`、耗时等，不把 Prompt、工具结果或异常原文写进去。

可以把它理解为两个出口：

```
Agent 调用
  ├─→ LangSmith Trace：由 LANGSMITH_HIDE_INPUTS/OUTPUTS 控制
  └─→ 控制台日志、audit.jsonl：由你写的日志/审计代码控制
```

所以你的方法没有白写。即使关闭 LangSmith tracing，应用仍会产生日志和审计记录；反过来，即使开启那两个隐藏参数，如果代码写了 `logger.info(prompt)`，Prompt 还是会出现在控制台日志里。

另外，Day 34 目前主要是**避免记录敏感字段**，严格说比“写进去后再脱敏”更准确、更稳妥。
