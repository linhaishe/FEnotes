# 标识符

第一个字符必须以字母（a-z, A-Z）或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感，count 和 Count 是不同的标识符。
标识符对长度无硬性限制，但建议保持简洁（一般不超过 20 个字符）。
禁止使用保留关键字，如 if、for、class 等不能作为标识符。

```python
# 合法标识符：

age = 25                # 普通变量名，最常见
user_name = "Alice"     # 用下划线连接单词，清晰易读
_total = 100            # 下划线开头通常表示“内部使用”或“私有”
MAX_SIZE = 1024         # 全大写通常表示“常量”（固定不变的值）
calculate_area()        # 函数名，动词+名词
StudentInfo             # 类名，首字母大写（驼峰命名法）
__private_var           # 双下划线开头，有特殊含义

# 非法标识符：

2nd_place = "silver"    # 错误：以数字开头
user-name = "Bob"       # 错误：包含连字符
class = "Math"          # 错误：使用关键字
$price = 9.99          # 错误：包含特殊字符
for = "loop"           # 错误：使用关键字
```

> 更多 Python 保留关键字参考：https://www.runoob.com/python3/python3-keyword.html。

# 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 **\** 来实现多行语句，例如：

```python
total = item_one + \
        item_two + \
        item_three
```

# 实例

```python
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
    item_three
    
**print**(total) # 输出为 6
```

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 **\**，例如：

```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```

# 标准数据类型

- **In Python type errors can reveal themselves during execution**, when the program is actually running and using your code.
- **Compiled languages catch type errors during the compile step**, before the program is allowed to run.

```python
内置类型
├── 数字类型
│   ├── int
│   └── float
├── 序列类型
│   ├── str
│   ├── list
│   ├── tuple
│   └── range
├── 映射类型
│   └── dict
└── 集合类型
    └── set
```



Python3 中有 6 种标准数据类型，以及 bool 布尔类型（bool 是 int 的子类，有时单独列出）：

- Number（数字）
- String（字符串）
- bool（布尔类型）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

按是否可变，可以分为以下两类：

- **不可变数据（4 个）：**Number（数字）、String（字符串）、bool（布尔）、Tuple（元组）
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）

此外还有一些高级的数据类型，如字节数组类型 bytes。

索引值以 0 为开始值，-1 为从末尾开始的位置。

![image-20260703114622995](https://i.postimg.cc/Bqw9pkPZ/image-20260703114622995.png?dl=1)

加号 **+** 是字符串的连接符，星号 ***** 表示复制当前字符串，与之结合的数字为复制的次数。

# 1. 数据类型转换

## 隐式类型转换 - 自动完成

```python
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_flo))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))

----

num_int 数据类型为: <class 'int'>
num_flo 数据类型为: <class 'float'>
num_new: 值为: 124.23
num_new 数据类型为: <class 'float'>
```

## 显式类型转换 - 需要使用类型函数来转换

```python
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))
```

## 转换方法

| 函数                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [int(x [,base\])](https://www.runoob.com/python3/python3-func-int.html") | 将x转换为一个整数                                   |
| [float(x)](https://www.runoob.com/python3/python3-func-float.html") | 将x转换到一个浮点数                                 |
| [complex(real [,imag\])](https://www.runoob.com/python3/python3-func-complex.html") | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python3/python3-func-str.html") | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python3/python3-func-repr.html") | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python3/python3-func-eval.html") | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python3/python3-func-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python3/python3-att-list-list.html) | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python3/python3-func-set.html") | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python3/python3-func-dict.html") | 创建一个字典。d 必须是一个 (key, value)元组序列。   |
| [frozenset(s)](https://www.runoob.com/python3/python3-func-frozenset.html") | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python3/python3-func-chr.html") | 将一个整数转换为一个字符                            |
| [ord(x)](https://www.runoob.com/python3/python3-func-ord.html") | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python3/python3-func-hex.html") | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python3/python3-func-oct.html") | 将一个整数转换为一个八进制字符串                    |
| [bool(x)](https://www.runoob.com/python3/python3-func-bool.html") | 将对象 x 转换为布尔值（True 或 False）              |
| [bytes([source[, encoding[, errors\]]])](https://www.runoob.com/python3/python3-func-bytes.html") | 将对象转换为不可变字节序列                          |
| [bytearray([source[, encoding[, errors\]]])](https://www.runoob.com/python3/python3-func-bytearray.html") | 将对象转换为可变字节数组                            |
| [memoryview(obj)](https://www.runoob.com/python3/python3-func-memoryview.html") | 返回给定参数的内存视图对象（不复制数据）            |
| [bin(x)](https://www.runoob.com/python3/python3-func-bin.html") | 将一个整数转换为一个二进制字符串                    |
| [ascii(x)](https://www.runoob.com/python3/python3-func-ascii.html") | 返回对象的 ASCII 表示，非 ASCII 字符会被转义        |

# 2. 注释

## 单行注释

```python
# 这是一个注释
**print**("Hello, World!")
# 这也是注释
```

## 多行注释

### 使用三个双/单引号

在 Python 中，多行注释是由三个单引号 **'''** 或三个双引号 **"""** 来定义的，**这种注释方式不能嵌套使用**。

```python
# wrong
'''
这是外部的多行注释
可以包含一些描述性的内容

    '''
    这是尝试嵌套的多行注释
    会导致语法错误
    '''
'''

# right

'''
这是外部的多行注释
可以包含一些描述性的内容

# 这是内部的单行注释
# 可以嵌套在多行注释中
'''

# right

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号
这是多行注释，用三个双引号
"""
```

## Docstring 文档字符串

Python 的 Docstring（文档字符串）是一种特殊的注释，用于为函数、类、模块等添加文档说明。

与普通注释不同，**Docstring 可以通过 `__doc__` 属性直接访问**，也可以使用 `help()` 函数查看。

> ## 基本语法
>
> Docstring 使用三个双引号 `"""` 或三个单引号 `'''` 包围，放在函数、类、模块的开头。

```python
def add(a, b):
  """返回两数之和"""
  return a + b

# 通过 __doc__ 属性访问
print(add.__doc__) # 输出: 返回两数之和
```

### 读取Docstring

#### 使用 help() 函数

可以查看完整Docstring

`help(add)`

#### 使用 inspect 模块提取文档

```python
import inspect # 需要 import 这个 inspect
def add(a, b):
  """返回两数之和"""
  return a + b

print(inspect.getdoc(add)) # 输出: 返回两数之和
```

## 多行 Docstring

```python
def calculate(a, b, operation="add"):
    """
    执行数学运算

    参数:
        a: 第一个数字
        b: 第二个数字
        operation: 操作类型，可选 "add", "subtract", "multiply"

    返回:
        计算结果
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        raise ValueError("不支持的操作")

# 查看完整文档
help(calculate)
```

## 类的 Docstring

```python
class Person:
  """人物类，用于表示一个人的基本信息"""

  def __init__(self, name, age):
    """
    初始化人物对象

    参数:
      name: 姓名
      age: 年龄
    """
    self.name = name
    self.age = age

  def introduce(self):
    """介绍这个人"""
    return f"我叫{self.name}，今年{self.age}岁"
```

访问类的文档

`print(Person.__doc__)`

访问方法的文档

`print(Person.introduce.__doc__)`

## Docstring 规范

Python 中有多种 Docstring 风格，常用的有：

- **Google 风格**：使用空格缩进，参数和返回值有明确的标签。
- **Sphinx/reST 风格**：使用冒号开头，如 `:param name:`。
- **NumPy 风格**：与 Google 风格类似，但格式略有不同。

# 3. 运算符

## 算术运算符

`以下假设变量 a=10，变量 b=21：`

| 运算符 | 描述                                            | 实例                      |
| :----- | :---------------------------------------------- | :------------------------ |
| +      | 加 - 两个对象相加                               | a + b 输出结果 31         |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -11        |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 210        |
| /      | 除 - x 除以 y                                   | b / a 输出结果 2.1        |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 1          |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的21次方         |
| //     | 取整除 - 往小的方向取整数                       | `>>> 9//2 4 >>> -9//2 -5` |

```python
a = 21
b = 10
c = 0

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print("6 - c 的值为：", c) # 8
```

## 比较运算符

以下假设变量 a 为 10，变量 b 为20：

| 运算符 | 描述                                                         | 实例                  |
| :----- | :----------------------------------------------------------- | :-------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。 |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 True。  |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。  |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 | (a < b) 返回 True。   |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。 |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 True。  |

## 赋值运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述                                                         | 实例                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| =      | 简单的赋值运算符                                             | c = a + b 将 a + b 的运算结果赋值为 c                        |
| +=     | 加法赋值运算符                                               | c += a 等效于 c = c + a                                      |
| -=     | 减法赋值运算符                                               | c -= a 等效于 c = c - a                                      |
| *=     | 乘法赋值运算符                                               | c *= a 等效于 c = c * a                                      |
| /=     | 除法赋值运算符                                               | c /= a 等效于 c = c / a                                      |
| %=     | 取模赋值运算符                                               | c %= a 等效于 c = c % a                                      |
| **=    | 幂赋值运算符                                                 | `c **= a 等效于 c = c ** a`                                  |
| //=    | 取整除赋值运算符                                             | c //= a 等效于 c = c // a                                    |
| :=     | 海象运算符，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。**Python3.8 版本新增运算符**。 | 在这个示例中，赋值表达式可以避免调用 len() 两次:<br />`if (n := len(a)) > 10:    print(f"List is too long ({n} elements, expected <= 10)")` |

## 逻辑运算符

Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                    |
| :----- | :--------- | :----------------------------------------------------------- | :---------------------- |
| and    | x and y    | 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。 | (a and b) 返回 20。     |
| or     | x or y     | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。      |
| not    | not x      | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

## 位运算符

| 运算符 | 描述                                                         | 实例                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
| \|     | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
| ^      | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
| ~      | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| <<     | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
| >>     | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111                  |

## 成员运算符

除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。

| 运算符 | 描述                                                    | 实例                                              |
| :----- | :------------------------------------------------------ | :------------------------------------------------ |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

```python
#!/usr/bin/python3
 
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")
```



## 身份运算符

身份运算符用于比较两个对象的存储单元

| 运算符 | 描述                                        | 实例                                                         |
| :----- | :------------------------------------------ | :----------------------------------------------------------- |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(x) != id(y)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

**注：** [id()](https://www.runoob.com/python/python-func-id.html) 函数用于获取对象内存地址。

## 运算符优先级

| 运算符                                                       | 描述                               |
| :----------------------------------------------------------- | :--------------------------------- |
| `(expressions...)`,`[expressions...]`, `{key: value...}`, `{expressions...}` | 圆括号的表达式                     |
| `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | 读取，切片，调用，属性引用         |
| await x                                                      | await 表达式                       |
| `**`                                                         | 乘方(指数)                         |
| `+x`, `-x`, `~x`                                             | 正，负，按位非 NOT                 |
| `*`, `@`, `/`, `//`, `%`                                     | 乘，矩阵乘，除，整除，取余         |
| `+`, `-`                                                     | 加和减                             |
| `<<`, `>>`                                                   | 移位                               |
| `&`                                                          | 按位与 AND                         |
| `^`                                                          | 按位异或 XOR                       |
| `|`                                                          | 按位或 OR                          |
| `in,not in, is,is not, <, <=, >, >=, !=, ==`                 | 比较运算，包括成员检测和标识号检测 |
| `not x`                                                      | 逻辑非 NOT                         |
| `and`                                                        | 逻辑与 AND                         |
| `or`                                                         | 逻辑或 OR                          |
| `if -- else`                                                 | 条件表达式                         |
| `lambda`                                                     | lambda 表达式                      |
| `:=`                                                         | 赋值表达式                         |

# 4. 数字(Number)

Python3 支持 **int、float、bool、complex（复数）**。

## 数值类型实例

| int    | float      | complex    |
| :----- | :--------- | :--------- |
| 10     | 0.0        | 3.14j      |
| 100    | 15.20      | 45.j       |
| -786   | -21.9      | 9.322e-36j |
| 0o17   | 32.3e+18   | .876j      |
| -0o112 | -90.       | -.6545+0J  |
| -0x260 | -32.54e100 | 3e+26J     |
| 0x69   | 70.2E-12   | 4.53e-7j   |

> 注意：Python 3 中整数字面量不允许前导零（如 `080`），八进制数必须使用 `0o` 前缀（如 `0o17`），十六进制使用 `0x` 前缀（如 `0x69`），二进制使用 `0b` 前缀。

Python 还支持复数，复数由实数部分和虚数部分构成，可以用 **a + bj** 或者 **complex(a, b)** 表示，复数的实部 **a** 和虚部 **b** 都是浮点型。

# 5. 字符串 String

可以被索引且下标从 0 开始，-1 为从末尾开始的位置，也可以进行截取。

**多行**

Python 中有三种常见的方式来写跨行代码：

------

## 1. 反斜杠 `\`（续行符）

告诉 Python：**这一行还没结束，下一行继续。**

```python
total = 10 + 20 + 30 + \
        40 + 50 + 60

print(total)
```

输出：

```python
210
```

再例如：

```python
name = "Tom"
age = 20

message = "My name is " + name + \
          ", I am " + str(age) + \
          " years old."

print(message)
```

输出：

```python
My name is Tom, I am 20 years old.
```

------

## 2. 圆括号 `()` 自动续行（推荐）

实际上，大多数情况下**不需要写 `\`**。

只要表达式在括号里面，就可以直接换行。

例如：

```python
total = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print(total)
```

或者：

```python
numbers = [
    1,
    2,
    3,
    4,
    5
]

print(numbers)
```

函数调用也是：

```python
print(
    "Hello",
    "Python",
    "World"
)
```

这是目前最推荐的写法，可读性最好。

------

## 3. 三引号 `"""..."""` 或 `'''...'''`

它们表示**多行字符串**。

例如：

```python
text = """
Hello
Python
World
"""

print(text)
```

输出：

```python
Hello
Python
World
```

也可以使用单引号三连：

```python
text = '''
第一行
第二行
第三行
'''

print(text)
```

输出：

```python
第一行
第二行
第三行
```

------

## 三引号常用于长文本

例如：

```python
html = """
<html>
    <body>
        <h1>Hello</h1>
    </body>
</html>
"""

print(html)
```

输出就是完整的 HTML：

```python
<html>
    <body>
        <h1>Hello</h1>
    </body>
</html>
```

------

## 注意：三引号不是代码续行

很多初学者容易误会，下面这种写法并不能把字符串拼接到一起：

```python
message = """
Hello
""" + """
World
"""

print(message)
```

输出是：

```python
Hello
World
```

这里实际上是**两个多行字符串相加**，而不是像 `\` 那样表示"代码没结束"。

------

## 三种方式对比

| 写法                     | 用途           | 是否推荐                           |
| ------------------------ | -------------- | ---------------------------------- |
| `\`                      | 代码续行       | 一般不推荐（容易遗漏或出错）       |
| `()`、`[]`、`{}`         | 自动续行       | **最推荐**                         |
| `"""..."""`、`'''...'''` | 定义多行字符串 | 适合保存长文本、SQL、HTML、JSON 等 |

**实际开发中**，你会发现：

- 写长表达式、函数调用时，几乎都使用 **括号自动续行**。
- 写长文本（如 SQL、HTML、提示词 Prompt、文档）时，使用 **三引号字符串**。
- `\` 现在已经比较少见，只在少数场景下使用。

# 6. List

## 列表可以切片（Slice）

==`列表[开始:结束)` 不包含最后一位==

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4]) # 

# [20, 30, 40]
```

```python
print(nums[:3])

# [10, 20, 30]
```

```python
print(nums[2:]) # 包含最后一位

# [30, 40, 50]
```

```python
print(nums[:]) # 全部复制
```

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)

# 输出：

# [1, 2, 3, 4, 5, 6]
```

==列表[开始:结束:步长]==

`print(letters[::2])`

`print(nums[::-1])` 步长为 -1（倒序）

**开始**：从哪里开始（默认第一个元素）

**结束**：到哪里结束（**不包含**该位置）

**步长**：每次移动几个元素（默认是 `1`，负数表示反向）

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f']

print(letters[1:5:2])

# 输出：

# ['b', 'd']

索引
0   1   2   3   4   5
a   b   c   d   e   f
    ↑       ↑
    每隔一个取一个
```

```python
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print (list[2])
print (list[2:3])
```

这两句话打印的内容其实是一样的:

```python
2.23
[2.23]
```

但注意是不同的类型，用变量接收一下：

```python
a = list[2]
b = list[2:3]
type(a) -> <class 'float'>
type(b) -> <class 'list'>
```

# 7. Tuple（元组）

无法修改

`my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2) # 避免使用 tuple 作为变量名`

```python
#!/usr/bin/python3

my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  # 避免使用 tuple 作为变量名
tinytuple = (123, 'runoob')

print(my_tuple)               # 输出完整元组
print(my_tuple[0])            # 输出第一个元素：abcd
print(my_tuple[1:3])          # 输出索引 1 和 2 的元素：(786, 2.23)
print(my_tuple[2:])           # 输出从索引 2 开始的所有元素
print(tinytuple * 2)          # 输出两次 tinytuple
print(my_tuple + tinytuple)   # 连接两个元组
```

构造包含 0 个或 1 个元素的元组比较特殊，有一些额外的语法规则：

```python
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
```

如果你想创建只有一个元素的元组，需要在元素后面添加一个逗号，以区分它是元组而不是普通的值。因为在没有逗号的情况下，Python 会将括号解释为数学运算中的括号：

```python
not_a_tuple = (42)  # 这是整数 42，不是元组
```

# 8. Set（集合）

Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

在 Python 中，集合使用大括号 **{}** 表示，元素之间用逗号 **,** 分隔。也可以使用 **set()** 函数创建集合。

> **注意：**创建一个空集合必须用 **set()** 而不是 **{}**，因为 **{}** 创建的是一个空字典。

创建格式：

```python
parame = {value01, value02, ...}
或者
set(value)
```

```python
#!/usr/bin/python3

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合（无序，重复元素会被自动去掉）

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)           # a 中的唯一字符

print(a - b)       # a 和 b 的差集（在 a 中但不在 b 中）
print(a | b)       # a 和 b 的并集（在 a 或 b 中）
print(a & b)       # a 和 b 的交集（同时在 a 和 b 中）
print(a ^ b)       # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）

{'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
Runoob 在集合中
{'b', 'c', 'a', 'r', 'd'}
{'r', 'b', 'd'}
{'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
{'c', 'a'}
{'z', 'b', 'm', 'r', 'l', 'd'}
```

列表和元组不会把相同的值合并，但是集合会把相同的合并。

```python
>>> clist = ['tom','tom','jerry']                #测试列表功能
>>> print (clist）
['tom','tom','jerry']

>>>ctuple = ('tom','tom','jerry')           #测试元组功能
>>>print(ctuple)
('tom','tom','jerry') 

>>>cset = {'tom','tom','jerry'}                #测试集合功能
>>>print(cset)
{'tom','jerry'}
```

# 9. Dictionary（字典）

字典（dictionary）是 Python 中另一个非常有用的内置数据类型。

字典是一种映射类型，用 **{}** 标识，它是一个 **键(key) : 值(value)** 的集合。键(key) 必须使用不可变类型，且在同一个字典中键必须是唯一的。

> **注意：**Python 3.7 起，字典会保持元素的**插入顺序**，不再是无序的。如果需要有序字典的特性，直接使用普通 `dict` 即可。

```python
#!/usr/bin/python3

my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 输出键为 'one' 的值
print(my_dict[2])           # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值
以上实例输出结果：

1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict_keys(['name', 'code', 'site'])
dict_values(['runoob', 1, 'www.runoob.com'])
```

# range

不是严格意义上的“基础数据类型”，但 **`range` 是 Python 内置的一种对象类型（内置类）**。

> `range` 是 Python 提供的一个**可迭代对象（iterable）类型**，专门用来表示一系列整数序列。

```python
range(stop)
range(start, stop)
range(start, stop, step)
```



# 10. 条件控制

### 条件判断关键字

| 关键字 / 函数 | 说明                                        | 示例                   |
| :------------ | :------------------------------------------ | :--------------------- |
| `if`          | 条件判断语句，当条件为 True 时执行代码块    | `if x > 0:`            |
| `elif`        | 多条件判断分支（else if）                   | `elif x == 0:`         |
| `else`        | 所有条件不满足时执行                        | `else:`                |
| `pass`        | 空语句，占位用，保证语法完整                | `if x > 0: pass`       |
| `match`       | 结构化模式匹配（Python 3.10+，类似 switch） | `match x: case 1: ...` |

```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

```python
#!/usr/bin/python3
 
var1 = 100
if var1:
    print ("1 - if 表达式条件为 true")
    print (var1)
 
var2 = 0
if var2: # bool(var2)
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")
```

```python
#!/usr/bin/python3
 
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")
```

```python
#!/usr/bin/python3 
 
# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
```

```python
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
```

```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
 
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))
```

```python
def check_permission(status):
    match status:
        case 200:
            return "OK - 请求成功"
        case 301 | 302:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 | 502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknown status - 未知状态码"
 
for code in [200, 301, 403, 500, 418]:
    print(f"状态码 {code}: {check_permission(code)}")
```

# 11. 循环语句

| 关键字 / 函数  | 说明                                 | 示例                               |
| :------------- | :----------------------------------- | :--------------------------------- |
| `for`          | 迭代循环，用于遍历序列或可迭代对象   | `for i in list:`                   |
| `while`        | 条件循环，条件为 True 时持续执行     | `while x > 0:`                     |
| `break`        | 立即终止当前循环                     | `break`                            |
| `continue`     | 跳过本次循环剩余代码，进入下一次迭代 | `continue`                         |
| `else（循环）` | 循环正常结束（未被 break）时执行     | `for i in range(3): ... else: ...` |
| `pass`         | 循环中的占位语句（空操作）           | `for i in range(5): pass`          |
| `range()`      | 生成整数序列，常与 for 循环配合使用  | `range(0, 5)`                      |
| `enumerate()`  | 遍历时同时获取索引和值               | `for i, v in enumerate(list):`     |

## while 循环

```python
while 判断条件(condition)：
    执行语句(statements)……
```

```python
#!/usr/bin/env python3
 
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
```

## while 循环使用 else 语句

```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

```python
#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

```python
flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")
```

**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。

## for 语句

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

```python
#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)
```

```python
#!/usr/bin/python3
 
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)
```

## for...else

```python
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
```

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

```python
#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

```python
>>>for i in range(0, 10, 3) :
    print(i)
 
    
0
3
6
9
>>>
```

```python
>>>for i in range(-10, -100, -30) :
    print(i)
 
    
-10
-40
-70
>>>
```

```python
>>>a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 Google
1 Baidu
2 Runoob
3 Taobao
4 QQ
>>>
```

**continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

```python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
```

```python
#!/usr/bin/python3
 
for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")
```

```python
while
│
├── var = var - 1
│
├── if
│    │
│    └── continue
│
└── print(var)

print("Good bye!") # 它已经不属于 while 循环了。等 while 全部结束之后才执行。
```

## pass 语句

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例

````python
#!/usr/bin/python3
 
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
````

# Example

**多重赋值（Multiple Assignment）** 或 **序列解包（Tuple Unpacking）**。

```python
#!/usr/bin/python3
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1 # a = 0, b = 1
while b < 10:
    print(b)
    a, b = b, a+b
```

## end 关键字

关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：

```python
#!/usr/bin/python3
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
    
# 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

# 推导式

Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。

在使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性。

Python 支持各种数据结构的推导式：

- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式
- 元组(tuple)推导式

## 列表推导式

列表推导式格式为：

```python
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

# 或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
```

- out_exp_res：列表生成元素表达式，可以是有返回值的函数。
- for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
- if condition：条件语句，可以过滤列表中不符合条件的值。

过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：

```python
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
['ALICE', 'JERRY', 'WENDY', 'SMITH']
```

计算 30 以内可以被 3 整除的整数：

```python
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

## 字典推导式

字典推导基本格式：

```python
{ key_expr: value_expr for value in collection }

# 或

{ key_expr: value_expr for value in collection if condition }
```

使用字符串及其长度创建字典：

```python
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
newdict
{'Google': 6, 'Runoob': 6, 'Taobao': 6}
```

提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：

```python
dic = {x: x**2 for x in (2, 4, 6)}
dic
{2: 4, 4: 16, 6: 36}
type(dic)
<class 'dict'>
```

## 集合推导式

集合推导式基本格式：

```python
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
```

计算数字 1,2,3 的平方数：

```python
setnew = {i**2 for i in (1,2,3)}
setnew
{1, 4, 9}
```

判断不是 abc 的字母并输出：

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'d', 'r'}
type(a)
<class 'set'>
```

## 元组推导式（生成器表达式）

元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

元组推导式基本格式：

```python
(expression for item in Sequence )
# 或
(expression for item in Sequence if conditional )
```

元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。

```python
a = (x for x in range(1,10))
a
<generator object <genexpr> at 0x7faf6ee20a50> # 返回的是生成器对象

tuple(a)    # 使用 tuple() 函数，可以直接将生成器对象转换成元组
(1, 2, 3, 4, 5, 6, 7, 8, 9)
```



# 迭代器与生成器

## 迭代器

迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：`iter()` 和  `next()`。

字符串，列表或元组对象都可用于创建迭代器：


```python
 list=[1,2,3,4]
 it = iter(list)   # 创建迭代器对象
 print (next(it))  # 输出迭代器的下一个元素
1
 print (next(it))
2
```

迭代器对象可以使用常规for语句进行遍历：

```python
#!/usr/bin/python3  
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象 
for x in it:
  print (x, end=" ")
```

执行以上程序，输出结果如下：

```python
1 2 3 4
```

也可以使用 next() 函数：

```python
#!/usr/bin/python3  
import sys         # 引入 sys 模块  
list=[1,2,3,4] 
it = iter(list)    # 创建迭代器对象  

while True:    
  try:        
    print (next(it))    
  except StopIteration:        
    sys.exit()
```

```python
1
2
3
4
```

### 创建一个迭代器

把一个类作为一个迭代器使用需要在类中实现两个方法 `__iter__()` 与 `__next__()` 。

如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 `__init__()`, 它会在对象初始化的时候执行。

`__iter__()` 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 `__next__()` 方法并通过 StopIteration 异常标识迭代的完成。

`__next__()` 方法（Python 2 里是 next()）会返回下一个迭代器对象。

创建一个返回数字的迭代器，初始值为 1，逐步递增 1：

```python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```

执行输出结果为：

```python
1
2
3
4
5
```

### StopIteration

StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

在 20 次迭代后停止执行：

```python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)
```

执行输出结果为：

```python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

------

## 生成器

在 Python 中，使用了 yield 的函数被称为生成器（generator）。

yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。

然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。

调用一个生成器函数，返回的是一个迭代器对象。

下面是一个简单的示例，展示了生成器函数的使用：

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
```

以上实例中，countdown 函数是一个生成器函数。它使用 yield 语句逐步产生从 n 到 1 的倒数数字。在每次调用 yield 语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行。

通过创建生成器对象并使用 next() 函数或 for 循环迭代生成器，我们可以逐步获取生成器函数产生的值。在这个例子中，我们首先使用 next() 函数获取前三个倒数值，然后通过 for 循环获取剩下的两个倒数值。

生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。

执行以上程序，输出结果如下：

```python
5
4
3
2
1
```

以下实例使用 yield 实现斐波那契数列：

```python
#!/usr/bin/python3
 
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```

执行以上程序，输出结果如下：

```python
0 1 1 2 3 5 8 13 21 34 55
```

# ==with==

> **`with` = 用完自动收拾现场。**

在 Python 编程中，资源管理是一个重要但容易被忽视的环节。`with` 关键字为我们提供了一种优雅的方式来处理文件操作、数据库连接等需要明确释放资源的场景。

with 是 Python 中的一个关键字，用于上下文管理协议（Context Management Protocol）。它简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）。

`with expression [as variable]:`

## with 语句的优势

`with` 语句通过上下文管理协议（Context Management Protocol）解决了这些问题：

1. **自动资源释放**：确保资源在使用后被正确关闭
2. **代码简洁**：减少样板代码
3. **异常安全**：即使在代码块中发生异常，资源也会被正确释放
4. **可读性强**：明确标识资源的作用域

## with 语句的基本语法

```python
with expression [as variable]:
  # 代码块
```

- `expression` 返回一个支持上下文管理协议的对象
- `as variable` 是可选的，用于将表达式结果赋值给变量
- 代码块执行完毕后，自动调用清理方法

### 文件操作示例

最常见的 `with` 语句应用是文件操作：

```python
with open('example.txt', 'r') as file:
  content = file.read()
  print(content)
# 文件已自动关闭
```

这段代码等价于前面的 `try-finally` 实现，但更加简洁明了。

## with 语句的工作原理

### 上下文管理协议

`with` 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：

1. `__enter__()`：进入上下文时调用，返回值赋给 `as` 后的变量
2. `__exit__()`：退出上下文时调用，处理清理工作

### 执行流程

<img src="https://www.runoob.com/wp-content/uploads/2025/06/python-with-runoob2.png" alt="img" style="zoom:50%;" />

### 异常处理机制

`__exit__()` 方法接收三个参数：

- `exc_type`：异常类型
- `exc_val`：异常值
- `exc_tb`：异常追踪信息

如果 `__exit__()` 返回 `True`，则表示异常已被处理，不会继续传播；返回 `False` 或 `None`，异常会继续向外传播。



# 函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

------

## 定义一个函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号 : 起始，并且缩进。
- return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

![img](https://www.runoob.com/wp-content/uploads/2014/05/py-tup-10-26-1.png)

------

### 语法

Python 定义函数使用 def 关键字，一般格式如下：

```python
def 函数名（参数列表）:
    函数体
```

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

```python
def hello() :
  print("Hello World!")

hello()
```

更复杂点的应用，函数中带上参数变量:

```python
#!/usr/bin/python3
 
def max(a, b):
    if a > b:
        return a
    else:
        return b
 
a = 4
b = 5
print(max(a, b))
```

```python
#!/usr/bin/python3
 
# 定义函数
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
```

## 参数传递

==在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：==

```python
a=[1,2,3]
a="Runoob"
```

以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，它仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

### python 传不可变对象

通过 id() 函数来查看内存地址变化：

```python
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)
```

以上输出结果为：

```python
4379369136
4379369136
4379369424
```

可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

### 传可变对象

可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

```python
#!/usr/bin/python3
 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
```

传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：

```python
函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
```

------

## 参数

以下是调用函数时可使用的正式参数类型：

- 必需参数
- 关键字参数
- 默认参数
- 不定长参数

### 位置参数（Positional Arguments）

```python
def add(a, b):
    print(a, b)
    
add(1, 2) # 按位置传
```

### 必需参数

必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

```python
#!/usr/bin/python3
 
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
printme()
```

以上输出结果：

```python
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
```

### 关键字参数

就可以不按位置穿参了

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

以下在函数 printme() 调用时使用参数名：

```python
#!/usr/bin/python3
 
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
```

以上输出结果：

```python
名字:  runoob
年龄:  50
```

### 默认参数

调用函数时，如果没有传递参数，则会使用默认参数。以下中如果没有传入 age 参数，则使用默认值：

```python
#!/usr/bin/python3
 
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )
```

以上输出结果：

```python
名字:  runoob
年龄:  50
------------------------
名字:  runoob
年龄:  35
```

### 不定长参数(*vartuple)

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

```python
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```python
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
```

以上输出结果：

```python
输出: 
70
(60, 50)
```

如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下：

```python
#!/usr/bin/python3
 
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
```

以上输出结果：

```python
输出:
10
输出:
70
60
50
```

### 两个星号 **

还有一种就是参数带两个星号 **基本语法如下：

```python
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了两个星号 *\* 的参数会以字典的形式导入。

```python
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```

以上输出结果：

```python
输出: 
1
{'a': 2, 'b': 3}
```

### 星号 * 单独

声明函数时，参数中星号 * 可以单独出现，例如:

```python
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：

```python
>>> def f(a,b,*,c):
...     return a+b+c
... 
>>> f(1,2,3)   # 报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(1,2,c=3) # 正常
6
>>>
```

----

所以最通用的写法就是：

```python
def wrapper(*args, **kwargs):
```

它能接收**任意数量的位置参数和关键字参数**，再通过：

```python
original_function(*args, **kwargs)
```

把参数**原封不动地转发**给原函数。这也是绝大多数 Python 装饰器都采用这种写法的原因。

------

## 匿名函数

Python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

- lambda 只是一个表达式，函数体比 def 简单很多。
- lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。

### 语法

lambda 函数的语法只包含一个语句，如下：

```python
lambda [arg1 [,arg2,.....argn]]:expression
```

设置参数 a 加上 10:

`x = lambda a : a + 10 print(x(5))`

以上输出结果：

```python
15
```

以下匿名函数设置两个参数：

```python
#!/usr/bin/python3
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
```

以上输出结果：

```python
相加后的值为 :  30
相加后的值为 :  40
```

我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。

以下将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：

```python
def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))
```

以上输出结果：

```python
22
33
```

更多匿名函数还可以参考：[Python lambda（匿名函数）](https://www.runoob.com/python3/python-lambda.html)

------

## return 语句

return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。之前的例子都没有示范如何返回数值。

```python
#!/usr/bin/python3
 
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)
```

------

## 强制位置参数

### `/` —— 前面的参数只能按位置传

Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

```python
def func(a, b, /, c):
    print(a, b, c)
```

> **a 和 b 不允许写参数名。**

正确

```python
func(1, 2, 3)
```

或者

```python
func(1, 2, c=3)
```

都可以。

错误

```python
func(a=1, b=2, c=3)
```

### `*` —— 后面的参数必须写名字

例如：

```python
def func(a, *, b):
    print(a, b)
```

这里

```python
*
```

表示：

> **后面的参数必须使用关键字。**

------

正确：

```python
func(1, b=2)
```

输出

```python
1 2
```

------

错误：

```python
func(1, 2)
```

现在来看教程里的例子：

```python
def func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

可以画成这样：

```python
        /
a  b    |   c  d    *    e  f
↑ ↑         ↑ ↑          ↑ ↑

只能位置     都可以      只能关键字
```

所以：

a、b

只能这样：

```python
func(1, 2, ...)
```

可以：

```python
func(1,2,3,4,e=5,f=6)
```

也可以：

```python
func(1,2,c=3,d=4,e=5,f=6)
```

甚至：

```python
func(1,2,3,d=4,e=5,f=6)
```

e、f

必须：

```python
e=5
f=6
```

## 函数自动触发

```python

def target_function():
    print("原函数执行")


x = target_function

x()
```

```python

def target_function():
    print("原函数执行")


x = target_function() # 自动就会输出"原函数执行"
```

# lambda（匿名函数）

Python 使用 **lambda** 来创建匿名函数。

lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。

匿名函数不需要使用 **def** 关键字定义完整函数。

lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。

**lambda 函数特点：**

- lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
- lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。

## lambda 语法格式：

```python
lambda arguments: expression
```

- `lambda`是 Python 的关键字，用于定义 lambda 函数。
- `arguments` 是参数列表，可以包含零个或多个参数，但必须在冒号(`:`)前指定。
- `expression` 是一个表达式，用于计算并返回函数的结果。

以下的 lambda 函数没有参数：

```python
some_function_name = lambda: "Hello, world!" print(f()) 
print(some_function_name())
# 输出: Hello, world!
```

以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果：

`x = lambda a : a + 10 print(x(5))`

输出结果为：15

## 多个参数

lambda 函数也可以设置多个参数，参数使用逗号 **,** 隔开：

以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果：

`x = lambda a, b : a * b print(x(5, 6))`

输出结果为：30

以下实例使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果：

`x = lambda a, b, c : a + b + c print(x(5, 6, 2))`

输出结果为：13

lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers)) 

print(squared)  

# 输出: [1, 4, 9, 16, 25]
```

下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：


```python
from functools import reduce  numbers = [1, 2, 3, 4, 5]  
# 使用 reduce() 和 lambda 函数计算乘积 
product = reduce(lambda x, y: x * y, numbers)  
print(product)  
# 输出：120
```

# 装饰器

装饰器（decorator）是 Python 中的一种高级功能，用于**在不修改原函数代码的前提下，动态扩展函数或类的功能**。

本质上，装饰器是一个函数：它接收一个函数作为参数，并返回一个新的函数（通常是对原函数的增强版本）。

装饰器通过 **@decorator_name** 语法应用在函数或方法定义之前。

Python 还提供了一些内置装饰器，例如 **@staticmethod** 和 **@classmethod**。

就像普通函数一样，装饰器本质上也是一个函数，所以它叫什么名字完全由你决定。

因为装饰器的目的就是：**把原函数包起来，再增加一些自己的逻辑。**

**常见应用场景：**

- **日志记录：**记录函数调用信息、参数和返回值
- **性能统计：**统计函数执行时间
- **权限控制：**限制函数访问权限
- **缓存：**缓存函数结果，提高性能

------

### 基本语法

装饰器的核心思想是：**用一个函数"包装"另一个函数**。

## 语法

```python
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 调用前
        print("执行前")

        result = original_function(*args, **kwargs)

        # 调用后
        print("执行后")

        return result
    return wrapper

@decorator_function # target_function = decorator_function(target_function)
def target_function():
    print("原函数执行")

# 调用 target_function() 时，实际上执行的是 wrapper()
```

```python
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("执行前")
        print(*args) # **kwargs 是负责关键字参数的饿 # args 负责 不是关键字的参数
        result = original_function(*args, **kwargs)

        print("执行后")

        return result # 为了保持原函数的行为不变 return result

    return wrapper


@decorator_function
def add(a, b):
    print(a + b)


add(3, 5)
```

**解析：**

- `decorator_function`：装饰器函数（接收原函数）
- `wrapper`：包装函数（真正被执行）
- `@decorator_function`：等价于函数替换

**等价写法：**

```python
target_function = decorator_function(target_function)
```

👉 调用 `target_function()` 时，实际上执行的是 `wrapper()`

------

### 使用装饰器

装饰器通过 **@** 语法糖应用在函数定义前：

```python
@time_logger
def target_function():
    pass
```

等价于：

```python
def target_function():
    pass

target_function = time_logger(target_function)
```

这种机制使我们可以在不修改原函数的情况下，统一添加功能（如日志、权限等）。

就像普通函数一样，装饰器本质上也是一个函数，所以它叫什么名字完全由你决定。

```python
# 打印日志
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```python
函数执行前
Hello!
函数执行后
```

- `my_decorator` 接收 `say_hello`
- `@my_decorator` 替换原函数

假设你写了：

```python
def my_decorator(func):
    print("装饰器执行")
    return func

@my_decorator
def say_hello():
    print("Hello")
```

Python 会自动转换成：

```python
def say_hello():
    print("Hello")

say_hello = my_decorator(say_hello)
```

注意这里：

```python
@my_decorator
```

其实就是：

```python
say_hello = my_decorator(say_hello)
```

可以 `return func`，也可以 `return wrapper`，取决于你想不想修改原函数的行为。

`return func`

- 返回原函数。
- **什么都没改。**
- 相当于没装饰。

`return wrapper`

- 返回包装后的函数。
- **以后调用的是 wrapper。**
- 这才是真正意义上的装饰器。

------

### 带参数的装饰器

如果原函数有参数，需要在 `wrapper` 中使用 `*args, **kwargs`：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("执行前")
        func(*args, **kwargs)
        print("执行后")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

输出：

```python
执行前
Hello, Alice!
执行后
```

**说明：**使用 `*args, **kwargs` 可以兼容任意参数函数。

------

## 带参数的装饰器（进阶）

```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

**说明：**这是"装饰器工厂"，外层函数用于接收参数。

```python
Hello!
Hello!
Hello!
```

<img src="https://www.runoob.com/wp-content/uploads/2024/03/decorators-python-2.png" alt="img" style="zoom:50%;" />

------

## 类装饰器

除了函数，装饰器也可以作用于类。

类装饰器接收一个类，并返回修改后的类或包装类。

- 增强类方法
- 控制实例化过程
- 实现单例、日志等功能

------

### 函数形式的类装饰器

```python
def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print("调用前")
            self.wrapped.display()
            print("调用后")

    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("原方法")

obj = MyClass()
obj.display()
```

```python
调用前
原方法
调用后
```

------

### 类形式的类装饰器

```python
# 单例模式
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)
```

```python
初始化
True
```

------

## 内置装饰器

常用内置装饰器：

1. **@staticmethod**：定义静态方法
2. **@classmethod**：定义类方法
3. **@property**：将方法变为属性

```python
class MyClass:
    @staticmethod
    def static_method():
        print("静态方法")

    @classmethod
    def class_method(cls):
        print(cls.__name__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```



------

## 多个装饰器的堆叠

多个装饰器在**定义阶段从下到上依次包裹函数**，**调用阶段从上到下依次执行**：

```python
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
```

最终输出：

```python
Decorator 1
Decorator 2
Hello!
```

------

## 核心总结

```python
装饰器 = 函数包装函数 + 不修改原代码扩展功能
```

- @ 语法本质是函数替换
- wrapper 才是真正执行的函数
- 推荐使用 *args, **kwargs 提高通用性
- 支持函数、类、甚至带参数的装饰器

# 数据结构

| 方法              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。        |
| list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。 |
| list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。 |
| list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
| list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） |
| list.clear()      | 移除列表中的所有项，等于del a[:]。                           |
| list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。 |
| list.count(x)     | 返回 x 在列表中出现的次数。                                  |
| list.sort()       | 对列表中的元素进行排序。                                     |
| list.reverse()    | 倒排列表中的元素。                                           |
| list.copy()       | 返回列表的浅复制，等于a[:]。                                 |
|                   |                                                              |

```python
is_empty = len(queue) == 0 **检查是否为空**

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

del a # del 删除实体变量
```

# 模块

在前面的几个章节中我们基本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。

为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。

Python 中的模块（Module）是一个包含 Python 定义和语句的文件，文件名就是模块名加上 **.py** 后缀。

模块可以包含函数、类、变量以及可执行的代码。通过模块，我们可以将代码组织成可重用的单元，便于管理和维护。

### 模块的作用

- **代码复用**：将常用的功能封装到模块中，可以在多个程序中重复使用。
- **命名空间管理**：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰。
- **代码组织**：将代码按功能划分到不同的模块中，使程序结构更清晰。

下面是一个使用 python 标准库中模块的例子。

```python
#!/usr/bin/python3
# 文件名: using_sys.py
 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')
```

执行结果如下所示：

```python
$ python using_sys.py 参数1 参数2
命令行参数如下:
using_sys.py
参数1
参数2


Python 路径为： ['/root', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages'] 
```

- 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
- 2、sys.argv 是一个包含命令行参数的列表。
- 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

------

## import 语句

想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：

```python
import module1[, module2[,... moduleN]
```

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

搜索路径时一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：

support.py 文件代码

```python
#!/usr/bin/python3
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return
```

test.py 引入 support 模块：

test.py 文件代码

```python
#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
```

以上实例输出结果：

```python
$ python3 test.py 
Hello :  Runoob
```

一个模块只会被导入一次，不管你执行了多少次 **import**。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？

这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。

### 不建议导入

Python 只是约定俗成：

```python
def _helper():
    ...
```

前面加一个 `_`。

表示：

> **这是内部函数，不建议外部使用。**

但是：

```python
from fibo import _helper
```

其实还是能导入。

## from … import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

```python
from modname import name1[, name2[, ... nameN]]
```

例如，要导入模块 fibo 的 fib 函数，使用如下语句：

```python
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

### 给模块起别名

使用 **as** 关键字为模块或函数起别名：

```python
import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root
```

------

## from … import * 语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

```python
from modname import *
```

这提供了一个简单的方法来导入一个模块中的所有项目。

不推荐，容易引起命名冲突。

------

## 深入模块

这段教程写得比较抽象，我用一个**真实项目例子**给你讲，你一下就能明白。

假设你的项目长这样：

```python
project/
│
├── main.py
├── math_util.py
└── string_util.py
```

------

### 第一句话

> **模块除了方法定义，还可以包括可执行的代码。**

什么意思？

例如：

#### math_util.py

```python
print("math_util 被加载了")

PI = 3.14

def add(a, b):
    return a + b
```

注意：

这里不仅有

```python
def add():
```

还有：

```python
print("math_util 被加载了")
```

这是**可执行代码**。

------

#### main.py

```python
import math_util

print("main 开始")
```

运行：

```python
math_util 被加载了
main 开始
```

为什么？

因为：

Python 导入模块的时候，会把模块里面的代码执行一遍。

------

### 第二句话

> **这些代码只有第一次被导入时才会被执行。**

什么意思？

例如：

```python
import math_util
import math_util
import math_util
```

输出：

```python
math_util 被加载了
```

只有一次。

因为：

Python 有模块缓存。

第一次：

```python
import math_util
```

流程：

```python
读取文件
    │
执行整个文件
    │
放入缓存(sys.modules)
```

第二次：

```python
import math_util
```

发现：

```python
缓存里面已经有了
```

直接使用。

不会再执行。

------

### 第三句话

> **每个模块有各自独立的符号表。**

这个最容易理解。

假设：

------

#### math_util.py

```python
a = 100

def test():
    print(a)
```

------

#### main.py

```python
a = 999

import math_util

print(a)

math_util.test()
```

输出：

```python
999
100
```

为什么？

因为：

```python
main.py
```

有自己的：

```python
a = 999
math_util.py
```

也有自己的：

```python
a = 100
```

互不影响。

可以画图：

```python
main.py

a = 999
```

和

```python
math_util.py

a = 100
```

是两个不同的命名空间。

所以教程说：

> 不会把其他用户的全局变量搞混。

------

### 第四句话

> **你可以通过 modname.itemname 访问模块里的东西。**

例如：

#### math_util.py

```python
PI = 3.14

def add(a, b):
    return a + b
```

------

#### main.py

```python
import math_util

print(math_util.PI)

print(math_util.add(3, 5))
```

输出：

```python
3.14
8
```

这里：

```python
math_util.PI
```

就是：

```python
模块名.变量
```

而：

```python
math_util.add()
```

就是：

```python
模块名.函数
```

和 JavaScript 很像：

```python
Math.max()
```

------

### 第五句话

> **模块可以导入其他模块。**

例如：

#### string_util.py

```python
def upper(text):
    return text.upper()
```

------

#### math_util.py

```python
import string_util

print(string_util.upper("hello"))
```

输出：

```python
HELLO
```

说明：

模块里面还能继续 import。

------

### 第六句话

> **还有一种导入的方法，可以使用 import 直接把模块内名称导入当前模块。**

这里其实是在说：

有两种 import。

------

#### 第一种

```python
import math_util
```

以后：

```python
math_util.add()
```

必须写：

```python
模块名.
```

例如：

```python
print(math_util.add(1,2))
```

------

#### 第二种

```python
from math_util import add
```

以后：

```python
add(1,2)
```

直接调用。

因为：

Python 已经把：

```python
add
```

放到当前文件里了。

------

可以画个图。

##### import

```python
main.py

math_util
      │
      ├── add()
      ├── PI
      └── test()
```

所以：

```python
math_util.add()
```

------

##### from import

```python
main.py

add()
PI
```

直接进入当前命名空间。

所以：

```python
add()
```

就可以了。

------

#### 最后总结（也是面试最常问的）

假设有：

```python
### math_util.py

PI = 3.14

def add(a,b):
    return a+b
```

##### 写法①

```python
import math_util

math_util.add(1,2)
math_util.PI
```

特点：

- 导入整个模块。
- 不容易和其他变量重名。
- **项目开发最推荐。**

------

##### 写法②

```python
from math_util import add

add(1,2)
```

特点：

- 直接导入某个函数。
- 调用更方便。
- 但是如果很多模块都有 `add()`，容易发生命名冲突。

------

所以在真实项目中，你会发现：

- **导入整个模块（`import xxx`）** 用得更多，代码更清晰，看到 `math_util.add()` 就知道这个函数来自哪个模块。
- **导入单个成员（`from xxx import add`）** 常用于特别常用、名字不容易冲突的函数或类，例如：

```python
from pathlib import Path
from datetime import datetime
from collections import Counter
```

这样使用时可以直接写：

```python
Path("demo.txt")
datetime.now()
Counter([1, 2, 2, 3])
```

代码会更加简洁。

## __name__ 属性

一个模块被另一个程序第一次引入时，其主程序将运行。

如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 **__name__** 属性来使该程序块仅在该模块自身运行时执行。

```python
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

运行输出如下：

```python
$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
>>>
```

**说明：每个模块都有一个 __name__ 属性。**

- 如果模块是被直接运行，`__name__` 的值为 `__main__`。
- 如果模块是被导入的，`__name__` 的值为模块名。

说明：**__name__** 与 **__main__** 底下是双下划线， **_ _** 是这样去掉中间的那个空格。

------

## dir() 函数

内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
```

如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir() # 得到一个当前模块中定义的属性列表
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
>>> a = 5 # 建立一个新的变量 'a'
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
>>>
>>> del a # 删除变量名a
>>>
>>> dir()
['__builtins__', '__doc__', '__name__', 'sys']
>>>
```

------

## 标准模块

Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。

| 模块名        | 功能描述                                    |
| :------------ | :------------------------------------------ |
| `math`        | 数学运算（如平方根、三角函数等）            |
| `os`          | 操作系统相关功能（如文件、目录操作）        |
| `sys`         | 系统相关的参数和函数                        |
| `random`      | 生成随机数                                  |
| `datetime`    | 处理日期和时间                              |
| `json`        | 处理 JSON 数据                              |
| `re`          | 正则表达式操作                              |
| `collections` | 提供额外的数据结构（如 defaultdict、deque） |
| `itertools`   | 提供迭代器工具                              |
| `functools`   | 高阶函数工具（如 reduce、lru_cache）        |

有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。

这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。

应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Runoob!')
Runoob!
C> 
```

------

## 包

包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。

比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。

就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。

这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。

不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。

现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。

并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。

这里给出了一种可能的包结构（在分层的文件系统中）:

```python
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。

最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。

用户可以每次只导入一个包里面的特定模块，比如:

```python
import sound.effects.echo
```

这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

还有一种导入子模块的方法是:

```python
from sound.effects import echo
```

这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

还有一种变化就是直接导入一个函数或者变量:

```python
from sound.effects.echo import echofilter
```

同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

```python
echofilter(input, output, delay=0.7, atten=4)
```

注意当使用 **from package import item** 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。

import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 **:exc:ImportError** 异常。

反之，如果使用形如 **import item.subitem.subsubitem** 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。

------

## 从一个包中导入*

| 写法                             | 含义                                                         | 推荐程度          |
| -------------------------------- | ------------------------------------------------------------ | ----------------- |
| `import sound.effects.echo`      | 导入整个模块                                                 | ⭐⭐⭐⭐⭐             |
| `from sound.effects import echo` | 导入指定模块                                                 | ⭐⭐⭐⭐⭐（最常用）   |
| `from sound.effects import *`    | 导入 `__all__` 指定的模块（若未定义 `__all__`，不会自动导入所有子模块） | ⭐（不推荐）       |
| `from . import echo`             | 导入当前包中的模块（相对导入）                               | ⭐⭐⭐（包内部常用） |
| `from .. import formats`         | 导入父包中的模块                                             | ⭐⭐⭐（包内部常用） |

```python
# __all__ 定义在对应包（Package）的 __init__.py 文件里。
sound/
│
├── __init__.py
│
└── effects/
    ├── __init__.py   ← 就是在这里定义
    ├── echo.py
    ├── surround.py
    └── reverse.py
```

```python
__all__ = [
    "effects",
    "filters"
]
```

如果我们使用 **from sound.effects import \*** 会发生什么呢？

Python 会进入文件系统，找到这个包里面所有的子模块，然后一个一个的把它们都导入进来。

但这个方法在 Windows 平台上工作的就不是非常好，==因为 Windows 是一个不区分大小写的系统==。

在 Windows 平台上，我们无法确定一个叫做 ECHO.py 的文件导入为模块是 echo 还是 Echo，或者是 ECHO。

为了解决这个问题，我们只需要提供一个精确包的索引。

导入语句遵循如下规则：如果包定义文件 **__init__.py** 存在一个叫做 **__all__** 的列表变量，那么在使用 **from package import \*** 的时候就把这个列表中的所有名字作为包内容导入。

作为包的作者，可别忘了在更新包之后保证 **__all__** 也更新了啊。

以下实例在 file:sounds/effects/__init__.py 中包含如下代码:

```python
__all__ = ["echo", "surround", "reverse"]
```

这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。

如果 **__all__** 真的没有定义，那么使用**from sound.effects import \***这种语法的时候，就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。

这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。看下这部分代码:

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

这个例子中，在执行 from...import 前，包 sound.effects 中的 echo 和 surround 模块都被导入到当前的命名空间中了。（当然如果定义了 __all__ 就更没问题了）

通常我们并不主张使用 ***** 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。

记住，使用 **from Package import specific_submodule** 这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。比如，如果模块sound.filters.vocoder 要使用包 sound.effects 中的模块 echo，你就要写成 from sound.effects import echo。

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。

包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。

这个功能并不常用，一般用来扩展包里面的模块。

# `__name__`

```python
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")
```

```python
# another_script.py

import example

example.greet()
```

- `__name__` 是一个内置变量，表示当前模块的名称。
- 当模块作为主程序运行时，`__name__` 的值是 `"__main__"`。
- 当模块被导入时，`__name__` 的值是模块的文件名。
- 使用 `if __name__ == "__main__":` 可以控制模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。

# 输入和输出

**`f-string` 已经是最推荐的字符串格式化方式**，例如：

```python
name = "Tom"
age = 18
print(f"{name} is {age} years old")
```

| 分类   | 方法/语法      | 作用                       | 示例                       |
| ------ | -------------- | -------------------------- | -------------------------- |
| 输出   | `print()`      | 输出内容                   | `print("Hello")`           |
| 输入   | `input()`      | 获取用户输入（返回 `str`） | `name = input("请输入：")` |
| 字符串 | `str()`        | 转成可读字符串             | `str(123)`                 |
| 字符串 | `repr()`       | 转成解释器表示形式         | `repr("abc")`              |
| 格式化 | `str.format()` | 新式字符串格式化           | `"{} {}".format(a, b)`     |
| 格式化 | `%`            | 旧式字符串格式化           | `"%.2f" % 3.14`            |

------

## `str.format()` 常用格式

| 写法     | 作用           | 示例                          |
| -------- | -------------- | ----------------------------- |
| `{}`     | 按顺序填充     | `"{} {}".format("A","B")`     |
| `{0}`    | 指定位置       | `"{1} {0}".format("A","B")`   |
| `{name}` | 关键字         | `"{name}".format(name="Tom")` |
| `{:.2f}` | 保留 2 位小数  | `"{:.2f}".format(3.14159)`    |
| `{:10}`  | 最小宽度 10    | `"{:10}".format("Tom")`       |
| `{:10d}` | 整数宽度 10    | `"{:10d}".format(123)`        |
| `{!s}`   | 调用 `str()`   | `"{!s}".format(obj)`          |
| `{!r}`   | 调用 `repr()`  | `"{!r}".format(obj)`          |
| `{!a}`   | 调用 `ascii()` | `"{!a}".format(obj)`          |

------

## 文件打开

| 方法          | 作用                   | 示例                   |
| ------------- | ---------------------- | ---------------------- |
| `open()`      | 打开文件               | `open("a.txt","r")`    |
| `with open()` | 推荐方式，自动关闭文件 | `with open(...) as f:` |

------

## 文件对象方法

| 方法           | 作用             |
| -------------- | ---------------- |
| `close()`      | 关闭文件         |
| `flush()`      | 刷新缓冲区       |
| `fileno()`     | 获取文件描述符   |
| `isatty()`     | 是否连接终端     |
| `read()`       | 读取内容         |
| `readline()`   | 读取一行         |
| `readlines()`  | 读取所有行       |
| `write()`      | 写入字符串       |
| `writelines()` | 写入多行         |
| `seek()`       | 移动文件指针     |
| `tell()`       | 获取当前指针位置 |
| `truncate()`   | 截断文件         |

------

## 文件打开模式

| 模式  | 含义               |
| ----- | ------------------ |
| `r`   | 只读（默认）       |
| `r+`  | 读写               |
| `w`   | 写入（覆盖）       |
| `w+`  | 读写（覆盖）       |
| `a`   | 追加写             |
| `a+`  | 追加读写           |
| `rb`  | 二进制读           |
| `wb`  | 二进制写           |
| `ab`  | 二进制追加         |
| `rb+` | 二进制读写         |
| `wb+` | 二进制读写（覆盖） |
| `ab+` | 二进制追加读写     |

------

## 指针相关

| 方法           | 作用         | 示例        |
| -------------- | ------------ | ----------- |
| `seek(offset)` | 移动指针     | `f.seek(0)` |
| `tell()`       | 当前指针位置 | `f.tell()`  |

------

## 实际开发最常用（★★★★★）

| 方法                                        | 使用频率                                     |
| ------------------------------------------- | -------------------------------------------- |
| `print()`                                   | ★★★★★                                        |
| `input()`                                   | ★★★★☆（学习阶段常用）                        |
| `str.format()`（现在很多人也会用 f-string） | ★★★★☆                                        |
| `open()`                                    | ★★★★★                                        |
| `with open()`                               | ★★★★★（推荐）                                |
| `read()`                                    | ★★★★★                                        |
| `readline()`                                | ★★★★☆                                        |
| `readlines()`                               | ★★★☆☆                                        |
| `write()`                                   | ★★★★★                                        |
| `seek()`                                    | ★★★☆☆                                        |
| `tell()`                                    | ★★★☆☆                                        |
| `close()`                                   | ★★☆☆☆（使用 `with open` 后通常无需手动调用） |

# File

# OS

# 错误和异常

作为 Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。

Python 有两种错误很容易辨认：语法错误和异常。

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

<img src="https://static.jyshare.com/images/mix/assets-py.webp" alt="img" style="zoom:50%;" />

## 语法错误

Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例

```python
\>>> **while** True **print**('Hello world')
 File "<stdin>", line 1, **in** ?
  **while** True **print**('Hello world')
          ^
SyntaxError: invalid syntax
```

这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号 **:** 。

语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

## 异常

即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

大多数的异常都不会被程序处理，都以错误信息的形式展现在这里。

异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。

错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。

## 异常处理

### try/except

异常捕捉可以使用 **try/except** 语句。

<img src="https://www.runoob.com/wp-content/uploads/2019/07/try_except.png" alt="img" style="zoom:50%;" />

以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。

```python
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
```

try 语句按照如下方式工作；

- 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
- 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
- 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
- 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

```python
except (RuntimeError, TypeError, NameError):
    pass
```

最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

### try/except...else

**try/except** 语句还有一个可选的 **else** 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

else 子句将在 try 子句没有发生任何异常的时候执行。

<img src="https://www.runoob.com/wp-content/uploads/2019/07/try_except_else.png" alt="img" style="zoom:50%;" />

以下实例在 try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句，读取文件内容：

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。

异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:

```python
>>> def this_fails():
        x = 1/0
   
>>> try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
   
Handling run-time error: int division or modulo by zero
```

### try-finally 语句

try-finally 语句无论是否发生异常都将执行最后的代码。

<img src="https://www.runoob.com/wp-content/uploads/2019/07/try_except_else_finally.png" alt="img" style="zoom:50%;" />

以下实例中 finally 语句无论异常是否发生都会执行：

```python
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')
```

------

## 抛出异常 / raise

Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：

```python
raise [Exception [, args [, traceback]]]
```

<img src="https://www.runoob.com/wp-content/uploads/2019/07/raise.png" alt="img" style="zoom:50%;" />

以下实例如果 x 大于 5 就触发异常:

```python
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```

执行以上代码会触发异常：

```python
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
Exception: x 不能大于 5。x 的值为: 10
```

raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

```python
>>> try:
        raise NameError('HiThere')  # 模拟一个异常。
    except NameError:
        print('An exception flew by!')
        raise
   
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in ?
NameError: HiThere
```

------

## 用户自定义异常

当然可以，这个例子有点抽象，我换一个更贴近实际开发的。

假设我们写一个**年龄校验**。

------

### 不使用自定义异常

```python
def check_age(age):
    if age < 0:
        raise Exception("年龄不能小于 0")

    print("年龄合法")


try:
    check_age(-5)
except Exception as e:
    print(e)
```

输出：

```python
年龄不能小于 0
```

虽然可以，但是：

> `Exception` 太宽泛了。

别人不知道这是：

- 数据库错误？
- 网络错误？
- 登录错误？
- 年龄错误？

------

###  使用自定义异常

定义一个异常：

```python
class AgeError(Exception):
    pass
```

这里：

```python
pass
```

表示：

> 我现在什么都不用加。

只是创建了一种新的异常类型。

------

然后：

```python
def check_age(age):
    if age < 0:
        raise AgeError("年龄不能小于 0")

    print("年龄合法")


try:
    check_age(-5)

except AgeError as e:
    print("捕获到年龄异常：", e)
```

输出：

```python
捕获到年龄异常： 年龄不能小于 0
```

------

###  再复杂一点（和官方例子一样）

官方例子：

```python
class MyError(Exception):

    def __init__(self, value):
        self.value = value
```

其实就是：

可以给异常保存自己的数据。

例如：

```python
class AgeError(Exception):

    def __init__(self, age):
        self.age = age
```

然后：

```python
def check_age(age):

    if age < 0:
        raise AgeError(age)
```

捕获：

```python
try:
    check_age(-10)

except AgeError as e:
    print("非法年龄：", e.age)
```

输出：

```python
非法年龄： -10
```

这里：

```python
e.age
```

就是我们自己保存进去的数据。

------

###  再完整一点

```python
class AgeError(Exception):

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"年龄 {self.age} 非法，不能小于 0"
```

然后：

```python
try:
    raise AgeError(-20)

except AgeError as e:
    print(e)
```

输出：

```python
年龄 -20 非法，不能小于 0
```

这里：

```python
print(e)
```

实际上调用的是：

```python
e.__str__()
```

所以我们可以自定义打印内容。

------

###  为什么继承 Exception？

因为：

```python
class AgeError(Exception):
```

就表示：

> **AgeError 也是一种 Exception。**

所以：

```python
try:
    raise AgeError(-10)

except Exception:
    print("捕获成功")
```

一样可以捕获。

但是：

```python
except AgeError:
```

会更精准。

------

###  实际开发最常见的写法

很多时候异常类甚至只有一行：

```python
class LoginError(Exception):
    """登录异常"""
    pass


class PermissionError(Exception):
    """权限异常"""
    pass


class OrderNotFound(Exception):
    """订单不存在"""
    pass
```

然后：

```python
raise LoginError("用户名或密码错误")

raise PermissionError("没有权限")

raise OrderNotFound("订单不存在")
```

这样别人看到异常类型就知道发生了什么，而不用全部都抛 `Exception`。

------

####  那 `__init__` 和 `__str__` 到底有什么作用？

你可以这样理解：

```python
class AgeError(Exception):

    def __init__(self, age):
        self.age = age          ###  保存数据

    def __str__(self):
        return f"年龄 {self.age} 非法"   ###  控制打印格式
```

- **`__init__`**：负责**保存异常相关的数据**（例如年龄、订单号、用户名等）。
- **`__str__`**：负责**定义这个异常打印出来是什么样子**。

如果你只是想定义一种新的异常类型，很多时候直接写：

```python
class AgeError(Exception):
    pass
```

就已经足够了。只有当异常需要携带额外信息或自定义显示内容时，才会重写 `__init__` 或 `__str__`。

------

## 预定义的清理行为

> **`with` 的核心目的不是让代码更短，而是保证资源一定会被正确释放**。这也是为什么现在几乎所有涉及文件、数据库、网络连接、锁等资源的 Python 代码，都会优先使用 `with`。

一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

下面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

```python
for line in open("myfile.txt"):
    print(line, end="")
```

以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。



# 面向对象

# 命名空间/作用域

一般有三种命名空间：

- **内置名称（built-in names**）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
- **全局名称（global names）**，模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
- **局部名称（local names）**，函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

<img src="https://www.runoob.com/wp-content/uploads/2014/05/types_namespace-1.png" alt="img" style="zoom:50%;" />

命名空间查找顺序:

假设我们要使用变量 runoob，则 Python 的查找顺序为：**局部的命名空间 -> 全局命名空间 -> 内置命名空间**。

如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:

- **全局变量**在函数外部定义，可以在整个文件中访问。
- **局部变量**在函数内部定义，只能在函数内访问。
- 使用 `global` 可以在函数中修改全局变量。
- 使用 `nonlocal` 可以在嵌套函数中修改外部函数的变量。

# 虚拟环境的创建

# 类型注解

## 复杂类型注解

`from typing import List, Dict, Tuple, Set`

List[int] 表示这是一个只包含整数的列表
`numbers: List[int] = [1, 2, 3, 4, 5]`

Dict[str, int] 表示这是一个键为字符串、值为整数的字典
`student_scores: Dict[str, int] = {"Alice": 95, "Bob": 88}`

Tuple[int, str, bool] 表示这是一个包含整数、字符串、布尔值的元组
`person_info: Tuple[int, str, bool] = (25, "Alice", True)`

Set[str] 表示这是一个只包含字符串的集合
`unique_names: Set[str] = {"Alice", "Bob", "Charlie"}`

### 可选类型（Optional）

```python
def find_student(name: str) -> Optional[str]:
    """根据名字查找学生，可能找到也可能返回None"""
    students = {"Alice": "A001", "Bob": "B002"}
    return students.get(name)  # 可能返回字符串或None

# 等价于 Union[str, None]
```

### 联合类型（Union）

```python
from typing import Union

def process_input(data: Union[str, int, List[int]]) -> None:
    """处理可能是字符串、整数或整数列表的输入"""
    if isinstance(data, str):
        print(f"字符串: {data}")
    elif isinstance(data, int):
        print(f"整数: {data}")
    elif isinstance(data, list):
        print(f"列表: {data}")

process_input("hello")    # 输出：字符串: hello
process_input(42)         # 输出：整数: 42  
process_input([1, 2, 3])  # 输出：列表: [1, 2, 3]
```

使用 Mypy 进行静态类型检查

# 标准库概览

https://docs.python.org/zh-cn/3/library/index.html

------

# 内置核心能力

## 内置函数

Python 提供了大量**内置函数（Built-in Functions）**，无需导入任何库即可直接使用。 这些函数覆盖了**数据类型转换、数学计算、迭代操作、反射机制**等常见场景，是每个 Python 初学者必须掌握的基础工具。

- **数值计算：**`abs()`、`round()`、`min()`、`max()`、`sum()`
- **类型转换：**`int()`、`float()`、`str()`、`list()`、`tuple()`
- **迭代与函数式：**code>map()、`filter()`、`zip()`、`enumerate()`
- **反射与对象：**`type()`、`isinstance()`、`getattr()`、`setattr()`
- **输入输出：**`print()`、`input()`、`open()`

```python
# 求和
sum([1, 2, 3])  # 6

# 最大值
max([3, 6, 2])  # 6

# 类型转换
int("123")      # 123

# 枚举
for i, v in enumerate(['a', 'b']):
    print(i, v)

# map
list(map(lambda x: x * 2, [1,2,3]))  # [2,4,6]

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

account_balance = '12'

isinstance(account_balance, int) # False

account_balance = 12
isinstance(account_balance, (int, float)) # true
```

|                           内置函数                           |                                                              |                                                              |                                                              |                                                              |
| :----------------------------------------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [abs()](https://www.runoob.com/python3/python3-func-number-abs.html) | [dict()](https://www.runoob.com/python3/python3-func-dict.html) | [help()](https://www.runoob.com/python3/python3-func-help.html) | [min()](https://www.runoob.com/python3/python3-func-number-min.html) | [setattr()](https://www.runoob.com/python3/python3-func-setattr.html) |
| [all()](https://www.runoob.com/python3/python3-func-all.html) | [dir()](https://www.runoob.com/python3/python3-func-dir.html) | [hex()](https://www.runoob.com/python3/python3-func-hex.html) | [next()](https://www.runoob.com/python3/python3-func-next.html) | [slice()](https://www.runoob.com/python3/python3-func-slice.html) |
| [any()](https://www.runoob.com/python3/python3-func-any.html) | [divmod()](https://www.runoob.com/python3/python3-func-divmod.html) | [id()](https://www.runoob.com/python3/python3-func-id.html)  | [object()](https://www.runoob.com/python3/python-func-object.html) | [sorted()](https://www.runoob.com/python3/python3-func-sorted.html) |
| [ascii()](https://www.runoob.com/python3/python3-func-ascii.html) | [enumerate()](https://www.runoob.com/python3/python3-func-enumerate.html) | [input()](https://www.runoob.com/python/python3-func-input.html) | [oct()](https://www.runoob.com/python/python3-func-oct.html) | [staticmethod()](https://www.runoob.com/python3/python3-func-staticmethod.html) |
| [bin()](https://www.runoob.com/python3/python3-func-bin.html) | [eval()](https://www.runoob.com/python3/python3-func-eval.html) | [int()](https://www.runoob.com/python3/python3-func-int.html) | [open()](https://www.runoob.com/python3/python3-func-open.html) | [str()](https://www.runoob.com/python3/python3-func-str.html) |
| [bool()](https://www.runoob.com/python3/python3-func-bool.html) | [exec()](https://www.runoob.com/python3/python3-func-exec.html) | [isinstance()](https://www.runoob.com/python3/python3-func-isinstance.html) | [ord()](https://www.runoob.com/python3/python3-func-ord.html) | [sum()](https://www.runoob.com/python3/python3-func-sum.html) |
| [bytearray()](https://www.runoob.com/python3/python3-func-bytearray.html) | [filter()](https://www.runoob.com/python3/python3-func-filter.html) | [issubclass()](https://www.runoob.com/python3/python3-func-issubclass.html) | [pow()](https://www.runoob.com/python3/python3-func-number-pow.html) | [super()](https://www.runoob.com/python3/python3-func-super.html) |
| [bytes()](https://www.runoob.com/python3/python3-func-bytes.html) | [float()](https://www.runoob.com/python3/python3-func-float.html) | [iter()](https://www.runoob.com/python3/python3-func-iter.html) | [print()](https://www.runoob.com/python3/python3-func-print.html) | [tuple()](https://www.runoob.com/python3/python3-func-tuple.html) |
| [callable()](https://www.runoob.com/python3/python3-func-callable.html) | [format()](https://www.runoob.com/python/att-string-format.html) | [len()](https://www.runoob.com/python3/python3-string-len.html) | [property()](https://www.runoob.com/python3/python3-func-property.html) | [type()](https://www.runoob.com/python3/python3-func-type.html) |
| [chr()](https://www.runoob.com/python3/python3-func-chr.html) | [frozenset()](https://www.runoob.com/python3/python3-func-frozenset.html) | [list()](https://www.runoob.com/python3/python3-att-list-list.html) | [range()](https://www.runoob.com/python3/python3-func-range.html) | [vars()](https://www.runoob.com/python3/python3-func-vars.html) |
| [classmethod()](https://www.runoob.com/python3/python3-func-classmethod.html) | [getattr()](https://www.runoob.com/python3/python3-func-getattr.html) | [locals()](https://www.runoob.com/python3/python3-func-locals.html) | [repr()](https://www.runoob.com/python3/python3-func-repr.html) | [zip()](https://www.runoob.com/python3/python3-func-zip.html) |
| [compile()](https://www.runoob.com/python3/python3-func-compile.html) | [globals()](https://www.runoob.com/python3/python3-func-globals.html) | [map()](https://www.runoob.com/python/python3-func-map.html) | [reversed()](https://www.runoob.com/python3/python3-func-reversed.html) | [__import__()](https://www.runoob.com/python3/python3-func-__import__.html) |
| [complex()](https://www.runoob.com/python3/python3-func-complex.html) | [hasattr()](https://www.runoob.com/python3/python3-func-hasattr.html) | [max()](https://www.runoob.com/python3/python3-func-number-max.html) | [round()](https://www.runoob.com/python3/python3-func-number-round.html) | [reload()](https://www.runoob.com/python3/python3-func-reload.html) |
| [delattr()](https://www.runoob.com/python3/python3-func-delattr.html) | [hash()](https://www.runoob.com/python3/python3-func-hash.html) | [memoryview()](https://www.runoob.com/python3/python3-func-memoryview.html) | [set()](https://www.runoob.com/python3/python3-func-set.html) |                                                              |



## math 模块

**Python math 模块**提供了大量常用数学函数，可用于完成：

- 三角函数计算（sin / cos / tan）
- 对数与指数运算（log / exp / pow）
- 取整与舍入（ceil / floor / trunc）
- 组合排列与阶乘（comb / perm / factorial）
- 距离与几何计算（dist / hypot / sqrt）

https://www.runoob.com/python3/python-math.html

## random 模块

```python
# 导入 random 包
import random

# 生成随机数
print(random.random())
```

```python
#!/usr/bin/python3
import random

random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
```

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [seed()](https://www.runoob.com/python3/python3-func-number-seed.html) | 初始化随机数生成器                                           |
| getstate()                                                   | 返回捕获生成器当前内部状态的对象。                           |
| setstate()                                                   | state 应该是从之前调用 getstate() 获得的，并且 setstate() 将生成器的内部状态恢复到 getstate() 被调用时的状态。 |
| getrandbits(k)                                               | 返回具有 k 个随机比特位的非负 Python 整数。 此方法随 MersenneTwister 生成器一起提供，其他一些生成器也可能将其作为 API 的可选部分提供。 在可能的情况下，getrandbits() 会启用 randrange() 来处理任意大的区间。 |
| [randrange()](https://www.runoob.com/python3/ref-random-randrange.html) | 从 range(start, stop, step) 返回一个随机选择的元素。         |
| [randint(a, b)](https://www.runoob.com/python3/ref-random-randint.html) | 返回随机整数 N 满足 a <= N <= b。                            |
| [choice(seq)](https://www.runoob.com/python3/python3-func-number-choice.html) | 从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError。 |
| choices(population, weights=None, *, cum_weights=None, k=1)  | 从 population 中选择替换，返回大小为 k 的元素列表。 如果 population 为空，则引发 IndexError。 |
| [shuffle(x[, random\])](https://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列 x 随机打乱位置。                                      |
| sample(population, k, *, counts=None)                        | 返回从总体序列或集合中选择的唯一元素的 k 长度列表。 用于无重复的随机抽样。 |
| [random()](https://www.runoob.com/python3/python3-func-number-random.html) | 返回 [0.0, 1.0) 范围内的下一个随机浮点数。                   |
| [uniform()](https://www.runoob.com/python3/python3-func-number-uniform.html) | 返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。 |
| triangular(low, high, mode)                                  | 返回一个随机浮点数 N ，使得 low <= N <= high 并在这些边界之间使用指定的 mode 。 low 和 high 边界默认为零和一。 mode 参数默认为边界之间的中点，给出对称分布。 |
| betavariate(alpha, beta)                                     | Beta 分布。 参数的条件是 alpha > 0 和 beta > 0。 返回值的范围介于 0 和 1 之间。 |
| expovariate(lambd)                                           | 指数分布。 lambd 是 1.0 除以所需的平均值，它应该是非零的。   |
| gammavariate()                                               | Gamma 分布（ 不是伽马函数） 参数的条件是 alpha > 0 和 beta > 0。 |
| gauss(mu, sigma)                                             | 正态分布，也称高斯分布。 mu 为平均值，而 sigma 为标准差。 此函数要稍快于下面所定义的 normalvariate() 函数。 |
| lognormvariate(mu, sigma)                                    | 对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。 |
| normalvariate(mu, sigma)                                     | 正态分布。 mu 是平均值，sigma 是标准差。                     |
| vonmisesvariate(mu, kappa)                                   | 冯·米塞斯分布。 mu 是平均角度，以弧度表示，介于0和 2*pi 之间，kappa 是浓度参数，必须大于或等于零。 如果 kappa 等于零，则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。 |
| paretovariate(alpha)                                         | 帕累托分布。 alpha 是形状参数。                              |
| weibullvariate(alpha, beta)                                  | 威布尔分布。 alpha 是比例参数，beta 是形状参数。             |

## sys 模块

`sys` 是 Python 标准库中的一个模块，提供了与 Python 解释器及其环境交互的功能。

通过 `sys` 库，你可以访问与 Python 解释器相关的变量和函数，例如命令行参数、标准输入输出、程序退出等。

```python
import sys

# 列出 os 模块的所有属性和方法
print(dir(os))
```

### sys 模块常用属性

| 属性             | 说明                                                    |
| :--------------- | :------------------------------------------------------ |
| `sys.argv`       | 命令行参数列表，`sys.argv[0]` 是脚本名称                |
| `sys.path`       | Python 模块搜索路径（`PYTHONPATH`）                     |
| `sys.modules`    | 已加载模块的字典                                        |
| `sys.platform`   | 操作系统平台标识（如 `'win32'`, `'linux'`, `'darwin'`） |
| `sys.version`    | Python 解释器版本信息                                   |
| `sys.executable` | Python 解释器的绝对路径                                 |
| `sys.stdin`      | 标准输入流（文件对象）                                  |
| `sys.stdout`     | 标准输出流（文件对象）                                  |
| `sys.stderr`     | 标准错误流（文件对象）                                  |
| `sys.byteorder`  | 字节序（`'little'` 或 `'big'`）                         |
| `sys.maxsize`    | 最大整数值（`2**31-1` 或 `2**63-1`）                    |

------

### sys 模块常用方法

| 方法                           | 说明                                           |
| :----------------------------- | :--------------------------------------------- |
| `sys.exit([status])`           | 退出程序，`status=0` 表示正常退出              |
| `sys.getsizeof(obj)`           | 返回对象占用的内存字节数                       |
| `sys.getdefaultencoding()`     | 获取默认字符串编码（通常 `'utf-8'`）           |
| `sys.setrecursionlimit(limit)` | 设置递归深度限制（默认 `1000`）                |
| `sys.getrecursionlimit()`      | 获取当前递归深度限制                           |
| `sys.getrefcount(obj)`         | 返回对象的引用计数                             |
| `sys.exc_info()`               | 获取当前异常信息（`(type, value, traceback)`） |
| `sys.settrace(tracefunc)`      | 设置调试跟踪函数                               |
| `sys.setprofile(profilefunc)`  | 设置性能分析函数                               |

### operator 模块

比较两个列表、数字或字符串等的大小关系。

| 运算         | 语法                | 函数                                |
| :----------- | :------------------ | :---------------------------------- |
| 加法         | `a + b`             | `add(a, b)`                         |
| 字符串拼接   | `seq1 + seq2`       | `concat(seq1, seq2)`                |
| 包含测试     | `obj in seq`        | `contains(seq, obj)`                |
| 除法         | `a / b`             | `truediv(a, b)`                     |
| 除法         | `a // b`            | `floordiv(a, b)`                    |
| 按位与       | `a & b`             | `and_(a, b)`                        |
| 按位异或     | `a ^ b`             | `xor(a, b)`                         |
| 按位取反     | `~ a`               | `invert(a)`                         |
| 按位或       | `a | b`             | `or_(a, b)`                         |
| 取幂         | `a ** b`            | `pow(a, b)`                         |
| 标识         | `a is b`            | `is_(a, b)`                         |
| 标识         | `a is not b`        | `is_not(a, b)`                      |
| 索引赋值     | `obj[k] = v`        | `setitem(obj, k, v)`                |
| 索引删除     | `del obj[k]`        | `delitem(obj, k)`                   |
| 索引取值     | `obj[k]`            | `getitem(obj, k)`                   |
| 左移         | `a << b`            | `lshift(a, b)`                      |
| 取模         | `a % b`             | `mod(a, b)`                         |
| 乘法         | `a * b`             | `mul(a, b)`                         |
| 矩阵乘法     | `a @ b`             | `matmul(a, b)`                      |
| 取反（算术） | `- a`               | `neg(a)`                            |
| 取反（逻辑） | `not a`             | `not_(a)`                           |
| 正数         | `+ a`               | `pos(a)`                            |
| 右移         | `a >> b`            | `rshift(a, b)`                      |
| 切片赋值     | `seq[i:j] = values` | `setitem(seq, slice(i, j), values)` |
| 切片删除     | `del seq[i:j]`      | `delitem(seq, slice(i, j))`         |
| 切片取值     | `seq[i:j]`          | `getitem(seq, slice(i, j))`         |
| 字符串格式化 | `s % obj`           | `mod(s, obj)`                       |
| 减法         | `a - b`             | `sub(a, b)`                         |
| 真值测试     | `obj`               | `truth(obj)`                        |
| 比较         | `a < b`             | `lt(a, b)`                          |
| 比较         | `a <= b`            | `le(a, b)`                          |
| 相等         | `a == b`            | `eq(a, b)`                          |
| 不等         | `a != b`            | `ne(a, b)`                          |
| 比较         | `a >= b`            | `ge(a, b)`                          |
| 比较         | `a > b`             | `gt(a, b)`                          |

```python
# Python 实例
# add(), sub(), mul()
  
# 导入  operator 模块
import operator
  
# 初始化变量
a = 4
  
b = 3
  
# 使用 add() 让两个值相加
print ("add() 运算结果 :",end="");
print (operator.add(a, b))
  
# 使用 sub() 让两个值相减
print ("sub() 运算结果 :",end="");
print (operator.sub(a, b))
  
# 使用 mul() 让两个值相乘
print ("mul() 运算结果 :",end="");
print (operator.mul(a, b))
```

# 文件 / 数据处理

## JSON 数据解析

- **json.dumps():** 对数据进行编码。
- **json.loads():** 对数据进行解码。

### Python 编码为 JSON 类型转换对应表：

| Python                                 | JSON   |
| :------------------------------------- | :----- |
| dict                                   | object |
| list, tuple                            | array  |
| str                                    | string |
| int, float, int- & float-derived Enums | number |
| True                                   | true   |
| False                                  | false  |
| None                                   | null   |

### JSON 解码为 Python 类型转换对应表：

| JSON          | Python |
| :------------ | :----- |
| object        | dict   |
| array         | list   |
| string        | str    |
| number (int)  | int    |
| number (real) | float  |
| true          | True   |
| false         | False  |
| null          | None   |

```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'https://www.runoob.com'
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
```

```python
Python 原始数据： {'no': 1, 'name': 'Runoob', 'url': 'https://www.runoob.com'}
JSON 对象： {"no": 1, "name": "Runoob", "url": "https://www.runoob.com"}
```

https://docs.python.org/3/library/json.html

## csv 模块

CSV（Comma-Separated Values）文件是一种常见的文件格式，用于存储表格数据。

CSV 文件由纯文本组成，每一行代表表格中的一行数据，而每一列则通过逗号（或其他分隔符）分隔。

CSV 文件通常用于数据交换，因为它简单且易于处理。

Python 提供了一个内置的 `csv` 模块，用于读取和写入 CSV 文件。这个模块简化了处理 CSV 文件的过程，使得开发者可以轻松地操作表格数据。

### 1. 读取 CSV 文件

要读取 CSV 文件，可以使用 `csv.reader` 对象。以下是一个简单的示例：

```python
import csv

# 打开 CSV 文件
with open('data.csv', mode='r', encoding='utf-8') as file:
    # 创建 csv.reader 对象
    csv_reader = csv.reader(file)
    
    # 逐行读取数据
    for row in csv_reader:
        print(row)
```

代码解释：

- `open('data.csv', mode='r', encoding='utf-8')`：以只读模式打开名为 `data.csv` 的文件，并指定编码为 UTF-8。
- `csv.reader(file)`：创建一个 `csv.reader` 对象，用于读取文件内容。
- `for row in csv_reader`：逐行读取文件内容，每一行数据会被解析为一个列表。

------

### 2. 写入 CSV 文件

要写入 CSV 文件，可以使用 `csv.writer` 对象。以下是一个示例：

```python
import csv

# 要写入的数据
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

# 打开 CSV 文件
with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    # 创建 csv.writer 对象
    csv_writer = csv.writer(file)
    
    # 写入数据
    for row in data:
        csv_writer.writerow(row)
```

代码解释：

- `open('output.csv', mode='w', encoding='utf-8', newline='')`：以写入模式打开名为 `output.csv` 的文件，并指定编码为 UTF-8。`newline=''` 用于避免在 Windows 系统中出现空行。
- `csv.writer(file)`：创建一个 `csv.writer` 对象，用于写入文件内容。
- `csv_writer.writerow(row)`：将每一行数据写入文件。

------

### 3. 使用字典读取和写入 CSV 文件

`csv` 模块还提供了 `DictReader` 和 `DictWriter` 类，它们可以将 CSV 文件的每一行解析为字典，或者将字典写入 CSV 文件。

#### 使用 `DictReader` 读取 CSV 文件：

```python
import csv

with open('data.csv', mode='r', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)
    
    for row in csv_dict_reader:
        print(row)
```

#### 使用 `DictWriter` 写入 CSV 文件：

```python
import csv

data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # 写入表头
    csv_dict_writer.writeheader()
    
    # 写入数据
    for row in data:
        csv_dict_writer.writerow(row)
```

------

### 常用的属性和方法

#### csv 模块核心方法

| 方法                           | 说明                                | 示例                                               |
| :----------------------------- | :---------------------------------- | :------------------------------------------------- |
| **`csv.reader()`**             | 从文件对象读取 CSV 数据             | `reader = csv.reader(file)`                        |
| **`csv.writer()`**             | 将数据写入 CSV 文件                 | `writer = csv.writer(file)`                        |
| **`csv.DictReader()`**         | 将 CSV 行读取为字典（带表头）       | `dict_reader = csv.DictReader(file)`               |
| **`csv.DictWriter()`**         | 将字典写入 CSV 文件（需指定字段名） | `dict_writer = csv.DictWriter(file, fieldnames)`   |
| **`csv.register_dialect()`**   | 注册自定义 CSV 格式（如分隔符）     | `csv.register_dialect('mydialect', delimiter='|')` |
| **`csv.unregister_dialect()`** | 删除已注册的方言                    | `csv.unregister_dialect('mydialect')`              |
| **`csv.list_dialects()`**      | 列出所有已注册的方言                | `print(csv.list_dialects())`                       |

#### csv.reader 和 csv.writer 对象常用方法

| 方法                  | 说明                                | 适用对象 |
| :-------------------- | :---------------------------------- | :------- |
| **`__next__()`**      | 迭代读取下一行（或使用 `for` 循环） | `reader` |
| **`writerow(row)`**   | 写入单行数据                        | `writer` |
| **`writerows(rows)`** | 写入多行数据（列表的列表）          | `writer` |

#### csv.DictReader 和 csv.DictWriter 对象特性

| 特性/方法           | 说明                                      | 示例                        |
| :------------------ | :---------------------------------------- | :-------------------------- |
| **`fieldnames`**    | 字段名列表（`DictReader` 自动从首行获取） | `dict_reader.fieldnames`    |
| **`writeheader()`** | 写入表头行（`DictWriter` 专用）           | `dict_writer.writeheader()` |

#### 常用参数说明

| 参数               | 说明                     | 示例值                      | 适用方法        |
| :----------------- | :----------------------- | :-------------------------- | :-------------- |
| `delimiter`        | 字段分隔符               | `','`（默认）, `'\t'`       | `reader/writer` |
| `quotechar`        | 引用字符（包围特殊字段） | `'"'`（默认）               | `reader/writer` |
| `quoting`          | 引用规则                 | `csv.QUOTE_ALL`（全部引用） | `reader/writer` |
| `skipinitialspace` | 忽略分隔符后的空格       | `True`/`False`              | `reader`        |
| `lineterminator`   | 行结束符                 | `'\r\n'`（默认）            | `writer`        |
| `dialect`          | 预定义的方言名称         | `'excel'`（默认）           | 所有方法        |

## 日期和时间

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳, 

```python
#!/usr/bin/python3

import time  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)
```

### time 模块

| 序号 | 属性及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | **time.timezone** 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。 |
| 2    | **time.tzname** 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。 |

| 方法                              | 解释                                         | 例子                                                   |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------------ |
| `time.altzone`                    | 返回夏令时地区相对 UTC 的偏移秒数。          | `print(time.altzone)`                                  |
| `time.asctime([tupletime])`       | 把时间元组转成可读字符串。                   | `time.asctime(time.localtime())`                       |
| `time.clock()`                    | 已废弃，Python 3.8 已移除。                  | 用 `time.perf_counter()` 或 `time.process_time()` 替代 |
| `time.ctime([secs])`              | 把时间戳转成可读字符串。                     | `time.ctime()`                                         |
| `time.gmtime([secs])`             | 把时间戳转成 UTC 时间元组。                  | `time.gmtime(time.time())`                             |
| `time.localtime([secs])`          | 把时间戳转成本地时间元组。                   | `time.localtime(time.time())`                          |
| `time.mktime(tupletime)`          | 把本地时间元组转成时间戳。                   | `time.mktime(time.localtime())`                        |
| `time.sleep(secs)`                | 让程序暂停指定秒数。                         | `time.sleep(5)`                                        |
| `time.strftime(fmt[, tupletime])` | 把时间元组格式化成字符串。                   | `time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())` |
| `time.strptime(str, fmt)`         | 把时间字符串解析成时间元组。                 | `time.strptime("2026-07-06", "%Y-%m-%d")`              |
| `time.time()`                     | 返回当前时间戳。                             | `time.time()`                                          |
| `time.tzset()`                    | 根据环境变量 `TZ` 重新设置时区。             | `time.tzset()`                                         |
| `time.perf_counter()`             | 高精度计时，适合统计代码耗时，包含睡眠时间。 | `start = time.perf_counter()`                          |
| `time.process_time()`             | 统计当前进程 CPU 执行时间，不包含睡眠时间。  | `start = time.process_time()`                          |

### datetime模块

#### **1. 核心类**

| 类                       | 说明                            | 示例                            |
| :----------------------- | :------------------------------ | :------------------------------ |
| **`datetime.date`**      | 日期类（年、月、日）            | `date(2023, 5, 15)`             |
| **`datetime.time`**      | 时间类（时、分、秒、微秒）      | `time(14, 30, 0)`               |
| **`datetime.datetime`**  | 日期时间类（包含日期和时间）    | `datetime(2023, 5, 15, 14, 30)` |
| **`datetime.timedelta`** | 时间间隔类（用于日期/时间计算） | `timedelta(days=5)`             |
| **`datetime.tzinfo`**    | 时区信息基类（需子类化实现）    | 自定义时区类                    |

#### **2. `date` 对象常用方法/属性**

| 方法/属性                     | 说明                           | 示例                                      |
| :---------------------------- | :----------------------------- | :---------------------------------------- |
| **`date.today()`**            | 返回当前本地日期               | `date.today()` → `date(2023, 5, 15)`      |
| **`date.fromisoformat(str)`** | 从 `YYYY-MM-DD` 字符串解析日期 | `date.fromisoformat("2023-05-15")`        |
| **`date.year`**               | 年份（只读）                   | `d.year` → `2023`                         |
| **`date.month`**              | 月份（1-12，只读）             | `d.month` → `5`                           |
| **`date.day`**                | 日（1-31，只读）               | `d.day` → `15`                            |
| **`date.weekday()`**          | 返回星期几（0=周一，6=周日）   | `d.weekday()` → `0`                       |
| **`date.isoformat()`**        | 返回 `YYYY-MM-DD` 格式字符串   | `d.isoformat()` → `"2023-05-15"`          |
| **`date.strftime(format)`**   | 自定义格式化输出               | `d.strftime("%Y/%m/%d")` → `"2023/05/15"` |

#### **3. `time` 对象常用方法/属性**

| 方法/属性                   | 说明                              | 示例                              |
| :-------------------------- | :-------------------------------- | :-------------------------------- |
| **`time.hour`**             | 小时（0-23，只读）                | `t.hour` → `14`                   |
| **`time.minute`**           | 分钟（0-59，只读）                | `t.minute` → `30`                 |
| **`time.second`**           | 秒（0-59，只读）                  | `t.second` → `0`                  |
| **`time.microsecond`**      | 微秒（0-999999，只读）            | `t.microsecond` → `0`             |
| **`time.isoformat()`**      | 返回 `HH:MM:SS.mmmmmm` 格式字符串 | `t.isoformat()` → `"14:30:00"`    |
| **`time.strftime(format)`** | 自定义格式化输出                  | `t.strftime("%H:%M")` → `"14:30"` |

#### **4. `datetime` 对象常用方法/属性**

| 方法/属性                        | 说明                         | 示例                                                   |
| :------------------------------- | :--------------------------- | :----------------------------------------------------- |
| **`datetime.now()`**             | 返回当前本地日期时间         | `datetime.now()` → `datetime(2023, 5, 15, 14, 30, 0)`  |
| **`datetime.utcnow()`**          | 返回当前 UTC 日期时间        | `datetime.utcnow()`                                    |
| **`datetime.fromtimestamp(ts)`** | 从时间戳创建 `datetime` 对象 | `datetime.fromtimestamp(1684146600)`                   |
| **`datetime.timestamp()`**       | 返回时间戳（浮点数秒）       | `dt.timestamp()` → `1684146600.0`                      |
| **`datetime.date()`**            | 提取日期部分                 | `dt.date()` → `date(2023, 5, 15)`                      |
| **`datetime.time()`**            | 提取时间部分                 | `dt.time()` → `time(14, 30)`                           |
| **`datetime.year`**              | 年份（同 `date`）            | `dt.year` → `2023`                                     |
| **`datetime.strftime(format)`**  | 自定义格式化输出             | `dt.strftime("%Y-%m-%d %H:%M")` → `"2023-05-15 14:30"` |

#### **5. `timedelta` 对象常用属性**

| 属性               | 说明               | 示例                              |
| :----------------- | :----------------- | :-------------------------------- |
| **`days`**         | 天数（可正可负）   | `delta.days` → `5`                |
| **`seconds`**      | 秒数（0-86399）    | `delta.seconds` → `3600`（1小时） |
| **`microseconds`** | 微秒数（0-999999） | `delta.microseconds` → `0`        |

#### **6. 常用格式化符号（`strftime`）**

| 符号 | 说明                  | 示例输出 |
| :--- | :-------------------- | :------- |
| `%Y` | 四位年份              | `2023`   |
| `%m` | 两位月份（01-12）     | `05`     |
| `%d` | 两位日（01-31）       | `15`     |
| `%H` | 24小时制小时（00-23） | `14`     |
| `%M` | 分钟（00-59）         | `30`     |
| `%S` | 秒（00-59）           | `00`     |
| `%A` | 完整星期名            | `Monday` |
| `%a` | 缩写星期名            | `Mon`    |
| `%B` | 完整月份名            | `May`    |
| `%b` | 缩写月份名            | `May`    |

### 日历（Calendar）模块

| 序号 | 函数及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | **calendar.calendar(year,w=2,l=1,c=6)** 返回一个多行字符串格式的 year 年年历，3 个月一行，间隔距离为 c。 每日宽度间隔为w字符。每行长度为 **21\* W+18+2\* C**。**l** 是每星期行数。 |
| 2    | **calendar.firstweekday( )** 返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。 |
| 3    | **calendar.isleap(year)** 是闰年返回 True，否则为 False。`>>> import calendar >>> print(calendar.isleap(2000)) True >>> print(calendar.isleap(1900)) False` |
| 4    | **calendar.leapdays(y1,y2)** 返回在Y1，Y2两年之间的闰年总数。 |
| 5    | **calendar.month(year,month,w=2,l=1)** 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。 |
| 6    | **calendar.monthcalendar(year,month)** 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。 |
| 7    | **calendar.monthrange(year,month)** 返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。`>>> import calendar >>> calendar.monthrange(2014, 11) (5, 30)`(5, 30)解释：5 表示 2014 年 11 月份的第一天是周六，30 表示 2014 年 11 月份总共有 30 天。 |
| 8    | **calendar.prcal(year, w=0, l=0, c=6, m=3)** 相当于 print (calendar.calendar(year, w=0, l=0, c=6, m=3))。 |
| 9    | **calendar.prmonth(theyear, themonth, w=0, l=0)** 相当于 **print(calendar.month(theyear, themonth, w=0, l=0))**。 |
| 10   | **calendar.setfirstweekday(weekday)** 设置每周的起始日期码。0（星期一）到6（星期日）。 |
| 11   | **calendar.timegm(tupletime)** 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。 |
| 12   | **calendar.weekday(year,month,day)** 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。 |

# 字符串核心能力

## re 模块 / 正则表达式

https://www.runoob.com/python3/python3-reg-expressions.html

https://www.runoob.com/python3/python-re.html

# 网络 & HTTP

## urllib

Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。

urllib 包 包含以下几个模块：

- **urllib.request** - 打开和读取 URL。
- **urllib.error** - 包含 urllib.request 抛出的异常。
- **urllib.parse** - 解析 URL。
- **urllib.robotparser** - 解析 robots.txt 文件。

Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。

本文主要介绍 Python3 的 urllib。

urllib 包 包含以下几个模块：

- **urllib.request** - 打开和读取 URL。
- **urllib.error** - 包含 urllib.request 抛出的异常。
- **urllib.parse** - 解析 URL。
- **urllib.robotparser** - 解析 robots.txt 文件。

![img](https://www.runoob.com/wp-content/uploads/2021/04/ulrib-py3.svg)

------

### urllib.request

urllib.request 定义了一些打开 URL 的函数和类，包含授权验证、重定向、浏览器 cookies等。

urllib.request 可以模拟浏览器的一个请求发起过程。

我们可以使用 urllib.request 的 urlopen 方法来打开一个 URL，语法格式如下：

```python
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

- **url**：url 地址。
- **data**：发送到服务器的其他数据对象，默认为 None。
- **timeout**：设置访问超时时间。
- **cafile 和 capath**：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
- **cadefault**：已经被弃用。
- **context**：ssl.SSLContext类型，用来指定 SSL 设置。

```python
from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.read())
```

- **read()** - 读取整个网页内容

  ```python
  from urllib.request import urlopen
  
  myURL = urlopen("https://www.runoob.com/")
  print(myURL.read(300))
  ```

- **readline()** - 读取文件的一行内容

  ```python
  from urllib.request import urlopen
  
  myURL = urlopen("https://www.runoob.com/")
  print(myURL.readline()) #读取一行内容
  ```

- **readlines()** - 读取文件的全部内容，它会把读取的内容赋值给一个列表变量。

  ```python
  from urllib.request import urlopen
  
  myURL = urlopen("https://www.runoob.com/")
  lines = myURL.readlines()
  for line in lines:
      print(line) 
  ```

如果要将抓取的网页保存到本地

```python
from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
f = open("runoob_urllib_test.html", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()
```

URL 的编码与解码可以使用 

- **urllib.request.quote()** 
- **urllib.request.unquote()** 

```python
import urllib.request 

encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
print(encode_url)

unencode_url = urllib.request.unquote(encode_url)    # 解码
print(unencode_url)
```

### 模拟头部信息

我们抓取网页一般需要对 headers（网页头信息）进行模拟，这时候需要使用到 urllib.request.Request 类：

```python
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

- **url**：url 地址。
- **data**：发送到服务器的其他数据对象，默认为 None。
- **headers**：HTTP 请求的头部信息，字典格式。
- **origin_req_host**：请求的主机地址，IP 或域名。
- **unverifiable**：很少用这个参数，用于设置网页是否需要验证，默认是 False。
- **method**：请求方法， 如 GET、POST、DELETE、PUT等。

 - py3_urllib_test.py 文件代码

```python
import urllib.request
import urllib.parse

url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
keyword = 'Python 教程' 
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request = urllib.request.Request(url_all,headers=header)
reponse = urllib.request.urlopen(request).read()

fh = open("./urllib_test_runoob_search.html","wb")    # 将文件写入到当前目录中
fh.write(reponse)
fh.close()
```

------

### urllib.error

urllib.error 模块为 urllib.request 所引发的异常定义了异常类，基础异常类是 URLError。

urllib.error 包含了两个方法，URLError 和 HTTPError。

URLError 是 OSError 的一个子类，用于处理程序在遇到问题时会引发此异常（或其派生的异常），包含的属性 reason 为引发异常的原因。

HTTPError 是 URLError 的一个子类，用于处理特殊 HTTP 错误例如作为认证请求的时候，包含的属性 **code** 为 HTTP 的状态码， **reason** 为引发异常的原因，**headers** 为导致 HTTPError 的特定 HTTP 请求的 HTTP 响应头。

对不存在的网页抓取并处理异常:

```python
import urllib.request
import urllib.error

myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())   # 200

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)   # 404
```

更多网页状态码可以查阅：https://www.runoob.com/http/http-status-codes.html。

------

### urllib.parse

urllib.parse 用于解析 URL，格式如下：

```python
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
```

urlstring 为 字符串的 url 地址，scheme 为协议类型，

allow_fragments 参数为 false，则无法识别片段标识符。相反，它们被解析为路径，参数或查询组件的一部分，并 fragment 在返回值中设置为空字符串。

```python
from urllib.parse import urlparse

o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)
```

以上实例输出结果为：

```python
ParseResult(scheme='https', netloc='www.runoob.com', path='/', params='', query='s=python+%E6%95%99%E7%A8%8B', fragment='')
```

从结果可以看出，内容是一个元组，包含 6 个字符串：协议，位置，路径，参数，查询，判断。

我们可以直接读取协议内容：

```python
from urllib.parse import urlparse

o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o.scheme)
```

以上实例输出结果为：

```python
https
```

完整内容如下：

| 属性       | 索引 | 值                       | 值（如果不存在） |
| :--------- | :--- | :----------------------- | :--------------- |
| `scheme`   | 0    | URL协议                  | *scheme* 参数    |
| `netloc`   | 1    | 网络位置部分             | 空字符串         |
| `path`     | 2    | 分层路径                 | 空字符串         |
| `params`   | 3    | 最后路径元素的参数       | 空字符串         |
| `query`    | 4    | 查询组件                 | 空字符串         |
| `fragment` | 5    | 片段识别                 | 空字符串         |
| `username` |      | 用户名                   | `None`           |
| `password` |      | 密码                     | `None`           |
| `hostname` |      | 主机名（小写）           | `None`           |
| `port`     |      | 端口号为整数（如果存在） | `None`           |

------

### urllib.robotparser

urllib.robotparser 用于解析 robots.txt 文件。

robots.txt（统一小写）是一种存放于网站根目录下的 robots 协议，它通常用于告诉搜索引擎对网站的抓取规则。

urllib.robotparser 提供了 RobotFileParser 类，语法如下：

```python
class urllib.robotparser.RobotFileParser(url='')
```

这个类提供了一些可以读取、解析 robots.txt 文件的方法：

- set_url(url) - 设置 robots.txt 文件的 URL。
- read() - 读取 robots.txt URL 并将其输入解析器。
- parse(lines) - 解析行参数。
- can_fetch(useragent, url) - 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
- mtime() -返回最近一次获取 robots.txt 文件的时间。 这适用于需要定期检查 robots.txt 文件更新情况的长时间运行的网页爬虫。
- modified() - 将最近一次获取 robots.txt 文件的时间设置为当前时间。
- crawl_delay(useragent) -为指定的 useragent 从 robots.txt 返回 Crawl-delay 形参。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
- request_rate(useragent) -以 named tuple RequestRate(requests, seconds) 的形式从 robots.txt 返回 Request-rate 形参的内容。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
- site_maps() - 以 list() 的形式从 robots.txt 返回 Sitemap 形参的内容。 如果此形参不存在或者此形参的 robots.txt 条目存在语法错误，则返回 None。

## requests 模块

| 对比项         | `requests`               | `urllib.request` |
| -------------- | ------------------------ | ---------------- |
| 来源           | 第三方库                 | Python 标准库    |
| 是否需要安装   | ✔ `pip install requests` | ❌ 不需要         |
| 易用性         | ⭐⭐⭐⭐⭐                    | ⭐⭐               |
| 代码量         | 少                       | 多               |
| 可读性         | 很高                     | 一般             |
| JSON 支持      | ✔ 内置                   | ❌ 手动处理       |
| Session/Cookie | ✔ 很方便                 | 支持但较麻烦     |
| 文件上传       | ✔ 很简单                 | 较复杂           |
| 超时设置       | ✔ 简单                   | 支持但写法复杂   |
| 实际项目       | ⭐⭐⭐⭐⭐                    | ⭐                |

Python requests 是一个常用的 HTTP 请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果。

requests 模块比 [urllib](https://www.runoob.com/python3/python-urllib.html) 模块更简洁。

使用 requests 发送 HTTP 请求需要先导入 requests 模块：

```python
import requests
```

导入后就可以发送 HTTP 请求，使用 requests 提供的方法向指定 URL 发送 HTTP 请求，例如：

```python
# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回网页内容
print(x.text)
```

每次调用 requests 请求之后，会返回一个 response 对象，该对象包含了具体的响应信息，如状态码、响应头、响应内容等：

```python
print(response.status_code)  # 获取响应状态码
print(response.headers)  # 获取响应头
print(response.content)  # 获取响应内容
```

更多响应信息如下：

| 属性或方法            | 说明                                                         |
| :-------------------- | :----------------------------------------------------------- |
| apparent_encoding     | 编码方式                                                     |
| close()               | 关闭与服务器的连接                                           |
| content               | 返回响应的内容，以字节为单位                                 |
| cookies               | 返回一个 CookieJar 对象，包含了从服务器发回的 cookie         |
| elapsed               | 返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。 |
| encoding              | 解码 r.text 的编码方式                                       |
| headers               | 返回响应头，字典格式                                         |
| history               | 返回包含请求历史的响应对象列表（url）                        |
| is_permanent_redirect | 如果响应是永久重定向的 url，则返回 True，否则返回 False      |
| is_redirect           | 如果响应被重定向，则返回 True，否则返回 False                |
| iter_content()        | 迭代响应                                                     |
| iter_lines()          | 迭代响应的行                                                 |
| json()                | 返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误) |
| links                 | 返回响应的解析头链接                                         |
| next                  | 返回重定向链中下一个请求的 PreparedRequest 对象              |
| ok                    | 检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False |
| raise_for_status()    | 如果发生错误，方法返回一个 HTTPError 对象                    |
| reason                | 响应状态的描述，比如 "Not Found" 或 "OK"                     |
| request               | 返回请求此响应的请求对象                                     |
| status_code           | 返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found） |
| text                  | 返回响应的内容，unicode 类型数据                             |
| url                   | 返回响应的 URL                                               |

```python
# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回 http 的状态码
print(x.status_code)

# 响应状态的描述
print(x.reason)

# 返回编码
print(x.apparent_encoding)

# 200
# OK
# utf-8
```

### requests 方法

requests 方法如下表：

| 方法                             | 描述                            |
| :------------------------------- | :------------------------------ |
| delete(*url*, *args*)            | 发送 DELETE 请求到指定 url      |
| get(*url*, *params, args*)       | 发送 GET 请求到指定 url         |
| head(*url*, *args*)              | 发送 HEAD 请求到指定 url        |
| patch(*url*, *data, args*)       | 发送 PATCH 请求到指定 url       |
| post(*url*, *data, json, args*)  | 发送 POST 请求到指定 url        |
| put(*url*, *data, args*)         | 发送 PUT 请求到指定 url         |
| request(*method*, *url*, *args*) | 向指定的 url 发送指定的请求方法 |

使用 requests.request() 发送 get 请求：

```python
# 导入 requests 包
import requests

# 发送请求
x = requests.request('get', 'https://www.runoob.com/')

# 返回网页内容
print(x.status_code)
```

设置请求头：

```python
# 导入 requests 包
import requests

 
kw = {'s':'python 教程'}

# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://www.runoob.com/", params = kw, headers = headers)

# 查看响应状态码
print (response.status_code)

# 查看响应头部字符编码
print (response.encoding)

# 查看完整url地址
print (response.url)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)
```

输出结果如下：

```python
200
UTF-8
https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B

... 其他内容...
```

post() 方法可以发送 POST 请求到指定 url，一般格式如下：

```python
requests.post(url, data={key: value}, json={key: value}, args)
```

- **url** 请求 url。
- **data** 参数为要发送到指定 url 的字典、元组列表、字节或文件对象。
- **json** 参数为要发送到指定 url 的 JSON 对象。
- **args** 为其他参数，比如 cookies、headers、verify等。

```python
# 导入 requests 包
import requests

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post.php')

# 返回网页内容
print(x.text)
```

输出结果如下：

```python
<p style='color:red;'>本内容是使用 POST 方法请求的。</p><p style='color:red;'>请求时间：
2022-05-26 17:30:47</p>
```

post 请求带参数：

```python
# 导入 requests 包
import requests

# 表单参数，参数名为 fname 和 lname
myobj = {'fname': 'RUNOOB','lname': 'Boy'}

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post2.php', data = myobj)

# 返回网页内容
print(x.text)
```

输出结果如下：

```python
<p style='color:red;'>你好，RUNOOB Boy，今天过得怎么样？</p>
```

------

### 附加请求参数

发送请求我们可以在请求中附加额外的参数，例如请求头、查询参数、请求体等，例如：

```python
headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
data = {'username': 'example', 'password': '123456'}  # 设置请求体
response = requests.post('https://www.runoob.com', headers=headers, params=params, data=data)
```

上述代码发送一个 POST 请求，并附加了请求头、查询参数和请求体。

除了基本的 GET 和 POST 请求外，requests 还支持其他 HTTP 方法，如 PUT、DELETE、HEAD、OPTIONS 等。

# 爬虫体系

BeautifulSoup

Scrapy

selenium

Playwright

| 对比项                 | BeautifulSoup          | Scrapy    | Selenium             | Playwright        |
| ---------------------- | ---------------------- | --------- | -------------------- | ----------------- |
| 定位                   | HTML 解析库            | 爬虫框架  | 浏览器自动化         | 现代浏览器自动化  |
| 是否发送 HTTP 请求     | ❌（需配合 `requests`） | ✔         | ✔                    | ✔                 |
| 是否解析 HTML          | ✔                      | ✔         | ✔                    | ✔                 |
| 是否执行 JavaScript    | ❌                      | ❌（默认） | ✔                    | ✔                 |
| 是否打开真实浏览器     | ❌                      | ❌         | ✔                    | ✔                 |
| 支持无头模式           | ❌                      | ❌         | ✔                    | ✔                 |
| 支持 Chrome / Edge     | ❌                      | ❌         | ✔                    | ✔                 |
| 支持 Firefox           | ❌                      | ❌         | ✔                    | ✔                 |
| 支持 Safari/WebKit     | ❌                      | ❌         | 部分                 | ✔                 |
| 自动等待元素           | ❌                      | ❌         | 一般（经常手动等待） | ✔（内置自动等待） |
| 网络请求拦截           | ❌                      | 一般      | ✔                    | ✔（更强）         |
| 多标签页               | ❌                      | ❌         | ✔                    | ✔                 |
| 多浏览器上下文         | ❌                      | ❌         | 一般                 | ✔                 |
| 登录自动化             | ❌                      | ❌         | ✔                    | ✔                 |
| 文件上传/下载          | ❌                      | ❌         | ✔                    | ✔                 |
| 截图/PDF               | ❌                      | ❌         | ✔                    | ✔                 |
| 性能                   | ⭐⭐⭐⭐⭐                  | ⭐⭐⭐⭐⭐     | ⭐⭐                   | ⭐⭐⭐⭐              |
| 学习成本               | ⭐                      | ⭐⭐⭐⭐      | ⭐⭐                   | ⭐⭐⭐               |
| 企业使用频率（新项目） | ⭐⭐⭐                    | ⭐⭐⭐⭐      | ⭐⭐⭐                  | ⭐⭐⭐⭐⭐             |

## 三者关系

很多新人以为三者是竞争关系，其实不是：

```python
          获取网页
             │
     ┌───────┴────────┐
     │                │
 requests         Selenium
     │                │
     └───────┬────────┘
             │
        HTML 内容
             │
     BeautifulSoup
```

而：

```python
Scrapy
```

其实是：

```python
Scrapy
│
├── 下载网页
├── 调度请求
├── 去重
├── 并发
├── 数据存储
└── HTML解析（可用XPath/CSS，也可以集成BeautifulSoup）
```

它是一整套框架。

- **`requests + BeautifulSoup`** 能解决大部分基础爬虫需求，也是学习网页抓取原理的最佳组合。
- **Selenium** 能处理需要登录、点击、执行 JavaScript 的网站，在自动化测试和数据采集中都很有用。
- **Scrapy** 更偏向专业爬虫工程，如果你以后不专门做爬虫开发，了解框架思想即可，不必投入太多时间。

另外补充一点：如果你现在开始学习新项目，**Playwright** 已经逐渐取代 Selenium 成为很多团队的新选择，尤其在现代前端网站自动化方面表现更好。

# 并发

## 多线程

### 什么是线程？

你可以把线程想象成办公室里的员工：

- 一个单线程程序就像只有一个员工，他必须顺序完成打印文档、回复邮件、泡咖啡等所有工作。
- 多线程程序则像拥有多个员工，他们可以**同时**进行不同的任务，大大提高了工作效率。

在计算机科学中：

- **进程**：一个运行中的程序，拥有独立的内存空间（例如，你同时打开的浏览器和音乐播放器就是两个进程）。
- **线程**：进程内的一个独立执行流，是 CPU 调度的基本单位。同一个进程内的所有线程**共享该进程的内存空间**（如全局变量）。

### 为什么使用多线程？

在单线程程序中，任务是一个接一个地顺序执行的。如果某个任务需要等待（例如等待网络响应或文件读取），整个程序会被阻塞，直到该任务完成。而多线程可以让程序在等待某个任务的同时，继续执行其他任务，从而提高程序的整体性能。

### Python 的线程与全局解释器锁 (GIL)

Python 有一个叫做 全局解释器锁 (Global Interpreter Lock， GIL) 的机制，GIL 确保了在任意时刻，只有一个线程可以执行 Python 字节码。

**这意味着什么？** 对于 CPU 密集型任务（如科学计算、图像处理），由于 GIL 的存在，多线程通常无法利用多核优势来提升计算速度，甚至可能因为线程切换的开销而变慢。

**那么，Python 多线程的用武之地在哪里？** 对于 I/O 密集型任务（如网络请求、读写文件、等待用户输入），线程在等待 I/O 操作完成时会释放 GIL，从而让其他线程运行。这可以显著提升程序的整体响应速度和效率，因为你在等待一个网页响应时，程序可以去处理另一个任务。

多线程类似于同时执行多个不同程序，多线程运行有如下优点：

- 使用线程可以把占据长时间的程序中的任务放到后台去处理。
- 用户界面可以更加吸引人，比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度。
- 程序的运行速度可能加快。
- 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。

每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。

指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。

- 线程可以被抢占（中断）。
- 在其他线程正在运行时，线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。

线程可以分为:

- **内核线程：**由操作系统内核创建和撤销。
- **用户线程：**不需要内核支持而在用户程序中实现的线程。

Python3 线程中常用的两个模块为：

- **_thread**
- **threading(推荐使用)**

thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。

Python中使用线程有两种方式：函数或者用类来包装线程对象。

------

### 线程模块 / threading

Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

- **threading.current_thread()**: 返回当前的线程变量。
- **threading.enumerate()**: 返回一个包含正在运行的线程的列表。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- **threading.active_count()**: 返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。
- **threading.Thread(target, args=(), kwargs={}, daemon=None)**：
  - 创建`Thread`类的实例。
  - `target`：线程将要执行的目标函数。
  - `args`：目标函数的参数，以元组形式传递。
  - `kwargs`：目标函数的关键字参数，以字典形式传递。
  - `daemon`：指定线程是否为守护线程。

#### threading.Thread 类方法与属性:

| 方法 / 属性                                                  | 作用                                                         | 示例                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
| `Thread.__init__(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)` | 初始化线程对象，指定执行函数、参数、线程名、是否守护线程等。 | `threading.Thread(target=task, args=(1,), daemon=True)` |
| `start()`                                                    | 启动线程，内部自动调用 `run()`。                             | `t.start()`                                             |
| `run()`                                                      | 定义线程执行的任务（通常重写该方法或通过 `target` 指定）。   | `class MyThread(Thread): def run(self): ...`            |
| `join(timeout=None)`                                         | 等待线程执行结束，可设置最大等待时间。                       | `t.join()`、`t.join(5)`                                 |
| `is_alive()`                                                 | 判断线程是否仍在运行。                                       | `t.is_alive()`                                          |
| `getName()`                                                  | 获取线程名称（**已不推荐**，建议使用 `name` 属性）。         | `t.getName()`                                           |
| `setName(name)`                                              | 设置线程名称（**已不推荐**，建议直接赋值 `name`）。          | `t.setName("Worker-1")`                                 |
| `ident`                                                      | 获取线程唯一标识符（ID），只读属性。                         | `print(t.ident)`                                        |
| `daemon`                                                     | 是否为守护线程，可读写属性。                                 | `t.daemon = True`                                       |
| `isDaemon()`                                                 | 判断是否为守护线程（**已不推荐**，建议使用 `daemon` 属性）。 | `t.isDaemon()`                                          |

```python
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# 创建线程
thread = threading.Thread(target=print_numbers)

# 启动线程
thread.start()

# 等待线程结束
thread.join()
```

输出结果为：

```python
0
1
2
3
4
```

------

#### 使用 threading 模块创建线程

我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：

```python
#!/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
```

以上程序执行结果如下；

```python
开始线程：Thread-1
开始线程：Thread-2
Thread-1: Wed Jan  5 17:34:54 2022
Thread-2: Wed Jan  5 17:34:55 2022
Thread-1: Wed Jan  5 17:34:55 2022
Thread-1: Wed Jan  5 17:34:56 2022
Thread-2: Wed Jan  5 17:34:57 2022
Thread-1: Wed Jan  5 17:34:57 2022
Thread-1: Wed Jan  5 17:34:58 2022
退出线程：Thread-1
Thread-2: Wed Jan  5 17:34:59 2022
Thread-2: Wed Jan  5 17:35:01 2022
Thread-2: Wed Jan  5 17:35:03 2022
退出线程：Thread-2
退出主线程
```

```python
thread1 = myThread(1, "Thread-1", 1)
# 实际上 Python 帮你做了：
myThread.__init__(thread1, 1, "Thread-1", 1)
# Python 自动把：thread1 作为：self
def __init__(self, threadID, name, delay):
```

------

### 线程同步

如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：

多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。

考虑这样一种情况：一个列表里所有元素都是 0，线程 "set" 从后向前把所有元素改成 1，而线程 "print" 负责从前往后读取列表并打印。

那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。

锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。

经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。

```python
#!/usr/bin/python3

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```



执行以上程序，输出结果为：

```python
开启线程： Thread-1
开启线程： Thread-2
Thread-1: Wed Jan  5 17:36:50 2022
Thread-1: Wed Jan  5 17:36:51 2022
Thread-1: Wed Jan  5 17:36:52 2022
Thread-2: Wed Jan  5 17:36:54 2022
Thread-2: Wed Jan  5 17:36:56 2022
Thread-2: Wed Jan  5 17:36:58 2022
退出主线程
```

------

### 线程优先级队列（ Queue）

Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:

| 方法                                        | 作用                                                     | 示例                    |
| ------------------------------------------- | -------------------------------------------------------- | ----------------------- |
| `Queue.qsize()`                             | 返回当前队列中的元素数量。                               | `q.qsize()`             |
| `Queue.empty()`                             | 判断队列是否为空，空返回 `True`，否则返回 `False`。      | `q.empty()`             |
| `Queue.full()`                              | 判断队列是否已满（与 `maxsize` 对应），满返回 `True`。   | `q.full()`              |
| `Queue.get(block=True, timeout=None)`       | 从队列取出一个元素；可阻塞等待，可设置超时时间。         | `item = q.get()`        |
| `Queue.get_nowait()`                        | 非阻塞获取元素，等价于 `q.get(False)`。                  | `item = q.get_nowait()` |
| `Queue.put(item, block=True, timeout=None)` | 向队列放入一个元素；可阻塞等待，可设置超时时间。         | `q.put("hello")`        |
| `Queue.put_nowait(item)`                    | 非阻塞放入元素，等价于 `q.put(item, False)`。            | `q.put_nowait("hello")` |
| `Queue.task_done()`                         | 表示当前取出的任务已经处理完成，通常在 `get()` 后调用。  | `q.task_done()`         |
| `Queue.join()`                              | 阻塞当前线程，直到队列中所有任务都调用了 `task_done()`。 | `q.join()`              |

```python
#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```

以上程序执行结果：

```python
开启线程：Thread-1
开启线程：Thread-2
开启线程：Thread-3
Thread-3 processing One
Thread-1 processing Two
Thread-2 processing Three
Thread-3 processing Four
Thread-1 processing Five
退出线程：Thread-3
退出线程：Thread-2
退出线程：Thread-1
退出主线程
```

```python
import queue

q = queue.Queue()

q.put("A")
q.put("B")

while not q.empty():
    item = q.get()
    print(item)

    # 处理完成
    q.task_done()

# 等待所有任务完成
q.join()

print("所有任务完成")
```

```python
put(A)
put(B)
   │
   ▼
get(A)
   │
task_done()
   │
get(B)
   │
task_done()
   │
join() 发现所有任务都完成
   │
继续执行后面的代码
```

## threading / asyncio 区别

| 对比项                 | `threading`              | `asyncio`                         |
| ---------------------- | ------------------------ | --------------------------------- |
| 并发方式               | 多线程                   | 单线程 + 协程（事件循环）         |
| 是否创建线程           | ✔                        | ❌（默认只有一个线程）             |
| 是否受 GIL 影响        | ✔                        | ✔（但影响较小，因为主要处理 I/O） |
| CPU 密集型             | ❌ 不适合                 | ❌ 不适合                          |
| I/O 密集型             | ✔ 适合                   | ✔✔✔ 更适合                        |
| 线程切换               | 操作系统调度             | Python 事件循环调度               |
| 内存开销               | 较大（每个线程有栈空间） | 很小                              |
| 上下文切换             | 较慢                     | 很快                              |
| 编程复杂度             | 较低                     | 较高                              |
| 是否需要 `async/await` | ❌                        | ✔                                 |
| 是否适合大量连接       | 一般                     | ✔ 非常适合                        |
| 企业使用场景           | 后台任务、下载、文件处理 | Web 服务、高并发 API、网络通信    |
| 学习优先级             | ⭐⭐⭐⭐                     | ⭐⭐⭐⭐⭐（AI / 后端必学）            |

## threading 模块

### 如何使用 threading 模块？

使用 `threading` 模块的第一步就是导入它：

```python
import threading
import time  # 用于模拟耗时操作
```

创建线程最基本的方式是使用 `threading.Thread` 类。

**语法说明：**

```python
thread_obj = threading.Thread(target=函数名, args=(参数元组,))
```

- **target**: 指定线程启动后要执行的函数。
- **args**: 传递给 target 函数的参数，必须是元组类型。如果只有一个参数，需要写成 `(参数,)` 的形式。

#### 1. 创建线程

在 Python 中，可以通过继承 `threading.Thread` 类或直接使用 `threading.Thread` 构造函数来创建线程。

##### 方法 1：继承 `threading.Thread` 类

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread = MyThread()
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")
```

##### 方法 2：使用 `threading.Thread` 构造函数

```python
import threading

def my_function():
    print("线程开始执行")
    # 在这里编写线程要执行的代码
    print("线程执行结束")

# 创建线程实例
thread = threading.Thread(target=my_function)
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")
```

#### 2. 线程同步

在多线程编程中，多个线程可能会同时访问共享资源，这可能导致数据不一致的问题。为了避免这种情况，可以使用线程同步机制，如锁（`Lock`）。

```python
import threading

# 创建一个锁对象
lock = threading.Lock()

def my_function():
    with lock:
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread1 = threading.Thread(target=my_function)
thread2 = threading.Thread(target=my_function)
# 启动线程
thread1.start()
thread2.start()
# 等待线程执行完毕
thread1.join()
thread2.join()
print("主线程结束")
```

#### 3. 线程间通信

线程间通信可以通过队列（`Queue`）来实现。`Queue` 是线程安全的，可以在多个线程之间安全地传递数据。

```python
import threading
import queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"处理项目: {item}")
        q.task_done()

# 创建一个队列并填充数据
q = queue.Queue()
for i in range(10):
    q.put(i)

# 创建线程实例
thread1 = threading.Thread(target=worker, args=(q,))
thread2 = threading.Thread(target=worker, args=(q,))
# 启动线程
thread1.start()
thread2.start()
# 等待队列中的所有项目被处理完毕
q.join()
print("所有项目处理完毕")
```

------

### 常用类、方法及属性

#### 1. 核心类

| 类/方法/属性                     | 说明                             | 示例                                 |
| :------------------------------- | :------------------------------- | :----------------------------------- |
| **`threading.Thread`**           | 线程类，用于创建和管理线程       | `t = Thread(target=func, args=(1,))` |
| **`threading.Lock`**             | 互斥锁（原始锁）                 | `lock = Lock()`                      |
| **`threading.RLock`**            | 可重入锁（同一线程可多次获取）   | `rlock = RLock()`                    |
| **`threading.Event`**            | 事件对象，用于线程同步           | `event = Event()`                    |
| **`threading.Condition`**        | 条件变量，用于复杂线程协调       | `cond = Condition()`                 |
| **`threading.Semaphore`**        | 信号量，控制并发线程数           | `sem = Semaphore(3)`                 |
| **`threading.BoundedSemaphore`** | 有界信号量（防止计数超过初始值） | `b_sem = BoundedSemaphore(2)`        |
| **`threading.Timer`**            | 定时器线程，延迟执行             | `timer = Timer(5.0, func)`           |
| **`threading.local`**            | 线程局部数据（各线程独立存储）   | `local_data = threading.local()`     |

#### 2. Thread 对象常用方法/属性

| 方法/属性                | 说明                                 | 示例                  |
| :----------------------- | :----------------------------------- | :-------------------- |
| **`start()`**            | 启动线程                             | `t.start()`           |
| **`run()`**              | 线程执行的方法（可重写）             | 自定义类时覆盖此方法  |
| **`join(timeout=None)`** | 阻塞当前线程，直到目标线程结束       | `t.join()`            |
| **`is_alive()`**         | 检查线程是否在运行                   | `if t.is_alive():`    |
| **`name`**               | 线程名称（可修改）                   | `t.name = "Worker-1"` |
| **`daemon`**             | 守护线程标志（主线程退出时自动结束） | `t.daemon = True`     |
| **`ident`**              | 线程标识符（未启动时为 `None`）      | `print(t.ident)`      |

#### 3. Lock/RLock 常用方法

| 方法                                     | 说明                   | 示例                    |
| :--------------------------------------- | :--------------------- | :---------------------- |
| **`acquire(blocking=True, timeout=-1)`** | 获取锁（阻塞或非阻塞） | `lock.acquire()`        |
| **`release()`**                          | 释放锁                 | `lock.release()`        |
| **`locked()`**                           | 检查锁是否被占用       | `if not lock.locked():` |

#### 4. Event 常用方法

| 方法                     | 说明                           | 示例                 |
| :----------------------- | :----------------------------- | :------------------- |
| **`set()`**              | 设置事件为真，唤醒所有等待线程 | `event.set()`        |
| **`clear()`**            | 重置事件为假                   | `event.clear()`      |
| **`wait(timeout=None)`** | 阻塞直到事件为真或超时         | `event.wait(2.0)`    |
| **`is_set()`**           | 检查事件状态                   | `if event.is_set():` |

#### 5. Condition 常用方法

| 方法                     | 说明                           | 示例                |
| :----------------------- | :----------------------------- | :------------------ |
| **`wait(timeout=None)`** | 释放锁并阻塞，直到被通知或超时 | `cond.wait()`       |
| **`notify(n=1)`**        | 唤醒最多 `n` 个等待线程        | `cond.notify(2)`    |
| **`notify_all()`**       | 唤醒所有等待线程               | `cond.notify_all()` |

#### 6. 模块级函数/属性

| 函数/属性                        | 说明                                | 示例                                                        |
| :------------------------------- | :---------------------------------- | :---------------------------------------------------------- |
| **`threading.active_count()`**   | 返回当前活跃线程数                  | `print(threading.active_count())`                           |
| **`threading.current_thread()`** | 返回当前线程对象                    | `print(threading.current_thread().name)`                    |
| **`threading.enumerate()`**      | 返回所有活跃线程的列表              | `for t in threading.enumerate():`                           |
| **`threading.main_thread()`**    | 返回主线程对象                      | `if threading.current_thread() is threading.main_thread():` |
| **`threading.get_ident()`**      | 返回当前线程的标识符（Python 3.3+） | `print(threading.get_ident())`                              |

------

### 注意事项

1. **全局解释器锁（GIL）**：Python 的 GIL 会限制同一时间只有一个线程执行 Python 字节码。因此，在 CPU 密集型任务中，多线程可能不会带来性能提升。对于 I/O 密集型任务，多线程仍然是有益的。
2. **线程安全**：在多线程环境中，确保对共享资源的访问是线程安全的，避免数据竞争和死锁。
3. **线程数量**：创建过多的线程可能会导致系统资源耗尽，影响程序性能。合理控制线程数量，或使用线程池（`ThreadPoolExecutor`）来管理线程。



## asyncio 模块

`asyncio` 是 Python 标准库中的一个模块，用于编写异步 I/O 操作的代码。

asyncio 提供了一种高效的方式来处理并发任务，特别适用于 I/O 密集型操作，如网络请求、文件读写等。

通过使用 `asyncio`，你可以在单线程中同时处理多个任务，而无需使用多线程或多进程。

### 为什么需要 asyncio？

在传统的同步编程中，当一个任务需要等待 I/O 操作（如网络请求）完成时，程序会阻塞，直到操作完成。这会导致程序的效率低下，尤其是在需要处理大量 I/O 操作时。

`asyncio` 通过引入异步编程模型，允许程序在等待 I/O 操作时继续执行其他任务，从而提高了程序的并发性和效率。

> 想象一下你正在经营一家餐厅：
>
> - **同步模式（普通函数）：** 你只有一个厨师。客人 A 点了一份牛排，厨师开始煎牛排（这需要等待 5 分钟）。在煎牛排的这 5 分钟里，厨师完全被占用，不能做任何其他事，即使客人 B 只想点一杯水，也必须干等着。
> - **异步模式（asyncio）：** 你有多个厨师（实际上还是一个，但非常聪明）。厨师开始煎客人 A 的牛排后，发现需要等待，他立刻把这份牛排标记为等待中，然后转头去给客人 B 倒水。倒完水回来，看看牛排是不是快好了，如果还没好，又可以去处理客人 C 的订单。这样，在等待 I/O（如煎牛排、网络请求、读写文件）的时间里，厨师（CPU）一直在高效地工作。
>
> asyncio 就是 Python 用来实现这种聪明工作模式的标准库，它允许你编写 单线程并发 的代码，特别适用于网络爬虫、Web 服务器、微服务等 I/O 密集型场景。

它的核心是 事件循环、协程 和 任务。

------

### asyncio 的核心概念

#### 1. 协程（Coroutine）

协程是 `asyncio` 的核心概念之一。它是一个特殊的函数，可以在执行过程中暂停，并在稍后恢复执行。协程通过 `async def` 关键字定义，并通过 `await` 关键字暂停执行，等待异步操作完成。

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
```

#### 2. 事件循环（Event Loop）

事件循环是 `asyncio` 的核心组件，负责调度和执行协程。它不断地检查是否有任务需要执行，并在任务完成后调用相应的回调函数。

```python
async def main():
    await say_hello()

asyncio.run(main())
```

#### 3. 任务（Task）

任务是对协程的封装，表示一个正在执行或将要执行的协程。你可以通过 `asyncio.create_task()` 函数创建任务，并将其添加到事件循环中。

```python
async def main():
    task = asyncio.create_task(say_hello())
    await task
```

#### 4. Future

`Future` 是一个表示异步操作结果的对象。它通常用于底层 API，表示一个尚未完成的操作。你可以通过 `await` 关键字等待 `Future` 完成。

```python
async def main():
    future = asyncio.Future()
    await future
```

#### 基础用法与代码示例

让我们通过一个经典的并发访问多个网址的例子来理解上述概念。

假设我们需要获取三个不同网址的内容。使用同步方式会顺序执行，总耗时是三次请求耗时的总和。使用 `asyncio`，我们可以让这三个请求同时发出，总耗时接近于最慢的那一次请求。

#### 同步版本（作为对比）

```python
import time
import requests

def fetch_url(url):
    """模拟一个耗时的网络请求（同步版本）"""
    print(f"开始获取: {url}")
    time.sleep(2)  # 模拟 2 秒网络延迟
    print(f"完成获取: {url}")
    return f"来自 {url} 的数据"

def main_sync():
    urls = ['https://example.com/1', 'https://example.com/2', 'https://example.com/3']
    results = []
    start = time.time()
    
    for url in urls:
        result = fetch_url(url)  # 必须等上一个完成才能开始下一个
        results.append(result)
    
    end = time.time()
    print(f"同步版本总耗时: {end - start:.2f} 秒")
    print(f"结果: {results}")

if __name__ == "__main__":
    main_sync()
```

**预期运行结果**：

```python
开始获取: https://example.com/1
完成获取: https://example.com/1
开始获取: https://example.com/2
完成获取: https://example.com/2
开始获取: https://example.com/3
完成获取: https://example.com/3
同步版本总耗时: 6.00 秒
结果: [‘来自 https://example.com/1 的数据‘, ‘来自 https://example.com/2 的数据‘, ‘来自 https://example.com/2 的数据‘]
```

总共花了约 6 秒。

#### 异步版本（使用 asyncio）

我们需要用 `aiohttp` 库来替代 `requests` 进行异步 HTTP 请求。首先安装它：`pip install aiohttp`。

```python
import asyncio
import aiohttp
import time

async def fetch_url_async(session, url):
    """模拟一个耗时的网络请求（异步版本）"""
    print(f"开始异步获取: {url}")
    # 注意：这里我们使用 aiohttp 的异步 get 方法，并用 await 等待
    async with session.get(url) as response:
        # 模拟处理响应也需要时间
        await asyncio.sleep(2)  # 使用 asyncio.sleep 模拟 I/O 等待，它不会阻塞线程
        text = await response.text()
        print(f"完成异步获取: {url}")
        return f"来自 {url} 的数据 (长度: {len(text)})"

async def main_async():
    urls = ['https://httpbin.org/get', 'https://httpbin.org/delay/1', 'https://httpbin.org/headers']
    
    async with aiohttp.ClientSession() as session:  # 创建异步 HTTP 会话
        # 为每个 URL 创建一个任务（Task）
        tasks = []
        for url in urls:
            # create_task 会将协程加入事件循环，立即开始调度
            task = asyncio.create_task(fetch_url_async(session, url))
            tasks.append(task)
        
        print("所有任务已创建，开始并发执行...")
        
        # 使用 asyncio.gather 并发运行所有任务，并等待它们全部完成
        # gather 返回一个结果列表，顺序与传入的任务顺序一致
        results = await asyncio.gather(*tasks)
        
        return results

if __name__ == "__main__":
    start = time.time()
    # asyncio.run() 是启动事件循环并运行顶层协程的简便方法
    final_results = asyncio.run(main_async())
    end = time.time()
    
    print(f"\n异步版本总耗时: {end - start:.2f} 秒")
    for res in final_results:
        print(res)
```

**预期运行结果**：

```python
所有任务已创建，开始并发执行...
开始异步获取: https://httpbin.org/get
开始异步获取: https://httpbin.org/delay/1
开始异步获取: https://httpbin.org/headers
（大约 2 秒后，所有请求几乎同时完成）
完成异步获取: https://httpbin.org/headers
完成异步获取: https://httpbin.org/get
完成异步获取: https://httpbin.org/delay/1

异步版本总耗时: 2.10 秒  # 注意！总耗时远小于 6 秒
来自 https://httpbin.org/get 的数据 (长度: 274)
来自 https://httpbin.org/delay/1 的数据 (长度: 392)
来自 https://httpbin.org/headers 的数据 (长度: 177)
```

**代码解析**：

- `async def`：定义了协程函数 `fetch_url_async` 和 `main_async`。
- `await`：在 `fetch_url_async` 中，我们 `await session.get()` 和 `await response.text()`，这告诉事件循环："这个网络请求需要时间，你先去执行其他就绪的任务吧"。
- `asyncio.create_task()`：将 `fetch_url_async` 协程包装成 `Task`，使其被事件循环调度，实现并发。
- `asyncio.gather(*tasks)`：一个非常实用的函数，它并发运行所有传入的协程/任务，并等待它们全部完成，最后收集所有结果。
- `asyncio.run(main_async())`：Python 3.7+ 推荐的方式，它负责创建事件循环、运行协程并关闭循环。

#### 关键函数与参数说明

下面以表格形式列出 `asyncio` 中几个最常用的高级函数：

| 函数                                                         | 主要作用                                                     | 常用参数说明                                                 |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **`asyncio.run(coro, \*, debug=False)`**                     | 运行一个顶层协程，管理事件循环的生命周期。是程序的主入口。   | `coro`: 要运行的协程对象。 `debug`: 设为 `True` 可启用事件循环的调试模式。 |
| **`asyncio.create_task(coro, \*, name=None)`**               | 将协程包装成一个 **Task** 对象，并排入事件循环等待调度。这是实现并发的主要方式。 | `coro`: 要包装的协程对象。 `name`: （Python 3.8+）为任务指定一个名称，便于调试。 |
| **`asyncio.gather(\*aws, return_exceptions=False)`**         | **并发运行**多个异步任务（`aws` 可接受协程、任务等），并等待所有完成，返回结果列表。 | `*aws`: 可变参数，传入多个异步对象。 `return_exceptions`: 默认为 `False`，任何任务抛出异常都会立即传播给 `gather` 的调用者。设为 `True` 时，异常会作为结果的一部分返回。 |
| **`asyncio.sleep(delay, result=None)`**                      | **异步地**休眠指定秒数。这是与 `time.sleep`（阻塞）的关键区别。 | `delay`: 休眠的秒数。 `result`: 休眠结束后返回的值。         |
| **`asyncio.wait(aws, \*, timeout=None, return_when=ALL_COMPLETED)`** | 并发运行任务，并等待满足指定条件。返回两个集合 `(done, pending)`，分别是已完成和未完成的任务。 | `aws`: 异步对象集合。 `timeout`: 超时时间（秒）。 `return_when`: 决定何时返回，可选：`FIRST_COMPLETED`（第一个完成）、`FIRST_EXCEPTION`（第一个异常）、`ALL_COMPLETED`（全部完成，默认）。 |
| **`asyncio.to_thread(func, /, \*args, \**kwargs)`**          | （Python 3.9+）将一个普通的、可能阻塞的同步函数放到一个单独的线程中运行，并返回一个可 `await` 的协程。用于处理 CPU 密集型或阻塞式 I/O。 | `func`: 要在线程中运行的同步函数。 `*args, **kwargs`: 传递给函数的参数。 |

#### 可视化理解：异步任务调度流程

<img src="https://www.runoob.com/wp-content/uploads/2025/04/asyncio-python-runoob12-scaled.jpg" alt="img" style="zoom:50%;" />

**图解说明**： 这个流程图展示了事件循环如何像调度员一样工作。它维护一个任务队列，当一个任务执行到 `await`（例如等待网络响应）时，它会被挂起，事件循环立即从队列中找出下一个可以运行（就绪）的任务来执行。当被挂起任务的 I/O 操作完成后，事件循环会收到通知，将该任务状态改回就绪，并在未来某个时刻继续执行它。通过这种方式，在 I/O 等待期间，CPU 被充分利用来执行其他任务，实现了单线程内的并发。

------

### asyncio 的基本用法

#### 1. 运行协程

要运行一个协程，你可以使用 `asyncio.run()` 函数。它会创建一个事件循环，并运行指定的协程。

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
```

#### 2. 并发执行多个任务

你可以使用 `asyncio.gather()` 函数并发执行多个协程，并等待它们全部完成。

```python
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

#### 3. 超时控制

你可以使用 `asyncio.wait_for()` 函数为协程设置超时时间。如果协程在指定时间内未完成，将引发 `asyncio.TimeoutError` 异常。

```python
import asyncio

async def long_task():
    await asyncio.sleep(10)
    print("Task finished")

async def main():
    try:
        await asyncio.wait_for(long_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())
```

------

### asyncio 的应用场景

`asyncio` 特别适用于以下场景：

1. **网络请求**：如 HTTP 请求、WebSocket 通信等。
2. **文件 I/O**：如异步读写文件。
3. **数据库操作**：如异步访问数据库。
4. **实时数据处理**：如实时消息队列处理。

------

### 常用类、方法和函数

#### **1. 核心函数**

| 方法/函数                       | 说明                          | 示例                                                 |
| :------------------------------ | :---------------------------- | :--------------------------------------------------- |
| **`asyncio.run(coro)`**         | 运行异步主函数（Python 3.7+） | `asyncio.run(main())`                                |
| **`asyncio.create_task(coro)`** | 创建任务并加入事件循环        | `task = asyncio.create_task(fetch_data())`           |
| **`asyncio.gather(\*coros)`**   | 并发运行多个协程              | `await asyncio.gather(task1, task2)`                 |
| **`asyncio.sleep(delay)`**      | 异步等待（非阻塞）            | `await asyncio.sleep(1)`                             |
| **`asyncio.wait(coros)`**       | 控制任务完成方式              | `done, pending = await asyncio.wait([task1, task2])` |

#### **2. 事件循环（Event Loop）**

| 方法                                   | 说明                 | 示例                              |
| :------------------------------------- | :------------------- | :-------------------------------- |
| **`loop.run_until_complete(future)`**  | 运行直到任务完成     | `loop.run_until_complete(main())` |
| **`loop.run_forever()`**               | 永久运行事件循环     | `loop.run_forever()`              |
| **`loop.stop()`**                      | 停止事件循环         | `loop.stop()`                     |
| **`loop.close()`**                     | 关闭事件循环         | `loop.close()`                    |
| **`loop.call_soon(callback)`**         | 安排回调函数立即执行 | `loop.call_soon(print, "Hello")`  |
| **`loop.call_later(delay, callback)`** | 延迟执行回调         | `loop.call_later(5, callback)`    |

#### **3. 协程（Coroutine）与任务（Task）**

| 方法/装饰器              | 说明                               | 示例                                   |
| :----------------------- | :--------------------------------- | :------------------------------------- |
| **`@asyncio.coroutine`** | 协程装饰器（旧版，Python 3.4-3.7） | `@asyncio.coroutine` `def old_coro():` |
| **`async def`**          | 定义协程（Python 3.5+）            | `async def fetch():`                   |
| **`task.cancel()`**      | 取消任务                           | `task.cancel()`                        |
| **`task.done()`**        | 检查任务是否完成                   | `if task.done():`                      |
| **`task.result()`**      | 获取任务结果（需任务完成）         | `data = task.result()`                 |

#### **4. 同步原语（类似`threading`）**

| 类                        | 说明       | 示例                                              |
| :------------------------ | :--------- | :------------------------------------------------ |
| **`asyncio.Lock()`**      | 异步互斥锁 | `lock = asyncio.Lock()` `async with lock:`        |
| **`asyncio.Event()`**     | 事件通知   | `event = asyncio.Event()` `await event.wait()`    |
| **`asyncio.Queue()`**     | 异步队列   | `queue = asyncio.Queue()` `await queue.put(item)` |
| **`asyncio.Semaphore()`** | 信号量     | `sem = asyncio.Semaphore(5)` `async with sem:`    |

#### **5. 网络与子进程**

| 方法/类                                | 说明          | 示例                                                         |
| :------------------------------------- | :------------ | :----------------------------------------------------------- |
| **`asyncio.open_connection()`**        | 建立TCP连接   | `reader, writer = await asyncio.open_connection('host', 80)` |
| **`asyncio.start_server()`**           | 创建TCP服务器 | `server = await asyncio.start_server(handle, '0.0.0.0', 8888)` |
| **`asyncio.create_subprocess_exec()`** | 创建子进程    | `proc = await asyncio.create_subprocess_exec('ls')`          |

#### **6. 实用工具**

| 方法                                  | 说明             | 示例                                   |
| :------------------------------------ | :--------------- | :------------------------------------- |
| **`asyncio.current_task()`**          | 获取当前任务     | `task = asyncio.current_task()`        |
| **`asyncio.all_tasks()`**             | 获取所有任务     | `tasks = asyncio.all_tasks()`          |
| **`asyncio.shield(coro)`**            | 保护任务不被取消 | `await asyncio.shield(critical_task)`  |
| **`asyncio.wait_for(coro, timeout)`** | 带超时的等待     | `try: await asyncio.wait_for(task, 5)` |

------

#### **注意事项**

1. **Python版本**：部分功能需Python 3.7+（如`asyncio.run()`）。
2. **阻塞操作**：避免在协程中使用同步阻塞代码（如`time.sleep()`）。
3. **调试**：设置`PYTHONASYNCIODEBUG=1`环境变量可启用调试模式。
4. **取消任务**：被取消的任务会引发`CancelledError`，需妥善处理。

# 系统 & 工具

## subprocess 模块

`subprocess` 是 Python 标准库中的一个模块，用于创建和管理子进程。

`subprocess` 允许你在 Python 程序中执行外部命令，并与这些命令进行交互。

通过 `subprocess` 模块，你可以执行系统命令、调用其他程序，并获取它们的输出或错误信息。

### 为什么使用 subprocess 模块？

在 Python 中，有时我们需要执行一些系统命令或调用其他程序来完成特定的任务。例如，你可能需要运行一个 shell 命令、启动一个外部应用程序，或者与一个命令行工具进行交互。`subprocess` 模块提供了一种安全且灵活的方式来处理这些需求。

与早期的 `os.system()` 或 `os.popen()` 相比，`subprocess` 模块提供了更强大的功能和更好的控制能力。它允许你更精细地管理子进程的输入、输出和错误流，并且可以处理更复杂的场景。

------

### subprocess 模块的核心功能

#### 1. 执行外部命令

`subprocess.run()` 是 `subprocess` 模块中最常用的函数之一。它可以执行一个外部命令，并等待命令完成。以下是一个简单的示例：

```python
import subprocess

# 执行一个简单的 shell 命令
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# 打印命令的输出
print(result.stdout)
```

在这个例子中，`subprocess.run()` 执行了 `ls -l` 命令，并将输出捕获到 `result.stdout` 中。

#### 2. 处理输入和输出

`subprocess` 模块允许你控制子进程的输入、输出和错误流。你可以将数据传递给子进程的标准输入，或者从子进程的标准输出和标准错误中读取数据。以下是一个示例：

```python
import subprocess

# 执行一个命令，并将输入传递给子进程
result = subprocess.run(['grep', 'python'], input='hello\npython\nworld', capture_output=True, text=True)

# 打印命令的输出
print(result.stdout)
```

在这个例子中，`subprocess.run()` 执行了 `grep python` 命令，并将字符串 `'hello\npython\nworld'` 作为输入传递给子进程。

#### 3. 处理错误

`subprocess` 模块还允许你处理子进程的错误。如果子进程返回非零的退出状态码，`subprocess.run()` 会抛出一个 `CalledProcessError` 异常。你可以通过检查 `result.returncode` 来获取子进程的退出状态码。

```python
import subprocess

try:
    result = subprocess.run(['ls', 'nonexistent_file'], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print(f"Error output: {e.stderr}")
```

在这个例子中，`subprocess.run()` 执行了 `ls nonexistent_file` 命令，由于文件不存在，命令失败并抛出了 `CalledProcessError` 异常。

------

### subprocess 模块的高级用法

#### 1. 使用 Popen 类

`subprocess.Popen` 类提供了更底层的接口，允许你更灵活地控制子进程。你可以使用 `Popen` 来启动一个子进程，并在后台运行它，或者与它进行交互。

```python
import subprocess

# 启动一个子进程
process = subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE, text=True)

# 读取子进程的输出
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 获取子进程的退出状态码
return_code = process.poll()
print(f"Process finished with return code {return_code}")
```

在这个例子中，`subprocess.Popen` 启动了一个 `ping google.com` 命令，并在后台运行它。程序通过循环读取子进程的输出，并在子进程结束后获取其退出状态码。

#### 2. 使用管道

`subprocess` 模块允许你使用管道将多个命令连接在一起。你可以将一个命令的输出作为另一个命令的输入。

```python
import subprocess

# 使用管道连接两个命令
p1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)

# 获取最终输出
output = p2.communicate()[0]
print(output)
```

在这个例子中，`ls -l` 命令的输出被传递给 `grep py` 命令，最终输出包含 `py` 的文件或目录。

------

### subprocess 模块的常用方法、类和参数

以下是 Python subprocess 模块的常用方法、类和参数的说明，包含功能描述及示例：

#### subprocess 模块核心方法

| 方法                            | 说明                         | 示例                                                         |
| :------------------------------ | :--------------------------- | :----------------------------------------------------------- |
| **`subprocess.run()`**          | 执行命令并等待完成（推荐）   | `subprocess.run(["ls", "-l"], capture_output=True, text=True)` |
| **`subprocess.Popen()`**        | 创建子进程（底层控制）       | `proc = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE)` |
| **`subprocess.call()`**         | 执行命令并返回退出码（旧版） | `exit_code = subprocess.call(["python", "--version"])`       |
| **`subprocess.check_call()`**   | 执行命令，失败时抛出异常     | `subprocess.check_call(["git", "commit"])`                   |
| **`subprocess.check_output()`** | 执行命令并返回输出（旧版）   | `output = subprocess.check_output(["date"], text=True)`      |

#### subprocess.CompletedProcess 对象属性（run() 方法的返回对象）

| 属性         | 说明                                     |
| :----------- | :--------------------------------------- |
| `args`       | 执行的命令参数列表                       |
| `returncode` | 进程退出状态码（0表示成功）              |
| `stdout`     | 标准输出内容（若设置了`capture_output`） |
| `stderr`     | 标准错误内容（若设置了`capture_output`） |

#### subprocess.Popen 类常用方法/属性

| 方法/属性       | 说明                                     | 示例                                              |
| :-------------- | :--------------------------------------- | :------------------------------------------------ |
| `poll()`        | 检查进程是否终止（返回`None`表示运行中） | `if proc.poll() is None: print("Running")`        |
| `wait()`        | 阻塞等待进程结束                         | `proc.wait()`                                     |
| `communicate()` | 交互式输入/输出                          | `stdout, stderr = proc.communicate(input="data")` |
| `terminate()`   | 发送终止信号（SIGTERM）                  | `proc.terminate()`                                |
| `kill()`        | 强制终止进程（SIGKILL）                  | `proc.kill()`                                     |
| `stdin`         | 进程的标准输入流                         | `proc.stdin.write("input")`                       |
| `stdout`        | 进程的标准输出流                         | `print(proc.stdout.read())`                       |
| `stderr`        | 进程的标准错误流                         | `errors = proc.stderr.read()`                     |

#### 常用参数说明（适用于 run() 和 Popen()）

| 参数      | 说明                            | 示例值                                    |
| :-------- | :------------------------------ | :---------------------------------------- |
| `args`    | 命令（列表或字符串）            | `["ls", "-l"]` 或 `"ls -l"`               |
| `stdin`   | 标准输入配置                    | `subprocess.PIPE`（管道）、`None`（继承） |
| `stdout`  | 标准输出配置                    | `subprocess.PIPE`、`open('log.txt', 'w')` |
| `stderr`  | 标准错误配置                    | `subprocess.STDOUT`（合并到stdout）       |
| `shell`   | 是否通过Shell执行               | `True`（支持字符串命令）                  |
| `cwd`     | 工作目录路径                    | `"/tmp"`                                  |
| `env`     | 自定义环境变量                  | `{"PATH": "/usr/bin"}`                    |
| `timeout` | 超时时间（秒）                  | `30`                                      |
| `text`    | 输入/输出是否为字符串（非字节） | `True`                                    |



## queue 模块

在 Python 中，`queue` 模块提供了一个线程安全的队列实现，用于在多线程编程中安全地传递数据。

队列是一种先进先出（FIFO）的数据结构，`queue` 模块提供了多种队列类型，包括 `Queue`、`LifoQueue` 和 `PriorityQueue`，以满足不同的需求。

------

### 队列类型

#### 1. Queue

`Queue` 是 `queue` 模块中最常用的队列类型，它实现了标准的先进先出（FIFO）队列。以下是 `Queue` 的基本用法：

```python
import queue

# 创建一个队列
q = queue.Queue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 1
print(q.get())  # 输出: 2
print(q.get())  # 输出: 3
```

#### 2. LifoQueue

`LifoQueue` 是一种后进先出（LIFO）的队列，类似于栈。以下是 `LifoQueue` 的基本用法：

```python
import queue

# 创建一个 LIFO 队列
q = queue.LifoQueue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 3
print(q.get())  # 输出: 2
print(q.get())  # 输出: 1
```

#### 3. PriorityQueue

`PriorityQueue` 是一种优先级队列，元素按照优先级顺序被取出。以下是 `PriorityQueue` 的基本用法：

```python
import queue

# 创建一个优先级队列
q = queue.PriorityQueue()

# 向队列中添加元素，元素为元组 (优先级, 数据)
q.put((3, 'Low priority'))
q.put((1, 'High priority'))
q.put((2, 'Medium priority'))

# 从队列中获取元素
print(q.get())  # 输出: (1, 'High priority')
print(q.get())  # 输出: (2, 'Medium priority')
print(q.get())  # 输出: (3, 'Low priority')
```

------

### 常用方法

| 方法                                  | 作用                   | 行为说明                                                     | 示例             |
| ------------------------------------- | ---------------------- | ------------------------------------------------------------ | ---------------- |
| `put(item, block=True, timeout=None)` | 向队列中放入元素       | 队列满时：• `block=True` → 阻塞等待空位（可设置超时）• `block=False` → 直接报错 | `q.put("A")`     |
| `get(block=True, timeout=None)`       | 从队列中取出并删除元素 | 队列空时：• `block=True` → 阻塞等待元素（可设置超时）• `block=False` → 直接报错 | `item = q.get()` |
| `qsize()`                             | 返回队列当前元素数量   | 只是“估计值”，在多线程环境下不完全精确                       | `q.qsize()`      |
| `empty()`                             | 判断队列是否为空       | 为空返回 `True`，否则 `False`                                | `q.empty()`      |
| `full()`                              | 判断队列是否已满       | 达到 `maxsize` 返回 `True`                                   | `q.full()`       |

------

### 线程安全

`queue` 模块的所有队列类型都是线程安全的，这意味着多个线程可以安全地同时操作同一个队列，而不需要额外的同步机制。这使得 `queue` 模块成为多线程编程中传递数据的理想选择。

------

### 示例：多线程队列

以下是一个使用 `Queue` 在多线程之间传递数据的示例：

```python
import queue
import threading
import time

# 创建一个队列
q = queue.Queue()

# 生产者线程
def producer():
    for i in range(5):
        print(f'生产 {i}')
        q.put(i)
        time.sleep(1)

# 消费者线程
def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f'消费 {item}')
        q.task_done()

# 启动生产者线程
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# 启动消费者线程
consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

# 等待生产者线程完成
producer_thread.join()

# 等待队列中的所有任务完成
q.join()

# 发送结束信号
q.put(None)
consumer_thread.join()
```

------

### 常用的属性和方法

以下是 Python queue 模块（线程安全队列）的常用类、方法及属性的表格说明，包含功能描述和示例：

#### queue 模块核心类

| 类                        | 说明                            | 适用场景             |
| :------------------------ | :------------------------------ | :------------------- |
| **`queue.Queue`**         | 先进先出（FIFO）队列            | 通用任务队列         |
| **`queue.LifoQueue`**     | 后进先出（LIFO）队列（类似栈）  | 需要后进先出的场景   |
| **`queue.PriorityQueue`** | 优先级队列（最小堆实现）        | 按优先级处理任务     |
| **`queue.SimpleQueue`**   | 更简单的FIFO队列（Python 3.7+） | 不需要高级功能的场景 |

#### 通用方法（所有队列类都支持）

| 方法              | 说明                         | 示例               | 返回值         |
| :---------------- | :--------------------------- | :----------------- | :------------- |
| **`put(item)`**   | 放入元素                     | `q.put("task1")`   | None           |
| **`get()`**       | 取出并移除元素               | `item = q.get()`   | 队列元素       |
| **`empty()`**     | 判断队列是否为空             | `if q.empty():`    | `True`/`False` |
| **`full()`**      | 判断队列是否已满             | `if q.full():`     | `True`/`False` |
| **`qsize()`**     | 返回队列当前大小             | `size = q.qsize()` | 整数           |
| **`task_done()`** | 标记任务完成（用于`join()`） | `q.task_done()`    | None           |
| **`join()`**      | 阻塞直到所有任务完成         | `q.join()`         | None           |

#### 阻塞控制参数

| 参数      | 说明                    | 默认值 | 示例                  |
| :-------- | :---------------------- | :----- | :-------------------- |
| `block`   | 当队列为空/满时是否阻塞 | `True` | `q.get(block=False)`  |
| `timeout` | 阻塞超时时间（秒）      | `None` | `q.put(x, timeout=5)` |

#### PriorityQueue 专用用法

```python
import queue, threading

q = queue.Queue(maxsize=3)  # 容量为3的队列

def producer():
    for i in range(5):
        q.put(f"Task-{i}")
        print(f"Produced: Task-{i}")

def consumer():
    while True:
        item = q.get()
        print(f"Consumed: {item}")
        q.task_done()

threading.Thread(target=producer, daemon=True).start()
threading.Thread(target=consumer, daemon=True).start()
q.join()  # 等待所有任务完成
```

## Pickle 模块

在 Python 开发中，我们经常需要把运行时的对象保存下来，或者在程序重启后恢复之前的状态，例如：

- 将计算结果缓存到磁盘，避免重复计算
- 保存用户配置、程序中间状态
- 在不同 Python 进程之间传递复杂对象

`pickle` 模块正是 Python 为解决这类问题提供的**官方内置方案**。

Python 的 `pickle` 模块是一个用于序列化和反序列化 Python 对象的标准库模块。

在开始使用 Pickle 之前，需要理解两个核心概念：

- 序列化（Pickling）：将 Python 对象转换为字节序列
- 反序列化（Unpickling）：将字节序列转换回 Python 对象

`pickle` 模块可以将几乎所有的 Python 对象（如列表、字典、类实例等）保存到文件中，或者通过网络传输，然后在需要时重新加载。

### 为什么使用 Pickle 模块？

1. **数据持久化**：将 Python 对象保存到文件中，以便在程序关闭后仍然可以访问这些数据。
2. **数据传输**：通过网络传输 Python 对象，例如在分布式系统中传递数据。
3. **快速存储和加载**：`pickle` 模块可以高效地处理复杂的数据结构，适合需要快速存储和加载的场景。

### Pickle 的典型使用场景

`pickle` 非常适合以下场景：

1. 本地数据持久化
2. 程序运行状态保存与恢复
3. 中间计算结果缓存
4. Python 进程间通信（IPC）
5. 机器学习模型、特征数据的保存

不适合的场景：

- 跨语言数据交换
- 前后端接口数据传输
- 不可信数据源的反序列化

#### Pickle 支持哪些对象？

##### 1. 支持的对象类型

| 类型                      | 是否支持 |
| :------------------------ | :------- |
| int / float / bool / str  | 支持     |
| list / tuple / dict / set | 支持     |
| None                      | 支持     |
| 自定义类实例              | 支持     |
| 嵌套结构                  | 支持     |

##### 不支持或不推荐的对象

- 打开的文件对象
- socket、数据库连接
- 操作系统资源
- 依赖运行环境状态的对象

#### 导入模块

使用 Pickle 模块非常简单，只需要导入即可：

```python
import pickle
```

------

### Pickle 模块的基本用法

#### 1. 序列化对象

使用 `pickle.dump()` 方法可以将 Python 对象序列化并保存到文件中。

```python
import pickle

# 创建一个 Python 对象
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'traveling']
}

# 将对象序列化并保存到文件
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
```

- `'wb'` 表示以二进制写模式打开文件。
- `pickle.dump()` 将 `data` 对象序列化并写入文件。

#### 2. 反序列化对象

使用 `pickle.load()` 方法可以从文件中加载并反序列化 Python 对象。

```python
import pickle

# 从文件中加载并反序列化对象
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
```

- `'rb'` 表示以二进制读模式打开文件。
- `pickle.load()` 从文件中读取字节流并反序列化为 Python 对象。

#### 3.序列化到字节串

如果不想保存到文件，可以使用 pickle.dumps() 将对象序列化为字节串：

```python
import pickle
data = [1, 2, 3, 4, 5]

# 序列化为字节串
byte_data = pickle.dumps(data)
print(byte_data)
# 输出类似: b'\x80\x04\x95\x0f\x00\x00\x00...'
```

#### 4. 从字节串反序列化

使用 pickle.loads() 可以从字节串反序列化对象：

```python
import pickle

byte_data = b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

# 从字节串反序列化
original_data = pickle.loads(byte_data)
print(original_data)
# 输出: [1, 2, 3, 4, 5]
```

#### 5. 可以序列化的对象类型

Pickle 可以序列化大多数 Python 对象，包括：

- 基本数据类型：整数、浮点数、字符串、布尔值、None
- 集合类型：列表、元组、字典、集合
- 自定义类的实例
- 函数和类（有一定限制）

```python
import pickle

# 序列化不同类型的数据
numbers = [1, 2, 3]
text = "Hello, Pickle"
dictionary = {'key': 'value'}
tuple_data = (1, 2, 3)
set_data = {1, 2, 3}

# 将所有数据放入一个列表
all_data = [numbers, text, dictionary, tuple_data, set_data]

# 序列化
with open('mixed_data.pkl', 'wb') as f:
    pickle.dump(all_data, f)

# 反序列化
with open('mixed_data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)
```

#### 6. 序列化自定义类

Pickle 可以很好地处理自定义类的实例：

```python
import pickle

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

# 创建实例
student = Student("李四", 20, "大三")

# 序列化
with open('student.pkl', 'wb') as f:
    pickle.dump(student, f)

# 反序列化
with open('student.pkl', 'rb') as f:
    loaded_student = pickle.load(f)
    print(loaded_student)
    # 输出: Student(name=李四, age=20, grade=大三)
```

#### 7. 序列化多个对象

可以多次调用 pickle.dump() 来保存多个对象：

```python
import pickle

data1 = {'item': 'apple', 'count': 5}
data2 = ['banana', 'orange', 'grape']
data3 = 42

# 保存多个对象
with open('multiple.pkl', 'wb') as f:
    pickle.dump(data1, f)
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# 读取多个对象（顺序必须一致）
with open('multiple.pkl', 'rb') as f:
    loaded_data1 = pickle.load(f)
    loaded_data2 = pickle.load(f)
    loaded_data3 = pickle.load(f)
    
print(loaded_data1)
print(loaded_data2)
print(loaded_data3)
```

### Pickle 模块的注意事项

1. **安全性**：`pickle` 模块在反序列化时会执行任意代码，因此不要加载来自不可信来源的 `pickle` 数据，以免遭受恶意攻击。
2. **兼容性**：`pickle` 生成的字节流是 Python 特有的，不同版本的 Python 之间可能存在兼容性问题。
3. **性能**：对于大型数据集，`pickle` 的序列化和反序列化可能会比较慢，可以考虑使用更高效的序列化工具，如 `json` 或 `msgpack`。

### pickle 模块常用方法

| 方法                      | 说明                          | 示例                                                  |
| :------------------------ | :---------------------------- | :---------------------------------------------------- |
| `pickle.dump(obj, file)`  | 将对象序列化并写入文件        | `pickle.dump(data, open('data.pkl', 'wb'))`           |
| `pickle.load(file)`       | 从文件读取并反序列化对象      | `data = pickle.load(open('data.pkl', 'rb'))`          |
| `pickle.dumps(obj)`       | 将对象序列化为字节串          | `bytes_data = pickle.dumps([1, 2, 3])`                |
| `pickle.loads(bytes)`     | 从字节串反序列化对象          | `lst = pickle.loads(bytes_data)`                      |
| `pickle.HIGHEST_PROTOCOL` | 可用的最高协议版本（属性）    | `pickle.dump(..., protocol=pickle.HIGHEST_PROTOCOL)`  |
| `pickle.DEFAULT_PROTOCOL` | 默认协议版本（属性，通常为4） | `pickle.dumps(obj, protocol=pickle.DEFAULT_PROTOCOL)` |

## StringIO 模块

在 Python 中，`StringIO` 模块是一个非常有用的工具，它允许我们在内存中处理字符串，就像处理文件一样。通常情况下，我们处理文件时需要打开、读取、写入和关闭文件，而 `StringIO` 模块则提供了一种更灵活的方式，让我们可以在内存中完成这些操作，而不需要实际创建文件。

### 为什么使用 StringIO 模块？

1. **内存效率**：`StringIO` 模块在内存中操作字符串，避免了频繁的磁盘 I/O 操作，提高了程序的运行效率。
2. **灵活性**：它允许我们像操作文件一样操作字符串，非常适合需要临时存储和处理字符串的场景。
3. **测试和调试**：在编写测试代码时，`StringIO` 可以模拟文件对象，方便我们进行单元测试和调试。

------

### 如何使用 StringIO 模块？

#### 导入 StringIO 模块

在 Python 3 中，`StringIO` 模块位于 `io` 模块中，因此我们需要从 `io` 模块中导入它：

`from io import StringIO`

```python
# 创建 StringIO 对象
string_io = StringIO()

# 写入数据
string_io.write("Hello, World!")

# 读取数据
data = string_io.getvalue()
print(data)  # 输出: Hello, World!

# 移动指针
string_io.seek(0)  # 将指针移动到开头

# 读取一行数据
line = string_io.readline()
print(line)  # 输出: Hello, World!

string_io.close()
```

### 实际应用示例

#### 示例 1：模拟文件操作

```python
from io import StringIO

# 创建 StringIO 对象
string_io = StringIO()

# 写入数据
string_io.write("Python is awesome!\n")
string_io.write("StringIO is useful!")

# 移动指针到开头
string_io.seek(0)

# 读取数据
print(string_io.read())

# 关闭 StringIO 对象
string_io.close()
```

#### 示例 2：单元测试中的使用

在单元测试中，`StringIO` 可以用于模拟文件对象，方便我们测试代码的输入输出。

```python
from io import StringIO
import unittest

def process_input(input_data):
    return input_data.upper()

class TestProcessInput(unittest.TestCase):
    def test_process_input(self):
        input_data = "hello"
        expected_output = "HELLO"
        
        # 使用 StringIO 模拟输入
        input_stream = StringIO(input_data)
        result = process_input(input_stream.read())
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
```

------

### 常用类、方法和函数

以下是 `StringIO` 模块中常用的属性和方法，以表格形式列出：

| **属性/方法**            | **描述**                                                     |
| :----------------------- | :----------------------------------------------------------- |
| `StringIO()`             | 创建一个 `StringIO` 对象，可以传入初始字符串作为参数。       |
| `write(s)`               | 将字符串 `s` 写入 `StringIO` 对象。                          |
| `read([size])`           | 从 `StringIO` 对象中读取最多 `size` 个字符。如果未指定 `size`，则读取全部内容。 |
| `readline([size])`       | 从 `StringIO` 对象中读取一行，最多读取 `size` 个字符。       |
| `readlines([sizehint])`  | 从 `StringIO` 对象中读取所有行，并返回一个列表。`sizehint` 用于限制读取的字符数。 |
| `getvalue()`             | 返回 `StringIO` 对象中的所有内容，作为一个字符串。           |
| `seek(offset[, whence])` | 移动文件指针到指定位置。`offset` 是偏移量，`whence` 是参考位置（0：文件开头，1：当前位置，2：文件末尾）。 |
| `tell()`                 | 返回当前文件指针的位置。                                     |
| `truncate([size])`       | 截断 `StringIO` 对象的内容到指定大小。如果未指定 `size`，则截断到当前文件指针位置。 |
| `close()`                | 关闭 `StringIO` 对象，释放资源。                             |
| `closed`                 | 返回一个布尔值，表示 `StringIO` 对象是否已关闭。             |



## logging 模块

在编程中，日志记录（logging）是一种非常重要的工具，它可以帮助我们跟踪程序的运行状态、调试错误以及记录重要信息。

Python 提供了一个内置的 `logging` 模块，专门用于处理日志记录任务。与简单的 `print` 语句相比，`logging` 模块更加灵活和强大，能够满足不同场景下的日志需求。

### 为什么使用 logging 模块？

1. **灵活性**：`logging` 模块允许你根据需要设置日志的级别、格式和输出位置。
2. **可扩展性**：你可以轻松地将日志输出到文件、控制台、网络等不同的目标。
3. **结构化日志**：`logging` 模块支持结构化日志记录，便于后续的分析和处理。
4. **性能优化**：与 `print` 相比，`logging` 模块在性能上进行了优化，适合在生产环境中使用。

------

### logging 模块的基本用法

#### 1. 导入 logging 模块

首先，我们需要导入 `logging` 模块：`**import** logging`

#### 2. 配置日志级别

日志级别用于控制日志的详细程度。`logging` 模块提供了以下几种日志级别：

- **DEBUG**：详细的调试信息，通常用于开发阶段。
- **INFO**：程序正常运行时的信息。
- **WARNING**：表示潜在的问题，但程序仍能正常运行。
- **ERROR**：表示程序中的错误，导致某些功能无法正常工作。
- **CRITICAL**：表示严重的错误，可能导致程序崩溃。

你可以通过以下代码设置日志级别：

`logging.basicConfig(level=logging.DEBUG)`

#### 3. 记录日志

设置好日志级别后，你可以使用以下方法记录日志：

```python
logging.debug("这是一条调试信息")
logging.info("这是一条普通信息")
logging.warning("这是一条警告信息")
logging.error("这是一条错误信息")
logging.critical("这是一条严重错误信息")
```

#### 4. 日志输出格式

你可以通过 `basicConfig` 方法自定义日志的输出格式。例如：

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
```

#### 5. 将日志输出到文件

默认情况下，日志会输出到控制台。如果你希望将日志保存到文件中，可以这样配置：

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log"
)
```

------

### logging 模块的高级用法

#### 1. 使用多个日志记录器

在大型项目中，你可能需要为不同的模块或组件创建独立的日志记录器。可以通过以下方式实现：

```python
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler("my_logger.log")
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug("这是一条调试信息")
logger.info("这是一条普通信息")
```

#### 2. 日志过滤器

你可以通过过滤器来控制哪些日志需要被记录。例如：

```python
class MyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

logger.addFilter(MyFilter())
```

#### 3. 日志轮转

当日志文件过大时，可以使用 `RotatingFileHandler` 或 `TimedRotatingFileHandler` 实现日志轮转：

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=1024, backupCount=3)
logger.addHandler(handler)
```

------

### logging 模块常用的属性和方法

#### 1. 核心类

| 类                      | 说明                                                         | 示例                                                         |
| :---------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **`logging.Logger`**    | 记录器，用于发出日志消息（通过 `logging.getLogger(name)` 获取） | `logger = logging.getLogger("my_logger")`                    |
| **`logging.Handler`**   | 处理器，决定日志输出位置（如文件、控制台等）                 | `handler = logging.FileHandler("app.log")`                   |
| **`logging.Formatter`** | 格式化器，控制日志输出的格式                                 | `formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')` |
| **`logging.Filter`**    | 过滤器，用于更精细地控制日志记录                             | `filter = logging.Filter("module.name")`                     |

#### 2. Logger 对象常用方法

| 方法                             | 说明                                               | 示例                             |
| :------------------------------- | :------------------------------------------------- | :------------------------------- |
| **`logger.setLevel(level)`**     | 设置日志级别（如 `logging.DEBUG`、`logging.INFO`） | `logger.setLevel(logging.DEBUG)` |
| **`logger.debug(msg)`**          | 记录 DEBUG 级别日志                                | `logger.debug("调试信息")`       |
| **`logger.info(msg)`**           | 记录 INFO 级别日志                                 | `logger.info("程序启动")`        |
| **`logger.warning(msg)`**        | 记录 WARNING 级别日志                              | `logger.warning("磁盘空间不足")` |
| **`logger.error(msg)`**          | 记录 ERROR 级别日志                                | `logger.error("操作失败")`       |
| **`logger.critical(msg)`**       | 记录 CRITICAL 级别日志                             | `logger.critical("系统崩溃")`    |
| **`logger.addHandler(handler)`** | 添加处理器                                         | `logger.addHandler(handler)`     |
| **`logger.addFilter(filter)`**   | 添加过滤器                                         | `logger.addFilter(filter)`       |

#### 3. Handler 常用类型

| Handler 类型                   | 说明                 | 示例                                                         |
| :----------------------------- | :------------------- | :----------------------------------------------------------- |
| **`StreamHandler`**            | 输出到流（如控制台） | `handler = logging.StreamHandler()`                          |
| **`FileHandler`**              | 输出到文件           | `handler = logging.FileHandler("app.log")`                   |
| **`RotatingFileHandler`**      | 按文件大小分割日志   | `handler = logging.RotatingFileHandler("app.log", maxBytes=1e6, backupCount=3)` |
| **`TimedRotatingFileHandler`** | 按时间分割日志       | `handler = logging.TimedRotatingFileHandler("app.log", when="midnight")` |
| **`SMTPHandler`**              | 通过邮件发送日志     | `handler = logging.SMTPHandler("mail.example.com", "from@example.com", "to@example.com", "Error Log")` |

#### 4. 日志级别（常量）

| 级别           | 数值 | 说明                           |
| :------------- | :--- | :----------------------------- |
| **`CRITICAL`** | 50   | 严重错误，程序可能无法继续运行 |
| **`ERROR`**    | 40   | 错误，但程序仍可运行           |
| **`WARNING`**  | 30   | 警告信息（默认级别）           |
| **`INFO`**     | 20   | 程序运行信息                   |
| **`DEBUG`**    | 10   | 调试信息                       |
| **`NOTSET`**   | 0    | 继承父记录器的级别             |

#### 5. Formatter 常用格式字段

| 字段            | 说明             | 示例输出                  |
| :-------------- | :--------------- | :------------------------ |
| `%(asctime)s`   | 日志创建时间     | `2023-01-01 12:00:00,123` |
| `%(levelname)s` | 日志级别名称     | `INFO`                    |
| `%(message)s`   | 日志消息内容     | `程序启动成功`            |
| `%(name)s`      | 记录器名称       | `my_logger`               |
| `%(filename)s`  | 生成日志的文件名 | `app.py`                  |
| `%(lineno)d`    | 生成日志的行号   | `42`                      |
| `%(funcName)s`  | 生成日志的函数名 | `main`                    |

#### 6. 快速配置方法

| 方法                        | 说明                                                 | 示例                                                         |
| :-------------------------- | :--------------------------------------------------- | :----------------------------------------------------------- |
| **`logging.basicConfig()`** | 一键配置日志级别、处理器和格式（通常在程序入口调用） | `logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')` |

**常用参数**：

- `level`：设置根记录器级别
- `filename`：输出到文件
- `filemode`：文件模式（如 `'w'` 覆盖）
- `format`：格式字符串
- `datefmt`：日期格式（如 `"%Y-%m-%d %H:%M:%S"`）

# 通信

## SMTP发送邮件

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

https://www.runoob.com/python3/python3-smtp.html

# 可视化 & 数据分析

## pyecharts库

pyecharts 是一个基于 ECharts 的 Python 数据可视化库，它允许用户使用 Python 语言生成各种类型的交互式图表和数据可视化。

ECharts 是一个使用 JavaScript 实现的开源可视化库，而 Pyecharts 则是 ECharts 的 Python 封装，使得在 Python 中使用 ECharts 变得更加方便。

pyecharts 提供了一组简单而灵活的 API，使用户能够轻松地创建各种图表，包括但不限于折线图、柱状图、散点图、饼图、地图等。

通过 pyecharts，用户可以使用 Python 语言处理和准备数据，然后使用简洁的代码生成交互式的图表，这些图表可以嵌入到 Web 应用程序中或保存为静态文件。

**pyecharts 特点与功能：**

- **简单易用：** Pyecharts 提供了直观而友好的 API，使得用户能够快速上手，轻松生成各种图表。
- **丰富的图表类型：** 支持多种常见的图表类型，包括线图、柱状图、散点图、饼图、地图等，满足不同场景的需求。
- **支持主流数据格式：** 能够处理常见的数据格式，如列表、字典、Pandas DataFrame 等。
- **交互性：** 生成的图表可以具有交互性，用户可以通过鼠标悬停、缩放等方式与图表进行互动。
- **丰富的配置选项：** 提供了丰富的配置选项，允许用户自定义图表的样式、布局等属性。
- **支持主题：** 提供多种主题，用户可以根据需要选择合适的主题，使图表更符合应用的整体风格。

## statistics 模块

在数据分析和科学计算中，统计学是一个非常重要的工具。

Python 提供了一个内置的 `statistics` 模块，专门用于处理基本的统计计算。本文将详细介绍 `statistics` 模块的功能和使用方法，帮助初学者快速掌握如何使用这个模块进行基本的统计分析。

`statistics` 模块提供了许多常用的统计函数，如均值、中位数、方差、标准差等。

### statistics 模块方法

| 方法                                                         | 描述                                                     |
| :----------------------------------------------------------- | :------------------------------------------------------- |
| [statistics.harmonic_mean()](https://www.runoob.com/python3/ref-stat-harmonic_mean.html) | 计算给定数据集的调和平均值。                             |
| [statistics.mean()](https://www.runoob.com/python3/ref-stat-mean.html) | 计算数据集的平均值                                       |
| [statistics.median()](https://www.runoob.com/python3/ref-stat-median.html) | 计算数据集的中位数                                       |
| [statistics.median_grouped()](https://www.runoob.com/python3/ref-stat-median_grouped.html) | 计算给定分组数据集的分组中位数                           |
| [statistics.median_high()](https://www.runoob.com/python3/ref-stat-median_high.html) | 计算给定数据集的高位中位数                               |
| [statistics.median_low()](https://www.runoob.com/python3/ref-stat-median_low.html) | 计算给定数据集的低位中位数。                             |
| [statistics.mode()](https://www.runoob.com/python3/ref-stat-mode.html) | 算数据集的众数（出现频率最高的值）                       |
| [statistics.pstdev()](https://www.runoob.com/python3/ref-stat-pstdev.html) | 计算给定数据集的样本标准偏差                             |
| [statistics.stdev()](https://www.runoob.com/python3/ref-stat-stdev.html) | 计算数据集的标准差                                       |
| [statistics.pvariance()](https://www.runoob.com/python3/ref-stat-pvariance.html) | 计算给定数据集的样本方差                                 |
| [statistics.variance()](https://www.runoob.com/python3/ref-stat-variance.html) | 计算数据集的方差                                         |
| [statistics.quantiles()](https://www.runoob.com/python3/ref-stat-quantiles.html) | 计算数据集的分位数，可指定分位数的数量（默认为四分位数） |

