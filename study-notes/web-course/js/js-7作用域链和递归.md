## 作用域链

全局执行环境是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

作用域链的最前端，是当前正在执行的代码所在的那个环境。

### 特点

1.  线性的；

2. 有序的；

   不能跳过某一节去访问其它的作用域环境，也不能向下查找作用域链，进入某一个执行环境。也就是说，作用域链是【单向的】

```javascript
var color = “blue”;
function getColor(){
  var color = “red”;
  return color; }
alert(getColor());  //”red” 
```

### no overloading

局部变量会覆盖同名全局变量的原因,会向上逐级查询与给定名字匹配的标识符，indentifier,找到即停止。

```javascript
var _x = 123;

function fn(){
	var _x = 666;
	console.log( _x );
}

fn();// 666
```

## recursion

递归，函数通过名字调用自身

```javascript
function factorial(num){
  if(num<=1){
    return 1;
  }else{
    return num * factorial(num-1);
  }
}

// factorial(3) //3*2*1=6
//factorial(300) //infinity

//easy error
var anotherFactorial = factorial;
factorial = null;
alert(anotherFactorial(4));//error
```

arguments.callee指向正在执行的函数的指针

```javascript
function factorial(num){
  if(num<=1){
    return 1;
  }else{
    return num * arguments.callee(num-1);
  }
}
//cant run in strict mode
```

```javascript
//This pattern works in both nonstrict mode and strict mode. 
//named function expressions 命名函数表达式
var factorial = (function f(num){
  if(num<=1){
    retun 1;
  }else{
    return num * f(num-1);
  }
});
//In this code, a named function expression f() is created and assigned to the variable factorial. The name fremains the same even if the function is assigned to another variable, so the recursive call will always execute correctly. 
```

**例子**

```javascript
//逐级向上查询

var rain = 1;//global context
function rainman() {
    var man = 2; 
    function inner() {
        var innerVar = 4;
        console.log(rain);
    }
    inner(); 
}
rainman(); 
//1
```

```javascript
var rain = 1;    //定义全局变量 rain
function check() {
    var rain = 100;    //定义局部变量rain
    return rain;       //这里会弹出 100
}
check(); //100
console.log(rain);    //1
```

仔细观察下面的代码，你会发现变量i、j、k作用域是相同的，他们在整个rain函数体内都是全局的。

```javascript
function rainman() {
    // rainman函数体内存在三个局部变量 i j k
    var i = 0;
    if (1) {
        var j = 0;
        for (var k = 0; k < 3; k++) {
            alert(k);    //分别弹出 0 1 2
        }
        alert(k);        //弹出3
    }
    alert(j);            //弹出0
}
```

### 函数中声明的变量在整个函数中都有定义

```javascript
function rain() {
    var x = 1;
    function man() {
        x = 100;
    }
    man();        //调用man
    alert(x);    //这里会弹出 100
}
rain();    //调用rain
```

```javascript
//example 1
var rain = 1;    //定义全局变量 rain
function check() {
    var rain = 100;    //定义局部变量rain
    return rain;       //100
}

check();

console.log(rain);    //1

//example 2

function rain2() {
    var x2 = 1;
    function man2() {
        x = 100;
        return x;
    }
    man2();   
}
rain2(); 
//undefined

//example 3
var x3 = 1;
function rain3() {
    console.log(x3);        // 'undefined'，而不是1
    var x3 = 'rain-man';
    console.log(x3);        // 'rain-man'
}

//是由于在函数rain内局部变量x在整个函数体内都有定义（ var x= 'rain-man'，进行了声明），所以在整个rain函数体内隐藏了同名的全局变量x。这里之所以会弹出'undefined'是因为，第一个执行alert(x)时，局部变量x仍未被初始化。所以上面的rain函数等同于下面的函数：

function rain() {
    var x;
    console.log(x);//undefined
    x = 'rain-man';
    console.log(x);//rain-man
}

```

```javascript
//未使用var、let、const关键字声明的变量都是全局变量

function rain() {
    x = 100;    //声明了全局变量x并进行赋值
}
rain();
alert(x);    //会弹出100

//全局变量都是window对象的属性
var x = 100;
alert(window.x);//弹出100
alert(x);

//等同于下面的代码
window.x = 100;
alert(window.x);
alert(x)
```

