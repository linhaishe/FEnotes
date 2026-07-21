# Refs

- https://www.w3schools.com/go/go_getting_started.php

 - Learning Go: An Idiomatic Approach to Real-world Go Programming, 2nd Edition / *[Jon Bodner](https://z-lib.by/author/Jon Bodner)*
 - https://www.runoob.com/go/go-error-handling.html

> ## 阶段一：基础语法与核心概念
>
> - **环境搭建**：安装 Go SDK、配置 `GOPATH` 与 `GOROOT`、掌握 `go module` 包管理机制，熟悉 VS Code 或 GoLand。
> - **基础语法**：
>   - 变量与常量定义（`var`、`:=`、`const`、`iota`）
>   - 基本数据类型（整型、浮点型、布尔型、字符串）
>   - 流程控制（`if-else`、`switch`、`for` 循环与 `range`）
> - **复合数据类型**：
>   - 数组与**切片（Slice）**（底层原理、扩容机制、截取）
>   - **Map**（映射的声明、初始化、遍历与键值删除）
>   - 结构体（Struct）与自定义类型
> - **函数与指针**：
>   - 多返回值、可变参数、匿名函数与**闭包**
>   - **指针**的基本用法（值传递 vs 引用传递）
>   - 延迟调用（`defer`）及其执行顺序与性能注意事项
>
> ## 阶段二： Go 特性与面向接口编程
>
> - **接口（Interface）**：
>   - 隐式接口实现机制
>   - 空接口 `interface{}` 与类型断言（Type Assertion / Type Switch）
>   - 面向接口编程设计原则
> - **错误处理机制**：
>   - `error` 接口的定义与扩展（`fmt.Errorf`、`errors.Is`、`errors.As`）
>   - `panic` 与 `recover` 的正确使用场景与注意事项
> - **面向对象思想**：
>   - 通过结构体嵌套实现“继承/组合”
>   - 方法定义（接收者类型：值接收者 vs 指针接收者）
>
> ## 阶段三：并发编程（ Go 的灵魂）
>
> - **Goroutine（协程）**：
>   - Goroutine 的创建与生命周期
>   - 与线程/进程的区别（轻量级、GMP 模型简介）
> - **Channel（管道）**：
>   - 有缓冲 vs 无缓冲 Channel
>   - 单向 Channel（只读/只写）
>   - 结合 `select` 实现多路复用与超时控制
> - **并发安全与同步（`sync` 包）**：
>   - 互斥锁（`sync.Mutex`）与读写锁（`sync.RWMutex`）
>   - 并发计数器（`sync.WaitGroup`）与单例模式（`sync.Once`）
>   - 并发安全的 Map（`sync.Map`）与对象池（`sync.Pool`）
>   - 原子操作（`sync/atomic`）
> - **上下文控制（`context` 包）**：
>   - 传递上下文信息（`WithCancel`、`WithTimeout`、`WithDeadline`、`WithValue`）
>   - 解决多 Goroutine 树状生命周期控制与超时取消
>
> ## 阶段四：工程实践与后端生态
>
> - **标准库与日常开发**：
>   - `net/http`（HTTP 服务端与客户端编写）
>   - `encoding/json`（JSON 序列化与反序列化）
>   - `os`、`io`、`bufio`（文件与 IO 流处理）
> - **测试与性能工具**：
>   - 单元测试（`testing` 包、基准测试 Benchmark）
>   - 代码覆盖率分析（Coverage）
>   - 性能剖析工具（`pprof` 分析 CPU、内存与协程阻塞）
> - **主流 Web 框架与 ORM**：
>   - **Web 框架**：Gin、Fiber 或 Echo
>   - **数据库/ORM**：GORM、Ent，以及原生的 `database/sql` + MySQL/PostgreSQL 驱动
>   - **缓存/消息队列**：go-redis、Sarama (Kafka) 或 RabbitMQ SDK
> - **微服务与 RPC**：
>   - Protobuf 编写与 gRPC 框架使用
>   - 微服务架构基础（服务注册与发现、配置中心、网关）
>
> ## 阶段五：底层原理与高级进阶
>
> - Go 运行时（Runtime）：
>   - **GMP 模型**原理（全局队列、Work Stealing、抢占式调度）
>   - 垃圾回收（GC）演进（三色标记法、混合写屏障）
>   - 内存分配器（mspan、mcache、mcentral、mheap）
> - **性能优化**：
>   - 减少内存逃逸（Escape Analysis）
>   - 零拷贝与高效 IO 技术
>   - 高并发场景下的连接池与对象池复用
>
> ### 推荐学习路线建议
>
> 1. **上手期**：先通读官方教程《A Tour of Go》，结合《Go 语言圣经》（*The Go Programming Language*）打牢语法基础。
> 2. **进阶期**：动手写一个简易的 HTTP API 服务，接入 MySQL 和 Redis，熟悉 Gin + GORM 的组合。
> 3. **拔高期**：尝试实现一个小型中间件（如简易的分布式缓存、RPC 框架或 KV 存储系统），深入剖析源码。

----

> ## 1. 命令行文件/文本并发搜索工具 (Mini-Grep)
>
> > **目标**：熟悉 Go 的文件操作、命令行参数解析，以及最核心的 **并发（Goroutine + Channel）**。
>
> - **功能需求**：
>   - 接收命令行参数：目标文件夹路径、要搜索的关键词。
>   - 递归遍历文件夹下的所有文件。
>   - 为每个文件开启一个 Goroutine 搜索关键词。
>   - 通过 Channel 汇总所有匹配到关键词的文件名和行号并打印。
> - **用到的 Go 特性**：
>   - `os`、`filepath` 模块进行目录遍历与文件读取。
>   - `flag` 模块解析命令行参数。
>   - `go func()` 启动协程、`chan` 传输结果、`sync.WaitGroup` 等待所有文件检索完成。
>
> ## 2. 静态文件 HTTP 服务器 / 简易图床 API
>
> > **目标**：体验 Go 原生强大的网络库，体会**几行代码搭一个高性能 Web 服务**的感觉。
>
> - **功能需求**：
>   - **接口 1**：文件上传接口（接收图片并保存到本地文件夹）。
>   - **接口 2**：图片/静态资源预览接口（直接在浏览器访问图片路径即可查看）。
>   - **接口 3**：文件列表查看（返回当前已上传文件的 JSON 列表）。
> - **用到的 Go 特性**：
>   - `net/http` 标准库（**完全不需要依赖外部 Web 框架**）。
>   - `struct` 结构体定义与 `encoding/json` 序列化。
>   - Go 原生并发处理 HTTP 请求（每个 Request 自动跑在独立 Goroutine 中）。
>
> ## 3. 网站/API 可用性健康监测器 (Site Checker)
>
> > **目标**：理解并发控制、定时器以及 Go 极简的错误处理机制。
>
> - **功能需求**：
>   - 从配置文件或数组中读取 10+ 个网址（如 baidu.com, github.com 等）。
>   - 定时（如每 10 秒）向这些网址发送 HTTP GET 请求。
>   - 如果请求超时或状态码非 200，记录错误日志并输出提示。
>   - 用 `time.Ticker` 实现周期调度，用 `context.WithTimeout` 实现超时控制。
> - **用到的 Go 特性**：
>   - `net/http` 发送 Client 请求。
>   - `time` 包（定时器 `Ticker`、休眠 `Sleep`）。
>   - `context` 上下文机制（控制 HTTP 请求超时）。
>   - `defer` 优雅关闭 HTTP 响应体（`resp.Body.Close()`）。
>
> ## 4. 简易 Redis/KV 内存数据库 (Mini KV-Store)
>
> > **目标**：理解指针、Map 结构以及**并发安全锁**的使用。
>
> - **功能需求**：
>   - 基于内存实现一个简单的 Key-Value 存储系统。
>   - 支持基本命令：`SET key value`、`GET key`、`DELETE key`。
>   - 支持给 Key 设置过期时间（TTL），过期后自动清理。
>   - （可选扩展）通过 TCP 暴露服务（使用 `net` 包），可以用 `telnet` 或 `nc` 连接测试。
> - **用到的 Go 特性**：
>   - `map[string]interface{}` 存取内存数据。
>   - `sync.RWMutex`（读写锁）保证并发读写安全。
>   - `time.AfterFunc` 或后台协程清理过期 Key。
>
> ### 推荐的上手顺序
>
> 1. 先做 **项目 2（静态文件服务器）**：只要 30~50 行代码就能跑起来，非常有成就感。
> 2. 再做 **项目 1（Mini-Grep）** 或 **项目 3（健康监测器）**：顺理成章地学会使用 Goroutine 和 Channel 处理并发。

> ## 推荐项目一：多源 API 数据抓取与本地报表生成器（以天气/财经/热搜为例）
>
> > **场景**：每天自动去网上调 API 抓取数据，清洗汇总后保存为本地 CSV 文件，并按日期自动创建文件夹归档。
>
> ### 核心功能步骤：
>
> 1. **网络请求 (`requests`)**：
>    - 调用免费的公开 API（比如某个天气 API、聚合热搜 API、或者加密货币价格 API）。
>    - 甚至可以用 `requests` 访问几个网页提取 JSON 响应。
> 2. **数据解析 (`json` / `csv`)**：
>    - 用 `response.json()` 提取出你关心的关键字段（比如：城市、温度、天气状况、更新时间）。
>    - 使用 Python 自带的 `csv` 模块，把这些结构化数据追加写入到本地的 `weather_report.csv` 中。
> 3. **文件与系统自动化 (`os` / `sys`)**：
>    - 使用 `sys.argv` 允许用户从命令行传入参数（例如指定城市或导出文件名：`python main.py --city Beijing`）。
>    - 用 `os.path.exists()` 检查今天日期的文件夹是否存在（如 `./reports/2026-07-20/`），如果不存在，用 `os.makedirs()` 自动创建文件夹并将 CSV 存入其中。
>
> ## 推荐项目二：网页静态资源批量下载与分类整理器
>
> > **场景**：给一个包含多张图片/文件链接的 API 或网页，自动把文件下载到本地，并根据文件类型或大小自动建文件夹归档。
>
> ### 核心功能步骤：
>
> 1. **网络请求 (`requests`)**：
>    - 用 `requests.get(url, stream=True)` 请求图片/文件链接，获取二进制流（`response.content`）。
> 2. **文件与系统自动化 (`os` / `sys`)**：
>    - 接收命令行参数 `sys.argv[1]` 作为目标的保存路径。
>    - 用 `os.walk()` 或 `os.listdir()` 扫描指定目录。
>    - 根据下载文件的扩展名（如 `.jpg`, `.pdf`, `.json`），自动用 `os.mkdir()` 创建对应的子文件夹（如 `/images/`, `/docs/`），并用 `os.rename()` 或 `shutil.move()` 把文件归类放进去。
> 3. **数据解析 (`json` / `csv`)**：
>    - 下载完成后，把所有下载成功的文件名、文件大小、下载时间、原始 URL 整理成一个字典列表。
>    - 用 `json.dump()` 将这次下载的历史记录保存为 `download_history.json`。

# Syntax

```go
package main
import ("fmt")

func main() {
  fmt.Println("Hello World!")
}

// go run test.go
```

# Comments

**Multi-line Comments**

```go
package main
import ("fmt")

func main() {
  /* The code below will print Hello World
  to the screen, and it is amazing */
  fmt.Println("Hello World!")
}
```

**single-line comment**

```go
package main
import ("fmt")

func main() {
  fmt.Println("Hello World!") // This is a comment
}
```

# Variables

- `int`- stores integers (whole numbers), such as 123 or -123
- `float32`- stores floating point numbers, with decimals, such as 19.99 or -19.99
- `string` - stores text, such as "Hello World". String values are surrounded by double quotes
- `bool`- stores values with two states: true or false

## two ways to declare

- `var variablename type = value`
- `variablename := value`

| var                                                          | :=                                                           |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Can be used **inside** and **outside** of functions          | Can only be used **inside** functions                        |
| Variable declaration and value assignment **can be done separately** | Variable declaration and value assignment **cannot be done separately** (must be done in the same line) |

```Go
package main

import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}

// 0 false false false
```

```Go
var i, j int = 1, 2

func main() {
	var c, python, java = true, false, "no!"
	fmt.Println(i, j, c, python, java)
}

// 1 2 true false no!
```

```go
package main
import ("fmt")

func main() {
  var student1 string = "John" //type is string
  var student2 = "Jane" //type is inferred
  x := 2 //type is inferred

  fmt.Println(student1)
  fmt.Println(student2)
  fmt.Println(x)
}
```

```go
package main
import ("fmt")

func main() {
  var a string
  var b int
  var c bool

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
}

// a is ""
// b is 0
// c is false
```

```go
package main
import ("fmt")

func main() {
  var student1 string
  student1 = "John"
  fmt.Println(student1)
}
```

```go
// wrong
package main
import ("fmt")

a := 1

func main() {
  fmt.Println(a)
}
```

## Multiple Variable Declaration

```go
package main
import ("fmt")

func main() {
  var a, b, c, d int = 1, 3, 5, 7 
  // type keyword, it is only possible to declare one type of variable per line.

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
  fmt.Println(d)
}
```

```go
package main
import ("fmt")

func main() {
  var a, b = 6, "Hello" // without type keyword
  c, d := 7, "World!"

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
  fmt.Println(d)
}
```

```go
package main
import ("fmt")

func main() {
   var (
     a int
     b int = 1
     c string = "hello"
   )

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
}
```

## Variable Naming Rules

- A variable name must start with a letter or an underscore character (_)
- A variable name cannot start with a digit
- A variable name can only contain alpha-numeric characters and underscores (`a-z, A-Z`, `0-9`, and `_` )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- There is no limit on the length of the variable name
- A variable name cannot contain spaces
- The variable name cannot be any Go keywords

### Camel Case

Each word, except the first, starts with a capital letter:

`myVariableName = "John"`

------

### Pascal Case

Each word starts with a capital letter:

`MyVariableName = "John"`

------

### Snake Case

Each word is separated by an underscore character:

`my_variable_name = "John"`

# Constants

`const CONSTNAME type = value`

- Constant names follow the same naming rules as [variables](https://www.w3schools.com/go/go_variable_naming_rules.php)
- Constant names are usually written in uppercase letters (for easy identification and differentiation from variables)
- Constants can be declared both inside and outside of a function

==**Constants: Unchangeable and Read-only**==

```go
package main
import ("fmt")

const PI = 3.14

func main() {
  fmt.Println(PI)
}
```

### two types of constants

- Typed constants
- Untyped constants

```go
package main
import ("fmt")

const A int = 1

func main() {
  fmt.Println(A)
}
```

```go
package main
import ("fmt")

const A = 1

func main() {
  fmt.Println(A)
}
```

```go
package main
import ("fmt")

const (
  A int = 1
  B = 3.14
  C = "Hi!"
)

func main() {
  fmt.Println(A)
  fmt.Println(B)
  fmt.Println(C)
}
```

```go
package main
import ("fmt")

// error
func main() {
  const A = 1
  A = 2
  fmt.Println(A)
}
```

# Output Functions

| **函数**        | **空格处理规则**                                             | **自动换行 (\n)**               | **支持格式化占位符 (如 %d, %s)** | **典型应用场景**                                           |
| --------------- | ------------------------------------------------------------ | ------------------------------- | -------------------------------- | ---------------------------------------------------------- |
| **`Print()`**   | 仅在**非字符串**参数之间自动添加空格。如果都是字符串，会紧贴在一起。 | ❌ 否（需手动加 `\n`）           | ❌ 否                             | 连续拼接输出、控制台进度条等不需要换行的场景。             |
| **`Println()`** | **所有**参数之间都会自动添加一个空格。                       | 是（结尾自动换行）              | ❌ 否                             | 最常用的普通打印，省去了手动加空格和换行符的麻烦。         |
| **`Printf()`**  | 完全取决于你在格式化字符串中如何编写，**不会**自动加空格。   | ❌ 否（需手动在模板末尾加 `\n`） | **是**（核心功能）               | 需要精确控制输出格式，如保留两位小数（`%.2f`）或排版对齐。 |

- `Print()`

  The `Print()` function prints its arguments with their default format.

- `Println()`

  The `Println()` function is similar to `Print()` with the difference that a whitespace is added between the arguments, and a newline is added at the end:

- `Printf()`

  The `Printf()` function first formats its argument based on the given formatting verb and then prints them.

| Verb | Description                            |
| :--- | :------------------------------------- |
| %v   | Prints the value in the default format |
| %#v  | Prints the value in Go-syntax format   |
| %T   | Prints the type of the value           |
| %%   | Prints the % sign                      |

```go
package main
import ("fmt")

func main() {
  var i,j string = "Hello","World"

  fmt.Print(i)
  fmt.Print(j)
  // HelloWorld
  
  fmt.Print(i, " ", j)
  // Hello World
}

```

```go
package main
import ("fmt")

func main() {
  var i,j string = "Hello","World"

  fmt.Println(i,j) // Hello World

}
```

```go
package main
import ("fmt")

func main() {
  var i string = "Hello"
  var j int = 15

  fmt.Printf("i has value: %v and type: %T\n", i, i)
  fmt.Printf("j has value: %v and type: %T", j, j)
}

// i has value: Hello and type: string
// j has value: 15 and type: int
```

```go
package main
import ("fmt")

func main() {
  var i = 15.5
  var txt = "Hello World!"

  fmt.Printf("%v\n", i)
  fmt.Printf("%#v\n", i)
  fmt.Printf("%v%%\n", i)
  fmt.Printf("%T\n", i)

  fmt.Printf("%v\n", txt)
  fmt.Printf("%#v\n", txt)
  fmt.Printf("%T\n", txt)
}

// 15.5
// 15.5
// 15.5%
// float64
// Hello World!
// "Hello World!"
// string
```



# Data Types

- **bool**: represents a boolean value and is either true or false
- **Numeric**: represents `integer` types, `floating point` values, and complex types
- **string**: represents a string value

```go
package main
import ("fmt")

func main() {
  var a bool = true     // Boolean
  var b int = 5         // Integer
  var c float32 = 3.14  // Floating point number
  var d string = "Hi!"  // String

  fmt.Println("Boolean: ", a)
  fmt.Println("Integer: ", b)
  fmt.Println("Float:   ", c)
  fmt.Println("String:  ", d)
}
```

## integer

- Signed Integers

  Signed integers, declared with one of the `int` keywords, can store both positive and negative values:

- Unsigned Integers

  Unsigned integers, declared with one of the `uint` keywords, can only store non-negative values:

**8 位**：小箱子，只能装小数字。

**16 位**：中箱子。

**32 位**：大箱子。

**64 位**：超大箱子。


| Type    | Size                                                         | Range                                                        |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| `int`   | Depends on platform: 32 bits in 32 bit systems and 64 bit in 64 bit systems | -2147483648 to 2147483647 in 32 bit systems and -9223372036854775808 to 9223372036854775807 in 64 bit systems |
| `int8`  | 8 bits/1 byte                                                | -128 to 127                                                  |
| `int16` | 16 bits/2 byte                                               | -32768 to 32767                                              |
| `int32` | 32 bits/4 byte                                               | -2147483648 to 2147483647                                    |
| `int64` | 64 bits/8 byte                                               | -9223372036854775808 to 9223372036854775807                  |
| `uint`  | Unsigned Integer（无符号整数）不能表示负数                   | 32 或 64                                                     |
| `uint8` | 无                                                           | 8                                                            |
| uint16  | 无                                                           | 16                                                           |

```go
package main
import ("fmt")

func main() {
  var x int = 500
  var y int = -4500
  fmt.Printf("Type: %T, value: %v", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
package main
import ("fmt")

func main() {
  var x uint = 500
  var y uint = 4500
  fmt.Printf("Type: %T, value: %v", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
// ./prog.go:5:7: constant 1000 overflows int8
package main
import ("fmt")

func main() {
  var x int8 = 1000
  fmt.Printf("Type: %T, value: %v", x, x)
}
```

## Float

| Type      | Size    | Range                   |
| :-------- | :------ | :---------------------- |
| `float32` | 32 bits | -3.4e+38 to 3.4e+38.    |
| `float64` | 64 bits | -1.7e+308 to +1.7e+308. |

```go
package main
import ("fmt")

func main() {
  var x float32 = 123.78
  var y float32 = 3.4e+38
  fmt.Printf("Type: %T, value: %v\n", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
package main
import ("fmt")

func main() {
  var x float64 = 1.7e+308
  fmt.Printf("Type: %T, value: %v", x, x)
}
```

# Arrays

1. With the `var` keyword:

```go
var array_name = [length]datatype{values} // here length is defined
var array_name = [...]datatype{values} // here length is inferred
```

2. With the `:=` sign:

```go
array_name := [length]datatype{values} // here length is defined
array_name := [...]datatype{values} // here length is inferred
```

```go
package main
import ("fmt")

func main() {
  var arr1 = [3]int{1,2,3}
  arr2 := [5]int{4,5,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
}

// [1 2 3]
// [4 5 6 7 8]

func main() { // with inferred lengths:
  var arr1 = [...]int{1,2,3}
  arr2 := [...]int{4,5,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
}

// [1 2 3]
// [4 5 6 7 8]


func main() {
  var cars = [4]string{"Volvo", "BMW", "Ford", "Mazda"}
  fmt.Print(cars)
}

// [Volvo BMW Ford Mazda]

// Access Elements of an Array
func main() {
  prices := [3]int{10,20,30}

  fmt.Println(prices[0])
  fmt.Println(prices[2])
}

// 10
// 30

// Change Elements of an Array
func main() {
  prices := [3]int{10,20,30}

  prices[2] = 50
  fmt.Println(prices)
}

// Array Initialization
func main() {
  arr1 := [5]int{} //not initialized
  arr2 := [5]int{1,2} //partially initialized
  arr3 := [5]int{1,2,3,4,5} //fully initialized

  fmt.Println(arr1)
  fmt.Println(arr2)
  fmt.Println(arr3)
}

// Initialize Only Specific Elements
func main() {
  arr1 := [5]int{1:10,2:40}

  fmt.Println(arr1)
}
// [0 10 40 0 0]

// Find the Length of an Array
func main() {
  arr1 := [4]string{"Volvo", "BMW", "Ford", "Mazda"}
  arr2 := [...]int{1,2,3,4,5,6}

  fmt.Println(len(arr1))
  fmt.Println(len(arr2))
}
```

# Slices

Like arrays, slices are also used to store multiple values of the same type in a single variable.

However, unlike arrays, the length of a slice can grow and shrink as you see fit.

## Create a Slice

### With `[]datatype{values}`

`slice_name := []datatype{values}`

```go
myslice := []int{}

myslice := []int{1,2,3}
```

- `len()` function - returns the length of the slice (the number of elements in the slice)
- `cap()` function - returns the capacity of the slice (the number of elements the slice can grow or shrink to)

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{}
  fmt.Println(len(myslice1))
  fmt.Println(cap(myslice1))
  fmt.Println(myslice1)

  myslice2 := []string{"Go", "Slices", "Are", "Powerful"}
  fmt.Println(len(myslice2))
  fmt.Println(cap(myslice2))
  fmt.Println(myslice2)
}

// 0
// 0
// []
// 4
// 4
// [Go Slices Are Powerful]
```

### Create a Slice From an Array

```go
var myarray = [length]datatype{values} // An array
myslice := myarray[start:end] // A slice made from the array
```

```go
package main
import ("fmt")

func main() {
  arr1 := [6]int{10, 11, 12, 13, 14,15}
  myslice := arr1[2:4]

  fmt.Printf("myslice = %v\n", myslice)
  fmt.Printf("length = %d\n", len(myslice))
  fmt.Printf("capacity = %d\n", cap(myslice))
}

// myslice = [12 13]
// length = 2
// capacity = 4
```

### Create a Slice With The make() Function

The `make()` function can also be used to create a slice.

`slice_name := make([]type, length, capacity)`

> **Note:** If the *capacity* parameter is not defined, it will be equal to *length*.

```go
package main
import ("fmt")

func main() {
  myslice1 := make([]int, 5, 10)
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  // with omitted capacity
  myslice2 := make([]int, 5)
  fmt.Printf("myslice2 = %v\n", myslice2)
  fmt.Printf("length = %d\n", len(myslice2))
  fmt.Printf("capacity = %d\n", cap(myslice2))
}

// myslice1 = [0 0 0 0 0]
// length = 5
// capacity = 10
// myslice2 = [0 0 0 0 0]
// length = 5
// capacity = 5
```

## Access, Change, Append and Copy Slices

### Access

```go
package main
import ("fmt")

func main() {
  prices := []int{10,20,30}

  fmt.Println(prices[0])
  fmt.Println(prices[2])
}
```

### Change

```go
package main
import ("fmt")

func main() {
  prices := []int{10,20,30}
  prices[2] = 50
  fmt.Println(prices[0])
  fmt.Println(prices[2])
}
```

### Append

#### Append element

`slice_name = append(slice_name, element1, element2, ...)`

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{1, 2, 3, 4, 5, 6}
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = append(myslice1, 20, 21)
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))
}

// myslice1 = [1 2 3 4 5 6]
// length = 6
// capacity = 6
// myslice1 = [1 2 3 4 5 6 20 21]
// length = 8
// capacity = 12
```

#### Append sclice

`slice3 = append(slice1, slice2...)`

> **Note:** The **'...'** after *slice2* is **necessary** when appending the elements of one slice to another.

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{1,2,3}
  myslice2 := []int{4,5,6}
  myslice3 := append(myslice1, myslice2...)

  fmt.Printf("myslice3=%v\n", myslice3)
  fmt.Printf("length=%d\n", len(myslice3))
  fmt.Printf("capacity=%d\n", cap(myslice3))
}

// myslice3=[1 2 3 4 5 6]
// length=6
// capacity=6
```

### Change The Length of a Slice

```go
package main
import ("fmt")

func main() {
  arr1 := [6]int{9, 10, 11, 12, 13, 14} // An array
  myslice1 := arr1[1:5] // Slice array 原数组不会被修改
  fmt.Printf("myslice1 = %v\n", myslice1) 
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = arr1[1:3] // Change length by re-slicing the array
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = append(myslice1, 20, 21, 22, 23) // Change length by appending items
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))
}

// myslice1 = [10 11 12 13]
// length = 4
// capacity = 5
// myslice1 = [10 11]
// length = 2
// capacity = 5
// myslice1 = [10 11 20 21 22 23]
// length = 6
// capacity = 10
```

### Memory Efficiency

 When using slices, Go loads all the underlying elements into the memory.

If the array is large and you need only a few elements, it is better to copy those elements using the `copy()` function.

The `copy()` function creates a new underlying array with only the required elements for the slice. This will reduce the memory used for the program. 

`copy(dest, src)`

```go
package main
import ("fmt")

func main() {
  numbers := []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
  // Original slice
  fmt.Printf("numbers = %v\n", numbers)
  fmt.Printf("length = %d\n", len(numbers))
  fmt.Printf("capacity = %d\n", cap(numbers))

  // Create copy with only needed numbers
  neededNumbers := numbers[:len(numbers)-10]
  numbersCopy := make([]int, len(neededNumbers))
  copy(numbersCopy, neededNumbers)

  fmt.Printf("numbersCopy = %v\n", numbersCopy)
  fmt.Printf("length = %d\n", len(numbersCopy))
  fmt.Printf("capacity = %d\n", cap(numbersCopy))
}

// Original slice
numbers = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
length = 15
capacity = 15
// New slice
numbersCopy = [1 2 3 4 5]
length = 5
capacity = 5
```

# Operators

## Arithmetic Operators

| Operator | Name           | Description                            | Example |
| :------- | :------------- | :------------------------------------- | :------ |
| +        | Addition       | Adds together two values               | x + y   |
| -        | Subtraction    | Subtracts one value from another       | x - y   |
| *        | Multiplication | Multiplies two values                  | x * y   |
| /        | Division       | Divides one value by another           | x / y   |
| %        | Modulus        | Returns the division remainder         | x % y   |
| ++       | Increment      | Increases the value of a variable by 1 | x++     |
| --       | Decrement      | Decreases the value of a variable by 1 | x--     |

```go
package main

import "fmt"

func main() {
    var a = '1' + 25
    fmt.Println(a)        // 输出数字: 74
    fmt.Printf("%c\n", a) // 输出对应的字符: J
}
// 字符 '1' 在 ASCII 码表中对应的十进制数字是 49。
```

## Assignment Operators

| Operator | Example | Same As    |
| :------- | :------ | :--------- |
| =        | x = 5   | x = 5      |
| +=       | x += 3  | x = x + 3  |
| -=       | x -= 3  | x = x - 3  |
| *=       | x *= 3  | x = x * 3  |
| /=       | x /= 3  | x = x / 3  |
| %=       | x %= 3  | x = x % 3  |
| &=       | x &= 3  | x = x & 3  |
| \|=      | x \|= 3 | x = x \| 3 |
| ^=       | x ^= 3  | x = x ^ 3  |
| >>=      | x >>= 3 | x = x >> 3 |
| <<=      | x <<= 3 | x = x << 3 |

## Comparison Operators

| Operator | Name                     | Example |
| :------- | :----------------------- | :------ |
| ==       | Equal to                 | x == y  |
| !=       | Not equal                | x != y  |
| >        | Greater than             | x > y   |
| <        | Less than                | x < y   |
| >=       | Greater than or equal to | x >= y  |
| <=       | Less than or equal to    | x <= y  |

## Logical Operators

| Operator | Name        | Description                                             | Example            |
| :------- | :---------- | :------------------------------------------------------ | :----------------- |
| &&       | Logical and | Returns true if both statements are true                | x < 5 && x < 10    |
| \|\|     | Logical or  | Returns true if one of the statements is true           | x < 5 \|\| x < 4   |
| !        | Logical not | Reverse the result, returns false if the result is true | !(x < 5 && x < 10) |

## Bitwise Operators

| Operator | Name                 | Description                                                  | Example |
| :------- | :------------------- | :----------------------------------------------------------- | :------ |
| &        | AND                  | Sets each bit to 1 if both bits are 1                        | x & y   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                   | x \| y  |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1              | x ^ b   |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right                | x << 2  |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2  |

# Conditions

## if Statement

```go
if condition {
  // code to be executed if condition is true
}
```

```go
if condition {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```

```go
if condition1 {
   // code to be executed if condition1 is true
} else if condition2 {
   // code to be executed if condition1 is false and condition2 is true
} else {
   // code to be executed if condition1 and condition2 are both false
}
```

```go
if condition1 {
   // code to be executed if condition1 is true
  if condition2 {
     // code to be executed if both condition1 and condition2 are true
  }
}
```

```go
package main
import ("fmt")

func main() {
  if 20 > 18 {
    fmt.Println("20 is greater than 18")
  }
}

func main() {
  x:= 20
  y:= 18
  if x > y {
    fmt.Println("x is greater than y")
  }
}
```

```go
func main() {
  time := 20
  if (time < 18) {
    fmt.Println("Good day.")
  } else {
    fmt.Println("Good evening.")
  }
}
```

```go
func main() {
  time := 22
  if time < 10 {
    fmt.Println("Good morning.")
  } else if time < 20 {
    fmt.Println("Good day.")
  } else {
    fmt.Println("Good evening.")
  }
}
```

```go
func main() {
  num := 20
  if num >= 10 {
    fmt.Println("Num is more than 10.")
    if num > 15 {
      fmt.Println("Num is also more than 15.")
     }
  } else {
    fmt.Println("Num is less than 10.")
  }
}
```

# switch Statement

- The expression is evaluated once
- The value of the `switch` expression is compared with the values of each `case`
- If there is a match, the associated block of code is executed
- The `default` keyword is optional. It specifies some code to run if there is no `case` match

## Single-case

All the `case` values should have the same type

```go
switch expression {
case x:
   // code block
case y:
   // code block
case z:
...
default:
   // code block
}
```

```go
package main
import ("fmt")

func main() {
  day := 4

  switch day {
  case 1:
    fmt.Println("Monday")
  case 2:
    fmt.Println("Tuesday")
  case 3:
    fmt.Println("Wednesday")
  case 4:
    fmt.Println("Thursday")
  case 5:
    fmt.Println("Friday")
  case 6:
    fmt.Println("Saturday")
  case 7:
    fmt.Println("Sunday")
  }
}
```

```go
package main
import ("fmt")

func main() {
  a := 3

  switch a {
  case 1:
    fmt.Println("a is one")
  case "b":
    fmt.Println("a is b") // ./prog.go:11:2: cannot use "b" (type untyped string) as type int
  }
}
```

## Multi-case

```go
switch expression {
case x,y:
   // code block if expression is evaluated to x or y
case v,w:
   // code block if expression is evaluated to v or w
case z:
...
default:
   // code block if expression is not found in any cases
}
```

```go
func main() {
   day := 5

   switch day {
   case 1,3,5:
    fmt.Println("Odd weekday")
   case 2,4:
     fmt.Println("Even weekday")
   case 6,7:
    fmt.Println("Weekend")
  default:
    fmt.Println("Invalid day of day number")
  }
}
```

# For Loops

The `for` loop loops through a block of code a specified number of times.

The `for` loop is the only loop available in Go.

Each execution of a loop is called an **iteration**.

```go
for statement1; statement2; statement3 {
   // code to be executed for each iteration
}
```

**statement1** Initializes the loop counter value.

**statement2** Evaluated for each loop iteration. If it evaluates to TRUE, the loop continues. If it evaluates to FALSE, the loop ends.

**statement3** Increases the loop counter value.

```go
package main
import ("fmt")

func main() {
  for i:=0; i < 5; i++ {
    fmt.Println(i)
  }
}
```

## continue / break Statement

```go
func main() {
  for i:=0; i < 5; i++ {
    if i == 3 {
      continue
    }
   fmt.Println(i)
  }
}

// 0
// 1
// 2
// 4

func main() {
  for i:=0; i < 5; i++ {
    if i == 3 {
      break
    }
   fmt.Println(i)
  }
}

// 0
// 1
// 2

func main() {
  adj := [2]string{"big", "tasty"}
  fruits := [3]string{"apple", "orange", "banana"}
  for i:=0; i < len(adj); i++ {
    for j:=0; j < len(fruits); j++ {
      fmt.Println(adj[i],fruits[j])
    }
  }
}

// big apple
// big orange
// big banana
// tasty apple
// tasty orange
// tasty banana
```

## Range Keyword

The `range` keyword is used to more easily iterate through the elements of an array, slice or map. It returns both the index and the value.

```go
for index, value := range array|slice|map {
   // code to be executed for each iteration
}
```

```go
package main
import ("fmt")

func main() {
  fruits := [3]string{"apple", "orange", "banana"}
  for idx, val := range fruits {
     fmt.Printf("%v\t%v\n", idx, val)
  }
}

// 0      apple
// 1      orange
// 2      banana
```

```go
// Tip: To only show the value or the index, you can omit the other output using an underscore (_).

func main() {
  fruits := [3]string{"apple", "orange", "banana"}
  for _, val := range fruits {
     fmt.Printf("%v\n", val)
  }
}

func main() {
  fruits := [3]string{"apple", "orange", "banana"}

  for idx, _ := range fruits {
     fmt.Printf("%v\n", idx)
  }
}
```

# Functions

```go
func FunctionName() {
  // code to be executed
}
```

```go
func FunctionName(param1 type, param2 type, param3 type) {
  // code to be executed
}
```

```go
func FunctionName(param1 type, param2 type) type {
  // code to be executed
  return output
}
```

```Go
// two or more consecutive named function parameters share a type, you can omit the type from all but the last
func add(x, y int) int {
	return x + y
}
```

## Naming Rules for Go Functions

- A function name must start with a letter
- A function name can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_` )
- Function names are case-sensitive
- A function name cannot contain spaces
- If the function name consists of multiple words, techniques introduced for [multi-word variable naming](https://www.w3schools.com/go/go_variable_naming_rules.php) can be used

**Tip:** Give the function a name that reflects what the function does!

```go
func myMessage() {
  fmt.Println("I just got executed!")
}

func main() {
  myMessage() // call the function
}
```

```go
// Parameters and Arguments
package main
import ("fmt")

func familyName(fname string) {
  fmt.Println("Hello", fname, "Refsnes")
}

func main() {
  familyName("Liam")
  familyName("Jenny")
  familyName("Anja")
}
```

```go
// Parameters and Arguments
func familyName(fname string, age int) {
  fmt.Println("Hello", age, "year old", fname, "Refsnes")
}

func main() {
  familyName("Liam", 3)
  familyName("Jenny", 14)
  familyName("Anja", 30)
}
```

> **Note:** When you are working with multiple parameters, the function call must have the same number of arguments as there are parameters, and the arguments must be passed in the same order.

```go
// Return Value
func myFunction(x int, y int) int {
  return x + y
}

func main() {
  fmt.Println(myFunction(1, 2))
}
```

```go
// Named Return Values
func myFunction(x int, y int) (result int) {
  result = x + y
  return // or return result
}

func main() {
  fmt.Println(myFunction(1, 2))
}
```

```go
// Multiple Return Values
func myFunction(x int, y string) (result int, txt1 string) {
  result = x + x
  txt1 = y + " World!"
  return
}

func main() {
  fmt.Println(myFunction(5, "Hello"))
}
// 10 Hello World!
```

## Recursion Functions

```go
package main
import ("fmt")

func testcount(x int) int {
  if x == 11 {
    return 0 // 立即结束当前函数，并把结果扔回去
  }
  fmt.Println(x)
  return testcount(x + 1)
}

func main(){
  testcount(1)
}
```

# Struct

A struct (short for structure) is used to create a collection of members of different data types, into a single variable.

While arrays are used to store multiple values of the same data type into a single variable, structs are used to store multiple values of different data types into a single variable.

A struct can be useful for grouping data together to create records.

## Declare a Struct

use the `type` and `struct` keywords:

```go
type struct_name struct {
  member1 datatype;
  member2 datatype;
  member3 datatype;
  ...
}
```

```go
type Person struct {
  name string
  age int
  job string
  salary int
}
```

```go
// Access Struct Members
package main
import ("fmt")

type Person struct {
  name string
  age int
  job string
  salary int
}

func main() {
  var pers1 Person
  var pers2 Person

  // Pers1 specification
  pers1.name = "Hege"
  pers1.age = 45
  pers1.job = "Teacher"
  pers1.salary = 6000

  // Pers2 specification
  pers2.name = "Cecilie"
  pers2.age = 24
  pers2.job = "Marketing"
  pers2.salary = 4500

  // Access and print Pers1 info
  fmt.Println("Name: ", pers1.name)
  fmt.Println("Age: ", pers1.age)
  fmt.Println("Job: ", pers1.job)
  fmt.Println("Salary: ", pers1.salary)

  // Access and print Pers2 info
  fmt.Println("Name: ", pers2.name)
  fmt.Println("Age: ", pers2.age)
  fmt.Println("Job: ", pers2.job)
  fmt.Println("Salary: ", pers2.salary)
}

// Name: Hege
// Age: 45
// Job: Teacher
// Salary: 6000
// Name: Cecilie
// Age: 24
// Job: Marketing
// Salary: 4500
```

```go
// Pass Struct as Function Arguments
package main
import ("fmt")

type Person struct {
  name string
  age int
  job string
  salary int
}

func main() {
  var pers1 Person
  var pers2 Person

  // Pers1 specification
  pers1.name = "Hege"
  pers1.age = 45
  pers1.job = "Teacher"
  pers1.salary = 6000

  // Pers2 specification
  pers2.name = "Cecilie"
  pers2.age = 24
  pers2.job = "Marketing"
  pers2.salary = 4500

  // Print Pers1 info by calling a function
  printPerson(pers1)

  // Print Pers2 info by calling a function
  printPerson(pers2)
}

func printPerson(pers Person) { // type assertion
  fmt.Println("Name: ", pers.name)
  fmt.Println("Age: ", pers.age)
  fmt.Println("Job: ", pers.job)
  fmt.Println("Salary: ", pers.salary)
}

// Name: Hege
// Age: 45
// Job: Teacher
// Salary: 6000
// Name: Cecilie
// Age: 24
// Job: Marketing
// Salary: 4500
```

# Maps

Maps are used to store data values in key:value pairs.

Each element in a map is a key:value pair.

A map is an unordered and changeable collection that does not allow duplicates.

The length of a map is the number of its elements. You can find it using the `len()` function.

The default value of a map is nil.

Maps hold references to an underlying hash table.

Go has multiple ways for creating maps.

## Create Maps

### Allowed Key Types

The map key can be of any data type for which the equality operator (`==`) is defined. These include:

- Booleans
- Numbers
- Strings
- Arrays
- Pointers
- Structs
- Interfaces (as long as the dynamic type supports equality)

Invalid key types are:

- Slices
- Maps
- Functions

These types are invalid because the equality operator (`==`) is not defined for them.

------

### Allowed Value Types

The map values can be **any** type.

### Create Maps Using `var` and `:=`

```go
var a = map[KeyType]ValueType{key1:value1, key2:value2,...}
b := map[KeyType]ValueType{key1:value1, key2:value2,...}
```

```go
package main
import ("fmt")

func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
  b := map[string]int{"Oslo": 1, "Bergen": 2, "Trondheim": 3, "Stavanger": 4}

  fmt.Printf("a\t%v\n", a)
  fmt.Printf("b\t%v\n", b)
}

// a   map[brand:Ford model:Mustang year:1964]
// b   map[Bergen:2 Oslo:1 Stavanger:4 Trondheim:3]
```

### Create Maps Using the `make()` Function:

```go
var a = make(map[KeyType]ValueType)
b := make(map[KeyType]ValueType)
```

```go
func main() {
  var a = make(map[string]string) // The map is empty now
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"
                                 // a is no longer empty
  b := make(map[string]int)
  b["Oslo"] = 1
  b["Bergen"] = 2
  b["Trondheim"] = 3
  b["Stavanger"] = 4

  fmt.Printf("a\t%v\n", a)
  fmt.Printf("b\t%v\n", b)
}

// a   map[brand:Ford model:Mustang year:1964]
// b   map[Bergen:2 Oslo:1 Stavanger:4 Trondheim:3]
```

### Create an Empty Map

```go
var a map[KeyType]ValueType
```

```go
package main
import ("fmt")

func main() {
  var a = make(map[string]string)
  var b map[string]string

  fmt.Println(a == nil) // fasle 
  fmt.Println(b == nil) // true
}
```

## Access Map Elements

`value = map_name[key]`

```go
func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Printf(a["brand"])
}
```

## Update and Add

`map_name[key] = value`

```go
package main
import ("fmt")

func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Println(a)

  a["year"] = "1970" // Updating an element
  a["color"] = "red" // Adding an element

  fmt.Println(a)
}
```

## Remove

`delete(map_name, key)`

```go
func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Println(a)

  delete(a,"year")

  fmt.Println(a)
}
```

## Check

`val, ok :=map_name[key]`

```go
func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964", "day":""}

  val1, ok1 := a["brand"] // Checking for existing key and its value
  val2, ok2 := a["color"] // Checking for non-existing key and its value
  val3, ok3 := a["day"]   // Checking for existing key and its value
  _, ok4 := a["model"]    // Only checking for existing key and not its value

  fmt.Println(val1, ok1)
  fmt.Println(val2, ok2)
  fmt.Println(val3, ok3)
  fmt.Println(ok4)
}

// Ford true
//  false
//  true
// true
```

## Iterate Over

use `range` to iterate over maps.

```go
package main
import ("fmt")

func main() {
  a := map[string]int{"one": 1, "two": 2, "three": 3, "four": 4}

  for k, v := range a {
    fmt.Printf("%v : %v, ", k, v)
  }
}
```

Maps are unordered data structures. If you need to iterate over a map in a specific order, you must have a separate data structure that specifies that order.

```go
// Iterate Over Maps in a Specific Order

package main
import ("fmt")

func main() {
  a := map[string]int{"one": 1, "two": 2, "three": 3, "four": 4}

  var b []string             // defining the order
  b = append(b, "one", "two", "three", "four")

  for k, v := range a {        // loop with no order
    fmt.Printf("%v : %v, ", k, v)
  }

  fmt.Println()

  for _, element := range b {  // loop with the defined order
    fmt.Printf("%v : %v, ", element, a[element])
  }
}

// two : 2, three : 3, four : 4, one : 1,
// one : 1, two : 2, three : 3, four : 4,
```

Maps are references to hash tables.

If two map variables refer to the same hash table, changing the content of one variable affect the content of the other.

```go
func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
  b := a

  fmt.Println(a)
  fmt.Println(b)

  b["year"] = "1970"
  fmt.Println("After change to b:")

  fmt.Println(a)
  fmt.Println(b)
}

// map[brand:Ford model:Mustang year:1964]
// map[brand:Ford model:Mustang year:1964]
// After change to b:
// map[brand:Ford model:Mustang year:1970]
// map[brand:Ford model:Mustang year:1970]
```

# Generics

Go functions can be written to work on multiple types using type parameters. The type parameters of a function appear between brackets, before the function's arguments.

```
func Index[T comparable](s []T, x T) int
```

This declaration means that `s` is a slice of any type `T` that fulfills the built-in constraint `comparable`. `x` is also a value of the same type.

`comparable` is a useful constraint that makes it possible to use the `==` and `!=` operators on values of the type. In this example, we use it to compare a value to all slice elements until a match is found. This `Index` function works for any type that supports comparison.

```Go
package main

import "fmt"

// Index returns the index of x in s, or -1 if not found.
func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		// v and x are type T, which has the comparable
		// constraint, so we can use == here.
		if v == x {
			return i
		}
	}
	return -1
}

func main() {
	// Index works on a slice of ints
	si := []int{10, 20, 15, -10}
	fmt.Println(Index(si, 15))

	// Index also works on a slice of strings
	ss := []string{"foo", "bar", "baz"}
	fmt.Println(Index(ss, "hello"))
}

// 2
// -1

```

In addition to generic functions, Go also supports generic types. A type can be parameterized with a type parameter, which could be useful for implementing generic data structures.

This example demonstrates a simple type declaration for a singly-linked list holding any type of value.

```Go
package main

// List represents a singly-linked list that holds
// values of any type.
type List[T any] struct {
	next *List[T]
	val  T
}

func main() {
}
```



# Error

When a function executes as expected, nil is returned for the error parameter.

```go
package main

import (
	"errors"
	"fmt"
	"os"
)

func calcRemainderAndMod(numerator, denominator int) (int, int, error) {
	if denominator == 0 {
		return 0, 0, errors.New("denominator is 0")
	}
	return numerator / denominator, numerator % denominator, nil
}

// When a function returns an error, use an if statement to check the error variable to see if it is non-nil:
func main() {
	numerator := 20
	denominator := 3
	remainder, mod, err := calcRemainderAndMod(numerator, denominator)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(remainder, mod)
}
```

## 显式返回错误

```go
package main

import (
        "errors"
        "fmt"
)

func divide(a, b int) (int, error) {
        if b == 0 {
                return 0, errors.New("division by zero")
        }
        return a / b, nil
}

func main() {
        result, err := divide(10, 0)
        if err != nil {
                fmt.Println("Error:", err)
        } else {
                fmt.Println("Result:", result)
        }
}
```

## 自定义错误

```go
package main

import (
        "fmt"
)

type DivideError struct {
        Dividend int
        Divisor  int
}

func (e *DivideError) Error() string {
        return fmt.Sprintf("cannot divide %d by %d", e.Dividend, e.Divisor)
}

func divide(a, b int) (int, error) {
        if b == 0 {
                return 0, &DivideError{Dividend: a, Divisor: b}
        }
        return a / b, nil
}

func main() {
        _, err := divide(10, 0)
        if err != nil {
                fmt.Println(err) // 输出：cannot divide 10 by 0
        }
}
```

## 错误格式化

```go
package main

import (
    "fmt"
)

// 定义一个 DivideError 结构
type DivideError struct {
    dividee int
    divider int
}

// 实现 `error` 接口
func (de *DivideError) Error() string {
    strFormat := `
    Cannot proceed, the divider is zero.
    dividee: %d
    divider: 0
`
    return fmt.Sprintf(strFormat, de.dividee)
}

// 定义 `int` 类型除法运算的函数
func Divide(varDividee int, varDivider int) (result int, errorMsg string) {
    if varDivider == 0 {
            dData := DivideError{
                    dividee: varDividee,
                    divider: varDivider,
            }
            errorMsg = dData.Error()
            return
    } else {
            return varDividee / varDivider, ""
    }

}

func main() {

    // 正常情况
    if result, errorMsg := Divide(100, 10); errorMsg == "" {
            fmt.Println("100/10 = ", result)
    }
    // 当除数为零的时候会返回错误信息
    if _, errorMsg := Divide(100, 0); errorMsg != "" {
            fmt.Println("errorMsg is: ", errorMsg)
    }

}
```

## panic 和 recover

Go 的 panic 用于处理不可恢复的错误，recover 用于从 panic 中恢复。

**panic:**

- 导致程序崩溃并输出堆栈信息。
- 常用于程序无法继续运行的情况。

**recover:**

- 捕获 `panic`，避免程序崩溃。

```go
package main

import "fmt"

func safeFunction() {
        defer func() {
                if r := recover(); r != nil {
                        fmt.Println("Recovered from panic:", r)
                }
        }()
        panic("something went wrong")
}

func main() {
        fmt.Println("Starting program...")
        safeFunction()
        fmt.Println("Program continued after panic")
}
```

# Concurrency

并发是指程序同时执行多个任务的能力。

Go 语言支持并发，通过 goroutines 和 channels 提供了一种简洁且高效的方式来实现并发。

**Goroutines：**

- Go 中的并发执行单位，类似于轻量级的线程。
- Goroutine 的调度由 Go 运行时管理，用户无需手动分配线程。
- 使用 `go` 关键字启动 Goroutine。
- Goroutine 是非阻塞的，可以高效地运行成千上万个 Goroutine。

**Channel：**

- Go 中用于在 Goroutine 之间通信的机制。
- 支持同步和数据共享，避免了显式的锁机制。
- 使用 `chan` 关键字创建，通过 `<-` 操作符发送和接收数据。

**Scheduler（调度器）：**

Go 的调度器基于 GMP 模型，调度器会将 Goroutine 分配到系统线程中执行，并通过 M 和 P 的配合高效管理并发。

- **G**：Goroutine。
- **M**：系统线程（Machine）。
- **P**：逻辑处理器（Processor）。

## Goroutine

goroutine 是轻量级线程，goroutine 的调度是由 Golang 运行时进行管理的。

`go 函数名( 参数列表 )`

Go 允许使用 go 语句开启一个新的运行期线程， 即 goroutine，以一个不同的、新创建的 goroutine 来执行一个函数。 同一个程序中的所有 goroutine 共享同一个地址空间。

```go
package main

import (
        "fmt"
        "time"
)

func sayHello() {
        for i := 0; i < 5; i++ {
                fmt.Println("Hello")
                time.Sleep(100 * time.Millisecond) // 让当前 goroutine 暂停 100 毫秒（0.1 秒）。
        }
}

func main() {
        go sayHello() // 启动 Goroutine
        for i := 0; i < 5; i++ {
                fmt.Println("Main")
                time.Sleep(100 * time.Millisecond)
        }
}

// 输出是没有固定先后顺序，因为它们是两个 goroutine 在执行
// Main
// Hello
// Main
// Hello
```

## Channel

通道（Channel）是用于 Goroutine 之间的数据传递。

通道可用于两个 goroutine 之间通过传递一个指定类型的值来同步运行和通讯。

使用 `make` 函数创建一个 channel，使用 `<-` 操作符发送和接收数据。如果未指定方向，则为双向通道。

```go
ch <- v    // 把 v 发送到通道 ch
v := <-ch  // 从 ch 接收数据 并把值赋给 v
```

声明一个通道

```go
ch := make(chan int)
```

> **注意**：默认情况下，通道是不带缓冲区的。发送端发送数据，同时必须有接收端相应的接收数据。
>
> 以下实例通过两个 goroutine 来计算数字之和，在 goroutine 完成计算后，它会计算两个结果的和：

```go
package main

import "fmt"

func sum(s []int, c chan int) { // 参数名叫 c，它是一个只能传递 int 的 channel。
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // 把 sum 发送到通道 c
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}

    c := make(chan int)
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    x, y := <-c, <-c // 从通道 c 中接收

    fmt.Println(x, y, x+y)
}

// -5 17 12
```

## Buffered Channels 通道缓冲区

带缓冲区的通道允许发送端的数据发送和接收端的数据获取处于异步状态，就是说发送端发送的数据可以放在缓冲区里面，可以等待接收端去获取数据，而不是立刻需要接收端去获取数据。

不过由于缓冲区的大小是有限的，所以还是必须有接收端来接收数据的，否则缓冲区一满，数据发送端就无法再发送数据了。

**注意**：如果通道不带缓冲，发送方会阻塞直到接收方从通道中接收了值。如果通道带缓冲，发送方则会阻塞直到发送的值被拷贝到缓冲区内；如果缓冲区已满，则意味着需要等待直到某个接收方获取到一个值。接收方在有值可以接收之前会一直阻塞。

```go
package main

import "fmt"

func main() {
    // 这里我们定义了一个可以存储整数类型的带缓冲通道
    // 缓冲区大小为2
    ch := make(chan int, 2)

    // 因为 ch 是带缓冲的通道，我们可以同时发送两个数据
    // 而不用立刻需要去同步读取数据
    ch <- 1
    ch <- 2

    // 获取这两个数据
    fmt.Println(<-ch)
    fmt.Println(<-ch)
}

// 1
// 2
```

### Go 遍历通道与关闭通道

Go 通过 range 关键字来实现遍历读取到的数据，类似于与数组或切片。

The loop `for i := range c` receives values from the channel repeatedly until it is closed.

A sender can `close` a channel to indicate that no more values will be sent. Receivers can test whether a channel has been closed by assigning a second parameter to the receive expression: after

`v, ok := <-ch`

`ok` is `false` if there are no more values to receive and the channel is closed.

如果通道接收不到数据后 ok 就为 false，这时通道就可以使用 **close()** 函数来关闭。

>  **Note:** Only the sender should close a channel, never the receiver. Sending on a closed channel will cause a panic.
>
> **Another note:** Channels aren't like files; you don't usually need to close them. Closing is only necessary when the receiver must be told there are no more values coming, such as to terminate a `range` loop.

```go
package main

import (
    "fmt"
)

func fibonacci(n int, c chan int) {
    x, y := 0, 1
    for i := 0; i < n; i++ {
        c <- x
        x, y = y, x+y
    }
    close(c)
}

func main() {
    c := make(chan int, 10)
    go fibonacci(cap(c), c)
    // range 函数遍历每个从通道接收到的数据，因为 c 在发送完 10 个
    // 数据之后就关闭了通道，所以这里我们 range 函数在接收到 10 个数据
    // 之后就结束了。如果上面的 c 通道不关闭，那么 range 函数就不
    // 会结束，从而在接收第 11 个数据的时候就阻塞了。
    for i := range c {
        fmt.Println(i)
    }
}
```

```go
0
1
1
2
3
5
8
13
21
34
```

### Select 语句

`select` 语句使得一个 goroutine 可以等待多个通信操作。`select` 会阻塞，直到其中的某个 case 可以继续执行：

The `select` statement lets a goroutine wait on multiple communication operations.

A `select` blocks until one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.

```go
package main

import "fmt"

func fibonacci(c, quit chan int) {
    x, y := 0, 1
    for {
        select {
        case c <- x:
            x, y = y, x+y
        case <-quit:
            fmt.Println("quit")
            return
        }
    }
}

func main() {
    c := make(chan int)
    quit := make(chan int)

    go func() {
        for i := 0; i < 10; i++ {
            fmt.Println(<-c)
        }
        quit <- 0
    }()
    fibonacci(c, quit)
}
```

```go
0
1
1
2
3
5
8
13
21
34
quit
```

#### Default Selection

The `default` case in a `select` is run if no other case is ready.

```Go
select {
case i := <-c:
    // use i
default:
    // receiving from c would block
}
```

```Go
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)
	elapsed := func() time.Duration {
		return time.Since(start).Round(time.Millisecond)
	}
	for {
		select {
		case <-tick:
			fmt.Printf("[%6s] tick.\n", elapsed())
		case <-boom:
			fmt.Printf("[%6s] BOOM!\n", elapsed())
			return
		default:
			fmt.Printf("[%6s]     .\n", elapsed())
			time.Sleep(50 * time.Millisecond)
		}
	}
}

```

## sync.Mutex

we just want to make sure only one goroutine can access a variable at a time to avoid conflicts?

This concept is called *mutual exclusion*, and the conventional name for the data structure that provides it is *mutex*.

Go's standard library provides mutual exclusion with [`sync.Mutex`](https://go.dev/pkg/sync/#Mutex) and its two methods:

- `Lock`
- `Unlock`

We can define a block of code to be executed in mutual exclusion by surrounding it with a call to `Lock` and `Unlock` as shown on the `Inc` method.

We can also use `defer` to ensure the mutex will be unlocked as in the `Value` method.

```Go
package main

import (
	"fmt"
	"sync"
	"time"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	mu sync.Mutex
	v  map[string]int
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	c.mu.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	defer c.mu.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go c.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(c.Value("somekey"))
}

```



## WaitGroup

sync.WaitGroup 用于等待多个 Goroutine 完成。

**同步多个 Goroutine：**

```go
package main

import (
        "fmt"
        "sync"
)

func worker(id int, wg *sync.WaitGroup) {
        defer wg.Done() // Goroutine 完成时调用 Done()
        fmt.Printf("Worker %d started\n", id)
        fmt.Printf("Worker %d finished\n", id)
}

func main() {
        var wg sync.WaitGroup

        for i := 1; i <= 3; i++ {
                wg.Add(1) // 增加计数器
                go worker(i, &wg)
        }

        wg.Wait() // 等待所有 Goroutine 完成
        fmt.Println("All workers done")
}
```

```go
Worker 1 started
Worker 1 finished
Worker 2 started
Worker 2 finished
Worker 3 started
Worker 3 finished
All workers done
```

**死锁 (Deadlock)：**

- 示例：所有 Goroutine 都在等待，但没有任何数据可用。
- 解决：避免无限等待、正确关闭通道。

**数据竞争 (Data Race)：**

- 示例：多个 Goroutine 同时访问同一变量。
- 解决：使用 Mutex 或 Channel 同步访问。

# Context

Servers need a way to handle metadata on individual requests. This metadata falls into two general categories: metadata that is required to correctly process the request, and metadata on when to stop processing the request. For example, an HTTP server might want to use a tracking ID to identify a chain of requests through a set of micro‐ services. It also might want to set a timer that ends requests to other microservices if they take too long. Many languages use threadlocal variables to store this kind of information, associat‐ ing data to a specific operating system thread of execution. This doesn’t work in Go because goroutines don’t have unique identities that can be used to look up values. 

Go 语言里的 **`context`（上下文）** 是处理**并发控制**和**请求生命周期管理**的“杀手锏”。

就像你引用的英文段落里说的：Go 没有 Thread-local（线程局部变量），也不搞“把变量隐式藏在后台”的魔法。Go 的哲学是**显式传递** — 把 `ctx context.Context` 作为**函数的第一个参数**一层层传下去。

在实际 Go 开发（尤其是后端 API、微服务和 AI Agent 开发）中，使用 `context` 的核心场景主要有以下 **3 个**：

## 1. 超时控制与取消（Timeout & Cancellation）

**场景**：你的服务需要调用下游接口（比如调用 OpenAI API、查 MySQL 数据库、发起 HTTP 请求）。如果下游卡住了，你不能让你的 Goroutine 一直傻等耗尽资源。

- **超时控制 (`context.WithTimeout`)**：限制某个操作最多执行多长时间。

  ```go
  // 设置 2 秒超时
  ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
  defer cancel() // 养成好习惯：退出时显式释放资源
  
  // 把 ctx 传给 HTTP 请求或数据库查询
  req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.openai.com/v1/models", nil)
  ```

- **手动取消 (`context.WithCancel`)**：比如前端用户取消了下载/请求，后端立刻感知并干掉正在后台跑的 Goroutine，释放 CPU 和内存。

## 2. 跨层级/跨服务传递请求元数据（Request Metadata）

**场景**：当一个 HTTP 请求打进来，会经过 **Web 框架中间件 -> Service 层 -> DAO 数据库层 -> 调用微服务**。你需要在整条链路上传递一些公共的“请求上下文信息”。

- **全链路追踪 (Tracing ID / Request ID)**：给每个请求生成一个 UUID 存入 `context`，后续打日志时带上这个 ID，排查问题时一搜就能看到整个调用链。
- **身份认证 (Auth / User Info)**：JWT 中间件解析出当前登录用户的 `userID` 存入 `context`，下层的业务函数直接拿出来用。

```go
// 1. 中间件写入：把 userID 存入 context
ctx := context.WithValue(r.Context(), "userID", 12345)

// 2. 业务层/数据库层读取
userID := ctx.Value("userID").(int)
```

> **⚠️ 注意**：`context.WithValue` **只用来传轻量级的请求元数据**，千万不要把复杂的业务参数或可选参数塞进去（那属于滥用）。

## 3. 级联取消（Cascade Cancellation）

**场景**：一个主 Goroutine 派生出了 5 个子 Goroutine 去并行抓取网页或处理任务。如果主 Goroutine 决定终止，或者其中一个任务报错了需要整体撤退，怎么通知所有 Goroutine 停下？

通过父子 `context` 树：**只要父 `context` 被 `cancel()`，所有由它衍生出来的子 `context` 也会收到取消信号 (`<-ctx.Done()`)**，实现“一键统统撤退”。

```go
select {
case <-ctx.Done():
    // 收到取消或超时信号，清理现场并退出 Goroutine
    return ctx.Err()
case res := <-ch:
    // 正常拿到结果
    return res
}
```

Go 函数签名看到 `ctx`

在写 Go 代码（特别是写 Go 的 API 客户端或 Agent 工具链）时：

1. **凡是涉及到 I/O、网络调用、数据库查询的函数**，第一个参数统一写 `ctx context.Context`。
2. **需要控制超时或传 TraceID 时**，用 `context`。
3. 它本质就是一个**通知机制**（告诉后台：“时间到了/用户撤了，别干了”）+ **一个小背包**（带一点点请求级别的全局信息）。

# packages

Programs start running in package `main`.

This program is using the packages with import paths `"fmt"` and `"math/rand"`.

By convention, the package name is the same as the last element of the import path. For instance, the `"math/rand"` package comprises files that begin with the statement `package rand`.

**一个目录 = 一个 package。**

**目录里的每个 `.go` 文件都要写相同的 `package xxx`。**

```Go
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```

```
myproject/
│
├── main.go
│
└── calculator/
    ├── add.go
    └── sub.go
```

```Go
calculator/
├── add.go          package calculator
├── sub.go          package calculator
└── add_test.go     package calculator_test
```

```Go
// calculator/add.go
package calculator

func Add(a, b int) int {
    return a + b
}
```

```Go
// main.go
package main

import (
    "myproject/calculator"
)

func main() {
    calculator.Add(1, 2)
}
```

```
import "myproject/calculator"
```

最后一级：

```
calculator
```

所以：

```
package calculator
```

# libraries

这三个标准库（`io`、`time`、`encoding/json`）是 Go 语言标准库中的**绝对核心**。无论是做后端开发，还是写高并发的 AI Agent、微服务，它们的使用频率几乎是 100%。

下面为你逐一拆解这些核心概念和机制：

## 1. `io` 及其家族（io and Friends）

Go 语言在架构设计上最经典、最优雅的设计之一就是 `io` 包。它通过极简的接口，统一了文件、网络 Socket、内存缓冲区、标准输入输出等所有 I/O 操作。

### 核心接口：流式处理的基石

- **`io.Reader`**：定义了 `Read(p []byte) (n int, err error)`。意思是“**从某个地方读取字节填满 byte 切片**”。
- **`io.Writer`**：定义了 `Write(p []byte) (n int, err error)`。意思是“**把 byte 切片里的数据写入某个地方**”。
- **`io.Closer`**：定义了 `Close() error`。用于释放文件或网络连接等资源。

### “Friends”（常用的扩展包）

- **`os`**：`os.File` 既实现了 `io.Reader` 也实现了 `io.Writer`，是读写文件的核心。
- **`bufio`**：带缓冲区的 I/O。如果要一行行读取大文件（如日志分析），用 `bufio.Scanner` 或 `bufio.Reader` 能极大减少系统调用开销，提高性能。
- **`bytes` & `strings`**：`bytes.Buffer` 和 `strings.Reader` 让你可以把内存中的字符串或字节切片当成 `io.Reader`/`io.Writer` 来用。
- **`io.Copy`**：直接把数据从 `Reader` 零拷贝/高效地“流”向 `Writer`（比如把网络响应直接存入文件）。

### 场景 1：用 `io.Copy` 实现“零内存占用”的文件复制

如果你想把一个几 GB 的文件复制到另一个地方，**千万不要一次性把整个文件读进内存**。用 `io.Copy`，它会用内部小缓冲区像水管接水一样，边读边写。

```Go
package main

import (
	"io"
	"os"
)

func main() {
	// 1. 打开源文件 (实现了 io.Reader)
	srcFile, _ := os.Open("source.txt")
	defer srcFile.Close()

	// 2. 创建目标文件 (实现了 io.Writer)
	dstFile, _ := os.Create("destination.txt")
	defer dstFile.Close()

	// 3. 像连接水管一样，把数据从 src 抽到 dst
	// 内存开销极小，速度极快！
	written, err := io.Copy(dstFile, srcFile)
	if err != nil {
		panic(err)
	}
	println("成功复制字节数:", written)
}
```

### 场景 2：用 `bufio` 按行高效读取大文件（如日志）

如果你需要处理日志文件或 CSV 逐行分析，使用带缓冲区的 `bufio.Scanner` 能极大减少对磁盘的系统调用开销。

```Go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("app.log")
	defer file.Close()

	// 用 bufio 包装文件 reader
	scanner := bufio.NewScanner(file)

	// 逐行扫描（默认按 '\n' 切割）
	lineNumber := 1
	for scanner.Scan() {
		line := scanner.Text() // 拿到当前行的字符串
		fmt.Printf("Line %d: %s\n", lineNumber, line)
		lineNumber++
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("读取文件出错:", err)
	}
}
```

### 场景 3：用 `bytes.Buffer` 在内存里拼接和处理流

当你调 API 或生成动态文本时，想用 `io.Reader` 传参，但手里只有内存中的数据，可以用 `bytes.Buffer`（它既是 `Writer` 也是 `Reader`）。

```Go
package main

import (
	"bytes"
	"fmt"
	"io"
)

func main() {
	// 1. 建立一个内存缓冲区 (实现了 io.ReaderWriter)
	var buf bytes.Buffer

	// 2. 像写文件一样往内存写数据
	buf.WriteString("Hello ")
	buf.WriteString("Go IO!")

	// 3. 把这个内存缓冲区当作 io.Reader 传给 io.ReadAll 一次性读取
	data, _ := io.ReadAll(&buf)
	fmt.Println("从 Buffer 读出:", string(data)) // 输出: Hello Go IO!
}
```

### 场景 4：用 `io.TeeReader` 实现“边下载边保存边处理”（高阶玩法）

假设你要从网络下载一个文件，想**一边**写入磁盘保存，**一边**实时计算它的进度或打印到控制台。`io.TeeReader`（T型管道，就像三通水管）能把读取流分叉！

```Go
package main

import (
	"io"
	"os"
	"strings"
)

func main() {
	// 假设这是从网络收到的数据流 (Reader)
	networkStream := strings.NewReader("这是一段非常重要的网络数据流...")

	// 创建本地保存文件 (Writer)
	localFile, _ := os.Create("downloaded.txt")
	defer localFile.Close()

	// TeeReader: 每次从 tee 里面 Reader 读数据，它会自动【顺便】往 localFile 里写一份！
	tee := io.TeeReader(networkStream, localFile)

	// 现在我们把 tee 里面的数据打印到标准输出 os.Stdout（屏幕）
	// 在打印的同时，downloaded.txt 文件里也被同步写入了！
	io.Copy(os.Stdout, tee)
}
```

| **工具**                | **解决的问题**                                               |
| ----------------------- | ------------------------------------------------------------ |
| **`os.File`**           | 最基础的磁盘文件 Reader/Writer。                             |
| **`io.Copy(dst, src)`** | 连接两个管道，把 `src` 的数据直接搬到 `dst`。                |
| **`bufio.Scanner`**     | 适合**按行/按分隔符**高效读取数据。                          |
| **`bytes.Buffer`**      | 内存中的字节管道，方便把内存数据当作 `io.Reader/Writer` 传递。 |
| **`io.ReadAll(r)`**     | 一次性把 Reader 里的所有数据读完（适合数据量小的场景）。     |



## 2. `time`：时间与定时任务

处理时间看起来简单，但高并发和跨平台场景下陷阱极多。Go 的 `time` 包在这方面做得很优秀。

### 单调时间（Monotonic Time） vs 墙上时间（Wall Clock Time）

- **墙上时间（Wall Clock Time）**：就是我们手表上的“真实时间”（比如 10:30:00）。它可能会因为 NTP 网络对时、闰秒或手动修改系统时间而发生**跳变或倒退**。
- **单调时间（Monotonic Time）**：**只会递增、绝不倒退**的时间，通常基于 CPU 开机以来的 Tick 计数。
- **Go 的优化**：Go 的 `time.Time` 结构体在内部**同时保存了这两者**。当你计算时间差（如 `time.Since(start)` 或 `t2.Sub(t1)`）时，Go 内部**会自动使用单调时间**，因此绝对不会受到系统对时改动的影响，性能基准测试和超时计算极度精准。

### 定时器与超时（Timers and Timeouts）

- **`time.Timer`（单次定时器）**：在未来某个时间点触发一次。结合 `select` 和 `context` 常常用来做并发超时控制：

  ```Go
  timer := time.NewTimer(2 * time.Second)
  select {
  case <-ch:
      timer.Stop() // 收到数据，取消定时器
  case <-timer.C:
      // 2秒到了还没拿到数据，报超时错误
  }
  ```

- **`time.Ticker`（周期定时器）**：按固定间隔重复触发（比如每 5 秒心跳检测一次）。用完必须调用 `ticker.Stop()` 释放 Goroutine 资源。

## 3. `encoding/json`：JSON 处理与序列化

在 API 交互和 LLM 接口调用中，JSON 随处可见。Go 语言通过结构体标签（Struct Tags）和反射机制实现了极度高效的 JSON 解析。

### 使用 Struct Tags 添加元数据

因为 Go 变量通常是首字母大写导出（如 `UserName`），而 JSON 通常用下划线或小驼峰（如 `user_name`），我们需要使用 Tag 来做映射：

```Go
type User struct {
    Name     string `json:"user_name"`           // 映射字段名
    Age      int    `json:"age,omitempty"`       // 如果 age 为 0/空，序列化时忽略该字段
    Password string `json:"password,string"`     // 强制把数字/布尔按字符串转义
    Secret   string `json:"-"`                   // 彻底忽略该字段，不参与 JSON 解析
}
```

### 序列化与反序列化（Unmarshaling and Marshaling）

这是处理**已在内存中的字节数组 (`[]byte`)** 时的方法：

- **`json.Marshal(v)`**：内存对象 $\rightarrow$ JSON `[]byte`。
- **`json.Unmarshal(data, &v)`**：JSON `[]byte` $\rightarrow$ 内存对象指针。

### JSON、Readers 和 Writers（流式编解码）

当处理 **HTTP 请求/响应体、文件** 等实现了 `io.Reader`/`io.Writer` 的流时，不要先把数据读进 `[]byte` 内存，而应该用流式编解码，**性能更好且省内存**：

- **`json.NewDecoder(r)`**：直接从 `io.Reader`（如 `http.Request.Body`）解析 JSON。
- **`json.Encoder(w)`**：直接将 JSON 写入 `io.Writer`（如 `http.ResponseWriter`）。

```Go
// 优雅的 HTTP Handler 写法：直接解析 HTTP 请求 Body
var req UserRequest
err := json.NewDecoder(r.Body).Decode(&req)
```

### 编解码 JSON 流（Encoding and Decoding JSON Streams）

如果遇到一个包含大量 JSON 对象的流（比如 OpenAI API 的 SSE 流式响应，或者按行分隔的 JSON Lines 大文件），你可以用 `Decoder.More()` 和循环，**逐个迭代读取 JSON 对象**，而不需要一次性把几千兆的文件载入内存。

### 自定义 JSON 解析（Custom JSON Parsing）

如果标准的 JSON 转换无法满足要求（比如后端接收到的时间格式是 `2026-07-21`，而 Go 默认需要 RFC3339 格式），你可以让自己的类型实现以下两个接口，来自定义解析逻辑：

- `json.Marshaler`：实现 `MarshalJSON() ([]byte, error)`
- `json.Unmarshaler`：实现 `UnmarshalJSON([]byte) error`

## 4. net/http

`net/http` 是 Go 语言标准库中的“镇国之宝”。Go 语言之所以在云原生（Docker/Kubernetes）、微服务和 Web 后端开发中统治力极强，很大程度上就是因为它的 `net/http` 标准库**性能极高、设计极度优雅，而且完全开箱即用**，不需要像 Python (Django/Flask) 或 Node.js (Express) 那样必须依赖第三方框架。

下面为你拆解 `net/http` 的三大核心板块：**Client（客户端）**、**Server（服务端）** 和 **ResponseController（响应控制器）**。

### 1. The Client（HTTP 客户端）

`net/http` 提供了强大的 HTTP 客户端，用来发起网络请求（比如调第三方 API、抓取网页或调 OpenAI/Claude 的大模型接口）。

#### ① 最简单的请求（默认客户端）

```Go
resp, err := http.Get("https://api.github.com")
if err != nil {
    // 处理网络错误
}
defer resp.Body.Close() // ⚠️ 必须手动关闭 Body，否则会泄漏 TCP 连接！

body, _ := io.ReadAll(resp.Body)
```

#### ② 生产环境最佳实践：自定义 `http.Client`

在真实工程中，**千万不要直接用 `http.Get` 或 `http.DefaultClient`**，因为它**没有默认超时时间**！一旦下游服务卡死，你的 Goroutine 就会无限期挂起，最终吃光系统资源。

必须显式配置 Timeout 和 Transport：

```Go
client := &http.Client{
    Timeout: 5 * time.Second, // 设置 5 秒全局超时
}

// 结合 Context 发起带取消/超时的请求
req, _ := http.NewRequestWithContext(ctx, "POST", url, bodyReader)
req.Header.Set("Content-Type", "application/json")

resp, err := client.Do(req)
```

### 2. The Server（HTTP 服务端）

Go 的 HTTP 服务器极度高效，每个进来的请求（Request）都会在一个**独立的 Goroutine** 中并发处理。

#### ① 核心接口：`http.Handler`

Go 的 Web 核心思想只有这一个接口：

```Go
type Handler interface {
    ServeHTTP(ResponseWriter, *Request)
}
```

只要实现了 `ServeHTTP` 方法，任何结构体都可以作为 HTTP 处理程序。

#### ② 编写一个简单的 Server

最常用的方式是使用 `http.HandleFunc`：

```Go
package main

import (
	"fmt"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	// r (*http.Request): 包含请求头、URL 参数、Body 等
	// w (http.ResponseWriter): 用来给客户端写回响应（Header、StatusCode、Body）
	
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "World"
	}
	
	w.Header().Set("Content-Type", "text/plain")
	w.WriteHeader(http.StatusOK) // 返回 200
	fmt.Fprintf(w, "Hello, %s!", name)
}

func main() {
	http.HandleFunc("/hello", helloHandler)
	
	// 启动 HTTP 服务器监听 8080 端口
	http.ListenAndServe(":8080", nil)
}
```

### 3. ResponseController（响应控制器，Go 1.20+ 新特性）

这是 Go 1.20 引入的一个非常优秀的增强特性，专门用来**在 HTTP Handler 中进行高阶控制**（比如做 **SSE 实时流式响应 / AI 大模型打字机输出**、或者 WebSocket 连接提升）。

在 Go 1.20 之前，如果你想在 Handler 里手动刷新缓冲区（Flush，把数据立刻推给前端）或者把连接劫持（Hijack），你必须把 `http.ResponseWriter` **强转类型**为 `http.Flusher` 或 `http.Hijacker` 接口。如果中间用了第三方中间件包装 `w`，强转就会失败并 `panic`。

`http.ResponseController` 统一并优雅地解决了这个问题。

#### 核心用法（以大模型 SSE 流式输出为例）：

当你在写 AI Agent 时，模型生成文本是一字一字出来的，你希望**每生成一个字就立刻推给前端**，而不是等整个回答生成完才一口气返回：

```Go
func streamHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "text/event-stream")
    w.Header().Set("Cache-Control", "no-cache")

    // 创建 ResponseController 控制器
    rc := http.NewResponseController(w)

    for i := 0; i < 5; i++ {
        // 模拟大模型逐字吐出数据
        fmt.Fprintf(w, "data: Chunk %d\n\n", i)

        // 🌟 核心：立刻把缓冲区的数据推送到客户端屏幕上！
        err := rc.Flush()
        if err != nil {
            return // 客户端断开了连接
        }

        time.Sleep(500 * time.Millisecond)
    }
}
```

#### `ResponseController` 的 4 个核心方法：

1. **`Flush()`**：强制将当前缓冲的数据发送给客户端（流式输出/SSE 必备）。
2. **`Hijack()`**：夺取底层 TCP 连接的控制权（常用于将 HTTP 协议升级为 WebSocket 协议）。
3. **`SetReadDeadline(t)`**：动态修改当前请求的**读取超时时间**（例如允许客户端上传一个超大文件）。
4. **`SetWriteDeadline(t)`**：动态修改当前请求的**写入超时时间**（例如允许长连接流式响应跑更长时间）。

| **组件**                 | **核心职能**             | **核心注意点 / 适用场景**                                    |
| ------------------------ | ------------------------ | ------------------------------------------------------------ |
| **`http.Client`**        | 发起 HTTP 请求           | 生产环境**严禁使用默认 Client**，必须显式配置 `Timeout`；响应 `resp.Body` 必须 `Close()`。 |
| **`http.Server`**        | 接收并处理 HTTP 请求     | 每一个请求跑在一个独立的 Goroutine 里；核心是 `http.Handler` 接口。 |
| **`ResponseController`** | 手工精细化控制 HTTP 响应 | **Go 1.20+ 推荐**。用于 **SSE 流式传输（大模型打字机）**、WebSocket 协议升级 (`Hijack`) 和动态调整请求超时。 |

# Tests

Go 语言将测试提升到了**一等公民（First-class citizen）\**的地位。在真实的工程与面试（特别是构建高并发服务或 AI Agent 系统）中，Go 测试体系中有几个\**绝对的核心要点**是必须吃透的。

结合你提供的这章大纲，以下是按“实战重要程度”为你抽离的**必知必会核心内容**：

### 1. 表格驱动测试（Table Tests）—— Go 社区的标准规范

这是 Go 中最推荐的单元测试编写方式，能用极少的重复代码覆盖大量边界条件。

- **核心写法**：定义一个匿名结构体切片（包含输入参数 `input` 和期望输出 `expected`），然后用 `for` 循环搭配 `t.Run(tt.name, func(t *testing.T) {...})` 跑子测试。
- **必注意点**：在循环中使用 `t.Parallel()` 时，一定要注意 Go 闭包变量捕获（Goroutine 变量捕获）的问题（虽然 Go 1.22+ 修复了循环变量问题，但理解机制依然重要）。

### 2. 核心与辅助工具链

#### ① `go-cmp` (Google 开源的对比库)

- **为什么用它**：Go 自带的 `reflect.DeepEqual` 经常因为未导出字段、切片顺序或指针不同而导致对比不准确，且报错信息极难看。
- **作用**：`cmp.Diff(want, got)` 能生成清晰的**类似 Git diff 的差异输出**，是处理复杂结构体测试的工业界标准。

#### ② 并发测试与 Data Race Detector (`-race`)

- **必须掌握**：在运行测试时加上 `-race` 标志（如 `go test -race ./...`）。
- **原理**：它会在编译时插入检测代码，运行时一旦发现两个 Goroutine 在没有加锁或无 Channel 同步的情况下同时读写同一个内存地址，**直接抛出 Race Warning**。这是 Go 排查并发 Bug 的最强工具。

#### ③ `httptest`（HTTP 接口测试）

- **为什么重要**：做后端 API 或 Agent 工具时，写完 HTTP Handler 不需要真的把服务器跑起来占用端口。
- **核心类**：`httptest.NewRecorder()`（模拟响应收集器）和 `httptest.NewServer()`（快速拉起一个本地 Mock HTTP 服务器测试第三方 API 调用）。

### 3. 性能与边界保障（Benchmarks & Fuzzing）

#### ① 性能基准测试（Benchmarks）

- **函数签名**：必须以 `BenchmarkXxx(b *testing.B)` 开头。
- **核心逻辑**：使用 `for i := 0; i < b.N; i++` 循环。`b.N` 是 Go 测试框架根据运行时间**动态调整**的，直到取得稳定的平均执行时间。
- **常用命令**：`go test -bench=. -benchmem`（`-benchmem` 可以查看每次操作分配了多少内存、发生了多少次内存分配 `allocs/op`，这对性能优化至关重要）。

#### ② 模糊测试（Fuzzing，Go 1.18+ 原生支持）

- **函数签名**：`FuzzXxx(f *testing.F)`。
- **原理**：你提供种子数据（Seed），Go 的 Fuzz 引擎会在后台自动生成海量的随机、畸形数据（比如空字符串、超长 Unicode、特殊符号）注入函数，去撞击你代码中的 panic 或隐蔽 Bug。对于解析 JSON、字符串处理等逻辑极其有效。

### 4. 架构隔离：Build Tags 与集成测试

- **问题**：单元测试（Unit Test）应该在几毫秒内跑完，而集成测试（Integration Test，需要连接真实数据库或 Docker）很慢。
- **解决方式**：使用 **Build Tags**（编译标签）。在集成测试文件顶部加上 `//go:build integration`。
- **效果**：平时直接运行 `go test ./...` 会自动忽略这些慢测试；只有当你在 CI/CD 中显式指定 `go test -tags=integration ./...` 时才会触发。

| **概念/工具**      | **解决什么问题**             | **一句话总结**                         |
| ------------------ | ---------------------------- | -------------------------------------- |
| **`t.Parallel()`** | 测试太慢                     | 告诉框架这个测试可以和其它测试并发跑。 |
| **`go-cmp`**       | `reflect.DeepEqual` 报错不清 | 比对两个复杂对象并优雅地输出 Diff。    |
| **`httptest`**     | 测试 Web API 麻烦            | 无需占端口即可模拟 HTTP 请求与响应。   |
| **`-race`**        | 难以定位的并发 Bug           | 编译时插桩，运行时精准捕获数据竞争。   |
| **`Build Tags`**   | 单元测试和集成测试混在一起   | 给测试文件加标签，实现按需分类执行。   |

在实际的 Go 工程（以及后端/AI 系统开发）中，**绝对不需要给每一行代码都写测试**。追求 100% 的测试覆盖率往往是性价比极低的“KPI 行为”。

我们可以把需要写测试的内容，按优先级分为以下 **4 个梯队**：

### 第一梯队：必写！核心业务逻辑与算法（Core Business & Algorithms）

这里是系统的“心脏”，一旦出问题会直接导致资金损失或系统崩溃。

- **核心计算/状态转换**：例如订单扣款、折扣计算、状态机（如订单从 `待支付` $\rightarrow$ `已支付` $\rightarrow$ `已发货` 的流转规则）。
- **复杂的数据处理/解析**：例如自研的协议解析器、JSON 数据清洗逻辑、文本 Token 切分、RAG 中的文档 Chunking（切块）算法。
- **权限与安全校验**：例如 JWT Token 解析、用户越权访问拦截逻辑。

> **测试方法**：非常适合用 **Table Tests（表格驱动测试）**，穷举各种边界输入（如空值、负数、超长字符串）。

### 第二梯队：必写！高并发与状态共享逻辑（Concurrency & Mutex）

Go 语言以并发见长，但并发也是最容易藏匿“偶发性 Bug”的地方。

- **Goroutine 之间的通信/同步**：例如自定义的 Worker Pool（协程池）、异步任务队列、限流器（Rate Limiter）。
- **带锁的共享资源**：例如使用了 `sync.Mutex` 或 `sync.Map` 的全局缓存。

> **测试方法**：写并发测试，并且在运行时**必须加上 `-race` 参数**（`go test -race ./...`），检测是否存在 Data Race（数据竞争）。

### 第三梯队：必须覆盖！边界条件与错误处理（Edge Cases & Errors）

Go 哲学强调 `if err != nil`。很多崩溃不是因为主流程跑不通，而是因为异常分支没处理好导致 `panic`。

- **边界/极端输入**：
  - 空指针（`nil`）、空切片（`[]`）、空字符串（`""`）。
  - 极大/极小数值（如整数溢出）、特殊 Unicode 字符/Emoji。
- **第三方服务失败**：
  - 网络超时、数据库连接断开、HTTP 接口返回 500。

> **测试方法**：使用 **Fuzzing（模糊测试）** 扔海量随机数据进去撞击代码；或者使用 `httptest` / Stub 来模拟第三方接口报错。

### 第四梯队：看情况写！API 接口与数据库交互（Integration Tests）

这部分测试属于“集成测试”，写起来成本稍高，但能保障系统的整体链路通畅。

- **HTTP / gRPC Handler**：验证请求参数校验、返回的状态码（200/400/500）和 Response JSON 格式是否符合预期。
- **数据库 DAO 层（复杂 SQL）**：普通的 CRUD 可以不写，但涉及多表联查、复杂事务（Transaction）的 SQL 逻辑需要写测试。

> **测试方法**：使用 `httptest` 模拟 HTTP 请求；对于数据库测试，通常配合 Docker（如 Testcontainers）拉起真实的轻量级数据库进行测试，并用 Build Tags (`//go:build integration`) 隔离。

### ❌ 什么东西“不需要”写测试？

写测试也是有维护成本的，以下内容通常**直接忽略**：

1. **纯 Get/Set 方法或简单的结构体赋值**：比如 `func (u *User) GetName() string { return u.Name }`。
2. **官方/第三方标准库的功能**：不需要去测试 `json.Marshal` 或 `fmt.Sprintf` 是否正常工作（要相信标准库）。
3. **纯胶水代码（Glue Code）**：例如把 `A` 变量拿出来传给 `B` 函数，里面没有任何判断逻辑的代码。
4. **`main.go` 的启动入口**：通常只负责读取配置和启动服务，很难也不需要写单元测试。

在做工程开发时，牢记这个测试策略：

$$\text{核心算法/业务 (100\% 覆盖)} > \text{并发与错误分支 (80\% 覆盖)} > \text{普通接口/胶水代码 (抽查/集成测试)}$$

先用 **Table Tests** 保证核心逻辑不出错，再用 **`-race`** 保证并发不出错，就能帮你解决 90% 以上的生产线问题！











