# Day 33：容器化与服务编排

本阶段学习如何把 Agent 服务打包成容器，并使用 Docker Compose 编排 API、Worker、Redis、数据库和监控服务。

参考：

- [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Compose](https://docs.docker.com/compose/)

## 项目启动

启动前创建 Secret：

```bash
cd observability_deployment/day33_containerization_service_orchestration

mkdir -p secrets
printf '%s' "$DEEPSEEK_API_KEY" > secrets/deepseek_api_key.txt

docker compose up --build
```

验证审批状态恢复：

```bash
curl -X POST http://localhost:8000/approvals \
  -H 'Content-Type: application/json' \
  -d '{"task_id":"task-1"}'

docker compose restart api

curl http://localhost:8000/approvals/task-1
```

验证 Redis 故障：

```bash
docker compose stop redis
curl -i http://localhost:8000/health/ready
docker compose start redis
```


## 学习目标

- 理解 Image、Container、Volume 的区别。
- 编写可缓存、可复现的 Dockerfile。
- 使用 Compose 编排多容器 Agent 应用。
- 使用内部网络隔离 API、Worker、Redis 和数据库。
- 将 API Key 等 Secrets 在运行时注入，不写入镜像。
- 配置健康检查、启动顺序、重启和持久化状态。
- 处理 Agent 的超时、重试、幂等和任务恢复。

## 一、容器基础

```text
Dockerfile → docker build → Image → docker run → Container
                                             ↓
                                           Volume
```

- Image：应用代码、依赖和启动命令的静态打包结果。
- Container：Image 的运行实例，拥有隔离的进程、文件系统和网络。
- Volume：容器重建后仍需保留的数据，例如审批状态、任务状态和数据库文件。

容器内的临时文件不能作为可靠的持久化存储。

## 二、Dockerfile

典型 FastAPI Agent 服务：

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

学习重点：

- 固定基础镜像版本，避免环境漂移。
- 先复制依赖文件再安装，利用 Docker 构建缓存。
- 最后复制经常变化的业务代码。
- 使用 exec form 的 `CMD`，正确接收停止信号。
- 用 `.dockerignore` 排除 `.env`、缓存、虚拟环境和测试产物。
- 尽量使用非 root 用户运行服务。

## 三、Agent 服务拆分

```text
api       → 对外提供 FastAPI 接口
worker    → 执行异步 Agent 任务
redis     → 队列、短期状态和限流
postgres  → 用户、任务和审批状态
prometheus→ 采集运行指标
grafana   → 展示监控大盘
```

不要把 API、数据库、Redis 和 Prometheus 全部安装在同一个镜像中。独立服务可以分别扩容、重启和限制权限。

## 四、Docker Compose

Compose 用 YAML 描述服务、网络、卷、环境变量和健康检查：

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      redis:
        condition: service_healthy
    networks: [app_net]

  redis:
    image: redis:7-alpine
    networks: [app_net]

networks:
  app_net:
    internal: true
```

容器之间用服务名访问：

```text
redis://redis:6379
http://api:8000
```

不要在容器内用 `localhost` 访问另一个服务；`localhost` 指向当前容器。

## 五、网络隔离

建议至少分为：

```text
public_net 反向代理 ↔ API
private_net API ↔ Redis ↔ 数据库
```

- 数据库和 Redis 不暴露到公网。
- 只有 API 或反向代理绑定宿主机端口。
- Agent 工具容器只连接必要的内部服务。
- 网络隔离可以降低 Prompt Injection 造成横向移动的风险。

## 六、Secrets 与配置

不要把密钥写进 Dockerfile：

```dockerfile
ENV DEEPSEEK_API_KEY=真实密钥
```

也不要把 `.env` 复制进镜像或提交 Git。开发环境可使用未提交的 `.env`，生产环境应使用 Secret Manager、Vault 或平台 Secret 机制，在运行时注入：

```yaml
services:
  api:
    env_file: [.env]
```

配置分类：

| 类型 | 示例 | 位置 |
| --- | --- | --- |
| 非敏感配置 | `LOG_LEVEL=INFO` | 环境变量/Compose |
| 敏感配置 | `DEEPSEEK_API_KEY` | Secret Manager |
| 持久化状态 | 审批、任务状态 | Volume/数据库 |
| 构建依赖 | Python 版本和包 | requirements/lock |

## 七、健康检查与生命周期

应用至少提供：

```text
/health/live   进程是否存活
/health/ready  依赖是否就绪
```

区分 liveness、readiness 和 startup。`depends_on` 只能帮助编排启动顺序，不能替代应用连接重试和健康判断。

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health/ready"]
  interval: 10s
  timeout: 3s
  retries: 5
```

## 八、Agent 特有的部署问题

- 模型 API 需要超时、限流和重试。
- 长任务不能依赖 HTTP 连接一直保持。
- 任务和审批状态必须持久化，容器重启后可恢复。
- Worker 重试要保证幂等，避免重复扣款或重复发邮件。
- Token、成本、延迟和错误指标要暴露给 Prometheus。
- 日志不能输出 API Key、PII 和完整敏感 Prompt。

## 九、常用命令

```bash
docker compose up --build
docker compose up -d
docker compose ps
docker compose logs -f api
docker compose exec api sh
docker compose down
docker compose down -v  # 会删除卷中的数据，谨慎使用
```

## 十、练习顺序

1. 为一个 FastAPI Agent 编写最小 Dockerfile。
2. 用 `.dockerignore` 排除密钥和本地文件。
3. 用 Compose 启动 API 和 Redis。
4. 增加 live/readiness 健康检查。
5. 增加 Prometheus、Grafana 和内部监控网络。
6. 把 DeepSeek Key 从镜像移到运行时 Secret。
7. 把审批状态从内存迁移到 Volume 或数据库。
8. 模拟 API 重启，验证任务和审批状态恢复。
9. 模拟 Redis/模型服务不可用，验证超时、重试和 readiness。
10. 使用非 root 用户运行镜像，检查不必要的端口暴露。

## 十一、完成标准

- `docker compose up --build` 能启动应用栈。
- 服务之间使用服务名通信。
- `.env` 和 Secrets 不进入镜像层。
- 数据库和 Redis 不暴露不必要的宿主机端口。
- 健康检查能区分存活和就绪。
- Agent 任务、审批状态和监控指标按设计恢复。
- 容器日志不包含 API Key、PII 和敏感上下文。

## 十二、可运行 Demo

本目录已经提供一个最小应用栈：

```text
api → FastAPI Agent API
redis → 任务计数和任务状态
prometheus → 抓取 /metrics
grafana → 监控展示
```

文件说明：

- `app/main.py`：API、健康检查、Redis 重试、运行时 Secret 和审批状态。
- `Dockerfile`：依赖缓存、非 root 用户和 8000 端口。
- `docker-compose.yml`：API、Redis、Prometheus、Grafana、网络、Secret 和 Volume。
- `prometheus.yml`：从 `api:8000/metrics` 抓取指标。
- `.dockerignore`：排除 `.env`、`secrets/`、Git 和本地缓存。

### 启动

先创建本地 Secret，不要提交这个文件：

```bash
mkdir -p secrets
printf '%s' "$DEEPSEEK_API_KEY" > secrets/deepseek_api_key.txt
docker compose up --build
```

访问：

```text
API:         http://localhost:8000
Liveness:    http://localhost:8000/health/live
Readiness:   http://localhost:8000/health/ready
Prometheus:  http://localhost:9090
Grafana:     http://localhost:3000
```

### 验证任务和审批状态恢复

```bash
curl -X POST http://localhost:8000/approvals \
  -H 'Content-Type: application/json' \
  -d '{"task_id":"task-1"}'

docker compose restart api

curl http://localhost:8000/approvals/task-1
```

重启后仍应返回：

```json
{"task_id":"task-1","status":"pending_approval"}
```

状态来自 `agent_state` Volume，而不是容器内存。

### 验证 readiness 和 Redis 重试

```bash
docker compose stop redis
curl -i http://localhost:8000/health/ready
docker compose start redis
```

Redis 停止时 readiness 返回 `503`，API 会按 `REDIS_MAX_RETRIES` 进行有限重试；Redis 恢复并通过健康检查后，readiness 恢复为 `200`。

### 完成标准对应关系

| 标准 | 实现 |
| --- | --- |
| Compose 启动应用栈 | `docker-compose.yml` |
| 服务名通信 | `REDIS_URL=redis://redis:6379/0`、Prometheus target `api:8000` |
| Secrets 不进镜像 | Compose Secret 挂载到 `/run/secrets`，`.dockerignore` 排除本地 Secret |
| 不暴露 Redis | Redis 只加入 `app_net`，没有 `ports` |
| live/readiness | `/health/live` 和 `/health/ready` |
| 状态恢复 | `agent_state:/data` |
| 指标恢复/采集 | `/metrics` + Prometheus `api:8000` |
| 超时/重试 | `redis_ping_with_retry()` |
| 非 root | Dockerfile 使用 UID `10001` 的 `appuser` |

生产环境仍应替换示例 Secret、固定所有依赖版本，并使用真正的 Secret Manager；本 Demo 只用于学习容器边界和编排关系。

FastAPI 官方教程强调用镜像打包依赖、利用 Docker 缓存并以容器作为部署单元；Compose 用于定义和运行多容器应用。[FastAPI Docker](https://fastapi.tiangolo.com/deployment/docker/)、[Docker Compose](https://docs.docker.com/compose/)
