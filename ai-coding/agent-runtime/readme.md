```
ai-coding/
├── agent-runtime/
│   ├── README.md
│   ├── pyproject.toml
│   ├── .env.example
│   │
│   ├── common/                  # 公共类型、配置、日志、错误
│   │   ├── types.py
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── day22_harness/           # Agent Loop 与预算
│   │   ├── agent_loop.py
│   │   ├── tools.py
│   │   ├── budget.py
│   │   └── test_agent_loop.py
│   │
│   ├── day23_context_cache/     # 上下文与 Redis 缓存
│   │   ├── context_manager.py
│   │   ├── compressor.py
│   │   ├── cache.py
│   │   ├── llm_cache.py
│   │   ├── embedding_cache.py
│   │   └── benchmark.py
│   │
│   ├── day24_state_resume/      # 状态、Checkpoint、幂等
│   │   ├── state.py
│   │   ├── checkpoint.py
│   │   ├── idempotency.py
│   │   ├── side_effect_tools.py
│   │   └── test_resume.py
│   │
│   ├── day25_async_tools/       # 异步、超时、取消、背压
│   │   ├── async_tools.py
│   │   ├── concurrency.py
│   │   ├── cancellation.py
│   │   ├── backpressure.py
│   │   └── test_async_tools.py
│   │
│   ├── day26_durable_workflow/  # 持久化工作流
│   │   ├── workflow.py
│   │   ├── task_queue.py
│   │   ├── worker.py
│   │   ├── storage.py
│   │   └── test_recovery.py
│   │
│   ├── day27_sandbox_model/     # Sandbox 与模型服务
│   │   ├── sandbox_fs.py
│   │   ├── sandbox_shell.py
│   │   ├── model_client.py
│   │   ├── docker-compose.yml
│   │   └── README.md
│   │
│   ├── day28_benchmark/         # 故障演练与性能压测
│   │   ├── failure_scenarios.py
│   │   ├── load_test.py
│   │   ├── metrics.py
│   │   └── reports/
│   │
│   ├── integration/             # 第 4 周最终整合版本
│   │   ├── runtime.py
│   │   ├── run_demo.py
│   │   └── test_runtime.py
│   │
│   ├── scripts/
│   │   ├── run_day22.sh
│   │   ├── run_day24_resume.sh
│   │   └── benchmark.sh
│   │
│   └── docs/
│       ├── 01-harness.md
│       ├── 02-context-cache.md
│       ├── 03-state-resume.md
│       ├── 04-async-concurrency.md
│       ├── 05-durable-workflow.md
│       ├── 06-sandbox-model-service.md
│       └── 07-benchmark-report.md

```

```
day22 Agent Loop
   ↓
day23 Context / Cache
   ↓
day24 State / Checkpoint / Idempotency
   ↓
day25 Async Tool Scheduler
   ↓
day26 Durable Workflow
   ↓
day27 Sandbox / Model Service
   ↓
day28 Failure Test / Benchmark
   ↓
integration/runtime.py
```

## Day 27：Sandbox 与模型服务

### 学习目标

让 Agent 能够使用文件、Shell、网络和模型服务，同时把每一种能力限制在明确的边界内：

```text
Agent
  → Policy / Tool Gateway
      ├── 文件沙箱：只允许工作目录
      ├── Shell 沙箱：限制命令、用户、资源和生命周期
      ├── 网络沙箱：默认拒绝，按域名或服务放行
      ├── 凭据代理：工具拿短期、最小权限凭据
      └── 模型服务：通过内部 API 调用开源模型
```

核心原则：模型输出是不可信输入；沙箱不是提示词约束，而是操作系统、容器、网络和凭据系统提供的真实边界。

### 一、文件隔离

- 为每个 Agent 运行创建独立工作目录，并设置生命周期和磁盘配额。
- 使用路径规范化、符号链接检查和目录白名单，防止 `../` 越权读取。
- 默认只挂载必要目录；宿主机目录、Docker socket、SSH key 和项目源码不应直接暴露。
- 区分临时输入、产物和日志，任务结束后按策略清理或归档。
- 记录文件读写审计：谁、何时、访问了什么、结果如何。

### 二、Shell 隔离

- 不把模型生成的字符串直接拼接进 `shell=True` 命令。
- 优先使用参数数组和允许命令表，例如 `subprocess.run(["python", "script.py"], shell=False)`。
- 限制工作目录、环境变量、用户权限、CPU、内存、进程数、执行时间和输出大小。
- 设置进程组；超时或取消时杀掉整个进程树，避免后台进程逃逸。
- 禁止危险能力：特权容器、宿主网络、设备访问、任意挂载、Docker socket。
- 将编译、数据处理、代码执行和部署命令分成不同权限级别。

### 三、网络隔离

- 默认无网络；只有确实需要的工具才允许出网。
- 使用 egress allowlist 限制域名、端口、协议和请求方法。
- 阻止访问云元数据服务、内网管理端口、回环地址和私有网段，防止 SSRF。
- 代理层统一处理 DNS、TLS、超时、重试、速率限制和请求审计。
- 将“允许模型服务访问模型仓库”和“允许 Agent 工具访问业务 API”分成不同网络策略。

### 四、凭据隔离

- 不把 API key、数据库密码、云凭据放进 prompt、状态、日志或工作目录。
- 使用凭据代理或短期 token，按工具和请求签发最小权限凭据。
- 通过环境注入或文件描述符传递凭据，避免命令行参数泄露到进程列表。
- 对日志、异常和模型上下文做脱敏；限制模型看到的凭据范围。
- 凭据应可撤销、轮换、过期，并记录使用审计。

### 五、开源模型服务化

模型服务化要把“模型推理进程”和“Agent 编排进程”分开：

```text
Agent Runtime → OpenAI-compatible HTTP API → vLLM / SGLang / TensorRT-LLM
```

学习内容：

- 离线批量推理与在线服务的区别。
- 模型权重、Tokenizer、GPU 显存和量化格式的关系。
- 请求队列、连续批处理、KV Cache、最大上下文和最大并发。
- streaming、工具调用、结构化输出和停止条件。
- timeout、取消、限流、熔断、重试以及模型服务故障时的降级。
- 采集首 token 延迟、端到端延迟、吞吐量、排队时间、显存和错误率。
- 模型服务 API 鉴权、网络隔离、模型仓库权限和权重供应链安全。

### 六、服务框架选择

先用 [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart.html) 学习离线推理和 OpenAI 兼容在线服务，再对比：

- [SGLang](https://github.com/sgl-project/sglang)：关注复杂生成程序、结构化生成和高性能服务。
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)：关注 NVIDIA GPU 上的编译优化、量化和生产级高性能推理。

不要先比较“哪个框架绝对更快”。先固定模型、硬件、上下文长度、并发、采样参数和数据集，再测 TTFT、TPOT、P95/P99 延迟、吞吐量和显存占用。

### 七、推荐实践顺序

1. 用普通 Python 实现文件沙箱：路径白名单、配额和清理。
2. 用 `subprocess` 实现 Shell 工具：无 shell、超时、进程组和输出上限。
3. 为 HTTP 工具加网络 allowlist、SSRF 防护和请求审计。
4. 接入凭据代理，验证 prompt、日志和异常中不会出现密钥。
5. 用 vLLM 启动一个 OpenAI-compatible 服务，Agent 只通过 HTTP 调用。
6. 用固定基准对比 vLLM、SGLang 或 TensorRT-LLM，记录性能和资源成本。
7. 注入故障：杀掉沙箱进程、阻断网络、撤销 token、重启模型服务，验证 Agent 能超时、取消、恢复或安全失败。

### 最小验收清单

- Agent 不能读取工作目录之外的文件。
- Shell 超时后没有遗留子进程。
- 未在 allowlist 中的域名和私网地址访问会被拒绝。
- 日志、checkpoint 和模型上下文不包含明文凭据。
- 模型服务与 Agent Runtime 通过受控 API 通信，而不是共享 GPU 进程或宿主权限。
- 模型服务重启时，请求有明确的超时、重试或降级结果。
- 性能报告至少包含 TTFT、总延迟、吞吐量、P95/P99 和显存占用。
