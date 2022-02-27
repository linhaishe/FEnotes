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
