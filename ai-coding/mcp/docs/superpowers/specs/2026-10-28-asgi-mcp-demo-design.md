# ASGI MCP Demo 设计

## 目标

新增一个不依赖 LangChain 或 Django 的最小示例，演示如何像参考项目的 `config/asgi.py` 一样，将 MCP HTTP 应用挂载到 ASGI 路由中。

## 范围

- `demo/asgi_mcp/server.py`：定义一个简单 MCP tool。
- `demo/asgi_mcp/asgi.py`：将 `/mcp` 路径交给 MCP 应用，将 `/health` 返回健康状态。
- `demo/asgi_mcp/README.md`：说明启动和调用方式。
- 复用现有 `mcp` 依赖；仅在确有需要时补充 ASGI/Uvicorn 运行依赖。

## 不做

- 不接入 LangChain、模型或 Django。
- 不修改现有 stdio/SSE demo。
- 不实现认证、数据库和生产级路由中间件。

## 方案

- 方案 A：新增独立 ASGI demo（采用）。职责清晰，最接近参考文件的路由挂载思想。
- 方案 B：改造现有 SSE demo。改动少，但会混合 MCP Server 定义与 ASGI 入口，示例边界不清晰。

## 验证标准

- `uvicorn demo.asgi_mcp.asgi:application` 可以启动。
- `GET /health` 返回健康状态。
- MCP 客户端可以通过 `/mcp` 发现并调用示例工具。
