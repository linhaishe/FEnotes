"""SQLite database and the read-only tool used by the demo agent."""

import sqlite3


def create_database() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
        CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL);
        INSERT INTO users VALUES (1, 'Alice', 'Shanghai'), (2, 'Bob', 'Beijing');
        INSERT INTO orders VALUES (1, 1, 120.5), (2, 1, 80.0), (3, 2, 200.0);
        """
    )
    return db


def query_database(db: sqlite3.Connection, sql: str) -> list[dict]:
    """Execute one bounded, read-only SELECT query."""
    statement = sql.strip().rstrip(";")
    if not statement.lower().startswith("select "):
        raise ValueError("only SELECT queries are allowed")
    if ";" in statement:
        raise ValueError("multiple SQL statements are not allowed")
    rows = db.execute(f"SELECT * FROM ({statement}) LIMIT 100").fetchall()
    return [dict(row) for row in rows]
