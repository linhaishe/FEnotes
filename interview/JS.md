## 一、Web 存储 / 浏览器能力

- 如何实现可过期的 localStorage 数据？
- JavaScript 如何计算一段文本渲染之后的长度
- jsBridge 是什么?工作原理是什么?
- 说说你对 requestAnimationFrame 的理解
- DOM 事件的类型和事件流机制?
- 什么是DOM和BOM?
- 什么是事件代理/事件委托？应用场景？
- 事件捕捉/事件冒泡/事件流 eventflow

### 13. 什么是DOM和BOM?

![image-20251224172324262](https://s2.loli.net/2025/12/24/HeuBjgIG2iqd6VP.png)

- DOM 指的是文档对象模型，它指的是把文档当做一个对象，这个对象主要定义了处理网页内容的方法和接口。
- BOM 指的是浏览器对象模型，它指的是把浏览器当做一个对象来对待，这个对象主要定义了与浏览器进行交互的法和接口。BOM的核心是 window，而 window 对象具有双重角色，它既是通过 js 访问浏览器窗口的一个接口，又是一个 Global（全局）对象。这意味着在网页中定义的任何对象，变量和函数，都作为全局对象的一个属性或者方法存在。window 对象含有 location 对象、navigator 对象、screen 对象等子对象，并且 DOM 的最根本的对象 document 对象也是 BOM 的 window 对象的子对象。

### 14. 常见的DOM操作有哪些

节点的增删改查

```js
getElementById // 按照 id 查询
getElementsByTagName // 按照标签名查询
getElementsByClassName // 按照类名查询
querySelectorAll // 按照 css 选择器查询

// 按照 id 查询
var imooc = document.getElementById('imooc') // 查询到 id 为 imooc 的元素
// 按照标签名查询
var pList = document.getElementsByTagName('p')  // 查询到标签为 p 的集合
console.log(divList.length)
console.log(divList[0])
// 按照类名查询
var moocList = document.getElementsByClassName('mooc') // 查询到类名为 mooc 的集合
// 按照 css 选择器查询
var pList = document.querySelectorAll('.mooc') // 查询到类名为 mooc 的集合
```

```js
// 首先获取父节点
var container = document.getElementById('container')
// 创建新节点
var targetSpan = document.createElement('span')
// 设置 span 节点的内容
targetSpan.innerHTML = 'hello world'
// 把新创建的元素塞进父节点里去
container.appendChild(targetSpan)
```

```js
// 获取目标元素的父元素
var container = document.getElementById('container')
// 获取目标元素
var targetNode = document.getElementById('title')
// 删除目标元素
container.removeChild(targetNode)
```

```js
// 获取父元素
var container = document.getElementById('container')   
 
// 获取两个需要被交换的元素
var title = document.getElementById('title')
var content = document.getElementById('content')
// 交换两个元素，把 content 置于 title 前面
container.insertBefore(content, title)
```

### 15. 说说你对BOM的理解，常见的BOM对象你了解哪些？

**1. Window**

- `moveBy(x,y)`：从当前位置水平移动窗体x个像素，垂直移动窗体y个像素，x为负数，将向左移动窗体，y为负数，将向上移动窗体
- `moveTo(x,y)`：移动窗体左上角到相对于屏幕左上角的(x,y)点
- `resizeBy(w,h)`：相对窗体当前的大小，宽度调整w个像素，高度调整h个像素。如果参数为负值，将缩小窗体，反之扩大窗体
- `resizeTo(w,h)`：把窗体宽度调整为w个像素，高度调整为h个像素
- `scrollTo(x,y)`：如果有滚动条，将横向滚动条移动到相对于窗体宽度为x个像素的位置，将纵向滚动条移动到相对于窗体高度为y个像素的位置
- `scrollBy(x,y)`： 如果有滚动条，将横向滚动条向左移动x个像素，将纵向滚动条向下移动y个像素

**2. location**

| 属性名   | 例子                                                   | 说明                                |
| -------- | ------------------------------------------------------ | ----------------------------------- |
| hash     | "#contents"                                            | utl中#后面的字符，没有则返回空串    |
| host     | www.wrox.com:80                                        | 服务器名称和端口号                  |
| hostname | www.wrox.com                                           | 域名，不带端口号                    |
| href     | http://www.wrox.com:80/WileyCDA/?q=javascript#contents | 完整url                             |
| pathname | "/WileyCDA/"                                           | 服务器下面的文件路径                |
| port     | 80                                                     | url的端口号，没有则为空             |
| protocol | http:                                                  | 使用的协议                          |
| search   | ?q=javascript                                          | url的查询字符串，通常为？后面的内容 |

**3. navigator**

![image-20251224172445256](https://s2.loli.net/2025/12/24/rwb5tf8OqsYRyv2.png)

![image-20251224172507004](https://s2.loli.net/2025/12/24/nmA4v7jRTf5UPSZ.png)

**4. screen**

![image-20251224172525327](https://s2.loli.net/2025/12/24/TIvCdzMKr7kmloG.png)

**5. history**

- `history.forward()`：向前跳转一个页面
- `history.back()`：向后跳转一个页面
- `history.length`：获取历史记录数

### 7. JavaScript脚本延迟加载的方式有哪些/js脚本异步加载

延迟加载就是等页面加载完成之后再加载 JavaScript 文件。 js 延迟加载有助于提高页面加载速度。

一般有以下几种方式：

- **defer 属性：**给 js 脚本添加 defer 属性，这个属性会让脚本的加载与文档的解析同步解析，然后在文档解析完成后再执行这个脚本文件，这样的话就能使页面的渲染不被阻塞。多个设置了 defer 属性的脚本按规范来说最后是顺序执行的，但是在一些浏览器中可能不是这样。
- **async 属性：**给 js 脚本添加 async 属性，这个属性会使脚本异步加载，不会阻塞页面的解析过程，但是当脚本加载完成后立即执行 js 脚本，这个时候如果文档没有解析完成的话同样会阻塞。多个 async 属性的脚本的执行顺序是不可预测的，一般不会按照代码的顺序依次执行。
- **动态创建 DOM 方式：**动态创建 DOM 标签的方式，可以对文档的加载事件进行监听，当文档加载完成后再动态的创建 script 标签来引入 js 脚本。
- **使用 setTimeout 延迟方法：**设置一个定时器来延迟加载js脚本文件
- **让 JS 最后加载：**将 js 脚本放在文档的底部，来使 js 脚本尽可能的在最后来加载执行。

### 3. ==Javascript本地存储的方式有哪些？区别及应用场景？==

#### 区别

关于`cookie`、`sessionStorage`、`localStorage`三者的区别主要如下：

- 存储大小：`cookie`数据大小不能超过`4k`，`sessionStorage`和`localStorage`虽然也有存储大小的限制，但比`cookie`大得多，可以达到5M或更大
- 有效时间：`localStorage`存储持久数据，浏览器关闭后数据不丢失除非主动删除数据； `sessionStorage`数据在当前浏览器窗口关闭后自动删除；`cookie`设置的`cookie`过期时间之前一直有效，即使窗口或浏览器关闭
- 数据与服务器之间的交互方式，`cookie`的数据会自动的传递到服务器，服务器端也可以写`cookie`到客户端； `sessionStorage`和`localStorage`不会自动把数据发给服务器，仅在本地保存

#### 应用场景

- 标记用户与跟踪用户行为的情况，推荐使用`cookie`
- 适合长期保存在本地的数据（令牌），推荐使用`localStorage`
- 敏感账号一次性登录，推荐使用`sessionStorage`
- 存储大量数据的情况、在线文档（富文本编辑器）保存编辑历史的情况，推荐使用`indexedDB`

`javaScript`本地缓存的方法我们主要讲述以下四种：

- cookie
- sessionStorage
- localStorage
- indexedDB

#### a. cookie

`Cookie`，类型为「小型文本文件」，指某些网站为了辨别用户身份而储存在用户本地终端上的数据。是为了解决 `HTTP`无状态导致的问题

作为一段一般不超过 4KB 的小型文本数据，它由一个名称（Name）、一个值（Value）和其它几个用于控制 `cookie`有效期、安全性、使用范围的可选属性组成

但是`cookie`在每次请求中都会被发送，如果不使用 `HTTPS`并对其加密，其保存的信息很容易被窃取，导致安全风险。举个例子，在一些使用 `cookie`保持登录态的网站上，如果 `cookie`被窃取，他人很容易利用你的 `cookie`来假扮成你登录网站

关于`cookie`常用的属性如下：

关于`cookie`常用的属性如下：

```js
document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";
```

- expires 用于设置 Cookie 的过期时间

```js
expires=Wed, 21 Oct 2015 07:28:00 GMT
```

- max-Age 用于设置在 Cookie 失效之前需要经过的秒数（优先级比`Expires`高）

```
max-Age=604800
```

- `;max-age=max-age-in-seconds` (e.g., `60*60*24*365` or 31536000 for a year)
- `;expires=date-in-GMTString-format` If neither `expires` nor `max-age` specified it will expire at the end of session.

- `Domain`指定了 `Cookie` 可以送达的主机名
- `Path`指定了一个 `URL`路径，这个路径必须出现在要请求的资源的路径中才可以发送 `Cookie` 首部

```js
Path=/docs   # /docs/Web/ 下的资源会带 Cookie 首部
```

- 标记为 `Secure`的 `Cookie`只应通过被`HTTPS`协议加密过的请求发送给服务端

通过上述，我们可以看到`cookie`又开始的作用并不是为了缓存而设计出来，只是借用了`cookie`的特性实现缓存

关于`cookie`的使用如下：

```js
document.cookie = '名字=值';
```

关于`cookie`的修改，首先要确定`domain`和`path`属性都是相同的才可以，其中有一个不同得时候都会创建出一个新的`cookie`

```js
Set-Cookie:name=aa; domain=aa.net; path=/  # 服务端设置
document.cookie =name=bb; domain=aa.net; path=/  # 客户端设置
```

最后`cookie`的删除，最常用的方法就是给`cookie`设置一个过期的事件，这样`cookie`过期后会被浏览器删除

#### b. localStorage

`HTML5`新方法，IE8及以上浏览器都兼容

特点

- 生命周期：持久化的本地存储，除非主动删除数据，否则数据是永远不会过期的
- 存储的信息在同一域中是共享的
- 当本页操作（新增、修改、删除）了`localStorage`的时候，本页面不会触发`storage`事件,但是别的页面会触发`storage`事件。
- 大小：5M（跟浏览器厂商有关系）
- `localStorage`本质上是对字符串的读取，如果存储内容多的话会消耗内存空间，会导致页面变卡
- 受同源策略的限制

下面再看看关于`localStorage`的使用

设置

```js
localStorage.setItem('username','cfangxu');
```

获取

```js
localStorage.getItem('username')
```

获取键名

```js
localStorage.key(0) //获取第一个键名
```

删除

```js
localStorage.removeItem('username')
```

一次性清除所有存储

```js
localStorage.clear()
```

`localStorage` 也不是完美的，它有两个缺点：

- 无法像`Cookie`一样设置过期时间
- 只能存入字符串，无法直接存对象

```js
localStorage.setItem('key', {name: 'value'});
console.log(localStorage.getItem('key')); // '[object, Object]'
```

#### c. sessionStorage

`sessionStorage`和 `localStorage`使用方法基本一致，唯一不同的是生命周期，一旦页面（会话）关闭，`sessionStorage` 将会删除数据。

#### d. indexedDB

`indexedDB`是一种低级API，用于客户端存储大量结构化数据(包括, 文件/ blobs)。该API使用索引来实现对该数据的高性能搜索

虽然 `Web Storage`对于存储较少量的数据很有用，但对于存储更大量的结构化数据来说，这种方法不太有用。`IndexedDB`提供了一个解决方案

优点：

- 储存量理论上没有上限
- 所有操作都是异步的，相比 `LocalStorage` 同步操作性能更高，尤其是数据量较大时
- 原生支持储存`JS`的对象
- 是个正经的数据库，意味着数据库能干的事它都能干

缺点：

- 操作非常繁琐
- 本身有一定门槛

关于`indexedDB`的使用基本使用步骤如下：

- 打开数据库并且开始一个事务
- 创建一个 `object store`
- 构建一个请求来执行一些数据库操作，像增加或提取数据等。
- 通过监听正确类型的 `DOM` 事件以等待操作完成。
- 在操作结果上进行一些操作（可以在 `request`对象中找到）

关于使用`indexdb`的使用会比较繁琐，大家可以通过使用`Godb.js`库进行缓存，最大化的降低操作难度

### 16. 如何在 url 中传递数组

在 URL 中如何传递数组这种复杂的数据，完全**取决于项目中前后端成员关于复杂数据在 URL 中传输的约定**，一般情况下可以使用以下方式来传递数组

```js
a=3&a=4&a=5

a=3,4,5

a[]=3&a[]=4&a[]=5

a[0]=3&a[1]=4&a[2]=5
```

但同样，需要后端开发者写一个 `querystring.parse` 来对指定的格式解析进行支持，同时也有对各种复杂 qs 支持较好的 package，比如：[qs: 据说是对 querystring 复杂对象解析最好的库](https://github.com/ljharb/qs#parsing-arrays)

### 8. 如何判断一个元素是否在可视区域中？

https://vue3js.cn/interview/JavaScript/visible.html#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F

<img src="https://s2.loli.net/2025/12/26/XMDIklN841wsRhz.png" alt="image-20251226165721563" style="zoom:33%;" />

在日常开发中，我们经常需要判断目标元素是否在视窗之内或者和视窗的距离小于一个值（例如 100 px），从而实现一些常用的功能，例如：

- 图片的懒加载
- 列表的无限滚动
- 计算广告元素的曝光情况
- 可点击链接的预加载

判断一个元素是否在可视区域，我们常用的有三种办法：

- offsetTop、scrollTop
- getBoundingClientRect
- Intersection Observer



### 9. ==大文件上传如何做断点续传？==

https://vue3js.cn/interview/JavaScript/continue_to_upload.html#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF

### 10. ==如何实现上拉加载，下拉刷新？==

https://vue3js.cn/interview/JavaScript/pull_up_loading_pull_down_refresh.html#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80

#### 上拉加载

上拉加载的本质是页面触底，或者快要触底时的动作

`scrollTop + clientHeight >= scrollHeight`

```js
let clientHeight = document.documentElement.clientHeight; //浏览器高度
let scrollHeight = document.body.scrollHeight;
let scrollTop = document.documentElement.scrollTop;

let distance = 50; //距离视窗还用50的时候，开始触发；

if (scrollTop + clientHeight >= scrollHeight - distance) {
  console.log("开始加载数据");
}
```

#### 下拉刷新

下拉刷新的本质是页面本身置于顶部时，用户下拉时需要触发的动作

关于下拉刷新的原生实现，主要分成三步：

- 监听原生`touchstart`事件，记录其初始位置的值，`e.touches[0].pageY`；
- 监听原生`touchmove`事件，记录并计算当前滑动的位置值与初始位置值的差值，大于`0`表示向下拉动，并借助CSS3的`translateY`属性使元素跟随手势向下滑动对应的差值，同时也应设置一个允许滑动的最大值；
- 监听原生`touchend`事件，若此时元素滑动达到最大值，则触发`callback`，同时将`translateY`重设为`0`，元素回到初始位置

### 11. ==什么是单点登录？如何实现？==

单点登录（Single Sign On），简称为 SSO，是目前比较流行的企业业务整合的解决方案之一

SSO的定义是在多个应用系统中，用户只需要登录一次就可以访问所有相互信任的应用系统

SSO 一般都需要一个独立的认证中心（passport），子系统的登录均得通过`passport`，子系统本身将不参与登录操作

当一个系统成功登录以后，`passport`将会颁发一个令牌给各个子系统，子系统可以拿着令牌会获取各自的受保护资源，为了减少频繁认证，各个子系统在被`passport`授权以后，会建立一个局部会话，在一定时间内可以无需再次向`passport`发起认证

上图有四个系统，分别是`Application1`、`Application2`、`Application3`、和`SSO`，当`Application1`、`Application2`、`Application3`需要登录时，将跳到`SSO`系统，`SSO`系统完成登录，其他的应用系统也就随之登录了

淘宝、天猫都属于阿里旗下，当用户登录淘宝后，再打开天猫，系统便自动帮用户登录了天猫，这种现象就属于单点登录

#### a. 同域名下的单点登录

`cookie`的`domain`属性设置为当前域的父域，并且父域的`cookie`会被子域所共享。`path`属性默认为`web`应用的上下文路径

利用 `Cookie` 的这个特点，没错，我们只需要将`Cookie`的`domain`属性设置为父域的域名（主域名），同时将 `Cookie`的`path`属性设置为根路径，将 `Session ID`（或 `Token`）保存到父域中。这样所有的子域应用就都可以访问到这个`Cookie`

不过这要求应用系统的域名需建立在一个共同的主域名之下，如 `tieba.baidu.com` 和 `map.baidu.com`，它们都建立在 `baidu.com`这个主域名之下，那么它们就可以通过这种方式来实现单点登录

#### b. 不同域名下的单点登录(一)

认证中心方式（服务端型 SSO）

前端 Token 同步方式（客户端型 SSO）

Cookie 仅在认证中心可用

应用系统需向认证中心确认 Token

支持跨域、扩展性好

标准服务端型 SSO 实现

```lua
用户           应用系统A          认证中心
 |                 |                 |
 |----访问A-------->|                 |
 |                 |--检查Token------>|
 |                 |                 |
 |                 |<--跳转登录------| (如果判断已经登陆过了，直接跳进页面。)
 |                 |                 |
 |                 |<--登录页面------|
 |                 |                 |
 |----输入账号密码-->|                 |
 |                 |--验证账号-------->|
 |                 |<--写Token(Cookie)|
 |                 |<--跳转回A--------|
 |                 |                 |
 |                 |--验证Token-------->|
 |                 |<--确认合法--------|
 |                 |                 |
 |<--------访问成功--------------------|

```

如果是不同域的情况下，`Cookie`是不共享的，这里我们可以部署一个认证中心，用于专门处理登录请求的独立的 `Web`服务

用户统一在认证中心进行登录，登录成功后，认证中心记录用户的登录状态，并将 `token` 写入 `Cookie`（注意这个 `Cookie`是认证中心的，应用系统是访问不到的）

应用系统检查当前请求有没有 `Token`，如果没有，说明用户在当前系统中尚未登录，那么就将页面跳转至认证中心

由于这个操作会将认证中心的 `Cookie` 自动带过去，因此，认证中心能够根据 `Cookie` 知道用户是否已经登录过了

如果认证中心发现用户尚未登录，则返回登录页面，等待用户登录

如果发现用户已经登录过了，就不会让用户再次登录了，而是会跳转回目标 `URL`，并在跳转前生成一个 `Token`，拼接在目标`URL` 的后面，回传给目标应用系统

应用系统拿到 `Token`之后，还需要向认证中心确认下 `Token` 的合法性，防止用户伪造。确认无误后，应用系统记录用户的登录状态，并将 `Token`写入`Cookie`，然后给本次访问放行。（注意这个 `Cookie` 是当前应用系统的）当用户再次访问当前应用系统时，就会自动带上这个 `Token`，应用系统验证 Token 发现用户已登录，于是就不会有认证中心什么事了

此种实现方式相对复杂，支持跨域，扩展性好，是单点登录的标准做法

#### c. 不同域名下的单点登录(二)

前端 Token 同步方式（客户端型 SSO）

Token 存储在浏览器 LocalStorage

前端通过 `iframe + postMessage` 跨域同步 Token

几乎不依赖后端

完全前端实现，支持跨域

```lua
用户           应用系统A          应用系统B
 |                 |                 |
 |----访问A-------->|                 |
 |                 |<--返回Token------|
 |                 |                 |
 |                 |--写LocalStorage-->|
 |                 |                 |
 |<---iframe+postMessage同步Token-->B |
 |                 |                 |
 |                 |                 |
 |----访问B-------->|                 |
 |                 |--读取LocalStorage Token->|
 |                 |--携带Token请求验证-->|
 |                 |                 |
 |<--------访问成功--------------------|

```

可以选择将 `Session ID` （或 `Token` ）保存到浏览器的 `LocalStorage` 中，让前端在每次向后端发送请求时，主动将`LocalStorage`的数据传递给服务端

这些都是由前端来控制的，后端需要做的仅仅是在用户登录成功后，将 `Session ID`（或 `Token`）放在响应体中传递给前端

单点登录完全可以在前端实现。前端拿到 `Session ID`（或 `Token` ）后，除了将它写入自己的 `LocalStorage` 中之外，还可以通过特殊手段将它写入多个其他域下的 `LocalStorage` 中

前端通过 `iframe`+`postMessage()` 方式，将同一份 `Token` 写入到了多个域下的 `LocalStorage` 中，前端每次在向后端发送请求之前，都会主动从 `LocalStorage` 中读取`Token`并在请求中携带，这样就实现了同一份`Token` 被多个域所共享

此种实现方式完全由前端控制，几乎不需要后端参与，同样支持跨域

```js
// 获取 token
var token = result.data.token;

// 动态创建一个不可见的iframe，在iframe中加载一个跨域HTML
var iframe = document.createElement("iframe");
iframe.src = "http://app1.com/localstorage.html";
document.body.append(iframe);
// 使用postMessage()方法将token传递给iframe
setTimeout(function () {
  iframe.contentWindow.postMessage(token, "http://app1.com");
}, 4000);
setTimeout(function () {
  iframe.remove();
}, 6000);

// 在这个iframe所加载的HTML中绑定一个事件监听器，当事件被触发时，把接收到的token数据写入localStorage
window.addEventListener(
  "message",
  function (event) {
    localStorage.setItem("token", event.data);
  },
  false
);
```

### 12. 浏览器的剪切板中如何监听复制事件

在 HTML 元素上

```html
<input oncopy="cb" />
```

在 JS 中获取具体元素

```js
document.querySelector("p").oncopy = cb;
document.oncopy = cb;
```

或者

```js
document.querySelector("p").addEventListener("copy", cb);
document.addEventListener("copy", cb);
```

### 13. 在前端开发中，如何获取浏览器的唯一标识

根据 `canvas` 可以获取浏览器指纹信息

1. 绘制 `canvas`，获取 `base64` 的 dataurl
2. 对 dataurl 这个字符串进行 `md5` 摘要计算，得到指纹信息

若在生产环境使用，可以使用 [fingerprintjs2 (opens new window)](https://github.com/Valve/fingerprintjs2)，根据业务需求，如单设备是否可跨浏览器，以此选择合适的 `component`

### 21. 如何裁剪图片 (情景：选择头像)

使用`ctx.arc()`和`ctx.clip()`进行裁剪`ctx.arc(x, y, radius, startAngle, endAngle)`; `ctx.clip()`; `ctx.drawImage(img, x, y, width, height)`

```js
var path = "https://static-zh.wxb.com.cn/customer/form/2020/11/1758696796d.jpg";
function clipImage(path) {
  const canvas = document.createElement("canvas");
  canvas.width = 200;
  canvas.height = 100;
  const ctx = canvas.getContext("2d");
  const img = document.createElement("img");
  img.src = path;
  img.setAttribute("crossOrigin", "Anonymous");
  img.onload = function () {
    ctx.drawImage(this, 0, 0, 200, 100);
    console.log(canvas.toDataURL());
  };
}
clipImage(path);

```

### 14. ==用 npm 发布过 package，如何发布==

1. 注册 npm 账号 https://www.npmjs.com/
2. 本地通过命令行 `npm login` 登陆
3. 进入到项目目录下（与 package.json 同级），在 package.json 中指定发布文件、文件夹

```json
{
  "name": "pkg-xxx",
  "version": "0.0.1",
  "main": "lib/index.js",
  "module": "esm/index.js",
  "typings": "types/index.d.ts",
  "files": [
    "CHANGELOG.md",
    "lib",
    "esm",
    "dist",
    "types",
  ],
  ...
}
```

执行 `npm publish --registry=https://registry.npmjs.org/` 即可发布

### 15. js 代码压缩 minify 的原理是什么

我们知道 `javascript` 代码经压缩 (uglify) 后，可以使体积变得更小，那它代码压缩的原理是什么。如果你来做这么一个功能的话，你会怎么去压缩一段 `js` 代码的体积。

https://github.com/shfshanyue/Daily-Question/issues/138

------

## 二、JavaScript 语言体系 / 运行环境认知

- JavaScript 和 BOM、DOM、ECMAScript、Node.js 之间是..
- 「use strict」是什么?它有什么用?为什么 JavaScript 严格模式会禁用 with 语句?
- ES6 代码转成 ES5 代码的实现思路是什么?

### 1. let, const, var区别

块级作用域，重复声明，变量提升，暂时性死区

块级作用域: 用 `{}` 包起来的一段代码，形成一个独立的作用域，在这个作用域里声明的变量，**外面访问不到**。

**减少变量污染**、**避免意外覆盖**、**让循环变量更符合直觉**、**为 TDZ 提供语义基础**、**让代码更容易推理**

```js
{
  let a = 1;
  const b = 2;
}

try {
  let errMsg = 'oops';
} catch (e) {
  // e 只在 catch 块中有效
}

```

ES6规定，`let/const` 命令会使区块形成封闭的作用域。若在声明之前使用变量，就会报错。总之，在代码块内，使用 `let` 命令声明变量之前，该变量都是不可用的。这在语法上，称为 **“暂时性死区”**（ temporal dead zone，简称 **TDZ**）。

使用 let 声明的变量不会挂在全局对象 window 上，因此无法通过 window.variableName 的方式访问。这与使用 var 声明的变量不同，var 声明的变量会被挂载在全局对象上，因此可以通过 window.variableName 的方式访问

![image-20251224155827191](https://s2.loli.net/2025/12/24/yEHXRW5r6jL9KZ3.png)

```js
// `function foo() {}` 是 **函数声明**，在作用域创建阶段：函数体就已经被创建并绑定,所以可以在定义之前调用。

foo(); // ✅ 正常执行

function foo() {
  console.log('hello');
}

// --

baz(); // ❌ ReferenceError（TDZ）

let baz = function () {
  console.log('yo');
};

// --

qux(); // ❌ ReferenceError（TDZ）

const qux = () => {
  console.log('yo');
};
```

| 写法                   | 是否 TDZ | 定义前调用结果   |
| ---------------------- | -------- | ---------------- |
| `function f(){}`       | ❌        | ✅ 正常           |
| `var f = function(){}` | ❌        | ❌ TypeError      |
| `let f = function(){}` | ✅        | ❌ ReferenceError |
| `const f = () => {}`   | ✅        | ❌ ReferenceError |

### 2. const 对象的属性可以更改吗

`const`保证的并不是变量的值不能改动，而是变量指向的那个内存地址不能改动。对于基本类型的数据（数值、字符串、布尔值），其值就保存在变量指向的那个内存地址，因此等同于常量。

但对于引用类型的数据（主要是对象和数组）来说，变量指向数据的内存地址，保存的只是一个指针，const只能保证这个指针是固定不变的，至于它指向的数据结构是不是可变的，就完全不能控制了。

```js
// const + 基本类型（真的“不能改”）
const a = 10
a = 20 // ❌ TypeError: Assignment to constant variable

const obj = {
  name: 'Alice',
  age: 18
}

// const + 引用类型（指针不可变，但内容可变）
// 修改对象内部属性 —— ✅ 可以
obj.age = 20
console.log(obj) 
// { name: 'Alice', age: 20 }

// 重新赋值整个对象 —— ❌ 不可以
obj = {
  name: 'Bob',
  age: 30
}
// TypeError: Assignment to constant variable

const user = Object.freeze({
  name: 'Tom',
  age: 18
})

user.age = 20 // ❌ 严格模式下报错，非严格模式静默失败

function deepFreeze(obj) {
  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === 'object' && obj[key] !== null) {
      deepFreeze(obj[key])
    }
  })
  return Object.freeze(obj)
}


```



### 24. 解释性语言和编译型语言的区别

（1）解释型语言

使用专门的解释器对源程序逐行解释成特定平台的机器码并立即执行。是代码在执行时才被解释器一行行动态翻译和执行，而不是在执行之前就完成翻译。解释型语言不需要事先编译，其直接将源代码解释成机器码并立即执行，所以只要某一平台提供了相应的解释器即可运行该程序。其特点总结如下

- 解释型语言每次运行都需要将源代码解释称机器码并执行，效率较低；
- 只要平台提供相应的解释器，就可以运行源代码，所以可以方便源程序移植；
- JavaScript、Python等属于解释型语言。

（2）编译型语言

使用专门的编译器，针对特定的平台，将高级语言源代码一次性的编译成可被该平台硬件执行的机器码，并包装成该平台所能识别的可执行性程序的格式。在编译型语言写的程序执行之前，需要一个专门的编译过程，把源代码编译成机器语言的文件，如exe格式的文件，以后要再运行时，直接使用编译结果即可，如直接运行exe文件。因为只需编译一次，以后运行时不需要编译，所以编译型语言执行效率高。其特点总结如下：

- 一次性的编译成平台相关的机器语言文件，运行时脱离开发环境，运行效率高；
- 与特定平台相关，一般无法移植到其他平台；
- C、C++等属于编译型语言。

**两者主要区别在于：**前者源程序编译后即可在该平台运行，后者是在运行期间才编译。所以前者运行速度快，后者跨平台性好。

### 23. 强类型语言和弱类型语言的区别

- **强类型语言**：强类型语言也称为强类型定义语言，是一种总是强制类型定义的语言，要求变量的使用要严格符合定义，所有变量都必须先定义后使用。Java和C++等语言都是强制类型定义的，也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，那么它就永远是这个数据类型了。例如你有一个整数，如果不显式地进行转换，你不能将其视为一个字符串。
- **弱类型语言**：弱类型语言也称为弱类型定义语言，与强类型定义相反。JavaScript语言就属于弱类型语言。简单理解就是一种变量类型可以被忽略的语言。比如JavaScript是弱类型定义的，在JavaScript中就可以将字符串'12'和整数3进行连接得到字符串'123'，在相加的时候会进行强制类型转换。

两者对比：强类型语言在速度上可能略逊色于弱类型语言，但是强类型语言带来的严谨性可以有效地帮助避免许多错误。

### 21. use strict是什么意思?使用它区别是什么

use strict 是一种 ECMAscript5 添加的（严格模式）运行模式，这种模式使得 Javascript 在更严格的条件下运行。设立严格模式的目的如下：

- 消除 Javascript 语法的不合理、不严谨之处，减少怪异行为;
- 消除代码运行的不安全之处，保证代码运行的安全；
- 提高编译器效率，增加运行速度；
- 为未来新版本的 Javascript 做好铺垫。

区别：

- 禁止使用 with 语句。
- 禁止 this 关键字指向全局对象。
- 对象不能有重名的属性

### 19. ==ES6 Module与CommonJS模块有什么异同==

**区别： **

- CommonJS是对模块的浅拷⻉，ES6 Module是对模块的引⽤，即ES6 Module只存只读，不能改变其值，也就是指针指向不能变，类似const；
- import的接⼝是read-only（只读状态），不能修改其变量值。 即不能修改其变量的指针指向，但可以改变变量内部指针指向，可以对commonJS对重新赋值（改变指针指向），但是对ES6 Module赋值会编译报错。 

**共同点： **

- CommonJS和ES6 Module都可以对引⼊的对象进⾏赋值，即对对象内部属性的值进⾏改变。

### 4. JavaScript有哪些内置对象

js 中的内置对象主要指的是在程序执行前存在全局作用域里的由 js 定义的一些全局值属性、函数和用来实例化其他对象的构造函数对象。一般经常用到的如全局变量值 NaN、undefined，全局函数如 parseInt()、parseFloat() 用来实例化对象的构造函数如 Date、Object 等，还有提供数学计算的单体内置对象如 Math 对象。

------

## 三、数据类型基础（Type System）

- 值类型和引用类型的区别
- 引用类型有哪些，有什么特点?
- 普通数据类型存储在哪里?堆还是栈?
- JavaScript 中的变量在内存中的具体存储形式是什么?
- JavaScript 对象的底层数据结构是什么?
- JS 中的数组和函数在内存中是如何存储的?
- JS 里面哪些类型是可以互转的?
- Symbol 数据类型特征与实际使用案例
- JS 数据类型里面，Set 和数组分别有哪些适用场景，开发中该。。。

### 1. JavaScript有哪些数据类型，它们的区别？

#### 可分为原始数据类型和引用数据类型

- 栈：Primitive Types 原始数据类型（Undefined、Null、Number、String、Boolean、BigInt、Symbol） 

- 堆：Reference Type 引用数据类型（Object）, Array, Function ...  作为Object的实例

  - Object
    Array
    Function
    Date
    RegExp / Regular expression
    Map / Set
    WeakMap / WeakSet
    Error
    Json

BigInt / Symbol 是“值本身” - 原始类型
Date / RegExp / Error / Set / Map 是“对象能力” - Object

JavaScript 中常见数据类型有Number、String、Boolean、Object、Array、Json、Function、Date、RegExp、Error、undefined、Null等十几种。ES6还有新增的数据类型有BigInt、Symbol、Set、Map等。

### 6. 什么是 Iterable 对象，与 Array 有什么区别

实现了 `[Symbol.iterator]` 属性的对象即是 `Iterable` 对象，然后可以使用操作符 `for...of` 进行迭代

https://javascript.info/iterable

###  24. 为什么会有BigInt的提案？

JavaScript中Number.MAX_SAFE_INTEGER表示最⼤安全数字，计算结果是9007199254740991，即在这个数范围内不会出现精度丢失（⼩数除外）。但是⼀旦超过这个范围，js就会出现计算不准确的情况，这在⼤数计算的时候不得不依靠⼀些第三⽅库进⾏解决，因此官⽅提出了BigInt来解决此问题。

### Symbol BigInt Set Map

- `Symbol` 代表创建后独一无二且不可变的数据类型，它主要是为了解决可能出现的全局变量冲突的问题。 

- `BigInt` 是一种数字类型的数据，它可以表示任意精度格式的整数，使用 BigInt 可以安全地存储和操作大整数，即使这个数已经超出了 Number 能够表示的安全整数范围。

- `Set` 是ES6新增的一种新集合类型，Set 在很多方面都像是加强的Map，这是因为他们的大多数API和行为都是共有的。Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。

- `Map` 是一个带键的数据项的集合，就像一个对象一样。但是它们直接最大的差别是 Map 允许任何类型的键。

### 34. 什么是 TypedArray

[ArrayBuffer，二进制数组](https://zh.javascript.info/arraybuffer-binary-arrays)

### 21. 什么是 JavaScript 中的包装类型

在 JavaScript 中，基本类型是没有属性和方法的，但是为了便于操作基本类型的值，在调用基本类型的属性或方法时 JavaScript 会在后台隐式地将基本类型的值转换为对象，如：

```js
const a = "abc";
a.length; // 3
a.toUpperCase(); // "ABC"
```

在访问`'abc'.length`时，JavaScript 将'abc'在后台转换成`String('abc')`，然后再访问其length属性。 JavaScript也可以使用Object函数显式地将基本类型转换为包装类型：

```js
var a = 'abc'
Object(a) // String {"abc"}
```

也可以使用valueOf方法将包装类型倒转成基本类型：



------

## 四、类型检测 / 判等 / 判空

- JavaScript 有几种方法判断变量的类型(类型检测)?

- isNaN 和 Number.isNaN 函数的区别？
- hasOwnProperty与instanceof 的区别
- Object.prototype.hasOwnProperty()的作用与使用场景
- 如何让一个属性变为 null?
- JavaScript 如何判空:覆盖所有常见“空值”类型
- 判断一个对象是否为空:是否包含原型链上的自定义属性或方。。。


### 2. 数据类型检测方式

#### a. typeof

Array , object , null typeof -> object

缺点：引用类型无法判断

```js
console.log(typeof 2);               // number
console.log(typeof true);            // boolean
console.log(typeof 'str');           // string
console.log(typeof function(){});    // function
console.log(typeof undefined);       // undefined

console.log(typeof {});              // object
console.log(typeof []);              // object    
console.log(typeof null);            // object
```

#### b. instanceof

instanceof可以正确判断对象的类型，其内部运行机制是判断在其原型链中能否找到该类型的原型。

缺点：instanceof只能正确判断引用数据类型，而不能判断基本数据类型。

instanceof 运算符可以用来测试一个对象在其原型链中是否存在一个构造函数的 prototype 属性。

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 

console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

#### c. constructor

constructor有两个作用，一是判断数据的类型，二是对象实例通过 constrcutor 对象访问它的构造函数。需要注意，如果创建一个对象来改变它的原型，constructor就不能用来判断数据类型了

```js
console.log((2).constructor === Number); // true
console.log((true).constructor === Boolean); // true
console.log(('str').constructor === String); // true
console.log(([]).constructor === Array); // true
console.log((function() {}).constructor === Function); // true
console.log(({}).constructor === Object); // true
```

```js
function Fn(){};

Fn.prototype = new Array();

var f = new Fn();

console.log(f.constructor === Fn);    // false
console.log(f.constructor === Array); // true
```

#### d. Object.prototype.toString.call()

Object.prototype.toString.call() 使用 Object 对象的原型方法 toString 来判断数据类型

```js
var a = Object.prototype.toString;
 
console.log(a.call(2));
console.log(a.call(true));
console.log(a.call('str'));
console.log(a.call([]));
console.log(a.call(function(){}));
console.log(a.call({}));
console.log(a.call(undefined));
console.log(a.call(null));
```

同样是检测对象obj调用toString方法，`obj.toString()`的结 果和`Object.prototype.toString.cal(obj)`的结果不一样，这是为什么?

这是因为toString是Object的原型方法，而Array、 Function等类型作为Object的实例,都重写了toString方法。不同的对象类型调用toString方法时，根据原型链的知识，调用的是对应的重写之后的toString方法(function类型返回内容为函数体的字符串，Array类型返回元素组成的字符串)，而不会去调用Object上原型toString方法(返回对象的具体类型)， 所以采用`obj.toString()`不能得到其对象类型，只能将obj转换为字符串类型;因此，在想要得到对象的具体类型时，应该调用Object原型上的toString方法。

#### e. 自创

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

### 3. 检测数组的方式有哪些

```js
Object.prototype.toString.call(obj).slice(8,-1) === 'Array';
obj.__proto__ === Array.prototype;
Array.isArrray(obj);
obj instanceof Array
Array.prototype.isPrototypeOf(obj)
```

### 7. ⚡️检测对象的方式有哪些

```js
Object.prototype.toString.call({}) === '[object Object]'
obj instanceof object
console.log(({}).constructor === Object); // true
```

### 28. typeof 与 instanceof 区别

- `typeof`会返回一个变量的基本类型，`instanceof`返回的是一个布尔值
- `instanceof` 可以准确地判断复杂引用数据类型，但是不能正确判断基础数据类型
- 而` typeof` 也存在弊端，它虽然可以判断基础数据类型（`null` 除外），但是引用数据类型中，除了` function` 类型以外，其他的判断类型都是object

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 
 
console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

### 9. intanceof 操作符的实现原理及实现

instanceof 运算符用于判断构造函数的 prototype 属性是否出现在对象的原型链中的任何位置。

```js
function _instanceof(L, R) {
  if (typeof L !== 'object') return false
  // L : 实例对象
  // R : 构造函数
  let O = R.prototype;
  L = L._proto_;
  while (true) {
    if (L === null) {
      return false;
    }
    if (L === O) {
      return true;
    }
    L = L._proto_;
  }
}

// 测试
function Car(make, model, year) {
  this.make = make
  this.model = model
  this.year = year
}

const auto = new Car('Honda', 'Accord', 1998)
console.log(_instanceof(auto, Car)) // expected output: true

// 测试
console.log(_instanceof([1, 2], Array)) // expected output: true
console.log(_instanceof({ a: 1 }, Object)) // expected output: true

let a = { name: '冯总' }
console.log(instance_of(a, Object));//true
```

```js
function myInstanceof(left, right) {
  // 获取对象的原型
  let proto = Object.getPrototypeOf(left)
  // 获取构造函数的 prototype 对象
  let prototype = right.prototype; 
 
  // 判断构造函数的 prototype 对象是否在对象的原型链上
  while (true) {
    if (!proto) return false;
    if (proto === prototype) return true;
    // 如果没有找到，就继续从其原型上找，Object.getPrototypeOf方法用来获取指定对象的原型
    proto = Object.getPrototypeOf(proto);
  }
}
```

```js
Object.prototype.toString({})       // "[object Object]"
Object.prototype.toString.call({})  // 同上结果，加上call也ok
Object.prototype.toString.call(1)    // "[object Number]"
Object.prototype.toString.call('1')  // "[object String]"
Object.prototype.toString.call(true)  // "[object Boolean]"
Object.prototype.toString.call(function(){})  // "[object Function]"
Object.prototype.toString.call(null)   //"[object Null]"
Object.prototype.toString.call(undefined) //"[object Undefined]"
Object.prototype.toString.call(/123/g)    //"[object RegExp]"
Object.prototype.toString.call(new Date()) //"[object Date]"
Object.prototype.toString.call([])       //"[object Array]"
Object.prototype.toString.call(document)  //"[object HTMLDocument]"
Object.prototype.toString.call(window)   //"[object Window]"
```

### 27. typeof null 的结果是什么，为什么？

typeof null 的结果是Object。 因为历史遗留问题。

在 JavaScript 第一个版本中，所有值都存储在 32 位的单元中，每个单元包含一个小的类型标签(1-3 bits) 以及当前要存储值的真实数据。类型标签存储在每个单元的低位中，共有五种数据类型

```
000: object   - 当前存储的数据指向一个对象。
  1: int      - 当前存储的数据是一个 31 位的有符号整数。
010: double   - 当前存储的数据指向一个双精度的浮点数。
100: string   - 当前存储的数据指向一个字符串。
110: boolean  - 当前存储的数据是布尔值。
```

如果最低位是 1，则类型标签标志位的长度只有一位；如果最低位是 0，则类型标签标志位的长度占三位，为存储其他四种数据类型提供了额外两个 bit 的长度。

有两种特殊数据类型： 

- undefined的值是 (-2)30(一个超出整数范围的数字)； 
- null 的值是机器码 NULL 指针(null 指针的值全是 0) 那也就是说null的类型标签也是000，和Object的类型标签一样，所以会被判定为Object

### 12. typeof NaN 的结果是什么？

NaN 指“不是一个数字”（not a number），NaN 是一个“警戒值”（sentinel value，有特殊用途的常规值），用于指出数字类型中的错误情况，即“执行数学运算没有成功，这是失败后返回的结果”。

```js
typeof NaN; // "number"
```

NaN 是一个特殊值，它和自身不相等，是唯一一个非自反（自反，reflexive，即 `x === x `不成立）的值。而 NaN !== NaN 为 true。

### 13. isNaN 和 Number.isNaN 函数的区别？ 

- 函数 isNaN 接收参数后，会尝试将这个参数转换为数值，任何不能被转换为数值的的值都会返回 true，因此非数字值传入也会返回 true ，会影响 NaN 的判断。 (is not a number 是否 不是数字，不是数字-true, 是数字false)。
- 函数 Number.isNaN 会首先判断传入参数是否为数字，如果是数字再继续判断是否为 NaN ，不会进行数据类型的转换，这种方法对于 NaN 的判断更为准确。

```js
isNaN(1);
isNaN("1");
Number.isNaN("123");
```

### 20. Object.is() 与比较操作符 “=== ”、“ ==” 的区别？ 

- 使用双等号（==）进行相等判断时，如果两边的类型不一致，则会进行强制类型转化后再进行比较。 
- 使用三等号（===）进行相等判断时，如果两边的类型不一致时，不会做强制类型准换，直接返回 false。 
- 使用 Object.is 来进行相等判断时，一般情况下和三等号的判断相同，它处理了一些特殊的情况，比如 -0 和 +0 不再相等，两个 NaN 是相等的。

### 8. null和undefined区别

- 首先 Undefined 和 Null 都是基本数据类型，这两个基本数据类型分别都只有一个值，就是 undefined 和 null。 
- undefined 代表的含义是未定义，null 代表的含义是空对象。一般变量声明了但还没有定义的时候会返回 undefined，null主要用于赋值给一些可能会返回对象的变量，作为初始化。 
- undefined 在 JavaScript 中不是一个保留字，这意味着可以使用 undefined 来作为一个变量名，但是这样的做法是非常危险的，它会影响对 undefined 值的判断。我们可以通过一些方法获得安全的 undefined 值，比如说 void 0。
- 当对这两种类型使用 typeof 进行判断时，Null 类型化会返回 “object”，这是一个历史遗留的问题。当使用双等号对两种类型的值进行比较时会返回 true，使用三个等号时会返回 false。

### 26. 如何判断一个对象是空对象

- 使用JSON自带的JSON.stringify方法来判断：

```js
if (JSON.stringify(Obj) == "{}") {
  console.log("空对象");
}
```

- 使用ES6新增的方法Object.keys()来判断：

```js
if (Object.keys(Obj).length === 0) {
  console.log("空对象");
}
```

- for...in...

```js
function isEmpty(obj) {
  for (var prop in obj) {
    if (obj.hasOwnProperty(prop)) return false;
  }
  return true;
}
```

### 11. 如何获取安全的 undefined 值？ 

因为 undefined 是一个标识符，所以可以被当作变量来使用和赋值，但是这样会影响 undefined 的正常判断。表达式 `void ___ `没有返回值，因此返回结果是 undefined。void 并不改变表达式的结果，只是让表达式不返回值。因此可以用 void 0 来获得 undefined。

------

## 五、类型转换 / 运算规则 / 数值系统

- 常见的位运算符有哪些?其计算规则是什么

### 14. == 操作符的强制类型转换规则？ 

对于 == 来说，如果对比双方的类型不一样，就会进行类型转换。假如对比 x 和 y 是否相同，就会进行如下判断流程： 

1. 首先会判断两者类型是否相同，相同的话就比较两者的大小； 
2. 类型不相同的话，就会进行类型转换； 
3. 会先判断是否在对比 null 和 undefined，是的话就会返回 true 
4. 判断两者类型是否为 string 和 number，是的话就会将字符串转换为 number

```js
1 == '1'
      ↓
1 ==  1
```

5. 判断其中一方是否为 boolean，是的话就会把 boolean 转为 number 再进行判断

```js
'1' == true
        ↓
'1' ==  1
        ↓
 1  ==  1
```

6. 判断其中一方是否为 object 且另一方为 string、number 或者 symbol，是的话就会把 object 转为原始类型再进行判断

```js
'1' == { name: 'js' }
        ↓
'1' == '[object Object]'
```

![image-20251223170348186](https://s2.loli.net/2025/12/23/5FKYnfAQBy146JM.png)

### 15. 谈谈 Javascript 中的类型转换机制

常见的类型转换有：

- 强制转换（显示转换）
- 自动转换（隐式转换）

1. Number()

![image-20251223170419471](https://s2.loli.net/2025/12/23/PV91FpxNB3CSOuW.png)

2. String()

![](https://s2.loli.net/2025/12/23/zmds1t49yDauxMA.png)

3. Boolean()

```js
Boolean(0)      // false
Boolean(1)      // true
Boolean("")     // false
Boolean("abc")  // true
Boolean(null)   // false
Boolean([])     // true
Boolean({})     // true
```

- `+` **操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==` **操作符**

### 22. JavaScript 中如何进行隐式类型转换？

- `+`**操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==`**操作符**

### 35. 隐式转换

`==` 会在比较前，尽量把两边转成“同一类型”，转换顺序是固定的，不是随意的。

运算符优先级：!  >  ==

1. **对象 == 基本类型**，对象先转原始值（ToPrimitive）

   对象转原始值时，JS 会依次调用 `valueOf → toString`，谁先返回原始值就用谁。

   `[]` 的 `valueOf()` 返回的仍是对象，所以最终使用了 `toString()` 的字符串结果。

2. **布尔值 == 其他类型**，布尔转数字（true → 1，false → 0）

3. **字符串 == 数字**，字符串转数字

```js
// 运算符优先级：!  >  ==
[] == (![])
// next positon
[] == false
// 对象 → 原始值（ToPrimitive）完整流程
// 对象转原始值（ToPrimitive）可以是 number / string / symbol，取决于转换规则和调用顺序。
// 当发生：对象 == 基本类型，JS 会对对象执行 ToPrimitive(obj, hint)。
// hint 有三种可能：number, string, default
// 执行顺序如下
1. obj[Symbol.toPrimitive]（如果有）
2. obj.valueOf()
3. obj.toString()
// 不是 JS 偏爱 string，而是 valueOf() 没给出原始值，toString() 给了
[].valueOf() // []
[].toString() // ""

```

| 优先级 | 类型       | 运算符                               | 说明 / 易错点         |
| ------ | ---------- | ------------------------------------ | --------------------- |
| 1      | 分组       | `()`                                 | 括号最高优先级        |
| 2      | 一元运算符 | `!` `+` `-` `typeof` `void` `delete` | `!` 比 `==` 高        |
| 3      | 指数       | `**`                                 | 右结合：`2 ** 3 ** 2` |
| 4      | 乘除取余   | `*` `/` `%`                          | 高于 `+ -`            |
| 5      | 加减       | `+` `-`                              | `+` 可能是字符串拼接  |
| 6      | 关系       | `<` `>` `<=` `>=` `in` `instanceof`  | 比 `==` 高            |
| 7      | 相等       | `==` `!=` `===` `!==`                | 隐式类型转换发生点    |
| 8      | 逻辑与     | `&&`                                 |                       |
| 9      | 逻辑或     | `||`                                 |                       |
| 10     | 三元       | `?:`                                 | 低于逻辑运算          |
| 11     | 赋值       | `=` `+=` `-=` `*=` `                 |                       |
| 12     | 逗号       | `,`                                  | 最低                  |

### 16. 其他值到字符串的转换规则

1. Null 和 Undefined 类型 ，null 转换为 "null"，undefined 转换为 "undefined"， 
2. Boolean 类型，true 转换为 "true"，false 转换为 "false"。 
3. Number 类型的值直接转换，不过那些极小和极大的数字会使用指数形式。
4. Symbol 类型的值直接转换，但是只允许显式强制类型转换，使用隐式强制类型转换会产生错误。 
5. 对普通对象来说，除非自行定义 toString() 方法，否则会调用 toString()（Object.prototype.toString()）来返回内部属性 [[Class]] 的值，如"[object Object]"。如果对象有自己的 toString() 方法，字符串化时就会调用该方法并使用其返回值。

### 17. 其他值到数字值的转换规则

1. Null 类型的值转换为 0。 
2. Undefined 类型的值转换为 NaN。 
3. Boolean 类型的值，true 转换为 1，false 转换为 0。 
4. String 类型的值转换如同使用 Number() 函数进行转换，如果包含非数字值则转换为 NaN，空字符串为 0。 
5. Symbol 类型的值不能转换为数字，会报错。 
6. 对象（包括数组）会首先被转换为相应的基本类型值，如果返回的是非数字的基本类型值，则再遵循以上规则将其强制转换为数字。

为了将值转换为相应的基本类型值，抽象操作 ToPrimitive 会首先（通过内部操作 DefaultValue）检查该值是否有valueOf()方法。如果有并且返回基本类型值，就使用该值进行强制类型转换。如果没有就使用 toString() 的返回值（如果存在）来进行强制类型转换。 如果 valueOf() 和 toString() 均不返回基本类型值，会产生 TypeError 错误。

### 18. 其他值到布尔类型的值的转换规则？ 

以下这些是假值： 

1. undefined 

2. null 

3. false 

4. +0、-0 和 NaN

5. ""

假值的布尔强制类型转换结果为 false。从逻辑上说，假值列表以外的都应该是真值。

### 23. + 操作符什么时候用于字符串的拼接？ 

简单来说就是，如果 + 的其中一个操作数是字符串（或者通过以上步骤最终得到字符串），则执行字符串拼接，否则执行数字加法。 那么对于除了加法的运算符来说，只要其中一方是数字，那么另一方就会被转为数字。

### 19. || 和 && 操作符的返回值？

|| 和 && 首先会对第一个操作数执行条件判断，如果其不是布尔值就先强制转换为布尔类型，然后再执行条件判断。 

**逻辑或（||）总结：**

1. 只要第一个值的布尔值为false，那么永远返回第二个值。
2. 逻辑或属于短路操作，第一个值为true时，不再操作第二个值，且返回第一个值。

**逻辑与（&&）总结：**

1. 只要第一个值的布尔值为true，那么永远返回第二个值。
2. 逻辑与属于短路操作，第一个值为false时，不再操作第二个值，且返回第一个值。

```js
// 只要第一个值的布尔值为false，那么永远返回第二个值，不管第二个值的布尔值是true还是false。
console.log(0 || '我是string，boolean值为true');          // 返回字符串
console.log(NaN || '我是string，boolean值为true');        // 返回字符串
console.log('' || '我是string，boolean值为true');         // 返回字符串
console.log(null || '我是string，boolean值为true');       // 返回字符串
console.log(undefined || '我是string，boolean值为true');  // 返回字符串
console.log(0 || 'NaN');           // 返回 NaN
console.log(NaN || '');            // 返回 '' 空字符串
console.log('' || null);           // 返回 null
console.log(null || 'undefined');  // 返回 undefined
console.log(undefined || 0);       // 返回 0

// 逻辑或短路操作
var obj = {};
console.log(obj || NaN);      // 返回 obj
console.log(obj || number);   // 返回 obj
console.log( 0 || number);    // 报错，number未定义
// 只要第一个值的布尔值为true，不再操作第二个值，直接返回第一个值，number变量未定义也不会报错。
```

```js
var obj = {};
var str = 'Riny';

/* 当第一个值的布尔值为true 返回第二个值 */
console.log(obj && 0);          // 返回 0
console.log(obj && NaN);        // 返回 NaN
console.log(obj && '');         // 返回 '' 空字符串
console.log(obj && undefined);  // 返回 undefined
console.log(obj && null);       // 返回 null

/* 当第一个值的布尔值为true 返回第二个值 */
console.log(obj && str);        // 返回 字符串
```

```js
const a = 3;
const b = -2;

console.log(a > 0 && b > 0);
```

### 10. 为什么`0.1+0.2 ! == 0.3`，如何让其相等

JavaScript 的 `Number` 使用 **64 位双精度浮点数（double）**，尾数是**有限长度的二进制**，小数无法用有限二进制精确表示时，会发生**舍入误差**

因为 JavaScript 使用 IEEE 754 浮点数 Floating Point Number，0.1 和 0.2 在二进制中是无限循环小数，只能近似存储，导致相加产生精度误差。

`0.2 + 0.2 === 0.4` 成立，是因为浮点舍入后恰好等于 0.4；

**金额或者电商场景**，我会把金额转成整数去算，比如用“分”代替“元”，避免小数精度问题。

**比较大小的时候**，不会直接用 `===`，会用一个误差范围，可以用 `Number.EPSILON` 来判断。/ˈep.sə.lɑːn/

**UI 展示**的时候，为了好看，会用 `toFixed` 四舍五入显示，但注意这是展示，不影响计算精度。

**金融或者利率等高精度计算**，我会用专门的高精度库，比如 `decimal.js`。

**普通的计算**，如果不涉及精确要求，就直接接受浮点数的误差。

如果**数值超过安全整数范围**，为了避免精度丢失，会使用 `BigInt`。”

| 场景                       | 推荐方案             |
| -------------------------- | -------------------- |
| 金额 / 电商                | 整数化               |
| 比较大小                   | epsilon              |
| UI 显示                    | toFixed              |
| 金融 / 利率                | 高精度库             |
| 普通计算                   | 接受误差             |
| 超过安全整数就可能丢失精度 | 可以用 `BigInt` 替代 |

[Javascript 数字精度丢失的问题](https://vue3js.cn/interview/JavaScript/loss_accuracy.html#%E4%B8%80%E3%80%81%E5%9C%BA%E6%99%AF%E5%A4%8D%E7%8E%B0)

计算机是通过二进制的方式存储数据的，所以计算机计算0.1+0.2的时候，实际上是计算的两个数的二进制的和。

0.1，0.2 表示为二进制会有精度的损失，比较时可引入一个很小的数值 `Number.EPSILON` 容忍误差，其值为 2^-52。

在ES6中，提供了`Number.EPSILON`属性，而它的值就是2^-52.

Number.MAX_SAFE_INTEGER = 2^53 - 1
Number.MIN_SAFE_INTEGER = -(2^53 - 1)

判断`0.1 + 0.2 - 0.3`是否小于`Number.EPSILON`，如果小于，就可以判断为`0.1 + 0.2 === 0.3`

```js
function equal(a, b) {
  return Math.abs(a - b) < Number.EPSILON;
}

console.log(numberepsilon(0.1 + 0.2, 0.3)); // true
```

```js
// 金额统一用“分”
const price1 = 10; // 0.1 元 → 10 分
const price2 = 20; // 0.2 元 → 20 分

(price1 + price2) / 100; // 0.3

// 比较大小
function isEqual(a, b, epsilon = Number.EPSILON) {
  return Math.abs(a - b) < epsilon;
}

isEqual(0.1 + 0.2, 0.3); // true

// 比较时引入误差容忍（epsilon）
function isEqual(a, b, epsilon = Number.EPSILON) {
  return Math.abs(a - b) < epsilon;
}

isEqual(0.1 + 0.2, 0.3); // true

// 结果取舍（toFixed / Math.round）
(0.1 + 0.2).toFixed(2); // "0.30"
Math.round((0.1 + 0.2) * 100) / 100; // 0.3

// 使用高精度库
import Decimal from 'decimal.js';
new Decimal(0.1).plus(0.2).toNumber();
// 0.3


```

### 31. Number 中最大数、最大安全整数、EPSILON 都是多少，原理是什么

| 常量                      | 值                        | 含义 / 原理                                   |
| ------------------------- | ------------------------- | --------------------------------------------- |
| `Number.MAX_VALUE`        | 1.7976931348623157e+308   | JS 能表示的最大正数，超过就是 Infinity        |
| `Number.MAX_SAFE_INTEGER` | 9007199254740991 (2^53-1) | JS 能安全表示的最大整数，超过可能精度丢失     |
| `Number.EPSILON`          | 2.220446049250313e-16     | JS 能表示的最小浮点间隔，1 与最小可分辨数的差 |



------

## 六、Array（数组）

### 4. 数组常用的方法

会影响原数组 ⭕️，不会影响原数组 ❌。✅ 会返回「新数组」的

1. 操作方法

   - 增

     - `push()`: 方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度 ⭕️
     - `unshift()`: 在数组开头添加任意多个值，然后返回新的数组长度 ⭕️
     - `splice()`: 传入三个参数，分别是开始位置、0（要删除的元素数量）、插入的元素，返回空数组 ⭕️
     - `concat()`: 首先会创建一个当前数组的副本，然后再把它的参数添加到副本末尾，最后返回这个新构建的数组 ❌✅

   - 删

     - `pop()`: 用于删除数组的最后一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `shift()`: 用于删除数组的第一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `splice()`: 传入两个参数，分别是开始位置，删除元素的数量，返回包含删除元素的数组，开始位置不会被删除 ⭕️
     - `slice()`: 不影响原数组：创建一个包含原有数组中一个或多个元素的新数组 ❌✅

   - 改

     `splice()`: 传入三个参数，分别是开始位置，要删除元素的数量，要插入的任意多个元素，返回删除元素的数组，对原数组产生影响 ⭕️

   - 查

     - `indexOf()`: 返回要查找的元素在数组中的位置，如果没找到则返回 -1❌
     - `includes()`: 返回要查找的元素在数组中的位置，找到返回`true`，否则`false` ❌
     - `find()`: 返回第一个匹配的元素 ❌
     - `findIndex()`: ❌

2. 转换方法：`join()`: 接收一个参数，即字符串分隔符，返回包含所有项的字符串 ❌

3. 排序方法：

   - `reverse()`: 顾名思义，将数组元素方向反转 ⭕️
   - `sort()`: 接受一个比较函数，用于判断哪个值应该排在前面 ⭕️

4. 迭代/遍历方法

- `some()`: 对数组每一项都运行传入的函数，如果有一项函数返回 true ，则这个方法返回 true ❌

- `every()`: 对数组每一项都运行传入的函数，如果对每一项函数都返回 true ，则这个方法返回 true ❌

- `forEach()`: 对数组每一项都运行传入的函数，没有返回值 ❌

- `filter()`: 对数组每一项都运行传入的函数，函数返回 `true` 的项会组成数组之后返回 ❌✅

- `map()`: 对数组每一项都运行传入的函数，返回由每次函数调用的结果构成的数组 ❌✅

- `reduce()`: 对数组中的每个元素按序执行一个由您提供的 reducer 函数，每一次运行 reducer 会将先前元素的计算结果作为参数传入，最后将其结果汇总为单个返回值。❌

### 5. 数组遍历方法

`forEach`、`map`共同点：

1. 只能遍历数组并参数都一样
2. 不改变原函数（引用类型除外）
3. 无法中断循环；return 只是结束本地循环，进入下一次循环
4. break 或 continue 都将会报错

| **方法**                      | **是否改变原数组** | **特点**                                                     |
| ----------------------------- | ------------------ | ------------------------------------------------------------ |
| `forEach()`                   | 否                 | 数组方法，不改变原数组，没有返回值。                         |
| `map()`                       | 否                 | 数组方法，不改变原数组，有返回值，可链式调用。               |
| `filter()`                    | 否                 | 数组方法，过滤数组，返回包含符合条件的元素的数组，可链式调用 |
| `for...of...`                 | 否                 | for...of遍历具有Iterator迭代器的对象的属性，返回的是数组的元素、对象的属性值，不能遍历普通的obj对象，将异步循环变成同步循环 |
| `every()` 和 `some()`         | 否                 | 数组方法，some()只要有一个是true，便返回true；而every()只要有一个是false，便返回false. |
| `find()` 和 `findIndex()`     | 否                 | 数组方法，find()返回的是第一个符合条件的值；findIndex()返回的是第一个返回条件的值的索引值 |
| `reduce()` 和 `reduceRight()` | 否                 | 数组方法，reduce()对数组正序操作；reduceRight()对数组逆序操作 |

### 5. forEach() / map() / for...of forof跳出循环

`map` / `forEach` 里不能用 `break` 和 `continue`，因为它们是回调函数，不是循环语句；如果需要中断遍历，应使用 `for...of`、`some` 或 `every`。

在 forEach 中，不能使用 continue 和 break ，都会报错。可以使用 return 或 return false 跳出循环，但是效果与 for 中 continue 一样。 这种方法无法一次结束所有循环。`map` 内部是一个 **函数作用域**回调函数 ≠ 循环体

| 方法        | 能 break  | 能 continue | 说明          |
| ----------- | --------- | ----------- | ------------- |
| for / while | ✅         | ✅           | 传统循环      |
| for...of    | ✅         | ✅           | 推荐          |
| forEach     | ❌         | ❌           | 回调函数      |
| map         | ❌         | ❌           | 映射          |
| filter      | ❌         | ❌           | 筛选          |
| some        | ✅（自动） | ❌           | 遇 true 结束  |
| every       | ✅（自动） | ❌           | 遇 false 结束 |

```js
for (初始化; 条件; 每次循环后的操作) {
  // 循环体
}

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}

let i = 1;

while (true) {
  if (i === 4) {
    break;
  }
  console.log(i);
  i++;
}

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // 跳过当前这一次循环
  }
  console.log(i);
} // 1 2 4 5
```

如何在forEach/map中跳出循环的总结：

1. 使用抛出异常来中断 forEach/map
2. 使用别的循环代替
   - 使用传统 for 循环
   - 使用数组 every/some 循环

forEach/map 中使用循环的注意事项:

1. 碰到需要终止的循环，避免使用 forEach 可以使用 for/for in循环
2. es6针对数组可以使用 every/some/find等方式
3. forEach/map 循环只能通 return 中断当次循环无法跳出循环
4. forEach/map 循环中使用 continue/break 报错
5. 如果非要使用 forEach/map 中断循环使用抛出异常

注意

- for/for...of： break跳出本次循环；continue结束本次循环执行下一次循环，没有return。
- for...in：会忽略break || continue。没有return。

```js
try{
    [1,2,3,4,5,6].forEach((val, index)=> {
        console.log(val);
        if(val === 3) {
        	console.log('满足条件后的操作');
            throw new Error();
        }
        console.log('满足条件后不再执行', val)
    })
}catch(e) {
   console.log('可以不处理');
}
console.log('继续执行');
```

- `forEach()`

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.forEach(x => {
  if (x === 4) {
    return;
  }
  newArr.push(x * 2);
});

```

在 forEach 中，不能使用 continue 和 break ，可以使用 return 或 return false 跳出循环，效果与 for 中 continue 一样。 注意该方法无法一次结束所有循环。

使用 `forEach()` 方法遍历了数组中的每一项，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `return` 语句，==跳出回调函数，并继续执行 `forEach()` 方法的下一次迭代。==(只是跳出，没有结束)

是因为 `forEach()` 方法有一个特定的用途，即对数组中的每一项执行一个操作。它不是一个循环，==所以不能使用 `break` 或 `continue` 语句来控制循环的执行。== ==Uncaught SyntaxError: Illegal break statement==

如果你想要在 `forEach()` 方法中使用 `break` 语句，那么你可以使用 `some()` 方法代替。`some()` 方法也会迭代数组的每一项，并对每一项执行一个回调函数。但是，它会在回调函数返回 `true` 的时候终止循环，并返回 `true`。

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.some(x => {
  if (x === 4) {
    return true;
  }
  newArr.push(x * 2);
});
```

- `map()`

在 `map()` 方法的回调函数中使用 `break` 语句是不合法的。这是因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。它不是一个循环，所以不能使用 `break` 或 `continue` 语句来控制循环的执行。

如果你想要在 `map()` 方法中使用 `break` 语句，那么你可以使用一个普通的循环代替。

```js
const arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
  const newArr = arr.map(x => {
    if (x === 4) {
      break; // Uncaught SyntaxError: Illegal break statement
      // continue // Uncaught SyntaxError: Illegal continue statement: no surrounding iteration statement
    }
    return x * 2;
  });
}
```

在这个例子中，我们在一个循环中调用了 `map()` 方法，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `break` 语句，终止循环。

但是，这种方法并不是很好，因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。如果你想要终止循环，那么更好的方法是使用 `for` 循环或者 `forEach()` 方法，而不是 `map()` 方法。

- for...of...

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

for (let i = 0; i < arr.length; i++) {
  if (arr[i] === 4) {
    break;
  }
  newArr.push(arr[i] * 2);
}
```

### 6. 扩展运算符的作用

#### 和rest参数的区别：

- **当用在函数定义时的形参前面时，称为rest参数；当函数调用时，用于接收不确定的参数。**
- **当与解构赋值组合使用时，称为rest参数，用于接收剩余的值,存储在数组中。**
- **当用在字符串或数组前面时称为扩展运算符，将数组或字符串进行拆解。**

```js
// 1. 对象扩展运算符: 复制，或者覆盖原有的属性
let bar = { a: 1, b: 2 };
let baz = { ...bar }; // { a: 1, b: 2 }

// 2. 数组扩展运算符: 可以展开数组，但是只能展开一层
console.log(...[1, 2, 3]) // 1 2 3
console.log(...[1, [2, 3, 4], 5]) // 1 [2, 3, 4] 5

// 3. 将数组转换为参数序列
function add(x, y) {
  return x + y;
}
const numbers = [1, 2];
add(...numbers) // 3

// 4. 合并数组
const arr1 = ['two', 'three'];
const arr2 = ['one', ...arr1, 'four', 'five']; // ["one", "two", "three", "four", "five"]

// 5. 扩展运算符与解构赋值结合起来，用于生成数组
const [first, ...rest] = [1, 2, 3, 4, 5];
first // 1
rest  // [2, 3, 4, 5]

// 如果将扩展运算符用于数组赋值，只能放在参数的最后一位，否则会报错
const [...rest, last] = [1, 2, 3, 4, 5];         // 报错
const [first, ...rest, last] = [1, 2, 3, 4, 5];  // 报错

// 6. 将类数组转化为真正的数组
// arguments对象 用于替换es5中的Array.prototype.slice.call(arguments)写法。
function foo() {
  const args = [...arguments];
}
```

### 8. 对象与数组的解构的理解

```js
const [a, b, c] = [1, 2, 3]

const stu = {
  name: 'Bob',
  age: 24
}
const { name, age } = stu
```



- 数组里面有10万个数据，取第一个元素和第10万个元素的时间。。
- 常见数组排序算法及其特点
- 如何实现数组的随机打乱

------

## 七、Object（对象操作）

### 31. Object.keys() 与 Object.getOwnPropertyNames()有何区别

- `Object.keys`: 列出可枚举的属性值
- `Object.getOwnPropertyNames`: 列出所有属性值(包括可枚举与不可枚举)

### 32. 如何把对象转化为 key/value 的二维数组

**方法一：**

`Object.entries({ a: 3 });`

**方法二：**

```js
const obj = {
  city: "New Delhi",
  maxTemp: 32,
  minTemp: 21,
  humidity: 78,
  aqi: 456,
  day: "Tuesday"
};

const objectToArray = (obj = {}) => {
  const res = [];
  const keys = Object.keys(obj);
  for (key of keys) {
    res.push([key, obj[key]]);
  }
  
  return res;
};

console.log(objectToArray(obj));
```

### 25. object.assign和扩展运算法是深拷贝还是浅拷贝，两者区别/合并对象

1. 扩展运算符

```js
let outObj = {
  inObj: {a: 1, b: 2}
}
let newObj = {...outObj}
newObj.inObj.a = 2
console.log(outObj) // {inObj: {a: 2, b: 2}}
```

2. Object.assign():

```js
let outObj = {
  inObj: {a: 1, b: 2}
}
let newObj = Object.assign({}, outObj)
newObj.inObj.a = 2
console.log(outObj) // {inObj: {a: 2, b: 2}}
```

可以看到，两者都是浅拷贝。 

- `Object.assign()`方法接收的第一个参数作为目标对象，后面的所有参数作为源对象。然后把所有的源对象合并到目标对象中。它会修改了一个对象，因此会触发 ES6 setter。 
- 扩展操作符（…）使用它时，数组或对象中的每一个值都会被拷贝到一个新的数组或对象中。它不复制继承的属性或类的属性，但是它会复制ES6的 symbols 属性。

### 33. 在 JS 中如何监听 Object 某个属性值的变化

[这章节对`Object.defineProperty`和`Proxy`有相关讲解](# 1. Vue的基本原理)

在 JS 中可以使用两种方式监听属性值变化

- Proxy
- Object.defineProperty

### 1. 对象创建的方式有哪些?

| 方式                    | 特点           | 典型场景           |
| ----------------------- | -------------- | ------------------ |
| 对象字面量 `{}`         | 简洁，最常用   | 普通对象           |
| `Object.create(proto)`  | 指定原型       | 原型继承、纯净对象 |
| 构造函数 + `new`        | 传统 OOP       | 面向对象实例       |
| ES6 class               | 语法糖、继承   | 面向对象、继承结构 |
| 工厂函数                | 每次返回新对象 | 模块化、组合式对象 |
| `Object.assign`         | 属性拷贝       | 合并对象或浅拷贝   |
| `new Object()`          | 等价 `{}`      | 少用               |
| `JSON.parse`            | 从字符串创建   | 数据解析           |
| `Object.setPrototypeOf` | 动态改变原型   | 特殊继承需求       |

### 2. 对象继承的方式有哪些?

| 继承方式            | 优点                           | 缺点                   | 适用场景             |
| ------------------- | ------------------------------ | ---------------------- | -------------------- |
| 原型链继承          | 方法共享                       | 属性共享问题，无法传参 | 简单继承             |
| 构造函数继承        | 可传参，属性独立               | 方法不共享             | 继承实例属性         |
| 组合继承            | 方法共享 + 属性独立            | 父类构造函数被调用两次 | 传统 ES5 面向对象    |
| 寄生继承            | 可扩展                         | 方法不共享             | 灵活继承             |
| 寄生组合继承        | 最优 ES5 继承                  | 需要写辅助函数         | 推荐 ES5 继承        |
| ES6 class + extends | 语法简洁，方法共享，支持 super | 需要 ES6 环境          | ES6 面向对象         |
| Object.create       | 不调用构造函数，简单原型继承   | 属性继承有限           | 原型式继承，纯粹对象 |

### 9. 如何提取高度嵌套的对象里的指定属性

可以用解构

```js
const school = {
   classes: {
      stu: {
         name: 'Bob',
         age: 24,
      }
   }
}
const { classes: { stu: { name } }} = school
```

### 12. 深拷贝和浅拷贝

- 浅拷贝是拷贝一层，属性为对象时，浅拷贝是复制，两个对象指向同一个地址
- 深拷贝是递归拷贝深层次，属性为对象时，深拷贝是新开栈，两个对象指向不同的地址

<mark>浅拷贝</mark>，如果属性是基本类型，拷贝的就是基本类型的值。如果属性是引用类型，拷贝的就是内存地址，即浅拷贝是拷贝一层，深层次的引用类型则共享内存地址。

- `Object.assign`
- `Array.prototype.slice()`, `Array.prototype.concat()`
- 使用拓展运算符实现的复制

<mark>深拷贝</mark>，深拷贝开辟一个新的栈，两个对象属性完成相同，但是对应两个不同的地址，修改一个对象的属性，不会改变另一个对象的属性。

常见的深拷贝方式有：

- _.cloneDeep()
- jQuery.extend()
- JSON.stringify()
- 手写循环递归





- Object 对象有哪些 api?
- 对象取值中 a.b.c.d 和 a['b’['c’】['d']有什么区别?
- 防止对象被篡改的常用方式
- 如何冻结一个 JavaScript 对象

------

## String

```js
var a = 'abc'
var b = Object(a)
var c = b.valueOf() // 'abc'
```

```js
var a = new Boolean( false );
if (!a) {
	console.log( "Oops" ); // never runs
}
```

### 6. 字符串的操作方法

`slice(start, end)` 里如果 `end` 是负数，表示：`字符串.length + end`

| 方法                      | 一句话                         |
| ------------------------- | ------------------------------ |
| **slice(start, end)**     | 按索引区间切（最推荐 ✅）       |
| **substr(start, length)** | 从 start 取 length（已废弃 ❌） |
| **substring(start, end)** | 按区间切，但会自动“纠正”参数   |

| 对比点           | slice         | substr   | substring     |
| ---------------- | ------------- | -------- | ------------- |
| 第二个参数       | end（不包含） | length   | end（不包含） |
| 是否支持负数     | ✅ 支持        | ⚠️ 不可靠 | ❌ 不支持      |
| start > end      | 返回空        | 正常取   | **自动交换**  |
| 是否修改原字符串 | ❌             | ❌        | ❌             |
| 标准状态         | ✅ 推荐        | ❌ 已废弃 | ✅ 仍可用      |

1. 操作方法

   - 增

     - concat():用于将一个或多个字符串拼接成一个新字符串

   - 删

     这里的删的意思并不是说删除原字符串的内容，而是创建字符串的一个副本，再进行操作

     `substr()` 已废弃，不建议再用，新代码只用 `substring()` 或 `slice()`，都只传1-2个参数

     - slice()
     - substr()
     - substring() 

     ```js
     const str = "abcdef";
     
     str.slice(1, 4);      // "bcd"
     str.substring(1, 4); // "bcd"
     str.substr(1, 3);    // "bcd"
     
     // 第二个参数含义不同（关键）
     str.slice(1, 4);    // 1 → 4 // "bcd"
     str.substring(1,4);// 1 → 4 // "bcd"
     str.substr(1,4);   // 从 1 开始取 4 个 // "bcde"
     
     
     // 负数的差异（最重要）
     str.slice(-3);      // "def"
     str.substring(-3); // "abcdef"（负数当 0）
     str.substr(-3);    // ❌ 行为不稳定（不推荐）
     
     // start > end 的情况（面试常考）
     str.slice(4, 1);      // ""
     str.substring(4, 1); // "bcd" **自动交换**...
     
     // 只传一个参数
     str.slice(2);      // "cdef"
     str.substring(2); // "cdef"
     str.substr(2);    // "cdef"
     
     str.slice(-2); // "ef" ✅ 推荐
     
     'abcdef'.slice(1, -1);  // 'bcde'
     'abcdef'.slice(0, -2);  // 'abcd'
     'abcdef'.slice(-3);     // 'def'
     'abcdef'.slice(-3, -1); // 'de'
     ```

   - 改

     - trim()、trimLeft()、trimStart()、trimRight()、trimEnd()
     - repeat()
     - padStart()、padEnd()
     - toLowerCase()、 toUpperCase()

   - 查

     - chatAt():返回给定索引位置的字符，由传给方法的整数参数指定
     - indexOf():从字符串开头去搜索传入的字符串，并返回位置（如果没找到，则返回 -1 ）
     - startWith():从字符串中搜索传入的字符串，并返回一个表示是否包含的布尔值
     - includes():从字符串中搜索传入的字符串，并返回一个表示是否包含的布尔值

2. 转换方法

   - Split:把字符串按照指定的分割符，拆分成数组中的每一项

3. 模版匹配方法

   - match():接收一个参数，可以是一个正则表达式字符串，也可以是一个`RegExp`对象，返回数组
   - search():接收一个参数，可以是一个正则表达式字符串，也可以是一个`RegExp`对象，找到则返回匹配索引，否则返回 -1
   - replace():接收两个参数，第一个参数为匹配的内容，第二个参数为替换的元素（可用函数

### 7. js 如何全部替代一个子串为另一个子串

假设有一个字符串 `hello. hello. hello.` 需要替换为 `AAA`，即把 `hello.` 替换为 `A`

- `str.split('foo').join('bar')`
- `str.replaceAll('foo', 'bar')`，在 `ESNext` 中，目前支持性不好



## 八、Map / Set / WeakMap / WeakSet

### 2. Map和Object的区别

|          | Map                                                          | Object                                                       |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 意外的键 | Map默认情况不包含任何键，只包含显式插入的键。                | Object 有一个原型, 原型链上的键名有可能和自己在对象上的设置的键名产生冲突。 |
| 键的类型 | Map的键可以是任意值，包括函数、对象或任意基本类型。          | Object 的键必须是 String 或是Symbol。                        |
| 键的顺序 | Map 中的 key 是有序的。因此，当迭代的时候， Map 对象以插入的顺序返回键值。 | Object 的键是无序的                                          |
| Size     | Map 的键值对个数可以轻易地通过size 属性获取                  | Object 的键值对个数只能手动计算                              |
| 迭代     | Map 是 iterable 的，所以可以直接被迭代。                     | 迭代Object需要以某种方式获取它的键然后才能迭代。             |
| 性能     | 在频繁增删键值对的场景下表现更好。                           | 在频繁添加和删除键值对的场景下未作出优化。                   |

### 3. Map和WeakMap的区别

- Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。
- WeakMap 结构与 Map 结构类似，也是用于生成键值对的集合。但是 WeakMap 只接受对象作为键名（ null 除外），不接受其他类型的值作为键名。而且 WeakMap 的键名所指向的对象，不计入垃圾回收机制。

**==Map==**

本质上就是键值对的集合，实际上Map是一个数组，它的每一个数据也都是一个数组。

```js
const map = [
  ["name", "张三"],
  ["age", 18]
];

const map = new Map([
  ["foo", 1],
  ["bar", 2]
]);

```

Map数据结构有以下操作方法：

- **size**： `map.size` 返回Map结构的成员总数。
- **set(key,value)**：设置键名key对应的键值value，然后返回整个Map结构，如果key已经有值，则键值会被更新，否则就新生成该键。（因为返回的是当前Map对象，所以可以链式调用）
- **get(key)**：该方法读取key对应的键值，如果找不到key，返回undefined。
- **has(key)**：该方法返回一个布尔值，表示某个键是否在当前Map对象中。
- **delete(key)**：该方法删除某个键，返回true，如果删除失败，返回false。
- **clear()**：map.clear()清除所有成员，没有返回值。

Map结构原生提供是三个遍历器生成函数和一个遍历方法

- keys()：返回键名的遍历器。
- values()：返回键值的遍历器。
- entries()：返回所有成员的遍历器。
- forEach()：遍历Map的所有成员。

**==WeakMap==**

WeakMap 对象也是一组键值对的集合，其中的键是弱引用的。其键必须是对象，原始数据类型不能作为key值，而值可以是任意的。

该对象也有以下几种方法：

- **set(key,value)**：设置键名key对应的键值value，然后返回整个Map结构，如果key已经有值，则键值会被更新，否则就新生成该键。（因为返回的是当前Map对象，所以可以链式调用）
- **get(key)**：该方法读取key对应的键值，如果找不到key，返回undefined。
- **has(key)**：该方法返回一个布尔值，表示某个键是否在当前Map对象中。
- **delete(key)**：该方法删除某个键，返回true，如果删除失败，返回false。

其clear()方法已经被弃用，所以可以通过创建一个空的WeakMap并替换原对象来实现清除。

WeakMap的设计目的在于，有时想在某个对象上面存放一些数据，但是这会形成对于这个对象的引用。一旦不再需要这两个对象，就必须手动删除这个引用，否则垃圾回收机制就不会释放对象占用的内存。

而WeakMap的**键名所引用的对象都是弱引用**，即垃圾回收机制不将该引用考虑在内。因此，只要所引用的对象的其他引用都被清除，垃圾回收机制就会释放该对象所占用的内存。也就是说，一旦不再需要，WeakMap 里面的**键名对象和所对应的键值对会自动消失，不用手动删除引用**。





- WeakSet 是什么数据结构及其应用场景
- ES6 中的 Set 对象该如何遍历
- JavaScript 中 Map 与 Object 的适用场景及抉择

------

## 九、Iterator / 遍历协议

### 5. forEach() / map() / for...of forof跳出循环

`map` / `forEach` 里不能用 `break` 和 `continue`，因为它们是回调函数，不是循环语句；如果需要中断遍历，应使用 `for...of`、`some` 或 `every`。

在 forEach 中，不能使用 continue 和 break ，都会报错。可以使用 return 或 return false 跳出循环，但是效果与 for 中 continue 一样。 这种方法无法一次结束所有循环。`map` 内部是一个 **函数作用域**回调函数 ≠ 循环体

| 方法        | 能 break  | 能 continue | 说明          |
| ----------- | --------- | ----------- | ------------- |
| for / while | ✅         | ✅           | 传统循环      |
| for...of    | ✅         | ✅           | 推荐          |
| forEach     | ❌         | ❌           | 回调函数      |
| map         | ❌         | ❌           | 映射          |
| filter      | ❌         | ❌           | 筛选          |
| some        | ✅（自动） | ❌           | 遇 true 结束  |
| every       | ✅（自动） | ❌           | 遇 false 结束 |

```js
for (初始化; 条件; 每次循环后的操作) {
  // 循环体
}

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}

let i = 1;

while (true) {
  if (i === 4) {
    break;
  }
  console.log(i);
  i++;
}

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // 跳过当前这一次循环
  }
  console.log(i);
} // 1 2 4 5
```

如何在forEach/map中跳出循环的总结：

1. 使用抛出异常来中断 forEach/map
2. 使用别的循环代替
   - 使用传统 for 循环
   - 使用数组 every/some 循环

forEach/map 中使用循环的注意事项:

1. 碰到需要终止的循环，避免使用 forEach 可以使用 for/for in循环
2. es6针对数组可以使用 every/some/find等方式
3. forEach/map 循环只能通 return 中断当次循环无法跳出循环
4. forEach/map 循环中使用 continue/break 报错
5. 如果非要使用 forEach/map 中断循环使用抛出异常

注意

- for/for...of： break跳出本次循环；continue结束本次循环执行下一次循环，没有return。
- for...in：会忽略break || continue。没有return。

```js
try{
    [1,2,3,4,5,6].forEach((val, index)=> {
        console.log(val);
        if(val === 3) {
        	console.log('满足条件后的操作');
            throw new Error();
        }
        console.log('满足条件后不再执行', val)
    })
}catch(e) {
   console.log('可以不处理');
}
console.log('继续执行');
```

- `forEach()`

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.forEach(x => {
  if (x === 4) {
    return;
  }
  newArr.push(x * 2);
});

```

在 forEach 中，不能使用 continue 和 break ，可以使用 return 或 return false 跳出循环，效果与 for 中 continue 一样。 注意该方法无法一次结束所有循环。

使用 `forEach()` 方法遍历了数组中的每一项，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `return` 语句，==跳出回调函数，并继续执行 `forEach()` 方法的下一次迭代。==(只是跳出，没有结束)

是因为 `forEach()` 方法有一个特定的用途，即对数组中的每一项执行一个操作。它不是一个循环，==所以不能使用 `break` 或 `continue` 语句来控制循环的执行。== ==Uncaught SyntaxError: Illegal break statement==

如果你想要在 `forEach()` 方法中使用 `break` 语句，那么你可以使用 `some()` 方法代替。`some()` 方法也会迭代数组的每一项，并对每一项执行一个回调函数。但是，它会在回调函数返回 `true` 的时候终止循环，并返回 `true`。

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.some(x => {
  if (x === 4) {
    return true;
  }
  newArr.push(x * 2);
});
```

- `map()`

在 `map()` 方法的回调函数中使用 `break` 语句是不合法的。这是因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。它不是一个循环，所以不能使用 `break` 或 `continue` 语句来控制循环的执行。

如果你想要在 `map()` 方法中使用 `break` 语句，那么你可以使用一个普通的循环代替。

```js
const arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
  const newArr = arr.map(x => {
    if (x === 4) {
      break; // Uncaught SyntaxError: Illegal break statement
      // continue // Uncaught SyntaxError: Illegal continue statement: no surrounding iteration statement
    }
    return x * 2;
  });
}
```

在这个例子中，我们在一个循环中调用了 `map()` 方法，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `break` 语句，终止循环。

但是，这种方法并不是很好，因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。如果你想要终止循环，那么更好的方法是使用 `for` 循环或者 `forEach()` 方法，而不是 `map()` 方法。

- for...of...

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

for (let i = 0; i < arr.length; i++) {
  if (arr[i] === 4) {
    break;
  }
  newArr.push(arr[i] * 2);
}
```

### 25. for...in和for...of的区别 forin forof

for…of 是ES6新增的遍历方式，允许遍历一个含有iterator接口的数据结构（数组、对象等）并且返回各项的值，和ES3中的for…in的区别如下 

1. for… in 会遍历对象的整个原型链，性能非常差不推荐使用，而 for … of 只遍历当前对象不会遍历原型链； 
2. for…of 遍历获取的是对象的键值，for…in 获取的是对象的键名； 
3. 对于数组的遍历，for…in 会返回数组中所有可枚举的属性(包括原型链上可枚举的属性)，for…of 只返回数组的下标对应的属性值； 

总结：==for...in 循环主要是为了遍历对象而生，不适用于遍历数组；for...of 循环可以用来遍历数组、类数组对象，字符串、Set、Map 以及 Generator 对象。==

### 26. 如何使用for...of遍历对象

for…of是作为ES6新增的遍历方式，允许遍历一个含有iterator接口的数据结构（数组、对象等）并且返回各项的值，普通的对象用for...of遍历是会报错的。

如果需要遍历的对象是类数组对象，用Array.from转成数组即可。

```js
var obj = {
  0: "one",
  1: "two",
  length: 2
};

obj = Array.from(obj);

for (var k of obj) {
  console.log(k);
}
```

```js
//方法一：
var obj = {
  a: 1,
  b: 2,
  c: 3
};

obj[Symbol.iterator] = function () {
  var keys = Object.keys(this);
  var count = 0;
  return {
    next() {
      if (count < keys.length) {
        return { value: obj[keys[count++]], done: false };
      } else {
        return { value: undefined, done: true };
      }
    }
  };
};

for (var k of obj) {
  console.log(k);
}

// 方法二
var obj = {
  a: 1,
  b: 2,
  c: 3
};

obj[Symbol.iterator] = function* () {
  var keys = Object.keys(obj);
  for (var k of keys) {
    yield [k, obj[k]];
  }
};

for (var [k, v] of obj) {
  console.log(k, v);
}
```

### 33. 如何遍历一个对象

1. for in
2. object.keys()
3. object.entries()

| 方法                  | 遍历对象类型   | 遍历原型链 | 返回值              | 备注                                       |
| --------------------- | -------------- | ---------- | ------------------- | ------------------------------------------ |
| `for…in`              | 可枚举属性     | ✅          | key                 | 顺序不保证；需 `hasOwnProperty` 过滤原型链 |
| `Object.keys(obj)`    | 自身可枚举属性 | ❌          | key 数组            | 常用，可配合 `for…of`                      |
| `Object.entries(obj)` | 自身可枚举属性 | ❌          | `[key, value]` 数组 | 遍历键值对，方便解构或 Map 转换            |

1. for…in

**遍历对象所有可枚举属性**（包括原型链上的可枚举属性）返回 **属性名**（key）;可以遍历数组，但会遍历自定义属性和原型链上的可枚举属性；顺序不保证严格按照插入顺序（对象属性是无序的，但 ES6+ 对于非整数键有顺序保证）

```js
const obj = { a: 1, b: 2 }
Object.prototype.c = 3  // 原型链属性

for (let key in obj) {
  console.log(key)
}

// 输出
// a
// b
// c （原型链属性）

// ⚠️ 注意：会遍历原型链上的属性，需要 hasOwnProperty 过滤掉

for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key)
  }
}

// a
// b
```

2. Object.keys(obj)

返回 **对象自身可枚举属性名组成的数组**,不会遍历原型链,数组形式，可直接使用数组方法

```js
const obj = { a: 1, b: 2 }
Object.prototype.c = 3

console.log(Object.keys(obj))
// ["a", "b"]

// 可以配合 for…of 遍历：also
for (let key of Object.keys(obj)) {
  console.log(key)
}
```

3. Object.entries(obj)

返回 **对象自身可枚举属性的键值对数组**,格式：`[ [key1, value1], [key2, value2], ... ]`,不会遍历原型链,常用于 **解构 + 遍历** 或 **转换成 Map**

```js
const obj = { a: 1, b: 2 }

console.log(Object.entries(obj))
// [["a", 1], ["b", 2]]

for (let [key, value] of Object.entries(obj)) {
  console.log(key, value)
}
// a 1
// b 2
```

```js
捕获阶段：html → body → div → button
目标阶段：button
冒泡阶段：button → div → body → html

const html = document.querySelector('html');
const div = document.querySelector('#parent');
const btn = document.querySelector('#btn');

html.addEventListener('click', () => console.log('html'), true); // 捕获阶段
div.addEventListener('click', () => console.log('div'), true);   // 捕获阶段
btn.addEventListener('click', () => console.log('button'));       // 默认冒泡阶段

btn.click();

// 输出顺序：
// html
// div
// button
// 捕获阶段的处理器先执行，再执行目标元素事件

你点击 button#btn。
捕获阶段 = 事件从顶楼往下爬
html → body → div → button
事件从祖先元素开始“走到”按钮
如果祖先元素在 捕获阶段 注册了事件处理器，会在事件到达目标前触发
目标阶段 = 事件到达按钮
按钮本身的事件处理器触发
冒泡阶段 = 事件从一楼回到顶楼
button → div → body → html
事件逐级向上冒泡，冒泡阶段注册的事件处理器依次触发
```





- 介绍一下迭代器 lterator，以及有哪些用法
- JS 有哪些迭代器，该如何使用?
- JS 对象可以使用 for...of 迭代吗?
- 如何使对象 iterable 化，以使其支持 for...of 迭代
- iterator 和数组有什么关系?
- iterator 对象有哪些特征
- 理解 JavaScript 中的 for...of、for...in 与 for 循环:三者的本。。。
- 为什么普通 for循环的性能远远高于 forEach 的性能?

------

## 十、原型 / 构造函数 / 类

### 22. ==如何判断一个对象是否属于某个类?==

- 第一种方式，使用 instanceof 运算符来判断构造函数的 prototype 属性是否出现在对象的原型链中的任何位置。
- 第二种方式，通过对象的 constructor 属性来判断，对象的 constructor 属性指向该对象的构造函数，但是这种方式不是很安全，因为 constructor 属性可以被改写。
- 第三种方式，如果需要判断的是某个内置的引用类型的话，可以使用 Object.prototype.toString() 方法来打印对象的[[Class]] 属性来进行判断。

### 1. 对原型、原型链的理解

**原型**

每个构造函数的内部都包含一个指针，这个指针指向构造函数的 `prototype`属性对应的值，这个指针被称为对象的原型。（在 ES5 中）

在JavaScript中是使用构造函数来新建一个对象的，每一个构造函数的内部都有一个`prototype`属性，它的属性值是一个对象，这个对象包含了可以由该构造函数的所有实例共享的属性和方法。在这个对象的内部将包含一个指针，这个指针指向构造函数的 `prototype`属性对应的值，在 ES5 中这个指针被称为对象的原型。

**获取原型的方法：**

1.  `__proto__ `属性来访问这个属性，但是最好不要使用这个属性，因为它不是规范中规定的。
2.  ES5 中新增了一个 Object.getPrototypeOf() 方法，可以通过这个方法来获取对象的原型。

**原型链（构造函数，原型，实例的关系）**

每个构造函数都有一个原型对象，原型有一个属性指回构造函数，而实例有一个内部指针指向原型。这样就在实例和原型之间构造了一条原型链。

prototype 是对象；constructor 是这个对象上的一个普通属性

<img src="https://s2.loli.net/2025/12/25/Nw75QrtVOWBgvhT.png" alt="image-20251225141508414" style="zoom: 33%;" />

<img src="https://s2.loli.net/2025/12/25/WPlgAmSITOZUBR5.png" alt="image-20251225141534774" style="zoom:33%;" />

### 2. 原型修改、重写

```js
function Person(name) {
  this.name = name;
}

// 修改原型
Person.prototype.getName = function () {};

var p = new Person("hello");
console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // true

// 重写原型，这里不是“修改原型”，而是“换了一个全新的原型对象”，直接赋予新的值了
// 而这个新对象默认的 constructor 指向的是 Object，不是 Person。
Person.prototype = {
  getName: function () {}
};

var p = new Person("hello");

console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // false
```

可以看到修改原型的时候p的构造函数不是指向Person了，因为直接给Person的原型对象直接用对象赋值时，它的构造函数指向的了根构造函数Object，所以这时候`p.constructor === Object` ，而不是`p.constructor === Person`。要想成立，就要用constructor指回来：

```js
Person.prototype = {
  getName: function () {}
};
var p = new Person("hello");
p.constructor = Person;
console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // true
```

### 3. 原型链指向

```js
p.__proto__; // Person.prototype
Person.prototype.__proto__; // Object.prototype
p.__proto__.__proto__; //Object.prototype
p.__proto__.constructor.prototype.__proto__; // Object.prototype
Person.prototype.constructor.prototype.__proto__; // Object.prototype
p1.__proto__.constructor; // Person
Person.prototype.constructor; // Person
```

### 4. 原型链的终点是什么?如何打印出原型链的终点？

由于`Object`是构造函数，原型链终点是`Object.prototype.__proto__`，而`Object.prototype.__proto__ === null // true`，所以，==原型链的终点是`null`。==

原型链上的所有原型都是对象，所有的对象最终都是由`Object`构造的，而`Object.prototype`的下一级是`Object.prototype.__proto__`。

### 5. 如何获得对象非原型链上的属性?

| 方法                                | 是否只取自身属性 | 是否包含原型链 | 是否包含不可枚举 | 是否包含 Symbol | 常见用途                   |
| ----------------------------------- | ---------------- | -------------- | ---------------- | --------------- | -------------------------- |
| `Object.keys(obj)`                  | ✅                | ❌              | ❌                | ❌               | 最常用，获取自身可枚举属性 |
| `Object.getOwnPropertyNames(obj)`   | ✅                | ❌              | ✅                | ❌               | 包含不可枚举属性           |
| `Object.getOwnPropertySymbols(obj)` | ✅                | ❌              | ✅                | ✅（仅 Symbol）  | 获取 Symbol 属性           |
| `Reflect.ownKeys(obj)`              | ✅                | ❌              | ✅                | ✅               | **最全，推荐面试加分**     |
| `for...in`                          | ❌                | ✅              | ❌                | ❌               | 不推荐，用于遍历原型链     |

使用`hasOwnProperty()`方法来判断属性是否属于原型链的属性：

```js
function iterate(obj) {
  var res = [];
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) res.push(key + ": " + obj[key]);
  }
  return res;
}
```

### 6. 在 ES6 Class 中，super 的过程中做了什么

派生类的方法可以通过 super 关键字引用它们的原型。这个关键字只能在派生类中使用，而且仅限于类构造函数、实例方法和静态方法内部。在类构造函数中使用super可以调用父类构造函数。

### 1. new操作符的实现原理

   - new关键字会首先创建一个空对象
   - 将这个空对象的原型对象指向构造函数的原型属性，从而继承原型上的方法
   - 将this指向这个空对象，执行构造函数中的代码，以获取私有属性
   - 如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象

<img src="https://s2.loli.net/2025/12/24/RToxy8knGcFVgBd.png" alt="image-20251224170807859" style="zoom:50%;" />

### 3. 如果new一个箭头函数会怎样

箭头函数是ES6中的提出来的，它没有prototype，也没有自己的this指向，更不可以使用arguments参数，所以不能New一个箭头函数。

new操作符的实现步骤如下：

1. 创建一个对象
2. 将构造函数的作用域赋给新对象（也就是将对象的proto属性指向构造函数的prototype属性）
3. 指向构造函数中的代码，构造函数中的this指向该对象（也就是为这个对象添加属性和方法）返回新的对象

所以，上面的第二、三步，箭头函数都是没有办法执行的。



----



- JS 里是否可能存在:对象有一个 name 属性，原型链上也有。。。

- JavaScript 中继承方式有哪些?

- 在创建对象的时候，new class 和 new function 有什么区别?

- JS 里的类就是构造函数的语法糖，这个说法是否正确?

- 当使用 new 关键字创建对象时，会经历哪些步骤?

- ES5 和 ES6 使用 new 关键字实例化对象的流程是一样的吗?

- ES6 class 装饰器是如何实现的?

  



------

## 十一、函数系统（Function）

### 4. 你对函数式编程的理解？优缺点？

#### intro

函数式编程是一种"编程范式"（programming paradigm），一种编写程序的方法论

主要的编程范式有三种：命令式编程，声明式编程和函数式编程

相比命令式编程，函数式编程更加强调程序执行的结果而非执行的过程，倡导利用若干简单的执行单元让计算结果不断渐进，逐层推导复杂的运算，而非设计一个复杂的执行过程。

简单来讲，就是要把过程逻辑写成函数，定义好输入参数，只关心它的输出结果。

```js
// 命令式编程
var array = [0, 1, 2, 3]
for(let i = 0; i < array.length; i++) {
    array[i] = Math.pow(array[i], 2)
}

// 函数式方式
[0, 1, 2, 3].map(num => Math.pow(num, 2))
```

**优点**

- 更好的管理状态：因为它的宗旨是无状态，或者说更少的状态，能最大化的减少这些未知、优化代码、减少出错情况
- 更简单的复用：固定输入->固定输出，没有其他外部变量影响，并且无副作用。这样代码复用时，完全不需要考虑它的内部实现和外部影响
- 更优雅的组合：往大的说，网页是由各个组件组成的。往小的说，一个函数也可能是由多个小函数组成的。更强的复用性，带来更强大的组合性
- 隐性好处。减少代码量，提高维护性

**缺点**

- 性能：函数式编程相对于指令式编程，性能绝对是一个短板，因为它往往会对一个方法进行过度包装，从而产生上下文切换的性能开销
- 资源占用：在 JS 中为了实现对象状态的不可变，往往会创建新的对象，因此，它对垃圾回收所产生的压力远远超过其他编程方式
- 递归陷阱：在函数式编程中，为了实现迭代，通常会采用递归操作

#### a. 纯函数

函数式编程旨在尽可能的提高代码的无状态性和不变性。要做到这一点，就要学会使用无副作用的函数，也就是纯函数

纯函数是对给定的输入返还相同输出的函数，并且要求你所有的数据都是不可变的，即纯函数=无状态+数据不可变

特性：

- 函数内部传入指定的值，就会返回确定唯一的值
- 不会造成超出作用域的变化，例如修改全局变量或引用传递的参数

优势：

- 使用纯函数，我们可以产生可测试的代码

```js
test('double(2) 等于 4', () => {
  expect(double(2)).toBe(4);
})
```

- 不依赖外部环境计算，不会产生副作用，提高函数的复用性
- 可读性更强 ，函数不管是否是纯函数 都会有一个语义化的名称，更便于阅读
- 可以组装成复杂任务的可能性。符合模块化概念及单一职责原则

#### b. 高阶函数

高级函数，就是以函数作为输入或者输出的函数被称为高阶函数。

```js
// 通过高阶函数抽象过程，注重结果。
const forEach = function (arr, fn) {
  for (let i = 0; i < arr.length; i++) {
    fn(arr[i]);
  }
};

let arr = [1, 2, 3];

forEach(arr, (item) => {
  console.log(item);
});
```

```js
// 高阶函数存在缓存的特性，主要是利用闭包作用
const once = (fn) => {
  let done = false;
  return function () {
    if (!done) {
      fn.apply(this, fn);
    } else {
      console.log("该函数已经执行");
    }
    done = true;
  };
};

```

#### c. 柯里化

柯里化是把一个多参数函数转化成一个嵌套的一元函数的过程

```js
// 二元函数
let fn = (x,y)=>x+y;

const curry = function (fn) {
  return function (x) {
    return function (y) {
      return fn(x, y);
    };
  };
};
let myfn = curry(fn);
console.log(myfn(1)(2));

// 多参数柯里化；
const curry = function (fn) {
  return function curriedFn(...args) {
    if (args.length < fn.length) {
      return function () {
        return curriedFn(...args.concat([...arguments]));
      };
    }
    return fn(...args);
  };
};
const fn = (x, y, z, a) => x + y + z + a;
const myfn = curry(fn);
console.log(myfn(1)(2)(3)(1));
```

关于柯里化函数的意义如下：

- 让纯函数更纯，每次接受一个参数，松散解耦
- 惰性执行

#### d. 组合函数与管道函数

**组合函数与管道函数的意义在于：可以把很多小函数组合起来完成更复杂的逻辑**

**组合函数，目的是将多个函数组合成一个函数**

**而管道函数，执行顺序是从左到右执行的**

```js
function afn(a) {
  return a * 2;
}

function bfn(b) {
  return b * 3;
}

const compose = (a, b) => (c) => a(b(c));

let myfn = compose(afn, bfn);
console.log(myfn(2));
// 可以看到compose实现一个简单的功能：形成了一个新的函数，而这个函数就是一条从 bfn -> afn 的流水线
```

```js
// compose执行是从右到左的
const compose = (...fns)=>val=>fns.reverse().reduce((acc,fn)=>fn(acc),val);
```

```js
// 而管道函数，执行顺序是从左到右执行的
const pipe = (...fns)=>val=>fns.reduce((acc,fn)=>fn(acc),val);
```



### 12. 为什么函数的arguments参数是类数组而不是数组？如何遍历类数组？

`arguments`是一个对象，它的属性是从 0 开始依次递增的数字，还有`callee`和`length`等属性，与数组相似；但是它却没有数组常见的方法属性，如`forEach`, `reduce`等，所以叫它们类数组。

```js
// 1. 将数组的方法应用到类数组上，这时候就可以使用call和apply方法，如：
function foo(){ 
  Array.prototype.forEach.call(arguments, a => console.log(a))
}

// 2. 使用Array.from方法将类数组转化成数组:
function foo(){ 
  const arrArgs = Array.from(arguments) 
  arrArgs.forEach(a => console.log(a))
}

// 3. 使用展开运算符将类数组转化成数组
function foo(){ 
    const arrArgs = [...arguments] 
    arrArgs.forEach(a => console.log(a)) 
}
```

### 30. 什么是纯函数

[What Is a Pure Function in JavaScript?](https://www.freecodecamp.org/news/what-is-a-pure-function-in-javascript-acb887375dfe/)

[純粹的好，Pure Function 知道](https://medium.com/frochu/%E7%B4%94%E7%B2%B9%E7%9A%84%E5%A5%BD-pure-function-%E7%9F%A5%E9%81%93-574d5c0d7819)

[4. 你对函数式编程的理解？优缺点？](# 4. 你对函数式编程的理解？优缺点？)

redux中的reducer就是纯函数

1. 输出仅由输入决定，每一个固定的输入总是返回相同的输出
2. 不产生副作用

```js
// impure function
let intercept = 2;
function math(x) {
  return 3 * x + intercept;
}
const result = math(4); // 14

// pure function, 这个有点像柯里化
function math(itr) {
  return function (x) {
    return 3 * x + itr;
  };
}
const result = math(2)(4); // 14
```

### 8. JavaScript类数组对象的定义?

一个拥有 length 属性和若干索引属性的对象就可以被称为类数组对象，类数组对象和数组类似，但是不能调用数组的方法。常见的类数组对象有 arguments 和 DOM 方法的返回结果，还有一个函数也可以被看作是类数组对象，因为它含有 length 属性值，代表可接收的参数个数。

常见的类数组转换为数组的方法有这样几种

```js
// 通过 call 调用数组的 slice 方法来实现转换
Array.prototype.slice.call(arrayLike);

// 通过 call 调用数组的 splice 方法来实现转换
Array.prototype.splice.call(arrayLike, 0);

// 通过 apply 调用数组的 concat 方法来实现转换
Array.prototype.concat.apply([], arrayLike);

// 通过 Array.from 方法来实现转换
Array.from(arrayLike);
```

```js
function demo(a, b, c) {
  console.log(arguments[0]) // 1
  console.log(arguments.length) // 3
  console.log(arguments.push) // undefined
}

demo(1, 2, 3)

// --

const divs = document.querySelectorAll('div')
console.log(divs[0]) // 第一个 div
console.log(divs.length) // div 的数量
console.log(divs.map) // undefined
```

### 4. 箭头函数和普通函数的区别

- 箭头函数没有自己的this
- call()、apply()、bind()等方法不能改变箭头函数中this的指向
- 箭头函数不能作为构造函数使用
- 箭头函数没有prototype

### 5. ==箭头函数的this指向哪里==

 ✔ 回调函数
 ✔ 定时器 / Promise / 事件包装
 ✔ 不希望 `this` 被改掉

箭头函数没有自己的 `this`，它的 `this` 在定义时就从外层作用域“静态捕获”，之后无法通过 call / apply / bind 改变。

箭头函数并没有属于⾃⼰的this，它所谓的this是捕获其所在上下⽂的 this 值，作为⾃⼰的 this 值。

箭头函数体内的 this 对象，就是定义该函数时所在的作用域指向的对象，而不是使用时所在的作用域指向的对象。

==普通函数的this，谁调用的this就指向谁==

```js
const obj = {
  name: 'Alice',
  sayName1: function () {
    console.log(this.name) // **普通函数**`this` 由**调用方式**决定,obj.sayName1() → this === obj
  },
  sayName2: () => {
    console.log(this.name) // 定义在对象字面量中，本质仍在全局作用域 , this === window / globalThis
  }
}

obj.sayName1() // ✅ 'Alice'
obj.sayName2() // ❌ undefined

```

### 7. 对rest参数的理解

1. 扩展运算符被用在函数形参上时，**它还可以把一个分离的参数序列整合成一个数组**。
2. 可以把函数的多个入参收敛进一个数组里。这一点**经常用于获取函数的多余参数，或者像上面这样处理函数参数个数不确定的情况。**

```js
function mutiple(...args) {
  let result = 1;
  for (var val of args) {
    result *= val;
  }
  return result;
}
mutiple(1, 2, 3, 4) // 24

function mutiple(...args) {
  console.log(args)
}
mutiple(1, 2, 3, 4) // [1, 2, 3, 4]
```

#### rest参数和argument的区别

arguments是一个类数组,本质是对象；方便处理函数传参。

而rest参数是真正的数组,可以正常调用数组的所有方法.所以在某些场景中,无需将arguments转为真正的数组,可以直接使用rest参数代替。

```js
function sumArgu() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
}
console.log(sumArgu(1, 2, 3)); // 6

function sumRest(...m) {
  var total = 0;
  for (var i of m) {
    total += i;
  }
  return total;
}
console.log(sumRest(1, 2, 3)); // 6
```

### 17. 如何实现 compose 函数，进行函数合成

https://github.com/shfshanyue/Daily-Question/issues/182

### 18. 前端中遇到过处理二进制的场景吗

### 19. js 中什么是可选链操作符，如何访问数组

`?.` 操作符，可以嵌套获取对象的属性值。通过获取对象属性获得的值可能是 undefined 或 null 时，可选链操作符提供了一种方法来简化被连接对象的值访问。

```js
const o = {};

// 添加可选链之前
o && o.a && o.a.b && o.a.b.c && o.a.b.c.d;

// 添加可选链之后
o?.a?.b?.c?.d;
```

### 5. ==Javascript中如何实现函数缓存？函数缓存有哪些应用场景？==

==实现函数缓存主要依靠闭包、柯里化、高阶函数。==

函数缓存，就是将函数运算过的结果进行缓存，本质上就是用空间（缓存存储）换时间（计算过程），常用于缓存数据计算结果和缓存对象。缓存只是一个临时的数据存储，它保存数据，以便将来对该数据的请求能够更快地得到处理

```js
// 高阶函数缓存
const memoize = function (func, content) {
  let cache = Object.create(null);
  content = content || this;
  return (...key) => {
    if (!cache[key]) {
      cache[key] = func.apply(content, key);
    }
    return cache[key];
  };
};
const add = (a,b) => a+b;
const calc = memoize(add); // 函数缓存
calc(10,20); // 30 缓存

// 柯里化
var add2 = function (x) {
  // 返回函数
  return function (y) {
    return x + y;
  };
};
add2(3)(4); // 7

// 闭包可以理解成，函数 + 函数体内可访问的变量总和
// add函数本身，以及其内部可访问的变量，即 a = 1，这两个组合在⼀起就形成了闭包
(function () {
  var a = 1;
  function add() {
    const b = 2;
    let sum = b + a;
    console.log(sum); // 3
  }
  add();
})();

```



---



- new Function 了解多少?

- 什么是匿名函数?

- 函数声明与函数表达式有什么区别?

- 箭头函数的作用以及使用场景

- 箭头函数解决了什么问题

- 普通函数动态参数和箭头函数的动态参数有什么区别?

- 函数有默认值的时候，如果传的参数是 undefned，会被默认。。。

- 什么是伪数组、什么是类数组

- 类数组转换成数组的方法有哪些

- Generator 是如何做到中断和恢复的

- 函数柯里化了解多少?

- JavaScript类数组对象的定义?

  

------

## 十二、作用域 / 执行上下文 / this

### 6. ==this指向的理解==

==普通函数的this，谁调用的this就指向谁==

`this` 关键字是函数运行时自动生成的一个内部对象，只能在函数内部使用，总指向调用它的对象。

箭头函数没有自己的 `this`，它的 `this` 在定义时就从外层作用域“静态捕获”，之后无法通过 call / apply / bind 改变。

```js
const obj = {
  name: 'Tom',
  say() {
    setTimeout(function () {
      console.log(this.name)
    }, 100)
  }
}

obj.say() // ❌ undefined
// setTimeout 里的回调是普通函数
// 调用时没有宿主对象
// this 默认指向 window / undefined（严格模式）
```

```js
const obj = {
  name: 'Tom',
  say() {
    setTimeout(() => {
      console.log(this.name)
    }, 100)
  }
}

obj.say() // ✅ 'Tom'
```

**调用方式**：`obj.say()`

**普通方法调用** → `this === obj`

所以此时，say 方法的执行上下文里的 `this` 指向 `obj`

**箭头函数没有自己的 this**

它的 this **静态绑定**到它**定义时所在的作用域**

这里的定义作用域就是 `say` 方法体内

say 方法内的 this = obj

👉 箭头函数捕获 this === obj

setTimeout 会在 100ms 后调用这个箭头函数

**调用方式无所谓**，箭头函数的 this 已经被“锁死”在 obj

执行 `console.log(this.name)` → 输出 `Tom`

### 38. 对作用域、作用域链的理解 Scope / Scope Chain

#### **作用域**

**作用域：函数和变量能被访问的区域，分有全局作用域、函数作用域、块级作用域。**

- 全局作用域：任何不在函数中或是大括号中声明的变量，都是在全局作用域下，全局作用域下声明的变量可以在程序的任意位置访问
- 函数作用域：函数作用域也叫局部作用域，如果一个变量是在函数内部声明的它就在一个函数作用域下面。这些变量只能在函数内部访问，不能在函数以外去访问
- 块级作用域：ES6引入了`let`和`const`关键字,和`var`关键字不同，在大括号中使用`let`和`const`声明的变量存在于块级作用域中。在大括号之外不能访问这些变量

#### **作用域链**

当在`Javascript`中使用一个变量的时候，首先`Javascript`引擎会尝试在当前作用域下去寻找该变量，如果没找到，再到它的上层作用域寻找，以此类推直到找到该变量或是已经到了全局作用域



### 39. 对执行上下文的理解

- 全局执行上下文：只有一个，浏览器中的全局对象就是 `window`对象，`this` 指向这个全局对象
- 函数执行上下文：存在无数个，只有在函数被调用的时候才会被创建，每次调用函数都会创建一个新的执行上下文
- 执行栈，也叫调用栈，具有 LIFO（后进先出）结构，用于存储在代码执行期间创建的所有执行上下文

### 17. ==JavaScript为什么要进行变量提升，他导致了什么问题？==

- 解析和预编译过程中的声明提升可以提高性能，让函数可以在执行时预先为变量分配栈空间
- 声明提升还可以提高JS代码的容错性，使一些不规范的代码也可以正常执行

```js
// 在这个函数中，原本是要打印出外层的tmp变量，但是因为变量提升的问题，内层定义的tmp被提到函数内部的最顶部，相当于覆盖了外层的tmp，所以打印结果为undefined。

var tmp = new Date();

function fn(){
	console.log(tmp);
	if(false){
		var tmp = 'hello world';
	}
}

fn();  // undefined
```

```js
// 由于遍历时定义的i会变量提升成为一个全局变量，在函数结束之后不会被销毁，所以打印出来11。
var tmp = 'hello world';

for (var i = 0; i < tmp.length; i++) {
	console.log(tmp[i]);
}

console.log(i); // 11
```

### 40. call() 和apply()、bind()的区别?

它们的作用一模一样，区别仅在于传入参数的形式的不同。

- apply 接受两个参数，第一个参数指定了函数体内 this 对象的指向，第二个参数为一个带下标的集合，这个集合可以为数组，也可以为类数组，apply 方法把这个集合中的元素作为参数传递给被调用的函数。
- call 传入的参数数量不固定，跟 apply 相同的是，第一个参数也是代表函数体内的 this 指向，从第二个参数开始往后，每个参数被依次传入函数。
- bind与call的参数相同，只不过返回的是函数，需要进行调用。

![image-20251224182101198](https://s2.loli.net/2025/12/24/GlYoKHAZpsOTW82.png)

![image-20251224182125879](https://s2.loli.net/2025/12/24/gz1lCaUA2eRn3bd.png)

### 41. 实现call、apply 及bind函数

- [【Q031】js 中如何实现 bind](https://github.com/shfshanyue/Daily-Question/issues/32)
- [【Q032】js 中什么是 softbind，如何实现](https://github.com/shfshanyue/Daily-Question/issues/33)
- [【Q656】JS 中如何实现 call/apply (代码集合)](https://github.com/shfshanyue/Daily-Question/issues/674)

#### 1. call 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 判断传入上下文对象是否存在，如果不存在，则设置为 window 。
- 处理传入的参数，截取第一个参数后的所有参数。
- 将函数作为上下文对象的一个属性。
- 使用上下文对象来调用这个方法，并保存返回结果。
- 删除刚才新增的属性。
- 返回结果。

```js
Function.prototype.myCall = function (context) {
  // 判断调用对象
  if (typeof this !== "function") {
    console.error("type error");
  }
  // 获取参数
  let args = [...arguments].slice(1),
    result = null;
  // 判断 context 是否传入，如果未传入则设置为 window
  context = context || window;
  // 将调用函数设为对象的方法
  context.fn = this;
  // 调用函数
  result = context.fn(...args);
  // 将属性删除
  delete context.fn;
  return result;
};

```

#### 2. apply 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 判断传入上下文对象是否存在，如果不存在，则设置为 window 。
- 将函数作为上下文对象的一个属性。
- 判断参数值是否传入
- 使用上下文对象来调用这个方法，并保存返回结果。
- 删除刚才新增的属性
- 返回结果

```js
Function.prototype.myApply = function (context) {
  // 判断调用对象是否为函数
  if (typeof this !== "function") {
    throw new TypeError("Error");
  }
  let result = null;
  // 判断 context 是否存在，如果未传入则为 window
  context = context || window;
  // 将函数设为对象的方法
  context.fn = this;
  // 调用方法
  if (arguments[1]) {
    result = context.fn(...arguments[1]);
  } else {
    result = context.fn();
  }
  // 将属性删除
  delete context.fn;
  return result;
};

```

#### 3. bind 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 保存当前函数的引用，获取其余传入参数值。
- 创建一个函数返回
- 函数内部使用 apply 来绑定函数调用，需要判断函数作为构造函数的情况，这个时候需要传入当前函数的 this 给 apply 调用，其余情况都传入指定的上下文对象。

```js
Function.prototype.myBind = function (context) {
  // 判断调用对象是否为函数
  if (typeof this !== "function") {
    throw new TypeError("Error");
  }
  // 获取参数
  var args = [...arguments].slice(1),
    fn = this;
  return function Fn() {
    // 根据调用方式，传入不同绑定值
    return fn.apply(
      this instanceof Fn ? this : context,
      args.concat(...arguments)
    );
  };
};

```

### 42. js 中什么是 softbind，如何实现

bind 函数多次调用会已第一次绑定的 this 为准，softbind以最后一次绑定传入的 this 为准；

```js
Function.prototype.softBind = function (obj, ...rest) {
  const fn = this;
  const bound = function (...args) {
    const o = !this || this === (window || global) ? obj : this;
    return fn.apply(o, [...rest, ...args]);
  };

  bound.prototype = Object.create(fn.prototype);
  return bound;
};

```



- 什么是执行上下文栈?它有什么作用?
- 执行上下文的生命周期有哪些阶段?
- 全局作用域中，用 const 和 let 声明的变量不在 window 上，.。。。
- JS 中 this 指向问题了解多少
- JavaScript 中 this 的使用场景解析
- 哪些原因会导致 JavaScript 里 this 指向混乱?

------

## 十三、闭包 / 内存 / 递归

### 37. ==对闭包的理解==

(函数缓存本质依赖闭包保存状态)，可以看本章 Javascript中如何实现函数缓存？函数缓存有哪些应用场景？

闭包是一个函数, 其可以记住并访问外部变量。

闭包是指有权访问另一个函数作用域中变量的函数，创建闭包的最常见的方式就是在一个函数内创建另一个函数，创建的函数可以访问到当前函数的局部变量。

```js
function init() {
    var name = "Mozilla"; // name 是一个被 init 创建的局部变量
    function displayName() { // displayName() 是内部函数，一个闭包
        alert(name); // 使用了父函数中声明的变量
    }
    displayName();
}
init();
```

在函数被创建时, 函数的隐藏属性 [[Environment]] 会记住函数被创建时的位置, 即当时的词法环境 Lexical Environment这样, 无论在哪里调用函数, 都会去到 [[Environment]] 所引用的词法环境，当查找变量时, 先在词法环境内部查找, 当没有找到局部变量时, 前往当前词法环境所记录的外部词法环境查找。

**使用场景**

==封装私有变量和处理回调函数==

==例如计数器、延迟调用、回调等闭包的应用，其核心思想还是创建私有变量和延长变量的生命周期==

- 创建私有变量
- 延长变量的生命周期

从作用域的角度理解，每创建一个函数会创建一个作用域，闭包里面的函数没有要释放，但是在外层却返回了本函数，导致变量不能被释放而留存下来，应用就是对于有存储变量的需求可以用

1. 柯里化函数：目的在于避免频繁调用具有相同参数函数的同时，又能够轻松的重用

2. 使用闭包模拟私有方法：在`JavaScript`中，没有支持声明私有变量，但我们可以使用闭包来模拟私有方法

   通过使用闭包来定义公共函数，并令其可以访问私有函数和变量，这种方式也叫模块方式

   两个计数器 `Counter1` 和 `Counter2` 是维护它们各自的独立性的，每次调用其中一个计数器时，通过改变这个变量的值，会改变这个闭包的词法环境，不会影响另一个闭包中的变量

3. 创建私有变量：闭包的第一个用途是使我们在函数外部能够访问到函数内部的变量。通过使用闭包，可以通过在外部调用闭包函数，从而在外部访问到函数内部的变量，可以使用这种方法来创建私有变量

4. 闭包的另一个用途是使已经运行结束的函数上下文中的变量对象继续留在内存中，因为闭包函数保留了这个变量对象的引用，所以这个变量对象不会被回收。

**闭包注意事项**

   **缺点：**

   - 常驻内存，增加内存使用量。
   - 使用不当会很容易造成内存泄露。

如果不是某些特定任务需要使用闭包，在其它函数中创建函数是不明智的，因为闭包在处理速度和内存消耗方面对脚本性能具有负面影响

在创建新的对象或者类时，方法通常应该关联于对象的原型，而不是定义到对象的构造器中。原因在于每个对象的创建，方法都会被重新赋值。

我们知道[闭包](https://so.csdn.net/so/search?q=闭包&spm=1001.2101.3001.7020)延展了局部变量的生命周期，使得外部操作局部变量成为可能，一般来讲函数在调用执行后函数就会被释放，但如果函数中产生了闭包，就会导致函数执行完毕后，函数内部的局部变量没有被释放，使得占用内存时间会变长，容易造成==内存泄漏==。

**解决办法**

1. 能不用闭包就不用
2. 及时释放

### 32. JS 如何检测到对象中有循环引用

```js
function cycle(obj, parent) {
  //表示调用的父级数组
  var parentArr = parent || [obj];
  for (var i in obj) {
    if (typeof obj[i] === "object") {
      //判断是否有循环引用
      parentArr.forEach((pObj) => {
        if (pObj === obj[i]) {
          obj[i] = "[cycle]";
        }
      });
      cycle(obj[i], [...parentArr, obj[i]]);
    }
  }
  return obj;
}
```

### 18. 什么是尾调用，使用尾调用有什么好处？

尾调用指的是函数的最后一步调用另一个函数。代码执行是基于执行栈的，所以当在一个函数里调用另一个函数时，会保留当前的执行上下文，然后再新建另外一个执行上下文加入栈中。使用尾调用的话，因为已经是函数的最后一步，==所以这时可以不必再保留当前的执行上下文，从而节省了内存，这就是尾调用优化。但是 ES6 的尾调用优化只在严格模式下开启，正常模式是无效的==





- JavaScript 如何做内存管理
- JavaScript 中，隐藏类是什么概念?
- 在 JavaScript 中如何避免递归导致的栈溢出问题?
- 递归和尾递归是什么?
- 副作用是什么?
- 深度遍历广度遍历的区别?

------

## 十四、异步 / 事件循环

### 36. ==eventLoop事件循环/事件轮询==

JavaScript 是单线程的，一次只能做一件事，但它通过事件循环实现非阻塞执行。事件循环不断检查调用栈，如果栈空，就从任务队列取出任务执行。任务分为 **宏任务**（setTimeout、setInterval、I/O 等）和 **微任务**（Promise.then、process.nextTick 等），微任务优先执行。

`JavaScript`是一门单线程的语言，意味着同一时间内只能做一件事，但是这并不意味着单线程就是阻塞，而实现单线程非阻塞的方法就是事件循环

JavaScript 中的事件循环是一个持续运行的过程，它不断监听call stack（调用栈）。它的主要功能是检查调用栈是否为空。如果调用栈为空，事件循环继续执行任务队列中等待的所有回调。在任务队列中，任务大致分为两类，即微任务和宏任务

宏任务：setTimeout、setInterval、DOM事件、AJAX请求

微任务：Promise, async/await

![ttt.gif](https://s2.loli.net/2025/12/24/8lUM2deRKaiQuhy.gif)



------

## 十五、JSON / 正则 / 编码

### 5. 常用的正则表达式有哪些?

### 6. 对JSON的理解

JSON 是一种基于文本的轻量级的数据交换格式。它可以被任何的编程语言读取和作为数据格式来传递。

JSON 中对象格式更加严格，比如说在 JSON 中属性值不能为函数，不能出现 NaN 这样的属性值等，因此大多数的 js 对象是不符合 JSON 对象的格式的。

### 16. escape、 encodeURI、encodeURIComponent的区别

这三个函数都是 JavaScript 中用来对 URL 或字符串进行编码的，但用途、范围和实现机制不同

| 函数                 | 编码对象        | 编码范围                              | 建议用途                 |
| -------------------- | --------------- | ------------------------------------- | ------------------------ |
| `escape`             | 字符串          | ASCII 字符保留，其余 `%XX` / `%uXXXX` | **不推荐使用**，历史遗留 |
| `encodeURI`          | 整个 URI        | 不编码 `: / ? # , ; & = @`            | 编码完整 URL             |
| `encodeURIComponent` | URI 组件/参数值 | 编码几乎所有非字母数字字符            | 编码单独参数或片段       |

```js
const url = 'http://example.com/你好?name=Tom&age=20'

console.log(escape(url))
// "http://example.com/%u4F60%u597D?name=Tom&age=20"

console.log(encodeURI(url))
// "http://example.com/%E4%BD%A0%E5%A5%BD?name=Tom&age=20"

console.log(encodeURIComponent(url))
// "http%3A%2F%2Fexample.com%2F%E4%BD%A0%E5%A5%BD%3Fname%3DTom%26age%3D20"
```

### 35. js 中什么是可选链操作符，如何访问数组

[可选链操作符 - MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

[Optional chaining (?.)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

`?.` 操作符，可以嵌套获取对象的属性值。通过获取对象属性获得的值可能是 undefined 或 null 时，可选链操作符提供了一种方法来简化被连接对象的值访问。

```js
const o = {};

// 添加可选链之前
o && o.a && o.a.b && o.a.b.c && o.a.b.c.d;

// 添加可选链之后
o?.a?.b?.c?.d;

const obj = { a: [1, 2], b() {} };
// 访问数组
obj?.a?.[0];
//使用方法
obj?.b?.();
```

### 10. es6中模板语法与字符串的处理

```js
var finalString = `my name is ${name}, I work as a ${career} I love ${hobby[0]} and ${hobby[1]}`
```



- 模版引擎实现原理？
- Unicode、 UTF-8、UTF-16、UTF-32的区别
- 说说你对正则表达式的理解？应用场景？

------

## 十六、Proxy / Reflect / 元编程

### 11. proxy实现什么功能

[这章节对`Object.defineProperty`和`Proxy`有相关讲解](# 1. Vue的基本原理)

`Object.defineProperty` 无法监听到数组、对象的修改，`Proxy`可以。

在 Vue3.0 中通过 `Proxy` 来替换原本的 `Object.defineProperty` 来实现数据响应式。

```js
let onWatch = (obj, setBind, getLogger) => {
  let handler = {
    get(target, property, receiver) {
      getLogger(target, property);
      return Reflect.get(target, property, receiver);
    },
    set(target, property, value, receiver) {
      setBind(value, property);
      return Reflect.set(target, property, value);
    }
  };
  return new Proxy(obj, handler);
};
let obj = { a: 1 };
let p = onWatch(
  obj,
  (v, property) => {
    console.log(`监听到属性${property}改变为${v}`);
  },
  (target, property) => {
    console.log(`'${property}' = ${target[property]}`);
  }
);
p.a = 2; // "监听到属性a改变为2"
p.a; // 'a' = 2
```



- Proxy 和 Reflect 有什么关系
- Proxy 和 Object.defneProperty 的区别
- Object.defneProperty 是否可以监听拦截数组变化
- Proxy 能否监听对象中嵌套对象的引用变化Proxy 有哪些实际使用场景
- Proxy set 拦截器有哪些参数?分别表示什么含义?
- Proxy 可以拦截数组变化吗?
- Reflect 内置对象及其常用函数详解
- Reflect.get()与直接通过对象点操作符访问属性的区别
- 如何排查是谁在修改对象?

------

## 十七、性能 / 安全 / eval

- 你对 eval 了解多少?
- 有没有遇到 js 捕捉不到异常堆栈信息的情况