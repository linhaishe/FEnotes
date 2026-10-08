"""Day 38 的审批、重启、重复投递与故障恢复回归测试。"""

import sqlite3
import tempfile
import unittest
from pathlib import Path

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver

from demo import build_graph, connect, decide, inspect_task, recover, submit, work_once


class DurableWorkflowTest(unittest.TestCase):
    """使用临时磁盘库模拟不同进程重新创建连接。"""

    def setUp(self):
        """为每个用例创建独立的队列库和 Checkpoint 库。"""
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.open_service()

    def tearDown(self):
        """关闭连接并清理临时目录。"""
        self.close_service()
        self.temp.cleanup()

    def open_service(self):
        """重新打开持久化存储，模拟 API/Worker 重启。"""
        self.db = connect(self.root / "queue.db")
        self.checkpoint_db = sqlite3.connect(self.root / "checkpoints.db", check_same_thread=False)
        self.graph = build_graph(self.db, SqliteSaver(self.checkpoint_db))

    def close_service(self):
        """释放当前服务持有的数据库连接。"""
        self.db.close()
        self.checkpoint_db.close()

    def test_approve_after_restart_and_duplicate_delivery(self):
        """重启保留待审批状态，重复投递不会重复写入。"""
        task_id = submit(self.db, "order-1")
        self.assertEqual(work_once(self.db, self.graph), task_id)
        before = inspect_task(self.db, self.graph, task_id)
        self.assertEqual(before["status"], "pending_approval")
        self.assertTrue(before["checkpoint_interrupted"])
        self.assertEqual(before["refund_count"], 0)
        self.assertIsNotNone(before["approval_id"])
        self.close_service()
        self.open_service()
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["approval_id"], before["approval_id"])
        decide(self.db, task_id, True)
        work_once(self.db, self.graph)
        with self.db:
            self.db.execute("INSERT INTO deliveries(task_id,status) VALUES (?, 'queued')", (task_id,))
        work_once(self.db, self.graph)
        after = inspect_task(self.db, self.graph, task_id)
        self.assertEqual(after["status"], "completed")
        self.assertEqual(after["refund_count"], 1)
        self.assertEqual(after["checkpoint_values"]["approval_status"], "approved")

    def test_rejection_and_ineligible(self):
        """审批拒绝和不符合规则均不能调用写工具。"""
        task_id = submit(self.db, "order-1")
        work_once(self.db, self.graph)
        decide(self.db, task_id, False)
        work_once(self.db, self.graph)
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["status"], "rejected")
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["refund_count"], 0)
        other = submit(self.db, "order-2")
        work_once(self.db, self.graph)
        self.assertEqual(inspect_task(self.db, self.graph, other)["result"], "ineligible")
        self.assertEqual(inspect_task(self.db, self.graph, other)["refund_count"], 0)

    def test_timeout_retry_and_ack_loss(self):
        """写前超时可重试；写后确认丢失不重复写入。"""
        task_id = submit(self.db, "order-1")
        work_once(self.db, self.graph)
        decide(self.db, task_id, True)
        work_once(self.db, self.graph, fail="before_write")
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["status"], "queued")
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["refund_count"], 0)
        with self.assertRaises(SystemExit):
            work_once(self.db, self.graph, fail="after_write")
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["refund_count"], 1)
        self.close_service()
        self.open_service()
        self.assertEqual(recover(self.db), 1)
        work_once(self.db, self.graph)
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["status"], "completed")
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["refund_count"], 1)

    def test_retry_limit(self):
        """连续工具超时达到上限时进入明确失败状态。"""
        task_id = submit(self.db, "order-1")
        work_once(self.db, self.graph)
        decide(self.db, task_id, True)
        work_once(self.db, self.graph, fail="before_write")
        work_once(self.db, self.graph, fail="before_write")
        task = inspect_task(self.db, self.graph, task_id)
        self.assertEqual(task["status"], "failed")
        self.assertEqual(task["error_type"], "TimeoutError")
        self.assertEqual(task["refund_count"], 0)
        self.assertIsNone(work_once(self.db, self.graph))

    def test_worker_crash_requeues(self):
        """崩溃留下 running 投递，重启恢复后可继续。"""
        task_id = submit(self.db, "order-1")
        with self.assertRaises(SystemExit):
            work_once(self.db, self.graph, fail="worker_crash")
        self.close_service()
        self.open_service()
        self.assertEqual(recover(self.db), 1)
        work_once(self.db, self.graph)
        self.assertEqual(inspect_task(self.db, self.graph, task_id)["status"], "pending_approval")

    def test_wrong_thread_does_not_resume(self):
        """新 thread_id 找不到旧审批快照。"""
        task_id = submit(self.db, "order-1")
        work_once(self.db, self.graph)
        self.assertIsNone(self.graph.get_state({"configurable": {"thread_id": "new-thread"}}).created_at)

    def test_memory_checkpointer_is_not_durable(self):
        """替换内存 Checkpointer 后，旧工作流快照不会保留。"""
        first = build_graph(self.db, InMemorySaver())
        config = {"configurable": {"thread_id": "memory-only"}}
        first.invoke({"task_id": "memory-only", "thread_id": "memory-only", "order_id": "order-1"}, config)
        self.assertTrue(first.get_state(config).interrupts)
        second = build_graph(self.db, InMemorySaver())
        self.assertIsNone(second.get_state(config).created_at)


if __name__ == "__main__":
    unittest.main()
