# SQL Agent Demo

这个 Demo 展示“自然语言查询数据库”的最小链路，并使用严格 JSON Schema 约束工具选择、参数和输出：

```text
自然语言 → Agent 生成 SQL → query_database Tool → SQLite → 结果
```

运行：

```bash
python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

当前 `to_sql()` 用固定规则模拟 LLM 的 SQL 生成，支持：

- 查询用户
- 查询订单
- 查询金额大于指定数值的订单

真正接入 LLM 时，只需替换 `to_sql()`；工具调用仍必须通过 Schema 校验。

## 严格 JSON Schema

Agent 先生成工具调用对象：

```json
{
  "tool": "query_database",
  "arguments": {"sql": "SELECT id, name FROM users"}
}
```

`TOOL_CALL_SCHEMA` 强制要求工具名为 `query_database`，要求 `sql` 参数为非空字符串，并通过 `additionalProperties: false` 拒绝未知字段。

最终输出也必须符合 `OUTPUT_SCHEMA`：

```json
{
  "question": "查询用户",
  "sql": "SELECT id, name, city FROM users",
  "rows": [{"id": 1, "name": "Alice", "city": "Shanghai"}]
}
```

安装并运行：

```bash
python -m pip install -r requirements.txt
python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

校验失败会直接抛出 `jsonschema.ValidationError`，不会执行不符合协议的工具调用或返回不符合协议的结果。数据库工具仍只允许单条 `SELECT`，最多返回 100 行；生产环境还应增加表/列白名单、超时和权限控制。
