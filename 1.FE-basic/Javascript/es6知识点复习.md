Pluralsight React notes

react is a library not a framework

Code sandbox: 在线写react网站，可以不用create-app

# React's basic concepts

React component

1. Function component
2. class component
3. Use upper case for component, for not using as function

```jsx
function Hello() {
	//return <div>Hello React!</div>;
  return React.createElement('div',null,"hello");
}

ReactDOM.render(
  //<Hello />, 
  React.createElement(Hello,null),
  document.getElementById('mountNode'),
);
```

render 的场景

```jsx
const render=()=>{
  document.getElementById('mountNode').innerHTML = `
	<div>
    Hello HTML
    <input />
    <pre>${new Date().toLocaleTimeString()}</pre>
  </div>
`;

ReactDOM.render(
  React.createElement(
    'div', 
    null, 
    'Hello React',
    React.createElement('input',null),
    React.createElement('pre',null,new Date().toLocaleTimeString())
  ),
  document.getElementById('mountNode2'),
);
  
}


// 	currentTime: new Date().toLocaleTimeString()
setInterval(render, 1000);



```

# es6知识点复习

## arrow-vs-regular-functions

```js
const X = function() {
  // "this" here is the caller of X
};

const Y = () => {
  // "this" here is NOT the caller of Y
  // It's the same "this" found in Y's scope
};

/*
  
  Regular functions give access to their "calling" environment while arrow functions give access to their "defining" environment 
  
  
  The value of the "this" keyword inside a regular function depends on HOW the function was CALLED (the OBJECT that made the call).
  
  The value of the "this" keyword inside an arrow function depends on WHERE the function was DEFINED (the SCOPE that defined the function).
  
  */

// console.log(this);

const testerObj = {
  func1: function() {
    console.log('In func1', this);
  },

  func2: () => {
    console.log('In func2', this);
  }
};

testerObj.func1();
testerObj.func2();

// const square1 = (a) => {
// 	return a * a;
// };
// const square2 = (a) => a * a;
// const square3 = a => a * a;

display.log([1, 2, 3, 4].map(a => a * a));

```

```jsx
const mystery = 'answer';
const InverseofPI = 1/math.PI;
const obj={
  p1:10,
  p2:20,
  f1(){},
	f2:()=>{},
  [mystery]:42,
  InverseofPI:InverseofPI,
  InverseofPI,
  //the same
}

console.log(obj.answer)  

// undefined
console.log(obj.mystery)
```

## object Destructuring

```js
// const PI = Math.PI;
// const E = Math.E;
// const SQRT2 = Math.SQRT2;

const {PI, E, SQRT2}  = Math;

// Somewhere in a React App
// const {Component, Fragment, useState} = require('react');
// useState();

const circle = {
  label: 'circleX',
  radius: 2,
};
//此处解析：
//precision等于一个对象，相当于{radius}从circle中取出，也相当于
//{radius}=
//  {
//  label: 'circleX',
//  radius: 2,
//}

//precision如果没有被置顶则使用默认值2
const circleArea = ({radius}, {precision = 2}={}) =>
  (PI * radius * radius).toFixed(precision);

console.log(
  //precision被重新指定，使用参数值3
  circleArea(circle, { precision: 3 })
);

// const [first, second,, forth] = [10, 20, 30, 40];

// const [value, setValue] = useState(initialValue);
```

## Array Destructuring

```js
const [first, ...restOfItems] = [10, 20, 30, 40];
//shadow copy
const newArray = [...restOfItems];

// console.log(first);
// console.log(restOfItems);

const data = {
	temp1: '001',
  temp2: '002',
  firstName: 'John',
  lastName: 'Doe',
};

const {temp1, temp2, ...person} = data;

const newObject = {
  ...person
}

console.log(newObject)
```

## Template-string

```js
const greeting = "Hello World";

const answer = 'Forty Two';

const html = `
  <div>
    ${Math.random()}
  </div>
`;
```

## classes

```js
class Person {
  constructor(name) {
    this.name = name;
  }
  greet() {
    console.log(`Hello ${this.name}!`);
  }
}

class Student extends Person {
  constructor(name, level) {
    super(name);
    this.level = level;
  }
  greet() {
    console.log(`Hello ${this.name} from ${this.level}`);
  }
}

const o1 = new Person("Max");
const o2 = new Student("Tina", "1st Grade");
const o3 = new Student("Mary", "2nd Grade");
o3.greet = () => console.log('I am special!');

o1.greet();
o2.greet();
o3.greet();
```

## promises

```js
// const fetchData = () => {
//   fetch('https://api.github.com').then(resp => {
//     resp.json().then(data => {
//       console.log(data);
//     });
//   }); 
// };

const fetchData = async () => {
  const resp = await fetch('https://api.github.com');
  const data = await resp.json();
  console.log(data);
};

fetchData();

```

from vlidation

client side routing with html5 pushState

pushStateallows js to update the browser url

uses proper URLs

requires server-side support



stopwatch demo

getstate()

dispatch()

subscribe()



two demo 

1. author quiz
2. stopwitch

first understand react and redux by themselves befor adding the extra complexity of react-redux





