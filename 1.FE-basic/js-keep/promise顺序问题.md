# promise顺序问题

`Promise`可通过`new`或者调用类方法`resolve()`、`reject()`等创建一个实例对象，每一个实例对象都会有`then`、`catch`、`finally`等实例方法。这些方法在调用时会返回一个新生成的promise对象，这就是链式调用的基础。

Promise 构造函数的代码是同步任务，立即执行的。但是 Promise.then 是微任务。

作为复习直接写题会议内容是最快的方式

## 1. 

```js
 // 说出以下输出顺序
 setTimeout(function () {
   console.log(1);
 }, 0);

 await new Promise(function (resolve) {
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

==`.then()` 的回调不是“立刻加入队列”，而是： 当前 then 执行完后，才把“下一个 then”加入微任务队列。==链式 then 是“执行一个，注册下一个”；**链式 then 的下一个回调**只有在前一个 then 执行完才注册，**外层 then 的下一个 then**注册时机可能比内部链式 then 的第二个 then 早，**微任务队列是 FIFO** → 注册顺序决定执行顺序，因此会出现 **“链式 then 中间被外层 then 插队”** 的情况。

```js
setTimeout(() => {
  console.log("0"), 0;
});

new Promise((resolve, reject) => {
  console.log("1");
  resolve(1);
})
  .then(() => {
    console.log("2");
    new Promise((resolve, reject) => {
      console.log("3");
      resolve();
    })
      .then(() => {
        console.log("4");
      })
      .then(() => {
        console.log("5");
      });
  })
  .then(() => {
    console.log("6");
  });

new Promise((resolve, reject) => {
  console.log("7");
  resolve();
}).then(() => {
  console.log("8");
});

```

## 4. 

**浏览器和规范的微任务调度，会**把 `.then()` 内部注册的回调**紧跟当前微任务一起入队**，而不是放到下一轮微任务队列的末尾。

？？？？？？？/1324567

**链式 then 的下一个回调注册时机**：

- Node.js: 前一个 then 执行完才注册微任务 → 可能出现“插队”
- 浏览器：链式 then 会紧跟在当前微任务队列中 **保证顺序**

**微任务队列是 FIFO**

**浏览器实现保证**：

- 内部链式 then 优先注册
- 外层 then 的下一个 then 放在后面

```js
new Promise((resolve) => {
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
    new Promise((resolve) => {
      resolve();
    })
      .then(() => {
        console.log(1);
      })
      .then(() => {
        console.log(2);
      });
  })
  .then(() => {
    new Promise((resolve) => {
      resolve();
    })
      .then(() => {
        new Promise((resolve) => {
          resolve();
        }).then(() => {
          console.log(4);
        });
      })
      .then(() => {
        console.log(5);
      });
  })
  .then(() => {
    console.log(3);
  });

```

## 5. 

```js
new Promise((resolve, reject) => {
  console.log("1");
  resolve();
})
  .then(() => {
    console.log("2");

    new Promise((resolve, reject) => {
      console.log("3");
      resolve();
    })
      .then(() => {
        console.log("4");
      })
      .then(() => {
        console.log("5");
      });
  })
  .then(() => {
    console.log("6");
  });

```

## 6. 

```js
new Promise((resolve) => {
  resolve();
})
  .then(
    // () => {
    //   return new Promise((r) => {
    //     console.log("1-1");
    //     // r();
    //   }).then(() => {
    //     console.log("1-1 p1");
    //   });
    // }
    () => {
      console.log("1");
    }
  )
  .then(() => {
    console.log("2");
  })
  .then(() => {
    console.log("3");
  });

new Promise((resolve) => {
  resolve(2);
})
  .then(() => {
    console.log("4");
  })
  .then(() => {
    console.log("5");
  })
  .then(() => {
    console.log("6");
  });
```

## 7.

```js
const first = () => (new Promise((resolve, reject) => {
    console.log(3);
    let p = new Promise((resolve, reject) => {
        console.log(7);
        setTimeout(() => {
            console.log(5);
            resolve(6);
        }, 0)
        resolve(1);
    });
    resolve(2);
    p.then((arg) => {
        console.log(arg);
    });

}));

first().then((arg) => {
    console.log(arg);
});
console.log(4);
```

## 8.

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success')
  }, 1000)
})
const promise2 = promise1.then(() => {
  throw new Error('error!!!')
})

console.log('promise1', promise1)
console.log('promise2', promise2)

setTimeout(() => {
  console.log('promise1', promise1)
  console.log('promise2', promise2)
}, 2000)
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
Promise.resolve(1)
  .then((res) => {
    console.log(res)
    return 2
  })
  .catch((err) => {
    return 3
  })
  .then((res) => {
    console.log(res)
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

因为返回任意一个非 promise 的值都会被包裹成 promise 对象，即 return new Error('error!!!') 等价于 return Promise.resolve(new Error('error!!!'))。

## 13.

```js
Promise.resolve()
  .then(function success1 (res) {
    throw new Error('error')
  }, function fail1 (e) {
    console.error('fail1: ', e)
  })
  .then(function success2 (res) {
  }, function fail2 (e) {
    console.error('fail2: ', e)
  })v
```

解析：.then 可以接收两个参数，第一个是处理成功的函数，第二个是处理错误的函数。.catch 是 .then 第二个参数的简便写法，但是它们用法上有一点需要注意：.then 的第二个处理错误的函数捕获不了第一个处理成功的函数抛出的错误，而后续的 .catch 可以捕获之前的错误。当然以下代码也可以：

```js
Promise.resolve()
  .then(function success1 (res) {
    throw new Error('error')
  }, function fail1 (e) {
    console.error('fail1: ', e)
  })
  .then(function success2 (res) {
  }, function fail2 (e) {
    console.error('fail2: ', e)
  })
```

## 14. 

```js
process.nextTick(() => {
  console.log('nextTick')
})
Promise.resolve()
  .then(() => {
    console.log('then')
  })
setImmediate(() => {
  console.log('setImmediate')
})
console.log('end')
```

process.nextTick 和 promise.then 都属于 microtask，而 setImmediate 属于 macrotask，在事件循环的 check 阶段执行。事件循环的每个阶段（macrotask）之间都会执行 microtask，事件循环的开始会先执行一次 microtask。

## 15. 

----

### `then` 返回 Promise 会产生 **PromiseResolveThenableJob**？？？？？？？？

- **这个 Job 会立刻被插入当前微任务队列**，不是排在微任务队列尾，而是 **当前正在执行的微任务之后立即执行**
- 所以 A2 的注册微任务 **会在 B3 执行后立即执行，先于 B4 注册**

这就是我的问题了，为什么A2会插队

```js
// A 链
Promise.resolve().then(() => {          // A1
  console.log(1);
  return Promise.resolve(2);            // 返回一个已 fulfilled 的 Promise
}).then((res) => {                      // A2
  console.log(res);
}).then(() => {                         // A3
  console.log(3);
});

// B 链
Promise.resolve().then(() => {          // B1
  console.log(10);
}).then(() => {                         // B2
  console.log(20);
}).then(() => {                         // B3
  console.log(30);
}).then(() => {                         // B4
  console.log(40);
});

```



-------

## 16.

当执行 then 方法时，如果前面的 promise 已经是 resolved 状态，则直接将回调放入微任务队列中

如果 then 中的回调返回了一个 promise，那么 then 返回的 promise 会等待这个 promise 被 resolve 后再 resolve。

```js
new Promise((resolve, reject) => {
  console.log("1");           // P1 executor
  resolve();
})
  .then(() => {               // P1 then1
    console.log("2");         
    new Promise((resolve, reject) => {  // P2 executor
      console.log("3");       
      resolve();
    })
      .then(() => {           // P2 then1
        console.log("4");
      })
      .then(() => {           // P2 then2
        console.log("5");
      });
  })
  .then(() => {               // P1 then2
    console.log("6");
  });

```

promise 的 then/catch 方法执行后会也返回一个 promise

当执行 then 方法时，如果前面的 promise 已经是 resolved 状态，则直接将回调放入微任务队列中

then 方法是同步执行的，回调才是异步的

回调事件根据 promise 状态不同，处理也不同：

4.1 pending : 回调会储存在 promise 内部，既不会执行，也不放到微任务中

4.2 resolve : 会遍历之前通过 then 给这个 promise 注册的所有回调，将它们依次放入微任务队列中

then 负责注册回调，不会触发回调，也不会将它推入微任务队列中去，是 resolve 负责将回调推入微任务队列，由事件循环取出并执行

对于 then 方法返回的 promise 它是没有 resolve 函数的，取而代之只要 then 中回调的代码执行完毕并**获得同步返回值**，这个 then 返回的 promise 就算被 resolve。`同步返回值`的意思换句话说，如果 then 中的回调返回了一个 promise，那么 then 返回的 promise 会等待这个 promise 被 resolve 后再 resolve。

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
// P1
new Promise(resolve => {
  console.log(1)
  resolve()
}).then(() => {
  console.log(2)
  // P2
  new Promise(resolve => {
    console.log(3)
    resolve()
  }).then(() => {
    console.log(4)
  }).then(() => {
    console.log(5)
  })
}).then(() => {
    console.log(6)
  })
// 1
// 2
// 3
// 4
// 注意：此时 P1 的第一个 then - 2 就算是执行完毕了，下面会执行 P1 的第二个 then
// 6
// 5
```

## 19. 

对于 then 方法返回的 promise 它是没有 resolve 函数的，取而代之只要 then 中回调的代码执行完毕并**获得同步返回值**，这个 then 返回的 promise 就算被 resolve。`同步返回值`的意思换句话说，如果 then 中的回调返回了一个 promise，那么 then 返回的 promise 会等待这个 promise 被 resolve 后再 resolve。

在第一个 `then` 里 `return` 了一个 `new Promise` ，最重要的是，内部的四个 `then` 是一起被返回的。外层代码下一个 `then` 必须等到 `return` 代码执行完成，**Promise 状态变更后**， 后面的 `then` 才能执行。`return` 未完成，第一个 `then` 就未完成，外部第二个 `then` 就要等着。

```js
// P1
new Promise(resolve => {
  console.log(1)
  resolve()
}).then(() => {
  console.log(2)
  // P2 , 和上面对比多了一个return
  return new Promise(resolve => {
    console.log(3)
    resolve()
  }).then(() => {
    console.log(4)
  }).then(() => {
    console.log(5)
  }).then(() => {
    console.log(7)
  }).then(() => {
    console.log(8)
  })
}).then(() => {
    console.log(6)
  })
// 1
// 2
// 3
// 4
// 注意：这里可以看到，跟上个例子不用的地方就在于，这里用了 return ，所以 P1 的第一个 then 执行完毕得等待 P2 完整执行完才算是执行完，才能 return 一个同步返回值回去
// 所以这里的结果跟上个例子不一样了
// 5
// 7
// 8
// 6
```

## 20.

```js
new Promise(resolve => {
  console.log(1)
  resolve()
}).then(async () => {
  console.log(2)
  // P2
  // 也等同于 return await P2
  await new Promise(resolve => {
    console.log(3)
    resolve()
  }).then(() => {
    console.log(4)
  }).then(() => {
    console.log(5)
  })
}).then(() => {
    console.log(6)
  })
// 1
// 2
// await 表达式会暂停整个 async 函数的执行进程并出让其控制权，只有当其等待的基于 promise 的异步操作被兑现或被拒绝之后才会恢复进程。promise 的解决值会被当作该 await 表达式的返回值。所以 P2 会被完整执行完毕后，当做 await 表达式的返回值，如果 await 后没有其他的代码的话（如果有，将会继续执行），不管是否 return ，此时都相当于执行完同步代码了，也就是 P1 的 then 执行完毕了
// 3
// 4
// 5
// 6
```

## 21. 

```js
// 简称 p1
new Promise(resolve => {
  console.log(1);
  resolve();
}) // no async
.then(() => {
  console.log(2)
  // 简称 p2
  new Promise(resolve => {
    console.log(3);
    resolve();
  })
  .then(() => console.log(4))
  .then(() => console.log(5))
  .then(() => console.log(6))
})
.then(() => console.log(7))
.then(() => console.log(8))
// 1 2 3 4 7 5 8 6
```

```js
// 简称 p1
new Promise(resolve => {
  console.log(1);
  resolve();
}) // async 
.then(async () => {
  console.log(2)
  // 简称 p2
  new Promise(resolve => {
    console.log(3);
    resolve();
  })
  .then(() => console.log(4))
  .then(() => console.log(5))
  .then(() => console.log(6))
})
.then(() => console.log(7))
.then(() => console.log(8))
// 1 2 3 4 5 6 7 8
```

## 22.

```js
new Promise(resolve => {
  resolve()
}).then(() => {
  return new Promise(r => {
    console.log('promise');
    r(5)
  })
}).then(r => {
  console.log(r)
})

new Promise(resolve => {
  resolve(2);
}).then(() => {
  console.log('1');
}).then(() => {
  console.log('2');
}).then(() => {
  console.log('3');
}).then(() => {
  console.log('4');
})

// promise 1 2 3 5 4
```

## 23.

```js
new Promise(resolve => {
  resolve()
}).then(() => {
  return new Promise(r => {
    console.log('1-1');
    r()
  }).then(() => {
    console.log('1-1 p1')
  })
}).then(() => {
  console.log('1-2')
})

new Promise(resolve => {
  resolve(2);
}).then(() => {
  console.log('2-1');
}).then(() => {
  console.log('2-2');
}).then(() => {
  console.log('2-3');
})
```

## 24. 

**外部的第二个 then 的注册，需要等待 外部的第一个 then 的同步代码执行完成。**  当执行内部的 new Promise 的时候，然后碰到 resolve，resolve 执行完成，代表此时的该 Promise 状态已经扭转，之后开始内部的第一个 .then 的微任务的注册，此时同步执行完成。

```js
new Promise((resolve, reject) => {
  console.log("外部promise");
  resolve();
})
  .then(() => {
    console.log("外部第一个then");
    new Promise((resolve, reject) => {
      console.log("内部promise");
      resolve();
    })
      .then(() => {
        console.log("内部第一个then");
      })
      .then(() => {
        console.log("内部第二个then");
      });
  })
  .then(() => {
    console.log("外部第二个then");
  });
```

## 25. 

```js
new Promise((resolve, reject) => {
  console.log("外部promise");
  resolve();
})
  .then(() => {
    console.log("外部第一个then");
  // new Promise(executor) 中的 executor 会在 Promise 创建时同步执行，它不是函数声明，而是被 Promise 构造函数立即调用的执行器函数。真正异步的是 .then 注册的回调。
    let p = new Promise((resolve, reject) => {
      console.log("内部promise");
      resolve();
    })
    p.then(() => {
        console.log("内部第一个then");
      })
    p.then(() => {
        console.log("内部第二个then");
      });
  })
  .then(() => {
    console.log("外部第二个then");
  });
```

## 26.

因为 **O2 的注册条件不是“有没有 Promise resolve”，而是“当前 then 是否执行完并返回了一个值”**。

JavaScript 中，变量声明 / 赋值 / 方法调用本身都是同步执行的；

变量定义的方式，注册都是同步的 比如这里的 p.then 和 var p = new Promise 都是同步执行的。

```js
new Promise((resolve, reject) => {
  console.log(1);      // S1
  resolve();
})
.then(() => {                      // O1
  console.log(2);   // M1

  let p = new Promise((resolve, reject) => {
    console.log(3);    // S2
    resolve();
  });

  p.then(() => {                   // I1
    console.log(4);
  });

  p.then(() => {                   // I2
    console.log(5);
  });
})
.then(() => {                      // O2
  console.log(6);
});

// 1 2 3 4 5 6
```

## 27.

```js
new Promise((resolve, reject) => {
  console.log(1);
  resolve();
})
  .then(() => {
    console.log(2);
    new Promise((resolve, reject) => {
      console.log(3);
      resolve();
    })
      .then(() => {
        console.log(4);
      })
      .then(() => {
        console.log(5);
      });
    return new Promise((resolve, reject) => {
      console.log(6);
      resolve();
    })
      .then(() => {
        console.log(7);
      })
      .then(() => {
        console.log(8);
      });
  })
  .then(() => {
    console.log(9);
  });

// 1 2 3 6 4 7 5 8 9
```

## 28.

如果有多个`fulfilled`的`Promise`实例，同时执行`then`链式调用，`then`会交替执行。

这是编译器的优化，防止一个 `Promise`占据过多时间。

在`then`中返回`Promise`实例，会出现 `慢两拍`的效果，具体表现为等待两个`.then()`执行完成。

- 第一拍：`Promise`需要等待`pending`变为`fulfilled`状态
- 第二拍：`then`函数挂载到`MicroTaskQueue`中

```js
// then 中无 返回 Promise 的情况
Promise.resolve().then(() => {
    console.log(0);     // 第1步
}).then(() => {
    console.log(2);     // 第3步
}).then(() => {
    console.log(4);     // 第5步
}).then(() => {
    console.log(6);     // 第7步
})

Promise.resolve().then(() => {
    console.log(1);     // 第2步
}).then(() => {
    console.log(3);     // 第4步
}).then(() => {
    console.log(5);     // 第6步
}).then(() => {
    console.log(7);     // 第8步
})

// 输出
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
```

```js
Promise.resolve().then(() => {
    console.log(0);     // 第1步

    // 等待两个 then 执行完成
    return Promise.resolve(4)
}).then((res) => {
    console.log(res);     // 第5步
}).then(() => {
    console.log(6);     // 第7步
}).then(() => {
    console.log(7);     // 第8步
})

Promise.resolve().then(() => {
    console.log(1);     // 第2步
}).then(() => {
    console.log(2);     // 第3步
}).then(() => {
    console.log(3);     // 第4步
}).then(() => {
    console.log(5);     // 第6步
})

// 输出
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
```



## 其他资料

1. [深度揭秘 Promise 微任务注册和执行过程](https://juejin.cn/post/6844903987183894535)
2. [为什么慢两拍：关于promise规范thenable的白话解释](https://juejin.cn/post/7018765637870698503)
3. [一道面试题：还在纠结async/ await、Promise的执行顺序？](https://juejin.cn/post/6871898249578921992)

题目：

1. [要就来45道Promise面试题一次爽到底](https://juejin.cn/post/6844904077537574919#heading-34)

2. [async, await, promise 面试题](https://www.learnnote.site/frontend/async-await-promise)

   
