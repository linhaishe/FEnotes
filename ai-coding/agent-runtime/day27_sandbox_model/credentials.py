"""凭据仅保留在 HTTP 客户端，不进入模型消息或审计事件。"""

import os


class CredentialBroker:
    """演示用最小接口；生产应改为外部短期凭据服务。"""

    def __init__(self, env_name: str = "DAY27_MODEL_TOKEN") -> None:
        self.env_name = env_name

    def authorization(self) -> dict[str, str]:
        """仅在发起请求时读取 token；缺失或撤销时拒绝调用。"""
        token = os.environ.get(self.env_name)
        if not token:
            raise PermissionError("model credential unavailable")
        return {"Authorization": f"Bearer {token}"}
