"""Run the benchmark against a real LangChain Agent backed by Gemini."""

import argparse
import os
import time

from langchain.agents import create_agent

from failure_scenarios import SCENARIOS
from metrics import calculate_metrics


def get_weather(city: str) -> str:
    """Demo tool used by the agent; replace this with a real application tool."""
    return f"The weather in {city} is sunny."


def build_agent():
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("请先设置 GEMINI_API_KEY")
    return create_agent(
        model=os.getenv("GEMINI_MODEL", "google_genai:gemini-2.5-flash-lite"),
        tools=[get_weather],
        system_prompt="You are a concise assistant. Use tools when they are useful.",
    )


def _usage_cost(result):
    """Return token usage; pricing is intentionally supplied by the caller."""
    tokens = 0
    for message in result.get("messages", []):
        tokens += message.response_metadata.get("usage", {}).get("total_tokens", 0)
        tokens += message.usage_metadata.get("total_tokens", 0)
    return tokens


def run_agent_task(agent, task, scenario, cost_per_token=0.0):
    started = time.perf_counter()
    try:
        if scenario == "timeout":
            raise TimeoutError("injected timeout")
        if scenario == "rate_limit":
            raise RuntimeError("injected rate limit")
        if scenario == "process_restart":
            raise RuntimeError("injected process restart")
        if scenario == "tool_failure":
            raise RuntimeError("injected tool failure")

        result = agent.invoke({"messages": [{"role": "user", "content": task}]})
        tokens = _usage_cost(result)
        return {
            "success": True,
            "latency_ms": round((time.perf_counter() - started) * 1000, 3),
            "cost": tokens * cost_per_token,
            "error": None,
        }
    except TimeoutError:
        error = "timeout"
    except RuntimeError as exc:
        error = str(exc).replace("injected ", "")

    return {
        "success": False,
        "latency_ms": round((time.perf_counter() - started) * 1000, 3),
        "cost": 0.0,
        "error": error,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=("none", *SCENARIOS), default="none")
    parser.add_argument("--task", default="What is the weather in Beijing?")
    parser.add_argument("--cost-per-token", type=float, default=0.0)
    args = parser.parse_args()
    result = run_agent_task(
        build_agent(), args.task, args.scenario, args.cost_per_token
    )
    print(result)


if __name__ == "__main__":
    main()
