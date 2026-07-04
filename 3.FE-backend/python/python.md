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

```text
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

```text
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

```text
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

```text
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

```html
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

```text
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

```
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print (list[2])
print (list[2:3])
```

这两句话打印的内容其实是一样的:

```
2.23
[2.23]
```

但注意是不同的类型，用变量接收一下：

```
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

```
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
```

如果你想创建只有一个元素的元组，需要在元素后面添加一个逗号，以区分它是元组而不是普通的值。因为在没有逗号的情况下，Python 会将括号解释为数学运算中的括号：

```
not_a_tuple = (42)  # 这是整数 42，不是元组
```

# 8. Set（集合）

Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

在 Python 中，集合使用大括号 **{}** 表示，元素之间用逗号 **,** 分隔。也可以使用 **set()** 函数创建集合。

> **注意：**创建一个空集合必须用 **set()** 而不是 **{}**，因为 **{}** 创建的是一个空字典。

创建格式：

```
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

# 10. 条件控制

### 条件判断关键字

| 关键字 / 函数 | 说明                                        | 示例                   |
| :------------ | :------------------------------------------ | :--------------------- |
| `if`          | 条件判断语句，当条件为 True 时执行代码块    | `if x > 0:`            |
| `elif`        | 多条件判断分支（else if）                   | `elif x == 0:`         |
| `else`        | 所有条件不满足时执行                        | `else:`                |
| `pass`        | 空语句，占位用，保证语法完整                | `if x > 0: pass`       |
| `match`       | 结构化模式匹配（Python 3.10+，类似 switch） | `match x: case 1: ...` |

```
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

```
while 判断条件(condition)：
    执行语句(statements)……
```

```
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

```
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

```
#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

```
flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")
```

**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。

## for 语句

```
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

```
#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)
```

```
#!/usr/bin/python3
 
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)
```

## for...else

```
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
```

```
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

```
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

```
>>>for i in range(0, 10, 3) :
    print(i)
 
    
0
3
6
9
>>>
```

```
>>>for i in range(-10, -100, -30) :
    print(i)
 
    
-10
-40
-70
>>>
```

```
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

```
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
```

```
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

```
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

````
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
0 1 1 2 3 5 8 13 21 34 55
```

# ==with==

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

```
with expression [as variable]:
  # 代码块
```

- `expression` 返回一个支持上下文管理协议的对象
- `as variable` 是可选的，用于将表达式结果赋值给变量
- 代码块执行完毕后，自动调用清理方法

### 文件操作示例

最常见的 `with` 语句应用是文件操作：

```
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

![img](https://www.runoob.com/wp-content/uploads/2025/06/python-with-runoob2.png)

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

```
def 函数名（参数列表）:
    函数体
```

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

```
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

```
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

在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

```
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

```
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)
```

以上输出结果为：

```
4379369136
4379369136
4379369424
```

可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

### 传可变对象

可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

```
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

```
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

```
def add(a, b):
    print(a, b)
    
add(1, 2) # 按位置传
```



### 必需参数

必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

```
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

```
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

```
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

```
名字:  runoob
年龄:  50
```

### 默认参数

调用函数时，如果没有传递参数，则会使用默认参数。以下中如果没有传入 age 参数，则使用默认值：

```
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

```
名字:  runoob
年龄:  50
------------------------
名字:  runoob
年龄:  35
```

### 不定长参数(*vartuple)

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

```
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```
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

```
输出: 
70
(60, 50)
```

如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下：

```
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

```
输出:
10
输出:
70
60
50
```

### 两个星号 **

还有一种就是参数带两个星号 **基本语法如下：

```
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了两个星号 *\* 的参数会以字典的形式导入。

```
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

```
输出: 
1
{'a': 2, 'b': 3}
```

### 星号 * 单独

声明函数时，参数中星号 * 可以单独出现，例如:

```
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：

```
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

```
lambda [arg1 [,arg2,.....argn]]:expression
```

设置参数 a 加上 10:

`x = lambda a : a + 10 print(x(5))`

以上输出结果：

```
15
```

以下匿名函数设置两个参数：

```
#!/usr/bin/python3
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
```

以上输出结果：

```
相加后的值为 :  30
相加后的值为 :  40
```

我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。

以下将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：

```
def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))
```

以上输出结果：

```
22
33
```

更多匿名函数还可以参考：[Python lambda（匿名函数）](https://www.runoob.com/python3/python-lambda.html)

------

## return 语句

return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。之前的例子都没有示范如何返回数值。

```
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

```
def func(a, b, /, c):
    print(a, b, c)
```

> **a 和 b 不允许写参数名。**

正确

```
func(1, 2, 3)
```

或者

```
func(1, 2, c=3)
```

都可以。

错误

```
func(a=1, b=2, c=3)
```

### `*` —— 后面的参数必须写名字

例如：

```
def func(a, *, b):
    print(a, b)
```

这里

```
*
```

表示：

> **后面的参数必须使用关键字。**

------

正确：

```
func(1, b=2)
```

输出

```
1 2
```

------

错误：

```
func(1, 2)
```

现在来看教程里的例子：

```
def func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

可以画成这样：

```
        /
a  b    |   c  d    *    e  f
↑ ↑         ↑ ↑          ↑ ↑

只能位置     都可以      只能关键字
```

所以：

a、b

只能这样：

```
func(1, 2, ...)
```

可以：

```
func(1,2,3,4,e=5,f=6)
```

也可以：

```
func(1,2,c=3,d=4,e=5,f=6)
```

甚至：

```
func(1,2,3,d=4,e=5,f=6)
```

e、f

必须：

```
e=5
f=6
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

```
lambda arguments: expression
```

- `lambda`是 Python 的关键字，用于定义 lambda 函数。
- `arguments` 是参数列表，可以包含零个或多个参数，但必须在冒号(`:`)前指定。
- `expression` 是一个表达式，用于计算并返回函数的结果。

以下的 lambda 函数没有参数：

```
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

```
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers)) 

print(squared)  

# 输出: [1, 4, 9, 16, 25]
```

下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：


```
from functools import reduce  numbers = [1, 2, 3, 4, 5]  
# 使用 reduce() 和 lambda 函数计算乘积 
product = reduce(lambda x, y: x * y, numbers)  
print(product)  
# 输出：120
```

# 装饰器

# 数据结构

# 模块

# `__name__`

# 输入和输出

# File

# OS

# 错误和异常

# 面向对象

# 命名空间/作用域

# 虚拟环境的创建

# 类型注解

# 标准库概览

实例

测验

------

1. 高级教程
2. 正则表达式
3. CGI编程
4. MySQL(mysql-connector)
5. MySQL(PyMySQL)
6. 网络编程
7. SMTP发送邮件
8. 多线程
9. XML 解析
10. JSON
11. 日期和时间
12. 内置函数
13. MongoDB
14. urllib
15. uWSGI 安装配置
16. pip
17. operator
18. math
19. requests
20. random
21. OpenAI
22. 有用的资源
23. AI 绘画
24. statistics
25. hashlib
26. 量化
27. pyecharts
28. selenium 库
29. 爬虫
30. Scrapy 库
31. Markdown
32. sys 模块
33. Pickle 模块
34. subprocess 模块
35. queue 模块
36. StringIO 模块
37. logging 模块
38. datetime 模块
39. re 模块
40. csv 模块
41. threading 模块
42. asyncio 模块
43. PyQt
44. for 循环
45. while 循环









