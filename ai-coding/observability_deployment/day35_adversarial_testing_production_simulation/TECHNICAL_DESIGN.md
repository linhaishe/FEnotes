# Day 35 技术设计：对抗演练与故障定位

状态：**待实现**。本文件是 [DEVELOPMENT.md](./DEVELOPMENT.md) 的实现契约，不代表 Day 35 已有 API、指标、报告或自动化测试。目标是在不改动 Day 29–34 现有 Demo 行为的前提下，先做离线回归，再用一个隔离的 Day 35 演练入口证明同次请求的 Trace、指标和日志能相互印证。

## 1. 边界和依赖

默认路径完全离线：固定样本、Mock Model、Mock Tool、临时目录中的审批文件，以及本地 Trace 上下文。真实 DeepSeek、远端 LangSmith、Docker 和 Redis 均不应成为默认单元测试的前置条件。容器/Redis 故障测试单独运行，只控制该测试创建的栈；不把 Day 33 的服务故障伪装成 Day 35 的同请求子 Trace。

Day 32 的 `check_input`、`check_external_content`、`validate_tool_call`、`check_output`、`ApprovalStore` 和 `AuditLog` 是安全与审计的来源；Day 34 的事件格式、请求 ID 和 Trace 传播方式是观测格式的参考。**不直接导入 Day 30 的全局 Counter，也不把 Day 33 独立进程的指标归到 Day 35 请求上。**这些 Demo 的 Prometheus registry、HTTP 请求和审批 ID 原本彼此独立。

## 2. 拟新增文件及职责

```text
day35_adversarial_testing_production_simulation/
├── README.md                 # 学习大纲，已有
├── DEVELOPMENT.md            # 开发范围与场景合同，已有
├── TECHNICAL_DESIGN.md       # 本文件
├── rehearsal.py              # 拟实现：单进程 Mock 演练入口和观测埋点
├── report_example.json        # 拟提供：仓库内保留的纯 Mock 演练报告样本
├── test_adversarial.py       # 拟实现：安全边界与审批回归
├── test_faults.py            # 拟实现：模型/工具故障与关联证据
└── test_service_failure.py   # 拟实现：显式触发的隔离容器演练
```

`rehearsal.py` 只组合已有的安全策略、Mock 调用和观测信号，不加入真实业务写操作。若实现时发现一个文件承载过多职责，再按实际测试需要拆分；不预建插件系统或通用故障平台。

## 3. 单请求处理契约

建议演练入口为 `POST /agent`，请求体仅包含 `prompt: str` 和可选 `external_content: str | None`。当前用户身份由服务端注入的可信测试上下文提供，不读取请求体、Prompt 或外部内容中的 `user_id` 作为授权依据；这仍是 Mock 身份，**不构成真实认证**。测试专用的故障模式通过依赖注入/替换 Mock 函数传入，不开放给外部 HTTP 请求选择。越权用例要尝试在不可信内容中伪造身份或资源归属，确认校验依据仍是可信上下文。

执行顺序固定：

1. 分配 HTTP `request_id`，创建根 Trace 并取 `trace_id`。响应头回传 `X-Request-ID` 和 `X-Trace-ID`。
2. 调用 Day 32 输入与外部内容检查。明确命中拒绝规则时不启动模型/工具；另设混合内容用例：可使用文档中的正常事实，但夹带的指令只能作为不可信数据，不能修改身份或工具权限。测试必须检查实际回答和工具执行结果，不能仅以整份文档被拒绝证明这一点。
3. 调用 Mock Model；若需工具，先执行 Day 32 参数/权限校验，再调用 Mock Tool。模型/工具各有独立计时和错误分类；模型提出的操作不能绕过服务端权限与审批策略。
4. 若请求删除，调用 `ApprovalStore.create()`，返回 `pending_approval` 和 `approval_id`；**不执行删除**。审批决定与执行由测试使用 Day 32 的 `decide()` / `execute_delete()` 驱动，拒绝后不得产生 `tool_executed`。待审批只是当前请求的结果，不代表工具已执行或任务最终成功；批准后的实际执行结果按审批 ID 单独验证。
5. 最终答案经 `check_output()` 处理后返回；响应结束时记录最终状态和耗时。任何失败都不把异常原文返回用户或写进日志。

建议将执行结果表达为 `status`（`success`、`blocked`、`pending_approval`、`error`）、`request_id`、`trace_id`、`answer`，审批场景再加 `approval_id`。具体 HTTP 状态可在实现时固定并测试：正常 200，待审批 202，安全拒绝 403，模型/工具依赖失败 503。不要把“模型建议执行”误报为“工具已执行”。

## 4. ID、事件和数据契约

| 字段 | 生成者 | 用途 | 约束 |
| --- | --- | --- | --- |
| `request_id` | Day 35 HTTP 入口 | 关联单次请求的响应、JSON 日志、根 Trace 元数据 | 每次请求唯一；不使用 Prompt 当 ID |
| `trace_id` | LangSmith 根 Trace | 关联根/子调用 | Mock 子步骤需显式创建 Trace；JSON 日志本身不是子 Trace |
| `approval_id` | Day 32 `ApprovalStore.create()` | 关联审批状态和审计 JSONL | 与 HTTP `request_id` 不同 |
| `case_id` | 测试样本 | 对照预期和实际 | 仅测试标识，不写入用户敏感内容 |

本阶段不实现持久化的 `request_id → approval_id` 查询映射。删除响应同时返回两个 ID；运行日志按 HTTP `request_id` 查，审批审计按 `approval_id` 查，演练报告并列记录两者。不能声称仅凭 HTTP ID 可跨重启查询完整审批链，也不能靠时间戳猜测两者的关系。

每条运行日志是单行 JSON，至少有 `timestamp`（UTC）、`level`、`event`、`request_id`、`trace_id`。允许增加 `duration_ms`、`status_code`、`error_type`、安全的工具名；禁止写完整 Prompt、外部内容、工具参数/结果、Key、PII 或异常消息。审计文件与运行日志分离，记录 `approval_requested`、`approval_approved` / `approval_rejected`、`tool_executed` 等实际状态变化，而非模型文本。

## 5. 故障注入接口与预期事件

通过测试替换可调用对象，而不是让用户请求包含 `fault=...`：

| 注入位置 | 测试输入/行为 | 预期处理 | 预期证据 |
| --- | --- | --- | --- |
| 输入 Guardrail | “忽略之前指令”等固定文本 | 拒绝；模型/工具调用 0 次 | `input_blocked`，无模型/工具子调用 |
| 外部内容 Guardrail | 文档中夹带提升权限指令 | 进入模型/工具前拒绝，不改变工具权限 | `external_content_blocked`，无危险工具执行 |
| 混合外部内容 | 文档同时包含正常事实和恶意指令 | 正常事实可用于回答；恶意指令不生效，工具权限与当前用户不变 | 正确回答、无越权工具执行；必要时记录安全的忽略/拦截类别 |
| 工具校验 | 非法金额、跨用户、缺少资源 ID | 执行前拒绝，副作用 0 次 | `tool_blocked`，无 `tool_executed` |
| Mock Model | 抛出 `TimeoutError` | 503；不调用工具 | `model_call_started → model_call_failed(timeout) → request_finished` |
| Mock Tool | 抛出受控异常 | 503；模型阶段仍成功 | `model_call_finished → tool_call_started → tool_call_failed(error)` |
| 审批决定 | `approved=False` | 状态为 rejected，不调用 `execute_delete` | `approval_requested → approval_rejected` |

异常只用于触发测试；原始异常消息可能含假凭据，不能被日志或响应原样序列化。模型超时只调用一次并返回 503，不做自动重试，以保留清晰的故障 Trace，也避免重复模型费用。对有副作用的工具同样不设计自动重试；如后续加入重试，必须先证明幂等性并单独测试执行次数。Day 33 Redis 的有限重试属于独立容器演练。

## 6. Trace、指标和日志如何同源

Day 35 演练入口应在**同一个进程和同一次请求**内更新自己的 Prometheus registry：`agent_tasks_total{status}`、`agent_task_failures_total{source}`、`agent_task_latency_seconds`，以及确有工具错误时的 `agent_tool_failures_total{tool,error}`。命名沿用 Day 30 的含义，但不要 import Day 30 的模块级 Counter，以免多个应用共享默认 registry 或产生重复注册。模型超时归 `source="model"`，工具失败归 `source="tool"`；安全拦截计为 `status="blocked"`，不增加模型/工具故障计数。待审批计为 `status="pending_approval"`，不算成功或失败；批准并实际执行后的结果按审批事件单独核对，不回填最初 HTTP 请求的成功数。

根 Trace 在请求入口创建；Mock 模型和工具步骤应在其实际执行点显式创建子 Trace，并将根上下文跨 FastAPI 异步任务传入。默认离线测试要验证根/子 Trace 的父子关系、`request_id` 与日志的对应关系，以及同次请求的指标增量；LangSmith 页面展示只作可选手动演练，不是 CI 前置条件。远端上传时需另行检查敏感输入输出隐藏策略。P95/P99 只有在足够多样本下才有统计意义，不能由一次故障请求推断。

定位顺序：从响应取得 `request_id` / `trace_id` → 按 ID 找 JSON 事件序列 → 查看同请求的 Trace 调用树 → 对比测试前后指标增量 → 若涉及审批，再用响应中的 `approval_id` 查独立审计文件。缺少 ID 或信号时，报告明确标记“无法关联”，不依靠时间戳猜测。

## 7. 测试分层与运行约定

**默认离线测试**：`python -m unittest discover -s observability_deployment/day35_adversarial_testing_production_simulation -p 'test_*.py' -v`。使用 `TemporaryDirectory` 保存审批/审计，`TestClient` 发送请求，`unittest.mock.patch` 注入故障，本地 Trace 禁止远端上传，指标使用独立 registry 或测试前后增量。每个测试检查具体行为和实际写入的事件，不只断言 Mock 被调用。

**容器故障演练**：`test_service_failure.py` 在默认 discovery 中通过 `DAY35_RUN_DOCKER` 开关跳过 Docker 测试；显式设置 `DAY35_RUN_DOCKER=1` 才运行。使用独有 Compose project name、临时测试数据和确定的容器目标；先记录健康状态，再只停止自己启动的 Redis，确认 Day 33 readiness 503 和有限重试，恢复后确认 200。Day 34 审计持久化属于另一项独立重启验证，不由该 Redis 测试证明：使用 Day 34 Compose 实际挂载的 `audit_state` Volume，重启其 API 容器后按审批 ID 重新读取事件；不得声称 Day 33 的 Redis Volume 就包含 Day 34 `audit.jsonl`。两项故障不强制挂到同一个 Day 35 `trace_id`。清理前确认项目/Volume 名称，绝不操作共享开发栈或使用宽泛删除命令。

**真实模型可选评估**：单独入口、显式 Key、费用可控；不要求模型生成文本完全一致，只断言安全边界和可观测字段。默认 CI 不运行。

**演练报告**：提供显式运行的报告生成命令，将脱敏 JSON 写到用户指定路径；文档示例使用系统临时目录。每个场景包含 `case_id`、判定结果、预期与实际事件序列、`request_id`、`trace_id`、模型/工具调用次数、指标增量及可安全公开的故障类别；审批场景再包含 `approval_id`。缺失证据要明确标记，不得写入 Prompt、外部内容、工具原始结果、Key、PII 或异常原文。仓库内另保留一份由固定 Mock 场景和假数据生成的 `report_example.json`，作为可读样本；**本 Demo 不为报告新增 `.gitignore` 规则，这是明确的例外**。日常运行不要求提交随机 ID 或时间戳的变更；测试验证报告结构、事件和数值关系，不逐字比较动态字段。更新仓库内样本前必须确认全为假数据。

## 8. 开发完成判定

- 正常、直接/间接注入、混合外部内容、越权、审批拒绝、模型超时、工具失败各有离线回归；危险工具没有副作用，正常请求及可用的外部事实未被误拦。
- HTTP 响应、同进程日志、Mock 子 Trace 和指标增量能按契约互证；审批场景并列记录两个 ID，不宣称存在跨 ID 查询映射。
- 错误分类、事件顺序、工具执行次数和最终 HTTP 状态符合场景表；运行日志与审计文件不包含假凭据、PII、完整 Prompt 或原始异常。
- 独立的容器演练分别显示 Redis 故障/恢复与审计存储重启后的可查询性；若未实际运行对应容器，只能报告配置或单元测试通过，不能宣称完成该项重启验证。
- 显式生成的脱敏 JSON 报告包含真实 Mock 演练证据，仓库内保留一份假数据样本；所有示例命令和报告只展示假数据，Day 29–34 现有测试不因本阶段改动回归。
