"""Run a small, reproducible benchmark without external dependencies.并发执行压测"""

import argparse
import json
import time
from concurrent.futures import ThreadPoolExecutor

from failure_scenarios import SCENARIOS, run_scenario
from metrics import calculate_metrics


def run_with_recovery(scenario, seed, idempotent=True):
    """执行一次任务，并应用场景对应的最小恢复策略。

    压测不真实 sleep；rate_limit 的退避时间只计入结果延迟，避免实验变慢。
    """
    result = run_scenario(scenario, seed)

    if result["success"]:
        return result

    if scenario == "process_restart" and not idempotent:
        result["error"] = "process_restarted_status_unknown"
        return result

    if scenario in {"timeout", "rate_limit", "process_restart"}:
        retry = run_scenario(scenario, seed + 1000)
        if scenario == "rate_limit":
            retry["latency_ms"] += 100
        result["latency_ms"] += retry["latency_ms"]
        result["cost"] += retry["cost"]
        return retry | {
            "latency_ms": result["latency_ms"],
            "cost": result["cost"],
        }

    if scenario == "tool_failure":
        # 非核心工具降级为空结果，主流程视为成功。
        result.update(success=True, latency_ms=0, cost=result["cost"], error=None)

    return result


def run_load_test(scenario, tasks, workers, seed):
    """并发执行多个任务，并返回聚合指标。

    参数：
        scenario: 每个任务使用的故障场景。
        tasks: 总任务数；每个任务都会获得 ``seed + task_index``。
        workers: 线程池大小，代表同时执行的任务数上限。
        seed: 起始随机种子，用于保证同一组参数可以复现。
    """
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        # executor.map 会按任务提交顺序返回结果，便于和 seed 对应。
        results = list(
            executor.map(
                lambda i: run_with_recovery(scenario, seed + i), range(tasks)
            )
        )
    elapsed_seconds = time.perf_counter() - started
    # 用整段压测耗时计算 QPS，而不是用单个任务的模拟延迟。
    return calculate_metrics(results, elapsed_seconds)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scenario",
        choices=SCENARIOS,
        default="tool_failure",
        help="故障场景（默认：tool_failure）",
    )
    parser.add_argument("--tasks", type=int, default=100, help="总任务数（默认：100）")
    parser.add_argument(
        "--workers", type=int, default=8, help="并发 worker 数（默认：8）"
    )
    parser.add_argument("--seed", type=int, default=1, help="起始随机种子（默认：1）")
    args = parser.parse_args()
    # 0 个任务或 0 个 worker 都无法形成有效压测，提前给出用户可读错误。
    if args.tasks < 1 or args.workers < 1:
        parser.error("--tasks and --workers must be positive")
    print(
        json.dumps(
            run_load_test(args.scenario, args.tasks, args.workers, args.seed), indent=2
        )
    )


if __name__ == "__main__":
    main()

"""
这段代码会并发执行 tasks 次 run_scenario，最后得到一个由结果字典组成的列表：

results = list(
    executor.map(
        lambda i: run_scenario(scenario, seed + i),
        range(tasks),
    )
)


run_scenario("timeout", 1)
run_scenario("timeout", 2)
run_scenario("timeout", 3)


result:

[
    {
        "scenario": "timeout",
        "success": False,
        "latency_ms": 250,
        "cost": 0.02,
        "error": "timeout",
    },
    {
        "scenario": "timeout",
        "success": False,
        "latency_ms": 250,
        "cost": 0.02,
        "error": "timeout",
    },
    {
        "scenario": "timeout",
        "success": False,
        "latency_ms": 250,
        "cost": 0.02,
        "error": "timeout",
    },
]
        
        
"""
