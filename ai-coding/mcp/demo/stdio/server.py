"""MCP weather server over stdio."""

import sys
from pathlib import Path

"""
sys.path 不是一个固定目录，而是 Python 查找模块时使用的目录列表
把项目中的 demo 目录加入 Python 的模块搜索路径，方便导入
如果不insert的话，就只会查找当前文件stdio的目录
0 表示插入到列表第一个位置：
sys.path.insert(0, 新目录)
"""

sys.path.insert(0, str(Path(__file__).parents[1]))

from mcp.server import MCPServer
from shared.weather import get_weather

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

mcp = MCPServer("weather-stdio")

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


if __name__ == "__main__":
    mcp.run(transport="stdio") # 启动 Server
