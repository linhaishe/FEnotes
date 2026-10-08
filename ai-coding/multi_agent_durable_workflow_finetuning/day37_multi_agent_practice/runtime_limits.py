"""Day 37 Task 4：同一请求的委派与模型调用共享运行限制。"""

from __future__ import annotations

import threading
import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable, Iterator

from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse


class LimitExceeded(RuntimeError):
    """标记任务因哪个运行限制而停止。"""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class RuntimeLimits:
    """单个任务的限制；费用单价按每 Token 美元计。"""

    max_depth: int = 1
    max_delegations: int = 2
    max_concurrency: int = 1
    max_tokens: int = 8000
    max_cost_usd: float = 0.1
    timeout_seconds: float = 30.0
    input_rate: float = 0.00000028
    output_rate: float = 0.00000110

    def __post_init__(self) -> None:
        """拒绝会让所有任务立即失败或失去限制的配置。"""
        if (
            any(
                value <= 0
                for value in (
                    self.max_depth,
                    self.max_delegations,
                    self.max_concurrency,
                    self.max_tokens,
                    self.max_cost_usd,
                    self.timeout_seconds,
                )
            )
            or self.input_rate < 0
            or self.output_rate < 0
        ):
            raise ValueError("运行限制必须为正数，Token 单价不能为负数")


class RequestBudget:
    """让 Manager 和两个子 Agent 共用一次请求的计数与截止时间。"""

    def __init__(self, limits: RuntimeLimits):
        """初始化请求预算。

        Args:
            limits: 深度、委派次数、并发、Token、费用和耗时上限。
        """
        self.limits = limits
        self.deadline = time.monotonic() + limits.timeout_seconds
        self._lock = threading.Lock()
        self._slots = threading.BoundedSemaphore(limits.max_concurrency)
        self.delegations = 0
        self.active_delegations = 0
        self.peak_concurrency = 0
        self.model_calls = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.cost_usd = 0.0
        self.stop_reason: str | None = None

    def _reject(self, code: str) -> None:
        self.stop_reason = code
        raise LimitExceeded(code)

    def check(self) -> None:
        """在下一次模型或委派调用前检查共享预算。"""
        with self._lock:
            self._check_locked()

    def _check_locked(self) -> None:
        if self.stop_reason:
            raise LimitExceeded(self.stop_reason)
        if time.monotonic() >= self.deadline:
            self._reject("timeout")
        if self.input_tokens + self.output_tokens >= self.limits.max_tokens:
            self._reject("token_budget")
        if self.cost_usd >= self.limits.max_cost_usd:
            self._reject("cost_budget")

    def begin_model_call(self) -> None:
        """原子地检查预算并登记即将发起的模型调用。"""
        with self._lock:
            self._check_locked()
            self.model_calls += 1

    @contextmanager
    def delegation(self, depth: int) -> Iterator[None]:
        """占用一个子任务并发位，超时或次数超限时拒绝。

        Args:
            depth: 本次委派的层级；Manager 直接委派为 1。
        """
        self.check()
        with self._lock:
            if depth > self.limits.max_depth:
                self._reject("depth_limit")
            if self.delegations >= self.limits.max_delegations:
                self._reject("delegation_limit")
            self.delegations += 1
        remaining = max(0.0, self.deadline - time.monotonic())
        if not self._slots.acquire(timeout=remaining):
            with self._lock:
                self._reject("timeout")
        try:
            self.check()
            with self._lock:
                self.active_delegations += 1
                self.peak_concurrency = max(
                    self.peak_concurrency, self.active_delegations
                )
            try:
                yield
            finally:
                with self._lock:
                    self.active_delegations -= 1
        finally:
            self._slots.release()

    def record(self, response: ModelResponse) -> None:
        """按模型响应的 usage_metadata 累加整条任务的实际用量。"""
        usage = [
            getattr(message, "usage_metadata", None) for message in response.result
        ]
        if not usage or any(item is None for item in usage):
            with self._lock:
                self._reject("usage_unavailable")
        input_tokens = sum(item.get("input_tokens", 0) for item in usage)
        output_tokens = sum(item.get("output_tokens", 0) for item in usage)
        with self._lock:
            self.input_tokens += input_tokens
            self.output_tokens += output_tokens
            self.cost_usd += (
                input_tokens * self.limits.input_rate
                + output_tokens * self.limits.output_rate
            )
            if time.monotonic() >= self.deadline:
                self._reject("timeout")
            if self.input_tokens + self.output_tokens > self.limits.max_tokens:
                self._reject("token_budget")
            if self.cost_usd > self.limits.max_cost_usd:
                self._reject("cost_budget")

    def snapshot(self) -> dict[str, Any]:
        """返回可以放入任务报告的计数和停止原因。"""
        with self._lock:
            return {
                "delegations": self.delegations,
                "peak_concurrency": self.peak_concurrency,
                "model_calls": self.model_calls,
                "input_tokens": self.input_tokens,
                "output_tokens": self.output_tokens,
                "total_tokens": self.input_tokens + self.output_tokens,
                "estimated_cost_usd": round(self.cost_usd, 8),
                "stop_reason": self.stop_reason,
            }


class RuntimeBudgetMiddleware(AgentMiddleware):
    """在每次 LangChain 模型调用前后检查同一个请求预算。"""

    def __init__(self, budget: RequestBudget):
        super().__init__()
        self.budget = budget

    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        """阻止预算耗尽后的新调用，并计入本次模型响应。"""
        self.budget.begin_model_call()
        response = handler(request)
        self.budget.record(response)
        return response
