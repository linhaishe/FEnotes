## 函数实例

instance

以前咱们使用new操作符，生成一个函数（它被称为构造函数、构造器）的实例。
在这种情况下，你也可以说，我们获得的这个值，它是函数（它其实就是引用类型）的一个实例。看上面这段话，“你获得的实例，是引用类型的一个实例”。基本上，所有的“引用类型的值”，都是 Object 类型的实例。

原文理解：

引用类型的值(对象)是引用类型的一个实例，引用类型是一种数据结构，用于将数据和功能组织在一起，它也被(incorrectly)称为类，尽管这是门面向对象的语言，但他不具备面向对象语言所支持的类和接口等基本结构。引用类型有时候也被称为对象的定义。因为它们描述的是一类对象所具有的属性和方法。

## 获得对象的实例有二种方法

1. function xxfn(){}

   `var _xx = new xxfn();`

   这是使用new 操作符，获得构造器xxfn的一个实例

   

   创建一个实例，其实是生成 Object 对象的一个实例，就这样，
   	`var _obj = new Object();`

新对象是使用new操作符后跟一个构造函数constructor来创建的。构造函数本身就是一个函数，只不过该函数是出于创建新对象的目的而定义的。

之前咱们说过，Object是js当中所有对象的基础。所以， Object 它也是一个引用类型，所以， 咱们所获得的 _obj，这个实例，它也是引用类型的值。

这行代码创建了object引用类型的一个新实例，然后把实例保存在变量_obj中。使用的构造函数是Object，他只是为新对象定义了默认的属性和方法。

### Create object

1. new操作符创建 object,new operator 

use the new operator with the Object constructor

```javascript
var person = new Object(); 
person.name = “Nicholas”; 
person.age = 29; 

var person = {};   //same as new Object() 
person.name = “Nicholas”; 
person.age = 29; //odd
```

2. 对象字面量表示法 Object literal notation 

```javascript
var person = {
  name : “Nicholas”,
  age : 29 //注意这里没有逗号
}; 
```

```javascript
var person = {
  “name” : “Nicholas”,
  “age” : 29,
  5: true 
};
//JSON?
```

The best approach is to use named arguments for those that are required and an object literal to encompass multiple optional arguments. 

### access object properties

1. dot notation
2. bracket notation

```javascript
alert(person[“name”]);    //”Nicholas” 
alert(person.name);       //”Nicholas” 
person[“first name”] = “Nicholas”; 
```

## 引用类型最常见的就是二种类型

1. 函数，function；

   函数是可以重复使用的代码段；

2. 对象字面量，{}

   从数据的角度来讲，它是一种数据结构，可以将数据和功能，组织在一起。

```javascript
var o = {
		a:123
  //这是数据；同时a也是对象o的属性
		fn:function(){
			// 这里就是功能，可以做一些逻辑上的操作
			// fn是函数，同时它也是对象 o 的属性，只不过，这个fn属性里保存的是一个匿名函数，这时，fn它就是一个js函数表达式
		}
	}
```

从传统语言的角度来讲，可以把上面的 o ，称为类。
但是在Js里，并没有类，所以一般也不那么称呼。

在使用 {} ，对象字面量表示法的，定义一个对象的时候，并没有调用 Object 构造函数。

对象字面量，它的属性都是字符串。如果不是，那么在实际工作时，会自动转换为字符串。
var o = {5:123}，这个属性5，在实际工作中会自动变成"5"

在实际工作中，使用对象字面是向函数中传入大量数据的最好的方法。

## 对象字面量向函数传值

```javascript
function xxfn( _obj ){
	console.log( _obj )
	// for(var i in _obj){
	// 	// console.log( i )
  // 输出键 name,5,age
	// 	console.log( _obj[i] )
  // 输出值 123,abc,今年18岁
	// }

	// 这是方括号表示法
  //使用_obj.5 会报错
	console.log( _obj["5"] )
}

xxfn({
	name:123,
	5:'abc',
	age:'今年18岁'
});
```

## 对象没有 .length 属性

也可以说，有 .length 属性，但它的值是 undefined

因为对象是一组无序的键值对的集合。
在数据结构上来讲，对象也可以说是字典的结构。
就是根据它的键，可以获得对应的值。

所以，使用for循环来操作对象时，要使用 for in
Js，它还支持方括号表示法，来访问对象的属性。
这样写的时候，就是用引号，把要访问的属性放在方括号里。

这种方式，一般用于函数内要操作的对象，
它的属性是不确定的。

结论，我们可以通过变量的方式，来添加或访问对象的属性。

```javascript
//一般用于函数内要操作的对象，它的属性是不确定的。
var xx = 'name'
function xxfn(){
	var _o = {}
	_o[xx] = 456;
	console.log( _o )
}
// xxfn();
//输出456

// more info to constructor pattern
function fnObj( _configObj ){
	console.log( _configObj )
	
	for(var i in _configObj){
		console.log( i )
		this[i] = _configObj[i]
	}

	console.log( this )
}
// 必须生成一个实例，让this指向 fnObj 这个对象
new fnObj({
	name:'我是老尚',
	age:'今年18',
	face:'长的白，好看'
})
```

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
alert(person1.sayName == person2.sayName);  //false 
//指向同一个构造函数Person
alert(person1.constructor == Person);  //true 
alert(person2.constructor == Person);  //true 

alert(person1 instanceof Object);  //true 
alert(person1 instanceof Person);  //true 
alert(person2 instanceof Object);  //true 
alert(person2 instanceof Person);  //true 
```

## function

函数其实是对象，每个函数都是Function类型的实例。

1. 函数声明的语法，function xx(){}
2. 函数表达式：var xx = function(){}
   通过xx，即可以引用到函数。
3. var xxfn = new Function();
   不推荐，因为它会导致函数被解析二次

### no overloading

没有重载
再一次强调一个概念，
1、函数名，不是函数本身；
2、函数名，是一个地址，它指向函数在内存中的位置；

因为函数、实例什么的，都是引用类型。
也就是说，我们可以认为，函数名和变量没什么区别。

定义了两个相同名字的函数，则改名字只属于后定义的函数。

```javascript
function addSomeNumber(num){
  return num + 100; 
}
function addSomeNumber(num) {
  return num + 200; 
}
var result = addSomeNumber(100);    //300 

//从上到下执行就直接覆盖了
var xxfn = function(n){
	console.log( n+1 )
}

xxfn = function(n){
	console.log( n+2 )
}
// xxfn(2)

```

## function

### 定义函数的方式

1. 函数声明 function declaration
2. 函数表达式 function expression，Function expressions have several forms.

```javascript
//function declaration
function functionName(arg0, arg1, arg2) {
  //function body 
} 

```

```javascript
//function expression,the most commom is as follows
//anonymous function 匿名函数
var functionName = function(arg0, arg1, arg2) {
  //function body  
};

```

### 函数声明、函数表达式的区别

1. 函数声明是

   function xxfn(){}

2. 函数表达式是给变量赋值
   var xx = function(){}

函数声明，在js代码执行之前，有一个js词法分析的过程，
它会创建一个js的源码树，这是一个概念，不可见。在执行这个过程的时候，会有一个【函数声明分析】的过程，会把函数声明，提到的最顶部。

所以，即使你对函数的调用，在它的定义之前，也是没有问题的。

### function declaration hoisting 

函数声明提升

在执行代码之前会先读取函数声明，可以把函数声明放在调用他的语句后面。

```javascript
sayHi(); 
function sayHi(){
  alert(“Hi!”); 
}
//never use,尽管这个function是对的
//error

```

```javascript
var sayHi = function(){
  alert("hi");
};
sayHi();
//没有函数声明提升 function expression

```

1. 在js执行之前，js引擎会先读取函数的声明，
   	并让它在真正执行之前就可用；

2. 函数表达式，是js引擎执行到它所在的那一行时，
   	它才会真正的被解释执行。

<!-- Js的词法分析 -->
词法分析，它纯是js背后的理论，如果你不了解，对你使用js也没什么太大的影响。只是说，有一些js代码运行中的现象，你可以会用，但不知道为什么。

其实就是知其然，和知其所以然的区别。

<!-- 主要用三个阶段 -->
1、分析参数；
2、分析变量的声明；
3、分析函数

<!-- 具体步骤 -->
1、函数在运行的瞬间，（瞬间是指，在js引擎已经读取js，但并没有执行，且刚刚开始进行词法分析的，那一刻）

2、会在内存中生成一个活动对象（Active Object）
简称AO，AO对象，这个对象不可见，不可操作，不可获取

3、分析参数，
函数接收到的形参，把它添加到AO对象，做为属性，此时它的值是undefined，例如，AO.a = undefined

<!-- 
形参parameter，就是函数定义时的参数名，function xxfn(a,b,c)
a,b,c就是形参
 -->

<!-- 
实参argument，就是函数调用时，向函数中传入的值，
xxfn(1,2,3)，这个1，2，3就是实参。
此时，函数xxfn中的a,b,c，它们的值分别就是1，2，3
 -->

4、接收实参，也把它添加到AO对象，覆盖之前的undefined，
	就这样，AO.a = 1

5、分析局部变量的声明，
	<!-- 就是说，函数当中的变量的声明。 -->
	例如var a;
	如果在分析局部变量的时候，
	1、还没有a，那么把它的值置为undefined
	2、如果AO上面已经有了a属性，那么不做任何的修改

6、分析函数的声明，它的规则只有一条，
	如果有 function a(){}，
	那么，把函数赋值给AO.a，覆盖之前的AO.a，
	这时，AO.a就指向了function a(){}

<!-- 上面是这几条规则，我说的未必正规，
但肯定没错，事就是这么个事 -->

看，词法分析1.html、词法分析2.html

<!--  -->

词法分析，是一个难点，今天就这么多，不再继续往下讲了。
也不再举更多的词法分析的例子了，因为没有必要，
它的规则都是一样的。