# Refs:

1. [深度揭秘 Promise 微任务注册和执行过程](https://juejin.cn/post/6844903987183894535)
2. [为什么慢两拍：关于promise规范thenable的白话解释](https://juejin.cn/post/7018765637870698503)
3. https://promisesaplus.com/


题目：

1. [要就来45道Promise面试题一次爽到底](https://juejin.cn/post/6844904077537574919#heading-34)
2. [async, await, promise 面试题](https://www.learnnote.site/frontend/async-await-promise)
3. [一道面试题：还在纠结async/ await、Promise的执行顺序？](https://juejin.cn/post/6871898249578921992)

# Wrap:

| 操作                    | 执行时机             | 是否产生微任务                       |
| :---------------------- | :------------------- | :----------------------------------- |
| `new Promise(executor)` | 同步                 | ❌                                    |
| `resolve()`/`reject()`  | 同步                 | ❌（但使已登记的.then回调有资格入队） |
| `.then(callback)` 登记  | 同步                 | ❌                                    |
| callback 执行           | 微任务               | ✅                                    |
| 链式`.then()`注册       | 前一个callback执行完 | ✅（当条件满足时）                    |

**核心**：`.then()` 本身是同步登记，回调是微任务执行。链式调用中，下一个`.then()`的注册要等前一个回调执行完（如果返回Promise则等其resolve）。

## 核心机制

### 1. **执行顺序原则**

- **Promise 构造函数（executor）**：同步执行
- **`.then()` 注册回调**：同步执行（只是登记）
- **`.then()` 中的回调函数**：微任务执行（异步）

### 2. **微任务入队时机**

javascript

```
const p = new Promise((resolve) => {
  console.log(1);     // ✅ 同步
  resolve(42);        // ✅ 同步：改变状态
  console.log(2);     // ✅ 同步
});

p.then((v) => {       // ✅ 同步：登记回调
  console.log(3);     // ⏳ 微任务：状态已确定，当前调用栈清空后执行
});

console.log(4);       // ✅ 同步
// 输出：1 2 4 3
```



### 3. **状态确定是关键**

- **pending → fulfilled/rejected** 时，已登记的 `.then()` 回调才**有资格**入队
- 入队实际发生在**当前调用栈清空后**

------

## 链式调用规则

### 规则1：下一个 `.then()` 何时注册？

javascript

```
Promise.resolve()
  .then(() => {
    console.log("A");
    // 同步代码执行完 → 下一个 .then 回调注册入队
  })
  .then(() => {
    console.log("B");  // 等A的回调执行完才注册
  });
// 输出：A B
```



### 规则2：返回值影响

javascript

```
Promise.resolve()
  .then(() => {
    console.log("A");
    return Promise.resolve("X"); // 返回新Promise
  })
  .then((res) => {
    console.log("B", res); // 等返回的Promise resolve才注册
  });
// 输出：A → (其他微任务可能插入) → B X
```



### 规则3：同一层级多个 `.then()`

javascript

```
const p = Promise.resolve();
p.then(() => console.log(1));
p.then(() => console.log(2));
// 输出：1 2（按注册顺序）
```



------

## 关键理解点

### 1. **`.then()` 的双重角色**

javascript

```
// 分解理解：
const p = Promise.resolve(42);

// 角色1：同步注册回调
const p2 = p.then(callback);  // ✅ 同步执行

// 角色2：返回新Promise
// callback ⏳ 异步执行（微任务）
```



### 2. **微任务队列是 FIFO**

- 先注册的微任务先执行
- 但**注册时间 ≠ 入队时间**

### 3. **状态改变与入队分离**

javascript

```
const p = new Promise(resolve => {
  resolve(1);          // 状态改变 ✅ 同步
  // 已登记的.then回调"有资格"入队
});

p.then(v => console.log(v)); // 登记回调 ✅ 同步

// 真正入队微任务队列：当前调用栈清空后
console.log(2);  // ✅ 同步
// 输出：2 1
```



------

## 复杂场景分析

### 场景1：嵌套微任务

javascript

```
Promise.resolve()
  .then(() => {
    console.log(1);
    Promise.resolve().then(() => console.log(2));
  })
  .then(() => {
    console.log(3);
  });
// 输出：1 2 3
// 解释：log(3)要等第一个.then回调执行完才注册
```



### 场景2：不同Promise链

javascript

```
Promise.resolve()
  .then(() => console.log("A"))
  .then(() => console.log("C"));

Promise.resolve()
  .then(() => console.log("B"))
  .then(() => console.log("D"));
// 可能输出：A B C D 或 A B D C
// 解释：不同链独立，可能交叉
```



### 场景3：返回Promise的链

javascript

```
Promise.resolve()
  .then(() => {
    console.log(1);
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(2);
        resolve();
      }, 0);
    });
  })
  .then(() => {
    console.log(3); // 等2秒后才执行
  });
// 输出：1 → (事件循环) → 2 → 3
```

# Promise-order

`Promise`可通过`new`或者调用类方法`resolve()`、`reject()`等创建一个实例对象，每一个实例对象都会有`then`、`catch`、`finally`等实例方法。这些方法在调用时会返回一个新生成的promise对象，这就是链式调用的基础。

Promise 构造函数的代码是同步任务，立即执行的。但是 Promise.then 是微任务。

作为复习直接写题会议内容是最快的方式。

## 0. 

```js
// 本质是 return Promise.resolve(4) 触发了 Promise 展开（adopt）+ 额外微任务 的机制。
Promise.resolve().then(() => {
  console.log(0);
  return Promise.resolve(4)
}).then(res => {
  console.log(res)
})

Promise.resolve().then(() => {
  console.log(1);
}).then(() => {
  console.log(2);
}).then(() => {
  console.log(3);
}).then(() => {
  console.log(5);
}).then(() =>{
  console.log(6);
})
// 0,1,2,3,4,5,6

Promise.resolve().then(() => {
  console.log(0);
  return Promise.resolve(4)
}).then(res => {
  console.log(res)
})

// 3 x 2 出6次结果后4进入微队列
Promise.resolve().then(() => {
  console.log(1);
}).then(() => {
  console.log(2);
}).then(() => {
  console.log(3);
}).then(() => {
  console.log(5);
}).then(() =>{
  console.log(6);
})

Promise.resolve().then(() => {
  console.log(99);
}).then(() => {
  console.log(98);
}).then(() => {
  console.log(97);
}).then(() => {
  console.log(96);
}).then(() =>{
  console.log(95);
})
```

------

### 二、整体结构先拆成两条“链”

#### 链 A（带 return Promise）

```js
Promise.resolve()
  .then(() => {
    console.log(0);
    return Promise.resolve(4);
  })
  .then(res => {
    console.log(res);
  });
```

#### 链 B（纯 then 链）

```
Promise.resolve()
  .then(() => console.log(1))
  .then(() => console.log(2))
  .then(() => console.log(3))
  .then(() => console.log(5))
  .then(() => console.log(6));
```

------

### 三、第一轮：同步阶段

- 两个 `Promise.resolve()` 都已经 fulfilled
- 所有 `.then(...)` **只是同步注册回调**
- **没有任何输出**

------

### 四、微任务队列初始状态（关键）

**谁先注册，谁先入队**

```
微任务队列：
A1: 打印 0（链 A 的第一个 then）
B1: 打印 1（链 B 的第一个 then）
```

------

### 五、开始执行微任务（逐拍分析）

------

#### 🥇 微任务 A1

```
() => {
  console.log(0);
  return Promise.resolve(4);
}
```

输出：

```
0
```

##### ⚠️ 重点：这里发生了什么？

- 返回了一个 **已经 fulfilled 的 Promise**

- 但 **规范规定**：

  > 外层 Promise **不会立刻变 fulfilled**

- 而是：

  1. **创建一个 PromiseResolveThenableJob（微任务）**
  2. 用来“展开”这个 Promise（adopt 它的状态）

👉 **这就是第 1 拍延迟**

------

#### 当前微任务队列变成：

```
B1: 打印 1
A_adopt: Promise 展开任务
```

------

#### 🥈 微任务 B1

输出：

```
1
```

- 普通 then
- 返回 `undefined`
- 下一步 B2 立刻可以排队

------

#### 🥉 微任务 B2

输出：

```
2
```

------

#### 🥊 微任务 B3

输出：

```
3
```

------

#### 🟢 微任务 A_adopt（关键）

- 把链 A 的第二个 `.then(res => ...)` **真正排入队列**

------

#### 🟣 微任务 A2

```
res => {
  console.log(res);
}
```

输出：

```
4
```

------

#### 剩余链 B 继续

```
5
6
```

------

### 六、为什么叫“慢两拍”？

我们数一下 **链 A 相比链 B 多了什么**：

#### 链 B（普通 then）

```
then → 直接入微任务
```

#### 链 A（return Promise）

```
then
↓
返回 Promise
↓
额外一个「Promise 展开微任务」
↓
下一个 then 才能入队
```

👉 **多了整整一个微任务调度阶段**
 再加上队列里已经有别的微任务在跑
 **体感就是“慢两拍”**

------

### 七、如果你把代码改一行，立刻不慢了

#### ❌ 原来（慢）

```
return Promise.resolve(4)
```

#### ✅ 改成（快）

```
return 4
```

输出会变成：

```
#0
4
1
2
3
5
6
```

👉 因为：

- `return 4`
   → 外层 Promise **立刻 fulfilled**
   → 下一个 `.then` **立刻入微任务队列**

------

### 八、一句“规范级总结”（你可以背）

> **`.then` 返回普通值：
>  下一个 then 直接入微任务。
>
> `.then` 返回 Promise：
>  必须先经历一次 Promise 展开（adopt），
>  多一个微任务，
>  所以看起来会“慢两拍”。**

## 1. 

```js
 // 说出以下输出顺序
 setTimeout(function () {
   console.log(1);
 }, 0);

 await new Promise(function (resolve) {
   // 这里是构造函数，这里是同步任务
   console.log(2);
   resolve();
   console.log(3);
 }).then(function () {
   console.log(4);
 });

 console.log(5);
```

## 2. 

```js
// 说出以下输出顺序
 setTimeout(function () {
   console.log(1);
 }, 0);

 new Promise(function (resolve) {
   console.log(2);
   resolve();
   console.log(3);
 }).then(function () {
   console.log(4);
 });
 console.log(5);
```

## 3. 

链式同层 `.then()` 的所有回调，都会在同步阶段就完成注册；

但某个回调是否能进入微任务队列，取决于它所依赖的 Promise 是否已经 settle。由于外层 Promise 可能更早 settle，其 then 回调可能比内部链式 Promise 的后续回调更早进入微任务队列；

链式 `.then()` 的所有回调，都会在各自所在的同步代码执行时完成注册；
回调函数的执行顺序，不由注册顺序直接决定，而由它们被推进微任务队列的先后顺序决定；
微任务队列是 FIFO；
回调何时进入微任务队列，取决于它所依赖的 Promise 何时 settle；
因此外层 Promise 可能更早 settle，其回调可能比内部链式 Promise 的后续回调更早进入微任列，从而在执行顺序上看起来像“插队”。

```js
new Promise(resolve => resolve())
  .then(() => {
    console.log(2);
  })
  .then(() => {
    console.log(6);
  });

// 第一个 .then 的回调：console.log(2)
// 链式 then 的下一个回调：console.log(6)
// console.log(6) 挂在谁上？
// 👉 挂在 第一个 then 返回的 Promise 上
```

```js
setTimeout(() => {
  console.log("0"), 0;
});

new Promise((resolve, reject) => { // pA
  console.log("1");
  resolve(1);
})
  .then(() => { // then pA-1 
    console.log("2"); 
    new Promise((resolve, reject) => { // pA1
      console.log("3");
      resolve();
    })
      .then(() => { // then pA1-1
        console.log("4");
      })
      .then(() => { // then pA1-2
        console.log("5");
      });
  })
  .then(() => { // then pA-3
    console.log("6");
  });

new Promise((resolve, reject) => { // pB
  console.log("7");
  resolve();
}).then(() => { // then pB-1
  console.log("8");
});
```

then(5) 注册在内部 Promise.then(4) 上 → 还不能入队（依赖 then(4) 执行完成）

**外层 then(6) 所依赖的 Promise 在 then(2) 执行完后 resolve → 6 进入微任务队列** ✅

```js
then6 在executor执行时已注册
队列中先有：then(2)微任务
执行then(2)回调:
  log2 -> 2
  内部Promise executor -> log3
  内部then(4)注册 -> 入队微任务
then(2)回调结束 -> then(6)可入队
fullfilled then5 入队列
```

## 4. 

**浏览器和规范的微任务调度，会**把 `.then()` 内部注册的回调**紧跟当前微任务一起入队**，而不是放到下一轮微任务队列的末尾。

**链式 then 的下一个回调注册时机**：

- Node.js: 前一个 then 执行完才注册微任务 → 可能出现“插队”
- 浏览器：链式 then 会紧跟在当前微任务队列中 **保证顺序**

**微任务队列是 FIFO**

**浏览器实现保证**：

- 内部链式 then 优先注册
- 外层 then 的下一个 then 放在后面

```js
new Promise((resolve) => {
  // p1
  setTimeout(() => {
    console.log(6);
    new Promise((resolve) => {
      resolve();
    }).then(() => {
      console.log(7);
    });
  });
  resolve();
})
  .then(() => {
    // then1
    new Promise((resolve) => {
      // p2
      resolve();
    })
      .then(() => {
        // then 1 - 1
        console.log(1);
      })
      .then(() => {
        // then 1 - 2
        console.log(2);
      });
  })
  .then(() => {
    // then 2
    new Promise((resolve) => {
      // p3
      resolve();
    })
      .then(() => {
        // then 2 - 1
        new Promise((resolve) => {
          // p4
          resolve();
        }).then(() => {
          // then 2 - 1 - 1
          console.log(4);
        });
      })
      .then(() => {
        // then 2 - 1 - 2
        console.log(5);
      });
  })
  .then(() => {
    // then 3
    console.log(3);
  });

```

## 5. 

```js
new Promise((resolve, reject) => {
  console.log("1"); // p1
  resolve();
})
  .then(() => { // then 1
    console.log("2");

    new Promise((resolve, reject) => { // p2
      console.log("3");
      resolve();
    })
      .then(() => { // then 2
        console.log("4");
      })
      .then(() => { // then 3
        console.log("5");
      });
  })
  .then(() => { // then 4
    console.log("6");
  });

```

## 6. 

```js
new Promise((resolve) => { // p1
  resolve();
})
  .then( // then 1
    () => {
      console.log("1");
    }
  )
  .then(() => {  // then 2
    console.log("2");
  })
  .then(() => { // then 3
    console.log("3");
  });

new Promise((resolve) => { // p2
  resolve(2);
})
  .then(() => { // then 4
    console.log("4");
  })
  .then(() => { // then 5
    console.log("5");
  })
  .then(() => { // then 6
    console.log("6");
  });
```



```js
new Promise((resolve) => { // p1
  resolve();
})
  .then( // then1
    () => {
      return new Promise((r) => { // p1-1
        console.log("A");
        r();
      }).then(() => { // then1-1
        console.log("B");
      })
      .then(() => { // then1-2
        console.log("C");
      });
    }
  )
  .then(() => {  // then2
    console.log("2");
  })
  .then(() => { // then3
    console.log("3");
  });

new Promise((resolve) => { // p2
  resolve(2);
})
  .then(() => { // then4
    console.log("4");
  })
  .then(() => { // then5
    console.log("5");
  })
  .then(() => { // then6
    console.log("6");
  });
```

1. `.then` 回调如果**返回 Promise**，则后续的 `.then` 会等待这个 Promise 解决

2. 微任务队列按**先进先出**顺序执行

3. 不同 Promise 链的微任务**交替执行**

4. `then1-1` 执行完后不会立即触发 `then2` 入队。then1 返回的 Promise 需要等待整个 Promise 链解决，而不仅仅是 `then1-1` 执行完。

5. 当一个 Promise 被 resolve 时，**它关联的 .then 回调是作为微任务加入队列的**。
   同样，**一个 .then 回调执行完后，它返回的 Promise 被 resolve，这个 resolve 操作本身也是一个微任务**。

   所以 `then1-1` 执行完后，不能立即让 `then2` 入队，而是要先加入一个"resolve 操作"的微任务，这个微任务执行后才触发 `then2` 入队。

```js
队列：[then1-1, then5]
执行 then1-1: 输出 "1-1 p1"，然后产生一个微任务"resolve P_then1-1"
队列变为：[then5, 微任务R]  // R 表示 resolve P_then1-1 的微任务

执行 then5: 输出 "5"，then6入队
队列变为：[微任务R, then6]

执行 微任务R: 触发 then2 入队
队列变为：[then6, then2]

执行 then6: 输出 "6"
队列变为：[then2]

执行 then2: 输出 "2"，then3入队
队列变为：[then3]

执行 then3: 输出 "3"
```

// image

## 7.

```js
const first = () =>
  new Promise((resolve, reject) => { // p1
    console.log(3);
    let p = new Promise((resolve, reject) => { // p2
      console.log(7);
      setTimeout(() => {
        console.log(5);
        resolve(6);
      }, 0);
      resolve(1);
    });
    resolve(2);
    p.then((arg) => { // then 2
      console.log(arg);
    });
  });

first().then((arg) => { // then1
  console.log(arg);
});

console.log(4);

```

## 8.

1. Promise 构造函数只执行一次

2. `promise.then(fn)` 只有在 Promise 已经确定状态时，才会把 `fn` 放进微任务队列；
   如果 Promise 还是 `pending`，就只能“订阅”，没法入队。

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success')
  }, 1000)
})

const promise2 = promise1.then(() => { // p2 then
  throw new Error('error!!!')
})

console.log('promise1', promise1) // p1
console.log('promise2', promise2) // p2

setTimeout(() => { // func1
  console.log('promise1', promise1)
  console.log('promise2', promise2)
}, 2000)
```

```js
时间 0s：
  - p1: pending, p2: pending
  - 输出：promise1 pending, promise2 pending

时间 1s：
  - p1 resolve → fulfilled
  - then 回调进入微任务队列
  - 执行 then 回调 → 抛出错误 → p2 rejected

时间 2s：
  - 输出：promise1 fulfilled, promise2 rejected
```

## 9.

promise 状态一旦改变则不能再变。

```js
const promise = new Promise((resolve, reject) => {
  resolve('success1')
  reject('error')
  resolve('success2')
})

promise
  .then((res) => {
    console.log('then: ', res)
  })
  .catch((err) => {
    console.log('catch: ', err)
  })
```

## 10. 

promise 可以链式调用。提起链式调用我们通常会想到通过 return this 实现，不过 Promise 并不是这样实现的。promise 每次调用 .then 或者 .catch 都会返回一个新的 promise，从而实现了链式调用。

```js
Promise.resolve(1)            // 创建已fulfilled的Promise，值为1
  .then((res) => {            // then1
    console.log(res)          // 输出: 1
    return 2                  // 返回2
  })
  .catch((err) => {           // catch1（不会执行）
    return 3
  })
  .then((res) => {            // then2
    console.log(res)          // 输出: 2
  })
```

## 11. 

1. Promise 构造函数只执行一次

2. `promise.then(fn)` 只有在 Promise 已经确定状态时，才会把 `fn` 放进微任务队列；
    如果 Promise 还是 `pending`，就只能“订阅”，没法入队。

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('once')
    resolve('success')
  }, 1000)
})

const start = Date.now()
promise.then((res) => {
  console.log(res, Date.now() - start)
})
promise.then((res) => {
  console.log(res, Date.now() - start)
})
```

```scss
同步阶段
│
├─ promise.then(fn1)   // 订阅
├─ promise.then(fn2)   // 订阅
│
└─ setTimeout(...)     // 宏任务

1s 后
┌───────────────┐
│ 宏任务队列     │ → 执行 setTimeout
└───────────────┘
        ↓
   resolve()
        ↓
┌───────────────┐
│ 微任务队列     │
│ fn1           │
│ fn2           │
└───────────────┘
        ↓
   fn1 → fn2

```

## 12.

```js
Promise.resolve()
  .then(() => {
    return new Error('error!!!')
  })
  .then((res) => {
    console.log('then: ', res)
  })
  .catch((err) => {
    console.log('catch: ', err)
  })
```

.then 或者 .catch 中 return 一个 error 对象并不会抛出错误，所以不会被后续的 .catch 捕获，需要改成其中一种：

```js
return Promise.reject(new Error('error!!!'))
throw new Error('error!!!')
```

因为返回任意一个非 promise 的值都会被包裹成 promise 对象，即 `return new Error('error!!!')` 等价于` return Promise.resolve(new Error('error!!!'))`。

## 13.

```js
Promise.resolve()
  .then(
    function success1(res) {
      throw new Error("error");
    },
    function fail1(e) {
      console.error("fail1: ", e); // fail1 只捕获前一个 Promise 的 rejection，不捕获 success1 函数内部抛出的错误
    }
  )
  .then(
    function success2(res) {},
    function fail2(e) {
      console.error("fail2: ", e);
    }
  );

```

解析：`.then`可以接收两个参数，第一个是处理成功的函数，第二个是处理错误的函数。`.catch` 是 `.then` 第二个参数的简便写法，但是它们用法上有一点需要注意：`.then` 的第二个处理错误的函数捕获不了第一个处理成功的函数抛出的错误，而后续的 `.catch `可以捕获之前的错误。当然以下代码也可以：

```js
Promise.resolve()
  .then(function success1(res) {
    throw new Error("error");
  })
  .then(
    null,  // 对应原代码的 success2（不执行）
    function fail2(e) {  // 对应原代码的 fail2
      console.error("fail2: ", e);
    }
  );
```

## 14. 

```js
process.nextTick(() => {
  console.log("nextTick");
});
Promise.resolve().then(() => {
  console.log("then");
});
setImmediate(() => {
  console.log("setImmediate");
});
console.log("end");
```

process.nextTick 和 promise.then 都属于 microtask，而 setImmediate 属于 macrotask，在事件循环的 check 阶段执行。事件循环的每个阶段（macrotask）之间都会执行 microtask，事件循环的开始会先执行一次 microtask。

## ==15.==

----

`then` 返回 Promise 会产生 **PromiseResolveThenableJob

```js
Promise.resolve() // p1
  .then(() => {
    // A1
    console.log(1);
    return Promise.resolve(2); // p-a1
  })
  .then((res) => {
    // A2
    console.log(res);
  })
  .then(() => {
    // A3
    console.log(3);
  });

Promise.resolve() // p2
  .then(() => {
    // B1
    console.log(10);
  })
  .then(() => {
    // B2
    console.log(20);
  })
  .then(() => {
    // B3
    console.log(30);
  })
  .then(() => {
    // B4
    console.log(40);
  });

```

<img src="https://s2.loli.net/2026/01/14/GlCPqnXNJmhLYbw.png" alt="IMG_3346" style="zoom:33%;" />

-------

## 16.

```js
new Promise((resolve, reject) => {
  console.log("1"); // P1
  resolve();
})
  .then(() => {
    // P1 - 1
    console.log("2");
    new Promise((resolve, reject) => {
      // P2
      console.log("3");
      resolve();
    })
      .then(() => {
        // P2 - 1
        console.log("4");
      })
      .then(() => {
        // P2 - 2
        console.log("5");
      });
  })
  .then(() => {
    // P1 - 2
    console.log("6");
  });
```

## 17. 

链式调用数据会透传，非链式调用的then的值，在promise有返回结果之后则不会再更改

```js
// 代码来自 [Promise 链](https://zh.javascript.info/promise-chaining)
// Promise 构造（通过 Promise 构造函数创建 Promise 实例）其中传入的函数称为 executor。
let promise = new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000); // executor
});

promise.then(function(result) {
  console.log(result); // 1
  return result * 2;
});

promise.then(function(result) {
  console.log(result) // 1
  return result * 2;
});

promise.then(function(result) {
 console.log(result) // 1
  return result * 2;
});
```

```js
// 代码来自 [Promise 链](https://zh.javascript.info/promise-chaining)
new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000); 
})
.then(function(result) {
  console.log(result); 
  return result * 2;
})
.then(function(result) { 
  console.log(result); 
  return result * 2;
})
.then(function(result) {
  console.log(result); 
  return result * 2;
});
```

## 18.

```js
new Promise((resolve) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    new Promise((resolve) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => { // then 2
        console.log(4);
      })
      .then(() => { // then 3
        console.log(5);
      });
  })
  .then(() => { // then 4
    console.log(6);
  });

```

## 19. 

因为 `then1` `return`了一个 Promise（p2 的整个链）。`then6` 要等待这个` Promise `解决后才能执行。

因为这是一个**单链**，没有多个独立的 Promise 链竞争。所有的 .then 都依赖于前一个。

```js
new Promise((resolve) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    return new Promise((resolve) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => { // then 2
        console.log(4);
      })
      .then(() => {  // then 3
        console.log(5);
      })
      .then(() => {  // then 4
        console.log(7);
      })
      .then(() => {  // then 5
        console.log(8);
      });
  })
  .then(() => { // then 6
    console.log(6);
  });

```

```js
new Promise((resolve) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    new Promise((resolve) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => { // then 2
        console.log(4);
      })
      .then(() => {  // then 3
        console.log(5);
      })
      .then(() => {  // then 4
        console.log(7);
      })
      .then(() => {  // then 5
        console.log(8);
      });
  })
  .then(() => { // then 6
    console.log(6);
  });

```

## 20.

```js
new Promise((resolve) => {
  console.log(1);
  resolve();
})
  .then(async () => {
    console.log(2);
    // P2
    // 也等同于 return await P2
    await new Promise((resolve) => {
      console.log(3);
      resolve();
    })
      .then(() => {
        console.log(4);
      })
      .then(() => {
        console.log(5);
      });
  })
  .then(() => {
    console.log(6);
  });

```

## 21. 

```js
new Promise((resolve) => {
  // p1
  console.log(1);
  resolve();
})
  .then(() => {
    // then 1
    console.log(2);
    new Promise((resolve) => {
      // p2
      console.log(3);
      resolve();
    })
      .then(() => console.log(4)) // then 2
      .then(() => console.log(5)) // then 3
      .then(() => console.log(6)); // then 4
  })
  .then(() => console.log(7)) // then 5
  .then(() => console.log(8)); // then 6

```

```js
new Promise((resolve) => { // p1
  console.log(1);
  resolve();
}) // async
  .then(async () => { // then 1
    console.log(2);
    new Promise((resolve) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => console.log(4))  // then 2
      .then(() => console.log(5))  // then 3
      .then(() => console.log(6));  // then 4
  })
  .then(() => console.log(7))  // then 5
  .then(() => console.log(8));  // then 6
```

## ==22.==

这里有thenablejob

**"thenable job"** 指的是当 Promise 解析（resolve）一个 thenable 对象时产生的额外微任务。在 Promise A+ 规范中，这称为 **"PromiseResolveThenableJob"**。

在 Promise A+ 规范中，当一个 Promise 解决另一个 Promise 时（Promise resolution），需要有一个额外的微任务来处理这个 "解包"（unwrapping）过程。

**关键点**：当 then1 返回一个 **原始 Promise 对象** 时，根据 Promise 规范，需要 **PromiseResolveThenableJob** 来处理！

在第23题，返回的是 `.then()` 的结果，**不是原始 Promise**，所以没有额外的 thenable job。

```js
new Promise((resolve) => { // p1
  resolve();
})
  .then(() => { // then 1
    return new Promise((r) => { // p2
      console.log("promise");
      r(5);
    });
  })
  .then((r) => {  // then 2
    console.log(r);
  });

new Promise((resolve) => { // p3
  resolve(2);
})
  .then(() => {  // then 3
    console.log("1");
  })
  .then(() => {  // then 4
    console.log("2");
  })
  .then(() => {  // then 5
    console.log("3");
  })
  .then(() => {  // then 6
    console.log("4");
  });

```

```js
new Promise((resolve) => { // p1
  resolve();
})
  .then(() => { // then 1
    new Promise((r) => { // p2
      console.log("promise");
      r(5);
    });
  })
  .then((r) => {  // then 2
    console.log(r);
  });

new Promise((resolve) => { // p3
  resolve(2);
})
  .then(() => {  // then 3
    console.log("1");
  })
  .then(() => {  // then 4
    console.log("2");
  })
  .then(() => {  // then 5
    console.log("3");
  })
  .then(() => {  // then 6
    console.log("4");
  });

```

## 23.

```js
new Promise((resolve) => { // p1
  resolve();
})
  .then(() => { // then 1
  	// 返回的是 `.then()` 的结果，**不是原始 Promise**，所以没有额外的 thenable job。直接按正常的队列流程进栈就好
    return new Promise((r) => { // p2 
      console.log("1");
      r();
    }).then(() => { // then 2
      console.log("2");
    });
  })
  .then(() => { // then 3
    console.log("3");
  });

new Promise((resolve) => { // p3
  resolve(2);
})
  .then(() => { // then 4
    console.log("4");
  })
  .then(() => { // then 5
    console.log("5");
  })
  .then(() => { // then 6
    console.log("6");
  });

```

<img src="https://s2.loli.net/2026/01/14/EyXBzse6MH1UCVT.png" alt="IMG_3348" style="zoom:33%;" />

## 24. 

```js
new Promise((resolve, reject) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    new Promise((resolve, reject) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => { // then 2
        console.log(4);
      })
      .then(() => { // then 4
        console.log(5);
      });
  })
  .then(() => { // then 5
    console.log(6);
  });

```

## 25. 

```js
new Promise((resolve, reject) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    let p = new Promise((resolve, reject) => { // p2
      console.log(3);
      resolve();
    });
    p.then(() => { // then 2
      console.log(4);
    });
    p.then(() => { // then 3
      console.log(5);
    });
  })
  .then(() => { // then 5
    console.log(6);
  });
```

## 26.

```js
new Promise((resolve, reject) => { // p1
  console.log(1);
  resolve();
})
  .then(() => { // then 1
    console.log(2);
    new Promise((resolve, reject) => { // p2
      console.log(3);
      resolve();
    })
      .then(() => { // then 2
        console.log(4);
      })
      .then(() => { // then 3
        console.log(5);
      });
    return new Promise((resolve, reject) => { // p3
      console.log(6);
      resolve();
    })
      .then(() => { // then 4
        console.log(7);
      })
      .then(() => { // then 5
        console.log(8);
      });
  })
  .then(() => { // then 6
    console.log(9);
  });

```

## 27.

Thenablejob

如果有多个`fulfilled`的`Promise`实例，同时执行`then`链式调用，`then`会交替执行。

这是编译器的优化，防止一个 `Promise`占据过多时间。

在`then`中返回`Promise`实例，会出现 `慢两拍`的效果，具体表现为等待两个`.then()`执行完成。

- 第一拍：`Promise`需要等待`pending`变为`fulfilled`状态
- 第二拍：`then`函数挂载到`MicroTaskQueue`中

```js
// then 中无 返回 Promise 的情况
Promise.resolve()
  .then(() => {
    console.log(0);
  })
  .then(() => {
    console.log(2);
  })
  .then(() => {
    console.log(4);
  })
  .then(() => {
    console.log(6);
  });

Promise.resolve()
  .then(() => {
    console.log(1);
  })
  .then(() => {
    console.log(3);
  })
  .then(() => {
    console.log(5);
  })
  .then(() => {
    console.log(7);
  });
```

```js
Promise.resolve() // p1
  .then(() => { // then 1
    console.log(0);
    return Promise.resolve(4); // p2
  })
  .then((res) => { // then 2
    console.log(res);
  })
  .then(() => { // then 3
    console.log(6);
  })
  .then(() => { // then 4
    console.log(7);
  });

Promise.resolve() // p3
  .then(() => { // then 5
    console.log(1);
  })
  .then(() => { // then 6
    console.log(2);
  })
  .then(() => { // then 7
    console.log(3);
  })
  .then(() => { // then 8
    console.log(5);
  });
```
