# SQL Agent Demo

这个 Demo 展示“自然语言查询数据库”的最小链路，并使用严格 JSON Schema 约束工具选择、参数和输出。现在提供两个工具：`query_database` 和 `get_schema`。

```text
自然语言 → Agent 生成 SQL → query_database Tool → SQLite → 结果
```

运行：

```bash
python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

Demo 保留两种 SQL 生成方式：

- `rules`：规则版，不调用模型，适合学习基础流程和离线测试
- `gemini`：Gemini 结构化输出版，`SQLPlan` Schema 要求模型返回非空 SQL 字符串

测试用 mock 模型避免调用真实 API。支持：

- 查询用户
- 查询订单
- 查询金额大于指定数值的订单
- 查看数据库表和列结构

加 SQL 安全限制: 两种模式都会经过工具调用 Schema、只读 SQL 和最终输出 Schema 校验。数据库 Tool 会拒绝 `DELETE`、`UPDATE`、`DROP` 等写操作，只允许访问 `users` 和 `orders`，单次查询最多运行 1 秒并返回 100 行。Agent 遇到“查看数据库结构/表结构”时会调用 `get_schema`。

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
export GEMINI_API_KEY="你的 Gemini API Key"
python demo/sql-agent/agent.py
SQL_AGENT_MODE=gemini python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

代码中也可以直接选择：

```python
answer("查询上海的用户", mode="rules")
answer("查询上海的用户", mode="gemini")
```

校验失败会直接抛出 `jsonschema.ValidationError`，不会执行不符合协议的工具调用或返回不符合协议的结果。这里的安全限制是 Demo 级别；生产环境仍应使用数据库只读账号和更严格的 SQL 解析/权限控制。
