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

## 安全边界与限制

- `Workspace` 每次运行创建临时目录，限制路径与文件大小；容器只读挂载该目录。Python 路径检查只保护工具入口；遇到不可信并发写入和链接替换时，需要更强的文件系统隔离。
- Shell 只运行 `list` 与 `syntax` 两个固定检查。Docker 容器禁网络、禁提权、只读根文件系统，并限制 CPU、内存、进程数、时间与输出。生产部署还需按环境固定镜像 digest、限制 Docker daemon 权限与实际宿主挂载。
- 模型 URL 由部署者配置，模型输出不能提供 URL。客户端检查域名和解析后的 IP；生产环境还需网络层 egress 规则，防止 DNS 重绑定和进程绕过 Python 检查。
- Token 只在 HTTP Header 中使用，不写入 prompt、工作区或返回结果。演示使用环境变量；生产环境应换成短期凭据代理。
- 审计日志只保存任务状态，不保存源码或凭据。若项目源码本身含密钥，当前示例不会识别它们，向模型发送源码前需要额外的内容审查。
- 模型返回的文本只当报告展示，不当文件路径或 Shell 命令执行。

## 验证重点

`test_security.py` 使用本地模拟模型响应验证工作区逃逸、命令白名单、地址拒绝、凭据缺失、报告不执行和模型降级。Docker 实际隔离需要在有 Docker daemon 的主机上运行 `worker.py` 并复核容器权限；测试中的容器调用使用替身，不能代替部署环境安全审计。
