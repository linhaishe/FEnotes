"""第一阶段 Demo：使用 Mock Tool 和 unittest 测试 Agent 流程。"""

from __future__ import annotations

import unittest
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Trace:
    """记录一次 Agent 运行中的工具调用轨迹。"""

    tool_calls: list[dict[str, Any]] = field(default_factory=list)


class MockWeatherTool:
    """不访问网络、始终返回固定结果的天气工具。"""

    def __init__(self, trace: Trace) -> None:
        """初始化工具。

        Args:
            trace: 用于记录工具名称和参数的轨迹对象。
        """
        self.trace = trace

    def invoke(self, city: str) -> str:
        """查询固定天气，并把调用写入轨迹。

        Args:
            city: 要查询的城市名。

        Returns:
            固定的天气结果。
        """
        self.trace.tool_calls.append({"tool": "weather", "args": {"city": city}})
        return {"上海": "sunny", "北京": "cloudy"}.get(city, "unknown")


class DemoAgent:
    """一个可预测的 Agent，用来学习如何编写流程测试。"""

    def __init__(self, weather_tool: MockWeatherTool) -> None:
        """初始化 Agent。

        Args:
            weather_tool: Agent 可以调用的 Mock 天气工具。
        """
        self.weather_tool = weather_tool

    def invoke(self, prompt: str) -> str:
        """根据输入决定是否调用工具，并返回最终答案。

        Args:
            prompt: 用户输入，例如 ``查询天气: 上海``。

        Returns:
            Agent 最终生成的答案。
        """
        if prompt.startswith("查询天气:"):
            city = prompt.split(":", 1)[1].strip()
            weather = self.weather_tool.invoke(city)
            return f"{city} weather: {weather}"
        return "I can answer without using a tool."


@dataclass(frozen=True)
class EvalCase:
    """描述一个输入和期望行为。"""

    prompt: str
    expected_answer: str
    expected_tool: str | None
    expected_args: dict[str, Any]


def run_case(case: EvalCase) -> tuple[str, Trace]:
    """运行一个 Mock Agent case。

    Args:
        case: 包含输入、答案、工具和参数期望值的测试用例。

    Returns:
        Agent 最终答案和本次运行轨迹。
    """
    trace = Trace()
    agent = DemoAgent(MockWeatherTool(trace))
    return agent.invoke(case.prompt), trace


class AgentEvalTests(unittest.TestCase):
    """第一阶段的四类基本断言。"""

    def test_final_answer(self) -> None:
        """验证 Agent 的最终答案。"""
        answer, _ = run_case(
            EvalCase(
                "查询天气: 上海", "上海 weather: sunny", "weather", {"city": "上海"}
            )
        )
        self.assertEqual(answer, "上海 weather: sunny")

    def test_tool_selection(self) -> None:
        """验证 Agent 选择了预期工具。"""
        _, trace = run_case(
            EvalCase(
                "查询天气: 上海", "上海 weather: sunny", "weather", {"city": "上海"}
            )
        )
        self.assertEqual(trace.tool_calls[0]["tool"], "weather")

    def test_tool_arguments(self) -> None:
        """验证传给工具的参数。"""
        _, trace = run_case(
            EvalCase(
                "查询天气: 上海", "上海 weather: sunny", "weather", {"city": "上海"}
            )
        )
        self.assertEqual(trace.tool_calls[0]["args"], {"city": "上海"})

    def test_trajectory_without_tool(self) -> None:
        """验证不需要工具时不会产生工具调用。"""
        answer, trace = run_case(
            EvalCase(
                "什么是 Prometheus？",
                "I can answer without using a tool.",
                None,
                {},
            )
        )
        self.assertEqual(answer, "I can answer without using a tool.")
        self.assertEqual(trace.tool_calls, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
