"""复用 Day 32 审批和删除工具，生成独立的持久化审计事件。"""

import argparse
from pathlib import Path

from observability_deployment.day32_security_guardrails_hitl.demo import (
    ApprovalStore,
    AuditLog,
    SecureAgentService,
    execute_delete,
)


def run_audit_demo(state_dir: Path) -> Path:
    """演示一次拒绝和一次批准后的工具执行。

    Args:
        state_dir: 保存审批状态和审计 JSONL 文件的目录。

    Returns:
        独立审计文件的路径。
    """
    state_dir.mkdir(parents=True, exist_ok=True)
    audit_path = state_dir / "audit.jsonl"
    store = ApprovalStore(state_dir / "approvals.json", AuditLog(audit_path))
    service = SecureAgentService(store)

    rejected_id = service.handle_request(
        "demo-user", "删除资源: secret-resource-1"
    ).split(":", 1)[1]
    store.decide(rejected_id, approved=False)

    approved_id = service.handle_request(
        "demo-user", "删除资源: secret-resource-2"
    ).split(":", 1)[1]
    store.decide(approved_id, approved=True)
    execute_delete(store.get(approved_id), store)
    return audit_path


def main() -> None:
    """解析状态目录参数并运行审计演示。"""
    parser = argparse.ArgumentParser(description="Day 34 审批审计演示")
    parser.add_argument(
        "--state-dir", type=Path, required=True, help="审批和审计文件目录"
    )
    args = parser.parse_args()
    print(run_audit_demo(args.state_dir))


if __name__ == "__main__":
    main()
