"""Day 35：仅显式开启时运行的隔离 Docker 故障演练。"""

import json
import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from uuid import uuid4


REPO_ROOT = Path(__file__).resolve().parents[2]
RUN_DOCKER = os.getenv("DAY35_RUN_DOCKER") == "1"


@unittest.skipUnless(RUN_DOCKER, "set DAY35_RUN_DOCKER=1 for isolated Docker rehearsals")
class ServiceFailureTests(unittest.TestCase):
    def setUp(self) -> None:
        """分配专用 Compose 项目；清理只针对该项目。"""
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.compose_file = self.directory / "compose.yaml"
        self.project = "day35test" + uuid4().hex[:12]
        self.addCleanup(self.cleanup_project)

    def compose(self, *args: str) -> subprocess.CompletedProcess[str]:
        """在唯一项目名下运行 Compose 命令。

        Args:
            args: 传给 ``docker compose`` 的子命令和参数。

        Returns:
            带 stdout/stderr 的命令执行结果。
        """
        try:
            return subprocess.run(
                ["docker", "compose", "-p", self.project, "-f", str(self.compose_file), *args],
                check=True, text=True, capture_output=True, timeout=240,
            )
        except subprocess.CalledProcessError as exc:
            if "exec" in args:
                raise
            raise AssertionError(f"isolated Compose command failed: {exc.stderr}") from exc

    def cleanup_project(self) -> None:
        """仅删除本测试创建的容器与 Volume。"""
        if self.project.startswith("day35test") and self.compose_file.exists():
            self.compose("down", "--volumes", "--remove-orphans")

    def api_status(self) -> int:
        """从容器内读取 readiness HTTP 状态，不暴露宿主机端口。"""
        script = (
            "import urllib.request, urllib.error; "
            "url='http://127.0.0.1:8000/health/ready'; "
            "\ntry: print(urllib.request.urlopen(url, timeout=5).status)"
            "\nexcept urllib.error.HTTPError as exc: print(exc.code)"
        )
        return int(self.compose("exec", "-T", "api", "python", "-c", script).stdout.strip())

    def wait_ready(self) -> None:
        """等待 API 启动及 Redis 恢复，不无限等待。"""
        for _ in range(30):
            try:
                if self.api_status() == 200:
                    return
            except (subprocess.CalledProcessError, ValueError):
                pass
            time.sleep(1)
        self.fail("isolated API did not become ready: " + self.compose("logs", "--tail", "40", "api").stdout)

    def test_redis_outage_and_recovery_change_readiness(self) -> None:
        """若 Redis 停止后 readiness 仍为 200，此测试应失败。"""
        secret = self.directory / "fake_key.txt"
        secret.write_text("sk-FAKE-DAY35-ONLY", encoding="utf-8")
        self.compose_file.write_text(
            "services:\n"
            "  api:\n"
            f"    build:\n      context: {REPO_ROOT / 'observability_deployment/day33_containerization_service_orchestration'}\n"
            "      dockerfile: Dockerfile\n"
            "    environment:\n      REDIS_URL: redis://redis:6379/0\n"
            "      DEEPSEEK_API_KEY_FILE: /run/secrets/deepseek_api_key\n"
            "    secrets: [deepseek_api_key]\n"
            "    depends_on: [redis]\n"
            "  redis:\n    image: redis:7-alpine\n"
            "secrets:\n  deepseek_api_key:\n    file: ./fake_key.txt\n",
            encoding="utf-8",
        )
        self.compose("up", "-d", "--build")
        self.wait_ready()
        self.assertEqual(self.api_status(), 200)
        self.compose("stop", "redis")
        self.assertEqual(self.api_status(), 503)
        self.compose("start", "redis")
        self.wait_ready()
        self.assertEqual(self.api_status(), 200)

    def test_audit_volume_survives_api_restart(self) -> None:
        """若审计文件只存容器临时层，重启后查询将失败。"""
        self.compose_file.write_text(
            "services:\n"
            "  api:\n"
            f"    build:\n      context: {REPO_ROOT}\n"
            "      dockerfile: observability_deployment/day34_structured_logging_audit/Dockerfile\n"
            "    environment:\n      AGENT_BACKEND: mock\n      LANGSMITH_TRACING: 'false'\n"
            "    volumes: [audit_state:/data]\n"
            "volumes:\n  audit_state:\n",
            encoding="utf-8",
        )
        self.compose("up", "-d", "--build")
        self.compose("exec", "-T", "api", "python", "-m",
                     "observability_deployment.day34_structured_logging_audit.audit_demo",
                     "--state-dir", "/data")
        read_events = (
            "import json, pathlib; p=pathlib.Path('/data/audit.jsonl'); "
            "print(json.dumps([json.loads(x) for x in p.read_text().splitlines()]))"
        )
        before = json.loads(self.compose("exec", "-T", "api", "python", "-c", read_events).stdout)
        self.assertEqual([e["event"] for e in before], [
            "approval_requested", "approval_rejected", "approval_requested",
            "approval_approved", "tool_executed",
        ])
        self.compose("restart", "api")
        after = json.loads(self.compose("exec", "-T", "api", "python", "-c", read_events).stdout)
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
