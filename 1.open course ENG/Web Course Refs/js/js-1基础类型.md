### js brief intro

JavaScript，它是目前最流行的编程语言，之一。

JavaScript它是一种轻量级脚本语言。

脚本语言的意思，是说它不能被编译。

它在运行时的代码，就是你开发编写时的代码，

这好处是简单，快速；

坏处就是不能保密源码，安全性也有一些问题。

现在一般把它放在页面的结尾部分

从上到下一行一行的执行，遇到错误会停止，不再执行。

在不同的宿主环境(运行js的环境)提供核心脚本的编程能力

Node/flash/explore都是宿主环境

ECMAScript + BOM + DOM = FULL JS (需要事件触发JS才能运行)

变量在赋值的时候，使用 var 关键字

变量不声明，成为非必要的全局变量，被称为“全局变量污染”

<mark>变量的生命周期</mark>，创建后被函数调用后，会被销毁。

```html
<!-- 
下面这个例子，要从变量的生命周期的角度来理解。
而不是从变量的作用域来考虑。
 -->

<script type="text/javascript">
// 定义一个函数
function fn(){
	// 创建一个变量并赋值
	var _v = 123;
	// console.log( _v )
}

// 调用函数
fn();
// 执行到这一行时，函数的调用已经结束了
console.log( _v ); // 报错

</script>

<!-- 
为什么会报错？
1、全局、局部作用域的原因；
2、第二个角度来说，就是函数执行完了，_v的变量已经没了所以你再打印_v，会报错。
-->
```

![Xnip2019-11-03_15-45-10.png](http://ww1.sinaimg.cn/large/005NUwygly1g8kwc3a7koj30pa0tm0w0.jpg)

### Null

### boolean

Boolean是ECMAScript当中使用最多的一种类型，因为所有的逻辑分支的判断，都需要用到boolean值。

```javascript
var test = 'test';
console.log(boolean(test))
//return true
```

<mark>VALUES CONVERTED TO TRUE / FALSE</mark>

| DATA TYPE | VALUES CONVERTED TO TRUE                | DATA TYPEVALUES CONVERTED TO TRUE |
| --------- | --------------------------------------- | --------------------------------- |
| Boolean   | true                                    | False                             |
| String    | Any nonempty string                     | “” (empty string)                 |
| Number    | Any nonzero number (including infinity) | 0, NaN                            |
| Object    | Any object                              | null                              |
| Undefined | n/a                                     | Undefined                         |

### number

八进制

第一位数字必须是0，070，56，079，79，严格模式下是无效的。

十六进制

前两位数字为0x,后面跟0-9或a-f

在实际计算的时候，所有的八进制，十六进制，都被转成了十进制进行计算。

number是使用IEEE754格式来表示整数，浮点数。但在浮点数值计算中会不准确。js中不要做小数点的计算。

0.05+0.25，0.1+0.2=0.30000000000004

### NaN

在有一些应该返回数字，但是没有返回数字的情况下。其和任何值都不相等，包括它自己。

### Number Conversions

Number ( )

parseInt ( )

parseFloat ( )

### string

每次的修改，都是销毁之后，再重新填充。

### function

任何函数都可以通过return语句来返回值，无return的情况下会返回，undefined

```javascript
var test = function(){
  return 123;
}

//console.log(xx());
//123

function testfn(){
  console.log(xxfn());
}
//undefined
```

#### no overloading

没有重载，定义了两个相同名字的函数，则改名字只属于后定义的函数。

```javascript
function addSomeNumber(num){
  return num + 100; 
}function addSomeNumber(num) {
  return num + 200; 
}
var result = addSomeNumber(100);    //300 
```

### data type, this object, scope

#### data type

js的变量有两种类型的值，基本类型和引用类型。

1. 基本类型，是数据的具体的值。

   String, number, boolean,null,undefined

2. 引用类型的值，一般是一些对象。

   - Array, Function, Object（非基本数据类型
   - 对象保存在内存中，出安全考虑，不能直接去访问内存中的值。js不能直接操作内存。操作对象，是操作对象的引用。

#### adding property 

1. Object 

```javascript
var _obj = {}
-obj.a = 1;
_obj.b = function(){
  cosnole.log('test')
}
//console.log(_obj)
```

2. Function 

```javascript
function fn(){}
fn.a = function(){}
fn.b = 'test';
console.log(fn);//以字符的形式打印一些信息，看不到新添的信息
console.dir(fn);//显示一个对象所有的属性和方法
console.log(fn.b)//进行调用
```

#### Argument Passing

传递参数 

copying values

##### for primitive values

指向基本数据类型的变量相当于包含了数据,并且它们是完全独立的拷贝，互不干涉,num1的值进行改变，num2不会受到影响

```javascript
// Each of these variables can now be used separately with no side effects. 
var num1 = 5; 
var num2 = num1; 

++num1;
console.log(a,b);
//return 10 , 5
```

##### for reference values，对象

如果一个变量绑定到一个非基本数据类型(Array, Function, Object)，那么它只记录了一个内存地址，该地址存放了具体的数据。注意之前提到指向基本数据类型的变量相当于包含了数据，而现在指向非基本数据类型的变量本身是不包含数据的。对象的引用只会传递地址，而不会传递数值。

```javascript
//var obj1 = new Object(); 
var obj1 = {};
var obj2 = obj1; 
obj1.name = 'Nicholas'; 
alert(obj2.name);    //”Nicholas” 

var obj1 = {};
var obj2 = obj1; 
obj1.name ='wowowo'; 
console.log(obj2.name)
//"wowowo"

var obj1 = {};
var obj2 = obj1; 
obj1.name ='wowowo';
console.log(obj2)
//{name: "wowowo"}
```

```javascript
function addTen(num) {
  //num 是局部变量
  num += 10;
  return num; 
}
var count = 20; 
var result = addTen(count); 
alert(count);    //20 - no change 
alert(result);   //30 
```

<mark>All arguments in ECMAScript are passed by value. It is not possible to pass arguments by reference.所有参数传递的都是值，都是按值传递，不可能通过引用传递参数，但访问变量有按值和按引用两种方式</mark>

按值传递：将函数外部的值复制给函数内部的参数，就把值从一个变量，复制到另一个变量一样。

引用类型值的传递，则如同引用类型变量的复制一样。P69-70

在向参数传递基本类型的值时，被传递的值会被复制给一个局部变量（argument）

在向参数传递引用类型的值时，会把这个值在内存中的地址复制给一个局部变量，将地址作为一个值传递。因此这个局部变量的变化会反映在函数的外部。

https://blog.fundebug.com/2017/08/09/explain_value_reference_in_js/

https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0?gi=b49510327a3a

### this object

1. 函数自己被调用

   - 在严格模式下，this没有指向，他的值是undefined
   - 非严格模式下，默认指向window

2. 函数的实例

   new了一个实例，this指向这个实例,constructor pattern,构造函数模式

3. 函数被作为某个对象的方法调用

   - 全局函数中this = window,函数被作为某个对象的方法调用时，this等于那个对象。匿名函数的执行环境具有全局性，其this通常指向windows

##### 函数自己被调用

```javascript
//函数自己被调用
function test(){
  cosole.log(this)
}
test()
//window

//use strict
fucntion test2(){
  'use strict'
  console.log(this)
}
test2()
//undefined
```

##### 函数的实例

```javascript
function Person(name, age, job){
  this.name = name;
  this.age = age;
  this.job = job;
  this.sayName = function(){
    alert(this.name);
  };    
}
//创建Person的新实例，必须使用new操作符
var person1 = new Person(“Nicholas”, 29, “Software Engineer”); 
var person2 = new Person(“Greg”, 27, “Doctor”); 

function test3(){
  cosnole.log(this)
}
new test3()
//test3{}
```

##### 函数被作为某个对象的方法调用

```javascript
var name = “The Window”;
var object = {
  name : “My Object”,
  getNameFunc : function(){
    return function(){
      return this.name;
    };
  } 
};
alert(object.getNameFunc()());  
//”The Window” (in non-strict mode) 
//匿名函数没有取得其包含作用域（外部作用域）的this对象
//匿名函数的执行环境具有全局性，其this通常指向windows
```

```javascript
var name = “The Window”;
var object = {
  name : “My Object”,
  getNameFunc : function(){
    var that = this;
    return function(){
      return that.name;
    };
  } 
};
alert(object.getNameFunc()());  
//”My Object” 
```

#### scope 作用域

全局执行环境是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

#### block-level scopes 

块级作用域

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

回想上逐级查询与给定名字匹配的标识符，indentifier,找到即停止。

```javascript
var color = “blue”;
function getColor(){
  var color = “red”;
  return color; }
alert(getColor());  //”red” 
```
