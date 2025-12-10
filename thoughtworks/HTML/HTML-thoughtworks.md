# chapter 1. 初识计算机网络

## 学习目标

- 了解客户端和服务端
- 了解IP地址
- 了解域名
- 了解协议
- 了解URL

## 学习内容

### 一、什么是互联网？

- 想象一下全世界的道路是如何相互连接起来的：各个小街道连接到城市的道路，然后连接到各省道国道，然后与国家和国际的公路相融合。通过这些道路交通网我们可以开车从自己家到世界上的任何其他地方。并且你会发现这个道路交通网是没有实际的中心的。

- 互联网也是与此相似的。只是不是道路交通网，而是电缆联结的网络；不是从一家连通到另一家，而是从一台电脑到另一台电脑。且在互联网上穿梭的不是汽车，而是各式各样的信息。

- 互联网是在1969年发明的，当时旨在连接美国各地的电脑。 到了如今，数十亿台设备（包括个人电脑，笔记本电脑，手机，电视机，冰箱......）彼此之间通过互联网相互关联。

### 二、什么是客户端和服务端？

- 通常互联网上的通讯是在两台计算机之间进行：
- 拥有数据信息的一端通常被称为服务端；
- 想要获取数据信息的一段通常被称为客户端。
- 客户端可以以不同的形式存在，比如：
- 一款Web浏览器（IE、Edge、Chrome）
- 一个电子邮件客户端（Foxmail、Outlook）
- 一款社交应用程序（微信）
- 以上这些程序都会从服务端中获取数据信息（网站、邮件、消息），虽然有时客户端也会向服务端发送一些信息，但是通常客户端不会存储这些信息，而服务端却可以存储数据信息。
- 服务端通常是一台始终连接到互联网的专用计算机，其唯一的目的就是提供数据信息。
- 虽然任何连接到互联网的设备可能同时是客户端和服务端，但我们使用的大多数设备都被视为客户端，因为我们通常只获取数据，而不存储任何数据。

### 三、什么是IP地址？

- 就像每个房子都有一个特定的、唯一的门牌号一样，每一台连接到互联网的计算机都会被赋予一个特定的IP地址，以便在整个互联网上进行识别。

- IPv4地址通常由32位组成（它们通常写成四个范围在0~255以内，由点分隔的数字组成，(比如：`121.23.199.146`)。

- IPv6地址通常是由128位组成，通常写成八组由冒号分隔的四个十六进制数(比如：`2027:0da8:8b73:0000:0000:8a2e:0370:1337`)

### 四、什么是域名？

- 任何连上互联网的电脑都可以通过一个公共IP地址访问到， 对于IPv4/IPv6来说，计算机可以很容易地处理这些IP地址, 但是对一个人来说很难找出谁在操控这些服务器以及这些网站提供什么服务, IP 地址很难记忆而且可能会随着时间的推移发生改变。

- 为了解决上述问题，于是在1985年发明了域名，将 `121.23.199.146` 之类的纯数字IP地址与 `baidu.com` 等一系列文本关联起来。因此，两者都是可以互换的：可以通过访问`https://121.23.199.146` 或 `https://baidu.com` 最终都将进入完全相同的网站。

- 一个域名通常有三部分组成，从右向左依次为：
  1. 顶级域名：包含通用域名（`.com，.org，.net`）还有国家特定域名（`.cn，.us，.nl，.fr`）。
  2. 域名：像 baidu 这样的名称，可以包含字母，数字，但不包含空格或点。
  3. 子域名（可选）：虽然子域名是可选的，但大多数网站都会使用 `www` 作为默认子域。有时还可以用子域名标识该网页的内容，如 `image.baidu.com` 就是百度图片的域名。

- 域名也可以被视为是一种计算机的命名，在对计算机命名后再连接到互联网，方便用户访问。

### 五、什么是协议？

- 在互联网上使各个计算机相互连接的目的也是使各计算机能够彼此交流通信。就像人类使用不同的语言进行交流一样，在互联网中，使用不同的协议进行沟通。

- 且不同的协议都有其不同的目的：

  | 议名 | 用途         | 发明时间 |
  | ---- | ------------ | -------- |
  | TP   | 文件传输     | 1971     |
  | SMTP | 发送邮件     | 1971     |
  | IMAP | 接收邮件     | 1986     |
  | RC   | 聊天         | 1988     |
  | TTP  | 浏览网页内容 | 1989     |

### 六、什么是URL？

- 到目前为止，我们已经介绍了域名和计算机网络协议，现在我们就可以构建一个URL（统一资源定位符）了。
- 例如：百度的URL是 https://www.baidu.com/index.html, 该URL可以分为3部分：
- https:// 是协议
- www.baidu.com 是域名
- /index.html 是路径名
- 每一个URL都是唯一的，它定义了我们应该该以何种协议读取它(https://)，从哪里读取它(www.baidu.com/index.html)。
- URL有时可能看起来更加复杂，至于更复杂的内容是什么，我们在之后的学习中也将会继续学习和了解。

### 七、什么是http协议

在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP，<mark>HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。</mark>    是一种无状态的协议。他不会识别到底是谁给服务器发送的消息。

![C08543BA8A8BA9459202D224175CE61B.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grcd16vytkj61d013mant02.jpg)

![9B8B23A373CA10A0883037632D448458.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grcdiqsb7cj60yw0gan0o02.jpg)

### HTTP请求步骤

步骤1：浏览器首先向服务器发送HTTP请求

步骤2：服务器向浏览器返回HTTP响应。

步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

### http响应码、状态码

响应代码：`200`表示成功，`3xx`表示重定向，`4xx`表示客户端发送的请求有错误，`5xx`表示服务器端处理时发生了错误；

### 两种 HTTP 请求方法：GET 和 POST

在客户机和服务器之间进行请求-响应时，两种最常被用到的方法是：GET 和 POST。

- **GET** - 从指定的资源请求数据。
- **POST** - 向指定的资源提交要被处理的数据。

```js
    $('#loginBtn').click(function(){
        $.ajax({
            url:'/login',
            data:{
                username:$('#loginUser').val(),
                password:$('#loginPass').val()
            },
            success:function(res){
                console.log(res);
            }
        })
    })

    $('#registerBtn').click(function(){
        $.ajax({
            url:'/register',
            type:'post',
            data:{
                username:$('#registerUser').val(),
                password:$('#registerPass').val()
            },
            success:function(res){
                console.log(res);
            }
        })
    })
```

<mark>用户提交的数据，get会从request.query中获取</mark>

```js
app.get('/login',function(request,response){
    //request 前端给后台发送的东西
    //response 后台给前端返回的东西
    console.log('someone login',request.query)
  	//out put someone login { username: '123', password: '123' }
  
  	//	不链接数据库的用法
  
    // if(request.query.username=='aaa' && request.query.password=='111'){
    //     response.json({error:0,msg:'登录成功'})
    // }else{
    //     response.json({error:1,msg:'登录失败'})
    // }
  
  //链接数据库
    var sql='select * from user where username="'+request.query.username+'" and password="'+request.query.password+'"';

    db.query(sql,function(err,data){
        console.log(err,data);
        if(!err){
            if(data.length){
              //响应给前端的数据会使用json方式传输，用json语句解析出来
                response.json({error:0,msg:'登录成功'})
            }else{
                response.json({error:1,msg:'登录失败'})
            }
        }
    })
})



//post的使用
//node js 中path 的数据解析需要通过bodyparser
//post的内容从body parser解析后获取，所以要先下载bodyparser中间件，最后从req.body中获取
app.post('/register',function(request,response){
    //console.log('有人注册了',req.query,req.body)
    if(request.body.username=='aaa' && request.body.password=='111'){
        response.json({error:0,msg:'注册成功'})
    }else{
        response.json({error:1,msg:'注册失败'})
    }
})
```

## 资源推荐(扩展学习)

- [互联网协议入门（一）](http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html)
- [互联网协议入门（二）](http://www.ruanyifeng.com/blog/2012/06/internet_protocol_suite_part_ii.html)
- [廖雪峰http协议简介](https://www.liaoxuefeng.com/wiki/1016959663602400/1017804782304672)
- [HTTP 协议入门](http://www.ruanyifeng.com/blog/2016/08/http.html)
- [alibaba http](https://hit-alibaba.github.io/interview/basic/network/HTTP.html)

application/x-www-form-urlencoded

# chapter 2. 认识www

## 学习目标

- 了解Web

- 了解网页

- 了解网站

## 学习内容

#### 什么是Web？

- Web（`World Wide Web`缩写称为`www`）即全球广域网，也称为万维网，它是一种基于超文本和HTTP的、全球性的、动态交互的、跨平台的分布式图形信息系统。是建立在Internet上的一种网络服务，为浏览者在Internet上查找和浏览信息提供了图形化的、易于访问的直观界面，其中的文档及超级链接将Internet上的信息节点组织成一个互为关联的网状结构。

- 我们已经知道了各个计算机通过互联网连接在一起，且不同的计算机之间通过不同的语言（协议）进行通信，以此来交换文件、邮件、聊天消息等。

- HTTP就是其中的一种网络协议， 该协议也是计算机彼此之间分享网页的协议，就像你现在正在阅读的网页一样。

- Web就是互联网的一部分，在Web中各个网页彼此分享，如果你在浏览器中输入的URL以http:// 或 https:// 开头，那么你也正在告诉浏览器你正在浏览Web。

#### 什么是网页？

- 网页是一种用HTML编写的文档，网页可以在网络上被彼此分享。

- 可以使用浏览器打开网页。

- 可以通过以下方法浏览网页：
  - 在浏览器地址栏中输入网址：如 [http://baidu.com](http://baidu.com/);
  - 点击一个链接，比如：[这个链接](http://baidu.com/)；

- 若是所有的网页都需要通过URL来访问会变得十分麻烦，因为我们要记住所有的URL。所以Web的起源就是基于相互关联的HTML文档，通过文档内部的跳转以浏览不同的文档，以方便用户浏览Web。

#### 什么是网站？

- 网站只是位于同一个域名中的所有网页集合。比如：
  - Web → https://
    - 网站 → baidu.com
      - 网页 → /index.html
      - 网页 → /about.html
      - 网页 → /setting.html

- 在浏览器中打开 [http://b](http://baidu.com/)[aidu.com](http://baidu.com/)

- 在浏览器地址栏中输入：http://baidu.com/index.html ，这意味着你需要从互联网中获取到 index.html 页面的内容。在这种情况下，你的浏览器就是客户端，你需要向百度服务器获取到名为 index.html的文件。大致经历了如下过程：

| 客户端：你的浏览器 | Hi，百度服务器，请向我返回 index.html 的页面 |
| ------------------ | -------------------------------------------- |
| 服务器：百度服务器 | 好的，我来检查一下是否有这个网页...          |
| 客户端：你的浏览器 | ok，我会一直等着...                          |
| 服务器：百度浏览器 | 噢，找到了，我把index.html 发送给你          |
| 客户端：你的浏览器 | 好的，收到                                   |

- 之后，你的浏览器就会展示 index.html 的内容。
- 这个文件也不会保存在你的电脑上，你只是暂时的浏览该网页。如果你稍后又访问了 http://baidu.com/about.html 它会再通过上面的过程向百度服务器请求about.html 文件。这样通过每一次的请求，可以保证浏览器中展示的总是最新的从服务器中返回的数据。

# chapter 3. 认识浏览器

## 学习目标

- 了解浏览器的功能

## 学习内容

> 网页浏览器（英语：web browser），常被简称为浏览器，是一种用于检索并展示万维网信息资源的应用程序。这些信息资源可为网页、图片、影音或其他内容，它们由统一资源标志符标志。信息资源中的超链接可使用户方便地浏览相关信息。 网页浏览器虽然主要用于使用万维网，但也可用于获取专用网络中网页服务器之信息或文件系统内之文件。 主流网页浏览器有Mozilla Firefox、Internet Explorer、Microsoft Edge、Google Chrome、Opera及Safari。

- 浏览器可以看做是一个文档查看器，这里的文档指的就是网页。
- 你现在就正在使用浏览器来阅读用HTML编写的网页。
- 我们通过浏览器可以访问网页并使用网络应用。
- HTML文档
  - 网页就是HTML文档，就像电脑上的其他文件一样。它们只是.html 扩展名的文本文件。
  - 在我们的电脑中，我们可能有不同类型的文件：
    - .jpg 是图片
    - .mp3 是音乐文件
    - .avi 是音乐文件
    - .doc 是Word文档
    - .xls 是Excel文档

- 所有的这些类型的文件都可以通过指定的程序打开。其中一些程序只能打开文件，而还有一些程序则不仅可以打开文件还可以创建和修改文件。例如：
  - 网易云音乐 可以打开 .mp3格式的音乐文件；
  - Microsoft Word则不仅可以打开.doc格式的文档，还可以新建doc文档或编辑doc文档；
  - PotPlayer则可以打开avi格式的视频文件。

- 用于打开HTML文档的程序就是浏览器，如 IE 或 Chrome。 用于创建HTML文档的程序是文本编辑器，如VSCode或SublimeText。

- 几款常见的浏览器：

  ![浏览器.png](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1547806020968-fe3470fa-c126-4950-ae3f-5b85d8b5c32c.png)

## 资源推荐(扩展学习)

- [浏览器 —— 百度百科](https://baike.baidu.com/item/浏览器)

# chapter 4. 初识HTML

## 学习目标

- 宏观了解HTML
- 掌握HTML中标签的组成
- 掌握HTML标签中常用的标签属性

## 学习内容

#### 什么是 HTML？

HTML用于告诉浏览器如何构造你访问的网页，使用标签来描述内容和结构。是为了创建网页而设计的语言。

- HTML 指的是超文本标记语言 (Hyper Text Markup Language)
- HTML 不是一种编程语言，而是一种标记语言 (markup language)
- 标记语言是一套标记标签 (markup tag)
- HTML 使用标记标签来描述网页

#### HTML 标签

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由尖括号包围的关键词，比如 <html>
- HTML 标签通常是成对出现的，比如 <b> 和 </b>
- 标签对中的第一个标签是开始标签，第二个标签是结束标签
- 开始和结束标签也被称为开放标签和闭合标签

#### HTML 属性

- HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
- 属性总是以名称/值对的形式出现，比如：name="value"。
- 属性总是在 HTML 元素的开始标签中规定。
- 属性实例： HTML 链接由 <a> 标签定义。链接的地址在 href 属性中指定：

```html
<a href="http://www.w3school.com.cn">This is a link</a>
```

#### HTML 文档 = 网页

- HTML 文档描述网页
- HTML 文档包含 HTML 标签和纯文本
- HTML 文档也被称为网页

#### HTML中的基本语法

- 标签不区分大小写，推荐小写
- 空标签可以不闭合，比如 input、meta
- 属性不必引号，推荐双引号
- 某些属性值可以省略，比如 required、readonly

#### 一个HTML文件

- 一个简单的HTML文件是这样的：

```html
<html>
<head>
  <title>Hello, Html!</title>
</head>

<body>
  <p>Hello, World!</p>
</body>

</html>
```

可以看到HTML是由成对的标签构成的。比如`<p>`和`</p>`、`<body>`和</body>`。HTML文件的所有内容都应包含在<html>标签之中，<head>中的内容用来描述当前文件，<body>中的内容则被显示在页面上。

- 将上述内容保存为`index.html`文件，并用浏览器打开：![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548045784773-270d3ff4-35bf-4d94-8f7b-62fef099649b.png)`<title>`中的内容显示在了标题栏中，而`<p>`（passage，段落标签）之间的内容显示在了页面上

#### 一个基本的HTML标签如下：

- 标签

  ```html
  <p>Hello world</p> 
  ```

  中共包含如下内容：

  1. 开始标签（Opening tag）：包括元素的名称（<p>），包裹在开始和结束尖括号中。这表示元素开始或开始生效 - 在这种情况下，表示了一个段落的开头。
  2. 结束标签（Closing tag）：这与开始标记相同，除了它在元素名称之前包含正斜杠（</p>）。这表示元素结束的位置 - 在这种情况下，表示了一个段落的结尾. 没有包含结束标记是一个常见的初学者错误，并可能导致奇怪的结果。
  3. 内容（Content）：这是元素的内容，在这种情况下只是文本。
  4. 元素（Element）：开始标记，加结束标记，加内容，等于元素。

- 在HTML的标签中，也可以互相嵌套，把一个元素放在另一个元素的内部。例如：如果我们想要加粗World，就可以这样：

  ```html
  <p>Hello, <strong>World</strong></p>
  ```

  1. 我们需要确保元素被正确的嵌套：在上面的例子中我们先打开<p>元素，然后才打开<strong>元素，因此必须先将<strong>元素关闭，然后再去关闭<p>元素。
  2. 这样写就是错误的：`<p>Hello, <strong>World</p></strong>`
  3. 所有的元素都需要正确的打开和关闭，这样才能按你所想的方式展现。如果像上述的例子一样进行了错误的嵌套，那么浏览器会去猜测你想要表达的意思，但很有可能会得出错误的结果。

- 在HTML中有两种你需要知道的重要元素类别，块级元素和内联元素。
  1. 块级元素在页面中以块的形式展现 —— 相对与其前面的内容它会出现在新的一行，其后的内容也会被挤到下一行展现。块级元素通常用于展示页面上结构化的内容，例如段落、列表、导航菜单、页脚等等。一个以block形式展现的块级元素不会被嵌套进内联元素中，但可以嵌套在其它块级元素中。
  2. 内联元素通常出现在块级元素中并包裹文档内容的一小部分，而不是一整个段落或者一组内容。内联元素不会导致文本换行：它通常出现在一堆文字之间例如超链接元素<a>或者强调元素<em>和 <strong>。

# chapter 5. 文本内容

## 学习目标

- 掌握P、h1~h6、hr标签的使用方法
- 掌握有序、无序、定义列表的使用方法
- 掌握引用的几种写法
- 掌握预格式化文本pre标签的用法
- 掌握标签的选择方法
- 掌握各个表示强调的标签的用法
- 掌握上标与下标的用法
- 掌握插入和删除标签的用法
- 掌握常用的实体字符

## 学习内容

- 常见的文本元素

| 元素名称 | 说明                                    | 举例                         | 解释                                                        |
| -------- | --------------------------------------- | ---------------------------- | ----------------------------------------------------------- |
| a        | 生成超链接                              | <a href="url">Link text</a>  | 可访问链接                                                  |
| br       | 强制换行                                | /                            | 在任意文本位置键入< br > 都会被换行                         |
| wbr      | 可安全换行                              | /                            | 会根据浏览器的宽度适当的裁切换行                            |
| b        | 标记一段文字但不强调                    | <b>Hello World</b>           | 加粗不强调信息                                              |
| strong   | 表示重要                                | <strong>Hello World</strong> | 加粗，主要是为了强调一段重要的文本                          |
| i        | 表示外文或科学术语                      | <i>Hello World</i>           | 斜体，区别于其他内容                                        |
| em       | 表示强制                                | <em>Hello World</em>         | 斜体，主要为了强调这段内容                                  |
| code     | 表示计算机代码                          | /                            | 用于表示计算机源代码                                        |
| del      | 表示被删除的文字                        | <del>Hello World</del>       | 删除线，语义中表示这段内容被删除掉                          |
| s        | 表示文字已不在确认                      | <s>Hello World</s>           | 删除线，语义中表示这段文字不准确或校正                      |
| small    | 表示小号字体内容                        | <small>Hello World</small>   | 缩小文字                                                    |
| sub      | 表示下标字体                            | Hello World<sub>1</sub>      | 给文字加上标                                                |
| sup      | 表示上标字体                            | Hello World<sup>2</sup>      | 给文字加下标                                                |
| u        | 标记一段文字但不强调                    | /                            | 给文字加下划线                                              |
| span     | 通用元素，没有任何语义。一般配合CSS修饰 | <span>Hello World</span>     | 没有实际作用；语义上就是表示一段文本，常用它来设置CSS等操作 |

- P标签表示段落，在语义上通常表达完整的一段话，是块级元素。
- h1 ~ h6 是一级 到 六级标题，一级标题最大，六级标题最小，是块级元素。
- hr元素代表分割线，可以分隔段落和标题。
- 如下图所示是p、h1 ~ h6、hr 标签示例：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss1tv5vttj221c1b8gvr.jpg)
- 有序列表用ol标签包围，意为order list，其中的每一项用li标签表示。
- 无序列表用ul标签包围，意为unorder list，其中的每一项用li标签表示。
- 列表列表用dl标签包围，意为definition list，其中用dt（definition title）表示定义的标题，用dd（definition description）表示定义的标题所对应的具体内容。
- 有序列表、无序列表、定义列表的示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss1vayy3tj221c18sqhi.jpg)
- 引用一共有如下三种写法<blockquote>、<cite>、<q>，<blockquote>标签会有段落的缩进，<cite>标签引用的内容会是内容倾斜，<q>标签引用的内容会在内容外面加上双引号。示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss1w1jyxwj221c18sk52.jpg)
- 预格式化文本采用<pre>标签，可以保留在标签内部的文本样式。示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss1ytu9nlj221c18sqem.jpg)
- 有这么多的标签，我们在使用时要选择哪一个呢，可以参考如下方法：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss1zkgermj221c18su02.jpg)
- 在HTML标签中，表示强调的几个标签其实使用场景：
  - strong：重要性、严重性和紧急性
  - em：从一句话中突出某个词语
  - b：将词语从视觉上和其它部分区分，比如一篇论文摘要中的关键词
  - i：换一种语调去说一句话时，比如其它语言翻译，对话中的旁白
- 在HTML中，我们分别使用<sup>和<sub>表示文本的上标和下标。示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss216lkouj221c18s12u.jpg)
- 在HTML中，分别使用<del>和<ins>两个标签表示插入和删除。示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss2261rynj221c18sqjk.jpg)
- HTML中的预留字符不能直接输出，需要通过实体字符进行替换。常见的实体字符如下：&  < > © ¥ ☯。输出示例如下图所示：![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss22u9gogj221c18sdqe.jpg)
- HTML 注释
  - 可以将注释插入 HTML 代码中，这样可以提高其可读性，使代码更易被人理解。浏览器会忽略注释，也不会显示它们，如下。

```html
<!-- This is a comment -->
```

## 资源推荐(扩展学习)

- [HTML 教程- W3school](http://www.w3school.com.cn/html/index.asp)

# chapter 6. 多媒体和可嵌入内容

## 学习目标

- 掌握HTML中的图片标签
- 掌握HTML中的视频标签
- 掌握HTML中的音频标签
- 掌握HTML中可嵌入其他网页的iframe标签

## 学习内容

#### img标签 - 图片

- 图片是在网页中出现的第一个非文本内容的多媒体资源，通常的图片资源包括.jpg，.png，.gif，.bmp……几乎所有格式的图片都可以嵌入在网页中。
- 在HTML中，图片采用单标签![img]()来表示。![img]()标签具有非常重要的src属性，定义图片的资源地址，src属性既可以是相对地址也可以是绝对地址。
- 如下所示是img标签的示例：

```html
<p>
  我是一张图片
  <br>
  <img width="500" height="250" 
       src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/240px-HTML5_logo_and_wordmark.svg.png">
</p>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss3z76tu9j20p00h0dhf.jpg)

- 在上述例子中，设置了该图像的宽为500px，高为250px。若我们不设置图片的宽和高，将会以图像本来的大小显示。
- img标签是一个内联元素，将不会单独占据一行，而是以图像设置的大小来在行内显示。示例如下：

```html
<p>
    i am a 
    <img width="100px" src="https://media.istockphoto.com/photos/red-apple-with-leaf-isolated-on-white-background-picture-id185262648?k=6&m=185262648&s=612x612&w=0&h=u9rMspGGTOkgUSzZ6INtT_Ww4NpGz9zHMGRmIJJjBqQ=" alt=""> 
    apple.
</p>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss3hfje3wj221c18sgs6.jpg)

#### video标签 - 视频

- video标签使我们简单的嵌入一段视频。举例如下：

```html
<video src="rabbit320.webm" controls>
  <p>Your browser doesn't support HTML5 video. Here is a <a href="rabbit320.webm">link to the video</a> instead.</p> 
</video>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548056409450-fe0b7de2-7275-4406-97db-06da45afdeeb.png)

- 其中src属性指向想要嵌入到网页中的视频资源，controls属性使用户具有了对视频的控制权限，使用户可以控制视频的暂停、播放等功能。

- video标签内部还有一个段落，被称为后备段落，当浏览器不支持Video标签的时候，后备段落就会显示出来。在上述例子中，添加了一个链接，指向该视频文件，可以使用户点击访问。

- video标签还有一些其他的属性，比如：

  - width和height，控制视频的尺寸，但当我们对视频的尺寸进行调整是，视频会一直保持固定的纵横比，如果未被视频内容填充的部分，将会显示为默认的背景颜色。

  - autoplay，这个属性会使视频内容自动播放，即使页面的其他部分还没有加载完全。

  - muted，该属性设置该视频在播放时，默认是处于静音的状态。

  - poster，同img标签类似，指向一个图像的URL，该图像作为该视频的海报，在视频播放前显示。

  - preload，该属性通常被用来缓存较大的视频文件，该属性有以下几个值： - none：不缓冲 - auto：页面加载后缓存视频文件 - metadata：仅缓冲视频的元数据

    ##### audio标签 - 音频

  - audio标签和video标签的使用用法几乎相同，只有一些细微的不同，示例如下。

```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3">
  <source src="viper.ogg" type="audio/ogg">
  <p>Your browser doesn't support HTML5 audio. Here is a <a href="viper.mp3">link to the audio</a> instead.</p>
</audio>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss3k2hx9zj221c18s76z.jpg)

- audio标签不支持width/height属性（因为只是显示音频播放内容，无视觉显示部件）。

- audio标签也不支持poster属性，同样是由于没有视觉显示部件。

  #### iframe标签

- iframe标签的目的是为了我们能够将其他的Web文档嵌入到当前文档中。一些常用的第三方内容提供商都采用该技术，如Disqus的评论系统、在线视频提供商的视频等。

- iframe的示例如下：

```html
<iframe src="https://baidu.com"
        width="500" height="500" frameborder="0"
        allowfullscreen sandbox>
  <p><a href="https://baidu.com">
    Fallback link for browsers that don't support iframes
  </a></p>
</iframe>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss3lbgzpcj221c18squi.jpg)

- 以上示例中iframe的常用属性介绍如下：
  - allowfullscreen，若设置为true，iframe则可以使用全屏的接口在当前页面采用全屏页面显示。
  - frameborder，边框，如果设置为1，则在当前页面和iframe嵌入的页面之间有1px的边框，若设置为0，代表删除边框。
  - scr，代表该iframe所需要链接的文档的地址。
  - width和width，代表iframe的宽度和高度。
  - 后备段落，和audio/video一样，当浏览器不支持iframe标签时，会显示后备段落中的内容。
  - sandbox，沙盒，体现了现代浏览器对安全性的设置。为了最大程度上减少网站被黑客的攻击，尽量始终使用sandbox属性。未沙盒化的内容可以做的不安去的事情太多，比如：执行JavaScript、提交表单等。

## 资源推荐(扩展学习)

- [HTML iframe- W3school](http://www.w3school.com.cn/html/html_iframe.asp)
- [HTML 教程- W3school](http://www.w3school.com.cn/html/html_media.asp)

# chapter 7. 表格内容

## 学习目标

- 了解什么是表格
- 掌握表格标签table，thead，tbody，tr，th，td，caption
- 掌握表格中常用的属性，colspan、rowspan、border

## 学习内容

- 表格是有行和列组成的二维结构化数据集，通过表格能够简捷迅速地查找某个表示不同类型数据之间的某种关系的值。
- 基本的表格示例如下：

```html
<table border="1">
  <thead>
    <tr>
      <th>浏览器</th>
      <th>渲染引擎</th>
      <th>JavaScript 引擎</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chrome</th>
      <td>Blink</td>
      <td>V8</td>
    </tr>
    <tr>
      <th>Opera</th>
      <td>Blink</td>
      <td>V8</td>
    </tr>
  </tbody>
</table>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss31gnbg4j221c18saee.jpg)

- table标签详细描述：
  - table - 定义表格
  - thead - 表格的页眉
  - tbody - 表格的主体
  - tr - 表格的一行
  - th - 表格的表头
  - td - 表格中的单元格
  - border - 表格是否有边框，数值代表边框的宽度
- table标签要有正确的嵌套方式，有table定义表格，子层嵌套thead和tbody，在页眉和主体内部分别嵌套表格的一行tr，最内层是表格的单元格td。
- 表格内部还可以合并行，如下示例：

```html
<table border="1">
  <thead>
    <tr>
      <th>浏览器</th>
      <th>渲染引擎</th>
      <th>JavaScript 引擎</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chrome</th>
      <td rowspan="2">Blink</td>
      <td rowspan="2">V8</td>
    </tr>
    <tr>
      <th>Opera</th>
    </tr>
  </tbody>
</table>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss32z5yv7j221c1b8n1a.jpg)

- 其中 rowspan 代表该列跨多少行，以此来合并行，同样我们可以通过 colspan 来表示该行跨了多少列，以此来合并列，如下示例所示。

```html
<table border="1">
  <thead>
    <tr>
      <th>浏览器</th>
      <th>Chrome</th>
      <th>Opera</th>
      <th>Firefox</th>
      <th>Edge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>渲染引擎</th>
      <td colspan="2">Blink</td>
      <td>Gecko</td>
      <td>Edge</td>
    </tr>
  </tbody>
</table>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss342qh1vj221c18swij.jpg)

- 还可以通过 caption 标签表示table的标题，如下所示：

```html
<table border="1">
  <!-- caption 必须是table的第一个元素 -->
  <caption>浏览器及其引擎</caption>
  <thead>
    <tr>
      <th>浏览器</th>
      <th>Chrome</th>
      <th>Opera</th>
      <th>Firefox</th>
      <th>Edge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>渲染引擎</th>
      <td colspan="2">Blink</td>
      <td>Gecko</td>
      <td>Edge</td>
    </tr>
  </tbody>
</table>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss350ovrvj221c18sn21.jpg)

- table标签中还可以采用 colgroup 进行列的分组，如下示例所示：

```html
<table border="1">
  <colgroup>
    <col class="browser">
    <col class="engine" span="2">
  </colgroup>
  <thead>
    <tr>
      <th>浏览器</th>
      <th>渲染引擎</th>
      <th>JavaScript 引擎</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chrome</th>
      <td>Blink</td>
      <td>V8</td>
    </tr>
    <tr>
      <th>Opera</th>
      <td>Blink</td>
      <td>V8</td>
    </tr>
  </tbody>
</table>
```

# chapter 8. 表单内容

## 学习目标

- 什么是表单
- 掌握单行文本框、密码、多行文本框、单选、多选、下拉选择、文件、按钮等类别的输入标签的具体用法

## 学习内容

- 表单通常用于诸如银行卡申请、登录、注册等场景下，包含单行文本框、单选、多选等多种类型的输入方式，以使用户填写，从而为系统提供数据。表单是用户和web网站或应用程序之间交互的主要内容之一，允许用户将数据发送到web网站。
- HTML表单通常是有一个或多个组件构成的，这些小的组件可以是单行/多行文本字段、选择框、按钮、复选框或单选按钮。
- 表单和普通的HTML文档有以下几点主要的不同：多数情况下，表单收集到的数据被发送到web服务器。这时，需要单独设置一个web服务器来接收和处理数据请求，但是HTML文档却不必要，尽在本地就可以正确运行。
- 基本的表单如下示例所示：

```html
<form action="/echo" method="POST">
  <p>用户名：<input type="text" name="username"></p>
  <p>密码：<input type="password" name="password"></p>
  <p><button type="submit">登录</button></p>
</form>
```

![img](https://ws1.sinaimg.cn/large/a3e6a3afly1fss3bnojzqj221c18s0vd.jpg)

- 其中包含的小组件主要有以下几种：
  - 单行文本框 - <input type='text'>
  - 密码输入 - <input type='password'>
  - 多行文本框 - <textarea>
  - 单选按钮 - <radio>
  - 多选按钮 - <checkbox>
  - 下拉选择（单选） - <select>
  - 下拉选择（多选） - <select multiple>
  - 文件选择 - <input type='file'>
  - 时间和日期 - <input type="date">/<input type="datetime-local">/<input type="month">/<input type="week">/<input type="time">
- HTML 表单中常用的属性
  - action - 向服务器发送的请求地址
  - method - 要发送的HTTP请求类型
  - name - 表单的名称
  - target - 用于发送请求和接收响应的窗口名称
  - value - 某一个具体的表单项所对应的值
  - placeholder - 输入框的占位符，当输入框中为空时占位符会显示
  - checked - 针对多选框/单选框，默认的状态时选中状态
- 表单设计的几个原则：
  - 尽量帮助用户不出差错
  - 尽早提示用户填写错误
  - 尽可能的扩大选择/点击区域
  - 当表单中控件较多是要分组
  - 在设计表单时要分清主要动作和次要动作

#### 如何获取form表单的引用？

```html
<form id="form" name="form1"></form>
```

我现在想取到上面的form表单的引用，一共有以下方式可以获取到上面 的form表单引用；

- 通过获取form表单的id，来获取form表单的引用；如下代码：

```js
var formId = document.getElementById("form");console.log(formId);
```

- 通过document.forms 取得页面中的所有表单元素，然后通过索引来取到对应的form元素，如下代码所示：取得页面第一个form元素；

```js
console.log(document.forms[0]);
```

- 通过from表单中的name属性来获取，代码如下：

```js
console.log(document.forms['form1']);
```

#### 如何提交表单?

用户单击提交按钮或图像按钮时，就会提交表单，使用input或者button都可以提交表单，只需将type设置为submit或者image即可，如下三种方式都可以；

第一种：

```html
<form id="form" name="form1" action="http://www.baidu.com">
    <!-- 存放一个input放在这，为了获取焦点，然后我们可以按enter键提交 -->
    <input type="text">
    <input type="submit" value="submit">
</form>
```

第二种：

```html
<form id="form" name="form1" action="http://www.baidu.com">
    <!-- 存放一个input放在这，为了获取焦点，然后我们可以按enter键提交 -->
    <input type="text">
    <button type="submit">submit</button>
</form>
```

第三种：

```html
<form id="form" name="form1" action="http://www.baidu.com">
    <!-- 存放一个input放在这，为了获取焦点，然后我们可以按enter键提交 -->
    <input type="text">
    <input type="image" src="aa.jpg">
</form>
```

#### 如何重置表单?

如果我们使用按钮重置表单的话，有下面2种方式：

第一种代码如下：

```html
<form id="form" name="form1" action="http://www.baidu.com">
    <input type="text">
    <input type="reset" value="reset">
</form>
```

第二种代码如下：

```html
<form id="form" name="form1" action="http://www.baidu.com">
    <input type="text">
    <button type="reset">reset</button>
</form>
```

## 资源推荐(扩展学习)

- [HTML 教程- W3school](http://www.w3school.com.cn/html/html_forms.asp)