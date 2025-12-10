# redux

1. react-redux模型图.png
   ![react-redux模型图.png](http://ww1.sinaimg.cn/large/005NUwyggy1gt4z7z08hhj60vf0hnwjn02.jpg)
2. react生命周期(旧)
   ![react生命周期(旧).png](http://ww1.sinaimg.cn/large/005NUwyggy1gt4z7ywsecj60nd0imq6k02.jpg)
3. react生命周期(新)
   ![react生命周期(新).png](http://ww1.sinaimg.cn/large/005NUwyggy1gt4z7yz5z4j60vh0lwgqt02.jpg)
4. redux原理图
   ![redux原理图.png](http://ww1.sinaimg.cn/large/005NUwyggy1gt4z7z98z3j60zk0k078s02.jpg)



## 1. 求和案例\_redux 精简版

1. 去除 Count 组件自身的状态
2. src 下建立:

```
- redux
    -store.js
    -count_reducer.js
```

3. .store.js：

   - 引入 redux 中的 createStore 函数，创建一个 store;因为我们通过 redux 存储状态，所以我们需要通过 redux 创建 store

   - createStore 调用时要传入一个为其服务的 reducer

   - 记得暴露 store 对象

4. count_reducer.js：

- reducer 的本质是一个函数，接收：preState,action，返回加工后的状态
- reducer 有两个作用：初始化状态，加工状态
- reducer 被第一次调用时，是 store 自动触发的，
  传递的 preState 是 undefined,
  传递的 action 是:{type:'@@REDUX/INIT_a.2.b.4}
- redux 只负责管理状态，不管理渲染，所以状态改变之后需要通过 store.subscribe(render);进行状态监听，实时状态更新渲染

5. 在 index.js 中监测 store 中状态的改变，一旦发生改变重新渲染<App/>
   备注：redux 只负责管理状态，至于状态的改变驱动着页面的展示，要靠我们自己写。

## 2. 求和案例\_redux 完整版

新增文件：

1. count_action.js 专门用于创建 action 对象
2. constant.js 放置容易写错的 type 值

## 3. 求和案例\_redux 异步 action 版

1. 明确：延迟的动作不想交给组件自身，想交给 action
2. 何时需要异步 action：想要对状态进行操作，但是具体的数据靠异步任务返回。
3. 具体编码：

- yarn add redux-thunk，并配置在 store 中
- 创建 action 的函数不再返回一般对象，而是一个函数，该函数中写异步任务。
- 异步任务有结果后，分发一个同步的 action 去真正操作数据。

4. 备注：异步 action 不是必须要写的，完全可以自己等待异步任务的结果了再去分发同步 action。

## 4. 求和案例\_react-redux 基本使用

1. 明确两个概念：

- 1).UI 组件:不能使用任何 redux 的 api，只负责页面的呈现、交互等。放在 components 文件夹里
- 2).容器组件：负责和 redux 通信，将结果交给 UI 组件。放在 containers 文件夹里

2. 如何创建一个容器组件————靠 react-redux 的 connect 函数。
   容器组件不能自己 rcc 创建，靠 react-redux 的 connect 函数。
   connect(mapStateToProps,mapDispatchToProps)(UI 组件)

- mapStateToProps:映射状态，返回值是一个对象
- mapDispatchToProps:映射操作状态的方法，返回值是一个对象

3. 备注 1：容器组件中的 store 是靠 props 传进去的，而不是在容器组件中直接引入
4. 备注 2：mapDispatchToProps，也可以是一个对象

## 5. 求和案例\_react-redux 优化

1. 容器组件和UI组件整合一个文件

2. 无需自己给容器组件传递store，给<App/>包裹一个<Provider store={store}>即可。

3. 使用了react-redux后也不用再自己检测redux中状态的改变了，容器组件可以自动完成这个工作。

4. mapDispatchToProps也可以简单的写成一个对象

5. 一个组件要和redux“打交道”要经过哪几步？

   1. 定义好UI组件---不暴露

   2. 引入connect生成一个容器组件，并暴露，写法如下：

      ```jsx
      connect(
      	state => ({key:value}), //映射状态
      	{key:xxxxxAction} //映射操作状态的方法
      )(UI组件)
      ```

   3. 在UI组件中通过this.props.xxxxxxx读取和操作状态

## 6. 求和案例\_react-redux 数据共享版

1. 定义一个Pserson组件，和Count组件通过redux共享数据。
2. 为Person组件编写：reducer、action，配置constant常量。
3. 重点：Person的reducer和Count的Reducer要使用combineReducers进行合并，合并后的总状态是一个对象！！！
4. 交给store的是总reducer，最后注意在组件中取出状态的时候，记得“取到位”。

## 7. 求和案例\_react-redux 开发者工具的使用

1. yarn add redux-devtools-extension
2. store中进行配置
   `import {composeWithDevTools} from 'redux-devtools-extension'`
   `const store = createStore(allReducer,composeWithDevTools(applyMiddleware(thunk)))`

## 8. 求和案例\_react-redux 最终版

1. 所有变量名字要规范，尽量触发对象的简写形式。
2. reducers文件夹中，编写index.js专门用于汇总并暴露所有的reducer

# 阮一峰 redux 笔记

```jsx
import { createStore } from 'redux';
let { subscribe, dispatch, getState } = createStore(reducer);

//creat store
//createStore函数接受另一个函数作为参数，返回新生成的 Store 对象。
//const store = createStore(fn)
const store = createStore(reducer)

//get data
const state = store.getState()

const ADD_TODO = '添加 TODO';

//type:状态的操作
function addTodo(text) {
  return {
    type: ADD_TODO,
    text
  }
}

//store.dispatch({
//  type: 'ADD_TODO',
//  payload: 'Learn Redux'
//});

store.dispatch(addTodo('Learn Redux'));

//接受 Action 和当前 State 作为参数，返回一个新的 State
const defaultState = 0;
const reducer = (state = defaultState, action) => {
  switch (action.type) {
    case 'ADD':
      return state + action.payload;
    default: 
      return state;
  }
};

const state = reducer(1, {
  type: 'ADD',
  payload: 2
});

store.subscribe(listener);


```

### redux

view -> (store.dispatch View 发出 Action 的唯一方法) ,让store知道action 的状态 ，）action -> get store -> get state -> update state= setState （reducer accept action and current state and return new state）-> subsribe(更新组件，重新渲染组件)

```javascript
import { createStore } from 'redux';
const store = createStore(fn);
const state = store.getState();
```

action creator -> return an object

const store = createStore(reducers);

store接收reducers，接收要更新的数据

### react-redux

#### 分为UI组件和容器组件

1. ui组件：

- 只负责 UI 的呈现，不带有任何业务逻辑
- 没有状态（即不使用`this.state`这个变量）
- 所有数据都由参数（`this.props`）提供
- 不使用任何 Redux 的 API

2. 容器组件

- 负责管理数据和业务逻辑，不负责 UI 的呈现
- 带有内部状态
- 使用 Redux 的 API

3. API

1. connect(): connect ui component and container component

   链接react组件和redux，从redux中取属性

- mapStateToProps return an object

-  mapDispatchToProps can be a function or an object
  - function will return two props, dispatch and ownprops,which as an object
  - object ,key->ownprops;value->action creator(function)

```jsx
import { connect } from 'react-redux'

const VisibleTodoList = connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoList)
```

2. `<provider>`

通过provider，让容器组件获取state对象，生成UI组件的参数

```JSX
render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

```jsx
const addMessage = (message) => {
  return {
    type: 'ADD',
    message: message
  }
};

// change code below this line
const mapDispatchToProps = (dispatch) => {
    return {
        submitNewMessage: (message)=>{
            dispatch(addMessage(message))
        }
    }
}
```

```jsx
const state = [];

// change code below this line
const mapStateToProps = (state)=>{
  return {
    messages: state
  }
```

```jsx
const addMessage = (message) => {
  return {
    type: 'ADD',
    message: message
  }
};

const mapStateToProps = (state) => {
  return {
    messages: state
  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (message) => {
      dispatch(addMessage(message));
    }
  }
};

class Presentational extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <h3>This is a Presentational Component</h3>
  }
};

const connect = ReactRedux.connect;
// change code below this line
const ConnectedComponent = connect(mapStateToProps, mapDispatchToProps) (Presentational)


```

```jsx
// Redux:
const ADD = 'ADD';

const addMessage = (message) => {
  return {
    type: ADD,
    message: message
  }
};

const messageReducer = (state = [], action) => {
  switch (action.type) {
    case ADD:
      return [
        ...state,
        action.message
      ];
    default:
      return state;
  }
};

const store = Redux.createStore(messageReducer);

// React:
class Presentational extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      messages: []
    }
    this.handleChange = this.handleChange.bind(this);
    this.submitMessage = this.submitMessage.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value
    });
  }
  submitMessage() {
    const currentMessage = this.state.input;
    this.setState({
      input: '',
      messages: this.state.messages.concat(currentMessage)
    });
  }
  render() {
    return (
      <div>
        <h2>Type in a new Message:</h2>
        <input
          value={this.state.input}
          onChange={this.handleChange}/><br/>
        <button onClick={this.submitMessage}>Submit</button>
        <ul>
          {this.state.messages.map( (message, idx) => {
              return (
                 <li key={idx}>{message}</li>
              )
            })
          }
        </ul>
      </div>
    );
  }
};

// React-Redux:
const mapStateToProps = (state) => {
  return { messages: state }
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (newMessage) => {
       dispatch(addMessage(newMessage))
    }
  }
};

const Provider = ReactRedux.Provider;
const connect = ReactRedux.connect;

// define the Container component here:
const Container = connect(mapStateToProps,mapDispatchToProps)(Presentational)


class AppWrapper extends React.Component {
  constructor(props) {
    super(props);
  }
 render() {
    // complete the return statement:
    return (
      <Provider store={store}>
        <Container />
      </Provider>
      );
  }
};

```

```jsx
// Redux:
const ADD = 'ADD';

const addMessage = (message) => {
  return {
    type: ADD,
    message: message
  }
};

const messageReducer = (state = [], action) => {
  switch (action.type) {
    case ADD:
      return [
        ...state,
        action.message
      ];
    default:
      return state;
  }
};

const store = Redux.createStore(messageReducer);

// React:
const Provider = ReactRedux.Provider;
const connect = ReactRedux.connect;

// Change code below this line
class Presentational extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      //messages: []
    }
    this.handleChange = this.handleChange.bind(this);
    this.submitMessage = this.submitMessage.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value
    });
  }
  submitMessage() {
    // this.setState({
    //   input: '',
    //   messages: this.state.messages.concat(this.state.input)
    // });
    this.props.submitNewMessage(this.state.input);
    this.setState({
      input: ''
    });
  }
  render() {
    return (
      <div>
        <h2>Type in a new Message:</h2>
        <input
          value={this.state.input}
          onChange={this.handleChange}/><br/>
        <button onClick={this.submitMessage}>Submit</button>
        <ul>
          {this.props.messages.map( (message, idx) => {
              return (
                 <li key={idx}>{message}</li>
              )
            })
          }
        </ul>
      </div>
    );
  }
};
// Change code above this line

const mapStateToProps = (state) => {
  return {messages: state}
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (message) => {
      dispatch(addMessage(message))
    }
  }
};

const Container = connect(mapStateToProps, mapDispatchToProps)(Presentational);

class AppWrapper extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Container/>
      </Provider>
    );
  }
};

```

```jsx
// import React from 'react'
// import ReactDOM from 'react-dom'
// import { Provider, connect } from 'react-redux'
// import { createStore, combineReducers, applyMiddleware } from 'redux'
// import thunk from 'redux-thunk'

// import rootReducer from './redux/reducers'
// import App from './components/App'

// const store = createStore(
//   rootReducer,
//   applyMiddleware(thunk)
// );

// ReactDOM.render(
//   <Provider store={store}>
//     <App/>
//   </Provider>,
//   document.getElementById('root')
// );

// change code below this line
console.log('Now I know React and Redux!');
```
