"""SQLite database and the read-only tool used by the demo agent."""

import sqlite3

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


def query_database(db: sqlite3.Connection, sql: str) -> list[dict]:
    """Execute one bounded, read-only SELECT query."""
    statement = sql.strip().rstrip(";")  # 去掉 SQL 前后空格，并去掉末尾分号。
    if not statement.lower().startswith("select "):  # 只允许以 SELECT 开头的查询
        raise ValueError("only SELECT queries are allowed")
    if ";" in statement:  # 拒绝一条输入里包含多条 SQL
        raise ValueError("multiple SQL statements are not allowed")
    rows = db.execute(f"SELECT * FROM ({statement}) LIMIT 100").fetchall()
    return [dict(row) for row in rows]
