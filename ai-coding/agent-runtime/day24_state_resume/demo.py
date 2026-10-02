"""Run State, checkpoint/resume, and idempotent side-effect demo."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RunState:
    # 一次 Agent 运行的最小可恢复状态；真实项目还可以放消息历史、预算等字段。
    run_id: str
    # 恢复时从这个步骤继续，而不是从用户输入重新开始。
    step: str = "create_order"
    input: dict[str, Any] = field(default_factory=dict)
    tool_results: dict[str, Any] = field(default_factory=dict)
    output: str | None = None


class CheckpointStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def save(self, state: RunState) -> None:
        # 先写临时文件，再替换正式文件，避免中断时留下半份 checkpoint。
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")
        temporary.replace(self.path)

    def load(self) -> RunState:
        return RunState(**json.loads(self.path.read_text(encoding="utf-8")))


class IdempotentOrderTool:
    """Create an order once for each tool-call key, even after a crash."""

    def __init__(self, ledger_path: Path) -> None:
        self.ledger_path = ledger_path

    def create(self, tool_call_id: str, item: str) -> dict[str, Any]:
        ledger = self._load()
        # Agent resume 可能重复发起同一个工具调用；命中幂等键时不再创建订单。
        if tool_call_id in ledger:
            return {**ledger[tool_call_id], "replayed": True}

        # 这里代表真实的有副作用操作，例如创建订单、扣款或发送邮件。
        order = {"order_id": f"order-{len(ledger) + 1}", "item": item}
        # 幂等账本必须在副作用结果产生后持久化，供恢复后的重复调用读取。
        ledger[tool_call_id] = order
        self.ledger_path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
        return {**order, "replayed": False}

    def _load(self) -> dict[str, Any]:
        if not self.ledger_path.exists():
            return {}
        return json.loads(self.ledger_path.read_text(encoding="utf-8"))


def run_once(
    state: RunState,
    checkpoints: CheckpointStore,
    create_order: IdempotentOrderTool,
    *,
    simulate_crash: bool = False,
) -> RunState:
    if state.step == "create_order":
        # 工具调用 ID 必须稳定；同一个 run 恢复后仍生成同一个幂等键。
        tool_call_id = f"{state.run_id}:create_order"
        result = create_order.create(tool_call_id, state.input["item"])
        state.tool_results[tool_call_id] = result

        if simulate_crash:
            # 模拟：副作用已成功，但 checkpoint 还没推进到 complete，进程此时崩溃。
            raise RuntimeError("process interrupted after tool execution")

        # 工具完成后推进状态并保存 checkpoint，下一次无需重新执行已完成步骤。
        state.step = "complete"
        state.output = f"created {result['order_id']}"
        checkpoints.save(state)

    return state


def demo() -> None:
    # 为了让 Demo 可重复运行，使用本地 JSON 文件模拟外部状态存储。
    directory = Path(__file__).with_name(".demo-data")
    directory.mkdir(exist_ok=True)
    checkpoint_path = directory / "run.json"
    ledger_path = directory / "orders.json"
    for path in (checkpoint_path, ledger_path):
        path.unlink(missing_ok=True)

    # 第一次运行：先保存初始 Run State。
    state = RunState(run_id="run-1", input={"item": "book"})
    checkpoints = CheckpointStore(checkpoint_path)
    order_tool = IdempotentOrderTool(ledger_path)
    checkpoints.save(state)

    try:
        # 工具创建订单后故意中断，模拟 worker 崩溃。
        run_once(state, checkpoints, order_tool, simulate_crash=True)
    except RuntimeError as error:
        print(error)

    # 第二次运行：从 checkpoint 恢复；重复遇到同一工具调用。
    resumed = checkpoints.load()
    result = run_once(resumed, checkpoints, order_tool)
    tool_result = result.tool_results["run-1:create_order"]

    assert result.step == "complete"
    assert result.output == "created order-1"
    assert tool_result["replayed"] is True
    assert json.loads(ledger_path.read_text(encoding="utf-8")) == {
        "run-1:create_order": {"order_id": "order-1", "item": "book"}
    }
    print("resume demo passed:", result.output, "(side effect replayed safely)")


if __name__ == "__main__":
    demo()
