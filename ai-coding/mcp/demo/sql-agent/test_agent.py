import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import agent
from agent import OUTPUT_SCHEMA, TOOL_CALL_SCHEMA, answer
from jsonschema import ValidationError, validate


class FakeSQLModel:
    def invoke(self, prompt):
        if "上海" in prompt:
            return agent.SQLPlan(sql="SELECT id, name, city FROM users WHERE city = 'Shanghai'")
        if "每个用户" in prompt:
            return agent.SQLPlan(
                sql="SELECT users.id, users.name, SUM(orders.amount) AS total_amount "
                "FROM users JOIN orders ON users.id = orders.user_id "
                "GROUP BY users.id, users.name"
            )
        return agent.SQLPlan(sql="SELECT id, user_id, amount FROM orders WHERE amount > 100")


agent.sql_model = FakeSQLModel()


def test_agent_queries_orders():
    result = answer("查询金额大于100的订单")
    assert result["sql"].startswith("SELECT")
    assert result["rows"] == [
        {"id": 1, "user_id": 1, "amount": 120.5},
        {"id": 3, "user_id": 2, "amount": 200.0},
    ]


def test_gemini_mode_uses_structured_model():
    result = answer("查询金额大于100的订单", mode="gemini")
    assert result["rows"][0]["amount"] == 120.5


def test_unknown_mode_is_rejected():
    try:
        answer("查询用户", mode="unknown")
    except ValueError:
        return
    raise AssertionError("unknown SQL mode must be rejected")


def test_agent_queries_users_by_city():
    result = answer("查询上海的用户")
    assert result["sql"] == "SELECT id, name, city FROM users WHERE city = 'Shanghai'"
    assert result["rows"] == [{"id": 1, "name": "Alice", "city": "Shanghai"}]


def test_agent_sums_orders_by_user():
    result = answer("查询每个用户的订单总金额")
    assert result["rows"] == [
        {"id": 1, "name": "Alice", "total_amount": 200.5},
        {"id": 2, "name": "Bob", "total_amount": 200.0},
    ]


def test_agent_gets_schema():
    result = answer("查看数据库结构")
    assert [table["table"] for table in result["rows"]] == ["orders", "users"]
    assert result["rows"][0]["columns"][0]["name"] == "id"


def test_schemas_reject_extra_fields():
    try:
        validate({"tool": "query_database", "arguments": {"sql": "SELECT 1", "limit": 1}}, TOOL_CALL_SCHEMA)
    except ValidationError:
        pass
    else:
        raise AssertionError("extra tool arguments must be rejected")

    try:
        validate({"question": "x", "sql": "SELECT 1", "rows": [], "debug": True}, OUTPUT_SCHEMA)
    except ValidationError:
        pass
    else:
        raise AssertionError("extra output fields must be rejected")


if __name__ == "__main__":
    test_agent_queries_orders()
    test_gemini_mode_uses_structured_model()
    test_unknown_mode_is_rejected()
    test_agent_queries_users_by_city()
    test_agent_sums_orders_by_user()
    test_agent_gets_schema()
    test_schemas_reject_extra_fields()
    print("ok")
