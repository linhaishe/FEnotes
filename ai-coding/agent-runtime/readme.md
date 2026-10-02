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