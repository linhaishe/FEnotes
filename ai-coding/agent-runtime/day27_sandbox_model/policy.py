"""Day 27 的固定权限策略；模型输出不能修改这些值。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Policy:
    # 只开放一个不会执行项目源码的检查命令。需要更多命令时逐个审查后加入。
    commands: tuple[str, ...] = ("list", "syntax")
    # 单个文件允许读取或写入的最大字节数。
    max_file_bytes: int = 64 * 1024
    # 单次命令执行允许返回的最大输出字节数。
    max_output_bytes: int = 16 * 1024
    # Shell 命令的最大执行时间，单位为秒。
    shell_timeout_seconds: float = 10.0
    # 模型请求的最大等待时间，单位为秒。
    model_timeout_seconds: float = 20.0
    # 发送给模型的文本允许达到的最大字符数。
    max_model_chars: int = 8000


POLICY = Policy()

"""
这行定义了一个名为 `commands` 的配置字段：

```python
commands: tuple[str, ...] = ("list", "syntax")
```

含义是：

- `commands`：变量名，表示允许执行的命令列表。
- `tuple[str, ...]`：类型注解，表示这是一个只包含字符串的元组，字符串数量不限。
- `("list", "syntax")`：默认值，只允许两个命令：
  - `"list"`：列出 workspace 中的文件。
  - `"syntax"`：检查 Python 文件语法。
- `=`：给这个字段设置默认值。

在代码中，如果传入其他命令，例如：

```python
command_for("rm -rf /")
```

就会因为不在 `commands` 白名单中而被拒绝。


```
from pathlib import Path
from sandbox_shell import run_check

result = run_check(Path("/path/to/workspace"), "syntax")
print(result)
```

它会：
1. 在 Docker 容器中运行；
2. 将 workspace 以只读方式挂载到 /workspace；
3. 查找所有 .py 文件；
4. 使用 ast.parse() 检查语法；
5. 语法正确时正常结束；
6. 发现语法错误时抛出 ShellUnavailable。

```
try:
    print(run_check(workspace.root, "syntax"))
except ShellUnavailable as exc:
    print(f"检查失败：{exc}")
```
"""