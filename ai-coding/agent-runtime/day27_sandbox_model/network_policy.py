"""固定模型地址的出口校验；任意 URL 不能由 Agent 自行决定。"""

import ipaddress
import socket
from urllib.parse import urlsplit


def validate_model_url(url: str, allowed_host: str, *, allow_loopback: bool = False) -> None:
    """检查 scheme、host 和所有 DNS 结果；本地开发需显式允许 loopback。

    这只是客户端入口检查。生产环境仍需容器/网络层 egress 策略，
    否则 DNS 重新解析和进程内其他 HTTP 库可能绕过本函数。
    """
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or parsed.hostname != allowed_host:
        raise ValueError("model endpoint not allowed")
    if parsed.username or parsed.password or parsed.fragment or parsed.path.rstrip("/") != "/v1":
        raise ValueError("invalid model endpoint")
    if parsed.scheme != "https" and not allow_loopback:
        raise ValueError("remote model endpoint requires HTTPS")
    addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])
        if not ip.is_global and not (allow_loopback and ip.is_loopback):
            raise ValueError("private model endpoint not allowed")
