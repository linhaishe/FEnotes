# Web 应用的基础设施

在我们正式开始编程之前，我们先简单看一个样例应用https://studies.cs.helsinki.fi/exampleapp/，了解一些web开发的基本原则。

这些应用只是为了演示本课程需要讲到的一些基本概念，绝不是 web 应用的开发标杆。 相反，它展示了一些陈旧的 web 开发技术，而这些技术在今天甚至可以被视作糟糕的实践。

我们将在[第1章](https://fullstackopen.com/zh/part1)正式讲推荐的编码风格。

现在以及接下来的课程都使用 Chrome 浏览器。

在浏览器上打开这个[示例应用](https://studies.cs.helsinki.fi/exampleapp)。应用加载通常需要等一会儿。

Web 开发第一规则: 始终在浏览器上打开你的开发者控制台。 在 macOS 上，按 `F12`或者 `option-cmd-i`打开控制台。 在 Windows 上，按 `F12`或 `ctrl-shift-i`打开控制台。

在继续课程之前，确保搞清楚如何在你的电脑上打开开发者控制台(如果必要的话请谷歌) ，并记得在开发 web 应用时始终保持它是开着的。

开发者控制台长这样：

![fullstack content](https://fullstackopen.com/static/aaaefdadeccea5768728b3cdd41fd8f2/5a190/1e.png)

请确保打开 Network 标签页，如图所示，选中 Disable cache 选项。 保存日志（Preserve log）选项也很有用: 它能够在重新加载页面时保存应用所打出日志。

虽然在入门介绍中我们常使用网络（Network）标签，但开发而言最重要的标签是控制台（*Console*）。

### HTTP GET

服务器和 web 浏览器使用 [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) 协议相互通信。 “网络（Network）”选项卡能够显示浏览器和服务器之间是如何通信的。

当你重新加载页面(在浏览器中按 F5 键或者 ↺ 按钮) ，控制台会显示两个事件:

- 浏览器会从服务器中获取*studies.cs.helsinki.fi/exampleapp* 页面的内容
- 然后下载图像 *kuva.png*

![fullstack content](https://fullstackopen.com/static/af6f88822db737cac2ea80d9343756fc/5a190/2e.png)

在小屏幕上，您可能需要拉大控制台窗口才能看到这些内容。

点击第一个事件会显示更多关于本次请求的细节

![fullstack content](https://fullstackopen.com/static/ddcd5afaeabfc1b0e8a4325bfeff90ee/5a190/3e.png)

上半部分，General 中的内容，说明了浏览器使用 [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) 方法向地址 https://studies.cs.helsinki.fi/exampleapp/ 发送了一个请求（虽然由于图片已经取到了，地址悄悄发生了变化），并且请求成功，因为服务器响应的状态码为 200。

浏览器的请求（request）和服务器的响应（response）有一些[Headers头](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)信息:

![fullstack content](https://fullstackopen.com/static/5e6569d4ad80edce4a03a25358b8f195/5a190/4e.png)

上面的 *响应头Response headers*部分告诉我们一些信息，例如，响应的大小(以字节为单位)和响应的具体时间。 有个重要的 header [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) 告诉我们，响应是[utf-8](https://en.wikipedia.org/wiki/UTF-8) 格式的文本文件，其内容已用 HTML 格式化。 通过这种方式，浏览器知道响应是一个常规的 html 页面，并将它“像一个网页”一样渲染到浏览器中。

Response 标签页展示了响应数据，这是一个常规的 html 页面。 *body*部分决定了其渲染在屏幕上的页面结构:

![fullstack content](https://fullstackopen.com/static/4e49815c455c943b6eb14fe8cc0cefb3/5a190/5e.png)

页面包含一个 [div](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) 元素，该元素又包含一个标题、一个指向 notes 页面的链接，以及一个 img 标签，并显示了创建 note 的数量。

由于有一个 img 标签，浏览器会执行第二个 http 请求，从服务器获取图像 kuba.png。 请求的详情如下:

![fullstack content](https://fullstackopen.com/static/f053fa9082a1ad72066fa193346d0378/5a190/6e.png)

这个请求是给地址 https://studies.cs.helsinki.fi/exampleapp/kuva.png 发送的，它的类型是 HTTP GET。 响应头告诉我们，响应大小为 89350 字节，其[Content-type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)为 image/png，因此它是一个 png 图像。 浏览器使用这些信息将图像正确地渲染到屏幕上。

在浏览器上打开页面 https://studies.cs.helsinki.fi/exampleapp/ 所产生的整个调用链条如下:

![fullstack content](https://fullstackopen.com/static/972354fefd202e82e2c4a64d4d7c6125/5a190/7e.png)

首先，浏览器向服务器发出 HTTP GET 请求，以获取页面的 HTML 代码。 Html 中的 img 标签提示浏览器还要去获取图像 kuba.png。 浏览器将 HTML 页面和图像渲染到屏幕上。

尽管很难观察到，但 HTML 页面在从服务器获取图像之前就已经开始渲染了。

### Traditional web applications

【传统的网络应用】

示例应用的主页运作方式与传统的 web 应用类似。 当进入一个页面时，浏览器会从服务器获取 HTML 文档的详细页面结构，以及文本内容。

服务器以某种方式生成了这个文档。 这个文档可能是保存在服务器目录中的静态文本文件， 也可能是服务器根据应用的代码动态构建的 HTML 文档，比如，数据可能是来自数据库的。

示例应用的 HTML 代码是动态的，因为它包含已创建 Note 的数量信息。

主页的 HTML 代码如下所示:

```js
const getFrontPageHtml = noteCount => {
  return `
    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
        <div class='container'>
          <h1>Full stack example app</h1>
          <p>number of notes created ${noteCount}</p>
          <a href='/notes'>notes</a>
          <img src='kuva.png' width='200' />
        </div>
      </body>
    </html>
`;
};

app.get('/', (req, res) => {
  const page = getFrontPageHtml(notes.length);
  res.send(page);
});
```

你目前还不需要去理解这些代码的细节。

Html 页面的内容被保存为 template 模板字符串，或者说是一个能够运行的字符串，因为它其中包含有变量。 在模板字符串中，页面中动态更改的那部分内容——已保存 Note 的数量（即代码中的 *noteCount*），被动态地替换为了 Note 的当前数量（即代码中的 *notes.length*）

在代码中间编写 HTML 当然不是明智的做法，但对于老派的 PHP 程序员来说，这是一种常规操作。

在传统的 web 应用中，浏览器是个“憨憨”。 它只会从服务器获取 HTML 数据，所有应用的逻辑都在服务器上处理。 服务器中的程序可以是，赫尔辛基大学 [Web-palvelinohjelmointi](https://courses.helsinki.fi/fi/tkt21007/119558639)课程中的 Java Spring、也可以是 [tietokantasovellus](https://materiaalit.github.io/tsoha-18/)课程中的 Python Flask ，又或者是 [Ruby on Rails](http://rubyonrails.org/)。

这个样例使用了 Node.js 中的 [Express](https://expressjs.com/)。

本课程都将会使用 Node.js 和 Express 来创建 Web 服务器。

### Running application logic on the browser

【在浏览器上运行应用逻辑】

保持控制台打开状态。 单击 🚫按钮清空控制台。

现在当你进入 [notes](https://studies.cs.helsinki.fi/exampleapp/notes)页面时，浏览器会执行 4 个 HTTP 请求:

![fullstack content](https://fullstackopen.com/static/02ed5b206f76e1f9bcf4ad3ffff8a2b4/5a190/8e.png)

所有的请求都请求了不同的类型。 第一个请求的类型是 document。 也就是页面的 HTML 代码，看起来如下:

![fullstack content](https://fullstackopen.com/static/8856aaf0012972e3b7d5b1dfc6aaa3f6/5a190/9e.png)

当我们比较浏览器上显示的页面和服务器返回的 HTML 代码时，我们注意到这些代码并不包含 Note 列表的数据。 Html 的 [head](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)部分 包含一个 [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) 标签，它会让浏览器去 获取一个名为 main.js 的 JavaScript 文件。

JavaScript 代码看起来像这样:

```js
var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const data = JSON.parse(this.responseText);
    console.log(data);

    var ul = document.createElement('ul');
    ul.setAttribute('class', 'notes');

    data.forEach(function(note) {
      var li = document.createElement('li');

      ul.appendChild(li);
      li.appendChild(document.createTextNode(note.content));
    });

    document.getElementById('notes').appendChild(ul);
  }
};

xhttp.open('GET', '/data.json', true);
xhttp.send();
```

代码的细节现在并不重要，穿插一些代码，是为了增加图像与文本的趣味性。我们将在[第1章](https://fullstackopen.com/zh/part1)正式地开始编码。 本章节的示例代码实际上与本课程所要讲的编码技术毫无关系。

> 有些人可能想问为什么要使用 xhttp 对象而不是使用现代的获取方法。 这是因为我们不想引入 promise 的概念，而且代码在这一章节只是二等公民。 在第 2 章节中，我们将回过头来用更加现代的方式来向服务器发送请求。

在获取到 script 标签后，浏览器便立即开始执行 script 的代码。

最后两行定义了让浏览器对服务器地址 /data.json 执行一个 HTTP GET 请求:

```js
xhttp.open('GET', '/data.json', true);
xhttp.send();
```

这是“Network”选项卡上显示 request 信息的最低要求。

我们可以试着直接通过浏览器访问 https://studies.cs.helsinki.fi/exampleapp/data.json 地址:

![fullstack content](https://fullstackopen.com/static/cb83e4c1c89fd4bc662942457f30403e/5a190/10e.png)

在这里我们找到了以 JSON 格式展示的 Note ，这就是Note的 “原始数据”。 默认配置下，浏览器不太擅长显示 json 格式的数据。 可以使用插件来处理 Json 格式。 例如，将 [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) 安装到 Chrome，然后重新加载页面。 数据现在可以被更好地格式化展示出来了:

![fullstack content](https://fullstackopen.com/static/fd335c19a19f2176040834b7c5533193/5a190/11e.png)

因此，上面 notes 页面的 JavaScript 代码会下载包含 Note 列表的的 JSON 数据，并利用 Note 的内容构建出一个符号列表:

构建是通过如下代码实现的:

```js
const data = JSON.parse(this.responseText);
console.log(data);

var ul = document.createElement('ul');
ul.setAttribute('class', 'notes');

data.forEach(function(note) {
  var li = document.createElement('li');

  ul.appendChild(li);
  li.appendChild(document.createTextNode(note.content));
});

document.getElementById('notes').appendChild(ul);
```

代码首先创建了一个带有 ul-标签 的无序列表...

```js
var ul = document.createElement('ul');
ul.setAttribute('class', 'notes');
```

然后再为每个 Note 加上一个 li-标签。仅将每个 Note 的 content 字段变成了 li-标签 的内容，而原始数据的 timestamps 时间戳在这里并没派上用场。

```js
data.forEach(function(note) {
  var li = document.createElement('li');

  ul.appendChild(li);
  li.appendChild(document.createTextNode(note.content));
});
```

现在打开控制台上的 Console 标签:

![fullstack content](https://fullstackopen.com/static/7b61ba46a7734400891ed78cf57011cb/5a190/12e.png)

通过单击行首的小三角形，可以展开控制台上的文本。

![fullstack content](https://fullstackopen.com/static/b6c827a56505ac8a9243162a448ada21/5a190/13e.png)

控制台上能输出内容是因为代码中的 console.log 命令:

```js
const data = JSON.parse(this.responseText);
console.log(data);
```

因此，在从服务器接收到数据之后，代码将其打印到了控制台。

在整个课程中，你会经常用到 Console 选项卡和 Console.log 命令。

### Event handlers and Callback functions

【事件处理和回调函数】

这段代码的结构有点奇怪:

```js
var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    // code that takes care of the server response
  }
};

xhttp.open('GET', '/data.json', true);
xhttp.send();
```

发送到服务器的请求放在了最后一行，但是处理响应的代码却在上面定义了。这是怎么回事？

这一行中，

```js
xhttp.onreadystatechange = function () {}
```

onreadystatechange 这个事件处理程序是定义在 xhttp 对象上的，xhttp对象是用于执行请求的。当这个对象的状态发生改变时，浏览器调用了这个事件处理函数。 这个函数代码检查了 [readyState](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState) 是否等于 4(它描述了操作已完成的状态) ，以及响应的 HTTP 状态码是否为 200。

```js
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    // code that takes care of the server response
  }
};
```

这种调用事件处理程序的机制在 JavaScript 中非常常见。 <mark>事件处理函数被称为回调函数（[callback](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) functions）。</mark> **应用代码并不直接调用函数本身，而是运行时环境（浏览器）会在事件发生时的适当时间调用函数。**

### Document Object Model or DOM

我们可以将 html 页面看作隐式树结构。

```
html
  head
    link
    script
  body
    div
      h1
      div
        ul
          li
          li
          li
      form
        input
        input
```

在控制台Elements选项卡中可以看到相同的树状结构。

![fullstack content](https://fullstackopen.com/static/081eb2d1f52d2536382d5d3efe0bc87f/5a190/14e.png)

浏览器的功能就是基于这种，把 HTML元素描述成一棵树的想法。

文档对象模型(Document Object Model，DOM)是一个应用编程接口(Application Programming Interface，API) ，它支持对 web 页面对应的元素树进行编程修改。

上一部分中介绍的 JavaScript 代码就是使用 DOM-API 向页面添加 Note 列表。

下面的代码为变量 ul 创建了一个新节点，并向其添加一些子节点:

```js
var ul = document.createElement('ul');

data.forEach(function(note) {
  var li = document.createElement('li');

  ul.appendChild(li);
  li.appendChild(document.createTextNode(note.content));
});
```

最后，ul 变量的树分支被接到了整个页面的 HTML 树中的适当位置:

```js
document.getElementById('notes').appendChild(ul);
```

### Manipulating the document-object from console

【从控制台中操作文档对象】

Html 文档 DOM 树的最顶层节点称为文档*document*对象。 我们可以使用 DOM-API 在网页上执行各种操作。 您可以通过在控制台中键入 document 来访问文档对象:

![fullstack content](https://fullstackopen.com/static/ac9364f4d597d187d271a1628a332e7d/5a190/15e.png)

让我们从控制台向页面添加一个新的 Note。

首先，我们从页面中获得 Note 列表，该列表位于页面的第一个 ul 元素中:

```js
list = document.getElementsByTagName('ul')[0];
```

然后创建一个新的 li 元素并添加一些文本内容:

```js
newElement = document.createElement('li');
newElement.textContent = 'Page manipulation from console is easy';
```

并将新的 li 元素添加到列表中:

```js
list.appendChild(newElement);
```

![fullstack content](https://fullstackopen.com/static/5971f5573de2bc91961f679e27430097/5a190/16e.png)

虽然页面在浏览器上被更新了，这些更改不是永久性的。 如果页面重新加载，新的 Note 就消失了，因为更改并没有推送到服务器。 浏览器获取的 JavaScript 代码会总是基于 https://studies.cs.helsinki.fi/exampleapp/data.json 的 JSON 数据来创建 Note 列表。

### CSS

Notes 页面的 HTML 代码中 head 元素包含了一个 [link](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link) 标签，该标签确定浏览器必须从地址 [main.css](https://studies.cs.helsinki.fi/exampleapp/main.css)中获取 [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 样式表。

层叠样式表, 或者叫 CSS，是一种用来确定 web 应用外观的标记语言。

获取的 css 文件如下所示:

```css
.container {
  padding: 10px;
  border: 1px solid;
}

.notes {
  color: blue;
}
```

该文件定义了两个类选择器 [class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors)。 它们用于选择页面的某些部分，并对它们定义样式规则来装饰它们。

类选择器的定义始终以句点开头，并包含类的名称。

这些类是属性[attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class)，可以添加到 HTML 元素中。

CSS 属性可以在控制台的 element 标签上查看:

![fullstack content](https://fullstackopen.com/static/4504fc2e95de826dd766aca1d0940ea4/5a190/17e.png)

最外面的 div 元素有 class 属性 ，值为 container ，包含 notes 列表的 ul 元素也有 class 属性 ，名为 notes。

CSS 规则定义了 container 类的元素，将用一个像素宽的边框 [border](https://developer.mozilla.org/en-US/docs/Web/CSS/border)勾勒出来。 它还为该元素设置了 10 个像素的填充 [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)。 这会在元素内容和边框之间增加一些空白。

第二个 CSS 规则将文本颜色设置为蓝色。

Html 元素也可以有 class 以外的其他属性。 包含 Note 的 div 元素有一个 id 属性。 JavaScript 代码使用 id 来查找元素。

控制台的*Elements*选项卡可用于更改元素的样式。

![fullstack content](https://fullstackopen.com/static/ef664dbcddaeef64c5ff6e180e42e5ca/5a190/18e.png)

在控制台上所做的更改也不是永久性的。 如果要进行持久的更改，必须将更改保存到服务器上的 CSS 样式表中。

### Loading a page containing JavaScript - revised

【加载一个包含 JavaScript 的页面-复习】

让我们复习一下在浏览器上打开页面 https://studies.cs.helsinki.fi/exampleapp/notes 时会发生什么。

![fullstack content](https://fullstackopen.com/static/7094858c9c7ec9149d10607e9e1d94bb/5a190/19e.png)

- 浏览器使用 HTTP GET 请求从服务器获取定义内容和页面结构的 HTML 代码
- Html 代码中的 Links 标签会让浏览器获取 CSS 样式表 main.css
- 以及 JavaScript 代码文件 main.js
- 浏览器执行 JavaScript 代码，代码向地址https://studies.cs.helsinki.fi/exampleapp/data.json 发出 HTTP GET 请求，请求返回了包含 note 的 JSON 数据。
- 获取数据后，浏览器执行一个*event handler 事件处理程序*, 使用 DOM-API 将 Note 渲染到页面

### Forms and HTTP POST

【表单与 HTTP POST】

接下来让我们看看添加 Note 是如何完成的。

Notes 页面包含一个 [form 元素](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form)

![fullstack content](https://fullstackopen.com/static/2dbe9f6d3c9999766d2cbad6200fea40/5a190/20e.png)

当单击表单上的按钮时，浏览器将向服务器发送用户的输入。 让我们打开 Network 标签页，看看提交表单时发生了什么:

![fullstack content](https://fullstackopen.com/static/7951d2221d80f63a78350106150d5e61/5a190/21e.png)

很惊奇吧，提交表单总共会导致 5 个 HTTP 请求。

第一个是表单提交事件。 让我们放大一下:

![fullstack content](https://fullstackopen.com/static/ac09c143991ad160bdaa1c1381d93f7b/5a190/22e.png)

它是对服务器 */new_note*地址发送的 [HTTP POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)请求。 服务器用 HTTP 状态码 302 进行响应。 这是一个[URL 重定向](https://en.wikipedia.org/wiki/URL_redirection)，服务器通过这个 URL 重定向，请求浏览器执行一个新的 HTTP GET 请求，该请求定义在 Header 的 Location (即 /notes 地址)中。

因此，浏览器重新加载 Notes 页面。 重新加载会导致另外三个 HTTP 请求: 获取样式表(main.css)、 JavaScript 代码(main.js)和 notes 的原始数据(data.json)。

Network选项卡还显示了与表单一起提交的表单数据:

![fullstack content](https://fullstackopen.com/static/baad2297bb966ed9387cb3a0d79fa4f8/5a190/23e.png)

Form 标签具有属性 action 和 method，它们定义了将表单作为一个 HTTP POST 请求提交到地址 */new_note*。

![fullstack content](https://fullstackopen.com/static/9463d1dca4170015c47e79065ff98820/5a190/24e.png)

服务器上负责 POST 请求的代码很简单(注意: 此代码在服务器上，而不是在浏览器获取的 JavaScript 代码上) :

```js
app.post('/new_note', (req, res) => {
  notes.push({
    content: req.body.note,
    date: new Date(),
  });

  return res.redirect('/notes');
});
```

数据作为 POST-请求的[body](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)发送到服务器。

服务器可以通过访问请求对象 req 的 req.body 字段来访问发送来的数据。

Server 创建一个新的 note 对象，并将其添加到一个名为 notes 的数组中。

```js
notes.push({
  content: req.body.note,
  date: new Date(),
});
```

Note 对象包含两个字段: 包含 Note 实际内容的 content，以及包含创建 Note 的日期和时间的 date。 服务器不会将新 Note 保存到数据库中，因此当服务器重新启动服务时，新的 Note 就会消失。

### AJAX

应用的 Notes 页面遵循本世纪初的 web 开发风格，并且“使用了 Ajax”。 这种技术在当时，2000 年初正处于 web 技术浪潮的顶峰。

[AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)) (Asynchronous JavaScript and XML) 是在浏览器技术进步的基础上于 2005 年 2 月引入的一个术语，它描述了一种新的革命性的方法，<mark>这种方法使用包含在 HTML 中的 JavaScript 来获取网页内容，而且不需要重新渲染页面。</mark>

在 AJAX 之前的年代，所有的 web 页面都像我们在本章前面看到的传统 web 应用一样工作。 页面上显示的所有数据都是从服务器生成的 html 代码获取的。

Notes 页面使用了 AJAX 获取 Notes 数据。 提交表单仍然使用传统的 web 表单提交机制。

<mark>应用的 url 反映了过去无忧无虑的时光。 数据从 url https://studies.cs.helsinki.fi/exampleapp/data.JSON 中获取，新的 Note 被发送到 url https://studies.cs.helsinki.fi/exampleapp/new_note 。 如今，这样的 url 被认为是不可接受的，因为它们没有遵循公认的 RESTful api 约定</mark>，我们将在第三章中进一步研究

现在 AJAX 这个术语是如此普遍，以至于人们认为它是理所当然的。 但这个词已经逐渐被遗忘，“新时代的我们”甚至没有听说过它。

### Single page app

【单页面应用】

在我们的示例应用中，主页的工作方式类似于传统的网页: 所有的逻辑都在服务器上，浏览器只按照指示渲染 HTML。

Notes 页面为浏览器提供了一些职责，为现有的 Note 生成 HTML 代码。 浏览器通过执行从服务器获取的 JavaScript 代码来处理这个任务。 代码从服务器以Json格式获取 Note，并对其添加 HTML 元素，并利用 DOM-API 将 Note 显示到页面中。

近年来，创建网络应用的单页应用 [Single-page application](https://en.wikipedia.org/wiki/Single-page_application) (SPA) 风格出现了。SPA 类型的网站不会像我们的示例应用那样从服务器上单独获取所有页面，而是只从服务器获取一个 HTML 页面，其内容由 JavaScript 在浏览器中执行操作。

我们的应用的 Notes 页面与 SPA 风格的应用有一些相似之处，但它还没有完全到位。 尽管显示Note 的逻辑是在浏览器上运行的，但页面仍然使用传统的方式添加新Note 。 数据通过表单提交发送到服务器，服务器指示浏览器重新加载带有重定向的 Notes 页面。

我们示例应用的单页应用版本可以在 https://studies.cs.helsinki.fi/exampleapp/spa 中找到。 乍一看，这个应用看起来与前一个应用完全相同。 Html 代码几乎完全相同，但 JavaScript 文件不同(spa.js) ，form 标签的定义方式有一个小小的变化:

![fullstack content](https://fullstackopen.com/static/cb1893b2f18168168b3337ef994f0347/5a190/25e.png)

表单没有*action*属性或*method*属性来定义如何以及往哪里发送输入数据。

打开 Network-选项卡并通过单击 🚫 按钮清空它。 当您现在创建一个新的便笺时，您会注意到浏览器只向服务器发送了一个请求。

![fullstack content](https://fullstackopen.com/static/07beb53097a520517c1c28ff17fc907a/5a190/26e.png)

Post 请求到地址*new_note_spa*，包含新 Note 的 JSON 数据，其中既包含 Note 的内容(content) ，也包含时间戳(date) :

```js
{
  content: "single page app does not reload the whole page",
  date: "2019-05-25T15:15:59.905Z"
}
```

请求的 Content-Type 头信息告诉服务器，所包含的数据是以 JSON 格式表示的。

![fullstack content](https://fullstackopen.com/static/5819436c98e4cce143fce3fe9bc534b9/5a190/27e.png)

如果没有这个头，服务器将不知道如何正确地解析数据。

服务器用创建的状态码[201](https://httpstatuses.com/201)进行响应。 这次服务器没有请求重定向，浏览器会保持在同一页面上，并且不再发送 http 请求。

这个应用的 SPA 版本并不以传统的方式发送表单数据，而是使用从服务器获取的 JavaScript 代码。 我们将稍微研究一下这段代码，虽然还没有必要理解它的所有细节。

```js
var form = document.getElementById('notes_form');
form.onsubmit = function(e) {
  e.preventDefault();

  var note = {
    content: e.target.elements[0].value,
    date: new Date(),
  };

  notes.push(note);
  e.target.elements[0].value = '';
  redrawNotes();
  sendToServer(note);
};
```

命令 *document.getElementById('notes_form')* 指示代码从页面中提取 form 元素，并注册一个事件处理函数来处理表单提交事件。 事件处理函数将立即调用方法 e.preventDefault () ，以防止对表单 submit 的默认处理。 默认处理会将数据发送到服务器并导致重定向（一次新的Get请求），这不是我们的初衷。

然后，事件处理程序创建一个新的 Note，使用命令*notes.push(note)*将其添加到 Note 列表中，并在页面上重新渲染了 Note 列表，最终向服务器发送了新建 Note 的请求。

向服务器发送 Note 的代码如下:

```js
var sendToServer = function(note) {
  var xhttpForPost = new XMLHttpRequest();
  // ...

  xhttpForPost.open('POST', '/new_note_spa', true);
  xhttpForPost.setRequestHeader('Content-type', 'application/json');
  xhttpForPost.send(JSON.stringify(note));
};
```

代码确定数据是通过 HTTP POST 请求发送的，数据类型是 JSON。 数据类型由 Content-type Header 确定。 然后，数据以 json 字符串的形式发送。

应用代码可以在 https://github.com/mluukkai/example_app 上找到。 值得注意的是，这个应用只是用来演示课程的概念。 该代码在某种程度上遵循了糟糕的开发风格，不应该在创建自己的应用时作为示例使用。 使用的 url 也是如此。 发送新Note 的 URL，即新建Note 的*new_note_spa*并不遵循当前的最佳实践。

### JavaScript-libraries

【JavaScript 库】

这个示例应用是通过所谓的[vanilla JavaScript](https://medium.freecodecamp.org/is-vanilla-javascript-worth-learning-absolutely-c2c67140ac34) 来完成的，只使用了 DOM-API 和 JavaScript 来操作页面的结构。

与仅使用 JavaScript 和 DOM-API 不同，通常会使用比直接操作 DOM-API 更容易的工具库来操作页面。 其中一个非常流行的库就是 [jQuery](https://jquery.com/) 。

当时，在 web 应用主要遵循服务器生成 HTML 页面的传统风格，jQuery 当时是在这种情况下发展起来的。这种风格的功能通过在浏览器端使用 JavaScript 搭配使用 jQuery 来增强。 jQuery 成功的原因之一是它所谓的跨浏览器兼容性。 不管是哪家公司的哪个浏览器，这个库都能正常工作，所以不需要特定于浏览器的解决方案。 如今，由于 VanillaJS 的进步，使用 jQuery 已经不那么合理了，而且最流行的浏览器通常都能很好地支持基本功能。

单页应用的兴起带来了几种比 jQuery 更“现代”的网页开发方式。 第一波开发者的最爱是 [BackboneJS](http://backbonejs.org/).。 自 2012 年 [launch](https://github.com/angular/angular.js/blob/master/CHANGELOG.md#100-temporal-domination-2012-06-13) 以来，谷歌的 [AngularJS](https://angularjs.org/) 几乎快速成为现代网络开发的行业标准。

然而，自从 Angular 团队在 2014 年 10 月宣布对第 1 版的支持将结束，Angular 2 将不再向后兼容第一版后，Angular 的受欢迎程度直线下降。 Angular 2 和更新的版本没有得到太热烈的欢迎。

目前，实现 web 应用浏览器端逻辑的最流行的工具是 Facebook 的 React-库。 在本课程中，我们将熟悉 React 和 [Redux](https://github.com/reactjs/redux) 库，它们经常一起使用。

React 的势头看起来很猛，但是 JavaScript 的世界是不断变化的。 例如，最近的一个新秀 [VueJS](https://vuejs.org/) 已经引起了一些兴趣。

### Full stack web development

【全栈-web 开发】

这个课程的名字是什么意思？全栈是一个流行词，每个人都在谈论它，但没有人真正知道它的意思。 或者至少，对于这个术语没有一致的定义。

几乎所有的 web 应用都有(至少)两个“层” : 最接近最终用户的浏览器是最顶层，而服务器是最底层。 在服务器下面通常还有一个数据库层。 因此，我们可以将 web 应用的体系结构看作是一层层的堆栈。

通常，我们也会讨论[前端frontend](https://en.wikipedia.org/wiki/Front_and_back_ends) 和 [后端backend](https://en.wikipedia.org/wiki/Front_and_back_ends)。 浏览器是前端，运行在浏览器上的 JavaScript 是前端代码。 另一方面，服务器是后端。

在本课程的上下文中，全栈 web 开发意味着我们关注应用的所有部分: 从前端、后端到数据库。 有时候，服务器上的软件及其操作系统会被看作是全栈的一部分，但我们不会深入讨论这部分内容。

我们将使用 JavaScript 编写后端代码，使用 [Node.js](https://nodejs.org/en/) 运行时环境。 在全栈的多个层次上使用相同的编程语言，给全栈 web 开发提供了一个全新的维度。 然而，对于所有层次的栈，使用相同的编程语言(JavaScript)并不是全栈 web 开发的必要条件。

过去，对于开发人员来说，更常见的做法是专注于全栈的某个层，例如后端。 后端和前端的技术栈完全不同。 随着全栈趋势的出现，对于开发人员来说，熟练掌握应用和数据库的全栈内容已经变得非常普遍。 通常情况下，全栈开发人员还必须有足够的配置和管理技能来操作他们的应用，例如，上云。

### JavaScript fatigue

【JavaScript 疲劳】

全栈 web 开发在许多方面都具有挑战性。 在许多地方会有突发情况，并且调试起来比普通桌面应用要困难得多。 JavaScript (与许多其他语言相比) 并不总是像你期望的那样工作 ，其运行时环境的异步工作方式带来了各种各样的挑战。 网络中的通信需要对 http 协议的知识储备。 还必须处理数据库、服务器管理和配置。 了解足够的 CSS 至少在一定程度上能够使应用显得好看。

JavaScript 的世界发展得很快，也带来了一系列的挑战。 工具、库和语言本身都在不断发展。 有些人已经开始厌倦了这种不断的变化，并为此创造了一个新词: JavaScript 疲劳。

在本课程中，您将遭受 JavaScript 疲劳的折磨。 对我们来说幸运的是，有几种方法可以使学习曲线变得平滑，我们可以从编码而不是配置开始。 我们不能完全避免配置，但是我们可以在接下来的几周里愉快地推进，同时避免糟糕的配置地狱。