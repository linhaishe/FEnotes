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

==在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：==

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

----

所以最通用的写法就是：

```
def wrapper(*args, **kwargs):
```

它能接收**任意数量的位置参数和关键字参数**，再通过：

```
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

## 函数自动触发

```

def target_function():
    print("原函数执行")


x = target_function

x()
```

```

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

```
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

```
target_function = decorator_function(target_function)
```

👉 调用 `target_function()` 时，实际上执行的是 `wrapper()`

------

### 使用装饰器

装饰器通过 **@** 语法糖应用在函数定义前：

```
@time_logger
def target_function():
    pass
```

等价于：

```
def target_function():
    pass

target_function = time_logger(target_function)
```

这种机制使我们可以在不修改原函数的情况下，统一添加功能（如日志、权限等）。

就像普通函数一样，装饰器本质上也是一个函数，所以它叫什么名字完全由你决定。

```
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

```
函数执行前
Hello!
函数执行后
```

- `my_decorator` 接收 `say_hello`
- `@my_decorator` 替换原函数

假设你写了：

```
def my_decorator(func):
    print("装饰器执行")
    return func

@my_decorator
def say_hello():
    print("Hello")
```

Python 会自动转换成：

```
def say_hello():
    print("Hello")

say_hello = my_decorator(say_hello)
```

注意这里：

```
@my_decorator
```

其实就是：

```
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

```
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

```
执行前
Hello, Alice!
执行后
```

**说明：**使用 `*args, **kwargs` 可以兼容任意参数函数。

------

## 带参数的装饰器（进阶）

```
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

```
Hello!
Hello!
Hello!
```

![img](https://www.runoob.com/wp-content/uploads/2024/03/decorators-python-2.png)

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

```
调用前
原方法
调用后
```

------

### 类形式的类装饰器

```
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

```
初始化
True
```

------

## 内置装饰器

常用内置装饰器：

1. **@staticmethod**：定义静态方法
2. **@classmethod**：定义类方法
3. **@property**：将方法变为属性

```
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

```
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

```
Decorator 1
Decorator 2
Hello!
```

------

## 核心总结

```
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

```
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

```
#!/usr/bin/python3
# 文件名: using_sys.py
 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')
```

执行结果如下所示：

```
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

```
import module1[, module2[,... moduleN]
```

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

搜索路径时一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：

support.py 文件代码

```
#!/usr/bin/python3
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return
```

test.py 引入 support 模块：

test.py 文件代码

```
#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
```

以上实例输出结果：

```
$ python3 test.py 
Hello :  Runoob
```

一个模块只会被导入一次，不管你执行了多少次 **import**。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？

这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。

### 不建议导入

Python 只是约定俗成：

```
def _helper():
    ...
```

前面加一个 `_`。

表示：

> **这是内部函数，不建议外部使用。**

但是：

```
from fibo import _helper
```

其实还是能导入。

## from … import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

```
from modname import name1[, name2[, ... nameN]]
```

例如，要导入模块 fibo 的 fib 函数，使用如下语句：

```
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

### 给模块起别名

使用 **as** 关键字为模块或函数起别名：

```
import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root
```

------

## from … import * 语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

```
from modname import *
```

这提供了一个简单的方法来导入一个模块中的所有项目。

不推荐，容易引起命名冲突。

------

## 深入模块

这段教程写得比较抽象，我用一个**真实项目例子**给你讲，你一下就能明白。

假设你的项目长这样：

```text
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

```text
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

```text
math_util 被加载了
```

只有一次。

因为：

Python 有模块缓存。

第一次：

```text
import math_util
```

流程：

```text
读取文件
    │
执行整个文件
    │
放入缓存(sys.modules)
```

第二次：

```text
import math_util
```

发现：

```text
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

```text
999
100
```

为什么？

因为：

```
main.py
```

有自己的：

```text
a = 999
math_util.py
```

也有自己的：

```text
a = 100
```

互不影响。

可以画图：

```text
main.py

a = 999
```

和

```text
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

```text
3.14
8
```

这里：

```python
math_util.PI
```

就是：

```
模块名.变量
```

而：

```python
math_util.add()
```

就是：

```
模块名.函数
```

和 JavaScript 很像：

```javascript
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

```text
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

```text
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

```text
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

```
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

运行输出如下：

```
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

```
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

```
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

```
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

```
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

```
import sound.effects.echo
```

这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

```
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

还有一种导入子模块的方法是:

```
from sound.effects import echo
```

这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

```
echo.echofilter(input, output, delay=0.7, atten=4)
```

还有一种变化就是直接导入一个函数或者变量:

```
from sound.effects.echo import echofilter
```

同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

```
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

```
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

```
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

```
__all__ = ["echo", "surround", "reverse"]
```

这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。

如果 **__all__** 真的没有定义，那么使用**from sound.effects import \***这种语法的时候，就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。

这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。看下这部分代码:

```
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

这个例子中，在执行 from...import 前，包 sound.effects 中的 echo 和 surround 模块都被导入到当前的命名空间中了。（当然如果定义了 __all__ 就更没问题了）

通常我们并不主张使用 ***** 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。

记住，使用 **from Package import specific_submodule** 这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。比如，如果模块sound.filters.vocoder 要使用包 sound.effects 中的模块 echo，你就要写成 from sound.effects import echo。

```
from . import echo
from .. import formats
from ..filters import equalizer
```

无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。

包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。

这个功能并不常用，一般用来扩展包里面的模块。

# `__name__`

```
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")
```

```
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

```
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

```
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

```
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

```
except (RuntimeError, TypeError, NameError):
    pass
```

最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

```
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

```
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

```
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

```
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

```
raise [Exception [, args [, traceback]]]
```

<img src="https://www.runoob.com/wp-content/uploads/2019/07/raise.png" alt="img" style="zoom:50%;" />

以下实例如果 x 大于 5 就触发异常:

```
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```

执行以上代码会触发异常：

```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
Exception: x 不能大于 5。x 的值为: 10
```

raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

```
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

```text
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

```text
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

```text
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

```text
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

```
for line in open("myfile.txt"):
    print(line, end="")
```

以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

```
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

```from typing import Optional
def find_student(name: str) -> Optional[str]:
    """根据名字查找学生，可能找到也可能返回None"""
    students = {"Alice": "A001", "Bob": "B002"}
    return students.get(name)  # 可能返回字符串或None

# 等价于 Union[str, None]
```

### 联合类型（Union）

```
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









