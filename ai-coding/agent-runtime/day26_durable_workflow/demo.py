"""LangGraph 持久化执行的最小 Demo。"""

from __future__ import annotations

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class RefundState(TypedDict, total=False):
    """一次退款工作流中持久化的可序列化状态。"""

    order_id: str
    amount: int
    approved: bool
    status: str


def prepare_refund(state: RefundState) -> dict[str, str]:
    """准备退款请求。

    Parameters:
        state: 当前工作流状态，包含 ``order_id`` 和 ``amount``。

    Returns:
        将请求标记为等待审批的状态更新。
    """
    return {"status": f"waiting_for_approval:{state['order_id']}"}


def request_approval(state: RefundState) -> dict[str, bool | str]:
    """暂停等待人工审批，并将响应持久化到图状态中。

    Parameters:
        state: 当前退款请求及其审批状态。

    Returns:
        包含审批决定和下一状态的状态更新。
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
    """完成已审批的退款。

    Parameters:
        state: 包含审批决定和订单 ID 的状态。

    Returns:
        将退款标记为已完成的状态更新。
    """
    if not state["approved"]:
        return {"status": "rejected"}
    # 真实的支付调用应放在这里，并且必须使用稳定的幂等键。
    return {"status": f"refunded:{state['order_id']}"}


def build_workflow() -> tuple[object, InMemorySaver]:
    """使用检查点存储构建并编译工作流图。

    Returns:
        编译后的工作流图，以及本 Demo 使用的检查点存储。
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
    """暂停一次，然后使用相同的 thread ID 恢复工作流。"""
    app, _ = build_workflow()
    config = {"configurable": {"thread_id": "refund-order-42"}}
    paused = app.invoke({"order_id": "order-42", "amount": 100}, config)
    assert paused["status"] == "waiting_for_approval:order-42" # 验证工作流是否成功暂停在“等待审批”状态
    """
    读取 paused 状态中的 status
    期望它等于 "waiting_for_approval:order-42"
    如果相等，程序继续执行
    如果不相等，抛出 AssertionError，说明工作流状态不符合预期
    """
    resumed = app.invoke(Command(resume={"approved": True}), config)
    assert resumed["status"] == "refunded:order-42"
    print("durable workflow resumed:", resumed["status"])


if __name__ == "__main__":
    demo()
