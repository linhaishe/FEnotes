# ES6

## ECMAScript 6 教程

### 导言

### 环境搭建

- Node.js
- webpack

	- 含义

		- webpack 是一个现代 JavaScript 应用程序的静态模块打包器 (module bundler) 。当 webpack 处理应用程序时，它会递归地构建一个依赖关系图 (dependency graph) ，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle 。

	- 入口 (entry)

		- 入口会指示 webpack 应该使用哪个模块，来作为构建其内部依赖图的开始。进入入口起点后，webpack 会找出有哪些模块和库是入口起点（直接和间接）依赖的。在 webpack 中入口有多种方式来定义
		- 单个入口（简写）语法:

			- const config = {
  entry: "./src/main.js"
}

		- 对象语法:

			- const config = {
  app: "./src/main.js",
  vendors: "./src/vendors.js"
}

	- 输出 (output)

		- output 属性会告诉 webpack 在哪里输出它创建的 bundles ，以及如何命名这些文件，默认值为 ./dist:

	- loader

		- loader 让 webpack 可以去处理那些非 JavaScript 文件（ webpack 自身只理解 JavaScript ）。loader 可以将所有类型的文件转换为 webpack 能够有效处理的模块，

	- 插件 (plugins)

		- loader 被用于转换某些类型的模块，而插件则可以做更多的事情。包括打包优化、压缩、定义环境变量等等。插件的功能强大，是 webpack 扩展非常重要的利器，可以用来处理各种各样的任务。使用一个插件也非常容易，只需要 require() ，然后添加到 plugins 数组中。

	- https://www.runoob.com/w3cnote/webpack-tutorial.html

- gulp

	- gulp 是一个基于流的自动化构建工具，具有易于使用、构建快速、插件高质和易于学习的特点，常用于轻量级的工程中。

## 声明与表达式

### let & const

- let

	- 基本用法

		- {
  let a = 0;
  a   // 0
}
a   // 报错 ReferenceError: a is not defined

	- let 是在代码块内有效，var 是在全局范围内有效

		- {
  let a = 0;
  var b = 1;
}
a  // ReferenceError: a is not defined
b  // 1
		- {
  let a = 0;
  a   // 0
}
a   // 报错 ReferenceError: a is not defined

	- 不能重复声明

		- let 只能声明一次 var 可以声明多次:
		- let a = 1;
let a = 2;
var b = 3;
var b = 4;
a  // Identifier 'a' has already been declared
b  // 4

	- for 循环计数器很适合用 let

		- for (var i = 0; i < 10; i++) {
  setTimeout(function(){
    console.log(i);
  })
}
// 输出十个 10
for (let j = 0; j < 10; j++) {
  setTimeout(function(){
    console.log(j);
  })
}
// 输出 0123456789

- const

	- const 声明一个只读变量，声明之后不允许改变。意味着，一旦声明必须初始化，否则会报错。
	- const PI = "3.1415926";
PI  // 3.1415926

const MY_AGE;  // SyntaxError: Missing initializer in const declaration  
	- 暂时性死区

### 结构赋值

- 含义

	- 解构赋值是对赋值运算符的扩展。

他是一种针对数组或者对象进行模式匹配，然后对其中的变量进行赋值。

在代码书写上简洁且易读，语义更加清晰明了；也方便了复杂对象中数据字段获取。
	- 解构的源，解构赋值表达式的右边部分。
	- 解构的目标，解构赋值表达式的左边部分。

- 数组模型的解构（Array）

	- 基本

		- let [a, b, c] = [1, 2, 3];
// a = 1
// b = 2
// c = 3

	- 可嵌套

		- let [a, [[b], c]] = [1, [[2], 3]];
// a = 1
// b = 2
// c = 3

	- 可忽略

		- let [a, , b] = [1, 2, 3];
// a = 1
// b = 3

	- 不完全解构

		- let [a = 1, b] = []; // a = 1, b = undefined

	- 剩余运算符

		- let [a, ...b] = [1, 2, 3];
//a = 1
//b = [2, 3]

	- 字符串等

		- 在数组的解构中，解构的目标若为可遍历对象，皆可进行解构赋值。可遍历对象即实现 Iterator 接口的数据。
		- let [a, b, c, d, e] = 'hello';
// a = 'h'
// b = 'e'
// c = 'l'
// d = 'l'
// e = 'o'

	- 解构默认值

		- let [a = 2] = [undefined]; // a = 2
		- 当解构模式有匹配结果，且匹配结果是 undefined 时，会触发默认值作为返回结果。

			- let [a = 3, b = a] = [];     // a = 3, b = 3
let [a = 3, b = a] = [1];    // a = 1, b = 1
let [a = 3, b = a] = [1, 2]; // a = 1, b = 2
			- a 与 b 匹配结果为 undefined ，触发默认值：a = 3; b = a =3
a 正常解构赋值，匹配结果：a = 1，b 匹配结果 undefined ，触发默认值：b = a =1
a 与 b 正常解构赋值，匹配结果：a = 1，b = 2

- 对象模型的解构（Object）

	- 基本

		- let { foo, bar } = { foo: 'aaa', bar: 'bbb' };
// foo = 'aaa'
// bar = 'bbb'

let { baz : foo } = { baz : 'ddd' };
// foo = 'ddd'

	- 可嵌套可忽略
	
		- let obj = {p: ['hello', {y: 'world'}] };
let {p: [x, { y }] } = obj;
// x = 'hello'
// y = 'world'
let obj = {p: ['hello', {y: 'world'}] };
let {p: [x, {  }] } = obj;
// x = 'hello'

	- 不完全解构
	
		- let obj = {p: [{y: 'world'}] };
let {p: [{ y }, x ] } = obj;
// x = undefined
// y = 'world'

	- 剩余运算符
	
		- let {a, b, ...rest} = {a: 10, b: 20, c: 30, d: 40};
// a = 10
// b = 20
// rest = {c: 30, d: 40}

	- 解构默认值
	
		- let {a = 10, b = 5} = {a: 3};
// a = 3; b = 5;
let {a: aa = 10, b: bb = 5} = {a: 3};
// aa = 3; bb = 5;

### symbol

- ES6 引入了一种新的原始数据类型 Symbol ，表示独一无二的值，最大的用法是用来定义对象的唯一属性名。

ES6 数据类型除了 Number 、 String 、 Boolean 、 Object、 null 和 undefined ，还新增了 Symbol 。
- 基本用法

	- Symbol 函数栈不能用 new 命令，因为 Symbol 是原始数据类型，不是对象。可以接受一个字符串作为参数，为新创建的 Symbol 提供描述，用来显示在控制台或者作为字符串的时候使用，便于区分。
	- let sy = Symbol("KK");
console.log(sy);   // Symbol(KK)
typeof(sy);        // "symbol"

// 相同参数 Symbol() 返回的值不相等
let sy1 = Symbol("kk"); 
sy === sy1;       // false

- 使用场景

	- 作为属性名

		- 由于每一个 Symbol 的值都是不相等的，所以 Symbol 作为对象的属性名，可以保证属性不重名。

			- let sy = Symbol("key1");

// 写法1
let syObject = {};
syObject[sy] = "kk";
console.log(syObject);    // {Symbol(key1): "kk"}

// 写法2
let syObject = {
[sy]: "kk"
};
console.log(syObject);    // {Symbol(key1): "kk"}

// 写法3
let syObject = {};
Object.defineProperty(syObject, sy, {value: "kk"});
console.log(syObject);   // {Symbol(key1): "kk"}

		- Symbol 作为对象属性名时不能用.运算符，要用方括号。因为.运算符后面是字符串，所以取到的是字符串 sy 属性，而不是 Symbol 值 sy 属性。
	
			- let syObject = {};
syObject[sy] = "kk";

syObject[sy];  // "kk"
syObject.sy;   // undefined

	- 注意点
	
		- Symbol 值作为属性名时，该属性是公有属性不是私有属性，可以在类的外部访问。但是不会出现在 for...in 、 for...of 的循环中，也不会被 Object.keys() 、 Object.getOwnPropertyNames() 返回。如果要读取到一个对象的 Symbol 属性，可以通过 Object.getOwnPropertySymbols() 和 Reflect.ownKeys() 取到。
		- let syObject = {};
syObject[sy] = "kk";
console.log(syObject);

for (let i in syObject) {
  console.log(i);
}    // 无输出

Object.keys(syObject);                     // []
Object.getOwnPropertySymbols(syObject);    // [Symbol(key1)]
Reflect.ownKeys(syObject);                 // [Symbol(key1)]

	- 定义常量
	
		- 用字符串不能保证常量是独特的，这样会引起一些问题
	
			- const COLOR_RED = "red";
const COLOR_YELLOW = "yellow";
const COLOR_BLUE = "blue";
const MY_BLUE = "blue"；

function getConstantName(color) {
    switch (color) {
        case COLOR_RED :
            return "COLOR_RED";
        case COLOR_YELLOW :
            return "COLOR_YELLOW ";
        case COLOR_BLUE:
            return "COLOR_BLUE";
        case MY_BLUE:
            return "MY_BLUE";         
        default:
            throw new Exception('Can't find this color');
    }
}

		- 使用 Symbol 定义常量，这样就可以保证这一组常量的值都不相等。用 Symbol 来修改上面的例子，Symbol 的值是唯一的，所以不会出现相同值得常量，即可以保证 switch 按照代码预想的方式执行。
	
			- const COLOR_RED = Symbol("red");
const COLOR_YELLOW = Symbol("yellow");
const COLOR_BLUE = Symbol("blue");

function getConstantName(color) {
    switch (color) {
        case COLOR_RED :
            return "COLOR_RED";
        case COLOR_YELLOW :
            return "COLOR_YELLOW ";
        case COLOR_BLUE:
            return "COLOR_BLUE";
        default:
            throw new Exception('Can't find this color');
    }
}

- Symbol.for()
- Symbol.keyFor()

## 内置对象

### 新增

- map & set

	- Map 对象

		- Map 对象保存键值对。任何值(对象或者原始值) 都可以作为一个键或一个值。
		- Maps 和 Objects 的区别

			- 一个 Object 的键只能是字符串或者 Symbols，但一个 Map 的键可以是任意值。
			- Map 中的键值是有序的（FIFO 原则），而添加到对象中的键则不是。
			- Map 的键值对个数可以从 size 属性获取，而 Object 的键值对个数只能手动计算。
			- Object 都有自己的原型，原型链上的键名有可能和你自己在对象上的设置的键名产生冲突。

		- Map 中的 key

			- key 是字符串
			- key 是对象
			- key 是函数
			- key 是 NaN

		- Map 的迭代

			- for...of
			- forEach()

		- Map 对象的操作

			- Map 与 Array的转换
			- Map 的克隆
			- Map 的合并

	- Set 对象

		- 含义

			- Set 对象允许你存储任何类型的唯一值，无论是原始值或者是对象引用。

		- Set 中的特殊值
		- 类型转换
		- Set 对象作用

			- 数组去重
			- 并集
			- 交集
			- 差集

- reflect & proxy

	- Proxy
	- Reflect 

### 扩展

- 字符串

	- 子串的识别

		- indexOf 方法, lastIndexOf 
		- includes()

			- 返回布尔值，判断是否找到参数字符串。

		- startsWith()

			- 返回布尔值，判断参数字符串是否在原字符串的头部。

		- endsWith()

			- 返回布尔值，判断参数字符串是否在原字符串的尾部。

		- 接受两个参数，需要搜索的字符串，和可选的搜索起始位置索引
		- let string = "apple,banana,orange";
string.includes("banana");     // true
string.startsWith("apple");    // true
string.endsWith("apple");      // false
string.startsWith("banana",6)  // true

	- 字符串重复

		- repeat()

			- 返回新的字符串，表示将字符串重复指定次数返回

				- console.log("Hello,".repeat(2));  // "Hello,Hello,"

			- 如果参数是小数，向下取整

				- console.log("Hello,".repeat(3.2));  // "Hello,Hello,Hello,"

			- 如果参数是 0 至 -1 之间的小数，会进行取整运算，0 至 -1 之间的小数取整得到 -0 ，等同于 repeat 零次

				- console.log("Hello,".repeat(-0.5));  // "" 

			- 如果参数是 NaN，等同于 repeat 零次

				- console.log("Hello,".repeat(NaN));  // "" 

			- 如果参数是负数或者 Infinity ，会报错:

				- console.log("Hello,".repeat(-1));  
// RangeError: Invalid count value

console.log("Hello,".repeat(Infinity));  
// RangeError: Invalid count value

			- 如果传入的参数是字符串，则会先将字符串转化为数字
	
				- console.log("Hello,".repeat("hh")); // ""
console.log("Hello,".repeat("2"));  // "Hello,Hello,"

	- 字符串补全
	
		- padStart：返回新的字符串，表示用参数字符串从头部补全原字符串。
		- padEnd：返回新的字符串，表示用参数字符串从头部补全原字符串。
		- 两个参数
	
			- 第一个参数是指定生成的字符串的最小长度
			- 第二个参数是用来补全的字符串。如果没有指定第二个参数，默认用空格填充
	
		- console.log("h".padStart(5,"o"));  // "ooooh"
console.log("h".padEnd(5,"o"));    // "hoooo"
console.log("h".padStart(5));      // "    h"
		- 如果指定的长度大于或者等于原字符串的长度，则返回原字符串

			- console.log("hello".padStart(5,"A"));  // "hello"
	
		- 如果原字符串加上补全字符串长度大于指定长度，则截去超出位数的补全字符串
	
			- console.log("hello".padEnd(10,",world!"));  // "hello,worl"
	
		- 常用于补全位数
	
			- console.log("123".padStart(10,"0"));  // "0000000123"
	
	- 模板字符串
	
		- 含义
	
			- 模板字符串相当于加强版的字符串，用反引号 `,除了作为普通字符串，还可以用来定义多行字符串，还可以在字符串中加入变量和表达式。
	
		- 基本用法
	
			- 普通字符串
	
				- let string = `Hello'\n'world`;
console.log(string); 
// "Hello'
// 'world"

			- 多行字符串
	
				- let string1 =  `Hey,
can you stop angry now?`;
console.log(string1);
// Hey,
// can you stop angry now?

			- 字符串插入变量和表达式
	
				- 变量名写在 ${} 中，${} 中可以放入 JavaScript 表达式。
				- let name = "Mike";
let age = 27;
let info = `My Name is ${name},I am ${age+1} years old next year.`
console.log(info);
// My Name is Mike,I am 28 years old next year.

			- 字符串中调用函数
	
				- function f(){
  return "have fun!";
}
let string2= `Game start,${f()}`;
console.log(string2);  // Game start,have fun!

			- 注意要点
	
				- 模板字符串中的换行和空格都是会被保留的
				- innerHtml = `<ul>
  <li>menu</li>
  <li>mine</li>
</ul>
`;
console.log(innerHtml);
// 输出
<ul>
 <li>menu</li>
 <li>mine</li>
</ul>


		- 标签模板
	
			- 标签模板，是一个函数的调用，其中调用的参数是模板字符串。
			- alert`Hello world!`;
// 等价于
alert('Hello world!');
			- 当模板字符串中带有变量，会将模板字符串参数处理成多个参数。

				- function f(stringArr,...values){
 let result = "";
 for(let i=0;i<stringArr.length;i++){
  result += stringArr[i];
  if(values[i]){
   result += values[i];
        }
    }
 return result;
}
let name = 'Mike';
let age = 27;
f`My Name is ${name},I am ${age+1} years old next year.`;
// "My Name is Mike,I am 28 years old next year."

f`My Name is ${name},I am ${age+1} years old next year.`;
// 等价于
f(['My Name is',',I am ',' years old next year.'],'Mike',28);

			- 应用
	
				- 过滤 HTML 字符串，防止用户输入恶意内容。
				- function f(stringArr,...values){
 let result = "";
 for(let i=0;i<stringArr.length;i++){
  result += stringArr[i];
   if(values[i]){
     result += String(values[i]).replace(/&/g, "&amp;")
               .replace(/</g, "&lt;")
               .replace(/>/g, "&gt;");
    }
 }
 return result;
}
name = '<Amy&MIke>';
f`<p>Hi, ${name}.I would like send you some message.</p>`;
// <p>Hi, &lt;Amy&amp;MIke&gt;.I would like send you some message.</p>

			- 国际化处理（转化多国语言）
	
				- i18n`Hello ${name}, you are visitor number ${visitorNumber}.`;  
// 你好**，你是第**位访问者

- 数值

	- 数值的表示

		- 进制表示法

			- 二进制表示法新写法: 前缀 0b 或 0B 。
			- 八进制表示法新写法: 前缀 0o 或 0O 。

		- 常量

			- Number.EPSILON
			- Number.EPSILON 属性表示 1 与大于 1 的最小浮点数之间的差。
			- 它的值接近于 2.2204460492503130808472633361816E-16，或者 2-52。

		- 最大/最小安全整数

			- 安全整数

				- 安全整数表示在 JavaScript 中能够精确表示的整数，安全整数的范围在 2 的 -53 次方到 2 的 53 次方之间（不包括两个端点），超过这个范围的整数无法精确表示。

			- 最大安全整数

				- 安全整数范围的上限，即 2 的 53 次方减 1 。

			- 最小安全整数

				- 安全整数范围的下限，即 2 的 53 次方减 1 的负数。

		- 方法

			- Number 对象新方法

				- 用于检查一个数值是否为有限的（ finite ），即不是 Infinity
				- Number.isFinite()

			- 从全局移植到 Number 对象的方法

				- 逐步减少全局方法，用于全局变量的模块化。
方法的行为没有发生改变。
				- 用于将给定字符串转化为指定进制的整数。
				- Number.parseInt()
				- https://www.runoob.com/w3cnote/es6-number.html

	- Math 对象的扩展

		- ES6 在 Math 对象上新增了 17 个数学相关的静态方法，这些方法只能在 Math 中调用。
		- 普通计算

			- Math.cbrt

				- 用于计算一个数的立方根。

			- Math.imul

				- 两个数以 32 位带符号整数形式相乘的结果，返回的也是一个 32 位的带符号整数。

			- Math.hypot

				- 用于计算所有参数的平方和的平方根。

			- Math.clz32

				- 用于返回数字的32 位无符号整数形式的前导0的个数。

		- 数字处理

			- Math.trunc

				- 用于返回数字的整数部分。

			- Math.fround

				- 用于获取数字的32位单精度浮点数形式。

		- 判断

			- Math.sign

				- 判断数字的符号（正、负、0）。

		- 对数方法

			- Math.expm1()

				- 用于计算 e 的 x 次方减 1 的结果，即 Math.exp(x) - 1 。

			- Math.log1p(x)

				- 用于计算1 + x 的自然对数，即 Math.log(1 + x) 。

			- Math.log10(x)

				- 用于计算以 10 为底的 x 的对数。

			- Math.log2()

				- 用于计算 2 为底的 x 的对数。

		- 双曲函数方法

			- Math.sinh(x): 用于计算双曲正弦。
			- Math.cosh(x): 用于计算双曲余弦。
			- Math.tanh(x): 用于计算双曲正切。
			- Math.asinh(x): 用于计算反双曲正弦。
			- Math.acosh(x): 用于计算反双曲余弦。
			- Math.atanh(x): 用于计算反双曲正切。

		- 指数运算符

			- 1 ** 2; // 1
// 右结合，从右至左计算
2 ** 2 ** 3; // 256
// **=
let exam = 2;
exam ** = 2; // 4

- 对象

	- 对象字面量

		- 属性的简洁表示法

			- const age = 12;
const name = "Amy";
const person = {age, name};
person   //{age: 12, name: "Amy"}
//等同于
const person = {age: age, name: name}

				- const person = {
  sayHi(){
    console.log("Hi");
  }
}
person.sayHi();  //"Hi"
//等同于
const person = {
  sayHi:function(){
    console.log("Hi");
  }
}
person.sayHi();//"Hi"

			- Generator 函数，则要在前面加一个星号

				- const obj = {
  * myGenerator() {
    yield 'hello world';
  }
};
//等同于
const obj = {
  myGenerator: function* () {
    yield 'hello world';
  }
};

		- 属性名表达式

			- ES6允许用表达式作为属性名，但是一定要将表达式放在方括号内。

				- const obj = {
 ["he"+"llo"](){
   return "Hi";
  }
}
obj.hello();  //"Hi"

			- 注意点：属性的简洁表示法和属性名表达式不能同时使用，否则会报错。

				- const hello = "Hello";
const obj = {
 [hello]
};
obj  //SyntaxError: Unexpected token }

const hello = "Hello";
const obj = {
[hello+"2"]:"world"
};
obj  //{Hello2: "world"}

	- 对象的拓展运算符
	
		- 基本用法
	
			- 拓展运算符（...）用于取出参数对象所有可遍历属性然后拷贝到当前对象。
			- let person = {name: "Amy", age: 15};
let someone = { ...person };
someone;  //{name: "Amy", age: 15}

		- 可用于合并两个对象
	
			- let age = {age: 15};
let name = {name: "Amy"};
let person = {...age, ...name};
person;  //{age: 15, name: "Amy"}

		- 注意点
	
			- 自定义的属性和拓展运算符对象里面属性的相同的时候：自定义的属性在拓展运算符后面，则拓展运算符对象内部同名的属性将被覆盖掉。
	
				- let person = {name: "Amy", age: 15};
let someone = { ...person, name: "Mike", age: 17};
someone;  //{name: "Mike", age: 17}

			- 自定义的属性在拓展运算度前面，则变成设置新对象默认属性值。
	
				- let person = {name: "Amy", age: 15};
let someone = {name: "Mike", age: 17, ...person};
someone;  //{name: "Amy", age: 15}

			- 拓展运算符后面是空对象，没有任何效果也不会报错。
	
				- let a = {...{}, a: 1, b: 2};
a;  //{a: 1, b: 2}

			- 拓展运算符后面是null或者undefined，没有效果也不会报错。
	
				- let b = {...null, ...undefined, a: 1, b: 2};
b;  //{a: 1, b: 2}

	- 对象的新方法
	
		- Object.assign(target, source_1, ···)
	
			- 用于将源对象的所有可枚举属性复制到目标对象中。
			- let target = {a: 1};
let object2 = {b: 2};
let object3 = {c: 3};
Object.assign(target,object2,object3);  
// 第一个参数是目标对象，后面的参数是源对象
target;  // {a: 1, b: 2, c: 3}
			- 如果目标对象和源对象有同名属性，或者多个源对象有同名属性，则后面的属性会覆盖前面的属性。
			- 如果该函数只有一个参数，当参数为对象时，直接返回该对象；当参数不是对象时，会先将参数转为对象然后返回。
			- 因为 null 和 undefined 不能转化为对象，所以会报错

				- Object.assign(null);       // TypeError: Cannot convert undefined or null to object
Object.assign(undefined);  // TypeError: Cannot convert undefined or null to object
当参数不止一个时，null 和 undefined 不放第一个，即不为目标对象时，会跳过 null 和 undefined ，不报错
Object.assign(1,undefined);  // Number {1}
Object.assign({a: 1},null);  // {a: 1}

Object.assign(undefined,{a: 1});  // TypeError: Cannot convert undefined or null to object

			- 注意点
	
				- assign 的属性拷贝是浅拷贝
	
					- let sourceObj = { a: { b: 1}};
let targetObj = {c: 3};
Object.assign(targetObj, sourceObj);
targetObj.a.b = 2;
sourceObj.a.b;  // 2

				- 同名属性替换
	
					- targetObj = { a: { b: 1, c:2}};
sourceObj = { a: { b: "hh"}};
Object.assign(targetObj, sourceObj);
targetObj;  // {a: {b: "hh"}}

				- 数组的处理
	
					- Object.assign([2,3], [5]);  // [5,3]
					- 会将数组处理成对象，所以先将 [2,3] 转为 {0:2,1:3} ，然后再进行属性复制，所以源对象的 0 号属性覆盖了目标对象的 0。
	
		- Object.is(value1, value2)
	
			- 用来比较两个值是否严格相等，与（===）基本类似。
	
				- Object.is("q","q");      // true
Object.is(1,1);          // true
Object.is([1],[1]);      // false
Object.is({q:1},{q:1});  // false

			- 与（===）的区别
	
				- //一是+0不等于-0
Object.is(+0,-0);  //false
+0 === -0  //true
//二是NaN等于本身
Object.is(NaN,NaN); //true
NaN === NaN  //false

- 数组

	- 数组创建

		- Array.of()

			- 将参数中所有值作为元素形成数组。
			- console.log(Array.of(1, 2, 3, 4)); // [1, 2, 3, 4]

// 参数值可为不同类型
console.log(Array.of(1, '2', true)); // [1, '2', true]

// 参数为空时返回空数组
console.log(Array.of()); // []

		- Array.from()
	
			- Array.from(arrayLike[, mapFn[, thisArg]])
			- 将类数组对象或可迭代对象转化为数组。
			- 参数
	
				- arrayLike
	
					- 想要转换的类数组对象或可迭代对象。
					- console.log(Array.from([1, 2, 3])); // [1, 2, 3]
	
				- mapFn
	
					- 可选，map 函数，用于对每个元素进行处理，放入数组的是处理后的元素。
					- console.log(Array.from([1, 2, 3], (n) => n * 2)); // [2, 4, 6]
	
				- thisArg
	
					- 可选，用于指定 map 函数执行时的 this 对象。
					- let map = {
	do: function(n) {
	    return n * 2;
	}
}
let arrayLike = [1, 2, 3];
console.log(Array.from(arrayLike, function (n){
    return this.do(n);
}, map)); // [2, 4, 6]

		- 类数组对象
	
			- 一个类数组对象必须含有 length 属性，且元素属性名必须是数值或者可转换为数值的字符。
			- let arr = Array.from({
  0: '1',
  1: '2',
  2: 3,
  length: 3
});
console.log(); // ['1', '2', 3]

// 没有 length 属性,则返回空数组
let array = Array.from({
  0: '1',
  1: '2',
  2: 3,
});
console.log(array); // []

// 元素属性名不为数值且无法转换为数值，返回长度为 length 元素值为 undefined 的数组  
let array1 = Array.from({
  a: 1,
  b: 2,
  length: 2
});
console.log(array1); // [undefined, undefined]

		- 转换可迭代对象
	
			- 转换 map
	
				- let map = new Map();
map.set('key0', 'value0');
map.set('key1', 'value1');
console.log(Array.from(map)); // [['key0', 'value0'],['key1',
// 'value1']]

			- 转换 set
	
				- let arr = [1, 2, 3];
let set = new Set(arr);
console.log(Array.from(set)); // [1, 2, 3]

			- 转换字符串
	
				- let str = 'abc';
console.log(Array.from(str)); // ["a", "b", "c"]

	- 扩展的方法
	
		- 查找
	
			- find()
	
				- 查找数组中符合条件的元素,若有多个符合条件的元素，则返回第一个元素。
	
			- findIndex()
	
				- 查找数组中符合条件的元素索引，若有多个符合条件的元素，则返回第一个元素索引。
	
		- 填充
	
			- fill()
	
				- 将一定范围索引的数组元素内容填充为单个指定的值。
	
			- copyWithin()
	
				- 将一定范围索引的数组元素修改为此数组另一指定范围索引的元素。
	
		- 遍历
	
			- entries()
	
				- 遍历键值对。
	
			- keys()
	
				- 遍历键名。
	
			- values()
	
				- 遍历键值。
	
		- 包含
	
			- includes()
	
				- 数组是否包含指定值。
	
			- 注意：与 Set 和 Map 的 has 方法区分；Set 的 has 方法用于查找值；Map 的 has 方法用于查找键名。
	
		- 嵌套数组转一维数组
	
			- flat()
			- flatMap()
	
				- 先对数组中每个元素进行了的处理，再对数组执行 flat() 方法。
	
	- 数组缓冲区
	
		- 创建数组缓冲区
	
			- 数组缓冲区是内存中的一段地址。
			- 定型数组的基础。
			- 实际字节数在创建时确定，之后只可修改其中的数据，不可修改大小。
	
		- 视图
	
			- 视图是用来操作内存的接口。
			- 视图可以操作数组缓冲区或缓冲区字节的子集,并按照其中一种数值数据类型来读取和写入数据。
			- DataView 类型是一种通用的数组缓冲区视图,其支持所有8种数值型数据类型。
	
	- 定型数组
	
		- 含义
	
			- 数组缓冲区的特定类型的视图。
			- 可以强制使用特定的数据类型，而不是使用通用的 DataView 对象来操作数组缓冲区。
	
	- 扩展运算符
	
		- 复制数组
	
			- let arr = [1, 2],
	arr1 = [...arr];
console.log(arr1); // [1, 2]

// 数组含空位
let arr2 = [1, , 3],
    arr3 = [...arr2];
console.log(arr3); [1, undefined, 3]

		- 合并数组
	
			- console.log([...[1, 2],...[3, 4]]); // [1, 2, 3, 4]

## 运算符与语句

### 函数

- 函数参数的扩展

	- 默认参数

		- 基本用法

			- function fn(name,age=17){
 console.log(name+","+age);
}
fn("Amy",18);  // Amy,18
fn("Amy","");  // Amy,
fn("Amy");     // Amy,17

		- 注意点：使用函数默认参数时，不允许有同名参数。

			- // 不报错
function fn(name,name){
 console.log(name);
}

// 报错
//SyntaxError: Duplicate parameter name not allowed in this context
function fn(name,name,age=17){
 console.log(name+","+age);
}

		- 只有在未传递参数，或者参数为 undefined 时，才会使用默认参数，null 值被认为是有效的值传递。
	
			- function fn(name,age=17){
	console.log(name+","+age);
}
fn("Amy",null); // Amy,null

		- 函数参数默认值存在暂时性死区，在函数参数默认值表达式中，还未初始化赋值的参数值无法作为其他参数的默认值。
	
			- function f(x,y=x){
	console.log(x,y);
}
f(1);  // 1 1

function f(x=y){
    console.log(x);
}
f();  // ReferenceError: y is not defined

	- 不定参数
	
		- 不定参数用来表示不确定参数个数，形如，...变量名，由...加上一个具名参数标识符组成。具名参数只能放在参数组的最后，并且有且只有一个不定参数。
		- function f(...values){
	console.log(values.length);
}
f(1,2);      //2
f(1,2,3,4);  //4

- 箭头函数

	- 基本语法

		- 箭头函数提供了一种更加简洁的函数书写方式
		- 参数 => 函数体

	- 基本用法

		- var f = v => v;
//等价于
var f = function(a){
 return a;
}
f(1);  //1

	- 当箭头函数没有参数或者有多个参数，要用 () 括起来

		- var f = (a,b) => a+b;
f(6,2);  //8

	- 当箭头函数函数体有多行语句，用 {} 包裹起来，表示代码块，当只有一行语句，并且需要返回结果时，可以省略 {} , 结果会自动返回。

		- var f = (a,b) => {
 let result = a+b;
 return result;
}
f(6,2);  // 8

	- 当箭头函数要返回对象的时候，为了区分于代码块，要用 () 将对象包裹起来

		- // 报错
var f = (id,name) => {id: id, name: name};
f(6,2);  // SyntaxError: Unexpected token :

// 不报错
var f = (id,name) => ({id: id, name: name});
f(6,2);  // {id: 6, name: 2}

	- 注意点：没有 this、super、arguments 和 new.target 绑定。
	
		- var func = () => {
  // 箭头函数里面没有 this 对象，
  // 此时的 this 是外层的 this 对象，即 Window 
  console.log(this)
}
func(55)  // Window 

var func = () => {    
  console.log(arguments)
}
func(55);  // ReferenceError: arguments is not defined

	- 箭头函数体中的 this 对象，是定义函数时的对象，而不是使用函数时的对象。不可以作为构造函数，也就是不能使用 new 命令，否则会报错
	
		- function fn(){
  setTimeout(()=>{
    // 定义时，this 绑定的是 fn 中的 this 对象
    console.log(this.a);
  },0)
}
var a = 20;
// fn 的 this 对象为 {a: 19}
fn.call({a: 18});  // 18

- 适合使用的场景

	- // 回调函数
var Person = {
    'age': 18,
    'sayHello': function () {
      setTimeout(function () {
        console.log(this.age);
      });
    }
};
var age = 20;
Person.sayHello();  // 20

var Person1 = {
    'age': 18,
    'sayHello': function () {
      setTimeout(()=>{
        console.log(this.age);
      });
    }
};
var age = 20;
Person1.sayHello();  // 18
//需要维护一个 this 上下文的时候，就可以使用箭头函数。

- 不适合使用的场景

	- var Person = {
    'age': 18,
    'sayHello': ()=>{
        console.log(this.age);
      }
};
var age = 20;
Person.sayHello();  // 20
// 此时 this 指向的是全局对象

var Person1 = {
    'age': 18,
    'sayHello': function () {
        console.log(this.age);
    }
};
var age = 20;
Person1.sayHello();   // 18
// 此时的 this 指向 Person1 对象
	- 需要动态 this 的时候

		- var button = document.getElementById('userClick');
button.addEventListener('click', () => {
     this.classList.toggle('on');
});

	- button 的监听函数是箭头函数，所以监听函数里面的 this 指向的是定义的时候外层的 this 对象，即 Window，导致无法操作到被点击的按钮对象。

### 迭代器

- 两个核心概念

	- Iterator 是 ES6 引入的一种新的遍历机制
	- 迭代器是一个统一的接口，它的作用是使各种数据结构可被便捷的访问，它是通过一个键为Symbol.iterator 的方法来实现。
	- 迭代器是用于遍历数据结构元素的指针（如数据库中的游标）。

- 迭代过程

	- 通过 Symbol.iterator 创建一个迭代器，指向当前数据结构的起始位置
	- 随后通过 next 方法进行向下迭代指向下一个位置， next 方法会返回当前位置的对象，对象包含了 value 和 done 两个属性， value 是当前属性的值， done 用于判断是否遍历结束
	- 当 done 为 true 时则遍历结束
	- const items = ["zero", "one", "two"];
const it = items[Symbol.iterator]();

it.next();
>{value: "zero", done: false}
it.next();
>{value: "one", done: false}
it.next();
>{value: "two", done: false}
it.next();
>{value: undefined, done: true}

- 可迭代的数据结构

	- Array
String
Map
Set
Dom元素（正在进行中）

- for...of 循环对数据结构进行迭代

	- Array

		- 数组 ( Array ) 和类型数组 ( TypedArray ) 他们是可迭代的。
		- for (let item of ["zero", "one", "two"]) {
  console.log(item);
}
// output:
// zero
// one
// two

	- String

		- 字符串是可迭代的，单他们遍历的是 Unicode 码，每个码可能包含一个到两个的 Javascript 字符。
		- for (const c of 'z\uD83D\uDC0A') {
    console.log(c);
}
// output:
// z
// \uD83D\uDC0A

	- Map

		- Map 主要是迭代它们的 entries ，每个 entry 都会被编码为 [key, value] 的项， entries 是以确定的形势进行迭代，其顺序是与添加的顺序相同。
		- const map = new Map();
map.set(0, "zero");
map.set(1, "one");

for (let item of map) {
  console.log(item);
}
// output:
// [0, "zero"]
// [1, "one"]

	- Set
	
		- Set 是对其元素进行迭代，迭代的顺序与其添加的顺序相同
		- 注意： WeakSets 不可迭代
		- const set = new Set();
set.add("zero");
set.add("one");

for (let item of set) {
  console.log(item);
}
// output:
// zero
// one

	- arguments
	
		- arguments 目前在 ES6 中使用越来越少，但也是可遍历的
		- function args() {
  for (let item of arguments) {
    console.log(item);
  }
}
args("zero", "one");
// output:
// zero
// one

	- 普通对象不可迭代
	
		- 普通对象是由 object 创建的，不可迭代
		- // TypeError
for (let item of {}) { 
  console.log(item);
}

- for...of循环

	- 作用

		- for...of 是 ES6 新引入的循环，用于替代 for..in 和 forEach() ，并且支持新的迭代协议。它可用于迭代常规的数据类型，如 Array 、 String 、 Map 和 Set 等等。

	- 迭代常规数据类型

		- Array

			- const nums = ["zero", "one", "two"];

for (let num of nums) {
  console.log(num);
}
TypedArray
const typedArray1 = new Int8Array(6);
typedArray1[0] = 10;
typedArray1[1] = 11;

for (let item of typedArray1) {
  console.log(item);
}

		- String
	
			- const str = "zero";

for (let item of str) {
  console.log(item);
}

		- Map
	
			- let myMap = new Map();
myMap.set(0, "zero");
myMap.set(1, "one");
myMap.set(2, "two");

// 遍历 key 和 value
for (let [key, value] of myMap) {
  console.log(key + " = " + value);
}
for (let [key, value] of myMap.entries()) {
  console.log(key + " = " + value);
}

// 只遍历 key
for (let key of myMap.keys()) {
  console.log(key);
}

// 只遍历 value
for (let value of myMap.values()) {
  console.log(value);
}

		- Set
	
			- let mySet = new Set();
mySet.add("zero");
mySet.add("one");
mySet.add("two");

// 遍历整个 set
for (let item of mySet) {
  console.log(item);
}

// 只遍历 key 值
for (let key of mySet.keys()) {
  console.log(key);
}

// 只遍历 value
for (let value of mySet.values()) {
  console.log(value);
}

// 遍历 key 和 value ，两者会相等
for (let [key, value] of mySet.entries()) {
  console.log(key + " = " + value);
}

	- 可迭代的数据结构
	
		- of 操作数必须是可迭代，这意味着如果是普通对象则无法进行迭代。如果数据结构类似于数组的形式，则可以借助 Array.from() 方法进行转换迭代。
		- const arrayLink = {length: 2, 0: "zero", 1: "one"}
		- // 报 TypeError 异常
for (let item of arrayLink) {
  console.log(item);
}

// 正常运行
// output:
// zero
// one
for (let item of Array.from(arrayLink)) {
  console.log(item);
}
		- let 、const 和 var 用于 for..of

			- const nums = ["zero", "one", "two"];

for (const num of nums) {
  console.log(num);
}
// 报 ReferenceError
console.log(num);
			- 最后一句会报异常，原因 num 的作用域只在循环体内部，外部无效，具体可查阅 let 与 const 章节。使用 var 则不会出现上述情况，因为 var 会作用于全局，迭代将不会每次都创建一个新的存储空间。
			- const nums = ["zero", "one", "two"];

forv (var num of nums) {
  console.log(num);
}
// output: two
console.log(num);

### class类

- 含义

	- class (类)作为对象的模板被引入，可以通过 class 关键字定义类。class 的本质是 function，它可以看作一个语法糖，让对象原型的写法更加清晰、更像面向对象编程的语法。

- 基础用法

	- 类定义

		- 类表达式可以为匿名或命名。
		- // 匿名类
let Example = class {
    constructor(a) {
        this.a = a;
    }
}
// 命名类
let Example = class Example {
    constructor(a) {
        this.a = a;
    }
}

	- 类声明

		- class Example {
    constructor(a) {
        this.a = a;
    }
}

	- 注意要点：

		- 不可重复声明。

			- class Example{}
class Example{}
// Uncaught SyntaxError: Identifier 'Example' has already been 
// declared

let Example1 = class{}
class Example{}
// Uncaught SyntaxError: Identifier 'Example' has already been 
// declared

		- 1.类定义不会被提升，这意味着，必须在访问前对类进行定义，否则就会报错。
2.类中方法不需要 function 关键字。
3.方法间不能加分号。
		- new Example(); 
class Example {}

	- 类的主体
	
		- 属性
	
			- prototype，虽然可以直接自类中定义方法，但是其实方法还是定义在 prototype 上的。 覆盖方法 / 初始化时添加方法
			- Example.prototype={
	//methods
}
//覆盖方法 / 初始化时添加方法

				- Object.assign(Example.prototype,{
	//methods
})
//添加方法

			- 静态属性
	
				- class 本身的属性，即直接定义在类内部的属性（ Class.propname ），不需要实例化。 ES6 中规定，Class 内部只有静态方法，没有静态属性。
				- class Example {
// 新提案
    static a = 2;
}
// 目前可行写法
Example.b = 2;

			- 公共属性
	
				- class Example{}
Example.prototype.a = 2;

			- 实例属性
	
				- 实例属性：定义在实例对象（ this ）上的属性。
				- class Example {
	a = 2;
	constructor () {
	    console.log(this.a);
	}
}

			- name 属性
	
				- 返回跟在 class 后的类名(存在时)。
				- let Example=class Exam {
	constructor(a) {
	    this.a = a;
	}
}
console.log(Example.name); // Exam

let Example=class {
    constructor(a) {
        this.a = a;
    }
}
console.log(Example.name); // Example

		- 方法
	
			- constructor 方法
	
				- constructor 方法是类的默认方法，创建类的实例化对象时被调用。
				- class Example{
	constructor(){
	  console.log('我是constructor');
	}
}
new Example(); // 我是constructor
				- 返回对象

					- class Test {
	constructor(){
	    // 默认返回实例对象 this
	}
}
console.log(new Test() instanceof Test); // true

class Example {
    constructor(){
        // 指定返回对象
        return new Test();
    }
}
console.log(new Example() instanceof Example); // false

			- 静态方法
	
				- class Example{
	static sum(a, b) {
	    console.log(a+b);
	}
}
Example.sum(1, 2); // 3

			- 原型方法
	
				- class Example {
	sum(a, b) {
	    console.log(a + b);
	}
}
let exam = new Example();
exam.sum(1, 2); // 3

			- 实例方法
	
				- class Example {
	constructor() {
	    this.sum = (a, b) => {
	        console.log(a + b);
	    }
	}
}

	- 类的实例化
	
		- new
	
			- class 的实例化必须通过 new 关键字。
			- class Example {}

let exam1 = Example(); 
// Class constructor Example cannot be invoked without 'new'

		- 实例化对象
	
			- 共享原型对象
			- class Example {
	constructor(a, b) {
	    this.a = a;
	    this.b = b;
	    console.log('Example');
	}
	sum() {
	    return this.a + this.b;
	}
}
let exam1 = new Example(2, 1);
let exam2 = new Example(3, 1);
console.log(exam1._proto_ == exam2._proto_); // true

exam1._proto_.sub = function() {
    return this.a - this.b;
}
console.log(exam1.sub()); // 1
console.log(exam2.sub()); // 2

- decorator

	- decorator 是一个函数，用来修改类的行为，在代码编译时产生作用。
	- 类修饰

		- 一个参数

			- function testable(target) {
    target.isTestable = true;
}
@testable
class Example {}
Example.isTestable; // true

		- 多个参数——嵌套实现

			- function testable(isTestable) {
    return function(target) {
        target.isTestable=isTestable;
    }
}
@testable(true)
class Example {}
Example.isTestable; // true

		- 实例属性

			- 上面两个例子添加的是静态属性，若要添加实例属性，在类的 prototype 上操作即可。

	- 方法修饰

		- 3个参数：target（类的原型对象）、name（修饰的属性名）、descriptor（该属性的描述对象）。
		- class Example {
    @writable
    sum(a, b) {
        return a + b;
    }
}
function writable(target, name, descriptor) {
    descriptor.writable = false;
    return descriptor; // 必须返回
}
		- 修饰器执行顺序，由外向内进入，由内向外执行。
		- class Example {
    @logMethod(1)
    @logMthod(2)
    sum(a, b){
        return a + b;
    }
}
function logMethod(id) {
    console.log('evaluated logMethod'+id);
    return (target, name, desctiptor) => console.log('excuted         logMethod '+id);
}
// evaluated logMethod 1
// evaluated logMethod 2
// excuted logMethod 2
// excuted logMethod 1

- 封装与继承

	- getter / setter

		- getter 不可单独出现
		- getter 与 setter 必须同级出现

	- extends
	- super

- 注意要点

	- 不可继承常规对象。
	- var Father = {
    // ...
}
class Child extends Father {
     // ...
}
// Uncaught TypeError: Class extends value #<Object> is not a constructor or null

// 解决方案
Object.setPrototypeOf(Child.prototype, Father);

### 模块

- 概述

	- 在 ES6 前， 实现模块化使用的是 RequireJS 或者 seaJS（分别是基于 AMD 规范的模块化库，  和基于 CMD 规范的模块化库）。
	- ES6 引入了模块化，其设计思想是在编译时就能确定模块的依赖关系，以及输入和输出的变量。
	- ES6 的模块化分为导出（export） @与导入（import）两个模块。

- 特点

	- ES6 的模块自动开启严格模式，不管你有没有在模块头部加上 use strict;。
	- 模块中可以导入和导出各种类型的变量，如函数，对象，字符串，数字，布尔值，类等。
	- 每个模块都有自己的上下文，每一个模块内声明的变量都是局部变量，不会污染全局作用域。
	- 每一个模块只加载一次（是单例的）， 若再去加载同目录下同文件，直接从内存中读取。

- export 与 import

	- 基本用法

		- 模块导入导出各种类型的变量，如字符串，数值，函数，类。
		- 导出的函数声明与类声明必须要有名称（export default 命令另外考虑）。 
		- 不仅能导出声明还能导出引用（例如函数）。
		- export 命令可以出现在模块的任何位置，但必需处于模块顶层。
		- import 命令会提升到整个模块的头部，首先执行。
		- 建议使用大括号指定所要输出的一组变量写在文档尾部，明确导出的接口。
		- 函数与类都需要有对应的名称，导出文档尾部也避免了无对应名称。

	- /*-----export [test.js]-----*/
let myName = "Tom";
let myAge = 20;
let myfn = function(){
    return "My name is" + myName + "! I'm '" + myAge + "years old."
}
let myClass =  class myClass {
    static a = "yeah!";
}
export { myName, myAge, myfn, myClass }

/*-----import [xxx.js]-----*/
import { myName, myAge, myfn, myClass } from "./test.js";
console.log(myfn());// My name is Tom! I'm 20 years old.
console.log(myAge);// 20
console.log(myName);// Tom
console.log(myClass.a );// yeah!

- as 的用法

	- export 命令导出的接口名称，须和模块内部的变量有一一对应关系。
	- 导入的变量名，须和导出的接口名称相同，即顺序可以不一致。
	- 不同模块导出接口名称命名重复， 使用 as 重新定义变量名。
	- /*-----export [test.js]-----*/
let myName = "Tom";
export { myName as exportName }

/*-----import [xxx.js]-----*/
import { exportName } from "./test.js";
console.log(exportName);// Tom
使用 as 重新定义导出的接口名称，隐藏模块内部的变量
/*-----export [test1.js]-----*/
let myName = "Tom";
export { myName }
/*-----export [test2.js]-----*/
let myName = "Jerry";
export { myName }
/*-----import [xxx.js]-----*/
import { myName as name1 } from "./test1.js";
import { myName as name2 } from "./test2.js";
console.log(name1);// Tom
console.log(name2);// Jerry

- import 命令的特点

	- 只读属性：不允许在加载模块的脚本里面，改写接口的引用指向，即可以改写 import 变量类型为对象的属性值，不能改写 import 变量类型为基本类型的值。
	- import {a} from "./xxx.js"
a = {}; // error

import {a} from "./xxx.js"
a.foo = "hello"; // a = { foo : 'hello' }
	- 单例模式：多次重复执行同一句 import 语句，那么只会执行一次，而不会执行多次。import 同一模块，声明不同接口引用，会声明对应变量，但只执行一次 import 。
	- import { a } "./xxx.js";
import { a } "./xxx.js";
// 相当于 import { a } "./xxx.js";

import { a } from "./xxx.js";
import { b } from "./xxx.js";
// 相当于 import { a, b } from "./xxx.js";
	- 静态执行特性：import 是静态执行，所以不能使用表达式和变量。
	- import { "f" + "oo" } from "methods";
// error
let module = "methods";
import { foo } from module;
// error
if (true) {
  import { foo } from "method1";
} else {
  import { foo } from "method2";
}
// error

- export default 命令

	- 在一个文件或模块中，export、import 可以有多个，export default 仅有一个。
	- export default 中的 default 是对应的导出接口变量。
	- 通过 export 方式导出，在导入时要加{ }，export default 则不需要。
	- export default 向外暴露的成员，可以使用任意变量来接收。
	- var a = "My name is Tom!";
export default a; // 仅有一个
export default var c = "error"; 
// error，default 已经是对应的导出变量，不能跟着变量声明语句

import b from "./xxx.js"; // 不需要加{}， 使用任意变量接收

- 复合使用

	- export 与 import 可以在同一模块使用，使用特点

		- 以将导出接口改名，包括 default。
		- 复合使用 export 与 import ，也可以导出全部，当前模块导出的接口会覆盖继承导出的。

	- export { foo, bar } from "methods";

// 约等于下面两段语句，不过上面导入导出方式该模块没有导入 foo 与 bar
import { foo, bar } from "methods";
export { foo, bar };

/* ------- 特点 1 --------*/
// 普通改名
export { foo as bar } from "methods";
// 将 foo 转导成 default
export { foo as default } from "methods";
// 将 default 转导成 foo
export { default as foo } from "methods";

/* ------- 特点 2 --------*/
export * from "methods";

## 异步编程

### promise 对象

- Promise 状态

	- 是异步编程的一种解决方案。从语法上说，Promise 是一个对象，从它可以获取异步操作的消息。
	- Promise 异步操作有三种状态：pending（进行中）、fulfilled（已成功）和 rejected（已失败）。除了异步操作的结果，任何其他操作都无法改变这个状态。
	- Promise 对象只有：从 pending 变为 fulfilled 和从 pending 变为 rejected 的状态改变。只要处于 fulfilled 和 rejected ，状态就不会再变了即 resolved（已定型）。
	- const p1 = new Promise(function(resolve,reject){
  resolve('success1');
  resolve('success2');
});

const p2 = new Promise(function(){
  resolve('success3');
  reject('reject');
});

p1.then(function(value){
  console.log(value); // success1
});
p2.then(function(value){
  console.log(value); // success3
});
	- 状态的缺点

		- 无法取消 Promise ，一旦新建它就会立即执行，无法中途取消。
		- 如果不设置回调函数，Promise 内部抛出的错误，不会反应到外部。
		- 当处于 pending 状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）。

- then 方法

	- then 方法接收两个函数作为参数，第一个参数是 Promise 执行成功时的回调，第二个参数是 Promise 执行失败时的回调，两个函数只会有一个被调用。
	- then 方法的特点

		- 在 JavaScript 事件队列的当前运行完成之前，回调函数永远不会被调用。
		- 通过 .then 形式添加的回调函数，不论什么时候，都会被调用。
		- const p = new Promise(function(resolve,reject){
  resolve('success');
});

p.then(function(value){
  console.log(value);
});

console.log('first');
// first
// success
		- 通过多次调用,可以添加多个回调函数，它们会按照插入顺序并且独立运行。
		- const p = new Promise(function(resolve,reject){
  resolve(1);
}).then(function(value){ // 第一个then // 1
  console.log(value);
  return value * 2;
}).then(function(value){ // 第二个then // 2
  console.log(value);
}).then(function(value){ // 第三个then // undefined
  console.log(value);
  return Promise.resolve('resolve'); 
}).then(function(value){ // 第四个then // resolve
  console.log(value);
  return Promise.reject('reject'); 
}).then(function(value){ // 第五个then //reject:reject
  console.log('resolve:' + value);
}, function(err) {
  console.log('reject:' + err);
});
		- then 方法将返回一个 resolved 或 rejected 状态的 Promise 对象用于链式调用，且 Promise 对象的值就是这个返回值。

	- then 方法注意点
	
		- 简便的 Promise 链式编程最好保持扁平化，不要嵌套 Promise。

注意总是返回或终止 Promise 链。
		- const p1 = new Promise(function(resolve,reject){
  resolve(1);
}).then(function(result) {
  p2(result).then(newResult => p3(newResult));
}).then(() => p4());
		- 创建新 Promise 但忘记返回它时，对应链条被打破，导致 p4 会与 p2 和 p3 同时进行。

大多数浏览器中不能终止的 Promise 链里的 rejection，建议后面都跟上 .catch(error => console.log(error));

### generator 函数

- 作用

	- ES6 新引入了 Generator 函数，可以通过 yield 关键字，把函数的执行流挂起，为改变执行流程提供了可能，从而为异步编程提供解决方案。

- Generator 函数组成

	- Generator 有两个区分于普通函数的部分
	- 一是在 function 后面，函数名之前有个 * ；
	- 函数内部有 yield 表达式。
	- 其中 * 用来表示函数为 Generator 函数，yield 用来定义函数内部的状态。
	- function* func(){
 console.log("one");
 yield '1';
 console.log("two");
 yield '2'; 
 console.log("three");
 return '3';
}

- 执行机制

	- 调用 Generator 函数和调用普通函数一样，在函数名后面加上()即可，但是 Generator 函数不会像普通函数一样立即执行，而是返回一个指向内部状态对象的指针，所以要调用遍历器对象Iterator 的 next 方法，指针就会从函数头部或者上一次停下来的地方开始执行。
	- f.next();
// one
// {value: "1", done: false}

f.next();
// two
// {value: "2", done: false}

f.next();
// three
// {value: "3", done: true}

f.next();
// {value: undefined, done: true}

- 函数返回的遍历器对象的方法

	- next 方法

		- 一般情况下，next 方法不传入参数的时候，yield 表达式的返回值是 undefined 。当 next 传入参数的时候，该参数会作为上一步yield的返回值。

			- function* sendParameter(){
    console.log("strat");
    var x = yield '2';
    console.log("one:" + x);
    var y = yield '3';
    console.log("two:" + y);
    console.log("total:" + (x + y));
}

		- next不传参

			- var sendp1 = sendParameter();
sendp1.next();
// strat
// {value: "2", done: false}
sendp1.next();
// one:undefined
// {value: "3", done: false}
sendp1.next();
// two:undefined
// total:NaN
// {value: undefined, done: true}
next传参
var sendp2 = sendParameter();
sendp2.next(10);
// strat
// {value: "2", done: false}
sendp2.next(20);
// one:20
// {value: "3", done: false}
sendp2.next(30);
// two:30
// total:50
// {value: undefined, done: true}

		- 除了使用 next ，还可以使用 for... of 循环遍历 Generator 函数生产的 Iterator 对象。

	- return 方法

		- return 方法返回给定值，并结束遍历 Generator 函数。

return 方法提供参数时，返回该参数；不提供参数时，返回 undefined 。
		- function* foo(){
    yield 1;
    yield 2;
    yield 3;
}
var f = foo();
f.next();
// {value: 1, done: false}
f.return("foo");
// {value: "foo", done: true}
f.next();
// {value: undefined, done: true}
throw 方法
throw 方法可以再 Generator 函数体外面抛出异常，再函数体内部捕获。
var g = function* () {
  try {
    yield;
  } catch (e) {
    console.log('catch inner', e);
  }
};

var i = g();
i.next();

try {
  i.throw('a');
  i.throw('b');
} catch (e) {
  console.log('catch outside', e);
}
// catch inner a
// catch outside b
		- 遍历器对象抛出了两个错误，第一个被 Generator 函数内部捕获，第二个因为函数体内部的catch 函数已经执行过了，不会再捕获这个错误，所以这个错误就抛出 Generator 函数体，被函数体外的 catch 捕获。

	- yield* 表达式
	
		- yield* 表达式表示 yield 返回一个遍历器对象，用于在 Generator 函数内部，调用另一个 Generator 函数。
		- function* callee() {
	console.log('callee: ' + (yield));
}
function* caller() {
    while (true) {
        yield* callee();
    }
}
const callerObj = caller();
callerObj.next();
// {value: undefined, done: false}
callerObj.next("a");
// callee: a
// {value: undefined, done: false}
callerObj.next("b");
// callee: b
// {value: undefined, done: false}

// 等同于
function* caller() {
    while (true) {
        for (var value of callee) {
          yield value;
        }
    }
}

- 使用场景

	- 实现 Iterator

		- 为不具备 Iterator 接口的对象提供遍历方法。

	- function* objectEntries(obj) {
    const propKeys = Reflect.ownKeys(obj);
    for (const propKey of propKeys) {
        yield [propKey, obj[propKey]];
    }
}

const jane = { first: 'Jane', last: 'Doe' };
for (const [key,value] of objectEntries(jane)) {
    console.log(`${key}: ${value}`);
}
// first: Jane
// last: Doe

### async 函数

- async

	- async 是 ES7 才有的与异步操作有关的关键字，和 Promise ， Generator 有很大关联的。
	- 语法

		- async function name([param[, param[, ... param]]]) { statements }
		- async 函数返回一个 Promise 对象，可以使用 then 方法添加回调函数。
		- async function helloAsync(){
    return "helloAsync";
  }
  

console.log(helloAsync())  // Promise {<resolved>: "helloAsync"}

helloAsync().then(v=>{
   console.log(v);         // helloAsync
})

	- async 函数中可能会有 await 表达式，async 函数执行时，如果遇到 await 就会先暂停执行 ，等到触发的异步操作完成后，恢复 async 函数的执行并返回解析值。

await 关键字仅在 async function 中有效。如果在 async function 函数体外使用 await ，你只会得到一个语法错误。

		- function testAwait(){
   return new Promise((resolve) => {
       setTimeout(function(){
          console.log("testAwait");
          resolve();
       }, 1000);
   });
}

async function helloAsync(){
   await testAwait();
   console.log("helloAsync");
 }
helloAsync();
// testAwait
// helloAsync

- await

	- await 操作符用于等待一个 Promise 对象, 它只能在异步函数 async function 内部使用。
	- 语法

		- [return_value] = await expression;
		- expression: 一个 Promise 对象或者任何要等待的值。
		- 返回 Promise 对象的处理结果。如果等待的不是 Promise 对象，则返回该值本身。

如果一个 Promise 被传递给一个 await 操作符，await 将等待 Promise 正常处理完成并返回其处理结果。

	- function testAwait (x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function helloAsync() {
  var x = await testAwait ("hello world");
  console.log(x); 
}
helloAsync ();
// hello world
	- 正常情况下，await 命令后面是一个 Promise 对象，它也可以跟其他值，如字符串，布尔值，数值以及普通函数。

		- function testAwait(){
   console.log("testAwait");
}
async function helloAsync(){
   await testAwait();
   console.log("helloAsync");
}
helloAsync();
// testAwait
// helloAsync

	- await针对所跟不同表达式的处理方式：
	
		- Promise 对象：await 会暂停执行，等待 Promise 对象 resolve，然后恢复 async 函数的执行并返回解析值。
		- 非 Promise 对象：直接返回对应的值。

## 内容框架

### 基本内容

*XMind: ZEN - Trial Version*