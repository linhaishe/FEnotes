# A. 函数

> 函数是一组有组织的、可重用的代码，用于执行单个相关操作。默认情况下，所有函数都返回一个值。

## a. 参数

> 函数参数是指在函数定义时声明的变量，用于接收函数调用时传入的值。函数参数的作用是让函数更加灵活和通用，可以接受不同的输入，并根据输入来执行不同的操作。

### 1. 函数参数类型

- 参数值类型

> 函数的参数是不具有类型限制的

1. 基本数据类型：包括字符串、数字、布尔值和 undefined。
2. 对象类型：包括对象、数组、函数、日期、正则表达式等。
3. null：虽然 null 是一个对象类型，但是在 JavaScript 中被认为是一个独立的基本数据类型。
4. Symbol：这是在 ES6 中引入的一种新的数据类型，它表示唯一的、不可变的值。

需要注意的是，在 JavaScript 中，函数的参数是不具有类型限制的，即使你在定义函数时指定了参数的类型，但实际上仍然可以传入其他类型的值。因此，在使用函数参数时，需要自行处理参数类型的问题，以确保函数的正确性和可靠性。

- 形参，实参

在调用函数时，可以传递实参来给形参赋值。如果函数有多个参数，实参之间用逗号分隔。

### 2. 传值 vs 传引用

1. 传值（by value）：将原始数据类型（例如字符串、数字、布尔值等）作为参数传递给函数时，函数会创建一个新的变量来存储传入的值，并将该变量传递给函数。在函数内部对该变量的修改不会影响到原始变量的值。
2. 传引用（by reference）：将对象类型（例如数组、对象、函数等）作为参数传递给函数时，实际上传递的是该对象在内存中的引用地址，函数参数和原始参数引用的是同一个对象，因此在函数内部对该对象的修改会影响到原始对象的值。

```js
function changeProperty(obj) {
  obj.prop = 'new value';
}

let myObj = { prop: 'old value' };
console.log(myObj.prop); // 输出 old value
changeProperty(myObj);
console.log(myObj.prop); // 输出 new value
```

### 3. 函数参数的默认值

> 函数参数的默认值是指在函数定义时，为参数指定一个默认值，这样在函数调用时如果没有传入该参数，就会使用该默认值。

#### a. 如何设置默认值

（解构设置默认值）

```js
function myFunc(param1 = defaultValue1, param2 = defaultValue2) {
  // 函数体
}
```

#### b. 默认值和 undefined 的区别

如果使用默认值的参数在函数调用时传递了一个 undefined 值，则该参数将使用默认值而不是 undefined 值。这是默认值和 undefined 的区别。传入undefined可以作为一个占位使用，如果某个参数不需要传的时候，可以传递undefined。

```js
function myFunc(param1 = 'default value') {
  console.log(param1);
}

myFunc(); // 输出 'default value'
myFunc(undefined); // 输出 'default value'
myFunc(null); // 输出 null
myFunc('other value'); // 输出 'other value'
```

### 4. 可变参数(不定参数)

不定参数（也称为可变参数）指在函数定义时不确定参数数量，使用 rest 参数将所有参数收集为一个数组。在函数体内使用该数组进行处理。

需要注意的是，不定参数必须是函数的最后一个参数。如果将其放在函数定义中的其他参数之前，那么在调用函数时，这些参数将被视为 undefined。因此，rest 参数应该始终放在函数定义中的最后一个参数位置。

```js
function myFunc(...args) {
  console.log(args);
}

myFunc(); // 输出 []
myFunc(1, 2, 3); // 输出 [1, 2, 3]
myFunc('a', 'b', 'c'); // 输出 ['a', 'b', 'c']
```

#### rest 参数

```js
function myFunc(a, b, ...rest) {
  console.log(a, b, rest);
}

myFunc(1, 2, 3, 4, 5); // 输出 1, 2, [3, 4, 5]
```

#### spread 参数

如果希望将数组中的每个元素作为单独的参数进行传递，则可以使用扩展运算符（...）来展开数组

```js
function myFunc(a, b, c) {
  console.log(a, b, c);
}

const arr = [1, 2, 3];
myFunc(...arr); // 输出 1, 2, 3
```

#### rest 和 argument 的区别

1. rest 参数是一个真正的数组，而 arguments 对象只是一个类数组对象。
2. rest 参数只包含传递给函数的实际参数，而 arguments 对象包含所有传递给函数的参数，包括函数定义时声明的参数和调用时传递的参数。
3. rest 参数可以使用 ES6 的数组方法进行处理，例如 forEach、map、filter 等，而 arguments 对象不支持这些数组方法，需要先将其转换为数组才能使用。

```js
function myFunc(...rest) {
  console.log(rest);
  console.log(arguments);
}

myFunc(1, 2, 3, 4); // 输出 [1, 2, 3, 4] 和 { '0': 1, '1': 2, '2': 3, '3': 4 }
```

### 5. 函数参数的解构

函数参数的解构是指在函数定义时使用对象解构或数组解构来获取函数参数中的某些值。通过解构，可以将需要的值从对象或数组中提取出来，使代码更加简洁易懂。

#### 使用对象解构

在函数定义时，可以使用对象解构来获取函数参数中的某些值

```js
function myFunc({ name, age }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person = { name: 'Alice', age: 20 };
myFunc(person); // 输出 "My name is Alice, and I'm 20 years old."

```

在上面的例子中，函数 myFunc 接收一个对象作为参数，并使用对象解构来获取 name 和 age 属性的值。在调用函数时，传递了一个包含 name 和 age 属性的对象作为参数。

#### 如何使用数组解构

在函数定义时，也可以使用数组解构来获取函数参数中的某些值，例如：

```js
function myFunc([first, second]) {
  console.log(`The first item is ${first}, and the second item is ${second}.`);
}

const arr = ['apple', 'orange', 'banana'];
myFunc(arr); // 输出 "The first item is apple, and the second item is orange."
```

在上面的例子中，函数 myFunc 接收一个数组作为参数，并使用数组解构来获取第一个和第二个元素的值。在调用函数时，传递了一个包含多个元素的数组作为参数。

#### 如何在函数参数中使用解构

除了在函数定义时使用解构来获取参数值之外，在函数调用时也可以使用解构来传递参数值，例如：

```js
function myFunc({ name, age }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person = { name: 'Bob', age: 30 };
myFunc(person); // 输出 "My name is Bob, and I'm 30 years old."

// 使用解构来传递参数值
myFunc({ name: 'Alice', age: 20 }); // 输出 "My name is Alice, and I'm 20 years old."
```

在上面的例子中，在第一次调用函数时，传递了一个包含 name 和 age 属性的对象作为参数。在第二次调用函数时，使用对象解构和对象字面量的方式传递参数值。

需要注意的是，在使用解构时，如果参数对象中不存在解构所需的属性，那么对应的变量将被赋值为 undefined。如果需要给变量设置默认值，可以使用解构赋值的方式，例如：

```js
function myFunc({ name = 'unknown', age = 0 }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person1 = { name: 'Bob' };
myFunc(person1); // 输出 "My name is Bob, and I'm 0 years old."

const person2 = { age: 30 };
myFunc(person2); // 输出 "My name is unknown, and I'm 30 years old."
```

###  6. 箭头函数的参数

- 在箭头函数中，如果只有一个参数，可以省略参数括号；如果有多个参数，则需要使用括号
- 如果参数需要默认值，则可以使用 ES6 中的默认参数语法。
- 箭头函数的参数没有自己的 arguments 对象。如果需要访问函数的参数，可以使用 rest 参数语法。

```js
 const func = (...args) => {
  console.log(args);
}

func(1, 2, 3); // 输出 [1, 2, 3]
```

### 7. 参数顺序

- 参数的顺序可能会影响函数的行为

- 如果函数参数有固定的顺序，但是中间的参数不想传递，可以通过在需要跳过的参数位置上使用 undefined 来实现。

- 如果不传递任何值或者传递 null 等 falsy 值时，函数会将该参数解释为缺失参数，而不是跳过该参数。因此，为了明确地跳过某个中间参数，需要显式地将其设置为 undefined。

可以考虑使用对象参数的方式，将参数封装为一个对象，这样你就可以只传递需要的参数，而不需要按照固定顺序传递所有参数。

```js
function greet({ message = "Hello", name = "World", age = null } = {}) {
  console.log(message + " " + name);
  if (age) {
    console.log("You are " + age + " years old.");
  }
}
// 使用 "= {}" 的默认参数值是为了确保当没有传入参数时，options 参数被解构时不会出现 undefined 错误。
greet(); // 输出 "Hello World"
greet({ name: "Tom" }); // 输出 "Hello Tom"
greet({ message: "Hi", name: "Alice" }); // 输出 "Hi Alice"
greet({ name: "Bob", age: 20 }); // 输出 "Hello Bob" 和 "You are 20 years old."
```

### 8. 通过参数创建函数（柯里化）

> 在 JavaScript 中，可以使用柯里化（currying）技术来通过参数创建函数。柯里化是一种将函数转换为接受一系列参数的函数序列的技术，每个序列中的函数只接受单个参数。
>
> 更通俗的讲法是，柯里化是将二维函数简化为一维函数

```js
function add(a, b) {
  return a + b;
}

function curryAdd(a) {
  return function(b) {
    return a + b;
  };
}

const add1 = curryAdd(1);
console.log(add1(2)); // 输出 3
console.log(add1(3)); // 输出 4
```

在 React 中，柯里化可以应用于很多场景，以下是几个常见的使用场景：

1. 高阶组件（Higher-Order Component，HOC）：HOC 是一个函数，它接受一个组件作为参数，并返回一个增强后的组件。HOC 可以用来实现一些横切关注点（cross-cutting concerns），例如日志、权限控制等。柯里化可以帮助我们将 HOC 的参数和返回值分别作为柯里化函数的前后两个参数，这样可以使 HOC 更加清晰和易于组合。
2. 函数式组件：函数式组件是一个只接受 props 参数并返回 React 元素的函数。柯里化可以用来将函数式组件转换为接受其他参数的函数，例如接受样式和事件处理函数等参数。这样可以使函数式组件更具通用性和可复用性。
3. 钩子函数（Hooks）：钩子函数是 React 16.8 引入的一种新的组件状态管理方式，它允许我们在函数式组件中使用状态和其他 React 特性。柯里化可以用来将钩子函数的参数分解为多个参数，这样可以使钩子函数更加清晰和易于测试。
4. 命名参数：React 组件的 props 是一个包含多个属性的对象，柯里化可以用来将这些属性拆分为多个参数，这样可以使组件的调用更具有可读性和可维护性。

## b. 返回值

JavaScript 函数的返回值是指在函数执行完毕后返回给调用者的值。函数可以返回任何 JavaScript 数据类型，包括数字、字符串、对象、数组和布尔值等。

函数的返回值通常通过 `return` 语句指定。如果函数没有指定 `return` 语句，则默认返回 `undefined` 值。

`return` 语句会立即结束函数的执行，并返回指定的值，因此函数中 `return` 语句后面的代码不会被执行。

```js
// 函数也可以返回一个对象或数组等复杂数据类型
function getPerson() {
  return {
    name: 'John',
    age: 30,
    gender: 'male'
  };
}

var person = getPerson(); 
```

## c. 闭包

> 闭包（Closure）是指函数和函数内部能访问到的变量（即自由变量）的组合。在JavaScript中，函数嵌套函数的情况非常常见，如果内部函数能够访问外部函数的变量，即使外部函数执行完毕，内部函数依然能够访问到这些变量，这种情况就称为闭包。

```js
function outer() {
  var count = 0;
  function inner() {
    count++;
    console.log(count);
  }
  return inner;
}

var increment = outer();
increment(); // 输出1
increment(); // 输出2
increment(); // 输出3
```

闭包只能取得包含函数中任何变量最后一个值，保存的是整个变量对象，不是某个特殊变量。

```js
// 只会返回10，即使是遍历函数，最终结果是10，不会返回各自不同的索引值
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(){
      return i;
    };
  }
  return result; 
} 

//强制返回各自不同的索引值
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(num){
      return function(){
        return num;
      };
    }(i);
  }
  return result;
}
```

闭包常见的应用包括：

1. 模块化开发：通过闭包来实现类似于私有变量的效果，防止变量被外部访问和修改。
2. 防抖和节流：通过闭包来实现防抖和节流等函数式编程的方法，提高程序的性能。
3. 实现回调函数：通过闭包来实现回调函数，可以让函数在异步执行时能够访问到原始的数据和环境。

在使用闭包时，需要注意以下几点：

1. 内存泄漏：由于闭包会保留外部函数的变量引用，如果不正确地使用闭包，可能会导致内存泄漏。因此，当闭包不再使用时，应该及时释放相关资源。
2. 变量共享：由于闭包可以访问外部函数的变量，因此多个闭包可能会共享同一个变量，这可能会导致不可预期的结果。为了避免这种情况，应该尽量避免使用全局变量，并在使用闭包时注意变量的作用域。
3. 性能问题：由于闭包会保留外部函数的变量引用，因此它的创建和销毁过程比普通函数要复杂。如果在循环中频繁使用闭包，可能会导致性能问题。为了避免这种情况，应该尽量避免在循环中使用闭包，并在需要使用时，尽量使用函数式编程的方法，如防抖、节流等。
4. 变量命名冲突：由于闭包可以访问外部函数的变量，因此在使用闭包时，应该避免变量命名冲突。为了避免这种情况，可以使用模块化编程的方法，将变量封装在模块内部，避免变量名冲突。

## d. 作用域

#### 作用域的基础知识

##### 什么是作用域？

作用域是指程序中定义变量的可访问范围。在JavaScript中，作用域由执行上下文和作用域链组成。执行上下文是指当前执行代码的环境，而作用域链是指在当前执行上下文中，可以访问的变量的链式结构。

##### 作用域链是什么

它由当前执行上下文的变量对象和其外部环境的变量对象构成。当代码在当前执行上下文中查找变量时，如果在当前的变量对象中找不到变量，就会在外部环境的变量对象中继续查找，直到找到该变量或者查找到全局对象。

##### 全局作用域和局部作用域

全局作用域是指在代码的任何地方都可以访问的变量，它定义在全局对象中。而局部作用域是指在特定的代码块或函数中定义的变量，只能在该代码块或函数内部访问。

在JavaScript中，每个函数都会创建一个新的局部作用域，而全局作用域则是整个程序的顶层作用域。通过合理的使用作用域和作用域链，可以避免变量名冲突，提高程序的可读性和可维护性。

#### 作用域链和执行上下文

##### 执行上下文是什么

执行上下文是 JavaScript 中用于管理代码执行的一种内部数据结构。每当 JavaScript 引擎执行一段代码时，都会创建一个执行上下文来存储该代码的相关信息，如变量、函数声明、作用域链等。执行上下文是 JavaScript 实现作用域和闭包的关键。

执行上下文是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

当代码在一个环境中执行时候，会创建变量对象的一个作用域链。作用域链的作用，保证对执行环境有权访问的所有变量和函数的有序访问。

##### 创建执行上下文的过程

1. 创建变量对象（Variable Object，VO）：变量对象是执行上下文中的一个重要概念，它用于存储该上下文中定义的变量、函数声明等信息。对于全局执行上下文来说，变量对象就是全局对象（Window），对于函数执行上下文来说，变量对象则包括了函数的参数、函数声明和内部声明的变量。
2. 建立作用域链（Scope Chain）：作用域链是用于解析标识符（变量名、函数名等）的一种机制，它由当前执行上下文的变量对象和所有外层执行上下文的变量对象组成，形成一个链式结构。当代码在当前执行上下文中访问一个变量时，JavaScript引擎会先查找当前执行上下文的变量对象，如果没找到，则在作用域链中查找。
3. 确定this指向：this指向在执行上下文创建时确定，它的值取决于函数调用方式。

##### 执行上下文栈

执行上下文栈（Execution Context Stack）是用于管理执行上下文的一种数据结构，也称为调用栈（Call Stack）。JavaScript引擎在执行代码时，会将每个执行上下文压入执行上下文栈中，当一个执行上下文执行完毕后，它会从执行上下文栈中弹出，控制权回到上一个执行上下文。

##### 作用域链的形成过程

1. 执行上下文在创建时会将当前变量对象添加到作用域链的最前端，这样当前执行上下文就可以访问到自己的变量。
2. 当代码在当前执行上下文中访问一个变量时，JavaScript引擎会先查找当前执行上下文的变量对象，如果没找到，则在作用域链中查找。作用域链的查找方向是由当前执行上下文的作用域链决定的，也就是说作用域链中靠前的变量对象拥有更高的优先级。如果在整个作用域链中都没找到该变量，则认为该变量未定义。

#### 词法作用域和动态作用域

词法作用域（Lexical Scope）和动态作用域（Dynamic Scope）是两种不同的作用域规则，它们决定了变量的可见范围和访问顺序。

词法作用域指的是作用域在代码编写时就已经确定好了，在代码的词法分析阶段就已经确定了，即在代码块中声明的变量的作用域在代码块内部。这种作用域是静态的，也就是说它的作用域范围在代码运行之前就已经确定好了。

动态作用域指的是作用域在程序运行时才能确定，它是根据函数调用栈来确定的，即当前正在执行的函数的作用域。这种作用域是动态的，也就是说它的作用域范围是随着程序运行时变化的。

JavaScript使用词法作用域。在JavaScript中，函数作用域是词法作用域，变量的作用域在函数定义时就已经确定好了，无论在何处调用函数，都会在函数内部找到相应的变量。这种作用域使得代码的行为更加可预测和易于理解。

#### ES6中的作用域

##### 块级作用域

S6中的作用域和之前的JavaScript版本中的作用域是相同的，都是基于词法作用域的。

但是，ES6中引入了块级作用域。在ES6之前，JavaScript中只有全局作用域和函数作用域，而没有块级作用域。块级作用域指的是在代码块内部定义的变量只在该块内部有效，超出该块范围就失效了。

##### const / let

ES6引入了两个新的关键字来声明块级作用域的变量：let和const。使用let或const声明的变量只在当前代码块内部有效，不会污染外部的作用域。在同一作用域中不能重复声明同名的let变量，但可以重复声明同名的const变量。变量提升的部分也会不同。

##### arrow function

ES6中也引入了箭头函数，箭头函数与普通函数不同，它没有自己的this和arguments，它的this和外层函数的this是相同的。这种特殊的函数作用域也被称为词法作用域。

##### 模板字面量中的作用域

模板字面量（Template literals）是 ES6 引入的一种字符串表达方式，可以使用反引号 `` 包裹字符串，并且支持在字符串中使用变量、表达式等语法。

在模板字面量中，变量和表达式可以通过 `${}` 语法嵌入到字符串中。这些变量和表达式的作用域和普通的 JavaScript 变量和表达式的作用域一样，都是在当前的代码块中。

举个例子：

```js
let name = "Tom";
console.log(`Hello, ${name}!`);
```

在这个例子中，模板字面量的作用域就是当前的代码块，也就是全局作用域。因为 `name` 变量是在全局作用域中定义的，所以在模板字面量中可以直接使用。

如果在模板字面量中使用的变量或表达式是在某个函数中定义的，那么它们的作用域就是这个函数的作用域。例如：

```js
function sayHello(name) {
  console.log(`Hello, ${name}!`);
}

sayHello("Tom");
```

在这个例子中，模板字面量 `${name}` 中的 `name` 变量就是在 `sayHello` 函数中定义的，因此它的作用域就是 `sayHello` 函数的作用域。

## e. 递归

> 递归是指一个函数在其定义中调用自身的过程。

1. 什么是递归？
   - 定义：递归是指一个函数在其定义中调用自身的过程。
   - 举例：计算阶乘、斐波那契数列等都可以使用递归算法实现。
2. 递归的基本原理
   - 递归必须包含一个基本情况，这个基本情况通常是指递归到一定程度时不再需要递归。
   - 递归算法通常包含两个部分：基本情况和递归情况。
3. 实现递归算法的方法
   - 递归函数的定义和调用。
   - 使用条件判断语句来判断递归结束的条件。
   - 确定递归函数的参数和返回值类型。
   - 使用递归函数来处理递归情况。
4. 递归的优缺点
   - 优点：递归能够简化问题的处理，使代码更加简洁、易读。
   - 缺点：递归调用会产生额外的函数调用开销，可能导致栈溢出等问题。
5. 递归应用场景
   - 树的遍历、搜索。
   - 分治算法。
   - 动态规划。
6. 如何避免递归问题

   - 避免无限递归：需要在函数的基本情况中终止递归。
   - 减少递归次数：可以尝试使用迭代或其他算法来避免递归。
   - 优化递归性能：可以尝试使用尾递归或记忆化递归等技术来提高递归的性能。
7. 递归的注意事项
   - 递归的边界条件：递归必须有一个边界条件，当满足该条件时，递归终止。如果没有边界条件或者边界条件不正确，递归将会无限进行，导致栈溢出。
   - 递归的递推公式：递归必须有一个递推公式，该公式描述了如何将一个问题分解成子问题。如果递推公式不正确，递归可能会产生无限循环或者结果不正确。
   - 递归的性能问题：递归可能导致栈溢出或者效率低下。因此，在使用递归时，应该考虑使用尾递归或迭代实现，避免过多的栈空间消耗和函数调用开销。
   - 递归的调试问题：递归代码通常比较难以调试，因为它会产生多层嵌套的函数调用。可以使用打印或者调试工具等方式，对递归进行调试。
   - 递归的可读性问题：递归可能导致代码变得比较复杂，因为它涉及到多层嵌套的函数调用。可以通过给函数命名、添加注释、使用尾递归等方式，提高代码的可读性。

## f. 普通函数、匿名函数、类函数、箭头函数

普通函数是指使用 `function` 关键字定义的一种函数。它可以接受参数，并且可以有返回值，可以在任何地方被调用。示例：

```js
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 输出 5
```

匿名函数是指没有函数名的函数，它通常是作为其他函数的参数传递，或者是赋值给一个变量。示例：

```js
const add = function(a, b) {
  return a + b;
};

console.log(add(2, 3)); // 输出 5
```

类函数是 ES6 引入的一种函数，它通过 `class` 关键字定义。类函数有一个构造函数和一些方法，可以用来创建对象。示例：

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHi() {
    console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

const john = new Person('John', 30);
john.sayHi(); // 输出 "Hi, my name is John and I'm 30 years old."
```

箭头函数是 ES6 引入的一种函数，它使用 `=>` 符号定义。箭头函数是匿名函数的一种特殊形式，它可以使用简洁的语法来定义函数，并且不需要使用 `function` 关键字。箭头函数没有自己的 `this`，它会使用定义时的 `this`。示例：

```js
const add = (a, b) => a + b;
console.log(add(2, 3)); // 输出 5

const person = {
  name: 'John',
  age: 30,
  sayHi: () => {
    console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old.`);
  }
};

person.sayHi(); // 输出 "Hi, my name is undefined and I'm undefined years old."
```

总结：

- 普通函数、匿名函数和类函数是三种常见的函数定义方式，用于实现不同的功能。
- 箭头函数是一种匿名函数的特殊形式，它使用简洁的语法定义函数，并且没有自己的 `this`。

## g. this指向

`this` 关键字是函数运行时自动生成的一个内部对象，只能在函数内部使用，总指向调用它的对象。

JavaScript中的`this`关键字指的是当前执行上下文的上下文对象。它的指向是在函数被调用时动态绑定的，具体取决于函数的调用方式和上下文。以下是关于`this`指向的知识内容框架：

### `this`的指向方式

- 默认绑定：在函数中直接调用，指向全局对象（在浏览器中为`window`对象，在Node.js中为`global`对象）。
- 隐式绑定：函数作为对象的方法调用时，`this`指向调用该方法的对象。
- 显式绑定：通过`call`、`apply`或`bind`方法指定函数执行时的上下文。
- new绑定：当一个函数被使用`new`关键字调用时，`this`指向新创建的实例对象。
- 箭头函数中的`this`：箭头函数没有自己的`this`绑定，它的`this`是外层作用域中的`this`。
- 如果函数使用了严格模式（'use strict'），那么在该函数中的 this 将不会指向全局对象。
- 当函数作为事件处理函数时，this 指向触发事件的元素。

需要特别注意的是，在 JavaScript 中，this 的值是在函数被调用时才确定的，而不是在函数被定义时就确定的。因此，在使用 this 关键字时，需要注意当前代码执行的上下文环境以及 this 的具体指向。

### 全局函数/匿名函数

全局函数中this = window,函数被作为某个对象的方法调用时，this等于那个对象。匿名函数的执行环境具有全局性，其this通常指向windows

```js
let message = {
  name:'john',
  regularFunction: function(){
    console.log(this)
    console.log('hello' + this.name);
    //hello john
  },
  arrowFunction:()=>console.log('hi'+this.name)
  //hi
}

message.regularFunction();
message.arrowFunction();
cnosole.log(this.name)// empty string
cnosole.log(this) // window object
```

### 箭头函数的this

箭头函数并没有属于⾃⼰的this，它所谓的this是捕获其所在上下⽂的 this 值，作为⾃⼰的 this 值。

箭头函数体内的 this 对象，就是定义该函数时所在的作用域指向的对象，而不是使用时所在的作用域指向的对象。

箭头函数的this对象是定义时所在的对象，而不是使用时所在的对象，所以指向的是the window

```javascript
var name = “The Window”;
var object = {
  name : “My Object”,
   //匿名函数
  getNameFunc : function(){
    return function(){
        //这个this指向全局，因为匿名函数的执行环境具有全局性，this.name会指向第一个出现的name
      return this.name;
    };
  } 
};
object.getNameFunc()() 
//”The Window” (in non-strict mode) 
```

在定义匿名函数之前，我们把对象赋值给了一个名叫`that`的变量，而在定义了闭包之后，闭包也可以访问这个变量，因为它是我们在包含函数中特意声明的一个变量，即使在函数返回之后，that也仍然引用着object,所以调用`object`,`getNameFunc()()`就返回了，`my object`.


```javascript
var name = “The Window”;
var object = {
  name : “My Object”,
  getNameFunc : function(){
    var that = this;
    return function(){
      return that.name;
    };
  } 
};
object.getNameFunc()()  //”My Object” 
```

# B. 类型

## 数据类型

JavaScript 中常见数据类型有Number、String、Boolean、Object、Array、Json、Function、Date、RegExp、Error、undefined、Null等十几种。ES6还有新增的数据类型有BigInt、Symbol、Set、Map等。

### Symbol BigInt Set Map

- `Symbol` 代表创建后独一无二且不可变的数据类型，它主要是为了解决可能出现的全局变量冲突的问题。 

- `BigInt` 是一种数字类型的数据，它可以表示任意精度格式的整数，使用 BigInt 可以安全地存储和操作大整数，即使这个数已经超出了 Number 能够表示的安全整数范围。

- `Set` 是ES6新增的一种新集合类型，Set 在很多方面都像是加强的Map，这是因为他们的大多数API和行为都是共有的。Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。

- `Map` 是一个带键的数据项的集合，就像一个对象一样。但是它们直接最大的差别是 Map 允许任何类型的键。

### 可分为原始数据类型和引用数据类型

- 栈：原始数据类型（Undefined、Null、Boolean、Number、String） 

- 堆：引用数据类型（对象、数组和函数）

### 包装类型

在 JavaScript 中，基本类型是没有属性和方法的，但是为了便于操作基本类型的值，在调用基本类型的属性或方法时 JavaScript 会在后台隐式地将基本类型的值转换为对象，如：

```js
const a = "abc";
a.length; // 3
a.toUpperCase(); // "ABC"
```

在访问`'abc'.length`时，JavaScript 将'abc'在后台转换成`String('abc')`，然后再访问其length属性。 JavaScript也可以使用Object函数显式地将基本类型转换为包装类型：

```js
var a = 'abc'
Object(a) // String {"abc"}
```

也可以使用valueOf方法将包装类型倒转成基本类型：

```js
var a = 'abc'
var b = Object(a)
var c = b.valueOf() // 'abc'
```

```js
var a = new Boolean( false );
if (!a) {
	console.log( "Oops" ); // never runs
}
```

## 类型判断

### 数据类型检测方式

#### a. typeof

Array , object , null typeof -> object

缺点：引用类型无法判断

```js
console.log(typeof 2);               // number
console.log(typeof true);            // boolean
console.log(typeof 'str');           // string
console.log(typeof function(){});    // function
console.log(typeof undefined);       // undefined

console.log(typeof {});              // object
console.log(typeof []);              // object    
console.log(typeof null);            // object
```

#### b. instanceof

instanceof可以正确判断对象的类型，其内部运行机制是判断在其原型链中能否找到该类型的原型。

缺点：instanceof只能正确判断引用数据类型，而不能判断基本数据类型。

instanceof 运算符可以用来测试一个对象在其原型链中是否存在一个构造函数的 prototype 属性。

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 

console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

#### c. constructor

constructor有两个作用，一是判断数据的类型，二是对象实例通过 constrcutor 对象访问它的构造函数。需要注意，如果创建一个对象来改变它的原型，constructor就不能用来判断数据类型了

```js
console.log((2).constructor === Number); // true
console.log((true).constructor === Boolean); // true
console.log(('str').constructor === String); // true
console.log(([]).constructor === Array); // true
console.log((function() {}).constructor === Function); // true
console.log(({}).constructor === Object); // true
```

```js
function Fn(){};

Fn.prototype = new Array();

var f = new Fn();

console.log(f.constructor === Fn);    // false
console.log(f.constructor === Array); // true
```

#### d. Object.prototype.toString.call()

Object.prototype.toString.call() 使用 Object 对象的原型方法 toString 来判断数据类型

```js
var a = Object.prototype.toString;
 
console.log(a.call(2));
console.log(a.call(true));
console.log(a.call('str'));
console.log(a.call([]));
console.log(a.call(function(){}));
console.log(a.call({}));
console.log(a.call(undefined));
console.log(a.call(null));
```

同样是检测对象obj调用toString方法，`obj.toString()`的结 果和`Object.prototype. toString.cal(obj)`的结果不一样，这是为什么?

这是因为toString是Object的原型方法，而Array、 Function等类型作为Object的实例,都重写了toString方法。不同的对象类型调用toString方法时，根据原型链的知识，调用的是对应的重写之后的toString方法(function类型返回内容为函数体的字符串，Array类型返回元素组成的字符串)，而不会去调用Object上原型toString方法(返回对象的具体类型)， 所以采用`obj.toString()`不能得到其对象类型，只能将obj转换为字符串类型;因此，在想要得到对象的具体类型时，应该调用Object原型上的toString方法。

#### e. 自创

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

## 类型转换

常见的类型转换有：

- 强制转换（显示转换）
- 自动转换（隐式转换）

1. Number()

![number()](http://tva1.sinaimg.cn/large/005NUwygly1h7ndy9bjjqj30kx082myl.jpg)

2. String()

![string()](http://tva1.sinaimg.cn/large/005NUwygly1h7ndynt2dgj30kn072gmy.jpg)

3. Boolean()

![boolean()](https://static.vue-js.com/53bdad10-6692-11eb-ab90-d9ae814b240d.png)

- `+` **操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==`  **操作符**

# C. 熟悉常用类型api

## a. Date

### Date() constructor

Date() 构造函数可以创建 Date 实例或返回表示当前时间的字符串。

**Note:** `Date()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new), but with different effects.

```js
new Date();
Date();
```

Calling `new Date()` (the `Date()` constructor) returns a [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object. If called with an invalid date string, or if the date to be constructed will have a UNIX timestamp less than `-8,640,000,000,000,000` or greater than `8,640,000,000,000,000` milliseconds, it returns a `Date` object whose [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString) method returns the literal string `Invalid Date`.

Calling the `Date()` function (without the `new` keyword) returns a string representation of the current date and time, exactly as `new Date().toString()` does. Any arguments given in a `Date()` function call (without the `new` keyword) are ignored; regardless of whether it's called with an invalid date string — or even called with any arbitrary object or other primitive as an argument — it always returns a string representation of the current date and time.

### Methods

See MDN.

## b. array

### 数组常用的方法

会影响原数组 ⭕️，不会影响原数组 ❌。

1. 操作方法

   - 增

     - `push()`: 方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度 ⭕️
     - `unshift()`: 在数组开头添加任意多个值，然后返回新的数组长度 ⭕️
     - `splice()`: 传入三个参数，分别是开始位置、0（要删除的元素数量）、插入的元素，返回空数组 ⭕️
     - `concat()`: 首先会创建一个当前数组的副本，然后再把它的参数添加到副本末尾，最后返回这个新构建的数组 ❌

   - 删

     - `pop()`: 用于删除数组的最后一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `shift()`: 用于删除数组的第一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `splice()`: 传入两个参数，分别是开始位置，删除元素的数量，返回包含删除元素的数组 ⭕️
     - `slice()`: 不影响原数组：创建一个包含原有数组中一个或多个元素的新数组 ❌

   - 改

     `splice()`: 传入三个参数，分别是开始位置，要删除元素的数量，要插入的任意多个元素，返回删除元素的数组，对原数组产生影响 ⭕️

   - 查

     - `indexOf()`: 返回要查找的元素在数组中的位置，如果没找到则返回 -1❌
     - `includes()`: 返回要查找的元素在数组中的位置，找到返回`true`，否则`false` ❌
     - `find()`: 返回第一个匹配的元素 ❌
     - `findIndex()`: ❌

2. 转换方法：`join()`: 接收一个参数，即字符串分隔符，返回包含所有项的字符串 ❌

3. 排序方法：

   - `reverse()`: 顾名思义，将数组元素方向反转 ⭕️
   - `sort()`: 接受一个比较函数，用于判断哪个值应该排在前面 ⭕️

4. 迭代/遍历方法

- `some()`: 对数组每一项都运行传入的函数，如果有一项函数返回 true ，则这个方法返回 true ❌

- `every()`: 对数组每一项都运行传入的函数，如果对每一项函数都返回 true ，则这个方法返回 true ❌

- `forEach()`: 对数组每一项都运行传入的函数，没有返回值 ❌

- `filter()`: 对数组每一项都运行传入的函数，函数返回 `true` 的项会组成数组之后返回 ❌

- `map()`: 对数组每一项都运行传入的函数，返回由每次函数调用的结果构成的数组 ❌

- `reduce()`: 对数组中的每个元素按序执行一个由您提供的 reducer 函数，每一次运行 reducer 会将先前元素的计算结果作为参数传入，最后将其结果汇总为单个返回值。❌

### 数组遍历方法

`forEach`、`map`共同点：

1. 只能遍历数组并参数都一样
2. 不改变原函数（引用类型除外）
3. 无法中断循环；return 只是结束本地循环，进入下一次循环
4. break 或 continue 都将会报错

| **方法**                      | **是否改变原数组** | **特点**                                                     |
| ----------------------------- | ------------------ | ------------------------------------------------------------ |
| `forEach()`                   | 否                 | 数组方法，不改变原数组，没有返回值。                         |
| `map()`                       | 否                 | 数组方法，不改变原数组，有返回值，可链式调用。               |
| `filter()`                    | 否                 | 数组方法，过滤数组，返回包含符合条件的元素的数组，可链式调用 |
| `for...of...`                 | 否                 | for...of遍历具有Iterator迭代器的对象的属性，返回的是数组的元素、对象的属性值，不能遍历普通的obj对象，将异步循环变成同步循环 |
| `every()` 和 `some()`         | 否                 | 数组方法，some()只要有一个是true，便返回true；而every()只要有一个是false，便返回false. |
| `find()` 和 `findIndex()`     | 否                 | 数组方法，find()返回的是第一个符合条件的值；findIndex()返回的是第一个返回条件的值的索引值 |
| `reduce()` 和 `reduceRight()` | 否                 | 数组方法，reduce()对数组正序操作；reduceRight()对数组逆序操作 |

### forEach() / map() / for...of 跳出循环

在 forEach 中，不能使用 continue 和 break ，都会报错。可以使用 return 或 return false 跳出循环，但是效果与 for 中 continue 一样。 这种方法无法一次结束所有循环。

如何在forEach/map中跳出循环的总结：

1. 使用抛出异常来中断 forEach/map
2. 使用别的循环代替
   - 使用传统 for 循环
   - 使用数组 every/some 循环

forEach/map 中使用循环的注意事项:

1. 碰到需要终止的循环，避免使用 forEach 可以使用 for/for in循环
2. es6针对数组可以使用 every/some/find等方式
3. forEach/map 循环只能通 return 中断当次循环无法跳出循环
4. forEach/map 循环中使用 continue/break 报错
5. 如果非要使用 forEach/map 中断循环使用抛出异常

注意

- for/for...of： break跳出本次循环；continue结束本次循环执行下一次循环，没有return。
- for...in：会忽略break || continue。没有return。

```js
try {
  [1, 2, 3, 4, 5, 6].forEach((val, index) => {
    console.log(val);
    if (val === 3) {
      console.log("满足条件后的操作");
      throw new Error();
    }
    console.log("满足条件后不再执行", val);
  });
} catch (e) {
  console.log("可以不处理");
}
console.log("继续执行");

```

- `forEach()`

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.forEach((x) => {
  if (x === 4) {
    return;
  }
  newArr.push(x * 2);
});

```

在 forEach 中，不能使用 continue 和 break ，可以使用 return 或 return false 跳出循环，效果与 for 中 continue 一样。 注意该方法无法一次结束所有循环。

使用 `forEach()` 方法遍历了数组中的每一项，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `return` 语句，==跳出回调函数，并继续执行 `forEach()` 方法的下一次迭代。==(只是跳出，没有结束)

是因为 `forEach()` 方法有一个特定的用途，即对数组中的每一项执行一个操作。它不是一个循环，==所以不能使用 `break` 或 `continue` 语句来控制循环的执行。== ==Uncaught SyntaxError: Illegal break statement==

如果你想要在 `forEach()` 方法中使用 `break` 语句，那么你可以使用 `some()` 方法代替。`some()` 方法也会迭代数组的每一项，并对每一项执行一个回调函数。但是，它会在回调函数返回 `true` 的时候终止循环，并返回 `true`。

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.some(x => {
  if (x === 4) {
    return true;
  }
  newArr.push(x * 2);
});
```

- `map()`

在 `map()` 方法的回调函数中使用 `break` 语句是不合法的。这是因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。它不是一个循环，所以不能使用 `break` 或 `continue` 语句来控制循环的执行。

如果你想要在 `map()` 方法中使用 `break` 语句，那么你可以使用一个普通的循环代替。

```js
const arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
  const newArr = arr.map((x) => {
    if (x === 4) {
      break; // Uncaught SyntaxError: Illegal break statement
      // continue // Uncaught SyntaxError: Illegal continue statement: no surrounding iteration statement
    }
    return x * 2;
  });
}

```

在这个例子中，我们在一个循环中调用了 `map()` 方法，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `break` 语句，终止循环。

但是，这种方法并不是很好，因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。如果你想要终止循环，那么更好的方法是使用 `for` 循环或者 `forEach()` 方法，而不是 `map()` 方法。

- for...of...

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

for (let i = 0; i < arr.length; i++) {
  if (arr[i] === 4) {
    break;
  }
  newArr.push(arr[i] * 2);
}
```

## c. RegExp

