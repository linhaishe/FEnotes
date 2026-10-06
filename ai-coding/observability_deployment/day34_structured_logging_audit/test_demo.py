"""验证每个 Agent 请求都有可关联且不泄露 Prompt 的 JSON 日志。"""

import io
import json
import logging
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from fastapi.testclient import TestClient
from langsmith import trace
from langsmith.run_helpers import get_current_run_tree
from langsmith.run_helpers import tracing_context

from demo import app, logger


class RequestLoggingTests(unittest.TestCase):
    """验证请求 ID、响应和运行日志的一致性。"""

    def capture_request(self, prompt: str, backend: str = "mock"):
        """发送请求并收集本次请求的 JSON 日志。

        Args:
            prompt: 测试请求输入。
            backend: 本次请求使用的 Agent 后端。

        Returns:
            HTTP 响应和解析后的日志事件列表。
        """
        output = io.StringIO()
        handler = logging.StreamHandler(output)
        logger.addHandler(handler)
        try:
            with patch("demo.LOG_FORMAT", "json"), patch.dict(os.environ, {"AGENT_BACKEND": backend}):
                with tracing_context(enabled="local"):
                    with TestClient(app) as client:
                        response = client.post("/agent", json={"prompt": prompt})
        finally:
            logger.removeHandler(handler)
        return response, [json.loads(line) for line in output.getvalue().splitlines()]

    def test_agent_request_logs_model_and_tool_success(self) -> None:
        """模型、工具和请求日志可通过同一个 ID 关联。"""
        response, records = self.capture_request("查询天气: 上海 sk-test-secret")

        self.assertEqual(response.status_code, 200)
        request_id = response.headers["X-Request-ID"]
        trace_id = response.headers["X-Trace-ID"]
        self.assertEqual(response.json()["request_id"], request_id)
        self.assertEqual(response.json()["trace_id"], trace_id)
        self.assertEqual(
            [record["event"] for record in records],
            [
                "model_call_started",
                "model_call_finished",
                "tool_call_started",
                "tool_call_finished",
                "agent_request_finished",
            ],
        )
        self.assertTrue(all(record["request_id"] == request_id for record in records))
        self.assertTrue(all(record["trace_id"] == trace_id for record in records))
        self.assertTrue(all("duration_ms" in record for record in records[1::2]))
        self.assertNotIn("sk-test-secret", json.dumps(records))
        self.assertTrue(all("prompt" not in record for record in records))

    def test_model_timeout_is_classified(self) -> None:
        """模型超时只记录错误分类，不泄露异常内容。"""
        with patch("demo.mock_model", side_effect=TimeoutError("sk-model-secret")):
            response, records = self.capture_request("任意请求")
        self.assertEqual(response.status_code, 503)
        self.assertTrue(all(record["trace_id"] == response.headers["X-Trace-ID"] for record in records))
        self.assertEqual(
            [record["event"] for record in records],
            ["model_call_started", "model_call_failed", "agent_request_finished"],
        )
        self.assertEqual(records[1]["error_type"], "timeout")
        self.assertGreaterEqual(records[1]["duration_ms"], 0)
        self.assertNotIn("sk-model-secret", json.dumps(records))

    def test_tool_error_is_classified(self) -> None:
        """工具异常被记录为 error，且不输出异常详情。"""
        with patch("demo.mock_weather", side_effect=ValueError("private result")):
            response, records = self.capture_request("查询天气: 上海")
        self.assertEqual(response.status_code, 503)
        self.assertTrue(all(record["trace_id"] == response.headers["X-Trace-ID"] for record in records))
        self.assertEqual(records[3]["event"], "tool_call_failed")
        self.assertEqual(records[3]["error_type"], "error")
        self.assertNotIn("private result", json.dumps(records))

    def test_real_agent_children_share_request_trace(self) -> None:
        """真实 Agent 入口内的模型和工具子 Trace 继承 HTTP 根 Trace。"""
        observed = {}

        class FakeAgent:
            async def ainvoke(self, inputs):
                """模拟 LangChain 在请求上下文内产生的模型和工具调用。"""
                root = get_current_run_tree()
                observed["root"] = root
                for name, run_type in (("model", "llm"), ("tool", "tool")):
                    with trace(name, run_type=run_type) as child:
                        observed[name] = child
                return {"messages": [SimpleNamespace(content="已完成")]}

        with patch("demo.build_real_agent", return_value=FakeAgent()):
            response, records = self.capture_request("查询天气: 上海", backend="deepseek")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["answer"], "已完成")
        trace_id = response.headers["X-Trace-ID"]
        self.assertEqual(str(observed["root"].trace_id), trace_id)
        for name in ("model", "tool"):
            self.assertEqual(observed[name].parent_run_id, observed["root"].id)
            self.assertEqual(str(observed[name].trace_id), trace_id)
        self.assertEqual(
            [record["event"] for record in records],
            ["agent_call_started", "agent_call_finished", "agent_request_finished"],
        )
        self.assertTrue(all(record["trace_id"] == trace_id for record in records))


if __name__ == "__main__":
    unittest.main()
