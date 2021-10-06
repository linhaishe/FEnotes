# 第1章：React入门

## 1.1. React的基本认识

### intro

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

### 官网

1) 英文官网:[ https://reactjs.org/](https://reactjs.org/)

2) 中文官网: https://doc.react-china.org/

### 介绍描述

1) 用于构建用户界面的 JavaScript 库(只关注于View)

2) 由Facebook开源

### React的特点

1) Declarative(声明式编码)

2) Component-Based(组件化编码)

3) Learn Once, Write Anywhere(支持客户端与服务器渲染)

4) 高效

5) 单向数据流

### React高效的原因

考点，一方面减少更新的次数，一方面减少更新的区域

1) 虚拟(virtual)DOM, 不总是直接操作DOM

2) DOM Diff算法, 最小化页面重绘

## 1.2. React的基本使用

注意: 此时只是测试语法使用, 并不是真实项目开发使用

### 相关js库

[bootcdn]( https://www.bootcdn.cn/ )

[cdnjs](https://cdnjs.com/ )

![Xnip2020-01-15_21-50-14.png](http://ww1.sinaimg.cn/large/005NUwyggy1gaxl4qt7g6j30c806o3z0.jpg)

1) react.js: React的核心库

2) react-dom.js: 提供操作DOM的react扩展库

3) babel.min.js: 解析JSX语法代码转为纯JS语法代码的库

### 在页面中导入js

React_test中，01helloworld中部分代码。

```JSX
<script type="text/javascript" src="../js/react.development.js"></script>
<script type="text/javascript" src="../js/react-dom.development.js"></script>
<script type="text/javascript" src="../js/babel.min.js"></script>

<script type="text/babel"> 
    //必须声明babel  
    // 创建虚拟DOM元素  
    const vDom = <h1>Hello React</h1> 
	// 千万不要加引号  
	// 渲染虚拟DOM到页面真实DOM容器中  
	ReactDOM.render(vDom, document.getElementById('test')) 
</script>
```

**使用React开发者工具调试 developer tools**

### 在页面中导入css

[React普通样式(className)和行内样式(LineStyle)多种设置样式设置详解]( https://blog.csdn.net/pcaxb/article/details/53896661 )

#### （外部CSS样式 

index.html文件中引入这个css文件

```html
<link rel="stylesheet" type="text/css" href="%PUBLIC_URL%/style.css">
```

 需要注意style.css文件需要放在public目录中 

```JSX
import 'style.css';

function Welcome(props) {
    return <h1 className='foo'>Hello, {props.name}</h1>
}
```

第一种引入样式的方法常常作用于整个应用的所有组件。

第二种引入的样式通常引用于某个组件。

但是全局样式我们也可以通过第二种方式，我们在入口js文件(一般是index.js)中引入就可以了。

#### 内联样式 

```jsx
function Welcome(props) {
    return <h1
        className='foo'
        style={{
            width: "100%",
            height: "50px",
            backgroundColor: "blue",
            fontSize: "20px"
        }}>Hello, {props.name}</h1>
}
```

```jsx
function Welcome(props) {
    const style = {
        width: '100%',
        height: '50px',
        backgroundColor: 'blue',
        fontSize: '20px'
    };
    return <h1 className='foo' style={style}>Hello, {props.name}</h1>
}
```

## 1.3. React JSX

### 虚拟DOM

```jsx
<div id='test'></div>

//1.创建虚拟dom元素对象
//<h1 id='myTitle'>hello</h1>
var element = React.createElement('h1', {id:'myTitle'},'hello')
//2.将虚拟dom渲染到页面真实dom容器中
ReactDOM.render(element,document.getElementById('test'))
```

1) React提供了一些API来创建一种 `特别` 的一般js对象

a. var element = React.createElement('h1', {id:'myTitle'},'hello')

b. 上面创建的就是一个简单的虚拟DOM对象

2) 虚拟DOM对象最终都会被React转换为真实的DOM

3) 我们编码时基本只需要操作react的虚拟DOM相关数据, react会转换为真实DOM变化而更新界面

真实dom虚拟dom的区别，

1.一个内容重，一个内容轻。

2.更改真实dom时，页面会变化，更改虚拟dom时,	页面不会变化，直到渲染后，页面才会变化

### JSX

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

1) 全称:  JavaScript XML

2) react定义的一种类似于XML的JS扩展语法: XML+JS

3) 作用: 用来创建react虚拟DOM(元素)对象

a. `var ele = <h1>Hello JSX!</h1>`

b. 注意1: 它不是字符串, 也不是HTML/XML标签

c. 注意2: 它最终产生的就是一个JS对象

4) 标签名任意: HTML标签或其它标签

5) 标签属性任意: HTML标签属性或其它

6) 基本语法规则

a. 遇到 < 开头的代码, 以标签的语法解析: html同名标签转换为html同名元素, 其它标签需要特别解析

b. 遇到以 { 开头的代码，以JS语法解析: 标签中的js代码必须用{ }包含

7) babel.js的作用

a. 浏览器不能直接解析JSX代码, 需要babel转译为纯JS的代码才能运行

b. 只要用了JSX，都要加上type="text/babel", 声明需要babel来处理

### 渲染虚拟DOM(元素)

1) 语法:  ReactDOM.render(virtualDOM, containerDOM) 

2) 作用: 将虚拟DOM元素渲染到页面中的真实容器DOM中显示

3) 参数说明

a. 参数一: 纯js或jsx创建的虚拟dom对象

b. 参数二: 用来包含虚拟DOM元素的真实dom元素对象(一般是一个div)

### 建虚拟DOM的2种方式

1) 纯JS(一般不用)

`React.createElement('h1',  {id:'myTitle'},  title)`

2) JSX:

`<h3 id='id'>{title}</h3>`

###  JSX练习

需求: 动态展示列表数据

react_test/helloreact.html

将一个数据的数组转化为一个标签的数组

`const names = ['jquery', 'zepto', 'angular', 'react', 'vue'];`

## 1.4. 模块与组件和模块化与组件化

### 模块

1) 理解: 向外提供特定功能的js程序, 一般就是一个js文件

2) 为什么:  js代码更多更复杂

3) 作用: 复用js, 简化js的编写, 提高js运行效率

### 组件

1) 理解: 用来实现特定(局部)功能效果的代码集合(html/css/js)

2) 为什么: 一个界面的功能更复杂

3) 作用: 复用编码, 简化项目编码, 提高运行效率

### 模块化

当应用的js都以模块来编写的, 这个应用就是一个模块化的应用

### 组件化

当应用是以多组件的方式实现, 这个应用就是一个组件化的应用。一个界面的部分功能模块，包括html,css,javasc,img...

[组件化理解]( http://huziketang.mangojuice.top/books/react/lesson14 )

# 第2章：React面向组件编程

## 2.1. 基本理解和使用

js面向对象 - > 面向模块 - > 面向组件

### 自定义组件(Component) :

1) 定义组件(2种方式)

方式1: 工厂函数组件(简单组件)

```jsx
function MyComponent () {  
  return (<h2>工厂函数组件(简单组件)</h2>)
} 
```

方式2:  ES6类组件(复杂组件)

```jsx
class MyComponent2 extends React.Component {  
  render () {   
    console.log(this) 
    // MyComponent2的实例对象   
    return (<h2>ES6类组件(复杂组件)</h2>)
  } 
  }
```

2) 渲染组件标签，（是渲染组件标签，不是渲染组件

```jsx
ReactDOM.render(<MyComponent />, document.getElementById('example1'))
```

### 注意

1) 组件名必须首字母大写

2) 虚拟DOM元素只能有一个根元素

3) 虚拟DOM元素必须有结束标签

### render()渲染组件标签的基本流程

1) React内部会创建组件实例对象

2) 得到包含的虚拟DOM并解析为真实DOM

3) 插入到指定的页面元素内部

## 2.2. 组件三大属性1: state

1) state是组件对象最重要的属性, 值是对象(可以包含多个数据)

2) 组件被称为"状态机", 通过更新组件的state来更新对应的页面显示(重新渲染组件)

3)定义组件，只要有状态的时候，就不能用工厂模式。没有状态的时候就用函数的方式。因为语法简单，效率高，不需要创建对象。

Refs:

[解构](https://stackoverflow.com/questions/55188257/const-name-value-event-target-what-does-this-mean)

[Object destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Object_destructuring)

### 编码操作

1) 初始化状态:

```js
constructor(props) {
    super(props)
	//给状态赋初值↓，初始化状态，写法是固定的
    this.state = {
	//是一个对象类型
        stateProp1: value1,
        stateProp2: value2
    }
}
```

2) 读取某个状态值

` this.state.statePropertyName`

this指向组件对象，

3) 更新状态---->组件界面更新

```jsx
this.setState({
    stateProp1: value1,
    stateProp2: value2
})
```

## 2.3. 组件三大属性2: props

04_component_props

### 理解

1) 每个组件对象都会有props(properties的简写)属性

2) 组件标签的所有属性都保存在props中

### 作用

1) 通过标签属性从组件外向组件内传递变化的数据

2) 注意: 组件内部不要修改props数据

### 编码操作

1) 内部读取某个属性值

`this.props.propertyName`

2) 对props中的属性值进行类型限制和必要性限制

```jsx
Person.propTypes = {

name: React.PropTypes.string.isRequired,

age: React.PropTypes.number.isRequired

}
```

3) 扩展属性: 将对象的所有属性通过props传递

4) 默认属性值

```jsx
Person.defaultProps = {

name: 'Mary'

}
```

5) 组件类的构造函数

```jsx
constructor (props) {

super(props)

console.log(props) // 查看所有属性

}
```

### 面试题

问题: 请区别一下组件的props和state属性

1) state: 组件自身内部可变化的数据

2) props: 从组件外部向组件内部传递数据, 组件内部只读不修改

## 2.4. 组件三大属性3: refs与事件处理

### 效果

需求: 自定义组件, 功能说明如下:
 2. 点击按钮, 提示第一个输入框中的值
 3. 当第2个输入框失去焦点时, 提示这个输入框中的值

### 组件的3大属性之二: refs属性

1) 组件内的标签都可以定义ref属性来标识自己

a. <input type="text" ref={input => this.msgInput = input}/>

b. 回调函数在组件初始化渲染完或卸载时自动调用

2) 在组件中可以通过this.msgInput来得到对应的真实DOM元素

3) 作用: 通过ref获取组件内容特定标签对象, 进行读取其相关数据

### 事件处理

1) 通过onXxx属性指定组件的事件处理函数(注意大小写)

a. React使用的是自定义(合成)事件, 而不是使用的原生DOM事件

b. React中的事件是通过事件委托方式处理的(委托给组件最外层的元素)

2) 通过event.target得到发生事件的DOM元素对象

```jsx
handleFocus(event) {

event.target  //返回input对象

}
```

### 强烈注意

1) 组件内置的方法中的this为组件对象

2) 在组件类中自定义的方法中this为null

a. 强制绑定this: 通过函数对象的bind()

b. 箭头函数(ES6模块化编码时才能使用)

## 2.5. 组件的组合

### 效果

功能: 组件化实现此功能

 1. 显示所有todo列表
 2. 输入文本, 点击按钮显示到列表的首位, 并清除输入的文本

### 功能界面的组件化编码流程(无比重要)

1) 拆分组件: 拆分界面,抽取组件

2) 实现静态组件: 使用组件实现静态页面效果

3) 实现动态组件

a. 动态显示初始化数据

b. 交互功能(从绑定事件监听开始)

## 2.6. 收集表单数据

### 效果

需求: 自定义包含表单的组件
 1. 输入用户名密码后, 点击登陆提示输入信息
 3. 不提交表单

### 理解

1) 问题: 在react应用中, 如何收集表单输入数据

2) 包含表单的组件分类

a. 受控组件: 表单项输入数据能自动收集成状态

b. 非受控组件: 需要时才手动读取表单输入框中的数据

## 2.7. 组件生命周期

### 理解

1) 组件对象从创建到死亡它会经历特定的生命周期阶段

2) React组件对象包含一系列的勾子函数(生命周期回调函数), 在生命周期特定时刻回调

3) 我们在定义组件时, 可以重写特定的生命周期回调函数, 做特定的工作

声明式编程，命令式编程，函数式编程

### 生命周期流程图

[react life-circle newest ver](https://medium.com/@baphemot/understanding-react-react-16-3-component-life-cycle-23129bc7a705)

[react life-circle previous ver](https://medium.com/@baphemot/understanding-reactjs-component-life-cycle-823a640b3e8d)

[life circle diagram](http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

![Xnip2020-04-06_20-52-57.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gdleqld0ooj31ba0p8tdj.jpg)

<img src="http://ww1.sinaimg.cn/large/005NUwyggy1gdleqley9ej31100uw41h.jpg" alt="Xnip2020-04-06_20-18-51.jpg" style="zoom:50%;" />

![Xnip2020-04-06_20-16-30.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gdleqlbhisj30i80fsgms.jpg)

<img src="http://ww1.sinaimg.cn/large/005NUwyggy1gdleqlb169j30uq0x6tb1.jpg" alt="Xnip2020-04-06_20-16-45.jpg" style="zoom:50%;" />


![Xnip2020-02-26_23-22-29.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gca7zq672dj31r615c11r.jpg)

![reactlifecircle.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbq8gfa7ldj30k70kvq5m.jpg) 

### 生命周期详述

1) 组件的三个生命周期状态:

   Mount：插入真实 DOM，挂载

   Update：被重新渲染

   Unmount：被移出真实 DOM

2) React 为每个状态都提供了勾子(hook)函数

- componentWillMount():

   The `componentWillMount()` method is called before the `render()` method when a component is being mounted to the DOM. Log something to the console within `componentWillMount()` - you may want to have your browser console open to see the output. 

- componentDidMount()
  - The best practice with React is to place API calls or any calls to your server in the lifecycle method `componentDidMount()`. This method is called after a component is mounted to the DOM. Any calls to `setState()` here will trigger a re-rendering of your component. When you call an API in this method, and set your state with the data that the API returns, it will automatically trigger an update once you receive the data. 
  -  The `componentDidMount()` method is also the best place to attach any event listeners you need to add for specific functionality.  

- componentWillUpdate()

- componentDidUpdate()

- componentWillUnmount()

- shouldComponentUpdate()

  But React provides a lifecycle method you can call when child components receive new `state` or `props`, and declare specifically if the components should update or not. The method is `shouldComponentUpdate()`, and it takes `nextProps` and `nextState` as parameters. 

   The method must return a `boolean` value that tells React whether or not to update the component.  

3) 生命周期流程:

a. 第一次初始化渲染显示: ReactDOM.render()

​    constructor(): 创建对象初始化state

​    componentWillMount() : 将要插入回调

​    render() : 用于插入虚拟DOM回调

​    componentDidMount() : 已经插入回调

b. 每次更新state: this.setSate()

​    componentWillUpdate() : 将要更新回调

​    render() : 更新(重新渲染)

​    componentDidUpdate() : 已经更新回调

c. 移除组件: ReactDOM.unmountComponentAtNode(containerDom)

​    componentWillUnmount() : 组件将要被移除回调

### 重要的勾子

1) render(): 初始化渲染或更新渲染调用

2) componentDidMount(): 开启监听, 发送ajax请求

3) componentWillUnmount(): 做一些收尾工作, 如: 清理定时器

4) componentWillReceiveProps(): 后面需要时讲

## 2.8. 虚拟DOM与DOM Diff算法

### 基本原理图

Diff 算法：最小页面重绘，实现最小化区域更新

![基本原理图.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbqhljtzoqj30rp0b3wga.jpg)

# 第3章：react应用(基于react脚手架)

## 3.1. 使用create-react-app创建react应用

### 3.1.1. react脚手架

1) xxx脚手架: 用来帮助程序员快速创建一个基于xxx库的模板项目

a. 包含了所有需要的配置

b. 指定好了所有的依赖

c. 可以直接安装/编译/运行一个简单效果

2) react提供了一个用于创建react项目的脚手架库: create-react-app

3) 项目的整体技术架构为:  react + webpack + es6 + eslint(代码规范的检查工具)

4) 使用脚手架开发的项目的特点: 模块化, 组件化, 工程化

### 3.1.2. 创建项目并启动

[guide](https://github.com/facebook/create-react-app)

```jsx
npx create-react-app my-app
cd my-app
npm start
```

查看是否已经下载过

`npm root -g`

查看全局的下载根目录 

### 3.1.3. react脚手架项目结构

ReactNews

​	|--node_modules---第三方依赖模块文件夹

​	|--public

​		|-- index.html-----------------主页面

​	|--scripts

​		|-- build.js-------------------build打包引用配置

​	|-- start.js-------------------start运行引用配置

​	|--src------------源码文件夹

​		|--components-----------------react组件

​		|--index.js-------------------应用入口js

​	|--.gitignore------git版本管制忽略的配置

​	|--package.json----应用包配置文件，每一个包都是一个应用，每个应用都有一个package.json，描述项目相关信息

​	|--README.md-------应用描述说明的readme文件

标识，依赖，运行/打包

组件可以全部放在一个文件夹里。取名小写component,放react 组件相关文件  

![Xnip2020-02-10_10-43-47.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbr3zedsh0j30fi094dio.jpg)

## 3.2. demo: 评论管理

### 3.2.1. 效果

#### 流程思路：

1. 区块划分
	- 最外层的组件，固定的app
	- Comment-add
	- Comment-list
	- Comment-item
2. 传入默认属性，可以使用简洁语法，不用constructor
3. 接收数据之前先声明接受什么属性
4. npm install --save prop-types
5. 引入prop
6. 取属性
7. 将默认属性传入citem
8. 写提交按钮
9. 绑定监听，箭头函数绑定
10. 受控组件必须有状态接受数据
11. 收集数据，并封装成comment对象
12. 添加comment的方法，获得原来的的状态，添加状态，更新状态
13. 删除评论。splice 增删改
14. 删除后有字显示

----

1. 组件里传递的属性，可以再this.props中获取到

![comment_component.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gbr6jj0plcg30r70gagr9.gif)

### 3.2.2. 拆分组件

应用组件: App

 state: comments/array

添加评论组件: CommentAdd

 state: username/string, content/string

 props: add/func

评论列表组件: CommentList

 props: comment/object, delete/func, index/number

评论项组件: CommentItem

 props: comments/array, delete/func

### 3.2.3. 实现静态组件

 

### 3.2.4. 实现动态组件

下载prop-types包，这个包默认是没有下载的，需要下载后再引入

`react_app git:(master) ✗ npm install --save prop-types`

动态展示初始化数据

 初始化状态数据

传递属性数据

响应用户操作, 更新组件界面

绑定事件监听, 并处理

获得输入数据，并更新数据

静态属性写在左边，动态属性写在右边，可以互反，但是必须要有规律。

更新state

```js
input => (this.content = input)

var _this = void 0;

(function (input) {
  return _this.content = input;
});
```

```jsx
addComment = (comment) =>{
const {comments} = this.state
comments.unshift(comment)
  this.setstate({comments})
}
```

```js
"use strict";

var _this = void 0;

addComment = function addComment(comment) {
  var comments = _this.state.comments;
  comments.unshift(comment);

  _this.setstate({
    comments: comments
  });
};
```

# 第4章：react ajax

## 4.1. 理解

### 4.1.1. 前置说明

1) React本身只关注于界面, 并不包含发送ajax请求的代码

2) 前端应用需要通过ajax请求与后台进行交互(json数据)

3) react应用中需要集成第三方ajax库(或自己封装)

### 4.1.2. 常用的ajax请求库

1. jQuery: 比较重, 如果需要另外引入不建议使用，ajax只是其小一部分功能，我们需要用专门传输ajax数据的库就可以了。

2. axios: 轻量级, 建议使用

   a. 封装XmlHttpRequest对象的ajax

   b. promise风格

   c. 可以用在浏览器端和node服务器端

3. fetch: 原生函数, 但老版本浏览器不支持

   a. 不再使用XmlHttpRequest对象提交ajax请求

   b. 为了兼容低版本的浏览器, 可以引入兼容库fetch.js

可以使用JQuery,axios,和Fetch函数，这三种方法做ajax请求。fetch函数是浏览器原生自带的，原本就有的，直接使用即可。但是老版浏览器不支持，可以引入兼容库fetch.js，它会对浏览器进行判断，判断是否使用fetch函数，否则使用JQ或者axios

### 4.1.3. 效果

需求:
 1. 界面效果如下
 2. 根据指定的关键字在github上搜索匹配的最受关注的库
 3. 显示库名, 点击链接查看库

4. 测试接口: https://api.github.com/search/repositories?q=r&sort=stars

![ajax.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gc23h7jhfig30cf09smzn.gif)

## 4.2. axios

### 4.2.1. 文档

https://github.com/axios/axios

### 4.2.2. 相关API

1) GET请求

```jsx
axios
  .get("/user?ID=12345")
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });
axios
  .get("/user", { params: { ID: 12345 } })
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  }); 
```

2) POST请求

```jsx
axios
  .post("/user", { firstName: "Fred", lastName: "Flintstone" })
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  }); 
```

## 4.3. Fetch

### 4.3.1. 文档

1) https://github.github.io/fetch/

2) https://segmentfault.com/a/1190000003810652

### 4.3.2. 相关API

1) GET请求

```jsx
fetch(url)
  .then(function(response) {
    return response.json();
    //说明return返回的是一个promise对象，response不能直接得到数据，返回的只是包含数据的promise对象
  })
  .then(function(data) {
    //这次返回的就是数据了
    console.log(data);
  })
  .catch(function(e) {
    console.log(e);
  });
```

```jsx
fetch(url)
.then(response => {
    return response.json();
})
.then(data => {
//得到数据
//data代表的就是result
const { name, html_url } = data.items[0];
//更新状态
this.setState({ repoName: name, repoUrl: html_url });
});
```

2) POST请求

```jsx
fetch(url, { method: "POST", body: JSON.stringify(data) })
  .then(function(data) {
    console.log(data);
  })
  .catch(function(e) {
    console.log(e);
  });
```

## 4.4. demo: github users

### 4.4.1. 效果

![demo_users.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gc2oeu2bjog30lk0fte81.gif)

#### 步骤：

1. 组件划分
2. a.初始:提示文本，请输入搜索关键字，b.搜索中loading，c.搜索成功显示搜索结果，d.搜索失败，显示出错的文本
   - loading，点击搜索按钮之前，默认为false,点击后变为true, 显示正在请求中的文本，如果为false的时候
3. 接收input内的输入数据
4. 发请求获取对应数据
5. 考虑发请求的组件
6. 如何将数据传给兄弟组件，先告诉父亲，父亲再传给子组件
7. 传输数据给子组件，子组件发送请求，请求搜索

### 4.4.2. 拆分组件

- App

`state: searchName/string`

- Search

`props: setSearchName/func`

- List

`props: searchName/string`

`state: firstView/bool, loading/bool, users/array, errMsg/string`

### 4.4.3. 编写静态组件

### 4.4.4. 编写动态组件

`componentWillReceiveProps(nextProps)`: 监视接收到新的props, 发送ajax

使用axios库发送ajax请求 

# 第5章：几个重要技术总结

## 5.1. 组件间通信

### 5.1.1. 方式一: 通过props传递

1) 共同的数据放在父组件上, 特有的数据放在自己组件内部(state)

2) 通过props可以传递一般数据和函数数据, 只能一层一层传递

3) 一般数据-->父组件传递数据给子组件-->子组件读取数据

4) 函数数据-->子组件传递数据给父组件-->子组件调用函数

父组件如果想传数据给孙子组件，兄弟组件互相传递数据，借助于父组件，props的传递方式。

### 5.1.2. 方式二: 使用消息订阅(subscribe)-发布(publish)机制

订阅消息相当于绑定监听，发布消息相当于触发事件，回调函数会被调用。

这种机制需要有库才能实现。(npm install )

有利于多重组件的通信方式

1) 工具库: PubSubJS

2) 下载: npm install --save pubsub-js

3) 使用: 

```jsx
import PubSub from 'pubsub-js' //引入
PubSub.subscribe('delete', function(data){ }); //订阅
PubSub.publish('delete', data) //发布消息
```

### 5.1.3. 方式三: redux

后面专门讲解

## 5.2. 事件监听理解

### 5.2.1. 原生DOM事件

1) 绑定事件监听

a. 事件名(类型): 只有有限的几个, 不能随便写

b. 回调函数

2) 触发事件

a. 用户操作界面

b. 事件名(类型)

c. 数据()

### 5.2.2. 自定义事件(消息机制)

1) 绑定事件监听

a. 事件名(类型): 任意

b. 回调函数: 通过形参接收数据, 在函数体处理事件

2) 触发事件(编码)

a. 事件名(类型): 与绑定的事件监听的事件名一致

b. 数据: 会自动传递给回调函数

## 5.3. ES6常用新语法

1) 定义常量/变量:  const/let

2) 解构赋值: `let {a, b} = this.props  import {aa} from 'xxx'`

3) 对象的简洁表达: {a, b}

4) 箭头函数: 

a. 常用场景

 组件的自定义方法: xxx = () => {}

 参数匿名函数

b. 优点:

​		 简洁

​		 没有自己的this,使用引用this查找的是外部this

5) 扩展(三点)运算符: 拆解对象(const MyProps = {}, <Xxx {...MyProps}>)

6) 类:  class/extends/constructor/super

7) ES6模块化:  export default | import

# 第6章：react-router4

## 6.1. 相关理解

### 6.1.1. react-router的理解

1) react的一个插件库

2) 专门用来实现一个SPA应用

3) 基于react的项目基本都会用到此库

### 6.1.2. SPA的理解

1) 单页Web应用（single page web application，SPA）

2) 整个应用只有一个完整的页面，都是由组件写成的

3) **点击页面中的链接不会刷新页面, 本身也不会向服务器发请求**，是有可能在组件内部发送请求，通过更新组件。不是单页点击链接是会像服务器发请求的。

4) 成为路由链接，当点击路由链接时, 只会做页面的局部更新

5) 数据都需要通过ajax请求获取, 并在前端异步展现

### 6.1.3. 路由的理解

1) 什么是路由?

​	a. 一个路由就是一个映射关系(key:value)

​	b. key为路由路径path, value可能是function(后台路由)/component(前台路由)

2) 路由分类

​	含义：router 路由器 ，route 路由

​		a. 后台路由: node服务器端路由, value是function, 用来处理客户端提交的请求并返回一个响应数据

​		b. 前台路由: 浏览器端路由, value是component, 当请求的是路由path时, 浏览器端前没有发送http请求, 但界面会更新显示对应的组件 

3) 后台路由

​	a. 注册路由: router.get(path, function(req, res))

​	b. 当node接收到一个请求时, 根据请求路径找到匹配的路由, 调用路由中的函数来处理请求, 返回响应数据

4) 前端路由

​	a. 注册路由: `<Route path="/about" component={About}>`

​	b. 当浏览器的hash变为#about时, 当前路由组件就会变为About组件

### 6.1.4. 前端路由的实现

1) history库

引用这个库可以记录浏览历史

​	a. 网址: https://github.com/ReactTraining/history

​	b. 管理浏览器会话历史(history)的工具库

​	c. 包装的是原生BOM中window.history和window.location.hash

2) history API

​	a. History.createBrowserHistory(): 得到封装window.history的管理对象

​	b. History.createHashHistory(): 得到封装window.location.hash的管理对象

​	c. history.push(): 添加一个新的历史记录

​	d. history.replace(): 用一个新的历史记录替换当前的记录

​	e. history.goBack(): 回退到上一个历史记录

​	f. history.goForword(): 前进到下一个历史记录

​	g. history.listen(function(location){}): 监视历史记录的变化


## 6.2. react-router相关API

### 6.2.1. 组件

1) `<BrowserRouter>`(不带#号的路由)

2)` <HashRouter>`(带#号的路由)

3) `<Route>`

4)` <Redirect>`

5) `<Link>`(路由链接)

6) `<NavLink>`(导航路由链接),区别link多了一个className属性

7) `<Switch>`

### 6.2.2. 其它

1) history对象，push(),replace()

2) match对象

3) withRouter函数

## 6.3. 基本路由使用

### 6.3.1. 效果

![react-router demo1.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gc5kn5s1lkg30il0cqmzq.gif)

### 6.3.2. 准备

1) 下载react-router: npm install --save react-router@4

2) 引入bootstrap.css: 

`<link rel="stylesheet" href="/css/bootstrap.css">`

### 6.3.3. 路由组件: views/about.jsx

不是所有的组件都是路由组件，路由组件和非路由组件分开写。路由组件一般放在pages/views文件夹里。

`import React from 'react' export default function About() {  return <div>About组件内容</div> }`

### 6.3.4. 路由组件: views/home.jsx

`import React from 'react' export default function About() {  return <div>Home组件内容</div> }`

### 6.3.5. 包装NavLink组件: components/my-nav-link.jsx

`import React from 'react' import {NavLink} from 'react-router-dom'  export default function MyNavLink(props) {  return <NavLink {...props} activeClassName='activeClass'/> }`

### 6.3.6. 应用组件: components/app.jsx

### 6.3.7. 自定义样式: index.css

`.activeClass {  color: red !important; }` 

### 6.3.8. 入口JS: index.js

 ```jsx
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, HashRouter } from "react-router-dom";
import App from "./components/app";
import "./index.css";
ReactDOM.render(
  <BrowserRouter>
    {" "}
    <App />{" "}
  </BrowserRouter>,
  document.getElementById("root")
);
 ```

## 6.4. 嵌套路由使用

### 6.4.1. 效果

Notes:路由组件中包含另外一个路由，称为子路由/二级路由

#### 如何编写路由效果

1. 编写路由组件

2. 在父路由组件中指定

   路由链接：`<NavLink>`

   路由：`<Route>`

### 6.4.2. 二级路由组件: views/news.jsx

```jsx
import React from "react";
export default class News extends React.Component {
  state = { newsArr: ["news001", "news002", "news003"] };
  render() {
    return (
      <div>
        {" "}
        <ul>
          {" "}
          {this.state.newsArr.map((news, index) => (
            <li key={index}>{news}</li>
          ))}{" "}
        </ul>{" "}
      </div>
    );
  }
}
```

### 6.4.3. 二级路由组件: views/message.jsx

```jsx
import React from "react";
import { Link, Route } from "react-router-dom";
export default class Message extends React.Component {
  state = { messages: [] };
  componentDidMount() {
    // 模拟发送ajax请求
    setTimeout(() => {
      const data = [
        { id: 1, title: "Message001" },
        { id: 3, title: "Message003" },
        { id: 6, title: "Message006" }
      ];
      this.setState({ messages: data });
    }, 1000);
  }
  render() {
    const path = this.props.match.path;
    return (
      <div>
        {" "}
        <ul>
          {" "}
          {this.state.messages.map((m, index) => {
            return (
              <li key={index}>
                {" "}
                <Link to="???">{m.title}</Link>{" "}
              </li>
            );
          })}{" "}
        </ul>{" "}
      </div>
    );
  }
}
```

### 6.4.4. 一级路由组件: views/home.jsx

```jsx
import React from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import MyNavLink from "./components/my-nav-link";
import News from "./views/news";
import Message from "./views/message";
export default function Home() {
  return (
    <div>
      {" "}
      <h2>Home组件内容</h2>{" "}
      <div>
        {" "}
        <ul className="nav nav-tabs">
          {" "}
          <li>
            {" "}
            <MyNavLink to="/home/news">News</MyNavLink>{" "}
          </li>{" "}
          <li>
            {" "}
            <MyNavLink to="/home/message">Message</MyNavLink>{" "}
          </li>{" "}
        </ul>{" "}
        <Switch>
          {" "}
          <Route path="/home/news" component={News} />{" "}
          <Route path="/home/message" component={Message} />{" "}
          <Redirect to="/home/news" />{" "}
        </Switch>{" "}
      </div>{" "}
    </div>
  );
}
 
```

## 6.5. 向路由组件传递参数数据

`props.match.params.id`

`match`,`history`

### 6.5.1. 效果

### 6.5.2. 三级路由组件: views/message-detail.jsx

```jsx
import React from "react";
const messageDetails = [
  { id: 1, title: "Message001", content: "我爱你, 中国" },
  { id: 3, title: "Message003", content: "我爱你, 老婆" },
  { id: 6, title: "Message006", content: "我爱你, 孩子" }
];
export default function MessageDetail(props) {
  const id = props.match.params.id;
  const md = messageDetails.find(md => md.id === id1);
  return (
    <ul>
      {" "}
      <li>ID: {md.id}</li> <li>TITLE: {md.title}</li>{" "}
      <li>CONTENT: {md.content}</li>{" "}
    </ul>
  );
}
```

### 6.5.3. 二级路由组件: views/message.jsx

```jsx
import React from "react";
import { Link, Route } from "react-router-dom";
import MessageDetail from "./views/message-detail";
export default class Message extends React.Component {
  state = { messages: [] };
  componentDidMount() {
    // 模拟发送ajax请求
    setTimeout(() => {
      const data = [
        { id: 1, title: "Message001" },
        { id: 3, title: "Message003" },
        { id: 6, title: "Message006" }
      ];
      this.setState({ messages: data });
    }, 1000);
  }
  render() {
    const path = this.props.match.path;
    return (
      <div>
        {" "}
        <ul>
          {" "}
          {this.state.messages.map((m, index) => {
            return (
              <li key={index}>
                {" "}
                <Link to={`${path}/${m.id}`}>{m.title}</Link>{" "}
              </li>
            );
          })}{" "}
        </ul>{" "}
        <hr /> <Route path={`${path}/:id`} component={MessageDetail}></Route>{" "}
      </div>
    );
  }
}
```

## 6.6. 多种路由跳转方式

### 6.6.1. 效果

### 6.6.2. 二级路由: views/message.jsx

```jsx
import React from "react";
import { Link, Route } from "react-router-dom";
import MessageDetail from "./views/message-detail";
export default class Message extends React.Component {
  state = { messages: [] };
  componentDidMount() {
    // 模拟发送ajax请求
    setTimeout(() => {
      const data = [
        { id: 1, title: "Message001" },
        { id: 3, title: "Message003" },
        { id: 6, title: "Message006" }
      ];
      this.setState({ messages: data });
    }, 1000);
  }
  ShowDetail = id => {
    this.props.history.push(`/home/message/${id}`);
  };
  ShowDetail2 = id => {
    this.props.history.replace(`/home/message/${id}`);
  };
  back = () => {
    this.props.history.goBack();
  };
  forward = () => {
    this.props.history.goForward();
  };
  render() {
    const path = this.props.match.path;
    return (
      <div>
        {" "}
        <ul>
          {" "}
          {this.state.messages.map((m, index) => {
            r;
            eturn(
              <li key={index}>
                {" "}
                <Link to={`${path}/${m.id}`}>{m.title}</Link>{" "}
                <button onClick={() => this.ShowDetail(m.id)}>
                  查看详情(push)
                </button>{" "}
                <button onClick={() => this.ShowDetail2(m.id)}>
                  查看详情(replace)
                </button>{" "}
              </li>
            );
          })}{" "}
        </ul>{" "}
        <p>
          {" "}
          <button onClick={this.back}>返回</button>{" "}
          <button onClick={this.forward}>前进</button>{" "}
        </p>{" "}
        <hr /> <Route path={`${path}/:id`} component={MessageDetail}></Route>{" "}
      </div>
    );
  }
}
```

# 第7章：react-ui

## 7.1. 最流行的开源React UI组件库

### 7.1.1. material-ui(国外)

1) 官网: [http://www.material-ui.com/#/](#/)

2) github: https://github.com/callemall/material-ui

### 7.1.2. ant-design(国内蚂蚁金服)

1) PC官网: https://ant.design/index-cn

2) 移动官网: https://mobile.ant.design/index-cn

3) Github: https://github.com/ant-design/ant-design/

4) Github: https://github.com/ant-design/ant-design-mobile/

## 7.2. ant-design-mobile使用入门

### 7.2.1. 效果

![antd-mobile.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gc6enr2jnsg30860cb0st.gif)

### 7.2.2. 使用create-react-app创建react应用

​	`npm install create-react-app -g`

​	`create-react-app antm-demo`

​	`cd antm-demo`

​	`npm start`

### 7.2.3. 搭建antd-mobile的基本开发环境

1) 下载

`npm install antd-mobile --save`

2) src/App.jsx

```jsx
import React, { Component } from 'react'
// 分别引入需要使用的组件
import Button from 'antd-mobile/lib/button'
import Toast from 'antd-mobile/lib/toast'

export default class App extends Component {
  handleClick = () => {
    Toast.info('提交成功', 2)
  }

  render() {
    return (
      <div>
        <Button type="primary" onClick={this.handleClick}>提交</Button>
      </div>
    )
  }
}
```

3) src/index.js

```jsx
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
// 引入整体css 
import 'antd-mobile/dist/antd-mobile.css'
ReactDOM.render(<App />, document.getElementById('root'))
```



4) index.html

<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no" /> <script src="https://as.alipayobjects.com/g/component/fastclick/1.0.6/fastclick.js"></script> <script>  if ('addEventListener' in document) {   document.addEventListener('DOMContentLoaded', function() {    FastClick.attach(document.body);   }, false);  }  if(!window.Promise) {   document.writeln('+'>'+'<'+'/'+'script>');  } </script> 
### 7.2.4. 实现按需打包(组件js/css)

1) 下载依赖包

yarn add react-app-rewired --dev

yarn add babel-plugin-import --dev

2) 修改默认配置:  

- package.json

```jsx
"scripts": {  
    "start": "react-app-rewired start",  
    "build": "react-app-rewired build",  
    "test": "react-app-rewired test --env=jsdom" 
}
```

- config-overrides.js

```jsx
const {injectBabelPlugin} = require('react-app-rewired'); 
module.exports = function override(config, env) {  
    config = injectBabelPlugin(['import', {libraryName: 'antd-mobile', style: 'css'}], config);  
    return config; 
};
```

3) 编码

```jsx
// import 'antd-mobile/dist/antd-mobile.css' 
// import Button from 'antd-mobile/lib/button' 
// import Toast from 'antd-mobile/lib/toast' 
import {Button, Toast} from 'antd-mobile'
```

# 第8章：redux

## 8.1. redux理解

### 8.1.1. 学习文档

1) 英文文档: https://redux.js.org/

2) 中文文档: http://www.redux.org.cn/

3) Github: https://github.com/reactjs/redux

### 8.1.2. redux是什么?

1) redux是一个独立专门用于做状态管理的JS库(不是react插件库)

2) 它可以用在react, angular, vue等项目中, 但基本与react配合使用

3) 作用: 集中式管理react应用中多个组件共享的状态

### 8.1.3. redux工作流程

![react-redux.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gdcwe2wa28j30hq0dbt90.jpg)

### 8.1.4. 什么情况下需要使用redux

1) 总体原则: 能不用就不用, 如果不用比较吃力才考虑使用

2) 某个组件的状态，需要共享

3) 某个状态需要在任何地方都可以拿到

4) 一个组件需要改变全局状态

5) 一个组件需要改变另一个组件的状态

## 8.2. redux的核心API

### 8.2.1. createStore()

1) 作用: 

创建包含指定reducer的store对象

2) 编码:

`import {createStore} from 'redux'`

`import counter from './reducers/counter'`

`const store = createStore(counter)`

### 8.2.2. store对象

1) 作用: 

redux库最核心的管理对象

2) 它内部维护着:

state

reducer，根据老的状态产生新的状态，一个函数，更新状态必然会调用这个函数

3) 核心方法:

- getState()

- dispatch(action)

- subscribe(listener)：更新组件，重新渲染组件

4) 编码:

- store.getState()

- store.dispatch({type:'INCREMENT', number})

- store.subscribe(render)

### 8.2.3. applyMiddleware()

1) 作用:

应用上基于redux的中间件(插件库)

2) 编码:

```js
import {createStore, applyMiddleware} from 'redux'

import thunk from 'redux-thunk'  // redux异步中间件

const store = createStore(

 counter,

 applyMiddleware(thunk) // 应用上异步中间件

)
```



### 8.2.4. combineReducers()

1) 作用:

合并多个reducer函数

2) 编码:

```js
export default combineReducers({

 user,

 chatUser,

 chat

})
```

```JSX
const INCREMENT = 'INCREMENT';
const DECREMENT = 'DECREMENT';

const counterReducer = (state = 0, action) => {
  switch(action.type) {
    case INCREMENT:
      return state + 1;
    case DECREMENT:
      return state - 1;
    default:
      return state;
  }
};

const LOGIN = 'LOGIN';
const LOGOUT = 'LOGOUT';

const authReducer = (state = {authenticated: false}, action) => {
  switch(action.type) {
    case LOGIN:
      return {
        authenticated: true
      }
    case LOGOUT:
      return {
        authenticated: false
      }
    default:
      return state;
  }
};

const rootReducer = Redux.combineReducers({
  auth: authReducer,
  count: counterReducer
});
const store = Redux.createStore(rootReducer);

```

## 8.3. redux的三个核心概念

### 8.3.1. action

1) 标识要执行行为的对象

2) 包含2个方面的属性

a. type: 标识属性, 值为字符串, 唯一, 必要属性

b. xxx: 数据属性, 值类型任意, 可选属性

3) 例子:

```react
const action = {

type: 'INCREMENT',
data: 2
//number:2
    //无论是number,等都直接取data
}
```

4) Action Creator(创建Action的工厂函数)

```jsx
const increment = (number) => ({type: 'INCREMENT', data: number})

//const increment = (number) => ({type: 'INCREMENT', number})
//大括号表示的是action对象，小括号是为了让其作为对象被处理，否则去掉小括号则会变成函数体。
```

### 8.3.2. reducer

1) 根据老的state和action, 产生新的state的**纯函数**

2) 样例

```js
export default function counter(state = 0, action) {
    //type值有可能增加，有可能减少
    switch (action.type) {
        case 'INCREMENT':
            return state + action.data
        case 'DECREMENT':
            return state - action.data
        default:
            return state
            //最后return的都是新的状态，不要修改原来的状态
    }

}
```

3) 注意

a. 返回一个新的状态

b. 不要修改原来的状态

### 8.3.3. store

1) 将state,action与reducer联系在一起的管理对象

2) 如何得到此对象?

```js
import {createStore} from 'redux'

import reducer from './reducers'

const store = createStore(reducer)
```



3) 此对象的功能?

- getState(): 得到state
- dispatch(action): 分发action, 触发reducer调用, 产生新的state
- subscribe(listener): 注册监听, 当产生了新的state时, 自动调用

## 8.4. 使用redux编写应用

### 8.4.1. 效果

![redux.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gc7tm2ltvmg30a8077myo.gif)

### 8.4.2. 下载依赖包

`npm install --save redux`

### 8.4.3. redux/action-types.js 

```jsx
//action对象的type常量名称模块  
export const INCREMENT = 'increment' 
export const DECREMENT = 'decrement'
```

### 8.4.4. redux/actions.js

```jsx
//action creator模块  
import {INCREMENT, DECREMENT} from './action-types' 
export const increment = number => ({type: INCREMENT, number}) 
export const decrement = number => ({type: DECREMENT, number})
```

### 8.4.5. redux/reducers.js

```jsx
//根据老的state和指定action, 处理返回一个新的state  

import {INCREMENT, DECREMENT} from '../constants/ActionTypes'  
import {INCREMENT, DECREMENT} from './action-types'  
export function counter(state = 0, action) {  
    console.log('counter', state, action)  
    switch (action.type) {   
        case INCREMENT:    
        return state + action.number   
        case DECREMENT:    
        return state - action.number   
        default:    
        return state 
    } 
    }
```



### 8.4.6. components/app.jsx

```jsx
//应用组件 
import React, {Component} from 'react' 
import PropTypes from 'prop-types' 
import as actions from '../redux/actions'  
export default class App extends Component {   
    static propTypes = {   
        store: PropTypes.object.isRequired,  
    }   
    increment = () => {   const number = this.refs.numSelect.value*1   
        this.props.store.dispatch(actions.increment(number))  }   
        decrement = () => {   
            const number = this.refs.numSelect.value*1   
            this.props.store.dispatch(actions.decrement(number))  
        }   
        incrementIfOdd = () => {   
            const number = this.refs.numSelect.value*1    
            let count = this.props.store.getState()   
            if (count % 2 === 1) {    
                this.props.store.dispatch(actions.increment(number))   
            }  
        }   
        incrementAsync = () => {   
            const number = this.refs.numSelect.value*1   
            setTimeout(() => {    
                this.props.store.dispatch(actions.increment(number))   
            }, 1000)  }   
            render() {   
                return (    
                <div>     
                    <p>click {this.props.store.getState()}times{' '}</p>     
                    <select ref="numSelect">      
                    <option value="1">1</option>      
                    <option value="2">2</option>      
                    <option value="3">3</option>    
                    </select>{' '}     
                    <button onClick={this.increment}>+</button>{' '}     
                    <button onClick={this.decrement}>-</button>{' '}     
                    <button onClick={this.incrementIfOdd}>increment if odd</button>{' '}     
                    <button onClick={this.incrementAsync}>increment async</button>    
                    </div>   
                    )  
                } 
            } 
```

### 8.4.7. index.js

```jsx
import React from 'react' 
import ReactDOM from 'react-dom' 
import {createStore} from 'redux'  import App from './components/app' 
import {counter} from './redux/reducers'  
// 根据counter函数创建store对象 
const store = createStore(counter)  
// 定义渲染根组件标签的函数 
const render = () => {  ReactDOM.render(   <App store={store}/>,document.getElementById('root')  ) } 
// 初始化渲染 
render()  
// 注册(订阅)监听, 一旦状态发生改变, 自动重新渲染 
store.subscribe(render)
```

### 8.4.8. 问题

1) redux与react组件的代码耦合度太高,依赖性特别强。

2) 编码不够简洁

## 8.5. react-redux

### 8.5.1. 理解

1) 一个react插件库，区分react-redux 和 redux 

2) 专门用来简化react应用中使用redux

### 8.5.2. React-Redux将所有组件分成两大类

1) UI组件

a. 只负责 UI 的呈现，不带有任何业务逻辑

b. 通过props接收数据(一般数据和函数)

c. 不使用任何 Redux 的 API

d. 一般保存在components文件夹下

2) 容器组件

a. 负责管理数据和业务逻辑，不负责UI的呈现

b. 使用 Redux 的 API

c. 一般保存在containers文件夹下

### 8.5.3. 相关API

1) Provider

让所有组件都可以得到state数据

```jsx
<Provider store={store}>
  <App />
</Provider>
```

2) connect()

用于包装 UI 组件生成容器组件

```jsx
import { connect } from "react-redux";
connect(mapStateToprops, mapDispatchToProps)(Counter);
```

3) mapStateToprops()

将外部的数据（即state对象）转换为UI组件的标签属性

```jsx
const mapStateToprops = function (state) {
    return {
     value: state
    }
}
```

4) mapDispatchToProps()

将分发action的函数转换为UI组件的标签属性

简洁语法可以直接指定为actions对象或包含多个action方法的对象

### 8.5.4. 使用react-redux

1) 下载依赖包

`npm install --save react-redux`

2) `redux/action-types.js`不变

3) `redux/actions.js`不变

4) `redux/reducers.js`不变

5) components/counter.jsx

```jsx
// UI组件: 不包含任何redux API  // 
import React from 'react' 
import PropTypes from 'prop-types'  
export default class Counter extends React.Component {   
    static propTypes = {   
        count: PropTypes.number.isRequired,   
        increment: PropTypes.func.isRequired,   
        decrement: PropTypes.func.isRequired  
    }   
    increment = () => {   
        const number = this.refs.numSelect.value*1   
        this.props.increment(number)  
    }   
        decrement = () => {   
            const number = this.refs.numSelect.value*1   
            this.props.decrement(number)  
        }   
        incrementIfOdd = () => {   
            const number = this.refs.numSelect.value*1   
            let count = this.props.count   
            if (count % 2 === 1) {    
                this.props.increment(number)   
            }  
        }   
        incrementAsync = () => {   
            const number = this.refs.numSelect.value*1   
            setTimeout(() => {    
                this.props.increment(number)   
            }, 1000)  }   
            render() {   return (    
            <div>     
                <p>click {this.props.count} times {' '}</p>    
                <select ref="numSelect">      
                <option value="1">1</option>      
                <option value="2">2</option>      
                <option value="3">3</option>     
                </select>{' '}     
                <button onClick={this.increment}>+</button>{' '}     
                <button onClick={this.decrement}>-</button>{' '}     
                <button onClick={this.incrementIfOdd}>increment if odd</button>{' '}     
                <button onClick={this.incrementAsync}>increment async</button>    
                </div>   
                )  
            } 
        }
```

6) containters/app.jsx

```jsx
//包含Counter组件的容器组件 
import React from 'react' 
// 引入连接函数 import {connect} from 'react-redux' 
// 引入action函数 
import {increment, decrement} from '../redux/actions'  
import Counter from '../components/counter'  
// 向外暴露连接App组件的包装组件 
export default connect(  state => ({count: state}),  {increment, decrement} )(Counter)
```

7) index.js

```jsx
import React from 'react' 
import ReactDOM from 'react-dom' 
import {createStore} from 'redux' 
import {Provider} from 'react-redux'  
import App from './containers/app' 
import {counter} from './redux/reducers'  
// 根据counter函数创建store对象 
const store = createStore(counter)  
// 定义渲染根组件标签的函数 
ReactDOM.render((
<Provider store={store}>    
<App />   
</Provider>  
),  
document.getElementById('root'))
```

### 8.5.5. 问题

1) redux默认是不能进行异步处理的, 

2) 应用中又需要在redux中执行异步任务(ajax, 定时器)

## 8.6. redux异步编程

### 8.6.1. 下载redux插件(异步中间件)

`npm install --save redux-thunk`

### 8.6.2. index.js

```jsx
import {createStore, applyMiddleware} from 'redux' 
import thunk from 'redux-thunk' 
// 根据counter函数创建store对象 
const store = createStore(  counter,  applyMiddleware(thunk) 
// 应用上异步中间件 )
```

### 8.6.3. redux/actions.js

```jsx
// 异步action creator(返回一个函数) 
export const incrementAsync = number => {  
    return dispatch => {   
        setTimeout(() => {    
            dispatch(increment(number))   
        }, 1000)  
    } 
}
```

### 8.6.4. components/counter.jsx

```jsx
incrementAsync = () => {  
    const number = this.refs.numSelect.value*1  
    this.props.incrementAsync(number) 
}
```

### 8.6.5. containers/app.jsx

```jsx
import {increment, decrement, incrementAsync} from '../redux/actions'
// 向外暴露连接App组件的包装组件 
export default connect(  
    state => ({count: state}),  
    {increment, decrement, incrementAsync} 
    )(Counter)
```

 ```jsx
const REQUESTING_DATA = 'REQUESTING_DATA'
const RECEIVED_DATA = 'RECEIVED_DATA'

const requestingData = () => { return {type: REQUESTING_DATA} }
const receivedData = (data) => { return {type: RECEIVED_DATA, users: data.users} }

const handleAsync = () => {
  return function(dispatch) {
    // dispatch request action here
dispatch(requestingData());
    setTimeout(function() {
      let data = {
        users: ['Jeff', 'William', 'Alice']
      }
      dispatch(receivedData(data))
      // dispatch received data action here

    }, 2500);
  }
};

const defaultState = {
  fetching: false,
  users: []
};

const asyncDataReducer = (state = defaultState, action) => {
  switch(action.type) {
    case REQUESTING_DATA:
      return {
        fetching: true,
        users: []
      }
    case RECEIVED_DATA:
      return {
        fetching: false,
        users: action.users
      }
    default:
      return state;
  }
};

const store = Redux.createStore(
  asyncDataReducer,
  Redux.applyMiddleware(ReduxThunk.default)
);

 ```



## 8.7. 使用上redux调试工具

### 8.7.1. 安装chrome浏览器插件

![img](file:////var/folders/0l/t83007b55bqgp9rdgmjr7cfr0000gn/T/com.kingsoft.wpsoffice.mac/wps-xusumu/ksohtml/wpskBrF1v.png)

### 8.7.2. 下载工具依赖包

`npm install --save-dev redux-devtools-extension`

### 8.7.3. 编码

```jsx
import { composeWithDevTools } from 'redux-devtools-extension' 
const store = createStore(  
    counter,  
    composeWithDevTools(applyMiddleware(thunk))  
)
```

## 8.8. 相关重要知识: 纯函数和高阶函数

### 8.8.1. 纯函数

1) 一类特别的函数: 只要是同样的输入，必定得到同样的输出

2) 必须遵守以下一些约束 

a. 不得改写参数

b. 不能调用系统 I/O 的API

c. 能调用Date.now()或者Math.random()等不纯的方法 

3) reducer函数必须是一个纯函数

### 8.8.2. 高阶函数

4) 理解: 一类特别的函数

a. 情况1: 参数是函数

b. 情况2: 返回是函数

5) 常见的高阶函数: 

a. 定时器设置函数

b. 数组的map()/filter()/reduce()/find()/bind()

c. react-redux中的connect函数

6) 作用: 

a. 能实现更加动态, 更加可扩展的功能

# make conditional decisions 

## Use && for a More Concise Conditional

 ```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      display: true
    }
    this.toggleDisplay = this.toggleDisplay.bind(this);
  }
  toggleDisplay() {
    this.setState(state => ({
      display: !state.display
    }));
  }
  render() {
    // change code below this line
    return (
       <div>
         <button onClick={this.toggleDisplay}>Toggle Display</button>
         {this.state.display&&<h1>Displayed!</h1>}
       </div>
    );
  }
};

 ```

## Render with an If-Else Condition

 ```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      display: true
    }
 this.toggleDisplay = this.toggleDisplay.bind(this);
 }
  toggleDisplay() {
    this.setState({
      display: !this.state.display
    });
  }
  render() {
    // change code below this line
    if (this.state.display) {
      return (
         <div>
           <button onClick={this.toggleDisplay}>Toggle Display</button>
           <h1>Displayed!</h1>
         </div>
      );
    } else {
      return (
        <div>
           <button onClick={this.toggleDisplay}>Toggle Display</button>
         </div>
      );
    }
  }
};
 ```

## Use a Ternary Expression for Conditional Rendering

  *ternary operator* : `condition ? expressionIfTrue : expressionIfFalse`

```jsx
const inputStyle = {
  width: 235,
  margin: 5
}

class CheckUserAge extends React.Component {
  constructor(props) {
    super(props);
    // change code below this line
    this.state = {
      input:"",
      userAge:""
    }
    // change code above this line
    this.submit = this.submit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.setState({
      input: e.target.value,
      userAge: ''
    });
  }
  submit() {
    this.setState(state => ({
      userAge: state.input
    }));
  }
  render() {
    const buttonOne = <button onClick={this.submit}>Submit</button>;
    const buttonTwo = <button>You May Enter</button>;
    const buttonThree = <button>You Shall Not Pass</button>;
    return (
      <div>
        <h3>Enter Your Age to Continue</h3>
        <input
          style={inputStyle}
          type="number"
          value={this.state.input}
          onChange={this.handleChange} /><br />
        {
          /* change code here */
          /*condition ? expressionIfTrue : expressionIfFalse
*/
        }
        {
          this.state.userAge === ''
            ? buttonOne
            : this.state.userAge >= 18
              ? buttonTwo
              : buttonThree
          }
      </div>
    );
  }
};

```

## Render Conditionally from Props

```jsx
class Results extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <h1>
      
        {this.props.fiftyFifty ? "You Win!" : "You Lose!"}
      
      </h1>
    )
  };
};

class GameOfChance extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 1
    }
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    this.setState({
      counter: this.state.counter+1 // change code here
    });
  }
  render() {
    const expression = Math.random() >= .5; // change code here
    return (
      <div>
        <button onClick={this.handleClick}>Play Again</button>
        { /* change code below this line */ }
<Results fiftyFifty={expression}/>
        { /* change code above this line */ }
        <p>{'Turn: ' + this.state.counter}</p>
      </div>
    );
  }
};

```

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
if(this.state.input.length > 15){
inputStyle.border =  '3px solid red'

}
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
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
      users: [
        {
          username: 'Jeff',
          online: true
        },
        {
          username: 'Alan',
          online: false
        },
        {
          username: 'Mary',
          online: true
        },
        {
          username: 'Jim',
          online: false
        },
        {
          username: 'Sara',
          online: true
        },
        {
          username: 'Laura',
          online: true
        }
      ]
    }
  }
  render() {
    const usersOnline = this.state.users; 
    // change code here
    const renderOnline = usersOnline.filter(user=>user.online==true); 
    // change code here
    return (
       <div>
         <h1>Current Online Users:</h1>
         <ul>
           {renderOnline.map(i=><li key={i.username +1}>{i.username }</li>)}
         </ul>
       </div>
    );
  }
};

```

### Register a Store Listener

监听是为了在状态更新的时候能够重绘组件

```jsx
const ADD = 'ADD';

const reducer = (state = 0, action) => {
  switch(action.type) {
    case ADD:
      return state + 1;
    default:
      return state;
  }
};

const store = Redux.createStore(reducer);

// global count variable:
let count = 0;

// change code below this line
//状态更新
const increments = function increments(){
  return count+=1;
}

//const addOne = () => (count += 1);
//状态更新后重绘组件
store.subscribe(increments)
// change code above this line

//动作分发，动作产生，每分发一次则add,则state+1
store.dispatch({type: ADD});
console.log(count);
store.dispatch({type: ADD});
console.log(count);
store.dispatch({type: ADD});
console.log(count);

```

## Redux: Never Mutate State

```jsx
const ADD_TO_DO = 'ADD_TO_DO';

// A list of strings representing tasks to do:
const todos = [
  'Go to the store',
  'Clean the house',
  'Cook dinner',
  'Learn to code',
];

const immutableReducer = (state = todos, action) => {
  switch(action.type) {
    case ADD_TO_DO:
      // don't mutate state here or the tests will fail
      return state.concat(action.todo)
    default:
      return state;
  }
};

// an example todo argument would be 'Learn React',
const addToDo = (todo) => {
  return {
    type: ADD_TO_DO,
    todo
  }
}

const store = Redux.createStore(immutableReducer);

```

## Spread Operator on Arrays

`let newArray = [...myArray];`

write `[...myArray, 'new value']`. This would return a new array composed of the values in `myArray` and the string `'new value'` as the last value

only makes a shallow copy of the array. That is to say, it only provides immutable array operations for one-dimensional arrays.

```jsx
const immutableReducer = (state = ['Do not mutate state!'], action) => {
  switch(action.type) {
    case 'ADD_TO_DO':
      // don't mutate state here or the tests will fail
      return [...state, action.todo]
    default:
      return state;
  }
};

const addToDo = (todo) => {
  return {
    type: 'ADD_TO_DO',
    todo
  }
}

const store = Redux.createStore(immutableReducer);

```

## Copy an Object with Object.assign

`const newObject = Object.assign({}, obj1, obj2);`

```jsx
const defaultState = {
  user: 'CamperBot',
  status: 'offline',
  friends: '732,982',
  community: 'freeCodeCamp'
};

const immutableReducer = (state = defaultState, action) => {
  switch(action.type) {
    case 'ONLINE':
      // don't mutate state here or the tests will fail
      return
    default:
      return state;
  }
};

const wakeUp = () => {
  return {
    type: 'ONLINE'
  }
};

const store = Redux.createStore(immutableReducer);

```

## Remove an Item from an Array

有点没弄明白

https://www.freecodecamp.org/learn/front-end-libraries/redux/remove-an-item-from-an-array

componentDidMount处理异步请求





