# promise顺序问题

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



