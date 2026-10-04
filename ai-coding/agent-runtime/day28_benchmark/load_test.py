"""Run a small, reproducible benchmark without external dependencies."""

import argparse
import json
import time
from concurrent.futures import ThreadPoolExecutor

from failure_scenarios import SCENARIOS, run_scenario
from metrics import calculate_metrics


def run_load_test(scenario, tasks, workers, seed):
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(lambda i: run_scenario(scenario, seed + i), range(tasks)))
    elapsed_seconds = time.perf_counter() - started
    return calculate_metrics(results, elapsed_seconds)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=SCENARIOS, default="tool_failure")
    parser.add_argument("--tasks", type=int, default=100)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if args.tasks < 1 or args.workers < 1:
        parser.error("--tasks and --workers must be positive")
    print(json.dumps(run_load_test(args.scenario, args.tasks, args.workers, args.seed), indent=2))


if __name__ == "__main__":
    main()
