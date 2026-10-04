"""Deterministic fault scenarios used by the benchmark exercises."""

import argparse
import json
import random
import time


SCENARIOS = ("timeout", "rate_limit", "process_restart", "tool_failure")


def run_scenario(name, seed=None):
    if name not in SCENARIOS:
        raise ValueError(f"unknown scenario: {name}")

    rng = random.Random(seed)
    latency_ms = rng.randint(20, 80)
    result = {"scenario": name, "success": True, "latency_ms": latency_ms, "cost": 0.01, "error": None}

    if name == "timeout":
        result.update(success=False, latency_ms=250, cost=0.02, error="timeout")
    elif name == "rate_limit":
        result.update(success=False, latency_ms=40, error="rate_limit")
    elif name == "process_restart":
        result.update(success=False, latency_ms=180, cost=0.03, error="process_restarted")
    elif name == "tool_failure":
        result.update(success=False, latency_ms=70, cost=0.015, error="tool_failed")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", choices=SCENARIOS)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    started = time.perf_counter()
    result = run_scenario(args.scenario, args.seed)
    result["elapsed_ms"] = round((time.perf_counter() - started) * 1000, 3)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
