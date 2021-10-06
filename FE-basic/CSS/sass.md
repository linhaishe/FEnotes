### intro

Sass uses variables. They are declared and set to store data, similar to JavaScript.  variables start with a `$` followed by the variable name. 

```css
<style type='text/sass'>

$main-fonts: Arial, sans-serif;
$headings-color: green;

//To use variables:
h1 {
  font-family: $main-fonts;
  color: $headings-color;
}
```

### Nest CSS with Sass

 nesting can help organize your code 

```css
nav {
  background-color: red;
}

nav ul {
  list-style: none;
}

nav ul li {
  display: inline-block;
}
```

```css
nav {
  background-color: red;

  ul {
    list-style: none;

    li {
      display: inline-block;
    }
  }
}
```

```html
<style type='text/sass'>
.blog-post {
	h1 {
    text-align: center;
    color: blue;
  }
    p {
    font-size: 20px;
  }
}
  
</style>

<div class="blog-post">
    <h1>Blog Title</h1>
    <p>This is a paragraph</p>
</div>
```

### @mixins

In Sass, a mixin is a group of CSS declarations that can be reused throughout the style sheet. 

The definition starts with `@mixin` followed by a custom name. The parameters (the `$x`, `$y`, `$blur`, and `$c` in the example above) are optional. Now any time a `box-shadow` rule is needed, only a single line calling the mixin replaces having to type all the vendor prefixes. A mixin is called with the `@include` directive: 

```css
div {
  -webkit-box-shadow: 0px 0px 4px #fff;
  -moz-box-shadow: 0px 0px 4px #fff;
  -ms-box-shadow: 0px 0px 4px #fff;
  box-shadow: 0px 0px 4px #fff;
}
```

```css
@mixin box-shadow($x, $y, $blur, $c){ 
  -webkit-box-shadow: $x, $y, $blur, $c;
  -moz-box-shadow: $x, $y, $blur, $c;
  -ms-box-shadow: $x, $y, $blur, $c;
  box-shadow: $x, $y, $blur, $c;
}
```

### @include

```css
div {
  @include box-shadow(0px, 0px, 4px, #fff);
}
```

```css
//wrong
<style type='text/sass'>
@mixin border-radius($radius) {
-webkit-border-radius:$radius;
-moz-border-radius:$radius;
-ms-border-radius:$radius;
}
$radius:15px;

  #awesome {
    width: 150px;
    height: 150px;
    background-color: green;
    border-radius:$radius;
    @include border-radius(15px);

  }
</style>

<div id="awesome"></div>
```

```css
//right answer
<style type='text/sass'>
  @mixin border-radius($radius) {
    -webkit-border-radius: $radius;
    -moz-border-radius: $radius;
    -ms-border-radius: $radius;
    border-radius: $radius;
  }

  #awesome {
    width: 150px;
    height: 150px;
    background-color: green;
    @include border-radius(15px);
  }
</style>

<div id="awesome"></div>
```

### @if and @else

The `@if` directive in Sass is useful to test for a specific case - it works just like the `if` statement in JavaScript.  `@else if` and `@else` test for more conditions: 

```css
@mixin make-bold($bool) {
  @if $bool == true {
    font-weight: bold;
  }
}
```

```css
@mixin text-effect($val) {
  @if $val == danger {
    color: red;
  }
  @else if $val == alert {
    color: yellow;
  }
  @else if $val == success {
    color: green;
  }
  @else {
    color: black;
  }
}
```

```css
<style type='text/sass'>
  @mixin border-stroke($val) {
    @if $val == light {
      border: 1px solid black;
    }
    @else if $val == medium {
      border: 3px solid black;
    }
    @else if $val == heavy {
      border: 6px solid black;
    }
    @else {
      border: none;
    }
  }


  #box {
    width: 150px;
    height: 150px;
    background-color: red;
    @include border-stroke(medium);
  }
</style>

<div id="box"></div>
```

### @for

used in two ways: "start through end" or "start to end".  

"start **to** end" ***excludes*** the end number as part of the count, 

"start **through** end" ***includes*** the end number as part of the count. 

```css
/*start through end */

@for $i from 1 through 12 {
  .col-#{$i} { width: 100%/12 * $i; }
}
```

```css
/*start through end 
*
*Sass file is converted to CSS
*/

.col-1 {
  width: 8.33333%;
}

.col-2 {
  width: 16.66667%;
}

...

.col-12 {
  width: 100%;
}
```

a `@for` directive that takes a variable `$j` that goes from 1 **to** 6.

It should create 5 classes called `.text-1` to `.text-5` where each has a `font-size` set to 10px multiplied by the index.

```css
<style type='text/sass'>
@for $j from 1 through 6 {
  .text-#{$j} { font-size: 10px * $j; }
}
</style>

<p class="text-1">Hello</p>
<p class="text-2">Hello</p>
<p class="text-3">Hello</p>
<p class="text-4">Hello</p>
<p class="text-5">Hello</p>

```

### @each

`@each` directive which loops over each item in a list or map. On each iteration, the variable gets assigned to the current value from the list or map. 

```css
@each $color in blue, red, green {
  .#{$color}-text {color: $color;}
}
```

```css
/*A map has slightly different syntax. Here's an example:*/

$colors: (color1: blue, color2: red, color3: green);

@each $key, $color in $colors {
  .#{$color}-text {color: $color;}
}
```

```css
/* converted into the following CSS */

.blue-text {
  color: blue;
}

.red-text {
  color: red;
}

.green-text {
  color: green;
}
```

```css
<style type='text/sass'>
@each $color in blue, black, red {
  .#{$color}-bg {background-color: $color;}
}


  div {
    height: 200px;
    width: 200px;
  }
</style>

<div class="blue-bg"></div>
<div class="black-bg"></div>
<div class="red-bg"></div>

```

### @while

It creates CSS rules until a condition is met. 

```css
$x: 1;
@while $x < 13 {
  .col-#{$x} { width: 100%/12 * $x;}
  $x: $x + 1;
}
```

```css
<style type='text/sass'>
$x: 1;
@while $x < 15 {
  .text-#{$x} { font-size: 15px * $x ;}
  $x: $x + 1;
}
</style>

<p class="text-1">Hello</p>
<p class="text-2">Hello</p>
<p class="text-3">Hello</p>
<p class="text-4">Hello</p>
<p class="text-5">Hello</p>

```

### @import

 if all your mixins are saved in a partial named "_mixins.scss", and they are needed in the "main.scss" file, this is how to use them in the main file 

```css
// In the main.scss file

@import 'mixins'
```

 Write an `@import` statement to import a partial named `_variables.scss` into the main.scss file. 

```css
// The main.scss file
@import "variables"
```

###  @extend

`extend` that makes it easy to borrow the CSS rules from one element and build upon them in another. 

```css
.panel{
  background-color: red;
  height: 70px;
  border: 2px solid green;
}

.big-panel{
  @extend .panel;
  width: 150px;
  font-size: 2em;
}
```

