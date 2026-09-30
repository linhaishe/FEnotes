"""SQLite database and the read-only tool used by the demo agent."""

import re
import sqlite3
import time

"""
:memory: 表示数据库只存在于内存中
不会生成数据库文件
程序结束后数据消失
适合 Demo 和测试

db.row_factory = sqlite3.Row
设置查询结果的行格式。

默认情况下:
rows = db.execute("SELECT id, name FROM users").fetchall()
print(rows)
[(1, "Alice")] # 只能通过下标访问 row[0]

设置 sqlite3.Row 后
db.row_factory = sqlite3.Row
row = db.execute("SELECT id, name FROM users").fetchone()

print(row["id"])
print(row["name"])

dict(row)
{
    "id": 1,
    "name": "Alice"
}

创建内存数据库 → 查询结果支持按列名访问 → 方便转换为 JSON / dict
"""


def create_database() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
        CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL);
        INSERT INTO users VALUES (1, 'Alice', 'Shanghai'), (2, 'Bob', 'Beijing');
        INSERT INTO orders VALUES (1, 1, 120.5), (2, 1, 80.0), (3, 2, 200.0);
        """)
    return db


ALLOWED_TABLES = {"users", "orders"}
FORBIDDEN_SQL = re.compile(r"\b(delete|update|drop|insert|alter|create|replace|attach|detach)\b", re.I)


def query_database(db: sqlite3.Connection, sql: str, timeout: float = 1.0) -> list[dict]:
    """Execute one bounded, read-only SELECT query."""
    statement = sql.strip().rstrip(";")  # 去掉 SQL 前后空格，并去掉末尾分号。
    if not statement.lower().startswith("select "):  # 只允许以 SELECT 开头的查询
        raise ValueError("only SELECT queries are allowed")
    if ";" in statement:  # 拒绝一条输入里包含多条 SQL
        raise ValueError("multiple SQL statements are not allowed")
    if FORBIDDEN_SQL.search(statement):
        raise ValueError("write operations are not allowed")
    tables = set(re.findall(r"\b(?:from|join)\s+([a-z_]\w*)", statement, re.I))
    unknown_tables = tables - ALLOWED_TABLES
    if unknown_tables:
        raise ValueError(f"table access is not allowed: {', '.join(sorted(unknown_tables))}")

    started = time.monotonic()

    def check_timeout() -> int:
        return int(time.monotonic() - started > timeout)

    db.set_progress_handler(check_timeout, 1000)
    try:
        rows = db.execute(f"SELECT * FROM ({statement}) LIMIT 100").fetchall()
        return [dict(row) for row in rows]
    except sqlite3.OperationalError as error:
        if "interrupted" in str(error).lower():
            raise TimeoutError(f"query exceeded {timeout} seconds") from error
        raise
    finally:
        db.set_progress_handler(None, 0)


def get_schema(db: sqlite3.Connection) -> list[dict]:
    """Return table and column metadata without reading business rows. 数据库结构"""
    tables = db.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    return [
        {
            "table": table["name"],
            "columns": [
                dict(column)
                for column in db.execute(f"PRAGMA table_info({table['name']})").fetchall()
            ],
        }
        for table in tables
    ]
