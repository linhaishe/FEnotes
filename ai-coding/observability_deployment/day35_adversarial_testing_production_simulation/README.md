# Day 35：对抗测试与生产环境模拟

本阶段用可重复的攻击样本和故障注入，验证 Agent 在接近生产的条件下是否守住权限边界、正确处理依赖故障，并能通过 Trace、指标和日志定位原因。本目录现有离线 Mock 演练；真实 DeepSeek 和远端 LangSmith 不参与默认回归。

## 运行 Demo

在仓库根目录运行：

```bash
python -m pip install -r observability_deployment/day35_adversarial_testing_production_simulation/requirements.txt
python -m unittest discover -s observability_deployment/day35_adversarial_testing_production_simulation -p 'test_*.py' -v
python -m observability_deployment.day35_adversarial_testing_production_simulation.rehearsal --report /tmp/day35-report.json
```

最后一条命令对 11 个固定场景发起进程内 HTTP 请求，输出单行 JSON 运行日志，并把脱敏观测证据写入指定路径；任一场景不通过时退出码为非零。仓库中的 [report_example.json](./report_example.json) 是使用纯 Mock、假用户生成的样本。**本 Demo 特例不为报告添加 `.gitignore` 规则**：普通运行应指定仓库外的路径，只有检查确认不含真实 Prompt、Key、PII 后才更新仓库样本。

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

## 六、按项目代码学习：五个阶段

先读 [技术设计](./docs/TECHNICAL_DESIGN.md) 的第 3～6 节，弄清请求的执行顺序和 11 个固定场景；[开发文档](./docs/DEVELOPMENT.md) 用于理解边界和交付物。然后按下面顺序实践。每阶段都先预测结果，再运行命令，对照测试断言和报告解释原因。所有命令均在仓库根目录执行。

### 阶段 1：跑通正常请求，认识四种证据

从 [rehearsal.py](./rehearsal.py) 的 `create_app()`、`agent()` 开始，顺着 `weather_ok` 阅读：请求先经过 `check_input()`，Mock Model 提议调用 `weather`，`validate_tool_call()` 校验后才运行 Mock Tool，最后更新指标并返回。运行：

```bash
python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_adversarial.AdversarialTests.test_weather_request_has_correlated_trace_events_and_metrics -v
python -m observability_deployment.day35_adversarial_testing_production_simulation.rehearsal --report /tmp/day35-report.json
```

在报告中找到 `weather_ok`：`http_status=200`、`model_calls=1`、`tool_calls=1`。`actual_events` 应按模型开始/完成、工具开始/完成、请求结束排列；`trace_spans` 中模型和工具的 `parent_run_id` 等于根节点的 `id`。`metrics_delta.tasks.success=1` 是该场景在独立 registry 中的计数增量，**不是**在 Prometheus 指标上按 `request_id` 查询。思考：仅有成功响应，能证明工具确实运行了吗？还需要哪条事件或子 Trace？

### 阶段 2：比较直接注入、间接注入与混合文档

读 [test_adversarial.py](./test_adversarial.py) 中 `test_direct_and_external_injection_stop_before_model` 和 `test_mixed_content_keeps_fact_but_not_instruction`，再看 `rehearsal.py` 的 `extract_fact()`。运行：

```bash
python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_adversarial.AdversarialTests.test_direct_and_external_injection_stop_before_model -v
python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_adversarial.AdversarialTests.test_mixed_content_keeps_fact_but_not_instruction -v
```

在报告中比较 `direct_injection`、`external_blocked`、`mixed_fact`：前两者应为 403 且模型/工具调用为 0；后者为 200，模型只看到提取出的事实，没有删除或审批事件。这里的 `事实:`/`指令:` 两行格式是**特定 Mock 样本协议**，不是通用的网页净化能力；Day 32 的原始 `check_external_content()` 命中注入词时会拒绝整份内容。思考：为何不能用“整份文档被拒绝”来证明 Agent 能安全利用文档中的正常事实？

### 阶段 3：验证工具权限与人工审批

读 `agent()` 中 `validate_tool_call()` 和 `ApprovalStore.create()` 的先后顺序，再读 `test_cross_user_and_invalid_delete_never_execute_or_create_approval`、`test_approval_rejection_and_approval_execution_are_separate`。运行：

```bash
python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_adversarial -v
```

报告中的 `cross_user`、`invalid_amount`、`invalid_delete` 应为 403，工具实际调用为 0，非法删除不生成审批。`approval_rejected` 和 `approval_approved` 的 HTTP 请求都先返回 202／`pending_approval`；前者审计只有请求与拒绝，后者还要经过批准和 `tool_executed`。HTTP `request_id` 与审批 `approval_id` 分开查询，不存在“只用一个 ID 查完整审批链”的持久化映射。正金额转账因 Day 35 未配置审批策略也会在工具前被拒绝；现有删除校验只检查资源 ID 非空，**不证明资源归属**。思考：为什么 202 不能计入已完成任务的成功数？

### 阶段 4：从模型/工具故障定位到报告

读 [test_faults.py](./test_faults.py) 的超时、工具异常和脱敏测试，再对比报告中的 `model_timeout` 与 `tool_failure`。运行：

```bash
python -m unittest observability_deployment.day35_adversarial_testing_production_simulation.test_faults -v
python -m json.tool /tmp/day35-report.json
```

两者都返回 503，但模型超时只有模型失败事件，`metrics_delta.failures.model=1`，工具未启动；工具失败先有模型完成事件，再有工具失败事件，`metrics_delta.failures.tool=1` 且 `metrics_delta.tool_failures` 增加。`error_type` 只记录安全类别，不记录异常原文。按一个场景的 `request_id` 对齐 JSON 日志，按 `trace_id` 对齐报告中的本地父子节点，再看指标增量；单次请求不能推出 QPS 或 P95/P99。思考：若删除工具失败，为什么不能直接重试？

### 阶段 5：独立演练容器故障与审计恢复

有 Docker 环境时阅读 [test_service_failure.py](./test_service_failure.py)，再运行上面的 `DAY35_RUN_DOCKER=1` 命令。第一项只停止测试创建的 Day 33 Redis，观察 readiness 从 200 变为 503、恢复后回到 200；第二项重启隔离的 Day 34 API，并从其 `audit_state` Volume 按审批 ID 读回同一批审计事件。两项是**不同服务的独立演练**，不应假称它们属于同一个 Day 35 请求 Trace。默认单元测试会跳过这两项；只有实际运行通过，才算验证了容器故障与重启恢复。

### 自检与下一步练习

不看测试名称，尝试仅凭报告中的 `actual_events`、`trace_spans`、`metrics_delta` 和 `approval_events` 判断一个场景是“安全拒绝”“模型失败”“工具失败”还是“待审批”。再任选一个固定 Mock 场景，先写出预期 HTTP 状态、模型/工具调用次数、事件顺序和指标变化，然后运行对应测试核对。若修改了代码，重跑本目录全部测试；真实模型评估必须单独启用，不能以固定 Mock 测试替代。项目只演示已列明的攻击样本，不代表能防御任意 Prompt Injection。

## 七、完成标准

- 直接/间接注入和越权调用均有可复现样本；危险工具未执行，正常请求未被误拦截。
- 模型超时、工具失败、服务故障能被区分；响应、日志、Trace 与指标的证据相互一致。
- 审批拒绝没有工具执行事件；审批通过和实际执行分开记录。
- 能按关联 ID 还原单次请求，按指标判断故障范围，并说明无法仅凭某一种信号得出的结论。
- 恢复及容器重启后，按设计持久化的审计记录仍可查询；测试不泄露真实凭据或敏感内容。
