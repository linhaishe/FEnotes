# Day 35：对抗测试与生产环境模拟

本阶段用可重复的攻击样本和故障注入，验证 Agent 在接近生产的条件下是否守住权限边界、正确处理依赖故障，并能通过 Trace、指标和日志定位原因。本目录现有离线 Mock 演练；真实 DeepSeek 和远端 LangSmith 不参与默认回归。

## 运行 Demo

在仓库根目录运行：

```bash
python -m pip install -r observability_deployment/day35_adversarial_testing_production_simulation/requirements.txt
python -m unittest discover -s observability_deployment/day35_adversarial_testing_production_simulation -p 'test_*.py' -v
python -m observability_deployment.day35_adversarial_testing_production_simulation.rehearsal --report /tmp/day35-report.json
```

第二条命令对 11 个固定场景发起进程内 HTTP 请求，输出单行 JSON 运行日志，并把脱敏观测证据写入指定路径；任一场景不通过时退出码为非零。仓库中的 [report_example.json](./report_example.json) 是使用纯 Mock、假用户生成的样本。**本 Demo 特例不为报告添加 `.gitignore` 规则**：普通运行应指定仓库外的路径，只有检查确认不含真实 Prompt、Key、PII 后才更新仓库样本。

容器故障演练单独显式启动：

```bash
DAY35_RUN_DOCKER=1 python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_service_failure -v
```

该测试创建独立 Compose 项目，分别验证 Day 33 Redis 不可用/恢复和 Day 34 审计 Volume 在 API 重启后仍可读取；默认测试不会启动 Docker。Day 35 的本地 LangSmith `RunTree` 只用于验证同请求父子关系，不上传远端。混合文档的 `事实:`/`指令:` 提取仅支持固定教学样本，不代表通用的 Prompt Injection 防护。

## 学习目标

完成后应能回答：恶意指令在哪个边界被拦截？一次越权工具调用是否真的到达工具？模型超时与工具失败如何区分？服务故障后任务和审批状态是否仍可查询？如何用同一个 `request_id` / `trace_id` 找到对应的 Trace、指标变化和日志事件？

## 一、先建立安全的演练边界

- 只在本地或隔离测试环境演练；使用假 API Key、假用户和无副作用的 Mock Tool，不针对真实用户或生产数据发起攻击。
- 为每个场景固定输入、预期响应、预期工具调用、日志事件和指标变化。先运行正常基线，再注入单一故障，最后恢复并复测。
- 给每次请求保存 `request_id`、`trace_id`、场景名和测试时间；不把完整 Prompt、凭据或个人信息写进运行日志。
- 区分两类判断：安全策略是否阻止危险动作，以及系统是否提供足够证据说明为何阻止或失败。

## 二、直接与间接 Prompt Injection

1. **直接注入**：用户输入要求忽略原指令、泄露系统提示词或绕过审批。验证输入 Guardrail 在模型和工具运行前拒绝。
2. **间接注入**：网页、文档或工具返回值夹带“改用高权限工具”等指令。验证外部内容只被当作数据，不能修改系统策略、工具允许列表或当前用户身份。
3. 同时保留正常样本，防止防御规则误拦截合法请求。
4. 在 Trace 中检查调用是否停在预期边界；在日志和审计事件中只记录拒绝类别与关联 ID，不记录攻击文本原文。

可复用 [Day 32 安全与 HITL](../day32_security_guardrails_hitl/) 的 Guardrail 和 Mock Tool，再用 [Day 31 Agent Evals](../day31_agent_evals_testing/) 的回归样本固定预期。

## 三、越权工具调用与审批绕过

- 构造跨用户读取、非法金额、缺少资源 ID、调用未授权工具等请求。断言参数校验在副作用发生前失败。
- 构造“模型建议删除”“审批待处理”“审批拒绝”三种状态，确认它们都不等同于 `tool_executed`；只有真实审批通过且执行成功后才能记录执行事件。
- 比较工具 Trace、运行日志和审计文件：拒绝路径不应出现实际工具执行；审计事件要能按审批请求 ID 还原请求、决定与执行。
- 注意 HTTP `request_id` 与审批请求 ID 可能不同；若跨流程关联，需显式记录映射，不能仅凭时间接近推断。

## 四、超时与服务故障注入

按单一变量逐项模拟：模型超时或 5xx、工具超时或异常、Redis 不可用、容器重启。每项分别检查：

1. 用户收到明确且不泄露内部细节的失败结果；请求不会无限等待。
2. `error_type` 能区分模型、工具和依赖故障；若设计了重试，记录次数、最终结果，并避免有副作用工具被重复执行。
3. readiness 反映关键依赖是否可用；liveness 不应因为短暂依赖失败而误判进程已死。
4. 恢复依赖或重启服务后，按设计持久化的任务和审批审计仍可查询。

优先使用 Mock、受控异常和测试容器复现故障，不通过真实 API 消耗额度或触发真实写操作。可参考 [Day 33 容器化](../day33_containerization_service_orchestration/) 的服务与重启场景。

## 五、用 Trace、指标和日志定位

| 证据 | 主要回答的问题 | 本阶段检查点 |
| --- | --- | --- |
| Trace | 哪一步失败、父子调用关系是什么？ | 按 `trace_id` 查看模型、工具子调用和耗时；确认敏感输入输出的上传策略。 |
| 指标 | 故障影响了多少请求、持续多久？ | 对比 QPS、错误率、P95/P99 延迟、模型/工具失败计数和重试趋势。 |
| JSON 日志 | 单次请求发生了哪些事件？ | 按 `request_id` 还原开始、失败分类和最终状态，不记录异常原文。 |
| 审计事件 | 高风险操作被请求、批准、拒绝还是执行？ | 按审批 ID 核对决定和实际工具执行，拒绝后没有执行记录。 |

分别复用 [Day 29 Trace](../day29_langsmith_tracing/)、[Day 30 指标大盘](../day30_metrics_dashboard/)、[Day 34 日志与审计](../day34_structured_logging_audit/) 的已有能力。指标用于观察总体趋势，不能单独证明某个请求的工具没有执行；单次 Trace 也不能代替总体错误率。

## 六、建议练习顺序

1. 准备正常、直接注入、间接注入、越权工具调用四组固定样本，记录各自允许或拒绝的预期。
2. 运行 Mock 回归测试，确认攻击样本没有到达危险工具，正常样本仍能完成。
3. 依次注入模型超时、工具失败和依赖不可用；每次只改变一个故障点。
4. 记录响应状态、`request_id` / `trace_id`、日志事件序列、审计事件和指标变化，对照预期解释故障来源。
5. 恢复依赖并复测正常路径；重启测试容器，检查持久化审计事件仍能查询。
6. 将稳定、无外部副作用的样本纳入 CI；真实模型测试单独运行，记录模型版本和可能的非确定性。

## 七、完成标准

- 直接/间接注入和越权调用均有可复现样本；危险工具未执行，正常请求未被误拦截。
- 模型超时、工具失败、服务故障能被区分；响应、日志、Trace 与指标的证据相互一致。
- 审批拒绝没有工具执行事件；审批通过和实际执行分开记录。
- 能按关联 ID 还原单次请求，按指标判断故障范围，并说明无法仅凭某一种信号得出的结论。
- 恢复及容器重启后，按设计持久化的审计记录仍可查询；测试不泄露真实凭据或敏感内容。
