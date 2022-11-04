# Chapter 3 Language Basics

## I. Syntax

#### 1. Case-sensitivity

Test ≠ test

#### 2. Identifiers

标识符,An identifier is the name of a variable, function, property, or function argument.

- The first character must be a letter, an underscore (_), or a dollar sign ($). 
- All other characters may be letters, underscores, dollar signs, or numbers.
- Keywords, reserved words, true, false, and null cannot be used as identifiers.

```
a
account
account_99
accountNumber
_accountNumber:for privite
$accountNumber
_123
__proto__
```

#### 3. Comments

- A single-line comment

```javascript
//single line comment 
```

- A block comment
```javascript
/*comment
*this is a multi-line
*comment
*/
```
#### 4. Strict Mode

` “use strict” `

some of the erratic behavior of ECMAScript 3 is addressed and errors are thrown for unsafe activities.

#### 5. Statements

Statements end with ; (semicolon 

in ECMAScript are terminated by a semicolon makes the parser determine where the end of a statement occurs.

`var diff = a - b;      //valid - preferred `

Multiple statements curly brace { } 


```javascript
if (test){
test = false;
alert(test); 
}
```
#### 6. Keywords are reserved words

保留字和关键字,By rule, keywords are reserved and cannot be used as identifiers or property names. 

Attempting to use a keyword as an identifier name will cause an “Identifier Expected” error in ECMAScript 3 JavaScript engines. Attempting to use a reserved word may or may not cause the same error, depending on the particular engine being used. 

#### 7. Variables

` var message = “hi”; `

defining a variable inside of a function using var means that the variable is destroyed as soon as the function exits。
```javascript
function test(){
var message = “hi”;  //local variable 局部变量
} 
test(); 
alert(message); //error! 
```
As soon as the function test() is called, the variable is defined and becomes accessible outside of the function once it has been executed. 
```javascript
function test(){
message = “hi”;  //global variable 全局变量
} 
test(); 
alert(message); //”hi” 
```
shortage of global variable 

Global variables defined locally are hard to maintain and cause confusion, because it’s not immediately apparent if the omission of var was intentional. Strict mode throws a ReferenceError when an undeclared variable is assigned a value. 

## II. Data Type

### 1. the typeof operator

“undefined” if the value is undefined, variable declared,but has no value

“boolean” if the value is a Boolean （true / false)

“string” if the value is a string 

“number” if the value is a number 

“object” if the value is an object (other than a function) or null 

“function” if the value is a function 

functions are considered objects in ECMAScript ,don’t represent another data type，但是有必要进行区分。

typeof null returns a value of “object”, as the special value null is considered to be an empty object reference.
```javascript
var message = “some string”; 
alert(typeof message);    //”string” ,no parenthesis are required
alert(typeof(message));   //”string” 
alert(typeof 95);         //”number” 
```
### 2. Undefined

by default, any uninitialized variable gets the value of undefined. 
```javascript
var message; 
alert(message == undefined);  //true 
```
未初始化和未声明 alert error
```javascript
var message;//this variable is declared but has a value of undefined
//make sure this variable isn’t declared 
//var age
alert(message);  //”undefined” 
alert(age);      //causes an error 
```

未初始化和未声明 typeof undefined
```javascript
var message;//this variable is declared but has a value of undefined，未初始化
//make sure this variable isn’t declared 
//var age //未声明
alert(typeof message);  //”undefined” 
alert(typeof age);      //”undefined” 
```
you’ll know that it’s because a given variable hasn’t been declared rather than was simply not initialized. 

### 3. Null 
```javascript
var car = null; 
alert(typeof car);   //”object” 
```
The value undefined is a derivative of null

```javascript
alert(null == undefined);   //true 
```

Any time an object is expected but is not available, null should be used in its place. This helps to keep the paradigm of null as an empty object pointer and further differentiates it from undefined. 为了区分空对象和未初始化的变量

### 4. Boolean 

only two literal values: true and false. 

Boolean literals true and false are case-sensitive, so True and False

```javascript
//Boolean( ) function
var message = “Hello world!”; 
var messageAsBoolean = Boolean(message); 
```

<mark>VALUES CONVERTED TO TRUE / FALSE</mark>

| DATA TYPE | VALUES CONVERTED TO TRUE                | DATA TYPEVALUES CONVERTED TO TRUE |
| --------- | --------------------------------------- | --------------------------------- |
| Boolean   | true                                    | False                             |
| String    | Any nonempty string                     | “” (empty string)                 |
| Number    | Any nonzero number (including infinity) | 0, NaN                            |
| Object    | Any object                              | null                              |
| Undefined | n/a                                     | Undefined                         |

variable you’re using in a flow-control statement are automatic conversion. 

```javascript
var message = “Hello world!”; 
if (message){
alert(“Value is true”); 
} 
```

### 5. Number  

#### a. integers and floating-point values

represent both integers and floating-point values/double-precision values

always looks for ways to convert values into integers

浮点型就是数字类型的一种，它不仅可以表示整数，还可以表示小数

```javascript
var floatNum1 = 1.; 
//missing digit after decimal - interpreted as integer 1 
var floatNum2 = 10.0;  
//whole number - interpreted as integer 10 
```

(暂时不明白进制，且暂时用不到，就略略略略略过吧～)

#### b. range of values

The smallest number : stored in Number.MIN_VALUE and is 5e-324 on most browsers

the largest number : stored in Number.MAX_VALUE and is 1.7976931348623157e+308 on most browsers.

Infinity, that value cannot be used in any further calculations

isFinite() function only returns true only if the argument is between the minimum and the maximum values,

```javascript
var result = Number.MAX_VALUE + Number.MAX_VALUE; 
alert(isFinite(result));    //false 
```

#### c. NaN (Not a Number)

indicate when an operation intended to return a number has failed (as opposed to throwing an error).

属于数字类型但不是数字

- any operation involving NaN always returns NaN (for instance, NaN /10)

- NaN is not equal to any value, including NaN

```javascript
alert(NaN == NaN); //false 
```

`isNaN( ) function`

```javascript
alert(isNaN(NaN));       //true 
alert(isNaN(10));        //false - 10 is a number 
alert(isNaN(“10”));      //false - can be converted to number 10 
alert(isNaN("blue"));    //true - cannot be converted to a number 
alert(isNaN(true));      //false - can be converted to number 1 
isNaN(NaN); //true
```

#### d. Number Conversions

##### Number ( )

be used on any data type

Rules:

- When applied to Boolean values, true and false get converted into 1 and 0, respectively. 

- When applied to numbers, the value is simply passed through and returned. 

- When applied to null, Number() returns 0. 

- When applied to undefined, Number() returns NaN. 

- When applied to strings,
  - If the string contains only numbers, optionally preceded by a plus or minus sign, it is always converted to a decimal number, so “1” becomes 1, “123” becomes 123, and “011” becomes 11 (note: leading zeros are ignored). 
  - If the string contains a valid floating-point format, such as “1.1”, it is converted into the appropriate floating point numeric value (once again, leading zeros are ignored). 
  - If the string contains a valid hexadecimal format, such as “0xf”, it is converted into an integer that matches the hexadecimal value. 
  - If the string is empty (contains no characters), it is converted to 0. 
  - If the string contains anything other than these previous formats, it is converted into NaN. number(22我)👉NaN

- When applied to objects

  the valueOf() method is called and the returned value is 

  converted based on the previously described rules. If that conversion results in NaN, the toString() method is called and the rules for converting strings are applied. 

  JavaScript调用`valueOf`方法将对象转换为原始值。

##### parseInt ( )

used specifically for converting strings to numbers.

```javascript
var num1 = parseInt(“1234blue”);    //1234 
var num2 = parseInt(“”);            //NaN 
var num3 = parseInt(“0xA”);         //10 - hexadecimal 
var num4 = parseInt(22.5);          //22 
var num5 = parseInt(“70”);          //70 - decimal 
var num6 = parseInt(“0xf”);         //15 - hexadecimal 
var num = parseInt(“0xAF”, 16);     //175 
```

##### parseFloat ( )

used specifically for converting strings to numbers.只解析十进制

- 解析到末尾，或解析到遇见一个无效的浮点数数字为止，解析到第一个小数点的位置，第二个无效。“22.34.5” = “22.34”
- 始终忽略前导的0

```javascript
var num1 = parseFloat(“1234blue”);    //1234 - integer 
var num2 = parseFloat(“0xA”);         //0 
var num3 = parseFloat(“22.5”);        //22.5 
var num4 = parseFloat(“22.34.5”);     //22.34 
var num5 = parseFloat(“0908.5”);      //908.5 
var num6 = parseFloat(“3.125e7”);     //31250000 
```

### 6. String 

##### Template literals (Template strings)

[template literals](https://css-tricks.com/template-literals/)

[template literal](https://developers.google.com/web/updates/2015/01/ES6-Template-Strings)

[Tagged Template Literals](https://www.youtube.com/watch?v=4oVJVglLLns)

They allow for both multiline strings and string interpolation.

```js
console.log(`foo
bar`);
// foo
// bar

var foo = 'bar';
console.log(`Let's meet at the ${foo}`);
// Let's meet at the bar
```

Strings can be delineated by either double quotes (“) or single quotes (‘)

```javascript
var firstName = "Nicholas"; 
var lastName = ‘Zakas’
```

<mark>Character Literals page42 字符字面量</mark>

##### string's are immutable

To change the string held by a variable, the original string must be destroyed and the variable filled with another string containing a new value

```javascript
var lang = "Java"; 
lang = lang + "Script"; 
```

##### Converting to a String 

- toString( ) 
  a. only to return the string equivalent of the value

  b. available on values that are numbers, Booleans, objects, and strings.

  c. If a value is null or undefined, this method is not available. 
  
```javascript
var age = 11; 
var ageAsString = age.toString();    //the string “11” 
var found = true; 
var foundAsString = found.toString(); //the string “true” 
var age = null;
var ageAsStrting = age.toString(); // undefined
var age = undefined;
var ageAsStrting = age.toString(); //undefined
```

- String( )

```javascript
//check null & undefined
var value1 = 10; 
var value2 = true; 
var value3 = null; 
var value4;

alert(String(value1));     //”10” 
alert(String(value2));     //”true” 
alert(String(value3));     //”null” 
alert(String(value4));     //”undefined”
```

#### slice()、 substring()和substr()的区别

[参考地址](https://www.jianshu.com/p/4d06661cf2b8)

| 方法                  | 参数                                                         | 返回值                              |
| :-------------------- | :----------------------------------------------------------- | :---------------------------------- |
| slice(start, end)     | start(必需) -起始位置； end(可选)-结束位置，若未指定，则默认到末尾所有元素 | 返回 [start,end)之间的元素          |
| substring(start, end) | start(必需) -起始位置；end(可选)-结束位置，若未指定，则默认到末尾所有元素 | 返回 [start,end)之间的元素          |
| substr(start, length) | start(必需)-起始位置；length(可选)-所截取的元素的个数，若未指定，则默认到末尾 | 返回[start, start+length)之间的元素 |

> 当传的参数都为正数的时候，substring和slice没有区别。当参数为负数时，三个函数的行为不尽相同。

- slice() - 将传入的负参数与字符串长度相加；
- substring() - 把所有的负值置为0；
- substr() - 将负的第一个参数与字符串长度相加，负的第二个参数置为0。

###### 例子

`1.` 参数为正数

```jsx
    var str = 'hello world';
    console.log(str.slice(3)); // lo world
    console.log(str.substring(3));// lo world
    console.log(str.substr(3));// lo world

    console.log(str.slice(3, 7)); // lo w
    console.log(str.substring(3, 7)); // lo w
    console.log(str.substr(3, 7));//lo worl
```

`2` 参数为负数

```jsx
  var str = 'hello world';
  console.log(str.slice(-3)); // rld
  console.log(str.substring(-3));// hello world
  console.log(str.substr(-3));// rld

  console.log(str.slice(3, -4)); // lo w
  console.log(str.substring(3, -4)); // hel
  console.log(str.substr(3, -4));// ""(空字符串)
```

###### 以上示例的元算过程如下：

------

- slice(-3) => slice(8)
- substring(-3) => substring(0)
- substr(-3) => substr(8)
- slice(3, -4) => slice(3, 7)
- substring(3, -4) => substring(3, 0) =>substring(0, 3)
- substr(3, -4) => substr(3, 0)

### 7. Object 

#### 创建对象的方法

search : Chapter 5 : Reference Types

Each Object instance has the following properties and methods:

- constructor
- hasOwnProperty(propertyName)
- isPrototypeOf(object)
- propertyIsEnumerable(propertyName)
- toLocaleString( )
- toString()
- valueOf( ) 

### 8. Function

## III. Operators

[表达式与运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Expressions_and_Operators)

### 1. unary operators

一元操作符。

#### a. Increment/Decrement  

(++)(--)

- prefix increment or a prefix decrement,

```javascript
var age = 29; 
++age; //age = age + 1; 

var age = 29; 
--age; //age = age - 1; 

```

SIDE EFFECT

```javascript
var age = 29; 
var anotherAge = --age + 2;
alert(age);          //outputs 28 
alert(anotherAge);  //outputs 30 

var num1 = 2; 
var num2 = 20; 
var num3 = --num1 + num2; //equals 21  
var num4 = num1 + num2;   //equals 21 
```

- Postfix increment and decrement (++)(--)

```javascript
var age = 29; 
age++; 

var num1 = 2; 
var num2 = 20; 
var num3 = num1-- + num2;    //equals 22 
var num4 = num1 + num2;      //equals 21 
```

#### b. =+,=-

```javascript
var num = 25; 
num = +num;    //still 25 
num = -num;    // -25 
```
these operators work on any values,integers,strings, Booleans, floating-point values, and objects. 

rules:

- string that is a valid representation of a number, convert to a number and apply the change.
- a string that is not a valid number, the variable’s value is set to NaN 
- used on a Boolean value that is false, convert to 0 , true, convert to 1 
- on a floating-point value, apply the change by adding or subtracting 1
- on an object, call its valueOf() method to get a value to work with. 

```javascript
var s1 = “01”; 
var s2 = “1.1”; 
var s3 = “z”; 
var b = false; 
var f = 1.1; 
var o = { valueOf: function() {return -1;} };
s1 = -s1;   //value becomes numeric -1 
s2 = -s2;   //value becomes numeric -1.1 
s3 = -s3;   //value becomes NaN 
b = -b;     //value becomes numeric 0 
f = -f;     //change to -1.1 
o = -o;     //value becomes numeric 1 
```

```javascript
var s1 = “01”; 
var s2 = “1.1”; 
var s3 = “z”; 
var b = false; 
var f = 1.1; 
var o = { valueOf: function() {return -1;} };
s1 = +s1;   //value becomes numeric 1 
s2 = +s2;   //value becomes numeric 1.1 
s3 = +s3;   //value becomes NaN 
b = +b;     //value becomes numeric 0 
f = +f;     //change to 1.1 
o = +o;     //value becomes numeric -1 
```

### 2. Bitwise Operators

位操作符。这章我很是拒绝。进制很方，那就先略过吧~

### 3. Boolean Operators

three Boolean operators: NOT, AND, and OR

#### a. Logical NOT 

！(exclamation point) / !! (two NOT operators)

```javascript
alert(!false);      //true object
alert(!”blue”);     //false nonempty string,
alert(!0);          //true 
alert(!NaN);        //true 
alert(!””);         //true empty string
alert(!12345);      
//false any number other than 0 (including Infinity),

alert(!!”blue”);     //true 
alert(!!0);          //false 
alert(!!NaN);        //false 
alert(!!””);         //false 
alert(!!12345);      //true 
```

#### b. Logical AND

double ampersand (&&) and is applied to two values

`var result = true && false; `

one false all false 

Logical AND can be used with any type of operand, not just Booleanvalues.logical AND does not always return a Boolean value; instead, it does one of the following: 

- If the fi rst operand is an object, then the second operand is always returned. 
- If the second operand is an object, then the object is returned only if the fi rst operand evaluates to true. 

- If both operands are objects, then the second operand is returned. 
- If either operand is null, then null is returned. 
- If either operand is NaN, then NaN is returned. 
- If either operand is undefined, then undefined is returned. 

#### c. Logical OR

double pipe (||) 

`var result = true || false; `

one true all true



logical OR will not always return a Boolean value; instead, it does one of the following: 

- If the first operand is an object, then the first operand is returned. 

- If the first operand evaluates to false, then the second operand is returned. 

- If both operands are objects, then the first operand is returned. 

- If both operands are null, then null is returned. 

- If both operands are NaN, then NaN is returned. 

- If both operands are undefined, then undefined is returned. 

### 4. Multiplicative Operators

#### a. Multiply

an asterisk (*) 

`var result = 34 * 56; `

如果操作数不是数值，则后台会自用Number()进行数值转换

rules:

- If the operands are numbers, regular arithmetic multiplication is performed, meaning that two positives or two negatives equal a positive, whereas operands with different signs yield a negative. 
- If either operand is NaN, the result is NaN. 
- If Infinity is multiplied by 0, the result is NaN. 
- If Infinity is multiplied by any finite number other than 0, the result is either Infinity or –Infinity, depending on the sign of the second operand. 
- If Infinity is multiplied by Infinity, the result is Infinity. 
- If either operand isn’t a number, it is converted to a number behind the scenes using Number() and then the other rules are applied. 

#### b. Divide

slash (/) 

`var result = 66 / 11; `

rules:

- If the operands are numbers, regular arithmetic division is performed, meaning that two positives or two negatives equal a positive, whereas operands with different signs yield a negative. If the result can’t be represented in ECMAScript, it returns either Infinity or –Infinity. 
- If either operand is NaN, the result is NaN. 
- If Infinity is divided by Infinity, the result is NaN. 
- If zero is divided by zero, the result is NaN. 
- If a nonzero finite number is divided by zero, the result is either Infinity or –Infinity, depending on the sign of the fi rst operand. 
- If Infinity is divided by any number, the result is either Infinity or –Infinity, depending on the sign of the second operand. 
- If either operand isn’t a number, it is converted to a number behind the scenes using Number() and then the other rules are applied. 

#### c. Modulus

percent sign (%)

`var result = 26 % 5; //equal to 1 `

rules:

- If the operands are numbers, regular arithmetic division is performed, and the remainder of that division is returned. 
- If the dividend is an infi nite number and the divisor is a fi nite number, the result is NaN. 
- If the dividend is a fi nite number and the divisor is 0, the result is NaN. 
- If Infinity is divided by Infinity, the result is NaN. 
- If the dividend is a fi nite number and the divisor is an infi nite number, then the result is the dividend. 
- If the dividend is zero and the divisor is nonzero, the result is zero. 
- If either operand isn’t a number, it is converted to a number behind the scenes using Number() and then the other rules are applied. 

### 5. Additive Operators

#### a. Add

operator (+) 

`var result = 1 + 2; `

- If the two operands are numbers:
  - If either operand is NaN, the result is NaN. 
  - If Infinity is added to Infinity, the result is Infinity. 
  - If –Infinity is added to –Infinity, the result is –Infinity. 
  - If Infinity is added to –Infinity, the result is NaN. 
  - If +0 is added to +0, the result is +0. 
  - If –0 is added to +0, the result is +0. 
  - If –0 is added to –0, the result is –0. 

- one of the operands is a string:
  - If both operands are strings, the second string is concatenated to the fi rst. 
  - If only one operand is a string, the other operand is converted to a string and the result is the concatenation of the two strings. 

- If either operand is an object, number, or Boolean,toString() method is called to get a string value and then the previous rules regarding strings are applied.

- For undefined and null, the String() function is called to retrieve the values “undefined” and “null”, respectively. 

```javascript
var result1 = 5 + 5;     //two numbers 
alert(result1);           //10 
var result2 = 5 + “5”;   //a number and a string 
alert(result2);           //”55” 
  
var num1 = 5; 
var num2 = 10; 
var message = “The sum of 5 and 10 is “ + num1 + num2;
alert(message);    //”The sum of 5 and 10 is 510” 
```

#### b. Subtract

operator (-) 

`var result = 2 - 1;`

- If the two operands are numbers, perform arithmetic subtract and return the result. 
- If either operand is NaN, the result is NaN. 
- If Infinity is subtracted from Infinity, the result is NaN. 
- If –Infinity is subtracted from –Infinity, the result is NaN. 
- If –Infinity is subtracted from Infinity, the result is Infinity. 
- If Infinity is subtracted from –Infinity, the result is –Infinity. 
- If +0 is subtracted from +0, the result is +0. 
- If –0 is subtracted from +0, the result is –0. 
- If –0 is subtracted from –0, the result is +0. 
- If either operand is a string, a Boolean, null, or undefined, it is converted to a number (using Number() behind the scenes) and the arithmetic is calculated using the previous rules. 
- If that conversion results in NaN, then the result of the subtraction is NaN.
- If either operand is an object, its valueOf() method is called to retrieve a numeric value to represent it. If that value is NaN, then the result of the subtraction is NaN. If the object doesn’t have valueOf() defined, then toString() is called and the resulting string is converted into a number. 

### 6. Relational Operators

less-than (<), greater-than (>), less-than-or-equal-to (<=), and greater-than-or-equal-to (>=) 

<mark>Each of these operators returns a Boolean value</mark>

```javascript
var result1 = 5 > 3;    //true 
var result2 = 5 < 3;    //false 
```

rules:

- If the operands are numbers, perform a numeric comparison. 
- If the operands are strings, compare the character codes of each corresponding character in the string. 
- If one operand is a number, convert the other operand to a number and perform a numeric comparison. 
- If an operand is an object, call valueOf() and use its result to perform the comparison according to the previous rules. If valueOf() is not available, call toString() and use that value according to the previous rules. 
- If an operand is a Boolean, convert it to a number and perform the comparison. 

<mark>字符串的比较会和数值比较得出的结果不一样</mark>

```javascript
var result = “Brick” < “alphabet”;  //true 
var result = “Brick”.toLowerCase() < “alphabet”.toLowerCase(); //false 
var result = “23” < “3”;  //true 
var result = “23” < 3;    //false
var result = “a” < 3;    //false because “a” becomes NaN
var result1 = NaN < 3;    //false 
var result2 = NaN >= 3;   //false 
```

### 7. Equality Operators

double equal sign (==),returns true only if the operands are equal without conversion

exclamation point followed by an equal sign (!=)

| expression        | value |
| :---------------- | :---- |
| null == undefined | true  |
| “NaN” == NaN      | false |
| 5 == NaN          | false |
| NaN == NaN        | false |
| NaN != NaN        | true  |
| false == 0        | true  |
| true == 1         | true  |
| true == 2         | false |
| undefined == 0    | false |
| null == 0         | false |
| “5” == 5          | true  |
| 0 === undefined   | false |

#### Identically Equal and Not Identically Equal 

 three equal signs (===)

returns true only if the operands are equal without conversion

```javascript
var result1 = (“55” == 55);    
//true - equal because of conversion 
var result2 = (“55” === 55);   
//false - not equal because different data types 
var result1 = (“55” != 55);    
//false - equal because of conversion 
var result2 = (“55” !== 55);   
//true - not equal because different data types 
```

rules:

- If an operand is a Boolean value, convert it into a numeric value before checking for equality. A value of false converts to 0, whereas a value of true converts to 1. 

- If one operand is a string and the other is a number, attempt to convert the string into a number before checking for equality. 

- If one of the operands is an object and the other is not, the valueOf() method is called on the object to retrieve a primitive value to compare according to the previous rules. 
- Values of null and undefined are equal. 
- Values of null and undefined cannot be converted into any other values for equality checking. 
- If either operand is NaN, the equal operator returns false and the not-equal operator returns true. Important note: even if both operands are NaN, the equal operator returns false because, by rule, NaN is not equal to NaN. 
- If both operands are objects, then they are compared to see if they are the same object. If both operands point to the same object, then the equal operator returns true. Otherwise, the two are not equal. 

### 8. Conditional Operator

variable = boolean_expression ? true_value : false_value;

var max = (num1 > num2) ? num1 : num2; 

max is to be assigned the number with the highest value. The expression states that if num1 is greater than num2, then num1 is assigned to max. If, however, the expression is false (meaning that num1 is less than or equal to num2), then num2 is assigned to max. 

### 9. Assignment Operators

equal sign (=) and simply assigns the value on the right to the variable on the left

```javascript
var num = 10; 
num = num + 10;

var num = 10; 
num += 10; 
```

- Multiply/assign (*=) 
- Divide/assign (/=) 

- Modulus/assign (%=) 

- Add/assign (+=) 

- Subtract/assign (-=) 

- Left shift/assign (<<=) 

- Signed right shift/assign (>>=) 

- Unsigned right shift/assign (>>>=) 

### 10. Comma Operator

The comma operator allows execution of more than one operation in a single statement,

```javascript
var num1=1, 
	num2=2, 
	num3=3; 
```

an also be used to assign values.When used in this way, the comma operator always returns the last item in the expression,

`var num = (5, 1, 4, 8, 0);  //num becomes 0 `

### 11. short circuiting

Since isColorRed function returns false, the is GreaterThan1400() function never runs.

```js
result = isColorRed("Black") && isGreaterThan1400(1401);

function isisColorRed(value){
  return value === "Red";
}
function isGreaterThan1400(value){
  return value > 1400;
}
```

`result = isColorRed("Red")||isGreaterThan1400(1401);`

when using the OR operator,only one expression needs to be true for the whole expression to be true.

## IV. Statements

### if 

```javascript
if (condition) statement1 else statement2 
```

```javascript
if (i > 25) {
  alert(“Greater than 25.”); 
} else if (i < 0) {
  alert(“Less than 0.”); 
} else {
  alert(“Between 0 and 25, inclusive.”); 
} 
```

### do-while 

post-test loop.后测试循环，the escape condition(出口条件) is evaluated(被测试) only after the code inside the loop has been executed. The body of the loop is always executed at least once before the expression is evaluated. 

do-while循环语句是一种后测试循环语句，即只有在循环体中的代码执行之后，才会测试出口条件。换句话说，在对条件表达式求值之前，循环体内的代码至少被执行一次。

```javascript
do{
循环体
}while(循环终止条件)
```

```javascript
do {
  statement 
} while (expression); 
```

```javascript
var i = 0; 
do {
  i += 2; 
} while (i < 10); 
//output 10
```

```javascript
var i = 0;
do {
  i += 2;
  document.write(i+'\n');
} while (i < 10);
//output 2 4 6 8 10
```

### while

pretest loop.前测试循环 This means the escape condition is evaluated before the code inside the loop has been executed. <mark>it is possible that the body of the loop is never executed.</mark>

`while`循环重复执行一段代码，直到某个条件不再满足。

`while`语句属于前测试循环语句，也就是说，在循环体内的代码被执行之前，就会对出口的条件求值。因此，循环体内的代码有可能永远不会被执行。

![while.png](http://ww1.sinaimg.cn/large/005NUwyggy1ga4ifqu7zej308f0b574b.jpg)

以下是`while`语句的语法：

```javascript
while(循环终止条件){
  循环体
}
```

```javascript
while(expression) statement
```

```javascript
var i = 0; 
while (i < 10) {
  i += 2; 
  document.write(i+'\n');
} 
//output 2 4 6 8 10
```

### For/of

iterates over values in array/string

The for statement is also a pretest loop with the added capabilities of variable initialization before entering the loop and defining postloop code to be executed. 具有在执行循环之前初始化变量和定义循环后要执行的代码的能力.If the body is executed, the postloop expression is also executed, iterating the variable i. i的值会被迭代，不断更新

![for.png](http://ww1.sinaimg.cn/large/005NUwyggy1ga4i4ijnpnj308g0ay3yk.jpg)

```js
    let _products = [
      {
        "productID": 680,
        "name": "HL Road Frame - Black, 58",
        "productNumber": "FR-R92B-58",
        "color": "Black",
        "standardCost": 1059.31,
        "listPrice": 1431.50
      },
      {
        "productID": 707,
        "name": "Sport-100 Helmet, Red",
        "productNumber": "HL-U509-R",
        "color": "Red",
        "standardCost": 13.08,
        "listPrice": 34.99
      },
      {
        "productID": 709,
        "name": "Mountain Bike Socks, M",
        "productNumber": "SO-B909-M",
        "color": "White",
        "standardCost": 3.3963,
        "listPrice": 9.50
      }
    ];
    
// Using a for/of loop
    function forofSample() {
      for (const item of _products) {
        console.log(JSON.stringify(item));
      }
    }

    // Looping over a string
    function loopStringSample() {
      let productName = "HL Road Frame - Black, 58";
      let letters = "";

      for (const char of productName) {
        letters += char;
      }
      console.log(letters);
    }
```

```javascript
for (initialization; expression; post-loop-expression) statement 
```

- 在该循环结构中，当条件成立时，执行语句1，否则跳出循环体。
- for语句的基本语法如下：

```javascript
for (循环变量初始化; 循环终止条件; 增量) {
    循环体;
}
```

```javascript
for(var i = 1; i<=10; i++){
    console.log('学员' + i + '号。');
}
```

```js
var longString = "";
// 创建一个 for 循环使 longString 包含六个 A，比如"AAAAAA"

for (var i=0;i<6;i++){
  longString = longString + "A";
}
console.log(longString)
```

首先`i=1`叫做初始条件，也就是说从哪里开始，特别的，我们的例子是从`i=1`开始的。出现在第一个分号后面的`i<=10`表示循环终止条件，每次循环都会先判断这个条件是否满足，如果满足则继续循环，否则停止循环，继续执行`for`循环后面的代码。你可能想问了，我们设定了`i=0`，岂不是永远都小于等于10吗？来看第三个部分。最后的`i++`表示让`i`在自身的基础上加`1`，这是每次循环后的动作。也就是说，每次循环结束时，`i`都会比原来大`1`，执行若干次循环之后，`i<=10`的条件就不满足了，这时循环结束。for循环后面的代码将得到执行。

```javascript
var count = 10; 
for (var i=0; i < count; i++){
  alert(i); 
} 
//output 0123456789
//This for loop is the same as the following: 
var count = 10; 
var i = 0; while (i < count){
  alert(i);
  i++; 
} 
```
```javascript
const prepareTea = () => 'greenTea';

const getTea = (numOfCups) => {
    const teaCups = [];

    for (let cups = 1; cups <= numOfCups; cups += 1) {
        const teaCup = prepareTea();
        teaCups.push(teaCup);
    }

    return teaCups;
};

const tea4TeamFCC = getTea(40);

console.log(tea4TeamFCC);
```

### For-in

The for-in statement is a strict iterative statement.

the 'in' keyword grabs all the property and method names from object

iterates over elements of object.

```javascript
for (property 变量 in expression 对象) statement 
```

```javascript
var a = ["Q","W","E"];
var n = '';
for (n in a){
  document.write(a[n]+"\n");
}
//用来遍历数组，按顺序把数组里的每个元素都访问一遍 QWE
```

```js
    // Using a for/in loop
    function forinSample() {
      let product = {
        "productID": 680,
        "name": "HL Road Frame - Black, 58",
        "productNumber": "FR-R92B-58",
        "color": "Black",
        "standardCost": 1059.31,
        "listPrice": 1431.50,
        calculateGrossProfit: function () {
          return this.listPrice - this.standardCost;
        }
      };

      for (const key in product) {
        console.log("'" + key + "'=" + product[key]);
      }
    }
```

### Labeled

defined a location to goto,no recommended for use

```javascript
//label: statement 
start: for (var i=0; i < count; i++) {alert(i); } 
```

```js
    // Use of a label.
    // NOTE: I don't recommend use of labels as this leads to spaghetti code
    function labelSample() {
      even:
      for (let index = 1; index <= 10; index++) {
        if (index % 2 == 1) {
          continue even;
        }
        console.log(index);
      }
    }
```

### Break and continue

The break and continue statements provide stricter control over the execution of code in a loop. 

The <mark>break statement</mark> exits the loop immediately, forcing execution to continue with the next statement after the loop.leave a loop early

The <mark>continue statement</mark>, on the other hand, exits the loop immediately, but execution continues from the top of the loop. next iteration of a loop.

continue will let you go back up to the top of the loop and continue with the next iteration, bypassing any code below the continue.

```javascript
var num = 0;
for (var i=1; i < 10; i++) {
  if (i % 5 == 0) {//能被5整除的都不要，都skip,if one matched , it break out the loop immediately
    break;
  }
  num++; 
  console.log(num); 
}
//num = 1 2 3 4

var num = 0;
for (var i=1; i < 10; i++) {
  if (i % 5 == 0) {//能被5整除的都不要，略过，但是继续遍历，留下不能被整除的
    continue;
  }
  num++; 
  console.log(num); 
}
//1,2,3,4,5,6,7,8,
```

```js
for (var i = 0; i < 6; i++) {
  if (i === 3) {
    continue;
  }
  console.log(i);
}
// -> 0
// -> 1
// -> 2
// -> 4
// -> 5
```

### With

```
with (expression) statement; 
```

### switch

```javascript
switch (expression)  {
  case value: statement
  break;
  case value: statement
  break;
  case value: statement
  break;
  case value: statement
  break;
  default: statement 
  //if no other statements matched
}
```

```javascript
var text;
var fruits = document.getElementById("myInput").value;

switch(fruits) {
  case "Banana":
    text = "Banana is good!";
    break;
  case "Orange":
    text = "I am not a fan of orange.";
    break;
  case "Apple":
    text = "How you like them apples?";
    break;
  default:
    text = "I have never heard of that fruit...";
}

switch (i) {
  case 25: alert(“25”);
    break;
  case 35: alert(“35”);
    break;
  case 45: alert(“45”);
    break;
  default: alert(“Other”); 
} 
//The equivalent switch statement is as follows: 

if (i == 25){
    alert(“25”); 
} else if (i == 35) {
    alert(“35”); 
} else if (i == 45) {
    alert(“45”); 
} else {
    alert(“Other”); 
}
```

```javascript
switch (i) {
    case 25: /* falls through */
    case 35: alert(“25 or 35”);
        break;
    case 45: alert(“45”);
        break;
    //以上都不成立则执行default代码
    default: alert(“Other”); 
} 
```

```javascript
switch (“hello world”) {
    case “hello” + “ world”: alert(“Greeting was found.”);
        break;
    case “goodbye”: alert(“Closing was found.”);
        break;
    default: alert(“Unexpected message was found.”); 
} 
```

The expression passed into the switch statement is true, because each case is a conditional that will return a Boolean value. Each case is evaluated, in order, until a match is found or until the default statement is encountered.

```javascript
var num = 25; 
switch (true) {
    case num < 0: alert(“Less than 0.”);
        break;
    case num >= 0 && num <= 10: alert(“Between 0 and 10.”);
        break;
    case num > 10 && num <= 20: alert(“Between 10 and 20.”);
        break;
    default: alert(“More than 20.”); 
} 
```

## V. Functions

a function is a block of organized ,reusable code that is used to perform a single , related action.

by default, all function return a value, in below example, the return value is undefined.

### basic syntax

```javascript
//basic syntax

function functionName(arg0, arg1,...,argN) {
 statements
}

function sayHi(name, message) {
 alert(“Hello “ + name + “, “ + message);
}

sayHi("Nicholas", “how are you today?”);
// “Hello Nicholas, how are you today?”

//Any function can return a value at any time by using the return statement followed by the value to return.
//任何函数，任何时候都可以通过return 语句后跟要返回的值来实现返回值。

function sum(num1, num2) {
 return num1 + num2;
}

// any code that comes after a return statement will never be executed
function sum(num1, num2) {
 return num1 + num2;
 alert(“Hello world”); //never executed
}

// possible to have more than one return statement in a function
function diff(num1, num2) {
 if (num1 < num2) {
 return num2 - num1;
 } else {
 return num1 - num2;
 }
}

//return statement can be used without specifying a return value
//the function stops executing immediately and returns undefined as its value

function sayHi(name, message) {
 return;
 alert(“Hello “ + name + “, “ + message); //never called
}
```

Argument:

an argument is a value that we pass to the function when we invoke it.（实参

Parameter:

a parameter is variable that we list as part of a function definition（形参

```js
//it takes two parameters num1 and num2
function sum(num1, num2) {
 return num1 + num2;
}

let result = sum(2,3);
console.log(result);
```

Strict mode places several restrictions on functions:

- No function can be named eval or arguments. 
- No named parameter can be named eval or arguments. 
- No two named parameters can have the same name. 

###  arguments object

an arguments object that can be accessed while inside a function to retrieve the values of each argument that was passed in.类数组，但也不是数组，因为有length property 实参的集合

-  arguments object acts like an array (though it isn’t an instance of Array) 
- can  access each argument using bracket notation (the first argument is arguments[0])

```javascript
function sayHi() {
    alert(“Hello “ + arguments[0] + “, “ + arguments[1]);
}

function printAll(){
  for(let i = 0 ; i<arguments.length;i++){
console.log(argument[i]);
  }
}

printAll(1,2,3,4,5);
```

###  length property

be used to check the number of arguments passed into the function 

```javascript
function howManyArgs() {
 alert(arguments.length);
}
howManyArgs(“string”, 45); //2
howManyArgs(); //0
howManyArgs(12); //1
```

arguments object can be used  in conjunction with named arguments

```javascript
function doAdd(num1, num2) {
 if(arguments.length == 1) {
 alert(num1 + 10);
 } else if (arguments.length == 2) {
 alert(arguments[0] + num2);
 }
}
```

Another thing to keep in mind: if only one argument is passed in, then setting arguments[1] to a value will not be refl ected by the named argument. 

Any named argument that is not passed into the function is automatically assigned the value undefined

<mark>Strict mode makes several changes to how the arguments object can be used.p82</mark>

### no overloading

覆盖，定义了两个相同名字的函数，则改名字只属于后定义的函数。overload,overwritten

```javascript
function addSomeNumber(num){
  return num + 100; 
}function addSomeNumber(num) {
  return num + 200; 
}
var result = addSomeNumber(100);    //300 
```

### function context

```js
function sayHi(){
console.log('Hi');
console.log(this);
}

sayHi();
//Hi
//window{...}

let greeting = {};
greeting.sayHi = funciton(){
  console.log('Hi');
  cosole.log(this);
}
//excution context in this function is diff
greeting.sayHi();
//Hi
//{sayHi:f}

function sayHi(){
console.log('Hi');
console.log(this);
}

let greeting = new sayHi();
//Hi
//[obj object]

```



# Chapter 4 : Variable, Scope, and Memory

变量，作用域，内存。

## I. Primitive and reference values

基本类型：简单的数据段

5种基本数据类型(in chapter 3):undefined , null , boolean , number , string

引用类型：指那些可能由多个值构成的对象。array,function, object

实际上是在操作对象的引用而不是实际的对象，引用类型的值是按引用访问的

### a. dynamic properties

Work for reference values

```javascript
//can add, change, or delete properties and methods at any time.
var person = new Object(); 
person.name = "Nicholas"; 
alert(person.name);    //"Nicholas" 

//Primitive values can’t have properties added to them
var name = "Nicholas"; 
name.age = 27; 
alert(name.age);    //undefined 
```

### b. copying values

#### for primitive values

```javascript
// Each of these variables can now be used separately with no side effects. 
var num1 = 5; 
var num2 = num1; 

++num1;
console.log(a,b);
//return 10 , 5
```

#### for reference values

```javascript
var obj1 = new Object(); 
var obj2 = obj1; 
obj1.name = "Nicholas"; 
alert(obj2.name);    //"Nicholas" 
```

### c. Argument Passing 

<mark>All arguments in ECMAScript are passed by value. It is not possible to pass arguments by reference.所有参数传递的都是值，都是按值传递，不可能通过引用传递参数，但访问变量有按值和按引用两种方式</mark>

按值传递：将函数外部的值复制给函数内部的参数，就把值从一个变量，复制到另一个变量一样。引用类型值的传递，则如同引用类型变量的复制一样。P69-70

在向参数传递基本类型的值时，被传递的值会被复制给一个局部变量（argument）

在向参数传递引用类型的值时，会把这个值在内存中的地址复制给一个局部变量，因此这个局部变量的变化会反映在函数的外部。

https://blog.fundebug.com/2017/08/09/explain_value_reference_in_js/

```javascript
function addTen(num) {
  //num 是局部变量
  num += 10;
  return num; 
}
var count = 20; 
var result = addTen(count); 
alert(count);    //20 - no change 
alert(result);   //30 
```

### d. determining type 

检测类型 

#### typeof operator

the best way to determine if a variable is a string, number, Boolean, or undefined. If the value is an object or null, then typeof returns “object”

```javascript
var s = "Nicholas"; 
var b = true; 
var i = 22; 
var u; 
var n = null; 
var o = new Object();
alert(typeof s);   //string 
alert(typeof i);   //number 
alert(typeof b);   //boolean 
alert(typeof u);   //undefined 
alert(typeof n);   //object 
alert(typeof o);   //object 
```

#### instanceof operator

syntax: result = variable instanceof constructor 

`instanceof`allows you to compare an object to a constructor, returning `true`or `false`based on whether or not that object was created with the constructor.

 Since the `constructor` property can be overwritten (which will be covered in the next two challenges) it’s generally better to use the `instanceof` method to check the type of an object. 

```javascript
let Bird = function(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 2;
}

let crow = new Bird("Alexis", "black");

crow instanceof Bird; // => true

let canary = {
  name: "Mildred",
  color: "Yellow",
  numLegs: 2
};

canary instanceof Bird; // => false

alert(person instanceof Object);   
//is the variable person an Object? 
alert(colors instanceof Array);    
//is the variable colors an Array? 
alert(pattern instanceof RegExp);  
//is the variable pattern a RegExp? 
```

## II. Execution content and scope

全局执行环境是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

当代码在一个环境中执行时候，会创建变量对象的一个作用域链。作用域链的作用，保证对执行环境有权访问的所有变量和函数的有序访问。

#### block-level scopes 

块级作用域

初始化变量没有使用var/let声明，该变量会自动被添加到全局环境。

sum变量在函数外部是访问不到的，如果省var，则可运行成功。

```javascript
function add(num1, num2) {
var sum = num1 + num2;
  return sum; 
}
var result = add(10, 20);  //30 
alert(sum);                
//causes an error since sum is not a valid variable 
```

会向上逐级查询与给定名字匹配的标识符，indentifier,找到即停止。

```javascript
var color = "blue";
function getColor(){
  var color = "red";
  return color; }
alert(getColor());  //”red” 

function greeting(){
  let message = 'hello';
  let sayHi = function hi(){
    message = 'hi';
  };
  sayHi();
  console.log(message);//hi
}
greeting();

function greeting(){
  let message = 'hello';
  let sayHi = function hi(){
    let message = 'hi';
  };
  sayHi();
  console.log(message);//hello
}
greeting();

//let const 块级作用域
```

## III. Garbage collection

# Chapter 5 : Reference Types

## I. object

### Create object

1. new操作符创建object,new operator,构造函数

use the new operator with the Object constructor

```javascript
//var person = new Object(); 
var person = {}; 
person.name = "Nicholas"; 
person.age = 29; 

var person = {};   //same as new Object() 
person.name = "Nicholas"; 
person.age = 29; //odd
```

2. 对象字面量表示法 Object literal notation 

```javascript
var person = {
  name : "Nicholas",
  age : 29 //注意这里没有逗号
}; 
```

```javascript
var person = {
  “name” : "Nicholas",
  “age” : 29,
  5: true 
};
//JSON
```

The best approach is to use named arguments for those that are required and an object literal to encompass multiple optional arguments. 

1. 构造函数；

​    `var _obj = new Object();`

2. 通过Object.create()方法初始化对象；

​    `var _o = {};`

​    `var _obj = Object.create(_o);`

3. 对象字面量

​    `var _obj = {}`

4. symbol

   we can set custom info only we can access to.

   ```js
   let mySymbol = Symbol();
   let person = {
     name:"jack",
     age:24,
     [mySymbol]:"secretInfomation"
   }
   ```

   

### access object properties

1. dot notation
2. bracket notation
```javascript
alert(person[“name”]);    //"Nicholas" 
alert(person.name);       //"Nicholas" 
person[“first name”] = "Nicholas"; 
```

3. Access Properties with Variables

```js
var prop = 'foo';
var obj = { foo: "bar", foo1: 123 };

console.log(obj[prop]);
// -> "bar"
console.log(obj[prop + 1]);
// -> 123

var car = {
  brand: "Toyota",
  speed: 0,
  acceleration: 2,
  "year of manufacture": 2016
};
// 修改下面一行
var prop = 'acceleration';
var acc = car[prop];
console.log(acc);
// -> 2
```



## II. array

### create array

1. Array constructor

```javascript
var colors = new Array(); 
var colors = new Array(3);
// var colors = [];
//create an array with three items 
var names = new Array("Greg");  
//create an array with one item, the string "Greg" 
var colors = Array(3);      
var names = Array("Greg"); 
```

2.  array literal notation

```javascript
var colors = ["red", "blue", "green"]; //creates an array with three strings 
var names = [];                        //creates an empty 
array var values = [1,2,];                   //AVOID! Creates an array with 2 or 3 items 
//containing the values 1, 2, and undefined n Internet Explorer 8 and earlier
var options = [,,,,,];                 
//AVOID! creates an array with 5 or 6 items 
```

### access array values

```javascript
var colors = ["red", "blue", "green"];           //define an array of strings 
alert(colors[0]);                                //display the first item "red"
colors[2] = “black”;                             //change the third item 
colors[3] = “brown”;                             //add a fourth item 

//length 属性不是只读的，可以修改数组的value
var colors = ["red", "blue", "green"];    //creates an array with three strings 
var names = [];                           //creates an empty array
alert(colors.length);    //3 
alert(names.length);     //0 

var colors = ["red", "blue", "green"];    //creates an array with three strings 
colors.length = 2; 
//Setting the length to 2 removes the last item
alert(colors[2]);        //undefined 

var colors = ["red", "blue", "green"];    //creates an array with three strings 
colors.length = 4; 
alert(colors[3]);        //undefined 

var colors = ["red", "blue", "green"];    //creates an array with three strings 
colors[colors.length] = “black”;          
//add a color (position 3) 
colors[colors.length] = “brown”;          
//add another color (position 4) 

var colors = ["red", "blue", "green"];    //creates an array with three strings 
colors[99] = “black”;                     
//add a color (position 99) 
alert(colors.length);  //100 
```

### detecting array

isArray() method

```javascript
if (Array.isArray(value)){
  //do something on the array 
} 
```

### Conversion methods

all objects have toLocaleString( ), toString( ), and valueOf( ) methods.toString( ):数组返回字符串，valueOf( )转换数组而返还的是数组。

```javascript
var colors = ["red", "blue", "green"];    //creates an array with three strings 
alert(colors.toString());    //red,blue,green 
alert(colors.valueOf());     //red,blue,green 
alert(colors);               //red,blue,green 

//toString() behind the scenes to get the same result as when toString() is called directly.
```

```javascript
//The join() method accepts one argument, which is the string separator to use, and returns a string containing all items

var colors = ["red", "green", "blue"]; alert(colors.join(“,”));   //red,green,blue 
alert(colors.join(“||”));  //red||green||blue 
```

### stack methods

An array object can act just like a stack, which is one of a group of data structures that restrict the insertion and removal of items. A stack is referred to as a last-in-first-out (LIFO) structure, meaning that the most recently added item is the fi rst one removed. 

#### pop() removal

#### push() insertion

### queue methods 

队列方法

queues restrict access in a first-in-first-out (FIFO) data structure. 

#### shift()

#### unshift()

### reodering methods

#### reverse()

反转数组顺序

#### sort()

升序序列排序数组

```javascript
//avoid
var values = [0, 1, 5, 10, 15]; 
values.sort(); 
alert(values);    //0,1,10,15,5 
```

```javascript
function compare(value1, value2) {
  if (value1 < value2) {
    return 1;
  } else if (value1 > value2) {
    return -1;
  } else {
    return 0;
  } 
}
var values = [0, 1, 5, 10, 15]; values.sort(compare); alert(values);    //15,10,5,1,0 


function compare(value1, value2) {
  if (value1 < value2) {
    return -1;
  } else if (value1 > value2) {
    return 1;
  } else {
    return 0;
  } 
} 

function compare(value1, value2){
  return value2 - value1; 
} 
//升序排列
```

### manipulation methods

#### concat()

#### splice()

### location methods

#### indexOf()

#### lastIndexOf()

### iterative methods

#### every()

Runs the given function on every item in the array and returns true if the function returns true for every item. 

#### filter()

Runs the given function on every item in the array and returns an array of all items for which the function returns true. 

#### forEach()

Runs the given function on every item in the array. This method has no return value. 

#### map()

Runs the given function on every item in the array and returns the result of each function call in an array. 

#### some()

Runs the given function on every item in the array and returns true if the function returns true for any one item. 

### reduction methods

#### reduce()

#### reduceRight()

## III. data

```javascript
//returns the millisecond representation of the date and time at which the method is executed.返回表示调用这个方法时的日期和时间的毫秒数
//get start time 
var start = Date.now(); 
//call a function 
doSomething(); 
//get stop time 
var stop = Date.now(),
    result = stop – start; 
```

### Date-Formatting Methods 

1. toDateString() — Displays the date’s day of the week, month, day of the month, and year in an implementation-specific format. 
2. toTimeString() — Displays the date’s hours, minutes, seconds, and time zone in an implementation-specifi c format. 
3. toLocaleDateString() — Displays the date’s day of the week, month, day of the month, and year in an implementation- and locale-specifi c format. 
4. toLocaleTimeString() — Displays the date’s hours, minutes, and seconds in an implementation-specifi c format. 
5. toUTCString() — Displays the complete UTC date in an implementation-specifi c format.
### Date/Time Component Methods p102

## IV. RegExp

### RegExp Instance Properties

1. g — Indicates global mode, meaning the pattern will be applied to all of the string instead of stopping after the fi rst match is found. 

2. i — ignorecase Indicates case-insensitive mode, meaning the case of the pattern and the string are ignored when determining matches. 

3. m — Indicates multiline mode, meaning the pattern will continue looking for matches after reaching the end of one line of text. 

## V. function

All Functions are Methods

In JavaScript all functions are object methods.

If a function is not a method of a JavaScript object, it is a function of the global object

```javascript
function sum(num1, num2){
  return num1 + num2; 
}        
alert(sum(10,10));    //20
var anotherSum = sum;        
alert(anotherSum(10,10));  //20
sum = null;  //即使设置null值还是可以调用函数      
alert(anotherSum(10,10));  //20 
//Note that using the function name without parentheses( ) accesses the function pointer instead of executing the function.不是调用函数，访问函数指针
```

```javascript
function sayName(name){
    alert(name); 
}      
function sum(num1, num2)
return num1 + num2; 
}
function sayHi(){
    alert(“hi”); 
}
alert(sayName.length);  //1 
alert(sum.length);      //2 
alert(sayHi.length);    //0 
```

**严格模式下，未指定环境对象而调用函数，则this值不会转为windows,除非明确把函数添加到某个对象或者调用call()/apply(),否则，this 的值会是undefined**

call(),在使用call()方法时，传递给函数的参数必须逐个列举出来

```javascript
function sum(num1, num2){
    return num1 + num2; 
}
function callSum(num1, num2){
    return sum.call(this, num1, num2); 
}
alert(callSum(10,10));   //20 
```

<mark>使用call()/apply()主要用于扩充函数运行的作用域</mark>

```javascript
window.color = "red"; 
var o = { color: "blue" };
function sayColor(){
    alert(this.color); 
}
sayColor();            //red
sayColor.call(this);   //red this指向windows.color
sayColor.call(window); //red 指向windows.color
sayColor.call(o);      //blue this指向了O
```

```js
let person1 = {name:'john',age:22}
let person2 = {name:"Mary",age:26}
let sayHi = function(){
console.log('Hi,'+this.name)
}

sayHi.call(person1) // Hi, john
sayHi.call(person2)//Hi, mary

let person1 = {name:'john',age:22}
let sayHi = function(message){
  console.log(message + ', ' + this.name);
}
//add additional parameter
sayHi.call(person1,'Hi')
//Hi, Jhon
```

```js
function introduction(name,profession){
console.log('My name is ' + name + 'and I am a ' + profession + ' .');
  console.log(this);
}

introduction('john','student');
introduction.apply(undefined,["marry" , 'Lawyer']);
introduction.call(undefined,["james" , 'artist']);

```

Apply vs call

apply():array input with similar elements;

call():individual arguments of varying type



bind():make a opy of funciton , and then change the value of it.

```javascript
window.color = "red"; 
var o = { color: "blue" };
function sayColor(){
    alert(this.color); 
} 
var objectSayColor = sayColor.bind(o); 
objectSayColor();   //blue 
```

### return

任何函数在任何时候都可以通过return语句否跟要返回的值来实现返回值。这个add函数的作用是把两个参数求和并将该值返回。除了return语句外，没有任何声明表示该函数会返回一个值。最终的结果将会弹出8。这里可以注意到，我们需要用一个变量(result)来接收add(3,5)返回的值，这是因为我们在add()函数内部将结果返回(return)了出来，如果不用变量接收，将无法对该结果进行操作。

```javascript
function add(num1, num2){
    return num1 + num2;
}

var result = add(3, 5);
alert(result); // 8
```



## VI. primitive wrapper types

基本包装类型，与引用类型相似，同时也具备基本类型相应的特殊行为。Boolean，Number, String,

the Boolean type, the Number type, and the String type. These types can act like the other reference types 

### a. Boolean

It’s very important to understand the difference between a primitive Boolean value and a Boolean object — it is recommended to never use the latter. 

`var booleanObject = new Boolean(true); `

### b. Number

Similar to the Boolean object, the Number object gives important functionality to numeric values but really should not be instantiated directly because of the same potential problems. 

`var numberObject = new Number(10);`

### c. String

#### charAt()

```javascript
var stringValue = “hello world”; 
alert(stringValue.length);   //”11” 

var stringValue = “hello world”; 
alert(stringValue.charAt(1));   //”e” 

var stringValue = “hello world”; 
alert(stringValue[1]);   //”e” 

```

#### charCodeAt()

输出字符编码

```javascript
var stringValue = “hello world”; 
alert(stringValue.charAt(1));   //”e” 
```

#### String-Manipulation Methods

concat()

slice()

substr()

substring()

indexOf()

lastIndexOf()

trim()

toLowerCase(), toLocaleLowerCase(), toUpperCase(), and toLocaleUpperCase(). 

match()

search()

localeCompare()

fromCharCode()

## VII. singleton built-in objects

### the global object

URI-Encoding Methods

eval()

Window Object 

### the math object

Math.ceil(), Math.floor(), and Math.round()

min()

max()

# Chapter 6 :OBJECTS, CLASSES, AND OBJECT-ORIENTED 

## I. understanding objects

### a. 属性类型

个人理解：镶嵌在object上的attribute，and property，只能用defineproperty()创建，和访问。

attribute:特性，property:属性

Object.defineProperty( )

name,age,job→property

sayName()→method

nicholas,29,software engineer→Value

```javascript
var person = {
  name: "Nicholas",
  age: 29,
  job: "Software Engineer",
  
  sayName: function(){
    alert(this.name);
  }
};

let dog = {
  name: "Spot",
  numLegs: 4,
  sayLegs: function() {return "This dog has " + dog.numLegs + " legs.";}
};

dog.sayLegs();
```

1. 数据属性 data property

   4 attributes:

   [[Configurable]]，能否delete属性，默认false,当且仅当该属性的 configurable 为 true 时，该属性`描述符`才能够被改变

   [[Enumerable]]，能否for-in,默认false

   [[Writable]]，能否修改属性值,默认false

   [[Value]]，包含这个属性的数据值，默认值undefined

   ![Xnip2019-10-08_22-03-26.png](http://ww1.sinaimg.cn/large/005NUwygly1g7r5bm7oq5j30iw0a80ua.jpg)

   To change any of the default property attributes, you must use the ECMAScript 5 Object .defineProperty() method.属性不能直接定义，必须通过Object .defineProperty() 

```javascript
//修改默认属性
var person = {};
Object.defineProperty(person, "name", {
  writable: false, //默认的值可以省略不写
  value: "Nicholas"
});
alert(person.name); //"Nicholas"
person.name = "Greg";
alert(person.name); //"Nicholas"

```

2. 访问器属性 Accessor Properties 

   不包含数据值，包含getter,setter函数，不是必须的。

   getter,读取访问器属性时调用，返回有效的值

   setter,传入新的写入访问器属性的值，负责决定如何处理数据

   4 attribute:

   Configurable,默认true

   Enumerable,默认true

   Get,默认undefined

   Set,默认undefined

   when setting a property value results in some other changes to occur. 

   underscore on _year is a common notation to indicate that a property is not intended to be accessed 

   from outside of the object’s methods. 

```javascript
var book = {
  _year: 2004,
  edition: 1
};
// legacy accessor support
book.__defineGetter__("year", function () {
  return this._year;
});
book.__defineSetter__("year", function (newValue) {
  if (newValue > 2004) {
    this._year = newValue;
    this.edition += newValue - 2004;
  }
});
book.year = 2005;
alert(book.edition); // 2

```

```js
let person = {
  name_: "",
  get name() {
    return this.name_;
  },
  set name(name) {
    this.name_ = name;
  },
  sayName() {
    console.log(`My name is ${this.name_}`);
  }
};
```

```javascript
var book = {
  _year: 2004,
  edition: 1
};
Object.defineProperty(book, "year", {
  get: function () {
    return this._year;
  },
  set: function (newValue) {
    if (newValue > 2004) {
      this._year = newValue;
      this.edition += newValue - 2004;
    }
  }
});
book.year = 2005;
alert(book.edition); // 2

```

### b. 定义多个属性

Object.defineProperties()

```javascript
var book = {};
Object.defineProperties(book, {
  _year: {
    value: 2004
  },
  edition: {
    value: 1
  },
  year: {
    get: function () {
      return this._year;
    },
    set: function (newValue) {
      if (newValue > 2004) {
        this._year = newValue;
        this.edition += newValue - 2004;
      }
    }
  }
});

```

### c. 读取属性的特性

Reading Property Attributes 

`Object.getOwnPropertyDescriptor()`

search own property

hasOwnProperty(),判定对象是否包含指定名称的属性，不会向原型链搜索。

```javascript
function Bird(name) {
  this.name = name;
  this.numLegs = 2;
}

let canary = new Bird("Tweety");
let ownProps = [];
// Add your code below this line
for (let property in canary) {
  if (canary.hasOwnProperty(property)) {
    ownProps.push(property);
  }
}

console.log(ownProps); //prints [ "name", "numLegs" ]

```

## II. Object creation

### a. singleton pattern

单例模式 

```js
var person = new Object();

person.name = "heather";
person.age = 29;
person.job = "manager";
person.sayName = function () {
  alert(this.name);
};

//以上的模式成为对象字面两创建的首选模式
var person = {
  name: "heather",
  age: 29,
  job: "manager",
  sayName: function () {
    alert(this.name);
  }
};

```

### b. factory pattern

工厂模式

```javascript
function createPerson(name, age, job) {
  var o = new Object();
  o.name = name;
  o.age = age;
  o.job = job;
  o.sayName = function () {
    alert(this.name);
  };
  return o;
}

var person1 = createPerson("Nicholas", 29, "Software Engineer");
var person2 = createPerson("Greg", 27, "Doctor");
```

### c. constructor pattern 
**构造函数模式**

`Constructors`are functions that create new objects. 

构造造函数是通过函数创建新对象。

Constructors constructor functions always begin with an uppercase letter, whereas non-constructor functions begin with a lower letter.构造函数始终以一个大写字母开头，非构造函数以小写字母开头。构造函数本身也是函数，只不过可以用来创建对象而已。

- **构造函数需要new操作符实例化才能使用**
- **构造函数没有return语句**
- **构造函数this指向调用者往往是调用构造函数的实例本身，而函数使用this则会指向window全局对象**
- **构造函数名首字母大写（非强制性的）**
- Constructors are defined with a capitalized name to distinguish them from other functions that are not `constructors`.
- Constructors use the keyword `this` to set properties of the object they will create. Inside the constructor, `this` refers to the new object it will create.
- Constructors define properties and behaviors instead of returning a value as other functions might.

要创建Person的新实例，必须使用new操作符，以这种方式调用的构造函数实际上会经历以下四步骤：

1. 创建一个新对象
2. 将构造函数的作用域赋给新对象(因此this指向了这个新对象)
3. 执行构造函数中的代码
4. <mark>返回新对象</mark>

不需要`return`也可以返回对象

```js
function show() {
  console.log(this);
}

console.log(show()); // undefined
console.log(new show()); // show()

```

```javascript
//This constructor defines a Bird object with properties name, color, and numLegs set to Albert, blue, and 2, respectively

//Use a Constructor to Create Objects
function Bird() {
  this.name = "Albert";
  this.color = "blue";
  this.numLegs = 2;
  // "this" inside the constructor always refers to the object being created
}

let blueBird = new Bird();
```


```javascript
function Person(name, age, job) {
  this.name = name;
  this.age = age;
  this.job = job;
  this.sayName = function () {
    alert(this.name);
  };
}
//创建Person的新实例，必须使用new操作符
var person1 = new Person("Nicholas", 29, "Software Engineer");
var person2 = new Person("Greg", 27, "Doctor");
alert(person1.sayName == person2.sayName); //false
//指向同一个构造函数Person
alert(person1.constructor == Person); //true
alert(person2.constructor == Person); //true

alert(person1 instanceof Object); //true
alert(person1 instanceof Person); //true
alert(person2 instanceof Object); //true
alert(person2 instanceof Person); //true
```

<mark>this example is considered to be both an instance of Object and an instance of Person</mark>

```javascript
function Person(name, age, job) {
  this.name = name;
  this.age = age;
  this.job = job;
  this.sayName = function () {
    alert(this.name);
  };
}
//用new的话则为构造函数，不用的话和普通函数没有区别
//use as a constructor
var person = new Person("Nicholas", 29, "Software Engineer");
person.sayName(); // "Nicholas"

//call as a function
Person("Greg", 27, "Doctor"); //adds to window
window.sayName(); // "Greg"

//call in the scope of another object在另一个对象的作用域中调用
var o = new Object();
Person.call(o, "Kristen", 25, "Nurse");
o.sayName(); // "Kristen"

// it’s called with a this value of the object o, which then gets assigned all of the properties and the sayName() method.

```

### d. Prototype pattern

**原型模式**

创建的每个函数都有一个prototype属性，（个人理解，每个函数有自己的基因，这个基因被称为prototype）这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法，如果按照字面意思来理解，那么prototype就是通过调用构造函数而创建的那个对象实例的原型对象。

使用原型对象的好处是可以让所有对象实例共享它所包含的属性和方法。换句话说，不必在构造函数中定义对象实例的信息，而是将信息直接添加到原型对象中。

This may not be an issue when there are only two instances, but imagine if there are millions of instances. That would be a lot of duplicated variables.

```javascript
function Person() {}
//构造函数成为空函数，将属性值添加在prototype属性中
Person.prototype.name = "Nicholas";
Person.prototype.age = 29;
Person.prototype.job = "Software Engineer";
Person.prototype.sayName = function () {
  console.log(this.name);
};

var person1 = new Person();
person1.sayName(); // "Nicholas"

var person2 = new Person();
person2.sayName(); // "Nicholas"

console.log(person1.sayName == person2.sayName); //true

// Person.prototype === person1.__proto__  -> true
console.log(11, Person.prototype);
console.log(33, person1.__proto__);
// 11 output
{
  age: 29,
  job: "Software Engineer",
  name: "Nicholas",
  sayName: ƒ()
};

console.log(22, Person.prototype.constructor); // ƒ Person() {}

```

```javascript
// 构造函数
function fn(){}

// prototype，原型
// output {constructor: ƒ}
console.log( fn.prototype )

// constructor，构造器
// output ƒ fn(){}
console.log( fn.prototype.constructor )

```

<mark>this example is considered to be both an instance of Object and an instance of Person</mark>

![QQ截图20191108113339.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8qhfte7dfj30ld0ahjrt.jpg)

![prototype chain.JPG](http://ww1.sinaimg.cn/large/005NUwygly1g8t0jo6zpwj316q0kyaen.jpg)

Whenever a property is accessed for reading on an object, a search is started to find a property with that name. The search begins on the object instance itself. If a property with the given name is found on the instance, then that value is returned; if the property is not found, then the search continues up the pointer to the prototype, and the prototype is searched for a property with the same name. If the property is found on the prototype, then that value is returned. 

==读取对象某个属性的时候搜索顺序从对象实例自身再到原型对象，找到即停止。==

不能通过对象实例修改原型对象中的值，实例对象和原型对象同名属性，修改实例对象会屏蔽原型中的那个属性。只会阻止访问原型中的属性，但原型属性不会被修改。

在已经创建了实例的情况下重写原型，会切断现有实例与新原型之间的联系。

```javascript
function Person() {}
Person.prototype.name = "Nicholas";
Person.prototype.age = 29;
Person.prototype.job = "Software Engineer";
Person.prototype.sayName = function () {
  alert(this.name);
};

var person1 = new Person();
var person2 = new Person();
person1.name = "Greg";

alert(person1.name); // "Greg" - from instance
alert(person2.name); // "Nicholas" - from prototype

```

hasOwnProperty(),判定对象是否包含指定名称的属性，不会向原型链搜索。

访问prototype会返回false,访问instance则会返回true

```javascript
function Person() {}
Person.prototype.name = "Nicholas";
Person.prototype.age = 29;
Person.prototype.job = "Software Engineer";
Person.prototype.sayName = function () {
  console.log(this.name);
};

var person1 = new Person();
var person2 = new Person();

console.log(person1.hasOwnProperty("name")); //false
person1.name = "Greg";
console.log(person1.name); // "Greg" - from instance
console.log(person1.hasOwnProperty("name")); //true

console.log(person2.name); // "Nicholas" - from prototype
console.log(person2.hasOwnProperty("name")); //false

delete person1.name;
console.log(person1.name); // "Nicholas" - from the prototype
console.log(person1.hasOwnProperty("name")); //false

```

<mark>简单写法</mark>

set the `prototype` to a new object that already contains the properties,

Person.prototype 被设置为等于一个通过对象字面量创建的新对象。最终结果是一样的， 只有一个问题：这样重写之后， ==Person.prototype 的 constructor 属性就不指向 Person== 了。在创建函数时，也会创建它的 prototype 对象同时会自动给这个原型的 constructor 属性赋 值。而上面的写法完全重写了默认的 prototype 对象，因此其 constructor 属性也指向了完全不同的新对象（Object 构造函数），不再指向原来的构造函数。虽然 instanceof 操作符还能可靠地返回值，但我们不能再依靠 constructor 属性来识别类型了

```javascript
// 简单写法的缺点 Person.prototype 的 constructor 属性就不指向 Person
function Person() {}
Person.prototype = {
  name: "jhon",
  age: 29,
  job: "writter",
  sayName: function () {
    console.log(this.name);
  }
};
console.log(22, Person.prototype.constructor); // ƒ Object() { [native code] }
// 如果要重新指向原来的原型
function Person() {}
Person.prototype = {
  constructor: Person,
  name: "Nicholas",
  age: 29,
  job: "Software Engineer",
  sayName() {
    console.log(this.name);
  }
};

```

每创建一个函数，就会同时创建他的prototype对象，这个对象也会自动获得constructor属性[[constructor]]。这个简单写法是对prototype对象的重写。

<mark>constructor属性是什么?</mark>

the `constructor`property is a reference to the constructor function that created the instance.

The advantage of the `constructor`property is that it's possible to check for this property to find out what kind of object it is. 

所以，constructor属性👉新对象的属性=object构造函数

constructor属性不👉Person函数

**Note**
Since the `constructor`property can be overwritten. it’s generally better to use the `instanceof`method to check the type of an object.

```javascript
var friend = new Person();
console.log(friend instanceof Object); //true
console.log(friend instanceof Person); //true
console.log(friend.constructor == Person); //false
console.log(friend.constructor == Object); //true
```

```javascript
function Dog(name) {
  this.name = name;
}

// Add your code below this line
function joinDogFraternity(candidate) {
  if (candidate.constructor === Dog) {
    return true;
  } else {
    return false;
  }
}

```

<mark>p156</mark>

<mark>crucial side effect </mark>

manually setting the `prototype`to a new object. It erased the `constructor`property!

```javascript
Bird.prototype = {
  constructor: Bird, // define the constructor property
  numLegs: 2,
  eat: function () {
    console.log("nom nom nom");
  },
  describe: function () {
    console.log("My name is " + this.name);
  }
};

```

### e. combination constructor/prototype pattern

组合使用(构造函数+原型模式)

这种方法是，属性写在构造里，方法写在原型里，可变的都放在构造函数里，传进来的东西都在构造函数里接收，不变的东西就放在原型里。

#### own properties and prototype properties

 `own`properties and `prototype`properties. `Own`properties are defined directly on the object instance itself. And `prototype`properties are defined on the `prototype`.

`name` and `numLegs` are called `own` properties, because they are defined directly on the instance object. That means that `duck` and `canary` each has its own separate copy of these properties. In fact every instance of `Bird` will have its own copy of these properties. The following code adds all of the `own` properties of `duck` to the array `ownProps`.(example 1)

```javascript
//example 1

function Bird(name) {
  this.name = name;
  this.numLegs = 2;
}

let duck = new Bird("Donald");
let canary = new Bird("Tweety");

let ownProps = [];

for (let property in duck) {
  if (duck.hasOwnProperty(property)) {
    ownProps.push(property);
  }
}

console.log(ownProps); // prints [ "name", "numLegs" ]

```

```javascript
function Bird(name) {
  this.name = name; //own property
}

Bird.prototype.numLegs = 2; // prototype property

let duck = new Bird("Donald");

let ownProps = [];
let prototypeProps = [];

for (let property in duck) {
  if (duck.hasOwnProperty(property)) {
    ownProps.push(property);
  } else {
    prototypeProps.push(property);
  }
}

console.log(ownProps); // prints ["name"]
console.log(prototypeProps); // prints ["numLegs"]

```

```javascript
//这种方法是，属性写在构造里，方法写在原型里，可变的都放在构造函数里，传进来的东西都在构造函数里接收，不变的东西就放在原型里。
function Person(name, age, job) {
  this.name = name;
  this.age = age;
  this.job = job;
  this.friends = ["Shelby", "Court"];
}
Person.prototype = {
  constructor: Person,
  sayName: function () {
    alert(this.name);
  }
};

function Person(name, age, job) {
  this.name = name;
  this.age = age;
  this.job = job;
  this.friends = ["Shelby", "Court"];
}
Person.prototype = function sayName() {
  alert(this.name);
};

var person1 = new Person("Nicholas", 29, "Software Engineer");
var person2 = new Person("Greg", 27, "Doctor");

person1.friends.push("Van");
console.log(person1.friends); //”Shelby,Court,Van”
console.log(person2.friends); //”Shelby,Court”
console.log(person1.friends === person2.friends); //false
console.log(person1.sayName === person2.sayName); //true

```

```javascript
function Dog(name) {
  this.name = name;
}

Dog.prototype.numLegs = 2;

let beagle = new Dog("Snoopy");    

beagle.numLegs // 2
```

### f. Dynamic Prototype Pattern

动态原型模式

将信息封装在构造函数中，通过在构造函数中初始化原型，保持构造函数和原型的优点

```javascript
function Person(name, age, job) {
  //properties
  this.name = name;
  this.age = age;
  this.job = job;
  //methods
  //在sayname()方法不存在的情况下，才会将它添加到原型中
  if (typeof this.sayName != "function") {
    Person.prototype.sayName = function () {
      alert(this.name);
    };
  }
}
var friend = new Person("Nicholas", 29, "Software Engineer");
friend.sayName();

```

### g. Parasitic Constructor Pattern 

寄生构造函数模式

建议不要使用这种模式

创建函数，封装创建对象代码，然后再返回新创建对象

寄生模式/稳妥函数模式创建的对象构造函数之间也没有什么关系，instanceof操作符对这种对象没有意义

```javascript
function SpecialArray() {
  //create the array
  var values = new Array();
  //add the values
  values.push.apply(values, arguments);
  //assign the method
  values.toPipedString = function () {
    return this.join(" | ");
  };
  //return it
  return values;
}

var colors = new SpecialArray("red", "blue", "green");
console.log(colors.toPipedString()); // ”red|blue|green”

```

### h. Durable Constructor Pattern

稳妥构造函数模式

适合在安全的环境中使用，禁止使用this，new，或放置数据被其他引用程序改动时使用。

```javascript
function Person(name, age, job) {
  //create the object to return
  var o = new Object();
  //optional: define private variables/functions here
  //attach methods
  o.sayName = function () {
    alert(name);
  };
  //return the object
  return o;
}

var friend = Person("Nicholas", 29, "Software Engineer");
friend.sayName(); // "Nicholas"

```

## III. inheritance

`isPrototypeOf()` 方法测试一个对象是否存在于另一个对象的原型链上,Understand Where an Object’s Prototype Comes From

```javascript
function Dog(name) {
  this.name = name;
}

let beagle = new Dog("Snoopy");

Dog.prototype.isPrototypeOf(beagle); // true
Object.prototype.isPrototypeOf(Dog.prototype); //true

function Bird(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 2;
}

let cardinal = new Bird("Bruce", "red");

```

```javascript
function Bird(name) {
  this.name = name;
}

let duck = new Bird("Donald");

Bird.prototype.isPrototypeOf(duck);
// returns true
// duck inherits its prototype from the Bird constructor function

```

some disadvantages when using this syntax for inheritance, which are too complex for the scope of this challenge. Instead, here's an alternative approach without those disadvantages

<mark>Object.create function</mark>

```javascript
//are too complex for the scope of this challenge
let animal = new Animal();

//better way to use
let animal = Object.create(Animal.prototype);
```

 `Object.create(obj)` creates a new object, and sets `obj` as the new object's `prototype`. Recall that the `prototype` is like the "recipe" for creating an object. By setting the `prototype` of `animal` to be `Animal's` `prototype`, you are effectively giving the `animal` instance the same "recipe" as any other instance of `Animal`. 

You’re right, this works. The difference is that this way, each object created by calling new Fn() will have its own version of print placed directly on the object. They’ll be distinct functions in memory. The problem with this is performance and memory usage.

1. inheriting behavior from the supertype (or parent) 

`Animal`: making a new instance of `Animal`. 

```javascript
const person = {
  isHuman: false,
  printIntroduction: function () {
    console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`);
  }
};
//因为需要继承的是整个对象，所以create(person)
const me = Object.create(person);

me.name = "Matthew"; // "name" is a property set on "me", but not on "person"
me.isHuman = true; // inherited properties can be overwritten

me.printIntroduction();
// expected output: "My name is Matthew. Am I human? true"

```

````javascript
function Animal() { }
Animal.prototype.eat = function() {
  console.log("nom nom nom");
};
//因为是将property设置在prototype中，所以是要继承prototype，所以写得Animal.prototype
let animal = Object.create(Animal.prototype);
//let animal = new Animal();

animal.eat(); // prints "nom nom nom"
animal instanceof Animal; // => true
````

```javascript
function Animal() { }

Animal.prototype = {
  constructor: Animal,
  eat: function() {
    console.log("nom nom nom");
  }
};

let duck = Object.create(Animal.prototype); 
let beagle = Object.create(Animal.prototype); 

duck.eat(); // Should print "nom nom nom"
beagle.eat(); // Should print "nom nom nom"

```

2. set the `prototype` of the subtype (or child)

 `Bird`—to be an instance of `Animal`.  the `prototype` is like the "recipe" for creating an object. In a way, the recipe for `Bird` now includes all the key "ingredients" from `Animal`  `duck` inherits all of `Animal`'s properties, including the `eat` method 

When you use `new` keyword, you are creating an instance/object from either a function constructor or a class constructor. In this case, it’s a function constructor. Then you get access to all the variables that are declared with `this` inside the function constructor. In this case Dog constructor inherits from Animal constructor and beagle is an instantiation of Dog constructor so beagle has access to all the methods and `this` values of Animal constructor. 

[Master JavaScript Prototypes & Inheritance]( https://codeburst.io/master-javascript-prototypes-inheritance-d0a9a5a75c4e?gi=584b76fbc46e )

```javascript
function Animal() {}

Animal.prototype = {
  constructor: Animal,
  eat: function () {
    console.log("nom nom nom");
  }
};

function Dog() {}

Dog.prototype = Object.create(Animal.prototype);

let beagle = new Dog();
beagle.eat();

// Should print "nom nom nom"

```

<mark>不理解第一种方法和第二种方法的区别</mark>

个人理解：

1.第一种方法没有先创建对象，而是直接继承

2.第二种方法先创建了对象，然后设置prototype

![prototype chain.JPG](http://ww1.sinaimg.cn/large/005NUwygly1g8t0jo6zpwj316q0kyaen.jpg)

subtype inherit from supertype,constructor指向supertype,subtype 用继承创造的实例他的constructor也会指向supertype,但是，对象的实例中constructor属性应该指向创造的对象（即生出她们的父母），所以要修改constructor。

```javascript
function Bird() {}
Bird.prototype = Object.create(Animal.prototype);
let duck = new Bird();
duck.constructor; // function Animal(){...}
//对象的实例中constructor属性应该指向创造的对象（即生出她们的父母）

//修改constructor
Bird.prototype.constructor = Bird;
duck.constructor; // function Bird(){...}

```

```javascript
function Animal() {}
function Bird() {}
function Dog() {}

Bird.prototype = Object.create(Animal.prototype);
Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.constructor = Dog;
Bird.prototype.constructor = Bird;

let duck = new Bird();
let beagle = new Dog();

```

OO支持两种继承方式：接口继承，实现继承

接口继承只继承方法签名，实现继承则继承实际的方法。

ECMAScript,只有实现继承，并通过原型链才能实现。

**1. JavaScript中一切皆是对象**
**2. 所有对象有[[prototype]] / `__proto__`属性，指向其构造函数的原型对象**
**3. 所有函数都有prototype属性，指向其原型对象**
**4. 所有实例都有constructor属性，指向其构造函数**

### prototype chaining

**原型链（构造函数，原型，实例的关系）**

每个构造函数都有一个原型对象，原型有一个属性指回构造函数，而实例有一个内部指针指向原型。这样就在实例和原型之间构造了一条原型链。

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7s351qy4lj30wq0ksgo3.jpg" alt="image.png" style="zoom:50%;" />

All objects in JavaScript (with a few exceptions) have a `prototype`. Also, an object’s `prototype`itself is an object.Because a `prototype`is an object, a `prototype`can have its own `prototype`!

In this `prototype`chain, `Bird`is the `supertype`for `duck`, while `duck`is the `subtype`. `Object`is a `supertype`for both `Bird`and `duck`.

```javascript
function Bird(name) {
  this.name = name;
}

typeof Bird.prototype; // => object

Object.prototype.isPrototypeOf(Bird.prototype);
// returns true

let duck = new Bird("Donald");
duck.hasOwnProperty("name"); // => true

```

利用原型让一个引用类型继承另一个引用类型的属性和方法。

<https://segmentfault.com/a/1190000013245739>

```javascript
//combination constructor and prototype
function SuperType() {
  this.property = true;
}
SuperType.prototype.getSuperValue = function () {
  return this.property;
};

//combination constructor and prototype
function SubType() {
  this.subproperty = false;
}
//inherit from SuperType
SubType.prototype = new SuperType();
SubType.prototype.getSubValue = function () {
  return this.subproperty;
};
var instance = new SubType();
alert(instance.getSuperValue()); //true

```

![P204.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8wed71u3kj30io0b40t6.jpg)

### constructor stealing

借用构造函数/伪造对象/经典继承，方法都在构造函数中定义，没有函数复用，此方法很少单独使用。

盗用构造函数的主要缺点， 也是使用构造函数模式自定义类型的问题： 必须在构造函数中定义方法，因此函数不能重用。此外，子类也不能访问父类原型上定义的方法，因此所有类型只能使用构造函数模式。由于存在这些问题，盗用构造函数基本上也不能单独使用。

```javascript
function SuperType() {
  this.colors = ["red", "blue", "green"];
}

function SubType() {
  // inherit from SuperType
  SuperType.call(this);
}

var instance1 = new SubType();
instance1.colors.push("black");
alert(instance1.colors); // "red,blue,green,black"

var instance2 = new SubType();
alert(instance2.colors); // "red,blue,green"

```

```javascript
function SuperType(name) {
  this.name = name;
}

function SubType() {
  //inherit from supertype and passing in an argument
  SuperType.call(this, "Nicholas");

  //instance property
  this.age = 29;
}

var instance = new SubType();
alert(instance.name); //"Nicholas";
alert(instance.age); //29

```

### Combination Inheritance 

组合继承, prototype chaining + constructor stealing

使用原型链实现对原型属性和方法的继承，通过借用构造函数来实现对实例属性的继承。将两者的优点集中了起来。基本的思路是使用原型链继承原型上的属性和方法，而通过盗用构造函数继承实例属性。这样既可以把方法定义在原型上以实现重用，又可以让每个实例都有自己的属性。

```javascript
function SuperType(name) {
  this.name = name;
  this.colors = ["red", "blue", "green"];
}

SuperType.prototype.sayName = function () {
  alert(this.name);
};

function SubType(name, age) {
  //inherit properties
  SuperType.call(this.name);

  this.age = age;
}

//inherit methods
SubType.prototype = new SuperType();
SubType.prototype.sayAge = function () {
  alert(this.age);
};

var instance1 = new SubType("nicholas", 29);
instance1.colors.push("black");
alert(instance1.colors); //”red,blue,green,black”
instance1.sayName(); //"Nicholas";
instance1.sayAge(); //29

var instance2 = new SubType("greg", 27);
alert(instance2.colors); //”red,blue,green”
instance2.sayName(); //"Greg";
instance2.sayAge(); //27

```

### Prototypal Inheritance 

原型式继承

```javascript
function object(o){
  function F(){}
  F.prototype = o;
  return new F(); 
}
```

```javascript
var person = {
  name: "Nicholas",
  friends: ["Shelby", "Court", "Van"]
};
var anotherPerson = object(person);
anotherPerson.name = "Greg";
anotherPerson.friends.push("Rob");

var yetAnotherPerson = object(person);
yetAnotherPerson.name = "Linda";
yetAnotherPerson.friends.push("Barbie");
alert(person.friends); //”Shelby,Court,Van,Rob,Barbie”

```

<mark>Object.create() </mark>

With one argument, object.create( )=object( )

```javascript
var person = {
  name: "Nicholas",
  friends: ["Shelby", "Court", "Van"]
};

var anotherPerson = Object.create(person); 
anotherPerson.name = "Greg";
anotherPerson.friends.push("Rob");

var yetAnotherPerson = Object.create(person); 
yetAnotherPerson.name = "Linda";
yetAnotherPerson.friends.push("Barbie");

alert(person.friends);   //”Shelby,Court,Van,Rob,Barbie”
```

```javascript
function Animal() {}
Animal.prototype.eat = function () {
  console.log("nom nom nom");
};
function Bird() {}
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;

Bird.prototype.fly = function () {
  console.log("I'm flying!");
};

let duck = new Bird();
duck.eat(); // prints "nom nom nom"
duck.fly(); // prints "I'm flying!"

```

With two argument,Object.create(),Object.defineProperties():

Any properties specified in this manner will shadow properties of the same name on the prototype object.

这种方法指定的任何属性都会覆盖原型对象上的同名属性。

```javascript
var person = {
  name: "Nicholas",
  friends: ["Shelby", "Court", "Van"]
};
var anotherPerson = Object.create(person, {
  name: {
    value: "Greg"
  }
});
alert(anotherPerson.name); //"Greg"

```

### Parasitic Inheritance 

寄生式继承

### Parasitic Combination Inheritance 

寄生组合式继承

实现基于类型继承的最有效方式

### Override Inherited Methods

no overloading，方式重新书写后会覆盖之前书写过的。

```javascript
function Animal() {}
Animal.prototype.eat = function () {
  return "nom nom nom";
};
function Bird() {}

// Inherit all methods from Animal
Bird.prototype = Object.create(Animal.prototype);

// Bird.eat() overrides Animal.eat()
Bird.prototype.eat = function () {
  return "peck peck peck";
};

```

If you have an instance `let duck = new Bird();` and you call `duck.eat()`, this is how JavaScript looks for the method on `duck’s` `prototype` chain:

1.  duck => Is eat() defined here? No.
2.  Bird => Is eat() defined here? => Yes. Execute it and stop searching.
3.  Animal => eat() is also defined, but JavaScript stopped searching before reaching this level.
4.  Object => JavaScript stopped searching before reaching this level.

###  Mixin

As you have seen, behavior is shared through inheritance. However, there are cases when inheritance is not the best solution. Inheritance does not work well for unrelated objects like `Bird` and `Airplane`. They can both fly, but a `Bird` is not a type of `Airplane` and vice versa.

For unrelated objects, it's better to use mixins. A mixin allows other objects to use a collection of functions.

```javascript
//The flyMixin takes any object and gives it the fly method

let flyMixin = function (obj) {
  obj.fly = function () {
    console.log("Flying, wooosh!");
  };
};

let bird = {
  name: "Donald",
  numLegs: 2
};

let plane = {
  model: "777",
  numPassengers: 524
};

flyMixin(bird);
flyMixin(plane);

bird.fly(); // prints "Flying, wooosh!"
plane.fly(); // prints "Flying, wooosh!"

```

## IV. Classes

Classes are syntactic sugar that overlay the current constructor- and prototype-based approach to types. 

```js
class MyClass {
  prop = value; // property

  constructor(...) { // constructor
    // ...
  }

  method(...) {} // method

  get something(...) {} // getter method
  set something(...) {} // setter method

  [Symbol.iterator]() {} // method with computed name (symbol here)
  // ...
}
```

**class getter/setter**

```js
class User {

  constructor(name) {
    // invokes the setter
    this.name = name;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (value.length < 4) {
      alert("Name is too short.");
      return;
    }
    this._name = value;
  }

}

let user = new User("John");
alert(user.name); // John

user = new User(""); // Name is too short.
```

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}
Person.prototype.sayName = function () {
  alert(this.name);
};
Person.prototype.getOlder = function (years) {
  this.age += years;
};

```

The `constructor()` method is called automatically by `new`, so we can initialize the object there.

```js
class Person {
  // 有构造函数的类，有效
  constructor(name, age) {
    public name = name;
    this.age = age;
  }
  // 有获取函数的类，有效 
  get myBaz() {}
  // 有静态方法的类，有效
  static myQux() {}
  sayName() {
    alert(this.name);
  }
  getOlder(years) {
    this.age += years;
  }
}

new Person("John", 39)
```

###  The Class Constructor 

类构造函数

使用 new 调用类的构造函数会执行如下操作。 

(1) 在内存中创建一个新对象。 

(2) 这个新对象内部的[[Prototype]]指针被赋值为构造函数的 prototype 属性。 

(3) 构造函数内部的 this 被赋值为这个新对象（即 this 指向新对象）

(4) 执行构造函数内部的代码（给新对象添加属性）

(5) 如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象。

(6) **No comma between class methods**

```js
class Animal {}
class Person {
  constructor() {
    console.log("person ctor");
  }
}
class Vegetable {
  constructor() {
    this.color = "orange";
  }
}
let a = new Animal();
let p = new Person(); // person ctor 
let v = new Vegetable(); 
console.log(v.color);  // orange

```

```js
// 类实例化时传入的参数会用作构造函数的参数。如果不需要参数，则类名后面的括号也是可选的：
class Person {
  constructor(name) {
    console.log(arguments.length);
    this.name = name || null;
  }
}

let p1 = new Person(); // 0
console.log(p1.name); // null

let p2 = new Person(); // 0
console.log(p2.name); // null

let p3 = new Person("Jake"); // 1
console.log(p3.name); // Jake

```

类构造函数与构造函数的主要区别是，调用类构造函数必须使用new 操作符。而普通构造函数如果不使用 new 调用，那么就会以全局的 this（通常是 window）作为内部对象。调用类构造函数时如果忘了使用new 则会抛出错误。

**立即调用函数表达式相似，类也可以立即实例化**

```js
let p = new (class Foo {
  constructor(x) {
    console.log(x);
  }
})("bar"); // bar
console.log(p); // Foo {}

```

**类可以像函数一样在任何地方定义，比如在数组中**

```js
let classList = [
  class {
    constructor(id) {
      this.id_ = id;
      console.log(`instance ${this.id_}`);
    }
  }
];

function createInstance(classDefinition, id) {
  return new classDefinition(id);
}

let foo = createInstance(classList[0], 3141); // instance 3141

```

**[Not just a syntactic sugar](https://javascript.info/class#not-just-a-syntactic-sugar)**

1. First, a function created by `class` is labelled by a special internal property `[[IsClassConstructor]]: true`. So it’s not entirely the same as creating it manually.

2. Class methods are non-enumerable. A class definition sets `enumerable` flag to `false` for all methods in the `"prototype"`.

   That’s good, because if we `for..in` over an object, we usually don’t want its class methods.

3. Classes always `use strict`. All code inside the class construct is automatically in strict mode.

**[Making bound methods with class fields](https://javascript.info/class#making-bound-methods-with-class-fields)**

```js
class Button {
  constructor(value) {
    this.value = value;
  }
  click = () => {
    alert(this.value);
  }
}

let button = new Button("hello");

// setTimeout(() => button.click(), 1000)
setTimeout(button.click, 1000); // hello
```



### Instance, Prototype, and Class Members 

#### Instance Members 

实例成员

每次通过new调用类标识符时， 都会执行类构造函数。 在这个函数内部， 可以为新创建的实例 （this）添加“自有”属性。至于添加什么样的属性，则没有限制。另外，在构造函数执行完毕后，仍然可以给实例继续添加新成员。每个实例都对应一个唯一的成员对象，这意味着所有成员都不会在原型上共享。

==通过this的方式，new出来的实例对象的属性是不相同的，都是各自唯一的。==

```js
class Person {
  constructor() {
    // 这个例子先使用对象包装类型定义一个字符串
    // 为的是在下面测试两个对象的相等性
    this.name = new String('Jack');
    this.sayName = () => console.log(this.name);
    this.nicknames = ["Jake", "J-Dog"];
  }
}
let p1 = new Person(),
    p2 = new Person();
p1.sayName(); // Jack
p2.sayName(); // Jack
console.log(1, p1.name === p2.name); // false
console.log(2, p1.sayName === p2.sayName); // false
console.log(3, p1.nicknames === p2.nicknames); // false
p1.name = p1.nicknames[0];
p2.name = p2.nicknames[1];
p1.sayName(); // Jake
p2.sayName(); // J-Dog
```

```js
class Person {
  constructor() {
    this.name = "hihi";
    this.sayName = () => console.log(this.name);
    this.nicknames = ["Jake", "J-Dog"];
  }
}
let p1 = new Person(),
  	p2 = new Person();
p1.sayName(); // hihi
p2.sayName(); // hihi
console.log(1, p1.name === p2.name); // true
console.log(2, p1.sayName === p2.sayName); // false
console.log(3, p1.nicknames === p2.nicknames); // false
p1.name = p1.nicknames[0];
p2.name = p2.nicknames[1];
p1.sayName(); // Jake
p2.sayName(); // J-Dog

```

#### Prototype Methods and Accessors  

**原型方法与访问器**

为了在实例间共享方法，类定义语法把在类块中定义的方法作为原型方法。

```js
class Person {
  constructor() {
    // 添加到this的所有内容都会存在于不同的实例上
    this.locate = () => console.log("instance");
  }
  // 在类块中定义的所有内容都会定义在类的原型上
  locate() {
    console.log("prototype");
  }
}

let p = new Person();
p.locate(); // instance
Person.prototype.locate(); // prototype

```

**可以把方法定义在类构造函数中或者类块中， 但不能在类块中给原型添加原始值或对象作为成员数据： **

```js
class Person {  name: 'Jake' } // Uncaught SyntaxError: Unexpected token 
```

**虽然类定义并不显式支持在原型或类上添加成员数据，但在类定义外部，可以手动添加：**

```js
class Person {
  sayName() {
    console.log(`${Person.greeting} ${this.name}`);
  }
}
Person.greeting = "My name is"; // 在类上定义数据成员
Person.prototype.name = "Jake"; // 在原型上定义数据成员
let p = new Person();
p.sayName(); // My name is Jake

```

**类定义也支持获取和设置访问器。语法与行为跟普通对象一样**

```js
class Person {
  set name(newName) {
    this.name_ = newName;
  }
  get name() {
    return this.name_;
  }
}
let p = new Person();
p.name = "Jake";
console.log(p.name); // Jake

```

#### Static Class Methods and Accessors

**静态类方法**

可以在类上定义静态方法。这些方法通常用于执行不特定于实例的操作，也不要求存在类的实例。与原型成员(prototype members)类似，静态成员每个类上只能有一个。

Usually, static methods are used to implement functions that belong to the class as a whole, but not to any particular object of it.

new 出来的对象访问不到父类的 static methods。

==Static methods aren’t available for individual objects.==, 但是extends的类available，就可以用static的方法/属性。

Static methods are callable on classes, not on individual objects.

```js
class Person {
  constructor() {
    // 添加到this的所有内容都会存在于不同的实例上
    this.locate = () => console.log("instance", this);
  } 
  
  // 定义在类的原型对象上
  locate() {
    console.log("prototype", this);
  } 
  
  // 定义在类本身上
  static locate() {
    console.log("class", this);
  }
}

let p = new Person();
p.locate(); // instance, Person {}
Person.prototype.locate(); // prototype, {constructor: ... }
Person.locate(); // class, class Person {}

```

```js
class Article {
  constructor(title, date) {
    this.title = title;
    this.date = date;
  }

  static compare(articleA, articleB) {
    return articleA.date - articleB.date;
  }
}

// usage
let articles = [
  new Article("HTML", new Date(2019, 1, 1)),
  new Article("CSS", new Date(2019, 0, 1)),
  new Article("JavaScript", new Date(2019, 11, 1))
];

articles.sort(Article.compare);
alert(articles[0].title); // CSS
```

```js
class Article {
  publisher = "Ilya Kantor";
}

// Article.publisher = "bbbbbb";

let cc = new Article();
console.log(11,cc.publisher);
console.log(22,Article.publisher);
```

==class里的静态方法写法等同于在class外面进行赋值==

![image-20221104212058224](/Users/chenruo/Library/Application Support/typora-user-images/image-20221104212058224.png)

```js
// 但是extends的类available，就可以用static的方法/属性。
class Animal {
  static planet = "Earth";

  constructor(name, speed) {
    this.speed = speed;
    this.name = name;
  }

  run(speed = 0) {
    this.speed += speed;
    alert(`${this.name} runs with speed ${this.speed}.`);
  }

  static compare(animalA, animalB) {
    return animalA.speed - animalB.speed;
  }
}

// Inherit from Animal
class Rabbit extends Animal {
  hide() {
    alert(`${this.name} hides!`);
  }
}

let rabbits = [new Rabbit("White Rabbit", 10), new Rabbit("Black Rabbit", 5)];

rabbits.sort(Rabbit.compare);

rabbits[0].run(); // Black Rabbit runs with speed 5.

alert(Rabbit.planet); // Earth

```

How does it work? Again, using prototypes. As you might have already guessed, `extends` gives `Rabbit` the `[[Prototype]]` reference to `Animal`.

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7terukl9wj30so0iugpl.jpg)

**Summary**

Static methods are used for the functionality that belongs to the class “as a whole”. It doesn’t relate to a concrete class instance.

Static properties are used when we’d like to store class-level data, also not bound to an instance.

For `class B extends A` the prototype of the class `B` itself points to `A`: `B.[[Prototype]] = A`. So if a field is not found in `B`, the search continues in `A`.

#### Private and protected properties and methods

##### protected properties and methods

Protected properties are usually prefixed with an underscore _.

- 利用get/set accessor 处理 private property, 使用方法是直接赋值。
- 利用getter/setter function 处理 private property，使用方法是函数传参。

```js
class CoffeeMachine {
  _waterAmount = 0;

  set waterAmount(value) {
    if (value < 0) {
      value = 0;
    }
    this._waterAmount = value;
  }

  get waterAmount() {
    return this._waterAmount;
  }

  constructor(power) {
    this._power = power;
  }
}

// create the coffee machine
let coffeeMachine = new CoffeeMachine(100);

// add water
coffeeMachine.waterAmount = -10; // _waterAmount will become 0, not -10

```

```js
class CoffeeMachine {
  _waterAmount = 0;

  setWaterAmount(value) {
    if (value < 0) value = 0;
    this._waterAmount = value;
  }

  getWaterAmount() {
    return this._waterAmount;
  }
}

new CoffeeMachine().setWaterAmount(100);

```

**只读方法**

不设置setter即可。

```js
class CoffeeMachine {
  // ...

  constructor(power) {
    this._power = power;
  }

  get power() {
    return this._power;
  }
}

// create the coffee machine
let coffeeMachine = new CoffeeMachine(100);

alert(`Power is: ${coffeeMachine.power}W`); // Power is: 100W

coffeeMachine.power = 25; // Error (no setter)

```

==Protected fields are inherited==

If we inherit class MegaMachine extends CoffeeMachine, then nothing prevents us from accessing this._waterAmount or this._power from the methods of the new class.

##### Private properties and methods

**Privates should start with #. They are only accessible from inside the class.**

只要在class外部，永远获取不到 Private properties and methods.

```js
class CoffeeMachine {
  #waterLimit = 200;

  #fixWaterAmount(value) {
    if (value < 0) return 0;
    if (value > this.#waterLimit) return this.#waterLimit;
  }

  setWaterAmount(value) {
    this.#waterLimit = this.#fixWaterAmount(value);
  }
}

let coffeeMachine = new CoffeeMachine();

// can't access privates from outside of the class
coffeeMachine.#fixWaterAmount(123); // Error
coffeeMachine.#waterLimit = 1000; // Error

```

**Private fields are not available as this[name]**

Private fields are special. As we know, usually we can access fields using `this[name]`:

```javascript
class User {
  ...
  sayHi() {
    let fieldName = "name";
    alert(`Hello, ${this[fieldName]}`);
  }
}
```

With private fields that’s impossible: `this['#name']` doesn’t work. That’s a syntax limitation to ensure privacy.

### Inheritance

#### Inheritance Basics

**extends**

ES6类支持单继承。使用`extends`关键字，就可以继承任何拥有[[Construct]]和原型的对象。很大程度上，这意味着不仅可以继承一个类，也可以继承普通的构造函数（保持向后兼容）。==**Any expression is allowed after** `extends`==

```js
// 继承类 Inherit from class 
class Vehicle {} 
class Bus extends Vehicle {}
let b = new Bus();

console.log(b instanceof Bus); // true
console.log(b instanceof Vehicle); // true

// 继承普通构造函数 Inherit from function constructor 
function Person() {} 
class Engineer extends Person {}
let e = new Engineer();

console.log(e instanceof Engineer); // true
console.log(e instanceof Person); // true

function f(phrase) {
  return class {
    sayHi() { alert(phrase); }
  };
}

class User extends f("Hello") {}

new User().sayHi(); // Hello
```

```js
// 派生类(derived class)都会通过原型链访问到类和原型上定义的方法。this 的值会反映调用相应方法的实例或者类
class Vehicle {
  identifyPrototype(id) {
    console.log(id, this);
  }
  static identifyClass(id) {
    console.log(id, this);
  }
}

class Bus extends Vehicle {}

let v = new Vehicle();
let b = new Bus();

b.identifyPrototype("bus"); // bus, Bus {}
v.identifyPrototype("vehicle"); // vehicle, Vehicle {}
Bus.identifyClass("bus"); // bus, class Bus {}
Vehicle.identifyClass("vehicle"); // vehicle, class Vehicle {}

```

```js
class Animal {
  constructor(name) {
    this.speed = 0;
    this.name = name;
  }
  run(speed) {
    this.speed = speed;
    alert(`${this.name} runs with speed ${this.speed}.`);
  }
  stop() {
    this.speed = 0;
    alert(`${this.name} stands still.`);
  }
}

let animal = new Animal("My animal");
```

```js
class Rabbit extends Animal {
  hide() {
    alert(`${this.name} hides!`);
  }
}

let rabbit = new Rabbit("White Rabbit");

rabbit.run(5); // White Rabbit runs with speed 5.
rabbit.hide(); // White Rabbit hides!
```

#### Constructors, HomeObjects, and super() 

**构造函数、HomeObject 和super() **

##### [Overriding a method](https://javascript.info/class-inheritance#overriding-a-method)

派生类的方法可以通过 super 关键字引用它们的原型。这个关键字只能在派生类中使用，而且仅限于类构造函数、实例方法和静态方法内部。在类构造函数中使用super 可以调用父类构造函数。

Classes provide "super" keyword for that.

- super.method(...) to call a parent method.
- super(...) to call a parent constructor (inside our constructor only).

```js
class Animal {
  constructor(name) {
    this.speed = 0;
    this.name = name;
  }

  run(speed) {
    this.speed = speed;
    alert(`${this.name} runs with speed ${this.speed}.`);
  }

  stop() {
    this.speed = 0;
    alert(`${this.name} stands still.`);
  }
}

class Rabbit extends Animal {
  hide() {
    alert(`${this.name} hides!`);
  }

  stop() {
    super.stop(); // call parent stop
    this.hide(); // and then hide
  }
}

let rabbit = new Rabbit("White Rabbit");

rabbit.run(5); // White Rabbit runs with speed 5.
rabbit.stop(); // White Rabbit stands still. White Rabbit hides!

```

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7te5iwulej31b20uudqd.jpg)

##### [Overriding constructor](https://javascript.info/class-inheritance#overriding-constructor)

According to the [specification](https://tc39.github.io/ecma262/#sec-runtime-semantics-classdefinitionevaluation), if a class extends another class and has no `constructor`, then the following “empty” `constructor` is generated:

当一个类中没有明确写出constructor时，class中会默认给到  `constructor(...args) { super(...args); }`

```js
class Rabbit extends Animal {
  // generated for extending classes without own constructors
  constructor(...args) {
    super(...args);
  }
}
```

```js
// Constructors in inheriting classes must call super(...), and (!) do it before using this.
class Vehicle {
  constructor() {
    this.hasEngine = true;
  }
}

class Bus extends Vehicle {
  constructor() {
    // 不要在调用super()之前引用this，否则会抛出ReferenceError
    super(); // 相当于super.constructor()
    console.log(this instanceof Vehicle); // true
    console.log(this); // Bus { hasEngine: true }
  }
}

new Bus();
```

```js
// 在静态方法中可以通过super 调用继承的类上定义的静态方法：
class Vehicle {
  static identify() {
    console.log("vehicle");
  }
}

class Bus extends Vehicle {
  static identify() {
    super.identify();
  }
}

Bus.identify(); // vehicle
```

We can override not only methods, but also class fields.原声方法会被继承类重写时覆盖，字段也会。

```js
class Animal {
  name = 'animal';

  constructor() {
    alert(this.name); // (*)
  }
}

class Rabbit extends Animal {
  name = 'rabbit';
}

new Animal(); // animal
new Rabbit(); // animal
```

In other words, the parent constructor always uses its own field value, not the overridden one.

Well, the reason is the field initialization order. The class field is initialized:

- Before constructor for the base class (that doesn’t extend anything),
- Immediately after `super()` for the derived class.

In our case, `Rabbit` is the derived class. There’s no `constructor()` in it. As said previously, that’s the same as if there was an empty constructor with only `super(...args)`.

So, `new Rabbit()` calls `super()`, thus executing the parent constructor, and (per the rule for derived classes) only after that its class fields are initialized. At the time of the parent constructor execution, there are no `Rabbit` class fields yet, that’s why `Animal` fields are used. 因为我们在`new Rabbit()`的时候调用了`super()`，运行了父类的构造函数，之后才会初始化Rabbit自己的字段。当父类构造函数运行时，就没有`Rabbit`的字段存在了。所以才会输出animal。

This subtle difference between fields and methods is specific to JavaScript.

If it becomes a problem, one can fix it by using methods or getters/setters instead of fields.

被覆盖后的解决方法即：==using methods or getters/setters instead of fields.==，用访问器和修改器重写，而不使用字段处理，就好了。

```js
class Animal {
  showName() {  // instead of this.name = 'animal'
    alert('animal');
  }

  constructor() {
    this.showName(); // instead of alert(this.name);
  }
}

class Rabbit extends Animal {
  showName() {
    alert('rabbit');
  }
}

new Animal(); // animal
new Rabbit(); // rabbit
```

==在使用super 时要注意几个问题==

1. super 只能在派生类构造函数和静态方法中使用

2. 不能单独引用super 关键字，要么用它调用构造函数，要么用它引用静态方法。

3. 调用super()会调用父类构造函数，并将返回的实例赋值给this。

4. super()的行为如同调用构造函数，如果需要给父类构造函数传参，则需要手动传入。

5. 如果没有定义类构造函数，在实例化派生类时会调用super()，而且会传入所有传给派生类的 

   参数。 

6. 在类构造函数中，不能在调用super()之前引用this。

7. 如果在派生类中显式定义了构造函数，则要么必须在其中调用 super()，要么必须在其中返回 

   一个对象。

That label affects its behavior with `new`.

- When a regular function is executed with new, it creates an empty object and assigns it to this.

- But when a derived constructor runs, it doesn’t do this. It expects the parent constructor to do this job.

So a derived constructor must call super in order to execute its parent (base) constructor, otherwise the object for this won’t be created. And we’ll get an error.

```js
// 1.
class Vehicle {
  constructor() {
    super(); // SyntaxError: 'super' keyword unexpected
  }
}
```

```js
// 2. 
class Vehicle {}
class Bus extends Vehicle {
  constructor() {
    console.log(super); // SyntaxError: 'super' keyword unexpected here
  }
}
```

```js
// 3. 
class Vehicle {}
class Bus extends Vehicle {
  constructor() {
    super();
    console.log(this instanceof Vehicle);
  }
}

new Bus(); // true
```

```js
// 4.
class Vehicle {
  constructor(licensePlate) {
    this.licensePlate = licensePlate;
  }
}
class Bus extends Vehicle {
  constructor(licensePlate) {
    super(licensePlate);
  }
}
console.log(new Bus("1337H4X")); // Bus { licensePlate: '1337H4X' }
```

```js
// 5.
class Vehicle {
  constructor(licensePlate) {
    this.licensePlate = licensePlate;
  }
}
class Bus extends Vehicle {}
console.log(new Bus("1337H4X")); // Bus { licensePlate: '1337H4X' }

```

```js
// 6.
class Vehicle {}
class Bus extends Vehicle {
  constructor() {
    console.log(this);
  }
}
new Bus(); 
// ReferenceError: Must call super constructor in derived class 
// before accessing 'this' or returning from derived constructor
```

```js
// 7.
class Vehicle {}
class Car extends Vehicle {}
class Bus extends Vehicle {
  constructor() {
    super();
  }
}
class Van extends Vehicle {
  constructor() {
    return {};
  }
}
console.log(new Car()); // Car {}
console.log(new Bus()); // Bus {}
console.log(new Van()); // {}
```



## Don't Repeat Yourself (DRY)

// inheritance ,关于继承，但是没有相关联，cat和dog 如何获取animal的方法？

[Don't Repeat Yourself (DRY)](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/object-oriented-programming/use-inheritance-so-you-dont-repeat-yourself)

```javascript
function Cat(name) {
  this.name = name;
}

Cat.prototype = {
  constructor: Cat
};

function Bear(name) {
  this.name = name;
}

Bear.prototype = {
  constructor: Bear
};

function Animal() {}

Animal.prototype = {
  constructor: Animal,
  eat: function () {
    console.log("nom nom nom");
  }
};

```

# Chapter 7: function expressions

## I. function expressions

定义函数的方式：函数声明 function declaration，函数表达式 function expression，Function expressions have several forms.

```javascript
//function declaration
function functionName(arg0, arg1, arg2) {
  //function body 
} 
```

```javascript
//function expression,the most commom is as follows
//anonymous function 匿名函数
var functionName = function(arg0, arg1, arg2) {
  //function body  
};
```

```js
let myFunction = function loggingFunction (){
console.log('here is a message')
}

myFunction();
loggingFunction();//error
//this function name here is noly for debugging purposes
```

function declaration hoisting 函数声明提升

在执行代码之前会先读取函数声明，可以把函数声明放在调用他的语句后面。

```javascript
sayHi(); 
function sayHi(){
  alert(“Hi!”); 
}
//never use,尽管这个function是对的
```

```javascript
var sayHi = function(){
  alert("hi");
};
sayHi();
//没有函数声明提升 function expression
```

## II. recursion

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

## III. closures

区分匿名函数和闭包。

闭包指的是有权访问另一个函数作用域中的变量的函数。

创建闭包的常见方式，就是在一个函数内部创建另一个函数。

In JavaScript, a function always has access to the context in which it was created. This is called `closure`. 

### closures and variables

闭包只能取得包含函数中任何变量最后一个值，保存的是整个变量对象，不是某个特殊变量。

```javascript
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(){
      return i;
    };
  }
  return result; 
} 

//只会返回10，即使是遍历函数，最终结果是10，不会返回各自不同的索引值

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

```javascript
function Bird() {
  let hatchedEgg = 10; // private variable

  /* publicly available method that a bird object can use */
  this.getHatchedEggCount = function() { 
    return hatchedEgg;
  };
}
let ducky = new Bird();
ducky.getHatchedEggCount(); // returns 10
```

public property 容易被串改到别的值，所以为了防止数据串改，将数据设为私有，通过闭包的方式。改变变量的作用域，由全局变量转变为局部变量。

This way, the variable can only be accessed and changed by methods also within the constructor function.

 Here `getHatchedEggCount` is a privileged method, because it has access to the private variable `hatchedEgg`. This is possible because `hatchedEgg` is declared in the same context as `getHatchedEggCount`. 

```js
//无论使用何种方式对函数类型的值进行传递，当函数在别处被调用的时候都可以观察到闭包
function foo(){
  var a = 222222;
  
  function baz(){
    console.log(a);
  }
  
  bar(baz);
}

function bar(fn){
  fn();//this is clousure
}

foo();
//传递函数也可以是间接的
var fn;
function foo(){
  var a =2 ;
  function baz(){
    console.log(a);
  }
  fn = baz;//将baz 分配给全局变量
}

function bar(){
  fn();
}

foo();
bar();
```

### this object

This , 指向的是当前触发事件的元素

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
cnosole.log(this.name)//empty string
cnosole.log(this) // window object
```

因为箭头函数的this对象是定义时所在的对象，而不是使用时所在的对象，所以指向的是the window object,他寻找the name variable in the global context , cannot find it

```javascript
var name = “The Window”;
var object = {
  name : “My Object”,
   //这是匿名函数
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

在定义匿名函数之前，我们把对象赋值给了一个名叫that的变量，而在定义了闭包之后，闭包也可以访问这个变量，因为它是我们在包含函数中特意声明的一个变量，即使在函数返回之后，that也仍然引用着object,所以调用object,getNameFunc()()就返回了，my object.


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

### IIFE

Immediately Invoked Function Expression

立即调用函数表达式

 Note that the function has no name and is not stored in a variable 

```javascript
(function () {
  console.log("Chirp, chirp!");
})(); 
// this is an anonymous function expression that executes right away
// Outputs "Chirp, chirp!" immediately
```

```javascript
function makeNest() {
  console.log("A cozy nest is ready");
}

makeNest();
```

```javascript
(function() {
  console.log("A cozy nest is ready");
})();
```

### Use an IIFE to Create a Module

This returned object contains all of the mixin behaviors as properties of the object. The advantage of the module pattern is that all of the motion behaviors can be packaged into a single object that can then be used by other parts of your code 

将变量变成局部变量，不影响其他代码的使用。

```javascript
function glideMixin(obj) {
  obj.glide = function() {
    console.log("Gliding on the water");
  };
}
function flyMixin(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  };
}
```

We can group these mixins into a module as follows:


```javascript
//Note that you have an immediately invoked function expression (IIFE) that returns an object motionModule
//赋予给一个变量


let motionModule = (function () {
  return {
    glideMixin: function(obj) {
      obj.glide = function() {
        console.log("Gliding on the water");
      };
    },
    flyMixin: function(obj) {
      obj.fly = function() {
        console.log("Flying, wooosh!");
      };
    }
  }
})(); 
// The two parentheses cause the function to be immediately invoked

let duck = {name:'cat'}; 
//let duck = {}; 

motionModule.glideMixin(duck);
duck.glide();
```

```javascript
let isCuteMixin = function(obj) {
  obj.isCute = function() {
    return true;
  };
};
let singMixin = function(obj) {
  obj.sing = function() {
    console.log("Singing to an awesome tune");
  };
};
```

We can group these mixins into a module as follows:

```javascript
let funModule = (function(){
  return {
    isCuteMixin : function(obj){
      obj.isCute = function(){
        return true;
      };
    },
    singMixin:function(obj){
      obj.sing = function (){
        console.log("Singing to an awesome tune");
      };
    }
  }
})();
```

how closure works

```js
//without closure

let greeting = (function(){
  let message = 'hello';
  let getMessage = function(){
    return message;
  };
})();

console.log(greeting.getMessage());//undefined

//with closure
let greeting = (function(){
  let message = 'hello';
  let getMessage = function(){
    return message;
  };
  //return object with property getmessage and the value is the function getmessage
  return {
    getMessage:getMessage,
  }
})();
console.log(greeting.getMessage());//hello


```

```js
function setupCounter (val){
  return function counter(){
    return val++;
  }
}
let counter1 = setupCounter(0);
console.log(counter1());//0
console.log(counter1());//1

let counter2 = setupCounter(10);
console.log(counter2());//10

```

### memory leaks

## IV. mimicking block scope

有块级作用域，找其他资料补充，这节jump

## V. private variables

任何函数中的定义的变量，都可以认为是私有变量，不能再函数外部访问这些变量。私有变量包括函数的参数，局部变量和在函数内部定义的其他函数。

闭包可以通过自己的作用域链访问这些内部变量。

```javascript
function add(num1, num2){
  var sum = num1 + num2;
  return sum; 
} 
```

when we have a local variable in the function,once this function finished execution, sum no longer exists

```js
let key =42;
function getSecretCode(value){
  let keyGenerator = function(){
    let key = 12;
    console.log("in keyGenerator",key); //12
    return key
  }
  
  let code = value * keyGenerator();
  console.log("in getSecretCode",key); //42
  return code;
}
```



特权方法(privileged method)：有权访问私有变量和私有函数的公有方法。（两种

a. 自定义类型创建私有变量和特权方法（在构造函数中定义特权方法

缺点：针对每个实例都会创建同一组新方法，使用静态私有变量来实现特权方法可避免此问题

```javascript
function MyObject(){
  //private variables and functions
  var privateVariable = 10;
  function privateFunction(){
    return false;
  }
  //privileged methods
  //closure
  this.publicMethod = function (){
    privateVariable++;
    return privateFunction();
  }; 
} 
```

利用私有和特权成员，隐藏不该被直接修改的数据

## VI. Statics private variables

b. 自定义类型创建私有变量和特权方法（在私有作用域中定义私有变量或函数

```javascript
(function(){
  //private variables and functions
  var privateVariable = 10;
  function privateFunction(){
    return false;
  }
  //constructor
  MyObject = function(){};
  //public and privileged methods 
  MyObject.prototype.publicMethod = function(){
    privateVariable++;
    return privateFunction();
  };
})(); 
```

b 与 a 的区别，私有变量和函数是由实例共享的

c. 单例(singleton)创建私有变量和特权方法（模块模式module pattern 之后的章节有讲

### the module pattern

单例(singleton)创建私有变量和特权方法（模块模式module pattern。单例，指的就是只有一个实例的对象。

```javascript
var singleton = {
  name : value,
  method : function () {
    //method code here
  } 
};
```

模块模式通过为单例添加私有变量和特权方法能够使其得到增强

```javascript
var singleton = function(){
  //private variables and functions
  var privateVariable = 10;
  function privateFunction(){
    return false;}//privileged/public methods and properties
  return {
    publicProperty: true,
    publicMethod : function(){
      privateVariable++;
      return privateFunction();
    }
  }; 
}(); 
```

### the module-augmentation patterns

适合那些单例必须是某种实例类型，同时还必须添加某些属性和(或)方法对其加以增强的情况。

```javascript
var application = function(){
  //private variables and functions
  var components = new Array();
  //initialization
  components.push(new BaseComponent());
  //public interface
  return {
    getComponentCount : function(){
      return components.length;
    },
    registerComponent : function(component){
      if (typeof component == “object”){
        components.push(component);
      }
    }
  }; 
}(); 
```

# Chapter: FCC Functional Programming

Functional programming is a style of programming where solutions are simple, isolated functions, without any side effects outside of the function scope. 

```javascript
INPUT -> PROCESS -> OUTPUT
```

Functional programming is about:

1. Isolated functions - there is no dependence on the state of the program, which includes global variables that are subject to change

2. Pure functions - the same input always gives the same output

3. Functions with limited side effects - any changes, or mutations, to the state of the program outside the function are carefully controlled

# Chapter 8: the browser object model(BOM)

浏览器对象模型

## I. window object

Since the window object doubles as the ECMAScript Global object, all variables and functions declared globally become properties and methods of the window object.

window object = global object(全局作用域中)

age 自动归在了windows对象名下,可以通过windows.age访问变量age(etc.)

```javascript
var age = 29; 
function sayAge(){
    alert(this.age); 
}
alert(window.age);    //29 
sayAge();             //29 
window.sayAge();      //29 
```

全局变量不能通过delete操作符删除，但是可以通过在windows对象上的定义的属性可以

```javascript
var age = 29; window.color = "red"; //throws an error in IE < 9, returns false in all other browsers delete window.age; //throws an error in IE < 9, returns true in all other browsers delete window.color;    //returns true alert(window.age);      //29 alert(window.color);    //undefined 
```

弹出窗口屏蔽程序

window.open()

间歇调用和超时调用

```javascript
//avoid! 
setTimeout("alert(‘Hello world!’)", 1000);
//preferred use function
setTimeout(function() { 
    alert(“Hello world!”); 
}, 1000); 

//set the timeout 
var timeoutId = setTimeout(function() {
    alert(“Hello world!”); 
}, 1000);
//nevermind - cancel it 
clearTimeout(timeoutId); 

//间歇调用 p205 chinese ver. p253 eng ver.
var num = 0; 
var max = 10; 
var intervalId = null;
function incrementNumber() {
    num++;
    //if the max has been reached, cancel all pending executions
    if (num == max) {
        clearInterval(intervalId);
        alert(”Done”);
    } 
}
intervalId = setInterval(incrementNumber, 500); 

//超时调用
var num = 0; 
var max = 10;
function incrementNumber() {
    num++;
    //if the max has not been reached, set another timeout
    if (num < max) {
        setTimeout(incrementNumber, 500);
    } else {
        alert(“Done”);
    } 
}
setTimeout(incrementNumber, 500); 
```

超时调用的代码都是在全局作用域中执行的，因此函数中this的值在非严格模式中指向windows对象，严格模式下是undefined.

## II. the location object

提供与当前窗口中加载的文档有关的信息，还提供了一些导航功能，将UR解析为独立片段开发人员可以通过不同属性访问这些片段

window.location = document.location

location对象的属性（省略了location前缀

| PROPERTY NAME | EXAMPLE                | DESCRIPTION                       |
| ------------- | ---------------------- | --------------------------------- |
| hash          | “#contents”            | P207 chinese ver                  |
| host          | “www.wrox.com:80”      |                                   |
| hostname      | “www.wrox.com”         |                                   |
| href          | “http://www.wrox .com” |                                   |
| pathname      | “/WileyCDA/”           |                                   |
| port          | “8080”                 |                                   |
| protocol      | “http:”                |                                   |
| search        | “?q=javascript”        | 返回URL查询的字符串，其以问号开头 |

查询字符串参数

## III. the navigator object

识别客户端浏览器的事实标准

检测插件,Detecting Plug-ins 

plugins array.

properties.

name — The name of the plug-in 

description — The description of the plug-in 

filename — The filename for the plug-in 

length — The number of MIME types handled by this plug-in ，插件所处理的mime类型数量

```javascript
//plugin detection - doesn’t work in Internet Explorer 
function hasPlugin(name){name = name.toLowerCase();for (var i=0; i < navigator.plugins.length; i++){if (navigator.plugins[i].name.toLowerCase().indexOf(name) > -1){return true;}}return false; }
//detect flash 
alert(hasPlugin(”Flash”));
//detect quicktime 
alert(hasPlugin(”QuickTime”)); 
```

## IV. the screen object

表明客户端的能力，包括浏览器窗口外部显示器的信息，像素宽度和高度等等。用处不大。

## V. the history object

保存用户上网的历史记录，用处不大。

# Chapter 9: Client Detection

## I. capability detection

不是识别特定浏览器，识别浏览器的能力，根据浏览器支持特定的能力，给出解决方案

## II. Quirks detection

识别浏览器的特殊行为，检测浏览器存在什么缺陷，以确定某一特性不能正常工作。

## III. user-agent detection

通过检测用户代理字符串来确定实际使用的浏览器。

navigator.userAgent

使用优先级排在能力检测和怪癖检测之后(capability/quirks detections)

使用原则：

- 不能直接准确使用能力检测或怪癖检测

- 同一款浏览器在不同平台下具备不同的能力。有必要确定浏览器位于哪个平台下。

- 为了跟踪分析等目的需要知道确切的浏览器

优先使用能力检测。

# Chapter 10: DOM the document object model

文档对象模型

[HTML DOM 简介](http://www.w3school.com.cn/htmldom/dom_intro.asp)

- DOM（文档对象模型）是针对 HTML 和 XML 文档的一个 API，通过 DOM 可以去改变文档。

- 简单的说，一个 web 网页就是一个文档，使用 DOM 改变文档就是使用 DOM 定义的一些方法操作具体的节点。比如用getElementById 来根据元素 id 来查找元素节点。

- 当浏览器载入HTML时，会生成相应的 DOM 树，大概长这样

  ![img](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LEnFv3jMWsHS31RfsLD%2F-LEnFymU6ro7LIcUvFQV%2F-LEnG-4J9dKFWiSXiSED%2Fhtml-dom.png?generation=1528794719454822&alt=media)

- 把它转成 HTML 代码的话会是这样

```html
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

```javascript
document.documentElement  // 可以直接拿到 html 节点的引用
document.title //  可以直接获取 title 节点的文本 “我是title”
document.URL // 获取 URL
```

- document 对象的常用方法

```javascript
document.getElementById 
// docment.getElementById('myId') 可以获取到属性 id 为 ‘myId’ 的节点，在上面的代码中获取的也就是 p 节点
document.getElementsByTagName 
//docment.getElementByTagName('p') 可以获取到节点为 p 的所有节点集
```

- 现在我们就根据 document 对象中的方法获取到 HTML 中任意节点了，下面我们来介绍在已经拿到节点的基础上该如何对该节点进行操作。

#### Element 类型

- 通常我们在使用 document 对象来获取节点时，返回的节点类型就是 Element 类型，所以我们想要对获取的节点进行操作，我们只需要使用 Element 包含的属性和方法即可。

- 常用的属性：

```javascript
var myNode = document.getElementById('myId');
myNode.id // 获取该节点的 id ，即 ‘myId‘
myNode.tagName // 获取该节点的节点名，即 'P'，大部分浏览器返回的标签名都是大写
myNode.className //获取该节点的 class
```

- 操作节点属性的常用方法：

```javascript
//假如我们有一个 input，我们想要获取 input 的 type 属性，并对 type 属性进行操作
<input type='text' id='input'/>

var myNode = document.getElementById('input')
myNode.getAttribute('type') // 获取属性值，即 ‘text’
myNode.setAttribute('type','password') // 将 type 属性值改为 password 类型
myNode.removeAttribute('type') // 移除 type 属性
```

- 编写一个模拟用户登录的功能，正确的账号密码均为123，页面需要两个 input 节点和一个 button 节点。要求：
- 点击 button 时需要判断用户输入的账号密码是否为 123 ，并给予相应的提示（方式不限）
- 如果账号或密码错误，将密码所在的 input 节点中的内容清空

![](http://ww1.sinaimg.cn/large/005NUwygly1g1ookel9tij32801e0nbt.jpg)

## hierarchy of node

节点层次

the node type

### the document type

#### characteristics:

1. nodeType is 9. 

2. nodeName is “#document”. 

3. nodeValue is null. 

4. parentNode is null. 

5. ownerDocument is null. 

6. Child nodes may be a DocumentType (maximum of one), Element (maximum of one), ProcessingInstruction, or Comment. 

### <mark>the element type</mark>

#### characteristics:

1. nodeType is 1. 

2. nodeName is the element’s tag name. 

3. nodeValue is null. 

4. parentNode may be a Document or Element. 

5. Child nodes may be Element, Text, Comment, ProcessingInstruction, CDATASection, or EntityReference. 

```html
<div id=”myDiv”></div>
```

```javascript
var div = document.getElementById(“myDiv”); 
alert(div.tagName);    //”DIV” 
alert(div.tagName == div.nodeName);   //true 
```

getAttribute(), setAttribute(), and removeAttribute()

### the text type

#### characteristics:

1. nodeType is 3. 

2. nodeName is “#text”. 

3. nodeValue is text contained in the node. 

4. parentNode is an Element. 

5. Child nodes are not supported. 

#### methods:

1. appendData(text) — Appends text to the end of the node. 

2. deleteData(offset, count) — Deletes count number of characters starting at position offset. 

3. insertData(offset, text) — Inserts text at position offset. 

4. replaceData(offset, count, text) — Replaces the text starting at offset through offset + count with text. 
5. splitText(offset) — Splits the text node into two text nodes separated at position offset. 

6. substringData(offset, count) — Extracts a string from the text beginning at position offset and continuing until offset + count. 

### the comment type

#### characteristics:

1. nodeType is 8. 

2. nodeName is “#comment”. 

3. nodeValue is the content of the comment. 

4. parentNode is a Document or Element. 

5. Child nodes are not supported. 

### the CDATASection type

#### characteristics:

1. nodeType is 4. 

2. nodeName is “#cdata-section”. 

3. nodeValue is the contents of the CDATA section. 

4. parentNode is a Document or Element. 

5. Child nodes are not supported. 

### the documenttype type

#### characteristics:

1. nodeType is 10. 

2. nodeName is the name of the doctype. 

3. nodeValue is null. 

4. parentNode is a Document. 

5. Child nodes are not supported. 

### the documentfragment type

#### characteristics:

1. nodeType is 11. 

2. nodeName is “#document-fragment”. 

3. nodeValue is null. 

4. parentNode is null. 

5. Child nodes may be Element, ProcessingInstruction, Comment, Text, CDATASection, or 

6. EntityReference. 

### the attr type

#### characteristics:

1. nodeType is 11. 

2. nodeName is the attribute name. 

3. nodeValue is the attribute value. 

4. parentNode is null. 

5. Child nodes are not supported in HTML. 

6. Child nodes may be Text or EntityReference in XML.

## working with the DOM

# Chapter 11: DOM Extensions

DOM主要的扩展是selectorAPI和HTML5

## selector API

### querySelector() 

### querySelectorAll()

### matchesSelector() 

## element traversal

元素遍历

childElementCount

firstElementChild

lastElementChild

previousElementSibling

nextElementSibling

```javascript
var i,
    len,
    child = element.firstElementChild; 
while(child != element.lastElementChild){
    processChild(child);   //already know it’s an element
    child = child.nextElementSibling; 
} 
```

## HTML 5

### getElementsByClassName()

### classList

```javascript
//remove the “disabled” class 
div.classList.remove(“disabled”);
//add the “current” class 
div.classList.add(“current”);
//toggle the “user” class 
div.classList.toggle(“user”);
//figure out what’s on the element now 
if (div.classList.contains(“bd”) && !div.classList.contains(“disabled”)){
    //do something 
}
//iterate over the class names 
for (var i=0, len=div.classList.length; i < len; i++){
    doSomething(div.classList[i]); 
} 
```

返回的对象是Nodelist

### document .activeElement

Determining if the document has focus allows you to determine if the user is interacting with 

the page. 

```javascript
var button = document.getElementById(“myButton”); 
button.focus(); 
alert(document.hasFocus());  //true 
```

## proprieties extensions

### children Property/ contains()

# Chapter 12: DOM levels 2 and 3

DOM级别主要定义是HTML和XML文档的地层结构。DOM2和DOM3级别则在这个结构

document object model

## DOM Style Properties and Methods 

- cssText — As described previously, provides access to the CSS code of the style attribute. 

- length — The number of CSS properties applied to the element. 

- parentRule — The CSSRule object representing the CSS information. The CSSRule type is discussed in a later section. 

- getPropertyCSSValue(propertyName) — Returns a CSSValue object containing the value of the given property. 

- getPropertyPriority(propertyName) — Returns “important” if the given property is set using !important; otherwise it returns an empty string. 

- getPropertyValue(propertyName) — Returns the string value of the given property. 

- item(index) — Returns the name of the CSS property at the given position. 

- removeProperty(propertyName) — Removes the given property from the style. 

- setProperty(propertyName, value, priority) — Sets the given property to the given value with a priority (either “important” or an empty string). 

# Chapter 13: EVENT

- [JavaScript 事件参考手册](http://www.runoob.com/jsref/dom-obj-event.html)
- [JS事件模型](https://segmentfault.com/a/1190000006934031)

## event flow
JavaScript’s interaction with HTML is handled through events, which indicate when particular moments of interest occur in the document or browser window. 

事件在触发的时候，先后执行的顺序，事件触发的流程，叫做事件流。

### event bubbling

事件冒泡，IE的事件流叫做事件冒泡，即事件开始时由最具体的元素(文档中嵌套层次最深的那个节点)接收，然后逐级向上传播到较为不具体的节点(文档)。

单击页面中的div元素。click event occurs in the following order.

```html
<!DOCTYPE html> 
<html> 
    <head>
    <title>Event Bubbling Example</title> 
    </head> 
    <body>
    <div id=”myDiv”>Click Me</div> 
    </body> 
</html> 
```

```js
// var aDiv=document.querySelectorAll('div');
// for(var i=0;i<aDiv.length;i++){
//     aDiv[i].onclick=function(){
//         alert(1);
//     }
// }
//事件冒泡优化
document.body.onclick = function () {
  //console.log(event.target)
  //console.log(event.srcElement)
  // if(event.target.nodeName=='DIV'){
  //     alert(1);
  // }
  if (event.target.tagName == "DIV") {
    alert(1);
  }
};
```



![QQ截图20191024102323.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g892u8gq65j30c20aht8s.jpg)

### event capturing

事件捕获(事件下沉)，其思想是不太具体的节点应该更早接收到事件，而最具体的节点应该最后接收到事件。事件捕捉的用意在于事件到达预定目标之前捕获他。

![QQ截图20191024103058.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g89320nnzbj309t08y3yi.jpg)

### DOM event flow

事件流包括三个阶段：事件捕获阶段，处于目标阶段和事件冒泡阶段

![QQ截图20191024103217.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8933cfsgtj30eb09174f.jpg)

## event handlers

事件处理程序，事件就是用户或者浏览器自身执行的某种动作，如click,load,mouseover，都是事件。而响应某个事件的函数就叫做事件处理程序。都以“on”开头。onclick,onload

### html event handlers

`<input type=”button” value=”Click Me” onclick=”alert(‘Clicked’)” /> `

`<input type=”button” value=”Click Me” onclick=”alert(&quot;Clicked&quot;)” /> `

```html
<script type=”text/javascript”>
function showMessage(){
alert(“Hello world!”);
}
</script> 
<input type=”button” value=”Click Me” onclick=”showMessage()” /> 
```

```javascript
//DOM Level 0 Event Handlers 
var btn = document.getElementById(“myBtn”); 
btn.onclick = function(){
    alert(“Clicked”); 
}; 

var btn = document.getElementById(“myBtn”); 
btn.onclick = function(){
    alert(this.id);    //”myBtn” 
}; 

btn.onclick = null;    //remove event handler 删除事件处理程序

```

DOM Level 2 Event Handlers

addEventListener()

removeEventListener()

capture phase (true) 

bubble phase (false)

```javascript
//DOM Level 2 Event Handlers 
var btn = document.getElementById(“myBtn”); 
btn.addEventListener(“click”, function(){
    alert(this.id); 
}, false); 
btn.addEventListener(“click”, function(){
    alert(“Hello world!”); 
}, false);
```

通过addEventListener()添加的事件处理程序，只能用removeEventListener()进行删除，移除时传入的参数与添加处理程序时使用的参相同，否则无法移除。即移除添加的匿名函数将无法移除。

```javascript
var btn = document.getElementById(“myBtn”); 
btn.addEventListener(“click”, function(){
    alert(this.id); 
}, false);

//other code here
btn.removeEventListener(“click”, function(){   
    //won’t work!
    alert(this.id); 
}, false); 
```

attachEvent() and detachEvent() for IE & OPERA

跨浏览器事件处理程序：Cross-Browser Event Handlers 

要保证处理事件的代码能在大多数浏览器下一致运行，只需要关注冒泡阶段。

addHandler()

removeHandler()

EventUtil

## event object

处理多个事件函数

```javascript
var btn = document.getElementById(“myBtn”); 
var handler = function(event){
    switch(event.type){
        case “click”:
            alert(“Clicked”);
            break;
        case “mouseover”:
            event.target.style.backgroundColor = "red";
            break;
        case “mouseout”:
            event.target.style.backgroundColor = “”;
            break;                        
    } 
};
btn.onclick = handler; 
btn.onmouseover = handler; 
btn.onmouseout = handler;
```

preventDefault()，阻止特定事件的默认行为

to navigate to the URL specified in its href attribute when clicked. If you want to prevent that navigation from occurring,

```javascript
var link = document.getElementById(“myLink”); 
link.onclick = function(event){
    event.preventDefault(); 
}; 
```

```js
oDiv.onclick = function (ev) {
  //ev  这个是形参 随便叫什么都行
  //event  这个必须是event 系统的一个全局变量 使用在函数内部
  //ev  只兼容高级浏览器
  //event  以前兼容非火狐   现在变得都兼容了
  //怎么处理兼容：
  var oEvent = event || ev;
};
```



跨浏览器的事件对象，The Cross-Browser Event Object 

## event type

- User interface (UI) events are general browser events that may have some interaction with the BOM. 

  用户界面事件

- Focus events are fired when an element gains or loses focus. 焦点事件

- Mouse events are fired when the mouse is used to perform an action on the page. 鼠标事件

- Wheel events are fired when a mouse wheel (or similar device) is used. 滚轮事件

- Text  events are fired when text is input into the document. 文本事件

- Keyboard events are fired when the keyboard is used to perform an action on the page. 键盘事件

- Composition events are fired when inputting characters for an Input Method Editor (IME). 合成事件

- Mutation events are fired when a change occurs to the underlying DOM structure. 变动事件

- Mutation name events are fired when element or attribute names are changed. These events are deprecated and not implemented by any browser, so they are intentionally omitted from this chapter. 变动名称事件

## UI events

1. DOMActivate:废弃
2. load
3. unload
4. abort
5. error
6. select
7. resize
8. scroll

## Focus events

1. blur,不冒泡
2. DOMFocusIn：废弃，=focusuin
3. DOMFocusOut：废弃，=focusout
4. focus，不冒泡

## mouse and wheel events

1. click Event
2. dbclick Event
3. mousedown Event
4. mouseenter Event
5. mouseleave Event
6. mousemove Event
7. mouseout Event
8. mouseover Event
9. mouseup Event

All elements on a page support mouse events. All mouse events bubble except mouseenter and 

mouseleave, and they can all be canceled, which affects the default behavior of the browser. 

Canceling the default behavior of mouse events can affect other events as well because of the 

relationship that exists amongst the events. 

A click event can be fi red only if a mousedown event is fi red and followed by a mouseup event 

on the same element; if either mousedown or mouseup is canceled, then the click event will not 

fi re. Similarly, it takes two click events to cause the dblclick event to fi re. If anything prevents 

these two click events from fi ring (either canceling one of the click events or canceling either 

mousedown or mouseup), the dblclick event will not fi re. These four mouse events always fi re in 

the following order:

1. mousedown

2. mouseup

3. click

4. mousedown

5. mouseup

6. click

7. dblclick 

## keyboard and text events

1. keydown Event
2. keypress Event
3. keyup Event

## composition events

DOM3级事件中新添加的一类事件，用于处理IME输入序列，input method editor,输入法编辑器。可以让用户输入在物理键盘上找不到的字符。

## mutation events

变动事件

DOM2级的变动事件能在DOM中的某一部分发生变化时给出提示。变动事件是为XML或HTML DOM设计的，并不特定于某种语言。

## html5 events

HTML5 详尽列出了浏览器应该支持的所有事件

1. contextmenu Event
2. beforeunload Event
3. DOMcontentLoaded Event
4. readystatechange Event
5. pagehow,pagehide Event
6. haschange Event

## device events

让开发人员确定用户在怎样使用设备

1. orientationchange Event

   确定用户何时将设备横向查看或纵向查看模式

2. MozOrientation Event 

3. deviceorientation Event

4. devicemotion Event

## touch and gesture events

## Touch Events

1. touchstart
2. touchmove
3. touchend
4. touchcancel
5. touches
6. targetTouches
7. clientX
8. clientY
9. identifier
10. pageX
11. pageY
12. screenX
13. screenY
14. target

## Gesture Events

1. gesturestart
2. gesturechange
3. gestureend

## memory and performance

## 事件委托

### 定义

“过多事件处理程序”的解决方案是使用事件委托。事件委托利用事件冒泡，可以只使用一个事件处理程序来管理一种类型的事件。例如，click 事件冒泡到 document。这意味着可以为整个页面指定一个 onclick 事件处理程序，而不用为每个可点击元素分别指定事件处理程序。

### 优点

1. document 对象随时可用，任何时候都可以给它添加事件处理程序（不用等待 DOMContentLoaded
   或 load 事件）。这意味着只要页面渲染出可点击的元素，就可以无延迟地起作用。
2. 节省花在设置页面事件处理程序上的时间。只指定一个事件处理程序既可以节省 DOM 引用，也
   可以节省时间。
3. 减少整个页面所需的内存，提升整体性能。

### 其他

最适合使用事件委托的事件包括：click、mousedown、mouseup、keydown 和 keypress。
mouseover 和 mouseout 事件冒泡，但很难适当处理，且经常需要计算元素位置（因为 mouseout 会
在光标从一个元素移动到它的一个后代节点以及移出元素之外时触发）。

### event.target

`event.target `[event.target](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_event_target)属性可以用来实现**事件委托** (**event delegation**),在该模型中，事件对象有一个 `srcElement` 属性，等价于`target` 属性。

The target event property returns the element that triggered the event.

The target property gets the element on which the event originally occurred, opposed to the [currentTarget](https://www.w3schools.com/jsref/event_currenttarget.asp) property, which always refers to the element whose event listener triggered the event.

The currentTarget property does not necessarily return the element that was clicked on, but the element whose eventlistener triggered the event

```html
<ul id="myLinks"> 
 <li id="goSomewhere">Go somewhere</li> 
 <li id="doSomething">Do something</li> 
 <li id="sayHi">Say hi</li> 
</ul>

<script>
var item1 = document.getElementById("goSomewhere");
var item2 = document.getElementById("doSomething");
var item3 = document.getElementById("sayHi");

item1.addEventListener("click", function (event) {
  location.href = "http:// www.wrox.com";
});
item2.addEventListener("click", function (event) {
  document.title = "I changed the document's title";
});
item3.addEventListener("click", function (event) {
  console.log("hi");
});
</script>

<!--如果对页面中所有需要使用 onclick 事件处理程序的元素都如法炮制，结果就会出现大片雷同的只为指定事件处理程序的代码。使用事件委托，只要给所有元素共同的祖先节点添加一个事件处理程序，就可以解决问题。-->
<!---->
<script>
  //事件会向上冒泡，存在的父级都可以委托处理事件，这种方式占用的内存更少
var list = document.getElementById("myLinks");
list.addEventListener("click", function (event) {
  var target = event.target;

  switch (target.id) {
    case "doSomething":
      document.title = "I changed the document's title";
      break;

    case "goSomewhere":
      location.href = "http:// www.wrox.com";
      break;

    case "sayHi":
      console.log("hi");
      break;
  }
}); 
</script>

```

## 移除事件处理程序

```html
<div id="myDiv"> 
	<input type="button" value="Click Me" id="myBtn"> 
</div> 

<script type="text/javascript"> 
//问题在于，按钮被删除之后仍然关联着一个事件处理程序。在<div>元素上设置 innerHTML 会完全删除按钮，但事件处理程序仍然挂在按钮上面。
let btn = document.getElementById("myBtn");

btn.onclick = function () {
  // 执行操作
  document.getElementById("myDiv").innerHTML = "Processing..."; // 不好！
};
</script>
```

```html
<div id="myDiv"> 
 	<input type="button" value="Click Me" id="myBtn"> 
</div> 

<script type="text/javascript"> 
let btn = document.getElementById("myBtn");
btn.onclick = function () {
  // 执行操作
  btn.onclick = null; // 删除事件处理程序
  document.getElementById("myDiv").innerHTML = "Processing..."; // 不好！
};
</script>
```

按钮的事件处理程序先被删除了。这样就可以确保内存被回收，按钮也可以安全地从 DOM 中删掉。
但也要注意，在事件处理程序中删除按钮会阻止事件冒泡。只有事件目标仍然存在于文档中时，事件才会冒泡。

## simulating events

# scripting forms

表单脚本

# Exception handling

```js
try{
//some code that chould fail
//the try block is where you put code that could fail
}
catch(error){
  //do something with the error
  //an error object is passed to the catch block
}
finally{
  //this code always runs,optional
}
```

```js
    function simpleTryCatch() {
      let result;

      try {
        result = x / 10;
      } catch (error) {
        console.log(error.message);
      }
    }
```

a js error object always has "name" and "message" properties and pass it to the catch block

自定义输出错误内容：you can throw your own custom error,create an object with at least two properties:"message",and "name"

```js
      function throwError() {
        try {
          attemptDivision();
        } catch (error) {
          console.log(error.message + " - Error Type: " + error.name);
        }
      }

      function attemptDivision() {
        let result;

        try {
          result = x / 10;
        } catch (error) {
          // Always include at least a 'message' and 'name' properties
          throw {
            message:
              "In the attemptDivision() method the following error occurred: " +
              error.message,
            name: "CustomError",
          };
        }
      }

```

### types of errors

ReferenceError

RangeError

TypeError

URIError

SyntaxError 

EvalError.(in some older code)























