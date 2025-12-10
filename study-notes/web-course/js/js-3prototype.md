https://www.tutorialsteacher.com/javascript/prototype-in-javascript

[Master JavaScript Prototypes & Inheritance]( https://codeburst.io/master-javascript-prototypes-inheritance-d0a9a5a75c4e )

### 函数名就是变量

再明确一下，在ECMAScript当中，函数名就是变量,所以不要把函数名，当成函数本身来理解。函数名和函数是二个东西，只不过因为函数是引用类型，所以函数名通过引用，指向了它所引用的那个函数。

可以把函数做为参数，传入到另一个函数当中。并不是你把函数这个引用对象，传入到了另一个函数中,而是把一个引用以地址的形式，传入到函数里面。

加括号是把函数执行后的值赋值给变量；

不加括号是把函数本身赋值给变量

（函数声明和函数表达式相关）

```javascript
function a(){
return("this is a");
}
var b=a;
var c=a();
console.log(b);
console.log(b());
console.log(c);
console.log(c());
```

```javascript
function afn(){
	console.log(77777)
}

//afn();

function getAjaxFn( callback ){
	console.log(callback)
	callback();
}

getAjaxFn( afn )

```

```javascript
function afn(_n){
	console.log(_n)
}

//afn();

function getAjaxFn( callback ){
	console.log(callback)
  //output 
  //function afn(_n){
	//console.log(_n)
//}


  //var test = 123;
  //function afn(test){
  //  console.log(test)
  //}
  
  var test = 123;
  callback(test)
  //这部分同于上面注释掉的部分，因为callback指向afn函数
  //output 123 
}

getAjaxFn( afn )
```


<mark>问题</mark>

![Xnip2019-11-09_22-24-56.png](http://ww1.sinaimg.cn/large/005NUwygly1g8s5q73dhjj317q0kwn32.jpg)


一般使用这种方式来做ajax类操作的封装回调的公共方法，

这种公共方法，一般放在common.js里面，就是公共的js文件。

### Callback function

https://stackoverflow.com/questions/9596276/how-to-explain-callbacks-in-plain-english-how-are-they-different-from-calling-o

https://stackoverflow.com/questions/9596276/how-to-explain-callbacks-in-plain-english-how-are-they-different-from-calling-o/9652434#9652434

https://developer.mozilla.org/zh-CN/docs/Glossary/Callback_function

https://www.youtube.com/watch?v=xHneyv38Jro

[彻底理解javascript的回调函数（推荐）](https://www.cnblogs.com/moltboy/archive/2013/04/24/3040213.html)

#### JavaScript两种执行模式

- “同步模式（Synchronous）”就是一个任务完成之后，后边跟着一个任务接着执行；程序的执行顺序和排列顺序是一直的；
- ”异步模式（Asychronous）”则完全不同，每一个任务都有一个或者多个回调函数（callback），前一个任务结束的时候，不是执行下一个任务，而是执行回调函数，后一个任务则是不等前一个任务结束就执行，所以程序的执行顺序与任务顺序不一致的，异步的。

其中回调函数和事件监听就是最基本的“异步模式”处理方法。

#### 回调函数（callback）

```javascript
function test(start, end, callback){
    var number = Math.ceil(Math.random() * (start - end) + arg2);
    callback(number);　　//传递结果
}

test(10, 20, function(num){
   console.log("Number: " + number); 
});　　　　//结果为10和20之间的随机数
```

- 回调函数具体的定义为：函数A作为参数(函数引用)传递到另一个函数B中，并且这个函数B执行函数A。我们就说函数A叫做回调函数。如果没有名称(函数表达式)，就叫做匿名回调函数。
- 回调函数不一定用于异步，一般同步(阻塞)的场景下也经常用到回调，比如要求执行某些操作后执行回调函数。
- 回调函数，一般在同步情境下是最后执行的，而在异步情境下有可能不执行，因为事件没有被触发或者条件不满足。
- 回调函数简单，容易理解和部署。但是不利于代码的阅读，和维护，各部分之间高度耦合，流程会很混乱，而且每一个任务只能指定一个回调函数。

#### 事件监听（Event）

- 当页面要发生一些事情或做一些事情时，我们称其为事件。事件是网页自带的属性，如click、mousemove、load等。
- 响应某个事件的函数则称为事件处理程序，或者叫做事件侦听器。
- 采用事件驱动模式，任务的执行不取决代码的顺序，而取决于某一个事件是否发生。
- 常见监听函数有：on，bind，listen，addEventListener，observe
- 事件监听比较容易理解，可以绑定多个事件，每一个事件可以指定多个回调函数，而且可以去耦合，有利于实现模块化。但是通过事件监听机制整个程序都要变成事件驱动型，运行流程会变得不清晰。

### 函数的属性、方法：prototype

每个函数都有自己的prototype属性和length。对于函数来讲，length是它要接收的参数的数量，

#### length property

```javascript
function howManyArgs() {
 alert(arguments.length);
}
howManyArgs(“string”, 45); //2
howManyArgs(); //0
howManyArgs(12); //1
```

arguments object can be used  in conjunction with named arguments

```javascript
function doAdd(num1, num2) {
 if(arguments.length == 1) {
 alert(num1 + 10);
 } else if (arguments.length == 2) {
 alert(arguments[0] + num2);
 }
}
```

Another thing to keep in mind: if only one argument is passed in, then setting arguments[1] to a value will not be refl ected by the named argument. 

Any named argument that is not passed into the function is automatically assigned the value undefined

<mark>Strict mode makes several changes to how the arguments object can be used.p82</mark>

### Prototype pattern

prototype属性是无法枚举的，使用for in是无法发现prototype属性的

创建的每个函数都有一个prototype属性，（个人理解，每个函数有自己的基因，这个基因被称为prototype）这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法，如果按照字面意思来理解，那么prototype就是通过调用构造函数而创建的那个对象实例的原型对象。

使用原型对象的好处是可以让所有对象实例共享它所包含的属性和方法。换句话说，不必在构造函数中定义对象实例的信息，而是将信息直接添加到原型对象中。

1、可以给函数添加自定义属性；

2、可以给构造函数所有的实例，添加共同拥有的方法；

你需要new一个实例,因为这个new一个实例的过程中，在第二步，把prototype上的方法、属性，添加到新生成的空对象上，然后把新的对象最后再返回，这时，新的对象上才有你使用prototype添加的方法。

This may not be an issue when there are only two instances, but imagine if there are millions of instances. That would be a lot of duplicated variables.

原型模式

```javascript
function Person(){
}
//构造函数成为空函数，将属性值添加在prototype属性中
Person.prototype.name = “Nicholas”; 
Person.prototype.age = 29; 
Person.prototype.job = “Software Engineer”; 
Person.prototype.sayName = function(){
  alert(this.name); 
};
var person1 = new Person(); 
person1.sayName();   //”Nicholas”
var person2 = new Person(); 
person2.sayName();   //”Nicholas”
alert(person1.sayName == person2.sayName);  //true 
```

<mark>简单写法</mark>

```javascript
function Person(){
}
Person.prototype = {
  name:"jhon";
  age:29,
  job:"writter",
  sayName:function(){
    alert(this.name);
  }
};
```

### 原型链的修复

简单写法其实是对prototype属性的覆盖重写，prototype这个值是可以被覆盖的。就是把constructor这个值，再重写回去
这个原型链，就又完整了。
每创建一个函数，就会同时创建他的prototype对象，这个对象也会自动获得constructor属性[[constructor]]。这个简单写法是对prototype对象的重写。

```javascript
//简单写法需要写明constructor指向
Bird.prototype = {
  constructor: Bird, // define the constructor property
  numLegs: 2,
  eat: function() {
    console.log("nom nom nom");
  },
  describe: function() {
    console.log("My name is " + this.name);
  }
};
```

### prototype chaining

原型链

All objects in JavaScript (with a few exceptions) have a `prototype`. Also, an object’s `prototype`itself is an object. Because a `prototype`is an object, a `prototype`can have its own `prototype`!

In this `prototype`chain, `Bird`is the `supertype`for `duck`, while `duck`is the `subtype`. `Object`is a `supertype`for both `Bird`and `duck`.

```javascript
function Bird(name) {
  this.name = name;
}

typeof Bird.prototype; // => object

Object.prototype.isPrototypeOf(Bird.prototype);
// returns true

let duck = new Bird("Donald");
duck.hasOwnProperty("name"); // => true
```

```javascript
// 构造函数
function fn(){}

// prototype，原型
console.log( fn.prototype )
//output object
//prototype指向一个对象

// constructor，构造器
console.log( fn.prototype.constructor )
//output ƒ fn(){}
```

<mark>this example is considered to be both an instance of Object and an instance of Person</mark>

![QQ截图20191108113339.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8qhfte7dfj30ld0ahjrt.jpg)

![prototype chain.JPG](http://ww1.sinaimg.cn/large/005NUwygly1g8t0jo6zpwj316q0kyaen.jpg)

例如jq源码，它会把prototype用一个变量再给保存一下，这个从某种程度上来讲，也有保护prototype的想法。jQuery.fn = jQuery.prototype..

<!-- prototype原型模式，初尝 -->

我个人使用这种方式，一般是把需求都分拆开，放在prototype里，做为一个一个的函数。加减乘除的计算demo.html



分析需求：

1、页面上有哪些用到数据的点？

2、有哪些UI操作？

3、它们之间的顺序？

4、...更多



我的步骤：

1、获得dom；

2、根据UI操作定义对应的功能函数；

​    <!-- 每个函数只做一件事情； -->

3、启动方法，init();



new一个实例，所返回的新对象，

它有构造器和prototype里面的方法。

所以，在返回的对象里，

prototype和构造器里的this，是相同的。


