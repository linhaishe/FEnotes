"""Contract tests for the stdio weather MCP server."""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER = Path(__file__).with_name("server.py")


async def run_contract() -> None:
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            weather = next(tool for tool in tools.tools if tool.name == "weather")
            assert weather.inputSchema["required"] == ["city"]
            assert weather.inputSchema["properties"]["city"]["type"] == "string"

            result = await session.call_tool("weather", {"city": "北京"})
            assert not result.isError
            assert result.content

            invalid = await session.call_tool("weather", {})
            assert invalid.isError


if __name__ == "__main__":
    asyncio.run(run_contract())
