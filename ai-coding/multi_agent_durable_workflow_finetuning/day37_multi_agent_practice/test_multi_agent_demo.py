"""Task 3 离线测试：检查实际委派、最小上下文和只读工具边界。"""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from demo import CASES
from multi_agent_demo import build_multi_agent, run_case


class FakeChild:
    def __init__(self, tool):
        self.tool = tool
        self.inputs = []

    def invoke(self, payload):
        prompt = payload["messages"][0]["content"]
        self.inputs.append(prompt)
        argument = "A100" if self.tool.name == "mock_order" else "standard"
        key = "order_id" if self.tool.name == "mock_order" else "rule_id"
        self.tool.invoke({key: argument})
        return {"messages": [SimpleNamespace(content="子任务完成")]}


class FakeManager:
    def __init__(self, tools, answer="A100 可退款：购买后 2 天，期限 7 天。"):
        self.tools = {tool.name: tool for tool in tools}
        self.results = []
        self.answer = answer

    def invoke(self, payload):
        self.results.append(self.tools["inspect_order"].invoke({"order_id": "A100"}))
        self.results.append(self.tools["inspect_rules"].invoke({"rule_id": "standard"}))
        return {"messages": [SimpleNamespace(content=self.answer)]}


class MultiAgentTests(unittest.TestCase):
    def test_manager_delegates_to_isolated_read_only_agents(self):
        children = []

        def fake_create_agent(*, model, tools, system_prompt):
            if len(children) < 2:
                child = FakeChild(tools[0])
                children.append(child)
                return child
            return FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[0], model=object())

        self.assertEqual(
            [child.tool.name for child in children], ["mock_order", "mock_refund_rules"]
        )
        self.assertEqual(
            children[0].inputs, ["读取订单 A100，并只依据工具结果提取事实。"]
        )
        self.assertEqual(
            children[1].inputs, ["读取规则 standard，并只依据工具结果提取条件。"]
        )
        self.assertTrue(report["passed"])
        self.assertEqual(
            [event["event"] for event in report["trace"]],
            [
                "manager_started",
                "delegation_started",
                "subagent_result",
                "delegation_started",
                "subagent_result",
                "final_answer",
            ],
        )
        facts = report["trace"][2]["result"]
        rules = report["trace"][4]["result"]
        self.assertEqual(facts["facts"]["days_since_purchase"], 2)
        self.assertEqual(facts["source"], "mock_order:A100")
        self.assertEqual(rules["rules"]["refund_days"], 7)
        self.assertEqual(rules["source"], "mock_refund_rules:standard")

    def test_other_case_cannot_pass_with_wrong_delegation_ids(self):
        def fake_create_agent(*, model, tools, system_prompt):
            return FakeChild(tools[0]) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[4], model=object())

        self.assertFalse(report["passed"])

    def test_equivalent_positive_wording_passes(self):
        def fake_create_agent(*, model, tools, system_prompt):
            return (
                FakeChild(tools[0])
                if len(tools) == 1
                else FakeManager(
                    tools, answer="订单 A100 可以退款，购买后 2 天，期限 7 天。"
                )
            )

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[0], model=object())

        self.assertTrue(report["passed"])

    def test_missing_subagent_tool_call_cannot_be_reported_as_success(self):
        class SkippingChild:
            def invoke(self, payload):
                return {"messages": [SimpleNamespace(content="已完成")]}

        agents = iter([SkippingChild(), SkippingChild()])

        def fake_create_agent(*, model, tools, system_prompt):
            return next(agents) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            manager, _ = build_multi_agent(model=object())
            with self.assertRaises(ValueError):
                manager.tools["inspect_order"].invoke({"order_id": "A100"})


if __name__ == "__main__":
    unittest.main()
