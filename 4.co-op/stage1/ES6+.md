# Promise & Generator & async-await

## Generator functions

Generator（生成器）是 ECMAScript 6 中新增的一种函数类型，通过 function* 关键字定义，可以用来控制迭代过程，并且可以在迭代过程中暂停或继续执行。Generator 函数使用起来像一个可迭代对象，可以使用 for ... of 循环或者 next() 方法进行迭代，每次迭代返回一个包含当前值和 done 属性的对象。最大特点就是可以交出函数的执行权（即暂停执行）

```js
function* myGenerator() {
  yield 'hello';
  yield 'world';
}

const iterator = myGenerator();
console.log(iterator.next()); // { value: 'hello', done: false }
console.log(iterator.next()); // { value: 'world', done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```
我们先定义了一个 Generator 函数 myGenerator，其中使用了 yield 关键字来定义要迭代的值。然后我们使用 Generator 函数创建了一个迭代器 iterator，并使用 next() 方法迭代，每次迭代返回一个包含当前值和 done 属性的对象。

```js
function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();

let one = generator.next().value;
// ---
one
1
generator.next().value
2
generator.next().value
3 // 可以拿到值
generator.next().value
undefined
```

cant get 3, It’s because for..of iteration ignores the last value, when done: true. So, if we want all results to be shown by for..of, we must return them with yield:

```js
function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();

for(let value of generator) {
  console.log(value); // 1, then 2
}
ConsoleLog.js:12 1
ConsoleLog.js:12 2
undefined // 拿不到3
```

```js
function* generateSequence() {
  yield 1;
  yield 2;
  yield 3;
}

let generator = generateSequence();

for(let value of generator) {
  alert(value); // 1, then 2, then 3
}
```
As generators are iterable, we can call all related functionality, e.g. the spread syntax ...:

```js
function* generateSequence() {
  yield 1;
  yield 2;
  yield 3;
}

let sequence = [0, ...generateSequence()];

alert(sequence); // 0, 1, 2, 3
```

### "yield" is a two-way street

"yield" 它不仅将结果返回给外部，还可以将值传递到generator内部。

That’s because yield is a two-way street: it not only returns the result to the outside, but also can pass the value inside the generator.
To do so, we should call generator.next(arg), with an argument. That argument becomes the result of yield.

调用 generator.next(arg)，并带上一个参数。这个参数会成为 yield 的结果。

```js
function* gen() {
  // Pass a question to the outer code and wait for an answer
  let result = yield "2 + 2 = ?"; // (*)

  alert(result);
}

let generator = gen();

let question = generator.next().value; // <-- yield returns the value

generator.next(4); // --> pass the result into the generator
```
==The first call generator.next() should be always made without an argument (the argument is ignored if passed).==

It starts the execution and returns the result of the first yield "2+2=?". At this point the generator pauses the execution, while staying on the line (*).
Then, as shown at the picture above, the result of yield gets into the question variable in the calling code.
On generator.next(4), the generator resumes, and 4 gets in as the result: let result = 4.
Please note, the outer code does not have to immediately call next(4). It may take time. That’s not a problem: the generator will wait.

```js
function* gen(x){
  var y = yield x + 2;
  return y;
}

var g = gen(1);
g.next() // { value: 3, done: false }
g.next(6) // { value: 6, done: true }
```
上面代码中，第一个 next 方法的 value 属性，返回表达式 x + 2 的值（3）。第二个 next 方法带有参数2，这个参数可以传入 Generator 函数，作为上个阶段异步任务的返回结果，被函数体内的变量 y 接收。因此，这一步的 value 属性，返回的就是6（变量 y 的值）。
就是相当于直接修改了yeild后面的值
### generator.throw
As we observed in the examples above, the outer code may pass a value into the generator, as the result of yield.
…But it can also initiate (throw) an error there. That’s natural, as an error is a kind of result.
```js
function* gen() {
  try {
    let result = yield "2 + 2 = ?"; // (1)

    console.log("The execution does not reach here, because the exception is thrown above");
  } catch(e) {
    console.log(e); // shows the error
  }
}

let generator = gen();

let question = generator.next().value;

generator.throw(new Error("The answer is not found in my database")); // (2)
```
Generator 函数体外，使用指针对象的 throw 方法抛出的错误，可以被函数体内的 try ... catch 代码块捕获。这意味着，出错的代码与处理错误的代码，实现了时间和空间上的分离，这对于异步编程无疑是很重要的。

```js
function* generate() {
  let result = yield "2 + 2 = ?"; // Error in this line
}

let generator = generate();

let question = generator.next().value;

try {
  generator.throw(new Error("The answer is not found in my database"));
} catch(e) {
  alert(e); // shows the error
}
```
### generator.return

generator.return(value) finishes the generator execution and return the given value.

```js
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();

g.next();        // { value: 1, done: false }
g.return('foo'); // { value: "foo", done: true }
g.next();        // { value: undefined, done: true }
```

### 迭代

在 JavaScript 中，Generator 对象默认只能被迭代一次。每次调用 `next()` 方法都会执行 Generator 函数中的代码，直到遇到 `yield` 关键字或者函数结束为止。当函数执行结束或者遇到 `return` 语句时，Generator 对象的迭代器状态就会变成 `done`，即迭代结束。

如果需要多次迭代 Generator 对象，可以通过将 Generator 函数的返回值设置为一个可迭代对象来实现。例如，可以使用 `yield*` 关键字将另一个 Generator 对象插入到当前 Generator 函数中，使得当前 Generator 对象可以迭代多次。

```js
javascriptCopy code
function* myGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const iterable = {
  [Symbol.iterator]: function* () {
    yield* myGenerator();
  },
};

for (const value of iterable) {
  console.log(value);
}

// Output:
// 1
// 2
// 3

for (const value of iterable) {
  console.log(value);
}

// Output:
// 1
// 2
// 3
```

在上面的示例代码中，我们定义了一个 Generator 函数 `myGenerator`，它可以生成 1、2、3 这三个数值。然后，我们通过定义一个可迭代对象 `iterable`，将 `myGenerator` 插入到其中，并使用 `for...of` 循环来迭代 `iterable`。由于 `iterable` 是一个可迭代对象，因此我们可以对其进行多次迭代，从而实现多次迭代 Generator 对象的效果。

### Summary

Generators are created by generator functions function* f(…) {…}.
Inside generators (only) there exists a yield operator.
The outer code and the generator may exchange results via next/yield calls.

refs: 
1. https://javascript.info/generators
2. https://www.ruanyifeng.com/blog/2015/04/generator.html

### Usage

```js
function* gen(){
  var url = 'https://jsonplaceholder.typicode.com/todos/1';
  var result = yield fetch(url);
}

var g = gen();
var result = g.next(); // 初始化运行

result.value.then(function(data){
  return data.json();
}).then(function(data){
  g.next(data); // 传值，改值，才能拿到数据
});
```

### shortage

1. 复杂性高：相较于普通的回调函数，使用 Generator 函数需要更复杂的代码结构和更高的抽象能力。不熟悉 Generator 函数的开发者可能会感到难以理解和使用。
2. 性能问题：Generator 函数的执行过程中需要保存状态，并利用 yield 暂停函数执行，这样会引入额外的性能开销，可能在某些场景下影响性能表现。Generator 是基于协程实现的，需要一些上下文切换的开销，这可能会影响性能。
3. 兼容性问题：Generator 函数并不是所有的浏览器都支持，在部分较旧的浏览器版本和环境下可能需要进行额外的兼容处理。
4. 可读性差： Generator 可以创建复杂的控制流和异步操作，但由于它们的实现通常需要使用许多 yield 关键字和 next() 方法，这会导致代码可读性较差。
5. 可维护性差：由于 Generator 可以控制异步流程，因此它们通常会导致代码变得复杂，难以维护。
6. 只能使用一次：Generator 只能被迭代一次，而且一旦迭代完成，就不能再重复使用。这意味着如果需要多次使用，需要重新创建一个新的 Generator 对象。
7. 无法中途取消：Generator 通常是在执行异步任务时创建的，一旦创建后，就无法中途取消任务。这可能会导致一些意外的结果，如内存泄漏等问题。

## Async & Await

`async/await` 是 JavaScript 中处理异步操作的一种方式。它是 ES2017 （ES8）引入的新特性，建立在 Promise 之上，可以让异步代码看起来像同步代码，更加易读和易维护。

在 JavaScript 中，async/await 就是一种语法糖，它简化了 Promise 的使用方式，使得异步操作的代码更加清晰、易读。async/await 的本质仍然是 Promise，它只是通过一种更加直观的方式来表达 Promise 的链式调用。

`async/await` 是一个语法糖，它本质上是基于 Promise 的一种封装。`async` 用于声明一个函数为异步函数，这个函数会自动返回一个 Promise 对象，可以使用 `await` 关键字来等待一个 Promise 对象的结果，并将其赋值给一个变量。使用 `try/catch` 可以处理异步操作的异常。

以下是一个使用 `async/await` 处理异步操作的示例：

```js
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

fetchData();
```

在上面的示例中，`fetchData` 函数被声明为异步函数，使用 `await` 关键字等待 `fetch` 返回的 Promise 对象和 `response.json()` 返回的 Promise 对象，分别将它们的结果赋值给 `response` 和 `data` 变量。`try/catch` 用于处理可能发生的异常。

使用 `async/await` 可以让异步代码看起来更加简洁、易读和易维护。但需要注意，`async/await` 本质上仍然是基于 Promise 的异步编程，因此需要理解 Promise 的基本概念和用法。

## diff

|          | Promise                                                      | Generator                                                    | async-await                                                |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 执行方式 | 通过 then 方法或 async/await 调用 resolve/reject 函数        | 通过 next 方法控制执行流程                                   | 通过 async/await 语法糖实现异步操作                        |
| 执行结果 | 异步操作结果可以是 resolved（已完成）、rejected（已拒绝）或 pending | 不返回具体的结果，而是通过 yield 暂停函数执行并返回一个可控制的迭代器 | 异步操作结果可以是 resolved（已完成）或 rejected（已拒绝） |
| 错误处理 | 通过 catch 方法或 async/await 中的 try/catch 捕获错误        | 在执行器函数中手动抛出错误并在调用方使用 try/catch 捕获      | 通过 try/catch 捕获错误                                    |
| 可读性   | 需要编写回调函数或链式调用，可读性较差                       | 可以在函数内部使用 yield 控制执行流程，可读性较好            | 语法糖实现，可读性较好                                     |
| 并发性   | 可以使用 Promise.all 或 Promise.race 实现并发操作            | 不支持并发执行多个异步操作；可以使用 co 库或自行实现并发控制 | 可以使用 Promise.all 或 Promise.race 实现并发操作          |

需要注意的是，Promise 和 async-await 都是基于回调函数的异步编程的改进，而 Generator 则是一种全新的异步编程方式。在实际开发中，选择使用哪种方式应根据具体的场景和需求来决定。



使用 async/await，我们可以使用类似于同步代码的方式来编写异步代码，代码的可读性得到了极大的提升，而且也方便了错误的处理。同时，async/await 还可以避免回调地狱和链式调用的问题，使得代码的结构更加清晰。

# Fetch vs XHR

## Fetch
Fetch 是 JavaScript 中的一种网络请求 API，可以用于从网络上获取数据。它比传统的 XMLHttpRequest 更易于使用和理解，并支持跨域请求。使用 fetch() 方法发起网络请求，然后使用 then() 和 catch() 方法处理响应。

fetch号称是AJAX的替代品，是在ES6出现的，使用了ES6中的promise对象。Fetch是基于promise设计的。Fetch的代码结构比起ajax简单多。==**fetch不是ajax的进一步封装，而是原生js，没有使用XMLHttpRequest对象**。==

The Fetch API provides an interface for fetching resources (including across the network). It is a more powerful and flexible replacement for XMLHttpRequest.

The fetch() method starts the process of fetching a resource from a server.
The fetch() method returns a Promise that resolves to a Response object.

```js
async function logJSONData() {
  const response = await fetch("http://example.com/movies.json");
  const jsonData = await response.json();
  console.log(jsonData);
}
```
https://javascript.info/fetch
https://javascript.info/fetch-api
https://developer.mozilla.org/en-US/docs/Web/API/fetch

- fetch只对网络请求报错，对400，500都当做成功的请求，服务器返回 400，500 错误码时并不会 reject，只有网络错误这些导致请求不能完成时，fetch 才会被 reject。
- fetch默认不会带cookie，需要添加配置项：` fetch(url, {credentials: 'include'})`
- fetch不支持abort，不支持超时控制，使用setTimeout及Promise.reject的实现的超时控制并不能阻止请求过程继续在后台运行，造成了流量的浪费
- fetch没有办法原生监测请求的进度，而XHR可以

## XHR
XMLHttpRequest is a built-in browser object that allows to make HTTP requests in JavaScript.

XMLHttpRequest（XHR）是一个 Web API，用于在浏览器和服务器之间进行异步通信。XHR 可以在不重新加载页面的情况下从服务器获取数据，并允许我们在页面上更新部分内容，而不是整个页面。

```js
function ajax(options) {
  //创建XMLHttpRequest对象
  const xhr = new XMLHttpRequest();

  //初始化参数的内容
  options = options || {};
  options.type = (options.type || "GET").toUpperCase();
  options.dataType = options.dataType || "json";
  const params = options.data;

  //发送请求
  if (options.type === "GET") {
    xhr.open("GET", options.url + (params ? ("?" + params) : ""), true);
    xhr.send(null);
  } else if (options.type === "POST") {
    const contentType = options.dataType === "json"
      ? "application/json"
      : "application/x-www-form-urlencoded";
    const postData = options.dataType === "json"
      ? JSON.stringify(params)
      : params;
    xhr.open("POST", options.url, true);
    xhr.setRequestHeader("Content-Type", contentType);
    xhr.send(postData);
  }

  //接收请求
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      const status = xhr.status;
      if (status >= 200 && status < 300) {
        let responseText = xhr.responseText;
        if (options.dataType === "json") {
          responseText = JSON.parse(responseText);
        }
        options.success && options.success(responseText, xhr);
      } else {
        options.fail && options.fail(status);
      }
    }
  };
}

```

xhr.onreadystatechange 事件会在 XMLHttpRequest 对象的状态发生变化时被触发。XMLHttpRequest 对象的状态是由 readyState 属性来表示的。readyState 属性有 5 种可能的值，分别是：

1. 0 (uninitialized)：已创建 XMLHttpRequest 对象，但尚未调用 open() 方法。
2. 1 (opened)：已经调用 open() 方法，但尚未调用 send() 方法。
3. 2 (headers_received)：已经调用 send() 方法，并且已经接收到了响应头。
4. 3 (loading)：已经接收到响应头，并正在接收响应体（response body）。
5. 4 (done)：已经接收到完整的响应，且可以在客户端使用。

在使用 xhr.onreadystatechange 事件时，通常只需要检查 readyState 的值是否为 4，表示请求已完成并成功接收到响应。此时可以通过 status 属性来获取服务器返回的状态码（如 200 表示请求成功，404 表示请求的资源不存在等），通过 responseText 或者 responseXML 属性获取服务器返回的数据。

```js
ajax({
  url: '/api/getUserInfo',
  type: 'GET',
  dataType: 'json',
  data: {
    id: 123
  },
  success: function (response, xhr) {
    console.log(response); // 处理响应结果
  },
  fail: function (status) {
    console.log(status); // 处理错误情况
  }
});
```



## diff

| 特点       | Fetch                                                        | XHR                                                          |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| API 设计   | Promise API，简单易用，支持链式调用，语法简洁易读。          | 基于事件的 API，使用起来稍微复杂一些，需要手动处理多个回调函数。 |
| 请求类型   | 基于 Promise，可以使用 async/await 和其他 Promise 方法来处理响应结果 | 基于回调函数，需要使用回调函数来处理响应结果                 |
| 凭证信息   | 默认情况下不发送 cookies 和 HTTP 认证信息，但可以通过设置 credentials 选项来启用 | 可以通过设置 withCredentials 属性来启用                      |
| 取消请求   | 支持通过 AbortController 和 AbortSignal 接口来取消请求       | 可以通过 abort() 方法来取消请求                              |
| 错误处理   | 可以使用 try-catch 和 catch() 方法来处理异常                 | 可以使用 onerror 和 onabort 事件来处理异常                   |
| 浏览器支持 | 需要比较新的浏览器支持，但支持程度在逐渐提高                 | 较老的浏览器也支持，但一些新特性可能不支持                   |
| 请求头处理 | 请求头和请求体分离，可以用 Headers 对象来设置请求头。        | 直接通过 setRequestHeader() 方法设置请求头。                 |
| CORS支持   | 原生支持跨域请求，但是在某些情况下仍然会受到跨域限制。       | 需要额外设置                                                 |

取消请求

abortController对象的signal属性被用作fetch请求的一个参数，以便绑定fetch请求。在需要取消fetch请求时，可以调用abort()方法。

需要注意的是，一旦fetch请求被取消，将不会再触发then()或catch()方法。另外，如果同一个AbortController对象用于多个fetch请求，那么它们都将被取消。

```js
const abortController = new AbortController();
const signal = abortController.signal;

fetch(url, {
  signal: signal,
  // 其他 fetch 配置项
}).then(response => {
  // 处理响应
}).catch(error => {
  // 处理错误
});

// 取消请求
abortController.abort();
```

XMLHttpRequest（XHR）对象的取消请求比Fetch API稍微复杂一些。XHR对象不直接提供取消请求的方法，但可以通过调用XHR对象的abort()方法来实现取消请求。

调用XHR对象的abort()方法将终止当前请求并关闭连接。在调用abort()方法后，会触发XHR对象的onreadystatechange事件，将readyState属性设置为0，status属性设置为0。

下面是一个简单的示例代码：

```js
const xhr = new XMLHttpRequest();
xhr.open('GET', url, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      // 处理响应
    } else {
      // 处理错误
    }
  }
};
xhr.send();

// 取消请求
xhr.abort();

```

调用了XHR对象的abort()方法来取消请求。需要注意的是，取消请求将会终止当前的请求，但并不会取消之前已经发送的请求。因此，如果需要在发送请求之前检查是否需要取消请求，需要在调用send()方法之前进行处理。

```js
const xhr = new XMLHttpRequest();
xhr.open('GET', url, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      // 处理响应
    } else {
      // 处理错误
    }
  }
};
xhr.onerror = function() {
  // 处理网络错误
};
xhr.send();

```

设置请求头

```js
const headers = new Headers();
headers.append('Content-Type', 'application/json');

const data = {
  name: 'John',
  age: 30
};

const options = {
  method: 'POST',
  headers: headers,
  body: JSON.stringify(data)
};

fetch('https://example.com/api/users', options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

在这个示例中，首先创建了一个Headers对象，并使用append()方法向其中添加了一个Content-Type头，指示请求体的格式为JSON。

然后，创建一个options对象，设置了请求的方法为POST、请求头为刚才创建的Headers对象、请求体为一个JavaScript对象，该对象通过JSON.stringify()方法进行序列化为JSON格式的字符串。

最后，使用fetch()方法发起请求，并将options对象作为第二个参数传入。在响应返回后，使用json()方法将响应体解析为JavaScript对象，并在控制台中打印出来。

需要注意的是，Headers对象中的头名是不区分大小写的，即'Content-Type'和'content-type'是等效的。

```js
const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};

xhr.open('GET', 'https://example.com/api/users', true);
xhr.setRequestHeader('Authorization', 'Bearer ' + accessToken);
xhr.send();
```

在这个示例中，首先创建了一个XMLHttpRequest对象。然后，通过setRequestHeader()方法设置了Authorization头，值为'Bearer ' + accessToken，其中accessToken是一个字符串，代表访问令牌。

接着，调用open()方法打开一个GET请求，指定了请求的URL和异步请求的方式。

最后，调用send()方法发送请求，并在onreadystatechange事件中处理响应。如果状态码为200，表示请求成功，将响应体输出到控制台中。

需要注意的是，setRequestHeader()方法需要在调用open()方法之后、调用send()方法之前调用。如果需要设置多个请求头，可以多次调用setRequestHeader()方法。同样地，头名也是不区分大小写的。

CORS

Fetch 原生支持跨域请求，但是在某些情况下仍然会受到跨域限制。Fetch 是基于浏览器的原生 API，使用了现代的跨域请求技术，如 CORS（跨域资源共享），因此默认情况下支持跨域请求。

但是，如果请求的目标服务器未在响应头中明确允许跨域请求，则浏览器将拒绝响应。在这种情况下，您将收到一个 CORS 错误，错误消息可能会因浏览器而异。

为了避免这种情况，目标服务器必须在响应头中包含以下内容之一：

- Access-Control-Allow-Origin: *
- Access-Control-Allow-Origin: <origin>

第一个选项表示目标服务器允许来自任何域的跨域请求。第二个选项表示目标服务器只允许来自特定来源的跨域请求，该来源必须在响应头中指定。

需要注意的是，Fetch API 不会自动携带用户凭证信息（例如 cookies）到跨域服务器，除非目标服务器明确允许。在默认情况下，Fetch API 发出跨域请求时不会发送凭证信息。如果您需要发送凭证信息，可以使用 `credentials` 选项设置为 `"include"`，例如：

```js
fetch('https://example.com/api/users', {
  credentials: 'include'
})
.then(response => {
  console.log(response);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，`credentials` 选项设置为 `'include'`，表示在跨域请求中发送凭证信息。如果目标服务器未明确允许，则浏览器仍将拒绝响应。

XMLHttpRequest (XHR) 可以通过 CORS (Cross-Origin Resource Sharing) 实现跨域请求。

CORS 是一种机制，允许 Web 应用服务器进行跨域访问控制。具体来说，CORS 允许一个网页的资源请求来自于不同的域名，其核心思想是使用额外的 HTTP 头来告诉浏览器，允许跨域访问该资源。

在 XHR 中使用 CORS，需要设置 `withCredentials` 属性为 `true`。`withCredentials` 属性指示是否应该在发送请求时使用凭据 (如 cookie 或授权头)。要启用 CORS，还需要设置 `Access-Control-Allow-Origin` 和其他相关响应头。

以下是一个 CORS 请求的例子：

```js
const xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.open('GET', 'https://example.com/api/data');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onload = function() {
  if (xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```

在上面的例子中，设置 `withCredentials` 属性为 `true` 以启用跨域请求，设置请求头 `Content-Type` 为 `application/json`。在服务端响应中，需要设置 `Access-Control-Allow-Origin` 头来允许来自某个源的跨域请求。

需要注意的是，如果要在客户端进行跨域请求，服务端必须允许跨域请求。否则，浏览器将阻止跨域请求，导致请求失败。

`credentials` 是 Fetch API 的一个选项，它是一个枚举类型，用于指定请求中是否包括凭证（例如 cookie、HTTP 认证等）。

默认情况下，Fetch API 不会在请求中包含凭证信息，这意味着不会自动将 cookie、HTTP 认证等信息发送到服务器端。如果需要在请求中包含凭证信息，可以使用 `credentials` 选项来指定。

`credentials` 选项有三个值：

- `omit`：默认值，不包含凭证信息。
- `same-origin`：仅在请求 URL 与当前页面 URL 同源时包含凭证信息。
- `include`：始终包含凭证信息，即使跨域请求。

以下是一个使用 `credentials` 选项的示例：

```js

fetch('https://example.com/api', {
  credentials: 'include'
})
  .then(response => {
    // 处理响应结果
  })
  .catch(error => {
    // 处理错误
  });
```

在上面的示例中，`credentials` 选项被设置为 `'include'`，表示始终包含凭证信息。

# Proxy vs Reflect

https://javascript.info/proxy

Proxy 和 Reflect 是 ES6 引入的两个新特性，它们可以帮助我们更加方便、灵活地处理对象的操作和行为。

代理（Proxy）和反射（Reflect）是 JavaScript 中允许开发人员以独特方式操作对象的两个特性。

代理是一个对象，允许您拦截并自定义对另一个对象执行的操作。当访问代理对象的属性或方法时，代理会拦截操作并可以对其进行自定义处理。代理对象可以用来实现数据绑定、访问控制等功能。

反射是一组内置的方法，可以让您在运行时操作对象的属性和方法。Reflect 对象提供了许多方法，如 Reflect.get()、Reflect.set()、Reflect.has() 等，可以替代传统的对象操作方法，提供更严谨的语法和错误处理。

虽然两者都可以用来操作对象，但它们的使用场景略有不同。代理通常用于实现高级功能，如数据绑定、访问控制等，而反射则用于对象操作的基础功能，例如读取、设置属性等。

## Proxy

Proxy 是一种用于创建对象代理的机制，可以在对象操作前后拦截并自定义处理。它通过在目标对象之前架设一层拦截器，可以对目标对象的读取、赋值、删除、函数调用等操作进行拦截和自定义处理。我们可以通过 Proxy 对象的 `get()`、`set()`、`deleteProperty()` 等方法拦截这些操作，并在其中添加自定义逻辑。

`let proxy = new Proxy(target, handler)`

```js
const validator = {
  set(target, property, value) {
    if (property === 'age') {
      if (typeof value !== 'number' || value <= 0 || value > 120) {
        throw new TypeError('Invalid age')
      }
    }
    target[property] = value
  }
}

const person = new Proxy({}, validator)

person.age = 30 // 正常赋值
console.log(person.age) // 30

person.age = 'foo' // 校验失败，抛出异常

```

## Reflect

Reflect is a built-in object that simplifies creation of Proxy.

Reflect 是一个内置对象，可以简化 Proxy 的创建。

| Operation           | `Reflect` call                      | Internal method |
| :------------------ | :---------------------------------- | :-------------- |
| `obj[prop]`         | `Reflect.get(obj, prop)`            | `[[Get]]`       |
| `obj[prop] = value` | `Reflect.set(obj, prop, value)`     | `[[Set]]`       |
| `delete obj[prop]`  | `Reflect.deleteProperty(obj, prop)` | `[[Delete]]`    |
| `new F(value)`      | `Reflect.construct(F, value)`       | `[[Construct]]` |
| …                   | …                                   | …               |

Reflect 是一个新的全局对象，提供了一组与 Proxy 对象拦截器方法一一对应的静态方法。Reflect 的静态方法与 Proxy 对象拦截器方法的名称和功能基本一致，例如 `Reflect.get()` 方法与 `Proxy` 对象的 `get()` 方法功能相同。使用 Reflect 方法可以更加灵活和方便地执行一些操作，例如在不确定一个对象是否有某个方法时，我们可以使用 `Reflect.has()` 方法来判断，而不需要使用 `obj.hasOwnProperty()` 方法。

```js
const log = {
  set(target, property, value) {
    console.log(`SET ${property} = ${value}`)
    return Reflect.set(target, property, value)
  },
  get(target, property) {
    console.log(`GET ${property} = ${Reflect.get(target, property)}`)
    return Reflect.get(target, property)
  }
}

const obj = new Proxy({}, log)

obj.a = 123 // SET a = 123
console.log(obj.a) // GET a = 123, 123

```



## diff

Proxy有以下限制：

1. 无法代理内部属性，例如一些内置对象(Map, Set, Date, Promise等)的内部属性被称为"internal slots"，Proxy无法拦截这些属性的访问和修改。
2. 私有属性也无法被代理，因为它们也是使用内部属性实现的。
3. 原始对象和代理对象是不同的对象，如果将原始对象用作键值，然后代理它，那么代理对象无法被找到。
4. 代理无法拦截严格相等运算符(===)，因为严格相等运算符只能比较对象和它们自身是否相等，不能比较代理对象和原始对象是否相等。

| 特性                     | Proxy                                           | Reflect                                           |
| ------------------------ | ----------------------------------------------- | ------------------------------------------------- |
| 用途                     | 创建代理对象                                    | 提供操作对象的方法                                |
| 是否可拦截原型链上的操作 | 是                                              | 否                                                |
| 是否可取消拦截操作       | 是                                              | 否                                                |
| 可拦截的操作类型         | get, set, apply等                               | 与Proxy一致                                       |
| 操作返回值               | 可自定义                                        | 固定为Boolean类型                                 |
| 是否可直接调用           | 否，需要通过代理对象来调用                      | 是，可以直接调用方法                              |
| 与Object的关系           | Proxy可以代理任何对象，包括原生对象和自定义对象 | Reflect只能用于操作对象，不具有创建代理对象的功能 |



| 特性       | Proxy                                      | Reflect                                                      |
| ---------- | ------------------------------------------ | ------------------------------------------------------------ |
| 用途       | 创建代理对象，可以拦截和改变目标对象的行为 | 提供了操作对象的方法，不会改变对象行为                       |
| 对象操作   | 可以代理对象的访问、赋值、删除等操作       | 可以操作对象的属性、方法、访问器等                           |
| 拦截方法   | 支持多个拦截方法，例如get、set、has等方法  | 不支持对象拦截，只支持方法拦截                               |
| 错误处理   | 支持抛出TypeError等错误                    | 不支持抛出TypeError等错误                                    |
| 返回值处理 | 有返回值，返回代理对象的代理结果           | 大部分方法返回布尔值或抛出异常，只有Reflect.construct()、Reflect.apply()、Reflect.defineProperty()等方法返回一个新的对象或修改原始对象 |
| 代理处理   | 需要在代理处理函数中处理代理对象           | 可以直接对对象进行元编程操作                                 |
| 性能       | 通常比Reflect性能差                        | 通常比Proxy性能好                                            |

# Map vs Set

Map 是一种以键值对的形式存储数据的集合。其中，键可以是任何类型的值（包括对象、函数等），值也可以是任何类型的值。与 JavaScript 中的普通对象相比，Map 对象支持更多的操作方法，例如迭代、批量操作等。Map 中的键是唯一的，可以通过 get() 和 set() 方法访问和修改对应的值。

Set 是一种存储唯一值的集合，其中的值可以是任何类型的值。与数组相比，Set 保证了其中的值是唯一的，且可以进行更高效的操作，例如查找、删除等。Set 中的值是唯一的，可以使用 add() 和 delete() 方法添加和删除值。

两者的使用场景有所不同。Map 主要用于存储具有一定结构的数据，例如用键值对存储的配置信息、对象之间的关系等；而 Set 则主要用于存储一组唯一的值，例如存储用户的标签、去重等。

需要注意的是，Map 和 Set 都是可迭代的对象，可以使用 for...of 循环遍历其中的元素。同时，它们都支持批量操作方法，例如 Map 的 set() 方法可以接受一个数组或另一个 Map 对象作为参数，从而快速初始化一个 Map。

## Map

Map – is a collection of keyed values.

JavaScript 中的 Map 是一种数据结构，用于存储键值对，其中键可以是任何 JavaScript 对象（包括原始类型、对象和函数），值也可以是任何 JavaScript 对象。

与普通的 JavaScript 对象不同，Map 允许使用对象作为键，并且可以迭代其元素。Map 还提供了一些有用的方法，如 set(key, value)、get(key)、has(key) 和 delete(key)，这些方法可以用来添加、获取、检查和删除键值对。另外，Map 的键和值是有序的，因此它可以按照插入的顺序迭代元素。

与数组相比，Map 可以提供更灵活的键和更快的查找速度，但是它的缺点是占用更多的内存。Map 在许多情况下都可以用来替代普通的 JavaScript 对象，尤其是当需要使用对象作为键时。

| 方法                | 描述                                                         |      |
| :------------------ | :----------------------------------------------------------- | :--- |
| new Map([iterable]) | 创建一个 Map 对象，可选地使用可迭代对象（例如数组）进行初始化，包含一组 [key, value] 键值对。 |      |
| map.set(key, value) | 存储一个键值对，使用给定的 key 和 value，返回 map 对象本身。 |      |
| map.get(key)        | 返回与给定 key 关联的值，如果 key 不存在则返回 undefined。   |      |
| map.has(key)        | 如果 key 存在则返回 true，否则返回 false。                   |      |
| map.delete(key)     | 删除指定 key 对应的元素，返回一个布尔值，如果 key 存在则为 true，否则为 false。 |      |
| map.clear()         | 删除 Map 中的所有元素。                                      |      |

```js
// 使用数组初始化 Map，其中每个子数组都包含一个键和一个对象
const myMap = new Map([
  ['apple', { color: 'red', price: 1 }],
  ['banana', { color: 'yellow', price: 2 }],
  ['orange', { color: 'orange', price: 3 }]
]);

// 获取 Map 中的值
console.log(myMap.get('banana').color); // 输出 'yellow'
```

## Set

Set – is a collection of unique values.

Methods and properties:

| 方法                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| new Set([iterable]) | 创建一个 Set 对象，可选地使用可迭代对象（例如数组）进行初始化，包含一组元素。 |
| set.add(value)      | 添加一个元素到 Set 中，如果该元素已存在则不进行任何操作，返回 set 对象本身。 |
| set.delete(value)   | 删除 Set 中的指定元素，返回一个布尔值，如果元素存在则为 true，否则为 false。 |
| set.has(value)      | 如果 Set 中存在给定元素则返回 true，否则返回 false。         |
| set.clear()         | 删除 Set 中的所有元素。                                      |
| set.size            | 返回 Set 中元素的数量。                                      |

# WeakMap vs WeakSet

The first difference between `Map` and `WeakMap` is that keys must be objects, not primitive values:

需要注意的是，由于 WeakMap 的键必须是对象，并且在没有其他引用时会被自动删除，因此 WeakMap 通常用于实现私有属性、缓存和垃圾回收等场景。而 Map 则适用于通用的键值对存储场景。

总体来说，Map 适用于存储任意类型的数据，并且需要在整个生命周期内保留键值对，而 WeakMap 适用于存储对象，并且需要在对象被销毁时自动删除键值对。

WeakMap is Map-like collection that allows only objects as keys and removes them together with associated value once they become inaccessible by other means.

WeakSet is Set-like collection that stores only objects and removes them once they become inaccessible by other means.

Their main advantages are that they have weak reference to objects, so they can easily be removed by garbage collector.

That comes at the cost of not having support for clear, size, keys, values…

WeakMap 和 WeakSet 被用作“辅助”数据结构，以补充“主要”对象存储。一旦对象从主存储中移除，如果它仅作为 WeakMap 的键或在 WeakSet 中找到，它将自动清除。

https://javascript.info/map-set#set

https://javascript.info/weakmap-weakset



| 特性     | Map                                                  | WeakMap                                              |
| :------- | :--------------------------------------------------- | :--------------------------------------------------- |
| 键类型   | 任何 JavaScript 对象（包括原始类型、对象和函数）     | 只能是对象（不包括原始类型和函数）                   |
| 垃圾回收 | 不会自动回收被引用的键，会一直占用内存               | 只要键不再被引用，垃圾回收机制就会自动将其回收       |
| 迭代     | 支持迭代器和 for-of 循环                             | 不支持迭代器和 for-of 循环                           |
| 大小     | 可以获取 size 属性来获取 Map 的大小                  | 没有 size 属性，不能获取 WeakMap 的大小              |
| 性能     | 存储大量数据时占用内存较多，但在查找和操作数据时较快 | 存储大量数据时占用内存较少，但在查找和操作数据时较慢 |
| 垃圾回收 | 不会被垃圾回收                                       | 可以被垃圾回收                                       |

# 模板字符串

Template literals 是一种在 JavaScript 中用于创建字符串的语法，它允许在字符串中插入表达式以生成动态内容。模板字符串由一对反引号（`）包围，插入表达式时使用 ${expression} 语法。例如：

```js
const name = 'Alice';
const greeting = `Hello, ${name}!`;
console.log(greeting); // 输出: Hello, Alice!
```

使用模板字符串的优点包括：

1. 更方便的字符串拼接：使用模板字符串可以避免传统字符串拼接时需要使用加号（+）来连接多个字符串和变量，使得代码更加简洁易懂。
2. 可读性更高：使用模板字符串可以将代码的结构清晰地呈现出来，从而使代码更易于阅读和理解。
3. 支持多行字符串：传统字符串必须使用反斜杠（\）来表示换行符，而使用模板字符串可以轻松地表示多行字符串。

