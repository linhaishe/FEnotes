"""用最小的本地实现演示三类记忆及其治理策略。无需模型或数据库。"""

from dataclasses import dataclass, field


@dataclass
class Memory:
    text: str
    tags: set[str] = field(default_factory=set)


def select(
    messages: list[Memory], query_tags: set[str], limit: int = 3
) -> list[Memory]:
    """选择与当前任务相关的消息，并保留最近消息。"""
    relevant = [message for message in messages if message.tags & query_tags]
    return relevant[-limit:]


"""
{tag for m in messages for tag in m.tags}
遍历每条消息 m，再遍历该消息的 m.tags，最后收集成一个去重的 set

tags = set()

for m in messages:
    for tag in m.tags:
        tags.add(tag)
===   
  
Memory(
    text="用户要把报告改成中文；报告截止日期是周五",
    tags={"report", "language", "deadline"},
)
"""


def compress(messages: list[Memory]) -> Memory:
    """把已选择的工作记忆压成一条摘要。生产环境可替换为模型摘要。"""
    return Memory(
        "；".join(message.text for message in messages),
        {tag for m in messages for tag in m.tags},
    )


class MemoryStore:
    def __init__(self) -> None:
        self._data: dict[tuple[str, ...], dict[str, Memory]] = {}

    def put(self, namespace: tuple[str, ...], key: str, value: Memory) -> None:
        self._data.setdefault(namespace, {})[key] = value

    def get(self, namespace: tuple[str, ...], key: str) -> Memory | None:
        return self._data.get(namespace, {}).get(key)

    def delete(self, namespace: tuple[str, ...], key: str) -> None:
        self._data.get(namespace, {}).pop(key, None)


def demo() -> None:
    session_state = [
        Memory("用户要把报告改成中文", {"report", "language"}),
        Memory("用户喜欢简洁的 UI", {"preference", "ui"}),
        Memory("报告截止日期是周五", {"report", "deadline"}),
        Memory("用户问了天气", {"weather"}),
    ]

    # 选择 -> 压缩：工作记忆只服务当前任务，不直接等同于全部会话历史。
    working_memory = compress(select(session_state, {"report", "deadline"}))
    
    # 一条断言，用来检查 Demo 结果是否符合预期
    """
    完整逻辑：
    if "报告" in working_memory.text and "天气" not in working_memory.text:
        pass
    else:
        raise AssertionError
    """
    assert "报告" in working_memory.text and "天气" not in working_memory.text

    # 隔离：同一个 key 在不同用户 namespace 下互不可见。
    store = MemoryStore()
    store.put(
        ("users", "alice", "memories"), "profile", Memory("偏好中文", {"preference"})
    )
    store.put(
        ("users", "bob", "memories"), "profile", Memory("偏好英文", {"preference"})
    )
    assert store.get(("users", "alice", "memories"), "profile").text == "偏好中文"
    assert store.get(("users", "bob", "memories"), "profile").text == "偏好英文"

    # 删除：显式删除长期记忆，而不是只从本次 prompt 中隐藏。
    store.delete(("users", "alice", "memories"), "profile")
    assert store.get(("users", "alice", "memories"), "profile") is None
    print("选择、压缩、隔离、删除策略检查通过")


if __name__ == "__main__":
    demo()

"""
应使用稳定且唯一的 user_id

登录系统生成的用户主键
数据库自增 ID
UUID / ULID
多租户场景使用 tenant_id + user_id
实际应用中应由认证系统或数据库提供稳定的 user_id
"""