"""MCP weather server over SSE."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from mcp.server.fastmcp import FastMCP
from shared.weather import get_weather

mcp = FastMCP("weather-sse")


@mcp.tool()
def weather(city: str) -> dict:
    """查询城市当前天气。"""
    return get_weather(city)


if __name__ == "__main__":
    mcp.run(transport="sse")
