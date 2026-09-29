"""A tiny natural-language-to-SQL agent demo."""

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
    match = re.search(r"金额大于\s*(\d+(?:\.\d+)?)", question)
    if match:
        return f"SELECT id, user_id, amount FROM orders WHERE amount > {match.group(1)}"
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
    result = {"question": question, "sql": sql, "rows": query_database(db, tool_call["arguments"]["sql"])}
    validate(result, OUTPUT_SCHEMA)
    return result


if __name__ == "__main__":
    print(answer("查询金额大于100的订单"))
