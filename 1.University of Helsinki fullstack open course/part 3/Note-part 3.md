Note-part 3

1. 通过命令行直接用 Node 运行程序

```js
node index.js
//脚本设置后可使用 
npm start
```

脚本设置

```js
//package.json
{
  // ...
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ...
}
```

2. express

主要通过中间件处理数据的请求和响应，作出后端服务器(web-server)

之前的是通过json-server

为了提供一个比内置的 http 模块更友好的界面，许多库已经开发出来，以简化使用 Node 作为服务器端开发。这些库致力于为构建后台服务器的一般的用例提供一个更好的抽象，到目前为止，最受欢迎的库是[express](http://expressjs.com/)。

```js
//http web server

const http = require('http')

let notes = [  
    {    
        id: 1,    
        content: "HTML is easy",    
        date: "2019-05-30T17:30:31.098Z",    
        important: true  
    },  
    {    
        id: 2,    
        content: "Browser can execute only Javascript",    
        date: "2019-05-30T18:39:34.091Z",    
        important: false  
    },  
    {    
        id: 3,    
        content: "GET and POST are the most important methods of HTTP protocol",    
        date: "2019-05-30T19:20:14.298Z",    
        important: true  
    }
]
const app = http.createServer((request, response) => {  
    response.writeHead(200, { 'Content-Type': 'application/json' }) 	
    response.end(JSON.stringify(notes))})
const PORT = 3001
app.listen(PORT)
console.log(`Server running on port ${PORT}`)
```

```js
//express

const express = require('express')
const app = express()

let notes = [
  ...
]

app.get('/', (req, res) => {
  res.send('<h1>Hello World!</h1>')
})

app.get('/api/notes', (req, res) => {
  res.json(notes)
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
```

3. Nodemon

```js
npm install --save-dev nodemon
node_modules/.bin/nodemon index.js

{
  // ..
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ..
}

我们现在可以在开发模式下使用如下命令启动服务器:
npm run dev
```

4. 通过 params 获取参数

```js
app.get('/api/notes/:id', (request, response) => {
  const id = Number(request.params.id)
  const note = notes.find(note => {
    console.log(note.id, typeof note.id, id, typeof id, note.id === id)
      //这里为什么要加Rreturn,因为是find函数里面的一部分。
    return note.id === id
  })
  console.log(note)
  response.json(note)
})
```

```js
app.get('/api/notes/:id', (request, response) => {
  const id = Number(request.params.id)
  const note = notes.find(note => note.id === id)
  if (note) {    
      response.json(note)  
  } else {    
      response.status(404).end()  
  }
}
)

//如果接收到的数据缺少*content* 属性的值，服务器将使用状态码400 bad request响应请求
if (!body.content) {
  return response.status(400).json({ 
    error: 'content missing' 
  })
}
```

返回的 HTTP状态码还是200，这意味着响应成功了。

如果删除资源成功，这意味着便笺存在并被删除，我们用状态码[204 no content](https://www.w3.org/protocols/rfc2616/rfc2616-sec10.html#sec10.2.5)响应请求，并返回没有数据的响应。

实际上，只有204和404两个可选项。 为了简单起见，我们的应用在这两种情况下都将响应204。

5. 我们可以通过使用 Node 的[cors](https://github.com/expressjs/cors) 中间件来允许来自其他源的请求。

在前面的部分中，前端可以从作为后端的 json 服务器向地址 http://localhost:3001/notes 索取便笺列表。

我们的后端有一个稍微不同的 url 结构，便笺可以从 http://localhost:3001/api/notes 中获取到。

```js
import axios from 'axios'
const baseUrl = 'http://localhost:3001/api/notes'
const getAll = () => {
  const request = axios.get(baseUrl)
  return request.then(response => response.data)
}

// ...

export default { getAll, create, update }
```

因为我们的服务器位于本地主机端口3001，而我们的前端位于本地主机端口3000，所以它们不具有相同的源。

使用命令安装*cors*

```bash
npm install cors
```

使用中间件并允许来自所有来源的请求:

```js
const cors = require('cors')

app.use(cors())
```

5. 从后端服务部署静态文件

为了让 express 显示 *static content*、 页面 *index.html* 和它用来fetch的 JavaScript 等等，我们需要一个来自 express 的内置中间件，称为[static](http://expressjs.com/en/starter/static-files.html)。

当我们在中间件声明中添加如下内容时

```js
app.use(express.static('build'))
```

每当 express 收到一个 HTTP GET 请求时，它都会首先检查*build* 目录是否包含与请求地址对应的文件。 如果找到正确的文件，express 将返回该文件。

### Proxy

【代理】

前端上的更改导致它不能再在开发模式下工作(当使用命令 npm start 启动时) ，因为到后端的连接无法工作。

![fullstack content](https://fullstackopen.com/static/19026b5379d1feef11ecc20ca2f669a9/5a190/32ea.png)

这是由于将后端地址更改为了一个相对 URL:

```js
const baseUrl = '/api/notes'
```

因为在开发模式下，前端位于地址*localhost: 3000*，所以对后端的请求会发送到错误的地址*localhost:3000/api/notes*。 而后端位于*localhost: 3001*。

如果这个项目是用 create-react-app 创建的，那么这个问题很容易解决。 将如下声明添加到前端仓库的*package.json* 文件中就足够了。

```bash
{
  "dependencies": {
    // ...
  },
  "scripts": {
    // ...
  },
  "proxy": "http://localhost:3001"
  }
```

在重新启动之后，React 开发环境将作为一个[代理](https://create-react-app.dev/docs/proxying-api-requests-in-development/)工作。 如果 React 代码对服务器地址*[http://localhost:3000](http://localhost:3000/)*发出了一个 HTTP 请求，而不是 React 应用本身管理的地址(即当请求不是为了获取应用的 CSS 或 JavaScript) ，那么该请求将被重定向到 *HTTP://localhost:3001* 的服务器。

现在前端也工作良好，可以在开发和生产模式下与服务器一起工作。

我们方法的一个劣势，是前端部署的复杂程度。 部署新版本需要生成新的前端生产构建并将其复制到后端存储库。 这使得创建一个自动化的[部署管道](https://martinfowler.com/bliki/DeploymentPipeline.html)变得更加困难。 部署管道是指通过不同的测试和质量检查将代码从开发人员的计算机转移到生产环境的自动化控制的方法。

有多种方法可以实现这一点(例如将后端和前端代码[放到同一仓库中](https://github.com/mars/heroku-cra-node)) ，但我们现在不讨论这些。

6. 后端连接数据库(getting data from mangoDB)

之前是后端和前端链接，并使用json-server作为仿数据库db.js(getting data from server)

use mongoose

7. 数据库逻辑配置到单独的模块

在我们重构后端的其余部分来使用数据库之前，让我们将 Mongoose 特定的代码提取到它自己的模块中。

让我们为模块*models* 创建一个新目录，并添加一个名为*note.js* 的文件:

8. 定义私密环境变量的值

npm install dotenv

a. 一种方法是在应用启动时定义它

MONGODB_URI=address_here 
npm run dev

b. 一个更复杂的方法是使用[dotenv](https://github.com/motdotla/dotenv#readme) ，你可以使用如下命令安装库:

```bash
npm install dotenv
```

为了使用这个库，我们创建一个 *.env* 文件在项目的根部。 环境变量是在文件内部定义的，它可以是这样的:

```bash
MONGODB_URI='mongodb+srv://fullstack:sekred@cluster0-ostce.mongodb.net/note-app?retryWrites=true'
PORT=3001
```

我们还将服务器的硬编码端口添加到 *PORT* 环境变量中。

*.env* 文件应立即放到gitignore中，因为我们不希望在网上公开任何机密信息! 

```js
//index.js
require('dotenv').config()
```

9. Verifying frontend and backend integration

【验证前端和后端的集成】

当后端扩展时，最好先用 **浏览器，Postman 或者 VS Code REST 客户端 **来测试后端。 接下来，让我们尝试在使用数据库之后创建一个新的便笺:

10. Error handling

我们来改变一下行为，当给定id的note不存在时，服务端会向请求响应404状态。另外我们来实现一个简单的*catch*代码块，来处理*findById*方法返回*rejected*的情况：

```js
app.get('/api/notes/:id', (request, response) => {
  Note.findById(request.params.id)
    .then(note => {
      if (note) {      
        response.json(note)      
      } else {        
        response.status(404).end()      
      }
    })
    .catch(error => {      
    console.log(error)      
    response.status(500).end()    
  })
})

//update
app.get('/api/notes/:id', (request, response) => {
  Note.findById(request.params.id)
    .then(note => {
      if (note) {
        response.json(note)
      } else {
        response.status(404).end() 
      }
    })
    .catch(error => {
      console.log(error)
      response.status(400).send({ error: 'malformatted id' })    
  })
})
```

如果在数据库中没有找到匹配的对象，*note* 的值会是 *null*， 于是 *else* 代码块执行。因此返回的状态是*404 not found*。而如果 *findById* 方法的promise 被拒绝则状态会是 *500 internal server error*。 可以在控制台中看到更多的错误打印信息。

If promise returned by the *findById* method is rejected, the response will have the status code *500 internal server error*. The console displays more detailed information about the error.

11. 最好在单个位置实现所有错误处理

如果我们以后想要将与错误相关的数据报告给外部的错误跟踪系统，比如[Sentry](https://sentry.io/welcome/)，那么这么做就特别有用。

将错误数据传递给中间件Express [error handlers](https://expressjs.com/en/guide/error-handling.html)统一处理

让我们更改 */api/notes/:id* 路由的处理程序，以便它使用*next* 函数向下传递错误。 下一个函数作为第三个参数传递给处理程序:

```js
app.get('/api/notes/:id', (request, response, next) => {  
  Note.findById(request.params.id)
    .then(note => {
      if (note) {
        response.json(note)
      } else {
        response.status(404).end()
      }
    })
    .catch(error => next(error))
})
```

将向前传递的错误作为参数给 *next* 函数。 如果在没有参数的情况下调用 *next*，那么执行将简单地转移到下一个路由或中间件上。 如果使用参数调用*next* 函数，那么执行将继续到*error 处理程序中间件*。

Express [error handlers](https://expressjs.com/en/guide/error-handling.html)是一种中间件，它定义了一个接受*4个参数* 的函数。 我们的错误处理程序如下所示:

错误处理程序检查错误是否是*CastError* 异常，在这种情况下，我们知道错误是由 Mongo 的无效对象 id 引起的。 在这种情况下，错误处理程序将向浏览器发送响应，并将response对象作为参数传递。 在所有其他错误情况下，中间件将错误转发给默认的 Express 错误处理程序。<mark>不是很明白error如何被处理</mark>

The error handler checks if the error is a *CastError* exception, in which case we know that the error was caused by an invalid object id for Mongo. In this situation the error handler will send a response to the browser with the response object passed as a parameter. In all other error situations, the middleware passes the error forward to the default Express error handler.

```js
const errorHandler = (error, request, response, next) => {
  console.error(error.message)

  if (error.name === 'CastError' && error.kind === 'ObjectId') {
    return response.status(400).send({ error: 'malformatted id' })
  } 

  next(error)
}

app.use(errorHandler)
```

12. 中间件加载顺序

```js
app.use(express.static('build'))
app.use(express.json())
app.use(logger)

app.post('/api/notes', (request, response) => {
  const body = request.body
  // ...
})

const unknownEndpoint = (request, response) => {
  response.status(404).send({ error: 'unknown endpoint' })
}

// handler of requests with unknown endpoint
app.use(unknownEndpoint)

const errorHandler = (error, request, response, next) => {
  // ...
}

// handler of requests with result to errors
app.use(errorHandler)
```

### middleware

中间件函数是按顺序执行的，因此中间件的顺序也很重要。

Middleware allows you to define a stack of actions that you should flow through. Express servers themselves are a stack of middlewares.

中间件使您可以定义应执行的操作堆栈。 Express服务器本身就是一堆中间件。

Express is a routing and middleware web framework that has minimal functionality of its own: An Express application is essentially a series of middleware function calls.

Express是一个路由和中间件Web框架，其自身的功能很少：Express应用程序本质上是一系列中间件函数调用。

*Middleware* functions are functions that have access to the [request object](https://expressjs.com/en/4x/api.html#req) (`req`), the [response object](https://expressjs.com/en/4x/api.html#res) (`res`), and the next middleware function in the application’s request-response cycle. The next middleware function is commonly denoted by a variable named `next`.

If the current middleware function does not end the request-response cycle, it must call next() to pass control to the next middleware function. Otherwise, the request will be left hanging.

To skip the rest of the middleware functions from a router middleware stack, call `next('route')` to pass control to the next route. 

**NOTE**: `next('route')` will work only in middleware functions that were loaded by using the `app.METHOD()` or `router.METHOD()` functions.(粗略理解next(),可写可不写，最好写一下)

比如常见的消息中间件，即系统之间的通讯与交互的专用通道，类似于邮局，系统只需要把传输的消息交给中间件，由中间件负责传递，并保证传输过程中的各类问题，如网络问题，协议问题，两端的开发接口问题等均由消息中间件屏蔽了，出现了网络故障时，消息中间件会负责缓存消息，以避免信息丢失。相当于你想给美国发一个邮包，只需要把邮包交给邮局，填写地址和收件人，至于运送过程中的一系列问题你都不需要关心了。

[What does middleware and app.use actually mean in Expressjs?](https://stackoverflow.com/questions/7337572/what-does-middleware-and-app-use-actually-mean-in-expressjs)

[NodeJS / Express: what is “app.use”?](https://stackoverflow.com/questions/11321635/nodejs-express-what-is-app-use)

[Express.js | app.use() Function](https://www.geeksforgeeks.org/express-js-app-use-function/)

[Using middleware](https://expressjs.com/en/guide/using-middleware.html)

## app.use(...)

As you correctly pointed, it is useful for "middlewares", **it will apply to all the GETs, POSTs, etc. you indicate afterwords**. For example, you can use a Middleware only before the GETs you want to be "with user/pass authentication".

- Indicate the folder for static contents: `app.use(express.static(__dirname + "/public"));`
- Including a parser for JSON contents: `app.use(bodyParser.json());`
- Define the "Cookie Parser" signing string: `app.use(cookieParser("Signing text example"));`
- Separate Routers for your URLs in different files: `app.use("/api", apiRouter);` or `app.use("/news", newsRouter);` or `app.use("/", siteRouter);`
- For a custom error handler: `app.use(sites404handler);` or `app.use(globalErrorHandler);`

[在 Node.js 应用程序中使用 ExpressJS IBM学习教程](https://developer.ibm.com/zh/tutorials/learn-nodejs-expressjs/)