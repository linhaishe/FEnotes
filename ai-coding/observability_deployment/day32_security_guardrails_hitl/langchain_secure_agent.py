"""把 Day 32 Guardrails 和 HITL 包装到 LangChain Agent 的示例。"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_deepseek import ChatDeepSeek

from demo import (
    ApprovalStore,
    AuditLog,
    GuardrailBlocked,
    check_external_content,
    check_input,
    check_output,
    validate_tool_call,
)

load_dotenv(Path(__file__).with_name(".env"), override=True)


def build_secure_agent(approval_store: ApprovalStore):
    """创建带输入、工具和输出安全边界的 LangChain Agent。

    Args:
        approval_store: 用于保存高风险工具审批请求的存储对象。

    Returns:
        注册了安全工具包装器的 LangChain Agent。

    Raises:
        RuntimeError: 未配置 ``DEEPSEEK_API_KEY`` 时抛出。
    """
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is not set")
    model = ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=api_key,
        temperature=0,
    )
    return create_agent(
        model=model,
        tools=[
            secure_weather,
            secure_transfer_money,
            make_secure_delete_tool(approval_store),
        ],
    )


@tool
def secure_weather(user_id: str, city: str) -> str:
    """经过权限和参数检查后查询 Mock 天气。

    Args:
        user_id: 当前用户标识，用于权限审计。
        city: 要查询的城市。

    Returns:
        固定天气结果。

    Raises:
        GuardrailBlocked: 参数或工具不符合安全策略时抛出。
    """
    validate_tool_call(user_id, "weather", {"city": city})
    return {"上海": "sunny", "北京": "cloudy"}.get(city, "unknown")


@tool
def secure_transfer_money(user_id: str, target_user_id: str, amount: float) -> str:
    """经过金额和用户归属校验的写操作工具。

    Args:
        user_id: 当前用户标识。
        target_user_id: 转账目标用户标识。
        amount: 转账金额，必须大于 0。

    Returns:
        Mock 转账结果。

    Raises:
        GuardrailBlocked: 金额非法或目标用户不属于当前用户时抛出。
    """
    validate_tool_call(
        user_id,
        "transfer_money",
        {"target_user_id": target_user_id, "amount": amount},
    )
    return "transfer accepted"


def make_secure_delete_tool(approval_store: ApprovalStore):
    """创建一个绑定审批存储的删除工具包装器。

    Args:
        approval_store: 审批请求存储对象。

    Returns:
        一个只创建审批请求、不执行删除的 LangChain 工具。
    """

    @tool
    def secure_delete_data(user_id: str, resource_id: str) -> str:
        """将删除请求转为人工审批，不直接执行删除。

        Args:
            user_id: 当前用户标识。
            resource_id: 待删除资源 ID。

        Returns:
            待审批请求 ID。
        """
        validate_tool_call(user_id, "delete_data", {"resource_id": resource_id})
        approval = approval_store.create(
            user_id=user_id,
            tool="delete_data",
            args={"resource_id": resource_id},
        )
        return f"pending approval: {approval.request_id}"

    return secure_delete_data


def run_secure_agent(
    agent: Any,
    user_id: str,
    prompt: str,
    external_content: str | None = None,
) -> str:
    """在输入和输出边界运行 LangChain Agent。

    Args:
        agent: 已创建的 LangChain Agent。
        user_id: 当前用户标识。
        prompt: 用户输入。
        external_content: 可选的网页或文档内容，必须先通过外部内容检查。

    Returns:
        经过输出脱敏的 Agent 最终答案。

    Raises:
        GuardrailBlocked: 输入 Guardrail 拦截请求时抛出。
    """
    # 入口 Guardrail：直接 Prompt Injection 在模型启动前被拦截。
    check_input(prompt)
    if external_content is not None:
        # 外部网页/文档是不可信数据，不能借此改变 Agent 权限。
        check_external_content(external_content)
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": f"当前用户 ID 是 {user_id}。高风险操作必须等待审批。",
                },
                {"role": "user", "content": prompt},
            ]
        }
    )
    # 输出 Guardrail：结果返回用户前统一脱敏。
    return check_output(result["messages"][-1].content)


def create_demo_agent() -> tuple[Any, ApprovalStore]:
    """创建用于应用接入的安全 Agent 和审批存储。

    Returns:
        ``(agent, approval_store)`` 元组。
    """
    state_dir = Path(os.getenv("AGENT_STATE_DIR", ".agent_state"))
    state_dir.mkdir(parents=True, exist_ok=True)
    audit = AuditLog(state_dir / "audit.jsonl")
    store = ApprovalStore(state_dir / "approvals.json", audit)
    return build_secure_agent(store), store
