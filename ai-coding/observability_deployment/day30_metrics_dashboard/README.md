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

## 运行

安装依赖：

```bash
pip install prometheus-client
```

启动 Demo：

这个Demo 和 Prometheus ，Grafana 是要同时开启的

```bash
python demo.py
```

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

学习入口：

- [Prometheus Python Client](https://github.com/prometheus/client_python)
- [Grafana Getting Started](https://grafana.com/docs/grafana/latest/getting-started/)





















