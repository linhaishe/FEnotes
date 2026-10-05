"""验证核心逻辑"""

import unittest

from metrics import calculate_metrics
from failure_scenarios import run_scenario


class BenchmarkTests(unittest.TestCase):
    """验证学习示例最重要的输出契约。"""

    def test_metrics_include_success_rate_qps_p99_and_cost(self):
        # 使用固定数据，直接检查四个学习目标指标的计算口径。
        result = calculate_metrics(
            [
                {"success": True, "latency_ms": 10, "cost": 0.02},
                {"success": True, "latency_ms": 20, "cost": 0.04},
                {"success": False, "latency_ms": 100, "cost": 0.01},
            ],
            elapsed_seconds=0.5,
        )

        self.assertEqual(result["success_rate"], 2 / 3)
        self.assertEqual(result["qps"], 6.0)
        self.assertEqual(result["p99_latency_ms"], 100)
        self.assertEqual(result["cost_per_task"], 0.07 / 3)

    def test_each_failure_scenario_returns_observable_result(self):
        # 每种故障都必须返回相同字段，压测器才能统一汇总。
        for scenario in ("timeout", "rate_limit", "process_restart", "tool_failure"):
            result = run_scenario(scenario, seed=7)
            self.assertIn("success", result)
            self.assertIn("latency_ms", result)
            self.assertIn("cost", result)
            self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
