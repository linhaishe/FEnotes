# Day 27：受控 Agent Worker 与模型服务

项目目标见 [总大纲](../readme.md#day-27-项目受控-agent-worker-与开源模型服务)。这个目录提供一个可运行的学习实现：临时工作区、固定 Shell 检查、受控模型地址、凭据隔离和故障降级。

## 运行

需要 Docker daemon、Python 3.10+、`httpx`。Shell 检查镜像是 `python:3.12-slim`；首次执行可能需要拉取镜像。

```bash
export DAY27_MODEL_URL=http://127.0.0.1:8000/v1
export DAY27_MODEL_HOST=127.0.0.1
export DAY27_MODEL_NAME=your-served-model
export DAY27_MODEL_TOKEN=your-local-server-token
export DAY27_AUDIT_LOG=day27_audit.jsonl
python agent-runtime/day27_sandbox_model/worker.py
python -m unittest discover -s agent-runtime/day27_sandbox_model -p 'test_*.py'
```

本地模型服务可按 [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart.html) 启动；也可换成支持相同 Chat Completions API 的 [SGLang](https://github.com/sgl-project/sglang) 或 [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)。部署命令随模型、GPU 和框架版本变化，因此由实际环境决定，不在这里硬编码模型权重或 GPU 参数。无模型服务时，Worker 返回 `degraded`；无 Docker daemon 时，Shell 检查失败并停止。

### vLLM 实际部署与 API 验证

本目录现在提供了可配置的 Docker Compose 部署和验证脚本。默认使用 `Qwen/Qwen2.5-1.5B-Instruct`，需要 NVIDIA GPU、Docker Compose 和 NVIDIA Container Toolkit；也可以通过 `VLLM_MODEL` 替换模型。

```bash
cd agent-runtime/day27_sandbox_model
export VLLM_MODEL=Qwen/Qwen2.5-1.5B-Instruct
export VLLM_API_KEY=day27-local-token
export HF_TOKEN=你的_huggingface_token  # 仅私有模型需要
./start_vllm.sh
```

`start_vllm.sh` 会启动 `docker-compose.vllm.yml`，然后检查 `/health` 和 OpenAI-compatible 的 `/v1/models`。验证单次推理：

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Authorization: Bearer ${VLLM_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"model":"'"${VLLM_MODEL}"'","messages":[{"role":"user","content":"用一句话说明什么是缓存"}],"max_tokens":64}'
```

验证现有受控 Worker：

```bash
export DAY27_MODEL_URL=http://127.0.0.1:8000/v1
export DAY27_MODEL_HOST=127.0.0.1
export DAY27_MODEL_NAME="$VLLM_MODEL"
export DAY27_MODEL_TOKEN="$VLLM_API_KEY"
python worker.py
```

停止服务：

```bash
docker compose -f docker-compose.vllm.yml down
```

## 安全边界与限制

- `Workspace` 每次运行创建临时目录，限制路径与文件大小；容器只读挂载该目录。Python 路径检查只保护工具入口；遇到不可信并发写入和链接替换时，需要更强的文件系统隔离。
- Shell 只运行 `list` 与 `syntax` 两个固定检查。Docker 容器禁网络、禁提权、只读根文件系统，并限制 CPU、内存、进程数、时间与输出。生产部署还需按环境固定镜像 digest、限制 Docker daemon 权限与实际宿主挂载。
- 模型 URL 由部署者配置，模型输出不能提供 URL。客户端检查域名和解析后的 IP；生产环境还需网络层 egress 规则，防止 DNS 重绑定和进程绕过 Python 检查。
- Token 只在 HTTP Header 中使用，不写入 prompt、工作区或返回结果。演示使用环境变量；生产环境应换成短期凭据代理。
- 审计日志只保存任务状态，不保存源码或凭据。若项目源码本身含密钥，当前示例不会识别它们，向模型发送源码前需要额外的内容审查。
- 模型返回的文本只当报告展示，不当文件路径或 Shell 命令执行。

## 验证重点

`test_security.py` 使用本地模拟模型响应验证工作区逃逸、命令白名单、地址拒绝、凭据缺失、报告不执行和模型降级。Docker 实际隔离需要在有 Docker daemon 的主机上运行 `worker.py` 并复核容器权限；测试中的容器调用使用替身，不能代替部署环境安全审计。



## Day 27 项目：受控 Agent Worker 与开源模型服务

### 项目问题

实现一个“代码分析 Agent Worker”：Agent 可以读取用户提供的项目、运行有限的检查命令、调用模型生成报告，但不能越权访问宿主机文件、私网、Shell 权限或凭据。

```text
任务 API
  → Worker / Policy Gateway
      ├── Workspace：文件白名单与清理
      ├── Shell Runner：命令白名单与资源限制
      ├── Network Proxy：默认拒绝与域名 allowlist
      ├── Credential Broker：短期、最小权限 token
      └── Model Client → OpenAI-compatible Model Server
                              └── vLLM / SGLang / TensorRT-LLM
```

核心交付物不是“把模型跑起来”，而是证明 Agent 在完成任务的同时，越权路径会被拒绝，模型服务故障也会安全失败。

### 原知识大纲

核心原则：模型输出是不可信输入；沙箱不是提示词约束，而是操作系统、容器、网络和凭据系统提供的真实边界。

#### 文件隔离

- 为每个 Agent 运行创建独立工作目录，并设置生命周期和磁盘配额。
- 使用路径规范化、符号链接检查和目录白名单，防止 `../` 越权读取。
- 默认只挂载必要目录；不暴露宿主机目录、Docker socket、SSH key 和项目源码。
- 区分临时输入、产物和日志，任务结束后按策略清理或归档。
- 记录文件读写审计：谁、何时、访问了什么、结果如何。

#### Shell 隔离

- 不把模型生成的字符串直接拼接进 `shell=True` 命令。
- 优先使用参数数组和允许命令表，例如 `subprocess.run(["python", "script.py"], shell=False)`。
- 限制工作目录、环境变量、用户权限、CPU、内存、进程数、执行时间和输出大小。
- 设置进程组；超时或取消时杀掉整个进程树，避免后台进程逃逸。
- 禁止特权容器、宿主网络、设备访问、任意挂载和 Docker socket。

#### 网络隔离

- 默认无网络；只有确实需要的工具才允许出网。
- 使用 egress allowlist 限制域名、端口、协议和请求方法。
- 阻止云元数据服务、内网管理端口、回环地址和私有网段，防止 SSRF。
- 代理层统一处理 DNS、TLS、超时、重试、速率限制和请求审计。
- 分离模型服务访问模型仓库与 Agent 工具访问业务 API 的网络策略。

#### 凭据隔离

- 不把 API key、数据库密码、云凭据放进 prompt、状态、日志或工作目录。
- 使用凭据代理或短期 token，按工具和请求签发最小权限凭据。
- 通过环境注入或文件描述符传递凭据，避免命令行参数泄露到进程列表。
- 对日志、异常和模型上下文做脱敏；凭据应可撤销、轮换、过期并记录审计。

#### 开源模型服务化

```text
Agent Runtime → OpenAI-compatible HTTP API → vLLM / SGLang / TensorRT-LLM
```

- 理解离线批量推理与在线服务的区别。
- 理解模型权重、Tokenizer、GPU 显存和量化格式的关系。
- 学习请求队列、连续批处理、KV Cache、最大上下文和最大并发。
- 学习 streaming、工具调用、结构化输出和停止条件。
- 为模型服务设置 timeout、取消、限流、熔断、重试和降级。
- 采集首 token 延迟、端到端延迟、吞吐量、排队时间、显存和错误率。
- 关注 API 鉴权、网络隔离、模型仓库权限和权重供应链安全。

#### 服务框架参考

- [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)：主线学习离线推理和 OpenAI 兼容在线服务。
- [SGLang](https://github.com/sgl-project/sglang)：对比复杂生成程序、结构化生成和高性能服务。
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)：对比 NVIDIA GPU 上的编译优化、量化和生产级推理。

比较框架时固定模型、硬件、上下文长度、并发、采样参数和数据集，再测 TTFT、TPOT、P95/P99、吞吐量和显存占用。

### 最终产物

```text
agent-runtime/day27_sandbox_model/
├── README.md
├── policy.py              # 文件、命令、网络和凭据策略
├── sandbox_fs.py          # 工作目录和路径校验
├── sandbox_shell.py      # 安全执行命令
├── network_policy.py      # 域名/IP allowlist 与 SSRF 防护
├── credentials.py         # 脱敏和短期凭据接口
├── model_client.py        # OpenAI-compatible 模型客户端
├── worker.py              # 编排沙箱工具与模型调用
├── docker-compose.yml     # 本地模型服务配置，可选
└── test_security.py       # 越权和故障测试
```

## 分阶段交付

### 阶段 1：定义威胁模型和策略

先写清楚 Agent 能做什么、不能做什么：

- 文件：只能访问独立 workspace，拒绝 `..`、符号链接逃逸和宿主敏感路径。
- Shell：只允许固定命令和参数，禁止 `shell=True`、特权、设备、Docker socket。
- 网络：默认拒绝，只允许配置的域名和端口；拒绝 loopback、私网和云元数据地址。
- 凭据：模型永远看不到明文；工具只拿到短期、最小权限 token。

交付：`policy.py`、威胁模型文档和每条策略对应的失败测试。

| 阶段 1 要求 | 当前所在位置 | 状态 |
|---|---|---|
| 策略配置 | [`policy.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/policy.py:1) | 部分完成 |
| 威胁模型说明 | [`README.md`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/README.md:130) | 已写在 README，未独立成文档 |
| 文件边界 | [`sandbox_fs.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/sandbox_fs.py:16) | 已实现 |
| Shell 边界 | [`sandbox_shell.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/sandbox_shell.py:17) | 已实现大部分 |
| 网络边界 | [`network_policy.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/network_policy.py:8) | 部分实现 |
| 凭据边界 | [`credentials.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/credentials.py:6) | 已有演示实现 |
| 失败测试 | [`test_security.py`](/Users/chenruo/Documents/GitHub/FEnotes/ai-coding/agent-runtime/day27_sandbox_model/test_security.py:20) | 已有基础覆盖 |

### 阶段 2：实现文件沙箱

实现 `sandbox_fs.py`：创建 workspace、规范化路径、检查真实路径、限制读写范围、限制文件大小，并在任务结束后清理。

验收：读取 workspace 内文件成功；读取 `../secret`、符号链接目标和宿主凭据失败。

### 阶段 3：实现 Shell Runner

实现 `sandbox_shell.py`：使用参数数组执行、固定 cwd、最小环境变量、超时、输出上限和进程组清理。

验收：允许的检查命令成功；未允许命令、超时命令和后台子进程被拒绝或清理；没有遗留进程。

### 阶段 4：实现网络与凭据边界

实现 `network_policy.py` 和 `credentials.py`：域名 allowlist、IP 解析后二次检查、请求 timeout、请求审计、日志脱敏和短期凭据注入。

验收：允许的模型服务地址可访问；私网、回环、元数据地址和未授权域名被拒绝；日志和模型输入不含密钥。

### 阶段 5：接入开源模型服务

实现 `model_client.py`，只依赖 OpenAI-compatible HTTP API，使 Worker 与推理引擎解耦。先用 [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart.html) 完成：

- 离线批量推理与在线服务的区别。
- chat/completions、streaming、超时和错误处理。
- 请求队列、连续批处理、KV Cache、最大上下文和最大并发。
- TTFT、TPOT、P95/P99、吞吐量、排队时间和显存指标。

再选择一个替代实现做对比：

- [SGLang](https://github.com/sgl-project/sglang)：重点观察结构化生成和复杂生成程序。
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)：重点观察 NVIDIA GPU 上的编译优化、量化和推理性能。

比较时固定模型、硬件、上下文长度、并发、采样参数和数据集；不比较脱离条件的“谁更快”。

### 阶段 6：串起 Worker 与故障演练

实现 `worker.py`：接收分析任务，读取 workspace，运行静态检查，调用模型生成报告，并保存审计事件。

注入故障并验证安全失败：

- 沙箱进程超时或被杀死。
- 网络被阻断或模型服务重启。
- 凭据过期或被撤销。
- 模型返回恶意路径、危险命令或超大输出。

预期结果是超时、拒绝、降级或可重试错误，不能越权执行或泄露凭据。

### 通过标准

- 文件、Shell、网络、凭据四条边界都有实现和失败测试。
- Agent 不能读取 workspace 之外的文件，不能访问私网和元数据地址。
- Shell 超时后没有遗留子进程，输出不会无限增长。
- 明文凭据不进入 prompt、checkpoint、日志、异常或工作目录。
- Worker 只通过受控 API 调用模型服务，不共享宿主权限。
- 模型服务重启、超时和限流时有明确的 timeout、重试或降级结果。
- 性能报告包含 TTFT、总延迟、P95/P99、吞吐量、排队时间和显存占用。
- 能说明 vLLM、SGLang、TensorRT-LLM 的选择依据，而不是只记录启动成功。
