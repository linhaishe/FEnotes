### 链式调用

`$('#xx').a().b().c()...`

这种不断的向下连续调用不同的js方法的写法，就叫链式调用

```javascript
function xxfn(){
	// 私有方法
	function b(){
		return 123
	}
    //返回的是b function 不是123，因为没有执行
    //注意返回并调用
	return b;
}

//隐含着一个闭包的操作，
var _xx = xxfn()();
console.log( _xx )

//var _xx = xxfn();
//console.log( _xx())

//以上返回值相同
```

### valueOf()

all objects have toLocaleString( ), toString( ), and valueOf( ) methods.toString( ):数组返回字符串，valueOf( )转换数组而返还的是数组。隐式调用。会直接返回。

toString() behind the scenes to get the same result as when toString() is called directly.

```javascript
var colors = [“red”, “blue”, “green”];    //creates an array with three strings 
alert(colors.toString());    //red,blue,green 
alert(colors.valueOf());     //red,blue,green 
alert(colors);               //red,blue,green 
```



```javascript
function xxfn(){
	return xxfn;
	// console.log( xxfn );//指向函数本身
	// console.log( this ); //指向window
}

// 修改、重写，隐式调用的 valueOf 方法,不影响运行
xxfn.valueOf = function(){
	return 111;
}

var _x = xxfn();

console.log( _x )
```




```javascript
function addFn(n){
	var _num = n;
  //n，是addFn第一次执行时的值，初始值
  //var _n = addFn(1)，返回的是 return _b ,_b函数整体，第一次传值都只有这个结果
	// 私有方法，链式不断调用它，
	var _b = function( _m ){
		_num += _m;
		console.log( _num )
		return _b;
	}

	_b.valueOf = function(){
		return _num;
	}

	// 第一次执行addFn的时候，返回这行_b
	return _b;

}
//addFn() = _b
//addFn()() = _b()
//不断的在_b函数中传入参数，因为不断返回，就会不断调用
var _v = addFn(1)(2)(3)(4)

console.log( _v )
```



### 设计模式

- [JavaScript 事件参考手册](http://www.runoob.com/jsref/dom-obj-event.html)
- [JS事件模型](https://segmentfault.com/a/1190000006934031)

设计模式很多各类，但实际工作中，前端开发用的比较多为三种。设计模式应用的前提之一，要理解面向对象（Object-Oriented）

1. 原型，prototype、constructor

2. 观察者，VueJs的MVVM模式，就是观察者的典型应用

3. 单例，jQuery就是单例模式的典型应用

#### 观察者模式

Observer pattern (观察者模式)，又被称为发布-订阅（Publish/Subscribe）模式

<mark>代码能看懂，但是对这种模式的意思不了解，需要再深入</mark>

```javascript
function fn(){
  a();
  b();
  c();
}

function a(){
  console.log("aaa");
}

function b(){
  console.log("bbb")
}

function c(){
  console.log("ccc")
}
```

```javascript
// - 发布者；（被观察者），它有一个方法
var pub = {
	publishFn:function(){
		_dep.notify() 
	}
}

// - 订阅者：（观察者）
var sub1 = {updata:function(){console.log('1111')}}
var sub2 = {updata:function(){console.log('2222')}}
var sub3 = {updata:function(){console.log('3333')}}


// - 主题对象，订阅者都在主题对象中被注册
function Dep(){
	this.subs = [sub1,sub2,sub3]
}
Dep.prototype.notify = function(){
	console.log( this )
	for(var i=0; i<this.subs.length; i++){
		this.subs[i].updata()
	}
}

// 发布消息
var _dep = new Dep();

// 发布者，发布消息，主题对象执行，订阅者被触发
pub.publishFn();
```

### 面向对象

设计模式应用的前提之一，要理解面向对象（Object-Oriented）

面向对象编程有一个典型的标志，就是类的概念，通过类可以创建多个有相同属性、方法的对象实例。但是js没有类，所以js当中的对象也和传统的开发语言不一样。

对象是一组无序的键值对的集合，每个键名字就是对象的属性，每个属性，对应着一个值，字典模式。

![Xnip2019-10-08_22-03-26.png](http://ww1.sinaimg.cn/large/005NUwygly1g7r5bm7oq5j30iw0a80ua.jpg)

