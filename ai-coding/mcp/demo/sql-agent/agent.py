"""A tiny natural-language-to-SQL agent demo. 自然语言转sql"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from database import create_database, query_database
from jsonschema import validate

TOOL_CALL_SCHEMA = {
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
}

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


def to_sql(question: str) -> str:
    question = question.lower()
    match = re.search(
        r"金额大于\s*(\d+(?:\.\d+)?)", question
    )  # 从问题中提取“金额大于多少”的数字
    if match:
        return f"SELECT id, user_id, amount FROM orders WHERE amount > {match.group(1)}"
    city = re.search(r"查询(.+?)的用户", question)
    if city:
        city_name = {"上海": "Shanghai", "北京": "Beijing"}.get(city.group(1).strip())
        if city_name is None:
            raise ValueError(f"暂不支持查询城市: {city.group(1).strip()}")
        return f"SELECT id, name, city FROM users WHERE city = '{city_name}'"
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
    raise ValueError("暂时只支持查询用户、订单或金额大于某个数的订单")


def answer(question: str) -> dict:
    db = create_database()
    sql = to_sql(question)
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
    print(answer("查询金额大于100的订单"))


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
