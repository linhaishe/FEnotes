import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from agent import OUTPUT_SCHEMA, TOOL_CALL_SCHEMA, answer
from jsonschema import ValidationError, validate


def test_agent_queries_orders():
    result = answer("查询金额大于100的订单")
    assert result["sql"].startswith("SELECT")
    assert result["rows"] == [
        {"id": 1, "user_id": 1, "amount": 120.5},
        {"id": 3, "user_id": 2, "amount": 200.0},
    ]


def test_agent_queries_users_by_city():
    result = answer("查询上海的用户")
    assert result["sql"] == "SELECT id, name, city FROM users WHERE city = 'Shanghai'"
    assert result["rows"] == [{"id": 1, "name": "Alice", "city": "Shanghai"}]


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
    test_agent_queries_users_by_city()
    test_schemas_reject_extra_fields()
    print("ok")
