"""持久化退款工作流：SQLite 队列 + LangGraph Checkpoint + 人工审批。"""

from __future__ import annotations

import argparse
import json
import sqlite3
import uuid
from pathlib import Path
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class RefundState(TypedDict, total=False):
    """Checkpoint 中的最小业务状态；不保存凭据或用户隐私。"""

    task_id: str
    thread_id: str
    order_id: str
    approval_status: str
    result: str
    error_type: str


ORDERS = {"order-1": {"paid": True, "refunded": False}, "order-2": {"paid": False, "refunded": False}}


def connect(path: Path) -> sqlite3.Connection:
    """打开本地状态库并建表。

    参数：path 是队列、审批和幂等执行记录共用的 SQLite 文件路径。
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY, thread_id TEXT UNIQUE NOT NULL,
            order_id TEXT NOT NULL, status TEXT NOT NULL,
            approval_id TEXT UNIQUE, decision TEXT, attempts INTEGER NOT NULL DEFAULT 0,
            error_type TEXT, result TEXT
        );
        CREATE TABLE IF NOT EXISTS deliveries (
            id INTEGER PRIMARY KEY, task_id TEXT NOT NULL, status TEXT NOT NULL,
            FOREIGN KEY(task_id) REFERENCES tasks(task_id)
        );
        CREATE TABLE IF NOT EXISTS refunds (
            task_id TEXT PRIMARY KEY, order_id TEXT NOT NULL,
            FOREIGN KEY(task_id) REFERENCES tasks(task_id)
        );
    """)
    return db


def build_graph(db: sqlite3.Connection, checkpointer: SqliteSaver):
    """构建只在审批通过后执行 Mock 写入的图。

    参数：db 是业务状态库；checkpointer 是独立的持久化图状态存储。
    """
    def inspect(state: RefundState) -> RefundState:
        """读取假订单并决定是否需要审批。"""
        order = ORDERS.get(state["order_id"])
        if not order or not order["paid"] or order["refunded"]:
            return {"result": "ineligible"}
        return {"result": "eligible"}

    def route(state: RefundState) -> str:
        """不符合规则的订单直接结束。"""
        return "approve" if state["result"] == "eligible" else END

    def approve(state: RefundState) -> RefundState:
        """暂停并等待外部审批；中断前不得产生写入副作用。"""
        decision = interrupt({"task_id": state["task_id"], "order_id": state["order_id"], "action": "mock_refund"})
        return {"approval_status": "approved" if decision is True else "rejected"}

    def after_approval(state: RefundState) -> str:
        """拒绝分支不得到达写工具。"""
        return "refund" if state["approval_status"] == "approved" else END

    def refund(state: RefundState) -> RefundState:
        """用任务 ID 作幂等键；已写入时再次执行不会新增退款。"""
        with db:
            db.execute("INSERT OR IGNORE INTO refunds(task_id, order_id) VALUES (?, ?)", (state["task_id"], state["order_id"]))
        return {"result": "refunded"}

    graph = StateGraph(RefundState)
    graph.add_node("inspect", inspect)
    graph.add_node("approve", approve)
    graph.add_node("refund", refund)
    graph.add_edge(START, "inspect")
    graph.add_conditional_edges("inspect", route)
    graph.add_conditional_edges("approve", after_approval)
    graph.add_edge("refund", END)
    return graph.compile(checkpointer=checkpointer)


def submit(db: sqlite3.Connection, order_id: str) -> str:
    """创建任务并入持久化队列，不在请求入口执行图。

    参数：order_id 是假订单 ID；返回新建 task_id。
    """
    task_id = uuid.uuid4().hex
    with db:
        db.execute("INSERT INTO tasks(task_id, thread_id, order_id, status) VALUES (?, ?, ?, 'queued')", (task_id, task_id, order_id))
        db.execute("INSERT INTO deliveries(task_id, status) VALUES (?, 'queued')", (task_id,))
    return task_id


def decide(db: sqlite3.Connection, task_id: str, approved: bool) -> None:
    """记录一次审批决定并重新入队；只接受待审批任务。

    参数：task_id 指向待审批任务；approved 为批准或拒绝。
    """
    with db:
        task = db.execute("SELECT status FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        if not task or task["status"] != "pending_approval":
            raise ValueError("task is not pending approval")
        db.execute("UPDATE tasks SET status='queued', decision=? WHERE task_id=?", ("approved" if approved else "rejected", task_id))
        db.execute("INSERT INTO deliveries(task_id, status) VALUES (?, 'queued')", (task_id,))


def recover(db: sqlite3.Connection) -> int:
    """单 Worker 重启时把未确认投递重新放回队列；返回恢复数。"""
    with db:
        count = db.execute("UPDATE deliveries SET status='queued' WHERE status='running'").rowcount
        db.execute("UPDATE tasks SET status='queued' WHERE status='running'")
    return count


def work_once(db: sqlite3.Connection, graph, *, fail: str = "") -> str | None:
    """消费一条投递，处理暂停/成功/失败，并限制工具重试。

    参数：db 是状态库；graph 是已编译工作流；fail 可选
    `before_write`、`after_write` 或 `worker_crash`，用于故障演练。
    返回 task_id；队列为空时返回 None。`worker_crash` 故意留下 running 投递。
    """
    with db:
        delivery = db.execute("SELECT id, task_id FROM deliveries WHERE status='queued' ORDER BY id LIMIT 1").fetchone()
        if delivery is None:
            return None
        task_id = delivery["task_id"]
        task = db.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        db.execute("UPDATE deliveries SET status='running' WHERE id=?", (delivery["id"],))
        if task["status"] in ("completed", "rejected", "failed") or task["status"] == "pending_approval":
            db.execute("UPDATE deliveries SET status='done' WHERE id=?", (delivery["id"],))
            return task_id
        db.execute("UPDATE tasks SET status='running' WHERE task_id=?", (task_id,))

    config = {"configurable": {"thread_id": task["thread_id"]}}
    try:
        if fail == "worker_crash":
            raise SystemExit("simulated worker crash")
        existing = graph.get_state(config)
        if existing and existing.created_at and not existing.next and not existing.interrupts:
            pass  # 图已完成但确认前崩溃；只回填业务状态。
        elif task["decision"] is None:
            graph.invoke({"task_id": task_id, "thread_id": task["thread_id"], "order_id": task["order_id"]}, config)
        else:
            # 真实执行由图推进；故障注入仅用于可重复的恢复演练。
            if fail == "before_write":
                raise TimeoutError("simulated tool timeout before write")
            graph.invoke(Command(resume=task["decision"] == "approved"), config)
            if fail == "after_write":
                raise SystemExit("simulated worker crash after write, before acknowledgement")
        snapshot = graph.get_state(config)
        state = snapshot.values
        status = "pending_approval" if snapshot.interrupts else ("rejected" if state.get("approval_status") == "rejected" else "completed")
        approval_id = task["approval_id"] or (uuid.uuid4().hex if status == "pending_approval" else None)
        with db:
            db.execute("UPDATE tasks SET status=?, approval_id=?, result=?, error_type=NULL WHERE task_id=?", (status, approval_id, state.get("result"), task_id))
            db.execute("UPDATE deliveries SET status='done' WHERE id=?", (delivery["id"],))
    except TimeoutError:
        with db:
            attempts = task["attempts"] + 1
            status = "failed" if attempts >= 2 else "queued"
            db.execute("UPDATE tasks SET status=?, attempts=?, error_type='TimeoutError' WHERE task_id=?", (status, attempts, task_id))
            db.execute("UPDATE deliveries SET status=? WHERE id=?", ("done" if status == "failed" else "queued", delivery["id"]))
    return task_id


def inspect_task(db: sqlite3.Connection, graph, task_id: str) -> dict:
    """按 task_id 查询队列、审批、写入数和图快照。"""
    task = db.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchone()
    if task is None:
        raise ValueError("unknown task")
    snapshot = graph.get_state({"configurable": {"thread_id": task["thread_id"]}})
    return {**dict(task), "refund_count": db.execute("SELECT count(*) FROM refunds WHERE task_id=?", (task_id,)).fetchone()[0], "checkpoint_next": list(snapshot.next) if snapshot else [], "checkpoint_interrupted": bool(snapshot.interrupts) if snapshot else False, "checkpoint_values": dict(snapshot.values) if snapshot else {}}


def main() -> None:
    """提供 submit/work/approve/reject/status/recover 命令供手工演练。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(".day38-state"))
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("submit").add_argument("order_id")
    worker = sub.add_parser("work")
    worker.add_argument("--fail", choices=["before_write", "after_write", "worker_crash"], default="")
    for name in ("approve", "reject", "status"):
        sub.add_parser(name).add_argument("task_id")
    sub.add_parser("recover")
    args = parser.parse_args()
    with connect(args.state_dir / "queue.db") as db, sqlite3.connect(args.state_dir / "checkpoints.db", check_same_thread=False) as checkpoint_db:
        graph = build_graph(db, SqliteSaver(checkpoint_db))
        if args.action == "submit":
            result = {"task_id": submit(db, args.order_id)}
        elif args.action == "work":
            result = {"task_id": work_once(db, graph, fail=args.fail)}
        elif args.action in ("approve", "reject"):
            decide(db, args.task_id, args.action == "approve")
            result = inspect_task(db, graph, args.task_id)
        elif args.action == "recover":
            result = {"requeued": recover(db)}
        else:
            result = inspect_task(db, graph, args.task_id)
        print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
