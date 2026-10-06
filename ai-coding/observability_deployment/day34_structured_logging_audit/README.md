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
3. 将同一请求的日志与 Day 29 `trace_id` 关联。
4. 为 Day 32 的审批请求、批准、拒绝和工具执行写独立审计事件。
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

## 第一个 Demo：请求 ID 与 JSON 日志

`demo.py` 提供一个 FastAPI Mock Agent。中间件给每次请求生成 `request_id`，把它同时放入响应体与 `X-Request-ID` 响应头。模型和工具调用分别记录开始、成功结束或失败事件，最后记录请求完成事件；每个事件占一行 JSON。日志不记录 Prompt、工具参数或异常原文。

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

响应中的 `X-Request-ID`、`request_id` 与服务终端 JSON 日志中的 `request_id` 应一致。天气请求会依次产生 `model_call_started`、`model_call_finished`、`tool_call_started`、`tool_call_finished` 和 `agent_request_finished`。结束事件包含 `duration_ms`；失败事件另外包含 `error_type`，值为 `timeout` 或 `error`。

运行验证：

```bash
python -m unittest test_demo.py -v
```

本 Demo 已覆盖练习 1 和 2。模型和工具目前为 Mock，实现可重复的成功与失败测试；后续可接入真实模型、工具和审计事件。
