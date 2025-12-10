## 浏览器如何编译解析js

`var num = 123;`

电脑它只认识0和1，所有的字符、视频等一切文件资料，在电脑看来，都是0和1的不同组合。

虽然JavaScript它是一门脚本语言，不像Java、.net之类的有编译之后的可执行文件。但是Js它是存在编译阶段的。

**编译阶段**

1. 理解词

   var, xx标识符, =, 123值

> 词法分析，这个阶段的词法分析，是单纯的在识别组成代码的这些单词，是把你写的一长串字符串，给解析为有意义的代码块。

2. 句子理解

> 生成程序的语法的结构的树（AST）

3. 解析整个js

>把AST的语法结构树，转换为进执行的机器语言（二进制的0101001010，执行）

## 作用域

### 分类

JavaScript它是【词法作用域】，也就是固定的。是依赖代码编写时的结构，所确定的作用域，在js代码的编译结束之后，作用域就已经确定了，在运行的过程中不再改变。

编程语言当中，作用域一般分为二种

1. 词法作用域；

   （其实就是固定的作用域）【词法作用域】，也就是固定的。是依赖代码编写时的结构，所确定的作用域，在js代码的编译结束之后，作用域就已经确定了，在运行的过程中不再改变。

2. 动态作用域；

   （不固定的，在程序运行当中，作用域会变）

### 含义
它是一组规则，用来确定，哪些标识符，拥有，对哪些语法的访问的权限。

全局执行环境是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

初始化变量没有使用var/let声明，该变量会自动被添加到全局环境。

sum变量在函数外部是访问不到的，如果省var，则可运行成功。

```javascript
function add(num1, num2) {
var sum = num1 + num2;
  return sum; 
}
var result = add(10, 20);  //30 
alert(sum);                
//causes an error since sum is not a valid variable 
```

会向上逐级查询与给定名字匹配的标识符，indentifier,找到即停止。

```javascript
var color = “blue”;
function getColor(){
  var color = “red”;
  return color; }
alert(getColor());  //”red” 
```

## 标识符
### Identifiers

标识符,An identifier is the name of a variable, function, property, or function argument.

- The first character must be a letter, an underscore (_), or a dollar sign ($). 
- All other characters may be letters, underscores, dollar signs, or numbers.
- Keywords, reserved words, true, false, and null cannot be used as identifiers.

### 操作标识符

操作标识符就是读取、赋值

```javascript
//定义了xx标识符，并赋值123，这个操作叫“LHS”
var xx = 123;

//读取xx的值，这是一个RHS的操作。也包括一些函数、对象的调用
console.log(xx);
```

## closures

区分匿名函数和闭包。

闭包指的是有权访问另一个函数作用域中的变量的函数。

创建闭包的常见方式，就是在一个函数内部创建另一个函数。

In JavaScript, a function always has access to the context in which it was created. This is called `closure`. 

### closures and variables

闭包只能取得包含函数中任何变量最后一个值，保存的是整个变量对象，不是某个特殊变量。

```javascript
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(){
      return i;
    };
  }
  return result; 
} 

//只会返回10，即使是遍历函数，最终结果是10，不会返回各自不同的索引值

//强制返回各自不同的索引值

function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(num){
      return function(){
        return num;
      };
    }(i);
  }
  return result;
}
```

```javascript
function Bird() {
  let hatchedEgg = 10; // private variable

  /* publicly available method that a bird object can use */
  this.getHatchedEggCount = function() { 
    return hatchedEgg;
  };
}
let ducky = new Bird();
ducky.getHatchedEggCount(); // returns 10
```

public property 容易被串改到别的值，所以为了防止数据串改，将数据设为私有，通过闭包的方式。改变变量的作用域，由全局变量转变为局部变量。

This way, the variable can only be accessed and changed by methods also within the constructor function.

Here `getHatchedEggCount` is a privileged method, because it has access to the private variable `hatchedEgg`. This is possible because `hatchedEgg` is declared in the same context as `getHatchedEggCount`. 

## 垃圾回收机制

from js高程

> 垃圾回收的原理很简单，找到那些不再使用的变量，然后释放它们占用的内存

## IIFE

Immediately Invoked Function Expression

立即调用函数表达式

 Note that the function has no name and is not stored in a variable 

```javascript
(function () {
  console.log("Chirp, chirp!");
})(); 
// this is an anonymous function expression that executes right away
// Outputs "Chirp, chirp!" immediately
```

```javascript
function makeNest() {
  console.log("A cozy nest is ready");
}

makeNest();
```

## Module

最简单的模块化，就是函数。也就是函数封装

This returned object contains all of the mixin behaviors as properties of the object. The advantage of the module pattern is that all of the motion behaviors can be packaged into a single object that can then be used by other parts of your code 

```javascript
function glideMixin(obj) {
  obj.glide = function() {
    console.log("Gliding on the water");
  };
}
function flyMixin(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  };
}
```

We can group these mixins into a module as follows:


```javascript
//Note that you have an immediately invoked function expression (IIFE) that returns an object motionModule

let motionModule = (function () {
  return {
    glideMixin: function(obj) {
      obj.glide = function() {
        console.log("Gliding on the water");
      };
    },
    flyMixin: function(obj) {
      obj.fly = function() {
        console.log("Flying, wooosh!");
      };
    }
  }
})(); 
// The two parentheses cause the function to be immediately invoked

let duck = {name:'cat'}; 
let duck = {}; 

motionModule.glideMixin(duck);
duck.glide();
```

```javascript
let isCuteMixin = function(obj) {
  obj.isCute = function() {
    return true;
  };
};
let singMixin = function(obj) {
  obj.sing = function() {
    console.log("Singing to an awesome tune");
  };
};
```

We can group these mixins into a module as follows:

```javascript
let funModule = (function(){
  return {
    isCuteMixin : function(obj){
      obj.isCute = function(){
        return true;
      };
    },
    singMixin:function(obj){
      obj.sing = function (){
        console.log("Singing to an awesome tune");
      };
    }
  }
})();
```