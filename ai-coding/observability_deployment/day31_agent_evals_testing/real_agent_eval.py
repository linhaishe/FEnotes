"""第四阶段：用真实 DeepSeek Agent 评估 Mock Tool 的调用行为。"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_deepseek import ChatDeepSeek

load_dotenv(Path(__file__).with_name(".env"), override=True)

TOOL_CALLS: list[dict[str, Any]] = []


@dataclass(frozen=True)
class RealEvalCase:
    """定义真实 Agent 评估用例的输入和期望行为。"""

    prompt: str
    expected_tool: str | None
    expected_city: str | None


@tool
def mock_weather(city: str) -> str:
    """返回固定天气数据，不调用真实服务。

    Args:
        city: Agent 请求查询的城市名。

    Returns:
        用于评估工具选择和参数的固定天气数据。
    """
    TOOL_CALLS.append({"tool": "mock_weather", "args": {"city": city}})
    return {"上海": "sunny", "北京": "cloudy"}.get(city, "unknown")


def build_agent():
    """创建由 DeepSeek 驱动、使用 Mock Tool 的真实 LangChain Agent。

    Returns:
        一个可以决定是否调用 ``mock_weather`` 的 LangChain Agent。

    Raises:
        RuntimeError: 未设置 ``DEEPSEEK_API_KEY`` 时抛出。
    """
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is not set")
    model = ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=api_key,
        temperature=0,
    )
    return create_agent(model=model, tools=[mock_weather])


def run_real_eval(prompt: str) -> dict[str, Any]:
    """运行一个真实模型评估用例，并返回答案和实际轨迹。

    Args:
        prompt: 发送给真实 Agent 的用户请求。

    Returns:
        可序列化为 JSON 的报告，包含最终答案和工具调用记录。
    """
    TOOL_CALLS.clear()
    result = build_agent().invoke({"messages": [{"role": "user", "content": prompt}]})
    return {
        "prompt": prompt,
        "answer": result["messages"][-1].content,
        "tool_calls": list(TOOL_CALLS),
    }


def evaluate_case(case: RealEvalCase) -> dict[str, Any]:
    """运行并评估一个真实 Agent 用例。

    Args:
        case: 包含用户输入、期望工具和期望城市参数的评估用例。

    Returns:
        包含实际结果、各项检查结果和总通过状态的评估报告。
    """
    result = run_real_eval(case.prompt)
    calls = result["tool_calls"]
    actual_call = calls[0] if calls else {}
    checks = {
        "tool_selection": actual_call.get("tool") == case.expected_tool,
        "tool_arguments": (
            case.expected_city is None
            or actual_call.get("args", {}).get("city") == case.expected_city
        ),
        "tool_call_count": len(calls) == (1 if case.expected_tool else 0),
    }
    return {**result, "checks": checks, "passed": all(checks.values())}

