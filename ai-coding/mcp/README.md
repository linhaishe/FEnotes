# MCP Demo 集合

本项目用几个最小示例演示 MCP Server、工具调用和 SQL Agent：

| Demo | 目录 | 内容 |
| --- | --- | --- |
| 天气 MCP | `demo/stdio/`、`demo/sse/` | 同一个天气工具分别使用 stdio 和 SSE 传输 |
| SQL Agent | `demo/sql-agent/` | 根据自然语言选择查询工具，生成 SQL 并返回严格 JSON Schema 结构化结果 |

## 环境准备（Miniconda3）

请先安装 [Miniconda3](https://docs.anaconda.com/miniconda/)，然后在项目根目录执行：

```bash
conda create -n mcp-demo python=3.11 -y
conda activate mcp-demo
python -m pip install -r requirements.txt
```

后续命令都在 `mcp-demo` 环境中运行。

## SQL Agent Demo

SQL Agent 使用内存 SQLite 数据库，不依赖外部数据库或模型 API，适合先理解 Agent 的基本链路：

```text
自然语言问题 → Agent 生成 SQL → query_database Tool → SQLite → 结构化结果
```

运行：

```bash
conda activate mcp-demo
python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

它演示了工具选择、只读 SQL 校验、结果行数限制，以及使用 JSON Schema 校验工具参数和最终输出。详细说明见 [`demo/sql-agent/README.md`](demo/sql-agent/README.md)。

### JSON Schema 结构化输出

SQL Agent 不直接返回一段不确定格式的文本，而是要求输出符合固定 Schema：

```json
{
  "question": "查询金额大于100的订单",
  "sql": "SELECT id, user_id, amount FROM orders WHERE amount > 100",
  "rows": [
    {"id": 1, "user_id": 1, "amount": 120.5}
  ]
}
```

工具调用也必须符合 Schema：

```json
{
  "tool": "query_database",
  "arguments": {"sql": "SELECT id, name FROM users"}
}
```

Schema 会校验工具名称、必需参数、字段类型和额外字段；校验失败时拒绝执行或返回结果。这样调用方可以稳定地读取 `question`、`sql` 和 `rows`，而不是解析自然语言文本。

天气业务在 `demo/shared/weather.py`，分别由两个 MCP Server 通过不同传输方式暴露。

## stdio

```bash
conda activate mcp-demo
python demo/stdio/server.py
```

这是一个使用 `stdio` 的 MCP Server。接入 MCP Host 时，将启动命令配置为：

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["/绝对路径/demo/stdio/server.py"]
    }
  }
}
```

## SSE

适合独立运行、通过 HTTP 连接的 Server：

```bash
conda activate mcp-demo
python demo/sse/server.py
```

默认 SSE 地址通常为 `http://localhost:8000/sse`，具体以 MCP SDK 版本输出为准。

## Host、Client、Server 与能力协商

- **Host**：用户使用的 AI 应用，例如 Cursor 或 Claude Desktop；负责对话、模型调用和用户授权。
- **Client**：嵌在 Host 中、与一个 Server 一对一连接的 MCP 客户端；负责协议通信和能力隔离。
- **Server**：这里的 `stdio/server.py` 或 `sse/server.py`，负责暴露 `weather` 工具。

调用链是：`用户问题 → Host/模型 → Client → Server.weather → Client → Host/模型 → 答案`。

连接建立后，Client 与 Server 先发送 `initialize`：双方交换 MCP 协议版本和能力（capabilities）。Server 声明自己提供工具能力，随后 Client 用 `notifications/initialized` 确认完成初始化。

之后 Client 可以调用：

1. `tools/list`：发现 Server 提供的工具名称、描述和输入 JSON Schema。
2. `tools/call`：传入 `{"name": "weather", "arguments": {"city": "北京"}}` 执行工具。

能力协商不会把业务逻辑放进 Host；它只确定双方支持哪些协议特性。工具清单和参数约束由 Server 自己声明，Host/模型据此决定是否调用。

## 自检

```bash
python -m py_compile demo/shared/weather.py demo/stdio/server.py demo/sse/server.py
```
