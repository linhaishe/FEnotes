Refs: 

1. https://www.typescriptlang.org/docs/
2. https://github.com/JasonkayZK/typescript-learn/tree/main?tab=readme-ov-file
3. https://segmentfault.com/a/1190000022876390#item-7
4. https://github.com/type-challenges/type-challenges

![image-20260117155535761](https://s2.loli.net/2026/01/17/eOfvSKHslLT37cn.png)

## 一、TypeScript 是什么

[TypeScript](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2F) 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集，而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。

TypeScript 提供最新的和不断发展的 JavaScript 特性，包括那些来自 2015 年的 ECMAScript 和未来的提案中的特性，比如异步功能和 Decorators，以帮助建立健壮的组件。下图显示了 TypeScript 与 ES5、ES2015 和 ES2016 之间的关系：

### 1.1 TypeScript 与 JavaScript 的区别

|                   TypeScript                   |                 JavaScript                 |
| :--------------------------------------------: | :----------------------------------------: |
| JavaScript 的超集用于解决大型项目的代码复杂性  |      一种脚本语言，用于创建动态网页。      |
|          可以在编译期间发现并纠正错误          |  作为一种解释型语言，只能在运行时发现错误  |
|           强类型，支持静态和动态类型           |          弱类型，没有静态类型选项          |
| 最终被编译成 JavaScript 代码，使浏览器可以理解 |           可以直接在浏览器中使用           |
|              支持模块、泛型和接口              |           不支持模块，泛型或接口           |
|          支持 ES3，ES4，ES5 和 ES6 等          |  不支持编译其他 ES3，ES4，ES5 或 ES6 功能  |
|       社区的支持仍在增长，而且还不是很大       | 大量的社区支持以及大量文档和解决问题的支持 |

### 1.2 获取 TypeScript

命令行的 TypeScript 编译器可以使用 Node.js 包来安装。

**1.安装 TypeScript**

```shell
$ npm install -g typescript
```

**2.编译 TypeScript 文件**

```shell
$ tsc helloworld.ts
# helloworld.ts => helloworld.js
```

当然，对于刚入门 TypeScript 的小伙伴，也可以不用安装 `typescript`，而是直接使用线上的 [TypeScript Playground](https://www.typescriptlang.org/play) 来学习新的语法或新特性。

## 二、TypeScript 基础类型

ts 传入了不是规定的数据类型，还是可以进行编译，如果没有对编译器进行配置的话。

ts可以转换成不同版本的es 语法，es3/es6，这种也可以通过配置进行处理，默认编译成es3的语法

- 类型声明

  - 类型声明是TS非常重要的一个特点；

  - 通过类型声明可以指定TS中变量（参数、形参）的类型；

  - 指定类型后，当为变量赋值时，TS编译器会自动检查值是否符合类型声明，符合则赋值，否则报错；

  - 简而言之，类型声明给变量设置了类型，使得变量只能存储某种类型的值；

  - 语法：

    - ```js
      let 变量: 类型;
      
      let 变量: 类型 = 值;
      
      function fn(参数: 类型, 参数: 类型): 类型{
          ...
      }
      ```

- 自动类型判断

  - TS拥有自动的类型判断机制
  - 当对变量的声明和赋值是同时进行的，TS编译器会自动判断变量的类型
  - 所以如果你的变量的声明和赋值时同时进行的，可以省略掉类型声明

- 类型：

  | **类型** | **例子**          | **描述**                       |
  | -------- | ----------------- | ------------------------------ |
  | number   | 1, -33, 2.5       | 任意数字                       |
  | string   | 'hi', "hi", `hi`  | 任意字符串                     |
  | boolean  | true、false       | 布尔值true或false              |
  | 字面量   | 其本身            | 限制变量的值就是该字面量的值   |
  | any      | *                 | 任意类型                       |
  | unknown  | *                 | 类型安全的any                  |
  | void     | 空值（undefined） | 没有值（或undefined）          |
  | never    | 没有值            | 不能是任何值                   |
  | object   | {name:'孙悟空'}   | 任意的JS对象                   |
  | array    | [1,2,3]           | 任意JS数组                     |
  | tuple    | [4,5]             | 元素，TS新增类型，固定长度数组 |
  | enum     | enum{A, B}        | 枚举，TS中新增类型             |

#### 2.1 Boolean 类型

<mark>如果变量的声明和赋值时同时进行的，TS可以自动对变量进行类型检测</mark>

但是不建议省略，方便后期维护

```typescript
let isDone: boolean = false;
// ES5：var isDone = false;

// 如果变量的声明和赋值时同时进行的，TS可以自动对变量进行类型检测
let c = false;
c = true;
//赋值为number会报错，因为ts会隐性进行数值类型赋值
c = 123;
```

#### 2.2 Number 类型

```typescript
let count: number = 10;
// ES5：var count = 10;
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 100n;
```

#### 2.3 String 类型

```typescript
let name: string = "Semliker";
// ES5：var name = 'Semlinker';
let color: string = "blue";
color = 'red';

let fullName: string = `Bob Bobbington`;
let age: number = 37;
let sentence: string = `Hello, my name is ${fullName}.

I'll be ${age + 1} years old next month.`;
```

#### 2.4 Array 类型

```typescript
let list: number[] = [1, 2, 3];
// ES5：var list = [1,2,3];

let list: Array<number> = [1, 2, 3]; // Array<number>泛型语法
// ES5：var list = [1,2,3];

//string[] 表示字符串数组
let e1:string[];
e1 = ['a','b','c'];
```

#### 2.5 Enum 类型

使用枚举我们可以定义一些带名字的常量。 使用枚举可以清晰地表达意图或创建一组有区别的用例。 TypeScript 支持数字的和基于字符串的枚举。枚举就是把我们所有的可能的情况都列出来。

##### **1.数字枚举**

```typescript
enum Gender{
    Male = 0,
    Female = 1,
}
let i: {name: string, gender: Gender};
i = {
    name: '孙悟空',
    gender: Gender.Male//'male'
}

console.log(i.gender === Gender.Male)
```

```typescript
enum Direction {
  NORTH,
  SOUTH,
  EAST,
  WEST,
}

let dir: Direction = Direction.NORTH;
```

默认情况下，NORTH 的<mark>初始值为 0，其余的成员会从 1 开始自动增长。</mark>换句话说，Direction.SOUTH 的值为 1，Direction.EAST 的值为 2，Direction.WEST 的值为 3。上面的枚举示例代码经过编译后会生成以下代码：

```javascript
"use strict";
var Direction;
(function (Direction) {
  Direction[(Direction["NORTH"] = 0)] = "NORTH";
  Direction[(Direction["SOUTH"] = 1)] = "SOUTH";
  Direction[(Direction["EAST"] = 2)] = "EAST";
  Direction[(Direction["WEST"] = 3)] = "WEST";
})(Direction || (Direction = {}));
var dir = Direction.NORTH;
```

当然我们也可以设置 NORTH 的初始值，比如：

```typescript
//给枚举赋值，后面的数据会自增
enum Direction {
  NORTH = 3,
  SOUTH,
  EAST,
  WEST,
}

enum Color {
  red, // 0
  blue = 2, //2
  yellow //3
}

//赋值字符串不会自增,那么后一个枚举属性必须赋值，否则不会自增
enum Color {
  red, // 0
  blue = 'abc', 
  yellow = 3 //3
}

```

```ts
//初始值为 0，其余的成员会从 1 开始自动增长
enum Color{
  red,
  green,
  blue
}

//相当于
/*
{
red:0,
green:1,
yellow:2,
o:'red',
1:'green',
2:'yellow'
}
*/

console.log(Color.red) // 0

//反向映射
console.log(Color[0]) // red
```

##### **2.字符串枚举**

在 TypeScript 2.4 版本，允许我们使用字符串枚举。在一个字符串枚举里，每个成员都必须用字符串字面量，或另外一个字符串枚举成员进行初始化。

```typescript
enum Direction {
  NORTH = "NORTH",
  SOUTH = "SOUTH",
  EAST = "EAST",
  WEST = "WEST",
}
```

以上代码对于的 ES5 代码如下：

```typescript
"use strict";
var Direction;
(function (Direction) {
    Direction["NORTH"] = "NORTH";
    Direction["SOUTH"] = "SOUTH";
    Direction["EAST"] = "EAST";
    Direction["WEST"] = "WEST";
})(Direction || (Direction = {}));
```

##### **3.异构枚举**

异构枚举的成员值是数字和字符串的混合：

```typescript
enum Enum {
  A,
  B,
  C = "C",
  D = "D",
  E = 8,
  F,
}
```

以上代码对于的 ES5 代码如下：

```typescript
"use strict";
var Enum;
(function (Enum) {
    Enum[Enum["A"] = 0] = "A";
    Enum[Enum["B"] = 1] = "B";
    Enum["C"] = "C";
    Enum["D"] = "D";
    Enum[Enum["E"] = 8] = "E";
    Enum[Enum["F"] = 9] = "F";
})(Enum || (Enum = {}));
```

通过观察上述生成的 ES5 代码，我们可以发现数字枚举相对字符串枚举多了 “反向映射”：

```javascript
console.log(Enum.A) //输出：0
console.log(Enum[0]) // 输出：A
```

#### 2.6 Any 类型

在 TypeScript 中，任何类型都可以被归为 any 类型。这让 any 类型成为了类型系统的顶级类型（也被称作全局超级类型）。一般在获取DOM类型使用。我们在接收用户输入 或 第三方代码库时，还不确定会返回什么值，此时也可以使用any类型。

```typescript
let txtName: any = document.getElementById('txtN');

let notSure: any = 666;
notSure = "Semlinker";
notSure = false;

//default value= 4
let d: any = 4;
d = 'hello';
d = true;
```

`any` 类型本质上是类型系统的一个逃逸舱。作为开发者，这给了我们很大的自由：TypeScript 允许我们对 `any` 类型的值执行任何操作，而无需事先执行任何形式的检查。比如：

```typescript
let value: any;

value.foo.bar; // OK
value.trim(); // OK
value(); // OK
new value(); // OK
value[0][1]; // OK
```

```js
//any 表示的是任意类型，一个变量设置类型为any后相当于对该变量关闭了TS的类型检测
//使用TS时，不建议使用any类型

//显示any
let d:any;

//隐式的any
//声明变量如果不指定类型，则TS解析器会自动判断变量的类型为any（隐式的any）
let d;
d = 10;
d = 'hello';
d = 'true';
```

在许多场景下，这太宽松了。使用 `any` 类型，可以很容易地编写类型正确但在运行时有问题的代码。如果我们使用 `any` 类型，就无法使用 TypeScript 提供的大量的保护机制。为了解决 `any` 带来的问题，TypeScript 3.0 引入了 `unknown` 类型。

#### 2.7 Unknown 类型

就像所有类型都可以赋值给 `any`，所有类型也都可以赋值给 `unknown`。这使得 `unknown` 成为 TypeScript 类型系统的另一种顶级类型（另一种是 `any`）。下面我们来看一下 `unknown` 类型的使用示例：

```typescript
let value: unknown;

value = true; // OK
value = 42; // OK
value = "Hello World"; // OK
value = []; // OK
value = {}; // OK
value = Math.random; // OK
value = null; // OK
value = undefined; // OK
value = new TypeError(); // OK
value = Symbol("type"); // OK
```

对 `value` 变量的所有赋值都被认为是类型正确的。但是，当我们尝试将类型为 `unknown` 的值赋值给其他类型的变量时会发生什么？

```typescript
let value: unknown;

let value1: unknown = value; // OK
let value2: any = value; // OK
let value3: boolean = value; // Error
let value4: number = value; // Error
let value5: string = value; // Error
let value6: object = value; // Error
let value7: any[] = value; // Error
let value8: Function = value; // Error
```

`unknown` 类型只能被赋值给 `any` 类型和 `unknown` 类型本身。直观地说，这是有道理的：只有能够保存任意类型值的容器才能保存 `unknown` 类型的值。毕竟我们不知道变量 `value` 中存储了什么类型的值。

现在让我们看看当我们尝试对类型为 `unknown` 的值执行操作时会发生什么。以下是我们在之前 `any` 章节看过的相同操作：

```typescript
let value: unknown;

value.foo.bar; // Error
value.trim(); // Error
value(); // Error
new value(); // Error
value[0][1]; // Error
```

将 `value` 变量类型设置为 `unknown` 后，这些操作都不再被认为是类型正确的。通过将 `any` 类型改变为 `unknown` 类型，我们已将允许所有更改的默认设置，更改为禁止任何更改。

#### 2.8 Tuple 类型

就是一个规定了元素数量和每个元素类型的‘数组’，而每个元素的类型，可以不相同。

作用：TS中，数组元素类型必需一致，如果需要不同元素，就可以使用元组。

特点：声明时，要指定元素个数

众所周知，数组一般由同种类型的值组成，但有时我们需要在单个变量中存储不同类型的值，这时候我们就可以使用<mark>元组(    tuple(元组)：就是固定长度的数组)</mark>。在 JavaScript 中是没有元组的，元组是 TypeScript 中特有的类型，其工作方式类似于数组。

元组可用于定义具有有限数量的未命名属性的类型。每个属性都有一个关联的类型。使用元组时，必须提供每个属性的值。为了更直观地理解元组的概念，我们来看一个具体的例子：

```typescript
let tupleType: [string, boolean];
tupleType = ["Semlinker", true];

//还可以这么写
let tupleType: [string, boolean] = ["Semlinker", true];

//重新赋值不影响，但是数据也是要按照规定的内容写
tupleType = ["h h h h", false];

```

在上面代码中，我们定义了一个名为 `tupleType` 的变量，它的类型是一个类型数组 `[string, boolean]`，然后我们按照正确的类型依次初始化 tupleType 变量。与数组一样，我们可以通过下标来访问元组中的元素：

```typescript
//可以访问元组的长度和元组中的元素
console.log(tupleType[0]); // Semlinker
console.log(tupleType[1]); // true

console.log(tupleType.length);
```

在元组初始化的时候，如果出现类型不匹配的话，比如：

```typescript
tupleType = [true, "Semlinker"];
```

此时，TypeScript 编译器会提示以下错误信息：

```delphi
[0]: Type 'true' is not assignable to type 'string'.
[1]: Type 'string' is not assignable to type 'boolean'.
```

很明显是因为类型不匹配导致的。在元组初始化的时候，我们还必须提供每个属性的值，不然也会出现错误，比如：

```typescript
tupleType = ["Semlinker"];
```

此时，TypeScript 编译器会提示以下错误信息：

```typescript
Property '1' is missing in type '[string]' but required in type '[string, boolean]'.
```



```

```



#### 2.9 Void 类型

某种程度上来说，void 类型像是与 any 类型相反，它表示没有任何类型。当一个函数没有返回值时，你通常会见到其返回值类型是 void：一般用在无返回值的函数。

```typescript
// 声明函数返回值为void
function warnUser(): void {
  console.log("This is my warning message");
}

//void 用来表示空，以函数为例，就表示没有返回值得函数
function fn2(): void{
  return null
  //return undefined
}

//-----
  
function sayHi2():void{
  console.log('hihihi')
}

//如需调用，直接调用即可。
sayHi2();
```

以上代码编译生成的 ES5 代码如下：

```typescript
"use strict";
function warnUser() {
  console.log("This is my warning message");
}


```

需要注意的是，声明一个 void 类型的变量没有什么作用，因为它的值只能为 `undefined` 或 `null`：

```typescript
let unusable: void = undefined;
```

#### 2.10 Null 和 Undefined 类型

TypeScript 里，`undefined` 和 `null` 两者有各自的类型分别为 `undefined` 和 `null`。

```typescript
let u: undefined = undefined;
let n: null = null;
```

默认情况下 `null` 和 `undefined` 是所有类型的子类型。 就是说你可以把 `null` 和 `undefined` 赋值给 `number` 类型的变量。**然而，如果你指定了`--strictNullChecks` 标记，`null` 和 `undefined` 只能赋值给 `void` 和它们各自的类型。**

#### 2.11 Never 类型

`never` 类型表示的是那些永不存在的值的类型。 例如，`never` 类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型。常用作为抛出异常或无限循环的函数返回值。

never: 表示永远不会返回结果;没有值

```typescript
// 返回never的函数必须存在无法达到的终点
function error(message: string): never {
  throw new Error(message);
}

function infiniteLoop(): never {
  while (true) {}
}
```

在 TypeScript 中，可以利用 never 类型的特性来实现全面性检查，具体示例如下：

```typescript
type Foo = string | number;

function controlFlowAnalysisWithNever(foo: Foo) {
  if (typeof foo === "string") {
    // 这里 foo 被收窄为 string 类型
  } else if (typeof foo === "number") {
    // 这里 foo 被收窄为 number 类型
  } else {
    // foo 在这里是 never
    const check: never = foo;
  }
}
```

注意在 else 分支里面，我们把收窄为 never 的 foo 赋值给一个显示声明的 never 变量。如果一切逻辑正确，那么这里应该能够编译通过。但是假如后来有一天你的同事修改了 Foo 的类型：

```typescript
type Foo = string | number | boolean;
```

然而他忘记同时修改 `controlFlowAnalysisWithNever` 方法中的控制流程，这时候 else 分支的 foo 类型会被收窄为 `boolean` 类型，导致无法赋值给 never 类型，这时就会产生一个编译错误。通过这个方式，我们可以确保

`controlFlowAnalysisWithNever` 方法总是穷尽了 Foo 的所有可能类型。 通过这个示例，我们可以得出一个结论：**使用 never 避免出现新增了联合类型没有对应的实现，目的就是写出类型绝对安全的代码。**

#### 2.12 字面量

- 也可以使用字面量去指定变量的类型，通过字面量可以确定变量的取值范围

```typescript
//也可以直接使用字面量进行类型声明

let a1:10;

a1 = 10;//但是后期不可修改有点儿类似常量了

let color: 'red' | 'blue' | 'black';
let num: 1 | 2 | 3 | 4 | 5;

//可以使用 | 来连接多个类型（联合类型）
let b1: "male" | "female";

b1= "male";
b1= "female";

//联合类型
let c1 : boolean | string;

c1 = true;
c1 = 'hello';

//也可以使用字面量去指定变量的类型，通过字面量可以确定变量的取值范围

let color: 'red' | 'blue' | 'black';
let num: 1 | 2 | 3 | 4 | 5;
```

#### 2.13 object, function

##### object

object 表示一个js对象,但是很少直接使用object，因为所有一切皆是对象，一般用于规范对象中的属性名和属性值。

```typescript
let z:object;
z = {};
z = function(){};
```

{ } 用来指定对象中可以包含哪些属性

语法：{属性名：属性值，属性名：属性值}

在属性名后面加上？，表示属性是可选的

```ts
let u: {name: string, age?:number};
//没有得话就会报错
u = {};

u = {name: "孙悟空", age: 18};

//[propName: string]:any 表示任意类型的属性
let v: {name: string, [propName: string]:any}

v = {name:"猪八戒", age: 18, gender: '男'}
```

##### function

<mark>实参和形参的类型和数量要一致</mark>

没有返回值，则函数后跟void,如果有返回值则写对应的数据类型。

###### 函数 返回值类型

```typescript
//特点：实参和形参的类型、数量都要一致

//函数 返回值类型

function 函数名():返回值类型{};
let 变量名:变量名:变量类型 = 函数名();

function sayHi():string{
  return 'hi!'
}

let res1:string = sayHi();
console.log(res1);
```

###### 函数 形参类型

```ts
//函数 形参类型

function 函数名(形参1:类型,形参2:类型)：返回值类型{}
let 变量名:变量类型=函数名(实参1,实参2);

//实参和形参的类型和数量要一致,为形参指定数据类型，编译器会对形参指定的实参做类型检查，保证形参和形参一致。

function jumpSan(cityName:string):void{
  console.log('where you wanna go?');
  console.log(`yep ,here we go${cityName}`);
}
```

###### 函数 可选参数

加上问号之后表示，参数可穿可不传。

`function 函数名(形参？:类型):返回值{}`

###### 函数 默认值

如果参数没有传递，则使用默认值。带默认值的参数，本身也是可选参数.

有默认值之后，可以不用填写问号字符，因为自带可传的属性了。

`function 函数名(形参1:类型=默认值1，形参2:类型=默认值2):返回值类型{}`

```
//不传递实参

函数名()--->函数名(默认值1，默认值2)

//传1个实参

函数名(实参1)--->函数名(实参1，默认值2)

//传两个实参

函数名(实参1，实参2)--->函数名(实参1，实参2)

//传第二个实参，不传第一个

函数名(undefined,实参2)--->函数名(默认值1，实参2)

```

```ts
function byGun(gunName: string, gunNum?: number): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun("233Gun");

//Parameter cannot have question mark and initializer.
function byGun(gunName:string='M416',gunNum?:number=1):void{
    console.log(`we gonna buy ${gunName} quantity of ${gunNum?gunNum:1} `)
}

byGun();

function byGun(gunName:string='M416',gunNum:number=1):void{
    console.log(`we gonna buy ${gunName} quantity of ${gunNum?gunNum:1} `)
}

byGun();

//形参没有传参默认就是undefined
function byGun(gunName: string = "M416", gunNum: number = 1): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun(undefined,30);
```

###### 函数 剩余参数

`function add(形参1:类型,形参2:类型,...形参2:类型[]):void{console.log(a+b)}`

1. 剩余参数只能定义一个
2. 剩余参数只能定义为数组
3. 剩余参数只能定义在形参列表最后
4. 形参没有传参默认就是undefined

```typescript
/* 
    多行注释（块注释）：' Alt+Shift+A ’
    设置函数结构的类型声明：
        语法: (形参：类型，形参：类型...)=> 返回值
*/

//这样限制基本没有什么意义，我们需要的是限制函数的结构，它有几个参数和返回值的类型。

//let d1 :Function;
//用类似于箭头函数的方式处理，设置函数的类型声明
let d1: (a:number ,b: number)=>number;

d1 = function (n1: number, n2: number): number {
    return n1 + n2
}

function add(number1: number, number2: number, ...restofNum: number[]): void {
  let resNum: number = number1 + number2;
  for (let ele of restofNum) {
    resNum += ele;
  }
  console.log("res", resNum);
}
```

#### 2.14 类型推断

如果变量的声明和初始化在同一行，可以省略掉变量类型的声明。

```typescript
let 变量名 = 值

let 变量名：变量类型 = 值

let age = 18;//已经默认number 类型
age="jack" // 报错
```

#### 2.15 联合类型 或

表示取值可以为多种类型的一种

```typescript
let 变量名：变量类型 1 ｜ 变量类型 2 = 值

//Eg. 接收promt 函数的返回值

//promt() 确定->得到用户的字符串，取消->null

let dName:string | null = promt('请输入名字')；
console.log('hello'+dname);
```

## 三、TypeScript 断言

有时候你会遇到这样的情况，你会比 TypeScript 更了解某个值的详细信息。通常这会发生在你清楚地知道一个实体具有比它现有类型更确切的类型。

通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。类型断言好比其他语言里的类型转换，但是不进行特殊的数据检查和解构。它没有运行时的影响，只是在编译阶段起作用。

**就是说，我清楚的知道这个数据的类型，但是TypeScript不知道，那么就是需要断言，直接和TypeScript说这个就是某某类型，其他别管。**

### 3.1 类型断言

#### 3.1.1 “尖括号” 语法

```typescript
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
```

#### 3.1.2 as 语法

```typescript
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;
```

```typescript
//类型断言: 可以用来告诉解析器变量的实际类型
/*
语法：
    变量 as 类型
    <类型>变量
*/
s = e as string;
s = <string>e;

function 3fn(num){
    if (num > 0) {
        return true;
    } else {
        return 123
    }  
}
```

```ts
function getLength(str: number | string): number {
    if ((str as string).length) {
        return (str as string).length
    } else {
        return str.toString().length
    }

}

console.log(getLength(1));
```

### 3.2 非空断言

```ts
function func3(arg?: string): number {
    // return arg!.length;
    return arg!.length;
    // 相当于 return arg && arg.length;
    //不传入数据会返回undefined / NaN / null

}

console.log(func3());
```

## 四、类型的别名 或|/与&/type

#### &,|,type

```typescript
//&表示同时

let j: {name: string} & {age: number};
j = {name: '孙悟空', age:18}

//报错
j = {name: '孙悟空'}

//可以使用 | 来连接多个类型（联合类型）,表示或
let b1: "male" | "female";

b1= "male";
b1= "female";

// 类型的别名,type,用于简化类型的使用
type myType = 1 | 2 | 3 | 4 | 5;

let k: myType;
let l: myType;

let m: myType;

k = 2;
//报错
k=6;
```

类型别名用来给一个类型起个新名字。

```typescript
type Message = string | string[];

let greet = (message: Message) => {
  // ...
};
```

## 五、类型守卫

> A type guard is some expression that performs a runtime check that guarantees the type in some scope. —— TypeScript 官方文档

类型保护是可执行运行时检查的一种表达式，用于确保该类型在一定的范围内。换句话说，类型保护可以保证一个字符串是一个字符串，尽管它的值也可以是一个数值。类型保护与特性检测并不是完全不同，其主要思想是尝试检测属性、方法或原型，以确定如何处理值。目前主要有四种的方式来实现类型保护：

### 4.1 in 关键字

```typescript
interface Admin {
  name: string;
  privileges: string[];
}

interface Employee {
  name: string;
  startDate: Date;
}

type UnknownEmployee = Employee | Admin;

function printEmployeeInformation(emp: UnknownEmployee) {
  console.log("Name: " + emp.name);
  if ("privileges" in emp) {
    console.log("Privileges: " + emp.privileges);
  }
  if ("startDate" in emp) {
    console.log("Start Date: " + emp.startDate);
  }
}
```

### 4.2 typeof 关键字

```typescript
function padLeft(value: string, padding: string | number) {
  if (typeof padding === "number") {
      return Array(padding + 1).join(" ") + value;
  }
  if (typeof padding === "string") {
      return padding + value;
  }
  throw new Error(`Expected string or number, got '${padding}'.`);
}
```

`typeof` 类型保护只支持两种形式：`typeof v === "typename"` 和 `typeof v !== typename`，`"typename"` 必须是 `"number"`， `"string"`， `"boolean"` 或 `"symbol"`。 但是 TypeScript 并不会阻止你与其它字符串比较，语言不会把那些表达式识别为类型保护。

### 4.3 instanceof 关键字

```typescript
interface Padder {
  getPaddingString(): string;
}

class SpaceRepeatingPadder implements Padder {
  constructor(private numSpaces: number) {}
  getPaddingString() {
    return Array(this.numSpaces + 1).join(" ");
  }
}

class StringPadder implements Padder {
  constructor(private value: string) {}
  getPaddingString() {
    return this.value;
  }
}

let padder: Padder = new SpaceRepeatingPadder(6);

if (padder instanceof SpaceRepeatingPadder) {
  // padder的类型收窄为 'SpaceRepeatingPadder'
}
```

### 4.4 自定义类型保护的类型谓词

```typescript
function isNumber(x: any): x is number {
  return typeof x === "number";
}

function isString(x: any): x is string {
  return typeof x === "string";
}
```

## 六、联合类型

### 5.1 联合类型

联合类型通常与 `null` 或 `undefined` 一起使用：

```typescript
const sayHello = (name: string | undefined) => {
  /* ... */
};
```

例如，这里 `name` 的类型是 `string | undefined` 意味着可以将 `string` 或 `undefined` 的值传递给`sayHello` 函数。

```typescript
sayHello("Semlinker");
sayHello(undefined);
```

通过这个示例，你可以凭直觉知道类型 A 和类型 B 联合后的类型是同时接受 A 和 B 值的类型。

### 5.2 可辨识联合

TypeScript 可辨识联合（Discriminated Unions）类型，也称为代数数据类型或标签联合类型。**它包含 3 个要点：可辨识、联合类型和类型守卫。**

这种类型的本质是结合联合类型和字面量类型的一种类型保护方法。**如果一个类型是多个类型的联合类型，且多个类型含有一个公共属性，那么就可以利用这个公共属性，来创建不同的类型保护区块。**

**1.可辨识**

可辨识要求联合类型中的每个元素都含有一个单例类型属性，比如：

```typescript
enum CarTransmission {
  Automatic = 200,
  Manual = 300
}

interface Motorcycle {
  vType: "motorcycle"; // discriminant
  make: number; // year
}

interface Car {
  vType: "car"; // discriminant
  transmission: CarTransmission
}

interface Truck {
  vType: "truck"; // discriminant
  capacity: number; // in tons
}
```

在上述代码中，我们分别定义了 `Motorcycle`、 `Car` 和 `Truck` 三个接口，在这些接口中都包含一个 `vType` 属性，该属性被称为可辨识的属性，而其它的属性只跟特性的接口相关。

**2.联合类型**

基于前面定义了三个接口，我们可以创建一个 `Vehicle` 联合类型：

```typescript
type Vehicle = Motorcycle | Car | Truck;
```

现在我们就可以开始使用 `Vehicle` 联合类型，对于 `Vehicle` 类型的变量，它可以表示不同类型的车辆。

**3.类型守卫**

下面我们来定义一个 `evaluatePrice` 方法，该方法用于根据车辆的类型、容量和评估因子来计算价格，具体实现如下：

```typescript
const EVALUATION_FACTOR = Math.PI; 

function evaluatePrice(vehicle: Vehicle) {
  return vehicle.capacity * EVALUATION_FACTOR;
}

const myTruck: Truck = { vType: "truck", capacity: 9.5 };
evaluatePrice(myTruck);
```

对于以上代码，TypeScript 编译器将会提示以下错误信息：

```delphi
Property 'capacity' does not exist on type 'Vehicle'.
Property 'capacity' does not exist on type 'Motorcycle'.
```

原因是在 Motorcycle 接口中，并不存在 `capacity` 属性，而对于 Car 接口来说，它也不存在 `capacity` 属性。那么，现在我们应该如何解决以上问题呢？这时，我们可以使用类型守卫。下面我们来重构一下前面定义的 `evaluatePrice` 方法，重构后的代码如下：

```typescript
function evaluatePrice(vehicle: Vehicle) {
  switch(vehicle.vType) {
    case "car":
      return vehicle.transmission * EVALUATION_FACTOR;
    case "truck":
      return vehicle.capacity * EVALUATION_FACTOR;
    case "motorcycle":
      return vehicle.make * EVALUATION_FACTOR;
  }
}
```

在以上代码中，我们使用 `switch` 和 `case` 运算符来实现类型守卫，从而确保在 `evaluatePrice` 方法中，我们可以安全地访问 `vehicle` 对象中的所包含的属性，来正确的计算该车辆类型所对应的价格。

## 七、交叉类型

TypeScript 交叉类型是将多个类型合并为一个类型。 这让我们可以把现有的多种类型叠加到一起成为一种类型，它包含了所需的所有类型的特性。

```typescript
interface IPerson {
  id: string;
  age: number;
}

interface IWorker {
  companyId: string;
}

type IStaff = IPerson & IWorker;

const staff: IStaff = {
  id: 'E1006',
  age: 33,
  companyId: 'EFT'
};

console.dir(staff)
```

在上面示例中，我们首先为 IPerson 和 IWorker 类型定义了不同的成员，然后通过 `&` 运算符定义了 IStaff 交叉类型，所以该类型同时拥有 IPerson 和 IWorker 这两种类型的成员。

## 八、让vscode自动变异ts文件

- 运行 tsp --init 创建 tsconfig.json文件
- 修改tsconfig.json文件，设置js文件夹，'outDir':'./js/'
- 设置vscode监视任务，之后修改项目中的ts，会自动生成js(终端，点击运行任务，点击tsc监视)

## 九、TypeScript 函数

<mark>实参和形参的类型和数量要一致</mark>

没有返回值，则函数后跟void,如果有返回值则写对应的数据类型。

### 7.1 TypeScript 函数与 JavaScript 函数的区别

| TypeScript     | JavaScript         |
| -------------- | ------------------ |
| 含有类型       | 无类型             |
| 箭头函数       | 箭头函数（ES2015） |
| 函数类型       | 无函数类型         |
| 必填和可选参数 | 所有参数都是可选的 |
| 默认参数       | 默认参数           |
| 剩余参数       | 剩余参数           |
| 函数重载       | 无函数重载         |

### 7.2 箭头函数

**1.常见语法**

```typescript
myBooks.forEach(() => console.log('reading'));

myBooks.forEach(title => console.log(title));

myBooks.forEach((title, idx, arr) =>
  console.log(idx + '-' + title);
);

myBooks.forEach((title, idx, arr) => {
  console.log(idx + '-' + title);
});
```

### 7.3 参数类型和返回类型

**返回值类型**

```typescript
//特点：实参和形参的类型、数量都要一致

//函数 返回值类型

function createUserId(name: string, id: number): string {
  return name + id;
}

function 函数名():返回值类型{};
let 变量名:变量名:变量类型 = 函数名();

function sayHi():string{
  return 'hi!'
}

let res1:string = sayHi();
console.log(res1);
```

**形参类型**

```ts
//函数 形参类型

function 函数名(形参1:类型,形参2:类型)：返回值类型{}
let 变量名:变量类型=函数名(实参1,实参2);

//实参和形参的类型和数量要一致,为形参指定数据类型，编译器会对形参指定的实参做类型检查，保证形参和形参一致。

function jumpSan(cityName:string):void{
  console.log('where you wanna go?');
  console.log(`yep ,here we go${cityName}`);
}
```

### 7.4 函数类型

```ts
/* 
    多行注释（块注释）：' Alt+Shift+A ’
    设置函数结构的类型声明：
        语法: (形参：类型，形参：类型...)=> 返回值
*/

//这样限制基本没有什么意义，我们需要的是限制函数的结构，它有几个参数和返回值的类型。

//let d1 :Function;
//用类似于箭头函数的方式处理，设置函数的类型声明
let d1: (a:number ,b: number)=>number;

d1 = function (n1: number, n2: number): number {
    return n1 + n2
}
```

```typescript
let IdGenerator: (chars: string, nums: number) => string;

function createUserId(name: string, id: number): string {
  return name + id;
}

IdGenerator = createUserId;
```

### 7.5 可选参数及默认参数

```ts
// 可选参数
function createUserId(name: string, id: number, age?: number): string {
  return name + id;
}

// 默认参数
function createUserId(
  name: string = "Semlinker",
  id: number,
  age?: number
): string {
  return name + id;
}
```

**可选参数**

加上问号之后表示，参数可穿可不传。

`function 函数名(形参？:类型):返回值{}`

**默认值**

如果参数没有传递，则使用默认值。带默认值的参数，本身也是可选参数.

有默认值之后，可以不用填写问号字符，因为自带可传的属性了。

`function 函数名(形参1:类型=默认值1，形参2:类型=默认值2):返回值类型{}`

```
//不传递实参

函数名()--->函数名(默认值1，默认值2)

//传1个实参

函数名(实参1)--->函数名(实参1，默认值2)

//传两个实参

函数名(实参1，实参2)--->函数名(实参1，实参2)

//传第二个实参，不传第一个

函数名(undefined,实参2)--->函数名(默认值1，实参2)

```

```ts
//传1个实参
function byGun(gunName: string, gunNum?: number): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun("233Gun");

//不传递实参
//Parameter cannot have question mark and initializer.
function byGun(gunName:string='M416',gunNum?:number=1):void{
    console.log(`we gonna buy ${gunName} quantity of ${gunNum?gunNum:1} `)
}

byGun();

function byGun(gunName:string='M416',gunNum:number=1):void{
    console.log(`we gonna buy ${gunName} quantity of ${gunNum?gunNum:1} `)
}

byGun();

//传第二个实参，不传第一个
//形参没有传参默认就是undefined
function byGun(gunName: string = "M416", gunNum: number = 1): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun(undefined,30);
```

### 7.6 剩余参数

`function add(形参1:类型,形参2:类型,...形参2:类型[]):void{console.log(a+b)}`

1. 剩余参数只能定义一个
2. 剩余参数只能定义为数组
3. 剩余参数只能定义在形参列表最后
4. 形参没有传参默认就是undefined

```ts
function push(array, ...items) {
  items.forEach(function (item) {
    array.push(item);
  });
}

let a = [];
push(a, 1, 2, 3);
```

```ts
function add(number1: number, number2: number, ...restofNum: number[]): void {
  let resNum: number = number1 + number2;
  for (let ele of restofNum) {
    resNum += ele;
  }
  console.log("res", resNum);
}
```

### 7.7 函数重载

函数重载或方法重载是使用相同名称和不同参数数量或类型创建多个方法的一种能力。要解决前面遇到的问题，方法就是为同一个函数提供多个函数类型定义来进行函数重载，编译器会根据这个列表去处理函数的调用。

```typescript
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: string, b: number): string;
function add(a: number, b: string): string;
function add(a: Combinable, b: Combinable) {
  if (typeof a === "string" || typeof b === "string") {
    return a.toString() + b.toString();
  }
  return a + b;
}
```

在以上代码中，我们为 add 函数提供了多个函数类型定义，从而实现函数的重载。之后，可恶的错误消息又消失了，因为这时 result 变量的类型是 `string` 类型。在 TypeScript 中除了可以重载普通函数之外，我们还可以重载类中的成员方法。

方法重载是指在同一个类中方法同名，参数不同（参数类型不同、参数个数不同或参数个数相同时参数的先后顺序不同），调用时根据实参的形式，选择与它匹配的方法执行操作的一种技术。所以类中成员方法满足重载的条件是：在同一个类中，方法名相同且参数列表不同。下面我们来举一个成员方法重载的例子：

```typescript
class Calculator {
  add(a: number, b: number): number;
  add(a: string, b: string): string;
  add(a: string, b: number): string;
  add(a: number, b: string): string;
  add(a: Combinable, b: Combinable) {
    if (typeof a === "string" || typeof b === "string") {
      return a.toString() + b.toString();
    }
    return a + b;
  }
}

const calculator = new Calculator();
const result = calculator.add("Semlinker", " Kakuqo");
```

这里需要注意的是，当 TypeScript 编译器处理函数重载时，它会查找重载列表，尝试使用第一个重载定义。 如果匹配的话就使用这个。 因此，在定义重载的时候，一定要把最精确的定义放在最前面。另外在 Calculator 类中，`add(a: Combinable, b: Combinable){ }` 并不是重载列表的一部分，因此对于 add 成员方法来说，我们只定义了四个重载方法。

## 十、TypeScript 类

### 11.1 类的属性与方法

在面向对象语言中，类是一种面向对象计算机编程语言的构造，是创建对象的蓝图，描述了所创建的对象共同的属性和方法。

在 TypeScript 中，我们可以通过 `Class` 关键字来定义一个类：

ts 的 class 描述相关的属性和方法，一种更高级的封装。其实就是把构造函数和prototype合并在一起了。

```typescript
class Greeter {
  // 静态属性
  static cname: string = "Greeter";
  // 成员属性
  greeting: string;

  // 构造函数 - 执行初始化操作，构造函数作用就是为成员变量赋值
  constructor(message: string) {
    this.greeting = message;
  }

  // 静态方法
  static getClassName() {
    return "Class name is Greeter";
  }

  // 成员方法
  greet() {
    return "Hello, " + this.greeting;
  }
}

let greeter = new Greeter("world");
console.log(greeter.greet()) // "Hello, world"
console.log(Greeter.getClassName()); //"Class name is Greeter"

//Property 'getClassName' does not exist on type 'Greeter'. Did you mean to access the static member 'Greeter.getClassName' instead?
console.log(greeter.getClassName());


```

```ts
class City {
  //成员变量
  cName: string;
  clevel: number;

  //构造函数
  constructor(name: string, level: number) {
    this.cName = name;
    this.clevel = level;
  }
  //成员方法

  about() {
    console.log(`here is ${this.cName},level is ${this.clevel}`);
  }
}

let c1 = new City("pcity", 2);

c1.about();

```



那么成员属性与静态属性，成员方法与静态方法有什么区别呢？这里无需过多解释，我们直接看一下以下编译生成的 ES5 代码：

```javascript
"use strict";
var Greeter = /** @class */ (function () {
    // 构造函数 - 执行初始化操作
    function Greeter(message) {
        this.greeting = message;
    }
    // 静态方法
    Greeter.getClassName = function () {
        return "Class name is Greeter";
    };
    // 成员方法
    Greeter.prototype.greet = function () {
        return "Hello, " + this.greeting;
    };
    // 静态属性
    Greeter.cname = "Greeter";
    return Greeter;
}());
var greeter = new Greeter("world");
```

### 11.2 访问器

在 TypeScript 中，我们可以通过 `getter` 和 `setter` 方法来实现数据的封装和有效性校验，防止出现异常数据。

```typescript
let passcode = "Hello TypeScript";

class Employee {
  private _fullName: string;

  get fullName(): string {
    return this._fullName;
  }

  set fullName(newName: string) {
    if (passcode && passcode == "Hello TypeScript") {
      this._fullName = newName;
    } else {
      console.log("Error: Unauthorized update of employee!");
    }
  }
}

let employee = new Employee();
employee.fullName = "Semlinker";
if (employee.fullName) {
  console.log(employee.fullName);
}
```

### 11.3 类的继承

继承 (Inheritance) 是一种联结类与类的层次模型。指的是一个类（称为子类、子接口）继承另外的一个类（称为父类、父接口）的功能，并可以增加它自己的新功能的能力，继承是类与类或者接口与接口之间最常见的关系。

继承是一种 [is-a ](https://link.segmentfault.com/?enc=7yFebk3Hw%2BQpxrav%2B8BPcA%3D%3D.q0PInNhvY6N0B3dkgAOWSBt%2Bvy8Med4T6lnNnAv1Qm8CtBt7GQ68VoPrIbV4g8z4)关系：

![ts-is-a.jpeg](https://segmentfault.com/img/bVPAFL)

在 TypeScript 中，我们可以通过 `extends` 关键字来实现继承：

```typescript
class Animal {
  name: string;
  
  constructor(theName: string) {
    this.name = theName;
  }
  
  move(distanceInMeters: number = 0) {
    console.log(`${this.name} moved ${distanceInMeters}m.`);
  }
}

class Snake extends Animal {
  constructor(name: string) {
    super(name);
  }
  
  move(distanceInMeters = 5) {
    console.log("Slithering...");
    super.move(distanceInMeters);
  }
}

let sam = new Snake("Sammy the Python");
sam.move();
```

### 11.4 ECMAScript 私有字段

在 TypeScript 3.8 版本就开始支持**ECMAScript 私有字段**，使用方式如下：

```typescript
class Person {
  #name: string;

  constructor(name: string) {
    this.#name = name;
  }

  greet() {
    console.log(`Hello, my name is ${this.#name}!`);
  }
}

let semlinker = new Person("Semlinker");

semlinker.#name;
//     ~~~~~
// Property '#name' is not accessible outside class 'Person'
// because it has a private identifier.
```

与常规属性（甚至使用 `private` 修饰符声明的属性）不同，私有字段要牢记以下规则：

- 私有字段以 `#` 字符开头，有时我们称之为私有名称；
- 每个私有字段名称都唯一地限定于其包含的类；
- 不能在私有字段上使用 TypeScript 可访问性修饰符（如 public 或 private）；
- 私有字段不能在包含的类之外访问，甚至不能被检测到。

## 十一、TypeScript 数组

### 8.1 数组解构

```typescript
let x: number; let y: number; let z: number;
let five_array = [0,1,2,3,4];
[x,y,z] = five_array;
```

### 8.2 数组展开运算符

```typescript
let two_array = [0, 1];
let five_array = [...two_array, 2, 3, 4];
```

### 8.3 数组遍历

```typescript
let colors: string[] = ["red", "green", "blue"];
for (let i of colors) {
  console.log(i);
}
```

## 十二、TypeScript 接口

在面向对象语言中，接口是一个很重要的概念，它是对行为的抽象，而具体如何行动需要由类去实现。

TypeScript 中的接口是一个非常灵活的概念，除了可用于[对类的一部分行为进行抽象](https://link.segmentfault.com/?enc=4N%2FL3%2FRAgzgtJPIfjP1boQ%3D%3D.I6Iy0PNn89x8e9Gt8qD05%2FJDo%2F0XzSyap6Jy7%2BcP02EOkRvScJWajLdo43Vm9pOqEG8IgyKJatL%2BVwR3W%2FLRF7iplAVWcWexBdCtJRwWEh0MMqEFVq11LTl4K4yG9qYBbaEjjeGriqG5OY6k5ICwcw%3D%3D)以外，也常用于对「对象的形状（Shape）」进行描述。

### 10.1 对象的形状

```typescript
//对象，使用接口来定义类型,接口和属性的数量和类型必须一致
interface Person1 {
  name: string;
  age: number;
}

let Semlinker: Person = {
  name: "Semlinker",
  age: 33,
};

//会报错，数量不一致
let Semlinker3: Person = {
  name: "Semlinker",
};

//定义空对象也会报错
let Semlinker2: Person = {};
```

### 10.2 可选 | 只读属性

```typescript
interface Person2 {
  readonly name: string;
  //可选属性
  age?: number;
}
```

只读属性用于限制只能在对象刚刚创建的时候修改其值。此外 TypeScript 还提供了 `ReadonlyArray<T>` 类型，它与 `Array<T>` 相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改。

```typescript
let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
ro[0] = 12; // error!
ro.push(5); // error!
ro.length = 100; // error!
a = ro; // error!
```

### 10.3 接口继承

- 单个接口继承

```ts
//单个接口继承

interface Person1 {
    name: string;
    age: number;
}

interface jackPerson extends Person1 {
    hobby: Array<string>;
}

//数量不一致也会报错
//Property 'name' is missing in type '{ age: number; hobby: string[]; }' but required in type 'jackPerson'.(2741)
let jackPerson: jackPerson = {
    // name: "Semlinker",
    age: 33,
    hobby: ['吃饭', '睡觉']
}

console.log(jackPerson)
```

- 多个接口继承
  - 可以通过extends实现多个接口继承
  - 也可以通过&实现多个接口继承

```ts
interface IName {
    name: string
}

interface IAge {
    age: number
}

//可以通过extends实现多个接口继承
interface Person extends IName, IAge {
    sex: string
}

let person3: Person = {
    name: '张三',
    age: 20,
    sex: '男'
}
```

```ts
interface IName {
    name: string
}

interface IAge {
    age: number
}

//可以通过extends实现多个接口继承
interface Person extends IName, IAge {
    sex: string
}

let person3: IName & IAge & Person = {
    name: '张三',
    age: 20,
    sex: '男'
}
```

### 10.4 不确定的属性

不确定的属性都是可选属性，可传入也可不传入

```ts
interface Person {
    [propName: string]: any
}

let person: Person = {}
let person2: Person = {
    a: 1
}
```

### 10.5 接口实现

```ts
interface Person {
    name: string;
    age: number;
    sex: string;
    getName: () => string;
    getAge(): number;
}

class onePerson implements Person {
    name: string = 'Jack';
    age: number = 9;
    sex: string;
    getName(): string {
        return this.name
    };
    getAge(): number {
        return this.age
    };
    sayHello(): void {
        console.log('hello ts')
    }
}

let jack = new onePerson();
jack.sayHello();
```

## 十三、TypeScript 泛型

软件工程中，我们不仅要创建一致的定义良好的 API，同时也要考虑可重用性。 组件不仅能够支持当前的数据类型，同时也能支持未来的数据类型，这在创建大型系统时为你提供了十分灵活的功能。

**在像 C# 和 Java 这样的语言中，可以使用泛型来创建可重用的组件，一个组件可以支持多种类型的数据。 这样用户就可以以自己的数据类型来使用组件。**

设计泛型的关键目的是在成员之间提供有意义的约束，这些成员可以是：类的实例成员、类的方法、函数参数和函数返回值。

泛型（Generics）是允许同一个函数接受不同类型参数的一种模板。相比于使用 any 类型，使用泛型来创建可复用的组件要更好，因为泛型会保留参数类型。

### 12.1 泛型接口

```typescript
interface GenericIdentityFn<T> {
  (arg: T): T;
}

function func4<T>(arg: T): void {
    console.log(arg)
 }

func4<number>(123);
func4<string>('abc');
```

### 12.2 泛型类

```typescript
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) {
  return x + y;
};
```

### 12.3 泛型变量

对刚接触 TypeScript 泛型的小伙伴来说，看到 T 和 E，还有 K 和 V 这些泛型变量时，估计会一脸懵逼。其实这些大写字母并没有什么本质的区别，只不过是一个约定好的规范而已。也就是说使用大写字母 A-Z 定义的类型变量都属于泛型，把 T 换成 A，也是一样的。下面我们介绍一下一些常见泛型变量代表的意思：

- T（Type）：表示一个 TypeScript 类型
- K（Key）：表示对象中的键类型
- V（Value）：表示对象中的值类型
- E（Element）：表示元素类型

### 12.4 泛型工具类型

为了方便开发者 TypeScript 内置了一些常用的工具类型，比如 Partial、Required、Readonly、Record 和 ReturnType 等。出于篇幅考虑，这里我们只简单介绍 Partial 工具类型。不过在具体介绍之前，我们得先介绍一些相关的基础知识，方便读者自行学习其它的工具类型。

**1.typeof**

在 TypeScript 中，`typeof` 操作符可以用来获取一个变量声明或对象的类型。

```typescript
interface Person {
  name: string;
  age: number;
}

const sem: Person = { name: 'semlinker', age: 30 };
type Sem= typeof sem; // -> Person

function toArray(x: number): Array<number> {
  return [x];
}

type Func = typeof toArray; // -> (x: number) => number[]
```

**2.keyof**

`keyof` 操作符可以用来一个对象中的所有 key 值：

```typescript
interface Person {
    name: string;
    age: number;
}

type K1 = keyof Person; // "name" | "age"
type K2 = keyof Person[]; // "length" | "toString" | "pop" | "push" | "concat" | "join" 
type K3 = keyof { [x: string]: Person };  // string | number
```

**3.in**

`in` 用来遍历枚举类型：

```typescript
type Keys = "a" | "b" | "c"

type Obj =  {
  [p in Keys]: any
} // -> { a: any, b: any, c: any }
```

**4.infer**

在条件类型语句中，可以用 `infer` 声明一个类型变量并且对它进行使用。

```typescript
type ReturnType<T> = T extends (
  ...args: any[]
) => infer R ? R : any;
```

以上代码中 `infer R` 就是声明一个变量来承载传入函数签名的返回值类型，简单说就是用它取到函数返回值的类型方便之后使用。

**5.extends**

有时候我们定义的泛型不想过于灵活或者说想继承某些类等，可以通过 extends 关键字添加泛型约束。

```typescript
interface ILengthwise {
  length: number;
}

function loggingIdentity<T extends ILengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}
```

现在这个泛型函数被定义了约束，因此它不再是适用于任意类型：

```typescript
loggingIdentity(3);  // Error, number doesn't have a .length property
```

这时我们需要传入符合约束类型的值，必须包含必须的属性：

```typescript
loggingIdentity({length: 10, value: 3});
```

**6.Partial**

`Partial<T>` 的作用就是将某个类型里的属性全部变为可选项 `?`。

**定义：**

```typescript
/**
 * node_modules/typescript/lib/lib.es5.d.ts
 * Make all properties in T optional
 */
type Partial<T> = {
  [P in keyof T]?: T[P];
};
```

在以上代码中，首先通过 `keyof T` 拿到 `T` 的所有属性名，然后使用 `in` 进行遍历，将值赋给 `P`，最后通过 `T[P]` 取得相应的属性值。中间的 `?` 号，用于将所有属性变为可选。

**示例：**

```typescript
interface Todo {
  title: string;
  description: string;
}

function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) {
  return { ...todo, ...fieldsToUpdate };
}

const todo1 = {
  title: "organize desk",
  description: "clear clutter",
};

const todo2 = updateTodo(todo1, {
  description: "throw out trash",
});
```

在上面的 `updateTodo` 方法中，我们利用 `Partial<T>` 工具类型，定义 `fieldsToUpdate` 的类型为 `Partial<Todo>`，即：

```typescript
{
   title?: string | undefined;
   description?: string | undefined;
}
```

## 十四、TypeScript 对象

### 9.1 对象解构

```typescript
let person = {
  name: "Semlinker",
  gender: "Male",
};

let { name, gender } = person;
```

### 9.2 对象展开运算符

```typescript
let person = {
  name: "Semlinker",
  gender: "Male",
  address: "Xiamen",
};

// 组装对象
let personWithAge = { ...person, age: 33 };

// 获取除了某些项外的其它项
let { name, ...rest } = person;
```

## 十五、TypeScript 装饰器

### 13.1 装饰器是什么

- 它是一个表达式
- 该表达式被执行后，返回一个函数
- 函数的入参分别为 target、name 和 descriptor
- 执行该函数后，可能返回 descriptor 对象，用于配置 target 对象

### 13.2 装饰器的分类

- 类装饰器（Class decorators）
- 属性装饰器（Property decorators）
- 方法装饰器（Method decorators）
- 参数装饰器（Parameter decorators）

### 13.3 类装饰器

类装饰器声明：

```typescript
declare type ClassDecorator = <TFunction extends Function>(
  target: TFunction
) => TFunction | void;
```

类装饰器顾名思义，就是用来装饰类的。它接收一个参数：

- target: TFunction - 被装饰的类

看完第一眼后，是不是感觉都不好了。没事，我们马上来个例子：

```typescript
function Greeter(target: Function): void {
  target.prototype.greet = function (): void {
    console.log("Hello Semlinker!");
  };
}

@Greeter
class Greeting {
  constructor() {
    // 内部实现
  }
}

let myGreeting = new Greeting();
myGreeting.greet(); // console output: 'Hello Semlinker!';
```

上面的例子中，我们定义了 `Greeter` 类装饰器，同时我们使用了 `@Greeter` 语法糖，来使用装饰器。

> 友情提示：读者可以直接复制上面的代码，在 [TypeScript Playground](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%2Findex.html) 中运行查看结果。

有的读者可能想问，例子中总是输出 `Hello Semlinker!` ，能自定义输出的问候语么 ？这个问题很好，答案是可以的。

具体实现如下：

```typescript
function Greeter(greeting: string) {
  return function (target: Function) {
    target.prototype.greet = function (): void {
      console.log(greeting);
    };
  };
}

@Greeter("Hello TS!")
class Greeting {
  constructor() {
    // 内部实现
  }
}

let myGreeting = new Greeting();
myGreeting.greet(); // console output: 'Hello TS!';
```

### 13.4 属性装饰器

属性装饰器声明：

```typescript
declare type PropertyDecorator = (target:Object, 
  propertyKey: string | symbol ) => void;
```

属性装饰器顾名思义，用来装饰类的属性。它接收两个参数：

- target: Object - 被装饰的类
- propertyKey: string | symbol - 被装饰类的属性名

趁热打铁，马上来个例子热热身：

```typescript
function logProperty(target: any, key: string) {
  delete target[key];

  const backingField = "_" + key;

  Object.defineProperty(target, backingField, {
    writable: true,
    enumerable: true,
    configurable: true
  });

  // property getter
  const getter = function (this: any) {
    const currVal = this[backingField];
    console.log(`Get: ${key} => ${currVal}`);
    return currVal;
  };

  // property setter
  const setter = function (this: any, newVal: any) {
    console.log(`Set: ${key} => ${newVal}`);
    this[backingField] = newVal;
  };

  // Create new property with getter and setter
  Object.defineProperty(target, key, {
    get: getter,
    set: setter,
    enumerable: true,
    configurable: true
  });
}

class Person { 
  @logProperty
  public name: string;

  constructor(name : string) { 
    this.name = name;
  }
}

const p1 = new Person("semlinker");
p1.name = "kakuqo";
```

以上代码我们定义了一个 `logProperty` 函数，来跟踪用户对属性的操作，当代码成功运行后，在控制台会输出以下结果：

```arcade
Set: name => semlinker
Set: name => kakuqo
```

### 13.5 方法装饰器

方法装饰器声明：

```typescript
declare type MethodDecorator = <T>(target:Object, propertyKey: string | symbol,          
  descriptor: TypePropertyDescript<T>) => TypedPropertyDescriptor<T> | void;
```

方法装饰器顾名思义，用来装饰类的方法。它接收三个参数：

- target: Object - 被装饰的类
- propertyKey: string | symbol - 方法名
- descriptor: TypePropertyDescript - 属性描述符

废话不多说，直接上例子：

```typescript
function LogOutput(tarage: Function, key: string, descriptor: any) {
  let originalMethod = descriptor.value;
  let newMethod = function(...args: any[]): any {
    let result: any = originalMethod.apply(this, args);
    if(!this.loggedOutput) {
      this.loggedOutput = new Array<any>();
    }
    this.loggedOutput.push({
      method: key,
      parameters: args,
      output: result,
      timestamp: new Date()
    });
    return result;
  };
  descriptor.value = newMethod;
}

class Calculator {
  @LogOutput
  double (num: number): number {
    return num * 2;
  }
}

let calc = new Calculator();
calc.double(11);
// console ouput: [{method: "double", output: 22, ...}]
console.log(calc.loggedOutput); 
```

下面我们来介绍一下参数装饰器。

### 13.6 参数装饰器

参数装饰器声明：

```typescript
declare type ParameterDecorator = (target: Object, propertyKey: string | symbol, 
  parameterIndex: number ) => void
```

参数装饰器顾名思义，是用来装饰函数参数，它接收三个参数：

- target: Object - 被装饰的类
- propertyKey: string | symbol - 方法名
- parameterIndex: number - 方法中参数的索引值

```typescript
function Log(target: Function, key: string, parameterIndex: number) {
  let functionLogged = key || target.prototype.constructor.name;
  console.log(`The parameter in position ${parameterIndex} at ${functionLogged} has
    been decorated`);
}

class Greeter {
  greeting: string;
  constructor(@Log phrase: string) {
    this.greeting = phrase; 
  }
}

// console output: The parameter in position 0 
// at Greeter has been decorated
```

介绍完 TypeScript 入门相关的基础知识，猜测很多刚入门的小伙伴已有 **“从入门到放弃”** 的想法，最后我们来简单介绍一下编译上下文。

## 十六、编译上下文

### 14.1 tsconfig.json 的作用

- 用于标识 TypeScript 项目的根路径；
- 用于配置 TypeScript 编译器；
- 用于指定编译的文件。

### 14.2 tsconfig.json 重要字段

- files - 设置要编译的文件的名称；
- include - 设置需要进行编译的文件，支持路径模式匹配；
- exclude - 设置无需进行编译的文件，支持路径模式匹配；
- compilerOptions - 设置与编译流程相关的选项。

### 14.3 compilerOptions 选项

compilerOptions 支持很多选项，常见的有 `baseUrl`、 `target`、`baseUrl`、 `moduleResolution` 和 `lib` 等。

compilerOptions 每个选项的详细说明如下：





















