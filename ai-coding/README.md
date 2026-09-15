# 尚硅谷 AI 课程笔记

尚硅谷 Python / LangChain / LangGraph / AI Coding 课程配套课件与代码整理

## 在线站点：

https://github.com/xbsheng/atguigu-note/tree/main

本地预览：

```
pnpm install
pnpm docs:dev
```

## 课程目录

| 课程                                                         | 说明                                                   | 在线视频                                                    | 详情                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------ |
| [Python](https://github.com/xbsheng/atguigu-note/blob/main/python) | Python 零基础入门到进阶（进程 / 线程 / 协程）          | [BV1tDsgzxECr](https://www.bilibili.com/video/BV1tDsgzxECr) | [README](https://github.com/xbsheng/atguigu-note/blob/main/python/README.md) |
| [LangChain](https://github.com/xbsheng/atguigu-note/blob/main/langchain) | LangChain 1.2 入门到 Agent / RAG 实战                  | [BV1rv7A6oEeP](https://www.bilibili.com/video/BV1rv7A6oEeP) | [README](https://github.com/xbsheng/atguigu-note/blob/main/langchain/README.md) |
| [LangGraph](https://github.com/xbsheng/atguigu-note/blob/main/langgraph) | LangGraph 入门到智能体部署实战                         | [BV1z3NY66EY1](https://www.bilibili.com/video/BV1z3NY66EY1) | [README](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/README.md) |
| [AI Coding](https://github.com/xbsheng/atguigu-note/blob/main/vibe_coding) | Vibe Coding 零基础实战（Claude Code / Skills / Codex） | [BV1RPET6tEp2](https://www.bilibili.com/video/BV1RPET6tEp2) | [README](https://github.com/xbsheng/atguigu-note/blob/main/vibe_coding/README.md) |

## 推荐项目

**[PyBridge](https://pybridge.quarkcode.cn/)** · 写给 Java / JS / Go 开发者的 Python 速查卡 —— 52 条概念映射词典（HashMap → dict、goroutine → asyncio）、三条来源语言的对照式课程、浏览器内直接运行 Python，无需安装环境。有其他语言基础的话，配合本站 Python 课程食用效率翻倍。（[GitHub 仓库](https://github.com/xbsheng/pybridge)）

## 仓库结构

```text
atguigu-note/
├── index.md              # 站点首页
├── .vitepress/           # VitePress 配置
├── .github/workflows/    # GitHub Pages 自动部署
├── python/               # Python 课件（按章节拆分）+ 代码 + 分 P 目录
├── langchain/            # LangChain 课件 + 代码 + 分 P 目录
├── langgraph/            # LangGraph 课件 + 代码 + 分 P 目录
└── vibe_coding/          # AI Coding（Vibe Coding）课件 + 代码 + 分 P 目录
```

站点直接复用各课程下的 `课件/` Markdown，无需复制文件。

## 学习建议

1. 打开站点或对应课程 README，按分 P 在 B 站在线观看
2. 对照课件复习笔记
3. 站点上的「Notebook 在线阅读」页面（LangChain / LangGraph）可直接在浏览器中打开配套 Notebook 跟练
4. AI Coding 课程可对照 `vibe_coding/代码/AICoding/` 下的实战项目练习

## 版权说明

课程版权归 [尚硅谷](http://www.atguigu.com/) 所有，本仓库仅供学习交流使用。