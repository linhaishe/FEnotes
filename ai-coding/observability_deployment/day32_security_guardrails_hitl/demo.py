"""Day 32：Guardrails、最小权限和 Human-in-the-loop 的可运行示例。"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

INJECTION_PATTERNS = (
    "忽略之前",
    "ignore previous",
    "泄露系统提示词",
    "导出所有用户数据",
)
SENSITIVE_PATTERN = re.compile(
    r"(?:sk-[A-Za-z0-9_-]+|api[_ -]?key\s*[:=]\s*\S+|"
    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|"
    r"(?<!\d)1[3-9]\d{9}(?!\d)|"
    r"internal system prompt\s*[:=]\s*.*|内部系统提示词\s*[:：]\s*.*)",
    re.I,
)


class GuardrailBlocked(Exception):
    """表示输入、工具或输出违反安全策略。"""


@dataclass
class Approval:
    """记录一次高风险工具审批请求。"""

    request_id: str
    user_id: str
    tool: str
    args: dict[str, Any]
    status: str = "pending_approval"


class AuditLog:
    """把安全事件写入 JSON Lines 审计日志。"""

    def __init__(self, path: Path) -> None:
        """初始化审计日志。

        Args:
            path: JSONL 审计文件路径。
        """
        self.path = path

    def write(self, event: str, **details: Any) -> None:
        """写入一条不包含原始敏感内容的审计事件。

        Args:
            event: 事件名称。
            details: 事件的结构化详情。
        """
        with self.path.open("a", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **details},
                    ensure_ascii=False,
                ) + "\n"
            )


def check_input(text: str) -> None:
    """检查用户输入，拦截直接 Prompt Injection。

    Args:
        text: 用户输入文本。

    Raises:
        GuardrailBlocked: 检测到已知注入模式时抛出。
    """
    if any(pattern.lower() in text.lower() for pattern in INJECTION_PATTERNS):
        raise GuardrailBlocked("input blocked")


def check_external_content(text: str) -> None:
    """检查外部网页或文档内容，避免其改变 Agent 权限。

    Args:
        text: 不可信的外部内容。

    Raises:
        GuardrailBlocked: 外部内容包含试图改变 Agent 指令的文本时抛出。
    """
    check_input(text)


def validate_tool_call(user_id: str, tool: str, args: dict[str, Any]) -> None:
    """在工具执行前校验最小权限和参数。

    Args:
        user_id: 当前用户标识。
        tool: 工具名称。
        args: 工具调用参数。

    Raises:
        GuardrailBlocked: 工具不存在、参数非法或用户无权访问时抛出。
    """
    if tool not in {"read_profile", "weather", "transfer_money", "delete_data"}:
        raise GuardrailBlocked("tool is not allowlisted")
    if tool == "read_profile" and args.get("user_id") != user_id:
        raise GuardrailBlocked("cross-user access blocked")
    if tool == "transfer_money":
        if args.get("amount", 0) <= 0:
            raise GuardrailBlocked("amount must be greater than zero")
        if args.get("target_user_id") != user_id:
            raise GuardrailBlocked("target user does not belong to current user")
    if tool == "delete_data" and not args.get("resource_id"):
        raise GuardrailBlocked("resource_id is required")


def check_output(text: str) -> str:
    """在返回用户前脱敏密钥、API Key 等敏感信息。

    Args:
        text: Agent 或工具产生的输出。

    Returns:
        脱敏后的安全文本。
    """
    return SENSITIVE_PATTERN.sub("[REDACTED]", text)


class ApprovalStore:
    """持久化待审批请求，模拟服务重启后的恢复。"""

    def __init__(self, path: Path, audit: AuditLog) -> None:
        """初始化审批存储。

        Args:
            path: 审批状态 JSON 文件路径。
            audit: 用于记录审批事件的审计日志。
        """
        self.path = path
        self.audit = audit

    def create(self, user_id: str, tool: str, args: dict[str, Any]) -> Approval:
        """创建待审批请求，不执行高风险工具。

        Args:
            user_id: 请求发起人。
            tool: 高风险工具名称。
            args: 已脱敏且待审批的工具参数。

        Returns:
            状态为 ``pending_approval`` 的审批对象。
        """
        approval = Approval(str(uuid4()), user_id, tool, args)
        self._save(approval)
        self.audit.write(
            "approval_requested", request_id=approval.request_id, tool=tool
        )
        return approval

    def decide(self, request_id: str, approved: bool) -> Approval:
        """批准或拒绝一个待审批请求。

        Args:
            request_id: 审批请求 ID。
            approved: 是否批准。

        Returns:
            更新状态后的审批对象。
        """
        approvals = self._load()
        approval = approvals[request_id]
        approval["status"] = "approved" if approved else "rejected"
        self._write_all(approvals)
        self.audit.write(
            "approval_approved" if approved else "approval_rejected",
            request_id=request_id,
            status=approval["status"],
        )
        return Approval(**approval)

    def get(self, request_id: str) -> Approval:
        """读取审批状态，用于恢复服务重启前的任务。

        Args:
            request_id: 审批请求 ID。

        Returns:
            持久化的审批对象。
        """
        return Approval(**self._load()[request_id])

    def _load(self) -> dict[str, dict[str, Any]]:
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, approval: Approval) -> None:
        approvals = self._load()
        approvals[approval.request_id] = approval.__dict__
        self._write_all(approvals)

    def _write_all(self, approvals: dict[str, dict[str, Any]]) -> None:
        self.path.write_text(
            json.dumps(approvals, ensure_ascii=False), encoding="utf-8"
        )


def execute_delete(approval: Approval, store: ApprovalStore) -> str:
    """在审批通过后再次校验并执行删除操作。

    Args:
        approval: 已持久化的审批对象。
        store: 审批存储，用于记录执行事件。

    Returns:
        执行结果。

    Raises:
        GuardrailBlocked: 审批不是 approved 状态时拒绝执行。
    """
    if approval.status != "approved":
        raise GuardrailBlocked("approval required")
    validate_tool_call(approval.user_id, approval.tool, approval.args)
    store.audit.write(
        "tool_executed", request_id=approval.request_id, tool=approval.tool
    )
    return "deleted"


class SecureAgentService:
    """生产请求入口：串联 Agent、工具和安全边界。"""

    def __init__(self, approval_store: ApprovalStore) -> None:
        """初始化安全 Agent 服务。

        Args:
            approval_store: 保存高风险操作审批状态的存储。
        """
        self.approval_store = approval_store

    def handle_request(
        self,
        user_id: str,
        prompt: str,
        external_content: str | None = None,
    ) -> str:
        """处理用户请求，并在工具执行前后应用安全策略。

        Args:
            user_id: 当前用户标识。
            prompt: 用户输入。
            external_content: 可选的网页或文档内容。

        Returns:
            安全处理后的响应，或待审批请求 ID。

        Raises:
            GuardrailBlocked: 输入或外部内容违反安全策略时抛出。
        """
        check_input(prompt)
        if external_content is not None:
            check_external_content(external_content)

        if prompt.startswith("查询天气:"):
            city = prompt.split(":", 1)[1].strip()
            validate_tool_call(user_id, "weather", {"city": city})
            return check_output({"上海": "sunny", "北京": "cloudy"}.get(city, "unknown"))

        if prompt.startswith("删除资源:"):
            resource_id = prompt.split(":", 1)[1].strip()
            validate_tool_call(user_id, "delete_data", {"resource_id": resource_id})
            approval = self.approval_store.create(
                user_id,
                "delete_data",
                {"resource_id": resource_id},
            )
            return f"pending_approval:{approval.request_id}"

        return check_output("request accepted without a tool")
