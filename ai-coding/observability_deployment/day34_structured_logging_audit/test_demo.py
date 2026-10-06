"""验证每个 Agent 请求都有可关联且不泄露 Prompt 的 JSON 日志。"""

import io
import json
import logging
import unittest

from fastapi.testclient import TestClient

from demo import app, logger


class RequestLoggingTests(unittest.TestCase):
    """验证请求 ID、响应和运行日志的一致性。"""

    def test_agent_request_emits_one_json_log(self) -> None:
        """一次请求只产生一行 JSON 日志，且不记录敏感输入。"""
        output = io.StringIO()
        handler = logging.StreamHandler(output)
        logger.addHandler(handler)
        try:
            with TestClient(app) as client:
                response = client.post(
                    "/agent", json={"prompt": "我的密钥是 sk-test-secret"}
                )
        finally:
            logger.removeHandler(handler)

        self.assertEqual(response.status_code, 200)
        request_id = response.headers["X-Request-ID"]
        self.assertEqual(response.json()["request_id"], request_id)
        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 1)
        record = json.loads(lines[0])
        self.assertEqual(record["request_id"], request_id)
        self.assertEqual(record["event"], "agent_request_finished")
        self.assertEqual(record["status_code"], 200)
        self.assertNotIn("sk-test-secret", lines[0])
        self.assertNotIn("prompt", record)


if __name__ == "__main__":
    unittest.main()
