# 事件处理

## 合成事件特性

构造合成事件 SyntheticEvent

在React中，合成事件特性是指React框架为开发者提供的一种事件系统，用于处理用户交互。它是建立在原生DOM事件系统之上的，但有一些区别和优化。

React的合成事件特性具有以下一些特点：

跨浏览器兼容性：React的合成事件系统可以处理不同浏览器之间的兼容性问题，使开发者无需担心不同浏览器之间的差异。

事件委托：React的合成事件特性实现了事件委托模式，即将事件绑定到组件的父元素上，通过冒泡机制来处理事件，提高了性能和效率。

合成事件对象：React的合成事件特性提供了一个合成事件对象，包含了与事件相关的信息，如事件类型、目标元素、键盘鼠标位置等，开发者可以方便地获取和操作这些信息。

自动绑定this：React的合成事件特性会自动将事件处理函数的this绑定到组件实例上，无需手动绑定，简化了代码编写。

事件池：React的合成事件特性实现了事件池机制，通过重用事件对象来减少内存消耗和垃圾回收的压力，提高了性能。

对冒泡和捕获的支持：React的合成事件特性支持事件的冒泡和捕获阶段，开发者可以根据需要进行事件的捕获或冒泡处理。

总之，React的合成事件特性通过跨浏览器兼容性、事件委托、合成事件对象、自动绑定this、事件池和对冒泡和捕获的支持等特点，为开发者提供了方便、高效和灵活的事件处理方式。

We all know the pain of cross-browser development when some browsers don’t support the feature we want. So we have to maintain multiple implementations. React makes our life easier and wraps all HTML DOM events into a synthetic event wrapper.
All it does — it normalises behaviour across different browsers, and we don’t need to worry about cross-browser code maintenance. We can reference event properties and use helper functions such as preventDefault, React will provide consistency across all browsers.

All DOM events are bubbling up from the innermost element out its parents. For example, we have a button inside a form. When we subscribe to click events from both, click events will firstly arrive from the button and then from the form. To prevent events from bubbling up to parent elements we should call event.stopPropagation.

Whenever we attach several event listeners to the same element, to prevent propagation we need to call event.stopImmediatePropagation. In React we usually use this function when integrating with 3rd party libraries.

When React wraps events into synthetic event wrappers, it reuses synthetic event objects to optimise performance. After function using the event finished execution, React will nullify or reset the event object to the default state and reuse it for a new event.

It means that if we use any asynchronous code like promise or timer, then we will end up with a nullified event. To avoid such behaviour, we should call event.persist to keep this event object for ourselves. React will not nullify this event object for further reuse.

Synthetic events in React are needed to normalise behaviour across different browsers. All DOM events propagate from the target to its parents. When we need to stop it, we can call event.stopPropagation or event.stopImmediatePropagation.

React optimises performance by reusing synthetic event objects, which means that after the event handler finished execution react will nullify the event object to reuse it later. To reference events from asynchronous code we need to call event.persist to notify React not to nullify it.

### refs

1. https://7km.top/main/synthetic-event/
2. https://cloud.tencent.com/developer/article/2193659
3. https://chrisdeo.github.io/2018/12/06/React%E4%B8%AD%E7%9A%84%E5%90%88%E6%88%90%E4%BA%8B%E4%BB%B6%E4%BB%A5%E5%8F%8A%E4%BC%A0%E5%8F%82%E9%97%AE%E9%A2%98/
4. https://www.cnblogs.com/WindrunnerMax/p/14305631.html
5. https://juejin.cn/post/6844903988794671117
6. https://www.freecodecamp.org/chinese/news/best-practices-for-react/

# 参数传递/组件通信

1. 组件通信的方式有哪些

     - ⽗组件向⼦组件通讯: ⽗组件可以向⼦组件通过传 props 的⽅式，向⼦组件进⾏通讯
     - ⼦组件向⽗组件通讯: props+回调的⽅式，⽗组件向⼦组件传递props进⾏通讯，此props为作⽤域为⽗组件⾃身的函数，⼦组件调⽤该函数，将⼦组件想要传递的信息，作为参数，传递到⽗组件的作⽤域中
     - 兄弟组件通信: 找到这两个兄弟节点共同的⽗节点,结合上⾯两种⽅式由⽗节点转发信息进⾏通信
     - 跨层级通信: Context 设计⽬的是为了共享那些对于⼀个组件树⽽⾔是“全局”的数据，例如当前认证的⽤户、主题或⾸选语⾔，对于跨越多层的全局数据通过 Context 通信再适合不过
     - 发布订阅模式: 发布者发布事件，订阅者监听事件并做出反应,我们可以通过引⼊event模块进⾏通信
     - 全局状态管理⼯具: 借助Redux或者Mobx等全局状态管理⼯具进⾏通信,这种⼯具会维护⼀个全局状态中⼼Store,并根据不同的事件产⽣新的状态

2. 父子组件的通信方式

     - 父组件向子组件通信：父组件通过 props 向子组件传递需要的信息。
     - 子组件向父组件通信：props+回调的方式。


3. 跨级组件的通信方式

   使用context，context相当于一个大容器，可以把要通信的内容放在这个容器中，这样不管嵌套多深，都可以随意取用，对于跨越多层的全局数据可以使用context实现。

   useContext: https://github.com/linhaishe/FEnotes/blob/main/FE-Framework/React.js/hooks/useContent.md

4. 非嵌套关系组件的通信方式

   即没有任何包含关系的组件，包括兄弟组件以及不在同一个父级中的非兄弟组件。

     - 可以使用自定义事件通信（发布订阅模式）

     - 可以通过redux等进行全局状态管理

     - 如果是兄弟组件通信，可以找到这两个兄弟节点共同的父节点, 结合父子间通信方式进行通信。


5. 如何解决props层级过深的问题

   - 使用Context API：提供一种组件之间的状态共享，而不必通过显式组件树逐层传递props；

   - 使用Redux等状态库。

## 发布订阅模式粗解

```js
const MessageState = {
  // 当前的状态
  state: {},
  // 订阅的消息列表
  subscriptions: [],
  // 更新状态，并且触发订阅的消息
  setState(state, skipCallbacks = false) {
    this.state = {
      ...this.state,
      ...state,
    };
    if (!skipCallbacks) {
      this.subscriptions.forEach((cb) => cb(this.state));
    }
  },
  // 获取状态
  getState() {
    return this.state;
  },
  // 订阅一个消息，返回值是取消订阅函数
  subscribe(cb) {
    this.subscriptions.push(cb);
    return () => {
      this.unsubscribe(cb);
    };
  },
  // 取消订阅
  unsubscribe(cb) {
    this.subscriptions = this.subscriptions.filter((item) => item !== cb);
  },
};

export default MessageState;
```

![image-20231016111929967](/Users/lichunxian/Library/Application Support/typora-user-images/image-20231016111929967.png)

![image-20231016111939767](/Users/lichunxian/Library/Application Support/typora-user-images/image-20231016111939767.png)

缺点： 

1. 复杂性增加：发布订阅模式会引入更多的代码和逻辑，增加了组件的复杂性。相比于使用其他状态管理库（如Redux或Mobx），发布订阅模式需要手动管理订阅、取消订阅和事件的发布。
2. 难以追踪状态流向：在发布订阅模式下，状态的流向不太明确。当一个事件被发布时，可能会导致多个订阅者对状态进行更新，而这些更新可能会相互影响。这样会增加调试和维护的难度，因为很难准确追踪状态的变化路径。
3. 性能问题：由于发布订阅模式中的事件通常是广播的，意味着每个订阅者都会接收到该事件。这可能导致不必要的渲染和更新操作，从而降低性能。
4. 不容易进行状态优化：在发布订阅模式中，状态的更新通常是全局的，即所有订阅者都会收到相同的更新。这可能导致不必要的渲染和性能问题。而在其他状态管理库中，可以更精细地控制状态的更新，进行性能优化。
5. 事件总线（event bus）和发布订阅属于同一种解决方案，通过注册公共事件和监听公共事件触发更新

refs：

1. https://juejin.cn/post/7242623149752320058
2. https://aarthinim.medium.com/pubsub-in-reactjs-eaa8f9d6ec0
3. https://medium.com/@nouraldin.alsweirki/pub-sub-pattern-in-react-example-c5bbd08fa02f

## refs
1. https://www.freecodecamp.org/chinese/news/pass-data-between-components-in-react/

# Class 组件事件 this 绑定

在构造函数中绑定this

```jsx
  constructor() {
    super();
    this.state = {
      liked: false
    };
    this.handleClick = this.handleClick.bind(this);
  }
```

函数定义的时候使用箭头函数

```jsx
constructor(props){
    super(props);
    this.state={
           msg:'hello world',
    }
    render(){
      <button onClcik={()=>{alert(this.state.msg)}}>点我</button>
    }
}
```

函数调用是使用bind绑定this

```jsx
 <button onClick={this.getMsg.bind(this)}>点我</button>
```


# 表单

## 受控组件 VS 非受控组件

- 受控组件，简单来讲，就是受我们控制的组件，组件的状态全程响应外部数据。组件添加value值和onChange事件
- 非受控组件，简单来讲，就是不受我们控制的组件。一般情况是在初始化的时候接受外部数据，然后自己在内部存储其自身状态。通过ref获取数据

In React, there are two ways of handling form data:

- **Controlled Components:** In this approach, form data is handled by React through the use of hooks such as the `useState` hook.
- **Uncontrolled Components:** Form data is handled by the Document Object Model (DOM) rather than by React. The DOM maintains the state of form data and updates it based on user input.

## 各个表单控件上的值处理区别

| 控件类型                   | 值处理方式                                                  | 示例代码                                                     |
| -------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| `<input type="text"/>`     | 通过`event.target.value`获取输入框的值                      | `const handleInputChange = (event) => {<br> setValue(event.target.value);<br>}` |
| `<textarea/>`              | 通过`event.target.value`获取文本域的值                      | `const handleTextareaChange = (event) => {<br> setTextValue(event.target.value);<br>}` |
| `<select>`和`<option>`     | 通过`event.target.value`获取选择框选中的值                  | `const handleSelectChange = (event) => {<br> setSelectedValue(event.target.value);<br>}` |
| `<input type="checkbox"/>` | 通过`event.target.checked`获取复选框的选中状态              | `const handleCheckboxChange = (event) => {<br> setChecked(event.target.checked);<br>}` |
| `<input type="radio"/>`    | 通过设置`checked`属性和`onChange`事件来处理单选框的选中状态 | `const handleRadioChange = (event) => {<br> setSelectedValue(event.target.value);<br>}` |

## 表单事件处理

React表单事件处理一般包括两个方面：受控组件的值管理和事件处理函数的编写。下面是一个简单的示例，说明如何在React中处理表单事件：

```js
import React, { useState } from 'react';

const MyForm = () => {
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`你输入的内容为：${inputValue}`);
    setInputValue('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        文本框：
        <input type="text" value={inputValue} onChange={handleInputChange} />
      </label>
      <br />
      <button type="submit">提交</button>
    </form>
  );
};
```

## refs

1. https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components
2. https://vue3js.cn/interview/React/controlled_Uncontrolled.html
3. https://github.com/careteenL/react/issues/7
4. https://learnku.com/docs/react-doc/shou-kong-yu-fei-shou-kong-zu-jian/13610
5. https://github.com/MuYunyun/blog/blob/main/React/Component_Design/%E9%87%8D%E6%96%B0%E8%AE%A4%E8%AF%86%E5%8F%97%E6%8E%A7%E4%B8%8E%E9%9D%9E%E5%8F%97%E6%8E%A7%E7%BB%84%E4%BB%B6.md
6. https://www.altogic.com/blog/difference-between-controlled-and-uncontrolled-component

# API

## 1. Suspense

React Suspense 是 React 的一个新特性，用于处理异步数据的加载和渲染。它提供了一种简单的方式来暂停组件的渲染，直到异步操作完成或者等待时间结束。通过使用 Suspense 组件和相关的属性和方法，可以轻松地实现数据的异步获取和渲染的暂停。

1. React Suspense 的介绍

   React Suspense 是 React 的一个新特性，它用于处理异步数据的加载和渲染。它提供了一种简单的方式来暂停组件的渲染，直到异步操作完成或者等待时间结束。

   React Suspense 的主要作用是改善用户体验和性能。传统上，当一个组件依赖于异步数据时，我们需要在组件中手动处理数据加载的状态，并在数据加载完成后更新组件。这样的处理方式会导致组件的代码变得复杂，同时也会影响用户的体验，因为他们可能会看到加载指示器或空白页面。

   通过使用 React Suspense，我们可以将异步操作的处理逻辑从组件中分离出来，使得组件的代码更加简洁和可读性。Suspense 组件可以暂停组件的渲染，并在异步操作完成后再继续渲染组件。这样，用户将不会看到加载指示器或空白页面，而是在数据加载完成后立即看到组件的内容。这提供了更好的用户体验。

   此外，React Suspense 还支持代码分割和懒加载，可以使得应用程序的加载速度更快，并减少了不必要的资源消耗。它还提供了错误边界的功能，可以更好地处理组件内部的错误，使得应用程序更加健壮和稳定。总的来说，React Suspense 为开发者提供了一种简单且强大的方式来处理异步数据的加载和渲染，提升了应用程序的性能和用户体验。

2. 异步渲染

   - 传统的异步数据加载方式

     在组件的生命周期方法中发送异步请求或执行异步操作。
     使用 isLoading 状态来跟踪数据是否正在加载。
     在加载完成后更新组件的状态，以便渲染数据。
     这种方式需要手动管理加载状态，如果有多个组件依赖于相同的异步数据，需要在每个组件中重复处理加载逻辑，使得代码变得复杂。同时，用户可能会在数据加载时看到加载指示器或空白页面。

     React Suspense 引入了一种更简单的异步渲染机制，它基于以下两个概念：

     Promise 和 Suspense 组件：React Suspense 允许组件暂停渲染，直到异步操作（如数据获取、代码分割等）完成。组件可以返回一个 Promise 对象，其中包含异步操作的结果。同时，使用 Suspense 组件来包裹需要等待异步操作的组件。

     fallback 属性：Suspense 组件接受一个 fallback 属性，用于指定在等待异步操作完成时展示的内容。可以是加载指示器、占位符或任何其他合适的内容。

   - React Suspense 的异步渲染机制

     1. 在组件的渲染方法中，返回一个 Promise 对象，该对象包含异步操作的结果。可以是数据获取、代码分割等。
     2. 使用 Suspense 组件包裹需要等待异步操作完成的组件，并设置 fallback 属性来指定加载时的内容。
     3. 当异步操作完成后，Suspense 组件会自动渲染被包裹的组件。

   - Suspense 组件的使用方法

     ```jsx
       import React, { Suspense } from 'react';
     
       const MyComponent = React.lazy(() => import('./MyComponent'));
     
       function App() {
         return (
           <div>
             <h1>My App</h1>
             <Suspense fallback={<div>Loading...</div>}>
               <MyComponent />
             </Suspense>
           </div>
         );
       }
     
       export default App;
     ```

     MyComponent 组件会被异步加载。在加载完成之前，Suspense 组件会显示 fallback 属性指定的加载中内容。加载完成后，Suspense 组件会渲染 MyComponent 组件。

     这就是 React Suspense 的基本使用方法，它简化了处理异步渲染的流程，提供了更好的用户体验和开发体验。

3. fallback 属性

   - fallback 属性的作用

     fallback 属性是 Suspense 组件的一个重要属性，它用于指定在等待异步操作完成时展示的内容。

     fallback 属性的作用是在异步操作进行过程中，为用户提供一个加载中的状态。当 Suspense 组件包裹的组件处于等待异步操作的状态时，fallback 属性指定的内容会代替被包裹组件的渲染。

   - 使用 Suspense 组件的 fallback 属性展示加载中状态

     当 MyComponent 组件处于加载状态时，Suspense 组件会显示 fallback 属性指定的 Loading... 文本。这样，用户在等待异步操作完成时可以看到一个友好的加载中状态。

     fallback 属性的内容可以是任何 React 元素，可以是加载指示器、占位符或者任意其他合适的内容。它可以根据实际需求进行定制，以提供更好的用户体验。

     需要注意的是，fallback 只在异步操作进行过程中显示，一旦异步操作完成，被包裹的组件会开始渲染，fallback 会被替换为真正的组件内容。

     总结来说，fallback 属性是 Suspense 组件的一个重要属性，它用于展示在等待异步操作完成时的加载中状态。它可以是任何 React 元素，用于提供更好的用户体验和反馈。

4. Suspense for Data Fetching

   - 使用 React Suspense 进行数据获取
   - 使用 Suspense 组件和 React.lazy 进行代码分割

   ```jsx
   import React, { Suspense } from 'react';
   
   const fetchData = () => {
     return new Promise((resolve) => {
       setTimeout(() => {
         resolve('Data fetched!');
       }, 2000);
     });
   };
   
   function MyComponent() {
     const data = fetchData();
   
     return <div>{data}</div>;
   }
   
   function App() {
     return (
       <div>
         <h1>My App</h1>
         <Suspense fallback={<div>Loading...</div>}>
           <MyComponent />
         </Suspense>
       </div>
     );
   }
   
   export default App;
   
   ```

### 5. 错误边界

   - 错误边界的概念

     错误边界是 React 中的概念，用于处理组件内部的错误。当组件内部发生错误时，错误边界可以捕获并处理这些错误，以避免整个应用程序崩溃。

     使用 React Suspense 进行异步加载和渲染时，可以使用 Suspense 组件来处理组件内部的错误。Suspense 组件接受一个 fallback 属性，我们可以在其中展示一个错误提示或备用内容。

   - 使用 Suspense  组件处理组件内部的错误

     ```jsx
     import React, { Suspense } from 'react';
     
     const MyComponent = React.lazy(() => import('./MyComponent'));
     
     function App() {
       return (
         <div>
           <h1>My App</h1>
           <ErrorBoundary fallback={<div>Oops! Something went wrong.</div>}>
             <Suspense fallback={<div>Loading...</div>}>
               <MyComponent />
             </Suspense>
           </ErrorBoundary>
         </div>
       );
     }
     
     export default App;
     
     ```

   - 使用 ErrorBoundary 组件处理渲染错误

     创建了一个 ErrorBoundary 组件。它通过重写 getDerivedStateFromError 和 componentDidCatch 方法来捕获组件内部的错误。如果发生错误，ErrorBoundary 组件会显示 fallback 属性指定的内容。

     使用 ErrorBoundary 组件，我们可以更全面地处理组件内部的渲染错误，包括异步加载和其他类型的错误。

     总结来说，使用 Suspense 组件可以处理组件内部的异步加载和渲染错误，通过设置 fallback 属性来展示错误提示或备用内容。而使用 ErrorBoundary 组件可以处理更广泛的渲染错误，并提供更详细的错误处理和记录功能。

     ```jsx
     import React from 'react';
     
     class ErrorBoundary extends React.Component {
       constructor(props) {
         super(props);
         this.state = { hasError: false };
       }
     
       static getDerivedStateFromError(error) {
         return { hasError: true };
       }
     
       componentDidCatch(error, errorInfo) {
         // 可以在这里记录错误信息
       }
     
       render() {
         if (this.state.hasError) {
           return this.props.fallback;
         }
     
         return this.props.children;
       }
     }
     
     function App() {
       return (
         <div>
           <h1>My App</h1>
           <ErrorBoundary fallback={<div>Oops! Something went wrong.</div>}>
             <MyComponent />
           </ErrorBoundary>
         </div>
       );
     }
     
     export default App;
     
     ```

     Hooks version

     ```jsx
     import React, { useState, useEffect } from 'react';
     
     function ErrorBoundary({ fallback, children }) {
       const [hasError, setHasError] = useState(false);
     
       useEffect(() => {
         return () => {
           // 清除错误状态
           setHasError(false);
         };
       }, []);
     
       const handleCatchError = () => {
         setHasError(true);
       };
     
       if (hasError) {
         return fallback;
       }
     
       return children;
     }
     
     function MyComponent() {
       const fetchData = () => {
         return new Promise((resolve, reject) => {
           setTimeout(() => {
             reject('Error occurred');
           }, 2000);
         });
       };
     
       useEffect(() => {
         fetchData()
           .then((data) => {
             // 使用数据
           })
           .catch((error) => {
             // 捕获错误
             handleCatchError();
           });
       }, []);
     
       return <div>My Component</div>;
     }
     
     function App() {
       return (
         <div>
           <h1>My App</h1>
           <ErrorBoundary fallback={<div>Oops! Something went wrong.</div>}>
             <MyComponent />
           </ErrorBoundary>
         </div>
       );
     }
     
     export default App;
     
     ```

6. Suspense 的最佳实践

   - 使用 Suspense 进行代码分割和懒加载

     使用 Suspense 进行代码分割和懒加载：将需要异步加载的组件使用 React.lazy 进行包装，并将其作为 Suspense 组件的子组件。这样，只有在需要时才会加载这个组件，提高应用程序的加载性能。

   - 结合错误边界处理组件错误

     结合错误边界处理组件错误：使用 ErrorBoundary 组件来捕获和处理组件内部的错误。将需要进行错误边界处理的组件包裹在 ErrorBoundary 组件中，并提供 fallback 属性来指定错误时的备用内容。

   - 注意事项和常见问题解决方案

     - Suspense 组件只能用于包裹 React.lazy 包装的组件，并且只能在组件树的顶层使用。
     - Suspense 组件目前只支持使用 React.lazy 进行异步加载，不支持使用其他动态导入方式。
     - 当多个 Suspense 组件嵌套时，只会展示最靠近根节点的 fallback 内容。如果想要在多个层级中展示不同的 fallback 内容，可以使用多个 Suspense 组件进行嵌套。
     - Suspense 组件的 fallback 属性可以是任何 React 元素，可以根据实际需求进行定制。
     - 当组件内部发生错误时，错误边界只会捕获其子组件的错误，不会捕获其父组件或其他兄弟组件的错误。

     通过遵循这些最佳实践和注意事项，我们可以更好地使用 Suspense 组件进行代码分割、懒加载和错误处理，提高应用程序的性能和用户体验。
   
   同时使用ErrorBoundary和Suspense来提供更全面的错误处理和加载状态管理。
   
   当在React应用程序中使用异步加载的组件时，可以将ErrorBoundary用于捕获和处理这些异步组件中可能发生的错误。这样，如果异步组件发生错误，错误边界将会捕获到错误并根据需要展示错误信息。
   
   同时，可以在Suspense组件中使用fallback属性来指定一个加载状态的UI。这样，在异步组件加载期间，可以显示备选UI（如加载指示器）来提供更好的用户体验。如果异步组件加载成功，Suspense会自动渲染出异步组件的内容。
   
   通过同时使用ErrorBoundary和Suspense，可以实现更好的错误处理和加载状态管理。错误边界用于捕获和处理错误，Suspense用于展示加载状态的UI，结合起来可以提供更好的用户体验和应用程序的稳定性。

## 2. React.lazy

React.lazy 是 React 提供的一个用于实现组件懒加载的函数。它可以让我们在需要的时候才加载组件，而不是将所有组件都一次性加载。

1. React.lazy

   React.lazy 是 React 提供的一个函数，用于实现组件的懒加载。懒加载意味着只有在需要时才会加载组件，而不是在应用程序初始化时就加载所有组件。

2. 使用 React.lazy 进行懒加载

  使用 React.lazy 时，我们需要将需要懒加载的组件作为参数传递给 React.lazy 函数。例如：`const MyComponent = React.lazy(() => import('./MyComponent'))`
  React.lazy 函数返回一个包装后的组件，我们可以像使用普通组件一样使用它。

3. 懒加载和 Suspense

  在使用 React.lazy 进行懒加载时，通常会结合使用 Suspense 组件。Suspense 组件可以在组件加载过程中显示一个加载状态，以提供更好的用户体验。
  可以将需要懒加载的组件放在 Suspense 组件内，并设置 fallback 属性来指定加载状态时的备用内容。
4. 其他注意事项

  React.lazy 只能用于默认导出的组件。如果组件使用命名导出，则需要先将其包装为默认导出的形式。
  React.lazy 目前只支持默认导出的组件作为参数，不支持命名导出的组件。
  使用 React.lazy 可以帮助我们优化应用程序的加载性能，只在需要的时候才加载组件。结合 Suspense 组件使用，可以提供更好的用户体验。

## 3. 新旧 Context

在React中，有两种类型的Context：旧版Context和新版Context。

1. 旧版Context： 旧版Context是在React v16.3之前引入的。使用旧版Context时，您需要使用`React.createContext()`来创建一个Context对象，并使用`Context.Provider`组件包裹提供给子组件的数据。

```jsx
1// 创建一个旧版Context对象
2const MyContext = React.createContext();
3
4// 使用Context.Provider包裹提供给子组件的数据
5function ParentComponent() {
6  const data = "Hello, World!";
7
8  return (
9    <MyContext.Provider value={data}>
10      <ChildComponent />
11    </MyContext.Provider>
12  );
13}
14
15// 在子组件中使用Context.Consumer来访问数据
16function ChildComponent() {
17  return (
18    <MyContext.Consumer>
19      {value => <p>{value}</p>}
20    </MyContext.Consumer>
21  );
22}
```

2. 新版Context： 新版Context是在React v16.3中引入的改进版本。使用新版Context时，您可以使用`React.createContext()`创建一个Context对象，并将其作为静态类属性或使用`useContext` Hook在函数组件中访问。

```jsx
1// 创建一个新版Context对象
2const MyContext = React.createContext();
3
4// 在父组件中提供数据
5function ParentComponent() {
6  const data = "Hello, World!";
7
8  return (
9    <MyContext.Provider value={data}>
10      <ChildComponent />
11    </MyContext.Provider>
12  );
13}
14
15// 在子组件中使用useContext Hook来访问数据
16function ChildComponent() {
17  const value = React.useContext(MyContext);
18
19  return <p>{value}</p>;
20}
```

无论使用旧版Context还是新版Context，它们的目标都是为了在组件树中共享数据。但是在使用上有一些差异，新版Context通过Hook的方式更加简洁方便，而旧版Context则需要使用`Context.Consumer`来获取数据。同时，新版Context还提供了更好的性能优化和更好的开发者体验。因此，推荐在React v16.3及以上的版本中使用新版Context。

## 4. 错误边界

### 1. 引言

   - 介绍错误边界的概念和作用

   当应用程序中的组件发生错误时，React默认会将错误信息打印到控制台，并中断整个组件树的渲染。这可能会导致整个应用程序出现崩溃的情况，给用户带来不好的体验。错误边界的作用就是为了解决这个问题。

   错误边界是一种React组件，用于捕获并处理其子组件内部抛出的错误。它能够在渲染过程中捕获错误，防止整个组件树崩溃，并提供备选UI或展示错误信息。通过使用错误边界，我们可以限制错误的影响范围，使应用程序能够继续正常运行，同时提供错误的可视化反馈和恢复策略。

   错误边界的主要目的是提高应用程序的稳定性和可靠性。它们通过将错误隔离到特定的组件中，并提供友好的错误处理机制来提升用户体验。在大型的React应用程序中，错误边界可以帮助我们更好地管理错误，快速定位和修复问题，避免整个应用程序的崩溃和不必要的维护成本。

   需要错误边界的原因包括：

   - 保护应用程序不受错误的影响，提高稳定性。
   - 提供更好的用户体验，避免整个应用程序的崩溃。
   - 提供友好的错误处理和恢复策略，减少维护成本。
   - 更好的代码可维护性和可测试性，方便定位和修复问题。

   总之，错误边界是一种重要的React特性，可以提供更好的错误处理和容错能力，帮助我们构建稳定、可靠的React应用程序。

### 2. 错误边界的基本使用

   - 创建一个错误边界组件
   - 使用`componentDidCatch`生命周期方法来捕获错误
   - 渲染错误的备选UI或展示错误信息

   ```jsx
   import React, { useState } from "react";
   
   function ErrorBoundary({ children }) {
     const [hasError, setHasError] = useState(false);
     const [error, setError] = useState(null);
   
     const handleCatchError = () => {
       setHasError(true);
       // 其他处理逻辑
     };
   
     if (hasError) {
       return (
         <div>
           <h2>Something went wrong.</h2>
           <p>{error.toString()}</p>
         </div>
       );
     }
   
     try {
       return children;
     } catch (error) {
       setError(error);
       handleCatchError();
       return null;
     }
   }
   
   export default ErrorBoundary;
   
   ```

   ```jsx
   class ErrorBoundary extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         hasError: false,
         error: null,
         errorInfo: null
       };
     }
   
     componentDidCatch(error, errorInfo) {
       this.setState({
         hasError: true,
         error: error,
         errorInfo: errorInfo
       });
     }
   
     render() {
       if (this.state.hasError) {
         // 渲染备选UI或展示错误信息
         return (
           <div>
             <h2>Something went wrong.</h2>
             <p>{this.state.error.toString()}</p>
             <p>{this.state.errorInfo.componentStack}</p>
           </div>
         );
       }
       // 渲染正常的子组件
       return this.props.children;
     }
   }
   
   ```

   ```jsx
   <ErrorBoundary>
     <ChildComponent />
   </ErrorBoundary>
   ```

### 3. ErrorBoundary vs Suspense

   | ErrorBoundary                                     | Suspense                                                    |
   | ------------------------------------------------- | ----------------------------------------------------------- |
   | 用于捕获并处理组件树中的错误                      | 用于在组件树中暂停和显示加载状态                            |
   | 通过捕获`componentDidCatch`方法中的错误来处理错误 | 通过`<Suspense>`组件和`fallback`属性来指定加载状态的UI      |
   | 可以将错误信息展示给用户或执行其他错误处理逻辑    | 在加载状态期间，可以显示备选UI、加载指示器等                |
   | 可以将错误边界组件嵌套在组件树的任何位置          | 可以将`<Suspense>`组件嵌套在组件树的任何位置                |
   | 错误边界只需要在错误边界组件中实现相关逻辑        | `<Suspense>`需要结合React异步组件（如`React.lazy`）一起使用 |
   | 错误边界适用于同步和异步组件                      | `<Suspense>`主要用于处理异步加载的组件                      |
   | 可以自定义错误边界的实现逻辑                      | `<Suspense>`的加载状态UI可以是静态的或动态的，根据需要定制  |
   | 错误边界在React v16之前不可用                     | `<Suspense>`是在React v16.6中引入的                         |

ErrorBoundary和Suspense是React提供的两个不同的特性，用于不同的场景。ErrorBoundary用于捕获和处理组件树中的错误，提供错误处理和恢复策略；而Suspense用于在组件树中暂停和显示加载状态，使得异步加载的组件能够更加友好地显示加载过程。它们的使用方式和适用场景有所不同，可以根据实际需求选择使用。

### 3. 错误边界的嵌套

   - 错误边界的嵌套结构和使用方法
   - 处理不同层级的错误

   ```jsx
   import React, { useState } from 'react';
   
   function ParentErrorBoundary({ children }) {
     const [hasError, setHasError] = useState(false);
     const [error, setError] = useState(null);
   
     const handleCatchError = (error) => {
       setHasError(true);
       setError(error);
     };
   
     if (hasError) {
       return (
         <div>
           <h2>Parent Component: Something went wrong.</h2>
           <p>{error.toString()}</p>
         </div>
       );
     }
   
     return (
       <div>
         <h2>Parent Component</h2>
         <ChildErrorBoundary onError={handleCatchError}>
           <ChildComponent />
         </ChildErrorBoundary>
       </div>
     );
   }
   
   function ChildErrorBoundary({ children, onError }) {
     const [hasError, setHasError] = useState(false);
     const [error, setError] = useState(null);
   
     const handleCatchError = (error) => {
       setHasError(true);
       setError(error);
       onError(error);
     };
   
     if (hasError) {
       return (
         <div>
           <h2>Child Component: Something went wrong.</h2>
           <p>{error.toString()}</p>
         </div>
       );
     }
   
     return (
       <div>
         <h2>Child Component</h2>
         {children}
       </div>
     );
   }
   
   function ChildComponent() {
     // 子组件的实现逻辑
     throw new Error('Error occurred in Child Component');
     return <div>Child Component</div>;
   }
   
   function App() {
     return (
       <ParentErrorBoundary>
         <h1>App Component</h1>
       </ParentErrorBoundary>
     );
   }
   
   export default App;
   
   ```

   这也太能嵌套了吧，如果我子组件还有子组件还有孙子组件这不就是套娃行为吗

   ```jsx
   import React, { useState } from 'react';
   
   function ErrorBoundary({ children }) {
     const [hasError, setHasError] = useState(false);
     const [error, setError] = useState(null);
   
     const handleCatchError = (error) => {
       setHasError(true);
       setError(error);
     };
   
     if (hasError) {
       return (
         <div>
           <h2>Something went wrong.</h2>
           <p>{error.toString()}</p>
         </div>
       );
     }
   
     return children;
   }
   
   function ChildComponent() {
     // 子组件的实现逻辑
     throw new Error('Error occurred in Child Component');
     return <div>Child Component</div>;
   }
   
   function GrandChildComponent() {
     // 孙子组件的实现逻辑
     throw new Error('Error occurred in GrandChild Component');
     return <div>GrandChild Component</div>;
   }
   
   function RecursiveErrorBoundary({ children }) {
     const [hasError, setHasError] = useState(false);
     const [error, setError] = useState(null);
   
     const handleCatchError = (error) => {
       setHasError(true);
       setError(error);
     };
   
     if (hasError) {
       return (
         <div>
           <h2>Something went wrong.</h2>
           <p>{error.toString()}</p>
         </div>
       );
     }
   
     return (
       <ErrorBoundary>
         {React.Children.map(children, (child) => {
           if (React.isValidElement(child)) {
             return React.cloneElement(child, {
               onError: handleCatchError,
             });
           }
           return child;
         })}
       </ErrorBoundary>
     );
   }
   
   function App() {
     return (
       <div>
         <h1>App Component</h1>
         <RecursiveErrorBoundary>
           <ChildComponent />
           <RecursiveErrorBoundary>
             <GrandChildComponent />
           </RecursiveErrorBoundary>
         </RecursiveErrorBoundary>
       </div>
     );
   }
   
   export default App;
   
   ```

   哈哈哈，真的大可不必啊。

### 4. 错误处理和错误边界的最佳实践

   - 错误边界的错误处理策略：
     错误边界可以用于捕获和处理React组件树中发生的JavaScript错误。一旦错误被错误边界捕获，你可以采取以下策略来处理错误：

     1. 显示错误信息：你可以在错误边界组件中渲染一些错误消息，告知用户发生了错误，并提供相关的错误详情。

     2. 回退UI或备用UI：你可以在错误边界组件中渲染一些备选的UI，代替发生错误的组件。这可以提供一种优雅的方式来处理错误，避免整个应用程序崩溃。

     3. 记录错误：你可以将错误信息记录到日志中，以便进行排查和调试。你可以使用第三方日志库或发送错误报告给服务器。

     4. 重置应用状态：在某些情况下，你可能希望在错误发生后重置应用的状态，以确保应用程序继续可用。

   - 错误边界适用于以下情况：

     1. 异步操作：当在组件的生命周期方法外部执行异步操作时，错误边界可以捕获并处理这些操作中的错误。

     2. 第三方库：当使用第三方库时，该库可能会抛出错误。通过将第三方库包装在错误边界组件中，可以在发生错误时进行处理。

     3. 大型组件树：当应用程序具有复杂的组件层级结构时，错误边界可以提供一种简化错误处理逻辑的方式。

   - 错误边界的局限性：

     1. 仅在渲染期间捕获错误：错误边界只能捕获在组件的渲染期间发生的错误。它无法捕获事件处理程序、异步操作（例如定时器或网络请求）或服务端渲染期间的错误。

     2. 仅适用于子组件：错误边界只能捕获其子组件中的错误，无法捕获其自身或父级组件中的错误。

     3. 不适用于Hooks：错误边界无法捕获自定义Hook中发生的错误。在使用自定义Hook的组件中，我们需要自行处理和捕获这些错误。

        因为自定义Hook实际上只是一个普通的JavaScript函数，并不是一个React组件。错误边界只能捕获在React组件的渲染过程中发生的错误，而自定义Hook并不是一个React组件，因此错误边界无法感知和捕获这些错误。

        当在自定义Hook中发生错误时，React会将错误抛出到调用该自定义Hook的组件中。这意味着需要在使用自定义Hook的组件中处理和捕获这些错误。可以通过使用`try/catch`语句或其他错误处理机制来捕获和处理自定义Hook中发生的错误。

        ```jsx
        import React, { useState, useEffect } from 'react';
        
        function useCustomHook() {
          const [data, setData] = useState(null);
        
          useEffect(() => {
            try {
              // 模拟发生错误的操作
              throw new Error('Error occurred in custom hook');
              // 其他自定义Hook的逻辑
            } catch (error) {
              // 在自定义Hook中处理错误
              console.error(error);
              // 可以选择设置错误状态或执行其他逻辑
            }
          }, []);
        
          return data;
        }
        
        function App() {
          const data = useCustomHook();
        
          return (
            <div>
              {data ? (
                <h2>Data: {data}</h2>
              ) : (
                <h2>No data available</h2>
              )}
            </div>
          );
        }
        
        export default App;
        ```

     4. 有限的错误处理能力：错误边界只能处理JavaScript错误，无法处理其他类型的错误，如CSS错误或渲染问题。

### 5. 错误边界的错误信息收集和上报

   - 收集错误的信息和堆栈轨迹
   - 使用第三方库将错误信息上报给服务器

   使用第三方库将错误信息上报给服务器：有许多第三方库可用于将错误信息上报给服务器，例如Sentry、Bugsnag、Rollbar等。这些库提供了捕获和上报错误的功能，并提供了丰富的错误跟踪和分析工具。

   ```jsx
   import * as Sentry from '@sentry/react';
   
   class ErrorBoundary extends React.Component {
     componentDidCatch(error, errorInfo) {
       this.setState({
         error: error,
         errorInfo: errorInfo,
       });
   
       // 使用Sentry将错误信息上报给服务器
       Sentry.captureException(error, { extra: errorInfo });
     }
   
     render() {
       if (this.state.errorInfo) {
         return (
           <div>
             <h2>Something went wrong.</h2>
             <p>{this.state.error.toString()}</p>
             <p>{this.state.errorInfo.componentStack}</p>
           </div>
         );
       }
   
       return this.props.children;
     }
   }
   ```

### 6. 错误边界的性能影响

   - 错误边界的性能特性和注意事项
   - 避免过度使用错误边界

错误边界是一个有用的工具，但是在使用时需要注意其性能特性和避免过度使用。下面是关于错误边界的性能特性和使用注意事项：

性能特性：

1. 错误边界对于捕获并处理单个组件树中的错误非常有效。当错误发生时，错误边界会阻止错误进一步传播并导致整个应用程序崩溃。这有助于提高应用程序的稳定性和用户体验。
2. 错误边界的性能开销相对较低，因为它们只会在错误发生时触发。在正常情况下，它们不会引入任何额外的性能开销。

注意事项：

1. 错误边界应该被谨慎使用。将它们放置在每个组件中可能会导致过度使用，并可能会隐藏应用程序中的真实问题。错误边界应该被用于捕获和处理无法避免的错误，而不是作为不负责任的容错机制。
2. 错误边界只能捕获其子组件中的错误。它们不能捕获在事件处理程序、异步代码（例如setTimeout或Promise）或服务端渲染期间发生的错误。在这些情况下，你需要使用适当的错误处理机制来捕获和处理错误。
3. 错误边界不会捕获在组件的constructor方法中抛出的错误。如果组件的构造函数中发生错误，它会导致组件无法正确地挂载和渲染。在这种情况下，你可以使用静态getDerivedStateFromError方法来处理错误边界。

避免过度使用错误边界的一些建议：

1. 只在必要时使用错误边界。将错误边界应用于核心组件或对应用程序稳定性至关重要的部分。
2. 避免在低级别的细粒度组件中使用错误边界。尽量将错误边界放在更高级别的组件中，这样可以更好地控制错误的边界范围，同时减少错误边界的数量。
3. 添加适当的错误处理逻辑。错误边界可以捕获错误，但是你仍然需要处理它们。确保在错误边界内部执行适当的错误处理逻辑，例如记录错误、向用户显示错误消息或触发适当的回退行为。

总之，错误边界是一个有用的工具，可以帮助我们在React应用程序中捕获和处理错误。但是，我们应该谨慎使用它们，避免过度使用，并在使用时注意性能特性和注意事项。这样可以确保错误边界的有效性，并避免引入不必要的开销或隐藏真实问题。

## ReactDom.createPortal()

[`createPortal(children, domNode, key?)`](https://react.dev/reference/react-dom/createPortal#createportal)

### 1.  Portal 是什么

   Portal 的概念，即允许将组件渲染到 DOM 结构中的不同位置。为什么需要 Portal 以及在哪些场景下它们特别有用。

   Portal 是 React 的一项功能，它允许你将组件渲染到 DOM 结构中的不同位置。通常情况下，React 组件会在它们自身的父组件内渲染，但 Portal 允许你将组件渲染到 DOM 结构中的任何位置，甚至是位于 React 组件层次结构之外的位置。

   React Portals are an advanced concept that allows developers to [render their elements](https://blog.logrocket.com/react-render-props-vs-custom-hooks/) outside the React hierarchy tree without comprising the parent-child relationship between components.

   Usually, typical React components are located within the [DOM](https://blog.logrocket.com/what-virtual-dom-react/). This means that it might be tricky for you to render modals or pop-up windows.

   Portals are great for places where you want to render elements on top of each other. 

   **为什么需要 Portal**

   Portal 在以下情况下特别有用：

   1. **解决样式和布局问题**：Portal 可以帮助你处理复杂的样式和布局需求。你可以在不影响父组件布局的情况下，将内容渲染到需要的位置。有时，父组件和子组件之间的 CSS 样式可能会发生冲突，导致不希望的布局问题。通过使用 Portal，你可以将子组件的内容渲染到 DOM 结构的不同层次结构中，使其脱离父组件的 CSS 影响。
   2. **模态对话框和弹出菜单**：Portal 是创建模态对话框、弹出菜单和其他覆盖全局内容的常见方式。这允许你创建交互性强的用户界面元素。
   3. **处理全局状态**：Portal 可用于将组件渲染到全局状态管理器（如 Redux 或 Mobx）所管理的 DOM 结构中，以确保组件能够访问全局状态。
   4. **处理第三方库集成**：当你需要在 React 中集成第三方库或外部组件时，Portal 可以用于将这些组件渲染到 React 应用的特定部分。
   5. **处理滚动固定元素**：Portal 还可以用于创建滚动固定元素，例如固定在页面某一位置的工具栏或侧边栏。这些元素可以独立于页面的滚动而保持固定，从而提供更好的用户体验。
   6. Cookie alerts: Provides the user with options to let them choose what cookies they want to allow in their web browser:

### 2. 基本的 createPortal 示例

   - 创建一个简单的 React 组件，其中使用 **`ReactDOM.createPortal()`** 将内容渲染到另一个 DOM 元素中。

   - 创建一个目标容器（目标 DOM 元素），以便将 Portal 渲染到特定位置。确保目标容器在组件渲染之前已存在。

Step 1: Adding an extra mount point in a `DOM` outside of `react-root`

```jsx
<div id="root"></div>
<div id="portal-root"></div>
```

Step 2: Build a reusable React Portal wrapper component using `createPortal` in React

`createPortal(children, domNode, key?)`

```jsx
import { createPortal } from 'react-dom';

// ...

<div>
  <p>This child is placed in the parent div.</p>
  {createPortal(
    <p>This child is placed in the document body.</p>,
    document.body
  )}
</div>
```

```jsx
function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null
  return createPortal(
    <div className="modal">
      <button onClick={onClose}>Close</button>
      {children}
    </div>,
    document.getElementById('portal-root')
  )
}
```

```jsx
import { useEffect } from "react";
import { createPortal } from "react-dom";

const Portal = ({children}) => {
  const mount = document.getElementById("portal-root");
  const el = document.createElement("div");

  useEffect(() => {
    mount.appendChild(el);
    return () => mount.removeChild(el);
  }, [el, mount]);

  return createPortal(children, el)
};

export default Portal;
```

```jsx
const App = () => {
  const [coords, setCoords] = useState({}); // takes current button coordinates
  const [isOn, setOn] = useState(false); // toggles button visibility

  return <Card style={{...styles.card, overflow: "hidden"}}> // [ 2 ]
      <Button
        onClick={e => {
          const rect = e.target.getBoundingClientRect();
          setCoords({
            left: rect.x + rect.width / 2,
            top: rect.y + window.scrollY
          });
          setOn(!isOn); // [ 3 ]
        }}
      >
        Click me
      </Button>
      {
        isOn &&
        <Portal>
          <TooltipPopover coords={coords}>
            <div>Awesome content that is never cut off by its parent container!</div>
          </TooltipPopover>
        </Portal>
      }
  </Card>
}
```

### 3. Creating our custom React Hook

```jsx
//file name: usePortal.js
// The complete breakdown of this code is in the comments
import { useState, useCallback, useEffect } from "react";
import ReactDOM from "react-dom";
const usePortal = (el) => {
  const [portal, setPortal] = useState({
    render: () => null,
    remove: () => null,
  });

  const createPortal = useCallback((el) => {
    //render a portal at the given DOM node:
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    //delete the portal from memory:
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  useEffect(() => {
    //if there is an existing portal, remove the new instance.
    //is prevents memory leaks
    if (el) portal.remove();
    //otherwise, create a new portal and render it
    const newPortal = createPortal(el);
    setPortal(newPortal);
    //when the user exits the page, delete the portal from memory.
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
export default usePortal; //link this Hook with the project
```

### 4. 处理事件传递

   通过 Portal 渲染的组件中的事件。事件冒泡和捕获如何在 Portal 中工作。

   In normal JavaScript code if an element is interacted with, for example a click event, that interaction will propagate up through the parent elements. We can see this in action by adding a click handler to the component outer div.

   Now whenever the button to open the modal is clicked the click event on the component div will fire since the click event will propagate up through the button element to its parent element and in the end **click** will be logged to the console.

   As we know from normal JavaScript this only works for elements that are children of the element with the click event listener. In our example with React portal, the modal is not a child of the component div since it is rendered to the document body and thus should not trigger the click event when clicked, but it does. This is because React uses the component hierarchy to determine propagation of events and the `Modal` component is a child of the component div in JSX.

   This is nice since when working with React you never have to worry about the actual DOM structure and only ever need to worry about the component structure when determining event propagation.

   1. 在普通JavaScript中，事件（例如点击事件）会从子元素传播到父元素，这是DOM事件传播的标准行为。
   2. 在React中，事件传播也遵循类似的模式，但是React使用组件层次结构而不是实际的DOM结构来确定事件如何传播。
   3. 使用React Portal时，如果一个组件将内容呈现到文档主体之外，例如模态框，它在组件层次结构上可能不是父组件的子组件。尽管它在DOM结构上不是子元素，但React仍然根据组件层次结构来处理事件传播。
   4. 这种行为是React的一种便利，因此无需担心实际的DOM结构，只需要关注组件层次结构，这简化了事件传播的处理。

   ```jsx
   function Modal({ isOpen, onClose, children }) {
     if (!isOpen) return null
     return ReactDOM.createPortal(
       <div className="modal">
         <button onClick={onClose}>Close</button>
         {children}
       </div>,
       document.body
     )
   }
   
   function Component() {
     const [open, setOpen] = useState(false)
     return (
       <div className="component" onClick={() => console.log("click")}>
         <button onClick={() => setOpen(true)}>Open Modal</button>
         <Modal isOpen={open} onClose={() => setOpen(false)}>
           Fancy Modal
         </Modal>
       </div>
     )
   }
   ```

### 5. 性能考虑

   - 探讨 Portal 的性能考虑，如何避免不必要的重新渲染和提高性能。
   - 讨论 React 16 版本引入的异步渲染和其对 Portal 的影响。

   Portal 在React中是强大的工具，但在使用它时需要考虑性能因素，特别是在处理大型应用或频繁更新的情况下。以下是一些有关Portal性能的考虑以及React 16版本引入的异步渲染对Portal的影响：

- Portal 的性能考虑：

   1. **不必要的重新渲染**：Portal 可能会导致组件重新渲染，尤其是在Portal内容发生变化时。为了避免不必要的重新渲染，可以使用React的`React.memo`或`shouldComponentUpdate`（对于类组件）来优化组件，以确保只在必要的情况下进行重新渲染。
   2. **避免频繁更新**：Portal内容的频繁更新可能会导致性能问题，特别是在需要大量重新渲染时。考虑使用状态管理工具（如Redux或Mobx）来管理Portal内容，以减少不必要的重新渲染。
   3. **事件处理和事件委托**：Portal中的事件处理需要谨慎处理。确保事件处理程序不会导致不必要的重新渲染。还可以使用事件委托技术，将事件处理程序附加到Portal容器上，而不是每个Portal子组件上。
   4. **内存泄漏**：如果Portal不被正确地清理，可能会导致内存泄漏。确保在不再需要Portal时卸载组件和事件处理程序。

- React 16 中的异步渲染对Portal的影响：

   React 16引入了异步渲染，其中渲染工作可以分成多个任务。这对Portal的性能和用户体验有一些积极影响：

   1. **更流畅的用户体验**：异步渲染可以使React更具响应性，因为在处理Portal时，React可以在主任务之外执行渲染工作，从而减少阻塞用户交互的情况。
   2. **性能优化**：异步渲染可以优化Portal的性能，尤其是在处理大量内容或频繁更新内容时。它可以确保渲染工作在适当的时机完成，而不会阻塞主线程。
   3. **并发模式**：React 18及以后版本引入了并发模式，可以进一步改进Portal的性能。它允许React在多个任务之间平衡渲染工作，以提供更好的性能。

   总之，Portal是处理复杂布局需求的重要工具，但需要注意性能方面的考虑。使用React的性能优化技巧，如`React.memo`、`shouldComponentUpdate`、事件委托以及合理的异步渲染，可以帮助避免性能问题并提高用户体验。异步渲染和未来的并发模式将进一步增强Portal的性能。

### 6. 处理全局状态

   嵌套 Portal、使用 React 的 Context API 传递数据。

   嵌套 Portal 和使用 React 的 Context API 传递数据是两个强大的功能，可以让你更灵活地组织你的组件树，同时在组件之间传递数据。以下是如何嵌套 Portal 和使用 Context API 来传递数据的示例：

   首先，假设你有一个 App 组件，它包含一个模态框和一些内容，你希望在模态框和内容之间传递数据：

   ```jsx
   jsxCopy code
   import React, { useState, useContext, createContext } from 'react';
   import { createPortal } from 'react-dom';
   
   // 创建一个 Context，用于在组件之间传递数据
   const MyContext = createContext();
   
   const Modal = ({ children }) => {
     return createPortal(
       <div className="modal">
         {children}
       </div>,
       document.getElementById('modal-root')
     );
   };
   
   const ModalContent = () => {
     const data = useContext(MyContext); // 使用 Context 获取数据
   
     return (
       <div className="modal-content">
         <p>{data}</p>
       </div>
     );
   };
   
   const App = () => {
     const [modalData, setModalData] = useState("Data from App Component");
   
     return (
       <MyContext.Provider value={modalData}>
         <div>
           <p>Some content in the main app</p>
           <Modal>
             <ModalContent />
           </Modal>
           <button onClick={() => setModalData("Updated Data")}>
             Update Modal Data
           </button>
         </div>
       </MyContext.Provider>
     );
   };
   
   export default App;
   ```

   在上面的示例中，我们首先创建了一个名为 `MyContext` 的 Context，然后在 `ModalContent` 组件中使用 `useContext` 钩子来获取数据。在 `App` 组件中，我们将数据放入 `MyContext.Provider` 中，这样在模态框中的 `ModalContent` 组件就能够访问到这些数据。

   这个示例演示了如何使用 Portal 和 Context API 在嵌套的组件之间传递数据，允许你在复杂的布局结构中更轻松地共享状态和信息。当你点击 "Update Modal Data" 按钮时，模态框中的内容会更新为新的数据，而不需要重新渲染整个页面。这显示了 Portal 和 Context API 的强大组合。


### refs

1. https://react.dev/reference/react-dom/createPortal
2. https://www.youtube.com/watch?v=LyLa7dU5tp8
3. https://blog.webdevsimplified.com/2019-12/how-to-use-react-portal/
4. https://blog.logrocket.com/learn-react-portals-example/

## 核心

- `React.Children`：提供了一些静态方法，用于操作React元素的子节点。
  - `React.Children.map(children, function[(thisArg)])`：对子元素逐个执行一个函数，并收集结果。
  - `React.Children.forEach(children, function[(thisArg)])`：对子元素逐个执行一个函数，不收集结果。
  - `React.Children.count(children)`：返回子元素的数量。
  - `React.Children.only(children)`：验证子元素只有一个，并返回它。
- `React.createRef()`：创建一个ref对象，用于引用组件或DOM元素。该对象可以通过`current`属性获取被引用的组件或DOM元素。
- `React.Component`：所有React组件的基类，提供了一些生命周期函数和其他方法。
- `React.PureComponent`：与`React.Component`类似，但提供了浅比较实现的`shouldComponentUpdate`方法，可以优化组件的性能。
- `React.memo()`：高阶组件，用于优化纯函数组件的性能。
- `React.cloneElement(element, [props], [...children])`：复制并返回一个新的React元素，带有新的props和children。如果原始元素带有ref属性，则也会被复制。
- `React.isValidElement(object)`：判断一个对象是否为React元素。
- `React.Suspense`：用于在等待异步组件加载时显示占位符组件，避免用户界面的闪烁。
  - `fallback`：必选属性，指定在异步组件加载完成前显示的占位符组件。
- `React.lazy()`：用于懒加载组件，返回一个可渲染的React组件。

## DOM

- `ReactDOM.render(element, container[, callback])`：将React元素渲染到指定的容器中。
- `ReactDOM.unmountComponentAtNode(container)`：从指定的容器中卸载React组件。
- `ReactDOM.createPortal(children, container)`：将React元素渲染到DOM树的另一个位置，跨越组件层级。
- `ReactDOM.findDOMNode(component)`：获取被引用组件的DOM元素。
- `ReactDOM.hydrate()`：与`ReactDOM.render()`类似，但是针对已经存在的页面，不会重新创建DOM结构。
- `ReactDOM.createRoot(container[, options])`：创建一个可交互的根节点，支持并发模式和批量更新。
- `ReactDOM.createBlockingRoot(container[, options])`：创建一个阻塞式的、可交互的根节点，不支持并发模式。

## 错误边界

- `componentDidCatch(error, info)`：生命周期函数，用于捕获渲染阶段中的JavaScript错误，并处理它们。

## Profiler

- `React.Profiler`：用于测量React组件的性能。
  - `onRender(id, phase, actualDuration, baseDuration, startTime, commitTime, interactions)`：用于记录一次组件的渲染时间和交互信息。

## 测试test delete

- `React.TestUtils`：提供了一些测试相关的工具函数，用于编写React组件的单元测试。
- `react-testing-library`：提供了一套通用的测试工具库，用于测试React组件的行为和交互。

```
Suspense ✅
lazy✅
新旧 Context ✅
错误边界 ✅
createPortal ✅
StrictMode
memo✅
cloneElement
isValidElement✅
flushSync
Profiler✅

React.Children✅
map✅
forEach✅
count✅
only✅
toArray
```

