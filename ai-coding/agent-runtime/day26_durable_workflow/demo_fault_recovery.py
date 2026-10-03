"""Use a state graph, task queue, and SQLite state to recover a long job."""

from __future__ import annotations

import asyncio
import sqlite3
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class JobState(TypedDict, total=False):
    """Serializable workflow state stored in SQLite."""

    job_id: str
    status: str
    completed: list[str]


class DurableStore:
    """Persist workflow checkpoints and idempotent task results in SQLite."""

    def __init__(self, path: Path) -> None:
        self.db = sqlite3.connect(path)
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS checkpoints (
                job_id TEXT PRIMARY KEY, status TEXT NOT NULL, completed TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS task_results (
                task_id TEXT PRIMARY KEY, result TEXT NOT NULL
            );
            """
        )

    def save(self, state: JobState) -> None:
        """Save the current state.

        Parameters:
            state: Workflow state containing job ID, status, and completed tasks.
        """ 
        self.db.execute(
            "REPLACE INTO checkpoints VALUES (?, ?, ?)",
            (state["job_id"], state["status"], ",".join(state.get("completed", []))),
        )
        self.db.commit()

    def load(self, job_id: str) -> JobState:
        """Load a checkpoint by job ID.

        Parameters:
            job_id: Stable workflow identifier.

        Returns:
            The last persisted workflow state.
        """
        row = self.db.execute("SELECT status, completed FROM checkpoints WHERE job_id = ?", (job_id,)).fetchone()
        if row is None:
            return {"job_id": job_id, "status": "queued", "completed": []}
        return {"job_id": job_id, "status": row[0], "completed": [x for x in row[1].split(",") if x]}

    def get_task(self, task_id: str) -> str | None:
        """Return an idempotent task result, if the task already ran."""
        row = self.db.execute("SELECT result FROM task_results WHERE task_id = ?", (task_id,)).fetchone()
        return None if row is None else row[0]

    def save_task(self, task_id: str, result: str) -> None:
        """Persist one task result under its stable idempotency key."""
        self.db.execute("INSERT OR IGNORE INTO task_results VALUES (?, ?)", (task_id, result))
        self.db.commit()

    def close(self) -> None:
        """Close the SQLite connection."""
        self.db.close()


def build_state_machine():
    """Build the queued -> running -> completed state machine."""
    graph = StateGraph(JobState)
    graph.add_node("run_tasks", lambda state: {"status": "running"})
    graph.add_node("finish", lambda state: {"status": "completed"})
    graph.add_edge(START, "run_tasks")
    graph.add_edge("run_tasks", "finish")
    graph.add_edge("finish", END)
    return graph.compile()


async def execute_task(task_id: str, store: DurableStore, calls: list[str]) -> str:
    """Execute one queued task exactly once from the workflow's point of view.

    Parameters:
        task_id: Stable task ID used as the idempotency key.
        store: SQLite-backed durable store.
        calls: Mutable list used to observe real side-effect executions.

    Returns:
        The persisted or newly created task result.
    """
    existing = store.get_task(task_id)
    if existing is not None:
        return existing
    await asyncio.sleep(0.01)
    calls.append(task_id)  # Represents an external side effect.
    result = f"done:{task_id}"
    store.save_task(task_id, result)
    return result


async def run_worker(job_id: str, store: DurableStore, *, crash_after: int | None = None) -> None:
    """Consume a bounded task queue and optionally simulate a worker crash.

    Parameters:
        job_id: Stable workflow identifier.
        store: SQLite-backed checkpoint and result store.
        crash_after: Crash after this many queue items, or ``None`` to finish.
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
    processed = 0
    while True:
        task_id = await queue.get()
        if task_id == "__done__":
            queue.task_done()
            break
        await execute_task(task_id, store, calls)
        processed += 1
        if crash_after == processed:
            raise RuntimeError("worker crashed after task side effect")
        state["completed"].append(task_id)
        store.save(state)
        queue.task_done()
    await producer
    state["status"] = "completed"
    store.save(state)
    print("worker side effects:", calls)


async def demo() -> None:
    """Crash once, restart, and verify durable recovery without duplication."""
    path = Path(__file__).with_name("durable-demo.sqlite")
    path.unlink(missing_ok=True)
    store = DurableStore(path)
    graph = build_state_machine()
    graph.invoke({"job_id": "job-1", "status": "queued", "completed": []})
    try:
        await run_worker("job-1", store, crash_after=1)
    except RuntimeError as error:
        print(error)
    await run_worker("job-1", store)
    state = store.load("job-1")
    assert state["status"] == "completed"
    assert state["completed"] == ["task-0", "task-1", "task-2"]
    assert [store.get_task(f"task-{i}") for i in range(3)] == ["done:task-0", "done:task-1", "done:task-2"]
    print("recovery verified:", state)
    store.close()
    path.unlink(missing_ok=True)


if __name__ == "__main__":
    asyncio.run(demo())
