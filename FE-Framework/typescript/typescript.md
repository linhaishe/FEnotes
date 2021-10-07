## 一、TypeScript 是什么

[TypeScript](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2F) 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集，而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。

TypeScript 提供最新的和不断发展的 JavaScript 特性，包括那些来自 2015 年的 ECMAScript 和未来的提案中的特性，比如异步功能和 Decorators，以帮助建立健壮的组件。下图显示了 TypeScript 与 ES5、ES2015 和 ES2016 之间的关系：

![typescript-scope-new.png](https://segmentfault.com/img/bVbH9l8)

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

当然，对于刚入门 TypeScript 的小伙伴，也可以不用安装 `typescript`，而是直接使用线上的 [TypeScript Playground](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%2F) 来学习新的语法或新特性。

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

**1.数字枚举**

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

默认情况下，NORTH 的初始值为 0，其余的成员会从 1 开始自动增长。换句话说，Direction.SOUTH 的值为 1，Direction.EAST 的值为 2，Direction.WEST 的值为 3。上面的枚举示例代码经过编译后会生成以下代码：

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
enum Direction {
  NORTH = 3,
  SOUTH,
  EAST,
  WEST,
}
```

**2.字符串枚举**

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

**3.异构枚举**

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

在 TypeScript 中，任何类型都可以被归为 any 类型。这让 any 类型成为了类型系统的顶级类型（也被称作全局超级类型）。

```typescript
let notSure: any = 666;
notSure = "Semlinker";
notSure = false;
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

众所周知，数组一般由同种类型的值组成，但有时我们需要在单个变量中存储不同类型的值，这时候我们就可以使用<mark>元组(    tuple(元组)：就是固定长度的数组)</mark>。在 JavaScript 中是没有元组的，元组是 TypeScript 中特有的类型，其工作方式类似于数组。

元组可用于定义具有有限数量的未命名属性的类型。每个属性都有一个关联的类型。使用元组时，必须提供每个属性的值。为了更直观地理解元组的概念，我们来看一个具体的例子：

```typescript
let tupleType: [string, boolean];
tupleType = ["Semlinker", true];
```

在上面代码中，我们定义了一个名为 `tupleType` 的变量，它的类型是一个类型数组 `[string, boolean]`，然后我们按照正确的类型依次初始化 tupleType 变量。与数组一样，我们可以通过下标来访问元组中的元素：

```typescript
console.log(tupleType[0]); // Semlinker
console.log(tupleType[1]); // true
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

#### 2.9 Void 类型

某种程度上来说，void 类型像是与 any 类型相反，它表示没有任何类型。当一个函数没有返回值时，你通常会见到其返回值类型是 void：

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

`never` 类型表示的是那些永不存在的值的类型。 例如，`never` 类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型。

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
```

#### 2.13 object, function

object 表示一个js对象,但是很少直接使用object，因为所有一切皆是对象，一般用于规范对象中的属性名和属性值。

```typescript
let z:object;
z = {};
z = function(){};
```

{ } 用来指定对象中可以包含哪些属性

语法：{属性名：属性值，属性名：属性值}

在属性名后面加上？，表示属性是可选的

```typescript
let u: {name: string, age?:number};
//没有得话就会报错
u = {};

u = {name: "孙悟空", age: 18};

//[propName: string]:any 表示任意类型的属性
let v: {name: string, [propName: string]:any}

v = {name:"猪八戒", age: 18, gender: '男'}
```

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
```



### 三、TypeScript 断言

有时候你会遇到这样的情况，你会比 TypeScript 更了解某个值的详细信息。通常这会发生在你清楚地知道一个实体具有比它现有类型更确切的类型。

通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。类型断言好比其他语言里的类型转换，但是不进行特殊的数据检查和解构。它没有运行时的影响，只是在编译阶段起作用。

**就是说，我清楚的知道这个数据的类型，但是TypeScript不知道，那么就是需要断言，直接和TypeScript说这个就是某某类型，其他别管。**

类型断言有两种形式：

#### 3.1 “尖括号” 语法

```typescript
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
```

#### 3.2 as 语法

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



### 四、类型的别名

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

