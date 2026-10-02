"""A small, framework-free agent loop."""

from __future__ import annotations

from dataclasses import dataclass, field
import time
from typing import Any, Callable, Protocol


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class ModelResponse:
    text: str | None = None
    tool_calls: tuple[ToolCall, ...] = ()
    cost: float = 0.0


class Model(Protocol):
    def complete(self, messages: list[dict[str, Any]]) -> ModelResponse:
        """
        根据消息列表生成一次模型响应。

        Args:
            messages: 对话消息列表，每条消息包含消息角色和内容。

        Returns:
            模型响应，可能包含文本、工具调用和调用成本。
        """
        ...


@dataclass(frozen=True)
class Budget:
    max_turns: int = 8
    timeout_seconds: float = 30.0
    max_cost: float = 1.0


@dataclass
class RunResult:
    output: str | None
    stop_reason: str
    turns: int
    cost: float
    messages: list[dict[str, Any]] = field(default_factory=list)


Tool = Callable[..., Any]
# Tool 代表一个可以被调用的对象，参数任意，返回值任意。
"""
Callable：可调用对象，比如函数、方法、实现了 __call__ 的对象
...：参数数量和类型不限
Any：返回值类型不限

等价于
tools: dict[str, Tool]

表示工具注册表
tools = {
    "add": lambda a, b: a + b,
    "greet": lambda name: f"你好，{name}",
}
"""

"""
Messages → Model
              ↓
        Tool calls
              ↓
           Tools
              ↓
Messages ← tool results
"""
# Harness 不负责做具体决策或动作，而是把各部分串起来
def run_agent(
    model: Model,
    user_input: str,
    tools: dict[str, Tool] | None = None,
    budget: Budget = Budget(),
    clock: Callable[[], float] = time.monotonic, # 不是立即调用。相比 time.time()，time.monotonic() 不会因为系统时间被手动调整或同步而倒退，因此适合超时判断
) -> RunResult:
    """
    运行模型和工具调用循环，直到生成文本或触发预算限制。

    Args:
        model: 用于生成响应的模型实现。
        user_input: 用户输入的初始消息。
        tools: 按名称注册的工具函数。
        budget: 最大轮数、超时时间和最大成本限制。
        clock: 返回当前时间的函数，默认使用单调时钟。

    Returns:
        包含最终输出、停止原因、轮数、成本和消息记录的运行结果。
    """
    if budget.max_turns < 1:
        raise ValueError("max_turns must be at least 1")
    if budget.timeout_seconds <= 0 or budget.max_cost < 0:
        raise ValueError("timeout_seconds must be positive and max_cost non-negative")

    registry = tools or {}
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_input}]
    started = clock()
    total_cost = 0.0

    for turn in range(1, budget.max_turns + 1):
        if clock() - started >= budget.timeout_seconds:
            return RunResult(None, "timeout", turn - 1, total_cost, messages)

        response = model.complete(messages)
        total_cost += response.cost
        if total_cost > budget.max_cost:
            return RunResult(None, "cost_budget", turn, total_cost, messages)
        
        # 如果模型返回了文本，并且没有要求调用工具
        if response.text is not None and not response.tool_calls:
            messages.append({"role": "assistant", "content": response.text})
            return RunResult(response.text, "completed", turn, total_cost, messages)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": [
                    {"name": call.name, "arguments": call.arguments}
                    for call in response.tool_calls
                ],
            }
        )
        for call in response.tool_calls:
            tool = registry.get(call.name)
            if tool is None:
                result: Any = {"error": f"unknown tool: {call.name}"}
            else:
                try:
                    result = tool(**call.arguments)
                except Exception as exc:  # Tool errors become model-visible results.
                    result = {"error": f"{type(exc).__name__}: {exc}"}
            messages.append({"role": "tool", "name": call.name, "content": result})

    return RunResult(None, "max_turns", budget.max_turns, total_cost, messages)


class ScriptedModel:
    """Deterministic model double used by the demo and self-check."""

    def __init__(self, responses: list[ModelResponse]):
        """
        初始化一个按顺序返回预设响应的模型。

        Args:
            responses: 需要按调用顺序返回的模型响应列表。
        """
        self._responses = iter(responses) # 表示把 responses 列表转换成一个迭代器，并保存到对象中。

    def complete(self, messages: list[dict[str, Any]]) -> ModelResponse:
        """
        返回下一个预设响应。

        Args:
            messages: 当前对话消息列表；脚本模型不会使用它。

        Returns:
            预设响应列表中的下一个模型响应。
        """
        return next(self._responses)
    
    """
    responses = ["第一次", "第二次", "第三次"]
    iterator = iter(responses)

    next(iterator)  # "第一次"
    next(iterator)  # "第二次"
    next(iterator)  # "第三次"
    """


def _demo() -> None:
    """运行一个工具调用后生成文本的最小自检示例。"""
    model = ScriptedModel(
        [
            ModelResponse(tool_calls=(ToolCall("add", {"a": 2, "b": 3}),), cost=0.01),
            ModelResponse(text="结果是 5", cost=0.01),
        ]
    )
    result = run_agent(model, "计算 2 + 3", {"add": lambda a, b: a + b})
    assert (result.output, result.stop_reason, result.turns) == (
        "结果是 5",
        "completed",
        2,
    )
    assert result.messages[-1]["role"] == "assistant"
    print(result.output)


if __name__ == "__main__":
    _demo()