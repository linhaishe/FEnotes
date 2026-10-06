"""Call a DeepSeek Agent and expose its runtime metrics for Prometheus."""

from __future__ import annotations

import json
import os
from pathlib import Path
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv
from prometheus_client import Counter, Gauge, Histogram, generate_latest

load_dotenv(Path(__file__).with_name(".env"), override=True)

TASKS = Counter("agent_tasks_total", "Total Agent tasks", ["status"])
TASK_FAILURES = Counter("agent_task_failures_total", "Agent task failures", ["source"])
TASK_LATENCY = Histogram(
    "agent_task_latency_seconds",
    "Agent task latency in seconds",
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5),
)
TASK_SUCCESS = Gauge("agent_task_success_rate", "Latest Agent task success rate")
TOKEN_USAGE = Counter("agent_tokens_total", "Total model tokens", ["type"])
TASK_COST = Counter("agent_cost_usd_total", "Estimated Agent cost in USD")
TOOL_FAILURES = Counter("agent_tool_failures_total", "Tool failures", ["tool", "error"])
QPS = Gauge("agent_qps", "Observed tasks per second")
DEEPSEEK_URL = (
    os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
    + "/chat/completions"
)
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
INPUT_COST_PER_TOKEN = float(os.getenv("DEEPSEEK_INPUT_COST_PER_TOKEN", "0.00000028"))
OUTPUT_COST_PER_TOKEN = float(os.getenv("DEEPSEEK_OUTPUT_COST_PER_TOKEN", "0.00000110"))


def run_task(prompt: str) -> str:
    """Run one task through DeepSeek and record its operational metrics.

    Args:
        prompt: User task sent to the Agent.

    Raises:
        RuntimeError: If the API key is missing or DeepSeek returns an error.
    """
    started = time.perf_counter()
    try:
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise RuntimeError("DEEPSEEK_API_KEY is not set")

        payload = json.dumps(
            {
                "model": DEEPSEEK_MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a concise helpful assistant.",
                    },
                    {"role": "user", "content": prompt},
                ],
            }
        ).encode("utf-8")
        request = Request(
            DEEPSEEK_URL,
            data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urlopen(request, timeout=60) as response:
            result = json.loads(response.read())

        usage = result.get("usage", {})
        input_tokens = usage.get("prompt_tokens", 0)
        output_tokens = usage.get("completion_tokens", 0)
        TOKEN_USAGE.labels(type="input").inc(input_tokens)
        TOKEN_USAGE.labels(type="output").inc(output_tokens)
        TASK_COST.inc(
            input_tokens * INPUT_COST_PER_TOKEN + output_tokens * OUTPUT_COST_PER_TOKEN
        )
        TASKS.labels(status="success").inc()
        TASK_SUCCESS.set(1.0)
        return result["choices"][0]["message"]["content"]
    except (HTTPError, URLError, KeyError, json.JSONDecodeError, RuntimeError) as exc:
        TASKS.labels(status="error").inc()
        TASK_FAILURES.labels(source="model").inc()
        TASK_SUCCESS.set(0.0)
        raise RuntimeError(f"DeepSeek request failed: {exc}") from exc
    finally:
        TASK_LATENCY.observe(time.perf_counter() - started)


class MetricsHandler(BaseHTTPRequestHandler):
    """Serve Prometheus metrics on /metrics."""

    def do_GET(self) -> None:  # noqa: N802
        """Return the current Prometheus exposition text."""
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
        """Keep the demo output focused on metrics."""


def main() -> None:
    """Generate demo traffic and serve metrics until interrupted."""
    server = HTTPServer(("0.0.0.0", 8000), MetricsHandler)
    print("Prometheus metrics: http://127.0.0.1:8000/metrics", flush=True)
    prompts = [
        "Explain in one sentence what Prometheus is used for.",
        "Give one practical tip for reducing Agent latency.",
        "What is the difference between a Counter and a Histogram?",
        "Summarize why Agent tool calls should be instrumented.",
        "Name one useful Agent reliability metric.",
    ]
    prompt_index = 0
    try:
        while True:
            batch_started = time.perf_counter()
            for _ in prompts:
                prompt = prompts[prompt_index % len(prompts)]
                prompt_index += 1
                try:
                    answer = run_task(prompt)
                    print(f"Agent: {answer}", flush=True)
                except RuntimeError as exc:
                    print(f"Agent error: {exc}", flush=True)
            QPS.set(5 / (time.perf_counter() - batch_started))
            server.handle_request()
    except KeyboardInterrupt:
        print("stopped", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
