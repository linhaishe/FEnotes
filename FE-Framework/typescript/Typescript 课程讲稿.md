# Typescript Pre

## 入门讲解

### 1. 为什么选择ts

1. 为什么选择ts
   1. 有强的类型检查，因为js是弱类型的，我们只有在代码实际跑完之后才知道他的对与错。比如说你进行一个加减的运算，如果用户传递的是一个字符串，js是没有办法识别到的。用户传了一个字符串a，我们与数字1相加，最后输a1，这不是我们想要的结果。使用ts的话，就可以限制传入参数的类型，在开发环境的时候就能很直接的看到这错误。
   2. ts支持最新的ecmascript，一些js的最新特性它都是支持的。我们也可以选择将ts编译成不同版本的js。因为ts我们最终还是要变编译成js的。
   3. 现在有很多公司也开始往ts上靠了，对你的就业方面还是有一定的加持。

### 2. 安装相关开发环境

```
//node

//全局安装
npm install typescript -g
yarn 
brew install typesctipt

//安装版本查看
tsc -v

//常见问题
//截图

//非全局安装
//项目限定了ts版本，防止因为ts版本的不同，导致项目无法运行。使用非全局安装的方式
yarn add typesctipt -D
```

### 3.vscode的ts配置

1. 文件后缀名是ts，不同的语言都是不同的扩展名，比如css
2. js也会进行类型检查，可以在vscode的设置中进行取消，搜索validate

### 4. ts compile

```
//typescipt compile
tsc 5.ts

//监听修改
tsc 5.ts -w
```

### 5. 类型校验

也就是说，代码是否执行成功只能在运行之后才能去判断，或者在浏览器查看。js引入到html中，在控制台查看结果。

求和函数怎么会有字符串呢

我们使用ts就可以在开发环境下查看到结果。

```
node sum.ts
```

```
function sum(a: number, b: number) {
  return a + b;
}
```

1. 复杂函数中更能清晰方便看到所需填入的参数类型
2. 有些数据结构会比较复杂，有类型提示的时候就能知道我们需要什么样的数据结构。
3. 如果在编译的时候如果参数传递有误，我们会在开发阶段就能发现。

### 6. 类型推断

1. 当你不明确设置类型的时候，ts会帮你来分析，间接的来帮你设置类型。

### 7. any类型

1. 参数有很多类型可以使用
2. 有的时候我们获取到的类型我们不知道是什么类型，比如用了别人的包，它给你返回的结果你不知道是什么类型。你又不想系统报错，你就用any，但是尽量不用或者少用。
3. 使用any其实和我们用原生js没有什么区别

### 8. unknow

1. Any : 什么类型都可以，我不限定类型，不会进行ts的类型检测
2. unknow: 我不知道什么类型，但我是有类型的，会进行ts的类型检测

### 9. as

```
let age: number = '99';
let height: string = age as string;

```

### 10. void

| 空值（undefined） | 没有值（或undefined） |
| ----------------- | --------------------- |
|                   |                       |

### 11. never

----

## 枚举和断言

### 枚举

枚举在数据库中使用的非常广泛。那么我们通过例子来看下

```js
//定义一个用户
let user = {
name: 'yang',
//gender 表示的不是很明确，魔鬼数字
gender: 1
}

enum genderType {
	male = 0,
	female = 1
}

enum genderType {
	male,
	female
}

//一般枚举要么都是字符串，要么都是数字
enum genderType {
	male = '男',
	female = '女'
}

//所以有类似的场景的时候就定义一个枚举，可以更清晰的语意去表达你的内容


```

### 断言

意思我理解为 我说了算

### 泛型 generics

指的是宽泛的类型，我们先看中文描述，型--指的就是类型，就是说他最终还是一个类型，还是通过一个类型去约束我们的程序。泛---指的是宽泛的不确定的，也就是说这个类型是不确定的。

```js
//什么是确定的类型，我们只能写入字符串，因为我们类型已经严格限定了。

let city: string = 'chengdu';
```

泛型也是控制类型，使用方式和类型一样，只不过这个类型是我们动态去指定的。

```js
function city(name) {
	return name
}

function city(name: string): string {
	return name
}

function city(name: boolean): boolean {
	return name
}

function city<T>(name: T): T {
	return name
}

console.log(city<string>('chengdu'))

//函数可以接受参数，name就是参数，形参，那么<T>中T也是形参的意思。
//可以理解为类型的参数，类型也可以接受参数，function city(name: string): string，表示我们把string传递给了t。
//这样我们就动态的传递了类型。

function city<T>(name: T): T {
	return name
}

//会自动推断，可以不写类型参数
console.log(city('chengdu'))
```

### generics 的 继承 extends

```js
function getLength(arg) {
  return arg.length
}

console.log(getLength('hahaha'));
console.log(getLength([1, 2]));
console.log(getLength(19));


//那么我们就可以使用刚才的泛型进行处理
function getLength<T>(arg: T): number {
  return arg.length
}


//Property 'length' does not exist on type 'T'.
//T是我们动态传入的类型，可以传入字符串可以传入数字，number类型下是没有length属性的。我们也可以这么理解，在目前我们的T里，它没有任何的规范。
//可以通过继承来解决这个问题

interface LengthInterface {
  length: number
}

function getLength<T extends LengthInterface>(arg: T): number {
  return arg.length
}

//继承之后得到的是一个类型
//那么数值类型是不满足这个约定的，那么就会报错。
//这个约定是这个借口

interface LengthInterface {
  length: number
}
console.log(getLength(19));

//这个概念类似于

type stype = {length: number}
let a: stype = 'shdfihsfusdf';
a = 23;

interface LengthInterface {length: number}
let a: LengthInterface = 'shdfihsfusdf';
//数字没有length类型，不满足类型约束，就报错了；
a = 23;

function getLength<T extends string | any[]>(arg: T): number {
  return arg.length
}

//T就用来约定数组的类型，数组是有length属性的，就不会报错
function getLength<T>(arg: T[]): number {
  return arg.length
}

1. t没有类型约束，他的类型是你传递过来的类型
2. 使用extends保证传递过来的参数这个类型都有length属性，这个时候就不会报错

```

### 泛型与类

```js
class collectionNumber {
  data: number[] = [];
	public push(...items: number[]) {
    this.data.push(...items)
  }

	public shift():number {
    return this.data.shift()
  }
}

const numberCollection = new collectionNumber();
numberCollection.push(12,3,4);

class Collection<T> {
  data: T[] = [];
	public push(...items: T[]) {
    this.data.push(...items)
  }

	public shift():T {
    return this.data.shift()
  }
}

const numberCollection1 = new Collection<number>();
const numberCollection2 = new Collection<string>();

type User = {name: string, age: number}
const user = {name: 'hah', age: 18}

const numberCollection2 = new Collection<User>();
numberCollection2.push(user)

```

## 类与接口

### 使用ts来约束class

```js
class User {
  name: string
  age: number

  constructor(n: string, a: number) {
    this.name = n
    this.age = a
  }

  info(): string {
    return `${this.name}的年龄是${this.age}`
  }
}

const user1 = new User('heather', 18);
const user2 = new User('33', 99);
console.log(user1.info());

const userList: User[] = [];

userList.push(user1, user2);
console.log(userList);
```

### Public 修饰符

默认不写的话其实就是public

```js
class User {
  name: string
  age: number

  constructor(n: string, a: number) {
    this.name = n
    this.age = a
  }

  info(): string {
    return `${this.name}的年龄是${this.age}`;
  }
}

const user2 = new User('33', 99);
console.log(user2.info());
```

### protected

[protected](https://so.csdn.net/so/search?q=protected&spm=1001.2101.3001.7020)可以修饰数据成员，构造方法，方法成员，不能修饰类（此处指外 部类，不考虑内部类）。被protected修饰的成员，能在定义它们的类中，同包 的类中被调用。如果有不同包的类想调用它们，那么这个类必须是定义它们的类 的子类。 

```js
class User {
  public name: string
  protected age: number

  constructor(n: string, a: number) {
    this.name = n
    this.age = a
  }

  protected info(): string {
    return `${this.name}的年龄是${this.age}`
  }

	public show(){
    return this.info()
  }
}

//同包类中被调用
const user2 = new User('33', 99);
console.log(user2.show());


//夫子类可以使用，外部不能使用
class Person {
  public name: string
  protected age: number
  protected info(): string {
    return `${this.name}的年龄是${this.age}`
  }

}

class User extend Person {
  constructor(n:string, a: number){
    //super调用父类的构造函数
    super()
    this.name = n
    this.age = a
  }
  public show(){
   return this.info()
  }
}

const user3 = new User('33', 99);
console.log(user3.show());
```

### private

//私用，其他地方都不可以使用

```js
class User {
  private name: string
  protected age: number

  constructor(n: string, a: number) {
    this.name = n
    this.age = a
  }

  protected info(): string {
    return `${this.name}的年龄是${this.age}`
  }

	public show(){
    return this.info()
  }
}

const user3 = new User('33', 99);
console.log(user3.name);
```

### static

静态属性，静态方法; 可以写一些公共的，不需要分给对象的方法用static去写,省内存。公共的东西放在静态里。类似于缓存的概念。

```js
class Axios {
static site: string = 'push.com'
public static getSite(): string {
return Axios.site
}
const instance = new Axios()
// console.log(Axios.site)
console.log(Axios.getSite())
}
```

### 构造函数中使用ts泛型

```js
class User {
  user = null
public construtor(user){
  this.user = user
}
//...
}

class User<T> {
public constructor(private _user: T){}
public get(): T {
return this._user
}
}

interface IUser {
name: string
age: number
}

const obj = new User<IUser>({name: 'hah', age: 23});
console.log(obj.get().name)
```

### 单例模式在ts中的实现

```

```















