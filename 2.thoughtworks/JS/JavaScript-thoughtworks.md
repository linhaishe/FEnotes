# chapter 1. 如何引入JavaScript

## 学习目标

- 能够通过内部引用和外部引用两种方式在页面中引入JavaScript代码

## 学习内容

HTML控制页面的内容，CSS控制页面的样式，JavaScript主要控制页面的行为。HTML文档中的一个个标签表达的就是页面中的内容；若想要在HTML文档中加入样式，可以在某一个标签中加入`style`属性同时写上CSS样式即可，如`<p style="font-size:16px"><p/>`，或者将不同选择器的样式写在HTML文档`head`中的`<style>//some css attributes</style>`标签下，也可以在HTML文档中的`head`下加入`link`标签外链CSS文件，如：`<link rel="stylesheet" type="text/css" href="//path to css file">` 。那么我们如何在HTML文档中引入JavaScript呢？

### 在HTML文档中引入JavaScript的两种方式

**1. 内部引用**

- 通过HTML文档内的`script`标签加载JavaScript代码。示例如下：

```html
    <script type="text/javascript">
      document.write("Hello World!");
    </script>
```

通过此方式就可以在当前页面中引入`script`标签中的JavaScript代码。

**2. 外部引用**

- 也是使用HTML文档的`script`标签，但是要使用`script`标签的`src`属性，指向外部JavaScript文件的路径。示例如下：

```html
    <script src="./main.js" />
```

由于HTML文档是由上向下对页面元素进行解析的，所以在一个HTML文档中，所有的`<script>`元素都会按照它们在页面中出现的顺序依次被解析，默认情况下，只有在解析完前面的`<script>`元素中的代码之后，才会开始解析后面的`<script>`元素中的代码，所以为防止网页加载缓慢，也可以把非关键的JavaScript放到网页最后，即主要内容后面，`</body>`元素的前面。示例如下：

```html
    // other code ...    
        <script type="text/javascript" src="./main.js"></script>
      </body>
    </html>
```

- 使用内部引用的方法在HTML中嵌入JavaScript代码虽然没有问题，但一般认为最好的做法还是尽可能使用外部文件来包含JavaScript代码。不过，并不存在必须使用外部文件的硬性规定，但支持使用外部文件的人多会强调如下优点：
  1. 可维护性：遍及不同HTML页面的JavaScript会造成维护问题。但把所有JavaScript文件都放在一个文件夹中，维护起来就轻松多了。而且开发人员因此也能够在不触及HTML标签的情况下，集中精力编辑JavaScript代码。
  2. 可缓存：浏览器能够根据具体的设置缓存链接的所有外部JavaScript文件。也就是说，如果有两个页面都使用同一个文件，那么这个文件只需下载一次。因此，最终结果就是能够加快页面加载的速度。
  3. 适应未来：统一定义JavaScript代码，方便查看，同时使代码更安全，可以压缩，也可以加密某个JavaScript文件。

# chapter 2. 变量

## 学习目标

- 理解程序中变量的概念
- 掌握JavaScript中是定义和初始化变量的方法

## 学习内容

- 简单来说，变量就是存储信息的容器。变量就相当与一个”盒子“，用来存储信息，比如：“Bob”，“true”，35等。同时，为了能够区分不同的盒子里存储的是什么信息，需要为每一个”盒子“起一个名字，称为“变量名”。当然，在“盒子”中存储的信息都有不同的数据类型，比如，若是存储了姓名“Bob”，那它就是字符串类型，若是存储了年龄`35`，那它就是数字类型，不同的语言会有不同的数据类型，JavaScript也有自己的数据类型，我们将会在下一节中讲述。变量在使用前通常有两个步骤：声明和初始化。声明就相当于拿了一个"盒子"说这个"盒子"就用来存储姓名了，即指定变量名；初始化相当于将信息放在这个"盒子"中存储，比如将“Bob”放在"盒子"中存储。

**JavaScript 变量**

- 在JavaScript中，变量是松散类型的，所谓松散类型就是可以用变量来保存任何类型的数据。换句哈说，每个变量仅仅是一个用户保存值的占位符而已。在JavaScript中定义变量使用

  ```js
  var
  ```

  来声明一个变量，后面跟一个变量名，变量名必须是合法的标识符

  1. 变量必须以字母开头
  2. 变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
  3. 变量名称对大小写敏感（y 和 Y 是不同的变量）

```js
  var message = 'Hello World';  // Right!
  var 2age = 30; // Wrong! 变量名不能以数字开头
```

**JavaScript 数据类型**

- 在上一面提到，JavaScript中的变量是松散类型的，但是松散类型不是说JavaScript中没有数据类型，而意思是：我们在用"盒子"来存储信息时，不必规定这个”盒子“这能存储数字类型的信息，而是数字，字符串，日期等什么类型的信息都可以存储，但是数据本身是由数据类型的。

```js
var pi=3.14;
var name="Bill Gates";
var answer='Yes I am!';
```

**声明（创建） JavaScript 变量**

- 我们也可以像下面这样来声明一个变量：

```js
  var information;
```

- 这行代码定义了一个名为`information`的变量，该变量可以用来存储任何值（像这样未经过初始化的变量，会被保存一个特殊的值——`undefined`）。
- 在JavaScript中当一个变量已经被声明和初始化之后，还可以对该变量的值进行修改，如下：

```js
  var name = 'Bob'; 
  name = 'Mike';
```

- 可以看到在上述代码中的第二行将姓名改为`’Mike‘`。之前我们提到JavaScript是松散类型的，我们是否可以向下面这样修改变量呢？

```js
  var name = 'Bob';
  name = 10; // 有效！但不推荐
```

- 在这个例子中，变量`name`一开始保存了一个字符串的值`’Bob‘`，然后该值又被一个数字值`10`取代。虽然这种方式在JavaScript中完全有效，但是我们不建议修改变量时修改所保存值的类型。
- 有时我们可能需要同时定义多个变量，比如要一起定义姓名，年龄，学号，我们可以用下面的方法来定义变量：

```js
  var name = 'Bob'; 
  var age = 16; 
  var stuNo = 0012323; 
  // 也可以这样定义 
  var name = 'Bob', age = 16, stuNo = 0012323;
```

- 第一种方法我们分别定义了三个变量，通过对比上面两种方法可以发现第二种方法将分号改为逗号，只有一个`var`同时定义了三个变量。同样，由于JavaScript是松散类型的，因而使用不同类型初始化变量的操作可以放在一条语句中来完成。虽然代码里的换行和变量缩进不是必须的，但这样做可以提高代码的可读性。

- ***Value 值为 undefined\***

在计算机程序中，经常会声明无值的变量。未使用值来声明的变量，其值实际上是 undefined。

```js
// 在执行过以下语句后，变量 name 的值将是 undefined：
var name;
```

- **重新声明 JavaScript 变量**

如果重新声明 JavaScript 变量，该变量的值不会丢失：

```js
//在以下两条语句执行后，变量 name 的值依然是 "Jack"：
var name="Jack";
var name;
```

## 资料推荐 (扩展学习)

- [JS 变量 - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)

# chapter 3. 数据类型

## 学习目标

- 了解JavaScript中的七种数据类型

## 学习内容

- 在上一节中我们提到每一种编程语言都有不同的数据类型，也就是我们的“盒子”里面存储的是字符串、还是数字等等。 
- JavaScript 是一种**弱类型**或者说**动态**语言。这意味着不用提前声明变量的类型，在程序运行过程中，类型会被自动确定。这也意味着可以使用同一个变量保存不同类型的数据：

```js
  var foo = 42; // foo is a Number now 
  var foo = "bar"; // foo is a String now 
  var foo = true; // foo is a Boolean now
```

在 JavaScript 规范中，共定义了七种数据类型，分为 “基本类型” 和 “引用类型” 两大类，如下所示：

- 基本类型：String、Number、Boolean、Symbol、Undefined、Null
- 引用类型：Object

| Data Types  | Description                                        | Example                           |
| ----------- | -------------------------------------------------- | --------------------------------- |
| `String`    | represents textual data                            | `'hello'`, `"hello world!"` etc   |
| `Number`    | an integer or a floating-point number              | `3`, `3.234`, `3e-2` etc.         |
| `BigInt`    | an integer with arbitrary precision                | `900719925124740999n` , `1n` etc. |
| `Boolean`   | Any of two values: true or false                   | `true` and `false`                |
| `undefined` | a data type whose variable is not initialized      | `let a;`                          |
| `null`      | denotes a `null` value                             | `let a = null;`                   |
| `Symbol`    | data type whose instances are unique and immutable | `let value = Symbol('hello');`    |
| `Object`    | key-value pairs of collection of data              | `let student = { };`              |

#### 1.字符串类型（String）

- JavaScript的字符串类型用于表示文本数据。在字符串中的每个元素占据了字符串的位置。第一个元素的索引为0，下一个是索引1，依此类推。字符串的长度是它的元素的数量。
- 在JavaScript中的字符串需要使用单引号`'**'`或双引号`"**"`括起来，表示该值是一个字符串。
- JavaScript 字符串是不可更改的。这意味着字符串一旦被创建，就不能被修改。但是，可以基于对原始字符串的操作来创建新的字符串。例如：
  1. 获取一个字符串的子串可通过选择个别字母或者使用`String.substr()`。
  2. 两个字符串的连接使用连接操作符 (`+`) 或者`String.concat()`。
- 符号类型（Symbol）：符号(Symbols)是ES6新定义的。符号类型是唯一的并且是不可修改的。

#### 2.Number

Number类型包含整数和浮点数（浮点数数值必须包含一个小数点，且小数点后面至少有一位数字）两种值

#### 3.布尔类型（Boolean）

布尔表示一个逻辑实体，意为真、假，可以有两个值：`true`和`false`。

#### 4.Symbol（了解）

Symbol 是 ES6 新增的一种原始数据类型，它的字面意思是：符号、标记。代表独一无二的值 。

#### 5.Undefined 和 Null

- Undefined 这个值表示变量不含有值。
- Null 类型只有一个值：`null`，表示空值，表示没有被呈现
- 可以通过将变量的值设置为 null 来清空变量。

```js
// 值：undefined
var car="Volvo"; //值："Volvo"
var car=null; //值：null
```

#### 6.对象（Object）

- javascript 中的对象(物体)，和其它编程语言中的对象一样，可以比照现实生活中的对象(物体)来理解它。 javascript 中对象(物体)的概念可以比照着现实生活中实实在在的物体来理解。
  - 在javascript中，一个对象可以是一个单独的拥有属性和类型的实体。我们拿它和一个杯子做下类比。一个杯子是一个对象(物体)，拥有属性。杯子有颜色，图案，重量，由什么材质构成等等。同样，javascript对象也有属性来定义它的特征。
  - 对象可以通过`new`操作符后跟要创建的对象类型的名称来创建。而创建Object类型的示例并为其添加属性和（或）方法，就可以创建自定义对象，如下所示：

```js
      var o = new Object();	
```

- 我们也可以通过下面的方式直接创建一个对象：

```js
      var person = { name: 'Bob', age: 20, gender: 'male' };
```

- 上述对象就定义了一个名为’Bob‘，20岁，的男生。

#### 7.typeof操作符

- 由于JavaScript是松散类型的，因此需要有一种手段来检测给定变量的数据类型——`typeof`就是负责提供这方面信息的操作符。对一个值使用`typeof`操作符可能返回下列某个字符串：

```js
    'undefined' —— 未定义 
    'boolean' —— 布尔值 
    'string' —— 字符串 
    'number' —— 数字值 
    'object' —— 对象或null 
    function —— 函数 
```

- 下面展示一下使用`typeof`的示例：

```js
    var message = 'some string'; 
    alert(typeof message); // "string" 
    alert(typeof(message)); // "string" 
    alert(typeof 95); // number
```

- 在实际编程的过程中，可以用`typeof`判断任何一个变量的数据类型。

## 资料推荐 (扩展学习)

- [JavaScript 数据类型](http://www.w3school.com.cn/js/js_datatypes.asp)

# chapter 4. 作用域

## 学习目标

- 理解什么是作用域
- 理解为什么需要有作用域
- 掌握JavaScript中的作用域原则

## 学习内容

- 作用域被用来描述在某个代码块可见的所有实体（或有效的所有标识符），更精准一点，叫做上下文。
- 那么为什么需要有作用域呢？
  - 最小访问原则
  - 通过限制变量的可见性，不允许代码中所有的东西在任意地方都可用的好处是什么？其中一个优势，是作用域为你的代码提供了一个安全层级。计算机安全中，有个常规的原则是：用户只能访问他们当前需要的东西。
- JavaScript的作用域链
  - 首先观看这段代码：

```html
    <script type="text/javascript">
        var rain = 1;
        function rainman(){
            var man = 2;
            function inner(){
                var innerVar = 4;
                alert(rain);
            }
            inner();    //调用inner函数
        }
        rainman();    //调用rainman函数
    </script>
```

- 观察alert(rain);这句代码。JavaScript首先在inner函数中查找是否定义了变量rain，如果定义了则使用inner函数中的rain变量；如果inner函数中没有定义rain变量，JavaScript则会继续在rainman函数中查找是否定义了rain变量，在这段代码中rainman函数体内没有定义rain变量，则JavaScript引擎会继续向上（全局对象）查找是否定义了rain；在全局对象中我们定义了rain = 1，因此最终结果会弹出'1'。

- 作用域链：JavaScript需要查询一个变量x时，首先会查找作用域链的第一个对象，如果以第一个对象没有定义x变量，JavaScript会继续查找有没有定义x变量，如果第二个对象没有定义则会继续查找，以此类推。
  - 上面的代码涉及到了三个作用域链对象，依次是：inner、rainman、window。

- 函数体内部，局部变量的优先级比同名的全局变量高
  - 首先看如下代码示例：

```html
    <script type="text/javascript">
        var rain = 1;    //定义全局变量 rain
        function check(){
            var rain = 100;    //定义局部变量rain
            alert( rain );       //这里会弹出 100
        }
        check();
        alert( rain );    //这里会弹出1
    </script>
```

- 没有块级作用域，只有函数作用域
  - 这一点也是JavaScript相比其它语言较灵活的部分。
  - 仔细观察下面的代码，你会发现变量i、j、k作用域是相同的，他们在整个rain函数体内都是全局的。

```html
    <script type="text/javascript">
        function rainman(){
            // rainman函数体内存在三个局部变量 i j k
            var i = 0;
            if ( 1 ) {
                var j = 0;
                for(var k = 0; k < 3; k++) {
                    alert( k );    //分别弹出 0 1 2
                }
                alert( k );        //弹出3
            }
            alert( j );            //弹出0
        }
    </script>
```

- 函数中声明的变量在整个函数中都有定义
  - 观察一下代码示例

```html
    <script type="text/javascript">
        function rain(){
            var x = 1;
            function man(){
                x = 100;
            }
            man();        //调用man
            alert( x );    //这里会弹出 100
        }
        rain();    //调用rain
    </script>
```

- 上面的代码说明了，变量x在整个rain函数体内都可以使用，并可以重新赋值。由于这条规则，会产生“匪夷所思”的结果，观察下面的代码。

```html
    <script type="text/javascript">
        var x = 1;
        function rain(){
            alert( x );        //弹出 'undefined'，而不是1
            var x = 'rain-man';
            alert( x );        //弹出 'rain-man'
        }
        rain();
    </script>	
```

- 是由于在函数rain内局部变量x在整个函数体内都有定义（ var x= 'rain-man'，进行了声明），所以在整个rain函数体内隐藏了同名的全局变量x。这里之所以会弹出'undefined'是因为，第一个执行alert(x)时，局部变量x仍未被初始化。所以上面的rain函数等同于下面的函数：

```js
    function rain(){
        var x;
        alert( x );
        x = 'rain-man';
        alert( x );
    }
```

- 未使用var、let、const关键字声明的变量都是全局变量

```html
    <script type="text/javascript">
        function rain(){
            x = 100;    //声明了全局变量x并进行赋值
        }
        rain();
        alert( x );    //会弹出100
    </script>
```

- 这也是JavaScript新手常见的错误，无意之中留下的许多全局变量。
- 全局变量都是window对象的属性

```html
    <script type="text/javascript">
        var x = 100 ;
        alert( window.x );//弹出100
        alert(x);
    </script>
```

- 等同于下面的代码

```html
    <script type="text/javascript">
        window.x = 100;
        alert( window.x );
        alert(x)
    </script>	
```

## 推荐资料 (扩展学习)

- [理解 JavaScript 作用域](http://web.jobbole.com/91134/)

# chapter 5. 字符串介绍(String)

## 学习目标

- 掌握字符串中常用的方法

## 学习内容

- 在JavaScript中，所有的文本数据均被存储为字符串。JavaScript中没有存储单个字符的数据类型，尽管只存储一个字符，也是长度为1的字符串。

#### 字符串的写法

- 字符串可以由双引号（`"`）或者单引号（`'`）表示，因此下面两种字符串的写法都是有效的：

```js
  var firstName = 'Hello';
  var lastName = "World";	
```

- 在别的编程语言中，单引号和双引号会影响对字符串的解释方式不同，但是在JavaScript中这两种语法没有什么区别。用双引号表示的字符串和用单引号表示的字符串完全相同。不过，以双引号开头的字符串也必须也双引号结尾，而以单引号开头的字符串必须以单引号结尾。例如：下面这种字符串表示法将会导致语法错误：

```js
  var firstName = 'Hello World"; // 语法错误（左右引号必须匹配）
```

- 在字符串中，`+`号表示连接，意为将右边的字符串连接在左边的字符串后面，例如：

```js
  var text = 'hello ';
  text = text + 'world'; // 也可以用+=表示：text+='world';
  console.log(text); // hello world
```

#### 字符字面量

- 在JavaScript中，String数据类型中包含一些特殊的字符字面量，也叫做转义字符，用于表示非打印字符，或者具有其他用途的字符。常用的字符字面量如下所示：

```html
   \n: 换行
   \t: 制表符
   \b: 退格
   \r: 回车
   \\: 斜杠（\）
   \': 单引号（'）
   \": 双引号（"） 
```

- 这些字面量可以出现在字符串中的任意位置，而且也将被作为一个字符来解析。如下面例子所示：

```js
  var text = 'Hello \n World';  // 加入了一个换行符(\n)
```

- 将会打印出如下字符串：

```html
  "Hello 
   World"
```

- 任何字符串的长度都可以通过访问其`length`属性取得，例如：

```js
  var text = 'Hello ';
  console.log(text.length); // 6 （注意Hello后面还有一个空格）
```

#### 字符串的特点

- 在JavaScript中，字符串是不可变的，也就是说，字符串一旦创建，它们的值就不能改变。要改变某个变量保存的字符串，首先要销毁原来的字符串，然后再用另一个包含新值的字符串填充该变量，例如：

```js
    var text = 'tws ';
    text = text + 'academy';
```

- 在这个例子中，变量`text`开始时包含字符串`'tws '`，而在第二行代码把`text`的值重新定义为`'tws '`与`'academy'`的组合，即：`'tws academy'`。在这个过程中，首先会创建一个能容纳11个字符的新字符串，然后在这个字符串中填充`'tws'`和`'academy'`，最后一步是销毁原来的字符串`'tws'`和字符串`'academy'`，因为这两个字符串已经没用了。

#### 字符串常用方法

###### 1.从字符串中取出单个字符

- 有两种方法：第一种方法是使用`charAt()`方法，示例：`'cat'.charAt(1); // 'a'`；另一种方法是把字符串当作一个类似数组的对象，其中的每个字符对应一个数值索引，示例：`'cat'[1]; // 'a'`。> 这里虽然使用括号访问字符串，但是不可以对其进行删除或添加，因为字符串是不可改变的。

###### 2.`concat()`方法 - 字符串连接

- `concat()`方法将一个或多个字符串与原字符串连接合并，形成一个新的字符串并返回。`concat()`方法并不影响原字符串。示例：

```js
      var hello = "Hello, ";
      console.log(hello.concat("tws", " have a nice day.")); // Hello, tws have a nice day.
      console.log(hello); // Hello, 
```

- 我们会发现，其实`concat()`方法的作用和`+`，`+=`的作用是一样的。但使用`+`，`+=`会获得更好的性能体验，因此，建议使用赋值操作符（`+`, `+=`）代替`concat()`方法。

###### 3. includes()方法 - 字符串搜索

- includes()方法用于判断一个字符串是否包含在另一个字符串中，根据情况返回true或false，且该方法是区分大小写的。示例：

```js
      'Blue Whale'.includes('blue'); // false (大小写不同)
      'Blue Whale'.includes('Blue'); // true
```

###### 4.substr()方法 - 提取子字符串

- substr()方法返回一个字符串中从指定位置开始到指定字符数的字符。该方法在调用的时候需要传入两个参数分别为：**开始提取字符的位置**和**提取的字符数长度**（可选）。示例：

```js
      var str = 'abcdefghij';
      str.substr(0,3); // 'abc'
      str.substr(3,3); // 'def'
      str.substr(3); // 'defghij'
```

###### 5.substring()方法 - 提取子字符串

- substring()方法返回一个字符串在开始索引位置到结束索引位置之间的一个子集, 或从开始索引直到字符串的末尾的一个子集。该方法也接受两个参数，第一个参数是**开始提取字符的位置**，但与substr()方法不同的是，substring()方法的第二个参数是**结束提取字符的位置**（可选）。示例：

```js
      var str = 'abcdefghij';
      str.substring(0,3); // 'abc'
      str.substring(3,3); // ''  (因为从3到3，中间没有字符)
      str.substring(3); // 'defghij'
      str.substring(2,3); // 'c'
```

## 推荐资料 (扩展学习)

- [JS 字符串](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String)
- [JavaScript String Methods Reference](https://www.impressivewebs.com/javascript-string-methods-reference/)

#  chapter 6. 数组介绍(Array)

## 学习目标

- 了解数组的常用方法

## 学习内容

- 在JavaScript中，除了对象(Object)外，数组(Array)类型应该是最常用的数据类型了。数组是数据的有序列表，在JavaScript中，数组中的每一项可以保存任何类型的数据，也就是说可以用数组的第一项保存字符串，第二项保存数值，第三项保存对象等，同时，JavaScript中数组的长度是可以动态调整的，即可以随着数据的添加自动增长以容纳新增数据。

#### 数组创建

- 创建数组的基本方式有两种。第一种是使用JavaScript中Array构造函数，示例如下：

```js
  var fruits = new Array();
```

- 如果预先知道数组要保存的项目数量，也可以给构造函数传递该参数，例如，下面的代码将创建一个长度为10的数组：

```js
  var fruits = new Array(10);
```

- 创建数组的第二种方式是使用数组字面量表示法。数组字面量也就是说我们直接把数组中的每一个数据项都列出来，包含在一对中括号之间，不同的数据项以逗号隔开，如下所示：

```js
  var fruits = ['apple', 'pear', 'peach']; // 创建了一个包含三个字符串的数组
  var names = []; // 创建了一个空数组
  var values = [1, 2, ,]; // 不要这样做!这样会创建一个包含2项或4项的数组
```

#### 数组读取

- 在我们要对数组进行读取操作时，我们可以使用中括号并提供相应的基于0的数字索引，如下所示：

```js
  var fruits = ['apple', 'pear', 'peach'];
  console.log(fruits[0]); // 显示第一项 - 'apple'
  fruits[1] = 'grape'; // 修改第二项
  console.log(fruits[1]); // 显示第二项 - 'grape'
  fruits[3] = 'banana'; // 新增第四项
  console.log(fruits[3]); // 显示第四项 - 'banana'
```

- 方括号中的索引表示要访问的值。如果索引小于数组中的项数，就返回对应项的值，就像上例中`fruits[0]`会返回'apple'一样。设置数组中某一项的值也是使用的相同的语法，但会替换指定位置的值。如果设置某个值的索引超过了该数组现有的长度，如上述例子中的`fruits[3]`所示，数组就会自动增加到该索引值加1的长度（就上例而言，索引是3，因此该数组的长度就是4）。

#### 数组的length属性

- 数组的项数保存在该数组的length属性中，这个属性始终会返回0或者更大的值，如下例所示：

```js
  var fruits = ['apple', 'pear', 'peach'];
  console.log(fruits.length); // 3
  var colors = [];
  console.log(colors.length); // 0
```

- 数组中的length属性很有特点，它**不是只读**的。因此，我们还可以通过设置这个属性，从数组的末尾移除数据项，请看下面的例子：

```js
  var fruits = ['apple', 'pear', 'peach'];
  fruits.length = 2;
  console.log(fruits[2]); // undefined - 相当于删除了数组中的第三项
```

#### JavaScript中常用方法：

###### 1.push()方法

- 向数组的末尾添加新的元素。示例如下：

  ```js
      var fruits = ['apple', 'pear', 'peach'];
      fruits.push('banana');
      console.log(fruits); // ['apple', 'pear', 'peach', 'banana']
  ```

###### 2.pop()方法

- 从数组的末尾移除一个元素。示例如下：

```js
        var fruits = ['apple', 'pear', 'peach'];
        fruits.pop();
        console.log(fruits); // ['apple', 'pear']
```

###### 3.unshift()方法

- 向数组的前面添加新的元素。示例如下：

```js
        var fruits = ['apple', 'pear', 'peach'];
        fruits.unshift('banana');
        console.log(fruits); // ['banana', 'apple', 'pear', 'peach']
```

###### 4.shift()方法

- 从数组的前面移除一个元素。示例如下：

```js
        var fruits = ['apple', 'pear', 'peach'];
        fruits.shift();
        console.log(fruits); // ['pear', 'peach']
```

以上四个方法是我们在对数组进行添加，删除的基本操作。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/32339584.jpg)

###### 5.indexOf()方法

- 找到某一个数据项在数组中的索引值。示例如下：

```js
        var fruits = ['apple', 'pear', 'peach'];
        console.log(fruits.indexOf('pear')); // 1	
```

###### 6. reverse()方法

- 反转数组项的顺序，改变原数组，示例如下：

```js
var fruits = ['apple', 'pear', 'peach'];
console.log(fruits.reverse()); // ["peach", "pear", "apple"]
```

###### 7. sort()方法

- 默认情况下，即无参数情况，sort()方法按升序排列数组。该方法会调用每个数组项的tostring()方法，然后比较字符串，因此即使数组中每一项都是数值，sort()方法比较的也是字符串。

```js
var fruits = ['apple', 'pear', 'peach'];
console.log(fruits.sort());  // ["apple", "peach", "pear"]
```

###### 8.join()

- 所有元素都转化为"字符串"并连接在一起

```js
var fruits = ['apple', 'pear', 'peach'];
console.log(fruits.join("-")); // apple-pear-peach
```

## 推荐资料

- [JavaScript数组 - MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array)

# chapter 7. 数学运算符

## 学习目标

- 掌握JavaScript中的数学相关的运算符，`+`，`-`，`*`，`/`，`+=`……
- 能够用JavaScript中的数学运算符进行数学运算

## 学习内容

- 通过之前的学习，我们知道变量可以用来存储信息，包括字符串，数字等。本节我们所要学的是如何用JavaScript实现基本的数学运算。
- 先做一道简单的数学题：“我们有15个苹果，20个梨，那么我们一共有多少个水果？”。答案是35个，那么我们如何用程序表示这道题呢？如下：

```js
  var apple = 15; 
  var pear = 20; 
  var fruit = apple + pear; 
  alert(fruit); // 35
```

- 首先声明一个变量存储苹果的数量（`var apple = 15;`），再声明一个变量存储梨的数量（`var pear = 20;`）,最后声明一个变量用来存储水果的数量，并将它初始化为苹果和梨的数量之和（`var fruit = apple + pear;`）,那么`fruit`就存储了我们计算出来的水果的数量，这里的加号（`+`）表示和数学里相同的含义即相加。

#### 1. =：赋值操作符

- 首先先介绍一下赋值操作符，也就是等号`'='`，在JavaScript中一个等号意为赋值，就是将等号右侧的值赋值给等号左侧的值。这里容易困惑的是赋值和判断相等的区别，一个等号代表赋值，若我们想判断`a`是否和`b`相等，则需要用`===`或`==`来判断，关于`===`和`==`的区别，简单来说就是三个等号是严格相等，既包含值的相等也包含数据类型的相等；但两个等号的相等只简单判断值，不判断数据类型；举个例子：

```js
  alert('0' === 0); // false 严格相等判断，’0‘是字符串，而0是数字，故不严格相等。
  alert('0' == 0); // true 非严格相等判断，会将’0‘隐式转换为0，再比较，即 0==0，故返回true。
```

#### 2. +：加法

```js
    var x = 5; 
    var result = x + 5; 
    alert(result); // 10
```

#### 3. -：减法

```js
    var x = 5; 
    var result = x - 5; 
    alert(result); // 0
```

#### 4. *：乘法

```js
    var x = 5; 
    var result = x * 5; 
    alert(result); // 25
```

#### 5. /：除法

```js
    var x = 5; 
    var result = x / 2; 
    alert(result); // 2.5
```

#### 6. %，取模

- 这里取模的意思其实就是求余数，比如：10除以3得3余1，那么10对3求模就是1。示例：

```js
    var x = 5; 
    var result = x % 2; 
    alert(result); // 1
```

#### 8. ++，自加

- 这里自加意为将自己的值加一，比如：3自加之后就是4。示例：

```js
    var x = 5; 
    x++; 
    alert(x); // 6
```

#### 9. +=，加等

```js
    var x = 5; 
    x += 2; // x = x + 2; 
    alert(x); // 7
```

- 加等就是将当前变量的值加上右侧的值，再赋值给当前值。比如上例中，`x += 2;`就是将`x`的值加上`2`在赋值给`x`。

#### 9. --，自减

- 这里自减意为将自己的值减一，比如：4自减之后就是3。示例：

```js
    var x = 5; 
    x--; 
    alert(x); // 4
```

#### 10. -=，减等

```js
    var x = 5; 
    x -= 2; // x = x - 2; 
    alert(x); // 3
```

- 减等就是将当前变量的值减去右侧的值，再赋值给当前值。比如上例中，`x -= 2;`就是将`x`的值减去`2`在赋值给`x`。

#### 11. `>` / `>=`，大于/大于等于

- 在JavaScript中用来做判断，和我们在数学中所理解的大于/大于等于的概念一致，结果返回true或false。示例：

```js
    var x = 5; 
    var y = 10; 
    var z = 10; 
    alert(y > x); // true 
    alert(y >= z); // true
```

#### 12. `<` / `<=`： 小于/小于等于

- 在JavaScript中用来做判断，和我们在数学中所理解的小于/小于等于的概念一致，结果返回true或false。示例：

```js
    var x = 5; 
    var y = 10; 
    var z = 10; 
    alert(y < x); // false 
    alert(z <= x); // false
```

#### 13.优先级

- 我们在数学中进行数学计算的时候，会有不同的优先级规则。比如：先算乘除，再算加减；有括号要先算括号里面的。这些规则在JavaScript中进行数学运算是同样适用。示例：

下表按从最高到最低的优先级列出JavaScript运算符。具有相同优先级的运算符按从左至右的顺序求值。

| 运算符                             | 描述                                         |
| ---------------------------------- | -------------------------------------------- |
| .                                  | 字段访问、数组下标、函数调用以及表达式分组   |
| ++ -- - ~ ! delete new typeof void | 一元运算符、返回数据类型、对象创建、未定义值 |
| * / %                              | 乘法、除法、取模                             |
| + - +                              | 加法、减法、字符串连接                       |
| << >> >>>                          | 移位                                         |
| < <= > >= instanceof               | 小于、小于等于、大于、大于等于、instanceof   |
| == != === !==                      | 等于、不等于、严格相等、非严格相等           |
| &                                  | 按位与                                       |
| ^                                  | 按位异或                                     |
| `|`                                | 按位或                                       |
| &&                                 | 逻辑与                                       |
| `||`                               | 逻辑或                                       |
| ?:                                 | 条件                                         |
| = oP=                              | 赋值、运算赋值                               |
| ,                                  | 多重求值                                     |

## 资料推荐 (扩展学习)

- [JS表达式和操作符 - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)

# chapter 8. 逻辑运算符

## 学习目标

- 掌握`&&`，`||`，`!`逻辑运算符的运算规则

## 学习内容

#### 逻辑与运算符(&&)

- 对两个表达式执行逻辑与运算(相当于英语中 and 的意思)
- 语法: `运算结果 = 表达式1 && 表达式2`
- 运算结果可以是任何变量,这个变量相当于一个容器,将运算结果放在这个容器里面。
- `and` 是 `与` `并且` 的意思,所以**只有**当 `表达式1` 和 `表达式2` 都是正确(也就是都为真 `true` )的时候,返回值才为 `true` ;

**运算结果 = 表达式1 && 表达式2**

| 运算结果 | 表达式1 | 表达式2 |
| -------- | ------- | ------- |
| true     | true    | true    |
| false    | true    | false   |
| false    | false   | true    |
| false    | false   | false   |

#### 逻辑或运算符(||)

- 只要“||”前面为false,不管“||”后面是true还是false，都返回“||”后面的值。
- 只要“||”前面为true,不管“||”后面是true还是false，都返回“||”前面的值。

**运算结果 = 表达式1 || 表达式2**

| 运算结果 | 表达式1 | 表达式2 |
| -------- | ------- | ------- |
| true     | true    | true    |
| true     | true    | false   |
| false    | false   | true    |
| false    | false   | false   |

- 从上面表格也可以看出来,**只要**`表达式1` 为 `true` 时,运算结果就为 `true` (可怜的表达式2,就这样被无情忽略了 - _ - );否则运算结果的值就跟`表达式2`的结果保持一致
- 这种现象跟上面我们提过的逻辑与运算 `&&` 是同一种现象,应该还记得吧,这种现象叫做 `短路运算`

#### 逻辑非运算符(!)

- 对一个表达式执行逻辑求反操作
- 语法: `运算结果 = !表达式`
- 运算结果的含义跟上面两种是一样的哈
- `非`是 `不是` `否定` 的意思,所以结果跟表达式相反就好啦

**运算结果 = !表达式**

| 运算结果 | 表达式 |
| -------- | ------ |
| true     | false  |
| false    | true   |

- 谁是 `true` 谁是 `false`
  - 能够转换为 `false` 的表达式有：`null` , `NaN` , `0` , `空字符串("")` , `undefined`

## 资料推荐 (扩展学习)

- [逻辑运算符-MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Logical_Operators)

# chapter 9. 条件分支语句

## 学习目标

- 掌握 `if-else` 语句的使用
- 掌握 `switch` 语句的使用

## 学习内容

- 网上一直流传这么一个段子：妻子说：“你去菜场买一个西瓜，如果看见西红柿，就买两个。” 过了一会，丈夫买了两个西瓜回来。 妻子问：“你怎么买了两个西瓜？” 程序员丈夫回答：“因为在菜场看见西红柿了！” 吃瓜群众表示一脸问号，但相信学完这一节，你一定会说：“嗯……没毛病！”

#### 理解条件分支语句

- 首先，我们来了解一下条件分支语句是做什么的。

- 条件分支语句就是基于不同的 **条件** 去执行不同的 **动作** 。

- 我们用程序员的思维来翻译一下上面的段子。"如果"后面的是"条件"，"条件"之后跟了相应的"动作"。于是，我们得到下面两组“条件 -> 动作”：

  - 条件成立：看见西红柿 -> 动作1：买两个西瓜
  - 条件不成立：没看见西红柿 -> 动作2：买一个西瓜

- 接着，我们来看一下 JavaScript 中是如何使用条件分支语句的。

  #### `if` 语句

- if 语句的语法格式如下

```
if (condition){
  // 当 condition==true 时执行的语句块
}
```

- 需要注意的是，这里的 condition 的身份是判断语句，只有真（true）、假（false）两种情况，即条件要么成立，要么不成立，只有两面。

```
var seeTomato = 'yes';
if (seeTomato == 'yes'){
  console.log('Buy two watermelons!');
}
//输出结果 Buy two watermelons!
```

- 那么好学的你可能会问，如果条件不成立，代码该怎么执行呢？答案是，跳过 if 语句块，执行 if 语句块后面的语句。

```
var seeTomato = 'no';
if (seeTomato == 'yes'){
  console.log('Buy two watermelons!');
}
console.log('Buy nothing!');
//输出结果 Buy nothing！
```

- 目前我们还无法用 JavaScript 翻译出上面的段子，这就需要用到 if-else 语句了。

  #### `if-else` 语句

  - if-else 语句的语法格式如下：

```js
if (condition){
  // 当 condition==true 时执行的语句块1
} else {
  // 当 condition==false 时执行的语句块2
}
```

- 当条件成立时，执行语句块1；当条件不成立时，执行语句块2.
- 好了，现在我们来翻译一下上面的段子。

```
var seeTomato = 'yes';
if (seeTomato == 'yes'){
  console.log('Buy two watermelons!');
} else {
  console.log('Buy one watermelon!');
}
// 输出结果 Buy two watermelons!
var seeTomato = 'no';
if (seeTomato == 'yes'){
  console.log('Buy two watermelons!');
} else {
  console.log('Buy one watermelon!');
}
// 输出结果 Buy one watermelon!
```

- 所以程序员丈夫是不是买得没毛病？！

- 可能好学的你又会问，上面只能设置一个条件，怎么设置多个条件呢？答案是，把 if-else 语句组合起来。

  #### `else-if`语句

- else-if的语法格式如下：

```
if (condition1){
  // 当 condition1==true 时执行的语句块1
} else if (condition2){
  // 当 condition2==true 时执行的语句块2
} else {
  // 当 condition1==false && condition2==false 时执行的语句块3
}
```

- 刚看到这个可能会一头雾水，我们来转换一下形式

```
if (condition1){
  // 当 condition1==true 时执行的语句块1
} else {
  if (condition2){
    // 当 condition2==true 时执行的语句块2
  } else {
    // 当 condition1==false && condition2==false 时执行的语句块3
  }
}
```

- 这样是不是就好理解了。第二个 if-else 嵌套在了第一个 if-else 中。但是，为了方便，为了美观，为了养成良好的代码书写习惯，我们要采用第一种写法。

```
var date = 3;
if (date == 1){
  console.log('星期一');
} else if (date == 2){
  console.log('星期二');
} else {
  console.log('未知');
}
// 输出结果 未知
```

- 看到这段代码，你可能回想，星期三、星期四……怎么办？那就再嵌套呗！

```
var date = 5;
if (date == 1){
  console.log('星期一');
} else if (date == 2){
  console.log('星期二');
} else if (date == 3){
  console.log('星期三');
} else if (date == 4){
  console.log('星期四');
} else if (date == 5){
  console.log('星期五');
} else if (date == 6){
  console.log('星期六');
} else if (date == 7){
  console.log('星期日');
} else {
  console.log('未知');
}
// 输出结果 星期五
```

- 于是好学的你又会发问了，代码这么长，有没有方便的方法可以简化一下。那么 switch 语句可以帮助到你。

  #### `swich` 语句

- switch 语句的语法格式如下

```
switch(n){ 
    case n1: 
      执行代码块 1
      break; 
    case n2: 
      执行代码块 2 
      break; 
    default: 
      与 case n1 和 case n2 不同时执行的代码块3 
}
```

- 这里的 n 是一个变量，若 n 与 n1 相等，则执行代码块1，若 n 与 n2 相等，则执行代码块2，若都不相等，则执行代码块3。 于是，之前的代码可以这样写：

```
var date = 5;
switch(date){
  case 1:
    console.log("星期一");
    break;
  case 2:
    console.log("星期二");
    break;
  case 3:
    console.log("星期三");
    break;
  case 4:
    console.log("星期四");
    break;
  case 5:
    console.log("星期五");
    break;
  case 6:
    console.log("星期六");
    break;
  case 7:
    console.log("星期日");
    break;
  default:
    console.log("未知");
}
//输出结果 星期五
```

- 最后，这里的 break 语句是做什么用的呢？`break`语句在这里的作用是跳出这个`switch`语句块。如果不使用`break`,成立的`case`后的代码都会接着执行，用了`break`,就可以跳出这个`switch`语句块。

```
var date = 5;
switch(date){
  case 1:
    console.log("星期一");
  case 2:
    console.log("星期二");
  case 3:
    console.log("星期三");
  case 4:
    console.log("星期四");
  case 5:
    console.log("星期五");
  case 6:
    console.log("星期六");
  case 7:
    console.log("星期日");
  default:
    console.log("未知");
}
// 输出结果:
星期五
星期六
星期日
未知
```

- 本节的知识讲解就到这了，最后强调一点，条件分支语句每次只执行多种情况中的一种情况。

# chapter 10. 循环语句（for，while...）

## 学习目标

- 掌握JavaScript中实现循环的几种方法

## 学习内容

- 在前面的内容中我们学习了`if else`和`switch`，分支结构使JavaScript具有了判断的能力，但其实电脑的判断能力和人比起来差远了，电脑更擅长一件事情不停地重复，也就是循环。在程序设计中，循环是反复执行同一个代码块的方式，可以减少源程序重复书写的工作量。在程序设计中，循环结构非常有用，也是最能发挥计算机特长的程序结构 。例如：我们想要对一个数组中的每一项都执行相同的操作，就可以使用循环结构。

- 循环结构的三个要素：**循环变量**、**循环体**和**循环终止条件**。循环变量是在该循环结构中指示当前在哪次循环的一个变量；循环体是在循环结构中被重复执行的程序；循环终止条件通常是一个条件判断语句，用来判断是否终止当前的循环结构，否则将会陷入无限的死循环中。当条件成立的时候，执行循环体的代码，当条件不成立的时候，跳出循环，执行循环结构后面的代码。

#### 在JavaScript中，通常通过以下三种方法实现循环结构：

###### 1.for 循环

- `for`语句的流程图如下所示： ﻿![img](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LEnFv3jMWsHS31RfsLD%2F-LEnFymU6ro7LIcUvFQV%2F-LEnG-cnGv5prhvBdUg2%2Ffor%E5%BE%AA%E7%8E%AF.png?generation=1528794721919357&alt=media)

- 在该循环结构中，当条件成立时，执行语句1，否则跳出循环体。

- for语句的基本语法如下：

  ```
  for (循环变量初始化;循环终止条件;增量){
  循环体;
  }
  ```

- 接下来我们来看一个简单的例子：有十个学员报数，“学员1号、学员2号……”。有了for循环，我们只用很少的代码就可以实现十个学员的报数。

```
for(var i = 1; i<=10; i++){
    console.log('学员' + i + '号。');
}
```

- 输出的结果如下所示：

```
学员1号。
学员2号。
学员3号。
学员4号。
学员5号。
学员6号。
学员7号。
学员8号。
学员9号。
学员10号。
```

- 在这个例子中，循环恰好执行了10次，那么`for(i=1; i<=10; i++)`一句中的10是不是10次的意思呢？下面我们就来看看`for`循环的工作机制。 首先`i=1`叫做初始条件，也就是说从哪里开始，特别的，我们的例子是从`i=1`开始的。出现在第一个分号后面的`i<=10`表示循环终止条件，每次循环都会先判断这个条件是否满足，如果满足则继续循环，否则停止循环，继续执行`for`循环后面的代码。你可能想问了，我们设定了`i=0`，岂不是永远都小于等于10吗？来看第三个部分。最后的`i++`表示让`i`在自身的基础上加`1`，这是每次循环后的动作。也就是说，每次循环结束时，`i`都会比原来大`1`，执行若干次循环之后，`i<=10`的条件就不满足了，这时循环结束。for循环后面的代码将得到执行。

###### 2. While 循环

- `while`循环重复执行一段代码，直到某个条件不再满足。
- `while`语句的流程图如下所示：![img](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LEnFv3jMWsHS31RfsLD%2F-LEnFymU6ro7LIcUvFQV%2F-LEnG-cyo0wqLfn1BI5j%2Fwhite%E5%BE%AA%E7%8E%AF.png?generation=1528794720902751&alt=media)

- `while`语句属于前测试循环语句，也就是说，在循环体内的代码被执行之前，就会对出口的条件求值。因此，循环体内的代码有可能永远不会被执行。以下是`while`语句的语法：

```
while(循环终止条件){
  循环体
}
```

- 和

  ```
  for
  ```

  循环类似，当循环条件成立时，执行花括号

  ```
  {}
  ```

  内的语句，否则跳出循环。下面用

  ```
  while
  ```

  循环实现上面相同的例子：

  ```
  var i = 1; 
  while(i<=10){
   console.log('学员' + i + '号。');
   i = i + 1;
  }
  ```

- 这两个例子实现的结果是完全相同的，只是实现的方式不同。看起来`while`循环好像比`for`循环少了点东西，只有一个判断条件。但其实`while`循环也是有初始条件的，只不过在之前就已经定义好了，例如上面例子中的`var i = 1;`，至于变量i的增大，则是放到了循环体里面，其实这个过程和`for`循环没有什么区别，也是变量i不断变大，直到判断条件不满足，则循环结束。

###### 3.do-while循环

- do-while循环语句是一种后测试循环语句，即只有在循环体中的代码执行之后，才会测试出口条件。换句话说，在对条件表达式求值之前，循环体内的代码至少被执行一次。以下是do-while语句的语法：

```
do{
循环体
}while(循环终止条件)
```

- 下面同样实现上面的那个例子：

```
var i = 1;
do{
console.log('学员' + i + '号。');
i = i + 1;
} while(i<=10)
```

- 这个例子的输出结果和上面的结果也是完全相同的。可以看到do-while和while也是很类似的，在循环外面初始化，循环体内改变循环变量，不同的只是先判断循环终止条件还是后判断循环终止条件。
- 像do-while这种后测试循环语句最常用于循环体中的代码至少要被执行一次的情形。

## 推荐资料

- [JS循环 - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
- [JS循环](http://www.dofactory.com/tutorial/javascript-loops)

# chapter 11. [重点] 函数介绍

## 学习目标

- 理解函数的概念和作用
- 理解在函数中参数的作用
- 掌握在JavaScript中定义和调用函数的方法

## 学习内容

- 函数对任何语言来说都算是一个核心的概念。通过函数可以封装任意多条语句，而且可以在任何地方、任何时候调用执行。那么到底什么是函数呢？

- 一段计算机程序代码，函数的出现主要是解决了程序代码共享问题，最初的计算机程序是顺序执行的，但是如果在多个程序中需要实现同一种计算，这时实现同样计算的代码就会出现多次，造成重复，而使用函数则不同，若把该计算规则封装在函数中，那么只需要在使用的地方调用该函数即可。就像下面中的例子那样：

![img](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LEnFv3jMWsHS31RfsLD%2F-LEnFymU6ro7LIcUvFQV%2F-LEnG0gG7-X8ZOWLfLWu%2Ffunction.png?generation=1528794720510412&alt=media)

- 在上图中，有一面漂亮的墙壁，当我们将这面墙壁的漂亮外衣拿掉，会发现在墙壁里面是由若干个砖头砌成的。若把一面修砌好的墙壁比作程序，那么这一个个的砖头就可以理解为函数。函数是一个执行特定功能的可重用的代码块。我们要想在程序中执行它，只需要给它传递参数并调用它，那么该函数就会返回给我们它的执行结果。

#### 定义函数

- 在JavaScript中，我们使用function关键字来定义函数，后面跟一组参数以及函数体。函数的基本语法如下：

```
function functionName(arg0, arg1, arg2 ... argn){
    statements;
}
```

- 下面是一个简单的函数示例：

```
function sayHi(name, message){
    alert('Hello ' + name + ', ' + message) + '!';
}
```

- 这个函数可以通过其函数名来调用，后面还有加上一对圆括号和参数（圆括号中的参数如果有多个，可以用逗号隔开）。调用sayHi()函数的代码如下所示：

```
sayHi('Mike', 'good morning'); // 'Hello Mike, good morning!'
```

- 这样函数的输出结果就是'Hello Mike, good morning!'。函数中定义的命名参数name和message被用作了字符串拼接的两个操作数，最终的结果通过警告框显示了出来。

- 以上例子是一个没有指定返回值的例子。在JavaScript中定义函数的时候，不必指定是否有返回值，但实际上，任何函数在任何时候都可以通过return语句否跟要返回的值来实现返回值。具有返回值的示例如下：

```
function add(num1, num2){
    return num1 + num2;
}
```

- 这个add函数的作用是把两个参数求和并将该值返回。除了return语句外，没有任何声明表示该函数会返回一个值。这个函数的调用示例如下：

```
var result = add(3, 5);
alert(result); // 8
```

- 最终的结果将会弹出8。这里可以注意到，我们需要用一个变量(result)来接收add(3,5)返回的值，这是因为我们在add()函数内部将结果返回(return)了出来，如果不用变量接收，将无法对该结果进行操作。

## 推荐资料

- [JavaScript函数 - MDN](javascript:void(0))

# chapter 12. [重点] DOM介绍

## 学习目标

- 了解DOM基础
- 使用 DOM 对 web 页面元素进行操作

## 学习内容

- DOM（文档对象模型）是针对 HTML 和 XML 文档的一个 API，通过 DOM 可以去改变文档。

- 简单的说，一个 web 网页就是一个文档，使用 DOM 改变文档就是使用 DOM 定义的一些方法操作具体的节点。比如用getElementById 来根据元素 id 来查找元素节点。

- 当浏览器载入HTML时，会生成相应的 DOM 树，大概长这样

  ![img](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LEnFv3jMWsHS31RfsLD%2F-LEnFymU6ro7LIcUvFQV%2F-LEnG-4J9dKFWiSXiSED%2Fhtml-dom.png?generation=1528794719454822&alt=media)

- 把它转成 HTML 代码的话会是这样

```
<html lang="en">
  <head>
    <title>我是title</title>
  </head>
  <body>
    <a href="#">我是文本链接</a>
    <p id="myId">我是p标签</p>
  </body>
</html>
```

- 对于一个 HTML 来说，文档节点 Document （是看不到的）就是它的根节点，这个根节点对应的对象就是 document ，我们可以通过根节点来访问它的子节点(Element 、Text)。

#### Document 类型

- 刚才说道 Document 是整个文档的根节点，我们想要访问某个节点的时候都必须通过 document 这个实例对象。

- document 对象的常用属性：

```
document.documentElement  // 可以直接拿到 html 节点的引用
document.title //  可以直接获取 title 节点的文本 “我是title”
document.URL // 获取 URL
```

- document 对象的常用方法

```
document.getElementById // docment.getElementById('myId') 可以获取到属性 id 为 ‘myId’ 的节点，在上面的代码中获取的也就是 p 节点
document.getElementsByTagName //docment.getElementByTagName('p') 可以获取到节点为 p 的所有节点集
```

- 现在我们就根据 document 对象中的方法获取到 HTML 中任意节点了，下面我们来介绍在已经拿到节点的基础上该如何对该节点进行操作。

#### Element 类型

- 通常我们在使用 document 对象来获取节点时，返回的节点类型就是 Element 类型，所以我们想要对获取的节点进行操作，我们只需要使用 Element 包含的属性和方法即可。

- 常用的属性：

```
var myNode = document.getElementById('myId');
myNode.id // 获取该节点的 id ，即 ‘myId‘
myNode.tagName // 获取该节点的节点名，即 'P'，大部分浏览器返回的标签名都是大写
myNode.className //获取该节点的 class
```

- 操作节点属性的常用方法：

```
//假如我们有一个 input，我们想要获取 input 的 type 属性，并对 type 属性进行操作
<input type='text' id='input'/>

var myNode = document.getElementById('input')
myNode.getAttribute('type') // 获取属性值，即 ‘text’
myNode.setAttribute('type','password') // 将 type 属性值改为 password 类型
myNode.removeAttribute('type') // 移除 type 属性
```

![Xnip2021-05-07_22-56-41.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gqa997ci4oj31e00mijvm.jpg)

## 推荐资料(扩展学习)

- [HTML DOM 简介](http://www.w3school.com.cn/htmldom/dom_intro.asp)
- [MDN nodetype](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/nodeType)
- [runoob nodetype](https://www.runoob.com/jsref/prop-node-nodetype.html)
- [w3c nodetype](https://www.w3school.com.cn/jsref/prop_node_nodetype.asp)

# chapter 13. [重点] 事件和回调

## 学习目标

- 掌握回调函数的使用方法
- 掌握事件监听的使用方法

## 学习内容

#### JavaScript两种执行模式

- “同步模式（Synchronous）”就是一个任务完成之后，后边跟着一个任务接着执行；程序的执行顺序和排列顺序是一直的；
- ”异步模式（Asychronous）”则完全不同，每一个任务都有一个或者多个回调函数（callback），前一个任务结束的时候，不是执行下一个任务，而是执行回调函数，后一个任务则是不等前一个任务结束就执行，所以程序的执行顺序与任务顺序不一致的，异步的。

其中回调函数和事件监听就是最基本的“异步模式”处理方法。

#### 回调函数（callback）

```
function test(start, end, callback){
    var number = Math.ceil(Math.random() * (start - end) + arg2);
    callback(number);　　//传递结果
}

test(10, 20, function(num){
   console.log("Number: " + number); 
});　　　　//结果为10和20之间的随机数
```

- 回调函数具体的定义为：函数A作为参数(函数引用)传递到另一个函数B中，并且这个函数B执行函数A。我们就说函数A叫做回调函数。如果没有名称(函数表达式)，就叫做匿名回调函数。
- 回调函数不一定用于异步，一般同步(阻塞)的场景下也经常用到回调，比如要求执行某些操作后执行回调函数。
- 回调函数，一般在同步情境下是最后执行的，而在异步情境下有可能不执行，因为事件没有被触发或者条件不满足。
- 回调函数简单，容易理解和部署。但是不利于代码的阅读，和维护，各部分之间高度耦合，流程会很混乱，而且每一个任务只能指定一个回调函数。

#### 事件监听（Event）

- 当页面要发生一些事情或做一些事情时，我们称其为事件。事件是网页自带的属性，如click、mousemove、load等。
- 响应某个事件的函数则称为事件处理程序，或者叫做事件侦听器。
- 采用事件驱动模式，任务的执行不取决代码的顺序，而取决于某一个事件是否发生。
- 常见监听函数有：on，bind，listen，addEventListener，observe
- 事件监听比较容易理解，可以绑定多个事件，每一个事件可以指定多个回调函数，而且可以去耦合，有利于实现模块化。但是通过事件监听机制整个程序都要变成事件驱动型，运行流程会变得不清晰。

常见的事件的列表

| 事件        | 描述                     |
| ----------- | ------------------------ |
| onchange    | 元素改变                 |
| onclick     | 用户点击 元素            |
| onmouseover | 用户在一个元素上移动鼠标 |
| onmouseout  | 用户从一个元素上移开鼠标 |
| onkeydown   | 用户按下键盘按键         |
| onload      | 浏览器已完成页面的加载   |

## 推荐资料(扩展学习)

- [JavaScript 事件参考手册](http://www.runoob.com/jsref/dom-obj-event.html)
- [JS事件模型](https://segmentfault.com/a/1190000006934031)
- [彻底理解javascript的回调函数（推荐）](https://www.cnblogs.com/moltboy/archive/2013/04/24/3040213.html)

# chapter 14. [重点] 对象介绍

## 学习目标﻿﻿

- 熟悉JavaScript中的对象的基本用法

## 学习内容

- 回想之前我们讲到的JavaScript数据类型，其中共有七种数据类型，其中有六种数据类型被称为原始类型，因为它们的值只包含单一的属性（是一个字符串，数字等）；还有一种数据类型就是这节将要讲述的内容 - 对象（Object）。

- JavaScript对象类似真实世界中的对象，它们有不同的属性和行为。也就是说，JavaScript对象就是一组**属性**和**方法（函数）**的集合。一个对象也需要用一个变量来存储，然后通过点(.)来访问该对象的属性和方法。

- 比如说：就一个人来说，他有姓名，年龄，可以说话，可以走路。姓名和年龄就是这个人的**属性**。说话，走路就是一个人的行为，当然他还可以有其他更为复杂的行为，像这样子的行为被称作**方法**。

- 在JavaScript中，用大括号的语法就可以创建一个对象，示例如下：

```
var person = {
  name: "Ming",
  age: 17,
  talk: function () { 
    console.log("another... Sky... walk...");
  }
};
```

- 在这个例子中，我们定义了一个姓名为'Ming'，年龄17岁的人，同时他还可以说话。其中，姓名和年龄就是**属性**，而说话就是**方法**。
- 我们可以通过点(.)来访问他的属性和方法：

```
var name = person.name; // 'Ming'
var age = person.age; // 17
person.talk(); // 'another... Sky... walk...'
```

- 当然我们也可以方便的修改他的属性或者再为他添加新的属性和方法，如下：

```
person.name = 'Jackie';
console.log(person.name); // 'Jackie' - edited
person.gender = 'male';
console.log(person.gender); // 'male' - added
```

- 一个对象的属性可以是任何的数据类型，比如我们可以将这个人的姓名修改为另一个对象，如下：

```
person.name = {
    first: 'Jeanne',
    last: 'Calment'
};
```

- 这样person.name也是一个对象了，同样我们也可以使用点(.)运算符来访问该对象的属性，如下：

```
console.log(person.name.first); // 'Jeanne'
console.log(person.name.last); // 'Calment'
```

## 推荐资料(扩展学习)

- [JavaScript对象基础](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Objects/Basics)
- [JavaScript对象基础讲解](http://www.codexiu.cn/javascript/blog/40328/)
- [JavaScript 对象基础](javascript:void(0))

# chapter 15. JSON

## 学习目标

- 掌握JSON对象的使用方法
- 掌握JSON.stringify和JSON.parse方法的使用方法

## 学习内容

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。
- JSON是一种嵌套层级结构，具有自我描述性，可以通过JavaScript进行解析，也通常会通过Ajax进行传输。

- JSON 语法是 JavaScript 语法的子集。
  - 数据是以键值对的形式存储的
  - 不同数据项之间以逗号分隔
  - 通过大括号来保存JSON对象
  - 在JSON对象内容，数据的值也可以是数组，通过中括号来保存数组

- JSON对象示例：

```
  {
    name: 'tw',
    age: '17',
    major: 'Computer Science'
  }
```

- JSON值可以是以下数据结构：
  - 数值（整数或浮点数）
  - 字符串（在双引号中）
  - 逻辑值（true 或 false）
  - 数组（在中括号中）
  - 对象（在大括号中）
  - null

- 因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。示例如下：

```
  var employees = [
    { "firstName":"Bill" , "lastName":"Gates" },
    { "firstName":"George" , "lastName":"Bush" },
    { "firstName":"Thomas" , "lastName": "Carter" }
  ];
  
  // 访问
  employees[1].lastName; // Bush
  
  // 更改
  employees[0].lastName = 'Michael';
```

#### JSON.stringify

- JSON.stringify方法用于将一个字符串转为 JSON 字符串。该字符串符合 JSON 格式，并且可以被JSON.parse方法还原。

- 示例如下：

```js
    JSON.stringify(100) // "100"
    JSON.stringify('tws') // ""tws""
    JSON.stringify([]) // "[]"
    JSON.stringify({}) // "{}"
    JSON.stringify(true) // "true"
    
    JSON.stringify(["true", true])
    // "["true",true]"
    
    JSON.stringify({ name: "tws" })
    // '{"name":"tws"}'
```

#### JSON.parse

- JSON.parse方法用于将 JSON 字符串转换成对应的值。
- 示例如下：

```js
    JSON.parse("100") // 100
    JSON.parse("[]") // []
    JSON.parse("{}") // {}
    JSON.parse("true") // true
    
    var person = JSON.parse('{"name":"tws"}')
    person.name // tws
```

- 如果传入的字符串不是有效的 JSON 格式，JSON.parse方法将报错。示例如下：

```
JSON.parse("'Number'") // Uncaught SyntaxError: Unexpected token' in                  JSON at position 0
```

## 推荐资料

- [介绍 JSON](https://www.json.org/json-zh.html)
- [MDN - JSON](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON)
- [深入理解JavaScript系列（9）：根本没有“JSON对象”这回事！](https://www.cnblogs.com/TomXu/archive/2012/01/11/2311956.html)

# chapter 16. [重点] AJAX

## 学习目标

- 理解Ajax的使用场景
- 掌握Ajax对象的创建过程和使用方法

## 学习内容

- Ajax 是 Asynchronous JavaScript And XML 的首字母缩写。Ajax并不是一种新的编程语言，而仅仅是一种新的技术，它可以创建更好、更快且交互性更强的 web 应用程序。Ajax 使用 JavaScript 在 web 浏览器与 web 服务器之间来发送和接收数据。通过与 web 服务器交换数据，而不是每当用户作出改变时重载整个 web 页面，Ajax 技术可以使网页更迅速地响应。

- Ajax 使用 XML 和 HTTP 请求
  - 传统的 web 应用程序会把数据提交到 web 服务器（使用 HTML 表单）。在 web 服务器把数据处理完毕之后，会向用户返回一张完整的新网页。
  - 由于每当用户提交输入，服务器就会返回新网页，传统的 web 应用程序往往运行缓慢，且越来越不友好。
  - 通过 Ajax，web 应用程序无需重载网页，就可以发送并取回数据。完成这项工作，需要通过向服务器发送 HTTP 请求，并通过当服务器返回数据时使用 JavaScript 仅仅修改网页的某部分。
  - 一般使用 JSON 作为接收服务器数据的格式。

- Ajax对象的创建过程示例：

```js
  // 1. 创建连接 
  var xhr = null; 
  xhr = new XMLHttpRequest() 
  // 2. 连接服务器 
  xhr.open('get', url, true) 
  // 3. 发送请求 
  xhr.send(null); 
  // 4. 接受请求 
  xhr.onreadystatechange = function(){ 
    if(xhr.readyState == 4){ 
      if(xhr.status == 200){ 
        success(xhr.responseText); 
      } else { 
      // fail fail && fail(xhr.status); 
      } 
    } 
  }
```

- Ajax的优点
  - 页面无刷新，局部请求，用户体验良好
  - 使用异步方式与服务器通信，具有更加迅速的响应能力
  - 以前一些服务器的工作可以转移到客户端，利用客户端闲置的能力来处理，减轻服务器和带宽的负担，节约空间和宽带租用成本。并且减轻服务器的负担，ajax的原则是“按需取数据”，可以最大程度的减少冗余请求，和响应对服务器造成的负担。

- Ajax的缺点
  - ajax不支持浏览器back按钮
  - 安全问题 AJAX暴露了与服务器交互的细节
  - 对搜索引擎的支持比较弱，不利于SEO
  - 不容易调试

[原生ajax函数封装](https://codepen.io/linhaishe/pen/oNZadqJ?editors=0010)

## 推荐资料(扩展学习)

- [Ajax 简介](https://www.ibm.com/developerworks/cn/web/wa-aj-ajaxhistory/index.html)
- [Ajax-MDN](https://developer.mozilla.org/zh-CN/docs/Web/Guide/AJAX)
- [Ajax总结篇](https://www.jianshu.com/p/c94e49772123)

# chapter 17. LocalStorage

## 学习目标

- 了解Localstorage的使用场景
- 掌握Localstorage不同方法的使用

## 学习内容

- 在HTML5中，最新加入了localStorage特性，这个特性主要是用来作为本地存储来使用的。在localStorage下一般浏览器支持的是5M大小，这个在不同的浏览器中localStorage会有所不同。

- localStorage只支持String类型的存储。
- 由于Localstorage在HTML5中才被提出，所以在使用localStorage的时候，需要先判断浏览器是否支持localStorage属性，示例如下：

```js
  if(!window.localStorage){
    alert("浏览器支持localstorage");
    return false;
  } else {
    // some code here...
  }
```

- Localstorage的方法：
  - localStorage.setItem(keyName, keyValue); 添加新的数据到Localstorage中存储

```js
    localStorage.setItem('name', 'tws');
    localstorage.name=value
```

- localStorage.getItem(keyName); 返回指定keyName的Localstorage中存储的值

```js
    localStorage.getItem('name'); // "tws"
    localstorage.name
```

- localStorage.removeItem(keyName); 从Localstorage中移除指定keyName的数据项

```js
    localStorage.removeItem('name');
    delete localstorage.name
    localstorage.clear()
```

  - localStorage.key(index); 返回指定顺序的Localstorage中存储的键。

```js
localStorage.key(1); // "name" 
```

- localStorage.clear(); 清除所有的本地Localstorage存储

```
 localstorage.clear()
```

- 要在浏览器中查看Localstorage中的存储数据，在Chrome下可通过DevTools下的 Application 面板，在其中左侧选择 Local Storage即可查看。如下图所示：![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/4687282.jpg)
- localStorage的优势(compaire with cookies)
  - localStorage拓展了cookie的4K限制，为前端数据存储提供了新的思路
  - localStorage会可以将第一次请求的数据直接存储到本地，这个相当于一个5M大小的针对于前端页面的数据库，相比于cookie可以节约带宽
- 没有过期时间
  - 不需要服务器环境
  - 没有路径的问题，不需要写path
  - ajax不会携带发送
- localstorage的不足
  - 不同浏览器的存储大小不统一，并且在IE8以上的IE版本才支持localStorage这个属性
  - localStorage的值类型限定为String类型，许多使用场景下会有限制
  - localStorage在浏览器的隐私模式下面是不可读取的
  - localStorage本质上是对字符串的读取，如果存储内容多的话会消耗内存空间，会导致页面变卡
  - 不能跨浏览器储存

sessionStorage 与 loaclStorage的使用方式是一样的，将名字改成sesscionStorage即可，特点为浏览器关闭即消失。

如果储存的是object对象，需要将数据json转化成字符串，才能在面板上查看(上处部分的面板截图)

## 推荐资料(扩展学习)

- [Localstorage - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Storage)
- [localStorage使用总结](http://www.cnblogs.com/st-leslie/p/5617130.html)
- [HTML5 Web Storage](https://www.w3schools.com/html/html5_webstorage.asp)

# chapter 18. Cookie

cookie是数据，存储在小的text文件中，并放在你的电脑中。是为了储存用户信息，方便下次用户访问网页的时候，cookie会使用记录过的用户信息。

[Cookie w3c](https://www.w3schools.com/js/js_cookies.asp)

[cookie segmentfault](https://segmentfault.com/a/1190000004556040)

## Create a Cookie

- 数据之间是一个分号加上一个空格

- Expires 设置cookie数据过期时间

- path 设置路径，一般将cookie文件设置在项目的根目录下，并将path写成path=/

  With a path parameter, you can tell the browser what path the cookie belongs to. By default, the cookie belongs to the current page.

```js
//添加方式只能是重复执行，没有快捷方式
document.cookie = "username=John Doe";

document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
```

### cookie的时间

`expires`其实是`cookie`失效日期，`expires`必须是 `GMT` 格式的时间（可以通过` new Date().toGMTString()`或者` new Date().toUTCString()` 来获得）如果没有设置该选项，则默认有效期为`session`，即会话`cookie`。这种`cookie`在浏览器关闭后就没有了。

New Date(),setTime(),getTime(),toUTCString()

```js
var birthday = new Date(1991, 9, 17);
var copy = new Date();
//getTime() 方法返回一个时间的格林威治时间数值。返回毫秒数
copy.setTime(birthday.getTime());
//toUTCString() 方法把一个日期转换为一个字符串，使用UTC时区
const event = new Date(1991,9,17);
console.log(event.toUTCString());
//"Wed, 16 Oct 1991 16:00:00 GMT"
```

## Change a Cookie

the same way you create it,The old cookie is overwritten.

```js
document.cookie = "username=John Smith; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
```

## Delete a Cookie

通过设置过期时间使数据过期即可，不需要单独去做删除功能

```js
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
```

## read a cookie

```js
var x = document.cookie;
```

```js
var oDate = new Date();
oDate.setDate(oDate.getDate() + 7);
document.cookie = "a=1";
document.cookie = "a=1";
document.cookie = "b=2;expires=" + oDate;
console.log(document.cookie);
```

## A Function to Set a Cookie

```js
function setCookie(cname, cvalue, exdays) {
  //获取当前时间
  var d = new Date();
  //设置过期时间，算出所需要的毫秒数
  //1s = 1000ms
  //1day = 24h x 60min x 60s x 1000s
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  //设置expires的字符串
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
```

```js
//cookie只能拿到自己目录下的缓存，不能夸目录获取

function setCookie(name, value, expires) {
  if (expires) {
    var oDate = new Date();
    oDate.setDate(oDate.getDate() + expires);
    document.cookie = name + "=" + value + ";path=/;expires=" + oDate;
  } else {
    document.cookie = name + "=" + value + ";path=/";
  }
}

function getCookie(name) {
  console.log(document.cookie);
  var arr = document.cookie.split("; "); // arr['a=1','b=2']

  for (var i = 0; i < arr.length; i++) {
    var arr2 = arr[i].split("="); //arr2 ['a','1']   ['b','2']

    if (arr2[0] == name) {
      return arr2[1];
    }
  }

  return "";
}

function removeCookie(name) {
  setCookie(name, "杨哥下午唱歌", -99999);
}

setCookie("a", 1, 3);
setCookie("b", 2); //setCookie({a:1,b:2})
//alert(getCookie('a')) //1
```



# chapter 19.【重点】面向对象基础

## 学习目标

1. 掌握面向对象的思想

## 学习内容

##### 什么是面向对象编程？

把一组数据结构和处理它们的方法组成**对象**(Object), 把相同行为的对象归纳为**类**(Class), 通过类的**封装**(encapsulation)隐藏内部细节，通过**继承**(inheritance)实现类的**特化**(specializetion)/**泛化**(generalization), 通过**多态**(polymorphism)实现基于对象类型的动**态分派**

其实很好理解，面向对象编程其实就是我们按照正常的思维去写程序，我们会将现实世界中的东西视为一个个对象，然后他们的行为就是一个个方法。

其实传统的面向过程编程，就是让我们以计算机的方式去写程序，我们需要告诉计算机每一步如何执行，

面向对象和面向过程不是对立的，面向对象编程中，我们肯定也会用面向过程的思想写代码。

就像：虽然我不知道空调是如何工作的，但是我会使用，但是空调内部确实存在一套工作过程，这是做空调的人需要关心的，我不关心。

也有人形象地称为：你办事我放心。

##### 面向对象的好处？

1. 接近人的思维，符合人类对现实世界的认知；

2. **封装**特性可以使开发者不必在意内部的具体实现，更方便互相协作；

3. **继承**特性可以减少代码冗余，实现代码复用；

4. 多态

   特性令子类相比父类有不同的行为，这是非常接近现实的；

   ##### 为什么要面向对象编程？

   其实还是因为计算机大多是帮助我们解决实际问题的，实际问题如果用面向过程的思维来想的话，过于复杂，不容易理解。但是如果用面向对象的思想来想的话，和实际正好可以对应起来。

## 推荐资料

- [什么是对象，为什么要面向对象，怎么才能面向对象？](https://blog.csdn.net/ltd010/article/details/78777705)
- [Class的基本语法](http://es6.ruanyifeng.com/#docs/class)
- [Class的继承](http://es6.ruanyifeng.com/#docs/class-extends)


# chapter 20. js基础运算练习

[练习地址](https://school.thoughtworks.cn/learn/program-center/student/index.html#/program/155/task/1911)

## 资料推荐（ 理解+应用）

- [数组常用方法](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [字符串常用方法](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [其它相关](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects)

# chapter 21. tasking任务分解

## 学习目标

- 使用任务分解（Tasking）方法对练习题进行分解
- 综合运用所学的编程知识

## 学习内容

- [Tasking入门](https://s3.cn-north-1.amazonaws.com.cn/tws-courses-resource/Tasking入门.mp4)

## 推荐资料

- [编程的精进之法](https://www.zybuluo.com/jtong/note/504192)
- [像机器一样思考（一）—— 宏观的基础](https://www.zybuluo.com/jtong/note/403738)
- [像机器一样思考（二）—— 数据的细节](https://www.zybuluo.com/jtong/note/471501)
- [像机器一样思考（三）—— 穷尽就是力量](https://www.zybuluo.com/jtong/note/473123)
- [像机器一样思考（四）—— 一图抵千言](https://www.zybuluo.com/jtong/note/774931)

# chapter 22.【重点】ES6 基础

## 学习目标

1. 了解ES6是什么
2. 掌握学习内容中的ES6的新特性
3. 根据推荐资料中的内容自学ES的其它特性（数组的拓展，Module）

## 学习内容

### 一、ECMAScript 6 简介

ECMAScript(ES6) 是JavaScript语言的下一代标准，已经在2015年6月正式发布了；在 JavaScript 的基础上做了重大的更新，提供了更优雅的语法和特性。

#### ECMAScript 和 JavaScript 的关系

ECMAScript 和 JavaScript 的关系是，前者是后者的规格，后者是前者的一种实现（另外的ECMAScript 方言还有 Jscript 和 ActionScript ）。日常场合，这两个词是可以互换的。那为什么不叫 JavaScript 为换名字了呢？原因如下：

1. 商标，1996年11月，JavaScript的创造者Netscape公司，决定将JavaScript提交给国际标准化组织ECMA，希望这种语言能够成为国际标准。根据授权协议，只有Netscape公司(Javascript 的创造者)可以合法地使用JavaScript这个名字，且 JavaScript 本身也已经被 Netscape 公司注册为商标
2. 想体现这门语言的制定者是 ECMA，不是 Netscape，这样有利于保证这门语言的开放性和中立性。

### 二、ES6 新特性

#### 1. let 和 const

ES6提供了两种新的声明变量的方式：let 和 const。

#### 1）作用域

let 和 const 相比于 var 声明的变量有块作用域，let 和 const 只在于当前的块作用域中有效。而 var 声明的变量是在函数作用域内有效。

```
{
  let a = 1;  // a 只能在当前块中被访问
  var b = 1;
}
a // ReferenceError: a is not defined.
b // 1
```

const 和 let 的区别则在于， const 声明变量的同时必须立即给一个初始值，且无法在对该值进行修改。如果该初始值是一个对象，那么该对象的值是可以被修改的。

#### 2）变量提升

变量如果在var 前使用，就会出现「变量提升」现象，值为undefined。let 声明的变量一定要在声明后使用，否则报错。

```
// var 的情况
console.log(a); // 输出undefined
var a = 1;

// let 的情况
console.log(b); // 报错ReferenceError
let b = 1;
```

上述代码，`a`变量用`var`声明，会进行变量提升，脚本刚开始执行就已经存在变量`a`,但是变量`a`没有值，所以输出`undefined`；`b`变量用`let`声明，不会发生变量提升，在声明它之前，变量b是不存在的，这时如果用到它，就会抛出一个错误。

#### 3）const 本质

const实际上保证的，并不是变量的值不得改动，而是变量指向的那个内存地址所保存的数据不得改动。

```
const user = {};

// 为 user 添加一个属性，可以成功
user.age = 23;
user.age // 23

// 将 user 指向另一个对象，就会报错
user = {}; // TypeError: "user" is read-only
```

上面代码中，常量user储存的是一个地址，这个地址指向一个对象。不可变的只是这个地址，即不能把user指向另一个地址，但对象本身是可变的，所以依然可以为其添加新属性。

#### 2. 变量的解构赋值

ES6 允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构。

```
//以前变量赋值只能直接指定
let a = 1;
let b = 2;
let c = 3;
//ES6 允许写成下面这样
let [a, b, c] = [1, 2, 3];
```

##### 1）数组的解构

```
var [a,b,c] = [1,2,3] // 结果 a=1 b=2 c=3
var [a,[b,c]] = [1,[2,3]] // 结果 a=1 b=2 c=3

//解构不成功
var [a] = [];  // a = undefined   
var [a, b] = [1]; //a=1 b=undefined

//不完全解构
var [a] = [1,2]; //a=1

//默认值
var [a=1] = [] //a=1
```

**如果等号的右边不是数组（或者严格地说，不是可遍历的结构），那么将会报错**

```
let [a] = 1;
let [a] = false;
let [a] = NaN;
let [a] = undefined;
let [a] = null;
let [a] = {};
```

##### 2）对象的解构

```
var { b, a } = { a: "aaa", b: "bbb" };
a // "aaa"
b // "bbb"

var { c } = { a: "aaa", b: "bbb" };
c // undefined

//变量名与属性名不一致，必须写成下面这样
let { a: hello } = { a: 'aaa', hello: 'bbb' };
hello // "aaa"

//对象的解构赋值的内部机制，是先找到同名属性，然后再赋给对应的变量
let { a: hello } = { a: "aaa", hello: "bbb" };
hello // "aaa"
a // error: foo is not defined

//对象的解构也可以指定默认值
var {x = 3} = {};
x // 3
var {x, y = 5} = {x: 1};
x // 1
y // 5
```

##### 3）字符串的解构赋值

字符串也可以解构赋值。这是因为此时，字符串被转换成了一个类似数组的对象。

```
const [a, b, c, d, e] = 'hello';
a // "h"
b // "e"
c // "l"
d // "l"
e // "o"

//类似数组的对象都有一个length属性，因此还可以对这个属性解构赋值
let {length : len} = 'hello';
len // 5
```

#### 3.字符串拓展

##### 1）模版字符串

模板字符串（template string）是增强版的字符串，用反引号（`）标识。它可以当作普通字符串使用，也可以用来定义多行字符串（类似 pre 标签的作用），或者在字符串中嵌入变量。

```
// 普通字符串 想要换行需要加上 '\n'
`In JavaScript '\n' is a line-feed.`

// 多行字符串
`In JavaScript this is
 not legal.`

// 字符串中嵌入变量
var name = "ac", time = "today";
`Hello ${name}, how are you ${time}?` // Hello ac, how are you today? 
```

##### 2）字符串的遍历器接口

ES6 为字符串添加了遍历器接口，使得字符串可以被for...of循环遍历

```
for (let codePoint of 'hello') {
  console.log(codePoint)
}
// "h"
// "e"
// "l"
// "l"
// "o"
```

##### 3）includes(), startsWith(), endsWith()

在这之前，JavaScript 只有indexOf方法，可以用来确定一个字符串是否包含在另一个字符串中。

**ES6 又提供了三种新方法：**

- includes()：返回布尔值，表示是否找到了参数字符串。
- startsWith()：返回布尔值，表示参数字符串是否在原字符串的头部。
- endsWith()：返回布尔值，表示参数字符串是否在原字符串的尾部。

```
let s = 'Hello world!';
s.startsWith('Hello') // true
s.endsWith('!') // true
s.includes('o') // true
这三个方法都支持第二个参数，表示开始搜索的位置。

let s = 'Hello world!';
s.startsWith('world', 6) // true
s.endsWith('Hello', 5) // true
s.includes('Hello', 6) // false
```

上面代码表示，使用第二个参数n时，endsWith的行为与其他两个方法有所不同。它针对前n个字符，而其他两个方法针对从第n个位置直到字符串结束。

##### 4）repeat()

`repeat`方法返回一个新字符串，表示将原字符串重复n次。

```
'x'.repeat(3) // "xxx"
'hello'.repeat(2) // "hellohello"
'na'.repeat(0) // ""

//参数如果是小数，会被取整
'na'.repeat(2.9) // "nana"

//如果repeat的参数是负数或者Infinity，会报错。
'na'.repeat(Infinity)
// RangeError
'na'.repeat(-1)
// RangeError

//参数是 0 到-1 之间的小数，则等同于 0
'na'.repeat(-0.9) // ""

//参数NaN等同于 0。
'na'.repeat(NaN) // ""

//如果repeat的参数是字符串，则会先转换成数字。
'na'.repeat('na') // ""
'na'.repeat('3') // "nanana"
```

##### 5）padStart()，padEnd()

ES2017 引入了字符串补全长度的功能。如果某个字符串不够指定长度，会在头部或尾部补全。padStart()用于头部补全，padEnd()用于尾部补全。

```
'x'.padStart(5, 'ab') // 'ababx'
'x'.padStart(4, 'ab') // 'abax'

'x'.padEnd(5, 'ab') // 'xabab'
'x'.padEnd(4, 'ab') // 'xaba'

//如果原字符串的长度，等于或大于最大长度，则字符串补全不生效，返回原字符串
'xxx'.padStart(2, 'ab') // 'xxx'
'xxx'.padEnd(2, 'ab') // 'xxx'

//如果省略第二个参数，默认使用空格补全长度
'x'.padStart(4) // '   x'
'x'.padEnd(4) // 'x   '
```

#### 4.数值的扩展

##### 1）Number.isFinite(), Number.isNaN()

ES6 在Number对象上，新提供了Number.isFinite()和Number.isNaN()两个方法。

Number.isFinite()用来检查一个数值是否为有限的（finite），即不是Infinity。

```
Number.isFinite(15); // true
Number.isFinite(0.8); // true
Number.isFinite(NaN); // false
Number.isFinite(Infinity); // false
Number.isFinite(-Infinity); // false
Number.isFinite('foo'); // false
Number.isFinite('15'); // false
Number.isFinite(true); // false
```

Number.isNaN()用来检查一个值是否为NaN

```
Number.isNaN(NaN) // true
Number.isNaN(15) // false
Number.isNaN('15') // false
Number.isNaN(true) // false
Number.isNaN(9/NaN) // true
Number.isNaN('true' / 0) // true
Number.isNaN('true' / 'true') // true
```

它们与传统的全局方法`isFinite()`和`isNaN()`的区别在于，传统方法先调用`Number()`将非数值的值转为数值，再进行判断，而这两个新方法只对数值有效，`Number.isFinite()`对于非数值一律返回`false`, `Number.isNaN()`只有对于`NaN`才返回`true`，非`NaN`一律返回`false`。

##### 2）Number.isInteger()

Number.isInteger()用来判断一个数值是否为整数

```
Number.isInteger(5) // true
Number.isInteger(5.1) // false

//JavaScript 内部，整数和浮点数采用的是同样的储存方法，所以 5 和 5.0 被视为同一个值
Number.isInteger(5) // true
Number.isInteger(5.0) // true
```

#### 5. Math 对象的扩展

##### 1）Math.trunc()

`Math.trunc`方法用于去除一个数的小数部分，返回整数部分

```
Math.trunc(4.1) // 4
Math.trunc(4.9) // 4
Math.trunc(-4.1) // -4
Math.trunc(-4.9) // -4
Math.trunc(-0.1234) // -0
```

##### 2）Math.sign()

`Math.sign`方法用来判断一个数到底是正数、负数、还是零。对于非数值，会先将其转换为数值。

它会返回五种值：

- 参数为正数，返回+1；
- 参数为负数，返回-1；
- 参数为 0，返回0；
- 参数为-0，返回-0;
- 其他值，返回NaN。

```
Math.sign(-5) // -1
Math.sign(5) // +1
Math.sign(0) // +0
Math.sign(-0) // -0
Math.sign(NaN) // NaN
```

#### 6.函数的扩展

##### 1）函数参数的默认值

ES6 允许为函数的参数设置默认值，即直接写在参数定义的后面

```
function log(x, y = 'World') {
  console.log(x, y);
}

log('Hello') // Hello World
log('Hello', 'China') // Hello China
log('Hello', '') // Hello
```

##### 2）rest 展开运算符

ES6 引入 rest 参数（形式为...变量名），用于获取函数的多余参数，这样就不需要使用arguments对象了。rest 参数搭配的变量是一个数组，该变量将多余的参数放入数组中。

```
function example(...values){
    console.log(values)// console: [1,2,3,4]
}

example(1,2,3,4) 
var a = [1,2,3]
var b = [...a,4,5,6] //b = [1,2,3,4,5,6]
```

##### 3） 箭头函数

ES6 提供了新的方式 `=>` 来定义函数

```
var func = parm => parm
等同于
var func = function (parm){
    return parm
}
```

如果函数没有参数或有多个参数，那么：

```
var func = () => //some code
等同于
var func = function (){
	some code
}

var func = (parm1,parm2) => //some code
等同于
var func = function (parm1,parm2){
	some code
}
```

如果箭头函数的函数体只包含一行代码，则可以不需要写大括号以及 return 语句返回（如果有返回值）

```
var sum = (num1,num2) => num1+num2
等同于
var sum = (num1,num2) => {return num1+num2}
等同于
var sum = function(num1,num2){return num1+num2}
```

箭头函数使得表达更加简洁

```
[1,2,3].map( item=> 2 * item)
等同于
[1,2,3].map(function(item){
    return item * 2
})

[1,3,2].sort((a,b) => a - b)
```

#### 7.数组的扩展

##### 1）扩展运算符

扩展运算符（spread）是三个点（...）。它好比 rest 参数的逆运算，将一个数组转为用逗号分隔的参数序列。

```
console.log(...[1, 2, 3])
// 1 2 3

console.log(1, ...[2, 3, 4], 5)
// 1 2 3 4 5
```

##### 2）扩展运算符的应用

- **复制数组**

数组是复合的数据类型，直接复制的话，只是复制了指向底层数据结构的指针，而不是克隆一个全新的数组。

```
const a = [1, 2];
const b = a;

b[0] = 2;
a // [2, 2]
```

上面代码中，a2并不是a1的克隆，而是指向同一份数据的另一个指针。修改a2，会直接导致a1的变化。

ES5 只能用变通方法来复制数组

```
const a = [1, 2];
const b = a.concat();

b[0] = 2;
a // [1, 2]
```

扩展运算符提供了复制数组的简便写法

```
const a1 = [1, 2];
// 写法一
const a2 = [...a1];
// 写法二
const [...a2] = a1;
```

- **合并数组**

扩展运算符提供了数组合并的新写法

```
const arr1 = ['a', 'b'];
const arr2 = ['c'];
const arr3 = ['d', 'e'];

// ES5 的合并数组
arr1.concat(arr2, arr3);
// [ 'a', 'b', 'c', 'd', 'e' ]

// ES6 的合并数组
[...arr1, ...arr2, ...arr3]
// [ 'a', 'b', 'c', 'd', 'e' ]
```

- **字符串**

扩展运算符还可以将字符串转为真正的数组

```
[...'hello']
// [ "h", "e", "l", "l", "o" ]
```

##### 3） Array.from()

Array.from方法用于将两类对象转为真正的数组：类似数组的对象（array-like object）和可遍历（iterable）的对象（包括 ES6 新增的数据结构 Set 和 Map）。

```
let arrayLike = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    length: 3
};

// ES5的写法
var arr1 = [].slice.call(arrayLike); // ['a', 'b', 'c']

// ES6的写法
let arr2 = Array.from(arrayLike); // ['a', 'b', 'c']

Array.from('hello')
// ['h', 'e', 'l', 'l', 'o']

let namesSet = new Set(['a', 'b'])
Array.from(namesSet) // ['a', 'b']
```

##### 4）Array.of()

Array.of方法用于将一组值，转换为数组

```
Array.of(3, 11, 8) // [3,11,8]
Array.of(3) // [3]
Array.of(3).length // 1
```

##### 5）数组实例的 find() 和 findIndex()

数组实例的`find`方法，用于找出第一个符合条件的数组成员。它的参数是一个回调函数，所有数组成员依次执行该回调函数，直到找出第一个返回值为`true`的成员，然后返回该成员。如果没有符合条件的成员，则返回`undefined`。

```
[1, 4, -5, 10].find((n) => n < 0)
// -5

//find方法的回调函数可以接受三个参数，依次为当前的值、当前的位置和原数组
[1, 5, 10, 15].find(function(value, index, arr) {
  return value > 9;
}) // 10
```

数组实例的`findIndex`方法的用法与`find`方法非常类似，返回第一个符合条件的数组成员的位置，如果所有成员都不符合条件，则返回`-1`

```
[1, 5, 10, 15].findIndex(function(value, index, arr) {
  return value > 9;
}) // 2
```

##### 6）数组实例的 includes()

Array.prototype.includes方法返回一个布尔值，表示某个数组是否包含给定的值，与字符串的includes方法类似。ES2016 引入了该方法。

```
[1, 2, 3].includes(2)     // true
[1, 2, 3].includes(4)     // false
[1, 2, NaN].includes(NaN) // true
```

该方法的第二个参数表示搜索的起始位置，默认为0

```
[1, 2, 3].includes(3, 3);  // false
[1, 2, 3].includes(3, -1); // true
```

## 推荐资料

- [ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/destructuring)

- https://cnodejs.org/topic/57d68794cb6f605d360105bf)

# chapter 23. Promise和Async函数的使用

## 学习目标

- 掌握Promise和Async函数的使用

## 学习内容

### 一、Promise 对象

Promise 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。

所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。从语法上说，Promise 是一个对象，从它可以获取异步操作的消息。Promise 提供统一的 API，各种异步操作都可以用同样的方法进行处理。

Promise对象代表一个异步操作，有三种状态：`pending`（进行中）、`fulfilled`（已成功）和`rejected`（已失败）

#### 1.基本用法

ES6 规定，Promise对象是一个构造函数，用来生成Promise实例

```
//方法1
//声明一个Promise对象
const promise = new Promise(function(resolve, reject) {
  // ... some code

  if (/* 异步操作成功 */){
    resolve(value);
  } else {
    reject(error);
  }
});

// 方法2
function promise () {
    return new Promise ( function (resolve, reject) {
        if ( success ) {
            resolve(a)
        } else {
            reject(err)
        }
    } )
}
```

#### 2.Promise.prototype.then()

Promise 实例具有then方法，也就是说，then方法是定义在原型对象Promise.prototype上的。它的作用是为 Promise 实例添加状态改变时的回调函数。前面说过，then方法的第一个参数是resolved状态的回调函数，第二个参数（可选）是rejected状态的回调函数。

then方法返回的是一个新的Promise实例（注意，不是原来那个Promise实例）。因此可以采用链式写法，即then方法后面再调用另一个then方法。

```
getJSON("/posts.json").then(function(json) {
  return json.post;
}).then(function(post) {
  // ...
});
```

#### 3. Promise.prototype.catch()

`Promise.prototype.catch`方法是`.then(null, rejection)`或`.then(undefined, rejection)`的别名，用于指定发生错误时的回调函数。

```
getJSON('/posts.json').then(function(posts) {
  // ...
}).catch(function(error) {
  // 处理 getJSON 和 前一个回调函数运行时发生的错误
  console.log('发生错误！', error);
});
```

getJSON方法返回一个 Promise 对象，如果该对象状态变为resolved，则会调用then方法指定的回调函数；如果异步操作抛出错误，状态就会变为rejected，就会调用catch方法指定的回调函数，处理这个错误。

#### 4.Promise.prototype.finally()

finally方法用于指定不管 Promise 对象最后状态如何，都会执行的操作。该方法是 ES2018 引入标准的。

```
promise
.then(result => {···})
.catch(error => {···})
.finally(() => {···});
```

上面代码中，不管promise最后的状态，在执行完then或catch指定的回调函数以后，都会执行finally方法指定的回调函数。

#### 5.Promise.all()、Promise.race()

Promise.all方法用于将多个 Promise 实例，包装成一个新的 Promise 实例

```
const p = Promise.all([p1, p2, p3]);
```

上面代码，Promise.all方法接受一个数组作为参数，p1、p2、p3都是 Promise 实例，如果不是，就会先调用下面讲到的Promise.resolve方法，将参数转为 Promise 实例，再进一步处理。（Promise.all方法的参数可以不是数组，但必须具有 Iterator 接口，且返回的每个成员都是 Promise 实例。）

```
const p = Promise.race([p1, p2, p3]);
```

上面代码，只要p1、p2、p3之中有一个实例率先改变状态，p的状态就跟着改变。那个率先改变的 Promise 实例的返回值，就传递给p的回调函数。

### 二、async(异步) 函数变体

#### 1.含义

ES2017 标准引入了 async 函数，使得异步操作变得更加方便。async 函数就是 Generator 函数的语法糖。

有一个 Generator 函数，依次读取两个文件

```
const fs = require('fs');

const readFile = function (fileName) {
  return new Promise(function (resolve, reject) {
    fs.readFile(fileName, function(error, data) {
      if (error) return reject(error);
      resolve(data);
    });
  });
};

const gen = function* () {
  const f1 = yield readFile('/etc/fstab');
  const f2 = yield readFile('/etc/shells');
  console.log(f1.toString());
  console.log(f2.toString());
};
```

上面代码的函数gen可以写成async函数。async函数就是将 Generator 函数的星号（*）替换成async，将yield替换成await。

```
const asyncReadFile = async function () {
  const f1 = await readFile('/etc/fstab');
  const f2 = await readFile('/etc/shells');
  console.log(f1.toString());
  console.log(f2.toString());
};
```

**async函数对 Generator 函数的改进，体现在以下四点：**

- 内置执行器

  Generator 函数的执行必须靠执行器，所以才有了co模块，而async函数自带执行器。也就是说，async函数的执行，与普通函数一模一样，只要一行。

- 更好的语义

  async和await，比起星号和yield，语义更清楚了。async表示函数里有异步操作，await表示紧跟在后面的表达式需要等待结果。

- 更广的适用性

  co模块约定，yield命令后面只能是 Thunk 函数或 Promise 对象，而async函数的await命令后面，可以是 Promise 对象和原始类型的值（数值、字符串和布尔值，但这时会自动转成立即 resolved 的 Promise 对象）。

- 返回值是 Promise

  async函数的返回值是 Promise 对象，这比 Generator 函数的返回值是 Iterator 对象方便多了。你可以用then方法指定下一步的操作。

#### 2.基本用法

async函数返回一个 Promise 对象，可以使用then方法添加回调函数。当函数执行的时候，一旦遇到await就会先返回，等到异步操作完成，再接着执行函数体内后面的语句。

```
async function getStockPriceByName(name) {
  const symbol = await getStockSymbol(name);
  const stockPrice = await getStockPrice(symbol);
  return stockPrice;
}

getStockPriceByName('goog').then(function (result) {
  console.log(result);
});
```

上面代码是一个获取股票报价的函数，函数前面的async关键字，表明该函数内部有异步操作。调用该函数时，会立即返回一个Promise对象。

async 函数有多种使用形式

```
// 函数声明
async function foo() {}

// 函数表达式
const foo = async function () {};

// 对象的方法
let obj = { async foo() {} };
obj.foo().then(...)

// Class 的方法
class Storage {
  constructor() {
    this.cachePromise = caches.open('avatars');
  }

  async getAvatar(name) {
    const cache = await this.cachePromise;
    return cache.match(`/avatars/${name}.jpg`);
  }
}

const storage = new Storage();
storage.getAvatar('jake').then(…);

// 箭头函数
const foo = async () => {};
```

#### 3.语法

- 返回 Promise 对象

  async函数返回一个 Promise 对象。async函数内部return语句返回的值，会成为then方法回调函数的参数。

```
async function f() {
  return 'hello world';
}

f().then(v => console.log(v))
// "hello world"
```

- Promise 对象的状态变化

  async函数返回的 Promise 对象，必须等到内部所有await命令后面的 Promise 对象执行完，才会发生状态改变，除非遇到return语句或者抛出错误。也就是说，只有async函数内部的异步操作执行完，才会执行then方法指定的回调函数。

```
async function getTitle(url) {
  let response = await fetch(url);
  let html = await response.text();
  return html.match(/<title>([\s\S]+)<\/title>/i)[1];
}
getTitle('https://tc39.github.io/ecma262/').then(console.log)
// "ECMAScript 2017 Language Specification"
```

- await 命令

  正常情况下，await命令后面是一个 Promise 对象，返回该对象的结果。如果不是 Promise 对象，就直接返回对应的值。

```
async function f() {
  // 等同于
  // return 123;
  return await 123;
}

f().then(v => console.log(v))
// 123
```

- 错误处理

  如果await后面的异步操作出错，那么等同于async函数返回的 Promise 对象被reject。

```
async function f() {
  await new Promise(function (resolve, reject) {
    throw new Error('出错了');
  });
}

f()
.then(v => console.log(v))
.catch(e => console.log(e))
// Error：出错了
```

上面代码中，async函数f执行后，await后面的 Promise 对象会抛出一个错误对象，导致catch方法的回调函数被调用，它的参数就是抛出的错误对象。具体的执行机制，可以参考后文的“async 函数的实现原理”。

## 推荐资料(扩展学习)

- [Promise 对象](http://es6.ruanyifeng.com/#docs/promise)
- [async 函数](http://es6.ruanyifeng.com/#docs/async)



# 主要练习

1. tasking 黄焖鸡

[tasking 黄焖鸡](https://school.thoughtworks.cn/learn/program-center/student/index.html#/program/155/task/1912)

2. tasking 学生成绩单

[学生成绩单](https://school.thoughtworks.cn/learn/program-center/student/index.html#/program/155/task/1915)

3. es6运算练习

[es6 运算练习](https://school.thoughtworks.cn/learn/program-center/student/index.html#/program/155/task/1916)

4. Todolist

[todolist](https://school.thoughtworks.cn/learn/program-center/student/index.html#/program/155/task/1917)

5. 完成待办事项表(Todo List)的网页应用，具体要求请看[GitHub](https://github.com/tws-online-quiz/tw-stage-2-project-1)