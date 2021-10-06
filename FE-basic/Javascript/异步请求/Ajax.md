# [重点] AJAX

## 学习目标

- 理解Ajax的使用场景
- 掌握Ajax对象的创建过程和使用方法

## 学习内容

### 1. AJAX介绍

- Ajax 是 Asynchronous JavaScript And XML 的首字母缩写。Ajax并不是一种新的编程语言，而仅仅是一种新的技术，它可以创建更好、更快且交互性更强的 web 应用程序。Ajax 使用 JavaScript 在 **web 浏览器与 web 服务器之间来发送和接收数据**。通过与 web 服务器交换数据，而不是每当用户作出改变时重载整个 web 页面，Ajax 技术可以使网页更迅速地响应。<mark>最大的优势：**无刷新获取数据。**</mark>

### 2. AJAX特点

**AJAX** **的优点** 

1. 可以无需刷新页面而与服务器端进行通信。 

2. 允许你根据用户事件来更新部分页面内容。 

**AJAX** **的缺点** 

1. 没有浏览历史，不能回退 

2. 存在跨域问题(同源) 

3. SEO 不友好

### 3. Ajax 使用 XML 和 HTTP 请求

- 传统的 web 应用程序会把数据提交到 web 服务器（使用 HTML 表单）。在 web 服务器把数据处理完毕之后，会向用户返回一张完整的新网页。
- 由于每当用户提交输入，服务器就会返回新网页，传统的 web 应用程序往往运行缓慢，且越来越不友好。
- **通过 Ajax，web 应用程序无需重载网页，就可以发送并取回数据。**完成这项工作，需要通过向服务器发送 HTTP 请求，并通过当服务器返回数据时使用 JavaScript 仅仅修改网页的某部分。
- 一般使用 JSON 作为接收服务器数据的格式。

### 4. XML 介绍

XML 可扩展标记语言。 

XML 被设计用来传输和存储数据。 

XML 和 HTML 类似，不同的是 HTML 中都是预定义标签，而 XML 中没有预定义标签， 

全都是自定义标签，用来表示一些数据。

```xml
//比如说我有一个学生数据： 
//name = "孙悟空" ; age = 18 ; gender = "男" ; 
//用 XML 表示： 
<student> 
  <name>孙悟空</name> 
	<age>18</age> 
	<gender>男</gender> 
</student>

//现在已经被 JSON 取代了。
//用 JSON 表示，可以通过json的方法将字符串转化为json格式，比较方便

{"name":"孙悟空","age":18,"gender":"男"}
```

### 5. HTTP协议

#### 介绍

HTTP协议（HyperText Transfer Protocol，超文本传输协议）是用于从WWW服务器传输超文本到本地浏览器的传输协议。

#### 1. 请求报文

```js
//(请求)行
POST /s?ie=utf-8 HTTP/1.1 //请求方式 请求参数 Http协议版本
Get /s?ie=utf-8 HTTP/1.1

//(请求)头
Host: atguigu.com
Cookie: name=guigu
Content-type: application/x-www-form-urlencoded
User-Agent:Chrome 83

//空行
//这里有个空行

//(请求)体
username=admin&password=admin
//get请求中，请求体必须为空
//post请求中，请求体可以不为空
```

#### 2. 响应报文

```js
//(响应)行
HTTP/1.1 200 ok // http协议版本 响应状态码 响应状态字符串

//(响应)头
Content-type: text/html;charset=utf-8
Content-length:2048
Content-encoding:gzip

//空行
//这里有个空行

//(响应)体
<html>
 	<body>一些文本内容</body>
</html>
```

### . Ajax对象的创建过程示例：

1. 创建连接,准备一个ajax
2. 连接服务器,通过ajax和后台创建联系
3. 发送请求，通过ajax发送数据
4. 接受请求，通过ajax接收请求

```js
  // 1. 创建连接,准备一个ajax
  var xhr = null; 
  xhr = new XMLHttpRequest() 
			//new 出来 xml格式的http的数据请求
  // 2. 连接服务器,通过ajax和后台创建联系
			//请求的方式,请求路径，是否异步
  xhr.open('get', '/login', true) 
  // 3. 发送请求，通过ajax发送数据
  xhr.send(null); 
  // 4. 接受请求，通过ajax接收请求
			//onreadystatechange当状态改变的时候
  xhr.onreadystatechange = function(){ 
    //查看所有的状态，2，3，4，
    console.log(xhr.readyState);
    //判断数据是否全部被接收
    if(xhr.readyState == 4){ 
      //判断网络请求是否通过。判断http状态码，2开头是成功，304重定向，重复请求 也是成功，3，4开头一般是前端问题，5，6开头一般是后台问题
      if(xhr.status == 200 && xhr.status<300 || xhr.status==304){ 
        success(xhr.responseText); 
        console.log(xhr.responseText)
      } else { 
      // fail fail && fail(xhr.status); 
      } 
    } 
  }
```

### ajax的xhr.readyState状态

console.log(xhr.readyState);

- 0，ajax创建，未初始化，尚未调用open()方法
- 1，ajax和后台建立联系。启动。已调用open()方法，但尚未调用send()方法
- 2，ajax发送数据。发送。已调用send()方法，但尚未接收到响应。
- 3，ajax接收数据（未解析的数据）已接收到部分响应数据
- 4，ajax接收数据（完全接受数据）已接收到全部响应数据，而且可以在客户端使用

- Ajax的优点

  - 页面无刷新，局部请求，用户体验良好
  - 使用异步方式与服务器通信，具有更加迅速的响应能力
  - 以前一些服务器的工作可以转移到客户端，利用客户端闲置的能力来处理，减轻服务器和带宽的负担，节约空间和宽带租用成本。并且减轻服务器的负担，ajax的原则是“按需取数据”，可以最大程度的减少冗余请求，和响应对服务器造成的负担。

- Ajax的缺点

  - ajax不支持浏览器back按钮
  - 安全问题 AJAX暴露了与服务器交互的细节
  - 对搜索引擎的支持比较弱，不利于SEO
  - 不容易调试


## ajax的注意事项

  1. ajax必须运行在服务器环境上

  2. 获取的数据都是字符串，可以通过设置，设置成json格式

  3. 前端、后台、数据库三个编码统一，设置成utf-8，不然会乱码

  4. get有缓存,数据会放在请求头里,post在请求体里发送。一个请求包裹请求体和请求头
           如何解决不缓存数据，方法是添加缓存因子
         
           aaa=1&bbb=2&t=(随机数)->即为缓存因子
                     t=Math.random()
                     t=new Date().getTime()
                     t=Math.random()+new Date().getTime()
          t=编译后的哈希值
         
           ![09D5D34921E78A97C4CE88747E876D4F.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grtqojwk2lj60ss0ccabi02.jpg)
         
  5. ajax不关心文件的后缀名
          ajax分为请求接口、请求文件内容。
          一般在公司请求文件会看到3种
              .data
              .json  具有文件格式
              .一堆hash值乱码

  6. ajax不能跨域
        为了安全,前端的内容里面 html是可以跨域的
                  link  cdn
                  script标签  cdn
                  img 
              js有同源策略
                  协议 + ip地址 + 端口号有一个不相同都是跨域

## get和post区别
1. get数据在地址栏，post不是。post的数据在请求体里面
2. get请求的数据根据浏览器不同32k左右。post理论上不限。有些做限制1g,上传文件、图片都用post
3. get请求有缓存(cache)，post没有,  浏览器对于相同的地址+参数。只访问一遍

 ## 如何解决跨域

1. jsonp  前端和后台都配合 ,一般用在企业，公布出来的第三方接口
2. 代理    只需要前端
3. CROS   只需要后台

  ### jsonp

本质和ajax没有任何关系

本质是html的非同源策略和函数的传参。动态创建script标签，在本地准备全局函数，用来接收引过来的调用传的值。

` 百度：https://www.baidu.com/sugrec?ie=utf-8&prod=pc&from=pc_web&wd=篮球&cb=show`

```html
<script>
  //jsonp.js
  //动态创建script标签,在本地准备全局函数
function show(a){alert(a)}
</script>
<!--用接收引过来的函数，调用传的值-->
<script src="show.js"></script>
```

```js
//show.js
show(1);
```

## 推荐资料(扩展学习)

- [Ajax 简介](https://www.ibm.com/developerworks/cn/web/wa-aj-ajaxhistory/index.html)
- [Ajax-MDN](https://developer.mozilla.org/zh-CN/docs/Web/Guide/AJAX)
- [Ajax总结篇](https://www.jianshu.com/p/c94e49772123)
- [Javascript异步编程的4种方法](http://www.ruanyifeng.com/blog/2012/12/asynchronous%EF%BC%BFjavascript.html)

[原生ajax函数封装](https://codepen.io/linhaishe/pen/oNZadqJ?editors=0010)

[学习笔记-异步的处理之promise对象](/Users/xusumu/OneDrive/1.notes/2.FE/Javascript/GXA-JS高级.md)

