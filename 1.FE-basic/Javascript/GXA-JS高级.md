## 1. js的执行顺序

1. 从上到下，从左到右

2. 遇到等号，先执行等号右边的

3. 遇到return，先执行return右边的，并终止向下运行代码，不解析后面的代码了。

4. 建议 return 后面加分号

5. 遇到括号，先算括号里面的    

   `alert(show())`,先执行show(),后将运行alert()

## 2. 预解析(变量/函数提升)

### 定义

系统在开始执行的时候，会把变量的定义，和函数的定义，提前。仅仅是定义提前。赋值不提前。

```js
var a = 1;
alert (a);
//output 1

alert (a);
var a = 1;
//output undefined,说明a声明了，但是没有赋值
//即相当于以下
var a
alert (a);

var a;
console.log(a);
//undefined

function show(){
  alert(a);
  var a = 1;
}
show();
//equal to 
//如果是在函数内，提到函数的开始位置,预解析
function show(){
  var a
  alert(a);
  a = 1;
}
show();
//undefined

function show(){
  alert(a);
  var a = 1;
}
show();
//undefined
alert(a)
//undefined

//这个是没有作用域的，变量还是被提升了
alert(a);
if(true){
  var a=1;
}
//undefined

if(true){
  var a=1;
}
alert(a);
//1

show();
function show(){
  alert(1)
};
//1
//函数的定义也会提升
```

### undefined出现的情况
1. 变量声明了，但没有赋值

2. 函数定义形参但没有传值

   ```js
   function f(x = 1, y) {
     return [x, y];
   }
   
   f(); // [1, undefined]
   f(2); // [2, undefined]
   ```

3. 函数没有返回值

```js
var a='1';
function k(){}
```

4. 对象取属性值，属性值不存在

### 预解析有作用域

1. 如果是在函数内，提到函数的开始位置，只有函数才有作用域
2. 如果是在script标签内提到script标签的开始地方

```html
<!--undefined-->
<script>
   alert(a);
</script>
<script>
    var a=1;
</script>

<script>
  //undefined
  show();
</script>
<script>
  function show() {
    alert(1);
  }
</script>
```

## 3. 函数的两种定义的区别

**函数表达式,变量名会预解析,赋值不会提前**

1. 命名式函数

   ` function show(){}`

2. 表达式定义

   `var show=function(){}`

```js
var show=function(){
  alert(1);
}
show();
//1

show();
var show = function () {
  alert(1);
};
//show is not a fucntion
//只把变量提前了，还没有赋值函数，调用失败
```

## 4. 声明变量不加var，成为全局变量

```js
  // a=1;
  // alert(a);

  function show() {
    var a = 1;
  }
  show();
  alert(a);
  //a is not defined

  function show() {
    a = 1;
  }
  show();
  alert(a);
//1
```

## 5. 赋值表达式

```js
//不能用赋值表达式声明多个变量,后面的会变成全局变量
  function show(){
      var a=b=c=d=1;
  }
  show();
  console.log(c,d);
//成为全局变量，后面的bcd没有用var 进行声明，外部就可以访问内部。
//1
 console.log(a);
//局部变量
//undefined

  function show() {
    var a = 1,
      b = 2,
      c = 3;
  }
  show();
  console.log(c);
//c is not defined
```

## 6. 全局变量和局部变量

全局变量：只要定义了在任何地方都可以使用  `a = 1,var a = 1 `
局部变量：只能在当前的作用于内使用,函数作用域内  `var a = 1`

| --       | 变量的生命周期                     | 是否占内存 |
| -------- | ---------------------------------- | ---------- |
| 全局变量 | 只要程序开启，永远存在             | 占         |
| 局部变量 | 函数调用的时候诞生，函数调用完消亡 | 不占       |

## 7. 逗号表达式

逗号两边的都会执行

```js
var a=(6,1,2,3,4,5);
console.log(a);
//5
//因为不断赋值再赋值，最后取到赋值5

逗号两边的都会执行
  for (var i = 1, j = 2; i < 3, j < 4; i++, j++) {
    console.log(i, j);
    // 1 2
    //2 3
  }
```

## 8. js的严格模式

**作用是为了修复js里面的bug和问题**

### 如何开启严格模式

`'use strict'`

1. 加在函数内，函数里面的东西是严格模式
2. 在script标签内。
3. 加在js文件内

**严格模式也有作用域**

### 严格模式和普通模式的区别

1. 声明变量必须加var
2. 不能在if或者for里面定义函数
3. this指向有区别，单独的函数调用不指向window,指向的是undefined,（但是全局的变量声明window还是能获取。如下图y）本质的原因是,在严格模式下全局的东西不属于window了,他不属于任何人,他指向undefined.减少window的使用率。使得性能提升，不把所有东西放在window里
4. 严格模式下，不能用delete删除变量

![03015A42867258A4B0BE2F420EA90712.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grlfjr6zhsj60eq0cigmn02.jpg)

```js
'use strict'
a=1;
alert(a);
//undefined

 "use strict";
  if (true) {
    function show() {
      console.log(1);
    }
  } else {
    function show() {
      console.log(2);
    }
  }
  show();
//而是show is not defined
//不用"use strict"是弹1，因为浏览器做了优化，按理来说，两个都会被预解析，两个show函数都会上升，按逻辑来说应该弹2
//不要在if等条件语句内定义函数
```

```js
 if (true) {
    function show() {
      console.log(1);
    }
  } else {
    function show() {
      console.log(2);
    }
  }
  show();

```

## 9. 关于this指向

| this位置                                                     | this指向                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 用在函数外，全局函数                                         | this 指向  window `console.log(this)`                        |
| 用在普通函数内,主要分辨是谁调用了这个函数，则这个this就指向谁 | 1、函数直接调用this指向window<br/>2、在事件内部this指向触发事件的元素<br/>3、定时器this指向window<br/>4、对象里面的方法  指向这个方法属于的对象<br/>5、自执行匿名函数this指向window |
| 用在构造函数里面                                             | this指向，函数里面创建的空白对象,指向实例，无法打印，控制台里显示的是构造函数 |
| 用在箭头函数内                                               | this 指向  window                                            |

```js
//全局函数和全局变量都是属于window的，分辨是谁调用了这个函数则这个this就指向谁。

var a=1;

//window call
function show(){
console.log(this);
  //this = window
}

show();

console.log(window.a);
console.log(window.show());

//在事件内部，this指向触发事件的元素
//document call show function
document.onclick = show;
//this = #document

//arr调用,this指向arr,arr里添加了一个函数
var arr=[1,2,3];
arr.show=show;
arr.show();

```

![679F307D3FCE477E60D1F8A4B0036183.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grlf6rhu9lj60cw0by74y02.jpg)

```js
 var a = 1;
  var json = {
    a: 2,
    b: {
      a: 3,
      b: function () {
        console.log(this.a);
      },
    },
  };
  json.b.b();
//3
//因为是b调用，所以this指向b

//构造函数this指向实例
class Polygon {
  constructor() {
    this.name = 'Polygon';
  }
}

const poly1 = new Polygon();

console.log(poly1.name);
// expected output: "Polygon"
```

## 10. eval()

正常情况下，字符串中的代码片段是不执行的。功能强大，会有隐患。

```js
console.log('12'+'+'+'5');
//是字符串，不能进行运算

var str = "12+5"
console.log(eval(str));
//17

var fn = "function show2(){console.log(1)}"
eval(fn);
show2();
```

## 11. apply(),call(),bind()

都用于更改this指向

### a. call( )

`fn.call(this的指向,参数1，参数2，参数3)`

```js
function show(){
console.log(this);
}

show.call(1)
//1

//传参
function show(a,b,c){
	console.log(this);
	console.log(a,b,c);
}
show.call("aaa",1,2,3)
//aaa
//1 2 3

//经常用于函数借用

let person1 = {
  firstname: "heather",
  lastname: "chen",
  printFullName: function () {
    console.log(this.firstname + " " + this.lastname);
  },
};

person1.printFullName();

let person2 = {
  firstname: "Linda",
  lastname: "xu",
};

//function borrowing
//借用有某个函数方法的函数，先直接调用，调用后使用call 或者 apply 方法，将this的指向改为我们需要的对象。
person1.printFullName.call(person2);
```

### b. apply( )

和call的区别在于，参数放在数组里进行传递,并将数组的内容分成单个单个进行处理

```js
function show(a,b,c){
	console.log(this);
  console.log(a,b,c);
}
show.apply("aaa",[1,2,3])
//aaa
//1 2 3

var array = ['a', 'b'];
var elements = [0, 1, 2];
array.push(elements);
console.info(array); 
//["a", "b", Array(3)]

var array = ['a', 'b'];
var elements = [0, 1, 2];
array.push.apply(array, elements);
console.info(array); 
// ["a", "b", 0, 1, 2]

let personName = {
  firstname: "heather",
  lastname: "chen",
};

let printFullName = function (hometown,province) {
  console.log(this.firstname + " " + this.lastname + " from " + hometown + province);
};

//区别在于call中参数分开传
let test = printFullName.call(personName,"zhognguo","beijing");

let personName2 = {
  firstname: "heather",
  lastname: "xu",
};

//apply中参数用数组进行传递
let test2 = printFullName.apply(personName2,["zhongguo","hk"]);

console.log(test);
console.log(test2);

let printMyName = printFullName.bind(personName2, ["zhongguo", "hk"]);

console.log(printMyName);
//it will return a function of printMyName
//ƒ (hometown,province) {
 // console.log(this.firstname + " " + this.lastname + "from" + hometown + province);
//
//invoke function
printMyName();
//heather xufromzhongguo,hkundefined


```

### c. bind( )

调用完返回的是一个改变了this指向的函数。

```js
function show(a,b,c){
	console.log(this);
  console.log(a,b,c);
}
var fn = show.bind("aaa");
fn();
//"aaa",undefined,undefined,undefined
function show(a,b,c){
	console.log(this);
  console.log(a,b,c);
}
var fn = show.bind("aaa",1);
fn(2,3);
//"aaa",1,2,3
```

![F6F0E4771C6AE418992009F2AEEBBADB.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grlg773be7j60to0g20uy02.jpg)

## 12. in的用法

查看属性是否属于对象,undefined and name 都属于window

```js
var json = {a:1};
console.log("b" in json);
//false

var a = 1;
cosnole.log('a' in window);
//true

//询问的是1是不是属于window,window里没有1这个属性
var a = 1;
cosnole.log(a in window);

//因为变量提升，预解析，虽然不走if语句，但是预解析了
if(flase){
  var a = 1;
}
console.log("a" in window);
//true

if(flase){
  var a = 1;
}
console.log(a in window);
//undefined 属于window
//true
//以下方便理解

var a;
if(flase){
   a = 1;
}
//则询问var a = undefined,undefined是否属于window
console.log(a in window);
//true


```

## 13. example

```js
//如果变量没有赋值，先提的变量，后提的函数。弹出的就是函数
//如果赋值了，最后执行的是赋值

//example 1
var a = 1;
function a(){
	console.log(1)
}
console.log(a)
//1

//原理如下,变量提升后再赋值
var a;
function a(){
  console.log(1)
}
a=1;
console.log(a)
//1

//example 2
var a;
function a(){
  console.log(1)
}
console.log(a)
//返回a函数

function a(){
  console.log(1)
}
var a;
console.log(a)
//还是返回函数

//如果参数传了，变量没赋值，看参数
//如果参数没传，变量赋值了，看变量
//如果都有，看变量
  function show(a) {
    var a;
    alert(a);
  }
  show(1);
//1

  function show(a) {
    var a=2;
    alert(a);
  }
  show(1);
//2

//变量和参数都没赋值,看函数
//参数有，变量没赋值，看函数
//参数有，变量有，看变量   
  function show(a) {
    var a;
    function a() {}
    alert(a);
  }
  show();
//函数，因为二次赋值

  function show(a) {
    var a;
    function a() {}
    alert(a);
  }
  show(2);
//函数，因为二次赋值

  function show(a) {
    var a=4;
    function a() {}
    alert(a);
  }
  show(2);
//4

```

## 14. 总结

### 变量名和函数名还有参数名相同的时候
#### 变量和函数
如果变量没有赋值，先提的变量(预解析)，后提的函数(预解析)。弹出的就是函数
如果赋值了，最后执行的是赋值

#### 变量和参数
如果参数传了，变量没赋值，看参数。
如果参数没传，变量赋值了，看变量
如果都有，看变量

#### 变量 函数 参数
变量和参数都没赋值  看函数
参数有，变量没赋值，看函数
参数有，变量有，看变量    

```js
//因为数组和对象和函数是引用数据类型，是引用传递
var arr = [1,2,3];
var arr2 = arr;
arr2.push(4);
console.log(arr,arr2);
//[1,2,3,4],[1,2,3,4]

var json = {a:1};
var json2 =json;
json2.b=2;
console.log(json,json2);
//{a: 1, b: 2} {a: 1, b: 2}
```

<mark>引用数据类型老师没有讲的很清楚，需要看小红书</mark>

## 15. let & const

### Let  和 var 区别

1. let会形成块级作用域
2. Let不会出现变量提升
3. let不能重复定义
4. let 声明的东西不在顶层作用域window里

### 好处：

1. 可以代替自执行匿名函数的用法
2. for 循环里面加事件，会避免i形成错误数据

```js
//	a 只能在作用域中生效
if(true){
	let a = 1;
}
console.log(a)
//not defined

//形成局部变量互不影响，实现多人写代码，防止变量同名
(function(){
  var a = 1;
})();

(function(){
  var a = 1;
  //...
})();

//同上的功能，不同的写法，比较少用
{
  let a = 1;
}

{
  let a = 1;
}
```

```html
<button>1</button>
<button>2</button>
<button>3</button>
```

```js
var aBtn = document.querySelector('button');

for(var i=0;i<aBtn.length;i++){
  aBtn[i].onclick=function(){
    alert(i)
  }
}
//3

//解决方法
//1. 加自定义属性
//2. 创建自执行匿名函数
//3. let 声明

var aBtn = document.querySelector('button');

for(var i=0;i<aBtn.length;i++){
  (function(index){
   aBtn[i].onclick=function(){
    alert(index)
  }
  })(i)
}
//0 1 2

//每次在循环的时候都产生了块级作用域，获得的都是当前的0 1 2
for(let i=0;i<aBtn.length;i++){
  aBtn[i].onclick=function(){
    alert(i)
  }
}
```

```js
//不会变量提升
console.log(a);
let a = 1;
console.log(a);
//a is not defined

//不能重复声明
let a = 1;
let a = "aaa";
//Identifier 'a' has already been declared
```

### const 和 let 区别

const 定义常量，常量是只要定义了就不会变

`const express=require('express')`

1. 变量声明后，不能被修改
2. 常量定义后必须要给赋值

```js
//变量声明后，不能被修改
const c = 1;
c = 2;
console.log(c)
//Assignment to constant variable.
//赋值给常量变量。

const b;
b = 2;
console.log(b);
//Missing initializer in const declaration
```

## 15. 解构赋值

通过等号两边相同的格式，把右边的数据，赋值给左边的变量

```js
let [a,b,c]=[1,2,3]

var [a, b, c, d] = [1, 2, 3, 4];
console.log(a, b, c, d);
//1 2 3 4

var { a, b, c } = {
  a: 1,
  b: 2,
  c: 3,
};

var [a, { b }, c] = [1, { b: 2 }, 3];
console.log(a, b, c);
//1 2 3

//默认值的设置
let [a,b,c]=[1,2];
console.log(a, b, c);
//1 2 undefined

let [a,b,c=3]=[1,2,4];
console.log(a, b, c);
//1 2 4

let [a,b,c=3]=[1,2];
console.log(a, b, c);
//1 2 3

//重命名
var {aa,bb,cc}={
    a:1,
    b:2,
    c:3
}
console.log(aa,bb,cc)
//undefined undefined undefined
var {a:aa,b:bb,c:cc}={
    a:1,
    b:2,
    c:3
}
console.log(aa,bb,cc)
//1 2 3


function ajax({ url, data = {}, type = "get" }) {}

ajax({
  url: "/login",
  data: { a: 1 },
  type: "post",
  success: function () {},
});

var a = 1;
var b = 2;
var [a, b] = [b, a];
console.log(a, b);

let { a } = { a: 1, b: 2, c: 3 };
console.log(a);
//1

let { a } = { a: 1, b: 2, c: 3 };
let json = { a: 1, b: 2, c: 3 };
console.log(a);
```

## 16. 面向对象

[廖雪峰面向对象](https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528)

面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

就是把数据和操作数据的函数封装起来，方便多次使用。

[Chapter 6 :Object-Oriented Programming-js高程 ](/Users/xusumu/OneDrive/1.notes/2.FE/Javascript/jsprofessional-wrox.md)

[chapter 18.【重点】面向对象基础-thoughtworks](/Users/xusumu/OneDrive/1.notes/2.FE/2.thoughtworks/JS/JavaScript-thoughtworks.md)

单例模式，工厂模式，构造模式，原型模式，构造和原型混合模式(combination constructor/prototype pattern)

### es6 对象的写法

```js
//es6之前;
var obj = {
  age: 1,
  name: "heather",
  alertFn: function alertFn() {
    console.log(this.name);
  }
};
//es6
//如果属性值和变量的值相同，则可以简写成一个变量名即可。
var age = 1;
var obj = {
  age
};

//简写成;
var age = 1;
var obj = {
  age,
  name: "heather",
  alertfn() {
    console.log(this.name);
  }
};
```

![6772ABDAE745A63B280A597541EA92E5.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grnmhef7nbj60fa0gcwfo02.jpg)

### es6 面向对象的写法

```js
class Dog {
  constructor(name, color) {
    //变量属性放这里
    this.name = name;
    this.color = color;
  }
  //函数单独写
  showName() {
    alert("我的名字叫" + this.name);
  }
  eatting() {
    alert("汪汪汪");
  }
}

let d1 = new Dog("旺财", "白色");
d1.showName();
```

### es6之前的继承

```js
function Person(name, age, job){
  this.name = name;
  this.age = age;
  this.job = job;
  this.friends = ["Shelby", "Court"]; 
}
Person.prototype = function sayName() {
      alert(this.name);
};

//example
function Cat(name, age) {
  this.name = name;
  this.age = age;
}
Cat.prototype.sound = function () {
  alert("我叫" + this.name + ",我会喵喵叫！");
};
new Cat("喵喵", 1);

//子级
function OrangeCat(name, age) {
  //Cat.call(this,name,age);
  //使其拥有父级的属性
  Cat.apply(this, arguments);
}
//这样的写法导致父子的原型都连在一起了，改了子集的原型父级的原型也会被修改，不建议使用。
//OrangeCat.prototype =Cat.prototype;
OrangeCat.prototype = new Cat();
let org = new OrangeCat("小橘", 2);
org.sound();
```

### es6的继承

```js
//父级
class Cat {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  sound() {
    alert("我叫" + this.name + ",我会喵喵叫！");
  }
}
new Cat("喵喵", 1);

//子级
class OrangeCat extends Cat {
  constructor(name, age) {
    //将属性指向父类，如果直想继承name，就只写name,age不会被继承
    super(name, age);
  }
}
let org = new OrangeCat("小橘", 3);
org.sound();

//传参方法2
class OrangeCat extends Cat {
  //...args变成数组进行接收
  constructor(...args) {
    //将数组进行分解
    super(...args);
  }
}
let org = new OrangeCat("小橘", 3);
org.sound();
```

## 17. 检测数据类型

### a. typeof

### b. instnceof:

检测是否有关系。

`instanceof` 是用来判断 `A` 是否为 `B` 的实例，表达式为：`A instanceof B`，如果 `A` 是 `B` 的实例，则返回 `true`,否则返回 `false`。

```js
var arr = new Array(1, 2, 3);
var oDate = new Date();

console.log(arr instanceof Array);
console.log(arr instanceof Object);
console.log(arr instanceof Date); //false
console.log(oDate instanceof Date);
console.log(oDate instanceof Object);
console.log(oDate instanceof Array); //false

//the relationship between function and object
console.log(Function instanceof Object); //true
console.log(Object instanceof Function); //true
console.log(Object instanceof Object); //true
console.log(Function instanceof Function); //true

let arr = [1, 2, 3];
console.log(arr instanceof Array); //true
console.log(Array instanceof Function); //true
//本质是arr是构造函数产生的实例，本质是一个对象，不属于function,arr不是构造函数
console.log(arr instanceof Function); //flase
console.log(arr instanceof Object); //true

//简写的创建方式虽然使用方式是一样的，但是不是new出来的，就属于对象的大类里面，对象里面的包装类，平常用是没有区别的，但是在检测的时候会有区别。
//js的包装类 number,string,boolean

let str='aaa';
//因为不是String的实例
console.log(str instanceof String);//false
console.log(String instanceof Object)//true
console.log(str instanceof Object)//false

let num=12;
console.log(num instanceof Number);//false
console.log(Number instanceof Object)//true
console.log(num instanceof Object)//false

let str1 = new String("aaa");
console.log(str1 instanceof String); //true
console.log(String instanceof Object); //true
console.log(str1 instanceof Object); //true


```

### c. constructor

检测是否是其实例，是否是其构造出来的,是否是其直接父级。

```js
let arr = new Array(1, 2, 3);
let oDate = new Date();
console.log(arr.constructor == Array);//true
console.log(arr.constructor == Date);//false
console.log(arr.constructor == Object);//false
```

### d. toString

toSting功能在object上，所以所有的number, array,string的功能都可以使用,但是每个的数据类型上功能都略有区别。

判别到底是谁调用了toString的方法，其他的数据类型都是直接转化成字符串。

```js
//toString
var n = 12;//12
var b = true;//true
var arr = [1, 2, 3];//1,2,3
//对象上的toString的方法是用于判别谁调用了toString方法
var json = { a: 1 }; //[object Object]
var reg = /aaa/;// /aaa/
alert(json); //[object Object]
//alert的东西都是自动转成字符串的
console.log(n.toString())
console.log(b.toString())
console.log(arr.toString())//1，2，3
console.log(json.toString())
console.log(reg.toString())

//直接使用祖宗上的toString的方法，但是toString本身是不能传参数的，我们通过call方法进行this指向更改。
console.log(Object.prototype.toString.call(n)); //[object Number]
console.log(Object.prototype.toString.call(b)); //[object Number]
console.log(Object.prototype.toString.call(arr)); //[object Number]
console.log(Object.prototype.toString.call(reg)); //[object Number]
console.log(Object.prototype.toString.call(new Date())); //[object Number]
console.log(Object.prototype.toString.call(function () {})); //[object Number]
console.log(Object.prototype.toString.call(json)); //[object Number]

function testType(val) {
  let str = Object.prototype.toString.call(val).split(" ")[1];
  return str.substring(0, str.length - 1);
}
console.log(testType(n));
console.log(testType(b));
console.log(testType(arr));

```



## 18. 检测属性是否属于这个对象

hasOwnProperty(): 指示对象自身属性中是否具有指定的属性,在继承函数中，prototype上的属性是继承过来的，新实例本身是没有这个属性的，所以会返回false

```js
let json = { age: 1 };

//第一种检测方式 in
console.log("age" in json)//true
console.log(json.hasOwnProperty("age"));//true

function Dog(name) {
  this.name = name;
}
Dog.prototype.age = 1;
let d1 = new Dog("旺财");
console.log("name" in d1);//true
console.log(d1.hasOwnProperty("name"));//true

console.log("age" in d1);//true
//检测是否是原型上面的属性
console.log(d1.hasOwnProperty("age"));//false

function HuskyDog(name) {
  Dog.call(this, name);
}
HuskyDog.prototype = new Dog();
let h1 = new HuskyDog("二哈");
console.log("name" in h1);//true
console.log(h1.hasOwnProperty("name"));//true

console.log("age" in h1);//true
console.log(h1.hasOwnProperty("age"));//false

```

## 19. 原型的利用

在原型本来就有的功能上添加功能。有些功能低版本浏览器不兼容，我们可以在原型方法的基础上添加兼容功能，即写原生的js方法即可使得低版本浏览器兼容。

如果我想要的功能要在number, object,array中进行使用的话，需要在object上进行更改和添加即可。

```js
/*
兼容低版本浏览器，indexOf只兼容高级浏览器，但是在写兼容的时候也要用作者写的内容，
所以要加上下面的判断，如果浏览器支持indexOf功能的话，则使用作者写的内容。
如果浏览器不支持则用我们自己写的方法，因为作者的方法对系统性能更好和数据响应速度更快
*/
/*
Arrar.prototype.indexOf = Arrar.prototype.indexOf || function(){}
如果浏览器存在indexOf方法则用浏览器自带的indexOF方法，否则赋值我们自写函数，实现兼容功能
*/


Array.prototype.indexOf =
  Array.prototype.indexOf ||
  function (val) {
    for (var i = 0; i < this.length; i++) {
      if (this[i] == val) {
        return i;
      }
    }
    return -1;
  };

var arr = [1,2,3];
var arr = new Array(1, 2, 3);
alert(arr.indexOf(2));

// str.trim() 也不兼容低级浏览器。
```

```js
String.prototype.trim =
  String.prototype.trim ||
  function () {
    return this.replace(/^\s+|\s+$/g, "");
  };
var str = "    aa         ";
console.log(str);
console.log(str.trim());
// str.trim() 也不兼容低级浏览器。
```

```js
Date.prototype.getCNDay = function () {
  return "星期" + "日一二三四五六".charAt(this.getDay());
};
var oDate = new Date();
console.log(oDate.getCNDay()); //'星期一'。。。。 '星期日'
//console.log(oDate.getDay())//0-6

```

## 20. 异步的处理之promise对象

[Javascript异步编程的4种方法](http://www.ruanyifeng.com/blog/2012/12/asynchronous%EF%BC%BFjavascript.html)

"同步模式"就是上一段的模式，后一个任务等待前一个任务结束，然后再执行，程序的执行顺序与任务的排列顺序是一致的、同步的；

"异步模式"则完全不同，每一个任务有一个或多个回调函数（callback），前一个任务结束后，不是执行后一个任务，而是执行回调函数，后一个任务则是不等前一个任务结束就执行，所以程序的执行顺序与任务的排列顺序是不一致的、异步的。

回调函数：在方法函数调用的时候，传进去一个函数。传进去的函数，会在方法函数的内部，在某种条件下调用

回调函数用多了。代码书写非常差,项目关于ajax有两个麻烦点,容易产生回调地狱

1. 首页数据多，同时发送多个ajax。每个ajax回来数据都要渲染一次页面。dom操作多。数据一次都过来统一渲染
2. ajax请求嵌套很多的时候，代码书写非常差

```js
            ajax({
                    url:'',
                    success:function(res){
                        ajax({
                            url:'',
                            data:{
                                a:res.a
                            }
                            success:function(res2){
                                ajax({
                                    url:'',
                                    data:{
                                        a:res.a
                                    }
                                    success:function(res){


                                    }
                                })

                            }
                        })
                    }
                })
```

### promise对象是什么

是处理异步的方法之一，每一个异步任务返回一个Promise对象，该对象有一个then方法，允许指定回调函数。有三种状态，resolved,pending,rejected.

### promise使用

ajax的封装只需要了解就可以了

```js
let p1 = new Promise((resolve, reject) => {
  //异步操作
  //resolve(成功的结果) 成功需要调用的函数 并传出结果
  //reject(失败的结果) 失败调用的函数 传出结果
});

p1.then(
  (成功的结果) => {},
  (失败的结果) => {}
);
```

```js

var a = false;
let p1 = new Promise((resolve, reject) => {
  //resolve 成功
  //reject  失败
  //放异步的，异步成功，调用resolve，失败调用reject
  if(a){
      resolve('成功')
  }else{
      reject('失败');
  }
  setTimeout(function () {
    resolve("成功了");
  }, 100);
});

p1.then(
  (res) => {
    console.log(res);
  },
  (err) => {
    console.log(err);
  }
);
```

### jquery ajax

[stage3 **0617**](https://github.com/linhaishe/GXA-assignment/tree/main/stage3/0617)

```js
//第一个请求获取的数据，作为第二个请求的参数
$.ajax({
  url: "a.txt",
})
//将res,即异步产生的结果作为参数传给下一个请求
  .then((res) => {
  //紧接着又会返回一个promise对象，也可以接着写链式调用
    return $.ajax({
      url: "a.txt",
      data: { a: res },
    });
  })
  .then((res) => {
    return $.ajax({
      url: "a.txt",
      data: { a: res },
    });
  })
  .catch((err) => {
    console.log(err);
  });

//第一个请求获取的数据，作为第二个请求的参数
let p1 = $.ajax({
  url: "a.txt",
})
//将res,即异步产生的结果作为参数传给下一个请求
  .then((res) => {
  //紧接着又会返回一个promise对象，即相当于赋值给了p1,可以接着写链式调用
    return $.ajax({
      url: "a.txt",
      data: { a: res },
    });
  })

//catch error,多个错误同时catch即可，不需要每个异步都写err func
$.ajax({
  url: "a.txt",
})
  .then((res) => {
    return $.ajax({
      url: "a.txt",
      data: { a: res },
    });
  })
  .then((res) => {
    return $.ajax({
      url: "a.txt",
      data: { a: res },
    });
  })
  .catch((err) => {
    console.log(err);
  });
```

```js
//一个页面一次性发送多个ajax请求，想要，统一进行数据渲染
let p1 = $.ajax({
  url: "a.txt",
});
let p2 = $.ajax({
  url: "b.txt",
});
let p3 = $.ajax({
  url: "c.txt",
});

 //res  是所有数据的一个数组集合
Promise.all([p1, p2, p3]).then((res) => {
  console.log(res);
});
```

```js
//promise里面不常用的;
ajax({})
  .then(() => {
    //成功时候执行的函数
  })
  .catch(() => {
    //失败时候执行的函数
  })
  .finally(() => {
    //不管成功还是失败都会执行的函数
  });

Promise.race([p1, p2, p3]).then((res) => {
  //res 是 p1,p2,p3中请求最快的一个结果。
});
```

## 21. generator function

[JavaScript Generators](https://www.javascripttutorial.net/es6/javascript-generators/)

can pause midway and then continues from where it paused.函数变成可控制的函数。

返回的数据格式{value:'返回的数据',done:true|false} ,是否结束

作为封装函数，一个功能需要三个ajax请求，可用于ajax请求，并且第一个请求获取的数据，作为第二个请求的参数，以此类推，可用yeild书写。作者后面写了新的async函数，是yeild函数的用于ajax的优化。

```js
function* show() {
  console.log(1);
}
//此方法返回一个对象
let obj = show(); //obj 对象 就相当于一个遥控器
obj.next();
//1
//{value: undefined, done: true}
```

### Yeild，能传参，暂停，返回数据

#### 暂停

```js
function* show3() {
  console.log(1);
  yield;
  console.log(2);
}
let obj3 = show(); 

obj3.next();
//1
//{value: undefined, done: false}
obj3.next();
//2
//{value: undefined, done: true}
```

#### 传参

```js
function* show(a) {
  alert(a);
  let b = yield;
  alert(b);
}
let obj = show(); //obj 对象 就相当于一个遥控器
obj.next(1); 
//undefiend
obj.next(3);
//3

function* show(a) {
  alert(a);
  let b = yield;
  alert(b);
}
let obj = show(1); //obj 对象 就相当于一个遥控器
obj.next(); //第一个next不传参数，第一部分的代码如果需要参数，函数调用传，第二部分的参数用第二个next函数传
//1
//obj.next() 改为 obj.next(2) 则不会显示2
obj.next(3);
//3
```

#### 返回数据

```js
function* show(a) {
  alert(a);
  let b = yield a + 10;
  alert(b);
  //最后一个部分用return返回值，否则返回undefined
  return b * 3;
}
let obj = show(1); //obj 对象 就相当于一个遥控器
console.log(obj.next()); //第一个next不传参数，第一部分的代码如果需要参数，函数调用传
console.log(obj.next(3));

//{value: 11, done: false}
//{value: 9, done: true}
```

## 22. Async函数

是generator函数的语法糖,语法糖就是把原本语法进行一次封装，让用法变得更加简便

```js
let show = async function () {
  //每一步完成后进行下一步，添加await
  //val1 第一次ajax请求的结果
  let val1 = await $.ajax({ url: "a.txt" });
  //val2 获得二次请求的结果
  let val2 = await $.ajax({ url: "b.txt", data: { a: val1 } });
  //如果想获得val2 则需要return出来，不过得到的是promise对象，若果想要获得val2的结果，最后一还是需要通过then方法
  return val2;
};
//不过得到的是promise对象，若果想要获得val2的结果，最后一还是需要通过then方法
console.log(show())
//获得结果
show().then((res) => {
  console.log(res);
});
```

## 23. symbol

### 定义

ES6之前对象属性名都是字符串，这容易造成属性名的冲突，为了保证每个属性的名字都是独一无二的， es6引入Symbol。

Symbol是一种新的原始数据类型,表示独一无二的值。是js的第七种数据类型，前六种是undefined,null,boolean,string,number,object

### 创建

Symbol值通过Symbol函数生成的，这就是说，对象的属性名现在可以有两种类型，原来就有的字符串，另一种就是新增的Symbol类型。凡是属性名属于此类型的，就都是独一无二的，可以保证不会与其他属性名产生冲突。

```js
let s = Symbol();
let s1 = Symbol();
console.log(s==s1)//false
console.log(s,s1)
```

### 可以接收字符串参数作为区分

Symbol函数可以接受一个字符串作为参数，表示对Symbol实例的描述，主要是为了在控制台显示，或者转字符串的时候，比较容易区分。

通过Symbol.description将描述获取出来

```js
let s1 = Symbol("s1");
let s2 = Symbol("s2");
console.log(s2,s1)
console.log(s1.description)//s1
```

![72E2DECA05E09C3673E7C0A9726F77FD.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grp1pipjxqj60b006ugm502.jpg)

### 放在对象中

需要加中括号，才是添加Symbol的方法

```js
let s1 = Symbol("s1");
let s2 = Symbol("s2");

//设置key value
var json={
  [s1]:1
}
//设置key value
console.log(json)
//{Symbol(s1): 1}
console.log(json)
json[s2]=2;
//{Symbol(s1): 1,Symbol(s2): 2}
```

![D3F5376B6B94278B2E0113505E7C8C40.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grp1tusldrj60gg0hw3zq02.jpg)

### 不可被遍历

Symbol作为属性名， 遍历对象的时候该属性不会出现在for...in、for...of循环中，也不会被Object.keys() 、Object.getOwnPropertyNames() 、JSON.stringify() 返回。

## 24. set

它是类似于数组，但其值都是唯一的，没有重复的值。

### 声明方式

```js
//不可重复 
let set1 = new Set();
set1.add(1);
set1.add(2);
set1.add(2);
console.log(set1);
//类数组,会自动将重复的数据删除
//Set(2) {1, 2}

let set2 = new Set([1,2,3,4,5]);
//Set(5) {1,2,3,4,5}
```

### 方法(增删改查)

```js
let set2 = new Set([1,2,3,4,5]);
set2.add(6);
set2.delete(6);
//查询是否存在此数据
console.log(set2.has(5));
//清空所有内容
set2.clear();
console.log(set2.size);
//0
```

### 变成真正的数组

```js
let set2 = new Set([1,2,3,4,5]);
let arr = [...set2];
let arr2 = Array.from(set2);
```

### 用于去重

```js
let arr = [1,2,2,2,2,3,4,5];
let uniqueArr = [...new Set(arr)]
```

### 如何遍历Set()

Set()获取不到下标？

For ... of and for ... in 对Set()不起作用的。

1. 使用forEach()进行Set()遍历。

2. 使用for-of遍历键值对。

```js
let set2 = new Set([1,2,3,4,5,5,5,5,5,5,5]);

for(let i = 0;i<set2.size;i++){
  console.log(set2[i]);
}
//无效

for(var i in set2){
  console.log(i)
}
//无效

//for-each循环
set2.forEach((v,i)=>{
  console.log(v,i)
})
//1,2,3,4,5
//1,2,3,4,5

//for-of
for(let i of set2){
  console.log(i)
}
//1,2,3,4,5

//for-of遍历键,keys，values获取到都是值
for(let i of set2.keys()){
  console.log(i)
}
for(let i of set2.values()){
  console.log(i)
}
//获取键值对
for(let i of set2.entries()){
  console.log(i)
}
//他的键值对就是1对1，2对2这样子的
```

![2AFBF469CE4195192484B94CFBA3DD93.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grp2miuf8vj60jk0bkjs702.jpg)

## 25. map

map键可以是任何数据类型的对象。

原始json的key只能是字符串或者symbol。

### 声明方式

```js
const m = new Map();
const o = {p:"hello world"};
m.set(o,"content");
m.set(a,1);
m.set(true,"true");
console.log(m)
```

### 方法

```js
const m = new Map();
const o = {p:"hello world"};
//增加
m.set(o,"content");
m.set('a',1);
//获取
m.get('a');
//删除
m.delete('a');
//查询
m.has('a');
//清空
m.clear();
//查询数据长度
m.size;
```

### 遍历

1. forEach()
2. For-of

- Keys() 返回键名的遍历器

- Values() 返回键值的遍历器

- entries() 返回键值对的遍历器，取出来整个对象

```js
const m2 = new Map();
m2.set('a',1);
m2.set('b',2);
m2.set('c',3);

//map指的是整个m的整体
m2.forEach((value,key,map)=>{
  console.log(value,key,map)
})

//出来的是键值对
for (let v of m2){
  console.log(v)
}

for (let v of m2.keys()){
  console.log(v)
}
//a,b,c

for (let v of m2.values()){
  console.log(v)
}
//1,2,3

for (let v of m2.entries()){
  console.log(v)
}
//["a", 1],["b", 2],["c", 3]

```

![4205E3E2E75682AC742C1C3E2C9D3780.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grp2yt7jmoj60jq0data702.jpg)

## 26. module

### es6模块化

1. 必须放在服务器环境中
2. import'xxx'直接写路径， 相当于引入文件
3. 关于路径可以写相对也可以写绝对
4. 多次引入相同的模块，只相当于一次
5. 引入模块的时候，会预加载提升到开头
6. 模块化的写法必须是严格模式，es6所有都是严格模式

### es6模块化好处

1. 一个模块一个js文件
2. 可以安需求加载，如果不需要可以不加载
3. 模块小，便于维护、减少冗余
4. 每个模块都有自己的作用域，变量都是私有变量

### 单独的文件引入

1. 是把文件所有的代码都加载一遍
2. 文件存在依赖文件，顺序必须固定。

### 1. export

export导出的是一个对象，不能直接导出变量

```js
//correct
//option 1
var a = 1;
export {a}

//option 2
export var a = 1;

//wrong
var a = 1;
export a
```

### 2. import

<mark>不直接写文件路径</mark>

```js
//import'xxx'直接写路径， 相当于引入文件
//const.js
var a = 1;
console.log(a);
export {a}

//main.js
import './const.js'
//这样引入相当于将const里文件的方法全部运行了一遍，前端会直接执行const内部的代码
```

<mark>引入模块名即可</mark>

```js
//const.js
var a = 1;
var b = 1;
console.log(a,b);
export {a,b}

//main.js
import {a,b} from './const.js'
console.log(a,b)
//1,2
```

<mark>导出名取别名</mark>

```js
//const.js
var a = 1;
var b = 1;
console.log(a,b);
export {a as aaa,b as bbb}

//main.js
import {aaa,bbb} from './const.js'
console.log(aaa,bbb)
//1,2
```

<mark>引入名取别名</mark>

```js
//const.js
var a = 1;
var b = 1;
console.log(a,b);
export {a as aaa,b as bbb}

//main.js
import {aaa as ccc,bbb as ddd} from './const.js'
console.log(ccc,ddd)
//1,2
```

<mark>全部引入并获取</mark>

```js
//const.js
var a = 1;
var b = 1;
console.log(a,b);
export {a as aaa,b as bbb}

//main.js
import * as test from './const.js'
console.log(test.aaa,test.bbb)
//1,2
```

<mark>Default 关键字</mark>

方便于不需要回头查看模块名是什么，且一个文件只能用一个default

```js
//const.js
var a = 1;
var b = 1;
console.log(a,b);
export default {a,b}

//main.js
import randomName from './const.js'
console.log(randomName.a,randomName.b)
//1,2
```

<mark>可以单独导出+default同时使用</mark>

```js
//const.js
var a = 1;
var b = 2;
var c = 3;
console.log(a,b);
export var c = 3;
export default {a,b};

//main.js
import randomName,{c} from './const.js'
console.log(randomName.a,randomName.b,c)
//1,2,3
```

### 动态引入

希望模块全部加载完毕之后再使用模块，模块化的异步加载

```js
//const.js
var a = 1;
var b = 2;
var c = 3;
console.log(a,b);
export var c = 3;
export default {a,b};

//main.js
//会返回一个promise对象
import("./const.js").then((res)=>{
  console.log(res)
})
//1,2,3

//条件引入是一种异步引入
if(true){
  import("./const.js").then((res)=>{
  console.log(res)
}else{
console.log("没有文件")                   
}
```

模块化的规范

| 模块      | 规范         | 区别                                                         |
| --------- | ------------ | ------------------------------------------------------------ |
| requireJS | AMD规范      | 异步加载，允许回调函数，用于客户端。                         |
| seaJS     | CMD规范      | 不用了解                                                     |
| nodeJS    | CommonJS规范 | 同步加载，后台语言，相当于在本地调文件。可能会有很多人访问，会出现被重复调用，有缓存处理。只加载一次。减少请求的次数。 |
| Es6       | 自己的规范   | 可以异步加载，同时也可以按需求加载。也用与客户端。           |








































