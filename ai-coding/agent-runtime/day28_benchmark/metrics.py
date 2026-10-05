"""Metrics for the day 28 failure and load-testing exercises.计算成功率、QPS、P99、成本"""


def percentile(values, percentile):
    """返回一个简单的离散百分位值。

    ``values`` 会被排序，百分位索引向下取整；本练习关注 P99 的比较，
    不引入统计库，以便学习者看清计算过程。
    """
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(
        len(ordered) - 1, int((percentile / 100) * len(ordered))
    )  # 计算 P99 百分位对应的索引
    return ordered[index]


def calculate_metrics(results, elapsed_seconds):
    """根据任务结果计算 benchmark 的核心指标。

    ``results`` 中每项至少包含 ``success``、``latency_ms`` 和 ``cost``。
    返回：任务数、成功率、QPS、P99 延迟、单任务成本和总成本。
    空结果也会返回 0，避免报告阶段出现除零错误。
    """
    total = len(results)
    # 成功率只统计最终成功的任务；失败任务仍然计入总任务数和成本。
    # 统计 results 中 success 为 True 的结果数量，也就是成功任务数。
    successes = sum(1 for result in results if result["success"])
    latencies = [result["latency_ms"] for result in results]
    total_cost = sum(result["cost"] for result in results)
    return {
        "tasks": total,
        "success_rate": successes / total if total else 0.0,
        # QPS 是整轮压测完成的任务数除以墙上时钟耗时。
        "qps": total / elapsed_seconds if elapsed_seconds else 0.0,
        "p99_latency_ms": percentile(latencies, 99),
        "cost_per_task": total_cost / total if total else 0.0,
        "total_cost": total_cost,
    }


"""
successes = sum(1 for result in results if result["success"])

==
success_count = 0

for result in results:
    if result["success"]:
        success_count += 1
"""
