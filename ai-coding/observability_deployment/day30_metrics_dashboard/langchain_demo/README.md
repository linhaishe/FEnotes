# Day 30：LangChain Agent 指标大盘

这个 Demo 保留了原来的直接 HTTP 版本，单独展示使用 LangChain 调用 DeepSeek Agent。

## 运行

```bash
cd observability_deployment/day30_metrics_dashboard_langchain
pip install -r requirements.txt
cp ../day30_metrics_dashboard/.env .env
python demo.py
```

程序会通过 `ChatDeepSeek` 创建 LangChain Agent，并连续执行示例任务。

检查指标：

```bash
curl http://127.0.0.1:8000/metrics
```

## Token 与成本

Token 从 LangChain 返回消息的 `usage_metadata` 或 `response_metadata` 中读取：

```text
agent_tokens_total{type="input"}
agent_tokens_total{type="output"}
agent_cost_usd_total
```

成本默认使用环境变量中的单价估算：

```bash
DEEPSEEK_INPUT_COST_PER_TOKEN=0.00000028
DEEPSEEK_OUTPUT_COST_PER_TOKEN=0.00000110
```

任务延迟、成功率和失败数仍然通过 Prometheus 指标记录，可复用原 demo 的 Grafana Dashboard。
