import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from agent import answer


def test_agent_queries_orders():
    result = answer("查询金额大于100的订单")
    assert result["sql"].startswith("SELECT")
    assert result["rows"] == [
        {"id": 1, "user_id": 1, "amount": 120.5},
        {"id": 3, "user_id": 2, "amount": 200.0},
    ]


if __name__ == "__main__":
    test_agent_queries_orders()
    print("ok")
