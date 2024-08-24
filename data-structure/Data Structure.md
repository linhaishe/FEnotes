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

study video: https://www.bilibili.com/video/BV1x7411L7Q7?p=13&vd_source=5d5cb2062ab059c137f6aa8f9809b93c

# 线性结构

## array / 数组

数组是一种线性结构，并且可以在数组的任意位置差如何删除数据。

数组在JS中的方法被封装的非常完善，查看API文档即可。

普通语言的数组封装 (比如Java的数组列表)

1. 常见语言的数组不能存放不同的数据类型，因此所有在封装时通常存放在数组中的是Object类型
2. 常见语言的数组容量不会自动改变(需要进行扩容操作)
3. 常见语言的数组进行中间插入和删除操作性能比较低.

## stack / 栈

There are two data structures that have some similarities to arrays, but which give us more control over the addition and removal of elements. These data structures are **stacks** and **queues**. 

我们为了实现某些功能，必须对数组的任意性插入和任意性删除加以限制，从而产生的具有限制性的线性结构，则为栈和队列。

A stack is an ordered collection of items that follows the last in, first out **(LIFO)** principle.后进先出

![Lightbox](https://s2.loli.net/2024/08/19/fxFAzsd7mhbZUSJ.png)

栈举例： 递归 - 递归容易出现栈溢出，如果没有做break

**Creating an array-based Stack class**

https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Fstack-array-based.js

```js
export default class StackArray {
  constructor() {
    this.items = [];
  }
  // 添加一个新元素到栈顶的位置
  push(element) {
    this.items.push(element);
  }
  // 从栈中取出元素
  pop() {
    return this.items.pop();
  }

  // 查看栈顶元素，不对栈做任何的修改
  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

  clear() {
    this.items = [];
  }

  toArray() {
    return this.items;
  }

  toString() {
    return this.items.toString();
  }
}

```

**Creating a JavaScript object-based** **Stack class**

https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Fstack-object-based.js

```js
// @ts-check

export default class Stack {
  // JavaScript object-based Stack class
  constructor() {
    this.count = 0;
    this.items = {};
  }
  // 添加元素到栈顶
  push(element) {
    this.items[this.count] = element;
    this.count++;
  }
  // 删除栈顶元素
  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }
  // 返回栈顶元素
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }
  // 栈是否为空
  isEmpty() {
    return this.count === 0;
  }
  // 栈里的元素个数
  size() {
    return this.count;
  }
  // 清空栈
  clear() {
    this.items = {};
    this.count = 0;
  }
  // 将栈结构的内容以字符形式返回
  toString() {
    if (this.isEmpty()) {
      return '';
    }
    let objString = `${this.items[0]}`;
    for (let i = 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

```

## queue / 队列

### inro

A queue is an ordered collection of items that follows the first in, first out (FIFO), also known as the first come, first served, principle. 

先进先出，尾进端出。

![image-20240824190221630](https://s2.loli.net/2024/08/24/PnxRhYaW8OZrAIM.png)

```js
export default function Queue() {
  this.items = [];
}

Queue.prototype.enqueue = function (element) {
  this.items.push(element);
};

Queue.prototype.dequeue = function () {
  return this.items.shift();
};

Queue.prototype.peek = function () {
  return this.items[0];
};

Queue.prototype.isEmpty = function () {
  return this.items.length === 0;
};

Queue.prototype.size = function () {
  return this.items.length;
};

Queue.prototype.toString = function () {
  let resultString = '';
  for (let i = 0; i < this.items.length; i++) {
    resultString += `${this.items[i]}`;
  }

  return resultString;
};

```

### deque / Double-ended queue / 双端队列

> The deque data structure, also known as the double-ended queue, is a special queue that allows us to insert and remove elements from the end or from the front of the queue.
>
> 双端队列是一种具有队列和栈性质的抽象数据类型。双端队列中的元素可以从两端弹出，插入和删除操作限定在队列的两边进行。

the deque implements both principles, FIFO and LIFO, we can also say that the deque is a merger between the queue and the stack data structures.

![image-20240824212252654](https://s2.loli.net/2024/08/24/hO59oZmFtAXxvHC.png)

```js
// @ts-check

export default class Deque {
  constructor() {
    this.count = 0;
    this.lowestCount = 0;
    this.items = {};
  }

  addFront(element) {
    if (this.isEmpty()) {
      this.addBack(element);
    } else if (this.lowestCount > 0) {
      this.lowestCount--;
      this.items[this.lowestCount] = element;
    } else {
      for (let i = this.count; i > 0; i--) {
        this.items[i] = this.items[i - 1];
      }
      this.count++;
      this.items[0] = element;
    }
  }

  addBack(element) {
    this.items[this.count] = element;
    this.count++;
  }

  removeFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  removeBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }

  peekFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }

  peekBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }

  isEmpty() {
    return this.size() === 0;
  }

  clear() {
    this.items = {};
    this.count = 0;
    this.lowestCount = 0;
  }

  size() {
    return this.count - this.lowestCount;
  }

  toString() {
    if (this.isEmpty()) {
      return '';
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

```

### priority queue / 优先级队列

A **priority queue** is a type of queue that arranges elements based on their priority values. 

优先队列是计算机科学中的一类抽象数据类型。优先队列中的每个元素都有各自的优先级，优先级最高的元素最先得到服务；优先级相同的元素按照其在优先队列中的顺序得到服务。优先队列通常使用“堆”实现。

There are several ways to implement a priority queue, including using an array, linked list, heap, or binary search tree, [binary heap](https://www.geeksforgeeks.org/binary-heap/) being the most common method to implement. heap的实现方式之后再展开。此处使用array的方式处理。

实现优先级队列相对队列主要有两方面需要考虑: 

1. 封装元素和优先级放在一起(可以封装一个新的构造函数
2. 添加元素时，将新插入元素的优先级和队列中已经存在的元素优先级进行比较,以获得自己正确的位置

```js
// 优先级队列 priorityQueue
import Queue from './queue-array-based.js';

// 定义PriorityQueue类
export default function PriorityQueue() {
  // 使用Queue类的构造函数初始化items
  Queue.call(this);
}

// 设置原型链继承Queue类的方法
PriorityQueue.prototype = Object.create(Queue.prototype);
PriorityQueue.prototype.constructor = PriorityQueue;

// 重写enqueue方法，实现带优先级的插入
PriorityQueue.prototype.enqueue = function (element, priority) {
  function QueueElement(element, priority) {
    this.element = element;
    this.priority = priority;
  }

  const queueElement = new QueueElement(element, priority);
  let added = false;

  for (let i = 0; i < this.items.length; i++) {
    if (queueElement.priority < this.items[i].priority) {
      this.items.splice(i, 0, queueElement);
      added = true;
      break;
    }
  }

  if (!added) {
    this.items.push(queueElement);
  }
};

```

### 队列的应用

- 线程队列：
  在开发中,为了让任务可以并行处理,通常会开启多个线程。但是，我们不能让大量的线程同时运行处理任务.(占用过多的资源)。这个时候，如果有需要开启线程处理任务的情况，我们就会使用线程队列。线程队列会依照次序来启动线程，并且处理对应的任务
