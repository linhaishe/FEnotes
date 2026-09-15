# 尚硅谷 LangChain 1.2 教程（2026 版）

> LangChain 学习一套通：从入门到 Agent / 中间件 / 记忆 / RAG 综合项目实战
> 讲师：尚硅谷 · 宋红康

## 在线视频（推荐）

**无需百度网盘会员，B 站直接在线观看：**

🎬 [2026 版 LangChain 教程 · Agent 智能体 · RAG 项目实战](https://www.bilibili.com/video/BV1rv7A6oEeP)

------

## 仓库结构

```text
langchain/
├── README.md                 # 本说明（含分 P 在线目录）
├── 课件/                     # Markdown 课件（可在线阅读）
│   ├── 01-LangChain概述.md
│   ├── 02-模型的创建与调用.md
│   ├── ...
│   ├── 10-RAG.md
│   └── assets/               # 章节共用图片资源
└── 代码/
    └── langchain1.2_tutorial/  # Jupyter Notebook 实战代码
        ├── chapter02_model/
        ├── chapter03_langsmith/
        ├── ...
        ├── chapter10-RAG/
        ├── requirements.txt
        └── requirements_full.txt
```

------

## 学习路线 & 资料对照

| 章节                            | 课件                                                         | 代码                                                         | 视频分 P    |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| 第 01 章 · LangChain 概述       | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/01-LangChain概述.md) | [chapter01_summary](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter01_summary) | P1 – P10    |
| 第 02 章 · 模型的创建与调用     | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/02-模型的创建与调用.md) | [chapter02_model](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter02_model) | P11 – P22   |
| 第 03 章 · LangSmith 的使用     | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/03-LangSmith的使用.md) | [chapter03_langsmith](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter03_langsmith) | P23 – P24   |
| 第 04 章 · Message 与提示词模板 | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/04-Message与提示词模板.md) | [chapter04_messages_prompt](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter04_messages_prompt) | P25 – P32   |
| 第 05 章 · Tools                | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/05-Tools.md) | [chapter05-tools](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter05-tools) | P33 – P40   |
| 第 06 章 · 结构化输出           | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/06-结构化输出.md) | [chapter06-structured_output](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter06-structured_output) | P41 – P50   |
| 第 07 章 · 智能体               | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/07-智能体.md) | [chapter07-Agents](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter07-Agents) | P51 – P63   |
| 第 08 章 · 中间件               | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/08-中间件.md) | [chapter08-Middleware](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter08-Middleware) | P64 – P85   |
| 第 09 章 · 上下文与记忆         | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/09-上下文与记忆.md) | [chapter09-memory](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter09-memory) | P86 – P101  |
| 第 10 章 · RAG                  | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langchain/课件/10-RAG.md) | [chapter10-RAG](https://github.com/xbsheng/atguigu-note/blob/main/langchain/代码/langchain1.2_tutorial/chapter10-RAG) | P102 – P120 |



## 快速开始（本地跑代码）

```
cd langchain/代码/langchain1.2_tutorial

# 建议使用 conda / venv 创建独立环境后安装依赖
pip install -r requirements.txt
# 或完整依赖：
# pip install -r requirements_full.txt

# 用 Jupyter / VS Code / Cursor 打开对应章节的 .ipynb 即可跟练
```

------

## 使用建议

1. **看视频**：点上方 B 站链接在线观看，按分 P 跳转，不需要下载，也不需要百度网盘会员。
2. **看课件**：打开 `课件/` 下对应章节的 Markdown，配合视频笔记复习。
3. **练代码**：打开 `代码/langchain1.2_tutorial/` 下对应 `chapter*` 目录中的 Notebook 动手实践。
4. **做项目**：第 10 章 RAG + Assistant 客服知识库可作为综合实战收尾。

------

## 版权说明

课程版权归 [尚硅谷](http://www.atguigu.com/) 所有。本仓库整理课件与代码目录，仅供学习交流使用。