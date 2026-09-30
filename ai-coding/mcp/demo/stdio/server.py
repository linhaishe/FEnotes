"""MCP weather server over stdio."""

import sys
import json
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

"""
sys.path 不是一个固定目录，而是 Python 查找模块时使用的目录列表
把项目中的 demo 目录加入 Python 的模块搜索路径，方便导入
如果不insert的话，就只会查找当前文件stdio的目录
0 表示插入到列表第一个位置：
sys.path.insert(0, 新目录)
"""

sys.path.insert(0, str(Path(__file__).parents[1]))
sys.path.insert(0, str(Path(__file__).parents[1] / "sql-agent"))

from mcp.server.fastmcp import FastMCP
from shared.weather import get_weather
from database import create_database, query_database

"""
MCPServer 是 MCP Python SDK v2 提供的高层封装，用来快速创建 MCP Server。

FastMCP 帮你处理了底层细节：
JSON-RPC 消息
协议初始化
能力协商
tools/list
tools/call
参数 Schema
stdio / SSE 传输
"""

mcp = FastMCP("weather-stdio")

"""
@mcp.tool() 会自动完成：
- 注册工具名称 weather
- 读取参数 city: str
- 生成输入 Schema
- 保存函数说明
- 处理 MCP 的工具调用
"""
# 注册工具
@mcp.tool()
def weather(city: str) -> dict:
    """查询城市当前天气。"""
    return get_weather(city)


@mcp.tool(name="query_database")
def query_database_tool(sql: str) -> list[dict]:
    """执行只读 SQLite SELECT 查询。"""
    with create_database() as db:
        return query_database(db, sql)


@mcp.tool(name="call_api")
def call_api(url: str) -> dict | str:
    """调用一个 HTTP GET API，并返回 JSON 或文本响应。"""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("url must be an absolute http or https URL")

    request = Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "mcp-demo"},
    )
    with urlopen(request, timeout=10) as response:
        body = response.read().decode("utf-8")
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return body


if __name__ == "__main__":
    mcp.run(transport="stdio") # 启动 Server
