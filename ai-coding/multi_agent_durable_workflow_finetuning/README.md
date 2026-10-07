# 第 6 周：Multi-Agent、Durable Workflow 与 Fine-tuning

本周的主线是：先用评估判断任务需要多少自主性，再让长任务能够暂停与恢复；只有 Prompt、RAG 和 Agent Harness 都无法解决、且收益能在保留集上测量时，才考虑微调。不要为了使用 Multi-Agent 或 Fine-tuning 而增加系统复杂度。架构选型可从 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) 的 Workflow 与 Agent 区别入手。

## 学习目标

- 根据任务的可预测性、工具需求和并行性，在固定 Workflow、Single-Agent、Multi-Agent 之间选择最简单可靠的方案。
- 理解 Manager、Handoff、Agent-as-Tool 与并行子任务的责任边界，并用质量、延迟和成本评估拆分是否值得。
- 构建有持久化状态、任务队列、Checkpoint、人工审批和失败恢复的长任务工作流。
- 理解 Fine-tuning 的完整闭环：能力缺口定位、数据质量、训练、保留集评估、部署与回滚。
- 区分 SFT、LoRA/QLoRA 与 DPO、RFT/GRPO 的适用前提，不把训练当作所有问题的默认解法。

## 动手主线

1. **同题比较架构**：用相同任务和评估集实现确定性 Workflow、Single-Agent；只有基线不足且子任务可独立验证时，再试 Multi-Agent。记录最终质量、工具错误、延迟、Token 与成本。
2. **持久化工作流**：用 LangGraph 或一个 Agent SDK 实现“开始 → 等待审批 → 批准/拒绝 → 继续执行”的流程。持久化状态与 Checkpoint，并测试进程重启、重复投递和工具失败后的恢复。
3. **有条件地拆给 Subagents**：选一种 Manager/Handoff/Agent-as-Tool 模式，限制委派深度、并发和预算；只有保留集评估显示收益时才保留拆分。
4. **小模型微调实验**：针对结构化输出或工具调用准备去重的训练、验证、测试集；先记录未微调基线，再用 SFT + LoRA/QLoRA 训练，比较准确率、格式错误率、延迟和推理成本。验证集用于调参，测试集保留到最终对比。

## 每日学习计划

| 天数 | 主题 | 资源 | 当日目标与产物 |
| --- | --- | --- | --- |
| 36 | 架构选型 | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 对同一任务比较 Workflow、Single-Agent、Multi-Agent；写出选择依据和基线指标。 |
| 37 | Multi-Agent 实战 | [LangGraph Multi-agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)、[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | 实现 Manager、Handoff 或 Agent-as-Tool 中一种模式；限制深度、并发和预算，并与单 Agent 比较。 |
| 38 | Durable Workflow | [LangGraph Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) | 加入任务队列、持久化状态、审批节点和 Checkpoint；演练暂停、重启与失败恢复。 |
| 39 | Fine-tuning 决策与数据 | [OpenAI Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)、[Hugging Face Datasets](https://huggingface.co/docs/datasets/) | 用评估确认模型能力缺口；构建去重且隔离的训练/验证/测试集与工具调用轨迹。 |
| 40–41 | SFT 与 LoRA/QLoRA | [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)、[Unsloth](https://github.com/unslothai/unsloth)、[PEFT](https://huggingface.co/docs/peft/) | 微调小模型的结构化输出或工具调用能力；监控过拟合并在保留集上对比基线。 |
| 42 | 偏好/强化微调与部署 | [TRL](https://huggingface.co/docs/trl/)、[OpenAI Fine-tuning API](https://platform.openai.com/docs/api-reference/fine-tuning) | 理解 DPO、RFT/GRPO、Grader 与 Reward Hacking；设计模型版本、灰度发布和回滚。 |

## 完成标准

- 能解释为什么某个任务用固定 Workflow、Single-Agent 或 Multi-Agent，并用同一评估集支持结论。
- 审批前不执行高风险工具；批准、拒绝、重启和故障恢复都有可重复的测试。
- Subagents 的收益以质量、延迟、成本的对照结果说明，而不是仅凭更复杂的架构推断。
- 微调实验保留未微调基线和独立测试集；结果包含失败案例、过拟合检查与回滚方案。若评估没有明显收益，结论可以是“不微调”。

本目录目前只有学习计划，Day 36–42 的 Demo 按每日任务逐步新增。


**学习内容:**

- **架构选型**: 先判断固定 Workflow、Single-Agent 或 Multi-Agent 哪个最简单可靠
- **Multi-Agent 模式**: Manager、Handoff、Agent-as-Tool、并行子任务
- **Durable Workflow**: 状态机、任务队列、持久化、审批与恢复
- **Fine-tuning 决策**: Prompt/RAG/Harness 无法解决且评估可度量时再训练
- **训练方法**: SFT、LoRA/QLoRA；了解 DPO、RFT/GRPO 的适用边界

**手撕系列:**

- [ ] 用 LangGraph 或一个 Agent SDK 构建可暂停、审批和恢复的工作流
- [ ] 只在评估证明有收益时，将独立任务拆给 Subagents 并比较质量、延迟和成本
- [ ] 使用 SFT + LoRA/QLoRA 微调一个小模型的结构化输出或工具调用能力，并在保留集上对比基线

**解锁技能:**

- 能根据任务的可预测性和并行性选择 Workflow、Single-Agent 或 Multi-Agent
- 能构建有持久化状态、人工审批和失败恢复的长任务系统
- 理解数据质量、训练方法、评估、部署和回滚组成的 Fine-tuning 闭环
