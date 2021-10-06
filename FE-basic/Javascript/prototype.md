When defining a custom constructor, the prototype gets the constructor property only by default; all other methods are inherited from Object. Each time the constructor is called to create a new instance, that instance has an internal pointer to the constructor’s prototype. In ECMA-262 fifth edition, this is called [[Prototype]]. There is no standard way to access [[Prototype]] from script, but Firefox, Safari, and Chrome all support a property on every object called __proto__.; in other implementations, this property is completely hidden from script. The important thing to understand is that a direct link exists between the instance and the constructor’s prototype but not between the instance and the constructor. 

Each instance of Person, person1, and person2 has internal properties that point back to Person.prototype only; each has no direct relationship with the constructor. 

```javascript
function Gadget(name, color) {
    this.name = name;
    this.color = color;
    this.whatAreYou = function() {
        return 'I am ' + this.color + '  ' + this.name; 
    }
}

var newobj = new Gadget('car','red')

return newobj.constructor.prototype === Gadget.prototype
```

```javascript
.__proto__ = .constructor.prototype
//most of ，需考虑constructor是否被更改
```

<mark>1. JavaScript中一切皆是对象</mark>
<mark>2. 所有对象有[[prototype]] ，指向其构造函数的原型对象</mark>
<mark>3. 所有函数都有prototype属性，指向其原型对象</mark>
<mark>4. 所有实例都有constructor属性，指向其构造函数</mark>
<mark>5.每个对象都有` __proto__`属性，它指向的是[构造函数的prototype属性]（指向的对象</mark>

<mark>所有函数原型是一个对象</mark>

```js
function fn(){}

fn.prototype
//{}

fn.prototype.__proto__
//Object

fn.prototype.constructor.prototype === Object.prototype
//false
fn.prototype.__proto__ === Object.prototype
//true
```

Function构造函数的构造函数是Object,即函数自己的构造函数是对象Object,所有js对象的基类。

```js
function fn(){}
Function.prototype.__proto__
```

函数Gadget的原型是空对象Object，所有函数的构造函数都是Function

```javascript
function Gadget(a,b) {
    return a+b;
}
Gadget.prototype
//是空对象Object{},
//{constructor:f}
//所有函数的构造函数都是Function
Gadget.constructor
//constructor指向其构造函数的原型对象Gadget(a,b)
//ƒ Function() { [native code] }
```

## 使用原型给对象添加方法和属性

```javascript
//不使用原型，使用构造函数给对象添加属性和方法的是通过this
function Gadget(name, color) {
    this.name = name;
    this.color = color;
    this.whatAreYou = function() {
        return 'I am ' + this.color + '  ' + this.name; 
    }
}
//此时，Gadget.prototype对象为空对象
//利用原型属性给对象添加方法和属性

Gadget.prototype.price = 100;
Gadget.prototype.rating = 3;
Gadget.prototype.getInfo = function() {
    return 'Rating: ' + this.rating +', price: ' + this.price;
}
```

## 使用原型对象的属性和方法

New operator

```javascript
var newtoy = new Gadget('car','red')
```

每个实例/对象都有constructor属性，只有函数才有prototype属性，通过constructor可以访问实例的prototype。

```javascript
.__proto__ === .constructor.prototype
//most of ，需考虑constructor是否被更改
```

```javascript
newtoy.__proto__ === newtoy.constructor.prototype
//true
```

函数的[[Prototype]]指着函数的构造构造函数Function的prototype属性。

```js
(function(){}).__proto__ === Function.prototype 
//true
```

![](https://pic1.zhimg.com/80/92241be9f5f60797d6b3b8f280c475c0_hd.jpg)

```javascript
Foo.prototype.__proto__.prototype
//undefined
Object.prototype
//所有js对象的基类的prototype的值，为null

Foo.prototype 为对象，所有对象有[[prototype]] ，Foo.prototype.__proto__指向其构造函数的原型对象，其构造函数为Object(妈)，则其构造函数的原型对象为Object.prototype

默认构造函数的原型同时拥有constructor，__proto__，属性。
其余对象则.__proto_ === .constructor.prototype
```

<mark>三种构造一个对象的方法，分析三种构造对象的方法如何决定[[prototype]]属性</mark>

1. 这个对象是通过**对象字面量**构造出来的

其[[prototype]]指向Object.prototype

```js
var person1 = {
    name: 'cyl',
    sex: 'male'
};

person1.__proto__ === Object.prototype

person1.__proto__ === person1.constructor.prototype

//all true
```

2. 这个对象是由**构造函数**构造出来的

通过new操作符调用的函数就是构造函数。由构造函数构造的对象，其[[prototype]]指向其**构造函数的prototype**属性指向的对象。每个函数都有一个prototype属性，其所指向的对象带有constructor属性，这一属性指向函数自身。

```javascript
function Person(){}
var person2 = new Person();

person2.__proto__ === Person.prototype
person2.constructor.prototype === Person.prototype

//all true

//因为Object是自然存在的，直接new出来即可，也为构造函数
var two = new Object();
two.__proto__ === Object.prototype // true
```

对象的`__proto__`和函数的prototype，用途是一样的，都是为了要找到它们各个的构造函数。

3. 这个对象是由**函数Object.create()**构造的。

```js
var person1 = {
    name: 'cyl',
    sex: 'male'
};

var person2 = Object.create(person1);

person2.__proto__ === person1
//true
person2.constructor.prototype === Object.prototype
//true
person2.__proto__ === person1.prototype
//false
```

```js
var p = {
  name:'xxx',
  sex:'female'
};

Object.create = function(p) {
    function f(){}
    f.prototype = p;
    return new f();
}
//修改了原型指向，指向参数p，
```
