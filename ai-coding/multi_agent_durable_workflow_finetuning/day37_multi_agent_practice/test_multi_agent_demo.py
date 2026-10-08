"""Task 3 离线测试：检查实际委派、最小上下文和只读工具边界。"""

import json
import unittest
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import patch

from demo import CASES, ORDERS, RULES
from multi_agent_demo import build_multi_agent, run_case
from runtime_limits import RuntimeLimits


class FakeChild:
    def __init__(self, tool, order_id="A100", rule_id="standard"):
        self.tool = tool
        self.inputs = []
        self.order_id = order_id
        self.rule_id = rule_id

    def invoke(self, payload):
        prompt = payload["messages"][0]["content"]
        self.inputs.append(prompt)
        argument = self.order_id if self.tool.name == "mock_order" else self.rule_id
        key = "order_id" if self.tool.name == "mock_order" else "rule_id"
        self.tool.invoke({key: argument})
        return {"messages": [SimpleNamespace(content="子任务完成")]}


class FakeManager:
    def __init__(self, tools, answer="A100 可退款：购买后 2 天，期限 7 天。",
                 order_id="A100", rule_id="standard"):
        self.tools = {tool.name: tool for tool in tools}
        self.results = []
        self.answer = answer
        self.order_id = order_id
        self.rule_id = rule_id

    def invoke(self, payload):
        self.results.append(self.tools["inspect_order"].invoke({"order_id": self.order_id}))
        self.results.append(self.tools["inspect_rules"].invoke({"rule_id": self.rule_id}))
        return {"messages": [SimpleNamespace(content=self.answer)]}


class MultiAgentTests(unittest.TestCase):
    def test_manager_delegates_to_isolated_read_only_agents(self):
        children = []

        def fake_create_agent(*, model, tools, system_prompt, middleware):
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
        def fake_create_agent(*, model, tools, system_prompt, middleware):
            return FakeChild(tools[0]) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[4], model=object())

        self.assertFalse(report["passed"])

    def test_equivalent_positive_wording_passes(self):
        def fake_create_agent(*, model, tools, system_prompt, middleware):
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

        def fake_create_agent(*, model, tools, system_prompt, middleware):
            return next(agents) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            manager, _ = build_multi_agent(model=object())
            with self.assertRaises(ValueError):
                manager.tools["inspect_order"].invoke({"order_id": "A100"})

    def test_delegation_limit_stops_case_before_second_subagent(self):
        def fake_create_agent(*, model, tools, system_prompt, middleware):
            return FakeChild(tools[0]) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[0], model=object(),
                              limits=RuntimeLimits(max_delegations=1))

        self.assertEqual(report["status"], "limit_exceeded")
        self.assertEqual(report["usage"]["stop_reason"], "delegation_limit")
        self.assertEqual([event["agent"] for event in report["trace"]
                          if event["event"] == "subagent_result"], ["order"])

    def test_child_timeout_reports_missing_evidence_without_false_success(self):
        class TimeoutChild:
            def invoke(self, payload):
                raise TimeoutError("secret details must not be printed")

        children = iter([TimeoutChild(), FakeChild(None)])

        def fake_create_agent(*, model, tools, system_prompt, middleware):
            return next(children) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[0], model=object())

        self.assertEqual(report["status"], "incomplete")
        self.assertFalse(report["passed"])
        self.assertEqual(report["missing_agents"], ["order", "rules"])
        self.assertEqual(report["failure_source"], "subagent")
        self.assertIn("缺少", report["answer"])
        self.assertNotIn("secret details", json.dumps(report, ensure_ascii=False))

    def test_read_only_tool_failure_is_classified_and_not_reported_as_success(self):
        def fake_create_agent(*, model, tools, system_prompt, middleware):
            return FakeChild(tools[0]) if len(tools) == 1 else FakeManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent), \
             patch("multi_agent_demo.mock_order") as failing_order:
            failing_order.invoke.side_effect = ConnectionError("private backend address")
            report = run_case(CASES[0], model=object())

        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["failure_source"], "tool")
        self.assertFalse(report["passed"])
        self.assertNotIn("private backend address", json.dumps(report, ensure_ascii=False))

    def test_manager_cannot_hide_failed_child_with_confident_answer(self):
        class TimeoutChild:
            def invoke(self, payload):
                raise TimeoutError("private model request")

        class SwallowingManager(FakeManager):
            def invoke(self, payload):
                try:
                    self.tools["inspect_order"].invoke({"order_id": "A100"})
                except TimeoutError:
                    pass
                self.tools["inspect_rules"].invoke({"rule_id": "standard"})
                return {"messages": [SimpleNamespace(content="A100 可退款。") ]}

        created = iter([TimeoutChild(), FakeChild(None)])

        def fake_create_agent(*, model, tools, system_prompt, middleware):
            if len(tools) == 1:
                child = next(created)
                if isinstance(child, FakeChild):
                    child.tool = tools[0]
                return child
            return SwallowingManager(tools)

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[0], model=object())

        self.assertEqual(report["status"], "incomplete")
        self.assertFalse(report["passed"])
        self.assertEqual(report["missing_agents"], ["order"])
        self.assertNotIn("可退款", report["answer"])

    def test_injected_rule_note_does_not_reach_manager_or_grant_write_tool(self):
        original_orders, original_rules = deepcopy(ORDERS), deepcopy(RULES)
        created = []

        def fake_create_agent(*, model, tools, system_prompt, middleware):
            created.append([tool.name for tool in tools])
            if len(tools) == 1:
                return FakeChild(tools[0], order_id="A104", rule_id="injected")
            manager = FakeManager(tools, answer="A104 可退款：购买后 2 天。",
                                  order_id="A104", rule_id="injected")
            created.append(manager)
            return manager

        with patch("multi_agent_demo.create_agent", side_effect=fake_create_agent):
            report = run_case(CASES[4], model=object())

        self.assertTrue(report["passed"])
        self.assertEqual(created[:3], [["mock_order"], ["mock_refund_rules"],
                                       ["inspect_order", "inspect_rules"]])
        self.assertNotIn("external_note", created[3].results[1])
        self.assertNotIn("忽略之前限制", json.dumps(report, ensure_ascii=False))
        self.assertEqual(ORDERS, original_orders)
        self.assertEqual(RULES, original_rules)


if __name__ == "__main__":
    unittest.main()
