"""Run State, checkpoint/resume, and idempotent side-effect demo."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RunState:
    run_id: str
    step: str = "create_order"
    input: dict[str, Any] = field(default_factory=dict)
    tool_results: dict[str, Any] = field(default_factory=dict)
    output: str | None = None


class CheckpointStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def save(self, state: RunState) -> None:
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
        if tool_call_id in ledger:
            return {**ledger[tool_call_id], "replayed": True}

        order = {"order_id": f"order-{len(ledger) + 1}", "item": item}
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
        tool_call_id = f"{state.run_id}:create_order"
        result = create_order.create(tool_call_id, state.input["item"])
        state.tool_results[tool_call_id] = result

        if simulate_crash:
            # The side effect is durable, but the run has not advanced yet.
            raise RuntimeError("process interrupted after tool execution")

        state.step = "complete"
        state.output = f"created {result['order_id']}"
        checkpoints.save(state)

    return state


def demo() -> None:
    directory = Path(__file__).with_name(".demo-data")
    directory.mkdir(exist_ok=True)
    checkpoint_path = directory / "run.json"
    ledger_path = directory / "orders.json"
    for path in (checkpoint_path, ledger_path):
        path.unlink(missing_ok=True)

    state = RunState(run_id="run-1", input={"item": "book"})
    checkpoints = CheckpointStore(checkpoint_path)
    order_tool = IdempotentOrderTool(ledger_path)
    checkpoints.save(state)

    try:
        run_once(state, checkpoints, order_tool, simulate_crash=True)
    except RuntimeError as error:
        print(error)

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
