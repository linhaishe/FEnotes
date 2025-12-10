# Basic Node and Expressn 210611

以下内容来自 freecodecamp

Intro: 

## 1. Node

Node.js is a JavaScript runtime that allows developers to write backend (server-side) programs in JavaScript. Node.js comes with a handful of built-in modules - small, independent programs - that help facilitate this purpose.

- HTTP: a module that acts as a server
- File System: a module that reads and modifies files
- Path: a module for working with directory and file paths
- Assertion Testing: a module that checks code against prescribed constraints

## 2. Express

Express,while not included with Node.js, is another module often used with it. Express runs between the server created by Node.js and the frontend pages of a web application. Express also handles an application's routing. Routing directs users to the correct page based on their interaction with the application. While there are alternatives to using Express, its simplicity makes it a good place to begin when learning the interaction between a backend powered by Node.js and the frontend.

所有node模块的使用方法都是先在命令行中安装，然后在后端配置文件中引入即调用实例。

```js
//导入模块函数
var express = require('express');
var app = express();

console.log("Hello World");
module.exports = app;
```

<mark>app.listen(port)</mark>:It tells your server to listen on a given port, putting it in running state.

<mark>app.METHOD(PATH, HANDLER)</mark>:

- METHOD: an http method in lowercase.

- PATH:a relative path on the server (it can be a string, or even a regular expression).

- HANDLER:a function that Express calls when the route is matched.

  Handlers take the form `function(req, res) {...}`, where req is the request object, and res is the response object. For example, the handler


## 3. express method

### app.use()

use是使用中间件的意思，最简单的用法是直接加一个函数

响应静态文件,静态文件放在public文件中，相当于根目录是public,访问文件直接在路由中输入文件名和后缀

![951623480322_.pic.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grfhd1debij60bm0eoq3t02.jpg)

http://localhost:3000/test.png，则可打开图片

http://localhost:3000/darktheme/dark.png

```js
app.use('/assets',express.static('public'));

app.use(express.static("public"));
```

```js
//会先输出first middleware -> second middleware -> first middleware after

app.use(function (req, res, next) {
  console.log("first middleware");
  next();
  /*用next()函数将结果传递给下一个中间件，若没有next()函数则流程则直接结束，不会进行下一步操作，如果下一个中间件是get，且没有next，则会不响应okkkkkkkkkkkkkkrrrrrrrrrrrrrrr，next只是参数名，名字可以任意更改，简易不要更改*/
  console.log("first middleware after");
});

//不加路由就表示路径后面随便写什么内容都能到这个页面里面去，这样不安全
//即http://localhost:3000/kkk,也可以打开有okkkkkkkkkkkkkkrrrrrrrrrrrrrrr的页面
app.use(function (req, res, next) {
  console.log("second middleware");
  res.send("okkkkkkkkkkkkkkrrrrrrrrrrrrrrr");
});

//最好加上路径
app.use("/home", function (req, res, next) {
  console.log("second middleware");
  res.send("ok");
});
```

### app.get()

**数据获取**

```js
app.get("地址", function (request, response) {
  //request 前端给后台的请求
  //response 后台给前端的相应
  request.query; //前端发送的数据
  response.json({});
});

app.post("地址", function (req, res) {
  req.body; //前端发送的数据
});
```

```js
function(req, res) {
  res.send('Response String');
}
//will serve the string 'Response String'.
```

```js
var express = require('express');
var app = express();

app.get("/", function(req, res) {
  res.send("Hello Express");
});

app.listen(3000);

//Use the app.get() method to serve the string "Hello Express" to GET requests matching the / (root) path. 
```

![29B89A89B06DF78A90C0629CD8744FBA.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grcffrjwkbj60og0auwf902.jpg)

### res.send()

```js
//定义路由，调用方法，方法不止get，还有post，delete等
app.get("/", function (req, res) {
  res.send("this is the home page");
 });
```

将后端想要发送的数据发送给前端，传送的内容格式可以是字符串，也可以是json对象，并默认执行json.stringfy()方法。

由于后端向前端发送数据时，<mark>后端都会将数据自动转成字符串格式</mark>，导致我们获取数据的时候不能取到对象内容，所以我们在传送前，手动将传输数据转为json.stringify()，需要用时，调用执行json.parser的方法，获取对象的属性值。从而规避send将一切内容都转化为string,传输数据后前端获取不到数据的问题。

send()只能发送一个内容，由上到下执行，只发送去第一个的数据给前端

![C05CEAAF-F6F0-4F09-9A98-775078F531A3.png](http://ww1.sinaimg.cn/large/005NUwyggy1grcfry0mmbj60sq0a6wfh02.jpg)

### 路由路径里的参数获取

1. 后端设置的动态路由

```js
//动态路由参数获取
app.get("/profile/:id/user/:name", function (req, res) {
  console.log("req.params", req.params);
  res.send(
    "you requested to see a profile with the name of " + req.params.name
  );
}    

//正则表达式
//此正则表达式表示问号前面的字符可以出现一次或者不出现，即b出现0次或者1次
//localhost:3000/abbcd则不能成功
app.get("/ab?cd", function (req, res) {
  res.send("/ab?cd");
});
```

获取后端动态路由数据信息，在前端修改之后，通过req.params,`  console.dir(req.params);`

当我们在地址栏输入http://localhost:3000/profile/1/user/yeah时则可到相应的数据页面,1和yeah都是可以自定义的，只要有冒号的路由都是可以自定义的。

可以读取出路径中:id的值，路由的参数是动态的，冒号的表示是动态的

```js
//output
//console.dir 是输出一个对象所包含的内容
//console.log("req.params", req.params);
//和console.dir输出内容相同
console.dir(req.params)
{id:'1',name:'yeah'}

localhost:3000/profile/1/user/hd0300 
//output:{id:'1',name:'hd0300'}
```

2. 前端地址栏输入的动态路径参数

查询字符串，使用get请求时，它带有一个参数在地址栏当中，如何获取此参数,前端发送的请求的数据从req.query中获取

地址栏写localhost:3000?find=hot （find(参数名)，hot(值)

localhost的参数名find 要和 req.query.find 中的 find 参数名要对应即可,find和hot都可以自定义

```js
//地址栏写 localhost:3000?find=hot
app.get("/", function (req, res) {
  console.dir(req.query);
  //{ find: 'hot' }
  res.send("home page: " + req.query.find);
});
```

### app.post()

**数据获取**

```js
app.get("地址", function (request, response) {
  //request 前端给后台的请求
  //response 后台给前端的相应
  request.query; //前端发送的数据
  response.json({});
});


app.post("地址", function (req, res) {
  req.body; //前端发送的数据
});
```



#### 非文件上传等的数据请求

post请求的文件需要通过body-parser中间件进行解析，express需要安装和引入

Post的请求都需要使用中间件进行对请求的数据解析，urlencoded表示对urlencoded的文件的处理，因为我们post的是x-www-form-urlencoded格式，不同上传的方法用不同的方式进行解析

```js
var bodyParser = require('body-parser')
//因为要同时处理表单内容和json内容则需要将这两行解析写入

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))
// parse application/json
app.use(bodyParser.json())

app.post("/", function (req, res) {
  //后端打印数据
  console.dir(req.body);
  //给前端返回数据
  res.send(req.body.name);
});

//postman 亦可使用
app.get("/dynamicRoute", function (req, res) {
  console.dir(req.query);
  //localhost:3000/dynamicRoute?find=hot
  //{ find: 'hot' }
  res.send("dynamicRoute: " + req.query.find);
});
```

![E2D66BEFE427BAE47B547FBA238F1E76.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grdfr0rbcdj60z20cu3zp02.jpg)

**postman**

在不使用表单的情况下可以模拟各种请求。

body分为很多种，说明http协议对请求的提交格式是没有限制，二进制，字符串，json，都可以。提交不同数据进行的处理是不一样的。

正常的表单提交，不带文件上传的，用x-www-form-urlencoded格式，from-data 是可以上传文件的方式

raw的选项下选择json,或者body下选择x-www-form-urlencoded,form-data,进行文件上传

在x-www-form-urlencoded的解析格式下，我们需要填写key和value，形成对象进行数据传输。后端才好接收数据。

后端获取数据的方式`req.body.key`,key为你填写的变量名



![9856D0D80B5285A6653321DBE1F7A708.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grdfhpg805j610s0hwabn02.jpg)

#### 文件上传的数据请求

[Nodejs进阶：基于express+multer的文件上传](https://www.cnblogs.com/chyingp/p/express-multer-file-upload.html)

```html
    <!-- 上传文件要用post -->
    <form action="/upload" method="post" enctype="multipart/form-data">
      <!--nctype="multipart/form-data,表示用formdata处理数据，不是用常规的urlencoded处理-->
      <h2>单图上传</h2>
      <input type="file" name="logo" />
      <input type="submit" value="提交" />
    </form>
```

### express.Router()

有多个路由的话，最好分开为更多的文件，方便维护，专门放在一个路由文件中，routers

![D529D03D-5293-4FB8-8784-C1A5405949C3.png](http://ww1.sinaimg.cn/large/005NUwyggy1grfi10kt0zj621c0vqtgl02.jpg)

### res.sendFile(path)

请求和响应根目录,在响应中调用一个send方法，将数据信息响应给浏览器，匿名函数，中间件。express封装好了一些常用方法,send方法可以给浏览器前端发送字符串 this is the home page，也可以发送其他数据，json，对象等,可以返回字符串数组等等，查看官方api文档



requests with a file,<mark>Serve an HTML File</mark>

- will set the appropriate headers to instruct your browser on how to handle the file you want to send, according to its type. Then it will read and send the file. 
- This method needs an absolute file path. 
- Express evaluates routes from top to bottom, and executes the handler for the first match. You have to comment out the preceding solution, or the server will keep responding with a string.从上而下响应，必须清除之前的字符串，否则只响应字符串了。

```js
//Node global variable __dirname to calculate the path 
absolutePath = __dirname + relativePath/file.ext

//这样的操作会将.html文件通过中间件EXPRESS 显示在前端。
//Send the /views/index.html file as a response to GET requests to the / path.
app.get("/", function(req, res) {
  res.sendFile(__dirname + "/views/index.html");
});
```

![image-20201030145414704.png](http://ww1.sinaimg.cn/large/005NUwyggy1gkax953ogfj30hs0d9ab5.jpg)

If you have a website and want to serve an index.html file you probably want to put this in a public folder. This is to ensure the public doesn’t see something you dont want them to, and it sometimes is called “public” or “views,” but you can technically call it whatever you want.

- express.static(path) <mark>Serve Static Assets</mark> 中间件 middleware

  此处用于处理静态文件，一些图片或者CSS

  Basically, middleware are functions that intercept route handlers, adding some kind of information. 

  A middleware needs to be mounted using the method `app.use(path, middlewareFunction)`. The first `path` argument is optional. If you don’t pass it, the middleware will be executed for all requests.

```js
app.use(express.static(__dirname + "/public"));

//Mount the express.static() middleware for all requests with app.use(). The absolute path to the assets folder is __dirname + /public.
```

- <mark>Serve JSON on a Specific Route</mark>

  the preferred data format for moving information around the web is JSON,JSON is a convenient way to represent a JavaScript object as a string, so it can be easily transmitted.

```js
app.get("/json",function(req, res) {
  res.json({"message": "Hello json"});
})
```

res.json() : This method closes the request-response loop, returning the data.Behind the scenes, it converts a valid JavaScript object into a string, then sets the appropriate headers to tell your browser that you are serving JSON, and sends the data back. 

![image-20201030154849417.png](http://ww1.sinaimg.cn/large/005NUwyggy1gkax8ofluaj30d7043q34.jpg)

- <mark>.env File</mark>

  The `.env` file is a hidden file that is used to pass environment variables to your application. This file is secret, no one but you can access it, and it can be used to store data that you want to keep private or hidden. 记得先安装包之后，在app.js中引用，然后创建.env file

  - store API keys from external services

  - store your database URI.

  - store configuration options

- environment variable names
  - uppercase
  - words separated by an underscore
  - don’t need to wrap names or values in quotes (cuz The `.env` is a shell file)
  - cannot be space around the equals sign
  - e.g. VAR_NAME=value

```js
app.get("/json",function(req, res) {
  res.json({"message": "Hello json"});
})
```

```js
//didnt pass ans
app.get("/json", function(req, res) {
  //console.log(process.env.MESSAGE_STYLE);
  if (process.env.MESSAGE_STYLE === "uppercase") {
    res.json({ message: "HELLO JSON" });
  } else {
    res.json({ message: "Hello Json" });
  }
});
```

```js
//passed ans 神他妈有error..
app.get("/json", function(req, res) {
  if (process.env.MESSAGE_STYLE === "uppercase") {
    res.json({
      message: "HELLO JSON"
    });
  }
  res.json({
    message: "Hello json"
  });
});
```

- <mark>Middleware</mark>

  Middleware functions are functions that take 3 arguments: the request object, the response object, and the next function in the application’s request-response cycle. These functions execute some code that can have side effects on the app, and usually add information to the request or response objects. They can also end the cycle by sending a response when some condition is met. If they don’t send the response when they are done, they start the execution of the next function in the stack. This triggers calling the 3rd argument, `next()`.

  - app.METHOD(path, middlewareFunction)

    to mount a middleware function at root level, you can use the `app.use(<mware-function>)` method.if you want a function to be executed only for POST requests, you could use `app.post(<mware-function>)`. Analogous methods exist for all the HTTP verbs (GET, DELETE, PUT, …).
    
```js
function(req, res, next) {
  console.log("I'm a middleware...");
  next();
}
```

```js
//app.use(<mware-function>)

app.use((req, res, next) => {

 let string = `${req.method} ${req.path} - ${req.ip}`
 console.log(string) 
   
 next();
});

```

  - Chain middleware


```js
app.get('/user', function(req, res, next) {
  req.user = getTheUserSync();  // Hypothetical synchronous operation
  next();
}, function(req, res) {
  res.send(req.user);
});
```

```js
app.get('/now', function(req, res, next){
   req.time = new Date().toString();
   console.log(req.time)
  next();
},function(req,res){
  res.json({time:req.time})
})
```

## Get Route Parameter Input from the Client

get input from the client is by encoding the data after the route path,

用冒号自定义路径名称，并通过req.params.自定义名称，进行获取。没有前后位置之分。

```js
route_path: '/user/:userId/book/:bookId'
actual_request_URL: '/user/546/book/6754'
req.params: {userId: '546', bookId: '6754'}

app.get('/:word/echo', function(req,res){
  res.json({echo:req.params.word})
})

//https://boilerplate-express-2.xuheather.repl.co/freecodecamp/echo
//{"echo":"freecodecamp"}
```

## Get Query Parameter Input from the Client

The query string is delimited by a question mark (?), and includes field=value couples. Each couple is separated by an ampersand (&). 

{ name: 'firstname lastname'}

e.g. `?first=firstname&last=lastname`

https://boilerplate-express-2.xuheather.repl.co/name?first=546&last=6754

```js
route_path: '/library'
actual_request_URL: '/library?userId=546&bookId=6754'
req.query: {userId: '546', bookId: '6754'}

//与例子不同
app.get('/name', function(req,res){
  res.json({ name: `${req.query.firstname} ${req.query.lastname}`})
})
```

```js
//按照eg所写
app.get("/name", function(req, res) {
  var firstName = req.query.first;
  var lastName = req.query.last;
  // OR you can destructure and rename the keys
  var { first: firstName, last: lastName } = req.query;
  // Use template literals to form a formatted string
  res.json({
    name: `${firstName} ${lastName}`
  });
});
```

## Use body-parser to Parse POST Requests

[link from fcc](https://www.freecodecamp.org/learn/apis-and-microservices/basic-node-and-express/use-body-parser-to-parse-post-requests)

<mark>app.post()</mark>

POST is the default method used to send client data with HTML forms. POST is used to send data to create new items in the database (a new user, or a new blog post).

```js
app.use('/',bodyParser.urlencoded({extended: false}))
```

the raw content of an HTTP POST request

```js
POST /path/subpath HTTP/1.0
From: john@example.com
User-Agent: someBrowser/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 20
name=John+Doe&age=25
```

As usual, the middleware must be mounted before all the routes which need it.

**Note:** `extended=false` is a configuration option that tells the parser to use the classic encoding. When using it, values can be only strings or arrays. The extended version allows more data flexibility, but it is outmatched by JSON.

## Get Data from POST Requests

If the body-parser is configured correctly, you should find the parameters in the object `req.body`.

```js
route: POST '/library'
urlencoded_body: userId=546&bookId=6754
req.body: {userId: '546', bookId: '6754'}

app.post("/name", function(req, res) {
  var firstName = req.body.first;
  var lastName = req.body.last;
  // OR you can destructure and rename the keys
  var { first: firstName, last: lastName } = req.body;
  // Use template literals to form a formatted string
  res.json({
    name: `${firstName} ${lastName}`
  });
});
```

```js
app.use('/',bodyParser.urlencoded({extended: false}))
app.post("/name", function(req, res) {
  // Handle the data in the request
  var string = req.body.first + " " + req.body.last;
  res.json({ name: string });
});
```

Tip: There are several other http methods other than GET and POST. And by convention there is a correspondence between the http verb, and the operation you are going to execute on the server. The conventional mapping is:

POST (sometimes PUT) - Create a new resource using the information sent with the request,

GET - Read an existing resource without modifying it,

PUT or PATCH (sometimes POST) - Update a resource using the data sent,

DELETE => Delete a resource.

There are also a couple of other methods which are used to negotiate a connection with the server. Except from GET, all the other methods listed above can have a payload (i.e. the data into the request body). The body-parser middleware works with these methods as well.

*Authentication* Advanced Node and Express notes

The most common and easiest way to use authentication middleware for Node.js is [Passport](http://passportjs.org/).

template engines which allow for use of *Pug* and web sockets which allow for real time communication between all your clients and your server. 

### Template Engine

A template engine enables you to use static template files (such as those written in Pug) in your app. At runtime, the template engine replaces variables in a template file with actual values which can be supplied by your server. Then it transforms the template into a static HTML file that is sent to the client. This approach makes it easier to design an HTML page and allows for displaying variables on the page without needing to make an API call from the client.

One of the greatest features of using a template engine is being able to pass variables from the server to the template file before rendering it to HTML.

在渲染前进行数据交互，数据传输到服务端，通过template file 。

use a variable by referencing the variable name as `#{variable_name}` inline with other text on an element or by using an equal sign on the element without a space such as `p=variable_name` which assigns the variable's value to the p element's text.

## 4. middleware

### 1. Express-favicon

用户制作浏览器tab中的图标，使用的时候需要将图片转化成ico后缀的模式，在网上找相关的工具即可，并图片文件放在static指定的文件目录下

```js
//安装favicon
//npm install serve-favicon
//路径也要一起使用
var path = require("path");
var favicon = require("serve-favicon");

app.use(express.static("public"));
app.use(favicon("./public/favicon.ico"));
```

### 2. Express-session,passport

[Passport Local Configuration (Node + Passport + Express)](https://www.youtube.com/watch?v=xMEOT9J0IvI&list=PLYQSCk-qyTW2ewJ05f_GKHtTIzjynDgjK&index=5)

使用逻辑：用户登入成功后，session模块创建加密的用户数据，通过地址的形式(?)储存并将用户的数据通过cookie传送给前端，前端通过session加密方式后储存的内容查找用户信息。

we will use Express-session to handle sessions. Using this middleware saves the session id as a cookie in the client and allows us to access the session data using that id on the server. This way we keep personal account information out of the cookie used by the client to verify to our server they are authenticated and just keep the *key* to access the data stored on the server.

**the difference between session and cookie**

Basically,a session and a cookie are different in the place that their data is stored.cookie has its data stored inthe browser and that session stored the data in the server side.express seesion is going to store a little bit bigger types of data,so in a cookie you cannot put a whole lot of data.it would be tedious.with cookie,a hacker is easily get a whole of that imformation and steal personal data.

a session is used to store information about a paritcular user moving throughout the browser or a client.我们需要有一个存储的空间去存储我们的用户信息，session store implementation则用于放置用户的信息。

it would be useful to have an actual database storing that information, by default the express session middleware just come with its own implementaion of a session store and its not using a database.it's just using in memory or memory that's local to your application,and it's not going to be a scalable solution.

we know that the cookie in the browser has the session id and we use that session id to look up the session in the database or the session store

- 数据存储位置不同，cookie保存在浏览器中,session保存在后端
- session安全性更高

**session store implementation**

it deciding what persistent memory are we going to store our sessions

用户第一次浏览时，请求头中是没有cookie的，二次进入会自动创建。

![B7C7CF5A67AC11783AA53834C52CA377.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grfkr5hj0cj60p40gc75u02.jpg)

![3421371ADDD0E121067B114925831043.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grfkrnmdz6j61080fsac802.jpg)

![B0E93D7256224A4E05D6BC75D5959BAA.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgo60bfguj61dc0xagse02.jpg)

<mark>**操作逻辑**</mark>

1. 后端文件中引入session 模块

```js
const express = require("express");
var session = require("express-session");

const app = express();

app.use(express.static("public"));

var bodyParser = require("body-parser");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.set("trust proxy", 1); // trust first proxy
//session的配置要放在接口前面，server内容真的很注意顺序！！！！！
app.use(
  session({
    //密钥保存是根据secret+userinfo
    secret: "keyboard cat",
    //是否重新保存
    resave: true,
    //更新过期时间
    rolling: true,
    saveUninitialized: true,
    //设置过期时间 maxAge
    cookie: { maxAge: 60000 },
  })
);
```

2. 后端接口文件中将用户信息写入session中

```js
myRouter.get("/login", function (req, res) {
  //数据库内容
  var userInfo = {
    name: "heather",
    pwd: 123,
  };
  //直接获取数据存储在session中
  console.log("数据数据", req.session);
  obj = req.session;
  obj.user = userInfo;
  console.log("objusername", obj.user.name);
  console.log(req.query);
  if (
    obj.user.name == req.query.username &&
    obj.user.pwd == req.query.password
  ) {
    console.log("req.session", req.session);
    //   obj.user = JSON.stringify(userInfo);
    res.json({ error: 0, msg: "登录成功" });
  } else {
    res.json({ error: 1, msg: "注册失败" });
  }
});
```

3. 前端js文件中通过session判断用户，并设置权限

```js
$("#btn").click(function () {
  $.ajax({
    url: "/login",
    data: {
      username: $("#loginId").val(),
      password: $("#loginpwd").val(),
    },
    success: function (res) {
      //json解析后台返回的数据
      var json = res;
      console.log("jsonjsonjson", json);
      if (json.error == 1) {
        window.location.href = "./index.html";
        console.log("失败");
      } else {
        window.location.href = "./user.html";
        console.log("登入成功");
      }
    },
  });
});

```

要注意，在mysql中，后端需要将在数据库获得的数据设置成json解析字符串将数据进行传输，前端做相印的解析

![5BCB17B7D0B00E6F8C4288ACC3CA17D2.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgofmhnzwj60uk0gwjtq02.jpg)

![38CFFD07C2EA6E8D24982CE17D5312BF.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgogv7u6kj60pc0j276t02.jpg)

### 3. Express-multer

[Nodejs进阶：基于express+multer的文件上传](https://www.cnblogs.com/chyingp/p/express-multer-file-upload.html)

1. 创建form表单，表单中多加了enctype="multipart/form-data"这个属性，使得处理文件的方式不同，不会再使用一般默认的x-www-form-urlencoded解析方式对文件进行解析

   不同的文件上传的方式：[本页内容点击跳转](# req.post())

```html
<--！表单点击提交后会进入/upload路径中-->    
<form action="/upload" method="post" enctype="multipart/form-data">
      <!--nctype="multipart/form-data,表示用formdata处理数据，不是用常规的urlencoded处理-->
      <h2>单图上传</h2>
      <input type="file" name="logo" />
      <input type="submit" value="提交" />
    </form>
```

2. 引入fs module

```js
var fs = require("fs");
```

3. 创建表单路径页面

**`fs.readFile(path[, options], callback)`**

[readFile reflink](http://nodejs.cn/api/fs.html#fs_fs_readfile_path_options_callback)

用于读取文件内容，将文件内容返回到设定的路径中，这里会在form路径中显示出写好的html页面

```js
app.get("/form", function (req, res) {
  //读取文件内容
  var form = fs.readFileSync("./form.html", { encoding: "utf8" });
  res.send(form);
  //以上等同于res.sendFile(__dirname+'/form.html');
  // var person = req.params.name;
  // res.sendFile(__dirname + "/form.html");
  //传递动态的数据，比如变量，比如将person传递到html文件中，则需要用到模版引擎，将变量数据通过模板引擎放入html文件中，可以嵌入动态的数据
  //ejs模板引擎
});
```

4. 引入multer,设置文件保存路径

```js
//使用multer进行上传路径的指定，表示当前路径下的uploads这个目录
//上传之后才会创建这个uploads目录，并将上传的文件放到目录中
var multer = require("multer");
var upload = multer({ dest: "uploads/" });
```

![0C6D5FD7921CEFD56BE30708FE352606.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgpfzkgquj60c205sweu02.jpg)

5. 设置上传表单的name，获取对应表单的内容，到这一步即可测试上传文件功能，已可以上传成功

upload.single("logo"),表示上传单个文件

```js
//第一步中的表单页面中的input标签中的name

app.post("/upload", upload.single("logo"), function (req, res) {
  //logo是html文件的input的name,因为它要知道哪个文件的标签
  res.send({ ret_code: 0 });
});
```

6. 修改文件名

修改文件名时，引入说明文档中storage 中 diskstorage 的内容，并将第四步中的`var upload = multer({ dest: "uploads/" });`删除并替换成引入的内容

```js
//以下是官方文档的代码内容

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, '/tmp/my-uploads')
  },
  filename: function (req, file, cb) {
    cb(null, file.fieldname + '-' + Date.now())
  }
})
 
var upload = multer({ storage: storage })

//根据以上内容进行修改，使用以下内容，生成的文件名为input name属性+时间戳，即logo-1623572642270
//创建保存的目录

//如果目录存在则用"./upload/"目录，如果不存在则创建
var createFolder = function (folder) {
  try {
    fs.accessSync(folder);
  } catch (e) {
    fs.mkdirSync(folder);
  }
};

var uploadFolder = "./upload/";
createFolder(uploadFolder);

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadFolder);
  },
  filename: function (req, file, cb) {
    // 将保存文件名设置为 字段名 + 时间戳，比如 logo-1478521468943
    cb(null, file.fieldname + "-" + Date.now());
  },
});
// 通过 storage 选项来对 上传行为 进行定制化
var upload = multer({ storage: storage });
```

7. 自定义文件名

文档说明我们可以通过req.file获得文件所有信息内容

```js
app.post("/upload", upload.single("logo"), function (req, res) {
  //logo是html文件的input的name,因为它要知道哪个文件的标签
  console.log(req.file);
  res.send({ ret_code: 0 });
});


//storage里的部分里的文件名可以自己自定义
  filename: function (req, file, cb) {
    // 将保存文件名设置为 字段名 + 时间戳，比如 logo-1478521468943
    //file.fieldname改为originalname，可以设置成自定义的名字，看自己喜欢
    cb(null, file.originalname + "-" + Date.now());
  },
```

![5458E2FCF98D4077060948D4F48D76FC.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgpzcafk5j60q2096q4702.jpg)

![56E8E52D776585EAFA2AA834C72D99C0.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgq0peagej614q0m8tbs02.jpg)

8. 通过poatman上传文件

![A247EBDE0758EA8ED9A78A2EB0F5625E.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgq3qfaqsj61jm0oe41802.jpg)

![AEEA3CE6746203B015BA9648A5A7797F.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgq5l0g6mj61mu0j441802.jpg)

9. 多图上传

**方法一**：这里创建的两个input框，觉得不是很合适，应该一个框就可以实现多个图片上传的功能

```js
//servr.js
//修改upload single -> upload.array("logo", 2)
app.post("/upload", upload.array("logo", 2), function (req, res) {
  //logo是html文件的input的name,因为它要知道哪个文件的标签
  console.log(req.file);
  res.send({ ret_code: 0 });
});
```

```html
<form action="/upload" method="post" enctype="multipart/form-data">
      <!--nctype="multipart/form-data,表示用formdata处理数据，不是用常规的urlencoded处理-->
      <h2>多图片上传</h2>
      <input type="file" name="logo" />
      <input type="file" name="logo" />
      <input type="submit" value="提交" />
</form>
```

**方法二**：

```js
//servr.js
//修改upload single -> upload.array("logo", 2)
app.post("/upload", upload.array("logo", 2), function (req, res) {
  //logo是html文件的input的name,因为它要知道哪个文件的标签
  console.log(req.file);
  res.send({ ret_code: 0 });
});
```

```html
<form action="/upload" method="post" enctype="multipart/form-data">
      <!--nctype="multipart/form-data,表示用formdata处理数据，不是用常规的urlencoded处理-->
      <h2>多图片上传</h2>
      <input type="file" name="logo" multiple />
      <input type="submit" value="提交" />
</form>
```

注意点：

<mark>多个文件的时候从req.files获取文件内容,单个文件的时候从req.file获取文件内容</mark>

```js
app.post("/upload", upload.array("logo", 2), function (req, res) {
  //logo是html文件的input的name,因为它要知道哪个文件的标签
  //单个文件的时候从req.file获取文件内容
  //多个文件的时候从req.files获取文件内容
  // console.log(req.files);
  console.log(req.files);
  res.send({ ret_code: 0 });
});
```

### 4. Express-mysql

```js
var mysql = require('mysql')

var db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "web258",
  //确认端口，因为不确定每个数据库的端口都是3306,如果不是默认值则修改为数据库的端口值
  port: "3306"
});

db.query(sql, function (error, data) {
  //error 错误信息
  //data sql执行后的结果
});
```

### 5. Express-morgan

记录请求文件日志

```js
var morgan = require('morgan')
```

### 6. Express-ws(web-socket)

`npm install ws`

**http请求**
ajax请求 必须要前端先给后台发送一个消息，后台才能返回消息。有一些业务，比如说k线图。实时变化。ajax请求会非常多。还有比如聊天的业务。

**socket请求**
只要建立起联系。联系会一直保持通信的状态，联通的状态，后台可以直接推送消息。不用一次一次的访问。

前台有前台的socket,和后台也有后台的soket，服务器和服务器之间也会有socket，因为他们之间也要建立联系。

socket相当于重新创建了一个服务。ws服务 socket服务，不要和http相关的端口区别开，因为这是一个新的服务。必须写在http的下面，也就是文件最下面。

**使用逻辑**

前台：

1. 创建ws服务 `var socket = new WebSocket("ws://172.17.7.249:9999");`
2. 发送消息`socket.send(JSON.stringify(msg));`
3. 建立连接等待消息`socket.onopen`
4. 接收别人的消息`socket.onmessage`
5. 断开链接`socket.close();`

后台：

1. 创建服务`var server = new ws.Server({})`
2. 有人建立连接时`server.on("connection",function(ws){})`
3. 接收消息` ws.on("message", function (data) {}`
4. 发送消息`arr[i].send(data)`
5. 断开连接`ws.on("close", function () {}`

![FFD5D3A790361B07757970DAD5797D39.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgw7hq399j61uq0qmwk202.jpg)












