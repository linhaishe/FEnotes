# Classes

# Class basic syntax

## intro

> *In object-oriented programming, a* *class* *is an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods).*
>
> 在面向对象编程中，一个类是一个可扩展的程序代码模板，用于创建对象，并提供状态的初始值（成员变量）和行为的实现（成员函数或方法）；类是一种封装了数据和方法的模板或蓝图，它可以被用来创建具有相似属性和方法的对象。

Classes are syntactic sugar that overlay the current constructor- and prototype-based approach to types. ([Not just a syntactic sugar](https://javascript.info/class#not-just-a-syntactic-sugar))

类是一种语法糖，它覆盖了当前基于构造函数和原型的类型定义方法。类是在当前的构造函数和原型的基础上添加的一种更为简单、直观的语法糖，方便开发者定义和创建对象。

## basic syntax

A class element can be characterized by three aspects:

Kind: Getter, setter, method, or field
Location: Static or instance
Visibility: Public or private

## 定义类

### 类声明式

⚠️**No comma between class methods**

```js
// 类声明 
class Person {}
```

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

```js
class User {
  constructor(name) {
    this.name = name;
  }

  sayHi() {
    alert(this.name);
  }
}

// Usage:
let user = new User("John");
user.sayHi();
```

### 类表达式

```js
// 类表达式 
const Animal = class {};
```

## class in pure functions/普通构造函数

与函数表达式类似，类表达式在它们被求值前也不能引用。不过，与函数定义不同的是，虽然函数声明可以提升，但类定义不能。

```js
// 传统的类写法，普通构造函数
// rewriting class User in pure functions

// 1. Create constructor function
function Person(name) {
  this.name = name;
}
// a function prototype has "constructor" property by default,
// so we don't need to create it

// 2. Add the method to prototype
Person.prototype.sayHi = function() {
  alert(this.name);
};

// Usage:
let user = new Person("John");
user.sayHi();
```

```js
// 使用 class 的写法
class Person1 {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const person = new Person1("Bob", 30);
console.log(person1.name); // 输出 "Bob"
console.log(person1.age); // 输出 30
```

## 普通构造函数和类构造函数的区别

1. 使用class关键字创建的函数被标记为具有特殊的内部属性[[IsClassConstructor]]: true，因此与手动创建的函数不完全相同。
2. 类的方法是不可枚举的，这是因为类定义将所有方法的枚举标志设置为false
3. 类中的所有代码都自动处于严格模式

| 类构造函数                          | 普通构造函数                    |
| ----------------------------------- | ------------------------------- |
| 使用 class 关键字定义               | 使用 function 关键字定义        |
| 使用 constructor 关键字定义构造函数 | 函数名即为构造函数              |
| 可以使用 static 关键字定义静态方法  | 可以使用 prototype 定义原型方法 |
| 可以使用 extends 关键字实现继承     | 可以使用原型链实现继承          |
| 类方法默认不可枚举                  | 方法可枚举                      |
| 类方法内部默认为严格模式            | 函数内部默认为非严格模式        |
| 可以使用 class fields 定义实例属性  | 需要在构造函数内部定义实例属性  |

## class getter/setter

Just like literal objects, classes may include getters/setters, computed properties etc.

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

## Class fields/类字段

“Class fields” is a syntax that allows to add any properties.

“Class fields”是一种语法，它允许我们在类中直接添加任何属性，包括静态属性和实例属性，而不必通过构造函数或原型链来定义。使用class fields语法，我们可以在类中直接定义属性并初始化它们。

```js
class User {
  name = "John"; // 实例属性
  static className = "User"; // 静态属性
}
```

```js
class Person {
  name = '';
  age = 0;

  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const person2 = new Person();
console.log(person2.name); // undefined
console.log(person2.age); // undefined
```

类构造函数会按照顺序执行，如果在执行 `constructor` 函数时没有为 `name` 和 `age` 定义对应的值，那么它们就会是 `undefined`，而不是默认值。

```js
class Person {
  name = '';
  age = 0;

  constructor(name, age) {
    this.name =  name || this.name;
    this.age = age || this.age;
  }
}

const person1 = new Person(); // using default values
console.log(person1.name); // output: ''
console.log(person1.age); // output: 0
```

#  The Class Constructor

类构造函数

The constructor method is a special method of a class for creating and initializing an object instance of that class.

constructor 关键字用于在类定义块内部创建类的构造函数。 方法名constructor 会告诉解释器 在使用new操作符创建类的新实例时，应该调用这个函数。

==构造函数的定义不是必需的，不定义构造函数相当于将构造函数定义为空函数。==

```js
class Person {
  name = 'John';
  age = 30;
}

const person = new Person();
console.log(person.name); // Output: "John"
console.log(person.age); // Output: 30
```

在这个例子中，虽然没有显式地定义构造函数，但在创建 `Person` 类的实例时，仍会默认调用一个空的构造函数来初始化实例的属性。因此，`person` 实例的 `name` 属性被初始化为字符串 "John"，`age` 属性被初始化为数字 30。

## 使用 new 调用类的构造函数会执行如下操作

1. 在内存中创建一个新对象。 
2. 这个新对象内部的[[Prototype]]指针被赋值为构造函数的 prototype 属性。 
3. 构造函数内部的 this 被赋值为这个新对象（即 this 指向新对象）
4. 执行构造函数内部的代码（给新对象添加属性）
5. 如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象。

```js
class Animal {}
class Person {
  constructor() {
    console.log("person 111");
  }
}
class Vegetable {
  constructor() {
    this.color = "orange";
  }
}
let a = new Animal();
let p = new Person(); // person 111 
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

```js
function Person() {} 
class Animal {} 
// 把window作为this来构建实例 
let p = Person(); 
let a = Animal(); 
// TypeError: class constructor Animal cannot be invoked without 'new'
```

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

# Instance, Prototype, and Class Members 

笔记中涉及到prototype的内容：

[d. Prototype pattern](# d. Prototype pattern)

[prototype chaining](# prototype chaining)

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

![image-20221104212058224](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/image-20221104212058224.png)

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

![image.png](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/005NUwygly1h7terukl9wj30so0iugpl.jpg)

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

# Inheritance

## Inheritance Basics

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

## Constructors, HomeObjects, and super() 

**构造函数、HomeObject 和super() **

### [Overriding a method](https://javascript.info/class-inheritance#overriding-a-method)

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

![image.png](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/005NUwygly1h7te5iwulej31b20uudqd.jpg)

### [Overriding constructor](https://javascript.info/class-inheritance#overriding-constructor)

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

We can override not only methods, but also class fields. 原生方法会被继承类重写时覆盖，字段也会。

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
