"""Trace a small LangChain Agent in LangSmith.

Required for a real run:
    DEEPSEEK_API_KEY
    LANGSMITH_API_KEY
    LANGSMITH_TRACING=true
"""

from __future__ import annotations

import argparse
import os
import time

from langchain.agents import create_agent
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv(override=True)


def get_weather(city: str) -> str:
    """Return deterministic demo data so the tool call is easy to inspect."""
    return f"The weather in {city} is sunny and 22C."


def build_agent():
    """Create the Agent whose model and tool calls LangSmith will trace."""
    if not os.getenv("DEEPSEEK_API_KEY"):
        raise RuntimeError("请先设置 DEEPSEEK_API_KEY")
    try:
        from langchain_deepseek import ChatDeepSeek
    except ImportError as error:
        raise RuntimeError(
            "缺少 DeepSeek 集成，请先运行：pip install -U langchain-deepseek"
        ) from error
    model = ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        timeout=float(os.getenv("DEEPSEEK_TIMEOUT_SECONDS", "60")),
        max_retries=0,
    )
    return create_agent(
        model=model,
        tools=[get_weather],
        system_prompt="You are concise. Use the weather tool when the user asks about weather.",
    )


@traceable(name="day29_agent_task", run_type="chain")
def run(task: str) -> dict[str, object]:
    """Run one traced Agent task and return local summary metrics.

    Args:
        task: User task sent to the Agent.

    Returns:
        A local summary. Detailed nested runs are visible in LangSmith.
    """
    print("开始调用 Agent...", flush=True)
    agent = build_agent()
    started = time.perf_counter()
    result = agent.invoke({"messages": [{"role": "user", "content": task}]})
    print("Agent 调用完成，正在整理结果...", flush=True)
    elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
    messages = result.get("messages", [])
    tool_calls = sum(
        len(getattr(message, "tool_calls", []) or []) for message in messages
    )
    final = messages[-1].content if messages else ""
    return {
        "success": True,
        "latency_ms": elapsed_ms,
        "message_count": len(messages),
        "tool_call_count": tool_calls,
        "final": final,
        "langsmith_project": os.getenv("LANGSMITH_PROJECT", "langsmith-demo"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--task", default="What is the weather in Beijing? Answer in one sentence."
    )
    args = parser.parse_args()
    if os.getenv("LANGSMITH_TRACING", "").lower() not in {"true", "1", "yes"}:
        raise RuntimeError("请设置 LANGSMITH_TRACING=true，确保运行会发送到 LangSmith")
    try:
        print(run(args.task), flush=True)
    except Exception as error:
        print(f"Agent 调用失败：{type(error).__name__}: {error}", flush=True)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
