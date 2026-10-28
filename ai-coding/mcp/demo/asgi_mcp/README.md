# ASGI MCP Demo

这个示例参考 `config/asgi.py` 的路由思路，但不依赖 Django、LangChain 或模型 API。

```text
/mcp/*   → MCP Streamable HTTP 应用
/health  → 普通 ASGI 健康检查
其他路径 → 404
```

## 运行

在仓库根目录安装依赖：

```bash
python -m pip install -r requirements.txt
uvicorn demo.asgi_mcp.asgi:application --reload
```

检查健康状态：

```bash
curl http://127.0.0.1:8000/health
```

MCP endpoint 是：

```text
http://127.0.0.1:8000/mcp
```

也可以用 MCP Inspector 连接这个地址，查看并调用 `greet` 工具。

## 代码结构

- `server.py`：创建 `FastMCP` 实例并注册 `greet` 工具。
- `asgi.py`：把 `mcp.streamable_http_app()` 挂载到 `/mcp`，其他路径由这个 ASGI 应用处理。

这个示例只演示 ASGI 路由组合，不包含认证、数据库或生产环境中间件。

-----

Demo 里已经包含了这些能力。

不是普通的 REST 接口，而是使用 MCP 协议的接口，可以：
- 获取有哪些工具
- 调用指定工具
- 获取工具执行结果

对应关系是：

- 获取工具列表：MCP 客户端调用 `tools/list`
- 调用工具：调用 `greet`
- 获取执行结果：返回 `Hello, xxx!`

工具定义在：

[server.py](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/mcp/demo/asgi_mcp/server.py>)

```python
@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

MCP 接口挂载在：

[asgi.py](</Users/chenruo/Documents/GitHub/FEnotes/ai-coding/mcp/demo/asgi_mcp/asgi.py>)

```python
mcp_application = mcp.streamable_http_app()
```

这个 Demo 的测试已经验证了：

```text
发现工具：greet
调用工具：greet({"name": "HTTP"})
返回结果：Hello, HTTP!
```

这些 MCP 协议细节由 SDK 自动处理，不需要我们手动写 `/tools/list` 或 `/tools/call` 路由。
