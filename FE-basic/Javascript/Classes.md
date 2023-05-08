# classes

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

## function constructor/普通构造函数

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

## Class fields / 类字段

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

类字段重写

如果一个类扩展了另一个类并且没有 constructor，那么将生成下面这样的“空” constructor

```js
class Rabbit extends Animal {
  // 为没有自己的 constructor 的扩展类生成的,调用了父类的 constructor，并传递了所有的参数
  constructor(...args) {
    super(...args);
  }
}
```

```js
class Animal {
  name = 'animal';

  constructor() {
    alert(this.name); // (*)
  }
}
// 一个类扩展了另一个类并且没有 constructor
class Rabbit extends Animal {
  name = 'rabbit';
}

new Animal(); // animal
new Rabbit(); // animal

// new Rabbit() 调用了 super()，因此它执行了父类构造器，并且（根据派生类规则）只有在此之后，它的类字段才被初始化。在父类构造器被执行的时候，Rabbit 还没有自己的类字段，这就是为什么 Animal 类字段被使用了。

// 父类构造器总是会使用它自己字段的值，而不是被重写的那一个。
```

```js
class Animal {
  showName() {  // 而不是 this.name = 'animal'
    alert('animal');
  }

  constructor() {
    this.showName(); // 而不是 alert(this.name);
  }
}

class Rabbit extends Animal {
  showName() {
    alert('rabbit');
  }
}

new Animal; // animal
new Rabbit(); // rabbit
```

原因在于字段初始化的顺序。类字段是这样初始化的：

- 对于基类(base class)（还未继承任何东西的那种），在构造函数调用前初始化。
- 对于派生类，在 `super()` 后立刻初始化。



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

**使用 new 调用类的构造函数会执行如下操作**

1. 在内存中创建一个新对象。 
2. 这个新对象内部的`[[Prototype]]`指针被赋值为构造函数的 prototype 属性。 
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

类块(class body)

笔记中涉及到prototype的内容：

[d. Prototype pattern](# d. Prototype pattern)

[prototype chaining](# prototype chaining)

## Instance Members

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

## Prototype Methods and Accessors  

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

**可以把方法定义在类构造函数中或者类块(class body)中， 但不能在类块中给原型添加原始值或对象作为成员数据： **

```js
class Person {  
  name: 'Jake' 
} // caught SyntaxError: Unexpected identifier 'name'
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

## Static Class Methods and Accessors

**静态类方法**

可以在类上定义静态方法。这些方法通常用于执行不特定于实例的操作，也不要求存在类的实例。与原型成员(prototype members)类似，静态成员每个类上只能有一个。

Usually, static methods are used to implement functions that belong to the class as a whole, but not to any particular object of it.

new 出来的对象访问不到父类的 static methods。

==Static methods aren’t available for individual objects.==, 但是extends的类available，就可以用static的方法/属性。

一个类可以通过 `extends` 关键字继承另一个类。这个新的类可以使用父类中的静态方法和属性，因为这些方法和属性是属于类本身的，而不是类的实例。

Static methods are callable on classes, not on individual objects.

```js
class Person {
  constructor() {
    // 添加到this的所有内容都会存在于不同的实例上
    this.locate = () => console.log("instance", this);
  } 
  
  // 定义在类的原型对象上 / Defined on the class prototype object
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

```js
class MyClass {
  static property = ...;

  static method() {
    ...
  }
}
```

```js
MyClass.property = ...
MyClass.method = ...
```

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

```js
// 定义一个父类 Animal
class Animal {
  static sayHello() {
    console.log('Hello from Animal!');
  }
}

// 定义一个子类 Dog
class Dog extends Animal {
  static sayHello() {
    console.log('Hello from Dog!');
    // 调用父类的静态方法
    super.sayHello();
  }
}

// 调用父类的静态方法
Animal.sayHello(); // 输出 "Hello from Animal!"

// 调用子类的静态方法
Dog.sayHello(); // 输出 "Hello from Dog!" 和 "Hello from Animal!"

```

**Summary**

静态方法用于属于整个类的功能。它与具体的类实例无关。

静态属性用于存储与实例无关的类级别数据。

对于 `class B extends A`，类 `B` 本身的原型指向 `A`：`B.[[Prototype]] = A`。因此，如果在 `B` 中找不到一个字段，搜索会继续在 `A` 中进行。

## Private and protected properties and methods

### protected properties and methods

- 利用get/set accessor 处理 property, 使用方法是直接赋值。
- 利用getter/setter function 处理  property，使用方法是函数传参。

Protected properties are usually prefixed with an underscore _.

```js
// get/set accessor 处理 property
class CoffeeMachine {
  _waterAmount = 0;// 内部的水量

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
// getter/setter function 处理  property
// 函数更灵活。它们可以接受多个参数
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

==Protected fields are inherited==

If we inherit class MegaMachine extends CoffeeMachine, then nothing prevents us from accessing this._waterAmount or this._power from the methods of the new class.

### readonly

不设置setter即可。

设为只读。有时候一个属性必须只能被在创建时进行设置，之后不再被修改。

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

### Private properties and methods

- 利用get/set accessor 处理 private property, 使用方法是直接赋值。
- 利用getter/setter function 处理 private property，使用方法是函数传参。

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

## Inheritance Basics / 继承基础

### extends

ES6类支持单继承。使用`extends`关键字，就可以继承任何拥有`[[Construct]]`和原型的对象。很大程度上，这意味着不仅可以继承一个类，也可以继承普通的构造函数（保持向后兼容）。

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

==**Any expression is allowed after** `extends`==

在`extends`后允许任意表达式

```js
function f(phrase) {
  return class {
    sayHi() { alert(phrase); }
  };
}

class User extends f("Hello") {}

new User().sayHi(); // Hello
```

## Constructors and super() 

这块内容主要介绍继承时，super、Constructors的使用和说明

我们不希望完全替换父类的方法，而是希望在父类方法的基础上进行调整或扩展其功能。我们在我们的方法中做一些事儿，但是在它之前或之后或在过程中会调用父类方法

派生类(derived class)指的是从另一个类（称为基类或父类）继承属性和方法的类。派生类可以使用`extends`关键字定义，并在其中实现新的功能或覆盖基类的行为。派生类还可以添加新的实例变量和方法，以扩展基类的功能。

派生类的方法可以通过`super`关键字引用它们的原型。这个关键字只能在派生类中使用，而且仅限于类构造函数、实例方法和静态方法内部。在类构造函数中使用`super`可以调用父类构造函数。

如果一个类扩展了另一个类并且没有 constructor，那么将生成下面这样的“空” constructor

```js
class Rabbit extends Animal {
  // 为没有自己的 constructor 的扩展类生成的,调用了父类的 constructor，并传递了所有的参数
  constructor(...args) {
    super(...args);
  }
}
```

派生的 constructor 必须调用 super 才能执行其父类（base）的 constructor，否则 this 指向的那个对象将不会被创建。并且我们会收到一个报错。

Classes provide "super" keyword for that.

- `super.method(...)` to call a parent method.
- `super(...)` to call a parent constructor (inside our constructor only).

具体而言，super 关键字有以下作用：

1. 在子类中调用父类的构造函数，以便初始化对象时使用父类的属性；
2. 在子类中调用父类的实例方法，以便在子类中重写父类方法但仍能够使用父类的行为；
3. 在子类中调用父类的静态方法，以便在子类中扩展父类的行为但仍能够使用父类的功能。

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  static run() {
    console.log(this.name + ' has run away.');
  }
  
  speak() {
    console.log(this.name + ' makes a noise.');
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    // 不要在调用super()之前引用this，否则会抛出ReferenceError
    super(name); // 调用父类的构造函数
    this.breed = breed;
  }
  
  speak() {
    console.log(this.name + ' barks.'); // 重写了父类的 speak 方法
    super.speak(); // 调用父类的 speak 方法
  }
  
  // 在静态方法中可以通过 super 调用继承的类上定义的静态方法
  static info() {
    console.log('Dogs are loyal animals.');
    super.speak(); // 调用父类的 speak 方法
  }

  static run() {
    super.run();
  }
}

let fido = new Dog('Fido', 'Labrador Retriever');

fido.speak(); // 输出：Fido barks. Fido makes a noise.
Dog.info(); // 输出：Dogs are loyal animals. undefined makes a noise.
Dog.run();

```

```js
class Animal {

  constructor(name) {
    this.speed = 0;
    this.name = name;
  }

  // ...
}

class Rabbit extends Animal {

  constructor(name, earLength) {
    super(name);
    this.earLength = earLength;
  }

  // ...
}

// 现在可以了
let rabbit = new Rabbit("White Rabbit", 10);
alert(rabbit.name); // White Rabbit
alert(rabbit.earLength); // 10
```

**在使用`super`时，要注意的7个问题**

1. `super`只能在派生类构造函数和静态方法中使用。
2. 不能单独引用`super`关键字，要么用它调用构造函数，要么用它引用静态方法
3. 调用`super()`会调用父类构造函数，并将返回的实例赋值给`this`。
4. `super()`的行为如同调用构造函数，如果需要给父类构造函数传参，则需要手动传入。
5. 如果没有定义类构造函数，在实例化派生类时会调用`super()`，而且会传入所有传给派生类的参数。
6. 在类构造函数中，不能在调用`super()`之前引用`this`。
7. 如果在派生类中显式定义了构造函数，则要么必须在其中调用`super()`，要么必须在其中返回一个对象。
8. 箭头函数没有`super`

```js
class Rabbit extends Animal {
  stop() {
    setTimeout(() => super.stop(), 1000); // 1 秒后调用父类的 stop
    setTimeout(function() { super.stop() }, 1000); // 意料之外的 super
  }
}
```

## Abstract Base Classes / 抽象基类

抽象基类它可供其他类继承，但本身不会被实例化。

1. 通过`new.target`，在实例化时检测是不是抽象基类，可以阻止对抽象基类的实例化
2. 通过在抽象基类构造函数中进行检查，可以要求派生类必须定义某个方法

```js
class Animal { // 定义一个抽象基类
  constructor() {
    if (new.target === Animal) { // 判断是否是通过 Animal 实例化
      throw new Error('Cannot instantiate abstract class.'); // 抛出错误
    }
  }
  
  // 定义一个抽象方法
  makeSound() {
    throw new Error('Method must be implemented in derived classes.');
  }

  // 要求派生类必须定义某个方法
  if (!this.foo) {
    throw new Error('Inheriting class must define foo()');
    }
}

class Dog extends Animal { // 继承抽象类并实现 makeSound 方法
  makeSound() {
    console.log('Woof!');
  }
  foo() {}
}

const animal = new Animal(); // 抛出错误：Cannot instantiate abstract class.
const dog = new Dog();
dog.makeSound(); // 输出：Woof!
```

## Inheriting from Built-in Types / 继承内置类型

... skip ...

## (待优化)class mixin / 类混入

把不同类的行为集中到一个类

很多JavaScript框架(特别是React)已经抛弃混入模式，转向了组合模式(把方法 提取到独立的类和辅助对象中，然后把它们组合起来，但不使用继承)。“组合胜过继承(composition over inheritance)。”

一个策略是定义一组“可嵌套”的函数，每个函数分别接收一个超类作为参数，而将混入类定义为这个参数的子类，并返回这个类。这些组合函数可以连缀调用，最终组合成超类表达式。

`Person extends C extends B extends A`

```js
class Vehicle {}
let FooMixin = (Superclass) =>
  class extends Superclass {
    foo() {
      console.log("foo");
    }
  };
let BarMixin = (Superclass) =>
  class extends Superclass {
    bar() {
      console.log("bar");
    }
  };
let BazMixin = (Superclass) =>
  class extends Superclass {
    baz() {
      console.log("baz");
    }
  };
function mix(BaseClass, ...Mixins) {
  return Mixins.reduce(
    (accumulator, current) => current(accumulator),
    BaseClass
  );
}

class Bus extends mix(Vehicle, FooMixin, BarMixin, BazMixin) {}
let b = new Bus();
b.foo(); // foo
b.bar(); // bar
b.baz(); // baz

```
https://zh.javascript.info/mixins

ERROR

然后我们定义了一个空白类 Child，让它继承 Father 类，并使用 Object.assign() 方法将 Father、Mother 和 Mixin 混入到 Child 类中
```js
// 定义一个 Father 类和一个 Mother 类
class Father {
  constructor(x) {
    this.x = x;
  }
  
  say() {
    console.log('I am the father!');
  }
}

class Mother {
  constructor(y, z) {
    this.y = y;
    this.z = z;
  }
  
  tell() {
    console.log('I am the mother!');
  }
}

// 定义一个空白类，用于接受 mixin 的方法和属性并最终输出到目标类
class Child extends Father { }

// 定义一个 mixin 类，包含需要混入到 Child 类中的方法和属性
class Mixin {
  constructor(y, z) {
    this.y = y;
    this.z = z;
  }
  
  speak() {
    console.log('I can speak!');
  }
}

// 使用 Object.assign() 方法将 Father、Mother 和 Mixin 混合到 Child 类中
Object.assign(Child.prototype, Father.prototype, Mother.prototype, Mixin.prototype);

// 测试
const child = new Child(1, 2);
console.log(child.x); // 输出: 1
console.log(child.y); // 输出: 2
console.log(child.z); // 输出: 2
child.say(); // 输出: "I am the father!"
child.tell(); // 输出: "I am the mother!"
child.speak(); // 输出: "I can speak!"
```

# refs

1. https://javascript.info/classes
2. js 高程 4th chapter8
3. https://www.boldare.com/blog/how-to-use-javascript-classes/#prototype-based-classes
4. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor