# hello-ajax

[课程地址](https://www.bilibili.com/video/BV1WC4y1b78y)

# 第一章： 原生Ajax

## 1. Ajax简介

- Ajax全称为Asynchronous Javascript And XML，即异步JS和XML
- 通过Ajax可以在浏览器中向服务器发送异步请求，最大的优势：==**无刷新获取数据**==
- AJAX不是新的编程语言，而是一种将现有的标准组合在一起使用的新方式

-

## 2. AJAX的优缺点

### AJAX的优点

1. 页面无刷新，局部请求，用户体验良好
2. 使用异步方式与服务器通信，具有更加迅速的响应能力
3. 以前一些服务器的工作可以转移到客户端，利用客户端闲置的能力来处理，减轻服务器和带宽的负担，节约空间和宽带租用成本。并且减轻服务器的负担，ajax的原则是“按需取数据”，可以最大程度的减少冗余请求，和响应对服务器造成的负担。

### AJAX 的缺点

1. ajax不支持浏览器back按钮，没有浏览历史，不能回退
2. 存在跨域问题（同源）
3. 对搜索引擎的支持比较弱，不利于SEO，SEO不友好（爬虫获取不到信息）
4. 安全问题 AJAX暴露了与服务器交互的细节
5. 不容易调试

## 3. Ajax 通过 XML 和 HTTP 发请求

- 传统的 web 应用程序会把数据提交到 web 服务器（使用 HTML 表单）。在 web 服务器把数据处理完毕之后，会向用户返回一张完整的新网页。
- 由于每当用户提交输入，服务器就会返回新网页，传统的 web 应用程序往往运行缓慢，且越来越不友好。
- **通过 Ajax，web 应用程序无需重载网页，就可以发送并取回数据。**完成这项工作，需要通过向服务器发送 HTTP 请求，并通过当服务器返回数据时使用 JavaScript 仅仅修改网页的某部分。
- 一般使用 JSON 作为接收服务器数据的格式。

### 1. XML

- XML 可扩展标记语言。
- XML 被设计用来传输和存储数据。
- XML 和 HTML 类似，不同的是 HTML 中都是预定义标签，而 XML 中没有预定义标签，全都是自定义标签，用来表示一些数据。
- 现在已被JSON取代

```html
// 比如说我有一个学生数据： 
// name = "孙悟空" ; age = 18 ; gender = "男" ; 
// 用 XML 表示： 
<student> 
  <name>孙悟空</name> 
	<age>18</age> 
	<gender>男</gender> 
</student>

// 现在已经被 JSON 取代了。
// 用 JSON 表示，可以通过json的方法将字符串转化为json格式，比较方便

{"name":"孙悟空","age":18,"gender":"男"}
```

### 2. HTTP协议

HTTP协议（HyperText Transfer Protocol，超文本传输协议）是用于从WWW服务器传输超文本到本地浏览器的传输协议。协议详细规定了浏览器和万维网服务器之间互相通信的规则

请求和响应都分别包括==行、头、空行、体==

#### 1. 请求报文

```
//(请求)行;分别为 请求方式 请求参数 Http协议版本：POST /s?ie=utf-8 HTTP/1.1
POST /s?ie=utf-8 HTTP/1.1
Get /s?ie=utf-8 HTTP/1.1

//(请求)头：都是键值对的表现方式
Host: atguigu.com
Cookie: name=guigu
Content-type: application/x-www-form-urlencoded
User-Agent: Chrome 83

//空行
//这里有个空行

//(请求)体
username=admin&password=admin
//get请求中，请求体必须为空
//post请求中，请求体可以不为空
```

#### 2. 响应报文

```html
//(响应)行
HTTP/1.1 200 ok // http协议版本 响应状态码 响应状态字符串

//(响应)头
Content-type: text/html; charset=utf-8
Content-length: 2048
Content-encoding: gzip

//空行
//这里有个空行

//(响应)体
<html>
 	<body>一些文本内容</body>
</html>
```

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7u6y945wkj31d810eqkn.jpg" alt="image.png" style="zoom: 33%;" />

## 4. Ajax对象的创建过程示例

1. 创建连接,准备一个ajax
2. 连接服务器,通过ajax和后台创建联系
3. 发送请求，通过ajax发送数据
4. 接受请求，通过ajax接收请求

```js
// 1. 创建连接,准备一个ajax
var xhr = null;
xhr = new XMLHttpRequest();
// new 出来 xml格式的http的数据请求
// 2. 连接服务器,通过ajax和后台创建联系
// 请求的方式,请求路径，是否异步
xhr.open("get", "/login", true);
// 3. 发送请求，通过ajax发送数据
xhr.send(null);
// 4. 接受请求，通过ajax接收请求
// onreadystatechange当状态改变的时候
xhr.onreadystatechange = function () {
  // 查看所有的状态，2，3，4，
  console.log(xhr.readyState);
  // 判断数据是否全部被接收
  if (xhr.readyState == 4) {
    // 判断网络请求是否通过。判断http状态码，2开头是成功，304重定向，重复请求 也是成功，3，4开头一般是前端问题，5，6开头一般是后台问题
    if ((xhr.status == 200 && xhr.status < 300) || xhr.status == 304) {
      success(xhr.responseText);
      console.log(xhr.responseText);
    } else {
      // fail fail && fail(xhr.status);
    }
  }
};
```

**ajax的xhr.readyState状态**

- 0：ajax创建，未初始化，尚未调用open()方法
- 1：ajax和后台建立联系。启动。已调用open()方法，但尚未调用send()方法
- 2：ajax发送数据。发送。已调用send()方法，但尚未接收到响应。
- 3：ajax接收数据（未解析的数据）已接收到部分响应数据
- 4：ajax接收数据（完全接受数据）已接收到全部响应数据，而且可以在客户端使用

## 5. Ajax的注意事项

1. ajax必须运行在服务器环境上

2. 获取的数据都是字符串，可以通过设置，设置成json格式

3. 前端、后台、数据库三个编码统一，设置成utf-8，不然会乱码

4. get有缓存,数据会放在请求头里,post在请求体里发送。一个请求包裹请求体和请求，如何解决不缓存数据，方法是添加缓存因子

   `aaa=1&bbb=2&t=Math.random();`
   t即为缓存因子
   t=Math.random()
   t=new Date().getTime()
   t=Math.random()+new Date().getTime()
   t=编译后的哈希值

<img src="http://ww1.sinaimg.cn/large/005NUwyggy1grtqojwk2lj60ss0ccabi02.jpg" alt="09D5D34921E78A97C4CE88747E876D4F.jpg" style="zoom:50%;" />

5. ajax不关心文件的后缀名

   ajax分为请求接口、请求文件内容。一般在公司请求文件会看到3种
   ` .data` 、`.json` (具有文件格式) 、 `.一堆hash值乱码`

6. ajax不能跨域

   1. 为了安全，前端的内容里面 html是可以跨域的
      - link  cdn
      - script标签  cdn
      - img
   2. js有同源策略，协议 + ip地址 + 端口号有一个不相同都是跨域

## 6. get和post区别

1. get数据在地址栏，post不是。post的数据在请求体里面
2. get请求的数据根据浏览器不同32k左右。post理论上不限。有些做限制1g，上传文件、图片都用post
3. get请求有缓存(cache)，post没有,  浏览器对于相同的地址+参数，只访问一遍。

# 第二章：跨域

## 1. 同源策略

同源策略（Same-Origin Policy）最早由 Netscape 公司提出，是浏览器的一种安全策略。

==同源：协议、域名、端口号必须完全相同。不来自同一个服务则是不同源。==

==违背同源策略就是跨域==

a.com 向 b.com发请求则是域名不同

## 2. 如何解决跨域

### 1. JSONP

1. JSONP是什么

   JSONP (JSON with Padding)

   本质和ajax没有任何关系,本质是html的非同源策略和函数的传参。动态创建script标签，在本地准备全局函数，用来接收引过来的调用传的值，是一个非官方的跨域解决方案，纯粹凭借程序员的聪明才智开发出来，==只支持get请求==

2. JSONP 怎么工作的？

   在网页有一些标签天生具有跨域能力，比如：img, link, iframe, script

   JSONP就是利用**`script`**标签的跨域能力来发送请求的

3. JSONP的使用

   - 动态的创建一个script标签

   ```
   var script = document.createElement("script");
   ```

   - 设置script的src，设置回调函数

   ```js
   script.src = "http://locallhost:3000/textAJAX?callback=abc"
   ```

### 3. CORS

1. CORS是什么？

   CORS (Cross-Origin Resource Sharing), 跨域资源共享。CORS 是==官方==的跨域解决方案，它的特点是不需要在客户端做任何特殊的操作，完全**在服务器中进行处理**，支持 get 和 post 等多种请求。跨域资源共享标准新增了一组 HTTP首部字段（响应头），允许服务器声明哪些源站通过浏览器有权限访问哪些资源。

2. CORS怎么工作的？

   CORS 是通过设置一个响应头来告诉浏览器，该请求允许跨域，浏览器收到该响应以后就会对响应放行。

3. CORS 的使用

   主要是服务端的设置
   
   ```js
   app.all("/cors-server", (request, response) => {
     //设置响应头
     response.setHeader("Access-Control-Allow-Origin", "*");
     response.setHeader("Access-Control-Allow-Headers", "*");
     response.setHeader("Access-Control-Allow-Method", "*");
     // response.setHeader("Access-Control-Allow-Origin", "http://127.0.0.1:5500");
   
     response.send("hello CORS");
   });
   ```

# 推荐阅读

- [ruanyifeng blog](http://www.ruanyifeng.com/blog/2016/04/cors.html)
- [mozilla CORS](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)
- [Ajax 简介](https://www.ibm.com/developerworks/cn/web/wa-aj-ajaxhistory/index.html)
- [Ajax-MDN](https://developer.mozilla.org/zh-CN/docs/Web/Guide/AJAX)
- [Ajax总结篇](https://www.jianshu.com/p/c94e49772123)
- [Javascript异步编程的4种方法](http://www.ruanyifeng.com/blog/2012/12/asynchronous%EF%BC%BFjavascript.html)
