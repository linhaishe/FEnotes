// 整体思路
// 1.先写html显示页面
// 2.写js代码，获取html元素，然后写函数
// 3.将html元素,函数和事件绑定

//获取html中的元素以及他的值，才能与js代码相连通，js代码就可以去控制html页面中的交互效果

//JS中事件绑定，是将HTML元素、事件与处理函数进行绑定

//通常将变量的定义都卸载程序最上方，统一存放。并写上注释，表明定义的变量代表了什么

//获取运算元素符号
var addBtn=document.getElementById("add");
var subBtn=document.getElementById("sub");
var mulBtn=document.getElementById("mul");
var divBtn=document.getElementById("div");

//a_float、b_float早就已经获取好了，而不理会你后来才填入的值.早先就获取好的a_float、b_float都是空的，计算不出来结果,在点击按钮后再去获取，因为你到点击按钮这一步时肯定是已经输入要运算的数字.所以，我们把获取输入框中的值，放在处理函数里面, 而不是放在这里。

//获取输入框中数字的值
// var a = document.getElementById("num1").value;
// var b = document.getElementById("num2").value;

//通过getElementById函数获得的数据全都被转换成字符串类型的数据,parseFloat()函数,会将别的类型的数据转化为浮点型的数据

// var a_float = parseFloat(a);
// var b_float = parseFloat(b);

//获取显示结果的段落元素
var show = document.getElementById("re");

//定义一个全局变量用于存放计算结果
var result;

function addtion(x,y){
    return x+y;
}

function substraction(x,y){
    return x-y;
}

function multiplication(x,y){
    return x*y;
}

function division(x,y){
    if(y==0){
        alert("0 cannot be divisible");
        return null;
    }else{
        return x/y;
    }
}

//error，Cannot set property 'onclick' of null at calculator.js:59
// addBtn.onclick=function(){
//     //获取输入框中数字的值
//     var a = document.getElementById("num1").value;
//     var b = document.getElementById("num2").value;
//     var a_float = parseFloat(a);
//     var b_float = parseFloat(b);
//     //调用含参数、带返回值的函数
//     result = addtion(a_float,b_float);
//     //将结果写入，段落元素的位置
//     show.innerHTML=result;
// };

// subBtn.onclick=function(){
//     //获取输入框中数字的值
//     var a = document.getElementById("num1").value;
//     var b = document.getElementById("num2").value;
//     var a_float = parseFloat(a);
//     var b_float = parseFloat(b);
//     //调用含参数、带返回值的函数
//     result = substraction(a_float,b_float);
//     //将结果写入，段落元素的位置
//     show.innerHTML=result;
// };

// mulBtn.onclick=function(){
//     //获取输入框中数字的值
//     var a = document.getElementById("num1").value;
//     var b = document.getElementById("num2").value;
//     var a_float = parseFloat(a);
//     var b_float = parseFloat(b);
//     //调用含参数、带返回值的函数
//     result = multiplication(a_float,b_float);
//     //将结果写入，段落元素的位置
//     show.innerHTML=result;
// };

// divBtn.onclick=function(){
//     //获取输入框中数字的值
//     var a = document.getElementById("num1").value;
//     var b = document.getElementById("num2").value;
//     var a_float = parseFloat(a);
//     var b_float = parseFloat(b);
//     //调用含参数、带返回值的函数
//     result = division(a_float,b_float);
//     //将结果写入，段落元素的位置
//     show.innerHTML=result;
// };

function getInputValue(){
    var a = document.getElementById("num1").value;
    var b = document.getElementById("num2").value;
    a_float = parseFloat(a);
    b_float = parseFloat(b);
}

function sendResult(r){
    show.innerHTML=r;
}

addBtn.onclick=function(){
    getInputValue();
    result = addtion(a_float,b_float);
    sendResult(result);
}

subBtn.onclick=function(){
    getInputValue();
    result = substraction(a_float,b_float);
    sendResult(result);
}

mulBtn.onclick=function(){
    getInputValue();
    result = multiplication(a_float,b_float);
    sendResult(result);
}

divBtn.onclick=function(){
    getInputValue();
    result = division(a_float,b_float);
    sendResult(result);
}