"""Gemini + LangChain Function Calling with a strict tool schema."""

import asyncio
import os
import sys
from pathlib import Path

from langchain.agents import create_agent
from langchain_core.tools import StructuredTool
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, ConfigDict, Field

sys.path.insert(0, str(Path(__file__).parents[1] / "sql-agent"))
from database import create_database, query_database


class QueryArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    sql: str = Field(description="A single read-only SELECT query")


def run_query(args: QueryArgs) -> list[dict]:
    return query_database(create_database(), args.sql)


# 把普通 Python 函数包装成 LangChain Tool，供 Gemini 进行 Function Calling
query_tool = StructuredTool.from_function(
    func=run_query,  # 指定实际执行的 Python 函数
    name="query_database",
    description="Execute one read-only SQL SELECT query against the demo database.",
    args_schema=QueryArgs,  # 把 QueryArgs 这个模型当作工具参数定义。LangChain 会读取这个类的字段、类型和描述，并转换成 JSON Schema。
)

"""
args_schema=QueryArgs

{
  "type": "object",
  "properties": {
    "sql": {
      "type": "string",
      "description": "A single read-only SELECT query"
    }
  },
  "required": ["sql"],
  "additionalProperties": false
}
"""


async def main() -> None:
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("请先设置 GEMINI_API_KEY")
    os.environ.setdefault("GOOGLE_API_KEY", os.environ["GEMINI_API_KEY"])

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    agent = create_agent(model, [query_tool])
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "查询金额大于100的订单"}]}
    )

    for message in result["messages"]:
        if getattr(message, "tool_calls", None):
            print("Function Calling:", message.tool_calls)
    print("Answer:", result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
