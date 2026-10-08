"""Task 1 的离线回归测试，不调用 DeepSeek。"""

import unittest
from types import SimpleNamespace

from demo import CASES, evaluate_case, mock_order, mock_refund_rules


class FakeAgent:
    def invoke(self, payload):
        return {
            "messages": [
                SimpleNamespace(
                    tool_calls=[{"name": "mock_order", "args": {"order_id": "A100"}}],
                    usage_metadata={"input_tokens": 100, "output_tokens": 20},
                ),
                SimpleNamespace(
                    tool_calls=[{"name": "mock_refund_rules", "args": {"rule_id": "standard"}}],
                    usage_metadata={"input_tokens": 80, "output_tokens": 30},
                ),
                SimpleNamespace(content="A100 可退款：购买后 2 天，在 7 天内。", tool_calls=[]),
            ]
        }


class TaskOneTests(unittest.TestCase):
    def test_fixed_cases_cover_required_boundaries(self):
        self.assertEqual(len(CASES), 5)
        self.assertEqual({case.case_id for case in CASES},
                         {"eligible", "expired", "missing_field", "conflicting_rules", "injection"})

    def test_read_only_tools_return_fixed_data(self):
        self.assertEqual(mock_order.invoke({"order_id": "A100"})["days_since_purchase"], 2)
        self.assertEqual(mock_refund_rules.invoke({"rule_id": "standard"})["refund_days"], 7)

    def test_report_collects_all_model_usage_and_tool_calls(self):
        report = evaluate_case(CASES[0], FakeAgent(), input_rate=0.000001,
                               output_rate=0.000002, model_id="deepseek-chat")
        self.assertTrue(report["passed"])
        self.assertEqual(report["order_id"], "A100")
        self.assertEqual(report["rule_id"], "standard")
        self.assertIn("订单 A100", report["prompt"])
        self.assertEqual(report["expected_result"], "A100 可退款：购买后 2 天，未超过 7 天退款期限。")
        self.assertEqual(report["model_id"], "deepseek-chat")
        self.assertEqual(report["allowed_tools"], [
            {"name": "mock_order", "permission": "read_only"},
            {"name": "mock_refund_rules", "permission": "read_only"},
        ])
        self.assertEqual(report["input_cost_per_token_usd"], 0.000001)
        self.assertEqual(report["output_cost_per_token_usd"], 0.000002)
        self.assertEqual(report["input_tokens"], 180)
        self.assertEqual(report["output_tokens"], 50)
        self.assertEqual(report["model_calls"], 2)
        self.assertEqual(report["tool_calls"], [
            {"name": "mock_order", "args": {"order_id": "A100"}},
            {"name": "mock_refund_rules", "args": {"rule_id": "standard"}},
        ])
        self.assertAlmostEqual(report["estimated_cost_usd"], 0.00028)
        self.assertGreaterEqual(report["duration_seconds"], 0)

    def test_agent_failure_is_recorded_not_silently_passed(self):
        class BrokenAgent:
            def invoke(self, payload):
                raise TimeoutError("model timeout")

        report = evaluate_case(CASES[0], BrokenAgent(), input_rate=0,
                               output_rate=0, model_id="deepseek-chat")
        self.assertFalse(report["passed"])
        self.assertEqual(report["error_type"], "TimeoutError")
        self.assertEqual(report["model_id"], "deepseek-chat")


if __name__ == "__main__":
    unittest.main()
