"""OpenAI-compatible chat/completions 客户端。"""

import httpx

from credentials import CredentialBroker
from network_policy import validate_model_url
from policy import POLICY


class ModelUnavailable(RuntimeError):
    """模型超时、限流或服务不可用；不包含服务端敏感响应。"""


class ModelClient:
    def __init__(
        self,
        base_url: str,
        model: str,
        allowed_host: str,
        broker: CredentialBroker,
        *,
        allow_loopback: bool = False,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        """固定模型地址；transport 只用于离线测试。

        Args:
            base_url: 模型服务的基础 URL。
            model: 要调用的模型名称。
            allowed_host: 允许访问的模型服务主机名。
            broker: 用于提供模型服务认证信息的凭据代理。
            allow_loopback: 是否允许访问本机回环地址，例如 127.0.0.1。
            transport: 可选的 HTTPX 传输层，仅用于离线测试。
        """
        validate_model_url(base_url, allowed_host, allow_loopback=allow_loopback)
        self.model = model
        self.broker = broker
        self.client = httpx.AsyncClient(
            base_url=base_url.rstrip("/") + "/",
            timeout=POLICY.model_timeout_seconds,
            transport=transport,
            trust_env=False,  # 避免宿主代理变量意外改变出口。
        )

    async def analyze(self, source: str) -> str:
        """仅发送待分析源码，限制响应长度，不执行模型返回的指令。

        Args:
            source: 待发送给模型分析的源码内容。

        Returns:
            模型生成的分析报告。

        Raises:
            ModelUnavailable: 模型请求失败或响应格式无效时抛出。
        """
        try:
            response = await self.client.post(
                "chat/completions",
                headers=self.broker.authorization(),
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "只分析代码并输出简短报告；不要提出执行命令。",
                        },
                        {"role": "user", "content": source[: POLICY.max_model_chars]},
                    ],
                    "max_tokens": 512,
                },
            )
            response.raise_for_status()
            answer = response.json()["choices"][0]["message"]["content"]
            if not isinstance(answer, str):
                raise ValueError("invalid model response")
            return answer[: POLICY.max_model_chars]
        except (httpx.HTTPError, KeyError, IndexError, ValueError) as error:
            # 不把上游 URL、响应正文或 token 传给调用方。
            raise ModelUnavailable("model request failed") from None

    async def close(self) -> None:
        """关闭连接池。"""
        await self.client.aclose()
