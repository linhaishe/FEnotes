# Data Structure

https://miro.com/app/board/uXjVPEXED68=/

<img src="https://s2.loli.net/2024/08/19/ERPlonh46yDUFNO.jpg" alt="数据结构" style="zoom:50%;" />

# 数据结构/算法定义

> _A data structure is a way of organizing and storing data in a computer so that it can be accessed and used efficiently. It refers to the logical or mathematical representation of data, as well as the implementation in a computer program._
>
> 计算机中存储、组织数据的方式。

> _The word_ [**Algorithm**](https://www.geeksforgeeks.org/fundamentals-of-algorithms) _means ”_ **A set of finite rules or instructions to be followed in calculations or other problem-solving operations** _”_ > _Or\*\*”_ **A procedure for solving a mathematical problem in a finite number of steps that frequently involves recursive operations”\***.\*
>
> An [algorithm](https://www.techtarget.com/searchenterpriseai/definition/clustering-in-machine-learning) is a procedure used for solving a problem or performing a computation. Algorithms act as an exact list of instructions that conduct specified actions step by step in either hardware- or software-based routines.
>
> 解决问题的办法/步骤逻辑。

all source code in: https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Findex.js

study video: https://www.bilibili.com/video/BV1x7411L7Q7?p=13&vd_source=5d5cb2062ab059c137f6aa8f9809b93c

# 线性结构

## array / 数组

数组是一种线性结构，并且可以在数组的任意位置差如何删除数据。

数组在 JS 中的方法被封装的非常完善，查看 API 文档即可。

普通语言的数组封装 (比如 Java 的数组列表)

1. 常见语言的数组不能存放不同的数据类型，因此所有在封装时通常存放在数组中的是 Object 类型
2. 常见语言的数组容量不会自动改变(需要进行扩容操作)
3. 常见语言的数组进行中间插入和删除操作性能比较低.

## stack / 栈

There are two data structures that have some similarities to arrays, but which give us more control over the addition and removal of elements. These data structures are **stacks** and **queues**.

我们为了实现某些功能，必须对数组的任意性插入和任意性删除加以限制，从而产生的具有限制性的线性结构，则为栈和队列。

A stack is an ordered collection of items that follows the last in, first out **(LIFO)** principle.后进先出

<img src="https://s2.loli.net/2024/08/19/fxFAzsd7mhbZUSJ.png" alt="Lightbox" style="zoom:50%;" />

栈举例： 递归 - 递归容易出现栈溢出，如果没有做 break

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

<img src="https://s2.loli.net/2024/08/24/PnxRhYaW8OZrAIM.png" alt="image-20240824190221630" style="zoom: 33%;" />

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

<img src="https://s2.loli.net/2024/08/24/hO59oZmFtAXxvHC.png" alt="image-20240824212252654" style="zoom:33%;" />

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

There are several ways to implement a priority queue, including using an array, linked list, heap, or binary search tree, [binary heap](https://www.geeksforgeeks.org/binary-heap/) being the most common method to implement. heap 的实现方式之后再展开。此处使用 array 的方式处理。

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

数组的创建通常需要申请一段连续的内存空间(一整块的内存)，并且大小是固定的(大多数编程语言数组都是固定的)，所以当当前数组不能满足容量需求时，需要扩容。(一般情况下是申请一个更大的数组，比如 2 倍。然后将原数组中的元素复制过去)，而且在数组开头或中间位置插入数据的成本很高，需要进行大量元素的位移，尽管我们已经学过的 JavaScript 的 Array 类方法可以帮我们做这些事，但背后的原理依然是这样。

- 要存储多个元素，另外一个选择就是链表
- 但不同于数组，链表中的元素在内存中不必是连续的空间
- 链表的每个元素由一个存储元素本身的节点和一个指向下一个元素的引用(有些语言称为指针或者连接)组成

| Pros                                                                     | Cons                                                                                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| 内存空间不是必须连续的。可以充分利用计算机的内存，实现灵活的内存动态管理 | 链表访问任何一个位置的元素时,都需要从头开始访问.(无法跳过第一个元素访问任何一个元素) |
| 链表不必在创建时就确定大小，并且大小可以无限的延伸下去                   | 无法通过下标直接访问元素,需要从头一个个访问,直到找到对应的元素                       |
| 链表在插入和删除数据时，时间复杂度可以达到 O(1)。相对数组效率高很多      |                                                                                      |

### 单向链表 / Singly Linked List

[singly linked list code](https://stackblitz.com/edit/vitejs-vite-iznntc?file=data-structure%2Fstack%2Fstack-object-based.js,data-structure%2Fqueue%2Fpriority-queue.js,data-structure%2Fqueue%2Fqueue-object-based.js,data-structure%2Fqueue%2Fqueue-array-based.js,data-structure%2Fqueue%2Findex.js,data-structure%2Fqueue%2Fdeque.js,data-structure%2Flinked-list%2Fsingly-linked-list.js,data-structure%2Flinked-list%2Findex.js)

> A **linked list** is a fundamental data structure in computer science. It mainly allows efficient **insertion** and **deletion** operations compared to [arrays](https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/). Like arrays, it is also used to implement other data structures like stack, queue and deque.
>
> A **linked list** is a linear data structure that consists of a series of nodes connected by pointers (in C or C++) or references (in Java, Python and JavaScript). Each node contains **data** and a **pointer** **reference** to the next node in the list. Unlike **arrays, linked lists** allow for efficient **insertion** or **removal** of elements from any position in the list, as the nodes are not stored contiguously in memory.

<img src="https://s2.loli.net/2024/08/25/2qDvI4osxFZdlgX.png" alt="image-20240825194807509" style="zoom:50%;" />

<img src="https://s2.loli.net/2024/08/25/ILhtwMAjK4PGvC2.png" alt="image-20240825195031042" style="zoom: 33%;" />

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

```js
// 单向链表
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

### 双向链表 / Doubly Linked List

> A **doubly linked list** is a data structure that consists of a set of nodes, each of which contains a **value** and **two pointers**, one pointing to the **previous node** in the list and one pointing to the **next node** in the list. This allows for efficient traversal of the list in **both directions**, making it suitable for applications where frequent **insertions** and **deletions** are required.

双向列表的缺点：

TBC

<img src="https://s2.loli.net/2024/08/25/tnpBjNiQzcVWTo9.png" alt="image-20240825213530496" style="zoom: 50%;" />

<img src="https://s2.loli.net/2024/08/25/7DvUTmSozLFk6qa.png" alt="image-20240825213615719" style="zoom:50%;" />

<img src="https://s2.loli.net/2024/08/25/SMrdtjnTZuagUGe.png" alt="image-20240825213603777" style="zoom:50%;" />

```js
import { defaultEquals } from '../util';
import LinkedList from './linked-list';
import { DoublyNode } from './models/linked-list-models';

// 1. 创建节点
// 2. 判断头中尾
// 3. 修改指针
export default class DoublyLinkedList extends LinkedList {
  constructor(equalsFn = defaultEquals) {
    super(equalsFn);
    this.tail = undefined;
  }
  push(element) {
    const node = new DoublyNode(element);
    if (this.head == null) { // 如果只有一个节点
      this.head = node;
      this.tail = node; // NEW
    } else { // last item, 非第一个节点，放在最后面
      // attach to the tail node // NEW
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.count++;
  }
  insert(element, index) {
    if (index >= 0 && index <= this.count) {
      const node = new DoublyNode(element);
      let current = this.head;
      // 如果插入的位置是第一个位置，需要判断第一个位置后面是否存在别的数据。分为有或者没有的情况
      // is first elements
      if (index === 0) {
        if (this.head == null) { // NEW
          this.head = node;
          this.tail = node; // NEW
        } else { // has other elements
          node.next = this.head;
          this.head.prev = node; // NEW
          this.head = node;
        }
      } else if (index === this.count) { // is last item / NEW
        current = this.tail;
        current.next = node;
        node.prev = current;
        this.tail = node;
      } else { // middle item
        const previous = this.getElementAt(index - 1);
        current = previous.next;
        node.next = current;
        previous.next = node;
        current.prev = node; // NEW
        node.prev = previous; // NEW
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
        this.head = this.head.next;
        // if there is only one item, then we update tail as well //NEW
        if (this.count === 1) {
          // {2}
          this.tail = undefined;
        } else {
          this.head.prev = undefined;
        }
      } else if (index === this.count - 1) {
        // last item //NEW
        current = this.tail;
        this.tail = current.prev;
        this.tail.next = undefined;
      } else {
        current = this.getElementAt(index);
        const previous = current.prev;
        // link previous with current's next - skip it to remove
        previous.next = current.next;
        current.next.prev = previous; // NEW
      }
      this.count--;
      return current.element;
    }
    return undefined;
  }
  indexOf(element) {
    let current = this.head;
    let index = 0;
    while (current != null) {
      if (this.equalsFn(element, current.element)) {
        return index;
      }
      index++;
      current = current.next;
    }
    return -1;
  }
  getHead() {
    return this.head;
  }
  getTail() {
    return this.tail;
  }
  clear() {
    super.clear();
    this.tail = undefined;
  }
  toString() {
    if (this.head == null) {
      return '';
    }
    let objString = `${this.head.element}`;
    let current = this.head.next;
    while (current != null) {
      objString = `${objString},${current.element}`;
      current = current.next;
    }
    return objString;
  }
  inverseToString() {
    if (this.tail == null) {
      return '';
    }
    let objString = `${this.tail.element}`;
    let previous = this.tail.prev;
    while (previous != null) {
      objString = `${objString},${previous.element}`;
      previous = previous.prev;
    }
    return objString;
  }
}

```

# set / 集合

> A set is a collection of items that are unordered and consists of unique elements (meaning they cannot be repeated). This data structure uses the same mathematical concept as finite sets, but it is applied to a computer science data structure.
>
> 1. 无序的
> 2. 不能重复

ECMAScript 2015 introduced the Set class as part of the JavaScript API

具体需要实现的方法

- add(element): This adds a new element to the set.
- delete(element): This removes the element from the set.
- has(element): This returns true if the element exists in the set and false otherwise.
- clear(): This removes all the elements from the set.
- size(): This returns how many elements the set contains. It is similar to the length property of an array.
- values(): This returns an array of all the values (elements) of the set.

Set operations 

- Union / 并集: Given two sets, this returns a new set of elements from both of the given sets

  对于给定的两个集合，返回一个包含两个集合中所有元素的新集合

- Intersection / 交集: Given two sets, this returns a new set with the elements that exist in both sets

  对于给定的两个集合，返回一个包含两个集合中共有元素的新集合

- Difference / 差集: Given two sets, this returns a new set with all the elements that exist in the first set and do not exist in the second set

  对于给定的两个集合，返回一个包含所有存在于第一个集合且不存在于第二个集合的元素的新集合

- Subset / 子集: This confirms whether a given set is a subset of another set

  验证一个给定集合是否是另一集合的子集

```js
export default class Set {
  constructor() {
    this.items = {};
  }

  add(element) {
    if (!this.has(element)) {
      // 集合的元素是不能重复的，需要判断是否已经存在
      this.items[element] = element;
      return true;
    }
    return false;
  }

  delete(element) {
    if (this.has(element)) {
      delete this.items[element];
      return true;
    }
    return false;
  }

  has(element) {
    return Object.prototype.hasOwnProperty.call(this.items, element);
  }

  values() {
    return Object.values(this.items);
  }
  // Set operations / 集合间的操作
  /**
   * 并集
   */

  // 在你的代码中，Set 是一个你自定义的类，它并不是 JavaScript 内置的 Set 类。当你在 union 方法内部使用 new Set() 时，你实际上是创建了一个新的 Set 实例，这个实例是基于你自定义的 Set 类而不是JavaScript的内置 Set 类。

  // 这是因为当你定义了一个类（如 export default class Set { ... }），这个类就变成了一个构造函数，你可以使用 new 关键字来调用这个构造函数以创建该类的新实例。所以在 union 方法中，new Set() 这一行代码就是用来创建一个新的 Set 类的实例，这个新实例将用于存储两个集合的并集。

  // 简而言之，因为 Set 在这里是你自己定义的一个类，所以你完全有权使用 new Set() 来创建它的实例，就像你可以对任何其他自定义类或JavaScript内置类（如 Array、Object 等）做的一样。
  union(otherSet) {
    const unionSet = new Set(); // 创建新的集合，为什么这里可以直接new？⬆
    this.values().forEach((value) => unionSet.add(value)); // this 指向当前的Set
    otherSet.values().forEach((value) => unionSet.add(value));
    return unionSet;
  }

  /**
   * 交集
   */
  intersection(otherSet) {
    const intersectionSet = new Set();
    const values = this.values();
    const otherValues = otherSet.values();
    // Fewer iterations means a cheaper processing cost,
    // 找到最小的集合用最短的数据进行遍历
    let biggerSet = values;
    let smallerSet = otherValues;
    if (otherValues.length - values.length > 0) {
      biggerSet = otherValues;
      smallerSet = values;
    }
    smallerSet.forEach((value) => {
      if (biggerSet.includes(value)) {
        intersectionSet.add(value);
      }
    });
    return intersectionSet;
  }

  /**
   * 差集
   * 数据在setA里，但不在setB里
   */
  difference(otherSet) {
    const differenceSet = new Set();
    this.values().forEach((value) => {
      if (!otherSet.has(value)) {
        differenceSet.add(value);
      }
    });
    return differenceSet;
  }

  /**
   * 子集
   */
  isSubsetOf(otherSet) {
    if (this.size() > otherSet.size()) {
      return false;
    }
    let isSubset = true;
    this.values().every((value) => {
      if (!otherSet.has(value)) {
        isSubset = false;
        return false;
      }
      return true;
    });
    return isSubset;
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return Object.keys(this.items).length;
  }

  clear() {
    this.items = {};
  }

  toString() {
    if (this.isEmpty()) {
      return '';
    }
    const values = this.values();
    let objString = `${values[0]}`;
    for (let i = 1; i < values.length; i++) {
      objString = `${objString},${values[i].toString()}`;
    }
    return objString;
  }
}

```

# Hash / 哈希

哈希表通常是基于数组进行实现的,但是相对于数组,它也很多的优势:

- 它可以提供非常快速的插入-删除-查找操作
- 无论多少数据,插入和删除值需要接近常量的时间: 即O(1)的时间级.实际上,只需要几个机器指令即可完成哈希表的速度比树还要快,基本可以瞬间查找到想要的元素
- 哈希表相对于树来说编码要容易很多。

哈希表相对于数组的一些不足:

- 哈希表中的数据是没有顺序的,所以不能以一种固定的方式(比如从小到大)来遍历其中的元素。
- 通常情况下，哈希表中的key是不允许重复的,不能放置相同的key, 用于保存不同的元素。

霍纳算法 - 计算哈希值

<img src="https://s2.loli.net/2024/09/25/8DYvourVJnHeN9F.png" alt="image-20240925220637602" style="zoom:33%;" />


2024/09/04

HashTable class, also known as HashMap, a hash implementation of the Dictionary class. Hashing consists of finding a value in a data structure in the shortest time possible.

TBC - unicode 的前世今生 to be add

解决冲突的方法：

1. 链地址法（拉链法）：每个数组单元中存储的不再是单个数据，而是一个链条。

2. 开放地址法：寻找空白的单元格莱添加重复的数据。

   探索空白的的位置方式不同，有三种方法：

   - 线性探测：每次步长+1，一个一个位置去查找空白单元
   - 二次探测：二次探测可以解决线性探测的聚集问题。对步长进行了优化，1，4，9，16
   - 再哈希法：把关键字用另外一个哈希函数，再进行一次哈希化，用这次哈希化的结果作为步长
     - 哈希函数：1. stepSize = constant - (key % constant); 2. 其中 constant 是质数，且小于数组的容量。
     - 优秀的哈希函数应该具有快速的计算且尽可能的将元素映射到不同的位置，让元素在哈希表中均匀的分布。

## 哈希函数

- 哈希函数：1. stepSize = constant - (key % constant); 2. 其中 constant 是质数，且小于数组的容量。
- 优秀的哈希函数应该具有快速的计算，尽最快的速度获取元素对应的 hashcode 且尽可能的将元素映射到不同的位置，让元素在哈希表中均匀的分布。

快速计算：霍纳法则/秦九韶算法，提升时间复杂度

均匀分布：链地址法/开放地址法，在使用常量的地方，尽量使用质数

质数的使用：哈希表的长度/N 次幂的底数

The hash function we will use in this book is the most common one, called a lose-lose hash function, in which we simply sum up the ASCII values of each character of the key length:

<img src="https://s2.loli.net/2024/09/28/Q1pz32uWo64Dah5.png" alt="image-20240928232651450" style="zoom:33%;" />

```js
loseloseHashCode(key) {
  if (typeof key === 'number') {
    return key;
  }
  const tableKey = this.toStrFn(key);
  let hash = 0;
  for (let i = 0; i < tableKey.length; i++) {
    hash += tableKey.charCodeAt(i);
  }
  return hash % 37;
}
djb2HashCode(key) {
  const tableKey = this.toStrFn(key);
  let hash = 5381; // consists of initializing the hash variable with a prime number,most implementations use 5381
  for (let i = 0; i < tableKey.length; i++) {
    // multiply the hash value by 33 (used as a magical number)
    hash = (hash * 33) + tableKey.charCodeAt(i); // sum it with the ASCII value of the characte
  }
  // use the rest of the division of the total by another random prime number ({5}), greater than the size we think the HashTable instance can have. just random, size in what we need.
  return hash % 1013;
}
```

- put(key, value): This method adds a new item to the hash table (or it can also update it)

- remove(key): This method removes the value from the hash table using the key

- get(key): This method returns a specific value searched by the key

collisions: separate chaining, linear probing, and double hashing.

### separate chaining

separate chaining（分离链接法）：做法是将散列到同一个值的所有元素保留到一个链表中。

<img src="https://s2.loli.net/2024/09/28/oAQdDkfS89nztTN.png" alt="image-20240928232755130" style="zoom:33%;" />

### linear probing

linear probing（线性探测）**Open Addressing**：all elements are stored in the **hash table** itself. So at any point, the size of the table must be greater than or equal to the total number of keys (Note that we can increase table size by copying old data if needed). This approach is also known as closed hashing.

每个数据都会直接被存储在 hash table 里，如果有相同的数据，则 index+1.如果需要查询到相同的 key，就 index+1 一个一个找下去。

<img src="https://s2.loli.net/2024/09/28/sEUYgVbTc4JBa8n.png" alt="image-20240928232851124" style="zoom:33%;" />

1. soft delete: 一个一个判断是否是需要删除的数据。删除的数据的位置会被放置一个 flag，每次查询的时候，会通过判断是否是 delete flag，如果是，则跳过，检查下一个数据。如果不是且是对应的数据，则删除，并添加 delte flag.

   <img src="https://s2.loli.net/2024/09/28/RZ89q2naKFYIBeE.png" alt="image-20240928232938744" style="zoom:33%;" />

2. lazy delete

   second approach requires verifying whether it is necessary to move one or more elements to a backward position.

   The second approach requires verifying whether it is necessary to move one or more elements to a backward position. When searching for a key, this approach prevents finding an empty spot, but if it is necessary to move elements, this means we will need to shift key-values within the hash table. The following diagram exemplifies this process.

   From there, when doing a deletion, you can shift elements backwards one spot to fill the gap from the removed element until you either hit a blank or an element that's already in the right place and doesn't need to be moved.

   删除之后移动后面的元素向前面的位置移动，直到你已经遇到空白处或者对应的元素的位置则会停止查找。

   <img src="https://s2.loli.net/2024/09/28/nfJ6DByxCRm3Sgd.png" alt="image-20240928233030197" style="zoom:33%;" />

# Tree / 树

a tree, which is very useful for storing information that needs to be found easily.

- Tree terminology
- Creating a binary search tree
- Traversing a tree / 树遍历 / tree traversal
- Adding and removing nodes
- The AVL tree

## tree terminology

A tree is an abstract model of a hierarchical structure

<img src="https://s2.loli.net/2024/09/28/vPGrnx3LzgsqBJ5.png" alt="image-20240928233224039" style="zoom:33%;" />

- <mark>root</mark>: The top node of a tree
- <mark>internal nodes</mark>: is a node with at least one child (7, 5, 9, 15, 13, and 20).
- <mark>external nodes / leaf</mark>: is a node that does not have children.
- <mark>ancestors / descendants</mark> : The ancestors of a node (except the root) are the parent, grandparent, great-grandparent, and so on.The descendants of a node are children (child), grandchildren (grandchild), great-grandchildren (great-grandchild), and so on. node 5 has 7 and 11 as its ancestors and 3 and 6 as its descendants.
- <mark>subtree</mark>: A subtree consists of a node and its descendants.

  the nodes 13, 12, and 14 constitute a subtree from the tree of the preceding diagram.

- <mark>The depth of a node</mark>: The depth of a node consists of the number of ancestors. For example, node 3 has a depth of 3 because it has three ancestors (5, 7, and 11).

- <mark>The height of a tree</mark>: The height of a tree consists of the maximum depth of any node. A tree can also be broken down into levels.

  The root is on level 0, its children are on level 1, and so on. The tree from the preceding diagram has a height of 3 (the maximum depth is 3, as shown in the preceding figure on level 3).

## The binary and binary search trees

binary search trees / 二叉搜索树 / 二叉排序树 / 二叉查找树 / BST

A node in a binary tree has two children at most: one left child and one right child.

A binary search tree (BST) is a binary tree, but it only allows you to store nodes with lesser values on the left-hand side and nodes with greater values on the right-hand side.

<img src="https://s2.loli.net/2024/09/28/GBRbTn2PsdqjlQg.png" alt="image-20240928233303837" style="zoom: 33%;" />

二叉搜索树如果不为空，满足以下性质

- 非空左子树的所有键值小于其根节点的键值
- 非空右子树的所有键值大于其根节点的键值
- 左、右子树本身也都是二叉搜索树

the function we need:

- insert(key): This method inserts a new key in the tree
- search(key): This method searches for the key in the tree and returns true if it exists and false if the node does not exist
- inOrderTraverse(): This method visits all nodes of the tree using in-order traverse
- preOrderTraverse(): This method visits all nodes of the tree using pre-order traverse
- postOrderTraverse(): This method visits all the nodes of the tree using postorder traverse
- min(): This method returns the minimum value/key in the tree
- max(): This method returns the maximum value/key in the tree
- remove(key): This method removes the key from the tree

## Traversing (or walking) a tree

Traversing (or walking) a tree is the process of visiting all the nodes of a tree and performing an operation at each node.

有非常多的方式可以做树遍历，从上从下从左从右，接下来的章节会使用: in-order, pre-order, and post-order.这三种方式。

### in-order traversal

An in-order traversal visits all the nodes of a BST in an ascending order, meaning it will visit the nodes from the smallest to the largest. An application of in-order traversal would be to sort a tree. 从最小的 node 开始遍历依次到最大的

```
3 5 6 7 8 9 10 11 12 13 14 15 18 20 25
```

<img src="https://s2.loli.net/2024/09/28/DsIl2fGiazOjBw7.png" alt="image-20240928233424130" style="zoom:33%;" />

### pre-order traversal

A pre-order traversal visits the node prior to its descendants. 从祖先开始再到子辈进行遍历获得数据

根 -> 左 -> 右

```
11 7 5 3 6 9 8 10 15 13 12 14 20 18 25
```

<img src="https://s2.loli.net/2024/09/28/mf9JpROVaHAB2vz.png" alt="image-20240928233518668" style="zoom: 33%;" />

### post-order traversal

A post-order traversal visits the node after it visits its descendants. An application of post-order traversal could be computing the space used by a file in a directory and its subdirectories.先遍历子辈节点再遍历祖先节点，会在没有子辈节点后再遍历祖辈节点，所以 7,15,11 都在每个子节点遍历完后才能遍历到。

```
3 6 5 8 10 9 7 12 14 13 18 25 20 15 11
```

<img src="https://s2.loli.net/2024/09/28/gzF5fbVsy7Gq2nJ.png" alt="image-20240928233554353" style="zoom: 33%;" />

## Searching for values in a tree

### Searching for minimum/maximum values

### Searching for a specific value

## removing

// 1 - a leaf node

// 2 - a node with only 1 child / a left or right child

// 3 - a node with 2 children

## self-balancing tree

### <mark>AVL tree??</mark>

Adelson-Velskii and Landi’s tree

The AVL tree is a self-balancing tree, meaning the tree tries to self-balance whenever a node is added to it or removed from it. The height of the left or right subtree of any node (and any level) differs by 1 at most. This means the tree will try to become a complete tree whenever possible while adding or removing a node.

### Red-Black tree

if we need a self-balancing tree that involves many frequent insertions or deletions, then the Red-Black tree is preferred. 

如果有很多插入和删除的操作的时候，我们更倾向于使用红黑树，否则使用avl tree即可。应为avl tree在处理增加和删除操作的时候会产生rotations。

In the Red-Black tree, every node follows the rules which are listed as follows: 

1. As the name of the tree suggests, each node is either red or black. 

2. The root of the tree is black. 

3. All of the leaves are black (nodes represented with the NULL reference). 

4. If a node is red, then both of its children are black. 

5. There cannot be two adjacent red nodes. A red node cannot have a red parent or child. 

6. Every path from a given node to any of its descendants (NULL leaves) contains the same number of black nodes.

7. 新节点默认都是红色

![image-20241020162958866](https://s2.loli.net/2024/10/20/Je9wGFNZ4Xiu3Q5.png)

红黑树在增加node的时候保持树平衡，需要通过换色和反转的方式处理平衡。

#### recoloring

After inserting a new node into the tree, this new node will be red.
#### rotation

## 优缺点对比

|        | 优点                                                         | 缺点                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 数组   | 1. 数组的主要优点是根据下标值访问效率会很高<br />2. 比较好的方式是先对数组进行排序，再进行二分查找 | 1. 需要先对数组进行排序,生成有序数组,才能提高查找效率<br />2. 另外数组在插入和删除数据时,需要有大量的位移操作(插入到首位或者中间位置的时候),效率很低 |
| 链表   | 插入和删除操作效率都很高                                     | 1.查找效率很低,需要从头开始依次访问链表中的每个数据项,直到找到<br />2. 即使插入和删除操作效率很高，但是如果要插入和删除中间位置的数据,还是需要重头先找到对应的数据 |
| 哈希表 | 哈希表的插入/查询/删除效率都是非常高                         | 1. 空间利用率不高，底层使用的是数组,并且某些单元是没有被利用的<br/>2. 哈希表中的元素是无序的,不能按照固定的顺序来遍历哈希表中的元素.<br/>3. 不能快速的找出哈希表中的最大值或者最小值这些特殊的值 |
| 输     | 1. 树确实也综合了上面的数据结构的优点,但效率一般情况下没有哈希表高。<br />2. 数结构的非线性的,可以表示一对多的关系比如文件的目录结构 | Ï                                                            |

- 一个二叉树第 i 层的最大节点数为 : 2^(i-1),i >= 1;
- 深度为k的二又树有最大节点总数为 : 2^k - 1,k >= 1;
- 对任何非空二叉树T，若n0表示叶节点的个数、n2是度为2的非叶节点个数，那么两者满足关系n^0 = n2 +1



完全二叉树
非完全二叉树

# Graphs

## Graph terminology

a _vertex_ ( pl. : _vertices_ or *vertex*es) / 顶点

A graph is an abstract model of a network structure. A graph is a set of nodes (or vertices) connected by edges. Learning about graphs is important because any binary relationship can be represented by a graph.

A graph： G = (V, E) is composed of:

- V: A set of vertices
- E: A set of edges（边） connecting the vertices in V

<img src="https://s2.loli.net/2024/09/28/Y7JXeD9EVnZqa4W.png" alt="image-20240928233724498" style="zoom:33%;" />

1. adjacent vertices

2. degree of a vertex: 有多少个相邻顶点被链接，A 有 3 dgree，B 有 2 degree

3. path: is a sequence of consecutive vertices. (一系列连续的顶点), A - B - E - W - I.

   A simple path does not contain repeated vertices. A - D - G

   cycle: is a simple path, except for the last vertex which is the same as the first vertex. A - D - C - A

4. A graph is acyclic(无环的) if it does not have cycles. A graph is connected if there is a path between every pair of vertices.

5. directed and undirected graphs / 有向图、无向图

6. unweighted and weighted graphs / 无权图、加权图

<img src="https://s2.loli.net/2024/12/01/Notnujyq2wOs1i6.png" alt="image-20241201131212299" style="zoom: 50%;" /><img src="https://s2.loli.net/2024/12/01/kJA2H5Ew4hV8G3a.png" alt="image-20241201131246942" style="zoom: 50%;" />

## Representing a graph in three different ways

### adjacency matrix / 邻接矩阵

there is  a matrix with many zero entries in the adjacency matrix. 

This means we would waste space in the computer memory to represent edges that do not exist.

如果我们需要根据邻接矩阵去查询顶点，那么就会需要去遍历整个row,即使只有一个顶点存在的情况下，会浪费memory。

顶点的数量是会变的，所以在使用二维数组实现的时候会不灵活。

<img src="https://s2.loli.net/2024/12/01/RCTrudxsKQFAn1Y.png" alt="image-20241201124443471" style="zoom:33%;" />

### adjacency list / 领接表

This consists of a list of adjacent vertices for every vertex of the graph.

通常可以用不同的方式去实现这个表，比如数组、链表、哈希表、字典等。

<img src="https://s2.loli.net/2024/12/01/xfRIway7VJSE5mD.png" alt="image-20241201124510399" style="zoom: 33%;" />

### incidence matrix / 关联矩阵

Row: a vertex

Column: an edge

An incidence matrix is usually used to save space and memory when we have more edges than vertices.

<img src="https://s2.loli.net/2024/12/01/WgRx1THjOm6V7Ik.png" alt="image-20241201124656534" style="zoom:33%;" />



## The graph data structure in class

```js
import Dictionary from './dictionary';

export default class Graph {
  constructor(isDirected = false) {
    this.isDirected = isDirected; // 是否有向
    this.vertices = [];
    this.adjList = new Dictionary(); // an object
  }
  
  addVertex(v) {
    if (!this.vertices.includes(v)) {
      this.vertices.push(v);
      this.adjList.set(v, []); // initialize adjacency list with array as well;m
    }
  }
  
  addEdge(a, b) {
    if (!this.adjList.get(a)) {
      this.addVertex(a);
    }
    if (!this.adjList.get(b)) {
      this.addVertex(b);
    }
    this.adjList.get(a).push(b);
    if (this.isDirected !== true) {
      this.adjList.get(b).push(a);
    }
  }
  
  getVertices() {
    return this.vertices;
  }
  
  getAdjList() {
    return this.adjList;
  }
  
  toString() {
    let s = '';
    for (let i = 0; i < this.vertices.length; i++) {
      s += `${this.vertices[i]} -> `;
      const neighbors = this.adjList.get(this.vertices[i]);
      for (let j = 0; j < neighbors.length; j++) {
        s += `${neighbors[j]} `;
      }
      s += '\n';
    }
    return s;
  }
}
```

```js
const graph = new Graph();
const myVertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
for (let i = 0; i < myVertices.length; i++) {
	graph.addVertex(myVertices[i]);
}
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('A', 'D');
graph.addEdge('C', 'D');
graph.addEdge('C', 'G');
graph.addEdge('D', 'G');
graph.addEdge('D', 'H');
graph.addEdge('B', 'E');
graph.addEdge('B', 'F');
graph.addEdge('E', 'I');

console.log(graph.toString());
```

## Graph search algorithms

### Breadth-first search (BFS

广度优先搜索

visits the vertices first widely and then deeply

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20241201133053273.png" alt="image-20241201133053273" style="zoom: 50%;" />



1. Create a queue Q 
2. Mark v as discovered (grey) and enqueue v into Q 
3. While Q is not empty, perform the following steps: 
   1. dequeue u from Q 
   2. Mark u as discovered (grey) 
   3. enqueue all the unvisited (white) neighbors w of u 
   4. Mark u as explored (black)

```js
import Queue from '../../data-structures/queue';

const Colors = {
  WHITE: 0, // unvisited
  GREY: 1, // discovered - 正在探索的
  BLACK: 2 // explored - 已探索完的
};

const initializeColor = vertices => {
  const color = {};
  for (let i = 0; i < vertices.length; i++) {
    color[vertices[i]] = Colors.WHITE;
  }
  return color;
};

export const breadthFirstSearch = (graph, startVertex, callback) => {
  const vertices = graph.getVertices();
  const adjList = graph.getAdjList();
  const color = initializeColor(vertices);
  const queue = new Queue();

  queue.enqueue(startVertex);

  while (!queue.isEmpty()) {
    const u = queue.dequeue();
    const neighbors = adjList.get(u);
    color[u] = Colors.GREY;
    for (let i = 0; i < neighbors.length; i++) {
      const w = neighbors[i];
      if (color[w] === Colors.WHITE) {
        color[w] = Colors.GREY;
        queue.enqueue(w);
      }
    }
    color[u] = Colors.BLACK;
    if (callback) {
      callback(u);
    }
  }
};

export const BFS = (graph, startVertex) => {
  const vertices = graph.getVertices();
  const adjList = graph.getAdjList();
  const color = initializeColor(vertices);
  const queue = new Queue();
  const distances = {};
  const predecessors = {};
  queue.enqueue(startVertex);
  for (let i = 0; i < vertices.length; i++) {
    distances[vertices[i]] = 0;
    predecessors[vertices[i]] = null;
  }
  while (!queue.isEmpty()) {
    const u = queue.dequeue();
    const neighbors = adjList.get(u);
    color[u] = Colors.GREY;
    for (let i = 0; i < neighbors.length; i++) {
      const w = neighbors[i];
      if (color[w] === Colors.WHITE) {
        color[w] = Colors.GREY;
        distances[w] = distances[u] + 1;
        predecessors[w] = u; // derive the shortest path from v to every other vertex u
        queue.enqueue(w);
      }
    }
    color[u] = Colors.BLACK;
  }
  return {
    distances,
    predecessors
  };
};

```

#### 1. outputting the order of vertices visited

#### 2. finding shortest path / Shortest path algorithms

Dijkstra's algorithm / Floyd-Warshall algorithm / 

```js
// finding the shortesr path
const shortestPathA = BFS(graph, myVertices[0]);
console.log(shortestPathA);
```

### Depth-first search (DFS

深度优先搜索

visits the vertices first deep and then wide

To visit vertex v, perform the following steps: 

1. Mark v as discovered (grey). 
2. For all unvisited (white) neighbors w of v, visit vertex w. 
3. Mark v as explored (black).

<img src="https://s2.loli.net/2024/12/01/6V9Z3blABjuD7hW.png" alt="image-20241201150804238" style="zoom: 50%;" />

```js
// import Graph from '../../data-structures/graph';

const Colors = {
  WHITE: 0,
  GREY: 1,
  BLACK: 2
};

const initializeColor = vertices => {
  const color = {};
  for (let i = 0; i < vertices.length; i++) {
    color[vertices[i]] = Colors.WHITE;
  }
  return color;
};

const depthFirstSearchVisit = (u, color, adjList, callback) => {
  color[u] = Colors.GREY;
  if (callback) {
    callback(u);
  }
  // console.log('Discovered ' + u);
  const neighbors = adjList.get(u);
  for (let i = 0; i < neighbors.length; i++) {
    const w = neighbors[i];
    if (color[w] === Colors.WHITE) {
      depthFirstSearchVisit(w, color, adjList, callback);
    }
  }
  color[u] = Colors.BLACK;
  // console.log('explored ' + u);
};

export const depthFirstSearch = (graph, callback) => {
  const vertices = graph.getVertices();
  const adjList = graph.getAdjList();
  const color = initializeColor(vertices);

  for (let i = 0; i < vertices.length; i++) {
    if (color[vertices[i]] === Colors.WHITE) {
      depthFirstSearchVisit(vertices[i], color, adjList, callback);
    }
  }
};

const DFSVisit = (u, color, d, f, p, time, adjList) => {
  // console.log('discovered ' + u);
  color[u] = Colors.GREY;
  d[u] = ++time.count;
  const neighbors = adjList.get(u);
  for (let i = 0; i < neighbors.length; i++) {
    const w = neighbors[i];
    if (color[w] === Colors.WHITE) {
      p[w] = u;
      DFSVisit(w, color, d, f, p, time, adjList);
    }
  }
  color[u] = Colors.BLACK;
  f[u] = ++time.count;
  // console.log('explored ' + u);
};

export const DFS = graph => {
  const vertices = graph.getVertices();
  const adjList = graph.getAdjList();
  const color = initializeColor(vertices);
  const d = {};
  const f = {};
  const p = {};
  const time = { count: 0 };
  for (let i = 0; i < vertices.length; i++) {
    f[vertices[i]] = 0;
    d[vertices[i]] = 0;
    p[vertices[i]] = null;
  }
  for (let i = 0; i < vertices.length; i++) {
    if (color[vertices[i]] === Colors.WHITE) {
      DFSVisit(vertices[i], color, d, f, p, time, adjList);
    }
  }
  return {
    discovery: d,
    finished: f,
    predecessors: p
  };
};
```

Topological sorting using DFS

tbc..

## Minimum spanning tree algorithms

Prim's algorithm / Kruskal's algorithm

# Sorting and Searching Algorithms

## Sorting algorithms

### 1. bubble sort / 冒泡排序

> The bubble sort algorithm compares every two adjacent values and swaps them if the first one is bigger than the second one. 

<img src="https://s2.loli.net/2024/12/01/auzkVe9hisUjyx5.png" alt="image-20241201152628895" style="zoom: 50%;" />

```js
export function swap(array, a, b) {
  /* const temp = array[a];
  array[a] = array[b];
  array[b] = temp; */
  [array[a], array[b]] = [array[b], array[a]];
}

export function defaultCompare(a, b) {
  if (a === b) {
    return Compare.EQUALS;
  }
  return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
}

export const Compare = {
  LESS_THAN: -1,
  BIGGER_THAN: 1,
  EQUALS: 0
};


export function bubbleSort(array, compareFn = defaultCompare) {
  const { length } = array;
  for (let i = 0; i < length; i++) {
    // console.log('--- ');
    for (let j = 0; j < length - 1; j++) {
    // for (let j = 0; j < length - 1 - i; j++) { // 优化后
      // avoid all the unnecessary comparisons made by the inner loop
      // console.log('compare ' + array[j] + ' with ' + array[j + 1]);
      if (compareFn(array[j], array[j + 1]) === Compare.BIGGER_THAN) {
        // console.log('swap ' + array[j] + ' with ' + array[j + 1]);
        swap(array, j, j + 1);
      }
    }
  }
  return array;
}

```

优化后减少不必要的比较

![image-20241201153623373](https://s2.loli.net/2024/12/01/jpcQSP2NmIWVMo8.png)

### 2. selection sort / 选择排序

> The selection sort algorithm is an in-place comparison (就地比较) sort algorithm. The general idea of the selection sort is to find the minimum value in the data structure, place it in the first position, then find the second minimum value, place it in the second position, and so on.

<img src="https://s2.loli.net/2024/12/01/ocibD3KZq2fIRJl.png" alt="image-20241201154127842" style="zoom:33%;" />

```js
import { Compare, defaultCompare, swap } from '../../util';

export const selectionSort = (array, compareFn = defaultCompare) => {
  const { length } = array;
  let indexMin;
  for (let i = 0; i < length - 1; i++) {
    indexMin = i;
    // console.log('index ' + array[i]);
    for (let j = i; j < length; j++) {
      if (compareFn(array[indexMin], array[j]) === Compare.BIGGER_THAN) {
        // console.log('new index min ' + array[j]);
        indexMin = j;
      }
    }
    if (i !== indexMin) {
      // console.log('swap ' + array[i] + ' with ' + array[indexMin]);
      swap(array, i, indexMin);
    }
  }
  return array;
};
```

### 3. insertion sort / 插入排序

> The insertion sort algorithm builds the final sorted array one value at a time. It assumes that the first element is already sorted. Then, a comparison with the second value is performed—should the second value stay in its place or be inserted before the first value? The first two values will get sorted, then the comparison will take place with the third value (that is, should it be inserted in the first, second, or third position?), and so on.
>
> 默认第一个数据是已经被排序过的，第二个数据会和第一个数据进行比较，看是否交换位置。1、2数据已经被比较，第三个数据会直接和第二个数据进行比较。
>
> This algorithm has a better performance than the selection and bubble sort algorithms when sorting small arrays.

```js
import { Compare, defaultCompare } from '../../util';

export const insertionSort = (array, compareFn = defaultCompare) => {
  const { length } = array;
  let temp;
  for (let i = 1; i < length; i++) {
    let j = i;
    temp = array[i];
    // console.log('to be inserted ' + temp);
    while (j > 0 && compareFn(array[j - 1], temp) === Compare.BIGGER_THAN) {
      // console.log('shift ' + array[j - 1]);
      array[j] = array[j - 1];
      j--;
    }
    // console.log('insert ' + temp);
    array[j] = temp;
  }
  return array;
};

```

#### shell sort / 希尔排序

递减增量排序算法，是插入排序的一种更高效的改进版本。 希尔排序是非稳定排序算法

希尔排序就是按照一定的gap值，不断地对数组进行插入排序。不一样的希尔排序算法可能采用不一样的gap值。

```js
// shell sort / 希尔排序
import { Compare, defaultCompare } from '../../util';

export function shellSort(array, compareFn = defaultCompare) {
  let increment = array.length / 2; // 
  while (increment > 0) {
    for (let i = increment; i < array.length; i++) {
      let j = i;
      const temp = array[i];
      while (j >= increment && compareFn(array[j - increment], temp) === Compare.BIGGER_THAN) {
        array[j] = array[j - increment];
        j -= increment;
      }
      array[j] = temp;
    }
    if (increment === 2) {
      increment = 1;
    } else {
      increment = Math.floor((increment * 5) / 11);
    }
  }
  return array;
}

```

### 4. merge sort

> The merge sort is a divide-and-conquer（分而治之） algorithm. The idea behind it is to divide the original array into smaller arrays until each small array has only one position, and then merge these smaller arrays into bigger ones until we have a single big array at the end that is sorted.
>
> 找到中间数，然后将数组分成两拨数据，一拨数值小的，一拨数值大的，排序完后再合并在一起

the merge sort has good performance with a complexity of O(n log n).

<img src="https://s2.loli.net/2024/12/01/HCdfV8sBK7qoJ9W.png" alt="image-20241201160923619" style="zoom:33%;" />

```js
import { Compare, defaultCompare } from '../../util';

function merge(left, right, compareFn) {
  let i = 0;
  let j = 0;
  const result = [];
  while (i < left.length && j < right.length) {
    result.push(compareFn(left[i], right[j]) === Compare.LESS_THAN ? left[i++] : right[j++]);
  }
  return result.concat(i < left.length ? left.slice(i) : right.slice(j));
}
export function mergeSort(array, compareFn = defaultCompare) {
  if (array.length > 1) {
    const { length } = array;
    const middle = Math.floor(length / 2);
    const left = mergeSort(array.slice(0, middle), compareFn);
    const right = mergeSort(array.slice(middle, length), compareFn);
    array = merge(left, right, compareFn);
  }
  return array;
}
```

### 5. quick sort / 快速排序

> Similarly to the merge sort, it also uses the divide-and-conquer approach, dividing the original array into smaller ones (but without splitting them as the merge sort does) to do the sorting.
>
> partition operation / 分区操作

1. First, we need to select a value from the array called ==pivot==, which will be the value at the middle of the array. 
2. We will create two pointers (references)—the left-hand side one will point to the first value of the array, and the right-hand side one will point to the last value of the array. We will move the left pointer until we find a value that is bigger than the pivot, and we will also move the right pointer until we find a value that is less than the pivot and swap them. We will repeat this process until the left-hand side pointer passes the right-hand side pointer. This process helps to have values lower than the pivot reference before the pivot and values greater than the pivot after the pivot reference. This is called the partition operation.
3. Next, the algorithm repeats the previous two steps for smaller arrays (subarrays with smaller values and then subarrays with greater values) until the arrays are completely sorted.

pivot的值可以取头中尾的中位数，8、12、3的排序后的中间位数是8，则取8，这里的事例用的是直接取中位数。

```js
import { Compare, defaultCompare, swap } from '../../util';

function partition(array, left, right, compareFn) {
  const pivot = array[Math.floor((right + left) / 2)];
  let i = left;
  let j = right;

  while (i <= j) {
    while (compareFn(array[i], pivot) === Compare.LESS_THAN) {
      i++;
    }
    while (compareFn(array[j], pivot) === Compare.BIGGER_THAN) {
      j--;
    }
    if (i <= j) {
      swap(array, i, j);
      i++;
      j--;
    }
  }
  return i;
}
function quick(array, left, right, compareFn) {
  let index;
  if (array.length > 1) {
    index = partition(array, left, right, compareFn);
    if (left < index - 1) {
      quick(array, left, index - 1, compareFn);
    }
    if (index < right) {
      quick(array, index, right, compareFn);
    }
  }
  return array;
}
export function quickSort(array, compareFn = defaultCompare) {
  return quick(array, 0, array.length - 1, compareFn);
}

```

### 6. counting sort

The counting sort is the first ==distribution sort== (分布排序) we will learn about in this book. Distribution sort algorithms use ==auxiliary data structures (known as buckets)==that are organized and then merged, resulting in the sorted array. The counting sort uses a temporary array that will store how many times each element appears in the original array. After all the elements are counted, the temporary array is sorted and it can be iterated to construct the resultant sorted array.

==integer sorting algorithm==

```js
export function findMaxValue(array, compareFn = defaultCompare) {
  if (array && array.length > 0) {
    let max = array[0];
    for (let i = 1; i < array.length; i++) {
      if (compareFn(max, array[i]) === Compare.LESS_THAN) {
        max = array[i];
      }
    }
    return max;
  }
  return undefined;
}

export function countingSort(array) {
  if (array.length < 2) {
    return array;
  }
  const maxValue = findMaxValue(array);
  let sortedIndex = 0;
  const counts = new Array(maxValue + 1);
  array.forEach(element => {
    if (!counts[element]) {
      counts[element] = 0;
    }
    counts[element]++;
  });
  // console.log('Frequencies: ' + counts.join());
  counts.forEach((element, i) => {
    while (element > 0) {
      array[sortedIndex++] = i;
      element--;
    }
  });
  return array;
}
```

### 7. bucket sort

> The bucket sort algorithm (also known as bin sort) is also a distributed sorting algorithm that separates the elements into different buckets (smaller arrays), and then uses a simpler sorting algorithm, such as the insertion sort (a good algorithm for small arrays), to sort each bucket. It then merges all the buckets into the resultant sorted array.  (分布排序)

<img src="https://s2.loli.net/2024/12/01/IYORLlfToNMiPz7.png" alt="image-20241201162516846" style="zoom: 50%;" />

### 8. radix sort / 基数排序

> The radix sort algorithm is also a distribution sort algorithm that distributes the integers into buckets based on a number's significant digit or value (the radix, hence the name radix sort). The radix is based on the number system of the values of the arrays. (分布排序)

<img src="https://s2.loli.net/2024/12/01/ecVNgLtKxDJ3wWY.png" alt="image-20241201162637516" style="zoom: 50%;" />

```js
import { findMaxValue, findMinValue } from '../search/min-max-search';

const getBucketIndex = (value, minValue, significantDigit, radixBase) =>
  Math.floor(((value - minValue) / significantDigit) % radixBase);

const countingSortForRadix = (array, radixBase, significantDigit, minValue) => {
  let bucketsIndex;
  const buckets = [];
  const aux = [];
  for (let i = 0; i < radixBase; i++) {
    buckets[i] = 0;
  }
  for (let i = 0; i < array.length; i++) {
    bucketsIndex = getBucketIndex(array[i], minValue, significantDigit, radixBase);
    buckets[bucketsIndex]++;
  }
  for (let i = 1; i < radixBase; i++) {
    buckets[i] += buckets[i - 1];
  }
  for (let i = array.length - 1; i >= 0; i--) {
    bucketsIndex = getBucketIndex(array[i], minValue, significantDigit, radixBase);
    aux[--buckets[bucketsIndex]] = array[i];
  }
  for (let i = 0; i < array.length; i++) {
    array[i] = aux[i];
  }
  return array;
};
export function radixSort(array, radixBase = 10) {
  if (array.length < 2) {
    return array;
  }
  const minValue = findMinValue(array);
  const maxValue = findMaxValue(array);
  // Perform counting sort for each significant digit, starting at 1
  let significantDigit = 1;
  while ((maxValue - minValue) / significantDigit >= 1) {
    // console.log('radix sort for digit ' + significantDigit);
    array = countingSortForRadix(array, radixBase, significantDigit, minValue);
    // console.log(array.join());
    significantDigit *= radixBase;
  }
  return array;
}
```


## Searching algorithms

### 1. sequential search / 顺序搜索

> The sequential search or linear search is the most basic search algorithm. It consists of comparing each element of the data structure with the one we are looking for. It is also the most ==inefficient== one.

<img src="https://s2.loli.net/2024/12/01/dMr8sEIu9k7Nocf.png" alt="image-20241201163553562" style="zoom: 50%;" />

```js
export function sequentialSearch(array, value, equalsFn = defaultEquals) {
  for (let i = 0; i < array.length; i++) {
    if (equalsFn(value, array[i])) {
      return i;
    }
  }
  return -1;
}
```

### 2. binary search / 二分搜索

二分查找和二叉树搜索是不一样的东西

1. the data structure needs to be sorted first
2. A value is selected in the middle of the array. 
3. If the value is the one we are looking for, we are done (the value was found). 
4. If the value we are looking for is less than the selected one, then we will go back to step 1 using the left subarray (lower). 
5. If the value we are looking for is bigger than the selected one, then we will go back to step 1 using the right subarray (higher).

<img src="https://s2.loli.net/2024/12/01/tS7BL3UTHdMwXsV.png" alt="image-20241201163540359" style="zoom: 50%;" />

```js
import { Compare, defaultCompare, DOES_NOT_EXIST } from '../../util';
import { quickSort } from '../sorting/quicksort';

export function binarySearch(array, value, compareFn = defaultCompare) {
  const sortedArray = quickSort(array);
  let low = 0;
  let high = sortedArray.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const element = sortedArray[mid];
    // console.log('mid element is ' + element);
    if (compareFn(element, value) === Compare.LESS_THAN) {
      low = mid + 1;
      // console.log('low is ' + low);
    } else if (compareFn(element, value) === Compare.BIGGER_THAN) {
      high = mid - 1;
      // console.log('high is ' + high);
    } else {
      // console.log('found it');
      return mid;
    }
  }
  return -1; // DOES_NOT_EXIST
}
```

### 3. interpolation search / 插值搜索

> The interpolation search algorithm is an improved variation of the binary search. While the binary search always checks the value in the mid position, the interpolation search might check different places of the array depending on the value that is being searched.

1. the data structure needs to be sorted first
2. A value is selected using the position formula
3. If the value is the one we are looking for, we are done (the value was found) 
4. If the value we are looking for is lesser than the selected one, then we will go back to step 2 using the left subarray (lower) 
5. If the value we are looking for is bigger than the selected one, then we will go back to step 2 using the right subarray (higher)

<img src="https://s2.loli.net/2024/12/01/3HLW7CRnTKPihQv.png" alt="image-20241201164150043" style="zoom:50%;" />

```js
import {
  biggerEquals,
  Compare,
  defaultCompare,
  defaultEquals,
  defaultDiff,
  DOES_NOT_EXIST,
  lesserEquals
} from '../../util';

export function interpolationSearch(
  array,
  value,
  compareFn = defaultCompare,
  equalsFn = defaultEquals,
  diffFn = defaultDiff
) {
  const { length } = array;
  let low = 0;
  let high = length - 1;
  let position = -1;
  let delta = -1;
  while (
    low <= high &&
    biggerEquals(value, array[low], compareFn) &&
    lesserEquals(value, array[high], compareFn)
  ) {
    delta = diffFn(value, array[low]) / diffFn(array[high], array[low]);
    position = low + Math.floor((high - low) * delta);
    if (equalsFn(array[position], value)) {
      return position;
    }
    if (compareFn(array[position], value) === Compare.LESS_THAN) {
      low = position + 1;
    } else {
      high = position - 1;
    }
  }
  return DOES_NOT_EXIST;
}

```

## Shuffle algorithms / 洗牌算法

### Fisher-Yates shuffle / 费舍尔-耶茨

It consists of iterating each position of the array, starting with its last position and swapping the current position with a random position. The random position is lesser than the current position; this way, the algorithm makes sure the positions already shuffled will not be shuffled again (the more we shuffle a deck of cards, the worse is the shuffle).

```js
import { swap } from '../../util';

export function shuffle(array) {
  let currentIndex = array.length;
  while (currentIndex !== 0) {
    const randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    swap(array, currentIndex, randomIndex);
  }
  return array;
}
```

![image-20241201164541666](https://s2.loli.net/2024/12/01/9Iz6muVdWGFDCge.png)
