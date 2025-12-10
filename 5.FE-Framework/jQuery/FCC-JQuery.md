### Introduction to jQuery

jQuery is one of the many libraries for JavaScript. It is designed to simplify scripting done on the client side. jQuery's most recognizable characteristic is its dollar sign (`$`) syntax. With it, you can easily manipulate elements, create animations and handle input events.

Your browser will run any JavaScript inside a `script` element, including jQuery.  The important thing to know is that code you put inside this `function` will run as soon as your browser has loaded your page 


```HTML
<script>
$(document).ready(function(){});
</script>
```

### target id，class , HTML element

jq的使用和css的选择器也有相关，针对id，class , HTML element的选择语法是和css selector 是一样的。

 three ways of targeting elements: by type: `$("button")`, by class: `$(".btn")`, and by id `$("#target1")`. 

```html
<script>
  $(document).ready(function() {
    $("button").addClass("animated bounce");
    $(".well").addClass("animated shake");
    $("#target3").addClass("animated fadeOut");

  });
</script>

<div class="container-fluid">
  <h3 class="text-primary text-center">jQuery Playground</h3>
  <div class="row">
    <div class="col-xs-6">
      <h4>#left-well</h4>
      <div class="well" id="left-well">
        <button class="btn btn-default target" id="target1">#target1</button>
        <button class="btn btn-default target" id="target2">#target2</button>
        <button class="btn btn-default target" id="target3">#target3</button>
      </div>
    </div>
    <div class="col-xs-6">
      <h4>#right-well</h4>
      <div class="well" id="right-well">
        <button class="btn btn-default target" id="target4">#target4</button>
        <button class="btn btn-default target" id="target5">#target5</button>
        <button class="btn btn-default target" id="target6">#target6</button>
      </div>
    </div>
  </div>
</div>

```

### targeting one element and adding only one class at a time 

Target the Same Element with Multiple jQuery Selectors 

```html
<script>
  $(document).ready(function() {
    $("button").addClass("animated");
    $(".btn").addClass("shake");
    $("#target1").addClass("btn-primary");
  });
</script>

<!-- Only change code above this line. -->

<div class="container-fluid">
  <h3 class="text-primary text-center">jQuery Playground</h3>
  <div class="row">
    <div class="col-xs-6">
      <h4>#left-well</h4>
      <div class="well" id="left-well">
        <button class="btn btn-default target" id="target1">#target1</button>
        <button class="btn btn-default target" id="target2">#target2</button>
        <button class="btn btn-default target" id="target3">#target3</button>
      </div>
    </div>
    <div class="col-xs-6">
      <h4>#right-well</h4>
      <div class="well" id="right-well">
        <button class="btn btn-default target" id="target4">#target4</button>
        <button class="btn btn-default target" id="target5">#target5</button>
        <button class="btn btn-default target" id="target6">#target6</button>
      </div>
    </div>
  </div>
</div>

```

### Remove Classes

```html
<script>
  $(document).ready(function() {
    $("button").addClass("animated bounce");
    $(".well").addClass("animated shake");
    $("#target3").addClass("animated fadeOut");
    $("button").removeClass("btn-default");

  });
</script>
```

### Change the CSS

 jQuery has a function called `.css()` that allows you to change the CSS of an element. 

change its color to blue 

` $("#target1").css("color", "blue"); `

```html
<script>
  $(document).ready(function() {
$("#target1").css("color","red")
  });
</script>

<!-- Only change code above this line. -->

<div class="container-fluid">
  <h3 class="text-primary text-center">jQuery Playground</h3>
  <div class="row">
    <div class="col-xs-6">
      <h4>#left-well</h4>
      <div class="well" id="left-well">
        <button class="btn btn-default target" id="target1">#target1</button>
        <button class="btn btn-default target" id="target2">#target2</button>
        <button class="btn btn-default target" id="target3">#target3</button>
      </div>
    </div>
    <div class="col-xs-6">
      <h4>#right-well</h4>
      <div class="well" id="right-well">
        <button class="btn btn-default target" id="target4">#target4</button>
        <button class="btn btn-default target" id="target5">#target5</button>
        <button class="btn btn-default target" id="target6">#target6</button>
      </div>
    </div>
  </div>
</div>

```

### Disable an Element

  `.prop()` that allows you to adjust the properties of elements. 

` $("button").prop("disabled", true); `

 Disable only the `target1` button. 

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled",true);
  });
</script>
```

### Change Text

  `.html()` that lets you add HTML tags and text within an element. Any content previously within the element will be completely replaced with the content you provide using this function. 

 `.text()` that only alters text without adding tags. In other words, this function will not evaluate any HTML tags passed to it, but will instead treat it as the text you want to replace the existing content with. 

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target4").html("<em>#target4</em>");
  });
</script>
```

### Remove an Element

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
  });
</script>
```

### Move Elements

 `appendTo()` that allows you to select HTML elements and append them to another element. 

For example, if we wanted to move `target4` from our right well to our left well, we would use:

`$("#target4").appendTo("#left-well");`

target2 原本在left的，修改后跑到id#right-well区域了

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
    $("#target2").appendTo("#right-well");
  });
</script>

<!-- Only change code above this line. -->

<div class="container-fluid">
  <h3 class="text-primary text-center">jQuery Playground</h3>
  <div class="row">
    <div class="col-xs-6">
      <h4>#left-well</h4>
      <div class="well" id="left-well">
        <button class="btn btn-default target" id="target1">#target1</button>
        <button class="btn btn-default target" id="target2">#target2</button>
        <button class="btn btn-default target" id="target3">#target3</button>
      </div>
    </div>
    <div class="col-xs-6">
      <h4>#right-well</h4>
      <div class="well" id="right-well">
        <button class="btn btn-default target" id="target4">#target4</button>
        <button class="btn btn-default target" id="target5">#target5</button>
        <button class="btn btn-default target" id="target6">#target6</button>
      </div>
    </div>
  </div>
</div>

```

### Clone an Element

  `clone()` that makes a copy of an element. 

For example, if we wanted to copy `target2` from our `left-well` to our `right-well`, we would use:

`$("#target2").clone().appendTo("#right-well");`

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
    $("#target2").appendTo("#right-well");
    $("#target5").clone().appendTo("#left-well");
  });
</script>
```

### Target the Parent of an Element

 `parent()` that allows you to access the parent of whichever element you've selected. 

use the `parent()` function if you wanted to give the parent element of the `left-well` element a background color of blue: 

` $("#left-well").parent().css("background-color", "blue") `

这里的parent指的是那个？？？？？？

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
    $("#target2").appendTo("#right-well");
    $("#target5").clone().appendTo("#left-well");
$("#target1").parent().css("background-color", "red")
  });
</script>

<!-- Only change code above this line. -->

<body>
  <div class="container-fluid">
    <h3 class="text-primary text-center">jQuery Playground</h3>
    <div class="row">
      <div class="col-xs-6">
        <h4>#left-well</h4>
        <div class="well" id="left-well">
          <button class="btn btn-default target" id="target1">#target1</button>
          <button class="btn btn-default target" id="target2">#target2</button>
          <button class="btn btn-default target" id="target3">#target3</button>
        </div>
      </div>
      <div class="col-xs-6">
        <h4>#right-well</h4>
        <div class="well" id="right-well">
          <button class="btn btn-default target" id="target4">#target4</button>
          <button class="btn btn-default target" id="target5">#target5</button>
          <button class="btn btn-default target" id="target6">#target6</button>
        </div>
      </div>
    </div>
  </div>
</body>

```

### Target the Children of an Element

 `children()` that allows you to access the children of whichever element you've selected. 

 use the `children()` function to give the children of your `left-well` element the color `blue`: 

` $("#left-well").children().css("color", "blue") `

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
    $("#target2").appendTo("#right-well");
    $("#target5").clone().appendTo("#left-well");
    $("#target1").parent().css("background-color", "red");
$("#right-well").children().css("color", "orange")
  });
</script>
```

### Target a Specific Child of an Element

The `target:nth-child(n)` CSS selector allows you to select all the nth elements with the target class or element type. 

` $(".target:nth-child(3)").addClass("animated bounce"); `

```html
<script>
  $(document).ready(function() {
    $("#target1").css("color", "red");
    $("#target1").prop("disabled", true);
    $("#target4").remove();
    $("#target2").appendTo("#right-well");
    $("#target5").clone().appendTo("#left-well");
    $("#target1").parent().css("background-color", "red");
    $("#right-well").children().css("color", "orange");
$(".target:nth-child(2)").addClass("animated bounce");
  });
</script>
```

### Target Even/odd Elements

 target elements based on their positions using `:odd` or `:even` selectors. 

 jQuery is zero-indexed ( zero-based system ) which means the first element in a selection has a position of 0.  

class的 target ， 不是 id # target

` $(".target:odd").addClass("animated shake"); `

target135 will shake

```html
<script>
  $(document).ready(function() {
      $(".target:even").addClass("animated shake");
  });
</script>
```

### Modify the Entire Page

` $("body").addClass("animated fadeOut"); `

`$("body").addClass("animated hinge");`

### add event

`$(#id).on('click',fucniton(){})`