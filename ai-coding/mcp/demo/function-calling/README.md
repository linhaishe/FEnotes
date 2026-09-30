# Gemini Function Calling Demo

这个 Demo 不使用 MCP，而是直接使用 Gemini/LangChain 的 Function Calling：

```text
自然语言
  → Gemini 选择 query_database
  → 按 QueryArgs Schema 生成 sql 参数
  → 本地执行 query_database
  → LangChain 把结果回传给模型
  → 最终答案
```

## 严格参数 Schema

`QueryArgs` 使用 Pydantic 定义工具参数：

```python
class QueryArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    sql: str
```

- `extra="forbid"`：拒绝 `limit` 等未声明字段
- `strict=True`：不把其他类型隐式转换成字符串
- `sql: str`：工具参数必须是字符串

`StructuredTool.from_function(..., args_schema=QueryArgs)` 会把这个模型转换成工具的 JSON Schema。数据库层仍然只允许单条 `SELECT`，最多返回 100 行。

## 运行

```bash
conda activate mcp-demo
python -m pip install -r requirements.txt
export GEMINI_API_KEY="你的 Gemini API Key"
python demo/function-calling/agent.py
python demo/function-calling/test_schema.py
```

终端会打印模型发起的 `Function Calling` 参数和最终答案。
