"""Run a LangChain Agent backed by DeepSeek and expose runtime metrics."""

from __future__ import annotations

import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from prometheus_client import Counter, Gauge, Histogram, generate_latest

load_dotenv(Path(__file__).with_name(".env"), override=True)

TASKS = Counter("agent_tasks_total", "Total Agent tasks", ["status"])
TASK_FAILURES = Counter("agent_task_failures_total", "Agent task failures", ["source"])
TASK_LATENCY = Histogram(
    "agent_task_latency_seconds",
    "Agent task latency in seconds",
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 30, 60),
)
TASK_SUCCESS = Gauge("agent_task_success_rate", "Latest Agent task success rate")
TOKEN_USAGE = Counter("agent_tokens_total", "Total model tokens", ["type"])
TASK_COST = Counter("agent_cost_usd_total", "Estimated Agent cost in USD")
QPS = Gauge("agent_qps", "Observed tasks per second")

INPUT_COST_PER_TOKEN = float(os.getenv("DEEPSEEK_INPUT_COST_PER_TOKEN", "0.00000028"))
OUTPUT_COST_PER_TOKEN = float(os.getenv("DEEPSEEK_OUTPUT_COST_PER_TOKEN", "0.00000110"))


def build_agent():
    """Create a LangChain Agent using the DeepSeek chat model."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is not set")
    model = ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=api_key,
        temperature=0,
    )
    return create_agent(model=model, tools=[])


def _usage_from_result(result: dict) -> dict[str, int]:
    """Read token usage from LangChain message metadata."""
    usage = {"input": 0, "output": 0}
    for message in result.get("messages", []):
        metadata = getattr(message, "usage_metadata", None) or {}
        response_metadata = getattr(message, "response_metadata", None) or {}
        response_usage = response_metadata.get("usage", {})
        usage["input"] += metadata.get(
            "input_tokens", response_usage.get("prompt_tokens", 0)
        )
        usage["output"] += metadata.get(
            "output_tokens", response_usage.get("completion_tokens", 0)
        )
    return usage


def run_task(agent, prompt: str) -> str:
    """Invoke the LangChain Agent and record task metrics."""
    started = time.perf_counter()
    try:
        result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
        usage = _usage_from_result(result)
        TOKEN_USAGE.labels(type="input").inc(usage["input"])
        TOKEN_USAGE.labels(type="output").inc(usage["output"])
        TASK_COST.inc(
            usage["input"] * INPUT_COST_PER_TOKEN
            + usage["output"] * OUTPUT_COST_PER_TOKEN
        )
        TASKS.labels(status="success").inc()
        TASK_SUCCESS.set(1.0)
        return result["messages"][-1].content
    except Exception as exc:
        TASKS.labels(status="error").inc()
        TASK_FAILURES.labels(source="agent").inc()
        TASK_SUCCESS.set(0.0)
        raise RuntimeError(f"LangChain Agent failed: {exc}") from exc
    finally:
        TASK_LATENCY.observe(time.perf_counter() - started)


class MetricsHandler(BaseHTTPRequestHandler):
    """Serve Prometheus metrics on /metrics."""

    def do_GET(self) -> None:  # noqa: N802
        if self.path != "/metrics":
            self.send_error(404)
            return
        payload = generate_latest()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args: object) -> None:
        pass


def main() -> None:
    agent = build_agent()
    server = HTTPServer(("0.0.0.0", 8000), MetricsHandler)
    print("Prometheus metrics: http://127.0.0.1:8000/metrics", flush=True)
    prompts = [
        "Explain in one sentence what Prometheus is used for.",
        "Give one practical tip for reducing Agent latency.",
        "What is the difference between a Counter and a Histogram?",
    ]
    try:
        while True:
            batch_started = time.perf_counter()
            for prompt in prompts:
                try:
                    print(f"Agent: {run_task(agent, prompt)}", flush=True)
                except RuntimeError as exc:
                    print(f"Agent error: {exc}", flush=True)
            QPS.set(len(prompts) / (time.perf_counter() - batch_started))
            server.handle_request()
    except KeyboardInterrupt:
        print("stopped", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
