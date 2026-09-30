"""LangChain Agent that can chain the three MCP tools."""

import asyncio
import os
from pathlib import Path

from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain_google_genai import ChatGoogleGenerativeAI


async def main() -> None:
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("请先设置 GEMINI_API_KEY")
    os.environ.setdefault("GOOGLE_API_KEY", os.environ["GEMINI_API_KEY"])

    server = Path(__file__).parent / "stdio" / "server.py"
    async with MCPAdapter(server) as adapter:
        tools = await adapter.list_tools()
        expected = {"weather", "query_database", "call_api"}
        actual = {tool.name for tool in tools}
        if actual != expected:
            raise RuntimeError(f"MCP tools mismatch: expected {expected}, got {actual}")

        agent = create_agent(
            ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0),
            tools,
            system_prompt=(
                "你是一个可以连续调用工具的助手。根据问题选择并调用需要的工具；"
                "如果前一个工具的结果能帮助下一个工具，请继续调用，不要提前结束。"
                "最后用中文总结所有工具结果。"
            ),
        )
        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            "查询北京当前天气，并查询数据库中北京的用户。"
                            "最后调用 API 获取 https://api.open-meteo.com/v1/forecast?"
                            "latitude=39.9&longitude=116.4&current=temperature_2m 的结果，"
                            "综合返回天气、用户和 API 信息。"
                        ),
                    }
                ]
            }
        )
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
