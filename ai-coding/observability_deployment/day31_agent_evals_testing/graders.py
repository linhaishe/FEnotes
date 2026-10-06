"""第五阶段：用于 Agent Eval 的确定性 Grader。"""

from __future__ import annotations

import json
from typing import Any


def exact_match(actual: str, expected: str) -> bool:
    """判断实际答案是否与期望答案完全一致。

    Args:
        actual: Agent 实际输出。
        expected: 测试用例期望输出。

    Returns:
        完全一致返回 ``True``，否则返回 ``False``。
    """
    return actual == expected


def contains_text(actual: str, expected_fragment: str) -> bool:
    """判断实际答案是否包含指定文本。

    Args:
        actual: Agent 实际输出。
        expected_fragment: 期望出现的片段。

    Returns:
        包含片段返回 ``True``，否则返回 ``False``。
    """
    return expected_fragment in actual


def json_field_equals(actual_json: str, field: str, expected: Any) -> bool:
    """判断 JSON 输出中的指定字段是否等于期望值。

    Args:
        actual_json: Agent 返回的 JSON 字符串。
        field: 要检查的字段名。
        expected: 字段期望值。

    Returns:
        JSON 合法且字段值匹配时返回 ``True``。
    """
    try:
        return json.loads(actual_json).get(field) == expected
    except (TypeError, json.JSONDecodeError):
        return False


def rule_score(checks: dict[str, bool]) -> float:
    """根据多个布尔检查计算 0 到 1 的规则得分。

    Args:
        checks: 检查名称到通过状态的映射。

    Returns:
        通过检查数量占总检查数量的比例；没有检查时返回 ``0.0``。
    """
    if not checks:
        return 0.0
    return sum(checks.values()) / len(checks)
