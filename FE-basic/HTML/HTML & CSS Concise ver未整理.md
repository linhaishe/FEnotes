# HTML & CSS Concise ver

## HTML

### 概述

- HTML文档的后缀名

	- .html
	- .htm

- 网页编码格式声明

	- 对于中文网页需要使用 <meta charset="utf-8"> 声明编码，否则会出现乱码。有些浏览器(如 360 浏览器)会设置 GBK 为默认编码，则你需要设置为 <meta charset="gbk">。
	- 目前在大部分浏览器中，直接输出中文会出现中文乱码的情况，这时候我们就需要在头部将字符声明为 UTF-8。

- HTML含义

	- HTML 指的是超文本标记语言: HyperText Markup Language
	- HTML 不是一种编程语言，而是一种标记语言
	- 标记语言是一套标记标签 (markup tag)
	- HTML 使用标记标签来描述网页
	- HTML 文档包含了HTML 标签及文本内容
	- HTML文档也叫做 web 页面
	- HTML对大小写不敏感，尽量使用小写

- <!DOCTYPE> 声明

	- 声明有助于浏览器中正确显示网页。网络上有很多不同的文件，如果能够正确声明HTML的版本，浏览器就能正确显示网页内容。doctype 声明是不区分大小写的

- 相对路径和绝对路径

	- 相对路径(Relative Path)

		- 含义

			- 用途：指定由这个文件所在的路径引起的跟其它文件（或文件夹）的路径关系,如果源文件和引用文件在同一个目录里，直接写引用文件名即可，这时引用文件的方式就是使用相对路径。

		- 同一个目录的相对文件引用—直接写引用文件名即可 

			- 假设info.html路径是：c:/Inetpub/wwwroot/sites/blabla/info.html 
假设index.html路径是：c:/Inetpub/wwwroot/sites/blabla/index.html 
			- 在info.html加入index.html超链接的代码应该这样写：<a href = "index.html">这是超连接</a>

		- ../表示源文件所在目录的上一级目录，../../表示源文件所在目录的上上级目录，以此类推。
		- 如何表示上级目录

			- 假设info.html路径是：c:/Inetpub/wwwroot/sites/blabla/info.html 
假设index.html路径是：c:/Inetpub/wwwroot/sites/index.html 
			- info.html加入index.html超链接的代码

				- <a href = "../index.html">这是超连接</a>

		- 如何表示上上级目录

			- 假设info.html路径是：c:/Inetpub/wwwroot/sites/blabla/info.html 
假设index.html路径是：c:/Inetpub/wwwroot/index.html 
			- <a href = "../../index.html">index.html</a>

		- 如何表示下级目录

			- 假设info.html路径是：c:/Inetpub/wwwroot/sites/blabla/info.html 
假设index.html路径是：c:/Inetpub/wwwroot/sites/blabla/html/index.html 
			- 在info.html加入index.html超链接的代码应该这样写

				- <a href = "html/index.html">这是超连接</a>

			- 假设info.html路径是：c:/Inetpub/wwwroot/sites/blabla/info.html 
假设index.html路径是：c:/Inetpub/wwwroot/sites/blabla/html/tutorials/index.html 
			- <a href = "html/tutorials/index.html">这是超连接</a>

	- 绝对路径(Absolute Path)

		- c:/website /img/photo.jpg

### 编辑器

- Notepad++：https://notepad-plus-plus.org/
- Sublime Text：http://www.sublimetext.com/
- VS Code：https://code.visualstudio.com/

### 元素

- HTML 标签

	- <标签>内容</标签>

- "HTML 标签" 和 "HTML 元素" 通常都是描述同样的意思.但是严格来讲, 一个 HTML 元素包含了开始标签与结束标签
- <p>这是一个段落。</p>

### 属性

- 基本内容

	- HTML 元素可以设置属性
	- 属性可以在元素中添加附加信息
	- 属性一般描述于开始标签
	- 属性总是以名称/值对的形式出现，比如：name="value"。

### 标题

- 标题

	- <h1>这是一个标题</h1>
<h2>这是一个标题</h2>
<h3>这是一个标题</h3>

- 水平线

	- <hr>

- 注释

	- <!-- 这是一个注释 -->

### 段落

- <p>这是一个段落。</p>
<p>这是另外一个段落。</p>
- 浏览器会自动地在段落的前后添加空行。（</p> 是块级元素）
- 换行（新行）

	- <br>
	- <p>这个<br>段落<br>演示了分行的效果</p>

### 文本格式化

- "计算机输出" 标签

	- <code>定义计算机代码
	- <kbd>	定义键盘码
	- <samp>定义计算机代码样本
	- <var>	定义变量
	- <pre>	定义预格式文本

- 文本格式化标签

	- <b>	定义粗体文本
	- <em>	定义着重文字
	- <i> 定义斜体字
	- <small> 定义小号字
	- <strong> 定义加重语气
	- <sub>	定义下标字
	- <sup>	定义上标字
	- <ins>	定义插入字
	- <del>	定义删除字

- 引文, 引用, 及标签定义

	- <abbr>定义缩写
	- <address>定义地址
	- <bdo>	定义文字方向
	- <blockquote>	定义长的引用
	- <q>定义短的引用语
	- <cite>	定义引用、引证
	- <dfn>	定义一个定义项目。

### 链接

- <a href="http://www.runoob.com">这是一个链接</a>
- 默认情况下，链接将以以下形式出现在浏览器中

	- 一个未访问过的链接显示为蓝色字体并带有下划线。
	- 访问过的链接显示为紫色并带有下划线。
	- 点击链接时，链接显示为红色并带有下划线。
	- 如果为这些超链接设置了 CSS 样式，展示样式会根据 CSS 的设定而显示。

- Dead Links

	- href="#"
	- <p>Click here to view more <a href="#">cat photos</a>.</p>
	- <a href='#'> <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

- target 属性

	- <a href="http://www.runoob.com/" target="_blank">访问菜鸟教程!</a>
	- 如果你将 target 属性设置为 "_blank", 链接将在新窗口打开。“_top”为同窗口打开

- 跳转

	- 在HTML文档中插入ID:

<a id="tips">有用的提示部分</a>

在HTML文档中创建一个链接到"有用的提示部分(id="tips"）"：

<a href="#tips">访问有用的提示部分</a>

或者，从另一个页面创建一个链接到"有用的提示部分(id="tips"）"：

<a href="http://www.runoob.com/html/html-links.html#tips">
访问有用的提示部分</a>

		- <p>
<a href="#C4">查看章节 4</a>
</p>
 
<h2><a id="C4">章节 4</a></h2>
<p>这边显示该章节的内容……</p>

### 头部

-  <head> 

	- 包含了所有的头部标签元素

-  <title>

	- 作用

		- 定义了浏览器工具栏的标题
		- 当网页添加到收藏夹时，显示在收藏夹中的标题
		- 显示在搜索引擎结果页面的标题

	- <title>文档标题</title>

-  <base> 

	- 标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接:
	- <base href="http://www.runoob.com/images/" target="_blank">
	- <head>
<base href="http://www.runoob.com/images/" target="_blank">
</head>
<body>
<img src="logo.png" width="24" height="39" alt="Stickman">
<a href="http://www.runoob.com">runoob.com</a>
</body>

		- 这里我们设置了图片的相对地址。能正常显示是因为我们在 head 部分设置了 base 标签，该标签指定了页面上所有链接的默认 URL，所以该图片的访问地址为 "http://www.runoob.com/images/logo.png"
		- 这个链接会在新窗口打开，即便它没有 target="_blank" 属性。因为在 base 标签里我们已经设置了 target 属性的值为 "_blank"。

-  <link> 

	- 作用

		- <link> 标签定义了文档与外部资源之间的关系。
		- <link> 标签通常用于链接到样式表:

	- <link rel="stylesheet" type="text/css" href="mystyle.css">

- <style>

	- 作用

		- <style> 标签定义了HTML文档的样式文件引用地址.
		- 在<style> 元素中你也可以直接添加样式来渲染 HTML 文档:

	- <style type="text/css">
h1 {color:red;}
p {color:blue;}
</style>

-  <meta>

	- 作用

		- meta标签描述了一些基本的元数据。不显示在页面上，但会被浏览器解析。
		- 用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。

	- <meta name="description" content="免费在线教程">
<meta name="keywords" content="HTML,CSS,XML,JavaScript">
<meta name="author" content="runoob">
<meta charset="UTF-8">

- <script>

	- 标签用于加载脚本文件，如： JavaScript。

### CSS

- 内联样式

	- 特殊的样式需要应用到个别元素时，就可以使用内联样式。 方法是在相关的标签中使用样式属性。
	- <p style="color:blue;margin-left:20px;">This is a paragraph.</p>

- 内部样式表

	- 当单个文件需要特别样式时，就可以使用内部样式表。你可以在<head> 部分通过 <style>标签定义内部样式表
	- <head>
<style type="text/css">
body {background-color:yellow;}
p {color:blue;}
</style>
</head>

- 外部样式表

	- 当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。
	- <head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

### 图像

- <img src="pulpit.jpg" alt="Pulpit rock" width="304" height="228">
- alt 属性用来为图像定义一串预备的可替换的文本。
- <map>	定义图像地图
- <area>	定义图像地图中的可点击区域
- coords指的应该是链接区域在图片中的坐标（像素为单位）
- shape指的是点击区域的形状
- 创建图像映射

	- 创建带有可供点击区域的图像地图。其中的每个区域都是一个超级链接。
	- <img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">

<map name="planetmap">
  <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
  <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
  <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
</map>

### 表格

- 表格表头

	- <table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>

- 没有边框的表格

	- <table border="0"></table>

- 带有标题的表格

	- <table border="1">
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$50</td>
  </tr>
</table>

- 跨行或跨列的表格单元格

	- <table border="1">
<tr>
  <th>Name</th>
  <th colspan="2">Telephone</th>
</tr>
<tr>
  <td>Bill Gates</td>
  <td>555 77 854</td>
  <td>555 77 855</td>
</tr>
</table>

<h4>单元格跨两列:</h4>
<table border="1">
<tr>
  <th>First Name:</th>
  <td>Bill Gates</td>
</tr>
<tr>
  <th rowspan="2">Telephone:</th>
  <td>555 77 854</td>
</tr>
<tr>
  <td>555 77 855</td>
</tr>
</table>

- 表格内的标签

	- <table border="1">
<tr>
  <td>
   <p>这是一个段落</p>
   <p>这是另一个段落</p>
  </td>
  <td>这个单元格包含一个表格:
   <table border="1">
   <tr>
     <td>A</td>
     <td>B</td>
   </tr>
   <tr>
     <td>C</td>
     <td>D</td>
   </tr>
   </table>
  </td>
</tr>
<tr>
  <td>这个单元格包含一个列表
   <ul>
    <li>apples</li>
    <li>bananas</li>
    <li>pineapples</li>
   </ul>
  </td>
  <td>HELLO</td>
</tr>
</table>

- 单元格边距(Cell padding)

	- <table border="1" 
cellpadding="10">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>   
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

- 单元格间距(Cell spacing)

	- <table border="1" cellspacing="0">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table> //细边框

### 列表

- 有序列表

	- <ol>
<li>Coffee</li>
<li>Milk</li>
</ol>

- 无序列表

	- <ul>
<li>Coffee</li>
<li>Milk</li>
</ul>

- 嵌套列表

	- <ul>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea</li>
    </ul>
  </li>
  <li>Milk</li>
</ul>

		- <ul>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea
        <ul>
          <li>China</li>
          <li>Africa</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Milk</li>
</ul>

- 自定义列表

	- <dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>

		- Coffee
- black hot drink
Milk
- white cold drink

- 不同类型的有序列表

	- <ol type="A">

		- 大写字母列表

	- <ol type="a">

		- 小写字母列表

	- <ol type="I">

		- 罗马数字列表

	- <ol type="i">

		- 小写罗马数字列表

- 不同类型的无序列表

	- style="list-style-type:disc"

		- 圆点列表

	- style="list-style-type:circle"

		- 圆圈列表

	- style="list-style-type:square"

		- 正方形列表

### 区块

- 区块元素block-level

	- 块级元素在浏览器显示时，通常会以新行来开始（和结束）。
	- <h1>, <p>, <ul>, <table>

- 内联元素inline

	- 内联元素在显示时通常不会以新行开始。
	- <b>, <td>, <a>, <img>

- <div> 元素

	- 块级元素，它可用于组合其他 HTML 元素的容器。
	- 与 CSS 一同使用，<div> 元素可用于对大的内容块设置样式属性。

-  <span> 元素

	- 内联元素，可用作文本的容器
	- 与 CSS 一同使用时，<span> 元素可用于为部分文本设置样式属性。
	- <p>我的母亲有 <span style="color:blue;font-weight:bold">蓝色</span> 的眼睛，我的父亲有 <span style="color:darkolivegreen;font-weight:bold">碧绿色</span> 的眼睛。</p>

### 布局

### 表单

- 作用

	- 用于收集不同类型的用户输入。

-  <form> </form>

	- 多数情况下被用到的表单标签是输入标签（<input>）。输入类型是由类型属性（type）定义的。

- 文本域（Text Fields）

	- <form>
First name: <input type="text" name="firstname" value="your name"><br>
Last name: <input type="text" name="lastname">
<input type="reset" value="重置">
</form>

- 密码字段 Password

	- <form>
Password: <input type="password" name="pwd">
</form>

- 单选按钮（Radio Buttons）

	- <form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>

- 复选框（Checkboxes）

	- <form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car" checked="checked">I have a car 
</form>
	- checked 默认选择

- 提交按钮(Submit Button)

	- <form name="input" action="html_form_action.php" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
	- <form id="form" name="form1" action="http://www.baidu.com">
    <!-- 存放一个input放在这，为了获取焦点，然后我们可以按enter键提交 -->
    <input type="text">
    <button type="submit">submit</button>
</form>

- 下拉列表

	- 简单下拉列表

		- <form action="">
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat">Fiat</option>
<option value="audi">Audi</option>
</select>
</form>

	- 预选下拉列表

		- <form action="">
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat" selected>Fiat</option>
<option value="audi">Audi</option>
</select>
</form>

- 带边框的表单

	- <form action="">
<fieldset>
<legend>Personal information:</legend>
Name: <input type="text" size="30"><br> // size是输入框的长度
E-mail: <input type="text" size="30"><br>
Date of birth: <input type="text" size="10">
</fieldset>
</form>

- 从表单发送电子邮件

	- <form action="MAILTO:someone@example.com" method="post" enctype="text/plain">
Name:<br>
<input type="text" name="name" value="your name"><br>
E-mail:<br>
<input type="text" name="mail" value="your email"><br>
Comment:<br>
<input type="text" name="comment" value="your comment" size="50"><br><br>
<input type="submit" value="发送">
<input type="reset" value="重置">
</form>

- <label>

	- <label> 标签为 input 元素定义标注（标记）。

label 元素不会向用户呈现任何特殊效果。不过，它为鼠标用户改进了可用性。如果您在 label 元素内点击文本，就会触发此控件。就是说，当用户选择该标签时，浏览器就会自动将焦点转到和标签相关的表单控件上。

<label> 标签的 for 属性应当与相关元素的 id 属性相同
	- 和单选按钮对比，效果体现在能在元素周围点击也可以进行选择，但是单选按钮简单模式只能点击选择框才可以进行选择
	- 提示:"for" 属性可把 label 绑定到另外一个元素。请把 "for" 属性的值设置为相关元素的 id 属性的值。
	- <form action="demo_form.phpp">
  <label for="male">Male</label>
  <input type="radio" name="sex" id="male" value="male"><br>
  <label for="female">Female</label>
  <input type="radio" name="sex" id="female" value="female"><br><br>
  <input type="submit" value="提交">
</form>
	- for	属性

		- 值：for_id

			- 规定 label 与哪个表单元素绑定。

	- form 属性

		- 值：form_id

			- 规定 label 字段所属的一个或多个表单。

		- <p>第一个单选按钮在表单之外,但它仍属于该表单的一部分。尝试点击文本标签切换单选按钮。</p>

<form action="demo_form.php" id="form1">
  <input type="radio" name="sex" id="male" value="male"><br>
  <label for="female">Female</label>
  <input type="radio" name="sex" id="female" value="female"><br><br>
  <input type="submit" value="提交">
</form>

<label for="male" form="form1">Male</label>

- <fieldset>

	- 可以将表单内的相关元素分组。
	- 会在相关表单元素周围绘制边框。
	- <form>
<fieldset>
<legend>Personalia:</legend>
Name: <input type="text"><br>
Email: <input type="text"><br>
Date of birth: <input type="text">
</fieldset>
</form>

		- <form>
  <fieldset disabled>
    <legend>Personalia:</legend>
    Name: <input type="text"><br>
    Email: <input type="text"><br>
    Date of birth: <input type="text">
  </fieldset>
</form>

			- <form action="demo-form.php" method="get" id="form1">
What is your favorite color? <input type="text" name="fav_color"><br>
<input type="submit">
</form>

<p>下面的自定义字段在表单外,但仍是表单的一部分。</p>

<fieldset form="form1">
  <legend>Personalia:</legend>
  Name: <input type="text" name="username"><br>
  Email: <input type="text" name="usermail"><br>
</fieldset>

<p><b>注意：</b>目前，只有 Opera 支持 form 属性。</p>

				- <form action="demo-form.php" method="get">
<fieldset name="personalia">
  Name: <input type="text" name="username"><br>
  Email: <input type="text" name="usermail"><br>
</fieldset>
<button type="button" onclick="form.personalia.style.backgroundColor='yellow'">改变控件的背景颜色</button>
<input type="submit">
</form>

- <legend>	

	- 定义了 <fieldset> 元素的标题
	- <form>
  <fieldset>
    <legend>Personalia:</legend>
    Name: <input type="text" size="30"><br>
    Email: <input type="text" size="30"><br>
    Date of birth: <input type="text" size="10">
  </fieldset>
</form>

- <optgroup>

	- 把相关的选项组合在一起
	- <select>
  <optgroup label="Swedish Cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
  </optgroup>
  <optgroup label="German Cars">
    <option value="mercedes">Mercedes</option>
    <option value="audi">Audi</option>
  </optgroup>
</select>
	- disabled属性

		- <select>
  <optgroup label="Swedish Cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
  </optgroup>
  <optgroup label="German Cars" disabled>
    <option value="mercedes">Mercedes</option>
    <option value="audi">Audi</option>
  </optgroup>
</select>
		- 规定选项组应该被禁用。

被禁用的选项组既不可用，也不可点击。

可以设置 disabled 属性，直到满足某些条件（比如选择一个复选框），才恢复用户对该选项组的使用。然后，可以使用 JavaScript 来移除 disabled 属性的值，以使选项组变为可用状态。

	- label 属性

		- 为选项组规定描述标签

- <button>

	- 定义一个点击按钮
	- <button type="button">点我!</button>
	- 提示：请始终为 <button> 元素规定 type 属性。不同的浏览器对 <button> 元素的 type 属性使用不同的默认值。
	- 如果在 HTML 表单中使用 <button> 元素，不同的浏览器可能会提交不同的按钮值。请使用 <input> 在 HTML 表单中创建按钮。
	- autofocus

		- 规定当页面加载时按钮应当自动地获得焦点
		- <button type="button" autofocus>点我！</button>

	- disabled

		- 禁用该按钮
		- <button disabled>
		- <button type="button" disabled>点我！</button>

	- form

		- <button form="form_id">
		- 规定按钮属于一个或多个表单
		- <form action="demo-form.php" method="get" id="nameform">
First name: <input type="text" name="fname" /><br>
Last name: <input type="text" name="lname" /><br>
</form>

<p>下面的按钮是在表单元素外,但仍是表单的一部分。</p>

<button type="submit" form="nameform" value="提交">提交</button>


	- formaction

		- <button type="submit" formaction="URL">
		- URL
		- 规定当提交表单时向何处发送表单数据。覆盖 form 元素的 action 属性。该属性与 type="submit" 配合使用。
		- <form action="demo_form.html" method="get">
First name: <input type="text" name="fname"><br>
Last name: <input type="text" name="lname"><br>
<button type="submit">提交</button><br>
<button type="submit" formaction="demo_admin.html">提交</button>
</form>
		- 可能值

			- 绝对 URL - 完整的页面URL地址(如：href="http://www.example.com/formresult.html")
			- 相对 URL 地址 -指向当前网站的一个文件(如：href="formresult.html")

	- formenctype

		- 规定在向服务器发送表单数据之前如何对其进行编码。覆盖 form 元素的 enctype 属性。该属性与 type="submit" 配合使用。
		- <form action="demo_post_enctype.asp" method="post">
Name: <input type="text" name="fname" value="Ståle Refsnes"><br>
<button type="submit" >使用编码提交</button>
<button type="submit" formenctype="text/plain">不使用编码提交</button>
</form>

	- formmethod

		- get

			- 表单数据在URL中以 name/value 对出现。
			- get传送的数据量较小，不能大于2KB，这主要是因为受URL长度限制。
			- 不要使用 "get" 方法传送敏感信息！(密码或者敏感信息会出现在浏览器的地址栏中)

		- post

			- 以 HTTP post 形式发送表单数据。
			- 比 "get" 方法更强大更安全。
			- 没有大小限制

		- <form action="demo-form.php" method="get">
First name: <input type="text" name="fname" /><br>
Last name: <input type="text" name="lname" /><br>
<button type="submit" >提交</button>
<button type="submit" formmethod="post" formaction="demo-post.php">使用 POST 提交</button>
</form>
		- 规定用于发送表单数据的 HTTP 方法。覆盖 form 元素的 method 属性。该属性与 type="submit" 配合使用。

	- formnovalidate

		- 如果使用该属性，则提交表单时不进行验证。覆盖 form 元素的 novalidate 属性。该属性与 type="submit" 配合使用。
		- <button type="submit" formnovalidate>
		- <form action="demo_form.html" method="get">
E-mail: <input type="email" name="userid"><br>
<button type="submit">提交</button><br>
<button type="submit" formnovalidate>不验证提交</button>
</form>

	- formtarget

		- _blank

			- 在新窗口/选项卡中将表单提交到文档。

		- _self

			- 在同一框架中将表单提交到文档。（默认）

		- _parent

			- 在父框架中将表单提交到文档。

		- _top

			- 在整个窗口中将表单提交到文档。

		- framename

			- 在指定的框架中将表单提交到文档。

		- <button type="submit" formtarget="_blank|_self|_parent|_top|framename">

		- 规定在何处打开 action URL。覆盖 form 元素的 target 属性。该属性与 type="submit" 配合使用。
		- <form action="demo-form.php" method="get">
  First name: <input type="text" name="fname" /><br>
  Last name: <input type="text" name="lname" /><br>
<button type="submit" >提交</button>
<button type="submit" formtarget="_blank">提交到一个新窗口或选项卡</button>
</form>

	- name
	- type

		- <button type="button|submit|reset">
		- <button type="button" onclick="alert('你好，世界!')">点我!</button>
		- button

			- 该按钮是重置按钮（清除表单数据）。

		- reset

			- 该按钮是重置按钮（清除表单数据）。

		- submit 

			- 该按钮是提交按钮（除了 Internet Explorer，该值是其他浏览器的默认值）。

	- value

- <datalist>

	- 指定一个预先定义的输入控件选项列表
	- <input list="browsers">
<datalist id="browsers">
<option value="Internet Explorer">
<option value="Firefox">
<option value="Chrome">
<option value="Opera">
<option value="Safari">
</datalist>

- <keygen>

	- 定义了表单的密钥对生成器字段

- <output>

	- 定义一个计算结果

### 框架

- 作用

	- 通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。
	- 提示：使用 CSS 为 <iframe> （包括滚动条）定义样式。

- iframe语法

	- <iframe src="URL"></iframe>
	- height
	- width
	- name	
	- sandbox
	- seamless
	- srcdoc
	- frameborder

		- 1
		- 0

	- longdesc
	- marginheight
	- marginwidth
	- scrolling

		- yes
		- no
		- auto

	- align

		- left
		- right
		- top
		- middle
		- bottom

- <iframe src="demo_iframe.htm" width="200" height="200" frameborder="0">
 <p>您的浏览器不支持  iframe 标签。</p>
</iframe>
- <iframe src="demo_iframe.htm" name="iframe_a"></iframe>
<p><a href="http://www.runoob.com" target="iframe_a">RUNOOB.COM</a></p>

<p><b>注意：</b> 因为 a 标签的 target 属性是名为 iframe_a 的 iframe 框架，所以在点击链接时页面会显示在 iframe框架中。</p>

- <iframe src="http://www.runoob.com">
  <p>您的浏览器不支持  iframe 标签。</p>
</iframe>

### 颜色

- 颜色值

	- 颜色(Color)

		- black

	- 颜色十六进制(Color HEX)

		- #000000

	- 颜色RGB(Color RGB)

		- rgb(0,0,0)

	- http://www.runoob.com/html/html-colors.html

- 颜色名

	- http://www.runoob.com/html/html-colornames.html

### 字符实体

- 不间断空格(Non-breaking Space)
- 使用实体名而不是数字的好处是，名称易于记忆。不过坏处是，浏览器也许并不支持所有实体名称（对实体数字的支持却很好）。
- HTML 实体参考手册

	- http://www.runoob.com/tags/ref-entities.html

- HTML 符号实体参考手册

	- http://www.runoob.com/tags/html-symbols.html

- HTML URL 编码 参考手册

	- http://www.runoob.com/tags/html-urlencode.html

- HTML 语言代码 参考手册

	- http://www.runoob.com/tags/html-language-codes.html

### HTMLX简介

- XML 是一种必须正确标记且格式良好的标记语言。
- http://www.runoob.com/xml/xml-attributes.html

	- 教程

### 媒体(Media)

- 最新的 HTML5 标准只支持 MP4, WebM, 和 Ogg 视频格式。
- HTML5 的最新标准支持 MP3, WAV, 和 Ogg 音频格式。

### 插件

- 插件的功能是扩展 HTML 浏览器的功能。
- <object> 

	- <object width="400" height="50" data="bookmark.swf"></object>
	- 该标签用于插入对象 (例如在网页中嵌入 Java 小程序, PDF 阅读器, Flash 播放器) 。图片/文件

- <embed> 

	- <embed width="400" height="50" src="bookmark.swf">

### 音频(Audio)

- <audio controls height="100" width="100">
  <source src="horse.mp3" type="audio/mpeg">
  <source src="horse.ogg" type="audio/ogg">
  <embed height="50" width="100" src="horse.mp3">
</audio> //最好的 HTML 解决方法
- 例子使用了两个不同的音频格式。HTML5 <audio> 元素会尝试以 mp3 或 ogg 来播放音频。如果失败，代码将回退尝试 <embed> 元素。
- <track> 标签

	- <video width="320" height="240" controls>
<source src="forrest_gump.mp4" type="video/mp4">
<source src="forrest_gump.ogg" type="video/ogg">
<track src="subtitles_en.vtt" kind="subtitles" srclang="en"
label="English">
<track src="subtitles_no.vtt" kind="subtitles" srclang="no"
label="Norwegian">
</video>
	- 为媒体元素（比如 <audio> and <video>）规定外部文本轨道。
	- default

		- 规定该轨道是默认的。如果用户没有选择任何轨道，则使用默认轨道。
		- <track src="subtitles_en.vtt" default>

	- kind

		- captions

			- 该轨道定义将在播放器中显示的简短说明。

		- chapters

			- 该轨道定义章节，用于导航媒介资源。

		- descriptions

			- 该轨道定义描述，用于通过音频描述媒介的内容，假如内容不可播放或不可见。

		- metadata

			- 该轨道定义脚本使用的内容。

		- subtitles	

			- 该轨道定义字幕，用于在视频中显示字幕。

		- 规定文本轨道的文本类型。
		- <track src="subtitles_en.vtt" kind="subtitles" srclang="en">

	- label

		- 规定文本轨道的标签和标题。

	- src

		- 必需的。规定轨道文件的 URL。

	- srclang

		- 规定轨道文本数据的语言。如果 kind 属性值是 "subtitles"，则该属性是必需的。

- <object> 
- <embed> 

### 视频（Videos）

- <video width="320" height="240" controls>
<source src="movie.mp4" type="video/mp4">
<source src="movie.ogg" type="video/ogg">
<source src="movie.webm" type="video/webm">
<object data="movie.mp4" width="320" height="240">
<embed src="movie.swf" width="320" height="240">
</object>
</video>
- 最好的 HTML 解决方法

	- <video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.webm" type="video/webm">
  <object data="movie.mp4" width="320" height="240">
    <embed src="movie.swf" width="320" height="240">
  </object> 
</video>
	- 以下实例中使用了 4 中不同的视频格式。HTML 5 <video> 元素会尝试播放以 mp4、ogg 或 webm 格式中的一种来播放视频。如果均失败，则回退到 <embed> 元素。

- <object> 
- <embed> 

## HTML5

### 基础内容

- <!doctype> 声明

	- <!doctype> 声明必须位于 HTML5 文档中的第一行,使用非常简单

- 对于中文网页需要使用 <meta charset="utf-8"> 声明编码，否则会出现乱码。
- HTML5 的改进

	- 新元素
	- 新属性
	- 完全支持 CSS3
	- Video 和 Audio
	- 2D/3D 制图
	- 本地存储
	- 本地 SQL 数据
	- Web 应用

- HTML5 应用

	- 本地数据存储
	- 访问本地文件
	- 本地 SQL 数据
	- 缓存引用
	- Javascript 工作者
	- XHTMLHttpRequest 2

- HTML5 图形

	- 使用 <canvas> 元素。
	- 使用内联 SVG。
	- 使用 CSS3 2D 转换、CSS3 3D 转换。

- HTML5 使用 CSS3

	- 新选择器
	- 新属性
	- 动画
	- 2D/3D 转换
	- 圆角
	- 阴影效果
	- 可下载的字体

- 语义元素

	- <article>	定义页面独立的内容区域。
	- <aside>	定义页面的侧边栏内容。
	- <bdi>	允许您设置一段文本，使其脱离其父元素的文本方向设置。
	- <command>	定义命令按钮，比如单选按钮、复选框或按钮
	- <details>	用于描述文档或文档某个部分的细节
	- <dialog>	定义对话框，比如提示框
	- <summary>	标签包含 details 元素的标题
	- <figure>	规定独立的流内容（图像、图表、照片、代码等等）。
	- <figcaption>	定义 <figure> 元素的标题
	- <footer>	定义 section 或 document 的页脚。
	- <header>	定义了文档的头部区域
	- <mark>	定义带有记号的文本。
	- <meter>	定义度量衡。仅用于已知最大和最小值的度量。
	- <nav>	定义导航链接的部分。
	- <progress>	定义任何类型的任务的进度。
	- <ruby>	定义 ruby 注释（中文注音或字符）。
	- <rt>	定义字符（中文注音或字符）的解释或发音。
	- <rp>	在 ruby 注释中使用，定义不支持 ruby 元素的浏览器所显示的内容。
	- <section>	定义文档中的节（section、区段）。
	- <time>	定义日期或时间。
	- <wbr>	规定在文本中的何处适合添加换行符。

- HTML5 表单

	- 新表单元素, 新属性，新输入类型，自动验证。

### 浏览器支持

- 为 HTML 添加新元素

	- <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"> 
<title>为 HTML 添加新元素</title>
<script>
document.createElement("myHero")
</script>
<style>
myHero {
    display: block;
    background-color: #ddd;
    padding: 50px;
    font-size: 30px;
}
</style> 
</head>
 
<body>
 
<h1>我的第一个标题</h1>
 
<p>我的第一个段落。</p>
 
<myHero>我的第一个新元素</myHero>
 
</body>
</html>
	- JavaScript 语句 document.createElement("myHero") 是为 IE 浏览器添加新的元素。

### 新元素(未仔细看完和语义元素重合

- 新图像元素

	- <canvas> 标签定义图形，比如图表和其他图像。该标签基于 JavaScript 的绘图 API

- 新多媒体元素

	- <audio>	定义音频内容
	- <video>	定义视频（video 或者 movie）
	- <source>	定义多媒体资源 <video> 和 <audio>
	- <embed>	定义嵌入的内容，比如插件。
	- <track>	为诸如 <video> 和 <audio> 元素之类的媒介规定外部文本轨道。

- 新表单元素

	- <datalist>	定义选项列表。请与 input 元素配合使用该元素，来定义 input 可能的值。
	- <keygen>	规定用于表单的密钥对生成器字段。
	- <output>	定义不同类型的输出，比如脚本的输出。

- 新的语义和结构元素

	- <article>	定义页面独立的内容区域。
	- <aside>	定义页面的侧边栏内容。
	- <bdi>	允许您设置一段文本，使其脱离其父元素的文本方向设置。
	- <command>	定义命令按钮，比如单选按钮、复选框或按钮
	- <details>	用于描述文档或文档某个部分的细节
	- <dialog>	定义对话框，比如提示框
	- <summary>	标签包含 details 元素的标题
	- <figure>	规定独立的流内容（图像、图表、照片、代码等等）。
	- <figcaption>	定义 <figure> 元素的标题
	- <footer>	定义 section 或 document 的页脚。
	- <header>	定义了文档的头部区域
	- <mark>	定义带有记号的文本。
	- <meter>	定义度量衡。仅用于已知最大和最小值的度量。
	- <nav>	定义导航链接的部分。
	- <progress>	定义任何类型的任务的进度。
	- <ruby>	定义 ruby 注释（中文注音或字符）。
	- <rt>	定义字符（中文注音或字符）的解释或发音。
	- <rp>	在 ruby 注释中使用，定义不支持 ruby 元素的浏览器所显示的内容。
	- <section>	定义文档中的节（section、区段）。
	- <time>	定义日期或时间。
	- <wbr>	规定在文本中的何处适合添加换行符。

- 已移除的元素

	- <acronym>
	- <applet>
	- <basefont>
	- <big>
	- <center>
	- <dir>
	- <font>
	- <frame>
	- <frameset>
	- <noframes>
	- <strike>
	- <tt>

### Canvas

- 作用

	- 用于图形的绘制，通过脚本 (通常是JavaScript)来完成.
	- <canvas> 标签只是图形容器，您必须使用脚本来绘制图形。
	- 可以通过多种方法使用 canvas 绘制路径,盒、圆、字符以及添加图像。

- <script>

var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.fillStyle="#FF0000";
ctx.fillRect(0,0,150,75);

</script>
- 更多教程

	- http://www.runoob.com/html/html5-canvas.html
	- 其他知识点，来不及看了，需要用时再研究

### 内联 SVG

- 作用

	- SVG 指可伸缩矢量图形 (Scalable Vector Graphics)
	- SVG 用于定义用于网络的基于矢量的图形
	- SVG 使用 XML 格式定义图形
	- SVG 图像在放大或改变尺寸的情况下其图形质量不会有损失
	- SVG 是万维网联盟的标准

- SVG优势

	- SVG 图像可通过文本编辑器来创建和修改
	- SVG 图像可被搜索、索引、脚本化或压缩
	- SVG 是可伸缩的
	- SVG 图像可在任何的分辨率下被高质量地打印
	- SVG 可在图像质量不下降的情况下被放大

- 把 SVG 直接嵌入 HTML 页面

	- <!DOCTYPE html>
<html>
<body>
 
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="190">
  <polygon points="100,10 40,180 190,60 10,60 160,180"
  style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;">
</svg>
 
</body>
</html>

- 更多教程

	- http://www.runoob.com/svg/svg-tutorial.html

### SVG 与 Canvas

- 区别

	- SVG 是一种使用 XML 描述 2D 图形的语言。
	- Canvas 通过 JavaScript 来绘制 2D 图形。
	- SVG 基于 XML，这意味着 SVG DOM 中的每个元素都是可用的。您可以为某个元素附加 JavaScript 事件处理器。
	- 在 SVG 中，每个被绘制的图形均被视为对象。如果 SVG 对象的属性发生变化，那么浏览器能够自动重现图形。
	- Canvas 是逐像素进行渲染的。在 canvas 中，一旦图形被绘制完成，它就不会继续得到浏览器的关注。如果其位置发生变化，那么整个场景也需要重新绘制，包括任何或许已被图形覆盖的对象。

- 比较

	- Canvas

		- 依赖分辨率
		- 不支持事件处理器
		- 弱的文本渲染能力
		- 能够以 .png 或 .jpg 格式保存结果图像
		- 最适合图像密集型的游戏，其中的许多对象会被频繁重绘

	- SVG

		- 不依赖分辨率
		- 支持事件处理器
		- 最适合带有大型渲染区域的应用程序（比如谷歌地图）
		- 复杂度高会减慢渲染速度（任何过度使用 DOM 的应用都不快）
		- 不适合游戏应用

### MathML

- 数学标记语言，是一种基于XML（标准通用标记语言的子集）的标准，用来在互联网上书写数学符号和公式的置标语言。
- http://www.runoob.com/html/html5-mathml.html

### 拖放

- 作用

	- 拖放是一种常见的特性，即抓取对象以后拖到另一个位置。
	- 在 HTML5 中，拖放是标准的一部分，任何元素都能够拖放。

- http://www.runoob.com/html/html5-draganddrop.html

### 地理定位

- 作用

	- HTML5 Geolocation API 用于获得用户的地理位置。
	- 鉴于该特性可能侵犯用户的隐私，除非用户同意，否则用户位置信息是不可用的。

- http://www.runoob.com/html/html5-geolocation.html

### Video(视频)

- <video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
您的浏览器不支持Video标签。
</video>
- HTML5 <video> - 使用 DOM 进行控制
- HTML 音频/视频 DOM 参考手册

	- http://www.runoob.com/tags/ref-av-dom.html

- 这些方法、属性和事件允许您使用 JavaScript 来操作 <audio> 和 <video> 元素。

### Audio(音频)

- <audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
您的浏览器不支持 audio 元素。
</audio>
- HTML5 <audio> - 使用 DOM 进行控制
- HTML 音频/视频 DOM 参考手册

	- http://www.runoob.com/tags/ref-av-dom.html

- 这些方法、属性和事件允许您使用 JavaScript 来操作 <audio> 和 <video> 元素。

### Input 类型(HTML5 新的 Input 类型

- color

	- <form action="demo-form.php">
  选择你喜欢的颜色: <input type="color" name="favcolor"><br>
  <input type="submit">
</form>

- date

	- <form action="demo-form.php">
  生日: <input type="date" name="bday">
  <input type="submit">
</form>

- datetime

	- <form action="demo-form.php">
  生日 (日期和时间): <input type="datetime" name="bdaytime">
  <input type="submit">
</form>

- datetime-local

	- <form action="demo-form.php">
  生日 (日期和时间): <input type="datetime-local" name="bdaytime">
  <input type="submit">
</form>

- email

	- <form action="demo-form.php">
  E-mail: <input type="email" name="usremail">
  <input type="submit">
</form>
	- 在提交表单时，会自动验证 email 域的值是否合法有效:

- month

	- <form action="demo-form.php">
  生日 ( 月和年 ): <input type="month" name="bdaymonth">
  <input type="submit">
</form>

- number

	- <form action="demo-form.php">
  数量 ( 1 到 5 之间): <input type="number" name="quantity" min="1" max="5">
  <input type="submit">
</form>
	- 下面的属性来规定对数字类型的限定

		- disabled	规定输入字段是禁用的
		- max	规定允许的最大值
		- maxlength	规定输入字段的最大字符长度
		- min	规定允许的最小值
		- pattern	规定用于验证输入字段的模式
		- readonly	规定输入字段的值无法修改
		- required	规定输入字段的值是必需的

			- <input type="text" placeholder="cat photo URL" required>
			- You can require specific form fields so that your user will not be able to submit your form until he or she has filled them out.

		- size	规定输入字段中的可见字符数
		- step	规定输入字段的合法数字间隔
		- value	规定输入字段的默认值

- range

	- <form action="demo-form.php" method="get">
Points: <input type="range" name="points" min="1" max="10">
<input type="submit">
</form>
	- 用于应该包含一定范围内数字值的输入域。
	- max - 规定允许的最大值
	- min - 规定允许的最小值
	- step - 规定合法的数字间隔
	- value - 规定默认值

- search

	- <form action="demo-form.php">
  Search Google: <input type="search" name="googlesearch"><br>
  <input type="submit">
</form>

- tel

	- <form action="demo-form.php">
  电话号码: <input type="tel" name="usrtel"><br>
  <input type="submit">
</form>

- time

	- <form action="demo-form.php">
  选择时间: <input type="time" name="usr_time">
  <input type="submit">
</form>

- url

	- <form action="demo-form.php">
  添加你的主页: <input type="url" name="homepage"><br>
  <input type="submit">
</form>

- week

	- <form action="demo-form.php">
  选择周: <input type="week" name="year_week">
  <input type="submit">
</form>

### 表单元素

- <datalist>

	- <datalist> 元素规定输入域的选项列表。
	- <form action="demo-form.php" method="get">
<input list="browsers" name="browser">
<datalist id="browsers">
  <option value="Internet Explorer">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
</datalist>
<input type="submit">
</form>

- <keygen>

	- <keygen> 元素的作用是提供一种验证用户的可靠方法。
	- 当提交表单时，会生成两个键，一个是私钥，一个公钥。

私钥（private key）存储于客户端，公钥（public key）则被发送到服务器。公钥可用于之后验证用户的客户端证书（client certificate）。
	- <form action="demo_keygen.php" method="get">
  用户名: <input type="text" name="usr_name">
  加密: <keygen name="security">
  <input type="submit">
</form>

- <output>

	- <output> 元素用于不同类型的输出，比如计算或脚本输出：
	- <form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
<input type="range" id="a" value="50">100
+<input type="number" id="b" value="50">
=<output name="x" for="a b"></output>
</form>

### 表单属性

- <form>新属性

	- autocomplete

		- autocomplete 属性规定 form 或 input 域应该拥有自动完成功能。
		- 提示: autocomplete 属性有可能在 form元素中是开启的，而在input元素中是关闭的。
		- 注意: autocomplete 适用于 <form> 标签，以及以下类型的 <input> 标签：text, search, url, telephone, email, password, datepickers, range 以及 color。
		- <form action="demo-form.php" autocomplete="on">
  First name:<input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  E-mail: <input type="email" name="email" autocomplete="off"><br>
  <input type="submit">
</form>

	- novalidate

		- novalidate 属性规定在提交表单时不应该验证 form 或 input 域。
		- <form action="demo-form.php" novalidate>
  E-mail: <input type="email" name="user_email">
  <input type="submit">
</form>

- <input>新属性

	- autocomplete

		- autocomplete 属性规定 form 或 input 域应该拥有自动完成功能。
		- 提示: autocomplete 属性有可能在 form元素中是开启的，而在input元素中是关闭的。
		- 注意: autocomplete 适用于 <form> 标签，以及以下类型的 <input> 标签：text, search, url, telephone, email, password, datepickers, range 以及 color。
		- <form action="demo-form.php" autocomplete="on">
  First name:<input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  E-mail: <input type="email" name="email" autocomplete="off"><br>
  <input type="submit">
</form>

	- autofocus

		- autofocus 属性规定在页面加载时，域自动地获得焦点。
		-  boolean 属性
		- <form action="demo-form.php">
  First name: <input type="text" name="fname" autofocus><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit">
</form>

	- form

		- form 属性规定输入域所属的一个或多个表单。
提示:如需引用一个以上的表单，请使用空格分隔的列表。
		- <form action="demo-form.php" id="form1">
First name: <input type="text" name="fname"><br>
<input type="submit" value="提交">
</form>

<p> "Last name" 字段没有在 form 表单之内，但它也是 form 表单的一部分。</p>

Last name: <input type="text" name="lname" form="form1">

	- formaction

		- The formaction 属性用于描述表单提交的URL地址.
		- The formaction 属性会覆盖<form> 元素中的action属性.
		- 注意: The formaction 属性用于 type="submit" 和 type="image".
		- <form action="demo-form.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交"><br>
  <input type="submit" formaction="demo-admin.php" value="提交">
</form>

	- formenctype

		- formenctype 属性描述了表单提交到服务器的数据编码 (只对form表单中 method="post" 表单)
		- formenctype 属性覆盖 form 元素的 enctype 属性。
		- 主要: 该属性与 type="submit" 和 type="image" 配合使用。
		- <form action="demo-post_enctype.php" method="post">
  First name: <input type="text" name="fname"><br>
  <input type="submit" value="提交">
  <input type="submit" formenctype="multipart/form-data"
  value="以 Multipart/form-data 提交">
</form>

	- formmethod

		- formmethod 属性定义了表单提交的方式。
		- formmethod 属性覆盖了 <form> 元素的 method 属性。
		- 注意: 该属性可以与 type="submit" 和 type="image" 配合使用。
		- <form action="demo-form.php" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交">
  <input type="submit" formmethod="post" formaction="demo-post.php"
  value="使用 POST 提交">
</form>

	- formnovalidate

		-  boolean 属性.
		- novalidate属性描述了 <input> 元素在表单提交时无需被验证。
		- formnovalidate 属性会覆盖 <form> 元素的novalidate属性.
		- 注意: formnovalidate 属性与type="submit一起使用
		- <form action="demo-form.php">
  E-mail: <input type="email" name="userid"><br>
  <input type="submit" value="提交"><br>
  <input type="submit" formnovalidate value="不验证提交">
</form>

	- formtarget

		- formtarget 属性指定一个名称或一个关键字来指明表单提交数据接收后的展示。
		- The formtarget 属性覆盖 <form>元素的target属性.
		- 注意: formtarget 属性与type="submit" 和 type="image"配合使用.
		- <form action="demo-form.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="正常提交">
  <input type="submit" formtarget="_blank"
  value="提交到一个新的页面上">
</form>

	- height 与 width

		- height 和 width 属性规定用于 image 类型的 <input> 标签的图像高度和宽度。
		- 注意: height 和 width 属性只适用于 image 类型的<input> 标签。
		- 提示:图像通常会同时指定高度和宽度属性。如果图像设置高度和宽度，图像所需的空间 在加载页时会被保留。如果没有这些属性， 浏览器不知道图像的大小，并不能预留 适当的空间。图片在加载过程中会使页面布局效果改变 （尽管图片已加载）。
		- <input type="image" src="img_submit.gif" alt="Submit" width="48" height="48">

	- list

		- list 属性规定输入域的 datalist。datalist 是输入域的选项列表。
		- <input list="browsers">

<datalist id="browsers">
  <option value="Internet Explorer">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
</datalist>

	- min 与 max

		- min、max 和 step 属性用于为包含数字或日期的 input 类型规定限定（约束）。
		- 注意: min、max 和 step 属性适用于以下类型的 <input> 标签：date pickers、number 以及 range。
		- Enter a date before 1980-01-01:
<input type="date" name="bday" max="1979-12-31">

Enter a date after 2000-01-01:
<input type="date" name="bday" min="2000-01-02">

Quantity (between 1 and 5):
<input type="number" name="quantity" min="1" max="5">

	- multiple

		-  boolean 属性.
		- multiple 属性规定<input> 元素中可选择多个值。
		- 注意: multiple 属性适用于以下类型的 <input> 标签：email 和 file:
		- Select images: <input type="file" name="img" multiple>

	- pattern (regexp)

		- pattern 属性描述了一个正则表达式用于验证 <input> 元素的值。

注意:pattern 属性适用于以下类型的 <input> 标签: text, search, url, tel, email, 和 password.

提示： 是用来全局 title 属性描述了模式.
		- Country code: <input type="text" name="country_code" pattern="[A-Za-z]{3}" title="Three letter country code">//下面的例子显示了一个只能包含三个字母的文本域（不含数字及特殊字符）

	- placeholder

		- placeholder 属性提供一种提示（hint），描述输入域所期待的值。
		- 简短的提示在用户输入值前会显示在输入域上。
		- 注意: placeholder 属性适用于以下类型的 <input> 标签：text, search, url, telephone, email 以及 password。
		- <form action="demo-form.php">
  <input type="text" name="fname" placeholder="First name"><br>
  <input type="text" name="lname" placeholder="Last name"><br>
  <input type="submit" value="提交">
</form>

	- required

		- required 属性是一个 boolean 属性.
		- required 属性规定必须在提交之前填写输入域（不能为空）。
		- 注意:required 属性适用于以下类型的 <input> 标签：text, search, url, telephone, email, password, date pickers, number, checkbox, radio 以及 file。
		- <form action="demo-form.php">
  Username: <input type="text" name="usrname" required>
  <input type="submit">
</form>

	- step

		- step 属性为输入域规定合法的数字间隔。
		- 如果 step="3"，则合法的数是 -3,0,3,6 等
		- 提示： step 属性可以与 max 和 min 属性创建一个区域值.
		- 注意: step 属性与以下type类型一起使用: number, range, date, datetime, datetime-local, month, time 和 week.
		- <form action="demo-form.php">
  <input type="number" name="points" step="3">
  <input type="submit">
</form>

### 语义元素

- 含义

	- 语义= 意义，语义元素 = 有意义的元素

- 无语义 元素实例

	-  <div> 和 <span> - 无需考虑内容

- 语义元素实例

	- <form>, <table>, and <img> - 清楚的定义了它的内容

- HTML5中新的语义元素

	- <header>

		- <header>元素描述了文档的头部区域
		- <article>
  <header>
    <h1>Internet Explorer 9</h1>
    <p><time pubdate datetime="2011-03-15"></time></p>
  </header>
  <p>Windows Internet Explorer 9(缩写为 IE9 )是在2011年3月14日21:00发布的</p>
</article>

	- <nav>

		- <nav> 标签定义导航链接的部分。
		- <nav> 元素用于定义页面的导航链接部分区域，但是，不是所有的链接都需要包含在 <nav> 元素中!
		- <nav>
<a href="/html/">HTML</a> |
<a href="/css/">CSS</a> |
<a href="/js/">JavaScript</a> |
<a href="/jquery/">jQuery</a>
</nav>

	- <section>

		- <section> 标签定义文档中的节（section、区段）。

	- <article>

		- <article> 标签定义独立的内容。.
		- <article>
  <h1>Internet Explorer 9</h1>
  <p>Windows Internet Explorer 9(缩写为 IE9 )在2011年3月14日21:00 发布。</p>
</article>

	- <aside>

		- <aside> 标签定义页面主区域内容之外的内容（比如侧边栏）。
		- <aside>
  <h4>Epcot Center</h4>
  <p>The Epcot Center is a theme park in Disney World, Florida.</p>
</aside>

	- <figure>

		- <figure>标签规定独立的流内容（图像、图表、照片、代码等等）。
		- <figure> 元素的内容应该与主内容相关，但如果被删除，则不应对文档流产生影响。

	- <figcaption>

		- <figcaption> 标签定义 <figure> 元素的标题.
		- <figcaption>元素应该被置于 "figure" 元素的第一个或最后一个子元素的位置。
		- <figure>
  <img src="img_pulpit.jpg" alt="The Pulpit Rock" width="304" height="228">
  <figcaption>Fig1. - The Pulpit Pock, Norway.</figcaption>
</figure>

	- <footer>

		- <footer> 元素描述了文档的底部区域.
		- <footer> 元素应该包含它的包含元素
		- 一个页脚通常包含文档的作者，著作权信息，链接的使用条款，联系信息等
		- 文档中你可以使用多个 <footer>元素.
		- <footer>
  <p>Posted by: Hege Refsnes</p>
  <p><time pubdate datetime="2012-03-01"></time></p>
</footer>

	- 使用注意事项

		- 针对老版本浏览器

			- 为了让这些块及元素在所有版本的浏览器中生效，你需要在样式表文件中设置一下属性 (以下样式代码可以让旧版本浏览器支持本章介绍的块级元素):
			- header, section, footer, aside, nav, article, figure
{ 
    display: block; 
}

		- Internet Explorer 8 及更早IE版本中的问题

			- 无法在这些元素中渲染CSS效果
			- 解决办法: 你可以使用HTML5 Shiv Javascript脚本来解决IE的兼容问题。HTML5 Shiv下载地址：http://cdn.static.runoob.com/libs/html5shiv/3.7/html5shiv.min.js
			- 下载后，将以下代码放入到网页中
			- <!--[if lt IE 9]>
<script src="html5shiv.js"></script>
<![endif]-->
			- 以上代码在浏览器小于IE9版本时会加载html5shiv.js文件. 你必须将其放置于<head> 元素中，因为 IE浏览器需要在头部加载后渲染这些HTML5的新元素

### Web 存储localStorage 和sessionStorage

- 客户端存储数据的两个对象

	- localStorage

		- 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。

	- sessionStorage

		- 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。

- 检查浏览器是否支持 localStorage 和sessionStorage

	- if(typeof(Storage)!=="undefined")
{
    // 是的! 支持 localStorage  sessionStorage 对象!
    // 一些代码.....
} else {
    // 抱歉! 不支持 web 存储。
}

- localStorage

	- 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。
	- <script>
if(typeof(Storage)!=="undefined")
{
  localStorage.sitename="菜鸟教程";
  document.getElementById("result").innerHTML="网站名：" + localStorage.sitename;
}
else
{
  document.getElementById("result").innerHTML="对不起，您的浏览器不支持 web 存储。";
}
</script>
	- 使用 key="sitename" 和 value="菜鸟教程" 创建一个 localStorage 键/值对。
	- 检索键值为"sitename" 的值然后将数据插入 id="result"的元素中。
	- 也可以这么写
	- // 存储
localStorage.sitename = "菜鸟教程";
// 查找
document.getElementById("result").innerHTML = localStorage.sitename;
//移除
localStorage.removeItem("sitename");
	- <script>
function clickCounter()
{
	if(typeof(Storage)!=="undefined")
	{
		if (localStorage.clickcount)
		{
			localStorage.clickcount=Number(localStorage.clickcount)+1;
		}
		else
		{
			localStorage.clickcount=1;
		}
		document.getElementById("result").innerHTML=" 你已经点击了按钮 " + localStorage.clickcount + " 次 ";
	}
	else
	{
		document.getElementById("result").innerHTML="对不起，您的浏览器不支持 web 存储。";
	}
}
</script>
</head>
<body>
<p><button onclick="clickCounter()" type="button">点我！</button></p>
<div id="result"></div>
<p>点击该按钮查看计数器的增加。</p>
<p>关闭浏览器选项卡(或窗口),重新打开此页面,计数器将继续计数(不是重置)。</p>
</body>

- sessionStorage

	- 针对一个 session 进行数据存储。当用户关闭浏览器窗口后，数据会被删除。
	- <script>
function clickCounter()
{
	if(typeof(Storage)!=="undefined")
	{
		if (sessionStorage.clickcount)
		{
			sessionStorage.clickcount=Number(sessionStorage.clickcount)+1;
		}
		else
		{
			sessionStorage.clickcount=1;
		}
		document.getElementById("result").innerHTML="在这个会话中你已经点击了该按钮 " + sessionStorage.clickcount + " 次 ";
	}
	else
	{
		document.getElementById("result").innerHTML="抱歉，您的浏览器不支持 web 存储";
	}
}
</script>
</head>
<body>
<p><button onclick="clickCounter()" type="button">点我！</button></p>
<div id="result"></div>
<p>点击该按钮查看计数器的增加。</p>
<p>关闭浏览器选项卡(或窗口),重新打开此页面,计数器将重置。</p>
</body>

- Web Storage 开发一个简单的网站列表程序

	- 简单的 localStorage 存储与查找
	- 使用 JSON.stringify 来存储对象数据
	- 主要内容详解：http://www.runoob.com/html/html5-webstorage.html

### Web SQL 数据库

- http://www.runoob.com/sql/sql-tutorial.html

- http://www.runoob.com/html/html5-web-sql.html

### 应用程序缓存

- 含义

	- 这意味着 web 应用可进行缓存，并可在没有因特网连接时进行访问。
	- 通过创建 cache manifest 文件，可以轻松地创建 web 应用的离线版本。

- 优势

	- 离线浏览 - 用户可在应用离线时使用它们
	- 速度 - 已缓存资源加载得更快
	- 减少服务器负载 - 浏览器将只从服务器下载更新过或更改过的资源。

- Cache Manifest 基础

	- 每个指定了 manifest 的页面在用户对其访问时都会被缓存。如果未指定 manifest 属性，则页面不会被缓存（除非在 manifest 文件中直接指定了该页面）。
	- manifest 文件的建议的文件扩展名是：".appcache"。
	- manifest 文件需要配置正确的 MIME-type，即 "text/cache-manifest"。必须在 web 服务器上进行配置。
	- 文件可分为三个部分

		- CACHE MANIFEST - 在此标题下列出的文件将在首次下载后进行缓存

			- CACHE MANIFEST
/theme.css
/logo.gif
/main.js
			- manifest 文件列出了三个资源：一个 CSS 文件，一个 GIF 图像，以及一个 JavaScript 文件。当 manifest 文件加载后，浏览器会从网站的根目录下载这三个文件。然后，无论用户何时与因特网断开连接，这些资源依然是可用的。

		- NETWORK - 在此标题下列出的文件需要与服务器的连接，且不会被缓存

			- NETWORK:
login.php

				- NETWORK 小节规定文件 "login.php" 永远不会被缓存，且离线时是不可用的：

			- NETWORK:
*

				- 可以使用星号来指示所有其他资源/文件都需要因特网连接：

		- FALLBACK - 在此标题下列出的文件规定当页面无法访问时的回退页面（比如 404 页面）

			- FALLBACK:
/html/ /offline.html

				- FALLBACK 小节规定如果无法建立因特网连接，则用 "offline.html" 替代 /html5/ 目录中的所有文件：
				- 注意: 第一个 URI 是资源，第二个是替补。

	- 更新缓存(一旦应用被缓存，它就会保持缓存直到发生下列情况

		- 用户清空浏览器缓存
		- manifest 文件被修改（参阅下面的提示）
		- 由程序来更新应用缓存

	- 完整的 Manifest 文件

		- CACHE MANIFEST
# 2012-02-21 v1.0.0
/theme.css
/logo.gif
/main.js

NETWORK:
login.php

FALLBACK:
/html/ /offline.html

	-  "#" 开头的是注释行，但也可满足其他用途。应用的缓存会在其 manifest 文件更改时被更新。如果您编辑了一幅图片，或者修改了一个 JavaScript 函数，这些改变都不会被重新缓存。更新注释行中的日期和版本号是一种使浏览器重新缓存文件的办法。

- 注意

	- 一旦文件被缓存，则浏览器会继续展示已缓存的版本，即使您修改了服务器上的文件。为了确保浏览器更新缓存，您需要更新 manifest 文件。
	- 浏览器对缓存数据的容量限制可能不太一样（某些浏览器设置的限制是每个站点 5MB）。

### Web Workers

- 含义作用

	- 当在 HTML 页面中执行脚本时，页面的状态是不可响应的，直到脚本已完成。
	- web worker 是运行在后台的 JavaScript，独立于其他脚本，不会影响页面的性能。您可以继续做任何愿意做的事情：点击、选取内容等等，而此时 web worker 在后台运行。
	- web worker 是运行在后台的 JavaScript，不会影响页面的性能。

### 服务器发送事件(Server-Sent Events)SSE

- HTML5 服务器发送事件（server-sent event）允许网页获得来自服务器的更新。
- 接收 Server-Sent 事件通知

	- EventSource 对象用于接收服务器发送事件通知：
	- <body>
<h1>获取服务端更新数据</h1>
<div id="result"></div>

<script>
if(typeof(EventSource)!=="undefined")
{
	var source=new EventSource("demo_sse.php");
	source.onmessage=function(event)
	{
		document.getElementById("result").innerHTML+=event.data + "<br>";
	};
}
else
{
	document.getElementById("result").innerHTML="抱歉，你的浏览器不支持 server-sent 事件...";
}
</script>

- 检测 Server-Sent 事件支持

	- 以下实例，我们编写了一段额外的代码来检测服务器发送事件的浏览器支持情况：
	- if(typeof(EventSource)!=="undefined")
{
    // 浏览器支持 Server-Sent
    // 一些代码.....
}
else
{
    // 浏览器不支持 Server-Sent..
}

- onopen	当通往服务器的连接被打开
- onmessage	当接收到消息
- onerror	当发生错误

### WebSocket

- WebSocket 是 HTML5 开始提供的一种在单个 TCP 连接上进行全双工通讯的协议。
- WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。
- http://www.runoob.com/html/html5-websocket.html

## HTML(5) 代码规范

### 使用正确的文档类型

### 使用小写元素名

- <section> 
  <p>这是一个段落。</p>
</section>

### 关闭空的 HTML 元素

- <meta charset="utf-8" />

### 空格和等号

- 推荐少用空格
- <link rel="stylesheet" href="styles.css">

### 避免一行代码过长

- 使用 HTML 编辑器，左右滚动代码是不方便的。
每行代码尽量少于 80 个字符。

### 空行和缩进

- 不要无缘无故添加空行。

为每个逻辑功能块添加空行，这样更易于阅读。

缩进使用两个空格，不建议使用 TAB。

比较短的代码间不要使用不必要的空行和缩进。

### HTML 注释

- <!-- 这是注释 -->

### 样式表

- 短的规则可以写成一行:
- 长的规则可以写成多行:

	- body {
  background-color: lightgrey;
  font-family: "Arial Black", Helvetica, sans-serif;
  font-size: 16em;
  color: black;
}

- 注意事项

	- 将左花括号与选择器放在同一行。
	- 左花括号与选择器间添加一个空格。
	- 使用两个空格来缩进。
	- 冒号与属性值之间添加一个空格。
	- 逗号和符号之后使用一个空格。在逗号和冒号后添加空格是常用的一个规则。
	- 每个属性与值结尾都要使用分号。
	- 只有属性值包含空格时才使用引号。
	- 右花括号放在新的一行。
	- 每行最多 80 个字符。

## CSS

### 简介

- 含义

	- CSS 指层叠样式表 (Cascading Style Sheets)
	- 样式定义如何显示 HTML 元素
	- 样式通常存储在样式表中
	- 把样式添加到 HTML 4.0 中，是为了解决内容与表现分离的问题
	- 外部样式表可以极大提高工作效率
	- 外部样式表通常存储在 CSS 文件中
	- 多个样式定义可层叠为一个

### 语法（加图片

- 主要的构成部分：选择器，以及一条或多条声明

	- p
{
color:red;
text-align:center;
}

- CSS声明总是以分号(;)结束，声明组以大括号({})括起来:
- 注释

	- /*这是个注释*/
p
{
text-align:center;
/*这是另一个注释*/
color:black;
font-family:arial;
}

- 不要在属性值与单位之间留有空格（如："margin-left: 20 px" ），正确的写法是 "margin-left: 20px" 

### CSS选择器

- 类名的第一个字符不能使用数字！它无法在 Mozilla 或 Firefox 中起作用。
- id 选择器

	- #
	- #para1
{
    text-align:center;
    color:red;
}

- class 选择器

	- .center {text-align:center;}

- 指定特定的HTML元素使用class

	- p.center {text-align:center;}

- CSS选择器笔记

	- http://www.ruanyifeng.com/blog/2009/03/css_selectors.html

- 30个你必须熟记的CSS选择器

	- https://code.tutsplus.com/zh-hans/tutorials/the-30-css-selectors-you-must-memorize--net-16048

- 组合选择符
- 伪类
- 伪元素
- 属性选择器

### CSS创建

- 外部样式表(External style sheet)

	- 当样式需要应用于很多页面时
	- <head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

- 内部样式表(Internal style sheet)

	- 当单个文档需要特殊的样式时，就应该使用内部样式表。
	- <head>
<style>
hr {color:sienna;}
p {margin-left:20px;}
body {background-image:url("images/back40.gif");}
</style>
</head>

- 内联样式(Inline style)（慎用）

	- 由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。
	- <p style="color:sienna;margin-left:20px">这是一个段落。</p>

- 多重样式优先级

	- 如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来。 
	- 如果外部样式放在内部样式的后面，则外部样式将覆盖内部样式。
	- 内联样式）Inline style > （内部样式）Internal style sheet >（外部样式）External style sheet > 浏览器默认样式
	- 优先级逐级增加的选择器列表

		- 通用选择器（*）
		- 元素(类型)选择器
		- 类选择器
		- 属性选择器
		- 伪类
		- ID 选择器
		- 内联样式

	- !important规则

		- 当 !important 规则被应用在一个样式声明中时，该样式声明会覆盖CSS中任何其他的声明，无论它处在声明列表中的哪里。
		- 使用的经验法则

			- 1.Always 要优化考虑使用样式规则的优先级来解决问题而不是 !important
2.Only 只在需要覆盖全站或外部 css（例如引用的 ExtJs 或者 YUI ）的特定页面中使用 !important
3.Never 永远不要在全站范围的 css 上使用 !important
4.Never 永远不要在你的插件中使用 !important

	- 更多资料

		- http://www.runoob.com/w3cnote/css-style-priority.html

### Backgrounds(背景)

- background-color

	- 定义了元素的背景颜色
	- body {background-color:#b0c4de;}
	- 颜色值通常以以下方式定义

		- 十六进制 - 如："#ff0000"
		- RGB - 如："rgb(255,0,0)"
		- 颜色名称 - 如："red"

- background-image

	- 描述了元素的背景图像
	- <style>
body 
{
	background-image:url('paper.gif');
}
</style>

- background-repeat

	- 水平或垂直平铺

		- body
{
background-image:url('gradient2.png');
background-repeat:repeat-x;
}

	- 设置定位与不平铺

		- body
{
background-image:url('img_tree.png');
background-repeat:no-repeat;
}

- background-attachment

	- 背景图像是否固定或者随着页面的其余部分滚动。
	- fixed/scroll

		- body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-attachment: fixed;}

- Background Position

	- background-position-percentage

		- body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-position: center top;}

	- Background Position

		- body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-position: 50% 50%;}
		- left top / center / bottom ; center top / center / bottom ; right top / center / bottom
		- left top
		- left center
		- left bottom
		- right top
		- right center
		- right bottom
		- center top
		- center center
		- center bottom

- background-position

	- body
{
background-image:url('img_tree.png');
background-repeat:no-repeat;
background-position:right top;
}

- 简写属性

	- body {background:#ffffff url('img_tree.png') no-repeat right top;}
	- 属性值的顺序为

		- background-color；background-image；background-repeat；background-attachment；background-position

### Text(文本)

- 文本颜色

	- body {color:red;}
h1 {color:#00ff00;}
h2 {color:rgb(255,0,0);}

- 文本的对齐方式

	- 文本排列属性是用来设置文本的水平对齐方式。
	- h1 {text-align:center;}
p.date {text-align:right;}
p.main {text-align:justify;}
	- left	把文本排列到左边。默认值：由浏览器决定。
right	把文本排列到右边。
center	把文本排列到中间。
justify	实现两端对齐文本效果。
inherit	规定应该从父元素继承 text-align 属性的值。

- 文本修饰

	- 从设计的角度看 text-decoration属性主要是用来删除链接的下划线：
	- a {text-decoration:none;}
	- 不建议强调指出不是链接的文本，因为这常常混淆用户。
	- h1 {text-decoration:overline;}
h2 {text-decoration:line-through;}
h3 {text-decoration:underline;}
	- blink	

		- 定义闪烁的文本。

- 文本大小写转换

	- 文本转换属性是用来指定在一个文本中的大写和小写字母。
	- p.uppercase {text-transform:uppercase;}
p.lowercase {text-transform:lowercase;}
p.capitalize {text-transform:capitalize;}

- 文本缩进

	- 指定文本的第一行的缩进
	- p {text-indent:50px;}

- 间距

	- 字符间距

		- 母与字母之间的间距
		- h2 {letter-spacing:-3px}

	- 字间距

		- 英文单词之间的间距
		- p
{ 
word-spacing:30px;
}

- 行高

	- 在大多数浏览器默认行高约20 px

		- p.small
{
	line-height: 10px
}

	- 浏览器的默认行高为“1”

		- p.small
{
line-height: 0.5
}

- 文字阴影

	- h1
{
    text-shadow: 2px 2px #ff0000;
}
	- text-shadow: h-shadow v-shadow blur color;
	- h-shadow	必需。水平阴影的位置。允许负值。
v-shadow	必需。垂直阴影的位置。允许负值。
blur	可选。模糊的距离。

- 设置或返回文本是否被重写 

	- unicode-bidi: normal|embed|bidi-override|initial|inherit;

- 设置元素的垂直对齐

	- baseline	默认。元素放置在父元素的基线上。
sub	垂直对齐文本的下标。
super	垂直对齐文本的上标
top	把元素的顶端与行中最高元素的顶端对齐
text-top	把元素的顶端与父元素字体的顶端对齐
middle	把此元素放置在父元素的中部。
bottom	把元素的底端与行中最低的元素的顶端对齐。
text-bottom	把元素的底端与父元素字体的底端对齐。
length	 
%	使用 "line-height" 属性的百分比值来排列此元素。允许使用负值。
	- <style>
img.top {vertical-align:text-top;}
img.bottom {vertical-align:text-bottom;}
</style>

- 设置元素中空白的处理方式

	- 规定段落中的文本不进行换行：
	- p
{
    white-space:nowrap;
}
	- normal	默认。空白会被浏览器忽略。
pre	空白会被浏览器保留。其行为方式类似 HTML 中的 <pre> 标签。
nowrap	文本不会换行，文本会在在同一行上继续，直到遇到 <br> 标签为止。
pre-wrap	保留空白符序列，但是正常地进行换行。
pre-line	合并空白符序列，但是保留换行符。

### Fonts(字体)

- 字体系列

	- 特定字体系列

		- 一个特定的字体系列（如 "Times" 或 "Courier"）

	- 通用字体系列

		- 拥有相似外观的字体系统组合如 "Serif" 或 "Monospace"）

- Web安全字体组合

	- http://www.runoob.com/cssref/css-websafe-fonts.html
	- font-family属性是多种字体的名称，作为一个"应变"制度，以确保浏览器/操作系统之间的最大兼容性。如果浏览器不支持的第一个字体，它尝试下一个的字体。

你想要的字体类型如果浏览器找不到，它会从通用的字体类型中找到与你相似的:

- 文本的字体

	- font-family 

		- 如果字体系列的名称超过一个字，它必须用引号，如Font Family："宋体"。

多个字体系列是用一个逗号分隔指明
		- p{font-family:"Times New Roman", Times, serif;}

- 字体样式

	- font-style

		- p.normal {font-style:normal;}
		- p.italic {font-style:italic;}
		- p.oblique {font-style:oblique;}

			- 不推荐

- 字体大小

	- font-size

		- h1 {font-size:40px;}

	- 如果你不指定一个字体的大小，默认大小和普通文本段落一样，是16像素（16px=1em
	- 为了避免Internet Explorer 中无法调整文本的问题，许多开发者使用 em 单位代替像素。

em的尺寸单位由W3C建议。

1em和当前字体大小相等。在浏览器中默认的文字大小是16px。

因此，1em的默认大小是16px。可以通过下面这个公式将像素转换为em：px/16=em
	- 使用百分比和EM组合

		- 在所有浏览器的解决方案中，设置 <body>元素的默认字体大小的是百分比：
		- body {font-size:100%;}
h1 {font-size:2.5em;}
h2 {font-size:1.875em;}
p {font-size:0.875em;}

- 字体粗细

	- p.normal {font-weight:normal;}
p.thick {font-weight:bold;}
p.thicker {font-weight:900;}
	- bold	定义粗体字符。
bolder	定义更粗的字符。
lighter	定义更细的字符。
	- 定义由粗到细的字符。400 等同于 normal，而 700 等同于 bold。

		- 100
200
300
400
500
600
700
800
900

- 把段落设置为小型大写字母字

	- p.small
{
font-variant:small-caps;
}

- 在一个声明中的所有字体属性

	- p
{
	font:italic bold 12px/30px Georgia,serif;
}

### 链接(link)

- a:link - 正常，未访问过的链接
a:visited - 用户已访问过的链接
a:hover - 当用户鼠标放在链接上时
a:active - 链接被点击的那一刻
- a:hover 必须跟在 a:link 和 a:visited后面
a:active 必须跟在 a:hover后面
- a:link {text-decoration:none;}
- a:link {background-color:#B2FF99;}
- <style>
a:link {background-color:#B2FF99;}    /* 未访问链接 */
a:visited {background-color:#FFFF85;} /* 已访问链接 */
a:hover {background-color:#FF704D;}   /* 鼠标移动到链接上 */
a:active {background-color:#FF704D;}  /* 鼠标点击时 */
</style>
- a.five:link {color:#ff0000;text-decoration:none;}
a.five:visited {color:#0000ff;text-decoration:none;}
a.five:hover {text-decoration:underline;}
- <style>
a:link,a:visited
{
	display:block;
	font-weight:bold;
	color:#FFFFFF;
	background-color:#98bf21;
	width:120px;
	text-align:center;
	padding:4px;
	text-decoration:none;
}
a:hover,a:active
{
	background-color:#7A991A;
}
</style>

### 列表样式(ul)

- 无序列表 - 列表项标记用特殊图形（如小黑点、小方框等）
- 有序列表 - 列表项的标记有数字或字母
- list-style-type

	- 指定列表项标记的类型

		- <style>
ul.a {list-style-type:circle;}
ul.b {list-style-type:square;}
ol.c {list-style-type:upper-roman;}
ol.d {list-style-type:lower-alpha;}
</style>
</head>

<body>
<p>无序列表实例:</p>

<ul class="a">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Coca Cola
</body>

- list-style-image

	- 要指定列表项标记的图像，使用列表样式图像属性

		- ul
{
    list-style-image: url('sqpurple.gif');
}

- list-style-position

	- 规定列表中列表项目标记的位置

		- ul {
    list-style-position: inside;
}
		- inside	列表项目标记放置在文本以内，且环绕文本根据标记对齐。
		- outside	默认值。保持标记位于文本的左侧。列表项目标记放置在文本以外，且环绕文本不根据标记对齐。

- 浏览器兼容性解决方案

	- 同样在所有的浏览器，下面的例子会显示的图像标记
	- ul
{
    list-style-type: none;
    padding: 0px;
    margin: 0px;
}
ul li
{
    background-image: url(sqpurple.gif);
    background-repeat: no-repeat;
    background-position: 0px 5px; 
    padding-left: 14px; 
}

		- ul:
设置列表样式类型为没有删除列表项标记
设置填充和边距0px（浏览器兼容性）
ul中所有li:
设置图像的URL，并设置它只显示一次（无重复）
您需要的定位图像位置（左0px和上下5px）
用padding-left属性把文本置于列表中

- 列表 -简写属性

	- 在单个属性中可以指定所有的列表属性。这就是所谓的简写属性。
	- ul
{
    list-style: square url("sqpurple.gif");
}

- 所有不同的列表项标记

	- http://www.runoob.com/try/try.php?filename=trycss_list-style-type_all

### Table(表格)

- 表格边框

	- table, th, td
{
    border: 1px solid black;
}
	- 例子中的表格有双边框。这是因为表和th/ td元素有独立的边界。

- 折叠边框

	- 设置表格的边框是否被折叠成一个单一的边框或隔开
	- border-collapse
	- table
{
    border-collapse:collapse;
}
table,th, td
{
    border: 1px solid black;
}

- 表格宽度和高度

	- table 
{
    width:100%;
}
th
{
    height:50px;
}

- 表格文字对齐

	- 水平对齐

		- text-align
		- td
{
    text-align:right;
}

	- 垂直对齐

		- vertical-align
		- td
{
    height:50px;
    vertical-align:bottom;
}

- 表格内边距

	- td
{
    padding:15px;
}

- 表格颜色

	- table, td, th
{
    border:1px solid green;
}
th
{
    background-color:green;
    color:white;
}

- basic table structure

	- <table>
	- <tr> table row
	- <td>table data

- table elements

	- <table>	定义表格
	- <th>	定义表格的表头
	- <tr>	定义表格的行
	- <td>	定义表格单元
	- <caption>	定义表格标题
	- <colgroup>	定义表格列的组
	- <col>	定义用于表格列的属性
	- <thead>	定义表格的页眉
	- <tbody>	定义表格的主体
	- <tfoot>	定义表格的页脚

- spanning columns/跨列/colspan
- spanning rows/跨行/rowspan

### 盒子模型（图片

- Margin(外边距) - 清除边框外的区域，外边距是透明的。
- Border(边框) - 围绕在内边距和内容外的边框。
- Padding(内边距) - 清除内容周围的区域，内边距是透明的。
- Content(内容) - 盒子的内容，显示文本和图像。
- 总元素的宽度=宽度+左填充+右填充+左边框+右边框+左边距+右边距
- 总元素的高度=高度+顶部填充+底部填充+上边框+下边框+上边距+下边距

### Border(边框)（图片

- 边框样式

	- border-style

		- none: 默认无边框


dotted: 定义一个点线边框


dashed: 定义一个虚线边框


solid: 定义实线边框


double: 定义两个边框。 两个边框的宽度和 border-width 的值相同


groove: 定义3D沟槽边框。效果取决于边框的颜色值


ridge: 定义3D脊边框。效果取决于边框的颜色值


inset:定义一个3D的嵌入边框。效果取决于边框的颜色值


outset: 定义一个3D突出边框。 效果取决于边框的颜色值
		- p.dotted {border-style:dotted;}

- 边框宽度

	- border-width

		- p.one
{
    border-style:solid;
    border-width:5px;
}

- 边框颜色

	- border-color

		- p.one
{
    border-style:solid;
    border-color:red;
}

- 单独设置各边

	- 普通方式

		- p
{
    border-top-style:dotted;
    border-right-style:solid;
    border-bottom-style:dotted;
    border-left-style:solid;
}

	- 简写方式

		- border-style:dotted solid double dashed;

			- 上边框是 dotted
右边框是 solid
底边框是 double
左边框是 dashed

		- border-style:dotted solid double;

			- 上边框是 dotted
左、右边框是 solid
底边框是 double

		- border-style:dotted solid;

			- 上、底边框是 dotted
右、左边框是 solid

- 边框-简写属性

	- border:5px solid red;

		- border-width
border-style (required)
border-color

### 轮廓（outline）属性

- 轮廓（outline）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

轮廓（outline）属性指定元素轮廓的样式、颜色和宽度。
- p 
{
	border:1px solid red;
	outline:green dotted thick;
}
- outline-style:solid;
outline-width:thin;
outline-color:#00ff00;

### margin(外边距)(图片

- margin 清除周围的（外边框）元素区域。margin 没有背景颜色，是完全透明的。

margin 可以单独改变元素的上，下，左，右边距，也可以一次改变所有的属性。
- 单边外边距属性

	- p.margin
{
	margin-top:100px;
	margin-bottom:100px;
	margin-right:50px;
	margin-left:50px;
}

- 简写属性

	- margin:25px 50px 75px 100px;

		- 上边距为25px
右边距为50px
下边距为75px
左边距为100px

	- margin:25px 50px 75px;

		- 上边距为25px
左右边距为50px
下边距为75px

	- margin:25px 50px;

		- 上下边距为25px
左右边距为50px

	- margin:25px;

		- 所有的4个边距都是25px

- Margin可以使用负值，重叠的内容。

### padding（内边距）（图片

- 定义元素边框与元素内容之间的空间，即上下左右的内边距。
- 当元素的 padding（填充）内边距被清除时，所释放的区域将会受到元素背景颜色的填充。

单独使用 padding 属性可以改变上下左右的填充。
- 单边外边距属性

	- padding-top:25px;
padding-bottom:25px;
padding-right:50px;
padding-left:50px;

- 简写属性

	- padding:25px 50px 75px 100px;
	- padding:25px 50px 75px;
	- padding:25px 50px;
	- padding:25px;

### 尺寸 (Dimension)height	

- 注意： 负值是不允许的，大多数浏览器的默认行高约为110%至120%。
- height	设置元素的高度。
- line-height	设置行高。

	- p.small {line-height:70%;}

- max-height	设置元素的最大高度。
- max-width	设置元素的最大宽度。
- min-height	设置元素的最小高度。
- min-width	设置元素的最小宽度。

### Display(显示) 与 Visibility（可见性）

- 隐藏元素 

	- display:none

		- 隐藏某个元素，且隐藏的元素不会占用任何空间

	- visibility:hidden/visible

		- 隐藏的元素仍需占用与未隐藏之前一样的空间

	- h1 {display:none;}
	- h1{visibility:hidden;}

- CSS中块级、内联元素的应用

	- display:block  -- 显示为块级元素
	- display:inline  -- 显示为内联元素
	- display:inline-block -- 显示为内联块元素，表现为同行显示并可修改宽高内外边距等属性

- 表的collapse属性

	- <style>
table, th, td {
    border: 1px solid black;
}

tr.collapse {
    visibility: collapse;
}
</style>
</head>
<body>

<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  <tr>
    <td>Peter</td>
    <td>Griffin</td>
  </tr>
  <tr class="collapse">
    <td>Lois</td>
    <td>Griffin</td>
  </tr>
</table>

<p><b>注意:</b> IE8 及其更早版本需要通过指定 !DOCTYPE 才可以支持 visibility:collapse。</p>

</body>

### Position(定位)

- position:static

	- you do not need a CSS property to indicate
	- static 定义：元素默认值，没有定位，遵循正常的文档流对象，不会受到 top、bottom、left、right 偏移量的影响

- position:relative 相对定位

	- p.example { position: relative; top: 10px; left: 100px;}

	- 定义：相对定位，当前元素的位置是相对其正常位置进行定位。元素通过偏移量属性：top、bottom、left、right进行规定

- position:absolute 绝对定位

	- h1 { position: absolute; top: 0px; left: 500px; width: 250px;}p { width: 450px;}
	- 定义：绝对定位，当前元素的位置相对于父元素（没有父元素默认是<html>元素）的位置
	- absolute 定位使元素的位置与文档流无关，因此不占据空间。所以它们可以覆盖页面上的其它元素。
	- absolute 定位的元素和其他元素重叠。

- position:fixed

	- when a user scrolls down the page, it stays in the exact same place
	- h1 { position: fixed; top: 0px; left: 50px; padding: 10px; margin: 0px; width: 100%; background-color: #efefef;}p.example { margin-top: 100px;}
	- 定义：当前元素相对于浏览器的窗口的位置，元素通过偏移量属性：top、bottom、left、right进行规定，元素位置相对于浏览器窗口是固定位置，即使窗口是滚动的，它也不会移动。Fixed定位使元素的位置与文档流无关，因此不占据空间。Fixed定位的元素和其他元素重叠。

- z-index

	- If you want to control which element sits on top，堆叠顺序（哪个元素应该放在前面，或后面）
	- 元素的定位与文档流无关，所以它们可以覆盖页面上的其它元素

z-index属性指定了一个元素的堆叠顺序（哪个元素应该放在前面，或后面）

一个元素可以有正数或负数的堆叠顺序：
	- h1 { position: fixed; top: 0px; left: 0px; margin: 0px; padding: 10px; width: 100%; background-color: #efefef; z-index: 10;}p { position: relative; top: 70px; left: 70px;}
	- img 
{ 
position:absolute; 
left:0px; 
top:0px; 
z-index:-1; 
}
	-  Its value is a number, and the higher the number the closer that element is to the front.

- float

	- blockquote {    float: right;    width: 275px;    font-size: 130%;    font-style: italic;    font-family: Georgia, Times, serif;    margin: 0px 0px 10px 10px;    padding: 10px;    border-top: 1px solid #665544;    border-bottom: 1px solid #665544;}
	- 1. 浮动元素从常规流中脱离，被漂浮在容器(包含块)左边或右边
2. 浮动盒会一直漂到其外边缘挨到容器边缘或另外的浮动盒
3. 浮动元素不会影响其后面的流内块级盒
4. 但是浮动元素后面的行级盒子会变短以避开浮动元素
	- left 
right 
none 
inherit
	- Clearing Floats

		- clear

			- 含义

				- 指定元素哪一边不能与之前的浮动框相邻

			- 取值

				- left
				- right
				- both
				- none

- sticky

	- 定义：粘性定位的元素是依赖于用户的滚动，在 position:relative 与 position:fixed 定位之间切换。它的行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置。
	- <style>
.sticky {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  padding: 5px;
  border: 1px solid red;
}
</style>
<p>尝试滚动页面。</p>
<div class="sticky">通过position:sticky 定位</div>
<div style="padding-bottom:2000px">
  <p>滚动我</p>
  <p>来回滚动我</p>
  <p>滚动我</p>
  <p>来回滚动我</p>
  <p>滚动我</p>
  <p>来回滚动我</p>
</div>

### Overflow

- visible	默认值。内容不会被修剪，会呈现在元素框之外。
- hidden	内容会被修剪，并且其余内容是不可见的。
- scroll	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
- auto	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
- div {
    width: 200px;
    height: 50px;
    background-color: #eee;
    overflow: visible;
}

### Float（浮动）

- CSS 的 Float（浮动），会使元素向左或向右移动，其周围的元素也会重新排列。
- float

	- blockquote {    float: right;    width: 275px;    font-size: 130%;    font-style: italic;    font-family: Georgia, Times, serif;    margin: 0px 0px 10px 10px;    padding: 10px;    border-top: 1px solid #665544;    border-bottom: 1px solid #665544;}
	- 1. 浮动元素从常规流中脱离，被漂浮在容器(包含块)左边或右边
2. 浮动盒会一直漂到其外边缘挨到容器边缘或另外的浮动盒
3. 浮动元素不会影响其后面的流内块级盒
4. 但是浮动元素后面的行级盒子会变短以避开浮动元素
	- img
{
    float:right;
}
	- left 
right 
none 
inherit
	- Clearing Floats

		- clear

			- 含义

				- 指定元素哪一边不能与之前的浮动框相邻

			- 取值

				- left
				- right
				- both
				- none

			- .text_line
{
    clear:both;
}

- 让段落的第一个字母浮动到左侧

	- http://www.runoob.com/try/try.php?filename=trycss_float4

- 创建一个没有表格的网页

	- http://www.runoob.com/try/try.php?filename=trycss_float6

### 水平 & 垂直对齐

- 元素居中对齐

	- margin: auto;

- 文本居中对齐

	- text-align: center;

- 图片居中对齐

	- margin: auto;
	- img {
    display: block;
    margin: auto;
    width: 40%;
}

- 垂直居中对齐

	- padding

		- .center {
    padding: 70px 0;
    border: 3px solid green;
}

	-  line-height

		- .center {
    line-height: 200px;
    height: 200px;
    border: 3px solid green;
    text-align: center;
}
 
/* 如果文本有多行，添加以下代码: */
.center p {
    line-height: 1.5;
    display: inline-block;
    vertical-align: middle;
}
		- http://www.runoob.com/try/try.php?filename=trycss_align_line

	-  position 和 transform

		- .center { 
    height: 200px;
    position: relative;
    border: 3px solid green; 
}
 
.center p {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
		- http://www.runoob.com/try/try.php?filename=trycss_align_transform

- 水平和垂直都居中

	- .center {
    padding: 70px 0;
    border: 3px solid green;
    text-align: center;
}

- 左右对齐 

	- 使用定位方式

		- .right {
    position: absolute;
    right: 0px;
    width: 300px;
    border: 3px solid #73AD21;
    padding: 10px;
}

	- 使用 float 方式

		- body {
    margin: 0;
    padding: 0;
}
 
.container {
    position: relative;
    width: 100%;
}
 
.right {
    position: absolute;
    right: 0px;
    width: 300px;
    background-color: #b0e0e6;
}

### 导航栏

- http://www.runoob.com/css/css-navbar.html

### 下拉菜单

- http://www.runoob.com/css/css-dropdowns.html

### 提示工具

- http://www.runoob.com/css/css-tooltip.html

### 图片廊

- http://www.runoob.com/css/css-image-gallery.html

### 图像透明/不透明

- Opacity
- img
{
  opacity:0.4;
  filter:alpha(opacity=40); /* IE8 及其更早版本 */
}
- Opacity / rgba

	- alpha value

		- a number between 0.0 and 1.0 (so a value of 0.5 is 50% opacity and 0.15 is 15% opacity).

	- 悬停效果

		- img
 {
 opacity:0.4;
 filter:alpha(opacity=40); /* For IE8 and earlier */
 }
 img:hover
 {
 opacity:1.0;
 filter:alpha(opacity=100); /* For IE8 and earlier */
 }

### 图像拼合技术

- 图像拼合 - 创建一个导航列表
- http://www.runoob.com/css/css-image-sprites.html

### 媒体类型

- all	用于所有的媒体设备。
- aural	用于语音和音频合成器。
- braille	用于盲人用点字法触觉回馈设备。
- embossed	用于分页的盲人用点字法打印机。
- handheld	用于小的手持的设备。
- print	用于打印机。
- projection	用于方案展示，比如幻灯片。
- screen	用于电脑显示器。
- tty	用于使用固定密度字母栅格的媒体，比如电传打字机和终端。
- tv	用于电视机类型的设备。
- 媒体类型允许你指定文件将如何在不同媒体呈现。该文件可以以不同的方式显示在屏幕上，在纸张上，或听觉浏览器等等。 
- http://www.runoob.com/css/css-mediatypes.html

### 实例

- CSS 响应式设计

	- Viewport
	- 网格视图
	- 媒体查询
	- 图片
	- 视频(Video)
	- 框架

## CSS3

### 教程

### 简介

### 边框（Borders）

### 背景

### 渐变

### 文本效果

### 字体

### 2D 转换

### 3D 转换

### 过渡

### 动画

### 多列

### 用户界面

### 图片（w3c多出的内容

### 按钮

### 分页实例

### 框大小

### 弹性盒子Flex Box

### 多媒体查询

*XMind: ZEN - Trial Version*