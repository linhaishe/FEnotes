# 天气 MCP Demo

天气业务在 `demo/shared/weather.py`，分别由两个 MCP Server 通过不同传输方式暴露。

## stdio

```bash
conda create -n mcp-demo python=3.11 -y
conda activate mcp-demo
python -m pip install -r requirements.txt
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
python -m pip install -r requirements.txt
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
