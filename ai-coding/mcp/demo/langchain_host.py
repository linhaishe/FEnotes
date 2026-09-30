"""LangChain Host that connects to the local weather MCP Server."""

import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path

from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain_google_genai import ChatGoogleGenerativeAI
from rich.console import Console
from rich.pretty import Pretty


console = Console()
load_dotenv()

async def main() -> None:
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("请先设置 GEMINI_API_KEY")
    os.environ.setdefault("GOOGLE_API_KEY", os.environ["GEMINI_API_KEY"])

    server = Path(__file__).parent / "stdio" / "server.py"
    async with MCPAdapter(server) as adapter:
        tools = await adapter.list_tools()
        console.print("[bold cyan]MCP tools:[/bold cyan]")
        for tool in tools:
            console.print(f"  - {tool.name}: {tool.description}")

        model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
        agent = create_agent(model, tools)
        request = {"messages": [{"role": "user", "content": "查询北京当前天气"}]}
        last_message = None
        async for update in agent.astream(request, stream_mode="updates"):
            console.print("[bold yellow]LangChain update:[/bold yellow]")
            console.print(Pretty(update))
            for state in update.values():
                if isinstance(state, dict) and state.get("messages"):
                    last_message = state["messages"][-1]

        if last_message is None:
            raise RuntimeError("Agent 没有返回结果")
        console.print("[bold green]Final answer:[/bold green]")
        console.print(last_message.content)


if __name__ == "__main__":
    asyncio.run(main())
