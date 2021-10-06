# chapter 1. Node.js概述

## 学习目标

- 了解Node.js是什么
- 安装好Node.js环境

## 学习内容

1. Node.js概述

> Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行环境。
>
> Node.js 使用了一个事件驱动、非阻塞式 I/O 的模型，使其轻量又高效。
>
> Node.js 的包管理器 npm，是全球最大的开源库生态系统。
>
> 一个后台语言，本质就是javascript

2. Node.js特点

- 使用的是为Google Chrome提供动力的V8虚拟机。V8让node在性能上得到巨大的提升，因为它去掉了中间环节，执行的不是字节码，用的也不是解释器，而是直接编译成了本地机器码。
- JavaScript语言
- 事件驱动，非阻塞式I/O
- 使用 npm 来管理包

3. 好处
   - 免费
   - js语言，和前端配合，对于前端上手容易
   - 性能高
   - 中间件、业务服务器代码（b/s  c/s, b/s/s c/s/s 
   - 大公司都在推
   - 生态搭建起来了，框架也成熟了。

4. Node.js安装

- http://nodejs.cn/download/ 官网下载安装，此时 npm 也是一并安装好了。
- 在控制台(windows中的cmd)中输入node -v和npm -v如果输出了版本号，那么 Node 安装成功。
- 我们还可以安装一些编辑器方便我们编辑node代码。比如[webstorm](https://www.jetbrains.com/webstorm/)，[visual studio code](https://code.visualstudio.com/)

## 推荐资料（扩展学习）

- [廖雪峰的教程（左侧菜单 node.js 下的四个教程 ）](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434501245426ad4b91f2b880464ba876a8e3043fc8ef000)

# chapter 2. npm常用命令实战

## 学习目标

- 了解NPM是什么
- 了解NPM的作用
- 掌握NPM常用命令

## 学习内容

### 1. NPM是什么？

NPM（node package manager)，通常称为node包管理器，主要功能就是管理node包，包括：安装、卸载、更新、查看、搜索、发布等。NPM是基于couchdb一个数据库，详细记录了每个包的信息（作者、版本、依赖、授权信息等）。它是世界上最大的软件注册表，每星期大约有 30 亿次的下载量，包含超过 600000 个 *包（package）* （即，代码模块）。来自各大洲的开源软件开发者使用 npm 互相分享和借鉴。包的结构使您能够轻松跟踪依赖项和版本。

### 2. NPM的作用

- 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

### 3. NPM常用命令

所有的东西都可以在[npm](https://www.npmjs.com/)找 

#### npm —S 和 npm —D的使用以及区别

npm i module_name -S 也就是（npm install module_name --save）的简写，它是把安装包的名称和版本号存到到dependencies中

npm i module_name -D也就是*（npm install module_nam --save-dev）的简写，它是把安装包的名称和版本号存到devDependencies中

1）存在dependencies 中的，是在生产环境中要用到的，

比如项目插件：例如element ui、iview、echarts这种插件要在运行中使用的，就要放在dependencies 中所以就用  -S

2）存在devDependencies中的，是在开发环境中要用到的

比如构建工具：gulp和webpack是用来压缩代码，打包等需要的工具，程序实际运行的时候并不需要，就要放在devDependencies中所以要用  -D

3）啥也不写

包名不会进入package.json里面，因此别人不知道安装了这个包，不建议这样。

#### package-lock.json file

保存小依赖的版本。package.json中保存主依赖的主版本。防止别人安装依赖的时候因为版本号的问题而不能运行文件。

- NPM 命令的一般格式都是 npm <command> [ args ]

- 现在带大家一起从零开始创建一个项目，其中所有使用到的命令都是常用命令

  1. 首先确保 `npm` 可用，在控制台中输入 `npm -v` ，输出版本号的话就是可用的

  2. 新建一个目录作为我们的项目目录

  3. 在新建目录下，使用 `npm init` 初始化项目，这个命令会提示一些关于项目的基本信息，作为入门我们可以随意填写。![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/57117826.jpg)

  4. 初始化之后，可以看到项目中多了一个 package.json 文件，里面包含了项目的基本信息，项目依赖的模块以及定义的脚本信息。

     ```json
     {
       "name": "npmTurorial",
       "version": "1.0.0",
       "description": "",
       "main": "index.js",
       "scripts": {
         "test": "echo \"Error: no test specified\" && exit 1"
       },
       "keywords": [],
       "author": "",
       "license": "ISC"
     }
     ```

  5. 在项目中新建一个index.js文件

     第一行总是写上'use strict';是因为我们总是以严格模式运行JavaScript代码，避免各种潜在陷阱。
  
     ```
   'use strict'
     const _ = require('lodash'); //是一个一致性、模块化、高性能的 JavaScript 实用工具库。
     ```
   ```
  
  6. 在控制台用node运行这个index.js
  
   ```
     node index.js
   ```
  
   报错了，显示没有lodash模块，现在就是我们使用npm的时候啦
  
   ```
7. 执行命令 `npm install --save lodash` 安装 lodash 模块![img](http://ww1.sinaimg.cn/large/a4866c58ly1fu3t6zkjxsj20vq05m0tf.jpg)
  
8. 再次运行 index.js 文件没有报错，说明执行成功；![img](http://ww1.sinaimg.cn/large/a4866c58ly1fu3t7rni9cj20aa01s747.jpg)
  
9. 再次查看项目目录多了一个node_modules文件夹，刚才安装的 lodash 模块就保存在 node_modules 中。
  
   ![img](http://ww1.sinaimg.cn/large/a4866c58ly1fu3t9rdm4sj20aa04ijrf.jpg)![img](http://ww1.sinaimg.cn/large/a4866c58ly1fu3ta94k09j207602y745.jpg)
  
  10. lodash 模块安装成功后，pacakge.json 中会看到 dependencies 块下多了 lodash。
  
      ```js
      {
        "name": "npmTurorial",
        "version": "1.0.0",
        "description": "",
        "main": "index.js",
        "scripts": {
          "test": "echo \"Error: no test specified\" && exit 1"
        },
        "keywords": [],
        "author": "",
        "license": "ISC",
        "dependencies": {
          "lodash": "^4.17.10"
      }
      }
      ```

多了一个`dependencies`，这个东西就是我们这个项目所依赖的包啦。我们只安装了一个，所以目前就这么一个。除了查看package.json文件，我们还可以通过一个命令来查看我们所依赖的所有包。在命令行中输入`npm ls`可以查看当前项目下依赖的包是不是非常方便。

11. npm init -y(快捷键创建项目，所有内容自动填写默认内容)

#### 搭建node服务步骤

1. 下载node 

2. 创建一个项目文件夹

3. 创建项目的工程文件

   （npm init -y 资料默认填写 npm init 自己写入相关资料

4. 下载express 

   Nom i express -s

   下载完以后会多了一个node_module,里面都是项目的依赖文件和package-lock.json

   我们同步到托管平台的代码，或者是给别人的代码是不带node_module只需要给项目代码和package.json和package-lock.json就行了别人拿到以后只需要输入 npm i

5. 创建后台入口文件：进入后台最先进入的文件

   server.js  / app.js

6. 配置js文件（配置后台的服务）

   注意：别的后台语言比如java，只需要写后台代码。不需要写服务器代码，有如专门的服务器软件（tomcat、nginx、Apache）node没有，需要自己写。

   - 引入express,require('地址'),var  app=require('express');

     模块引入，node将模块封装，并将接口暴露出来，我们需要通过require引入后，放在变量中，通过变量对其封装的方法进行调用即可。

   - 创建服务

     var app=express()

   - 配置端口号

     端口号的取值范围1-65535 但是1000以下的最好不要用，1000以下是操作系统。默认预留的,80是默认端口,数据库3306

     ```js
     app.listen(端口号,function(){启动后的函数})
     ```

   - 配置客户端可以访问的静态文件目录，将静态文件放在public文件中，index页面默认页面

   - 项目图标配置

     ```js
     //后台配置，只需要配置一次
     serve-favicon
     //下载
     npm i serve-favicon -D
     //引入 
     var favicon = require('serve-favicon')
     //配置
     app.use(favicon('./http/favicon.ico'))
     ```

   - 配置日志

     ```js
     //morgan
     //下载
     npm i morgan -D
     //引入 
     var morgan = require('morgan')
     //配置
     app.use(favicon('./http/favicon.ico'))
     ```

   - 配置mysql

     ```js
     //下载
     npm i mysql -D
     //引入 
     var mysql = require('mysql')
     //配置
     app.use(favicon('./http/favicon.ico'))
     ```

     

### 4. 命令执行

- cls，清空控制台屏幕

- dir，列出当前目录中的文件和目录`node空格+文件名`注意，一定要在当前目录下，可以tab键，自动补齐

- ^c ，停止运行

- ctrl + c，快速的停止node的服务

### 5. 命令行模式和Node交互模式的区分

- 类似C:\>是在Windows提供的命令行模
- 看到>是在Node交互式环境下
- 在命令行模式下，可以执行node进入Node交互式环境，也可以执行node hello.js运行一个.js文件。
- Node交互式环境会把每一行JavaScript代码的结果自动打印出来，但是，直接运行JavaScript文件却不会。

```js
xusumudeMacBook-Pro:~ xusumu$ cd workspace

xusumudeMacBook-Pro:workspace xusumu$ node hello.js
Hello, world.

xusumudeMacBook-Pro:workspace xusumu$ node
```

## 6. 使用严格模式

- 给Nodejs传递一个参数，让Node直接为所有js文件开启严格模式：node --use_strict calc.js
- 后续代码，如无特殊说明，我们都会直接给Node传递--use_strict参数来开启严格模式。

## 推荐资料

- [菜鸟教程(NPM 使用介绍 章节)](https://www.runoob.com/nodejs/nodejs-npm.html)

# chapter 3. Node.js 模块

## 1. http模块

### 学习目标

- 掌握http模块的使用

### 学习内容

### 一、http模块简介

http模块是nodejs中的一个核心模块，不需要我们用npm下载，直接`const http = require('http')`就可以用啦。这个http模块是干嘛的呢？这个模块提供了HTTP服务器和客户端的接口，学习过其他后台开发语言的同学应该知道，我们一般都会使用一个软件（比如Apache、Nginx、IIS）作为我们的HTTP服务器，但是nodejs不需要，一个程序自身就可以构建服务器，而且http模块使用C++实现的，性能可靠，所以我们就来学习一下http模块的使用方法吧。

- 构建一个最简单的返回helloworld的http服务器

  ```
  const http = require('http');
  //引入http模块
  const app = http.createServer(function (req, res) {
      res.end('hello world');
  });
  
  app.listen(3000);
  ```

  运行命令：`node hello.js`

  浏览器访问地址：`localhost:3000` 结果如下：![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1550476364387-3e80fbd4-8f5f-4353-8239-3c80d9329851.png)

  大家可以自己打一下代码，然后用node运行这个文件，如果没有出现错误的话（一般不会有错误，除非3000端口被占用，那就可以换一个端口，就是app.listen(****)），我们打开浏览器，访问localhost:3000

  我们可以看到一个空白的页面，上面就只有一个hello world，没错，一个最简单的http服务器就是这样的啦，我们看看整个HTTP请求的流程是如何的，如图：

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/64293384.jpg)

  然后我们看看代码，函数`http.createServer()`可以创建一个http服务器，函数只有一个参数，一个回调函数

  ```
  function (req, res) {
      res.end('hello world');
  }
  ```

  服务器每收到一个HTTP请求，就会调用这个函数，这个函数的两个参数，req(request是[http.IncomingMessage类](http://nodejs.cn/api/http.html#http_class_http_incomingmessage))是客户端发来的请求对象，res(response是[http.ServerResponse类](http://nodejs.cn/api/http.html#http_class_http_serverresponse))是我们要发回去的响应对象。在触发回调函数之前，node会解析请求的http头，并将它们作为req对象的一部分，我们通过设置res对象，控制返回给客户端的数据。

### 二、req，res对象的属性以及方法

#### A. req对象的常用属性

（我们一般读他们的属性，但是我们也可以写属性，所以我们后面会有各种中间件来帮助我们提取req的属性，便于我们写程序）：

- headers

- httpVersion

- method

- rawHeaders

- statusCode

- statusMessage

- url

  我们修改一下代码来看看这些属性具体是什么：

  ```
  const http = require('http');
  //引入http模块
  const app = http.createServer(function (req, res) {
      console.log(req.headers);
      console.log(req.httpVersion);
      console.log(req.method);
      console.log(req.rawHeaders);
      console.log(req.url);
      res.end('hello world');
  });
  
  app.listen(3000);
  ```

  然后运行，然后访问一下localhost:3000，看看控制台的输出吧。内容非常多，我们每个分看看一下:

- **headers**返回http头信息：

  ```
  { host: 'localhost:3000',
    accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'upgrade-insecure-requests': '1',
    cookie: 'Webstorm-958cac1b=76a05768-7c4e-4fd8-97b1-d55532d1c68e; Phpstorm-9fbc4777=1f12f60a-be06-4174-931b-78c6e8f7e7f8; Webstorm-958ca85c=442f5ab1-8a15-407f-af66-1dcff44c7a21; foo=bar',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
    'accept-language': 'zh-cn',
    'accept-encoding': 'gzip, deflate',
    connection: 'keep-alive' }
  ```

  主要是host主机url地址，cookie，accept接受的返回内容，user-agent用户代理简称UA，用于识别用户的使用环境，accept-language接受的语言，accept-encoding接受的编码类型，这是我们从程序中看到的headers信息，我们可以直接打开我们chrome的控制台，查看网络部分，刷新一下网页，就可以看到一个请求，可以详细的查看这个请求的内容以及响应的内容，如图所示：

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/7003714.jpg)

  可以看到跟我们程序的输出基本一致。

- **httpVersion：** 1.1 就是使用的http协议的版本，一般都是1.1

- **method：** GET 就是使用什么方式发送的请求，一般有GET、POST两种方式

- **rawHeaders：** 其实就是headers，但是它是一个数组，而且实际上他和headers有区别，可以理解为是未经过处理过的headers，具体请看[message.rawHeaders](http://nodejs.cn/api/http.html#http_class_http_incomingmessage)

- **url：** / 就是我们访问的url是什么，我们改变一下我们的url，就可以看到这个值也在变，我们可以依据这个来给用户返回不同的内容。

  ------

  #### 2. *res 对象的常用方法:*

  - **end([data][,encoding][,callback])：** 通知服务器，所有响应头和响应主体都已被发送，即服务器将其视为已完成。每次响应都必须调用 `response.end()` 方法
  - **setHeader(name, value)：** 设置响应头 eg:`response.setHeader('Content-Type', 'text/html');`具体响应头有哪些以及作用，请看[HTTP响应头信息](http://www.runoob.com/http/http-header-fields.html)
  - **write(chunk[,encoding][,callback])：** 发送一块响应主体，也就是发送给客户端的内容
  - **writeHead(statusCode[,statusMessage][,headers])：** 这个结合setHeader方法和设置statusCode，可以一起设置状态码和头信息

#### b. res 对象的常用属性:

- **statusCode：** 设置被发送客户端的状态码

> http模块就到这里啦，这个模块没有什么特别多的内容，然而我们的完备的后台就可以通过这个模块来构建，因为这个模块过于简单，所以才有了网上的各种的框架(express,koa等)，但是不要忘记都是基于这个最基本的模块

### 推荐资料

- [http模块文档](http://nodejs.cn/api/http.html)
- [廖雪峰老师的http教程](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/0014345015296018cac40c198b543fead5c549865b9bd4a000)

### 三、构建web服务器

#### 学习目标

- 更加深入地掌握http模块
- 了解构建服务器的基本方法

#### 学习内容

##### 1.HTTP请求

```
HTTP`请求信息由`http.request`事件发送，这个事件发送的对象是`http.ServerRequest
```

###### 1）http.ServerRequest对象的属性

| 名称        | 含义                                         |
| ----------- | -------------------------------------------- |
| complete    | 描述这个请求信息是不是发送完成了             |
| httpVersion | 描述HTTP协议版本，通常是1.0或者1.1           |
| method      | 描述HTTP请求方法，比如GET,POST,PUT,DELETE等  |
| url         | 描述原始的请求路径                           |
| headers     | 描述HTTP请求头                               |
| trailers    | 描述HTTP请求尾                               |
| connection  | 描述当前的HTTP连接套接字，是net.Socket的实例 |
| socket      | connection属性的别面，套接字                 |
| client      | client属性的别名                             |

###### 2）http.ServerRequest对象的相关事件

| 名称  | 含义                                                         |
| ----- | ------------------------------------------------------------ |
| data  | 请求体数据来了，触发这个事件。                               |
| chunk | 表示接收的数据。如果这个事件服务器没有监听，请求体数据就扔了。 |
| end   | 请求体数据传输完成了，这个事件被触发。后面没数据了           |
| close | 用户请求正常结束了，或者强制中断，都触发                     |

##### 2.HTTP响应

这个对象一般由HTTP 服务器(也就是http.Server)建立而非用户自己手动建立。

###### 1）response对象的属性

| 方法                                                         | 含义                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| response.setEncoding([Encoding](https://school.thoughtworks.cn/learn/program-center/student/index.html)) | 设置默认的编码，data事件触发的时候，响应数据将会以encoding编码的形式发送给浏览器客户端。如果你不设置的话，默认的就是null，就是没有编码，是用Buffer形式存储的。常用的编码就是’utf-8’ |
| response.pause                                               | 暂时停止接收数据和发送的事件，方便实现下载功能               |
| response.resume                                              | 从暂停的状态中恢复过来                                       |

###### 2）response对象的属性

response事件发送的是http.ClientResponse对象，这个对象描述的就是响应信息。

| 名称        | 含义                      |
| ----------- | ------------------------- |
| statusCode  | HTTP状态码: 如200,404,500 |
| httpVersion | HTTP协议版本: 1.0或1.1    |
| headers     | HTTP响应头                |
| trailers    | HTTP响应尾                |

###### 3）http.ClientResponse相关的事件

| 名称  | 含义                                     |
| ----- | ---------------------------------------- |
| data  | 响应数据到达的时候触发                   |
| chunk | 表示接收到的数据，是data事件的第一个参数 |
| end   | 响应数据接收结束的时候触发               |
| close | 客户端和服务端连接结束的时候触发         |

##### 3.简单的服务器

使用node构建web服务器我们在学习http模块的时候就已经看过了，但是当时的例子比较简单，我们需要完善一下。

首先我们还是写一个基本的服务器出来。

```
//一个用helloworld做响应的服务器
const http = require('http');
const app = http.createServer(function (req, res) {
    res.write('hello world');
    res.end();
});
app.listen(3000);
```

当然其实write和end可以合起来写

```
res.end('hello world');
```

当然这个程序里真正的web服务器还差得远，我们得一步一步来，目前这个程序使用res.end发送内容的时候，默认的响应状态码是200，以及默认的响应头。我们可以打开chrome的控制台的网络部分来查看这个响应。

我们最好设定相应的类型以及长度，来帮助浏览器更好更快的解析相应的内容。这个就需要我们设置相应的头字段(我们在http模块中讲过)。

```
const body = 'hello world';
res.setHeader('Content-Type', 'text/plain');
res.serHeader('Content-Length', body.length);
res.end(body);
```

头字段的设置(添加和删除)都必须在res.write和res.end发送之前。现在我们都是返回的简单的字符串，如果我们返回html怎么弄？那我们可以把body改为一段html的代码，然后Content-Type字段需要设定为'text/html'浏览器才能正常解析。

- 根据不同路由，响应不同内容，设置不同的状态码

  一般我们都是200(成功)，还有一个很常见的状态码就是404 Not Found。我们更改一下我们的程序：

  ```
  const http = require('http');
  const app = http.createServer(function (req, res) {
      const url = new URL(req.url,'http://localhost:3000');
      if(url.pathname === '/') {
          const body = 'hello world';
          res.setHeader('Content-Type', 'text/plain');
          res.setHeader('Content-Length', body.length);
          res.write(body);
          res.end();
      } else {
          res.statusCode = 404;
          res.end('404 Not Found');
      }
  });
  
  app.listen(3000, function() {
      console.log('app is listening on localhost:3000');
  })
  ```

  只要访问的不是`/`路径，那么就会返回一个404错误。这是一个简单的路由功能，已经有框架为我们提供了简单方便的路由功能，我们不需要自己每次都这么判断。

- 根据请求的类型，响应不同的内容

  其实我们还可以根据请求的方法(GET, POST)不同来提供不同的内容，现在我们来写一个用POST请求创建待办事项的例子，GET请求就是获取所有的待办事项

  获取请求的方法，req.method属性就是这个方法。

  ```
  todolist = [];
  switch(req.method) {
      case 'GET' : {
          //....
      }
      
      case 'POST' : {
          //....
      }
  }
  ```

- 获取POST方法传递的数据

  POST方法往往伴随着数据，所以我们得接收从浏览器传过来的数据，req对象有data事件和end事件让我们获取到数据，data事件在有数据发送过来的时候触发，end事件在数据发送结束的时候触发，我们就可以写这么一个程序返回我们接收到的数据。

  ```
  let data = '';
  req.on('data', function (chunk) {
      data += chunk;
  });
  
  req.on('end', function () {
      res.end(data);
  })
  break; //别忘了这一段是在case中的
  ```

  然后我们需要测试一下这个程序是不是按照我们的预期运行，我们用控制台的一个命令curl来测试

  ```
  curl -d hello localhost:3000
  ```

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/4194204.jpg)

  看到确实是返回了我们发送给它的数据啦，但是我们的程序肯定不是在控制台中的呀，我们需要在网页上写一个表单，然后让表单提交我们的数据

- 写一个表单

  我们给GET方法写一些内容，让他可以显示我们的待办事项，以及创建待办事项的表单。

  ```
  let body = '<ul>';
  body += todolist.map(item => `<li>${item}</li>`).join('');
  body += `</ul>
  <form method='post'>
      <input type='text' name='item'>
      <input type='submit'>
  </form>`;
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Content-Length', body.length);
  res.write(body);
  res.end();
  break;
  ```

  这个表单用post方式提交，然后我们再用浏览器访问下localhost:3000。

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/3457989.jpg)

  可以看到表单有了，然后目前还没有待办事项的列表，因为目前还没有任何待办事项，我们提交一下看看。

- 修改post方法的内容

  我们之前的post方法的响应就是显示提交的内容，所以我们提交一下这个表单看看

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/16154464.jpg)

  返回了一个这样的字符串（我们的input中的name是item，我输入的是12321312），我们需要解析一下才能拿到我们想要的内容，大家可能想到了之前我们讲过的querystring模块了，没错，我们使用这个模块可以很方便的解析post提交的内容。

  首先引入这个模块`const qs = require('querystring')`

  ```
  let data = '';
  req.on('data', function (chunk) {
      data += chunk;
  });
  
  req.on('end', function () {
      todolist.push(qs.parse(data).item);	 //把数据存到我们的todolist中
      res.end('OK');
  })
  break; //别忘了这一段是在case中的
  ```

  然后我们再次提交，显示OK，然后用GET方式访问localhost:3000(不能在这个页面刷新，因为还是以POST方式发送的，我们重新访问一下就好了)会看到上面有一个待办事项了。

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/5478704.jpg)

  我们的todolist差不多完成了，这里我们直接把待办事项存取在服务器内存中的，我们以后学了数据库之后，可以放在数据库中。

- 支持中文

  我们对于中文的支持没有做，如果我们写一个中文在里面，会发现出来的是乱码，那么我们需要改一个地方，显示页面的时候要指定为utf-8的页面编码。

  在GET那一部分我们设置响应头的时候设置一下

  ```
  res.setHeader('Content-Type', 'text/html;charset=utf-8');
  ```

  就可以了，提交中文之后的显示也正常了。

#### 推荐资料

- [创建最简单的HTTP服务器](https://blog.csdn.net/oneqinglong/article/details/72025776)

### 四、构建接口，返回主页

#### 学习目标

- 掌握在服务器中返回主页的方法

#### 学习内容

上一小节我们都是直接把html代码用字符串的形式返回了，对于一些简单的html来说，可以这样，但是如果我们需要返回一个复杂的页面，那这么写不是要命吗？所以我们应该返回我们的一个html文件，看看应该如何操作吧

- 首先还是写一个最基本的web服务器

```
  const http = require('http');
  const app = http.createServer(function (req, res) {
      res.write('hello world');
      res.end();
  });
  app.listen(3000);
```

- 然后我们先把我们的主页写出来，随便写一个html文件都可以

```
  <!DOCTYPE html>
  <html>

  <head>
      <meta charset="utf-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>ThoughtWorks</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>

  <body>
      <h1>Hello World</h1>
      Hello World 中文意思是『你好,世界』。因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，所以后来的程序员在学习编程或进行设备调试时延续了这一习惯。
  </body>

  </html>
```

写一个简单的html页面就好啦，我们就需要把这个html作为响应发送到客户端。

- 现在就需要在服务器中把这个文件读取出来，并且发送给客户端

  读取文件需要用到fs模块的内容，还记得吗？

```
  const data = fs.readFileSync(__dirname + '/index.html');
```

还记得global模块中的__dirname吗，index.html文件和app.js文件放在同一个目录下，这样就可以获取到html的内容啦，然后我们把它返回给客户端。

```
  const app = http.createServer(function (req, res) {
      const data = fs.readFileSync(__dirname + '/index.html');
      res.setHeader('Content-Type', 'text/html');
      res.write(data);
      res.end();
  });
```

运行之后，我们访问一下localhost:3000看看

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/24084580.jpg)

可以了，然后我们还可以用一个更加简单的写法来传递html的内容。

```
  const app = http.createServer(function (req, res) {
      res.setHeader('Content-Type', 'text/html');
      fs.createReadStream(__dirname + '/index.html').pipe(res);
  });
```

我们用管道操作符把数据流导向response就行了，我们可以用数据流的方式是因为response这个对象的类实现了**可写流**的接口，详细内容可以去官方文档查看哟

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-4/17273355.jpg)

#### 推荐资料

- [http官方文档](http://nodejs.cn/api/http.html)
- [阮老师的参考教程](http://javascript.ruanyifeng.com/nodejs/http.html)
- [创建http，https服务器和客户端](https://blog.csdn.net/ligang2585116/article/details/72827781)

## 2. fs模块

### 学习目标

- 掌握fs模块的使用

### 学习内容

fs（文件系统）模块提供了一些API(类似Unix标准)，让我们可以和文件系统进行一些交互，同样是核心模块，我们不需要npm下载，直接`const fs = require('fs')`就可以使用啦。fs模块的内容比较多，推荐大家去[官网](http://nodejs.cn/api/fs.html#fs_file_system)查看详细的内容，我们讲讲常用的几个API

- **fs.readFile(path[,options],callback)：** 异步地读取一个文件的内容:

  ```
  var fs = require('fs');
  fs.readFile('/etc/passwd', (err, data) => {
    if (err) throw err;
    console.log(data);
  });
  ```

- **fs.readFileSync(path[,options])：** 同步版本的readFile

```
var fs = require('fs');
var data = fs.readFileSync('/etc/passwd');
console.log(data);
```

- **fs.existsSync(path)：** 文件是否存在
- fs.readdir(path[,options],callback) 异步读取一个目录的内容， 回调有两个参数 `(err, files)`，其中 `files` 是目录中不包括 `'.'` 和 `'..'` 的文件名的数组。 注意: 'path' 的路径是以当前文件为基准进行查找的,而不是运行的时候的相对路径。：

```
  var fs = require('fs');
  fs.readdir(__dirname, (err, files) => {
      if (err) throw err;
      console.log(files);
  });
```

files参数就是读取到的所有文件的文件名，它同样有同步版本readdirSync

- **fs.writeFile(path,data,callback)：**异步的写入文件

```
var fs = require('fs');
var data = 'hello node';
fs.writeFile('hello.txt', data, (err) => {
    if (err) throw err;
    console.log('success');
});
```

- **fs.writeFileSync(path,data)：** 同步的写入文件

```
var fs = require('fs');

var data = 'hello node';
fs.writeFileSync('hello.txt', data);
```

> fs模块的内容比较多而且比较杂，大家多参考官方文档以及查询资料来学习

### 推荐资料（推荐学习）

- [fs 官方文档](http://nodejs.cn/api/fs.html)
- [廖雪峰老师的教程](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434501497361a4e77c055f5c4a8da2d5a1868df36ad1000)

## 3. url模块

### 学习目标

- 掌握url模块的使用

### 学习内容

#### 1.URL 字符串与 URL 对象

url模块提供了一些实用的函数，用于url的解析和处理，引入方式：

```
const url = require('url');
```

- 使用url模块解析url

  ```
  const url = require('url');
  console.log(url.parse('http://user:pass@sub.host.com:8080/p/a/t/h?query=string#hash'))
  ```

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/58563355.jpg)是不是把我们所需要的东西都全部解析出来啦。任何东西都可以在这个url.parse()返回的对象中找到，我们用一个图来看看url.parse()的功能

  是不是非常的清晰。但是这个url.parse()方法不是官方推荐的用法，它是旧版本遗留的一个API，所以以后可能会去掉，所以大家写新的程序的时候肯定需要用新的用法，要与时俱进。

  url模块中定义了一个URL类，浏览器端也有，并且浏览器端是全局有效的。我们看看它如何解析url。我们同样解析一个一摸一样的url看看是什么结果。

  ```
  const {URL} = require('url') // const URL = require('url').URL
  console.log(new URL('http://user:pass@sub.host.com:8080/p/a/t/h?query=string#hash'))
  ```

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/58474963.jpg)

  可以看到大部分和url.parse()是一样的，那我们一样放一个图让大家看看这个new URL()和url.parse()的区别。

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/55600818.jpg)

  "url"上方是url.parse()的解析方式，下面的new URL()的解析方式，可以看到new URL()的方式更加好用，第一它解析了username和password，第二他的searchParams属性已经帮我们分隔好了参数的各个内容，我们不需要使用querystring(下面会讲到)来解析了。我们来写一个用searchParams属性获取url中参数的内容。

  ```
  const {URL} = require('url');
  const myURL = new URL('https://example.org/?abc=123');
  console.log(myURL.searchParams.get('abc'));
  ```

  url中abc参数的值就简单的获取到了，非常的好用。

#### 2.URL 接口

- **url.hash**

获取及设置URL的分段(hash)部分

```
const { URL } = require('url');
const myURL = new URL('https://example.org/foo#bar');
console.log(myURL.hash);
  // 输出 #bar

myURL.hash = 'baz';
console.log(myURL.href);
  // 输出 https://example.org/foo#baz
```

- **url.host**

获取及设置URL的主机(host)部分

```
const { URL } = require('url');
const myURL = new URL('https://example.org:81/foo');
console.log(myURL.host);
  // 输出 example.org:81

myURL.host = 'example.com:82';
console.log(myURL.href);
  // 输出 https://example.com:82/foo
```

- **url.hostname**

获取及设置URL的主机名(hostname)部分。 url.host和url.hostname之间的区别是url.hostname不 包含端口

```
const { URL } = require('url');
const myURL = new URL('https://example.org:81/foo');
console.log(myURL.hostname);
  // 输出 example.org

myURL.hostname = 'example.com:82';
console.log(myURL.href);
  // 输出 https://example.com:81/foo
```

- **url.href**

获取及设置序列化的URL

```
const { URL } = require('url');
const myURL = new URL('https://example.org/foo');
console.log(myURL.href);
  // 输出 https://example.org/foo

myURL.href = 'https://example.com/bar';
console.log(myURL.href);
  // 输出 https://example.com/bar
```

- **url.port**

获取及设置URL的端口(port)部分

```
const { URL } = require('url');
const myURL = new URL('https://example.org:8888');
console.log(myURL.port);
  // 输出 8888

myURL.port = 1234;
console.log(myURL.port);
  // 输出 1234
console.log(myURL.href);
  // 输出 https://example.org:1234/
```

### 推荐资料(扩展学习)

- [url官方文档](http://nodejs.cn/api/url.html)
- [nodejs之url模块](https://www.cnblogs.com/whiteMu/p/5983125.html)

## 4. global模块

### 学习目标

- 掌握常用global全局变量

### 学习内容

这个模块是全局变量模块，我们不需要手动引入，在任何地方都可以直接使用。在浏览器环境中(javascript)，一般window是全局对象，而node中global是全局对象，我们直接用的都是global对象的属性和方法。

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1550735441302-14b50742-a0ea-4f7b-89e7-07dc5a246b49.png)

| 对象                                                         | 描述              |
| ------------------------------------------------------------ | ----------------- |
| Buffer                                                       | 数据类型          |
| __dirname                                                    | 当前文件目录      |
| __filename                                                   | 当前文件名称      |
| console                                                      | 控制台输出模块    |
| exports                                                      | commonjs关键字    |
| global                                                       | 共享的全局对象    |
| module                                                       | commonjs关键字    |
| process                                                      | 当前node进程对象  |
| require()、require.cache、require.extensions、require.resolve() | commonjs关键字    |
| setImmediate(callback, …args])                               | event loop相关api |
| setInterval(callback, delay, …args])                         | event loop相关api |
| setTimeout(callback, delay, …args])                          | event loop相关api |
| clearImmediate(immediateObject)                              | event loop相关api |
| clearInterval(intervalObject)                                | event loop相关api |
| clearTimeout(timeoutObject)                                  | event loop相关api |

> 这一部分大家在平时的编程中很有可能会遇到，如果没有遇到过也不要着急，现在知道有这个东西就行，如果遇到了，可以去[官网](http://nodejs.cn/api/globals.html)看更加详细的内容。

### 推荐资料

- [Global 官方文档](http://nodejs.cn/api/globals.html)
- [Node.js 的 Global全局对象](https://cnodejs.org/topic/59a36413bc6d95370812889f)

## 5. path模块

### 学习目标

- 掌握path模块的使用

### 学习内容

path是路径模块，提供了一些工具函数，帮助我们处理文件和目录的路径。通过

`const path = require('path');`来使用，模块的内容不是很多。

### 常用的方法

#### basename(path ,`[`ext`]`)

返回path的最后一个部分比如`/foo/bar/baz/asdf/quux.html`的结果是`quux.html`

#### dirname(path)

返回path的目录名比如`/foo/bar/baz/asdf/quux.html`的结果是`/foo/bar/baz/asdf`

#### extname(path)

返回拓展名比如`/foo/bar/baz/asdf/quux.html`的结果是`html`

#### format(pathObject)

pathObject是一个路径对象详情看[文档](http://nodejs.cn/api/path.html#path_path_basename_path_ext)，这个方法根据这个对象生成一个path

#### isAbsolute(path)

判断是不是绝对路径

#### join(`[`...paths`]`)

使用平台特定的分隔符把全部给定的 `path` 片段连接到一起，并规范化生成的路径。

#### normalize(path)

规范化给定的 `path`，并解析 `'..'` 和 `'.'` 片段比如`path.normalize('/foo/bar//baz/asdf/quux/..');`返回`/foo/bar/baz/asdf`

#### parse(path)

方法跟format方法相反，它可以把一个path解析为一个对象，这个对象的属性有：![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/73426775.jpg)

#### relative(from, to)

返回从from到to的相对路径

#### resolve(`[`...paths`]`)

该方法会把一个路径或路径片段的序列解析为一个绝对路径，如果处理完还为生成一个绝对路径，那么返回当前的工作目录。比如：`path.resolve('/foo/bar', './baz');`的结果是`'/foo/bar/baz'`

### 推荐资料

- [Path 官方文档](http://nodejs.cn/api/path.html)
- [Path 模块部分常用函数解析](https://www.cnblogs.com/xuepei/p/6344670.html)

## 6. querystring模

### 学习目标

- 掌握querystring模块的使用

### 学习内容

querystring模块的内容很少，主要就是用来解析url中查询字符串的，生成一个对象。

通过下面的方式引入:

```
const querystring = require('querystring');
```

- **`querystring.parse(str[, sep[, eq[, options]]])`**

我们一般就是用这个模块来解析http请求中的参数，请求的参数一般都是这个格式的`foo=bar&abc=xyz&abc=123`，我们虽然可以自己写一个函数来解析它，但是node已经提供了非常方便的API供我们调用了，我们看看如何使用。

```
querystring.parse('foo=bar&abc=xyz&abc=123');
```

结果是

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/72228014.jpg)

给我们解析成了一个对象，并且同样的属性会变成一个数组，非常的好用了。

有时候参数的键值对不是用&分隔的，或者键与值之间不是=，我们用这个方法的时候就可以自定义分隔符了，`parse(str[, sep[, eq[, options]]])`是这个函数的定义，sep就是界定查询字符串中的键值对的子字符串，默认为 `&`。eq就是界定查询字符串中的键与值的子字符串,默认为 `=`。

有解析的方法，那就一样有一个生成的方法

- **`querystring.stringify(obj[, sep[, eq[, options]]])`**

它把给入的对象变成一个query string。

```
querystring.stringify({ foo: 'bar', baz: ['qux', 'quux'], corge: '' });
// 返回 'foo=bar&baz=qux&baz=quux&corge='

querystring.stringify({ foo: 'bar', baz: 'qux' }, ';', ':');
// 返回 'foo:bar;baz:qux'
```

其实我们也可以自定义解析和生成使用的函数，一般我们不会自定义，但是我们知道有这个东西就行了。这个模块我们在学习http模块的时候用的比较多（主要就是解析请求的参数），但是在框架中，框架都为我们做好了，我们一般不会用到这个模块。

### 推荐资料(扩展学习)

- [querystring 官方文档](http://nodejs.cn/api/querystring.html)

# chapter 4. nodejs事件循环机制

## 学习目标

- 掌握nodejs的事件驱动和异步I/O的机制
- 了解nodejs的事件队列

## 学习内容

- nodejs的事件驱动

  Node.js 采用**事件驱动**和**异步 I/O** 的方式，实现了一个**单线程**、**高并发**的 JavaScript 运行时环境，而单线程就意味着同一时间只能做一件事。

  大家可能对事件驱动不太了解，那么我们举一个我们之前学习过的例子，大家还记得我们上周学习的http模块吗，它可以创建一个服务器，然后等待客户端进行连接，我给大家放一下当时的代码

  ```
  const http = require('http');
  //引入http模块
  const app = http.createServer(function (req, res) {
      res.end('hello world');
  });
  
  app.listen(3000);
  ```

  这样可能还不是很好看出来是事件驱动的，那么我们换一个等价的写法

  ```
  const http = require('http');
  
  const app = http.createServer();
  
  app.on('request', function(req, res) {	//on('request')这种写法就能感觉到是被动的										  接受请求
      res.end('hello');
  })
  
  app.listen(3000);
  ```

  大家仔细思考一下，这个服务器是不是就是事件驱动的，因为我们不知道什么时候会有人连接，会有谁连接，服务器就只能被动的等待别人连接之后，然后发送数据，所以http的Server类就是事件驱动的。

- 事件循环机制

  我们来看看**事件循环**的原理：![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/58352648.jpg)

  Node.js 在主线程里维护了一个**事件队列，**当接到请求后，就将该请求作为一个事件放入这个队列中，然后继续接收其他请求。当主线程空闲时(没有请求接入时)，就开始循环事件队列，检查队列中是否有要处理的事件，这时要分两种情况：如果是非 I/O 任务，就亲自处理，并通过回调函数返回到上层调用；如果是 I/O 任务，就从 **线程池** 中拿出一个线程来处理这个事件，并指定回调函数，然后继续循环队列中的其他事件。

  简单的说node会在主线程空闲的时候，去查看事件队列中的事件是否发生了，如果发生了，就去执行对应的回调函数。

  我们举个例子大家会了解的更好一点：

  ```
  console.log('hello');
  
  setTimeout(function() {		//我们在global模块中讲过，就是设定过多久以后这个函数会执
      console.log('world');   //行，我们这里设定的是0ms
  }, 0);
  
  console.log('bye');
  ```

  这个程序大家觉得最后的输出是什么呢？这个函数过0ms就执行，相当于立马就执行了，所以输出应该是

  ```
  hello
  world
  bye
  ```

  其实不是，因为我们使用setTimeout之后，里面的那个回调函数就被加入到了事件队列中了，虽然0ms就可以执行（就是事件发生了），但是我们得等到主线程是空闲状态才行，我们知道setTimeout下面还有一句话可以直接执行，所以最后的结果就是

  ```
  hello
  bye
  world
  ```

  因为采用了事件驱动的机制，那么异步I/O就是必然的了。其实node中大部分模块都是基于事件驱动的，node中也提供了一个原始的事件分发器类EventEmitter，它在[event模块](http://nodejs.cn/api/events.html)中，我们可以用它自定义我们的事件,大家有兴趣可以去看看哦。

好了，大家肯定认为node非常的强，仅仅有一个线程就完成了别人需要多线程的工作。我们可以把这种需要IO比较多的程序称为DIRT（data-intensive real-time）程序，也就是数据十分多，所以web(同时连接的数量非常大，IO密集)就是node最擅长的领域了。那么node不擅长什么呢？相对应的就是计算复杂的程序了，如果计算复杂的，就相当于主线程一直在计算，没有办法响应别的事件了。

## 推荐资料

- [JavaScript 运行机制详解：再谈Event Loop — 阮一峰](http://www.ruanyifeng.com/blog/2014/10/event-loop.html)
- [Node.js Event Loop 的理解](https://cnodejs.org/topic/57d68794cb6f605d360105bf)

