function sum(a, b) {
    return a + b;
}
console.log(sum(1, 2));
console.log(sum('sumFun', 2));
//类型推断
var typeCheck = '123';
typeCheck = 1;
function sum2(a, b) {
    return '结果是： ' + a + b;
}
console.log(sum2(9, 3));
var examples = [true, '123', 4];
var examples2 = [true, '123', 4];
examples2.push({ a: 1 });
//设置基本数据类型
var array2 = [];
//泛型设置
var array3 = [];
array2.push('1', 3);
//any 会失去严格的类型保护
var array5 = [];
//如果使用any则会报错
var Animal = /** @class */ (function () {
    function Animal() {
        this.bark = function () { return 'bark'; };
    }
    return Animal;
}());
var dog = new Animal();
console.log(dog.run());
//as
var age = '99';
//类型转换会有问题,ts是不让转换的，但是我们可以先转换成未知类型再转换成数字类型，可以通过unknown作为中间类型进行数据类型的转换
var height = age;
//void
//有返回的结果，值是null或者undefined
function sum0(a, b) {
    a + b;
}
function sum1(a, b) {
    return a + b;
}
//never,什么都没有
function throwError() {
    throw new Error('类型错误');
}
//null undefined
//一般用于promise接口请求后的返回值时使用
//默认情况下，null和undefiend可以变成其他类型的值
var str = '字符串';
str = null;
str = undefined;
//function
var function3 = function () { return 'string'; };
var test = function3;
//arguments 参数类型
function sum9(a, b, selectable) {
    return a + b;
}
sum9(1, 2);
function addUSer(user) {
    console.log('addUser' + user);
}
function updateUSer(user) {
    console.log('updateUSer' + user);
}
//函数的结构定义
