该笔记为观看**尚硅谷Web前端Promise教程从入门到精通（2021抢先版）**与**尚硅谷Promise教程(promise前端进阶必学)**两个课程视频以及参考其课件;预备知识链: ajax -- promise -- axios


# 一、Promise的理解与使用

1、概念:

Promise是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。通俗讲，Promise是一个许诺、承诺，是对未来事情的承诺，承诺不一定能完成，但是无论是否能完成都会有一个结果。

* Pending：正在做
* Resolved：完成这个承诺
* Rejected：这个承诺没有完成，失败了

Promise 用来预定一个不一定能完成的任务，要么成功，要么失败。在具体的程序中具体的体现，通常用来封装一个异步任务，提供承诺结果。Promise 是异步编程的一种解决方案，**主要用来解决回调地狱的问题，可以有效的减少回调嵌套。**真正解决需要配合async/await。

2、特点:

- 对象的状态不受外界影响。

  Promise对象代表一个异步操作，有三种状态：Pending（进行中）、Resolved（已完成，又称Fulfilled）和Rejected（已失败）。

- 只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态。

- 一旦状态改变，就不会再变。

  任何时候都可以得到这个结果。Promise对象的状态改变，只有两种可能：从Pending变为Resolved和从Pending变为Rejected。只要这两种情况发生，状态就凝固了，不会再变了，会一直保持这个结果。就算改变已经发生了，你再对Promise对象添加回调函数，也会立即得到这个结果。

3、缺点:

- 无法取消Promise，一旦新建它就会立即执行，无法中途取消。和一般的对象不一样，无需调用。
- 如果不设置回调函数，Promise内部抛出的错误，不会反应到外部。
- 当处于Pending状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）

## 1、Promise是什么?

### a、概念

1. 抽象表达:  Promise 是一门新的技术(ES6 规范)，Promise 是 JS 中进行异步编程的新解决方案 (备注：旧方案是单纯使用回调函数)

2. 具体表达: 

- 从语法上来说: Promise 是一个`构造函数`
- 从功能上来说: promise 对象用来封装一个异步操作并可以获取其成功/ 失败的结果值

### b、promise 的状态

####  a) promise 的状态

实例对象中的一个属性 [[PromiseState]]

* pending  未决定的
* resolved / fullfilled  成功
* rejected  失败

####  b) promise 的状态改变

1. pending 变为 resolved 

2. pending 变为 rejected

说明: **只有这 2 种**, 且一个 promise 对象**只能改变一次**无论变为成功还是失败, 都会有一个结果数据成功的结果数据一般称为 value, 失败的结果数据一般称为 reason。

### c、promise的基本流程

![image-20230325202628753](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/promise/image-20230325202628753.png)

### d、promise的基本使用

#### 1. 使用 promise 封装基于定时器的异步

```js
function doDelay(time) {
  // 1. 创建 promise 对象(pending 状态), 指定执行器函数
  return new Promise((resolve, reject) => {
    // 2. 在执行器函数中启动异步任务
    console.log("启动异步任务");
    setTimeout(() => {
      console.log("延迟任务开始执行...");
      const time = Date.now(); // 假设: 时间为奇数代表成功, 为偶数代表失败
      if (time % 2 === 1) {
        // 成功了
        // 3. 1. 如果成功了, 调用 resolve()并传入成功的 value
        resolve("成功的数据 " + time);
      } else {
        // 失败了
        // 3.2. 如果失败了, 调用 reject()并传入失败的 reason
        reject("失败的数据 " + time);
      }
    }, time);
  });
}
const promise = doDelay(2000);
promise.then(
  // promise 指定成功或失败的回调函数来获取成功的 vlaue 或失败的 reason
  (value) => {
    // 成功的回调函数 onResolved, 得到成功的 vlaue
    console.log("成功的 value: ", value);
  },
  (reason) => {
    // 失败的回调函数 onRejected, 得到失败的 reason
    console.log("失败的 reason: ", reason);
  }
);

```

#### 2. 使用 promise 封装 ajax 异步请求

```js
/**
 * 封装一个函数 sendAJAX 发送 GET AJAX 请求
 * 参数   URL
 * 返回结果 Promise 对象
 */
function sendAJAX(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("GET", url);
    xhr.send();
    //处理结果
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        //判断成功
        if (xhr.status >= 200 && xhr.status < 300) {
          //成功的结果
          resolve(xhr.response);
        } else {
          reject(xhr.status);
        }
      }
    };
  });
}

sendAJAX("https://api.apiopen.top/getJok").then(
  (value) => {
    console.log(value);
  },
  (reason) => {
    console.warn(reason);
  }
);

```

#### 3. fs模块使用Promise

```js
function mineReadFile(path) {
  return new Promise((resolve, reject) => {
    //读取文件
    require("fs").readFile(path, (err, data) => {
      //判断
      if (err) reject(err);
      //成功
      resolve(data);
    });
  });
}

mineReadFile("./resource/content.txt").then(
  (value) => {
    //输出文件内容
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);

```

#### 4. 异常穿透

可以在每个then()的第二个回调函数中进行err处理,也可以利用异常穿透特性,到最后用`catch`去承接统一处理,两者一起用时，前者会生效(因为err已经将其处理,就不会再往下穿透)而走不到后面的catch。在每个.then()中我可以将数据再次传出给下一个then()

```js
let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    // resolve("OK");
    reject("Err");
  }, 1000);
});

p.then((value) => {
  // console.log(111);
  throw "失败啦!";
})
  .then((value) => {
    // console.log(222);
    reject("error"); // 不会输出
  })
  .then((value) => {
    console.log(333);
  })
  .catch((reason) => {
    console.warn(444, reason); // 只会输出第一个错误
  });

```

#### 5.`util.promisify方法`

可以将函数直接变成promise的封装方式,不用再去手动封装

```js
/**
 * util.promisify 方法
 * Takes a function following the common error-first callback style, i.e. taking a (err, value) => ... callback as the last argument, and returns a version that returns promises.
 */
//引入 util 模块
const util = require("util");
//引入 fs 模块
const fs = require("fs");
//返回一个新的函数
let mineReadFile = util.promisify(fs.readFile);

mineReadFile("./resource/content.txt").then((value) => {
  console.log(value.toString());
});

```

## 2、为什么要用Promise?

### a、指定回调函数的方式更加灵活

1. 旧的: 必须在启动异步任务前指定 
2. promise: 启动异步任务 = 返回promie对象 = 给promise对象绑定回调函数(甚至可以在异步任务结束后指定/多个)

### b、支持链式调用, 可以解决回调地狱问题

#####  1、什么是回调地狱

回调函数嵌套调用, 外部回调函数异步执行的结果是嵌套的回调执行的条件

```js
// 地狱回调
asyncFunc1(opt, (...args1) => {
  asyncFunc2(opt, (...args2) => {
    asyncFunc3(opt, (...args3) => {
      asyncFunc4(opt, (...args4) => {
        // some operation
      });
    });
  });
});
```

#####  2、回调地狱的缺点?

不便于阅读 不便于异常处理

#####  3、解决方案?

promise链式调用,用来解决回调地狱问题，但是只是简单的改变格式，并没有彻底解决上面的问题真正要解决上述问题，一定要利用promise再加上await和async关键字实现异步传同步。

#####  4、终极解决方案?

 promise + async/await

------

## 3、Promise中的常用 API 概述

 此处列举几个最常用的API的概述,如果想看详细描述的可以继续往下看下方的Promise方法的具体使用描述

####   a、Promise 构造函数: new Promise(executor)

- executor 函数: 执行器 (resolve, reject) = {}

- resolve 函数: 内部定义成功时我们调用的函数 value = {} 

- reject 函数: 内部定义失败时我们调用的函数 reason = {} 

```js
const myFirstPromise = new Promise((resolve, reject) => {
  // do something asynchronous which eventually calls either:
  //
  //   resolve(someValue)        // fulfilled
  // or
  //   reject("failure reason")  // rejected
});
```

说明: executor 会在 Promise ==内部立即**同步调用**==,异步操作在执行器中执行,换话说Promise支持同步也支持异步操作

####   b、Promise.prototype.then: (onResolved, onRejected) = {}

(1) onResolved 函数: 成功的回调函数 (value) = {} 

(2) onRejected 函数: 失败的回调函数 (reason) = {} 

说明: 指定用于得到成功 value 的成功回调和用于得到失败 reason 的失败回调 返回一个新的 promise 对象

then()是异步函数，属于微任务。

```js
const p1 = new Promise((resolve, reject) => {
  resolve("Success!");
  // or
  // reject(new Error("Error!"));
});

p1.then(
  (value) => {
    console.log(value); // Success!
  },
  (reason) => {
    console.error(reason); // Error!
  }
);

```

####    c、Promise.prototype.catch: (onRejected) = {}

- onRejected 函数: 失败的回调函数 (reason) = {}

说明: then()的语法糖, 相当于: then(undefined, onRejected)

- 异常穿透使用:当运行到最后,没被处理的所有异常错误都会进入这个方法的回调函数中   

```js
const promise1 = new Promise((resolve, reject) => {
  throw "Uh-oh!";
});

promise1.catch((error) => {
  console.error(error);
});
// expected output: Uh-oh!

```

####   d、Promise.resolve: (value) = {}

value: 成功的数据或 promise 对象 

说明: 返回一个成功/失败的 promise 对象,直接改变promise状态

```js
const promise1 = Promise.resolve(123);

promise1.then((value) => {
  console.log(value);
  // expected output: 123
});

```

####   e、Promise.reject: (reason) = {}

reason: 失败的原因 

说明: 返回一个失败的 promise 对象,直接改变promise状态。

```js
function resolved(result) {
  console.log("Resolved");
}

function rejected(result) {
  console.error(result);
}

Promise.reject(new Error("fail")).then(resolved, rejected);
// expected output: Error: fail

```

#### f、Promise.all: (promises) = {}

promises: 包含 n 个 promise 的数组 

说明: 返回一个新的 promise, 只有所有的 promise都成功才成功, 只要有一个失败了就直接失败。

```js
let p1 = new Promise((resolve, reject) = { resolve('成功');  })
let p2 = Promise.reject('错误错误错误');
let p3 = Promise.resolve('也是成功')
const result = Promise.all([p1, p2, p3]);
console.log(result);
```

#### g、Promise.race: (promises) = {}

promises: 包含 n 个 promise 的数组 

说明: 返回一个新的 promise, 第一个完成的 promise 的结果状态就是最终的结果状态。

如p1延时,开启了异步,内部正常是同步进行,所以p2p3p1,结果是P2

```js
let p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("OK");
  }, 1000);
});
let p2 = Promise.resolve("Success");
let p3 = Promise.resolve("Oh Yeah");
//调用
const result = Promise.race([p1, p2, p3]);
console.log(result);

```

## 4、Promise的几个关键问题

#### a、如何改变 promise 的状态?

- resolve(value): 如果当前是 pending 就会变为 resolved 

- reject(reason): 如果当前是 pending 就会变为 rejected 

- 抛出异常: 如果当前是 pending 就会变为 rejected

#### b、一个 promise 指定多个成功/失败回调函数, 都会调用吗?

当 promise**改变为对应状态时**都会调用,改变状态后,多个回调函数都会调用,并不会自动停止。

```js
let p = new Promise((resolve, reject) => {
  resolve("OK");
});
//指定回调 - 1
p.then((value) => {
  console.log(value); // 'ok'
});
//指定回调 - 2
p.then((value) => {
  alert(value); // "ok"
});

```

#### c、改变 promise 状态和指定回调函数谁先谁后?

1. 都有可能, 正常情况下是先指定回调再改变状态, 但也可以先改状态再指定回调 
   - 先指定回调再改变状态(**异步**): 先指定回调 -> 再改变状态 -> 改变状态后才进入异步队列执行回调函数
   - 先改状态再指定回调(**同步**): 改变状态 -> 指定回调并马上执行回调

2. 如何先改状态再指定回调? ==注意:指定并不是执行==
   - 在执行器中直接调用 resolve()/reject()，即不使用定时器等方法,执行器内直接同步操作 
   - 延迟更长时间才调用 then()，即在`.then()`这个方法外再包一层例如延时器这种方法

3. 什么时候才能得到数据? 
   - 如果先指定的回调, 那当状态发生改变时, 回调函数就会调用, 得到数据 
   - 如果先改变的状态, 那当指定回调时, 回调函数就会调用, 得到数据

当我们创建一个 Promise 实例时，我们通常会指定一个异步操作，并在操作完成后改变 Promise 的状态。

```js
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Operation completed successfully!"); // 改变 Promise 状态为 fulfilled
  }, 1000);
});

myPromise.then((result) => {
  console.log(result); // 在 Promise 状态变为 fulfilled 后执行回调函数
});
```

在上面的例子中，我们创建了一个 Promise 实例并指定了一个异步操作（在这里是一个定时器）。当定时器完成时，我们调用 resolve 方法并传递一个成功的消息，这会将 Promise 的状态从 pending 改变为 fulfilled。然后，我们调用 then 方法并指定一个回调函数，当 Promise 状态变为 fulfilled 后，这个回调函数将被执行并输出 "Operation completed successfully!"。

如果我们先指定回调函数，再改变 Promise 的状态，回调函数将在状态改变后立即被执行，如下所示：

```js
const myPromise = new Promise((resolve, reject) => {
  // ...
});

myPromise.then((result) => {
  console.log(result); // 在 Promise 状态变为 fulfilled 后执行回调函数
});

setTimeout(() => {
  myPromise.resolve("Operation completed successfully!"); // 改变 Promise 状态为 fulfilled
}, 1000);
```

在上面的例子中，我们先调用 then 方法并指定一个回调函数，在这个回调函数中我们输出一个消息。然后，我们通过 setTimeout 方法在 1 秒钟后调用 resolve 方法来改变 Promise 的状态。由于 Promise 的状态在 1 秒钟后被改变，因此回调函数会在这个时候立即被执行，并输出 "Operation completed successfully!"。

```js
let p = new Promise((resolve, reject) => {
  //异步写法,这样写会先指定回调,再改变状态
  setTimeout(() => {
    resolve("OK");
  }, 1000);
  //这是同步写法,这样写会先改变状态,再指定回调
  // resolve("OK");
});
p.then(
  (value) => {
    console.log(value);
  },
  (reason) => {}
);

```

4. 个人理解

源码中,promise的状态是通过一个`默认为pendding`的变量进行判断,所以当你`resolve/reject`延时(异步导致当then加载时,状态还未修改)后,这时直接进行p.then()会发现,目前状态还是`进行中`,所以只是这样导致只有同步操作才能成功。

所以promise将传入的`回调函数`拷贝到promise对象实例上,然后在`resolve/reject`的执行过程中再进行调用，达到异步的目的。

#### d、promise.then()返回的新 promise 的结果状态由什么决定?

1. 简单表达: 由then()指定的回调函数执行的结果决定 

2. 详细表达: 
   1. 如果抛出异常, 新 promise 变为 rejected, reason 为抛出的异常 
   2. 如果返回的是非 promise 的任意值, 新 promise 变为 resolved, value 为返回的值 
   3. 如果返回的是另一个新 promise, 此 promise 的结果就会成为新 promise 的结果

```js
let p = new Promise((resolve, reject) => {
  resolve("ok");
});
//执行 then 方法
let result = p.then(
  (value) => {
    console.log(value);
    // 1. 抛出错误 ,变为 rejected
    throw "出了问题";
    // 2. 返回结果是非 Promise 类型的对象,新 promise 变为 resolved
    return 521;
    // 3. 返回结果是 Promise 对象,此 promise 的结果就会成为新 promise 的结果
    return new Promise((resolve, reject) => {
      // resolve('success');
      reject("error");
    });
  },
  (reason) => {
    console.warn(reason);
  }
);

```

#### e、promise 如何串连多个操作任务?

1. promise 的 then()返回一个新的 promise, 可以开成 then()的链式调用 

2. 通过 then 的链式调用串连多个同步/异步任务,这样就能用`then()`将多个同步或异步操作串联成一个同步队列

```js
let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("OK");
  }, 1000);
});

p.then((value) => {
  return new Promise((resolve, reject) => {
    resolve("success");
  });
})
  .then((value) => {
    console.log(value);
  })
  .then((value) => {
    console.log(value);
  });

```

#### f、promise 异常传透?


* 当使用 promise 的 then 链式调用时, 可以在最后指定失败的回调
* 前面任何操作出了异常, 都会传到最后失败的回调中处理

```javascript
let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    // resolve("OK");
    reject("Err");
  }, 1000);
});

p.then((value) => {
  // console.log(111);
  throw "失败啦!";
})
  .then((value) => {
    // console.log(222);
    reject("error"); // 不会输出
  })
  .then((value) => {
    console.log(333);
  })
  .catch((reason) => {
    console.warn(444, reason); // 只会输出第一个错误
  });

```

注:可以在每个then()的第二个回调函数中进行err处理,也可以利用异常穿透特性,到最后用`catch`去承接统一处理,两者一起用时,前者会生效(因为err已经将其处理,就不会再往下穿透)而走不到后面的catch。

#### g、中断 promise 链?

在关键问题2中,可以得知,当promise状态改变时,他的链式调用都会生效,那如果我们有这个一个实际需求:我们有5个then(),但其中有条件判断,如当我符合或者不符合第三个then条件时,要直接中断链式调用,不再走下面的then,该如何?

1. 当使用 promise 的 then 链式调用时, 在中间中断, 不再调用后面的回调函数 
2. 办法: 在回调函数中返回一个 `pendding` 状态的`promise 对象`

```js
let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("OK");
  }, 1000);
});
p.then((value) => {
  return new Promise(() => {});
}) //有且只有这一个方式
  .then((value) => {
    console.log(222);
  })
  .then((value) => {
    console.log(333);
  })
  .catch((reason) => {
    console.warn(reason);
  });

```

## 5、 Promise的实际应用

### a、加载图片

我们可以将图片的加载写成一个`Promise`，一旦加载完成，`Promise`的状态就发生变化。

```javascript
const preloadImage = function (path) {
  return new Promise(function (resolve, reject) {
    const image = new Image();
    image.onload = resolve;
    image.onerror = reject;
    image.src = path;
  });
};

```


### b、Generator 函数与 Promise 的结合

使用 Generator 函数管理流程，遇到异步操作的时候，通常返回一个`Promise`对象。

```javascript
function getFoo() {
  return new Promise(function (resolve, reject) {
    resolve("foo");
  });
}

const g = function* () {
  try {
    const foo = yield getFoo();
    console.log(foo);
  } catch (e) {
    console.log(e);
  }
};

function run(generator) {
  const it = generator();

  function go(result) {
    if (result.done) return result.value;

    return result.value.then(
      function (value) {
        return go(it.next(value));
      },
      function (error) {
        return go(it.throw(error));
      }
    );
  }

  go(it.next());
}

run(g);

```

上面代码的 Generator 函数`g`之中，有一个异步操作`getFoo`，它返回的就是一个`Promise`对象。函数`run`用来处理这个`Promise`对象，并调用下一个`next`方法。

# 二、Promise API 用法详解

ES6 规定，`Promise`对象是一个构造函数，用来生成`Promise`实例。

此部分是对于 **Promise API 用法的详解** ,尽量详细地列举其常见用法,所以篇幅较长

## a、基本用法

### 1. 举个创造 Promise 实例的栗子

 下面代码创造了一个`Promise`实例。

 ```javascript
 const promise = new Promise((resolve, reject) => {
   if (/* 异步操作成功 */) {
     resolve(value);
   } else {
     //将该 Promise 修改为成功且返回
     reject(error);
   } //将该 Promise 修改为失败且返回
 });
 ```

 `Promise`构造函数接受一个函数作为参数，该函数的两个参数分别是`resolve`和`reject`。它们是两个函数，由 JavaScript 引擎提供，不用自己部署。

 `resolve`函数的作用是，将`Promise`对象的状态从“未完成”变为“成功”（即从 pending 变为 resolved），在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；`reject`函数的作用是，将`Promise`对象的状态从“未完成”变为“失败”（即从 pending 变为 rejected），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。

### 2. 使用then方法分别指定 成功/失败 的回调

`Promise`实例生成以后，可以用then()方法分别指定`resolved`状态和`rejected`状态的回调函数。

```javascript
promise.then(
  function (value) {
    // 当promise状态返回为resolve 时会执行的回调函数
  },
  function (error) {
    // 当promise状态返回为rejected 时会执行的回调函数
  }
);

```

then方法可以接受两个回调函数作为参数。第一个回调函数是`Promise`对象的状态变为`resolved`时调用，第二个回调函数是`Promise`对象的状态变为`rejected`时调用。其中，**第二个函数是可选的，不一定要提供**。这两个函数都接受`Promise`对象传出的值作为参数。

### 3. 举个 Promise 对象的简单栗子

下面是一个`Promise`对象的简单例子。

 setTimeout的第三个参数是给第一个函数的参数，而且是先于第一个参数(即回调函数)执行的 

```javascript
function timeout(ms) {
  //声明一个方法, 传入的 参数ms 为延时器时间
  return new Promise((resolve, reject) => {
    //这行代码实际效果: 当 [ms] 毫秒后 执行 resolve('test')
    setTimeout(() => resolve("test"), ms);
  });
}

timeout(100).then((value) => {
  console.log(value);
});
//打印结果 : test

```

上面代码中，`timeout`方法返回一个`Promise`实例，表示一段时间以后才会发生的结果。过了指定的时间（`ms`参数）以后，`Promise`实例的状态变为`resolved`，就会触发`then`方法绑定的回调函数。

### 4. Promise 新建后就会立即执行

```javascript
let promise = new Promise((resolve, reject) => {
  console.log("Promise");
  resolve();
});

promise.then(() => {
  console.log("resolved.");
});

console.log("Hi!");

// Promise
// Hi!
// resolved

```

上面代码中，Promise 新建后立即执行，所以首先输出的是`Promise`。然后，`then`方法指定的回调函数，将在当前脚本所有同步任务执行完才会执行，所以`resolved`最后输出。

实际上,这个运行结果相关知识点是 [ [宏任务与微任务](https://gitee.com/hongjilin/hongs-study-notes/tree/master/%E7%BC%96%E7%A8%8B_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/Promise%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%9B%9B%E5%AE%8F%E4%BB%BB%E5%8A%A1%E4%B8%8E%E5%BE%AE%E4%BB%BB%E5%8A%A1) ] ,单独梳理在下方.这里可以先初步理解为: 

1. JS是单线程的,至上往下运行,在声明 **Promise** 时实际上已经执行到了内部方法

2. 为何 resolve() 运行后没有立即打印?

 - JS中用来存储待执行回调函数的队列包含2个不同特定的列队

    `宏队列`:用来保存待执行的宏任务(回调),比如:`定时器`回调/ajax回调/dom事件回调
   
    `微队列`:用来保存待执行的微任务(回调),比如:`Promise`的回调/muntation回调

 - JS执行时会区别这2个队列:

   JS执行引擎首先必须执行所有的`初始化同步任务`代码
   
   每次准备取出第一个`宏任务执行前`,都要将所有的`微任务`一个一个取出来执行

### 5. 举个异步加载图片的栗子

```javascript
function loadImageAsync(url) {
  return new Promise((resolve, reject) => {
    const image = new Image();

    image.onload = function () {
      console.log("图片加载成功");
      resolve(image);
    };

    image.onerror = function () {
      reject(new Error(`无法从 ${url} 中加载图片`));
    };
    image.src = url;
  });
}
loadImageAsync("正确的url"); //打印图片加载成功
loadImageAsync("错误的url"); //抛出异常

```

上面代码中，使用`Promise`包装了一个图片加载的异步操作。如果加载成功，就调用`resolve`方法，否则就调用`reject`方法。

### 6. 举个用`Promise`对象实现的 Ajax 操作的栗子

```javascript
const getJSON = function (url) {
  const promise = new Promise(function (resolve, reject) {
    const handler = function () {
      if (this.readyState !== 4) return; //当readyState 为4 时直接返回,不修改 promise 状态
      if (this.status === 200) resolve(this.response);
      //返回状态为 200 时将状态修改为成功,且将响应内容返回
      else reject(new Error(this.statusText)); //失败时抛出异常
    };
    const client = new XMLHttpRequest(); //实例化xml实例
    client.open("GET", url); //下面这几行都是对xml实例进行配置,不懂的同学要去补一下ajax知识点
    client.onreadystatechange = handler;
    client.responseType = "json";
    client.setRequestHeader("Accept", "application/json");
    client.send();
  });
  return promise;
};

getJSON("./hong.json").then(
  function (json) {
    console.log("Contents: ", json);
  },
  function (error) {
    console.error("出错了", error);
  }
);

```

上面代码中，`getJSON`是对 XMLHttpRequest 对象的封装，用于发出一个针对 JSON 数据的 HTTP 请求，并且返回一个`Promise`对象。需要注意的是，在`getJSON`内部，`resolve`函数和`reject`函数调用时，都带有参数。

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7z2oliql2j31ji0n6qj7.jpg)

### 7. resolve()  的参数可以是另一个 Promise 实例

如果调用`resolve`函数和`reject`函数时带有参数，那么它们的参数会被传递给回调函数。`reject`函数的参数通常是`Error`对象的实例，表示抛出的错误；`resolve`函数的参数除了正常的值以外，还可能是另一个 Promise 实例，比如像下面这样。

```javascript
const p1 = new Promise((resolve, reject) => {
  resolve("test");
});

const p2 = new Promise((resolve, reject) => {
  resolve(p1);
});

p2.then((value) => {
  console.log(11, value);
});
```

上面代码中，`p1`和`p2`都是 Promise 的实例，但是`p2`的`resolve`方法将`p1`作为参数，即一个异步操作的结果是返回另一个异步操作。

注意，这时`p1`的状态就会传递给`p2`，也就是说，`p1`的状态决定了`p2`的状态。如果`p1`的状态是`pending`，那么`p2`的回调函数就会等待`p1`的状态改变；如果`p1`的状态已经是`resolved`或者`rejected`，那么`p2`的回调函数将会立刻执行。

```javascript
const p1 = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("p1的状态改为错误")), 0);
});

const p2 = new Promise((resolve, reject) => {
  setTimeout(() => resolve(p1), 3000); //将p1传给p2.
});

p2.then(
  (value) => console.log(11, value),
  (result) => console.log(22, "失败")
).catch((error) => console.log(33, "catch异常捕获:" + error));

```

上面代码运行后执行效果:

* 首先马上会打印一个报错 : "Uncaught (in promise) Error: p1的状态改为错误" (红色报错)
* 然后等3秒后再打印:  '失败'
* 注意: 如果 **p2.then()** 中没有写 **reject** 回调函数(第二个参数),则会被 **catch** 捕获,变为`catch异常捕获:Error: p1的状态改为错误`

解释:

* 首先前面说过,promise定义时就会立即执行,所以刚开始就运行了 **p1 的reject()**,所以直接控制台报错了
* `resolve`方法返回的是`p1`。由于`p2`返回的是另一个 Promise，导致`p2`自己的状态无效了，由`p1`的状态决定`p2`的状态
* 总结来说,promise返回promise这种嵌套形式,将由最内层的promise决定外层的状态

### 8. 调用`resolve`或`reject`并不会终结 Promise 的参数函数的执行

调用`resolve`或`reject`并不会终结 Promise 的参数函数的执行。

```javascript
new Promise((resolve, reject) => {
  resolve(1);
  console.log(2);
}).then((r) => {
  console.log(r);
});
// 2
// 1

```

上面代码中，调用`resolve(1)`以后，后面的`console.log(2)`还是会执行，并且会首先打印出来。这是因为立即 resolved 的 Promise 是在本轮事件循环的末尾执行，总是晚于本轮循环的同步任务。

### 9. 建议在修改状态函数前加return 

一般来说，调用`resolve`或`reject`以后，Promise 的使命就完成了，后继操作应该放到`then`方法里面，而不应该直接写在`resolve`或`reject`的后面。所以，最好在它们前面加上`return`语句，这样就不会有意外。

```javascript
new Promise((resolve, reject) => {
  return resolve(1);
  // 后面的语句不会执行
  console.log(2);
});

```

有同学可能就会问了,不加感觉也没啥事啊,反正我在这个函数体内就是要做这些操作,放在 `resolve/reject`前后好像都不影响啊! 这里我给举个实际场景

#### a. 不加 return 导致的错误场景

一般来说,错误发生在 Promise 内,是不会传到外部的,只会在 Promise 内部消化,详见下方API详解部分的 [②Promise.prototype.catch()](#② Promise.prototype.catch())

```javascript
const promise = new Promise((resolve, reject) => {
  resolve("ok"); //如果你加了 return , 函数执行到此步就停止了
  setTimeout(() => {
    throw new Error("错误错误!!!!!");
  }, 0);
});
promise.then((value) => {
  console.log(value);
});
// ok
// Uncaught Error: 错误错误!!!!

```

上面代码中，Promise 指定在下一轮“事件循环”再抛出错误。到了那个时候，Promise 的运行已经结束了，所以这个错误是在 Promise 函数体外抛出的，会冒泡到最外层，成了未捕获的错误。

## b、API 用法详解

此处将对于所有API进行详细剖析,参照资料为 [阮一峰的ES6日志]()

### ① Promise.prototype.then()

Promise 实例具有`then`方法，也就是说，`then`方法是定义在原型对象`Promise.prototype`上的。它的作用是为 Promise 实例添加状态改变时的回调函数。前面说过，`then`方法的第一个参数是`resolved`状态的回调函数，第二个参数（可选）是`rejected`状态的回调函数。

#### a) `then`方法返回的是一个新的`Promise`实例

`then`方法返回的是一个新的`Promise`实例（注意，不是原来那个`Promise`实例）。因此可以采用链式写法，即`then`方法后面再调用另一个`then`方法。

```javascript
getJSON("./hong.json")
  .then(function (json) {
    return json.name;
  })
  .then(function (name) {
    console.log(`My name is ${name}`);
  });

```

上面的代码使用`then`方法，依次指定了两个回调函数。第一个回调函数完成以后，会将返回结果作为参数，传入第二个回调函数。

#### b) 采用链式的`then`, 会等待前一个Promise状态发生改变才会被调用

采用链式的`then`，可以指定一组按照次序调用的回调函数。这时，前一个回调函数，有可能返回的还是一个`Promise`对象（即有异步操作），这时后一个回调函数，就会等待该`Promise`对象的状态发生变化，才会被调用。

```javascript
getJSON("./hong.json")
  .then(function (json) {
    return getJSON(json.name);
  })
  .then(
    function (name) {
      console.log("resolved: My name is ", name);
    },
    function (err) {
      console.log("rejected: ", err);
    }
  );

```

上面代码中，第一个`then`方法指定的回调函数，返回的是另一个`Promise`对象。这时，第二个`then`方法指定的回调函数，就会等待这个新的`Promise`对象状态发生变化。如果变为`resolved`，就调用第一个回调函数，如果状态变为`rejected`，就调用第二个回调函数。

#### c) 使用箭头函数简写

如果采用箭头函数，上面的代码可以写得更简洁 (实际代码中基本都是这样写了)

```js
getJSON("./hong.json")
  .then((json) => getJSON(json.name))
  .then(
    (name) => console.log("resolved: My name is ", name),
    (err) => console.log("rejected: ", err)
  );

```

### ② Promise.prototype.catch()

`Promise.prototype.catch()`方法是`.then(null, rejection)`或`.then(undefined, rejection)`的别名，用于指定发生错误时的回调函数。

#### a) 基本用法

```javascript
getJSON("./hong.json")
  .then(function (posts) {})
  .catch(function (error) {
    // 处理 getJSON 和 前一个回调函数运行时发生的错误
    console.log("发生错误！", error);
  });

```

上面代码中，`getJSON()`方法返回一个 Promise 对象

* 如果该对象状态变为`resolved`，则会调用`then()`方法指定的回调函数；
* 如果异步操作抛出错误，状态就会变为`rejected`，就会调用`catch()`方法指定的回调函数，处理这个错误
* 另外，`then()`方法指定的回调函数，如果运行中抛出错误，也会被`catch()`方法捕获。
* 被 catch 方法捕获的前提是前方的 then() 方法中没有对 `rejected` 进行捕获处理(即没有写reject回调函数)

```js
p.then((val) => console.log("指定成功回调:", val)).catch((err) =>
  console.log("在catch中进行 rejected 的处理", err)
);
// 等同于
p.then((val) => console.log("指定成功回调:", val)).then(null, (err) =>
  console.log("等同于另起一个then,只指定 rejected 的处理", err)
);

```

#### b)  `reject()`方法的作用，等同于抛出错误

```javascript
const promise = new Promise(function (resolve, reject) {
  throw new Error("直接抛出错误");
});
promise.catch(function (error) {
  console.log("异常捕获: ", error);
});
//异常捕获:  Error: 直接抛出错误

```

上面代码中，`promise`抛出一个错误，就被`catch()`方法指定的回调函数捕获。注意，上面的写法与下面两种写法是等价的。

```javascript
/******************  写法一 ***************************************/
const promise = new Promise(function (resolve, reject) {
  try {
    throw new Error(11, "直接抛出错误");
  } catch (e) {
    console.log(22, "进入catch,然后再用 reject(e)抛出. ");
    reject(e);
  }
});
promise.catch(function (error) {
  console.log(33, error);
});
// 22
// 33, 这里会把11打印出来
//进入catch,然后再用 reject(e)抛出
//Error: 直接抛出错误

/******************  写法二 ***************************************/
const promise1 = new Promise((resolve, reject) => {
  reject(new Error("使用 reject() 抛出错误"));
});
promise1.catch(function (error) {
  console.log(error);
});
//Error: 使用 reject() 抛出错误

```

比较上面两种写法，可以发现`reject()`方法的作用，等同于抛出错误,所以不必用try..catch()去承接后再去抛出了

#### c) 如果 Promise 状态已经被修改，再抛出错误是无效的

```javascript
const promise = new Promise((resolve, reject) => {
  resolve("成功了"); //换成 reject('成功了') 结果也是一样的
  throw new Error("成功后扔抛出异常");
});
promise
  .then((value) => {
    console.log(value);
  })
  .catch((error) => {
    console.log(error);
  });
// 成功了.

```

上面代码中，Promise 在`resolve/reject`语句后面，再抛出错误，不会被捕获，等于没有抛出。因为 Promise 的状态一旦改变，就永久保持该状态，不会再变了(前面有说过)

#### d) Promise 对象的错误具有 “冒泡” 性质

Promise 对象的错误具有“冒泡”性质，会一直向后传递，直到被捕获为止。也就是说，错误总是会被下一个`catch`语句捕获。

```javascript
getJSON("./hong.json") //第一个promise
  .then(function (post) {
    //第二个promise
    return getJSON(post.commentURL);
  })
  .then(function (comments) {
    //第三个promise
  })
  .catch(function (error) {
    // 处理前面三个Promise产生的错误
  });

```

上面代码中，一共有三个 Promise 对象(**then返回的仍可能是一个Promise对象**)：一个由`getJSON()`产生，两个由`then()`产生。它们之中任何一个抛出的错误，都会被最后一个`catch()`捕获。也是因为这个特性,有了 **异常穿透问题** 

#### e) 异常穿透问题

* 当使用 promise 的 then 链式调用时, 可以在最后指定失败的回调
* 前面任何操作出了异常, 都会传到最后失败的回调中处理

```javascript
getJSON("./hong.json")
  .then((posts) => {
    throw new Error("抛出异常");
  })
  .then(
    (res) => console.log(res),
    (e) => console.log("被then的错误回调捕获", e)
  )
  .catch((error) => {
    // 处理 getJSON 和 前一个回调函数运行时发生的错误
    console.log("错误捕获: ", error);
  });
//执行结果: 被then的错误回调捕获 Error: 抛出异常

/******************** 利用异常穿透 ****************************************/
getJSON("./hong.json")
  .then((posts) => {
    throw new Error("抛出异常");
  })
  .then((res) => console.log(res)) //此处差异,不指定 reject 回调,利用异常穿透传到最后
  .catch((error) => {
    console.log("错误捕获: ", error);
  });
//执行结果:  错误捕获:  Error: 抛出异常

```

注:可以在每个then()的第二个回调函数中进行err处理,也可以利用异常穿透特性,到最后用`catch`去承接统一处理,两者一起用时,前者会生效(因为err已经将其处理,就不会再往下穿透)而走不到后面的catch.

#### f) 建议使用 catch() 进行异常处理

一般来说，不要在`then()`方法里面定义 Reject 状态的回调函数（即`then`的第二个参数），总是使用`catch`方法。

```javascript
// bad
promise.then(
  (data) => console.log("成功", data),
  (err) => console.log("失败了", err)
);
// good 
promise
  .then((data) => console.log("成功", data)) //只指定成功回调
  .catch((err) => console.log("失败了", err));

```

上面代码中，第二种写法要好于第一种写法:

* 理由是第二种写法可以捕获前面`then`方法执行中的错误
* 也更接近同步的写法（`try/catch`）
* 因此, 建议总是使用`catch()`方法，而不使用`then()`方法的第二个参数。

#### g) 与传统 `try/catch` 代码块的差异

跟传统的`try/catch`代码块不同的是，如果没有使用`catch()`方法指定错误处理的回调函数，Promise 对象抛出的错误不会传递到外层代码，即不会有任何反应。

```javascript
const someAsyncThing = function () {
  return new Promise((resolve, reject) => {
    // 下面一行会报错，因为ok没有声明
    resolve(ok);
  });
};

//Promise 的 then() 处理,但不处理异常
someAsyncThing().then(() => {
  console.log("只指定成功回调,不处理异常错误");
});

setTimeout(() => {
  console.log("test");
}, 2000);
// Uncaught (in promise) ReferenceError: ok is not defined
// test

```

上面代码中，`someAsyncThing()`函数产生的 Promise 对象，内部有语法错误。

* 浏览器运行到这一行，会打印出错误提示`Uncaught (in promise) ReferenceError: ok is not defined`
* 但是不会退出进程、终止脚本执行, 2 秒之后还是会输出`test`。
* 这就是说，Promise 内部的错误不会影响到 Promise 外部的代码，通俗的说法就是“Promise 会吃掉错误”。

#### h) catch()方法后还能跟 then() 方法

一般总是建议，Promise 对象后面要跟`catch()`方法，这样可以处理 Promise 内部发生的错误。`catch()`方法返回的还是一个 Promise 对象，因此后面还可以接着调用`then()`方法。

```javascript
const someAsyncThing = function () {
  return new Promise(function (resolve, reject) {
    // 下面一行会报错，因为 ok 没有声明
    resolve(ok);
  });
};

someAsyncThing()
  .catch((error) => {
    console.log("捉到错误咯:", error);
  })
  .then(() => {
    console.log("错误捕获后我还要浪");
  });
//捉到错误咯: ReferenceError: ok is not defined
//错误捕获后我还要浪

```

上面代码运行完`catch()`方法指定的回调函数，会接着运行后面那个`then()`方法指定的回调函数。

如果没有报错，则会跳过`catch()`方法。

```js
Promise.resolve("硬是成功了")
  .catch((error) => {
    console.log("捉错误", error);
  })
  .then((v) => console.log("catch后面的then: ", v));
//catch后面的then:  硬是成功了

```

上面的代码因为没有报错，跳过了`catch()`方法，直接执行后面的`then()`方法。此时，要是`then()`方法里面报错，就与前面的`catch()`无关了。

#### i) `catch()`方法之中，还能再抛出错误

`catch()`方法之中，还能再抛出错误。

```javascript
const someAsyncThing = function () {
  return new Promise((resolve, reject) => {
    // 下面一行会报错，因为 hong 没有声明
    resolve(ok);
  });
};

someAsyncThing()
  .then(() => someOtherAsyncThing())
  .catch(function (error) {
    console.log("ctach:", error);
    // 下面一行会报错，因为 sum 没有声明
    sum++;
  })
  .then(() => {
    console.log("捕获后的then()");
  });

// ctach: [ReferenceError: ok is not defined]
// Uncaught (in promise) ReferenceError: sum is not defined

```

上面代码中，`catch()`方法抛出一个错误，因为后面没有别的`catch()`方法了，导致这个错误不会被捕获，也不会传递到外层。如果改写一下，结果就不一样了。

```javascript
someAsyncThing()
  .then(() => {
    return someOtherAsyncThing();
  })
  .catch((error) => {
    console.log("catch: ", error);
    // 下面一行会报错，因为 sum 没有声明
    sum++;
  })
  .catch((error) => {
    console.log("catch()后的catch: ", error);
  });
//catch:  ReferenceError: hong is not defined
//catch()后的catch:  ReferenceError: sum is not defined

```

上面代码中，第二个`catch()`方法用来捕获前一个`catch()`方法抛出的错误。

### ③ Promise.prototype.finally()

`finally()`方法用于指定不管 Promise 对象最后状态如何，都会执行的操作。该方法是 `ES2018` 引入标准的。

```javascript
promise
.then(result => {···})
.catch(error => {···})
.finally(() => {···});
```

上面代码中，不管`promise`最后的状态，在执行完`then`或`catch`指定的回调函数以后，都会执行`finally`方法指定的回调函数。

* `finally`方法的回调函数不接受任何参数，
* 这意味着没有办法知道，前面的 Promise 状态到底是`fulfilled`还是`rejected`。
* 这表明，`finally`方法里面的操作，应该是与状态无关的，不依赖于 Promise 的执行结果。

```js
function checkMail() {
  return new Promise((resolve, reject) => {
    if (Math.random() > 0.5) {
      resolve('Mail has arrived');
    } else {
      reject(new Error('Failed to arrive'));
    }
  });
}

checkMail()
  .then((mail) => {
    console.log(mail);
  })
  .catch((err) => {
    console.error(err);
  })
  .finally(() => {
    console.log('Experiment completed');
  });

```



#### a) `finally`本质上是`then`方法的特例

```javascript
promise.finally(() => {});

// 等同于
promise.then(
  (result) => result,
  (error) => throw error
);

```

上面代码中，如果不使用`finally`方法，同样的语句需要为成功和失败两种情况各写一次。有了`finally`方法，则只需要写一次。

#### b) 它的实现

它的实现也很简单。

```javascript
Promise.prototype.finally = function (callback) {
  let P = this.constructor;
  return this.then(
    (value) => P.resolve(callback()).then(() => value),
    (reason) =>
      P.resolve(callback()).then(() => {
        throw reason;
      })
  );
};

```

上面代码中，不管前面的 Promise 是`fulfilled`还是`rejected`，都会执行回调函数`callback`。

从上面的实现还可以看到，`finally`方法总是会返回原来的值(传入什么即传出什么)

```javascript
// resolve 的值是 undefined
Promise.resolve(2).then(
  () => {},
  () => {}
);

// resolve 的值是 2
Promise.resolve(2).finally(() => {});

// reject 的值是 undefined
Promise.reject(3).then(
  () => {},
  () => {}
);

// reject 的值是 3
Promise.reject(3).finally(() => {});

```

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z4r5oqz4j30jg0hkwio.jpg" alt="image.png" style="zoom: 50%;" />

### ④ Promise.all()

`Promise.all()`方法用于将多个 Promise 实例，包装成一个新的 Promise 实例。

```javascript
const p = Promise.all([p1, p2, p3]);
```

* `Promise.all()`方法接受一个数组作为参数，
* `p1`、`p2`、`p3`都是 Promise 实例，如果不是，就会先调用下面讲到的`Promise.resolve`方法，将参数转为 Promise 实例，再进一步处理。
* 另外，`Promise.all()`方法的参数可以不是数组，但必须具有 Iterator 接口，且返回的每个成员都是 Promise 实例。

#### a) 返回的状态由什么决定?

`p`的状态由`p1`、`p2`、`p3`决定，分成两种情况。

1. 只有`p1`、`p2`、`p3`的状态都变成`fulfilled`，`p`的状态才会变成`fulfilled`，此时`p1`、`p2`、`p3`的返回值组成一个数组，传递给`p`的回调函数。
2. 只要`p1`、`p2`、`p3`之中有一个被`rejected`，`p`的状态就变成`rejected`，此时第一个被`reject`的实例的返回值，会传递给`p`的回调函数。

**例子1**

```javascript
let p1 = new Promise((resolve, reject) => {
  resolve("OK");
});
// let p2 = Promise.resolve('Success');
let p2 = Promise.reject("Error");
let p3 = Promise.resolve("Oh Yeah");

const result = Promise.all([p1, p2, p3]);
console.log(result);

```

上面代码中，`promises`是包含 3 个 Promise 实例的数组，只有这 3 个实例的状态 **都** 变成`fulfilled`，或者**其中有一个变为`rejected`**，才会调用`Promise.all`方法后面的回调函数。

**例子2**

```javascript
const databasePromise = connectDatabase(); //假设定义了一个异步方法,此方法能拿到你需要的所有数据

const booksPromise = databasePromise //定义一个方法,在 databasePromise() 执行后寻找其内部书本信息
  .then(findAllBooks);

const userPromise = databasePromise //定义一个方法,在 databasePromise() 执行后寻找其内部当前用户信息
  .then(getCurrentUser);

Promise.all([booksPromise, userPromise]).then(([books, user]) =>
  pickTopRecommendations(books, user)
);

```

上面代码中，`booksPromise`和`userPromise`是两个异步操作，只有等到它们的结果都返回了，才会触发`pickTopRecommendations`这个回调函数。

#### b) 如果参数中的Promise实例定义了自己的catch方法 ?

注意，如果作为参数的 Promise 实例，自己定义了`catch`方法，那么它一旦被`rejected`，并不会触发`Promise.all()`的`catch`方法。

```javascript
//定义一个状态将为成功的的promise
const p1 = new Promise((resolve, reject) => {
  resolve("hello");
})
  .then((result) => result)
  .catch((e) => e);

//定义一个将抛出错误的promise
const p2 = new Promise((resolve, reject) => {
  throw new Error("报错了");
})
  .then((result) => result)
  .catch((e) => {
    console.log("p2自己的catch捕获: ", e);
    return e; //异常获取后原样返回,不做修改
  });

//调用 Promise.all 方法
Promise.all([p1, p2])
  .then((result) => console.log(" Promise.all 方法中的成功回调: ", result))
  .catch((e) => console.log(" Promise.all 方法中的catch", e));

// p2自己的catch捕获:  Error: 报错了
// Promise.all 方法中的成功回调:  (2) ['hello', Error: 报错了]

```

上面代码中，

* `p1`会`resolved`，`p2`首先会`rejected`
* 但是`p2`有自己的`catch`方法，该方法返回的是一个新的 Promise 实例，`p2`指向的实际上是这个实例。
* 该实例执行完`catch`方法后，也会变成`resolved`，导致`Promise.all()`方法参数里面的两个实例都会`resolved`
* 因此会调用`then`方法指定的回调函数，而不会调用`catch`方法指定的回调函数

#### c)  如果参数中的Promise实例没有定义自己的catch方法 ?

如果`p2`没有自己的`catch`方法，就会调用`Promise.all()`的`catch`方法。

```javascript
//定义一个状态将为成功的的promise
const p1 = new Promise((resolve, reject) => {
  resolve("hello");
}).then((result) => result);

//定义一个将抛出错误的promise
const p2 = new Promise((resolve, reject) => {
  throw new Error("报错了");
}).then((result) => result);

//调用 Promise.all 方法
Promise.all([p1, p2])
  .then((result) => console.log(" Promise.all 方法中的成功回调: ", result))
  .catch((e) => console.log(" Promise.all 方法中的catch", e));

// Promise.all 方法中的catch Error: 报错了

```

### ⑤ Promise.race()

`Promise.race()`方法同样是将多个 Promise 实例，包装成一个新的 Promise 实例。

```javascript
const p = Promise.race([p1, p2, p3]);
```

上面代码中，只要`p1`、`p2`、`p3`之中有一个实例率先改变状态，`p`的状态就跟着改变。那个率先改变的 Promise 实例的返回值，就传递给`p`的回调函数。

`Promise.race()`方法的参数与`Promise.all()`方法一样，如果不是 Promise 实例，就会先调用下面讲到的`Promise.resolve()`方法，将参数转为 Promise 实例，再进一步处理。

#### a) 举个简单的例子

如p1延时,开启了异步,内部正常是同步进行,所以`p2p3p1`,结果是`P2`

```js
let p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("OK");
  }, 1000);
});
let p2 = Promise.resolve("Success");
let p3 = Promise.resolve("Oh Yeah");

//调用
const result = Promise.race([p1, p2, p3]);

console.log(result);
```

#### b) 举个应用实例

下面是一个例子，如果指定时间内没有获得结果，就将 Promise 的状态变为`reject`，否则变为`resolve`。

```javascript
const p = Promise.race([
  fetch("https://gitee.com/hongjilin"),
  new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error("请求超时!!!!")), 5000);
  })
]);

p.then(console.log).catch(console.error);
```

上面代码中，如果 5 秒之内`fetch`方法无法返回结果，变量`p`的状态就会变为`rejected`，从而触发`catch`方法指定的回调函数。

### ⑥ Promise.allSettled()

`Promise.allSettled()`方法接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例。

**只有等到所有这些参数实例都返回结果**，不管是`fulfilled`还是`rejected`，包装实例才会结束。

该方法由 [ES2020](https://github.com/tc39/proposal-promise-allSettled) 引入。

#### a) 举个简单的例子

```javascript
const promises = [
  fetch("https://gitee.com/hongjilin"),
  fetch("https://github.com/Hongjilin"),
  fetch("./hong.json")
];
loading = true; //请求前将 loading 改为true ; 页面出现滚动加载图标蒙层
await Promise.allSettled(promises);
loading = false;

```

上面代码对服务器发出三个请求，等到三个请求都结束，不管请求成功还是失败，加载的滚动图标就会消失。

#### b)  该方法返回的新的 Promise 实例，一旦结束，状态总是`fulfilled`，不会变成`rejected`

该方法返回的新的 Promise 实例，一旦结束，状态总是`fulfilled`，不会变成`rejected`。状态变成`fulfilled`后，Promise 的监听函数接收到的参数是一个数组，每个成员对应一个传入`Promise.allSettled()`的 Promise 实例。

```javascript
const resolved = Promise.resolve("返回成功状态的promise");
const rejected = Promise.reject("返回失败状态的promise");

const allSettledPromise = Promise.allSettled([resolved, rejected]);
// Promise.allSettled 得到的新实例状态只会是 `fulfilled`
allSettledPromise.then((results) => {
  console.log(results); //注意,这是 `fulfilled` 的回调函数,只有其状态为成功才能进到这里
});
/*
[
{ "status": "fulfilled", "value": "返回成功状态的promise" },
{ "status": "rejected", "reason": "返回失败状态的promise" }
]
*/

```

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7z6il4qsfj30pg07aq6h.jpg)

* `Promise.allSettled()`的返回值`allSettledPromise`，状态只可能变成`fulfilled`(注意,是 **allSettledPromise** 的状态,而不是内部的promise实例)
* 它的监听函数接收到的参数是数组`results`。该数组的每个成员都是一个对象，对应的是传入`Promise.allSettled()`的 Promise 实例。
* 每个对象都有`status`属性，该属性的值只可能是字符串`fulfilled`或字符串`rejected`。
* `fulfilled`时，对象有`value`属性，`rejected`时有`reason`属性，对应两种状态的返回值。

#### c) 举个返回值用法的例子

```javascript
const promises = [fetch("./data.json"), fetch("https://gitee.com/data")];
const results = await Promise.allSettled(promises);

// 过滤出成功的请求
const successfulPromises = results.filter(
  (item) => item.status === "fulfilled"
);

// 过滤出失败的请求，并取得它们的失败原因
const errors = results
  .filter((p) => p.status === "rejected")
  .map((p) => p.reason);

```

有时候，我们不关心异步操作的结果，只关心这些操作有没有结束。这时，`Promise.allSettled()`方法就很有用。如果没有这个方法，想要确保所有操作都结束，就很麻烦。`Promise.all()`方法无法做到这一点。

```javascript
const urls = ["https://gitee.com/hongjilin", "https://github.com/Hongjilin"];
const requests = urls.map((x) => fetch(x));
//举例用 Promise.all 尝试实现,很明显,难以实现
try {
  await Promise.all(requests);
  console.log("所有请求都成功。");
} catch {
  console.log("至少一个请求失败，其他请求可能还没结束。");
}

```

上面代码中，`Promise.all()`无法确定所有请求都结束。想要达到这个目的，写起来很麻烦，有了`Promise.allSettled()`，这就很容易了

### ⑦ Promise.any()

ES2021 引入了[`Promise.any()`方法](https://github.com/tc39/proposal-promise-any)。该方法接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例返回。只要参数实例有一个变成`fulfilled`状态，包装实例就会变成`fulfilled`状态；如果所有参数实例都变成`rejected`状态，包装实例就会变成`rejected`状态。

#### a) 与 `Promise.race()` 方法的区别

`Promise.any()`跟`Promise.race()`方法很像，只有一点不同，就是不会因为某个 Promise 变成`rejected`状态而结束。

```javascript
const promises = [
  fetch("https://gitee.com/hongjilin").then(() => "a"),
  fetch("https://github.com/Hongjilin").then(() => "b"),
  fetch("./data.json").then(() => "c")
];
try {
  const first = await Promise.any(promises);
  console.log(first);
} catch (error) {
  console.log(error);
}

```

上面代码中，`Promise.any()`方法的参数数组包含三个 Promise 操作。其中只要有一个变成`fulfilled`，`Promise.any()`返回的 Promise 对象就变成`fulfilled`。如果所有三个操作都变成`rejected`，那么`await`命令就会抛出错误。

#### b) Promise.any() 抛出的错误

`Promise.any()`抛出的错误，不是一个一般的错误，而是一个 AggregateError 实例。它相当于一个数组，每个成员对应一个被`rejected`的操作所抛出的错误。下面是 AggregateError 的实现示例。

```javascript
new AggregateError() extends Array - AggregateError

const err = new AggregateError();
err.push(new Error("first error"));
err.push(new Error("second error"));
throw err;
```

捕捉错误时，如果不用`try...catch`结构和 await 命令，可以像下面这样写。

```javascript
Promise.any(promises).then(
  (first) => {
    // Any of the promises was fulfilled.
  },
  (error) => {
    // All of the promises were rejected.
  }
);

```

#### c) 再举个例子

下面是一个例子。

```javascript
const resolved = Promise.resolve("成功");
const rejected = Promise.reject("失败了");
const alsoRejected = Promise.reject("太失败了");

Promise.any([resolved, rejected, alsoRejected]).then((result) => {
  console.log(result); // 成功
});

Promise.any([rejected, alsoRejected]).catch((results) => {
  console.log(results); //AggregateError: All promises were rejected
});

```

三个Promise中有一个为成功，则总的结果就是成功,三个中全部失败，才会变成失败。

### ⑧ Promise.resolve()

有时需要将现有对象转为 Promise 对象，`Promise.resolve()`方法就起到这个作用。

```javascript
const jsPromise = Promise.resolve($.ajax("https://gitee.com/hongjilin"));
```

上面代码将 jQuery 生成的`deferred`对象，转为一个新的 Promise 对象。

`Promise.resolve()`等价于下面的写法。

```javascript
Promise.resolve("data");
// 等价于
new Promise((resolve = resolve("data")));
```

`Promise.resolve()`方法的参数分成四种情况

#### a) 参数是一个 Promise 实例

 如果参数是 Promise 实例，那么`Promise.resolve`将不做任何修改、原封不动地返回这个实例。

```js
let p1 = Promise.resolve(521);
//如果传入的参数为 非Promise类型的对象, 则返回的结果为成功promise对象
//如果传入的参数为 Promise 对象, 则参数的结果决定了 resolve 的结果
let p2 = Promise.resolve(
  new Promise((resolve, reject) => {
    // resolve('OK');
    reject("Error");
  })
);
// console.log(p2);
p2.catch((reason) => {
  console.log(reason);
});
```

#### b) 参数是一个`thenable`对象

`thenable`对象指的是具有`then`方法的对象，比如下面这个对象。

```javascript
let thenable = {
  then: (resolve, reject) => {
    resolve("成功");
  }
};

```

`Promise.resolve()`方法会将这个对象转为 Promise 对象，然后就立即执行`thenable`对象的`then()`方法。

```javascript
let thenable = {
  then: (resolve, reject) => {
    resolve("成功");
  }
};

let p1 = Promise.resolve(thenable);
p1.then((value) => {
  console.log(value); // '成功'
});

```

上面代码中，`thenable`对象的`then()`方法执行后，对象`p1`的状态就变为`resolved`，从而立即执行最后那个`then()`方法指定的回调函数，输出 **'成功'**。 

###/# c) 参数不是具有`then()`方法的对象，或根本就不是对象

如果参数是一个原始值，或者是一个不具有`then()`方法的对象，则`Promise.resolve()`方法返回一个新的 Promise 对象，状态为`resolved`。

```javascript
const p = Promise.resolve("ok");

p.then((s) => {
  console.log(s);
});
// ok
```

上面代码生成一个新的 Promise 对象的实例`p`。

* 由于字符串 `ok` 不属于异步操作（判断方法是字符串对象不具有 then 方法）
* 返回 Promise 实例的状态从一生成就是`resolved`，所以回调函数会立即执行
* `Promise.resolve()`方法的参数会同时传给回调函数作为其参数

#### d) 不带有任何参数

`Promise.resolve()`方法允许调用时不带参数，直接返回一个`resolved`状态的 Promise 对象。

所以，如果希望得到一个 Promise 对象，比较方便的方法就是直接调用`Promise.resolve()`方法。

```js
const p = Promise.resolve();

p.then(() => {});
```

```javascript
const p = Promise.resolve();

p.then((val) => {
  console.log(val); // undefined
});
```

上面代码的变量`p`就是一个 Promise 对象。

需要注意的是，立即`resolve()`的 Promise 对象，是在本轮“事件循环”（event loop）的结束时执行，而不是在下一轮“事件循环”的开始时。

```javascript
setTimeout(() => {
  console.log("three"); //这里是新的一轮事件循环
}, 0);

Promise.resolve().then(() => {
  console.log("two"); //本轮同步代码结束后,新一轮事件循环前,就执行
});

console.log("one");

// one
// two
// three

```

上面代码中，`setTimeout(fn, 0)`在下一轮“事件循环”开始时执行，`Promise.resolve()`在本轮“事件循环”结束时执行，`console.log('one')`则是立即执行，因此最先输出。

### ⑨ Promise.reject()

`Promise.reject(reason)`方法也会返回一个新的 Promise 实例，该实例的状态为`rejected`。

```javascript
const p = Promise.reject("出错了");
// 等同于
const p = new Promise((resolve, reject) => reject("出错了"));

p.then(null, (s) => {
  console.log(s);
});
// 出错了

```

上面代码生成一个 Promise 对象的实例`p`，状态为`rejected`，回调函数会立即执行。

`Promise.reject()`方法的参数，会原封不动地作为`reject`的理由，变成后续方法的参数。

```javascript
Promise.reject("出错了").catch((e) => {
  console.log(e === "出错了");
});
// true

```

上面代码中，`Promise.reject()`方法的参数是一个字符串，后面`catch()`方法的参数`e`就是这个字符串。

### ⑩ Promise.try()

实际开发中，经常遇到一种情况：不知道或者不想区分，函数`f`是同步函数还是异步操作，但是想用 Promise 来处理它。因为这样就可以不管`f`是否包含异步操作，都用`then`方法指定下一步流程，用`catch`方法处理`f`抛出的错误。一般就会采用下面的写法。

```javascript
Promise.resolve().then(f);
```

上面的写法有一个缺点，就是如果`f`是同步函数，那么它会在本轮事件循环的末尾执行。

```javascript
const f = () => console.log("now");
Promise.resolve().then(f);
console.log("next");
// next
// now

```

上面代码中，函数`f`是同步的，但是用 Promise 包装了以后，就变成异步执行了。

#### 那么有没有一种方法，让同步函数同步执行，异步函数异步执行，并且让它们具有统一的 API 呢？

#### a) 写法一 : 用`async`函数来写

该知识点如果不懂的可以继续往下看,这是ES6的另外一块知识点内容

```javascript
const f = () => console.log("now");
(async () => f())();
console.log("next");
// now
// next

```

上面代码中，第二行是一个立即执行的匿名函数，会立即执行里面的`async`函数，因此如果`f`是同步的，就会得到同步的结果；如果`f`是异步的，就可以用`then`指定下一步，就像下面的写法。

```javascript
(async () => f())()
.then(...)
```

需要注意的是，`async () = f()`会吃掉`f()`抛出的错误。所以，如果想捕获错误，要使用`promise.catch`方法。

```javascript
(async () => f())()
.then(...)
.catch(...)
```

#### b)  写法二 : 使用`new Promise()`

```javascript
const f = () => console.log("now");
(() => new Promise((resolve) => resolve(f())))();
console.log("next");
// now
// next

```

上面代码也是使用立即执行的匿名函数，执行`new Promise()`。这种情况下，同步函数也是同步执行的。

#### c) Promise.try的引出

鉴于这是一个很常见的需求，所以现在有一个[提案](https://github.com/ljharb/proposal-promise-try)，提供`Promise.try`方法替代上面的写法。

```javascript
const f = () => console.log("now");
Promise.try(f);
console.log("next");
// now
// next
```

事实上，`Promise.try`存在已久，Promise 库[`Bluebird`](http://bluebirdjs.com/docs/api/promise.try.html)、[`Q`](https://github.com/kriskowal/q/wiki/API-Reference#promisefcallargs)和[`when`](https://github.com/cujojs/when/blob/master/docs/api.md#whentry)，早就提供了这个方法。

由于`Promise.try`为所有操作提供了统一的处理机制，所以如果想用`then`方法管理流程，最好都用`Promise.try`包装一下。这样有[许多好处](http://cryto.net/~joepie91/blog/2016/05/11/what-is-promise-try-and-why-does-it-matter/)，其中一点就是可以更好地管理异常。

```javascript
function getUsername(userId) {
  return database.users.get({ id: userId }).then((user) => {
    return user.name;
  });
}

```

上面代码中，`database.users.get()`返回一个 Promise 对象，如果抛出异步错误，可以用`catch`方法捕获，就像下面这样写。

```javascript
database.users.get({id: userId})
.then(...)
.catch(...)
```

但是`database.users.get()`可能还会抛出同步错误（比如数据库连接错误，具体要看实现方法），这时你就不得不用`try...catch`去捕获。

```javascript
try {
database.users.get({id: userId})
.then(...)
.catch(...)
} catch (e) {
// ...
}
```

上面这样的写法就很笨拙了，这时就可以统一用`promise.catch()`捕获所有同步和异步的错误。

```javascript
Promise.try(() => database.users.get({id: userId}))
.then(...)
.catch(...)
```

事实上，`Promise.try`就是模拟`try`代码块，就像`promise.catch`模拟的是`catch`代码块。

# 三、Promise + async + await 

Promise异步，await异步转同步，async同步转异步

1. await 可以理解为是 async wait 的简写。await 必须出现在 async 函数内部，不能单独使用。
2. await 后面可以跟任何的JS 表达式。虽然说 await 可以等很多类型的东西，但是它最主要的意图是用来等待 Promise 对象的状态被 resolved。如果await的是 promise对象会造成异步函数停止执行并且等待 promise 的解决,如果等的是正常的表达式则立即执行      
3. 方法体内部的某个表达式使用await修饰，那么这个方法体所属方法必须要用async修饰所以使用awit方法会自动升级为异步方法

## a、async函数

1. 函数的返回值为 promise 对象 
2. promise 对象的结果由 async 函数执行的返回值决定

## b、await表达式

1. await 右侧的表达式一般为 promise 对象, 但也可以是其它的值 

2. 如果表达式是 promise 对象, await 返回的是 promise 成功的值 
3. 如果表达式是其它值, 直接将此值作为 await 的返回值

```js
async function main() {
  try {
    //读取第一个文件的内容
    let data1 = await mineReadFile("./resource/1x.html");
    let data2 = await mineReadFile("./resource/2.html");
    let data3 = await mineReadFile("./resource/3.html");
    console.log(data1 + data2 + data3);
  } catch (e) {
    console.log(e.code);
  }
}

```

## c、注意

1. await 必须写在 async 函数中, 但 async 函数中可以没有 await 
2. 如果 await 的 promise 失败了, 就会抛出异常, 需要通过 try...catch... 捕获处理

## d、自己对某些问题理解解答

### 1、如何在Promise外部使用Promise的结果

1. axios本质上就是一个promise,所以下面用定时器 + Promise模拟axios,效果一样。

   ```js
   new Promise((resolve) => {
     setTimeout(() => {
       resolve("promise普通结果");
     }, 1000);
   });
   // 等价于
   axios({})
   ```

2. resolve() 与reject()是修改Promise状态并往外抛出的,一个Promise只能改变一次状态,所以一个Promise中只能调用一次

3. 上一步抛出后可以在下面的.then()中获取到

   - 如果没有用.then(),则值会抛往Promise外部
   - 如果声明了.then(),则值会被.then()接住,放到里面处理,如果需要再次抛出 --`某些业务场景需要` ,然后在下一个then()或者外部使用, 则可以 .then( v => return v ) --- 前提这个链式调用前曾使用过resolve() 与reject()才用return,不然就用这两个resolve() 与reject()

```js
new Promise((resolve) => {
  setTimeout(() => {
    resolve("promise普通结果");
  }, 1000);
});

let resolveCommon = () => {
  let result = "普通promise初始值";
  result = new Promise((resolve) => {
    setTimeout(() => {
      resolve("promise普通结果");
    }, 1000);
  });
  console.log(result); //打印结果: Promise { <pending }
};

let resolveAsync = async () => {
  let result = "await+async的promise初始值";
  result = await new Promise((resolve) => {
    setTimeout(() => {
      resolve("这是async+await结果");
    }, 1000);
  });
  console.log(result);
  //打印结果: 这是async+await结果  这里就是正确的值,你可以在下一步进行正常使用,也可以用在下一步的promise中
  //------------------------------------------------------
  //在第二个promise中调用使用
  let result2 = "";
  result2 = await new Promise((resolve) => {
    setTimeout(function () {
      resolve(result + "+经过第二个promise加工");
    }, 1000);
  }).then((v) => {
    console.log("第二个promise的then()中打印并返回:", v);
    return v + ",经过then()加工返回";
  });
  console.log("最终结果:第二个promise外部结果打印,", result2);
  //---------------------------------------------
};
resolveCommon(); //调用普通promise函数
resolveAsync(); //调用await+async
/**
运行结果
1.resolveCommon() 运行结果:    Promise { <pending }
2.resolveAsync() 运行结果:     
这是async+await结果
第二个promise的then()中打印并返回: 这是async+await结果+经过第二个promise加工
最终结果:第二个promise外部结果打印, 这是async+await结果+经过第二个promise加工,经过then()加工返回
*/
```

原因解析:

1. new Promise()是一个异步任务,会加到异步队列中,而正常运行比如console.log()是同步运行的(即从上往下运行),会加到同步队列 

  所以 Promise()通常是会在同一等级的同步任务之后才得到结果的 所以你得到的是一个挂起的 `Promise { <pending }` 对象

2. 而await则是让跟在后面的异步任务转为同步任务(效果如此,就通俗来讲,具体概念需要自学),所以result就能得到一个已经修改状态为成功或者失败的值，所以下面的任务就可以使用到这个值

# 四、promise 输出顺序题目

相关资料：

1. [ES6 Promise笔试题](https://segmentfault.com/a/1190000020934020)
2. [让人头秃的promise-then执行顺序问题](https://juejin.cn/post/7109088946889424932)
3. [Promise 链式调用顺序引发的思考](https://mp.weixin.qq.com/s/vFluh-_5ou0a_PnfLZacpA)
4. [对嵌套的 Promise 的理解](https://juejin.cn/post/6871103526786760718)
5. [JS系列之 Promise 及链式调用顺序](https://juejin.cn/post/6887480063307038734#heading-23)
6. [深度揭秘 Promise 微任务注册和执行过程](https://juejin.cn/post/6844903987183894535)
7. [为什么慢两拍：关于promise规范thenable的白话解释](https://juejin.cn/post/7018765637870698503)
8. [Promise.then 中的交替执行](https://juejin.cn/post/7088595497086091301)
9. [要就来45道Promise面试题一次爽到底](https://juejin.cn/post/6844904077537574919#heading-34)
10. [async, await, promise 面试题](https://www.learnnote.site/frontend/async-await-promise)
11. [一道面试题：还在纠结async/ await、Promise的执行顺序？](https://juejin.cn/post/6871898249578921992)

## 题目二

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

## 题目三

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

## 题目四

```js
new Promise((resolve) => {
  setTimeout(() => {
    console.log(666);
    new Promise((resolve) => {
      resolve();
    }).then(() => {
      console.log(777);
    });
  });
  resolve();
})
  .then(() => {
    new Promise((resolve) => {
      resolve();
    })
      .then(() => {
        console.log(111);
      })
      .then(() => {
        console.log(222);
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
          console.log(444);
        });
      })
      .then(() => {
        console.log(555);
      });
  })
  .then(() => {
    console.log(333);
  });

```

## 题目五

```js
new Promise((resolve, reject) => {
  console.log("promisel");
  resolve();
})
  .then(() => {
    console.log("then11");

    new Promise((resolve, reject) => {
      console.log("promise2");
      resolve();
    })
      .then(() => {
        console.log("then21");
      })
      .then(() => {
        console.log("then23");
      });
  })
  .then(() => {
    console.log("then12");
  });

```

## 题目六

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
      console.log("1-1");
    }
  )
  .then(() => {
    console.log("1-2");
  })
  .then(() => {
    console.log("1-3");
  });

new Promise((resolve) => {
  resolve(2);
})
  .then(() => {
    console.log("2-1");
  })
  .then(() => {
    console.log("2-2");
  })
  .then(() => {
    console.log("2-3");
  });
// 。。

```

# 五、宏任务与微任务

## a、说明

原理图:

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z8266uimj314a0jo44k.jpg" alt="image.png" style="zoom: 50%;" />

说明:

1. JS中用来存储待执行回调函数的队列包含2个不同特定的列队
  - `宏队列`:用来保存待执行的宏任务(回调),比如:`定时器`回调/ajax回调/dom事件回调
  - `微队列`:用来保存待执行的微任务(回调),比如:`Promise`的回调/muntation回调
2. JS执行时会区别这2个队列:
    - JS执行引擎首先必须执行所有的`初始化同步任务`代码
    - 每次准备取出第一个`宏任务执行前`,都要将所有的`微任务`一个一个取出来执行
    - **同步任务** -- **微任务** -- **宏任务**

## b、代码与示例

你需要一些栗子来帮助验证自己的想法是否正确,尽量先不看结果去自己思考下打印结果顺序

### 1、代码示例:

#### a) 例子1

 此处会给出每个打印放入什么队列,加深你的印象

 ```js
 setTimeout(() => {
   console.log("timeout callback1（）"); //立即放入宏队列
   Promise.resolve(3).then((value) => {
     console.log("Promise onResolved3()", value); //当这个宏任务执行后 立马放入微队列,所以这个微任务执行完后下个宏任务才能执行
   });
 }, 0);
 
 setTimeout(() => {
   console.log("timeout callback2（）"); //立即放入宏队列,
 }, 0);
 
 Promise.resolve(1).then((value) => {
   console.log("Promise onResolved1()", value); //立即放入微队列
   setTimeout(() => {
     console.log("timeout callback3（）", value); //立即放入宏任务
   }, 0);
 });
 
 Promise.resolve(2).then((value) => {
   console.log("Promise onResolved2()", value); //立即放入微队列
 });
 console.log("同步代码"); //同步代码立即执行
 
 ```

#### b) 尝试自己思考下

```js
setTimeout(() => console.log("代码开始执行"), 0);
new Promise((resolve, reject) => {
  console.log("开始for循环");
  for (let i = 0; i < 10000; i++) {
    i == 99 && resolve();
  }
}).then(() => console.log("执行then函数"));
console.log("代码执行结束");

```

### 2、示例结果:

#### a) 第一个栗子的结果

```js
'同步代码',
'Promise onResolved1()',
'Promise onResolved2()',
'timeout callback1（）',
'Promise onResolved3()',
'timeout callback2（）',
'timeout callback3（）'
```

#### b) 第二个栗子的结果

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z88ff2n9j30ku0em42z.jpg" alt="image.png" style="zoom:50%;" />

PS: 可以忽略`undefined`这个打印结果, 因为这会加重我们对于宏任务与微任务的理解负担.

# 六、对浏览器console控制台输出undefined的分析

是在控制台输入的内容,它的返回值会显示出来，如果是没有返回值的表达式或语句，则会返回 `undefined`。

## 1、出现场景

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z88ff2n9j30ku0em42z.jpg" alt="image.png" style="zoom:50%;" />

## 2、尝试输入其他内容进行分析

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z8anisw8j30mu0jy42p.jpg" alt="image.png" style="zoom:50%;" />

那么做个合理推测: 应该是在控制台输入的内容,它的 `返回值` 会显示出来,这让我们不禁想到JS的 [ **eval()** ]

## 3、eval（string） 

其作用是将 接收的 string 字符串作为参数，对其进行JavaScript 表达式或语句计算，返回得到的值；

如果是没有返回值的表达式或语句，则会返回 undefined；如果没有合法的表达式和语句，则会抛出 SyntaxError 异常 。于是我们可以猜测console控制台的实质就是调用了`eval()`函数

## 4、验证一下

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z8c0k7o6j30kw074dgx.jpg" alt="image.png" style="zoom:50%;" />

## 5、分析其在宏任务与微任务的打印顺序

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7z88ff2n9j30ku0em42z.jpg" alt="image.png" style="zoom:50%;" />

可以看到 [ undefined ] 实在微任务完成后,宏任务执行前打印