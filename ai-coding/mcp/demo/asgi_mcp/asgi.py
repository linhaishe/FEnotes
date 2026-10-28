import json

from .server import mcp

# MCP SDK 提供的方法，用来把 FastMCP Server 转成一个可挂载的 ASGI 应用。
# 让 MCP Server 可以通过 HTTP 接口被访问
mcp_application = mcp.streamable_http_app()


async def application(scope, receive, send):
    if scope["type"] != "http":
        await mcp_application(scope, receive, send)
        return

    path = scope.get("path", "")
    if path == "/health":
        body = json.dumps({"status": "ok"}).encode()
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    (b"content-type", b"application/json"),
                    (b"content-length", str(len(body)).encode()),
                ],
            }
        )
        await send({"type": "http.response.body", "body": body})
        return

    if path == "/mcp" or path.startswith("/mcp/"):
        await mcp_application(scope, receive, send)
        return

    body = b"Not Found"
    await send(
        {
            "type": "http.response.start",
            "status": 404,
            "headers": [(b"content-length", str(len(body)).encode())],
        }
    )
    await send({"type": "http.response.body", "body": body})
