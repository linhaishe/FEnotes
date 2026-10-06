"""Expose Agent runtime metrics for Prometheus and generate demo traffic."""

from __future__ import annotations

import random
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from prometheus_client import Counter, Gauge, Histogram, generate_latest

TASKS = Counter("agent_tasks_total", "Total Agent tasks", ["status"])
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


def run_task(rng: random.Random) -> None:
    """Simulate one Agent task and record its operational metrics.

    Args:
        rng: Deterministic random generator used by the demo.
    """
    started = time.perf_counter()
    latency = rng.uniform(0.03, 0.4)
    time.sleep(latency)
    success = rng.random() > 0.15
    input_tokens = rng.randint(80, 180)
    output_tokens = rng.randint(20, 80)
    cost = input_tokens * 0.000001 + output_tokens * 0.000002

    TASK_LATENCY.observe(time.perf_counter() - started)
    TASKS.labels(status="success" if success else "error").inc()
    TOKEN_USAGE.labels(type="input").inc(input_tokens)
    TOKEN_USAGE.labels(type="output").inc(output_tokens)
    TASK_COST.inc(cost)
    if not success:
        TOOL_FAILURES.labels(tool="weather", error="timeout").inc()
    TASK_SUCCESS.set(1.0 if success else 0.0)


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
    rng = random.Random(1)
    try:
        while True:
            batch_started = time.perf_counter()
            for _ in range(5):
                run_task(rng)
            QPS.set(5 / (time.perf_counter() - batch_started))
            server.handle_request()
    except KeyboardInterrupt:
        print("stopped", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
