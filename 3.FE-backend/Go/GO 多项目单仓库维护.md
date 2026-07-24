# GO 多项目单仓库维护

## 方案一：单 Go Module 结构

如果这 4 个小项目只是你的练习作业（例如 Mini-Grep、简易 HTTP 服务器、KV 存储等），**强烈推荐这种方式**。整个仓库只在根目录有一个 `go.mod` 文件。

### 目录结构

Plaintext

```
my-go-projects/          <-- Git 仓库根目录
├── go.mod               <-- 整个仓库唯一的 module
├── go.sum
├── README.md
├── cmd/                 <-- 存放所有可执行程序的入口
│   ├── mini-grep/
│   │   └── main.go
│   ├── mini-redis/
│   │   └── main.go
│   ├── http-server/
│   │   └── main.go
│   └── chat-room/
│       └── main.go
└── pkg/                 <-- （可选）多个项目通用的公共代码/工具包
    └── utils/
        └── utils.go
```

### 为什么推荐这种方式？

1. **零配置成本：** 只需要运行一次 `go mod init my-go-projects`。

2. **共享依赖极其方便：** 如果项目 A 和项目 B 都用到了同一个第三方库（比如 `logrus`），根目录的 `go.mod` 一次性管理即可。

3. **极佳的编译体验：** Go 官方非常推荐 `cmd/` 这种目录约定。你在根目录下直接运行下面的命令就能构建对应的程序：

   ```Bash
   # 构建 mini-grep
   go build ./cmd/mini-grep
   
   # 运行 mini-grep
   go run ./cmd/mini-grep --path ./test --key "hello"
   ```

## 方案二：Go Workspaces 多 Module 结构（适合彻底隔离的项目）

如果你的 4 个项目**完全独立**，甚至未来有可能把其中某一个项目拆出去单独发版，或者各个项目依赖的第三方库版本有冲突，你可以为每个子目录单独建 `go.mod`，并使用 Go 官方支持的 **Go Workspaces (`go.work`)**。

### 目录结构

```Plaintext
my-go-projects/          <-- Git 仓库根目录
├── go.work              <-- Go 工作区配置文件
├── README.md
├── mini-grep/
│   ├── go.mod           <-- 独立的 module
│   └── main.go
├── mini-redis/
│   ├── go.mod
│   └── main.go
└── http-server/
    ├── go.mod
    └── main.go
```

### 如何设置？

在根目录下运行：

```Bash
# 1. 初始化工作区
go work init

# 2. 把各个子项目加入工作区
go work use ./mini-grep ./mini-redis ./http-server
```

> **这种方式的好处：** 每个子项目彻底解耦，依赖互不干扰；但在本地开发时，Go 依然能感知到它们同属于一个工作区。

## 总结与建议

| **需求场景**                               | **推荐方案**                          | **核心优势**                       |
| ------------------------------------------ | ------------------------------------- | ---------------------------------- |
| **日常练习 / 学习项目集 / 快速写 Demo**    | **方案一：单 `go.mod` + `cmd/` 目录** | 最省心，极速构建，符合 Go 社区规范 |
| **独立性极强 / 依赖冲突 / 未来的开源单品** | **方案二：多 `go.mod` + `go.work`**   | 边界清晰，完全隔离                 |

