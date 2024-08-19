# Data Structure

https://miro.com/app/board/uXjVPEXED68=/

![数据结构](https://s2.loli.net/2024/08/19/ERPlonh46yDUFNO.jpg)

# 数据结构/算法定义

> *A data structure is a way of organizing and storing data in a computer so that it can be accessed and used efficiently. It refers to the logical or mathematical representation of data, as well as the implementation in a computer program.*
>
> 计算机中存储、组织数据的方式。

> *The word* [***\*Algorithm\****](https://www.geeksforgeeks.org/fundamentals-of-algorithms) *means ”* **A set of finite rules or instructions to be followed in calculations or other problem-solving operations** *”*
> *Or**”* **A procedure for solving a mathematical problem in a finite number of steps that frequently involves recursive operations”***.*
>
> An [algorithm](https://www.techtarget.com/searchenterpriseai/definition/clustering-in-machine-learning) is a procedure used for solving a problem or performing a computation. Algorithms act as an exact list of instructions that conduct specified actions step by step in either hardware- or software-based routines.
>
> 解决问题的办法/步骤逻辑。

all source code in: https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Findex.js

# 线性结构

## 数组

数组是一种线性结构，并且可以在数组的任意位置差如何删除数据。

数组在JS中的方法被封装的非常完善，查看API文档即可。

普通语言的数组封装 (比如Java的数组列表)

1. 常见语言的数组不能存放不同的数据类型，因此所有在封装时通常存放在数组中的是Object类型
2. 常见语言的数组容量不会自动改变(需要进行扩容操作)
3. 常见语言的数组进行中间插入和删除操作性能比较低.

## 栈

There are two data structures that have some similarities to arrays, but which give us more control over the addition and removal of elements. These data structures are **stacks** and **queues**. 

我们为了实现某些功能，必须对数组的任意性插入和任意性删除加以限制，从而产生的具有限制性的线性结构，则为栈和队列。

A stack is an ordered collection of items that follows the last in, first out **(LIFO)** principle.后进先出

![Lightbox](https://s2.loli.net/2024/08/19/fxFAzsd7mhbZUSJ.png)

栈举例： 递归 - 递归容易出现栈溢出，如果没有做break

**Creating an array-based Stack class** 

**Creating a JavaScript object-based** **Stack class** 

## 队列

## 链表















