function sum(a, b) {
  return a + b;
}

console.log(sum(1, 2));
console.log(sum('sumFun', 2));

//类型推断

let typeCheck = '123';
typeCheck = 1;

function sum2(a, b): string {
  return '结果是： ' + a + b;
}

console.log(sum2(9, 3));

const examples = [true, '123', 4];
const examples2: (boolean | string | number)[] = [true, '123', 4];
examples2.push({ a: 1 });

//设置基本数据类型
const array2: string[] = [];
//泛型设置
const array3: Array<string> = [];
array2.push('1', 3);

//any 会失去严格的类型保护
let array5: any[] = [];

//如果使用any则会报错
class Animal {
  constructor() {}
  bark = () => 'bark';
}

const dog = new Animal();
console.log(dog.run());

//as
let age: string = '99';
//类型转换会有问题,ts是不让转换的，但是我们可以先转换成未知类型再转换成数字类型，可以通过unknown作为中间类型进行数据类型的转换
let height: number = age as unknown as number;

//void
//有返回的结果，值是null或者undefined
function sum0(a, b): void {
  a + b;
}

function sum1(a, b): number {
  return a + b;
}

//never,什么都没有
function throwError(): never {
  throw new Error('类型错误');
}

//null undefined

//一般用于promise接口请求后的返回值时使用

//默认情况下，null和undefiend可以变成其他类型的值
let str: string = '字符串';
str = null;
str = undefined;

//function

let function3: Function = () => 'string';
let test: string = function3;

//arguments 参数类型

function sum9(a: number, b: number, selectable?: number) {
  return a + b;
}

sum9(1, 2);

//type
//主要对对象和函数进行生命，之后会讲type和interface接口的区别
//简化代码，把规范统一提取出来进行定义

type userType = { name: string; age: number; gender?: string };

function addUSer(user: userType) {
  console.log('addUser' + user);
}

function updateUSer(user: userType) {
  console.log('updateUSer' + user);
}

//函数的结构定义
