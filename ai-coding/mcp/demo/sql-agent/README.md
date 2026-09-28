# SQL Agent Demo

这个 Demo 展示“自然语言查询数据库”的最小链路：

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

真正接入 LLM 时，只需替换 `to_sql()`；数据库工具仍负责执行和安全校验。查询工具只允许单条 `SELECT`，并最多返回 100 行。生产环境还应增加表/列白名单、超时和权限控制。
