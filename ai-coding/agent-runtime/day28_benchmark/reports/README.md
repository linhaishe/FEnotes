# Day 28：故障演练与性能压测

## 学习目标

完成本日练习后，你应该能：

- 用可重复的方式模拟超时、限流、进程重启和工具失败；
- 区分成功率、QPS、P99 延迟和单任务成本；
- 从压测结果判断系统的主要瓶颈，而不是只看平均耗时；
- 记录故障假设、观测结果和下一步改进。

## 任务 1：先建立基线

运行：

```bash
python load_test.py --scenario tool_failure --tasks 100 --workers 8 --seed 1
```

记录输出中的 `success_rate`、`qps`、`p99_latency_ms` 和 `cost_per_task`。解释：QPS 是单位时间完成的任务数，P99 是最慢 1% 请求的边界，单任务成本是总成本除以任务数。

## 任务 2：逐个演练故障

依次运行：

```bash
python failure_scenarios.py timeout
python failure_scenarios.py rate_limit
python failure_scenarios.py process_restart
python failure_scenarios.py tool_failure
```

对每种故障回答：故障发生在哪里？用户看到什么？延迟和成本如何变化？系统应该重试、降级还是快速失败？

## 任务 3：比较并发度

对每个场景分别使用 `--workers 1`、`8`、`32`，保持任务数和随机种子不变。把四个指标填入表格，观察并发提升是否真的带来更高 QPS，以及 P99 是否恶化。

## 任务 4：写故障复盘

在报告中记录：

1. 实验假设；
2. 命令和参数；
3. 四项指标；
4. 发现的异常；
5. 一个最小改进方案；
6. 改进前后的指标差异。

## 指标口径

- 成功率 = 成功任务数 / 总任务数；
- QPS = 完成任务数 / 压测耗时（秒）；
- P99 = 按耗时排序后第 99 百分位的任务延迟；
- 单任务成本 = 所有任务成本之和 / 总任务数。

## 验收

```bash
python -m unittest test_benchmark.py
python load_test.py --scenario timeout --tasks 20 --workers 4 --seed 7
```

能解释四类故障对四项指标的影响，并指出“成功率高但 P99 或成本变差”的情况，即完成本日学习。

# 与ai agent 结合

可以把这套 benchmark 放在 AI Agent 的“任务执行层”外面，观察 Agent 在故障下是否能恢复、降级和控制成本。

一个典型结构是：

```text
用户任务
   ↓
Agent Loop
   ├── 思考 / 规划
   ├── 调用工具
   ├── 重试 / 降级 / 中断
   └── 输出结果
          ↓
   Benchmark Harness
   ├── 注入故障
   ├── 记录每次调用
   └── 计算指标
```

对应关系如下：

| Benchmark 内容 | Agent 中的对应位置 |
|---|---|
| 超时 | LLM 请求超时、工具执行超时、网络请求超时 |
| 限流 | 模型 API 429、工具服务并发上限 |
| 进程重启 | Agent worker 崩溃后恢复任务 |
| 工具失败 | 搜索、数据库、文件系统等工具返回错误 |
| 成功率 | Agent 是否最终完成任务 |
| QPS | 单位时间完成的 Agent 任务数 |
| P99 | 从任务开始到最终结果的长尾耗时 |
| 单任务成本 | LLM token 成本 + 工具调用成本 + 重试成本 |

例如，当前的 `run_scenario()` 可以从“直接模拟任务”改成包装 Agent：

```python
def run_agent_task(agent, task, scenario):
    started = time.perf_counter()
    cost = 0.0

    try:
        with fault_injection(scenario):
            result = agent.run(task)
        success = result.completed
        error = None
    except TimeoutError:
        success = False
        error = "timeout"
    except RateLimitError:
        success = False
        error = "rate_limit"
    except ToolError:
        success = False
        error = "tool_failure"

    return {
        "success": success,
        "latency_ms": (time.perf_counter() - started) * 1000,
        "cost": cost,
        "error": error,
    }
```

更适合 Agent 学习的任务不是简单“调用一次工具”，而是：

1. Agent 需要搜索资料并总结；
2. Agent 需要调用数据库完成查询；
3. Agent 需要调用多个工具完成一个订单；
4. Agent 需要从中断状态恢复任务。

然后观察它在不同故障下的行为：

- 超时后是否重试？
- 限流后是否退避，而不是疯狂重试？
- 工具失败后是否选择替代工具？
- 进程重启后是否丢失任务状态？
- 重试增加后，成功率提高了多少，成本和 P99 增加了多少？

最值得加入的是“Agent 决策指标”，例如：

```text
任务成功率
工具调用成功率
平均重试次数
最大重试次数
恢复成功率
重复调用次数
单任务 token 成本
单任务总成本
```

因此，当前 `day28_benchmark` 可以作为底层压测工具；下一步可以新增：

```text
agent-runtime/day28_benchmark/
├── agent_runner.py        # 调用真实 Agent
├── fault_injection.py     # 注入超时、限流、工具错误
├── load_test.py
├── metrics.py
├── failure_scenarios.py
└── reports/
```

核心思想是：不要只测 Agent “能不能回答”，而要测它在外部世界不可靠时，能否稳定完成任务，并且知道什么时候重试、降级或停止。
