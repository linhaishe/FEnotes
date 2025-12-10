# 20. DOM

HTML tag is just opening or closing entity. For example:

`<p> and </p> are called HTML tags`

HTML element encompasses opening tag, closing tag, content (optional for content-less tags) Eg:

`<p>This is the content</p>` : This complete thing is called a HTML element

文档对象模型（DOM，Document Object Model）是 HTML 和 XML 文档的编程接口。DOM 表示由多层节点构成的文档，通过它开发者可以添加、删除和修改页面的各个部分。脱胎于网景和微软早期的动态 HTML（DHTML，Dynamic HTML），DOM 现在是真正跨平台、语言无关的表示和操作网页的方式。

- The HTML elements as **objects**
- The **properties** of all HTML elements
- The **methods** to access all HTML elements
- The **events** for all HTML elements

In other words: **The HTML DOM is a standard for how to get, change, add, or delete HTML elements.**

![](https://www.w3schools.com/js/pic_htmltree.gif)

## Node vs Elemet

以下摘自MDN:

> A Node is an interface from which a number of DOM types inherit, and allows these various types to be treated (or tested) similarly.

> The following interfaces all inherit from Node its methods and properties: Document, Element, CharacterData (which Text, Comment, and CDATASection inherit), ProcessingInstruction, DocumentFragment, DocumentType, Notation, Entity, EntityReference.

## DOM Root Nodes

[dom node](https://www.w3schools.com/jsref/prop_node_nodetype.asp)

There are two special properties that allow access to the full document:

- `document.body` - The body of the document
- `document.documentElement` - The full document

**Tip:** The difference between this property and the [document.body](https://www.w3schools.com/jsref/prop_doc_body.asp) property, is that the document.body element returns the <body> element, while the document.documentElement returns the <html> element.

```html
<html>
<body>

<p>Hello World!</p>
<div>
<p>The DOM is very useful!</p>
<p>This example demonstrates the <b>document.body</b> property.</p>
</div>

<script>
alert(document.body.innerHTML);
</script>

</body>
</html>
```

```html
<html>
<body>

<p>Hello World!</p>
<div>
<p>The DOM is very useful!</p>
<p>This example demonstrates the <b>document.documentElement</b> property.</p>
</div>

<script>
alert(document.documentElement.innerHTML);
</script>

</body>
</html>
```

### The nodeType Property(类型)

The `nodeType` property is read only. It returns the type of a node.html

<mark>所有东西都有一个nodetype属性</mark>

The most important nodeType properties are:

| Node               | Type | Example                                         |
| :----------------- | :--- | :---------------------------------------------- |
| ELEMENT_NODE       | 1    | <h1 class="heading">W3Schools</h1>              |
| ATTRIBUTE_NODE     | 2    | class = "heading" (deprecated)                  |
| TEXT_NODE          | 3    | W3Schools                                       |
| COMMENT_NODE       | 8    | <!-- This is a comment -->                      |
| DOCUMENT_NODE      | 9    | The HTML document itself (the parent of <html>) |
| DOCUMENT_TYPE_NODE | 10   | <!Doctype html>                                 |

| 节点类型 | 描述                      | 子节点                                              |                                                              |
| :------- | :------------------------ | :-------------------------------------------------- | ------------------------------------------------------------ |
| 1        | <mark>Element</mark>      | 代表元素                                            | Element, Text, Comment, ProcessingInstruction, CDATASection, EntityReference |
| 2        | <mark>Attr</mark>         | 代表属性                                            | Text, EntityReference                                        |
| 3        | <mark>Text</mark>         | 代表元素或属性中的文本内容。                        | None                                                         |
| 4        | CDATASection              | 代表文档中的 CDATA 部分（不会由解析器解析的文本）。 | None                                                         |
| 5        | EntityReference           | 代表实体引用。                                      | Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference |
| 6        | Entity                    | 代表实体。                                          | Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference |
| 7        | ProcessingInstruction     | 代表处理指令。                                      | None                                                         |
| 8        | <mark>Comment</mark>      | 代表注释。                                          | None                                                         |
| 9        | <mark>Document</mark>     | 代表整个文档（DOM 树的根节点）。                    | Element, ProcessingInstruction, Comment, DocumentType        |
| 10       | <mark>DocumentType</mark> | 向为文档定义的实体提供接口                          | None                                                         |
| 11       | DocumentFragment          | 代表轻量级的 Document 对象，能够容纳文档的某个部分  | Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference |
| 12       | Notation                  | 代表 DTD 中声明的符号。                             | None                                                         |

```html
<!DOCTYPE html>
<html>
<body>

<h2 id="hh">JavaScript HTML DOM!</h2>

<p>Hello World!</p>

<p>Hello Norway!</p>

<p id="demo"></p>
<p id="demo1"></p>
<p id="demo2"></p>

<script>
var myNodelist = document.querySelectorAll("p");
var hh = document.getElementById("hh");

//获取ID这种指向性明确的节点直接使用firstChild，lastChild等直接获取子文本内容
document.getElementById("demo").innerHTML =
"The innerHTML of the second paragraph is: " +
hh.firstChild.nodeValue;

//当获取的是节点集合时，需要通过index获取某个节点后再通过firstChild，lastChild等直接获取子文本内容
document.getElementById("demo1").innerHTML =
"The innerHTML of the second paragraph is: " +
myNodelist[1].firstChild.nodeValue;

document.getElementById("demo2").innerHTML =
"The innerHTML of the second paragraph is: " +
myNodelist[1].firstChild.innerHTML;
</script>

</body>
</html>

```

### The nodeName Property

The `nodeName` property specifies the name of a node.

`childNodes[0].nodeValue`

- nodeName is read-only
- nodeName of an element node is the same as the tag name
- nodeName of an attribute node is the attribute name
- nodeName of a text node is always #text
- nodeName of the document node is always #document
- 如果是元素节点,`nodeName`属性和`tagName`属性返回相同的值,但如果是文本节点,`nodeName`属性会返回`"#text"`,而`tagName`属性会返回`undefined`.

```html
<!DOCTYPE html>
<html>
<body>

<p id="id01">My First Page</p>
<p id="id02"></p>

<script>
document.getElementById("id02").innerHTML = document.getElementById("id01").nodeName;
</script>

</body>
</html>

<!DOCTYPE html>
<html>
<body>

<p id="myP">Click the button to get the node name of this element.</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  var x = document.getElementById("myP").firstChild.nodeName;
  //var x = document.getElementById("myP").firstChild.nodeType;
	//var x = document.getElementById("myP").firstChild.nodeValue;
  document.getElementById("demo").innerHTML = x;
}
//output #text
</script>


</body>
</html>
```

### The nodeValue Property

The `nodeValue` property specifies the value of a node.

- nodeValue for element nodes is `null`

  元素节点的nodeValue返回null，因为需要通过`parentNode``childNodes[nodenumber]``firstChild``lastChild``nextSibling``previousSibling`这些方式去获取文本节点

- nodeValue for text nodes is the text itself

- nodeValue for attribute nodes is the attribute value

```html
<!DOCTYPE html>
<html>
<body>

<p>Click the button get the node name, node type and node value of the div's first child.</p>

<div id="myDIV">This is a div element and id is mayDIV.the first child node of div is textnode and its node type is 3</div>
<br>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  var x = document.getElementById("myDIV").firstChild;
  var txt = "";
  txt += "The node name: " + x.nodeName + "<br>";
  //#text
  txt += "The node value: " + x.nodeValue + "<br>";
  //This is a div element and id is mayDIV.the first child node of div is textnode and its node type is 3
  txt += "The node type: " + x.nodeType;
  //3
  document.getElementById("demo").innerHTML = txt;
}
  
  function myFunction2() {
  var x = document.getElementById("myDIV");
  var txt = "";
  txt += "The node name: " + x.nodeName + "<br>";
  //DIV
  txt += "The node value: " + x.nodeValue + "<br>";
  //null
  txt += "The node type: " + x.nodeType;
  //1
  document.getElementById("demo").innerHTML = txt;
}
</script>

</body>
</html>
```

## Navigating Between Nodes

You can use the following node properties to navigate between nodes with JavaScript:

- `parentNode`
- `childNodes[nodenumber]`
- `firstChild`
- `lastChild`
- `nextSibling`
- `previousSibling`
- previousElementSibling

```html
<!DOCTYPE html>
<html>
<body>

<h1 id="id01">My First Page</h1>
<p id="id02"></p>

<script>
document.getElementById("id02").innerHTML = document.getElementById("id01").firstChild.nodeValue;
//the same
//document.getElementById("id02").innerHTML = document.getElementById("id01").childNodes[0].nodeValue;
</script>

</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<body>


<h1 id="id01">My First Page1</h1>
<h3 id="id02">My First Page3</h3>

<!--div框起来的元素获取兄弟节点时候，不能越出div框外获取，因为那就不是兄弟节点了-->
<div>
<h1 id="id03">My First Page1</h1>
<h3 id="id04">My First Page3</h3>
</div>

<p id="id05"></p>
<p id="id06"></p>


<script>
document.getElementById("id05").innerHTML ="id05:"+ document.getElementById("id01").nextSibling.nextSibling.nextSibling.nextSibling.nodeName;

//output p

document.getElementById("id06").innerHTML ="id06:获取失败" + document.getElementById("id03").nextSibling.nextSibling.nextSibling.nextSibling.nodeName;

</script>

</body>
</html>

```

## Document 类型

| Attribute     | Value     |
| :------------ | :-------- |
| nodeType      | 9         |
| nodeName      | #document |
| nodeValue     | Null      |
| parentNode    | Null      |
| ownerDocument | Null      |

刚才说道 Document 是整个文档的根节点，我们想要访问某个节点的时候都必须通过 document 这个实例对象。

[文档的属性和方法](https://www.w3schools.com/jsref/dom_obj_document.asp)

- document 对象的常用属性：

```js
document.documentElement  // 可以直接拿到 html 节点的引用
document.title //  可以直接获取 title 节点的文本 “我是title”
document.URL // 获取 URL
document.domain
```

- document 对象的常用方法

```js
document.getElementById 
// docment.getElementById('myId') 可以获取到属性 id 为 ‘myId’ 的节点，在上面的代码中获取的也就是 p 节点
document.getElementsByTagName 
//docment.getElementByTagName('p') 可以获取到节点为 p 的所有节点集
document.getElementsByClassName
document.getElementsByName
document.querySelector()
document.querySelectorAll()
document.addEventListener()
document.removeEventListener()
document.write()
document.createElementAttribute()
document.createElement()
document.createEvent()
document.createTextNode()
```

- 现在我们就根据 document 对象中的方法获取到 HTML 中任意节点了，下面我们来介绍在已经拿到节点的基础上该如何对该节点进行操作。

## Element 类型

- 通常我们在使用 document 对象来获取节点时，返回的节点类型就是 Element 类型，所以我们想要对获取的节点进行操作，我们只需要使用 Element 包含的属性和方法即可。

- 常用的属性：

```js
var myNode = document.getElementById('myId');
myNode.id // 获取该节点的 id ，即 ‘myId‘
myNode.tagName // 获取该节点的节点名，即 'P'，大部分浏览器返回的标签名都是大写
myNode.className //获取该节点的 class
```

- 操作节点属性的常用方法：

```js
//假如我们有一个 input，我们想要获取 input 的 type 属性，并对 type 属性进行操作
<input type='text' id='input'/>

var myNode = document.getElementById('input')
myNode.getAttribute('type') // 获取属性值，即 ‘text’
myNode.setAttribute('type','password') // 将 type 属性值改为 password 类型
myNode.removeAttribute('type') // 移除 type 属性
```

![Xnip2021-05-07_22-56-41.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gqa997ci4oj31e00mijvm.jpg)

## Finding HTML Elements

| Method                                  | Description                   |
| :-------------------------------------- | :---------------------------- |
| document.getElementById(*id*)           | Find an element by element id |
| document.getElementsByTagName(*name*)   | Find elements by tag name     |
| document.getElementsByClassName(*name*) | Find elements by class name   |

------

## Changing HTML Elements

| Property                                   | Description                                   |
| :----------------------------------------- | :-------------------------------------------- |
| *element*.innerHTML = *new html content*   | Change the inner HTML of an element           |
| *element*.*attribute = new value*          | Change the attribute value of an HTML element |
| *element*.style.*property = new style*     | Change the style of an HTML element           |
| Method                                     | Description                                   |
| *element*.setAttribute*(attribute, value)* | Change the attribute value of an HTML element |

------

```html
<!DOCTYPE html>
<html>
<body>

<img id="myImage" src="smiley.gif">
<!--*element*.setAttribute*(attribute, value)*-->
<script>
document.getElementById("myImage").src = "landscape.jpg";
</script>

</body>
</html>
```

## Adding and Deleting Elements

| Method                             | Description                                                  |
| :--------------------------------- | :----------------------------------------------------------- |
| document.createElement(*element*)  | Create an HTML element,创建标签必须是document才有权限        |
| document.removeChild(*element*)    | Remove an HTML element                                       |
| document.appendChild(*element*)    | Add an HTML element                                          |
| document.replaceChild(*new, old*)  | Replace an HTML element                                      |
| document.write(*text*)             | Write into the HTML output stream                            |
| insertBefore(*target*,*reference*) | 如果第二个参数是null或者undefined，那么会默认执行appendChild |

```html
<!DOCTYPE html>
<html>
<body>

<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);
var element = document.getElementById("div1");
element.appendChild(para);
</script>

</body>
</html>
```

## Adding Events Handlers

| Method                                                      | Description                                                  |
| :---------------------------------------------------------- | :----------------------------------------------------------- |
| document.getElementById(*id*).onclick = function(){*code*}  | Adding event handler code to an onclick event                |
| `<div onclick="xxx"></div>`                                 | html 事件 添加 event,内联添加                                |
| oDiv.onclick=function(){}                                   | 外联文件添加事件函数                                         |
| 元素.addEventListener('不加on的事件名',函数名,是否事件下沉) | DOM2级事件，只兼容高级浏览器，真正工作中，还是有新出的高级事件都要用这种方法添加 |
| 元素.attachEvent('加on的事件名',函数名)                     | ie事件处理方式，兼容ie系列                                   |

```js
//浏览器兼容判断
function addEvent(obj, sEvent, fn) {
  if (obj.addEventListener) {
    obj.addEventListener(sEvent, fn, false);
  } else {
    obj.attactEvent("on" + sEvent, fn);
  }
}
```

## 一些 DOM 对象方法

| 方法                     | 描述                                                         |
| :----------------------- | :----------------------------------------------------------- |
| getElementById()         | 返回带有指定 ID 的元素。                                     |
| getElementsByTagName()   | 返回包含带有指定标签名称的所有元素的节点列表（集合/节点数组）。 |
| getElementsByClassName() | 返回包含带有指定类名的所有元素的节点列表。                   |
| appendChild()            | 把新的子节点添加到指定节点。                                 |
| removeChild()            | 删除子节点。                                                 |
| replaceChild()           | 替换子节点。                                                 |
| insertBefore()           | 在指定的子节点前面插入新的子节点。                           |
| createAttribute()        | 创建属性节点。                                               |
| createElement()          | 创建元素节点。                                               |
| createTextNode()         | 创建文本节点。                                               |
| getAttribute()           | 返回指定的属性值。                                           |
| setAttribute()           | 把指定属性设置或修改为指定的值。                             |
| cloneNode()(true)        | 克隆一个元素                                                 |

```html
<!DOCTYPE html>
<html>
<body>

<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
var child = document.getElementById("p1");
element.insertBefore(para,child);
</script>

</body>
</html>
```

```html
<!--The remove() method does not work in older browsers, see the example below on how to use removeChild() instead.-->

<div>
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
var elmnt = document.getElementById("p1");
elmnt.remove();
</script>


<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.removeChild(child);
</script>
```

```html
<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.replaceChild(para, child);
</script>
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div index="1">aaaaaaaaaaa</div>
  </body>
</html>
<script>
  // var oDiv=document.querySelector('div');
  // oDiv.setAttribute('web258','aaa')
  // oDiv.removeAttribute('web258')
  // alert(oDiv.getAttribute('index'))
  // alert(oDiv.getAttribute('web258'))

  var oDiv = document.querySelector("div");
  oDiv.setAttribute("web258", "aaa");
  //oDiv.removeAttribute('web258')
  console.log(oDiv.getAttribute("index"));
  console.log(oDiv.getAttribute("web258"));
</script>

```