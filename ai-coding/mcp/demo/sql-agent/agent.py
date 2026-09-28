"""A tiny natural-language-to-SQL agent demo."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from database import create_database, query_database


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
    return {"question": question, "sql": sql, "rows": query_database(db, sql)}


if __name__ == "__main__":
    print(answer("查询金额大于100的订单"))
