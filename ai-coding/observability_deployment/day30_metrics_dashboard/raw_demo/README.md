# Day 30：指标与大盘

这个 Demo 使用 Prometheus Python Client 暴露 Agent Runtime 指标，并提供 Grafana Dashboard。

## 指标

| 指标 | Prometheus 名称 | 类型 |
| --- | --- | --- |
| QPS | `agent_qps` | Gauge |
| 任务总数与错误数 | `agent_tasks_total{status}` | Counter |
| 延迟 | `agent_task_latency_seconds` | Histogram |
| 任务成功率 | `agent_task_success_rate` | Gauge |
| Token | `agent_tokens_total{type}` | Counter |
| 成本 | `agent_cost_usd_total` | Counter |
| 工具失败率 | `agent_tool_failures_total{tool,error}` | Counter |

`Counter, Gauge, Histogram, generate_latest`

```
TASKS = Counter("agent_tasks_total", "Total Agent tasks", ["status"])
TASK_LATENCY = Histogram(
    "agent_task_latency_seconds",
    "Agent task latency in seconds",
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5),
)
```

这些都是 `prometheus_client` 提供的指标工具：

```
from prometheus_client import Counter, Gauge, Histogram, generate_latest
```

- `Counter`：只增不减，适合累计值
  例如任务总数、Token 总量、累计成本。

```
TASKS = Counter("agent_tasks_total", "Total tasks")
TASKS.inc()
```

- `Gauge`：可增可减，表示当前状态
  例如当前 QPS、队列长度、成功率。

```
QPS = Gauge("agent_qps", "Current QPS")
QPS.set(1.5)
```

- `Histogram`：记录数值分布
  适合统计延迟，并计算 P95/P99。

```
TASK_LATENCY = Histogram("agent_task_latency_seconds", "Task latency")
TASK_LATENCY.observe(0.35)
```

- `generate_latest`：把当前所有指标转换成 Prometheus 可读取的文本格式。

```
payload = generate_latest()
```

在这个 Demo 中：

```
Counter   → 任务数、Token、成本、失败数
Gauge     → QPS、最近一次成功率
Histogram → Agent 任务延迟
generate_latest → 暴露 /metrics 接口
```

这些参数可以这样理解：

```
TASKS = Counter(
    "agent_tasks_total",
    "Total Agent tasks",
    ["status"],
)
```

- `agent_tasks_total`：Prometheus 指标名，Python Client 会自动转成 `_total`
- `"Total Agent tasks"`：指标说明
- `["status"]`：标签名，使用时需要传值：

```
TASKS.labels(status="success").inc()
TASKS.labels(status="error").inc()
```

最终会产生：

```
agent_tasks_total{status="success"}
agent_tasks_total{status="error"}
```

------

```
TASK_FAILURES = Counter(
    "agent_task_failures_total",
    "Agent task failures",
    ["source"],
)
```

记录任务失败来源：

```
TASK_FAILURES.labels(source="model").inc()
TASK_FAILURES.labels(source="tool").inc()
```

可以区分失败来自模型还是工具。

------

```
TASK_LATENCY = Histogram(
    "agent_task_latency_seconds",
    "Agent task latency in seconds",
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5),
)
```

记录任务延迟，单位是秒。

`buckets` 是延迟区间：

```
≤ 0.01 秒
≤ 0.05 秒
≤ 0.1 秒
≤ 0.25 秒
≤ 0.5 秒
≤ 1 秒
≤ 2 秒
≤ 5 秒
```

例如：

```
TASK_LATENCY.observe(0.35)
```

Prometheus 会把这次请求统计到 `≤ 0.5` 秒的桶中，用于计算 P95/P99。

------

```
TASK_SUCCESS = Gauge(
    "agent_task_success_rate",
    "Latest Agent task success rate",
)
```

记录最近一次任务是否成功：

```
TASK_SUCCESS.set(1.0)  # 成功
TASK_SUCCESS.set(0.0)  # 失败
```

注意：它表示“最近一次状态”，不是真正的历史成功率。历史成功率应该用：

```
sum(rate(agent_tasks_total{status="success"}[5m]))
/
sum(rate(agent_tasks_total[5m]))
```

------

```
TOKEN_USAGE = Counter(
    "agent_tokens_total",
    "Total model tokens",
    ["type"],
)
```

累计模型 Token：

```
TOKEN_USAGE.labels(type="input").inc(input_tokens)
TOKEN_USAGE.labels(type="output").inc(output_tokens)
```

最终可以区分：

```
agent_tokens_total{type="input"}
agent_tokens_total{type="output"}
```

------

```
TASK_COST = Counter(
    "agent_cost_usd_total",
    "Estimated Agent cost in USD",
)
```

累计任务成本，单位是美元：

```
TASK_COST.inc(cost)
```

例如查询最近一小时成本：

```
increase(agent_cost_usd_total[1h])
```

------

```
TOOL_FAILURES = Counter(
    "agent_tool_failures_total",
    "Tool failures",
    ["tool", "error"],
)
```

记录工具失败，并按工具名和错误类型区分：

```
TOOL_FAILURES.labels(
    tool="weather",
    error="timeout",
).inc()
```

对应指标：

```
agent_tool_failures_total{
  tool="weather",
  error="timeout"
}
```

------

```
QPS = Gauge(
    "agent_qps",
    "Observed tasks per second",
)
```

记录当前观测到的每秒任务数：

```
QPS.set(5 / elapsed_seconds)
```

不过生产环境更推荐直接通过任务 Counter 计算 QPS：

```
rate(agent_tasks_total[5m])
```

------

```
DEEPSEEK_URL = (
    os.getenv(
        "DEEPSEEK_BASE_URL",
        "https://api.deepseek.com",
    ).rstrip("/")
    + "/chat/completions"
)
```

DeepSeek API 地址。

- 如果设置了 `DEEPSEEK_BASE_URL`，使用自定义地址
- 否则使用官方地址
- `rstrip("/")` 用于去掉末尾 `/`，避免出现双斜杠
- 最终拼接出：

```
https://api.deepseek.com/chat/completions
```

------

```
DEEPSEEK_MODEL = os.getenv(
    "DEEPSEEK_MODEL",
    "deepseek-chat",
)
```

使用的模型名：

- 环境变量设置了 `DEEPSEEK_MODEL` 时使用它
- 否则默认使用 `deepseek-chat`

------

```
INPUT_COST_PER_TOKEN = float(
    os.getenv(
        "DEEPSEEK_INPUT_COST_PER_TOKEN",
        "0.00000028",
    )
)
```

输入 Token 单价，默认：

```
0.00000028 美元 / Token
```

也就是：

```
0.28 美元 / 百万 Token
```

------

```
OUTPUT_COST_PER_TOKEN = float(
    os.getenv(
        "DEEPSEEK_OUTPUT_COST_PER_TOKEN",
        "0.00000110",
    )
)
```

输出 Token 单价，默认：

```
0.00000110 美元 / Token
```

也就是：

```
1.10 美元 / 百万 Token
```

最终成本计算类似：

```
cost = (
    input_tokens * INPUT_COST_PER_TOKEN
    + output_tokens * OUTPUT_COST_PER_TOKEN
)
```

这些价格是估算参数，模型或 DeepSeek 价格变化后，应通过 `.env` 覆盖。

## 运行

安装依赖：

```bash
pip install -r requirements.txt
```

配置 DeepSeek API：

```bash
export DEEPSEEK_API_KEY="your-api-key"
```

成本默认按 `deepseek-chat` 的每 Token 价格估算；如价格变化，可通过环境变量覆盖：

```bash
export DEEPSEEK_INPUT_COST_PER_TOKEN="0.00000028"
export DEEPSEEK_OUTPUT_COST_PER_TOKEN="0.00000110"
```

启动 Demo：

这个Demo 和 Prometheus ，Grafana 是要同时开启的

```bash
python demo.py
```

Demo 会连续发送 5 个示例任务到 DeepSeek。API 调用失败会记录为
`agent_task_failures_total{source="model"}`，不会伪造工具失败数据。

检查指标：

```bash
curl http://127.0.0.1:8000/metrics
```

![image-20261006143643752](https://picgocloud.com/m/fe719158-38a2-4cb9-97a9-db6a8f8ccce6.png)

启动 Prometheus 和 Grafana：

```bash
docker compose up
```

打开：

- Prometheus：http://localhost:9090
- Grafana：http://localhost:3000

这个 Demo 使用 Grafana 默认账号：

```text
用户名：admin
密码：admin
```

首次登录后 Grafana 通常会要求你修改密码。

如果 `admin/admin` 不行，可以重置容器：

```bash
docker compose down -v
docker compose up
```

注意：`-v` 会删除 Grafana 容器保存的数据。

在 Grafana 中添加 Prometheus 数据源，地址填写：

```text
http://prometheus:9090
```

![image-20261006142601872](https://picgocloud.com/m/3ac01c48-3a00-4a85-94dd-534015f38d73.png)

然后导入 `grafana/dashboards/agent-runtime.json`。

![image-20261006142630741](https://picgocloud.com/m/d6353218-01d5-4f7b-85f7-e74bd7c82be1.png)

## 学习重点

- Counter 适合累计任务数、Token、成本和错误数；
- Histogram 适合计算 P95/P99 延迟；
- Gauge 适合当前 QPS 和最近成功率；
- 生产环境应从真实 Agent、模型和工具调用处埋点，而不是使用本 Demo 的随机数据。

# content

## 1. 先理解四类指标

重点掌握：

- `Counter`：只增不减，例如任务数、Token、成本、错误数
- `Gauge`：当前值，例如 QPS、当前成功率
- `Histogram`：分布数据，例如延迟，用于计算 P95/P99
- `labels`：按状态、工具、错误类型拆分指标

重点看：

[demo.py](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day30_metrics_dashboard/demo.py)

------

## 2. 运行 Demo，观察原始指标

```
cd observability_deployment/day30_metrics_dashboard
pip install prometheus-client
python demo.py
```

另开终端：

```
curl http://127.0.0.1:8000/metrics
```

重点搜索：

```
agent_tasks_total
agent_task_latency_seconds
agent_tokens_total
agent_cost_usd_total
agent_tool_failures_total
```

先理解 Prometheus 暴露出来的文本格式。

------

## 3. 启动 Prometheus 和 Grafana

```
docker compose up
```

访问：

```
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
```

在 Grafana 添加数据源：

```
http://prometheus:9090
```

然后导入：

[grafana/dashboards/agent-runtime.json](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day30_metrics_dashboard/grafana/dashboards/agent-runtime.json)

------

## 4. 学会写 PromQL

在 Prometheus 页面尝试：

```
agent_qps
rate(agent_tasks_total[1m])
histogram_quantile(
  0.95,
  sum(rate(agent_task_latency_seconds_bucket[1m])) by (le)
)
rate(agent_tokens_total[1m])
rate(agent_tool_failures_total[1m])
```

理解：

- `rate()`：计算 Counter 的增长速度
- `histogram_quantile()`：计算 P95/P99
- `sum by (...)`：按标签聚合
- `[1m]`：最近一分钟的数据窗口

![image-20261006143540280](https://picgocloud.com/m/5a5d6ff4-f96c-4d7b-8550-e317861a9717.png)

------

## 5. 修改 Demo，观察图表变化

可以依次尝试：

- 把失败率从 `0.15` 改成 `0.5`
- 把延迟范围从 `0.03–0.4` 改成 `0.5–2`
- 增加 Token 数量
- 增加不同工具名称
- 增加 `retry`、`model`、`scenario` 标签

每次只改一个变量，然后观察 Grafana 图表变化。

![image-20261006143727906](https://picgocloud.com/m/84c41cf0-d5cb-42b7-8c8b-c99cecff59c8.png)

------

## 6. 接入真实 Agent

下一步把：

```
run_task(rng)
```

替换成真实 Agent 调用，并在 Agent 入口和工具调用处埋点：

```
TASKS.labels(status="success").inc()
TASK_LATENCY.observe(latency_seconds)
TOKEN_USAGE.labels(type="input").inc(input_tokens)
TASK_COST.inc(cost)
```

最终你应该能回答：

- Agent 当前 QPS 是多少？
- P95/P99 延迟是多少？
- 失败主要来自模型还是工具？
- 每个任务消耗多少 Token？
- 每小时大约花费多少钱？
- 哪个工具失败率最高？



是的，但你现在列出的埋点还不足以直接回答全部问题。

| 问题                   | 是否能回答        | 还需要什么                                                   |
| ---------------------- | ----------------- | ------------------------------------------------------------ |
| Agent 当前 QPS         | 可以              | 用任务总数的 `rate()` 计算                                   |
| P95/P99 延迟           | 可以              | `TASK_LATENCY` 必须是 Histogram，并在任务结束时记录          |
| 失败来自模型还是工具   | 目前不完整        | 给失败指标增加 `source="model/tool"` 或分别埋点              |
| 每个任务消耗多少 Token | 可以做平均值/分布 | 记录 input/output token，最好用 Histogram，而不是只用 Counter |
| 每小时花费             | 可以              | `TASK_COST` 按任务记录成本，再用 `increase(...[1h])` 聚合    |
| 哪个工具失败率最高     | 目前不能          | 工具调用指标必须带 `tool` 和 `status` 标签                   |

建议至少补充这些指标：

```
TASKS.labels(status="success").inc()
TASKS.labels(status="failure", source="model").inc()
TASKS.labels(status="failure", source="tool").inc()

TASK_LATENCY.observe(latency_seconds)

TOKEN_USAGE.labels(type="input").inc(input_tokens)
TOKEN_USAGE.labels(type="output").inc(output_tokens)

TASK_COST.inc(cost)

TOOL_CALLS.labels(tool=tool_name, status="success").inc()
TOOL_CALLS.labels(tool=tool_name, status="failure").inc()
```

对应 Prometheus 查询大致是：

```
# QPS
rate(tasks_total[5m])

# P95 / P99
histogram_quantile(0.95, rate(task_latency_seconds_bucket[5m]))
histogram_quantile(0.99, rate(task_latency_seconds_bucket[5m]))

# 模型/工具失败占比
sum by (source) (rate(tasks_total{status="failure"}[5m]))

# 每小时成本
increase(task_cost_total[1h])

# 工具失败率
sum by (tool) (rate(tool_calls_total{status="failure"}[5m]))
/
sum by (tool) (rate(tool_calls_total[5m]))
```

所以，这一节的核心结论是：这些埋点可以支撑运营分析，但需要补齐“失败来源”和“工具名称”等维度，并确保延迟、Token、成本使用适合的 Prometheus 指标类型。注意不要把 `task_id` 这类高基数值放进 labels。

## `grafana/dashboards/agent-runtime.json`

[agent-runtime.json](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/observability_deployment/day30_metrics_dashboard/grafana/dashboards/agent-runtime.json) 是 Grafana Dashboard 配置文件。

它定义了：

- 显示哪些图表
- 每个图表使用什么 PromQL
- 图表标题、单位和布局
- 使用哪个 Prometheus 数据源

它本身不保存监控数据，只保存“如何展示数据”的配置。

当前 Dashboard 主要展示：

```text
agent_task_success_rate     最近一次任务成功状态
agent_task_latency_seconds  任务延迟和 P95
agent_tokens_total          Token 使用量
agent_tool_failures_total   工具失败次数
agent_cost_usd_total        任务成本
```

数据流大致是：

```text
LangChain / Agent
      ↓
Prometheus 指标
      ↓
prometheus.yml 抓取 /metrics
      ↓
Grafana
      ↓
agent-runtime.json 定义图表
```

导入这个 JSON 后，Grafana 就会自动创建对应的 Agent Runtime 监控面板。

# 学习入口

- [Prometheus Python Client](https://github.com/prometheus/client_python)
- [Grafana Getting Started](https://grafana.com/docs/grafana/latest/getting-started/)


















