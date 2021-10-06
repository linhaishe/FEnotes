# React


## 1. 脚手架
### 什么是脚手架
1. xxx 脚手架: 用来帮助程序员快速创建一个基于 xxx 库的模板项目

- 包含了所有需要的配置（语法检查、jsx 编译、devServer…）
- 下载好了所有相关的依赖
- 可以直接运行一个简单效果

2. react 提供了一个用于创建 react 项目的脚手架库: create-react-app
3. 项目的整体技术架构为: react + webpack + es6 + eslint
4. 使用脚手架开发的项目的特点: 模块化, 组件化, 工程化

### 脚手架创建

1. 第一步，全局安装：npm i -g create-react-app

2. 第二步，切换到想创项目的目录，使用命令：create-react-app hello-react

3. 第三步，进入项目文件夹：cd hello-react

4. 第四步，启动项目：npm start

### 文件分析


```
public ---- 静态资源文件夹

        favicon.icon ------ 网站页签图标

        index.html -------- 主页面

        logo192.png ------- logo图

        logo512.png ------- logo图

        manifest.json ----- 应用加壳的配置文件，移动端的配置

        robots.txt -------- 爬虫协议文件，类似小程序的sitemap,给浏览器搜索引擎用的，写入相关关键词，浏览器可搜索到。

src ---- 源码文件夹

        App.css -------- App组件的样式

        App.js --------- App组件

        App.test.js ---- 用于给App做测试

        index.css ------ 样式

        index.js ------- 入口文件

        logo.svg ------- logo图

        reportWebVitals.js

            --- 页面性能分析文件(需要web-vitals库的支持)

       setupTests.js

           ---- 组件单元测试的文件(需要jest-dom库的支持)

```

### 脚手架安装报错

5. https://stackoverflow.com/questions/67399785/how-to-solve-npm-install-error-npm-err-code-1

6. 由于自己下载的是 node 最新版本 16.XX,导致安装失败，一直报错。

7. 使用 nvm 版本管理，下载了最新的稳定版本。并使用 nvm use 14.17.4,转换为稳定版本。nvm ls 查看通过 nvm 下载的 node 版本进行切换

8. 由于 node 删除失败，选择通过 nvm 进行版本转换。

9. nvm use 14.17.4,转换 node 版本

10. 使用以下命令可以改变默认的版本：nvm alias default v4.3.0 这样就不用每次都切换版本了

11. 相关资料：

- https://segmentfault.com/a/1190000039188394

- https://zhuanlan.zhihu.com/p/99841609

- https://segmentfault.com/a/1190000004330350

- https://zhuanlan.zhihu.com/p/89158928

## 2. React 简介

### 1. react 官网

1. 英文官网:[ https://reactjs.org/](https://reactjs.org/)

2. 中文官网: https://react.docschina.org/

### 2. 相关 js 库

1. react.js：React 核心库。

2. react-dom.js：提供操作 DOM 的 react 扩展库。

3. babel.min.js：解析 JSX 语法代码转为 JS 代码的库。

### 3. 介绍描述

1. 用于动态构建用户界面的 JavaScript 库(只关注于视图)

2. 由 Facebook 开源

### 4. React 的特点

1. 声明式编码

2. 组件化编码

3. React Native 编写原生应用

4. 高效（优秀的 Diffing 算法）

### 5. React 高效的原因

1. 使用虚拟(virtual)DOM, 不总是直接操作页面真实 DOM。
2. DOM Diffing 算法, 最小化页面重绘。
3. react 中{}为分隔符，只有在这里面...p 才能展开对象，仅适用于标签属性传递时使用。

`<Com {...person}/>`

### 6. 虚拟DOM和真实DOM

1. React提供了一些API来创建一种 “特别” 的一般js对象

```js
const vDom1 = React.createElement(
  "h2",
  { id: myId.toLowerCase() },
  msg.toUpperCase()
);
//上面创建的就是一个简单的虚拟DOM对象
```

2. 虚拟DOM对象最终都会被React转换为真实的DOM
3. 我们编码时基本只需要操作react的虚拟DOM相关数据, react会转换为真实DOM变化而更新界。

## 3. 基本使用

### 1. JSX

1. 全称:  JavaScript XML

2. react定义的一种类似于XML的JS扩展语法: 

```jsx
const vDom1 = React.createElement(
  "h2",
  { id: myId.toLowerCase() },
  msg.toUpperCase()
);
//JS + XML本质是上面创建的方法的语法糖
```

3. 作用: 用来简化创建虚拟DOM 

- 1) 写法：`const ele = <h1>hello jsx</h1>`

- 2) 注意1：它不是字符串, 也不是HTML/XML标签

- 3) 注意2：它最终产生的就是一个JS对象

4. 标签名任意: HTML标签或其它标签

5. 标签属性任意: HTML标签属性或其它

6. 基本语法规则

- 1) 遇到 <开头的代码, 以标签的语法解析: html同名标签转换为html同名元素, 其它标签需要特别解析

- 2) 遇到以 { 开头的代码，以JS语法解析: 标签中的js表达式必须用{ }包含

7. babel.js的作用

- 1) 浏览器不能直接解析JSX代码, 需要babel转译为纯JS的代码才能运行

- 2) 只要用了JSX，都要加上type="text/babel", 声明需要babel来处理

8. 渲染虚拟DOM(元素)

   1. 语法: ` ReactDOM.render(vDom2, document.getElementById("test3"));`

   2. 作用: 将虚拟DOM元素渲染到页面中的真实容器DOM中显示

   3. 参数说明

      - 1) 参数一: 纯js或jsx创建的虚拟dom对象

      - 2) 参数二: 用来包含虚拟DOM元素的真实dom元素对象(一般是一个div)

### 2. 模块与组件、模块化与组件化的理解

#### 1. 模块

1. 理解：向外提供特定功能的js程序, 一般就是一个js文件

2. 为什么要拆成模块：随着业务逻辑增加，代码越来越多且复杂。

3. 作用：复用js, 简化js的编写, 提高js运行效率

#### 2. 组件

1. 能效果的代码和资源的集合(html/css/js/image等等)

2. 为什么要用组件： 一个界面的功能更复杂
3. 作用：复用编码, 简化项目编码, 提高运行效率

#### 3. 模块化

当应用的js都以模块来编写的, 这个应用就是一个模块化的应用

#### 4. 组件化

当应用是以多组件的方式实现, 这个应用就是一个组件化的应用

[**02_component**](https://github.com/linhaishe/hello-react/tree/master/react_test/02_component)

##### 1. 函数式组件

```jsx
//html
<div id="example"></div>


//js
//名字要大写

function DemoComponent() {
		return <h2>use JavaScript function 函数组件</h2>;
}

ReactDOM.render(<DemoComponent />, document.getElementById("example"));

// 1.React解析组件标签，DemoComponent组件。
// 2.发现组件是使用函数定义的，随后调用该函数，将返回的虚拟DOM转为真实DOM，随后呈现在页面中。
```

##### 2. Class组件，类组件

```jsx
// 2. use ES6 `class` syntax 类组件使用
class DemoComponent3 extends React.Component {
  render() {
    return <h1>use ES6 `class` syntax</h1>;
  }
}

ReactDOM.render(<DemoComponent3 />, document.getElementById("example3"));

/* 
			执行了ReactDOM.render(<MyComponent/>.......之后，发生了什么？
					1.React解析组件标签，找到了MyComponent组件。
					2.发现组件是使用类定义的，随后new出来该类的实例，并通过该实例调用到原型上的render方法。
					3.将render返回的虚拟DOM转为真实DOM，随后呈现在页面中。
*/

```

### 3. 循环遍历

[Demolink](https://github.com/linhaishe/hello-react/tree/master/react_test/01_HelloWorld)

动态展示列表数据,将一个数据的数组转化为一个标签的数组

```jsx
<ul>
<li>{name}</li>
</ul>
```

以一个页面的方式去使用时(仅在讲基础例子的时候使用，之后的项目用脚手架)

以文件的方式在页面中使用需要引入三个文件

### 4. Props

[props-demo](https://github.com/linhaishe/hello-react/tree/master/react_test/04_component_props)

#### 1. 理解

a. 每个组件对象都会有props(properties的简写)属性

b. 组件标签的所有属性都保存在props中

c. 通过标签属性从组件外向组件内传递变化的数据

d. 注意: 组件内部不要修改props数据

#### 2. class组件里的state

```jsx
class Person extends React.Component {
  constructor(props) {
    //构造器是否接收props，是否传递给super，取决于：是否希望在构造器中通过this访问props
    // console.log(props);
    super(props);
    console.log("constructor", this.props);
  }

  //对标签属性进行类型、必要性的限制
  static propTypes = {
    name: PropTypes.string.isRequired, //限制name必传，且为字符串
    sex: PropTypes.string, //限制sex为字符串
    age: PropTypes.number, //限制age为数值
  };

  //指定默认标签属性值
  static defaultProps = {
    sex: "男", //sex默认值为男
    age: 18, //age默认值为18
  };

  render() {
    // console.log(this);
    const { name, age, sex } = this.props;
    //props是只读的
    //this.props.name = 'jack' //此行代码会报错，因为props是只读的
    return (
      <ul>
        <li>姓名：{name}</li>
        <li>性别：{sex}</li>
        <li>年龄：{age + 1}</li>
      </ul>
    );
  }
}

//渲染组件到页面
ReactDOM.render(<Person name="jerry" />, document.getElementById("test1"));

```

#### 3. 函数式组件里的state

```jsx
import React, { Component } from "react";
//引入属性所需的插件
import PropTypes from "prop-types";

//创建组件
function Person(props) {
  const { name, age, sex } = props;
  return (
    <ul>
      <li>姓名：{name}</li>
      <li>性别：{sex}</li>
      <li>年龄：{age}</li>
    </ul>
  );
}

Person.propTypes = {
  name: PropTypes.string.isRequired, //限制name必传，且为字符串
  sex: PropTypes.string, //限制sex为字符串
  age: PropTypes.number, //限制age为数值
};

//指定默认标签属性值
Person.defaultProps = {
  sex: "男", //sex默认值为男
  age: 18, //age默认值为18
};
//渲染组件到页面
ReactDOM.render(<Person name="jerry" />, document.getElementById("test1"));

```

### 5. state

[demo- link](https://github.com/linhaishe/hello-react/tree/master/react_test/03_component_state)

1. state是组件对象最重要的属性, 值是对象(可以包含多个key-value的组合)

2. 组件被称为"状态机", 通过更新组件的state来更新对应的页面显示(重新渲染组件)

3. 组件中render方法中的this为组件实例对象

4.  组件自定义的方法中this为undefined，如何解决？

   - a) 强制绑定this: 通过函数对象的bind()

   - b) 箭头函数
5. 状态数据，不能直接修改或更新

#### 1. Function components state

#### 2. class component state

##### simplify ver

```jsx
import React, { Component } from "react";

export default class text extends Component {
  //给组件对象添加state属性，默认的原始值是null,组件对象是this.state中的this
  state = {
    comments: [
      { username: "tom", content: "react is good!" },
      { username: "jack", content: "react is so hard!" },
    ],
  };
  //数据在哪个组件，更新数据的行为就应该定义在在哪个组件

  addComment = (comment) => {
    const { comments } = this.state;
    comments.unshift(comment);
    this.setState({ comments });
  };

  render() {
      //拿到state中的数据
    const { comments } = this.state;
    return (
      <div>
        <header className="site-header jumbotron">
          <div className="container">
            <div className="row">
              <div className="col-xs-12">
                <h1>请发表对React的评论</h1>
              </div>
            </div>
          </div>
        </header>
        <div className="container">
          <CommentAdd addComment={this.addComment} />
          <CommentList comments={comments} deleteComment={this.deleteComment} />
        </div>
      </div>
    );
  }
}
```

##### constructor ver

```jsx
class Input extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isInput: false,
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    const isInput = !this.state.isInput;
    this.setState({ isInput });
  }

  //如果不想使用bind绑定this的话，可以使用箭头函数改变this指向

  render() {
    const { isInput } = this.state;

    return (
      <h2 onClick={this.handleClick}>
        {isInput ? "已输入(true)" : "请输入(false)"}
      </h2>
    );
  }
}

ReactDOM.render(<Input />, document.getElementById("example"));
```

### 6. refs

[refs-demo](https://github.com/linhaishe/hello-react/tree/master/react_test/05_component_refs_event)

1. 字符串形式的 ref

`<input ref="input1"/>`

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.showInput = this.showInput.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
  }

  showInput() {
    //获得Input的输入值
    //可以看到this的内容，里面有refs，从里面拿到content 的值
    console.log(this);
    const input = this.refs.content;
    alert(input.value);
  }

  handleBlur(event) {
    alert(event.target.value);
  }

  render() {
    return (
      <div>
        {/*官方不建议用的方式*/}

        <input type="text" ref="content" />
        <br />
        {/*交互绑定事件监听,绑定事件监听函数的时候不能加上()进行调用*/}
        <button onClick={this.showInput}>plz input sth3...</button>

        <br />
        <input
          type="text"
          placeholder="失去焦点提示内容"
          onBlur={this.handleBlur}
        />
      </div>
    );
  }
}

```

2. 回调形式的 ref

`<input ref={(c)=>{this.input1 = c}}/>`

```jsx
//创建组件
class Demo extends React.Component {
  //展示左侧输入框的数据
  showData = () => {
    const { input1 } = this;
    alert(input1.value);
  };
  //展示右侧输入框的数据
  showData2 = () => {
    const { input2 } = this;
    alert(input2.value);
  };
  render() {
    return (
      <div>
        <input
          ref={(c) => (this.input1 = c)}
          type="text"
          placeholder="点击按钮提示数据"
        />
        &nbsp;
        <button onClick={this.showData}>点我提示左侧的数据</button>&nbsp;
        <input
          onBlur={this.showData2}
          ref={(c) => (this.input2 = c)}
          type="text"
          placeholder="失去焦点提示数据"
        />
        &nbsp;
      </div>
    );
  }
}
```

3. createRef 创建 ref 容器

```jsx
//创建组件
class Demo extends React.Component {
/* 
React.createRef调用后可以返回一个容器，该容器可以存储被ref所标识的节点,该容器是“专人专用”的
*/
  myRef = React.createRef();
  myRef2 = React.createRef();
  //展示左侧输入框的数据
  showData = () => {
    alert(this.myRef.current.value);
  };
  //展示右侧输入框的数据
  showData2 = () => {
    alert(this.myRef2.current.value);
  };
  render() {
    return (
      <div>
        <input ref={this.myRef} type="text" placeholder="点击按钮提示数据" />
        &nbsp;
        <button onClick={this.showData}>点我提示左侧的数据</button>&nbsp;
        <input
          onBlur={this.showData2}
          ref={this.myRef2}
          type="text"
          placeholder="失去焦点提示数据"
        />
        &nbsp;
      </div>
    );
  }
}

```

### 7. 事件处理

1. 通过 onXxx 属性指定事件处理函数(注意大小写)

- 1)React 使用的是自定义(合成)事件, 而不是使用的原生 DOM 事件

- 2)React 中的事件是通过事件委托方式处理的(委托给组件最外层的元素)

2. 通过 event.target 得到发生事件的 DOM 元素对象
3. 在组件中添加事件处理方法
   `eventHandler(event) {}`

### react EventListener

[SyntheticEvent - React](https://facebook.github.io/react/docs/events.html#supported-events) 更多的事件监听的方法

1. 绑定事件监听
   事件名,回调函数

2. 触发事件
   用户对对应的界面做对应的操作,编码

没有经过特殊处理的话，**这些 `on\*` 的事件监听只能用在普通的 HTML 的标签上，而不能用在组件标签上**。 

```jsx
class Title extends Component {
    //camelcase驼峰命名法
  handleClickOnTitle () {
    console.log('Click on title.')
  }

  render () {
    return (
        //注意this
      <h1 onClick={this.handleClickOnTitle}>React 小书</h1>
    )
  }
}

//output Click on title.
```

方法是被包装好的，直接使用就可以。 这些事件属性名都必须要用驼峰命名法。 

```jsx
class Title extends Component {
  handleClickOnTitle (e) {
    console.log(e.target.innerHTML)
  }

  render () {
    return (
      <h1 onClick={this.handleClickOnTitle}>React 小书</h1>
    )
  }
}

//output React 小书
```

#### bind()

事件监听方法需要手动 `bind` 到当前实例 

 JavaScript 的 [this](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this) 和 [bind](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) 

```jsx
class Title extends Component {
  handleClickOnTitle (e) {
    console.log(this)
  }

  render () {
    return (
      <h1 onClick={this.handleClickOnTitle.bind(this)}>React 小书</h1>
    )
  }
}
```

```jsx
class Title extends Component {
  handleClickOnTitle (word, e) {
    console.log(this, word)
  }

  render () {
    return (
      <h1 onClick={this.handleClickOnTitle.bind(this, 'Hello')}>React 小书</h1>
    )
  }
}
```

### 8. forms

[forms-demo](https://github.com/linhaishe/hello-react/tree/master/react_test/07_component_form)

1. 受控组件

- 通过 onChange 进行数据获取

2. 非受控组件(尽量少用)

- 通过 ref 进行控制

```jsx
//定义组件
class App extends React.Component {
  constructor(props) {
    super(props);
    //初始化状态
    this.state = {
      pwd: "",
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleSubmit(event) {
    //阻止事件的默认行为，即阻止表单提交，点击login后会自动进行提交行为
    event.preventDefault();
    //获得input中的内容
    const name = this.nameInput.value;
    const { pwd } = this.state;
    alert(`uername is ${name} , password is ${pwd}`);
  }

  handleChange(event) {
    //读取pwd输入框的值
    const pwd = event.target.value;
    //更新输入框的状态
    this.setState({ pwd });
  }

  render() {
    return (
      <div>
        {/*一般表单会自动提交，我们这个功能不需要表单进行提交需要阻止默认行为*/}
        <form onSubmit={this.handleSubmit}>
          username : {/*非受控组件*/}
          <input type="text" ref={(input) => (this.nameInput = input)} />
          <br />
          {/*设置pwd默认属性后，输入框不能输入，需要用到onchange 我们需要将交互中的输入内容传输到state状态中*/}
          password : {/*受控组件，建议写受控组件对表单进行处理*/}
          <input
            type="password"
            value={this.state.pwd}
            onChange={this.handleChange}
          />
          <br />
          <input type="checkbox" /> 篮球
          <input type="checkbox" /> 足球
          <br />
          <select name="" id="">
            <option value="male">男</option>
            <option value="female">女</option>
          </select>
          <br />
          <input type="submit" value="login" />
        </form>
      </div>
    );
  }
}

```

### 9. lifecircle

你可以使用此[生命周期图谱](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)作为速查表

1. componentWillMount 挂在前 不用了

2. componentDidMount 挂在后

3. componentWillUpdate 数据更新前 即将不用了

4. componentDidUpdate 数据更新后

5. componentWillUnmount 组件卸载前

```jsx
class LifeCircle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      opacity: 1,
    };
    this.distroyComponent = this.distroyComponent.bind(this);
  }
  
 //移除组件
  distroyComponent() {
    ReactDOM.unmountComponentAtNode(document.getElementById("example"));
  }

  componentWillMount() {
    console.log("componentWillMount(),组件挂载前");
  }

  componentDidMount() {
    console.log("componentDidMount(),组件已挂载");
    //启动循环定时器
    //重写已经内置好的componentDidMount()函数，所以需要bind(this)
    //注意this的指向,setInterval的回调函数是window
    this.intervalid = setInterval(
      function () {
        console.log("启动循环定时器");
        let { opacity } = this.state;
        opacity -= 0.1;
        if (opacity <= 0) {
          opacity = 1;
        }
        this.setState({ opacity });
      }.bind(this),
      200
    );
  }

  //组件卸载前
  componentWillUnmount() {
    //清理定时器
    //clearInterval是已经写好的函数MDN
    clearInterval(this.intervalid);
  }

  render() {
    const { opacity } = this.state;
    return (
      <div>
        {/*注意两个大括号是不同的作用，第一个大括号是表示jsx语法，第二个是对象*/}
        <h2 style={{ opacity: opacity }}>{this.props.msg}</h2>
        <button onClick={this.distroyComponent}>give up</button>
      </div>
    );
  }
}

ReactDOM.render(
  <LifeCircle msg="react is so hard" />,
  document.getElementById("example")
);
```

### 10. request

[Demolink](https://github.com/linhaishe/hello-react/tree/master/react_test/10_ajax)

#### 1. axios

```jsx
// 需要两个数据，仓库的名称，仓库的URL
class MostStarRepo extends React.Component {
  state = {
    repoName: "",
    repoUrl: "",
  };

  componentDidMount() {
    //使用axios发送异步的ajax请求

    //axios请求和响应的拦截，统一的用axios去处理
    //有两个方法可以用，get/post请求
    const url = `https://api.github.com/search/repositories?q=re&sort=stars`;
    axios
      .get(url)
      .then((response) => {
        const result = response.data;
        //console.log(response);
        //得到数据
        const { name, html_url } = result.items[0];
        //更新状态
        this.setState({ repoName: name, repoUrl: html_url });
      })
      .catch((error) => {
        alert(error.message);
      });
  }

  render() {
    const { repoName, repoUrl } = this.state;
    if (!repoName) {
      return <h2>loading...</h2>;
    } else {
      return (
        <h2>
          Most star repo is <a href={repoUrl}>{repoName}</a>
        </h2>
      );
    }
  }
}

```

#### 2. fetch

```jsx
// 需要两个数据，仓库的名称，仓库的URL
class MostStarRepo extends React.Component {
  state = {
    repoName: "",
    repoUrl: "",
  };

  componentDidMount() {
    //使用axios发送异步的ajax请求

    //axios请求和响应的拦截，统一的用axios去处理
    //有两个方法可以用，get/post请求
    const url = `https://api.github.com/search/repositories?q=re&sort=stars`;

    // 使用fetch发送异步的ajax请求
    fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        //得到数据
        const { name, html_url } = data.items[0];
        //更新状态
        this.setState({ repoName: name, repoUrl: html_url });
      });
  }

  render() {
    const { repoName, repoUrl } = this.state;
    if (!repoName) {
      return <h2>loading...</h2>;
    } else {
      return (
        <h2>
          Most star repo is <a href={repoUrl}>{repoName}</a>
        </h2>
      );
    }
  }
}

```

### 11. conditional rendering

[Demolink](https://github.com/linhaishe/hello-react/tree/master/react_test/11_Conditional_Rendering)

```jsx
let Box1 = function Box1(props) {
  return <div className="box">box1</div>;
};

let Box2 = function Box2(props) {
  return <div className="box">box2</div>;
};

let Box3 = function Box3(props) {
  return <div className="box">box3</div>;
};

//{this.state.sel==0?<Box1/>:this.state.sel==1?<Box2/>:<Box3/>}
// onClick={this.handleToggleClick(0)}
class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = { sel: 0 };
    //this.handleToggleClick = this.handleToggleClick.bind(this);
  }

  handleToggleClick(n) {
    let num = n;
    this.setState({
      sel: num,
    });
  }

  render() {
    return (
      <div>
        <button onClick={this.handleToggleClick.bind(this, 0)}>
          box1Show2
        </button>
        <button onClick={this.handleToggleClick.bind(this, 1)}>box2Show</button>
        <button onClick={this.handleToggleClick.bind(this, 2)}>box3Show</button>
        {this.state.sel == 0 ? (
          <Box1 />
        ) : this.state.sel == 1 ? (
          <Box2 />
        ) : (
          <Box3 />
        )}
      </div>
    );
  }
}

```

## 4. 高阶函数，高阶组件，函数柯理化

简单来说，就是一个函数里面又返回了一个函数，一个组件里面有返回了一个组件

**高阶函数**：如果一个函数符合下面2个规范中的任何一个，那该函数就是高阶函数。

1. 若A函数，接收的参数是一个函数，那么A就可以称之为高阶函数。

2. 若A函数，调用的返回值依然是一个函数，那么A就可以称之为高阶函数。

常见的高阶函数有：Promise、setTimeout、arr.map()等等

**函数的柯里化**：通过函数调用继续返回函数的方式，实现多次接收参数最后统一处理的函数编码形式。 

```js
function sum(a) {
  return (b) => {
    return (c) => {
      return a + b + c;
    };
  };
}
```

```jsx
class Login extends React.Component {
  //初始化状态
  state = {
    username: "", //用户名
    password: "", //密码
  };

  //保存表单数据到状态中
  saveFormData = (dataType) => {
    return (event) => {
      this.setState({ [dataType]: event.target.value });
    };
  };

  //表单提交的回调
  handleSubmit = (event) => {
    event.preventDefault(); //阻止表单提交
    const { username, password } = this.state;
    alert(`你输入的用户名是：${username},你输入的密码是：${password}`);
  };
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        用户名：
        <input
          onChange={this.saveFormData("username")}
          type="text"
          name="username"
        />
        密码：
        <input
          onChange={this.saveFormData("password")}
          type="password"
          name="password"
        />
        <button>登录</button>
      </form>
    );
  }
}

```

## 5. 命令式编程与声明式编程

1. 声明式编程
   只关注做什么, 而不关注怎么做(流程),  类似于填空题
2. 命令式编程
   要关注做什么和怎么做(流程), 类似于问答题

```js
var arr = [1, 3, 5, 7]
// 需求: 得到一个新的数组, 数组中每个元素都比arr中对应的元素大10: [11, 13, 15, 17]
// 命令式编程
var arr2 = []
for(var i =0;i<arr.length;i++) {
	arr2.push(arr[i]+10)
}
console.log(arr2)
// 声明式编程
var arr3 = arr.map(function(item){
	return item +10
})
// 声明式编程是建立命令式编程的基础上

// 数组中常见声明式方法
	map() / forEach() / find() / findIndex()
```



# react router

1. 下载 react-router-dom: npm install --save react-router-dom

相关资料：

github主页: https://github.com/ReactTraining/react-router
官网教程: https://github.com/reactjs/react-router-tutorial
阮一峰教程: http://www.ruanyifeng.com/blog/2016/05/react_router.html

### 一、路由介绍

#### 1. SPA 的理解

1. 单页 Web 应用（single page web application，SPA）。
2. 整个应用只有一个完整的页面。
3. 点击页面中的链接不会刷新页面，只会做页面的局部更新。
4. 数据都需要通过 ajax 请求获取, 并在前端异步展现。

#### 2. 路由的理解

##### 1. 什么是路由?

1. 一个路由就是一个映射关系(key:value)

2. key 为路径, value 可能是 function 或 component

##### 2. 路由分类

- 1.后端路由：

1. 理解： value 是 function, 用来处理客户端提交的请求。
2. 注册路由：` router.get(path, function(req, res))`
3. 工作过程：当 node 接收到一个请求时, 根据请求路径找到匹配的路由, 调用路由中的函数来处理请求, 返回响应数据

- 2.前端路由：

1. 浏览器端路由，value 是 component，用于展示页面内容。
2. 注册路由: `<Route path="/test" component={Test}> `
3. 工作过程：当浏览器的 path 变为/test 时, 当前路由组件就会变为 Test 组件

#### 3. react-router-dom 的理解

1. react 的一个插件库。
2. 专门用来实现一个 SPA 应用。
3. 基于 react 的项目基本都会用到此库。

#### 4. react-router-dom 相关 API

##### 1. 内置组件

1. `<BrowserRouter>`
   所有的路由都由一个路由器控制，即整个 app 应用中，只需要一个路由器去控制即可。
   有两种路由，BrowserRouter，HashRouter，按情况使用其中一种路由即可。为了方便，将路由包裹在根组件入口文件的地方。
   
   ```jsx
   ReactDOM.render(
   //一旦用了router,必须用路由组件包裹起来，用路由组件管理整个应用
   <BrowserRouter>
    <App />
   </BrowserRouter>,
   /*<HashRouter>
      <App />
    </HashRouter>*/
   document.getElementById("root")
   );
   ```

2. `<HashRouter>`
3. `<Route>`
4. `<Redirect>`
5. `<Link>`
6. `<NavLink>`
7. `<Switch>`

8. Link 按钮

`to="/xxx"` 

`to={``} `

`to={{}}`

```
to={{
		pathname: "/courses",
		search: "?sort=name",
		hash: "#the-hash",
		state: { fromDashboard: true }
}}
```

##### 2. 其它

1. history 对象
2. match 对象
3. withRouter 函数

## 三、路由的基本使用

1. 明确好界面中的导航区、展示区
2. 导航区的 a 标签改为 Link 标签
   `<Link to="/xxxxx">Demo</Link>`
3. 展示区写 Route 标签进行路径的匹配
   `<Route path='/xxxx' component={Demo}/>`
4. `<App>`的最外侧包裹了一个`<BrowserRouter>`或`<HashRouter>`

```jsx
export default class App extends Component {
	render() {
		return (
			<div>
				<div className="row">
					<div className="col-xs-offset-2 col-xs-8">
						<div className="page-header"><h2>React Router Demo</h2></div>
					</div>
				</div>
				<div className="row">
					<div className="col-xs-2 col-xs-offset-2">
						<div className="list-group">

							{/* 原生html中，靠<a>跳转不同的页面 */}
							{/* <a className="list-group-item" href="./about.html">About</a>
							<a className="list-group-item active" href="./home.html">Home</a> */}

							{/* 在React中靠路由链接实现切换组件--编写路由链接 */}
							<Link className="list-group-item" to="/about">About</Link>
							<Link className="list-group-item" to="/home">Home</Link>
						</div>
					</div>
					<div className="col-xs-6">
						<div className="panel">
							<div className="panel-body">
								{/* 注册路由 */}
								<Route path="/about" component={About}/>
								<Route path="/home" component={Home}/>
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}

```

## 四、路由组件与一般组件

1. 写法不同：
   一般组件：`<Demo/>`
   路由组件：`<Route path="/demo" component={Demo}/>`
2. 存放位置不同：
   一般组件：components
   路由组件：pages/views
3. 接收到的 props 不同：
   一般组件：写组件标签时传递了什么，就能收到什么
   路由组件：接收到三个固定的属性

```jsx
history:
   go: ƒ go(n)
   goBack: ƒ goBack()
   goForward: ƒ goForward()
   push: ƒ push(path, state)
   replace: ƒ replace(path, state)

location:
   pathname: "/about"
   search: ""
   state: undefined

match:
   params: {}
   path: "/about"
   url: "/about"
```

## 五、NavLink 与封装 NavLink

1. NavLink 可以实现路由链接的高亮，通过 activeClassName 指定样式名
2. 标签体内容是一个特殊的标签属性
3. 通过 this.props.children 可以获取标签体内容
   `<MyNavLink className="list-group-item" to="/home">Home</MyNavLink>`
   即 Home 可以通过 children 内置的已有的属性进行自动传递，可以不通过属性传递。

```jsx
export default class App extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-xs-offset-2 col-xs-8">
            <Header />
          </div>
        </div>
        <div className="row">
          <div className="col-xs-2 col-xs-offset-2">
            <div className="list-group">
              {/* 原生html中，靠<a>跳转不同的页面 */}
              {/* <a className="list-group-item" href="./about.html">About</a>
							<a className="list-group-item active" href="./home.html">Home</a> */}

              {/* 在React中靠路由链接实现切换组件--编写路由链接 */}
              <NavLink
                activeClassName="atguigu"
                className="list-group-item"
                to="/about"
              >
                About
              </NavLink>
              <NavLink
                activeClassName="atguigu"
                className="list-group-item"
                to="/home"
              >
                Home
              </NavLink>
            </div>
          </div>
          <div className="col-xs-6">
            <div className="panel">
              <div className="panel-body">
                {/* 注册路由 */}
                <Route path="/about" component={About} />
                <Route path="/home" component={Home} />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

```

```jsx
//nav-link的封装，用于统一样式，方便使用

import React from "react";
import { NavLink } from "react-router-dom";

//用组件包装nav-link，nav-link的二次封装

export default function MyNavLink(props) {
  // 将外部传入的所有属性传递给navlink，不用在定义prop-types
  return <NavLink {...props} activeClassName="activeClass" />;
}

```

## 六、Switch 的使用

1. 通常情况下，path 和 component 是一一对应的关系。
2. Switch 可以提高路由匹配效率(单一匹配)。
3. 作用：让路径之匹配上一个组件之后就不再进行匹配了。即/home 路由匹配上 Home 组件之后，就不再匹配 Test 组件了。如果不写 Switch 则会两个组件都显示

```jsx
{/*可切换的路由组件*/}
{/* 用switch组件将路由组件进行控制，所以才需要将内容放进switch中
只能显示其中一个，需要用switch包装起来进行调用转换 */}

//作用：让路径之匹配上一个组件之后就不再进行匹配了。即/home路由匹配上Home组件之后，就不再匹配Test组件了。如果不写Switch则会两个组件都显示

<Switch>
   <Route path="/about" component={About} />
   <Route path="/home" component={Home} />
   <Route path="/home" component={Test} />
</Switch>

```

## 七、解决多级路径刷新页面样式丢失的问题

1. public/index.html 中 引入样式时不写 ./ 写 / （常用）
2. public/index.html 中 引入样式时不写 ./ 写 %PUBLIC_URL% （常用）
3. 使用 HashRouter 较少用
   public 里面的 index.html 文件 css 样式路径修改
   `<link rel="stylesheet" href="%PUBLIC_URL%/css/bootstrap.css" />`
   以下刷新后会找不到，路由为多级路由时候刷新页面，样式会丢失。
   `<link rel="stylesheet" href="./css/bootstrap.css" />`

## 八、路由的严格匹配与模糊匹配

1. 默认使用的是模糊匹配（简单记：【输入的路径】必须包含要【匹配的路径】，且顺序要一致）

- 即 `<MyNavLink to="/home/a/b">Home</MyNavLink>` `<Route path="/home" component={Home}/>`即使 route 路径中写的/home,则还是会进行路由跳转
- `<Route path="/a/home" component={Home}/>` 顺序不一致，则也不会跳转

2. 开启严格匹配：`<Route exact={true} path="/about" component={About}/>`,那么上面的例子，路由就不能跳转
3. 严格匹配不要随便开启，需要再开，有些时候开启会导致无法继续匹配二级路由

```jsx
export default class App extends Component {
	render() {
		return (
			<div>
				<div className="row">
					<div className="col-xs-offset-2 col-xs-8">
						<Header/>
					</div>
				</div>
				<div className="row">
					<div className="col-xs-2 col-xs-offset-2">
						<div className="list-group">
							<MyNavLink to="/about">About</MyNavLink>
							<MyNavLink to="/home/a/b">Home</MyNavLink>
						</div>
					</div>
					<div className="col-xs-6">
						<div className="panel">
							<div className="panel-body">
								{/* 注册路由 */}
								<Switch>
									<Route exact path="/about" component={About}/>
									<Route exact path="/home" component={Home}/>
								</Switch>
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}
```

## 九、Redirect 的使用

1. 一般写在所有路由注册的最下方，当所有路由都无法匹配时，跳转到 Redirect 指定的路由
2. 具体写法

```jsx
<Switch>
   <Route path="/about" component={About}/>
   <Route path="/home" component={Home}/>
   <Redirect to="/about"/>
</Switch>
```

## 十、嵌套路由

1. 注册子路由时要写上父路由的 path 值； /home/news
2. 路由的匹配是按照注册路由的顺序进行的

- app.jsx 里的路由是先匹配的，所以回先匹配/home 路由。之后再在/home 路由里匹配/home/news 的路由

## 十一、向路由组件传递参数

1. params 参数

- 路由链接(携带参数)：`<Link to='/demo/test/tom/18'}>详情</Link>`
- 注册路由(声明接收)：`<Route path="/demo/test/:name/:age" component={Test}/>`
- 接收参数：this.props.match.params

2. search 参数（ajax 中的 query 参数传递）

- 路由链接(携带参数)：`<Link to='/demo/test?name=tom&age=18'}>详情</Link>`
- 注册路由(无需声明，正常注册即可)：`<Route path="/demo/test" component={Test}/>`
- 接收参数：this.props.location.search
- 备注：获取到的 search 是 urlencoded 编码字符串，需要借助 querystring 解析
- 所有需要引入 `import qs from "querystring";`
- `const {name,age} = qs.parse(search.slice(1))`

3. state 参数

- 路由链接(携带参数)：`<Link to={{pathname:'/demo/test',state:{name:'tom',age:18}}}>详情</Link>`
- 注册路由(无需声明，正常注册即可)：`<Route path="/demo/test" component={Test}/>`
- 接收参数：this.props.location.state
- 备注：刷新也可以保留住参数；路由组件身上独有的一个参数，不会将参数显示在地址栏中，会把数据进行隐藏

## 十二、编程式路由导航

1. 借助 this.prosp.history 对象上的 API 对操作路由跳转、前进、后退

- this.prosp.history.push()
- this.prosp.history.replace()
- this.prosp.history.goBack()
- this.prosp.history.goForward()
- this.prosp.history.go()

## 十三、withRouter

1. 将组件形成高阶组件

```jsx
import React, { Component } from 'react'

import {withRouter} from 'react-router-dom'

class Header extends Component {

    back = ()=>{
    	this.props.history.goBack()
    }

    forward = ()=>{
    	this.props.history.goForward()
    }

    go = ()=>{
    	this.props.history.go(-2)
    }

    render() {
    	console.log('Header组件收到的props是',this.props);
    	return (
    		<div className="page-header">
    			<h2>React Router Demo</h2>
    			<button onClick={this.back}>回退</button>&nbsp;
    			<button onClick={this.forward}>前进</button>&nbsp;
    			<button onClick={this.go}>go</button>
    		</div>
    	)
    }

}

export default withRouter(Header)

//withRouter 可以加工一般组件，让一般组件具备路由组件所特有的 API
//withRouter 的返回值是一个新组件
```

## 十四、BrowserRouter 与 HashRouter 的区别

1. 底层原理不一样：

- BrowserRouter 使用的是 H5 的 history API，不兼容 IE9 及以下版本。
- HashRouter 使用的是 URL 的哈希值。
- react 中的 history 的方法都是对原生的方法的二次封装

2. path 表现形式不一样

- BrowserRouter 的路径中没有#,例如：localhost:3000/demo/test
- HashRouter 的路径包含#,例如：localhost:3000/#/demo/test

3. 刷新后对路由 state 参数的影响

- (1).BrowserRouter 没有任何影响，因为 state 保存在 history 对象中。
- (2).HashRouter 刷新后会导致路由 state 参数的丢失！！！，因为没有 history 这个对象存储 state 数据

4. 备注：HashRouter 可以用于解决一些路径错误相关的问题。

## 十五、antd 的按需引入+自定主题

1. 安装依赖：yarn add react-app-rewired customize-cra babel-plugin-import less less-loader
2. 修改 package.json

```json
"scripts": {
"start": "react-app-rewired start",
"build": "react-app-rewired build",
"test": "react-app-rewired test",
"eject": "react-scripts eject"
},
```

3. 根目录下创建 config-overrides.js

```js
//配置具体的修改规则
const { override, fixBabelImports, addLessLoader } = require("customize-cra");
module.exports = override(
  fixBabelImports("import", {
    libraryName: "antd",
    libraryDirectory: "es",
    style: true,
  }),
  addLessLoader({
    lessOptions: {
      javascriptEnabled: true,
      modifyVars: { "@primary-color": "green" },
    },
  })
);
```

4. 备注：不用在组件里亲自引入样式了，即：import 'antd/dist/antd.css'应该删掉

# Hooks

## 1. setState

### setState更新状态的2种写法


(1). setState(stateChange, [callback])------**对象式的setState**
1. stateChange为状态改变对象(该对象可以体现出状态的更改)
2. callback是可选的回调函数, 它在状态更新完毕、界面也更新后(render调用后)才被调用
```js
this.setState({count:count+1},()=>{
			console.log(this.state.count);
})
```

(2). setState(updater, [callback])------**函数式的setState**
1. updater为返回stateChange对象的函数。
2. updater可以接收到state和props。
3. callback是可选的回调函数, 它在状态更新、界面也更新后(render调用后)才被调用。
1. **对象式的setState是函数式的setState的简写方式(语法糖)**
2. 使用原则：
- (1).如果新状态不依赖于原状态 ===> 使用对象方式
- (2).如果新状态依赖于原状态 ===> 使用函数方式
- (3).如果需要在setState()执行后获取最新的状态数据, 要在第二个callback函数中读取

```js
this.setState( state => ({count:state.count+1}))

//两次回调，第二次的方法是一个callback
this.setState( state => ({count:state.count+1}),()=>console.log(this.state.count))
```


```jsx
import React, { Component } from 'react'

export default class Demo extends Component {

	state = {count:0}

	add = ()=>{
		//对象式的setState
		/* //1.获取原来的count值
		const {count} = this.state
		//2.更新状态
		this.setState({count:count+1},()=>{
			console.log(this.state.count);
		})
		//console.log('12行的输出',this.state.count); //0 */

		//函数式的setState
		this.setState( state => ({count:state.count+1}),()=>console.log(this.state.count))
	}

	render() {
		return (
			<div>
				<h1>当前求和为：{this.state.count}</h1>
				<button onClick={this.add}>点我+1</button>
			</div>
		)
	}
}

```

useState() results

1. State object(getter)
2. Updater function(setter)

```jsx
function logButton(){
console.log(Math.random());
}

function Button() {
  const [counter,setCounter] = useState(0);
  //解构
	return <button onClick={logButton}>{counter}</button>;
}
ReactDOM.render(
  <Button />, 
  document.getElementById('mountNode'),
);
```

```jsx
function logButton(){
console.log(Math.random());
}

function Button() {
  const [counter,setCounter] = useState(0);
  //解构
	return <button onClick={()=>setCounter(counter+1)}>{counter}</button>;
}
ReactDOM.render(
  <Button />, 
  document.getElementById('mountNode'),
);
```

```jsx
function Button() {
  const [counter,setCounter] = useState(0);
  //避免在函数function中嵌套函数，尽量用变量进行传递
  const handleClick =()=>setCounter(counter+1);
  //解构
	return (
    <button onClick={handleClick}>
    </button>;
  )
}
           
function Display(){
  return(
  <div>
    ......
   </div>
  )
}
//1. 用数组的方法进行重绘,处理多个组件渲染
ReactDOM.render(
  [<Button />, <Display />]
  document.getElementById('mountNode'),
);

//2.使其成为子组件
ReactDOM.render(
  <div>
    <Button /> 
    <Display />
  </div>
  document.getElementById('mountNode'),
);

//3.not new dom parents will be used,just the same thing
ReactDOM.render(
  <React.Fragment>
    <Button /> 
    <Display />
  </React.Fragment>
  document.getElementById('mountNode'),
);

//4.放在一个新的组件里
function App(){
  return(
   <div>
    <Button /> 
    <Display />
  </div>
  )
}


ReactDOM.render(
  <App/>
  document.getElementById('mountNode'),
);
```

```jsx
//父子组件传值

function Button(props) {
	//const [counter, setCounter] = useState(0);
	return (
    <button onClick={props.onClickFcuntion}>
      +1
    </button>
  );
}

function Display(props){
  return(
  <div>
    {props.message}
  </div>
  )
}

function App(){
	const [counter, setCounter] = useState(0);
  const incrementCounter=()=>setCounter(counter+1);
  return(
  <div>
    <Button onClickFcuntion={incrementCounter}/>
    <Display message={counter}/>
  </div>
    
    )
}

ReactDOM.render(
  <App />, 
  document.getElementById('mountNode'),
);
```

### state and setstate

#### state

保存状态

```jsx
class LikeButton extends Component {
  constructor () {
    super()
    this.state = { isLiked: false }
  }

  handleClickOnLikeButton () {
    this.setState({
      isLiked: !this.state.isLiked
    })
  }

  render () {
    return (
      <button onClick={this.handleClickOnLikeButton.bind(this)}>
        {this.state.isLiked ? '取消' : '点赞'} 👍
      </button>
    )
  }
}
```

```jsx
class Index extends Component {
  render () {
    return (
      <div>
        <LikeButton />
      </div>
    )
  }
}

ReactDOM.render(
  <Index />,
  document.getElementById('root')
)
```

### setState()

 `setState` 方法由父类 `Component` 所提供。**当我们调用这个函数的时候，React.js 会更新组件的状态 `state` ，并且重新调用 `render` 方法，然后再把 `render` 方法所渲染的最新的内容显示到页面上**。 

#### 接收对象参数

```JSX
constructor (props) {
    super(props)
    this.state = {
      name: 'Tomy',
      isLiked: false
    }
  }

  handleClickOnLikeButton () {
    this.setState({
        //只需要传入，需要更新状态的部分即可，即我们需要更新的部分只是isliked的状态
      isLiked: !this.state.isLiked
    })
  }
```

#### 接收函数参数

**React.js 并不会马上修改 state**，是会把更新的状态合并到 `state` 当中，然后再触发组件更新。所以不会取得上一个状态下的值，用于运算处理。用函数作为参数可以进行参数的传输和运算处理。

这道例题我没懂，prevState.count是怎么获得值的？

```jsx
handleClickOnLikeButton () {
    this.setState((prevState) => {
      return { count: 0 }
    })
    this.setState((prevState) => {
      return { count: prevState.count + 1 } 
      // 上一个 setState 的返回是 count 为 0，当前返回 1
    })
    this.setState((prevState) => {
      return { count: prevState.count + 2 } 
      // 上一个 setState 的返回是 count 为 1，当前返回 3
    })
    // 最后的结果是 this.state.count 为 3
  }
```

### 

------



## 2. lazyLoad

### 路由组件的lazyLoad

作用：用的时候加载，不用的时候不加载。

1. 将所有懒加载的路由组件用`<Suspense>`包裹，并给一个fallback，返回一个组件，因为懒加载时需要一个不是懒加载的组件，在懒加载组件之前去渲染未懒加载的组件。

```jsx
	//1.通过React的lazy函数配合import()函数动态加载路由组件 ===> 路由组件代码会被分开打包
	const Login = lazy(()=>import('@/pages/Login'))
	
	//2.通过<Suspense>指定在加载得到路由打包文件前显示一个自定义loading界面
	<Suspense fallback={<h1>loading.....</h1>}>
        <Switch>
            <Route path="/xxx" component={Xxxx}/>
            <Redirect to="/login"/>
        </Switch>
    </Suspense>
```

## 3. Hooks

#### 1. React Hook/Hooks是什么?

- (1). Hook是React 16.8.0版本增加的新特性/新语法
- (2). 可以让你在函数组件中使用 state 以及其他的 React 特性

#### 2. 三个常用的Hook

- (1). State Hook: React.useState()
- (2). Effect Hook: React.useEffect()
- (3). Ref Hook: React.useRef()

#### 3. State Hook

`import React, { useState, useRef } from "react";`

- (1). State Hook让函数组件也可以有state状态, 并进行状态数据的读写操作

- (2). 语法: const [xxx, setXxx] = useState(initValue)  

- (3). useState()说明:

  - 参数: 第一次初始化指定的值在内部作缓存

  - 返回值: 包含2个元素的数组, 第1个为内部当前状态值, 第2个为更新状态值的函数

- (4). setXxx() 2种写法:
  - setXxx(newValue): 参数为非函数值, 直接指定新的状态值, 内部用其覆盖原来的状态值
  - setXxx(value => newValue): 参数为函数, 接收原本的状态值, 返回新的状态值, 内部用其覆盖原来的状态值

#### 4. Effect Hook

1. Effect Hook 可以让你在函数组件中执行副作用操作(用于模拟类组件中的生命周期钩子)

2. React中的副作用操作:

   - 发ajax请求数据获取
   - 设置订阅 / 启动定时器
   - 手动更改真实DOM

3. 语法和说明: 

```jsx
      useEffect(() => { 
             // 在此可以执行任何带副作用操作，这一段相当于 挂载 和 更新 两个生命周期
             return () => { // 在组件卸载前执行
               // 在此做一些收尾工作, 比如清除定时器/取消订阅等
       }
   }, [stateValue]) // 如果指定的是[],一个空数组, 回调函数只会在第一次render()后执行  
   // [stateValue]如果不写，则默认监听所有状态，如果写的话只表明监听写入的那个状态
```

```jsx
//1. 第二个参数为空数组，表明不检测任何数据。只表明调用componentDidMount()，当需要任务在挂载的时候执行，不需要其他生命周期的时候执行时可用这个方法，比如请求数据的时候。如果需要监听别的数据更新时有别的功能，那么就写多个useEffect实现不同状态时候的功能
useEffect(()=>{
	console.log("挂载时和更新时候调用");
  return function(){
    console.log("组件销毁时调用")
  }
},[])

//如果第二个参数写入空数组,[],则回调函数只会在第一次render后执行，即只会输出"挂载时和更新时候调用",不会输出"组件销毁时调用",console.log("组件销毁时调用")只会在销毁的时候执行！！！！！！！！

//注意这里有使用到销毁的时候可以执行的方法，用上面的例子可以使东西在销毁的时候才执行。记得加空数组。

//传入第二个参数为[]，空数组的时候只表明调用componentDidMount()

//2. 第二个参数不传入，表明检测所有数据componentDidMount()，componentDidUpdate()这个两个函数。
useEffect(()=>{
	console.log("挂载时和更新时候调用");
})

//不传入第二个参数即[]的时候，相当于react自动监听所有的数据。如果传入一个空数组，则表明谁也不检测。
//不传入第二个参数的时候调用componentDidMount()，componentDidUpdate()这个两个函数。


//3. 第二个参数传入数组，并写入数据，表明检测写入的数据的更新
const [count,setCount] = React.useState(0);
React.useEffect(()=>{
  console.log("@")
	},[count])

//传入的第二个参数数组中，写入需要监听的对象时，表明调用componentDidMount()，componentDidUpdate()这个两个函数。并在count数据更新是，调用回调函数。


//
	React.useEffect(()=>{
    //组件挂载时，和数据更新时
		let timer = setInterval(()=>{
			setCount(count => count+1 )
		},1000)
		return ()=>{
      //组件卸载时，做数据收尾工作，清除定时器等
			clearInterval(timer)
		}
	},[])//写入空数组
```

4. 可以把 useEffect Hook 看做如下三个函数的组合
- 1. componentDidMount()
- 2. componentDidUpdate()
- 3. componentWillUnmount() 


#### 5. Ref Hook

1. Ref Hook可以在函数组件中存储/查找组件内的标签或任意其它数据
2. 语法: const refContainer = useRef()
3. 作用:保存标签对象,功能与React.createRef()一样

## 4. Fragment

### 使用

```jsx
<Fragment><Fragment>
<></>
```

### 作用

> 可以不用必须有一个真实的DOM根标签了,用于规避jsx语法必须输入跟标签的作用。

<hr/>

## 5. Context

useContent hooks

### 理解

> 一种组件间通信方式, 常用于【祖组件】与【后代组件】间通信

### 使用

1. 创建Context容器对象：
   `const XxxContext = React.createContext() `
   XxxContext中有有两个标签：Provider & Consumer,可以通过结构赋值获取 

   `const {Provider,Consumer} = XxxContext`
   
2. 渲染子组时，外面包裹xxxContext.Provider, 通过value属性给后代组件传递数据：

   ```jsx
   <xxxContext.Provider value={数据}>
   		子组件
   </xxxContext.Provider>
   
   //如果通过结构赋值获取 provider 和 consumer就可以不用上面的写法
   const {Provider,Consumer} = XxxContext;
   //最大的组件里写上Provider，它里面包裹的都是它的子组件
   <Provider value={数据}>
   		子组件
   </Provider>
   
   //------------------------------------------------------------------
   
   //创建Context对象
   const MyContext = React.createContext()
   const {Provider,Consumer} = MyContext
   export default class A extends Component {
   
   	state = {username:'tom',age:18}
   
   	render() {
   		const {username,age} = this.state
   		return (
   			<div className="parent">
   				<h3>我是A组件</h3>
   				<h4>我的用户名是:{username}</h4>
   				<Provider value={{username,age}}>
   					<B/>
   				</Provider>
   			</div>
   		)
   	}
   }
   
   ```

3. 后代组件读取数据：

```jsx
//第一种方式:仅适用于类组件 
  static contextType = xxxContext  // 声明接收context
  this.context // 读取context中的value数据
  
//第二种方式: 函数组件与类组件都可以
  <xxxContext.Consumer>
    {
      value => ( // value就是context中的value数据
   							 //可以返回模版字符串，也可以返回标签
    							//{value => `${value.username},年龄是${value.age}`}
        要显示的内容
      )
    }
  </xxxContext.Consumer>
    
//如果开头解构之后可以这么写
//const {Provider,Consumer} = MyContext
<Consumer>
    {
      value => ( // value就是context中的value数据
   							 //可以返回模版字符串，也可以返回标签
    						 //{value => `${value.username},年龄是${value.age}`}
        要显示的内容
      )
    }
</Consumer>
```
```jsx
//类式组件需要声明接收context
class C extends Component {
	//声明接收context
	static contextType = MyContext
	render() {
		const {username,age} = this.context
		return (
			<div className="grand">
				<h3>我是C组件</h3>
				<h4>我从A组件接收到的用户名:{username},年龄是{age}</h4>
			</div>
		)
	}
} 

//函数组件不需要声明，只需要通过Consumer组件容器接收参数即可
function C(){
	return (
		<div className="grand">
			<h3>我是C组件</h3>
			<h4>我从A组件接收到的用户名:
			<Consumer>
				{value => `${value.username},年龄是${value.age}`}
			</Consumer>
			</h4>
		</div>
	)
}
```

3. 函数组件使用useContext

```jsx
import {createContext,useState,useContext} from 'react'
const ContextAPI=createContext();
let Demo2=()=>{
    const context=useContext(ContextAPI)
    return(
        <div>
            我是demo2-{context.state.a}
            <button onClick={
                ()=>{
                    context.setA(5)   
                }
            }>改变</button>
        </div>
    )
}
let Demo1=()=>{
    const context=useContext(ContextAPI)
    return(
        <div>
            我是demo1-{context.state.b}---{context.state.a}
            <Demo2/>
        </div>
    )
}
function Context() {
    const [a,setA]=useState(1);
    const b=2;

    return(
        <ContextAPI.Provider value={{state:{a,b},setA}}>
            <div>
                <h1>函数式组件</h1>
                <Demo1></Demo1>
            </div>
        </ContextAPI.Provider>
    )
}
export default Context;
```



### 注意

	在应用开发中一般不用context, 一般都用它的封装react插件

### 封装

跨页面跨组件使用，上面的方法只适用于一个文件内的不同组件数据传递。我们需要把contextProvider进行封装，使得别的组件都可以使用。需要传的store状体的管理

```jsx
//store.js
//创建store文件夹，写入一个store.js 文件

import React, { Component, createContext } from "react";

//创建上下文文本库，用于控制store
const Context = createContext();

export default class ProviderComponent extends Component {
  constructor() {
    super();
    this.state = {
      a: 1,
      b: 2,
    };
  }

  changeA = (a) => {
    this.setState({ a });
  };

  changeB = (b) => {
    this.setState({ b });
  };

  render() {
    return (
      <Context.Provider
        value={{
          state: this.state,
          changeA: this.changeA,
          changeB: this.changeB,
        }}
      >
        {this.props.children}
      </Context.Provider>
    );
  }
}

export { ProviderComponent, Context };

```

```jsx
//app.js
import React from "react";
import { ProviderComponent } from "../../store";
import Login from "../login/Login";

export default function App() {
  return (
    <ProviderComponent>
      <Login />
    </ProviderComponent>
  );
}

```

```jsx
//login.jsx
import React, { useContext } from "react";
import { Context } from "../../store";

export default function Login() {
  const context = useContext(Context);
  return (
    <div>
      login page
      <span>data from providecomponent:{context.state.a}</span>
      <button
        onClick={() => {
          context.changeA(10);
        }}
      ></button>
    </div>
  );
}

```



<hr/>


## 6. 组件优化

### Component的2个问题 

> 1. 只要执行setState(),即使不改变状态数据, 组件也会重新render() ==> 效率低
>
> 2. 只当前组件重新render(), 就会自动重新render子组件，纵使子组件没有用到父组件的任何数据 ==> 效率低

### 效率高的做法

>  只有当组件的state或props数据发生改变时才重新render()

### 原因

>  Component中的shouldComponentUpdate()总是返回true

### 解决

1. 办法1: 
   - 重写shouldComponentUpdate()方法
   - 比较新旧state或props数据, 如果有变化才返回true, 如果没有返回false
2. 办法2: 
   - 使用PureComponent
     PureComponent重写了shouldComponentUpdate(), 只有state或props数据有变化才返回true
   - 注意: 
     只是进行state和props数据的浅比较, 如果只是数据对象内部数据变了, 返回false
     不要直接修改state数据, 而是要产生新数据
     项目中一般使用PureComponent来优化



<hr/>


## 7. render props

### 如何向组件内部动态传入带内容的结构(标签)?

1. Vue中: 
   - 使用slot技术, 也就是通过组件标签体传入结构  <A><B/></A>
2. React中:
   - 使用children props: 通过组件标签体传入结构
   - 使用render props: 通过组件标签属性传入结构,而且可以携带数据，一般用render函数属性

### children props

```jsx
let A = () => {
  return (
    <div>
      这是A组件
      {/*写入 {this.props.children}才能获取hello内容，因为hello属于标签属性，会通过children进行传递*/}
      {this.props.children}
    </div>
  );
};

//父组件 App

export default function test() {
  return (
    <div>
      <A>hello</A>
    </div>
  );
}

//问题: 如果B组件需要A组件内的数据, ==> 做不到 
```

### render props

```jsx
<A render={(data) => <C data={data}></C>}></A>
//A组件: {this.props.render(内部state数据)}
//C组件: 读取A组件传入的数据显示 {this.props.data} 
```

```jsx
import React, { Component } from 'react'
import './index.css'
import C from '../1_setState'

export default class Parent extends Component {
	render() {
		return (
			<div className="parent">
				<h3>我是Parent组件</h3>
       {/*在组件A中写入一个回调函数，返回一个组件，并给组件传值，类似一个插槽的形式，形成父子关系组件*/}
				<A render={(name)=><B name={name}/>}/>
			</div>
		)
	}
}

class A extends Component {
	state = {name:'tom'}
	render() {
		console.log(this.props);
		const {name} = this.state
		return (
			<div className="a">
				<h3>我是A组件</h3>
        {/*通过获取render函数，并给子组件传值*/}
				{this.props.render(name)}
			</div>
		)
	}
}

class B extends Component {
	render() {
		console.log('B--render');
		return (
			<div className="b">
				<h3>我是B组件,{this.props.name}</h3>
			</div>
		)
	}
}

```



<hr/>

## 8. 错误边界

#### 理解：

错误边界(Error boundary)：用来捕获后代组件错误，渲染出备用页面，目的是不让子组件的错误影响父组件的呈现。

只会在生产环境中起作用，开发环境只能出现一下，并随后消失。

错误边界始终去找出错误的父组件去处理的。

#### 特点：

只能捕获**后代组件 ** **生命周期**产生的错误，不能捕获自己组件产生的错误和其他组件在合成事件、定时器中产生的错误

##### 使用方式：

getDerivedStateFromError配合componentDidCatch

```js
// 生命周期函数，一旦后台组件报错，就会触发
static getDerivedStateFromError(error) {
    console.log(error);
    // 在render之前触发
    // 返回新的state
    return {
        hasError: true,
    };
}

componentDidCatch(error, info) {
    // 一般统计页面的错误次数。发送请求发送到后台去，反馈给后台服务器，进行bug解决
    console.log(error, info);
}
```
## 9. 组件通信方式总结

#### 组件间的关系：

- 父子组件
- 兄弟组件（非嵌套组件）
- 祖孙组件（跨级组件）

#### 几种通信方式：

		1.props：
			(1).children props
			(2).render props
		2.消息订阅-发布：
			pubs-sub、event等等
		3.集中式管理：
			redux、dva等等
		4.conText:
			生产者-消费者模式

#### 比较好的搭配方式：
		父子组件：props
		兄弟组件：消息订阅-发布、集中式管理
		祖孙组件(跨级组件)：消息订阅-发布、集中式管理、conText(开发用的少，封装插件用的多)

## 10. 路由

根据hash值进行组件切换

1. hash      #xxx               onhashchange  当hash发生改变的时候
2. history   /xxx/xxx           onpopstate    当浏览器记录发生改变的时候

```
import {useEffect,useState} from 'react';

let Home=()=><div>首页</div>;
let List=()=><div>列表</div>;
let My=()=><div>我的</div>;

function MyRouter() {
    let RouterView;
    let [hashState,setHashState]=useState('#/home');
    
    useEffect(()=>{
        window.addEventListener('hashchange',()=>{
            console.log(window.location.hash)
            setHashState(window.location.hash);

        },false)
    },[])

    switch(hashState){
        case '#/home':
            RouterView=<Home/>;
            break;
        case '#/list':
            RouterView=<List/>;
            break;
        case '#/my':
            RouterView=<My/>;
            break;
    }
    return (
        <div>
            <h1>我的路由</h1>
            <ul>
                <li><a href="#/home">首页</a></li>
                <li><a href="#/list">列表</a></li>
                <li><a href="#/my">我的</a></li>
            </ul>
            {RouterView}
        </div>
    )
}

export default MyRouter
```



#### useParams

获取路由参数

动态路由

```jsx
import {HashRouter,Link,Route,Switch,useParams} from 'react-router-dom'
import './router.css'
let Router=()=>{
    let {id,order}=useParams();
    console.log(id,order);
    return(
        <div>
            我是要展示的内容---{id}---{order}
        </div>
    )
};

function ReactRouter() {
    return(
        <div>
            <HashRouter>
                <h1>reactRouter</h1>
                <ul>
                    <li><Link to="/home/1">home</Link></li>
                    <li><Link to="/list/2">list</Link></li>
                    <li><Link to="/my/3">my</Link></li>
                </ul>
                <Switch>
                    <Route exact path="/:id/:order"><Router/></Route>
                </Switch>
            </HashRouter>
        </div>
    )
}

export default ReactRouter;
```

#### useRouteMatch

嵌套路由,匹配路径

```jsx
import {HashRouter,Link,Route,Switch,useParams,useRouteMatch,Redirect } from 'react-router-dom'
import './router.css'
let Order=()=><div>我的订单</div>;
let History=()=><div>我的足迹</div>;
let Collect=()=><div>我的收藏</div>;

let Home=()=><div>首页</div>;
let List=()=><div>列表</div>;

let My=()=>{
    let {path,url}=useRouteMatch();
    console.log(path,url)
    return(
        <div>
            <h1>我的页面</h1>
            <ol>
                <li><Link to={`${url}/order`}>我的订单</Link></li>
                <li><Link to="/my/history">我的足迹</Link></li>
                <li><Link to="/my/collect">我的收藏</Link></li>
            </ol>
            <Switch>
                <Route path={`${path}/order`}><Order/></Route>
                <Route path='/my/history'><History/></Route>
                <Route path="/my/collect"><Collect/></Route>
            </Switch>
        </div>
    )
};


function ReactRouter() {
    return(
        <div>
            <HashRouter>
                <h1>reactRouter</h1>
                <ul>
                    <li><Link to="/home">home</Link></li>
                    <li><Link to="/list">list</Link></li>
                    <li><Link to="/my">my</Link></li>
                    
                </ul>
                <Switch>
                    <Route path="/home"><Home/></Route>
                    <Route path="/list"><List/></Route>
                    <Route path="/my"><My/></Route>
                    
                </Switch>
            </HashRouter>
        </div>
    )
}

export default ReactRouter;
```

#### useHistory

```jsx
import React from "react";
import { useHistory } from "react-router-dom";

export default function About(props) {
  let history = useHistory();
  console.log("这是about组件收到的props", props);
  let goHome = () => {
    history.push("/home");
  };
  return (
    <div>
      About组件内容 &nbsp;
      <button onClick={goHome}>回Home主页</button>
    </div>
  );
}
```

#### useLocation

```jsx
import { HashRouter, Link, Route, Switch, useParams, useRouteMatch, BrowserRouter, NavLink ,Redirect,useHistory,useLocation} from 'react-router-dom'

let Home = () => {
    let history=useHistory();
    let location=useLocation();
    console.log(url2json(location.search).a);
    let goList=()=>{
        history.push({pathname:'/list'});
    }
    let goMy=()=>{
        history.goBack();
    }
    

    return (
        <div>
            <h1>首页</h1>
            <button onClick={goList}>去列表页</button>
            <button onClick={goMy}>返回</button>
        </div>
    )
};

function ReactRouter() {
    return (
        <div>
            <BrowserRouter>
                <h1>reactRouter</h1>
                <ul>
                    <li><Link to="/home?a=1">home</Link></li>
                    <li><Link to={{pathname:"/list",search:'?b=2'}}>list</Link></li>
                    <li><Link to="/my">my</Link></li>

                </ul>
                <Switch>
                    <Route path="/home"><Home /></Route>
                    <Route path="/list"><List /></Route>
                    <Route path="/my"><My /></Route>
                    <Route path="*"><Error /></Route>

                </Switch>
            </BrowserRouter>
        </div>
    )
}

export default ReactRouter;
```

## 11. Mobx

状态管理，有其他的状态管理，如redux

和原生的react内容中的context的区别在于，多了一些计算属性的动能

Links: https://mobx.js.org/observable-state.html

```
npm i mobx
npm i mobx-react
(maybe)
```

```js
import { makeAutoObservable } from "mobx"//管理数据state
import { observer } from "mobx-react"//促使页面更新,动态的改变页面的状态
```

```jsx
//for stroe index.js
//class 类的用法
import { makeObservable, observable, computed, action, flow } from "mobx"

class Doubler {
    value

    constructor(value) {
        makeObservable(this, {
            value: observable,
            double: computed,
            increment: action,
            fetch: flow
        })
      //传入this，用于改变this的指向
        this.value = value
    }
  
  	a = 1;
		b = 2;

    addA(){
      this.a++
    }

     changeB(b){
       this.b=b
     }
	// computed 计算属性，需要在前面加一个get属性
		get sum(){
      return this.a + this.b
    }
    get double() {
        return this.value * 2
    }

    increment() {
        this.value++
    }
  

    *fetch() {
      //用于异步
        const response = yield fetch("/api/value")
        this.value = response.json()
    }
}

const store = new Doubler();
export default store;
//数据导出给app用
```

```jsx
//app index.jsx
import React from "react";
import store from "../../store";
import Login from "../login/Login";

const Context = createContext();//? 这里会报错
//const Context = React.createContext();//这个不会，但是笔记上写的是上面那个。。。





function App() {
  return (
    <Context.Provider value={store}>
      <Login />
    </Context.Provider>
  );
}

export default App;
export { Context };


```

```jsx
//login.jsx
import React, { useContext } from "react";
import { Context } from "../app/App";
import { Observer } from "mobx-react"
//如果数据需要动态渲染，那么需要动态渲染的数据就需要用Observer包裹起来


export default function Login() {
  const context = useContext(Context);
  console.log(context)
  return (
    <Observer>
    {()=>(
    <div>
      login page
      <span>data from store:{context.a}</span>      
      <span>data from store:{context.b}</span>      
      <span>data from store:{context.sum}</span>

      <button
        onClick={() => {
          context.addA(10);
        }}
      ></button>
    </div>
    )}
    </Observer>
  );
}
```

















































































## github demo

### react_pracs



![comment_component.gif](http://ww1.sinaimg.cn/large/005NUwyggy1gbr6jj0plcg30r70gagr9.gif)



### react_app



1. 写了一些 demo,留言板，github 用户搜素请求，todolist，留言板和 github 用户请求分 pubsub 写法和非 pubsub 写法。

2. 发现不足的地方是 app 组件应该放在根目录下方。但是不影响整体运行。

3. pubsub github user 讲解 react ajax(fetch)的使用



### react_test



此文件内容主要是 react 基础知识点的 demo



1. 原生渲染

2. 组件

3. state

4. props

5. refs

6. composing

7. form

8. 生命周期

9. ajax



### react_redux



### react_router



### notes



1. 文件内所有的根组件 App 都放在了 component 文件夹中，实际操作中应该放在最外层的文件中，和 index.js 文件同层级。由于过多文件如此，就不一一修改了。

2. less 安装

   npm i less

   npm less-loader@6.0

3. antUI