# MCP Demo 集合

本项目用几个最小示例演示 MCP Server、工具调用和 SQL Agent：

| Demo | 目录 | 内容 |
| --- | --- | --- |
| 天气 MCP | `demo/stdio/`、`demo/sse/` | 同一个天气工具分别使用 stdio 和 SSE 传输 |
| LangChain Host | `demo/langchain_host.py` | 使用 LangChain Agent 连接 stdio MCP Server 并自动调用天气工具 |
| SQL Agent | `demo/sql-agent/` | 根据自然语言选择查询工具，生成 SQL 并返回严格 JSON Schema 结构化结果 |

## 环境准备（Miniconda3）

请先安装 [Miniconda3](https://docs.anaconda.com/miniconda/)，然后在项目根目录执行：

```bash
conda create -n mcp-demo python=3.11 -y
conda activate mcp-demo
python -m pip install -r requirements.txt
```

后续命令都在 `mcp-demo` 环境中运行。

## LangChain Host Demo

这个 Demo 用 LangChain Agent 模拟 Host：`MCPAdapter` 启动并连接 `demo/stdio/server.py`，发现 `weather` 工具，再由模型根据自然语言自动决定是否调用。

先设置 Gemini API Key：

```bash
export GEMINI_API_KEY="你的 Gemini API Key"
```

运行：

```bash
conda activate mcp-demo
python demo/langchain_host.py
```

程序会用 Rich 打印已发现的 MCP Tools，以及 Agent 的每一步更新。看到类似 `weather` 的 tool call，说明 LangChain 已经调用 MCP Server；最后一条消息是模型生成的自然语言答案。

调用链：

```text
LangChain Agent → MCPAdapter → stdio MCP Server → weather Tool → Open-Meteo
```

这个 Demo 使用 Gemini，需要真实的 Gemini API Key；只想手动调试 MCP 工具时，可以使用 MCP Inspector，不需要运行 LangChain Host。

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

天气业务在 `demo/shared/weather.py`，分别由两个 MCP Server 通过不同传输方式暴露。Server 使用 MCP Python SDK v2 的 `MCPServer` API。

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

## 天气 Demo 完整使用流程

### 方式一：使用 stdio 接入 Host

1. 激活环境并进入项目根目录：

   ```bash
   conda activate mcp-demo
   cd /Users/你的用户名/项目路径/mcp
   ```

2. 在 MCP Host 的配置文件中添加 Server：

   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": ["/绝对路径/mcp/demo/stdio/server.py"]
       }
     }
   }
   ```

3. 重启 Host。Host 会自动启动 `server.py`，并通过 `initialize` 与 Server 建立连接。
4. 在 Host 中提问：

   ```text
   查询北京当前天气
   ```

5. Host 发现并调用 `weather(city="北京")`，Server 再请求 Open-Meteo，最后把结果交给模型生成回答。

### 方式二：使用 SSE 接入 Host

1. 在终端启动 SSE Server：

   ```bash
   conda activate mcp-demo
   python demo/sse/server.py
   ```

2. 在支持远程 MCP Server 的 Host 中添加 SSE 地址：

   ```text
   http://localhost:8000/sse
   ```

3. 连接成功后，在 Host 中提问：

   ```text
   上海今天的天气怎么样？
   ```

4. Host Client 通过 `tools/list` 发现 `weather` 工具，再通过 `tools/call` 传入城市名称并获取结果。

完整调用链：

```text
用户提问
  → Host 调用模型
  → MCP Client 连接 Server
  → tools/call(weather, city)
  → Open-Meteo
  → 天气结果
  → 模型生成回答
```

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

# MCP 工作流

```
Host
  ↓
MCP Client
  ↓ initialize / capabilities
MCP Server
  ↓ tools/list
weather Tool
  ↓ tools/call
Open-Meteo API
```
- `initialize`：Client 和 Server 协商协议版本与能力
- `tools/list`：Client 查询 Server 有哪些工具
- `tools/call`：Client 请求执行某个工具
