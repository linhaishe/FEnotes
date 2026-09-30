"""A tiny natural-language-to-SQL agent demo. 自然语言转sql"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from database import create_database, get_schema, query_database
from jsonschema import validate
try:
    from pydantic import BaseModel, Field
except ModuleNotFoundError:  # Keep the offline SQL tests runnable without LangChain deps.
    class SQLPlan:
        def __init__(self, sql: str):
            self.sql = sql

    BaseModel = None
    Field = None

"""
oneOf：必须匹配且只能匹配一个
anyOf：匹配一个或多个即可
allOf：必须同时匹配所有
"""

TOOL_CALL_SCHEMA = {
    "type": "object",
    "oneOf": [ # 输入数据必须严格符合其中一个 Schema，而且只能符合一个。
        {
            "type": "object",
            "properties": {
                "tool": {"const": "query_database"},
                "arguments": {
                    "type": "object",
                    "properties": {"sql": {"type": "string", "minLength": 1}},
                    "required": ["sql"],
                    "additionalProperties": False,
                },
            },
            "required": ["tool", "arguments"],
            "additionalProperties": False,
        },
        {
            "type": "object",
            "properties": {
                "tool": {"const": "get_schema"}, # tool 字段必须等于 "get_schema"
                "arguments": {"type": "object", "maxProperties": 0, "additionalProperties": False},
            },
            "required": ["tool", "arguments"], # 表示这个 JSON 对象必须包含两个字段
            "additionalProperties": False,
        },
    ],
}

"""
const 和 enum 的区别：
{"const": "get_schema"}
只允许一个值。
{"enum": ["get_schema", "query_database"]}
允许多个值。
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "question": {"type": "string", "minLength": 1},
        "sql": {"type": "string", "minLength": 1},
        "rows": {"type": "array", "maxItems": 100, "items": {"type": "object"}},
    },
    "required": ["question", "sql", "rows"],
    "additionalProperties": False,
}


if BaseModel is not None:
    class SQLPlan(BaseModel):
        sql: str = Field(description="A single read-only SELECT SQL query")


sql_model = None


def _get_sql_model():
    global sql_model
    if sql_model is None:
        from langchain_google_genai import ChatGoogleGenerativeAI

        if not os.getenv("GEMINI_API_KEY"):
            raise RuntimeError("请先设置 GEMINI_API_KEY")
        os.environ.setdefault("GOOGLE_API_KEY", os.environ["GEMINI_API_KEY"])
        sql_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", temperature=0
        ).with_structured_output(SQLPlan)
    return sql_model


def to_sql_rules(question: str) -> str:
    question = question.lower()
    if "金额大于100" in question:
        return "SELECT id, user_id, amount FROM orders WHERE amount > 100"
    if "查询上海的用户" in question:
        return "SELECT id, name, city FROM users WHERE city = 'Shanghai'"
    if "查询北京的用户" in question:
        return "SELECT id, name, city FROM users WHERE city = 'Beijing'"
    if "每个用户" in question and "总金额" in question:
        return (
            "SELECT users.id, users.name, SUM(orders.amount) AS total_amount "
            "FROM users JOIN orders ON users.id = orders.user_id "
            "GROUP BY users.id, users.name"
        )
    if "用户" in question or "user" in question:
        return "SELECT id, name, city FROM users"
    if "订单" in question or "order" in question:
        return "SELECT id, user_id, amount FROM orders"
    raise ValueError("规则版暂不支持这个问题")


def to_sql_gemini(question: str) -> str:
    prompt = f"""
你是一个只读 SQL 生成器。根据用户问题生成一条 SQLite SELECT 查询。

数据库结构：
- users(id INTEGER, name TEXT, city TEXT)
- orders(id INTEGER, user_id INTEGER, amount REAL)

要求：只能生成单条 SELECT；禁止 INSERT、UPDATE、DELETE、DROP；只能使用上述表和字段。
用户问题：{question}
"""
    return _get_sql_model().invoke(prompt).sql


def to_sql(question: str, mode: str = "rules") -> str:
    if mode == "rules":
        return to_sql_rules(question)
    if mode == "gemini":
        return to_sql_gemini(question)
    raise ValueError(f"unknown SQL mode: {mode}")


def answer(question: str, mode: str = "rules") -> dict:
    db = create_database()
    if "结构" in question or "schema" in question.lower(): # 查看数据库结构 belike 规则匹配，不是真正的 LLM 工具选择。真正接入模型后，可以让模型根据工具描述自动决定调用 get_schema 还是 query_database
        tool_call = {"tool": "get_schema", "arguments": {}}
        validate(tool_call, TOOL_CALL_SCHEMA)
        rows = get_schema(db)
        result = {"question": question, "sql": "get_schema", "rows": rows}
        validate(result, OUTPUT_SCHEMA)
        return result

    sql = to_sql(question, mode)
    tool_call = {"tool": "query_database", "arguments": {"sql": sql}}
    validate(tool_call, TOOL_CALL_SCHEMA)
    result = {
        "question": question,
        "sql": sql,
        "rows": query_database(
            db, tool_call["arguments"]["sql"]
        ),  # 普通的 Python 函数调用
    }
    validate(result, OUTPUT_SCHEMA)
    return result


if __name__ == "__main__":
    print(answer("查询金额大于100的订单", os.getenv("SQL_AGENT_MODE", "rules")))


"""
自然语言问题
  ↓
to_sql()
  ↓
生成工具调用
  ↓
JSON Schema 校验
  ↓
query_database()
  ↓
结构化结果


```
sql = to_sql(question)
tool_call = {
    "tool": "query_database",
    "arguments": {"sql": sql},
}
validate(tool_call, TOOL_CALL_SCHEMA)
result = query_database(db, sql)
validate(result, OUTPUT_SCHEMA)
```
"""
