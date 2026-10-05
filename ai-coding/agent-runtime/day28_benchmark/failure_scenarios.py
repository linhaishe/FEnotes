"""Deterministic fault scenarios used by the benchmark exercises.模拟四类故障"""

import argparse
import json
import random
import time

# CLI 和压测共用这组名称，避免命令行允许一种场景、代码却不认识它。
SCENARIOS = ("timeout", "rate_limit", "process_restart", "tool_failure")


def run_scenario(name, seed=None):
    """执行一次故障模拟。

    参数：
        name: 故障名称，必须是 ``SCENARIOS`` 中的值。
        seed: 随机种子；相同种子会产生相同的基础延迟，方便复现实验。

    返回值是统一的任务结果，供 ``metrics.py`` 汇总：
    ``success`` 表示是否成功，``latency_ms`` 是模拟延迟，``cost`` 是成本，
    ``error`` 是失败类型。
    """
    if name not in SCENARIOS:
        raise ValueError(f"unknown scenario: {name}")

    rng = random.Random(seed) # 创建一台“随机数机器”，seed 是这台机器的初始状态；只要初始状态相同，后续产生的数字序列就相同。
    # print(random.randint(20, 80)) 普通随机数每次运行可能不同
    # 先生成正常任务的基础延迟，再由具体故障覆盖它。作用是生成一个 20 到 80 之间的随机整数,生成包含边界的整数.
    # 如果使用固定种子，相同种子会生成相同的随机结果，便于复现实验。
    latency_ms = rng.randint(20, 80)
    result = {
        "scenario": name,
        "success": True,
        "latency_ms": latency_ms,
        "cost": 0.01,
        "error": None,
    }

    # 这里模拟“最终失败”的结果，不是真正 sleep；这样压测快速且可重复。
    if name == "timeout":
        result.update(success=False, latency_ms=250, cost=0.02, error="timeout")
    elif name == "rate_limit":
        result.update(success=False, latency_ms=40, error="rate_limit")
    elif name == "process_restart":
        result.update(
            success=False, latency_ms=180, cost=0.03, error="process_restarted"
        )
    elif name == "tool_failure":
        result.update(success=False, latency_ms=70, cost=0.015, error="tool_failed")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", choices=SCENARIOS, help="要模拟的故障场景")
    parser.add_argument(
        "--seed", type=int, default=1, help="随机种子；相同值用于复现实验（默认：1）"
    )
    args = parser.parse_args()
    started = time.perf_counter()
    result = run_scenario(args.scenario, args.seed)
    result["elapsed_ms"] = round((time.perf_counter() - started) * 1000, 3)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
