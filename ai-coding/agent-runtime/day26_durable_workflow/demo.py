"""Minimal LangGraph durable execution demo."""

from __future__ import annotations

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class RefundState(TypedDict, total=False):
    """The serializable state persisted for one refund workflow."""

    order_id: str
    amount: int
    approved: bool
    status: str


def prepare_refund(state: RefundState) -> dict[str, str]:
    """Prepare a refund request.

    Parameters:
        state: Current workflow state containing ``order_id`` and ``amount``.

    Returns:
        A state update marking the request as waiting for approval.
    """
    return {"status": f"waiting_for_approval:{state['order_id']}"}


def request_approval(state: RefundState) -> dict[str, bool | str]:
    """Pause for human approval and persist the response in graph state.

    Parameters:
        state: Current refund request and its approval status.

    Returns:
        A state update containing the approval decision and next status.
    """
    decision = interrupt(
        {
            "message": "Approve refund?",
            "order_id": state["order_id"],
            "amount": state["amount"],
        }
    )
    approved = bool(decision["approved"])
    return {"approved": approved, "status": "approved" if approved else "rejected"}


def complete_refund(state: RefundState) -> dict[str, str]:
    """Complete an approved refund.

    Parameters:
        state: State containing the approval decision and order ID.

    Returns:
        A state update marking the refund as completed.
    """
    if not state["approved"]:
        return {"status": "rejected"}
    # Real payment calls belong here and must use a stable idempotency key.
    return {"status": f"refunded:{state['order_id']}"}


def build_workflow() -> tuple[object, InMemorySaver]:
    """Build and compile the graph with a checkpoint store.

    Returns:
        The compiled graph and the checkpointer used by this demo.
    """
    checkpointer = InMemorySaver()
    builder = StateGraph(RefundState)
    builder.add_node("prepare", prepare_refund)
    builder.add_node("approval", request_approval)
    builder.add_node("complete", complete_refund)
    builder.add_edge(START, "prepare")
    builder.add_edge("prepare", "approval")
    builder.add_edge("approval", "complete")
    builder.add_edge("complete", END)
    return builder.compile(checkpointer=checkpointer), checkpointer


def demo() -> None:
    """Pause once, then resume the same workflow using its thread ID."""
    app, _ = build_workflow()
    config = {"configurable": {"thread_id": "refund-order-42"}}
    paused = app.invoke({"order_id": "order-42", "amount": 100}, config)
    assert paused["status"] == "waiting_for_approval:order-42"

    resumed = app.invoke(Command(resume={"approved": True}), config)
    assert resumed["status"] == "refunded:order-42"
    print("durable workflow resumed:", resumed["status"])


if __name__ == "__main__":
    demo()
