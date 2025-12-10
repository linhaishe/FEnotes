# 1. What is jQuery?

jQuery is a lightweight, "write less, do more", JavaScript library.

The jQuery library contains the following features:

- HTML/DOM manipulation
- CSS manipulation
- HTML event methods
- Effects and animations
- AJAX
- Utilities

<mark>尽可能将获取的节点声明成变量，减少代码对dom的操作</mark>

# 2. Adding jQuery

## a. download

There are two versions of jQuery available for downloading:

- Production version - this is for your live website because it has been minified and compressed
- Development version - this is for testing and development (uncompressed and readable code)

Both versions can be downloaded from [jQuery.com](http://jquery.com/download/).

```html
<head>
<script src="jquery-3.5.1.min.js"></script>
</head>
```

## b. CDN

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js">
  //2021 05 18
</script>
```

# 3. jQuery Syntax

`Basic syntax is: $(\selector\).\action\( )`

`$(this).hide( )` - hides the current element.

`$("p").hide( )` - hides all `<p>` elements.

`$(".test").hide( )` - hides all elements with class="test".

`$("#test").hide( )` - hides the element with id="test".

## $( ).ready( ){}

This is to prevent any jQuery code from running before the document is finished loading (is ready).

阻止所有JQ代码不在网页完成加载时运行。

```js
$(document).ready(function( ){
  // jQuery methods go here...
});

//当初始的 HTML 文档被完全加载和解析完成之后，DOMContentLoaded 事件被触发，而无需等待样式表、图像和子框架的完全加载。
window.onload = function () {
  alert("onload");
};

document.addEventListener("DOMContentLoaded", function () {
  console.log($("div"));
});
```

# 4. jQuery Selectors

- element Selector

`$("p")`

- #id Selector

`$("#test")`

- .class Selector

`$(".test")`

[More Examples of jQuery Selectors](https://www.w3schools.com/jquery/jquery_selectors.asp)

[jQuery Selector Tester ](https://www.w3schools.com/jquery/trysel.asp)

# 5. jQuery Events

In jQuery, most DOM events have an equivalent jQuery method.

```js
$("p").click(function( ){
  $(this).hide( );
});
```

## Commonly Used jQuery Event Methods

- click( )
- dblclick( )
- mouseenter( )
- mouseleave( )
- mousedown( )
- mousemove()
- mouseup( )
- hover( )
- focus( )
- blur( )

```js
$("div").mousedown(function(){
  $(this).after("Mouse button pressed down.");
});
```

<mark>The on( ) Method</mark>

可以绑定多个事件处理程序

`$(selector).on(event,[childSelector],[data],function,[map])`

The on( ) method attaches one or more event handlers for the selected elements.

```js
$(document).ready(function(){
  $("p").on("mouseover mouseout", function(){
    $(this).toggleClass("intro");
  });
});
```



```js
$("p").on("click", function(){
  alert("The paragraph was clicked.");
});

//移除绑定事件
  $("button").click(function(){
    $("p").off("click");
  });
```

```js
$("p").on({
  mouseenter: function( ){
    $(this).css("background-color", "lightgray");
  },
  mouseleave: function( ){
    $(this).css("background-color", "lightblue");
  },
  click: function( ){
    $(this).css("background-color", "yellow");
  }
});
```

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("div").on("click", "p", function(){
    $(this).slideToggle();
  });
  $("button").click(function(){
    $("<p>This is a new paragraph.</p>").insertAfter("button");
  });
});
</script>
</head>
<body>

<div style="background-color:yellow">
  <p>This is a paragraph.</p>
  <p>Click any p element to make it disappear. Including this one.</p>
  <button>Insert a new p element after this button</button>
</div>

</body>
</html>

```



- hide( ),show( ),toggle( )

  speed values: "slow", "fast", or milliseconds.

```js
$(selector).hide(speed,callback);

$(selector).show(speed,callback);

$(selector).toggle(speed,callback);
```

- `fadeIn( )`, `fadeOut( )`, `fadeToggle( )`, `fadeTo( )`

```js
$("button").click(function(){
  $("#div1").fadeIn();
  $("#div2").fadeIn("slow");
  $("#div3").fadeIn(3000);
});
```
<mark>其区别</mark>

1. `fadeIn( )`,` fadeOut( )`, `fadeToggle( )`

`$(selector).fadeIn(speed,callback);`

The optional speed parameter specifies the duration of the effect. It can take the following values: "slow", "fast", or milliseconds.

2. fadeTo( )

`$(selector).fadeTo(speed,opacity,callback);`

The jQuery `fadeTo()` method allows fading to a given opacity (value between 0 and 1).

```js
$("button").click(function(){
  $("#div1").fadeTo("slow", 0.15);
  $("#div2").fadeTo("slow", 0.4);
  $("#div3").fadeTo("slow", 0.7);
});
```

- `slideDown()`,`slideUp()`,`slideToggle()`

`$(selector).slideToggle(speed,callback);`

- animate( )

`$(selector).animate({params},speed,callback);`

1. 使用动画方法里的特定属性，实现元素的移动，show,hide,toggle

You can even specify a property's animation value as "`show`", "`hide`", or "`toggle`":

```js
$("button").click(function(){
  $("div").animate({
    height: 'toggle'
  });
}); 
```

2. 在params里一次性写完要变化的属性后，可以一次性修改并展现，并有过渡效果
3. Queue Functionality 属性分开写会有连续的效果，一个一个展现修改的效果

```js
$("button").click(function(){
  var div = $("div");
  div.animate({height: '300px', opacity: '0.4'}, "slow");
  div.animate({width: '300px', opacity: '0.8'}, "slow");
  div.animate({height: '100px', opacity: '0.4'}, "slow");
  div.animate({width: '100px', opacity: '0.8'}, "slow");
}); 
```

- stop( )

`$(selector).stop(stopAll,goToEnd);`

[stop animation](https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_stop_params)

```js
//stop sliding
$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideDown(5000);
  });
  $("#stop").click(function(){
    $("#panel").stop();
  });
});
```

# Callback Functions

js 声明时是一行一行运行，但是会有副作用，在第一行效果没有完成的时候，下一行的函数也会继续运行，容易产生错误。所以在使用效果的时候，用callback的方法，使动画效果函数运行完成后再调用下一行函数。

The example below has a callback parameter that is a function that will be executed after the hide effect is completed:

```js
$("button").click(function(){
  $("p").hide("slow", function(){
    alert("The paragraph is now hidden");
  });
});
```

```js
//without callback
$("button").click(function(){
  $("p").hide(1000);
  alert("The paragraph is now hidden");
});
```
# Method Chaining

Tip: This way, browsers do not have to find the same element(s) more than once.

The following example chains together the `css()`, `slideUp()`, and `slideDown()` methods. The "p1" element first changes to red, then it slides up, and then it slides down:

`$("#p1").css("color", "red").slideUp(2000).slideDown(2000);`

```js
$("#p1").css("color", "red")
  .slideUp(2000)
  .slideDown(2000);
```

# 6. jQuery DOM

## 1. get / set

### Get Content - text(), html(), and val()

```js
//返回所选节点的text文本，html文本，value值

$("#btn1").click(function(){
  alert("Text: " + $("#test").text());
});
$("#btn2").click(function(){
  alert("HTML: " + $("#test").html());
});
```

### Get Attributes - attr()

```js
$("button").click(function(){
  alert($("#w3s").attr("href"));
});
```

### Set Content - text(), html(), and val()

```js
$("#btn1").click(function(){
  $("#test1").text("Hello world!");
});
$("#btn2").click(function(){
  $("#test2").html("<b>Hello world!</b>");
});
$("#btn3").click(function(){
  $("#test3").val("Dolly Duck");
});
```

### Set Attributes - attr()

```js
//单个操作
$("button").click(function(){
  $("#w3s").attr("href", "https://www.w3schools.com/jquery/");
});
```

```js
//批量操作
$("button").click(function(){
  $("#w3s").attr({
    "href" : "https://www.w3schools.com/jquery/",
    "title" : "W3Schools jQuery Tutorial"
  });
});
```

### A Callback Function for attr()

two parameters: 

- the index of the current element in the list of elements selected,所选元素的下标
- the original (old) attribute value. 

```js
$("button").click(function(){
  $("#w3s").attr("href", function(i, origValue){
    return origValue + "/jquery/";
  });
});
```

### A Callback Function for text(), html(), and val()

 two parameters:

- the index of the current element in the list of elements selected 
- the original (old) value. 

```js
$("#btn1").click(function(){
  $("#test1").text(function(i, origText){
    return "Old text: " + origText + " New text: Hello world!
    (index: " + i + ")";
  });
});

$("#btn2").click(function(){
  $("#test2").html(function(i, origText){
    return "Old html: " + origText + " New html: Hello <b>world!</b>
    (index: " + i + ")";
  });
});

//(index: 0)
```

## 2. add

### `append()`,`prepend()`,`after()`,`before()`

- `append()` - Inserts content at the end of the selected elements
- `prepend()` - Inserts content at the beginning of the selected elements
- `after()` - Inserts content after the selected elements
- `before()` - Inserts content before the selected elements
- `appendTo()` - 子级.appendTo(父级)
- `prepend()` - 子级.prependTo(父级)
- `insertAfter()`
- `insertBefore()`

```js
$(document).ready(function(){
  $("#btn1").click(function(){
    $("p").prepend("<b>Prepended text</b>. ");
  });
  $("#btn2").click(function(){
    $("ol").prepend("<li>Prepended item</li>");
  });
});
```

### Add Several New Elements With append() and prepend()

```js
function appendText() {
  var txt1 = "<p>Text.</p>";               // Create element with HTML 
  var txt2 = $("<p></p>").text("Text.");   // Create with jQuery
  var txt3 = document.createElement("p");  // Create with DOM
  txt3.innerHTML = "Text.";
  $("body").append(txt1, txt2, txt3);      // Append the new elements
}
```

The jQuery `after()` method inserts content AFTER the selected HTML elements.

The jQuery `before()` method inserts content BEFORE the selected HTML elements.

```js
$(document).ready(function(){
  $("#btn1").click(function(){
    $("img").before("<b>Before</b>");
  });

  $("#btn2").click(function(){
    $("img").after("<i>After</i>");
  });
});
```

```js
function afterText() {
  var txt1 = "<b>I </b>";                    // Create element with HTML 
  var txt2 = $("<i></i>").text("love ");     // Create with jQuery
  var txt3 = document.createElement("b");    // Create with DOM
  txt3.innerHTML = "jQuery!";
  $("img").after(txt1, txt2, txt3);          // Insert new elements after <img>
}
```

## 3. Remove Elements

### remove(),empty()

- `remove()` - Removes the selected element (and its child elements)

  删除所选节点，包括其子节点

  ```js
  $("#div1").remove();
  ```

- `empty()` - Removes the child elements from the selected element

  删除子节点，父节点不删除
  
  ```js
  $("#div1").empty();
  ```

添加参数，Jq可以遍历所选节点，删除特定的节点

`$("p").remove(".test, .demo");`

[Filter the Elements to be Removed](https://www.w3schools.com/jquery/jquery_dom_remove.asp)

## 4. Get and Set CSS Classes

### addClass,removeClass,toggleClass,css

- `addClass()` - Adds one or more classes to the selected elements

- `removeClass()` - Removes one or more classes from the selected elements

- `toggleClass()` - Toggles between adding/removing classes from the selected elements

- `css()` - Sets or returns the style attribute

  - Return a CSS Property

  `css("propertyname");`
  
  - Set a CSS Property
  
  `css("propertyname","value");`
  
  `css({"propertyname":"value","propertyname":"value",...});`

```js
$("button").click(function(){
  $("h1, h2, p").addClass("blue");
  $("div").addClass("important");
});

//添加多个标签
$("button").click(function(){
  $("#div1").addClass("important blue");
});
```

```js
$("p").css({"background-color": "yellow", "font-size": "200%"});
```

## 5. jQuery Dimension

![dimension](https://www.w3schools.com/jquery/img_jquerydim.gif)

```js
$("button").click(function(){
  $("#div1").width(500).height(500);
});
```

## 6. position

### `offset([coordinates])`,`position()`,`scrollTop([val])`,`scrollLeft([val])`

- offset([coordinates]) - method set or returns the offset coordinates for the selected elements, relative to the document.
- position() - method returns the position (relative to its parent element) of the first matched element.
- scrollTop([val]) - sets or returns the vertical scrollbar position for the selected elements.
- scrollLeft([val]) - method sets or returns the horizontal scrollbar position for the selected elements.

Return the offset coordinates:

`$(selector).offset()`

`$(selector).scrollLeft()`

Set the offset coordinates:

`$(selector).offset({top:value,left:value})`

`$(selector).scrollLeft(position)`

```js
$("button").click(function(){
  var x = $("p").offset();
  alert("Top: " + x.top + " Left: " + x.left);
});
```

```js
$("button").click(function(){
  var x = $("p").position();
  alert("Top: " + x.top + " Left: " + x.left);
});
```



# 7. jQuery Traversing DOM



![DOM tree](https://www.w3schools.com/jquery/img_travtree.png)



- the <div> element is the parent of <ul>, and an ancestor of everything inside of it
- The <ul> element is the parent of both <li> elements, and a child of <div>
- The left <li> element is the parent of <span>, child of <ul> and a descendant of <div>
- The <span> element is a child of the left <li> and a descendant of <ul> and <div>
- The two <li> elements are siblings (they share the same parent)
- The right <li> element is the parent of <b>, child of <ul> and a descendant of <div>
- The <b> element is a child of the right <li> and a descendant of <ul> and <div>

An ancestor is a parent, grandparent, great-grandparent, and so on.
A descendant is a child, grandchild, great-grandchild, and so on.
Siblings share the same parent.

### 1. Ancestors
#### `parent()`,`parents()`,`parentsUntil()`


- `parent()` - method returns the direct parent element of the selected element.
- `parents()` - method returns all ancestor elements of the selected element, all the way up to the document's root element (`<html>`).
- `parentsUntil()` - method returns all ancestor elements between two given arguments.

```js
//parents中可以添加参数，去获得制定的父级元素，如此获得为ul的父级元素
$(document).ready(function(){
  $("span").parents("ul");
});
```

```js
//不包含div,获得直到div的父级
$(document).ready(function(){
  $("span").parentsUntil("div");
});
```

### 2. Descendants

#### `children()`,`find()`

- `children()` - method returns all direct children of the selected element.选取所有直接子级
- `find()` - method returns descendant elements of the selected element, all the way down to the last descendant.

```js
$(document).ready(function(){
  $("div").children("p.first");
});
```

```js
//The following example returns all <span> elements that are descendants of <div>:
$(document).ready(function(){
  $("div").find("span");
});
//The following example returns all descendants of <div>
$(document).ready(function(){
  $("div").find("");
});
```

### Siblings

#### `siblings()`,`next()`,`nextAll()`,`nextUntil()`

- `siblings()` - method returns all sibling elements of the selected element.
- `next()` - method returns the next sibling element of the selected element.只返回一个兄弟节点
- `nextAll()` - method returns all next sibling elements of the selected element
- `nextUntil()` - method returns all next sibling elements between two given arguments.

和以上next相反。

- `prev()`
- `prevAll()`
- `prevUntil()`

```js
//The following example returns all sibling elements of <h2> that are <p> elements:

$(document).ready(function(){
  $("h2").siblings("p");
});
//returns all sibling elements between a <h2> and a <h6> element，不包括h2和h6
$(document).ready(function(){
  $("h2").nextUntil("h6");
});

```

### Filtering

#### first(), last(), eq(), filter() and not()

- `first()` - method returns the first element of the specified elements.返回整个页面里的第一个指定元素，无关兄弟父母节点

- `last()` - method returns the last element of the specified elements.

- `eq()` - method returns an element with a specific index number of the selected elements.

  The index numbers start at 0, so the first element will have the index number 0 and not 1. 

- `filter()`

- `not()`

```js
$(document).ready(function(){
  $("div").last();
});

//returns all <p> elements with class name "intro":
$(document).ready(function(){
  $("p").filter(".intro");
});

$(document).ready(function(){
  $("p").eq(1);
});

// returns all <p> elements that do not have class name "intro":
$(document).ready(function(){
  $("p").not(".intro");
});
```

# 8. jQuery AJAX

In short; AJAX is about loading data in the background and display it on the webpage, without reloading the whole page.

With the jQuery AJAX methods, you can request text, HTML, XML, or JSON from a remote server using both HTTP Get and HTTP Post - And you can load the external data directly into the selected HTML elements of your web page!

## load()

`load()` method loads data from a server and puts the returned data into the selected element.

[Example](https://www.w3schools.com/jquery/jquery_ajax_load.asp)

`$(selector).load(URL,[data],[callback]);`

- Url : specifies the URL you wish to load
- data : specifies a set of querystring key/value pairs to send along with the request.
- the name of a function to be executed after the `load()` method is completed.

```html
<h2>jQuery and AJAX is FUN!!!</h2>
<p id="p1">This is some text in a paragraph.</p>
```

```js
$("#div1").load("demo_test.txt");
//output : jQuery and AJAX is FUN!!!
//output : his is some text in a paragraph.

$("#div1").load("demo_test.txt #p1");
//output : This is some text in a paragraph.
```

### Callback function

The callback function can have different parameters:

- `responseTxt` - contains the resulting content if the call succeeds
- `statusTxt` - contains the status of the call
- `xhr` - contains the XMLHttpRequest object

```js
$("button").click(function(){
  $("#div1").load("demo_test.txt", function(responseTxt, statusTxt, xhr){
    if(statusTxt == "success")
      alert("External content loaded successfully!");
    if(statusTxt == "error")
      alert("Error: " + xhr.status + ": " + xhr.statusText);
  });
});
```



## Get/Post
[jQuery -HTTP Request: GET vs. POST](https://www.w3schools.com/jquery/jquery_ajax_get_post.asp)

Two commonly used methods for a request-response between a client and server are: GET and POST.

- GET - Requests data from a specified resource
- POST - Submits data to be processed to a specified resource

GET is basically used for just getting (retrieving) some data from the server. Note: The GET method may return cached data.

POST can also be used to get some data from the server. However, the POST method NEVER caches data, and is often used to send data along with the request.

### get()

`$.get(URL,callback);`

```js
$("button").click(function(){
  $.get("demo_test.asp", function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```

### post()

$.post(URL,data,callback);

The first parameter of `$.post()` is the URL we wish to request ("demo_test_post.asp").

```js
$("button").click(function(){
  $.post("demo_test_post.asp",
  {
    name: "Donald Duck",
    city: "Duckburg"
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```

```js
$("#loginBtn").click(function () {
  $.ajax({
    url: "/login",
    data: {
      username: $("#loginId").val(),
      password: $("#loginpwd").val(),
    },
    success: function (res) {
      console.log(res);
    },
  });
});

```

# jquery 面试题

1. 插入节点都有几种方式

2. html、val、text 区别

3. attr prop的区别

4. 事件如何添加

   用on，其他的已经废除了，除了on还有bind事件添加、live、delegate事件委托，就算是在低版本里面也不用，因为他们的内部，都执行的是on方法，所以为了效率，都用on 

5. $.each()和$().each()
   
6. jq的对象和原生对象如何转化

7. offset和position区别

8. width、innerWidht、outerWIdth的区别

9. $是什么东西

   $在jquery里面是JQuery对象，整个jq是用面向对象写的。JQuery就是生成的一个对象、咱们用的所有的方法都在这个JQuery对象上面

10. $都有什么功能
           1、$('选择器')  获取元素
           2、$('<div>111</div>')  创建一个元素
           3、$(原生对象)  变成jq的对象
           4、$(function(){})  类似window.onload其实不是，是DOMContentLoaded
    
11. window.onload和DOMContentLoaded有什么区别

    window.onload是DOM、资源（图片、音频、视频）等全部加载完才会加载
    DOMContentLoaded是DOM加载完就会加载

12. 什么是DOMReady

```js
$(document).ready(function () {
  // 在这里写你的代码...
});
//其实就是;
$(function () {});
```

13. jqeury写法有什么特点

jqeury大部分函数调用完返回的都是，之前获取的对象。所以jquery有一个操作叫做链式操作
`$('div').css().attr().offset()`