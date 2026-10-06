"""验证 Day 34 演示复用 Day 32 审批流程并持久化独立审计事件。"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from observability_deployment.day32_security_guardrails_hitl.demo import (  # noqa: E402
    ApprovalStore,
    AuditLog,
    SecureAgentService,
    execute_delete,
)


class AuditDemoTests(unittest.TestCase):
    """从命令行运行真实审批流程，检查审计文件而非 Mock 调用。"""

    def test_rejected_and_approved_deletes_have_separate_events(self) -> None:
        """拒绝不执行，批准后执行，四种事件均落入独立 JSONL 文件。"""
        root = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "observability_deployment.day34_structured_logging_audit.audit_demo",
                    "--state-dir",
                    directory,
                ],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            audit_path = Path(directory) / "audit.jsonl"
            events = [json.loads(line) for line in audit_path.read_text().splitlines()]
            self.assertEqual(
                [event["event"] for event in events],
                [
                    "approval_requested",
                    "approval_rejected",
                    "approval_requested",
                    "approval_approved",
                    "tool_executed",
                ],
            )
            self.assertEqual(events[0]["request_id"], events[1]["request_id"])
            self.assertEqual(events[2]["request_id"], events[4]["request_id"])
            self.assertNotEqual(events[0]["request_id"], events[2]["request_id"])
            self.assertNotIn("secret-resource", audit_path.read_text())

    def test_sensitive_approval_input_stays_out_of_audit_events(self) -> None:
        """真实审批状态变更写审计时不带凭据、PII 或完整请求。"""
        sensitive = "sk-test-do-not-log alice@example.test 13800138000"
        prompt = f"删除资源: {sensitive}"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit_path = root / "audit.jsonl"
            store = ApprovalStore(root / "approvals.json", AuditLog(audit_path))
            service = SecureAgentService(store)

            rejected_id = service.handle_request("demo-user", prompt).split(":", 1)[1]
            store.decide(rejected_id, approved=False)
            approved_id = service.handle_request("demo-user", prompt).split(":", 1)[1]
            store.decide(approved_id, approved=True)
            execute_delete(store.get(approved_id), store)

            raw_events = audit_path.read_text(encoding="utf-8")
            events = [json.loads(line) for line in raw_events.splitlines()]
            self.assertEqual(
                [event["event"] for event in events],
                [
                    "approval_requested",
                    "approval_rejected",
                    "approval_requested",
                    "approval_approved",
                    "tool_executed",
                ],
            )
            for value in (
                "sk-test-do-not-log",
                "alice@example.test",
                "13800138000",
                prompt,
            ):
                self.assertNotIn(value, raw_events)

    def test_request_id_reconstructs_rejected_approval_without_execution(self) -> None:
        """混合审计事件按审批 ID 分组后，拒绝链不会误含执行事件。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit_path = root / "audit.jsonl"
            store = ApprovalStore(root / "approvals.json", AuditLog(audit_path))
            service = SecureAgentService(store)
            rejected_id = service.handle_request("demo-user", "删除资源: r1").split(":", 1)[1]
            approved_id = service.handle_request("demo-user", "删除资源: r2").split(":", 1)[1]
            store.decide(rejected_id, approved=False)
            store.decide(approved_id, approved=True)
            execute_delete(store.get(approved_id), store)

            events = [json.loads(line) for line in audit_path.read_text().splitlines()]
            rejected_events = [event for event in events if event["request_id"] == rejected_id]
            approved_events = [event for event in events if event["request_id"] == approved_id]
            self.assertEqual(
                [event["event"] for event in rejected_events],
                ["approval_requested", "approval_rejected"],
            )
            self.assertEqual(store.get(rejected_id).status, "rejected")
            self.assertEqual(
                [event["event"] for event in approved_events],
                ["approval_requested", "approval_approved", "tool_executed"],
            )


if __name__ == "__main__":
    unittest.main()
