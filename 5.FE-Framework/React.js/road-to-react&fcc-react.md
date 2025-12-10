### intro

这里的笔记包含FCC的内容也包含THE ROAD TO REACT 的内容

[REACT documentation](https://reactjs.org/docs/jsx-in-depth.html#specifying-the-react-element-type)

Please consult the [React documentation](https://facebook.github.io/react/docs/state-and-lifecycle.html) for further details.

[React 中文网](https://react.docschina.org/)
[阮老师的教程](http://www.ruanyifeng.com/blog/2015/03/react.html)
[胡子课堂](http://huziketang.mangojuice.top/books/react/)

**什么是React，React有什么用**

React是Facebook在2013年开源在GitHub上的JavaScript库。React把用户界面抽象成一个个组件，如按钮组件Button、对话框组件Dialog、日期组件Calendar。开发者通过组合这些组件，最终得到功能丰富、可交互的页面。通过引人JSX语法，复用组件变得非常容易,同时也能保证组件结构清晰：有了组件这层抽象，React把代码和真实渲染目标隔离开来，除了可以在浏览器端渲染到DOM来开发网页外，还能用于开发原生移动应用。

**为什么用React**

因为react专注视图层，可以非常轻松地创建用户交互界面。为你应用的每一个**状态**设计简洁的视图，当数据改变时，react也可以**高效**的更新渲染界面。并且，react是**组件化**的，我们知道传统的html页面是通过一个一个html标签组合起来的，在react中，我们可以自由的创建所需要的组件

**如何使用React**

使用[Create React App](https://github.com/facebook/create-react-app)来创建一个React应用

### React JSX

[JSX语法简介](https://www.cnblogs.com/zourong/p/6043914.html)

**Intro:** React is an Open Source view library created and maintained by Facebook. It's a great tool to render the User Interface (UI) of modern web applications.

JSX就是Javascript和XML结合的一种格式。React发明了JSX，利用HTML语法来创建虚拟DOM。当遇到<，JSX就当HTML解析，遇到{就当JavaScript解析。

JSX elements 

React uses a syntax extension of JavaScript called JSX that allows you to write HTML directly within JavaScript. 

JSX is not valid JavaScript, JSX code must be compiled into JavaScript. 

include the code you want to be treated as JavaScript within curly braces:

 `{ 'this is treated as JavaScript code' }`.  

several JSX elements written as siblings with no parent wrapper element will not transpile. 

在React中，是可以不用JSX的，JSX其实是语法糖，比如`Hello World`这个JSX元素，可以通过 `React.createElement(component, props, ...chilfren)`(`React.createElement("h1",null,"Hello World")`)来创建。一旦使用了JSX，就需要引入React。JSX是如何翻译为普通JS的，可以通过[Babel编译器](https://babeljs.io/repl/#?babili=false&evaluate=true&lineWrap=false&presets=es2015%2Creact%2Cstage-0&code=function hello() {  return Hello world!<%2Fdiv>%3B })来将JSX翻译出来

`getName()`是一个JavaScript表达式，用在了JSX中，那么就需要用大括号包起来

**JSX本身也是一种表达式**

JSX最后会被编译为普通的JavaScript，所以普通的JavaScript的形式，JSX也是有的,可以在任何语句中使用JSX

```jsx
function getName() {
    return 'ZhangSan';
}

const element = (
	<h1>
        Hello {getName()}
  </h1>
)
```

几个没有父包装器元素的 兄弟元素 的JSX元素将不会转换。

```jsx
//Valid JSX:
<div>
  <p>Paragraph One</p>
  <p>Paragraph Two</p>
  <p>Paragraph Three</p>
</div>

const JSX = (
  <div>
    <h1>Hello World</h1>
    <p>Lets render this to the DOM</p>
  </div>
);
```

```jsx
//Invalid JSX:

<p>Paragraph One</p>
<p>Paragraph Two</p>
<p>Paragraph Three</p>
```

### comments

`{/* comments */}`

### HTML in JSX

1. className 进行类标签 ，而不是用class

2. <mark>JSX内用camelcase,小驼峰命名法</mark>， `onchange` becomes `onChange` 

   因为 JSX 的特性更接近 JavaScript 而不是 HTML , 所以 React DOM 使用 `camelCase` 小驼峰命名 来定义属性的名称，而不是使用 HTML 的属性名称

   you can find all the supported HTML [attributes]( https://reactjs.org/docs/dom-elements.html#all-supported-html-attributes ) in React’s documentation,

3. Self-Closing JSX Tags

```jsx
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

```jsx
const element = <img src={user.avatarUrl} />;
```

```JSX
const JSX = (
  <div className="myDiv">
    <h1>Add a class to this div</h1>
  </div>
);
```

Any JSX element can be written with a self-closing tag, and every element must be closed. in order to be valid JSX that can be transpiled.

 The difference is that in the first syntax version there is no way to include anything in the ` <div />  `

```JSX
{/* valid JSX */}

<br />

{/* 
valid JSX 
<div />  = <div></div>  
*/}
```

```JSX
const JSX = (
  <div>

    <h2>Welcome to React!</h2> 
    <br />
    <p>Be sure to close all tags!</p>
    <hr />

  </div>
);
```

1. js

   `var element = React.createElement('h1',{id:'myTitle'},title)`

2. Jsx

   `Var element  = <h1 id='myTitle'>{title}</h1>`

### JavaScript object in JSX

```jsx
const welcome = { 
greeting: 'Hey', 
title: 'React', 
}; 
function App() { 
  return ( 
  <div> 
    <h1> {welcome.greeting} {welcome.title} </h1> 
    <label htmlFor="search">Search: </label> 
    <input id="search" type="text" /> 
  </div> 
); 
} 
```

```jsx
function getTitle(title) { 
    return title; 
} 
function App() { 
    return ( 
        <div> 
            <h1>Hello {getTitle('React')}</h1> 
            <label htmlFor="search">Search: </label> 
            <input id="search" type="text" /> </div> 
    ); 
} 
```

###  React component 

#### advantage

React以组件的方式去思考用户界面的构成，将用户界面上的每一个功能相对独立的模块定义成组件，然后将小组件通过组合或嵌套的方式构成大组件，最终完成整体UI的构建。这种组件化的思想，可以让我们从功能的角度重新思考界面的构成，而且每个组件都是独立封装的。

1. 组件之前是独立的，不同组件之间的属性、状态互不干扰，耦合性低。
2. 组件可以相互组合，可以轻易复用
3. 易于维护和拓展。每个组件仅仅包含自身的逻辑，很容易维护。

**组件封装几个要素**

- 基本的封装性，尽管说JavaScript没有真正面向对象的方法，但我们还是可以通过实例化的方法来制造对象。
- 简单的生命周期，下一小节我们会讲到。
- 明确的数据流动，调用组件的时候可以给组件传递参数，组件根据参数的不同作出不同的响应。

#### Usage

####  1. use JavaScript function

a.  Defining a component in this way creates a ***stateless functional component***.  

​	 can receive data and render it, but does not manage or track changes to that data 

b.  React requires your function name to begin with a **capital letter**. 

you can find all the supported HTML [attributes]( https://reactjs.org/docs/dom-elements.html#all-supported-html-attributes ) in React’s documentation,

```jsx
// After being transpiled, the <div> will have a CSS class of 'customClass'
const DemoComponent = function() {
  return (
    <div className='customClass' />
  );
};
```

```jsx
const MyComponent = function() {
return (<div>xxx</div>);
};

{/*The text is considered a child of the div element, so you will not be able to use a self-closing tag.*/}

{/* babel transpiled Babel 编译后的JSX表达*/}

"use strict";

{/*simply write a JavaScript function that returns either JSX or null.*/}

var MyComponent = function MyComponent() {
  return React.createElement("div", null, "xxx");
};
```

A common pattern is to try to minimize statefulness and to create stateless functional components wherever possible. This helps contain your state management to a specific area of your application. In turn, this improves development and maintenance of your app by making it easier to follow how changes to state affect its behavior. 

一种常见的模式是尝试最小化状态，并在可能的情况下创建无状态功能组件。 这有助于将状态管理包含在应用程序的特定区域。 反过来，这使得您可以更轻松地了解状态更改如何影响其行为，从而改善了应用程序的开发和维护。

```jsx
class CampSite extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <Camper />
            </div>
        );
    }
};
// asw 1
const Camper = props => <p>{props.name}</p>;

Camper.defaultProps = {
    name: "CamperBot"
};

Camper.propTypes = {
    name: PropTypes.string.isRequired
};

//asw 2
const Camper = (props) => {
    return (
        <div>
            <p>{props.name}</p>
        </div>
    );
};

Camper.propTypes = {
    name: PropTypes.string.isRequired
};

Camper.defaultProps = {
    name: 'CamperBot'
};
```

#### 2.  use ES6 `class` syntax 

It uses `super()` to call the constructor of the parent class, in this case `React.Component`. The constructor is a special method used during the initialization of objects that are created with the `class` keyword. It is best practice to call a component's `constructor` with `super`, and pass `props` to both. This makes sure the component is initialized properly.  

```jsx
class Kitten extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>Hi</h1>
    );
  }
}
```

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        // change code below this line
        return (
            <div>
                <h1>Hello React!</h1>
            </div>
        )
        // change code above this line
    }
};

```

###   Component composition

JSX嵌套，JSX nested

```jsx
const ChildComponent = () => {
    return (
        <div>
            <p>I am the child</p>
        </div>
    );
};

class ParentComponent extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <h1>I am the parent</h1>
                { /* change code below this line */}
                <ChildComponent />
                { /* change code above this line */}
            </div>
        );
    }
};

```

Take the `TypesOfFruit` component and compose it, or *nest* it, within the `Fruits` component. Then take the `Fruits` component and nest it within the `TypesOfFood` component. The result should be a child component, nested within a parent component, which is nested within a parent component of its own! 

```jsx
const TypesOfFruit = () => {
  return (
    <div>
      <h2>Fruits:</h2>
      <ul>
        <li>Apples</li>
        <li>Blueberries</li>
        <li>Strawberries</li>
        <li>Bananas</li>
      </ul>
    </div>
  );
};

const Fruits = () => {
  return (
    <div>
      { /* change code below this line */ }
        <TypesOfFruit />
      { /* change code above this line */ }
    </div>
  );
};

class TypesOfFood extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Types of Food:</h1>
        { /* change code below this line */ }
        <Fruits />
        { /* change code above this line */ }
      </div>
    );
  }
};
```

```jsx
class Fruits extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h2>Fruits:</h2>
        { /* change code below this line */ }
        <NonCitrus />
        <Citrus />
        { /* change code above this line */ }
      </div>
    )
  }
}

class TypesOfFood extends React.Component {
  constructor(props) {
     super(props);
  }
    render() {
      return (
        <div>
        <h1>Types of Food:</h1>
          { /* change code below this line */ }
          <Fruits />
          { /* change code above this line */ }
          <Vegetables />
        </div>
      );
    }
};
```

###  render JSX elements

we can render this JSX directly to the HTML DOM using React's rendering API known as ReactDOM. 

` ReactDOM.render(componentToRender, targetNode) `

componentToRender ( first argument ) is the React element or component that you want to render

targetNode ( second argument ) is the DOM node that you want to render the component to. 

render JSX elements to the DOM 

```JSX
const JSX = (
  <div>
    <h1>Hello World</h1>
    <p>Lets render this to the DOM</p>
  </div>
);

ReactDOM.render(JSX,document.getElementById('challenge-node'));
```

### render React components

```jsx
//link: http://scriptoj.mangojuice.top/problems/1

//html
<div id='root'></div>

//answer 1,直接在ReactDOM.render()方法中写我们的标签
//app.js
function renderContent (content) {
    ReactDOM.render(
        <h1>{ content }</h1>,
        document.getElementById('root')
    )
}
```

```jsx
//answer 2,写一个类继承Component
function renderContent(content) {
    
    class Content extends Component(
        render() {
            return (
                <h1>{ content }</h1>
            )
        }
    )

    ReactDOM.render(
        <Content />,
        document.getElementById('root')
    )
}
```

```jsx
class TypesOfFood extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <h1>Types of Food:</h1>
                {/* change code below this line */}
                <Fruits />
                <Vegetables />
                {/* change code above this line */}
            </div>
        );
    }
};

// change code below this line
ReactDOM.render(<TypesOfFood />, document.getElementById('challenge-node'));
```

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
    }
    render(){
        return (
        <div>
        <h1>My First React Component!</h1>
        </div>
        )
    }
};

ReactDOM.render(<MyComponent />, document.getElementById('challenge-node'));
```

###  JSX props( properties )

JSX属性

Note that for `prop` values to be evaluated as JavaScript, they must be enclosed in curly brackets, for instance `date={Date()}`.

```jsx
const CurrentDate = (props) => {
  return (
    <div>
      {/*The syntax prop.propName is used to render a prop.*/}
      <p>The current date is: {props.date}</p>
    </div>
  );
};

class Calendar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>What date is it?</h3>
        {/*Define a prop named date in the Calendar component*/}
        <CurrentDate date={Date()} />
      </div>
    );
  }
};
```

### Pass an Array

to pass an array to a JSX element, it must be treated as JavaScript and wrapped in curly braces.

```jsx
<ParentComponent>
  <ChildComponent colors={["green", "blue", "red"]} />
</ParentComponent>
```

```jsx
const List = (props) => {
  return <p>{props.tasks.join(', ')}</p>
};

class ToDo extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>To Do Lists</h1>
        <h2>Today</h2>
        <List tasks={["walk","eat"]}/>
        <h2>Tomorrow</h2>
        <List tasks={["walk","eat","run"]}/>
      </div>
    );
  }
};

```

###  default prop 

declare a default prop, the syntax to be followed is 

```jsx
itemName.defaultProps = {
  prop-x: value,
  prop-y: value
}
```

```jsx
const ShoppingCart = (props) => {
  return (
    <div>
      <h1>Shopping Cart Component</h1>
      defaultProps = {}
    </div>
  )
};

// 指定默认值
ShoppingCart.defaultProps = {
  items: 0
};
```

```jsx
const Items = (props) => {
    return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
}

Items.defaultProps = {
    quantity: 0
}

class ShoppingCart extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        { /* change code below this line */ }
        return <Items quantity={10} />
        { /* change code above this line */ }
    }
};
```

### PropTypes

For example, you can check that a prop is a React element. Please refer to the [documentation](https://reactjs.org/docs/jsx-in-depth.html#specifying-the-react-element-type) for all of the options.

**Note:** As of React v15.5.0, `PropTypes` is imported independently from React, like this: `import PropTypes from 'prop-types';`

```jsx
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
};

// change code below this line
Items.propTypes = {
  quantity: PropTypes.number.isRequired
};
// change code above this line

Items.defaultProps = {
  quantity: 0
};

class ShoppingCart extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <Items />
  }
};
```

### this.props

passing a prop to is an ES6 class component

Render an instance of the `ReturnTempPassword` component in the parent component `ResetPassword`. Here, give `ReturnTempPassword` a prop of `tempPassword` and assign it a value of a string that is at least 8 characters long. Within the child, `ReturnTempPassword`, access the `tempPassword` prop within the `strong` tags to make sure the user sees the temporary password. 

```JSX
class ReturnTempPassword extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
            <p>Your temporary password is: <strong>{this.props.tempPassword}</strong></p>
        </div>
    );
  }
};

class ResetPassword extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
          <h2>Reset Password</h2>
          <h3>We've generated a new temporary password for you.</h3>
          <h3>Please reset this password from your account settings ASAP.</h3>
          { /* change code below this line */ }
          <ReturnTempPassword tempPassword="serrPbqrPnzc" />
          { /* change code above this line */ }
        </div>
    );
  }
};
```

###  state property

State consists of any data your application needs to know about, that can change over time. 

This initializes the component with `state` when it is created. The `state` property must be set to a JavaScript `object`. 

```JSX
this.state = {
  // describe your state here
}
```

```JSX
class StatefulComponent extends React.Component {
    constructor(props) {
        super(props);
        //initialize state in the constructor
        this.state = {
            name: "freecodecamp"
        }
    }
    render() {
        return (
            <div>
                <h1>{this.state.name}</h1>
            </div>
        );
    }
};
```

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: 'freeCodeCamp'
        }
    }
    render() {
        // change code below this line
        const name = this.state.name;
        // change code above this line
        return (
            <div>
                { /* change code below this line */}
                <h1>{name}</h1>
                { /* change code above this line */}
            </div>
        );
    }
};
```

### setState method

a way to change the component's `state`

`this.setState()`passing in an object with key-value pairs. The keys are your state properties and the values are the updated state data. 

```jsx
this.setState({
  username: 'Lewis'
});
```

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: 'Initial State'
        };
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick() {
        // change code below this line
        this.setState({ name: "React Rocks!" })
        // change code above this line
    }
    render() {
        return (
            <div>
                <button onClick={this.handleClick}>Click Me</button>
                <h1>{this.state.name}</h1>
            </div>
        );
    }
};

```

### setState Function

Using a function with `setState` guarantees you are working with the most current values of state and props. 

```jsx
//not good
this.setState({
  counter: this.state.counter + this.props.increment
});

//right way
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

[不是很明白这章节](https://www.freecodecamp.org/learn/front-end-libraries/react/use-state-to-toggle-an-element)

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            visibility: false
        };
        // change code below this line
        this.toggleVisibility = this.toggleVisibility.bind(this);
        // change code above this line
    }
    // change code below this line
    toggleVisibility() {
        this.setState(state => {
            if (state.visibility === true) {
                return { visibility: false };
            } else {
                return { visibility: true };
            }
        });
    }
    // change code above this line
    render() {
        if (this.state.visibility) {
            return (
                <div>
                    <button onClick={this.toggleVisibility}>Click Me</button>
                    <h1>Now you see me!</h1>
                </div>
            );
        } else {
            return (
                <div>
                    <button onClick={this.toggleVisibility}>Click Me</button>
                </div>
            );
        }
    }
};

```

```jsx
class Counter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        };
        // change code below this line
        this.increment = this.increment.bind(this);
        this.decrement = this.decrement.bind(this);
        this.reset = this.reset.bind(this);
        // change code above this line
    }
    // change code below this line
    reset() {
        this.setState({
            count: 0
        });
    }
    increment() {
        this.setState(state => ({
            count: state.count + 1
        }));
    }
    decrement() {
        this.setState(state => ({
            count: state.count - 1
        }));
    }
    // change code above this line
    render() {
        return (
            <div>
                <button className='inc' onClick={this.increment}>Increment!</button>
                <button className='dec' onClick={this.decrement}>Decrement!</button>
                <button className='reset' onClick={this.reset}>Reset</button>
                <h1>Current Count: {this.state.count}</h1>
            </div>
        );
    }
};

```

### state and class

define methods for your component class.

```jsx
class MyClass {
  constructor() {
    this.myMethod = this.myMethod.bind(this);
  }

  myMethod() {
    // whatever myMethod does
  }
}
```

```jsx
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: "Hello"
        };
        // change code below this line
        this.handleClick = this.handleClick.bind(this);
        // change code above this line
    }
    handleClick() {
        this.setState({
            text: "You clicked!"
        });
    }
    render() {
        return (
            <div>
                { /* change code below this line */}
                <button onClick={this.handleClick}>Click Me</button>
                { /* change code above this line */}
                <h1>{this.state.text}</h1>
            </div>
        );
    }
};

```

## the road to react

[books link](https://www.roadtoreact.com/)

看到一半发现，2020最新版没有lifecycle这一章节了，为啥，有些章节字里行间写到“之前提到过的生命周期”，我还纳闷哪里提到了。查了下目录里直接没有了，搜了几年前的中文版是有的。

### Fundamentals of React 

1. Hello React

2. Requirements

3. Setting up a React Project

   - 一些基础的内容讲解，install  ide node npm,官方 create-react-app
   - 安装失败原因：网络原因

   ```
   npx create-react-app my-app
   
   or npm init react-app my-app
   
   cd my-app
   npm start
   ^C
   
   build micro project from 0 to 1
   
   1. file my-app : react router demo
   
   状况：
   1. 在安装hecker-stories时，npx安装失败，显示网络原因，换成npm 命令安装，最后成功。
   2. react 安装会自动生成新的文件夹，可以再指定目录下进行安装，不需要新建同名文件夹
   ```
   
- 对文件类型的基本讲解(This is a breakdown of the most important folders and files: )
   
  - README.md:a markdown file that gives instructions and useful information about the project.
   
  - node_moudles:contains all node packages that have been installed via npm
   
  - package.json:This file shows you a list of node package dependencies and other project configurations.
   
    ```json
       "scripts": 
       { "start": "react-scripts start", 
           "build": "react-scripts build", 
           "test": "react-scripts test", 
           "eject": "react-scripts eject" 
       }, 
       ```
   
    These scripts are executed with the npm run <script> command in an IDE-integrated terminal or command line tool. The run can be omitted for the start and test scripts. The commands are as follows:
   
    ```
       Command Line 
       # Runs the application in http://localhost:3000 
       npm start 
       # Runs the tests 
       npm test 
       # Builds the application for production 
       npm run build 
       ```
   
  - package-lock.json:This file indicates npm how to break down all node package versions. 
   
  - .gitignore:This file displays all files and folders that shouldn’t be added to your git repository when using git, as such files and folders should be located only in your local project.The node_modules/ folder is one example.
   
  - public:This folder holds development files, such as public/index.html. 
   
4. Meet the React Component

   React 的基础写法，大括号的基础使用

   - this is Js function,called functioncomponent,this called App component,因为function 的名字是App
   - the app component doesnot receive any parameters in its function signature
   - the app component returns code that resembles HTML which is called JSX

   ```jsx
   import React from "react";
   const title = "React";
   function App() {
     return (
       <div>
         {" "}
         <h1>Hello {title}</h1>{" "}
       </div>
     );
   }
   export default App;
   ```

5. React JSX

   react jsx,变量的使用，对象的使用，函数的使用

6. <mark>Lists in React</mark>

   数组，对象，数组里放入对象，这有点忘了

   map function 多多熟悉

7. Meet another React Component

   < />的用法

8. <mark>React Component Instantiation</mark>

   component definition , React Component Instantiation/instants,区分 class methods 的解释和用法

   [React Components, Elements, and Instances](https://medium.com/@dan_abramov/react-components-elements-and-instances-90800811f8ca)

9. React DOM

   Next to React, there is another imported library called react-dom, in which a ReactDOM.render() function uses an HTML node to replace it with JSX. The process integrates React into HTML. ReactDOM.render() expects two arguments; the first is to render the JSX. It creates an instance of your App component, though it can also pass simple JSX without any component instantiation. The second argument specifies where the Reactapplication enters your HTML. It expects an element with an id='root', found in the public/index.html file. This is a basic HTML file. 

   ```jsx
   //把这个解释一遍
   ReactDOM.render(
   <h1>Hello React World</h1>, 
   document.getElementById("root")
   );
   ```

10. <mark> 🌟🌟🌟🌟🌟React Component Definition (Advanced)</mark>

   箭头函数讲解，consice 方法讲解 

11. Handler Function in JSX

   [SyntheticEvent](https://reactjs.org/docs/events.html#generic-events)

   ```jsx
import React from "react";

//(event) handler

const App = () => {
  const handleChange = (event) => {
    console.log(event);
  };
  return (
    <div>
      {" "}
      <h1>My Hacker Stories</h1> 
          <label htmlFor="search">Search: </label>{" "}
          <input id="search" type="text" onChange={handleChange} /> 
          <hr /> 
          <List />{" "}
    </div>
  );
};
   ```

Always pass functions to these handlers, not the return value of the function, except when the return value is a function: 

```jsx
// don't do this 
<input id="search" type="text" onChange={handleChange()} /> 
// do this instead 
<input id="search" type="text" onChange={handleChange} /> 
```


12. React Props

React Props are used to pass information down the component tree，props只能将信息向下传递，不能向上传递，对于多组件使用同一个state信息来说非常不方便，可以使用react hook useState

   [How to pass props to components in React](https://www.robinwieruch.de/react-pass-props-to-component)

```JSX
const App = () => {
  const stories = [...];
  const handleChange = (event) => {...};
  return (
    <div>
      {" "}
      <h1>My Hacker Stories</h1> 
      <label htmlFor="search">Search: </label>{" "}
      <input id="search" type="text" onChange={handleChange} /> 
      <hr />{" "}
      <List list={stories} />{" "}
    </div>
  );
};
```

```JSX
const List = (props) =>
  props.list.map((item) => (
    <div key={item.objectID}>
      {" "}
      <span>
        {" "}
        <a href={item.url}>{item.title}</a>{" "}
      </span>{" "}
      <span>{item.author}</span> 
      <span>{item.num_comments}</span>{" "}
      <span>{item.points}</span>{" "}
    </div>
  ));
```

13. React State

   React state is used to make applications interactive.

   Reacthook , useState()

   ```jsx
const App = () => {
  const stories = [...];
  //看情况设置为empty string 或 0,此处设置为empty string
  const [searchTerm, setSearchTerm] = React.useState("");
  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };
  return (
    <div>
      {" "}
      <h1>My Hacker Stories</h1> 
      <label htmlFor="search">Search: </label>{" "}
      <input id="search" type="text" onChange={handleChange} />{" "}
      <p>
        {" "}
       {/* searchTerm 使用 */}
        Searching for <strong>{searchTerm}</strong>.{" "}
      </p>{" "}
      <hr /> 
      <List list={stories} />{" "}
    </div>
  );
};

//function List()
const List = (props) =>
  props.list.map((item) => (
    <div key={item.objectID}>
      {" "}
      <span>
        {" "}
        <a href={item.url}>{item.title}</a>{" "}
      </span>{" "}
      <span>{item.author}</span> 
      <span>{item.num_comments}</span>{" "}
      <span>{item.points}</span>{" "}
    </div>
  ));

   ```

React’s useState hook takes an initial state as an argument. We’ll use an empty string, and the function will return an array with two values. 

The first value (searchTerm) represents the current state;

the second value is <mark>a function</mark> to update this state (setSearchTerm).

JavaScript array destructuring.是这个hook 的语法，多了解。

14. Callback Handlers in JSX
15. Lifting State in React
16. React Controlled Components
17. Props Handling (Advannced) <mark>homework</mark>
18. React Side-Effects
19. React Custom Hooks (Advanced)



14. React Fragments
15. Reusable React Component
16. React Component Composition
17. Imperative React
18. Inline Handler in JSX
19. React Asynchronous Data



14. React Conditional Rendering   88 

15. React Advanced State  92 

16. React Impossible States  . 96

17. Data Fetching with React  101 

18. Data Re-Fetching in React  103 

19. Memoized Handler in React (Advanced) . 106 

    

20. Explicit Data Fetching with React  108 

21. Third-Party Libraries in React   . 111 

22. Async/Await in React (Advanced)  . 113 

23. Forms in React  115 

### how to open setting json file in vscode

To edit your **settings** in **settings**. **json** , start by opening the Command Palette with CMD/CTRL + SHIFT + P . From the Command Palette, you have a choice between two commands that edit your **settings**: The **Open Settings** (**JSON**) command will let you directly edit the **settings JSON** file

将一些基础用法总结一下，

arrow function 
Props Handling (Advanced) 
JavaScript’s destructuring assignment
(nested destructuring /objecte destructuring) 
JavaScript’s spread operator
JavaScript’s rest parameters

Props Handling (Advannced) <mark>homework</mark>

