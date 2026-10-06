"""真实 Agent 评估测试；默认跳过，显式开启后才调用 DeepSeek。"""

from __future__ import annotations

import os
import unittest

from real_agent_eval import RealEvalCase, evaluate_case


@unittest.skipUnless(
    os.getenv("RUN_REAL_AGENT_EVAL") == "1",
    "设置 RUN_REAL_AGENT_EVAL=1 才运行真实模型评估",
)
class RealAgentEvalTests(unittest.TestCase):
    """验证真实 Agent 的工具选择、参数和调用次数。"""

    def test_weather_request_uses_mock_tool(self) -> None:
        """天气请求应调用 Mock Tool 并传入上海。"""
        report = evaluate_case(
            RealEvalCase("查询天气: 上海", "mock_weather", "上海")
        )
        self.assertTrue(report["passed"], report)

    def test_general_question_does_not_use_tool(self) -> None:
        """普通问题不应调用天气工具。"""
        report = evaluate_case(RealEvalCase("什么是 Prometheus？", None, None))
        self.assertTrue(report["passed"], report)
