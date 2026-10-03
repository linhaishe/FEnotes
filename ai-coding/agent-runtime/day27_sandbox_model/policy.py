"""Day 27 的固定权限策略；模型输出不能修改这些值。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Policy:
    # 只开放一个不会执行项目源码的检查命令。需要更多命令时逐个审查后加入。
    commands: tuple[str, ...] = ("list", "syntax")
    max_file_bytes: int = 64 * 1024
    max_output_bytes: int = 16 * 1024
    shell_timeout_seconds: float = 10.0
    model_timeout_seconds: float = 20.0
    max_model_chars: int = 8000


POLICY = Policy()
