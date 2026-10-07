# **第 5 周：监控、可观测性与部署**

> **学习内容:**
>
> - **Agent 链路追踪**: LangSmith, OpenTelemetry
> - **Agent Evals**: 最终结果、工具选择、参数、轨迹与回归评估
> - **安全与 Guardrails**: Prompt Injection、输入/输出/工具校验、最小权限
> - **Human-in-the-loop**: 高风险工具的暂停、审批、拒绝与恢复
> - **指标监控**: Prometheus 监控业务和系统指标
> - **可视化**: Grafana 创建监控大盘
> - **日志系统**: ELK Stack (Elasticsearch, Logstash, Kibana)
> - **容器化部署**: Docker, Docker Compose
>
> **手撕系列:**
>
> - [ ] 为 Agent 应用集成 LangSmith，追踪每一步的调用和延迟
> - [ ] 建立包含正常、边界和攻击样本的 Agent 回归集，并接入 CI
> - [ ] 为写操作和外部副作用加入审批，验证间接 Prompt Injection 不会越权调用工具
> - [ ] 使用 Prometheus 暴露自定义指标 (如 Token 消耗, 缓存命中率)
> - [ ] 使用 Docker Compose 将 FastAPI + Milvus + Redis 整套系统一键部署
>
> **解锁技能:**
>
> - 具备构建完整 LLM 应用可观测性体系的能力
> - 能够用可重复评估而不是单次 Demo 判断 Agent 是否变好
> - 能够控制 Agent 的权限和执行边界
> - 能够快速定位和诊断线上问题
> - 掌握基于 Docker 的容器化部署和编排
> - 拥有完整的 DevOps for LLM Apps 经验

**🌟 每日学习计划**

| **天数** | **学习主题**             | **资源链接**                                                 | **目标**                                                     |
| -------- | ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 29       | 链路追踪 (LangSmith)     | 文档: [LangSmith](https://docs.smith.langchain.com/)<br>替代: [OpenTelemetry](https://opentelemetry.io/docs/languages/python/), [LangFuse](https://langfuse.com/) | 将 LangSmith 集成到现有 Agent 应用中，分析调用链路 ✅         |
| 30       | 指标与大盘               | 教程: [Prometheus Python Client](https://github.com/prometheus/client_python), [Grafana Dashboard](https://grafana.com/docs/grafana/latest/getting-started/) | 监控 QPS、延迟、错误率、任务成功率、Token、成本和工具失败率 ✅ |
| 31       | Agent Evals 与测试       | 文档: [OpenAI Evals](https://platform.openai.com/docs/guides/evals)<br>参考: [OpenAI Agents SDK Testing](https://openai.github.io/openai-agents-python/testing/) | 评估最终结果、工具选择、参数和轨迹，建立 Mock Tool 回归测试 ✅ |
| 32       | 安全、Guardrails 与 HITL | 参考: [OpenAI Guardrails](https://openai.github.io/openai-agents-python/guardrails/), [Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) | 防御直接/间接 Prompt Injection，为高风险工具配置最小权限和人工审批  ✅ |
| 33       | 容器化与服务编排         | 教程: [Docker for FastAPI](https://fastapi.tiangolo.com/deployment/docker/), [Docker Compose](https://docs.docker.com/compose/) | 使用 Docker Compose 启动应用栈，并隔离运行时、网络与 Secrets ✅ |
| 34       | 结构化日志与审计         | 教程: [Python Logging](https://docs.python.org/3/howto/logging.html)<br>工具: [structlog](https://www.structlog.org/) | 输出 JSON 日志和审计事件，避免记录凭据、PII 与敏感上下文 ✅   |
| 35       | 对抗测试与生产环境模拟   |                                                              | 模拟 Prompt Injection、越权工具调用、超时和服务故障，使用 Trace 与指标定位问题 |

按 `observability_deployment` 当前代码与配置核对，**五项都已有相关 Demo，但还没有作为同一套系统全部完成**。本次是静态核对，未重新运行线上 CI 或一键部署。

| 目标 | 判断 | 已有证据与缺口 |
| --- | --- | --- |
| LangSmith 追踪 Agent 每一步及延迟 | 部分完成 | [Day 29](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day29_langsmith_tracing/demo.py:27) 有真实 LangChain Agent 与 LangSmith Trace；[Day 34](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day34_structured_logging_audit/demo.py:223) 可将真实 Agent 子调用接到请求根 Trace。但需启用真实模型和 LangSmith；尚未接入 Day 33 的容器应用。 |
| 正常、边界、攻击回归集并接入 CI | 部分完成 | [Day 31](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day31_agent_evals_testing/demo.py:104) 有这些样本，[CI 工作流](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/.github/workflows/day31-agent-evals.yml:3) 会运行 Day 31 测试。但工作流的路径过滤和命令都只覆盖 Day 31；Day 32、Day 35 的安全与故障回归尚未纳入该 CI。真实模型评估默认跳过。 |
| 写操作审批与间接注入防越权 | 部分完成 | [Day 32 删除工具](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day32_security_guardrails_hitl/langchain_secure_agent.py:98) 会先创建审批，[Day 35 测试](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day35_adversarial_testing_production_simulation/test_adversarial.py:52) 覆盖固定间接注入样本。但 [转账工具](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day32_security_guardrails_hitl/langchain_secure_agent.py:75) 参数合法时可直接返回 `transfer accepted`，没有审批；也不能把固定样本测试视为通用注入防护。 |
| Prometheus 自定义指标，包括 Token、缓存命中率 | 部分完成 | [Day 30 LangChain Demo](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day30_metrics_dashboard/langchain_demo/demo.py:17) 暴露任务、延迟、Token、成本等指标；[Day 33 API](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day33_containerization_service_orchestration/app/main.py:17) 只有任务数和 Redis 重试等指标。当前目录未找到缓存命中率指标，也未把 Day 30 的 Token 指标接进 Day 33 容器服务。 |
| Compose 一键部署 FastAPI + Milvus + Redis | 未完成 | [Day 33 Compose](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day33_containerization_service_orchestration/docker-compose.yml:1) 有 FastAPI、Redis、Prometheus、Grafana，**没有 Milvus**；其 [FastAPI 任务接口](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day33_containerization_service_orchestration/app/main.py:107) 主要把任务写入 Redis，并非把前几天的真实 Agent 组合部署。 |

最关键的差距不是缺少单项示例，而是**Day 29–35 仍是分开的 Demo**。若完成这五条作为一个整体目标，需要选定一个 FastAPI Agent 应用作为主线，把追踪、安全审批、评估、指标和 Milvus/Redis 部署接到同一条实际请求链上。

# Day 29-31：监控、可观测性与部署

本目录用于学习 AI Agent Runtime 的监控、可观测性与部署。

## Demo

- [day29_langsmith_tracing](./day29_langsmith_tracing/)：使用 LangChain Agent 调用工具，并在 LangSmith 中查看完整调用链路。
- [day30_metrics_dashboard](./day30_metrics_dashboard/)：使用 Prometheus 和 Grafana 监控 Agent Runtime 指标。
- [day30_metrics_dashboard_langchain](./day30_metrics_dashboard_langchain/)：使用 LangChain 调用 DeepSeek Agent 并采集 Token、延迟和成本指标。
- [day31_agent_evals_testing](./day31_agent_evals_testing/)：使用 Mock Tool 回归测试最终结果、工具选择、参数和执行轨迹。
- [day32_security_guardrails_hitl](./day32_security_guardrails_hitl/)：学习 Prompt Injection 防御、最小权限、Guardrails 与高风险工具人工审批。
- [day33_containerization_service_orchestration](./day33_containerization_service_orchestration/)：学习 Dockerfile、Docker Compose、网络隔离、Secrets 和 Agent 服务编排。
- [day34_structured_logging_audit](./day34_structured_logging_audit/)：学习 JSON 结构化日志、请求关联、敏感信息保护与高风险操作审计。
