"""覆盖四条边界和模型故障路径。"""

import asyncio
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx

from credentials import CredentialBroker
from model_client import ModelClient, ModelUnavailable
from network_policy import validate_model_url
from sandbox_fs import Workspace
from sandbox_shell import command_for
from worker import analyze_project


class SecurityTests(unittest.TestCase):
    def test_workspace_rejects_escape_and_symlink(self) -> None:
        with Workspace() as workspace, tempfile.TemporaryDirectory() as outside:
            workspace.add("main.py", b"print(1)\n")
            self.assertEqual(workspace.read("main.py"), "print(1)\n")
            self.assertRaises(ValueError, workspace.read, "../secret")
            self.assertRaises(ValueError, workspace.read, "/etc/passwd")
            (workspace.root / "link").symlink_to(Path(outside))
            self.assertRaises(ValueError, workspace.read, "link/secret")

    def test_shell_only_maps_fixed_commands(self) -> None:
        self.assertEqual(command_for("syntax")[:2], ["python", "-c"])
        self.assertRaises(ValueError, command_for, "rm -rf /")

    def test_network_rejects_wrong_host_and_private_ip(self) -> None:
        self.assertRaises(
            ValueError,
            validate_model_url,
            "http://169.254.169.254/v1",
            "169.254.169.254",
        )
        self.assertRaises(
            ValueError, validate_model_url, "http://127.0.0.1/v1", "api.example.org"
        )
        validate_model_url("http://127.0.0.1:8000/v1", "127.0.0.1", allow_loopback=True)

    def test_credential_is_required_and_never_sent_in_prompt(self) -> None:
        async def scenario() -> None:
            captured = {}

            def handler(request: httpx.Request) -> httpx.Response:
                captured["body"] = request.content.decode()
                captured["header"] = request.headers["authorization"]
                return httpx.Response(
                    200, json={"choices": [{"message": {"content": "report"}}]}
                )

            with patch.dict(os.environ, {"DAY27_MODEL_TOKEN": "test-secret"}):
                client = ModelClient(
                    "http://127.0.0.1:8000/v1",
                    "demo",
                    "127.0.0.1",
                    CredentialBroker(),
                    allow_loopback=True,
                    transport=httpx.MockTransport(handler),
                )
                try:
                    self.assertEqual(await client.analyze("print(1)"), "report")
                finally:
                    await client.close()
            self.assertEqual(captured["header"], "Bearer test-secret")
            self.assertNotIn("test-secret", captured["body"])
            with patch.dict(os.environ, {}, clear=True):
                self.assertRaises(PermissionError, CredentialBroker().authorization)

        asyncio.run(scenario())

    def test_worker_degrades_and_never_executes_model_text(self) -> None:
        async def scenario() -> None:
            class StubModel:
                async def analyze(self, source: str) -> str:
                    self.assert_source = source
                    return "rm -rf /"

            with Workspace() as workspace, tempfile.TemporaryDirectory() as logs:
                workspace.add("main.py", b"print(1)\n")
                audit = Path(logs) / "audit.jsonl"
                with patch("worker.run_check", return_value="syntax ok"):
                    result = await analyze_project(
                        workspace, "main.py", StubModel(), audit
                    )
                self.assertEqual(result["report"], "rm -rf /")
                self.assertEqual(result["status"], "ok")

                class OfflineModel:
                    async def analyze(self, source: str) -> str:
                        raise ModelUnavailable("offline")

                with patch("worker.run_check", return_value="syntax ok"):
                    degraded = await analyze_project(
                        workspace, "main.py", OfflineModel(), audit
                    )
                self.assertEqual(degraded["status"], "degraded")
                self.assertNotIn("print(1)", audit.read_text())
                self.assertNotIn("rm -rf", audit.read_text())

        asyncio.run(scenario())


if __name__ == "__main__":
    unittest.main()
