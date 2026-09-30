# MCP Demo 集合

本项目用几个最小示例演示 MCP Server、工具调用和 SQL Agent：

| Demo | 目录 | 内容 |
| --- | --- | --- |
| 天气 MCP | `demo/stdio/`、`demo/sse/` | 天气、SQLite 查询和 HTTP API 工具，分别使用 stdio 和 SSE 传输 |
| LangChain Host | `demo/langchain_host.py` | 使用 LangChain Agent 连接 stdio MCP Server 并自动调用天气工具 |
| Gemini Function Calling | `demo/function-calling/` | 使用 Gemini/LangChain 按严格参数 Schema 选择并调用数据库函数 |
| SQL Agent | `demo/sql-agent/` | 根据自然语言选择查询工具，生成 SQL 并返回严格 JSON Schema 结构化结果 |

## 环境准备（Miniconda3）

请先安装 [Miniconda3](https://docs.anaconda.com/miniconda/)，然后在项目根目录执行：

```bash
conda create -n mcp-demo python=3.11 -y
conda activate mcp-demo
python -m pip install -r requirements.txt
```

后续命令都在 `mcp-demo` 环境中运行。

## LangChain Host Demo

这个 Demo 用 LangChain Agent 模拟 Host：`MCPAdapter` 启动并连接 `demo/stdio/server.py`，发现 `weather` 工具，再由模型根据自然语言自动决定是否调用。

先设置 Gemini API Key：

```bash
export GEMINI_API_KEY="你的 Gemini API Key"
```

运行：

```bash
conda activate mcp-demo
python demo/langchain_host.py
```

程序会用 Rich 打印已发现的 MCP Tools，以及 Agent 的每一步更新。看到类似 `weather` 的 tool call，说明 LangChain 已经调用 MCP Server；最后一条消息是模型生成的自然语言答案。

调用链：

```text
LangChain Agent → MCPAdapter → stdio MCP Server → weather Tool → Open-Meteo
```

这个 Demo 使用 Gemini，需要真实的 Gemini API Key；只想手动调试 MCP 工具时，可以使用 MCP Inspector，不需要运行 LangChain Host。

## SQL Agent Demo

SQL Agent 使用内存 SQLite 数据库，不依赖外部数据库或模型 API，适合先理解 Agent 的基本链路：

```text
自然语言问题 → Agent 生成 SQL → query_database Tool → SQLite → 结构化结果
```

运行：

```bash
conda activate mcp-demo
python demo/sql-agent/agent.py
python demo/sql-agent/test_agent.py
```

它演示了工具选择、只读 SQL 校验、结果行数限制，以及使用 JSON Schema 校验工具参数和最终输出。详细说明见 [`demo/sql-agent/README.md`](demo/sql-agent/README.md)。

### JSON Schema 结构化输出

SQL Agent 不直接返回一段不确定格式的文本，而是要求输出符合固定 Schema：

```json
{
  "question": "查询金额大于100的订单",
  "sql": "SELECT id, user_id, amount FROM orders WHERE amount > 100",
  "rows": [
    {"id": 1, "user_id": 1, "amount": 120.5}
  ]
}
```

工具调用也必须符合 Schema：

```json
{
  "tool": "query_database",
  "arguments": {"sql": "SELECT id, name FROM users"}
}
```

Schema 会校验工具名称、必需参数、字段类型和额外字段；校验失败时拒绝执行或返回结果。这样调用方可以稳定地读取 `question`、`sql` 和 `rows`，而不是解析自然语言文本。

## Function Calling：结构化工具调用

Function Calling 让模型返回结构化的工具调用参数，而不是一段需要手动解析的文本。仓库中的示例位于 [`demo/function-calling/agent.py`](demo/function-calling/agent.py)，使用 Gemini + LangChain 演示：

```text
用户问题 → 模型选择工具 → 生成工具名和参数 → Pydantic 校验 → 执行 SQLite → 返回结果给模型
```

Function Calling 是让模型能够“选择并生成调用工具所需参数”的机制。

它本身不负责真正执行工具。
完整流程是：

```
1. 代码定义工具
2. 将工具名称、描述、参数 Schema 提供给模型
3. 模型决定是否调用工具
4. 模型返回工具名和参数
5. 应用代码执行真正的函数
6. 将执行结果返回给模型
7. 模型生成最终回答
```

### 1. 定义参数 Schema

```python
class QueryArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    sql: str = Field(description="A single read-only SELECT query")
```

这表示 `sql` 必须存在且为字符串，并且不能传入额外字段。LangChain 会根据它生成工具参数 JSON Schema。

### 2. 注册工具

```python
query_tool = StructuredTool.from_function(
    func=run_query,
    name="query_database",
    description="Execute one read-only SQL SELECT query against the demo database.",
    args_schema=QueryArgs,
)
```

`func` 是实际执行函数，`name` 和 `description` 提供给模型，`args_schema` 约束模型必须生成的参数格式。

### 3. 创建 Agent 并调用

```python
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
agent = create_agent(model, [query_tool])
result = await agent.ainvoke({
    "messages": [{"role": "user", "content": "查询金额大于100的订单"}]
})
```

运行示例：

```bash
export GEMINI_API_KEY="你的 Gemini API Key"
python demo/function-calling/agent.py
python demo/function-calling/test_schema.py
```

`test_schema.py` 验证额外参数会被拒绝：

```python
QueryArgs(sql="SELECT 1", limit=10)  # ValidationError
```

### Function Calling 与 MCP 的区别

Function Calling 规定“模型如何生成工具调用”；MCP 规定“客户端如何发现并调用外部工具服务”。两者可以串联：

```text
模型 Function Calling → MCP Client → MCP Server 的 tools/call → 工具结果
```

当前 demo 使用 Gemini，不是 OpenAI SDK；它演示的是通用的结构化工具调用方式。若改用 OpenAI，主要替换模型客户端，参数 Schema、工具函数和校验逻辑仍可复用。

## LangChain 多工具链式 Agent

[`demo/langchain_multi_tool_host.py`](demo/langchain_multi_tool_host.py) 将现有三个 MCP 工具一次性挂载到 LangChain Agent：

```text
用户问题
  → LangChain Agent 选择 weather
  → 继续选择 query_database
  → 继续选择 call_api
  → 汇总所有工具结果
```

运行：

```bash
export GEMINI_API_KEY="你的 Gemini API Key"
# or env add GEMINI_API_KEY
python demo/langchain_multi_tool_host.py
```

这个示例的关键是 `MCPAdapter` 返回的三个工具直接交给 `create_agent()`。Agent 可以根据上一轮工具结果继续发起下一次工具调用；每一次调用都由 MCP Client 转发给 stdio MCP Server 的 `tools/call`。

### Agent 与 LCEL 的区别

上面的 `langchain_multi_tool_host.py` 使用的是 LangChain Agent，不是 LCEL（LangChain Expression Language）链。

Agent 的调用顺序由模型决定：

```text
问题 → 模型选择工具 → 工具结果 → 模型再次选择工具 → 最终回答
```

它适合工具选择和调用次数不确定的场景，例如模型可能先调用 `weather`，再调用 `query_database`，最后调用 `call_api`。

LCEL 则使用 `|` 把固定步骤连接起来：

```python
chain = prompt | model | parser
result = await chain.ainvoke(input)
```

LCEL 的调用顺序由代码决定，更适合确定性流程。MCP 只负责发现和调用工具，Agent 或 LCEL 负责组织工具调用：

| 组件 | 负责内容 |
| --- | --- |
| MCP | 工具发现、通信和 `tools/call` |
| Agent | 模型自主选择工具并循环调用 |
| LCEL | 按代码定义的顺序组合 Runnable 步骤 |

因此，本仓库当前展示的是 Agent 方式；如果要展示 LCEL，需要另写一个固定顺序的链式流程。

## ReAct Agent 官方示例

[`demo/react_agent/`](demo/react_agent/) 是一个基于 LangChain 官方 custom tool 示例的最小 Agent。它用 `create_agent()` 注册本地 `get_weather(city)` 工具，展示 ReAct 的基本循环：模型判断是否行动、调用工具、观察工具结果，再生成最终回答。

详细说明和运行方式见 [`demo/react_agent/README.md`](demo/react_agent/README.md)。

demo/langchain_multi_tool_host.py 就是“可以连续调用多个工具的 Agent”示例。
这里的“链式调用”指：
```
用户问题
  → Agent 调用 weather
  → 获取天气结果
  → Agent 再调用 query_database
  → 获取数据库结果
  → Agent 再调用 call_api
  → 汇总最终答案
```
关键点是：后一个工具调用可以基于前一个工具的结果继续进行。
不过要区分两种“链式”：
- Agent 链式调用：调用顺序由模型动态决定，当前 Demo 属于这种。
- LCEL 链式调用：调用顺序由代码固定，例如 step1 | step2 | step3。
当前 Demo 的设计目标是前者。`create_agent(model, tools)` 允许模型多轮决定是否继续调用工具，但实际调用哪些工具、调用顺序和次数仍由模型决定。

天气业务在 `demo/shared/weather.py`，SQLite 查询复用 `demo/sql-agent/database.py`，三个工具由 MCP Server 暴露。Server 使用 MCP Python SDK 的 `FastMCP` API。

三个自定义工具：

- `weather(city)`：查询城市当前天气；
- `query_database(sql)`：执行受限的只读 SQLite `SELECT` 查询；
- `call_api(url)`：调用 HTTP/HTTPS GET API，返回 JSON 或文本响应。

## stdio

```bash
conda activate mcp-demo
python demo/stdio/server.py
```

这是一个使用 `stdio` 的 MCP Server。接入 MCP Host 时，将启动命令配置为：

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["/绝对路径/demo/stdio/server.py"]
    }
  }
}
```

## MCP Client 与契约测试

契约测试验证 MCP Client 和 Server 之间的协议约定，而不是只测试工具函数内部逻辑。它检查：

- Client 能否完成 `initialize`；
- `tools/list` 是否返回 `weather`，以及参数 Schema 是否要求 `city: string`；
- `tools/call` 使用合法参数时是否返回结果；
- 缺少参数时是否返回 MCP 错误。

本项目的最小契约测试位于 [`demo/stdio/test_contract.py`](demo/stdio/test_contract.py)，使用 MCP Python Client 通过 stdio 启动真实 Server，不使用 Mock：

```bash
python demo/stdio/test_contract.py
```

测试调用链：

```text
契约测试 → MCP Client → stdio Server → tools/list / tools/call → weather
```

### 使用 MCP Inspector 手工验证

契约测试适合自动化回归；Inspector 适合查看工具清单、Schema 和原始响应。先确保已安装 Node.js，然后运行：

```bash
npx @modelcontextprotocol/inspector python demo/stdio/server.py
```

在 Inspector 页面连接后，确认 `weather` 工具的参数包含必填字符串 `city`，再分别调用：

```json
{"city": "北京"}
```

以及一个缺少 `city` 的参数对象，检查合法调用返回天气结果、非法调用返回错误。

stdio 和 SSE 的工具实现相同，区别只在 Client 连接方式：stdio 由 Client 启动子进程，SSE 则连接已运行的 HTTP Server。因此契约断言可以复用，先用 stdio 做本地自动化测试，再用 Inspector 或 SSE Client 验证远程传输。

FastMCP 是 MCP Python SDK 提供的高层 Server 封装；MCPServer 在当前安装的 SDK 中并不存在，所以原代码无法运行。

FastMCP 自动处理：
- MCP 初始化和能力协商
- tools/list
- tools/call
- Python 函数到 JSON Schema 的转换
- stdio、SSE 等传输启动
使用方式基本不变：

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def weather(city: str) -> dict:
    return get_weather(city)

mcp.run(transport="stdio")
```
```
from mcp.server import MCPServer
from shared.weather import get_weather

mcp = MCPServer("weather-sse")
```

## SSE

适合独立运行、通过 HTTP 连接的 Server：

```bash
conda activate mcp-demo
python demo/sse/server.py
```

默认 SSE 地址通常为 `http://localhost:8000/sse`，具体以 MCP SDK 版本输出为准。

## 天气 Demo 完整使用流程

### 方式一：使用 stdio 接入 Host

1. 激活环境并进入项目根目录：

   ```bash
   conda activate mcp-demo
   cd /Users/你的用户名/项目路径/mcp
   ```

2. 在 MCP Host 的配置文件中添加 Server：

   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": ["/绝对路径/mcp/demo/stdio/server.py"]
       }
     }
   }
   ```

3. 重启 Host。Host 会自动启动 `server.py`，并通过 `initialize` 与 Server 建立连接。
4. 在 Host 中提问：

   ```text
   查询北京当前天气
   ```

5. Host 发现并调用 `weather(city="北京")`，Server 再请求 Open-Meteo，最后把结果交给模型生成回答。

### 方式二：使用 SSE 接入 Host

1. 在终端启动 SSE Server：

   ```bash
   conda activate mcp-demo
   python demo/sse/server.py
   ```

2. 在支持远程 MCP Server 的 Host 中添加 SSE 地址：

   ```text
   http://localhost:8000/sse
   ```

3. 连接成功后，在 Host 中提问：

   ```text
   上海今天的天气怎么样？
   ```

4. Host Client 通过 `tools/list` 发现 `weather` 工具，再通过 `tools/call` 传入城市名称并获取结果。

完整调用链：

```text
用户提问
  → Host 调用模型
  → MCP Client 连接 Server
  → tools/call(weather, city)
  → Open-Meteo
  → 天气结果
  → 模型生成回答
```

## Host、Client、Server 与能力协商

- **Host**：用户使用的 AI 应用，例如 Cursor 或 Claude Desktop；负责对话、模型调用和用户授权。
- **Client**：嵌在 Host 中、与一个 Server 一对一连接的 MCP 客户端；负责协议通信和能力隔离。
- **Server**：这里的 `stdio/server.py` 或 `sse/server.py`，负责暴露 `weather` 工具。

调用链是：`用户问题 → Host/模型 → Client → Server.weather → Client → Host/模型 → 答案`。

连接建立后，Client 与 Server 先发送 `initialize`：双方交换 MCP 协议版本和能力（capabilities）。Server 声明自己提供工具能力，随后 Client 用 `notifications/initialized` 确认完成初始化。

之后 Client 可以调用：

1. `tools/list`：发现 Server 提供的工具名称、描述和输入 JSON Schema。
2. `tools/call`：传入 `{"name": "weather", "arguments": {"city": "北京"}}` 执行工具。

能力协商不会把业务逻辑放进 Host；它只确定双方支持哪些协议特性。工具清单和参数约束由 Server 自己声明，Host/模型据此决定是否调用。

## 自检

```bash
python -m py_compile demo/shared/weather.py demo/stdio/server.py demo/sse/server.py
```

# MCP 工作流

```
Host
  ↓
MCP Client
  ↓ initialize / capabilities
MCP Server
  ↓ tools/list
weather Tool
  ↓ tools/call
Open-Meteo API
```
- `initialize`：Client 和 Server 协商协议版本与能力
- `tools/list`：Client 查询 Server 有哪些工具
- `tools/call`：Client 请求执行某个工具

## connect other mcp

可以把“网上别人的 MCP”理解成一个已经运行好的工具服务。你不需要复制对方的函数代码，只需要连接它，发现它暴露的 Tools，然后交给 LangChain Agent。

### 1. 远程 MCP Server

例如对方提供：

```text
https://example.com/mcp
```

LangChain Host 可以这样连接：

```python
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

async with MCPAdapter("https://example.com/mcp") as adapter:
    tools = await adapter.list_tools()

    agent = create_agent(
        model,
        tools,
    )

    result = await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": "帮我查询相关信息",
            }
        ]
    })
```

执行过程：

```text
MCPAdapter 连接远程 Server
        ↓
initialize
        ↓
tools/list
        ↓
获得别人提供的 Tools
        ↓
交给 LangChain Agent
        ↓
Agent 自动决定调用哪个 Tool
```

LangChain 官方的 `MCPAdapter` 支持直接使用 HTTP URL 连接远程 MCP Server，并通过 `list_tools()` 发现工具。

### 2. 别人的本地 stdio MCP Server

有些 MCP Server 不是 URL，而是别人提供的 Python、Node.js 或命令行程序。

例如对方要求这样启动：

```bash
npx some-weather-mcp
```

你的 LangChain Host 可以通过 stdio 启动它：

```python
from pathlib import Path
from langchain.mcp import MCPAdapter

async with MCPAdapter(
    {
        "mcpServers": {
            "weather": {
                "command": "npx",
                "args": ["-y", "some-weather-mcp"],
            }
        }
    }
) as adapter:
    tools = await adapter.list_tools()
```

或者是本地 Python 文件：

```python
async with MCPAdapter(
    Path("/absolute/path/to/third_party_server.py")
) as adapter:
    tools = await adapter.list_tools()
```

### 3. 多个 MCP Server

一个 LangChain Agent 可以同时连接多个 MCP Server：

```python
async with MCPAdapter(
    {
        "mcpServers": {
            "weather": {
                "command": "python",
                "args": ["demo/stdio/server.py"],
            },
            "docs": {
                "url": "https://example.com/mcp",
            },
        }
    }
) as adapter:
    tools = await adapter.list_tools()
    agent = create_agent(model, tools)
```

Agent 看到的可能是：

```text
weather
search_docs
read_docs
```

当用户提问时，模型会根据每个 Tool 的名称、描述和参数 Schema 自动选择工具。

### 4. 别人的“方法”怎么处理？

你不需要直接调用别人的 Python 方法：

```python
# 不需要这样做
from someone_else import search_docs
```

MCP 的方式是：

```text
连接 MCP Server
→ 获取工具描述
→ Agent 生成工具调用
→ MCP Server 执行对方的方法
→ 返回结果
```

你只需要关心：

- MCP Server 的连接地址或启动命令
- 支持的传输方式
- 是否需要 API Key
- Tool 的输入参数
- 对方是否可信

### 5. 如果对方没有 MCP

如果对方只有普通 HTTP API，就不能直接用 `MCPAdapter`。你需要自己把 API 包装成 MCP Tool：

```python
@mcp.tool()
def search_products(keyword: str) -> dict:
    return requests.get(
        "https://example.com/api/search",
        params={"q": keyword},
    ).json()
```

这样才会变成：

```text
普通 API → 你的 MCP Server → LangChain Agent
```

安全上，不要把未知 MCP Server 直接接入生产 Agent。远程 MCP 可能具有读写数据、发送消息或执行操作的权限，应该先查看它的 Tools 和参数 Schema。

# 严格 JSON Schema 实现工具选择、参数校验和结构化输出
OpenAI 这篇文档的核心是：让模型输出符合预先定义的 JSON Schema，而不是依赖模型“自觉返回正确 JSON”。

文档: [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling),

[Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

## 1. Structured Outputs 解决什么问题

普通 JSON Mode 只能保证输出是合法 JSON：

```json
{"name": "Alice"}
```

但不一定保证：

- 字段存在
- 字段名称正确
- 字段类型正确
- 没有多余字段
- 嵌套结构符合要求

Structured Outputs 通过 JSON Schema 约束模型输出，使结果更适合程序直接解析。

## 2. 两种主要使用场景

### 场景一：约束模型最终回答

适用于：

```text
用户问题 → 模型 → 结构化结果
```

例如要求模型返回天气结果：

```json
{
  "city": "北京",
  "temperature": 20,
  "unit": "celsius"
}
```

这时使用 Response API 或 Chat Completions 的 `json_schema` 配置。

### 场景二：约束工具调用参数

适用于：

```text
用户问题 → 模型选择工具 → 生成工具参数
```

例如：

```json
{
  "name": "query_database",
  "arguments": {
    "sql": "SELECT id, name FROM users"
  }
}
```

这时使用 Function Calling，并设置：

```json
{
  "strict": true
}
```

你仓库里的 SQL Agent 更接近第二种，因为它需要让模型生成合法的工具调用。

## 3. `strict: true` 的作用

严格模式会要求工具参数符合 Schema：

```json
{
  "type": "object",
  "properties": {
    "sql": {
      "type": "string"
    }
  },
  "required": ["sql"],
  "additionalProperties": false
}
```

这样模型不能随意返回：

```json
{
  "query": "...",
  "limit": 10
}
```

因为 `limit` 不在定义中，且 Schema 设置了：

```json
"additionalProperties": false
```

## 4. Structured Outputs 和 JSON Mode 的区别

```text
JSON Mode
= 保证结果是 JSON

Structured Outputs
= 保证结果是符合 JSON Schema 的 JSON
```

JSON Mode 仍然可能返回错误字段或错误类型；Structured Outputs 更适合：

- 工具调用
- 数据提取
- 分类
- 结构化 Agent 状态
- 数据库查询参数
- 自动化工作流

## 5. Schema 编写限制

文档强调，Schema 不是任意 JSON Schema 都能使用，通常要注意：

- 根节点通常使用 `object`
- 明确声明 `required`
- 使用 `additionalProperties: false`
- 字段类型要明确
- 不要依赖模型返回缺失字段
- 可选字段可以使用 nullable，例如：
  
  ```json
  {
    "type": ["string", "null"]
  }
  ```

换句话说，结构化输出更偏向“固定协议”，而不是随意变化的 JSON。

## 6. 仍然要处理异常情况

即使使用 Structured Outputs，代码仍然需要处理：

- 模型拒绝回答
- 输出被截断
- 请求失败
- API 超时
- 工具执行失败
- Schema 之外的业务错误

Schema 只能约束格式，不能保证：

```text
SQL 一定正确
查询结果一定存在
业务逻辑一定合理
```

例如：

```json
{
  "sql": "SELECT * FROM nonexistent_table"
}
```

格式可能完全合法，但数据库仍然会执行失败。

## 7. 对当前 SQL Agent 的对应关系

当前 Demo 的流程：

```text
自然语言
  ↓
生成工具调用
  ↓
TOOL_CALL_SCHEMA 校验
  ↓
query_database()
  ↓
OUTPUT_SCHEMA 校验
  ↓
结构化结果
```

如果接入 OpenAI，可以让模型直接负责生成：

```json
{
  "tool": "query_database",
  "arguments": {
    "sql": "SELECT id, name, city FROM users"
  }
}
```

然后由程序负责：

1. 校验 Schema
2. 校验 SQL 是否只读
3. 执行数据库查询
4. 返回结构化结果

最重要的边界是：

```text
Structured Outputs 负责格式可靠
代码负责安全和业务正确性
```
