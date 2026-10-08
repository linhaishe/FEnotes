"""Task 4：共享预算、委派深度、并发及超时的离线测试。"""

import time
import unittest

from langchain.agents.middleware import ModelResponse
from langchain.messages import AIMessage

from runtime_limits import LimitExceeded, RequestBudget, RuntimeLimits, RuntimeBudgetMiddleware


class RuntimeLimitTests(unittest.TestCase):
    def test_budget_counts_all_model_calls_and_stops_next_call(self):
        limits = RuntimeLimits(max_tokens=10, max_cost_usd=1, input_rate=0.01,
                               output_rate=0.02)
        budget = RequestBudget(limits)
        middleware = RuntimeBudgetMiddleware(budget)
        calls = []

        def model_call(request):
            calls.append(1)
            return ModelResponse(result=[AIMessage(content="ok", usage_metadata={
                "input_tokens": 6, "output_tokens": 4, "total_tokens": 10,
            })])

        middleware.wrap_model_call(None, model_call)
        with self.assertRaises(LimitExceeded) as caught:
            middleware.wrap_model_call(None, model_call)
        self.assertEqual(caught.exception.code, "token_budget")
        self.assertEqual(len(calls), 1)
        self.assertEqual(budget.snapshot()["total_tokens"], 10)

    def test_cost_budget_stops_after_observed_usage(self):
        limits = RuntimeLimits(max_tokens=100, max_cost_usd=0.1,
                               input_rate=0.01, output_rate=0.02)
        budget = RequestBudget(limits)
        middleware = RuntimeBudgetMiddleware(budget)
        response = ModelResponse(result=[AIMessage(content="ok", usage_metadata={
            "input_tokens": 10, "output_tokens": 0, "total_tokens": 10,
        })])
        middleware.wrap_model_call(None, lambda request: response)
        with self.assertRaises(LimitExceeded) as caught:
            middleware.wrap_model_call(None, lambda request: self.fail("extra model call"))
        self.assertEqual(caught.exception.code, "cost_budget")

    def test_depth_and_repeated_delegation_are_limited(self):
        budget = RequestBudget(RuntimeLimits(max_depth=1, max_delegations=1))
        with budget.delegation(depth=1):
            self.assertEqual(budget.snapshot()["peak_concurrency"], 1)
        with self.assertRaises(LimitExceeded) as caught:
            with budget.delegation(depth=1):
                pass
        self.assertEqual(caught.exception.code, "delegation_limit")
        fresh = RequestBudget(RuntimeLimits(max_depth=1))
        with self.assertRaises(LimitExceeded) as caught:
            with fresh.delegation(depth=2):
                pass
        self.assertEqual(caught.exception.code, "depth_limit")

    def test_concurrency_limit_never_allows_second_active_delegation(self):
        budget = RequestBudget(RuntimeLimits(max_concurrency=1, timeout_seconds=0.02))
        with budget.delegation(depth=1):
            with self.assertRaises(LimitExceeded) as caught:
                with budget.delegation(depth=1):
                    pass
        self.assertEqual(caught.exception.code, "timeout")
        self.assertEqual(budget.snapshot()["peak_concurrency"], 1)

    def test_deadline_blocks_model_call_before_it_starts(self):
        budget = RequestBudget(RuntimeLimits(timeout_seconds=0.001))
        middleware = RuntimeBudgetMiddleware(budget)
        time.sleep(0.005)
        with self.assertRaises(LimitExceeded) as caught:
            middleware.wrap_model_call(None, lambda request: self.fail("called after deadline"))
        self.assertEqual(caught.exception.code, "timeout")

    def test_deadline_rejects_model_result_that_arrives_too_late(self):
        budget = RequestBudget(RuntimeLimits(timeout_seconds=0.001))
        middleware = RuntimeBudgetMiddleware(budget)

        def slow_model(request):
            time.sleep(0.005)
            return ModelResponse(result=[AIMessage(content="late", usage_metadata={
                "input_tokens": 1, "output_tokens": 1, "total_tokens": 2,
            })])

        with self.assertRaises(LimitExceeded) as caught:
            middleware.wrap_model_call(None, slow_model)
        self.assertEqual(caught.exception.code, "timeout")
        self.assertEqual(budget.snapshot()["model_calls"], 1)


if __name__ == "__main__":
    unittest.main()
