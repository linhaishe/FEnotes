import asyncio
import importlib.util

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


def load_application():
    from demo.asgi_mcp.asgi import application

    return application


def request(path: str) -> httpx.Response:
    async def send_request() -> httpx.Response:
        transport = httpx.ASGITransport(app=load_application())
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            return await client.get(path)

    return asyncio.run(send_request())


def test_asgi_module_is_importable_without_starting_a_server():
    assert importlib.util.find_spec("demo.asgi_mcp.asgi") is not None
    assert load_application() is not None


def test_health_route_returns_ok():
    response = request("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unknown_path_returns_not_found():
    response = request("/unknown")

    assert response.status_code == 404


def test_mcp_server_exposes_greet_tool():
    from demo.asgi_mcp.server import mcp

    tools = asyncio.run(mcp.list_tools())

    assert [tool.name for tool in tools] == ["greet"]


def test_mcp_http_route_supports_tool_call():
    async def call_tool():
        from demo.asgi_mcp.asgi import mcp_application

        transport = httpx.ASGITransport(app=load_application())
        async with mcp_application.router.lifespan_context(mcp_application):
            async with httpx.AsyncClient(
                transport=transport,
                base_url="http://localhost:8000",
            ) as client:
                async with streamable_http_client(
                    "http://localhost:8000/mcp",
                    http_client=client,
                ) as (read, write, _):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        tools = await session.list_tools()
                        result = await session.call_tool("greet", {"name": "HTTP"})
                        return tools, result

    tools, result = asyncio.run(call_tool())

    assert [tool.name for tool in tools.tools] == ["greet"]
    assert result.content[0].text == "Hello, HTTP!"
