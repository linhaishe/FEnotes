# Day 28：故障演练与性能压测

## 学习目标

完成本日练习后，你应该能：

- 用可重复的方式模拟超时、限流、进程重启和工具失败；
- 区分成功率、QPS、P99 延迟和单任务成本；
- 从压测结果判断系统的主要瓶颈，而不是只看平均耗时；
- 记录故障假设、观测结果和下一步改进。

```
day28_benchmark/
├── failure_scenarios.py  # 模拟四类故障
├── load_test.py          # 并发执行压测
├── metrics.py            # 计算成功率、QPS、P99、成本
├── test_benchmark.py     # 验证核心逻辑
└── README.md             # 学习任务和 Agent 结合方式
```

重点理解四个指标：

- 成功率：任务最终成功的比例
- QPS：每秒完成多少任务
- P99：最慢 1% 任务的延迟边界
- 单任务成本：平均完成一个任务花费多少资源

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

可以按下面的方式说明这 4 种故障：

### 1. `timeout`

```
python failure_scenarios.py timeout
```

- **故障发生在哪里？**
  调用外部服务时，服务迟迟没有返回，超过了设定的超时时间。
- **用户看到什么？**
  等待一段时间后看到“请求超时，请稍后重试”或类似错误。
- **延迟和成本如何变化？**
  代码把延迟设为 `250ms`，高于其他场景。延迟明显增加，因为系统一直等到超时；如果重试，还会增加总耗时和外部服务调用成本。
- **应该怎么处理？**
  可以有限重试，例如重试 1 次；如果仍然超时，就快速失败。不要无限重试。

------

### 2. `rate_limit`

```
python failure_scenarios.py rate_limit
```

- **故障发生在哪里？**
  Agent 请求外部服务过于频繁，被服务端限流，类似 HTTP `429 Too Many Requests`。

- **用户看到什么？**
  可能看到“请求过于频繁，请稍后再试”。

- **延迟和成本如何变化？**
  如果立即重试，可能继续被拒绝，增加延迟和请求次数；如果有退避等待，延迟会增加，但能减少无效请求。

  每次请求都会消耗配额，即使被拒绝也可能产生调用成本。立即重试会继续被限流，增加无效请求和延迟。

- **应该怎么处理？**
  根据服务返回的等待时间进行重试，并使用指数退避；超过次数后快速失败。不能连续立即重试。

------

### 3. `process_restart`

```
python failure_scenarios.py process_restart
```

- **故障发生在哪里？**
  Agent 所在进程崩溃、被系统杀死，或者服务实例发生重启。

- **用户看到什么？**
  正在进行的请求可能失败，用户看到“服务暂时不可用”；如果有自动恢复，短暂中断后可能恢复正常。

- **延迟和成本如何变化？**
  重启本身会造成一段不可用时间；重新初始化配置、连接数据库等也会增加延迟。未完成的请求可能需要重新执行，产生额外成本。

  进程重启会丢失内存状态，并需要重新建立连接、加载配置，导致请求失败或延迟增加。代码中将延迟设为 `180ms`、成本设为 `0.03`。

- **应该怎么处理？**
  对幂等请求可以重试；对支付、下单等操作不能盲目重试，否则可能重复执行。应先查询操作状态，必要时快速失败并保留恢复信息。

  对查询等幂等操作可以重试；对下单、支付等操作不能直接重试，应先查询操作是否已经成功，避免重复执行。无法确认状态时应快速失败并记录任务状态。

------

### 4. `tool_failure`

```
python failure_scenarios.py tool_failure
```

- **故障发生在哪里？**
  系统调用的工具或外部 API 执行失败，例如工具返回错误、参数不合法或服务内部异常。

  Agent 调用的工具执行失败，例如工具内部异常、返回错误结果或外部服务故障。

- **用户看到什么？**
  如果是核心功能，用户看到“操作失败，请稍后重试”；如果是非核心功能，主流程可能仍然成功，只是部分结果缺失。

- **延迟和成本如何变化？**
  重试会增加延迟和调用成本。如果错误是参数错误，重试相同请求没有意义，只会浪费资源。

  工具调用已经消耗了时间和资源。代码将延迟设为 `70ms`，成本设为 `0.015`。重试会继续增加调用次数和成本。

- **应该怎么处理？**
  判断错误类型：临时性错误可以有限重试；非核心工具可以降级；参数错误或确定性错误应快速失败并记录日志。

  如果是临时性错误，可以有限重试；如果是参数错误等确定性错误，应直接失败；如果工具属于非核心功能，则可以降级并继续主流程。“降级”就是：工具失败时，不让整个主流程一起失败，而是使用一个更简单的替代方案，或者跳过这个非核心步骤。

  > 常见降级方式包括：
  >
  > 返回空结果：推荐失败就返回空的推荐列表
  >
  > 使用默认值：个性化推荐失败时展示热门文章
  >
  > 使用缓存：工具失败时使用上一次成功的结果
  >
  > 使用简单逻辑：搜索工具失败时，改用本地关键词匹配
  >
  > 跳过非核心步骤：只完成总结，不生成推荐
  >
  > 返回部分结果：能完成的内容照常返回，并说明部分功能暂不可用

------

可以总结成：

| 故障              | 首选策略                                         |
| ----------------- | ------------------------------------------------ |
| `timeout`         | 有限重试，之后快速失败                           |
| `rate_limit`      | 退避等待后重试                                   |
| `process_restart` | 幂等请求重试，非幂等请求先确认状态               |
| `tool_failure`    | 临时错误重试，非核心功能降级，确定性错误快速失败 |

## 任务 3：比较并发度

进行压测

对每个场景分别使用 `--workers 1`、`8`、`32`，保持任务数和随机种子不变。把四个指标填入表格，观察并发提升是否真的带来更高 QPS，以及 P99 是否恶化。

在目录 `agent-runtime/day28_benchmark` 下运行。任务数和随机种子固定为 `100` 和 `1`，只改变 `--workers`：

```
cd agent-runtime/day28_benchmark
```

### `timeout`

```
python load_test.py --scenario timeout --tasks 100 --workers 1 --seed 1
python load_test.py --scenario timeout --tasks 100 --workers 8 --seed 1
python load_test.py --scenario timeout --tasks 100 --workers 32 --seed 1
```

### `rate_limit`

```
python load_test.py --scenario rate_limit --tasks 100 --workers 1 --seed 1
python load_test.py --scenario rate_limit --tasks 100 --workers 8 --seed 1
python load_test.py --scenario rate_limit --tasks 100 --workers 32 --seed 1
```

### `process_restart`

```
python load_test.py --scenario process_restart --tasks 100 --workers 1 --seed 1
python load_test.py --scenario process_restart --tasks 100 --workers 8 --seed 1
python load_test.py --scenario process_restart --tasks 100 --workers 32 --seed 1
```

### `tool_failure`

```
python load_test.py --scenario tool_failure --tasks 100 --workers 1 --seed 1
python load_test.py --scenario tool_failure --tasks 100 --workers 8 --seed 1
python load_test.py --scenario tool_failure --tasks 100 --workers 32 --seed 1
```

每次输出中记录这四个字段：

```
success_rate
qps
p99_latency_ms
cost_per_task
```

也可以用循环一次运行全部组合：

```
for scenario in timeout rate_limit process_restart tool_failure; do
  for workers in 1 8 32; do
    python load_test.py \
      --scenario "$scenario" \
      --tasks 100 \
      --workers "$workers" \
      --seed 1
  done
done
```

## 任务 4：写故障复盘

在报告中记录：

1. 实验假设；
2. 命令和参数；
3. 四项指标；
4. 发现的异常；
5. 一个最小改进方案；
6. 改进前后的指标差异。

### 本次实验记录（任务 3）

实验参数固定为 `--tasks 100 --seed 1`，仅改变 `--workers`。以下数据来自实际运行结果；QPS 保留两位小数。

| 场景 | workers | 成功率 | QPS | P99（ms） | 单任务成本 |
| --- | ---: | ---: | ---: | ---: | ---: |
| timeout | 1 | 0% | 59013.03 | 250 | 0.020 |
| timeout | 8 | 0% | 38339.27 | 250 | 0.020 |
| timeout | 32 | 0% | 29066.24 | 250 | 0.020 |
| rate_limit | 1 | 0% | 60072.11 | 40 | 0.010 |
| rate_limit | 8 | 0% | 40021.36 | 40 | 0.010 |
| rate_limit | 32 | 0% | 32586.56 | 40 | 0.010 |
| process_restart | 1 | 0% | 59142.41 | 180 | 0.030 |
| process_restart | 8 | 0% | 40731.12 | 180 | 0.030 |
| process_restart | 32 | 0% | 31614.31 | 180 | 0.030 |
| tool_failure | 1 | 0% | 54710.82 | 70 | 0.015 |
| tool_failure | 8 | 0% | 40892.82 | 70 | 0.015 |
| tool_failure | 32 | 0% | 33293.10 | 70 | 0.015 |

观察：并发从 1 提升到 8、32 并没有带来更高 QPS，反而整体下降；P99 没有随并发恶化，因为 `run_scenario` 只返回模拟延迟，没有真正等待。四种故障的成功率都是 0%，原因是当前实现把它们都定义为最终失败结果。

> QPS 是越高越好吗
>
> 通常来说，QPS 越高表示系统单位时间处理的任务越多，吞吐能力越强。
>
> 但不能只看 QPS，还要同时看：
>
> - **成功率**：QPS 高但大量请求失败，没有意义
> - **P99 延迟**：QPS 提高但用户等待时间变长，体验可能变差
> - **成本**：QPS 高但单任务成本明显增加，可能不划算
>
> 理想情况是：
>
> > 在成功率稳定、P99 可接受、成本没有明显增加的前提下，QPS 越高越好。
>
> 在你的实验中，`workers` 增大后 QPS 反而下降，而且所有任务成功率都是 `0%`，所以不能认为性能变好了。

### 本次实验复盘（任务 4）

1. **实验假设**：提高 worker 数可以提高吞吐；故障延迟较高或线程竞争加剧时，P99 可能恶化；故障处理不变时，成功率和单任务成本应保持不变。
2. **命令和参数**：对四个场景分别运行以下命令，仅把 `--workers` 替换为 `1`、`8`、`32`：

   ```bash
   python load_test.py --scenario <scenario> --tasks 100 --workers <workers> --seed 1
   ```

3. **四项指标**：完整数据见上表。成功率均为 `0%`；P99 分别由场景中写入的 `250ms`、`40ms`、`180ms`、`70ms` 决定；单任务成本分别为 `0.02`、`0.01`、`0.03`、`0.015`。
4. **发现的异常**：`workers` 增加后 QPS 下降。这不是业务服务吞吐下降，而是因为脚本没有真实等待，任务过于轻量，线程池调度开销占主导。另一个异常是所有场景都失败，因此不能仅凭当前结果评价恢复策略的效果。
5. **最小改进方案**：为每种错误增加最小恢复策略：`timeout` 最多重试一次；`rate_limit` 按退避时间重试；`process_restart` 对幂等任务重试、对非幂等任务先查询状态；`tool_failure` 对非核心工具返回缓存或空结果继续主流程。除此之外不改变压测参数和指标口径。
6. **改进前后的指标差异**：本次只运行了改进前基线，尚未修改恢复逻辑，因此没有可冒充为实测的“改进后”数字。按目标应重点观察：非核心 `tool_failure` 的成功率提高，重试策略会增加延迟和成本，降级策略则应减少 P99 和额外调用成本；实现改进后应使用同一组 12 条命令重新测量并补填对比表。

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



# QA

## 1. `argparse.ArgumentParser`

```
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("scenario", choices=SCENARIOS, help="要模拟的故障场景")
parser.add_argument(
    "--seed", type=int, default=1, help="随机种子；相同值用于复现实验（默认：1）"
)
args = parser.parse_args()
```

这段代码用于定义并解析命令行参数：

```
parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument(
    "scenario",
    choices=SCENARIOS,
    help="要模拟的故障场景",
)

parser.add_argument(
    "--seed",
    type=int,
    default=1,
    help="随机种子；相同值用于复现实验（默认：1）",
)

args = parser.parse_args()
```

含义：

- `scenario`：必填的位置参数，且值必须属于 `SCENARIOS`
- `--seed`：可选参数，必须是整数，默认值为 `1`
- `parse_args()`：读取命令行输入，并将结果保存到 `args`

例如：

```
python main.py network --seed 42
```

之后可以通过以下方式使用：

```
args.scenario  # "network"
args.seed      # 42
```

注意：你贴出的 `*description*`、`*choices*`、`*type*`、`*default*` 是 Markdown 斜体效果；Python 中应写成普通关键字参数 `description=`、`choices=` 等。

```
parser = argparse.ArgumentParser(description=__doc__)
```

作用是创建一个命令行参数解析器。

其中：

- `argparse.ArgumentParser(...)`：创建解析器对象
- `description=`：设置程序说明文字
- `__doc__`：当前 Python 文件的模块文档字符串

例如：

```
"""模拟各种故障场景的实验工具。"""

import argparse

parser = argparse.ArgumentParser(description=__doc__)
```

运行：

```
python main.py --help
```

会显示：

```
usage: main.py [-h]

模拟各种故障场景的实验工具。
```

如果文件顶部没有文档字符串，`__doc__` 通常是 `None`，帮助信息中就不会显示描述。
