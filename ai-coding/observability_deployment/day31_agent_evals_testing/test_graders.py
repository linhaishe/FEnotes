"""第五阶段 Grader 的确定性测试。"""

import unittest

from graders import contains_text, exact_match, json_field_equals, rule_score


class GraderTests(unittest.TestCase):
    """验证不同类型 Grader 的评分结果。"""

    def test_exact_match(self) -> None:
        """精确匹配适合固定格式或固定答案。"""
        self.assertTrue(exact_match("上海 weather: sunny", "上海 weather: sunny"))
        self.assertFalse(exact_match("上海天气晴朗", "上海 weather: sunny"))

    def test_contains_text(self) -> None:
        """包含匹配适合答案允许有额外解释的场景。"""
        self.assertTrue(contains_text("上海 weather: sunny", "sunny"))
        self.assertFalse(contains_text("上海 weather: cloudy", "sunny"))

    def test_json_field_equals(self) -> None:
        """JSON 字段匹配适合结构化输出。"""
        self.assertTrue(json_field_equals('{"city": "上海"}', "city", "上海"))
        self.assertFalse(json_field_equals("not-json", "city", "上海"))

    def test_rule_score(self) -> None:
        """规则评分汇总多个独立检查。"""
        self.assertEqual(rule_score({"answer": True, "tool": True}), 1.0)
        self.assertEqual(rule_score({"answer": True, "tool": False}), 0.5)
        self.assertEqual(rule_score({}), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
