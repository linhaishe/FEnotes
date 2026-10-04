"""Metrics for the day 28 failure and load-testing exercises."""


def percentile(values, percentile):
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, int((percentile / 100) * len(ordered)))
    return ordered[index]


def calculate_metrics(results, elapsed_seconds):
    total = len(results)
    successes = sum(1 for result in results if result["success"])
    latencies = [result["latency_ms"] for result in results]
    total_cost = sum(result["cost"] for result in results)
    return {
        "tasks": total,
        "success_rate": successes / total if total else 0.0,
        "qps": total / elapsed_seconds if elapsed_seconds else 0.0,
        "p99_latency_ms": percentile(latencies, 99),
        "cost_per_task": total_cost / total if total else 0.0,
        "total_cost": total_cost,
    }
