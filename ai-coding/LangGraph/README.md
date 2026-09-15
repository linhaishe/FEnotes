# 尚硅谷 LangGraph 教程

> 从入门到部署，零基础上手智能体 Agent 必备技能

## 在线视频（推荐）



🎬 [尚硅谷 LangGraph 教程 · 入门 · 智能体项目实战](https://www.bilibili.com/video/BV1z3NY66EY1)

------

## 仓库结构



```text
langgraph/
├── README.md                 # 本说明（含分 P 在线目录）
├── 课件/                     # Markdown 课件（可在线阅读）
│   ├── 00-环境配置.md
│   ├── 01-LangGraph基础入门.md
│   ├── 02-LangGraph控制流与节点执行.md
│   ├── 03-LangGraph持久化与记忆管理.md
│   ├── 04-LangGraph中断与工具与部署.md
│   ├── 05-LangGraph高级特性.md
│   └── images/
└── 代码/
    └── langgraph/            # Jupyter Notebook 实战代码
        ├── chapter01/
        ├── chapter02/
        ├── chapter03/
        ├── chapter04/
        ├── chapter05/
        ├── hitl_demo/
        └── requirements_full.txt
```



------

## 学习路线 & 资料对照



| 章节                               | 课件                                                         | 代码                                                         | 视频分 P    |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| 第 00 章 · 环境配置                | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/00-环境配置.md) | —                                                            | P1 – P7     |
| 第 01 章 · LangGraph 基础入门      | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/01-LangGraph基础入门.md) | [chapter01](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/代码/langgraph/chapter01) | P8 – P27    |
| 第 02 章 · 控制流与节点执行        | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/02-LangGraph控制流与节点执行.md) | [chapter02](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/代码/langgraph/chapter02) | P28 – P55   |
| 第 03 章 · 持久化与记忆管理        | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/03-LangGraph持久化与记忆管理.md) | [chapter03](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/代码/langgraph/chapter03) | P56 – P83   |
| 第 04 章 · 中断与工具与部署        | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/04-LangGraph中断与工具与部署.md) | [chapter04](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/代码/langgraph/chapter04) | P84 – P106  |
| 第 05 章 · 高级特性（流式 / 子图） | [课件](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/05-LangGraph高级特性.md) | [chapter05](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/代码/langgraph/chapter05) | P107 – P132 |

------

## 完整视频目录（点击即可跳转对应分 P）



> 链接格式：`https://www.bilibili.com/video/BV1z3NY66EY1?p=N`，打开后直接定位到第 N 集。

### 第 00 章 · 环境配置（P1 – P7）



| P    | 标题                                   | 时长  | 在线观看                                                  |
| ---- | -------------------------------------- | ----- | --------------------------------------------------------- |
| 1    | 01_LangGraph 教程介绍                  | 06:02 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=1) |
| 2    | 02_环境部署_miniConda                  | 13:50 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=2) |
| 3    | 03*环境部署*创建并激活 python 虚拟环境 | 07:16 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=3) |
| 4    | 04*环境部署*按照依赖库                 | 14:57 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=4) |
| 5    | 05*环境部署*配置 API key               | 04:31 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=5) |
| 6    | 06_环境部署_Jupyter 工具部署           | 08:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=6) |
| 7    | 07*环境部署*进行环境验证               | 03:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=7) |

### 第 01 章 · LangGraph 基础入门（P8 – P27）



| P    | 标题                                        | 时长  | 在线观看                                                   |
| ---- | ------------------------------------------- | ----- | ---------------------------------------------------------- |
| 8    | 08_入门基础_langchain 和 langgraph 定位区别 | 07:09 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=8)  |
| 9    | 09_入门基础_langgraph 三要素组成            | 06:50 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=9)  |
| 10   | 10*入门基础*图运行过程                      | 07:00 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=10) |
| 11   | 11_入门基础_API 风格选择                    | 04:37 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=11) |
| 12   | 12*入门基础*完成基础的 graph 流程           | 16:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=12) |
| 13   | 13*入门基础*图结构可视化展示                | 10:51 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=13) |
| 14   | 14*入门基础*状态的多种实现 dataclass        | 07:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=14) |
| 15   | 15*入门基础*状态的多种实现 pydantic         | 08:21 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=15) |
| 16   | 16*入门基础*状态合并定义 reducer            | 08:33 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=16) |
| 17   | 17_入门基础_reducer 在 langgraph 中的应用   | 08:49 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=17) |
| 18   | 18*入门基础*状态归约的使用                  | 10:04 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=18) |
| 19   | 19*入门基础*节点中调用状态                  | 08:41 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=19) |
| 20   | 20*入门基础*节点更新状态                    | 08:12 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=20) |
| 21   | 21*入门基础*节点的并行执行                  | 10:47 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=21) |
| 22   | 22_入门基础_langgraph 的 4 种状态           | 05:22 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=22) |
| 23   | 23*入门基础*状态的使用规范                  | 07:28 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=23) |
| 24   | 24*入门基础*状态的源码实现逻辑              | 08:15 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=24) |
| 25   | 25*入门基础*四种状态的案例讲解              | 13:26 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=25) |
| 26   | 26*入门基础*预定义状态                      | 14:40 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=26) |
| 27   | 27_入门基础_AgentState 和总结               | 04:01 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=27) |

### 第 02 章 · 控制流与节点执行（P28 – P55）



| P    | 标题                             | 时长  | 在线观看                                                   |
| ---- | -------------------------------- | ----- | ---------------------------------------------------------- |
| 28   | 28*控制流*边的简单使用           | 03:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=28) |
| 29   | 29_控制流_add_sequence           | 05:47 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=29) |
| 30   | 30*控制流*并行节点               | 05:30 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=30) |
| 31   | 31*控制流*并行运行展示           | 08:47 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=31) |
| 32   | 32*控制流*条件分支               | 09:32 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=32) |
| 33   | 33*控制流*使用 path_map          | 04:14 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=33) |
| 34   | 34*控制流*映射多节点             | 09:33 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=34) |
| 35   | 35*控制流*延时节点执行           | 12:21 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=35) |
| 36   | 36*控制流*动态分支               | 22:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=36) |
| 37   | 37_控制流_command 控制           | 12:22 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=37) |
| 38   | 38*控制流*静态扇入               | 12:32 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=38) |
| 39   | 39*控制流*动态扇入               | 28:46 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=39) |
| 40   | 40_控制流_agent 构建中的循环结构 | 06:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=40) |
| 41   | 41*控制流*大模型配置工具调用     | 09:25 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=41) |
| 42   | 42*控制流*静态循环控制           | 30:25 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=42) |
| 43   | 43*控制流*循环结构的动态实现     | 10:20 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=43) |
| 44   | 44*控制流*限制循环步数           | 07:01 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=44) |
| 45   | 45*控制流*主动退出               | 14:08 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=45) |
| 46   | 46*控制流*被动方法               | 11:27 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=46) |
| 47   | 47*控制流*边的总结               | 07:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=47) |
| 48   | 48*控制流*重试机制               | 13:36 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=48) |
| 49   | 49_控制流_retry_on 参数配置      | 06:27 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=49) |
| 50   | 50*控制流*超时控制               | 04:17 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=50) |
| 51   | 51*控制流*错误处理               | 02:38 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=51) |
| 52   | 52*控制流*节点缓存               | 05:33 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=52) |
| 53   | 53*控制流*缓存实例演示           | 15:27 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=53) |
| 54   | 54*控制流*缓存配置详解           | 03:20 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=54) |
| 55   | 55*控制流*全图默认配置           | 02:07 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=55) |

### 第 03 章 · 持久化与记忆管理（P56 – P83）



| P    | 标题                                     | 时长  | 在线观看                                                   |
| ---- | ---------------------------------------- | ----- | ---------------------------------------------------------- |
| 56   | 56*持久化*可恢复执行的含义               | 03:55 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=56) |
| 57   | 57*持久化*持久化机制介绍                 | 07:21 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=57) |
| 58   | 58*持久化*启用可恢复执行                 | 06:58 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=58) |
| 59   | 59*持久化*内存持久化                     | 16:19 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=59) |
| 60   | 60*持久化*内存持久化和数据库持久化的区别 | 02:48 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=60) |
| 61   | 61*持久化*安装 postgreSQL                | 11:34 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=61) |
| 62   | 62_持久化_pgSQL 基础使用介绍             | 06:51 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=62) |
| 63   | 63*持久化*创建 pgSQL 的数据库和用户      | 04:38 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=63) |
| 64   | 64_持久化_pgSQL 基础增删改查             | 04:37 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=64) |
| 65   | 65*持久化*使用数据库作为检查点           | 11:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=65) |
| 66   | 66*持久化*数据库检查点后端表结构         | 12:31 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=66) |
| 67   | 67_持久化-持久化模式                     | 10:10 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=67) |
| 68   | 68*持久化*查看历史检查点样例代码编写     | 19:52 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=68) |
| 69   | 69*持久化*查看所有检查点记录             | 15:48 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=69) |
| 70   | 70_持久化-查询单独一个检查点             | 06:15 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=70) |
| 71   | 71*持久化*失败恢复运行                   | 03:57 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=71) |
| 72   | 72*持久化*演示运行异常案例               | 25:22 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=72) |
| 73   | 73*持久化*错误恢复运行                   | 05:06 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=73) |
| 74   | 74*持久化*检查点重新运行                 | 09:59 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=74) |
| 75   | 75_持久化_fork 的案例代码                | 13:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=75) |
| 76   | 76_持久化_fork 案例代码                  | 12:18 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=76) |
| 77   | 77_持久化_fork 实现演示                  | 17:12 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=77) |
| 78   | 78*持久化*长期记忆数据库存储             | 16:57 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=78) |
| 79   | 79*持久化*长期记忆数据的使用上           | 17:27 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=79) |
| 80   | 80*持久化*长期记忆数据的使用下           | 22:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=80) |
| 81   | 81*持久化*环境上下文记忆                 | 18:18 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=81) |
| 82   | 82*持久化*节点总结                       | 07:28 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=82) |
| 83   | 83*持久化*节点的触发和执行总结           | 09:35 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=83) |

### 第 04 章 · 中断与工具与部署（P84 – P106）



| P    | 标题                                         | 时长  | 在线观看                                                    |
| ---- | -------------------------------------------- | ----- | ----------------------------------------------------------- |
| 84   | 84*中断*两种中断机制                         | 03:31 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=84)  |
| 85   | 85*中断*主动中断的具体执行                   | 08:49 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=85)  |
| 86   | 86_中断_HITL 案例演示                        | 13:34 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=86)  |
| 87   | 87*中断*并行执行多个中断                     | 14:59 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=87)  |
| 88   | 88*中断*审批模型                             | 17:03 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=88)  |
| 89   | 89*中断*其余案例                             | 14:30 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=89)  |
| 90   | 90*中断*使用规范                             | 10:39 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=90)  |
| 91   | 91*中断*触发中断时检查点信息                 | 11:40 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=91)  |
| 92   | 92*中断*多个并行中断的检查点                 | 06:43 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=92)  |
| 93   | 93*中断*同一超步部分任务触发中断的检查点     | 06:57 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=93)  |
| 94   | 94*中断*静态中断用法介绍                     | 09:54 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=94)  |
| 95   | 95*中断*静态断点基础案例                     | 11:01 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=95)  |
| 96   | 96*中断*静态中断出现在超步位置               | 06:20 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=96)  |
| 97   | 97*中断*执行设置断点                         | 03:29 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=97)  |
| 98   | 98*项目部署*本地部署对接 Langsmith           | 13:01 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=98)  |
| 99   | 99_项目部署_Langsmith 的调试使用             | 03:49 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=99)  |
| 100  | 100*项目部署*大模型 agent 部署               | 11:15 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=100) |
| 101  | 101*工具节点*手动调用工具案例代码上          | 14:52 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=101) |
| 102  | 102*工具节点*手动调研工具案例下              | 18:33 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=102) |
| 103  | 103*工具节点*使用 ToolNode 替代手动调用      | 03:19 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=103) |
| 104  | 104*工具节点*使用 ToolRuntime 自定义工具代码 | 11:15 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=104) |
| 105  | 105_工具节点_wrap_tool_call                  | 23:41 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=105) |
| 106  | 106*工具节点*实现自定义缓存                  | 14:19 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=106) |

### 第 05 章 · 高级特性（流式 / 子图 / 图设计）（P107 – P132）



| P    | 标题                                  | 时长  | 在线观看                                                    |
| ---- | ------------------------------------- | ----- | ----------------------------------------------------------- |
| 107  | 107_流式执行_langgraph 流式执行概述   | 08:00 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=107) |
| 108  | 108*流式执行*基础状态内容输出         | 09:34 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=108) |
| 109  | 109_流式执行_messages 消息            | 04:44 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=109) |
| 110  | 110_流式执行_checkpoints 信息         | 14:14 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=110) |
| 111  | 111*流式执行*其他的打印信息           | 06:11 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=111) |
| 112  | 112*流式执行*用户自定义输出           | 06:30 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=112) |
| 113  | 113_流式执行_asteam_events 输出内容   | 08:44 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=113) |
| 114  | 114*子图*父图直接在节点中调用子图     | 17:28 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=114) |
| 115  | 115*子图*直接调用的注意事项           | 04:18 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=115) |
| 116  | 116*子图*作为父图的节点               | 05:25 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=116) |
| 117  | 117*子图*父图检查点查看子图检查点信息 | 16:59 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=117) |
| 118  | 118*子图*持久化策略                   | 03:56 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=118) |
| 119  | 119*子图*中断场景持久化策略区别       | 04:57 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=119) |
| 120  | 120*子图*多轮会话场景持久化策略       | 03:55 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=120) |
| 121  | 121*子图*单节点多次调用同一个子图     | 06:46 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=121) |
| 122  | 122*子图*多节点调用时注意分散节点     | 07:25 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=122) |
| 123  | 123*子图*推荐使用 stateless 的场景    | 04:11 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=123) |
| 124  | 124*子图*持久化策略总结               | 03:13 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=124) |
| 125  | 125*子图*流式执行输出 chunk           | 04:51 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=125) |
| 126  | 126*子图*子图的 llm 流式输出          | 04:02 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=126) |
| 127  | 127*子图*子图动态路由                 | 06:24 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=127) |
| 128  | 128*图设计模型*提示词链和并行化       | 07:05 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=128) |
| 129  | 129*图设计模型*路由                   | 06:11 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=129) |
| 130  | 130*图设计模型*编排器_工作者模式      | 06:26 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=130) |
| 131  | 131*图设计模型*评估器_优化器          | 08:27 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=131) |
| 132  | 132_图设计模型_agent 模式和总结       | 03:53 | [▶ 观看](https://www.bilibili.com/video/BV1z3NY66EY1?p=132) |

------

## 快速开始（本地跑代码）



```
cd langgraph/代码/langgraph

# 建议使用 conda / venv 创建独立环境后安装依赖
pip install -r requirements_full.txt

# 用 Jupyter / VS Code / Cursor 打开对应章节的 .ipynb 即可跟练
```



环境配置细节可参考：[00-环境配置.md](https://github.com/xbsheng/atguigu-note/blob/main/langgraph/课件/00-环境配置.md)

------

## 使用建议



1. **看视频**：点上方 B 站链接在线观看，按分 P 跳转，不需要下载，也不需要百度网盘会员。
2. **看课件**：打开 `课件/` 下对应章节的 Markdown，配合视频笔记复习。
3. **练代码**：打开 `代码/langgraph/` 下对应 `chapter*` 目录中的 Notebook 动手实践。
4. **HITL 演示**：可参考 `代码/langgraph/hitl_demo/` 做人机协作相关实验。

------

## 版权说明



课程版权归 [尚硅谷](http://www.atguigu.com/) 所有。本仓库整理课件与代码目录，仅供学习交流使用。