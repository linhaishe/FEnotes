"""Day 35：验证模型/工具故障分类和脱敏报告。"""

import json
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from observability_deployment.day35_adversarial_testing_production_simulation.rehearsal import (
    create_app,
    generate_report,
    mock_model,
)


class FaultTests(unittest.TestCase):
    def setUp(self) -> None:
        """为故障演练准备独立的临时目录。"""
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.state_dir = Path(self.temp.name)

    def test_model_timeout_is_single_attempt_and_model_failure(self) -> None:
        """若模型重试或故障归因到工具，此测试应失败。"""
        attempts = []

        def timeout_model(prompt: str, fact: str | None):
            attempts.append(1)
            raise TimeoutError("sk-FAKE-SECRET alice@example.com")

        app = create_app(self.state_dir, model=timeout_model)
        with TestClient(app) as client:
            response = client.post("/agent", json={"prompt": "查询天气: 上海"})
            metrics = client.get("/metrics").text
        self.assertEqual(response.status_code, 503)
        self.assertEqual(len(attempts), 1)
        self.assertEqual(app.state.tool_calls, [])
        self.assertIn('agent_task_failures_total{source="model"} 1.0', metrics)
        events = [e for e in app.state.events if e["request_id"] == response.json()["request_id"]]
        self.assertEqual([e["event"] for e in events], [
            "model_call_started", "model_call_failed", "agent_request_finished",
        ])
        self.assertEqual(events[1]["error_type"], "timeout")
        self.assertNotIn("FAKE-SECRET", response.text + json.dumps(events))

    def test_tool_failure_is_classified_without_raw_exception(self) -> None:
        """若工具异常被归到模型或回显异常原文，此测试应失败。"""
        def failing_tool(name: str, args: dict):
            raise RuntimeError("sk-FAKE-SECRET 13800138000")

        app = create_app(self.state_dir, tool=failing_tool)
        with TestClient(app) as client:
            response = client.post("/agent", json={"prompt": "查询天气: 上海"})
            metrics = client.get("/metrics").text
        self.assertEqual(response.status_code, 503)
        self.assertIn('agent_task_failures_total{source="tool"} 1.0', metrics)
        self.assertIn('agent_tool_failures_total{error="error",tool="weather"} 1.0', metrics)
        events = [e for e in app.state.events if e["request_id"] == response.json()["request_id"]]
        self.assertEqual([e["event"] for e in events], [
            "model_call_started", "model_call_finished", "tool_call_started",
            "tool_call_failed", "agent_request_finished",
        ])
        self.assertNotIn("FAKE-SECRET", response.text + json.dumps(events))

    def test_sensitive_input_and_output_do_not_leak_to_events_or_spans(self) -> None:
        """若日志或本地 Trace 保存完整 Prompt/PII，此测试应失败。"""
        sensitive = "sk-FAKE-SECRET alice@example.com 13800138000"

        def response_model(prompt: str, fact: str | None):
            return sensitive

        app = create_app(self.state_dir, model=response_model)
        with TestClient(app) as client:
            response = client.post("/agent", json={"prompt": f"请回答 {sensitive}"})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("FAKE-SECRET", response.text)
        self.assertNotIn("alice@example.com", response.text)
        self.assertNotIn("13800138000", response.text)
        evidence = json.dumps(app.state.events + app.state.spans, ensure_ascii=False)
        self.assertNotIn("FAKE-SECRET", evidence)
        self.assertNotIn("alice@example.com", evidence)
        self.assertNotIn("13800138000", evidence)

    def test_report_contains_observed_mock_data_and_no_prompts(self) -> None:
        """若报告虚构观测证据或包含输入原文，此测试应失败。"""
        path = self.state_dir / "report.json"
        report = generate_report(path)
        self.assertEqual(report["schema_version"], 1)
        cases = {case["case_id"]: case for case in report["cases"]}
        self.assertEqual(len(cases), 11)
        self.assertTrue(all(case["passed"] for case in cases.values()))
        self.assertEqual(cases["weather_ok"]["http_status"], 200)
        self.assertEqual(cases["weather_ok"]["model_calls"], 1)
        self.assertEqual(cases["weather_ok"]["tool_calls"], 1)
        weather_spans = cases["weather_ok"]["trace_spans"]
        self.assertEqual([span["name"] for span in weather_spans], ["request", "model", "tool"])
        self.assertEqual(weather_spans[1]["parent_run_id"], weather_spans[0]["id"])
        self.assertGreaterEqual(cases["weather_ok"]["duration_ms"], 0)
        self.assertEqual(cases["approval_rejected"]["approval_events"], [
            "approval_requested", "approval_rejected",
        ])
        self.assertEqual(cases["model_timeout"]["error_type"], "timeout")
        self.assertEqual(cases["tool_failure"]["error_type"], "error")
        text = path.read_text(encoding="utf-8")
        self.assertNotIn("忽略之前指令", text)
        self.assertNotIn("查询天气: 上海", text)
        self.assertEqual(json.loads(text), report)


if __name__ == "__main__":
    unittest.main()
