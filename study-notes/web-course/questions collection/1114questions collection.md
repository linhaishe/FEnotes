### html css 部分问题

#### 问题1

问题：浮动元素定位问题，为什么444和555的内容重叠了？

4和5没有设置浮动，按照我的理解，在3设置float：left时候，4应该向上移动到3的位置，5移动到4的位置，为什么444和555的内容重叠了(pic1)？3设置为float:right之后，显示的是我所理解的浮动作用的效果。(pic2)

![Xnip2019-11-03_12-47-05.png](http://ww1.sinaimg.cn/large/005NUwygly1g8krjfe8n9j31ve0yg7c9.jpg)

![Xnip2019-11-03_12-53-15.png](http://ww1.sinaimg.cn/large/005NUwygly1g8krjffmvcj31w00sk44g.jpg)

#### 问题2

关于页面布局，我不是很清楚页面布局使用规则，没有很好的使用思维去决定一个网页应该用什么样的布局。

主要混淆点，css grid , css float , 

如果可以希望老师能根据下面一些网站的小作业和我说一下页面布局大概的逻辑。

[FCC: Product Landing Page](https://codepen.io/freeCodeCamp/full/RKRbwL)
[FCC: Technical Documentation Page](https://codepen.io/freeCodeCamp/full/NdrKKL)
[FCC: Personal Portfolio](https://codepen.io/freeCodeCamp/full/zNBOYG)
[nasa网页](https://www.nasa.gov/)

### js 部分问题

#### 问题1

callback(),自己改了下输出函数，为什么输出值会是undefined，callback()不就是直接执行了函数吗？

![Xnip2019-11-09_22-24-56.png](http://ww1.sinaimg.cn/large/005NUwygly1g8s5q73dhjj317q0kwn32.jpg)

#### 问题2

关于原型继承

1. inheriting behavior from the supertype (or parent) 

`Animal`: making a new instance of `Animal`. 

<mark>问题在这里：同样是创建新实例，为什么例子2是直接new出prototype，而不直接new构造器，为什么要这样处理呢？</mark>

例子1

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

例子2

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

```javascript
function Animal() { }

Animal.prototype = {
  constructor: Animal,
  eat: function() {
    console.log("nom nom nom");
  }
};

function Dog() { }

Dog.prototype = Object.create(Animal.prototype);

let beagle = new Dog();
beagle.eat();  

// Should print "nom nom nom"
```

```javascript
function Animal() { }
Animal.prototype.eat = function() {
  console.log("nom nom nom");
};
function Bird() { }
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;

Bird.prototype.fly = function() {
  console.log("I'm flying!");
};

let duck = new Bird();
duck.eat(); // prints "nom nom nom"
duck.fly(); // prints "I'm flying!"
```

#### 问题3

（利用原型让一个引用类型继承另一个引用类型的属性和方法）

根据解析图，FIGURE6-4,subType为什么没有继承getSuperValue()的方法？

```javascript
//combination constructor and prototype
function SuperType(){
    this.property = true; 
}
SuperType.prototype.getSuperValue = function(){
    return this.property; 
};

//combination constructor and prototype
function SubType(){
    this.subproperty = false; 
}
//inherit from SuperType 
SubType.prototype = new SuperType();
SubType.prototype.getSubValue = function (){
    return this.subproperty; 
};
var instance = new SubType(); 
alert(instance.getSuperValue());   //true 
```

![P204.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8wed71u3kj30io0b40t6.jpg)

### 闭包

#### 问题1

我在控制台输入这两个例子，得出的结果是一样的，第二个例子没有强制输出各自不同的索引值，我应该怎么操作才会输出各自不同的索引值？

例子1：

```javascript

//只会返回10，即使是遍历函数，最终结果是10，不会返回各自不同的索引值

function createFunctions(){
  //var result = new Array();
  var result = [];
  for (var i=0; i < 10; i++){
    result[i] = function(){
      return i;
    };
  }
  return result; 
} 
createFunctions()
```

例子2：

```javascript
//强制返回各自不同的索引值

function createFunctions(){
  var result = [];
  for (var i=0; i < 10; i++){
    result[i] = function(num){
      return function(){
        return num;
      };
    }(i);
  }
  return result;
}
createFunctions()
```

### 计算机demo的问题

#### 问题1 demo2的问题

数字运行不能显示在html上，希望老师能帮我看下。

#### 问题2 demo3的问题

想在除法中的for循环加入判断，输出失败，希望老师能帮我看下。

![Xnip2019-11-14_20-43-53.png](http://ww1.sinaimg.cn/large/005NUwygly1g8xwefq382j30q60l4mzv.jpg)