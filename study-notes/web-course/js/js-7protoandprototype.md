## 对象创建
Refer  : Chapter 5 : Reference Types

1. new operation
2. Object.create()
3. 对象字面量表示法 Object literal notation 

<mark>`prototype`属性只有在函数中才有</mark>

`prototype` is only available on functions since they are derived from `Function`, `Function`, and `Object` but in anything else it is not. However, `__proto__` is available everywhere.

```javascript
var obj = new Object(); // not a functional object
obj.prototype.test = function() { alert('Hello?'); }; // this is wrong!

function MyObject() {} // a first class functional object
MyObject.prototype.test = function() { alert('OK'); } // OK
```

## proto和prototype

LINK:

[JavaScript. The Core.Dmitry Soshnikov](http://dmitrysoshnikov.com/ecmascript/javascript-the-core/)

`[[Prototype]]` (or `__proto__`) 

<mark>1. JavaScript中一切皆是对象</mark>
<mark>2. 所有对象有[[prototype]] ，指向其构造函数的原型对象</mark>
<mark>3. 所有函数都有prototype属性，指向其原型对象</mark>
<mark>4. 所有实例都有constructor属性，指向其构造函数</mark>
<mark>5.每个对象都有` __proto__`属性，它指向的是[构造函数的prototype属性]</mark>

2和5 是同一个意思

由构造函数构造的对象，其[[prototype]]指向其**构造函数的prototype**属性指向的对象 

每个函数都有一个prototype属性，其所指向的对象带有constructor属性，这一属性指向函数自身 

1、函数它的`__proto__`是一个对象，指向所有js对象的基类，Object对象；

2、所有js对象的基类的prototype的值，为null,也就是原型链的最顶端。

Object {}

函数它的`__proto__`是一个对象，指向所有js对象的基类，Object对象,即Object {}，Object {} 是所有js对象的基类(超类)

### 函数 里的 `__proto__`

创建的每个函数都有一个prototype属性，（个人理解，每个函数有自己的基因，这个基因被称为prototype）,这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法，如果按照字面意思来理解，那么prototype就是通过调用构造函数而创建的那个对象实例的原型对象。

使用原型对象的好处是可以让所有对象实例共享它所包含的属性和方法。换句话说，不必在构造函数中定义对象实例的信息，而是将信息直接添加到原型对象中。

This may not be an issue when there are only two instances, but imagine if there are millions of instances. That would be a lot of duplicated variables.

```javascript
function Person(){}
//构造函数成为空函数，将属性值添加在prototype属性中
Person.prototype.name = “Nicholas”; 
Person.prototype.age = 29; 
Person.prototype.job = “Software Engineer”; 
Person.prototype.sayName = function(){
  alert(this.name); 
};
var person1 = new Person(); 
person1.sayName();   //”Nicholas”
var person2 = new Person(); 
person2.sayName();   //”Nicholas”
alert(person1.sayName == person2.sayName);  //true 
```

Person构造函数的prototype属性，指向person prototype ，person prototype是一个对象，即object,所以console.log(Person.prototype),output "Object".

当你创建函数时，JS会为这个函数自动添加`prototype`属性，~~值是空对象~~ **值是一个有 constructor 属性的对象，不是空对象**。而一旦你把这个函数当作构造函数（`constructor`）调用（即通过`new`关键字调用），那么JS就会帮你创建该构造函数的实例，实例继承构造函数`prototype`的所有属性和方法（实例通过设置自己的`__proto__`指向承构造函数的`prototype`来实现这种继承。

`person1.__proto__=== Person.prototype`

![prototype chain.JPG](http://ww1.sinaimg.cn/large/005NUwygly1g8t0jo6zpwj316q0kyaen.jpg)

<mark>5.每个对象都有` __proto__`属性，它指向的是[构造函数的prototype属性]</mark>

对象{}，没有prototype属性，为了要找到它的构造函数，所以它有 `__proto__`属性

```javascript
var obj = {}
obj.prototype
//undefined
```

```javascript
var one = {x: 1};
var two = new Object();
one.__proto__ === Object.prototype // true
two.__proto__ === Object.prototype // true
one.toString === one.__proto__.toString // true
```

`two = new Object()`中`Object`是构造函数，所以`two.__proto__`就是`Object.prototype`。至于`one`，ES规范定义对象字面量的原型就是`Object.prototype`。

<img src="http://ww1.sinaimg.cn/large/005NUwyggy1g9bs1egr3oj30xx1677ci.jpg" alt="jsobj_full.jpg" style="zoom:33%;" />

函数的[[Prototype]]指着函数的构造构造函数Function的prototype属性。

```js
(function(){}).__proto__ === Function.prototype 
//true
```

1. `Function.prototype`和`Function.__proto__`都指向`Function.prototype`，这就是鸡和蛋的问题怎么出现的。
2. `Object.prototype.__proto__ === null`，说明原型链到`Object.prototype`终止。

<mark>1. JavaScript中一切皆是对象</mark>
<mark>2. 所有对象有[[prototype]] ，指向其构造函数的原型对象</mark>
<mark>3. 所有函数都有prototype属性，指向其原型对象</mark>
<mark>4. 所有实例都有constructor属性，指向其构造函数</mark>
<mark>5.每个对象都有` __proto__`属性，它指向的是[构造函数的prototype属性]（指向的对象</mark>