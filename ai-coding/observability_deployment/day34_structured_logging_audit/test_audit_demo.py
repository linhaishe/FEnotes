"""验证 Day 34 演示复用 Day 32 审批流程并持久化独立审计事件。"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
