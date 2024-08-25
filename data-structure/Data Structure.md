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

## linked lists / 链表

数组的创建通常需要申请一段连续的内存空间(一整块的内存)，并且大小是固定的(大多数编程语言数组都是固定的)，所以当当前数组不能满足容量需求时，需要扩容。(一般情况下是申请一个更大的数组，比如2倍。然后将原数组中的元素复制过去)，而且在数组开头或中间位置插入数据的成本很高，需要进行大量元素的位移，尽管我们已经学过的JavaScript的Array类方法可以帮我们做这些事，但背后的原理依然是这样。

- 要存储多个元素，另外一个选择就是链表
- 但不同于数组，链表中的元素在内存中不必是连续的空间
- 链表的每个元素由一个存储元素本身的节点和一个指向下一个元素的引用(有些语言称为指针或者连接)组成

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 内存空间不是必须连续的。可以充分利用计算机的内存，实现灵活的内存动态管理 | 链表访问任何一个位置的元素时,都需要从头开始访问.(无法跳过第一个元素访问任何一个元素) |
| 链表不必在创建时就确定大小，并且大小可以无限的延伸下去       | 无法通过下标直接访问元素,需要从头一个个访问,直到找到对应的元素 |
| 链表在插入和删除数据时，时间复杂度可以达到O(1)。相对数组效率高很多 |                                                              |

### 单向链表 / Singly LinÏked List

[singly linked list code](https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Fstack-object-based.js,data-structure%2Fqueue%2Fpriority-queue.js,data-structure%2Fqueue%2Fqueue-object-based.js,data-structure%2Fqueue%2Fqueue-array-based.js,data-structure%2Fqueue%2Findex.js,data-structure%2Fqueue%2Fdeque.js,data-structure%2Flinked-list%2Fsingly-linked-list.js,data-structure%2Flinked-list%2Findex.js)

> A **linked list** is a fundamental data structure in computer science. It mainly allows efficient **insertion** and **deletion** operations compared to [arrays](https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/). Like arrays, it is also used to implement other data structures like stack, queue and deque.
>
> A **linked list** is a linear data structure that consists of a series of nodes connected by pointers (in C or C++) or references (in Java, Python and JavaScript). Each node contains **data** and a **pointer** **reference** to the next node in the list. Unlike **arrays, linked lists** allow for efficient **insertion** or **removal** of elements from any position in the list, as the nodes are not stored contiguously in memory.

![image-20240825194807509](https://s2.loli.net/2024/08/25/2qDvI4osxFZdlgX.png)

![image-20240825195031042](https://s2.loli.net/2024/08/25/ILhtwMAjK4PGvC2.png)

链表的方法

- push/append(element): This method adds a new element to the end of the list.
- insert(element, position): This method inserts a new element at a specified position in the list. 
- removeAt(position): This method removes an item from a specified position in the list. 
- remove(element): This method removes an element from the list. 
- update(position,element): 修改某个位置的元素 
- getElementAt(index): This method returns the element of a specific position in the list. If the element does not exist in the list, it returns undefined. 
- indexOf(element): This method returns the index of the element in the list. If the element does not exist in the list, it returns -1.
- isEmpty(): This method returns true if the linked list does not contain any elements, and false if the size of the linked list is bigger than 0. 
- size(): This method returns the number of elements the linked list contains. It is similar to the length property of the array. 
- toString(): This method returns a string representation of the linked list. As the list uses a Node class as an element, we need to overwrite the default .toString method inherited from the JavaScript Object class to output only the element values.

### 双向链表 / Doubly Linked List

> A **doubly linked list** is a data structure that consists of a set of nodes, each of which contains a **value** and **two pointers**, one pointing to the **previous node** in the list and one pointing to the **next node** in the list. This allows for efficient traversal of the list in **both directions**, making it suitable for applications where frequent **insertions** and **deletions** are required.

![image-20240825213530496](https://s2.loli.net/2024/08/25/tnpBjNiQzcVWTo9.png)

![image-20240825213615719](https://s2.loli.net/2024/08/25/7DvUTmSozLFk6qa.png)

![image-20240825213603777](https://s2.loli.net/2024/08/25/SMrdtjnTZuagUGe.png)

```js
function defaultEquals(a, b) {
  return a === b;
}

class Node {
  constructor(element, next) {
    this.element = element;
    this.next = next;
  }
}

export default class LinkedList {
  constructor(equalsFn = defaultEquals) {
    this.equalsFn = equalsFn;
    this.count = 0; // 链表的长度
    this.head = undefined;
  }
  // append
  push(element) {
    // 创建新节点
    const node = new Node(element);
    let current;

    if (this.head == null) {
      // catches null && undefined
      this.head = node;
    } else {
      // 通过while循环找到最后一个节点，让最后的一个节点的next指向新的节点，，
      current = this.head;
      // 循环找，找到最后一个节点
      while (current.next != null) {
        current = current.next;
      }
      // 如果current.next === null
      current.next = node;
    }

    // 链表长度增加
    this.count++;
  }

  getElementAt(index) {
    if (index >= 0 && index <= this.count) {
      let node = this.head;
      for (let i = 0; i < index && node != null; i++) {
        node = node.next;
      }
      return node;
    }
    return undefined;
  }

  /**
   *
   * @param {*} element
   * @param {*} index position
   * @returns
   */
  insert(element, index) {
    // position 边界判断，不能负数，不能太超过现有长度
    if (index >= 0 && index <= this.count) {
      const node = new Node(element);
      if (index === 0) {
        const current = this.head;
        node.next = current;
        this.head = node;
      } else {
        const previous = this.getElementAt(index - 1);
        // 包含了插入最后一个节点的情况
        node.next = previous.next;
        previous.next = node;
      }
      this.count++;
      return true;
    }
    return false;
  }

  removeAt(index) {
    if (index >= 0 && index < this.count) {
      let current = this.head;
      if (index === 0) {
        this.head = current.next;
      } else {
        const previous = this.getElementAt(index - 1);
        current = previous.next;
        previous.next = current.next;
      }
      this.count--;
      return current.element;
    }
    return undefined;
  }

  remove(element) {
    const index = this.indexOf(element);
    return this.removeAt(index);
  }

  indexOf(element) {
    let current = this.head;
    for (let i = 0; i < this.size() && current != null; i++) {
      if (this.equalsFn(element, current.element)) {
        return i;
      }
      current = current.next;
    }
    return -1;
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return this.count;
  }

  getHead() {
    return this.head;
  }

  clear() {
    this.head = undefined;
    this.count = 0;
  }

  toString() {
    if (this.head == null) {
      return "";
    }
    let objString = `${this.head.element}`;
    let current = this.head.next;
    for (let i = 1; i < this.size() && current != null; i++) {
      objString = `${objString},${current.element}`;
      current = current.next;
    }

    return objString;
  }
}
```

