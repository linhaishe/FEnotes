# DOM API

# 概述

简单来说，DOM 就是一个用于描述 HTML 页面结构的树形结构，程序员可以使用 DOM API 来读取或修改这个结构，以达到操作网页的目的。

文档对象模型（DOM）是一种平台和语言中立的接口，允许程序和脚本动态地访问和更新文档的内容、结构和样式。

DOM（文档对象模型，Document Object Model）是一种基于对象的编程接口，它将 web 页面和脚本语言（如 JavaScript）连接起来。它将 web 页面中的每个元素、属性、事件和文本内容都表示为对象，从而使开发人员能够通过编程方式操作和处理网页。

## What is the DOM?

The DOM is a W3C (World Wide Web Consortium) standard.

The DOM defines a standard for accessing documents:

*"The W3C Document Object Model (DOM) is a platform and language-neutral interface that allows programs and scripts to dynamically access and update the content, structure, and style of a document."*

文档对象模型（DOM）是一种平台和语言中立的接口，允许程序和脚本动态地访问和更新文档的内容、结构和样式。

## What is the HTML DOM?

The HTML DOM is a standard **object** model and **programming interface** for HTML. It defines:

HTML DOM 是 HTML 的标准对象模型和编程接口。

- The HTML elements as **objects**
- The **properties** of all HTML elements
- The **methods** to access all HTML elements
- The **events** for all HTML elements

In other words: **The HTML DOM is a standard for how to get, change, add, or delete HTML elements.**

When a web page is loaded, the browser creates a **D**ocument **O**bject **M**odel of the page.

The **HTML DOM** model is constructed as a tree of **Objects**:

![img](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/DOM/pic_htmltree.gif)

## 为什么使用

使用 DOM 的目的是让开发人员能够通过编程方式操作网页内容。这样可以实现许多功能，例如：

1. 动态改变网页的内容和样式，而不需要重新加载整个网页；

2. 在网页中添加、删除或修改元素、属性和事件处理程序，从而实现交互性；

3. 收集表单数据并发送到服务器；

4. 操作 cookies；

5. 实现 AJAX 功能，使用 JavaScript 向服务器请求数据并更新网页内容，而不需要重新加载整个网页。


| 接口名称              | 描述                                                         |
| --------------------- | ------------------------------------------------------------ |
| AbortController       | 用于中止DOM请求。 它允许通过将AbortController.signal传递给fetch()、XMLHttpRequest等API来取消网络请求。 |
| AbortSignal           | 用于在AbortController对象上发送取消信号。当调用AbortController.abort()时，所有已注册的AbortSignal处理函数将被调用。 |
| AbstractRange         | 抽象的范围，用于表示文档的一部分。它是其他具体范围类型的基础，例如Range和StaticRange。 |
| Attr                  | 表示元素的属性节点。                                         |
| CDATASection          | 用于表示XML文档中的CDATASECTION节点。这些节点是元素的一部分，但它们可以包含文本和实体引用等字符数据，这些数据不会被解释为标记。 |
| CharacterData         | 表示包含字符数据的节点，例如Text和Comment。                  |
| Comment               | 表示XML或HTML文档中的注释节点。                              |
| CustomEvent           | 表示开发者自定义的事件类型。                                 |
| ==Document==          | 表示整个HTML或XML文档。它是DOM树的根节点。                   |
| ==DocumentFragment==  | 用于表示文档的一部分，通常是一组节点。与Document不同，它没有属性和方法来表示文档级别信息，如标题和URL。 |
| DocumentType          | 表示XML或HTML文档类型声明的节点。它包含文档的名称、公共标识符和系统标识符等信息。 |
| DOMError              | 已弃用，表示在DOM操作期间发生错误的对象。                    |
| DOMException          | 表示在DOM操作期间发生错误的对象。                            |
| DOMImplementation     | 提供创建和操作DOM文档的方法。它是Document对象的工厂。        |
| DOMParser             | 用于解析XML或HTML文档并创建一个DOM文档对象。                 |
| DOMPoint              | 用于表示二维或三维坐标系中的点。                             |
| DOMPointReadOnly      | 与DOMPoint相同，但它是只读的。                               |
| DOMRect               | 用于表示在二维平面上定义的矩形。它通常用于元素的位置和大小计算。 |
| DOMTokenList          | 表示元素的类名属性的集合。它允许添加、删除和切换类名。       |
| ==Element==           | 表示HTML或XML文档中的元素节点。它包含元素的标记名称、属性和子元素等信息。 |
| ==Event==             | 表示事件的对象。它包含事件类型、目标元素、时间戳和其他与事件相关的信息。 |
| ==EventTarget==       | 定义了事件处理程序的通用接口，可以添加和删除事件监听器       |
| HTMLCollection        | 表示一个元素集合，是元素节点的有序列表                       |
| MutationObserver      | 监听 DOM 树中的更改并以异步方式进行通知                      |
| MutationRecord        | 描述 DOM 树中发生的单个更改的对象                            |
| NamedNodeMap          | 表示一个有名称的节点对象的集合                               |
| Node                  | 表示 DOM 中的单个节点                                        |
| NodeFilter            | 用于筛选要在 TreeWalker 或 NodeIterator 中遍历的节点的接口   |
| NodeIterator          | 用于遍历 DOM 树中的节点的接口                                |
| NodeList              | 表示一个无序的节点集合                                       |
| ProcessingInstruction | 描述处理指令节点的接口                                       |
| Range                 | 表示文档中的一个连续范围                                     |
| StaticRange           | 表示 DOM 中的一段不可变范围                                  |
| Text                  | 表示 DOM 中的文本内容                                        |
| TextDecoder           | 将字节序列解码为字符串的接口                                 |
| TextEncoder           | 将字符串编码为字节序列的接口                                 |
| TimeRanges            | 表示音频或视频元素的时间范围                                 |
| TreeWalker            | 用于遍历 DOM 树中的节点的接口                                |
| XMLDocument           | 表示一个 XML 文档                                            |

## 重要的数据类型

下面的表格简单则描述了这些数据类型。

| Data type (Interface) | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `document`            | 当一个成员返回 `document` 对象（例如，元素的 `**ownerDocument**` 属性返回它所属于 `document` ) ，这个对象就是 root `document` 对象本身。 [DOM `document` Reference](https://developer.mozilla.org/zh-CN/docs/Web/API/Document) 一章对 `document` 对象进行了描述。 |
| `element`             | `element` 是指由 DOM API 中成员返回的类型为 `element` 的一个元素或节点。例如， [document.createElement()](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createElement) 方法会返回一个 `node` 的对象引用，也就是说这个方法返回了在 DOM 中创建的 `element`。 `element` 对象实现了 DOM `Element` 接口以及更基本的 `Node` 接口，参考文档将两者都包含在内。 |
| `nodeList`            | `nodeList` 是一个元素的数组，如从 [document.getElementsByTagName()](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementsByTagName) 方法返回的就是这种类型。 `nodeList` 中的条目由通过下标有两种方式进行访问：list.item(1)list[1]两种方式是等价的，第一种方式中 **`item()`** 是 `nodeList` 对象中的单独方法。 后面的方式则使用了经典的数组语法来获取列表中的第二个条目。 |
| `attribute`           | 当 `attribute` 通过成员函数 (例如，通过 **`createAttribute()`**方法) 返回时，它是一个为属性暴露出专门接口的对象引用。DOM 中的属性也是节点，就像元素一样，只不过您可能会很少使用它。 |
| `namedNodeMap`        | `namedNodeMap` 和数组类似，但是条目是由 name 或 index 访问的，虽然后一种方式仅仅是为了枚举方便，因为在 list 中本来就没有特定的顺序。出于这个目的， `namedNodeMap` 有一个 item() 方法，你也可以从 `namedNodeMap` 添加或移除条目。 |
| `Node`                | Every object located within a document is a node of some kind. In an HTML document, an object can be an element node but also a text node or attribute node. |



Refs:

1. https://www.w3schools.com/js/js_htmldom.asp
2. https://www.w3.org/TR/DOM-Level-2-Events/events.html
3. https://en.wikipedia.org/wiki/DOM_events

# DOM Document

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

## Adding and Deleting Elements

| Method                            | Description                       |
| :-------------------------------- | :-------------------------------- |
| document.createElement(*element*) | Create an HTML element            |
| document.removeChild(*element*)   | Remove an HTML element            |
| document.appendChild(*element*)   | Add an HTML element               |
| document.replaceChild(*new, old*) | Replace an HTML element           |
| document.write(*text*)            | Write into the HTML output stream |

------

## Adding Events Handlers

| Method                                                     | Description                                   |
| :--------------------------------------------------------- | :-------------------------------------------- |
| document.getElementById(*id*).onclick = function(){*code*} | Adding event handler code to an onclick event |

------

## Finding HTML Objects

The first HTML DOM Level 1 (1998), defined 11 HTML objects, object collections, and properties. These are still valid in HTML5.

Later, in HTML DOM Level 3, more objects, collections, and properties were added.

| Property                     | Description                                                  | DOM  |
| :--------------------------- | :----------------------------------------------------------- | :--- |
| document.anchors             | Returns all <a> elements that have a name attribute          | 1    |
| document.applets             | Deprecated                                                   | 1    |
| document.baseURI             | Returns the absolute base URI of the document                | 3    |
| document.body                | Returns the <body> element                                   | 1    |
| document.cookie              | Returns the document's cookie                                | 1    |
| document.doctype             | Returns the document's doctype                               | 3    |
| document.documentElement     | Returns the <html> element                                   | 3    |
| document.documentMode        | Returns the mode used by the browser                         | 3    |
| document.documentURI         | Returns the URI of the document                              | 3    |
| document.domain              | Returns the domain name of the document server               | 1    |
| document.domConfig           | Obsolete.                                                    | 3    |
| document.embeds              | Returns all <embed> elements                                 | 3    |
| document.forms               | Returns all <form> elements                                  | 1    |
| document.head                | Returns the <head> element                                   | 3    |
| document.images              | Returns all <img> elements                                   | 1    |
| document.implementation      | Returns the DOM implementation                               | 3    |
| document.inputEncoding       | Returns the document's encoding (character set)              | 3    |
| document.lastModified        | Returns the date and time the document was updated           | 3    |
| document.links               | Returns all <area> and <a> elements that have a href attribute | 1    |
| document.readyState          | Returns the (loading) status of the document                 | 3    |
| document.referrer            | Returns the URI of the referrer (the linking document)       | 1    |
| document.scripts             | Returns all <script> elements                                | 3    |
| document.strictErrorChecking | Returns if error checking is enforced                        | 3    |
| document.title               | Returns the <title> element                                  | 1    |
| document.URL                 | Returns the complete URL of the document                     | 1    |

# DOM Elements

| Finding Method                         |                                             |
| -------------------------------------- | ------------------------------------------- |
| Finding HTML Element by Id             | `document.getElementById("intro");`         |
| Finding HTML Elements by Tag Nam       | ` document.getElementsByTagName("p");`      |
| Finding HTML Elements by Class Name    | `document.getElementsByClassName("intro");` |
| Finding HTML Elements by CSS Selectors | `document.querySelectorAll("p.intro");`     |

## DocumentFragment

The createDocumentFragment() method creates an offscreen node.

The offscreen node can be used to build a new document fragment that can be insert into any document.

The createDocumentFragment() method can also be used to extract parts of a document, change, add, or delete some of the content, and insert it back to the document.

```html
<ul id="myList">
</ul>

<script>
const fruits = ["Banana", "Orange", "Mango"];

// Create a document fragment:
const dFrag = document.createDocumentFragment();
for (let x in fruits) {
  const li = document.createElement('li');
  li.textContent = fruits[x];
  dFrag.appendChild(li);
}

// Add fragment to a list: 
document.getElementById('myList').appendChild(dFrag);
</script>
```

# DOM HTML

| Event                              | Method                                                | Explain                                                      |
| ---------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| Changing HTML Content              | document.getElementById(*id*).innerHTML = *new HTML*  |                                                              |
| Changing the Value of an Attribute | document.getElementById(*id*).*attribute = new value* | document.getElementById("myImage").src = "landscape.jpg";    |
| document.write()                   | document.write(Date());                               | Never use `document.write()` after the document is loaded. It will overwrite the document. |

# DOM CSS

| Event               | Method                                                       | Explain                                             |
| ------------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| Changing HTML Style | document.getElementById(*id*).style.*property* = *new style* | document.getElementById("p2").style.color = "blue"; |

# DOM Events

For a list of all HTML DOM events, look at our complete [HTML DOM Event Object Reference](https://www.w3schools.com/jsref/dom_obj_event.asp).

| Event               | Method                                                       |
| ------------------- | ------------------------------------------------------------ |
| In HTML onclick     | `<button onclick="myFunction()">Click me</button>`<br />`document.getElementById("myBtn").onclick = displayDate;` |
| In JavaScript click | `button.addEventListener("click", myFunction);`              |

# DOM EventListener

The `addEventListener()` method attaches an event handler to the specified element.

`element.addEventListener("click", myFunction);`

1. The `addEventListener()` method attaches an event handler to the specified element.

2. The `addEventListener()` method attaches an event handler to an element without overwriting existing event handlers.

3. You can add many event handlers to one element.

4. You can add many event handlers of the same type to one element, i.e two "click" events.

5. You can add event listeners to any DOM object not only HTML elements. i.e the window object.

6. The `addEventListener()` method makes it easier to control how the event reacts to bubbling.

7. When using the `addEventListener()` method, the JavaScript is separated from the HTML markup, for better readability and allows you to add event listeners even when you do not control the HTML markup.

   `addEventListener()` 方法可以用于将事件监听器附加到指定的 HTML 元素上，以响应特定的事件。与传统的 HTML 属性事件相比，使用`addEventListener()` 方法可以将 JavaScript 代码与 HTML 标记分离，从而提高代码可读性并支持更好的代码重用和维护性。

   使用 `addEventListener()` 方法，可以在不控制 HTML 标记的情况下，将事件监听器添加到 HTML 元素上。这是因为在使用` addEventListener()` 方法时，只需要知道要绑定事件的元素对象和事件类型，而不需要修改 HTML 标记中的代码。这也使得更多的开发者可以共同维护代码，因为他们不需要了解 HTML 页面的具体细节，只需要关注事件监听器的具体实现即可。

8. You can easily remove an event listener by using the `removeEventListener()` method.

## Event Bubbling or Event Capturing?

There are two ways of event propagation in the HTML DOM, bubbling and capturing.

Event propagation is a way of defining the element order when an event occurs. If you have a` <p>` element inside a` <div>` element, and the user clicks on the` <p>` element, which element's "click" event should be handled first?

In *bubbling* the inner most element's event is handled first and then the outer: the` <p> `element's click event is handled first, then the` <div>` element's click event.

In *capturing* the outer most element's event is handled first and then the inner: the` <div> `element's click event will be handled first, then the` <p>` element's click event.

With the addEventListener() method you can specify the propagation type by using the "useCapture" parameter:

`addEventListener(*event*, *function*, *useCapture*);`

The default value is false, which will use the bubbling propagation, when the value is set to true, the event uses the capturing propagation.

`document.getElementById("myP").addEventListener("click", myFunction, true);`

# DOM Navigation

With the HTML DOM, you can navigate the node tree using node relationships.（使用节点关系遍历节点树）

## DOM Nodes

According to the W3C HTML DOM standard, everything in an HTML document is a node:

- The entire document is a document node
- Every HTML element is an element node
- The text inside HTML elements are text nodes
- Every HTML attribute is an attribute node (deprecated)
- All comments are comment nodes

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/DOM/image-20230409235607538.png" alt="image-20230409235607538" style="zoom: 50%;" />

With the HTML DOM, all nodes in the node tree can be accessed by JavaScript.

New nodes can be created, and all nodes can be modified or deleted.

## Node Relationships

The nodes in the node tree have a hierarchical relationship to each other.

The terms parent, child, and sibling are used to describe the relationships.

- In a node tree, the top node is called the root (or root node)
- Every node has exactly one parent, except the root (which has no parent)
- A node can have a number of children
- Siblings (brothers or sisters) are nodes with the same parent

![image-20230409235954273](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/DOM/image-20230409235954273.png)

## node properties

- `parentNode`
- `childNodes[*nodenumber*]`
- `firstChild`
- `lastChild`
- `nextSibling`
- `previousSibling`

Accessing the innerHTML property is the same as accessing the `nodeValue` of the first child:

`myTitle = document.getElementById("demo").firstChild.nodeValue;`

```html
<html>
<body>

<h1 id="id01">My First Page</h1>
<p id="id02"></p>

<script>
document.getElementById("id02").innerHTML = document.getElementById("id01").firstChild.nodeValue;
</script>

</body>
</html>
```

## DOM Root Nodes

There are two special properties that allow access to the full document:

- `document.body` - The body of the document
- `document.documentElement` - The full document

## The nodeName Property

The `nodeName` property specifies the name of a node.

- nodeName is read-only
- nodeName of an element node is the same as the tag name
- nodeName of an attribute node is the attribute name
- nodeName of a text node is always #text
- nodeName of the document node is always #document

## The nodeValue Property

The `nodeValue` property specifies the value of a node.

- nodeValue for element nodes is `null`
- nodeValue for text nodes is the text itself
- nodeValue for attribute nodes is the attribute value

## The nodeType Property

The `nodeType` property is read only. It returns the type of a node.

```html
<h1 id="id01">My First Page</h1>
<p id="id02"></p>

<script>
document.getElementById("id02").innerHTML = document.getElementById("id01").nodeType;
</script>
```

| Node               | Type | Example                                         |
| :----------------- | :--- | :---------------------------------------------- |
| ELEMENT_NODE       | 1    | `<h1 class="heading">W3Schools</h1>`            |
| ATTRIBUTE_NODE     | 2    | class = "heading" (deprecated)                  |
| TEXT_NODE          | 3    | W3Schools                                       |
| COMMENT_NODE       | 8    | `<!-- This is a comment -->`                    |
| DOCUMENT_NODE      | 9    | The HTML document itself (the parent of <html>) |
| DOCUMENT_TYPE_NODE | 10   | `<!Doctype html>`                               |

# DOM Elements (Nodes)

就是通过node去添加元素拉

## Creating New HTML Elements (Nodes)

```HTML
<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
const para = document.createElement("p");
const node = document.createTextNode("This is new.");
para.appendChild(node);

const element = document.getElementById("div1");
element.appendChild(para);
</script>
```

## Creating new HTML Elements - insertBefore()

The `appendChild()` method in the previous example, appended the new element as the last child of the parent.

If you don't want that you can use the `insertBefore()` method:

```html
<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
const para = document.createElement("p");
const node = document.createTextNode("This is new.");
para.appendChild(node);

const element = document.getElementById("div1");
const child = document.getElementById("p1");
element.insertBefore(para, child);
</script>
```

## Removing Existing HTML Elements

```html
<div>
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
const elmnt = document.getElementById("p1"); elmnt.remove();
</script>
```

The `remove()` method does not work in older browsers, see the example below on how to use `removeChild()` instead.

## Removing a Child Node

```html
<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
const parent = document.getElementById("div1");
const child = document.getElementById("p1");
parent.removeChild(child);
</script>
```

## Replacing HTML Elements 

```html
<div id="div1">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
</div>

<script>
const para = document.createElement("p");
const node = document.createTextNode("This is new.");
para.appendChild(node);

const parent = document.getElementById("div1");
const child = document.getElementById("p1");
parent.replaceChild(para, child);
</script>
```

# 安全性和性能

## DOM 操作的安全性和性能问题是什么？

1. 安全性问题：DOM 操作的安全性问题包括跨站脚本攻击（XSS）和跨站请求伪造（CSRF）。
   1. XSS 攻击是指攻击者将恶意脚本注入到页面中，从而获取用户的敏感信息或执行其他恶意行为。
   2. CSRF 攻击则是利用用户在已登录的情况下访问一个恶意站点，从而在用户不知情的情况下完成某个操作。
   3. 在使用DOM API操作页面元素时，需要注意安全性问题，例如使用innerHTML属性插入未经转义的用户输入内容可能导致XSS攻击；使用eval()函数解析文本字符串也可能存在安全风险。
2. 性能问题：DOM操作可能导致性能问题，因为访问和操作DOM树是非常消耗资源的。频繁的DOM操作会导致页面重排和重绘，这会严重影响页面的性能。所以，应该尽量避免频繁的DOM操作，可以使用文档片段等技术批量操作DOM元素，减少DOM操作次数，提高性能。
3. 内存泄漏问题：在JavaScript中操作DOM元素时，需要注意内存泄漏问题。如果在DOM元素被移除之前没有正确地释放引用，那么这些DOM元素会一直保存在内存中，导致内存泄漏。所以，当不再需要DOM元素时，需要将其从DOM树中移除，并及时释放对它的引用。

## 如何使用 DOM API 最大限度地提高性能和安全性？

1. 避免频繁地使用DOM API：DOM操作可以很昂贵，因此应该尽可能地减少对DOM的操作。对于一些频繁变化的 DOM 元素，可以使用 CSS3 动画和变换代替频繁的 DOM 操作，从而提高性能。例如，可以使用文档片段来一次性将多个元素添加到文档中，而不是一次添加一个元素。
2. 缓存DOM查询的结果：如果您需要多次使用相同的DOM查询结果，请将查询结果缓存到变量中，而不是每次重新查询。
3. 使用事件委托：当需要为多个元素添加相同的事件监听器时，可以将事件监听器添加到它们的共同祖先元素上，并使用事件委托来捕获事件。
4. 避免使用全局选择器：全局选择器（如`document.querySelector`）需要遍历整个文档树，因此对性能有影响。如果可能，尽量使用更具体的选择器，或者将选择器与上下文参数一起使用。
5. 使用合适的API：DOM API中有很多种方法可以实现相同的任务。某些API比其他API更高效，因此应该使用最合适的API来提高性能。
6. 防止DOM注入攻击：当从用户输入或第三方源动态生成内容时，要小心防止DOM注入攻击。可以使用浏览器提供的内置安全特性，例如将HTML转义为纯文本，或使用安全的DOM API。
7. 最小化DOM更改：DOM更改可能导致重排和重绘，从而降低性能。尽可能最小化DOM更改，例如使用CSS3的变换和过渡来实现动画效果，而不是使用JavaScript直接更改元素的样式。
8. 避免直接操作 HTML 字符串，尤其是从未经过过滤的用户输入创建 HTML 时更要小心，而是使用 DOM API 中提供的方法。
9. 使用安全的事件处理方法，如使用 addEventListener() 方法代替 on* 属性。

攻击者注入恶意代码的方式可以有多种途径，以下是一些常见的攻击方式：

1. 通过跨站脚本（XSS）攻击：攻击者可以在一个网站上注入 JavaScript 代码，该代码会被传递给其他用户的浏览器并在其上下文中执行。
2. 通过第三方依赖库：攻击者可以在第三方依赖库中注入恶意代码，然后该库被其他网站使用，从而使攻击者能够在这些网站上执行任意代码。
3. 通过浏览器漏洞：攻击者可以利用浏览器中的漏洞来注入代码，这通常需要针对特定浏览器版本的已知漏洞。
4. 通过恶意广告：攻击者可以在广告中注入代码，当用户访问带有该广告的网站时，代码会被执行。