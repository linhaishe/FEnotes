### 轮播图笔记

分析需求的【点】：
	1、要能左右移动，有一个数字需要+-
	2、有二个按钮；
	3、ul在动

列出js的功能：
	1、要获得二个按钮；
	2、你要得到ul；
	3、你要能让数字+-
	4、要有一个获得dom的方法
	5、要有相应的事件

大概的js的结构，就用之前讲过的prototype原型模式，

 1. fn构造器

    for循环添加dom
    init()
    
2. fn.prototype，添加方法
    constr....: fn，补全原型链
    init
	左按钮事件
	右按钮事件
	ul移动fn
	获得dom

### 父子元素定位关系问题

[the relationship of absolute and relative](https://www.zhihu.com/question/19926700)

[学习css布局](http://zh.learnlayout.com/toc.html)这个网站有时间需要再过一遍

只要父级元素设置了position值（absolute或者relative），那么子元素的position都是以父级元素来定位的

[w3c recommendation](https://www.w3.org/TR/CSS21/box.html#padding-edge)

If the element has 'position: absolute', the containing block is established by the nearest ancestor with a 'position' of 'absolute', 'relative' or 'fixed', in the following way:

1. In the case that the ancestor is an inline element, the containing block is the bounding box around the padding boxes of the first and the last inline boxes generated for that element. In CSS 2.1, if the inline element is split across multiple lines, the containing block is undefined.
2. Otherwise, the containing block is formed by the padding edge of the ancestor.


### common.js文件

1. 构造器，首字母要大写，最好加上 obj 或是 fn之类的字母，表示这是个大对象或是函数的意思。

2. 一些公共的方法，要把它单独的封装在一个专门的文件里。这种文件，一般叫 common.js,个人理解是一些简单的重复性的代码进行封装。

3. js文件会阻塞浏览器的进程，所以一般把它放在页面的尾部。外部链接放顶部

### Apply, call

**严格模式下，未指定环境对象而调用函数，则this值不会转为windows,除非明确把函数添加到某个对象或者调用call()/apply(),否则，this的值会是undefined**

<mark>使用call()/apply()主要用于扩充函数运行的作用域</mark>

1. call()的用法

call(),在使用call()方法时，传递给函数的参数必须逐个列举出来

将callSum的作用域扩充到了sum函数中，但是callSum函数它不必为了sum函数做任何事情

```javascript
function sum(num1, num2){
    return num1 + num2; 
}
function callSum(num1, num2){
    return sum.call(this, num1, num2); 
}
alert(callSum(10,10));   //20 
```

```javascript
function addFn( a, b){
	console.log( this )
	console.log( a + b )
}

function minsFn( a, b){
	console.log( a - b )
}

//此时 addFn函数中的this，
// 在非严格模式下，指向window
// addFn(1,2);
// minsFn(4,3)

// 一个函数，它没有加减的功能，但需要实现加减数字
function xxfn(){}

// 那么我就需要借用其它的函数，
// 也就是把xxfn中的this，指向其它的函数
//此时 addFn函数中的this，被修改为xxfn的this了
addFn.call( xxfn, 4,3 );

/*
此时，xxfn中的this,还是xxfn;
同时，addFn中的this，也是 xxfn了，
所以说，真正强大的地方在于，【能够扩充xxfn函数的作用域】
*/
```

```javascript
window.color = “red”; 
var o = { color: “blue” };
function sayColor(){
    alert(this.color); 
}
sayColor();            //red
sayColor.call(this);   //red this指向windows.color
sayColor.call(window); //red 指向windows.color
sayColor.call(o);      //blue this指向了o
```

2. apply()的用法

```javascript
function addFn( a, b){
	// console.log( this )
	console.log( a + b )
}

function minsFn( a, b){
	console.log( a - b )
}

function xxfn(){}

// 有些时候，你接收到的是一个数组，就用apply比较方便
addFn.apply( xxfn, [2,6] );
minsFn.apply( xxfn, [2,6] );
```

3. bind()<mark>看不懂</mark>

https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind

this的引用，当一个函数，是一个对象的属性时，那么这个函数中的this，指向这个对象

```javascript
const module = {
  x: 42,
  getX: function() {
    return this.x;
  }
}

const unboundGetX = module.getX;
console.log(unboundGetX()); 
// The function gets invoked at the global scope
// expected output: undefined

const boundGetX = unboundGetX.bind(module);
console.log(boundGetX());
// expected output: 42
```

```javascript
this.x = 9;    // 在浏览器中，this指向全局的 "window" 对象
var module = {
  x: 81,
  getX: function() { return this.x; }
};

module.getX(); // 81

var retrieveX = module.getX;
retrieveX();   
// 返回9 - 因为函数是在全局作用域中调用的

// 创建一个新函数，把 'this' 绑定到 module 对象
// 新手可能会将全局变量 x 与 module 的属性 x 混淆
var boundGetX = retrieveX.bind(module);
boundGetX(); // 81
```

```javascript
window.color = “red”; 
var o = { color: “blue” };
function sayColor(){
    alert(this.color); 
} 
var objectSayColor = sayColor.bind(o); 
objectSayColor();   //blue 
```

### 继承说明

JavaScript当中的所谓的继承，就是this指向的改变。也可以说，是继承，是扩展了子类的this

### 三种继承方式

#### prototype原型继承

Prototype pattern章节，Prototypal Inheritance 章节 (javascript professional)

combination constructor/prototype pattern 章节(javascript professional)

这种方式的核心，在于把子类的prototype，指向了父类的实例。然后使得子类的实例，也能调用父类的实例的方法，原型链。

```javascript
function Axx( _n ){
	this.name = _n;
	this.age = 33;
}
// 如果要添加的方法不是特别多的情况下
Axx.prototype.say = function(){
	console.log( '说，这是' + this.name )
}
// var _axx = new Axx('我是老尚');
// _axx.say();
// 子类 - 构造器
function Bxx(){
	this.b_fn = function(){
		console.log('bxxx方法')
	}
}
Bxx.prototype = new Axx('我是子类 bxx');
// 这时就不能这么写了，
// Bxx.prototype = { a:4}
// 因为把上面的Bxx.prototype = new Axx...给覆盖了
Bxx.prototype.a = 4
Bxx.prototype.fnx = function(){
	console.log( 'fnxxxx' )
}
var _bxx = new Bxx();
_bxx.say(); //这是父类继承的方法
_bxx.fnx(); //这是Bxx的prototype添加的方法
_bxx.b_fn() //这是Bxx的构造器中
```

#### 构造函数继承

```javascript
function Axx(){
	this.a_say = function(){
		console.log('axxx')
	}
}

function Bxx(){
	this.parentsFn = Axx;
  //注意 不是 this.parentFn = Axx();

	this.parentsFn();
	this.b_say = function(){
		console.log( 'bxxx' )
	}
}

var _bxx = new Bxx();
console.log( _bxx )
```

在子类的构造器中，使用一个属性指向父类，`this.parentsFn = Axx`,这里父类不能加括号，否则就变成父类函数执行结果的赋值了，函数是引用传递，这时，是把 this.parentsFn 属性的值，指向了Axx函数

a. 这里是把父类做为子类的一个属性来执行；而不是单纯的执行父类的函数；

b. 这里没有new关键字，所以不可能生成一个什么实例。

<mark>那么这个父类中的 a_say方法，是怎么来到了 Bxx 中呢？</mark>

c. 说到这里，咱们还是要从this的引用上来解释

- parentsFn这个属性，它指向Axx这个函数；
- 我们执行 .parentsFn属性时，就等于执行了 Axx函数；parentsFn属性这时就是一个函数

d. this的引用,

(构造函数this指向调用者往往是调用构造函数的实例本身)

(全局函数中this = window,函数被作为某个对象的方法调用时，this等于那个对象。匿名函数的执行环境具有全局性，其this通常指向windows)

当一个函数，是一个对象的属性时，那么这个函数中的this，指向这个对象；

所以，.parentsFn函数，它是Bxx对象（因为函数也是对象）的属性，

所以，在调用的时候，

.parentsFn函数里面的this，就指向了Bxx，

也就是 Axx函数里面的this，指向了 Bxx，

所以我们能够在Bxx的实例中，得到 a_say 方法

<mark>为什么不是单独的执行Axx()?</mark>

就是为了把父类Axx函数，挂载在Bxx这个子类对象的this之上,然后再执行，就可以修改Axx()函数中this的引用

#### call & apply继承

```javascript
// 父类a - 构造器
function Axx( _n, _m ){
	this.a_fn = function(){
		console.log( _n + _m )
	}
}

// 子类 - 构造器--------------
function Children( a, b){
	Axx.call(this, a, b)
}

var _childrenObj = new Children( 1,3);
_childrenObj.a_fn()
```

Call & apply 的多重继承

```javascript
// 父类a - 构造器
function Axx( _n, _m ){
	this.a_fn = function(){
		console.log( _n + _m )
	}
}

// 父类b - 构造器
function Bxx(){
	this.b_fn = function(){
		console.log('bbbbb')
	}
}

// 父类c - 构造器
function Cxx(){
	this.c_fn = function(){
		console.log('cccccc')
	}
}

// 子类 - 构造器
function Children( a, b){
	Axx.call(this, a, b);
	Bxx.call(this);
	Cxx.call(this);
}

var _childrenObj = new Children( 1,3);
console.log( _childrenObj )
_childrenObj.a_fn();
_childrenObj.b_fn();
_childrenObj.c_fn();
```

### 原型链

通过prototype、constructor，不断的向上、向父类去查找方法

```javascript
function Base(){}

function Sub1(){}
Sub1.prototype = new Base(); //prototype，原型继承
Sub1.prototype.constructor = Sub1; //补全Sub1的原型链

// 自定义属性
Sub1.superCalss = Base.prototype; 
//Sub1.superCalss的值，是Base的constructor

function Sub2(){}
Sub2.prototype = new Sub1(); //prototype，原型继承
Sub2.prototype.constructor = Sub2; //补全Sub2的原型链

// 自定义属性
Sub2.superCalss = Sub1.prototype;

console.log( Sub2.prototype.constructor );//function Sub2(){}
console.log( Sub2.superCalss.constructor ); //function Sub1(){}
/*
Sub2.superCalss.constructor，换算等于，
Sub1.prototype.constructor;
所以结果是，function Sub1(){}
*/

console.log( Sub2.superCalss.constructor.superCalss.constructor );
//function Base(){}

/*
Sub2.superCalss.constructor.superCalss.constructor，换算等于，
Sub1.prototype.constructor.superCalss.constructor，换算等于，
Sub1.superCalss.constructor，换算等于，
Base.prototype.constructor，结果，自然就是Base
*/

```

