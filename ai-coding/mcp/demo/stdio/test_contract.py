"""Contract tests for the three stdio MCP tools."""

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
            assert {tool.name for tool in tools.tools} == {
                "weather",
                "query_database",
                "call_api",
            }

            weather = next(tool for tool in tools.tools if tool.name == "weather")
            assert weather.inputSchema["required"] == ["city"]
            assert weather.inputSchema["properties"]["city"]["type"] == "string"

            query = next(tool for tool in tools.tools if tool.name == "query_database")
            assert query.inputSchema["required"] == ["sql"]
            assert query.inputSchema["properties"]["sql"]["type"] == "string"

            api = next(tool for tool in tools.tools if tool.name == "call_api")
            assert api.inputSchema["required"] == ["url"]
            assert api.inputSchema["properties"]["url"]["type"] == "string"

            result = await session.call_tool("weather", {"city": "北京"})
            assert not result.isError
            assert result.content

            invalid = await session.call_tool("weather", {})
            assert invalid.isError

            rows = await session.call_tool(
                "query_database", {"sql": "SELECT id, name FROM users"}
            )
            assert not rows.isError
            assert rows.content

            response = await session.call_tool(
                "call_api",
                {
                    "url": "https://api.open-meteo.com/v1/forecast?latitude=39.9&longitude=116.4&current=temperature_2m"
                },
            )
            assert not response.isError
            assert response.content


if __name__ == "__main__":
    asyncio.run(run_contract())
