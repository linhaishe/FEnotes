"""LangGraph + Gemini demo for state, resume, and idempotent side effects.

Install:
    pip install -U langchain langchain-google-genai langgraph

Run with:
    GEMINI_API_KEY=... python day24_state_resume/demo_langchain_gemini.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph


class State(TypedDict, total=False):
    """LangGraph 在节点之间传递、并由 checkpoint 保存的运行状态。"""

    # 一次运行的稳定 ID，用于生成工具幂等键。
    run_id: str
    # 用户要求创建的商品。
    item: str
    # Gemini 生成的计划或确认结果。
    plan: str
    # 有副作用工具的执行结果。
    order: dict[str, Any]


class IdempotentOrderTool:
    """A side-effecting tool that executes once per stable tool-call ID."""

    def __init__(self, path: Path) -> None:
        """创建工具。

        Args:
            path: 保存幂等键和订单结果的 JSON 账本路径。
        """
        self.path = path

    def invoke(self, tool_call_id: str, item: str) -> dict[str, Any]:
        """创建订单；相同工具调用 ID 重复执行时返回原结果。

        Args:
            tool_call_id: 稳定的工具调用 ID，必须跨 resume 保持不变。
            item: 要创建的商品名称。

        Returns:
            订单结果，并用 ``replayed`` 标记是否命中了幂等记录。
        """
        ledger = self._load()
        if tool_call_id in ledger:
            return {**ledger[tool_call_id], "replayed": True}

        order = {"order_id": f"order-{len(ledger) + 1}", "item": item}
        ledger[tool_call_id] = order
        self.path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
        return {**order, "replayed": False}

    def _load(self) -> dict[str, Any]:
        """读取幂等账本；Demo 使用 JSON 模拟外部持久化存储。"""
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))


def build_graph(order_tool: IdempotentOrderTool):
    """构建带 checkpoint 的 LangGraph。

    Args:
        order_tool: 执行创建订单副作用的幂等工具。

    Returns:
        编译后的 LangGraph；使用 ``thread_id`` 区分不同运行。
    """
    # Gemini 负责 Agent 的模型步骤；LangGraph 负责状态、节点和恢复。
    model = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
        temperature=0,
    )

    def plan(state: State) -> State:
        """调用 Gemini 生成商品计划，并把结果写入 Run State。"""
        response = model.invoke(f"确认用户要创建的商品，只回复商品名：{state['item']}")
        content = response.content
        return {"plan": content if isinstance(content, str) else str(content)}

    def create_order(state: State) -> State:
        """执行副作用工具，并模拟一次执行后的进程崩溃。"""
        # run_id + 工具名是稳定幂等键；LangGraph 恢复重跑此节点时不会重复下单。
        result = order_tool.invoke(f"{state['run_id']}:create_order", state["item"])

        # 模拟“副作用已完成，但节点还没来得及返回/写完新 checkpoint”。
        crash_marker = order_tool.path.with_suffix(".crashed")
        if os.getenv("SIMULATE_CRASH") == "1" and not crash_marker.exists():
            crash_marker.touch()
            raise RuntimeError("simulated crash after order creation")
        return {"order": result}

    graph = StateGraph(State)
    graph.add_node("plan", plan)
    graph.add_node("create_order", create_order)
    graph.add_edge(START, "plan")
    graph.add_edge("plan", "create_order")
    graph.add_edge("create_order", END)
    return graph.compile(checkpointer=MemorySaver())


def demo() -> None:
    """运行完整 Demo：首次失败，随后从 checkpoint 恢复。

    环境变量：
        GEMINI_API_KEY: Gemini API 密钥，由 LangChain Google 集成读取。
        GEMINI_MODEL: Gemini 模型名，可选，默认 ``gemini-2.0-flash``。
    """
    # JSON 文件分别模拟外部订单系统和“已执行工具”账本。
    data_dir = Path(__file__).with_name(".langchain-demo-data")
    data_dir.mkdir(exist_ok=True)
    ledger = data_dir / "orders.json"
    crash_marker = ledger.with_suffix(".crashed")
    ledger.unlink(missing_ok=True) # 删除旧文件，再重新创建。
    crash_marker.unlink(missing_ok=True)

    graph = build_graph(IdempotentOrderTool(ledger))
    config = {"configurable": {"thread_id": "run-1"}}
    initial_state: State = {"run_id": "run-1", "item": "book"}

    os.environ["SIMULATE_CRASH"] = "1"
    try:
        graph.invoke(initial_state, config)
    except RuntimeError as error:
        print(error)
    finally:
        os.environ.pop("SIMULATE_CRASH", None)

    # 使用相同 thread_id 恢复；LangGraph 从最近 checkpoint 重跑失败节点。
    resumed = graph.invoke(None, config)
    assert resumed["order"] == {
        "order_id": "order-1",
        "item": "book",
        "replayed": True,
    }
    assert json.loads(ledger.read_text(encoding="utf-8")) == {
        "run-1:create_order": {"order_id": "order-1", "item": "book"}
    }
    print("LangChain/Gemini resume demo passed:", resumed["order"])


if __name__ == "__main__":
    demo()
