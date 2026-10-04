"""使用状态图、任务队列和 SQLite 状态恢复长任务。"""

from __future__ import annotations

import asyncio
import sqlite3
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class JobState(TypedDict, total=False):
    """存储在 SQLite 中的可序列化工作流状态。"""

    job_id: str
    status: str
    completed: list[str]


class DurableStore:
    """在 SQLite 中持久化工作流检查点和幂等任务结果。"""

    def __init__(self, path: Path) -> None:
        self.db = sqlite3.connect(path)
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS checkpoints (
                job_id TEXT PRIMARY KEY, status TEXT NOT NULL, completed TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS task_results (
                task_id TEXT PRIMARY KEY, result TEXT NOT NULL
            );
            """)

    def save(self, state: JobState) -> None:
        """保存当前状态。

        Parameters:
            state: 包含任务 ID、状态和已完成任务的工作流状态。
        """
        self.db.execute(
            "REPLACE INTO checkpoints VALUES (?, ?, ?)",
            (state["job_id"], state["status"], ",".join(state.get("completed", []))),
        )
        self.db.commit()

    def load(self, job_id: str) -> JobState:
        """根据任务 ID 加载检查点。

        Parameters:
            job_id: 稳定的工作流标识符。

        Returns:
            最近一次持久化的工作流状态。
        """
        row = self.db.execute(
            "SELECT status, completed FROM checkpoints WHERE job_id = ?", (job_id,)
        ).fetchone()
        if row is None:
            return {"job_id": job_id, "status": "queued", "completed": []}
        return {
            "job_id": job_id,
            "status": row[0],
            "completed": [x for x in row[1].split(",") if x],
        }

    def get_task(self, task_id: str) -> str | None:
        """如果任务已经执行过，则返回幂等任务结果。"""
        row = self.db.execute(
            "SELECT result FROM task_results WHERE task_id = ?", (task_id,)
        ).fetchone()
        return None if row is None else row[0]

    def save_task(self, task_id: str, result: str) -> None:
        """使用稳定的幂等键持久化一个任务结果。"""
        self.db.execute(
            "INSERT OR IGNORE INTO task_results VALUES (?, ?)", (task_id, result)
        )
        self.db.commit()

    def close(self) -> None:
        """关闭 SQLite 连接。"""
        self.db.close()


def build_state_machine():
    """构建 queued -> running -> completed 状态机。"""
    graph = StateGraph(JobState)
    graph.add_node("run_tasks", lambda state: {"status": "running"})
    graph.add_node("finish", lambda state: {"status": "completed"})
    graph.add_edge(START, "run_tasks")
    graph.add_edge("run_tasks", "finish")
    graph.add_edge("finish", END)
    return graph.compile()


async def execute_task(task_id: str, store: DurableStore, calls: list[str]) -> str:
    """从工作流角度看，仅执行一次排队中的任务。

    Parameters:
        task_id: 用作幂等键的稳定任务 ID。
        store: 基于 SQLite 的持久化存储。
        calls: 用于观察真实副作用执行情况的可变列表。

    Returns:
        已持久化或新创建的任务结果。
    """
    existing = store.get_task(task_id)
    if existing is not None:
        return existing
    await asyncio.sleep(0.01)
    calls.append(task_id)  # 代表一次外部副作用。
    result = f"done:{task_id}"
    store.save_task(task_id, result)
    return result


async def run_worker(
    job_id: str, store: DurableStore, *, crash_after: int | None = None
) -> None:
    """消费有界任务队列，并可选择模拟 Worker 崩溃。

    Parameters:
        job_id: 稳定的工作流标识符。
        store: 基于 SQLite 的检查点和结果存储。
        crash_after: 处理指定数量的队列项目后崩溃；为 ``None`` 时执行完成。
    """
    state = store.load(job_id)
    state["status"] = "running"
    store.save(state)
    queue: asyncio.Queue[str] = asyncio.Queue(maxsize=2)
    calls: list[str] = []
    tasks = [f"task-{i}" for i in range(3) if f"task-{i}" not in state["completed"]]

    async def produce() -> None:
        for task_id in tasks:
            await queue.put(task_id)
        await queue.put("__done__")

    producer = asyncio.create_task(produce())
    processed = 0  # 初始化已处理任务数量为 0
    while True:
        task_id = await queue.get()
        if task_id == "__done__":
            queue.task_done()
            break
        await execute_task(
            task_id, store, calls
        )  # 执行当前任务。如果任务已经执行过，会直接复用已有结果，避免重复执行外部副作用。
        processed += 1
        if (
            crash_after == processed
        ):  # 模拟 Worker 崩溃 表示第一个任务执行完成后立刻崩溃，用来测试故障恢复。
            raise RuntimeError("worker crashed after task side effect")
        state["completed"].append(task_id)
        store.save(state)
        queue.task_done()  # 通知队列：当前任务已经处理完成。
    await producer  # 等待生产者任务彻底结束，确保它已经把所有任务和结束标记放入队列。
    state["status"] = (
        "completed"  # 所有任务处理完成后，将工作流状态更新为 completed，并持久化保存。
    )
    store.save(state)
    print("worker side effects:", calls)


async def demo() -> None:
    """崩溃一次后重启，并验证持久化恢复不会造成重复执行。"""
    path = Path(__file__).with_name("durable-demo.sqlite")
    path.unlink(missing_ok=True)
    store = DurableStore(path)
    graph = build_state_machine()
    graph.invoke({"job_id": "job-1", "status": "queued", "completed": []})
    try:
        await run_worker("job-1", store, crash_after=1)
    except RuntimeError as error:  # except 捕获异常并打印错误，程序不会因此终止。
        print(error)
    await run_worker(
        "job-1", store
    )  # 重新启动 Worker，不再设置崩溃参数，让剩余任务继续执行。
    state = store.load("job-1")
    assert state["status"] == "completed"
    assert state["completed"] == ["task-0", "task-1", "task-2"]
    assert [store.get_task(f"task-{i}") for i in range(3)] == [
        "done:task-0",
        "done:task-1",
        "done:task-2",
    ]  # 确认三个任务的结果都已持久化到 SQLite 中。
    print("recovery verified:", state)
    store.close()
    path.unlink(
        missing_ok=True
    )  # 删除 Demo 运行过程中创建的 SQLite 文件。missing_ok=True 表示：如果文件已经不存在，也不要抛出异常。


"""
第一次执行
  ↓
task-0 执行后 Worker 崩溃
  ↓
捕获异常
  ↓
重新启动 Worker
  ↓
跳过已执行的副作用，继续完成任务
  ↓
验证最终状态和任务结果
  ↓
清理 SQLite 文件
"""

if __name__ == "__main__":
    asyncio.run(demo())
