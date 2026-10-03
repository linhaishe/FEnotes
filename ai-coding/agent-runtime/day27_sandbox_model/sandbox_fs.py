"""工作目录的文件入口；真正的进程隔离由容器负责。"""

from pathlib import Path
from tempfile import TemporaryDirectory

from policy import POLICY


class Workspace:
    """每次任务使用一个独立的临时目录。"""

    def __init__(self) -> None:
        self._temporary = TemporaryDirectory(prefix="day27-")
        self.root = Path(self._temporary.name).resolve()

    def resolve(self, relative: str) -> Path:
        """解析工作区内路径，拒绝绝对路径、遍历与符号链接逃逸。"""
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts or not path.parts:
            raise ValueError("path outside workspace")
        target = (self.root / path).resolve()
        if not target.is_relative_to(self.root):
            raise ValueError("path outside workspace")
        return target

    def read(self, relative: str) -> str:
        """最多读取策略允许的字节数，避免模型上下文被大文件撑满。"""
        target = self.resolve(relative)
        if not target.is_file() or target.stat().st_size > POLICY.max_file_bytes:
            raise ValueError("missing or oversized file")
        return target.read_text(encoding="utf-8")

    def add(self, relative: str, data: bytes) -> None:
        """写入演示输入；禁止覆盖已有文件及符号链接。"""
        target = self.resolve(relative)
        if len(data) > POLICY.max_file_bytes or target.exists() or target.is_symlink():
            raise ValueError("oversized or existing file")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def close(self) -> None:
        """任务完成后清理临时工作区。"""
        self._temporary.cleanup()

    def __enter__(self) -> "Workspace":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
