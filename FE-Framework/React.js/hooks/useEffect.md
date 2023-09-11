# useEffect

> `useEffect` is a React Hook that lets you [synchronize a component with an external system.](https://react.dev/learn/synchronizing-with-effects)

```js
useEffect(
    () => {
        // execute side effect
      
    // return optional function for cleanup
    // in this case acts like componentWillUnmount
      return () => {};
    },
    // optional dependency array
    [ ] // 0 or more entries 
)
```

```jsx
import { useEffect } from 'react';
import { createConnection } from './chat.js';

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [serverUrl, roomId]);
  // ...
}
```

## The key concepts of using effects

What are the effects, really? Examples are:

- Fetching data
- Reading from local storage
- Registering and deregistering event listeners

- You must thoroughly understand when components (re-)render because effects run after every render cycle
- You should ensure that components are not re-rendered unnecessarily. This constitutes another strategy to skip unnecessary reruns of effects.
- You have to understand that functions defined in the body of your function component get recreated on every render cycle. This has an impact if you use it inside of your effect. There are strategies to cope with it (hoist them outside of the component, define them inside of the effect, use `useCallback`)
- You have to understand basic JavaScript concepts such as [stale closures](https://dmitripavlutin.com/react-hooks-stale-closures/), otherwise, you might have trouble tackling problems with outdated props or state values inside of your effect. There are strategies to solve this, e.g., with an effect’s dependency array or with the [`useRef`](https://blog.logrocket.com/react-reference-guide-hooks-api/#useref) Hook

> - 获取数据
> - 从本地存储中读取数据
> - 注册和注销事件监听器
> - 您必须充分了解组件何时（重新）渲染，因为效果在每个渲染周期后运行。
> - 您应该确保组件不会不必要地重新渲染。这构成了跳过不必要的效果重新运行的另一种策略。
> - 您必须了解，函数在函数组件的主体中定义时，会在每次渲染周期都重新创建。如果在效果内部使用它，这会产生影响。有一些策略可以处理这个问题（将它们移到组件外部，将它们定义在效果内部，使用 `useCallback` 等）。
> - 您必须了解基本的 JavaScript 概念，比如[陈旧闭包（stale closures）](https://dmitripavlutin.com/react-hooks-stale-closures/)，否则，您可能会在效果内部遇到使用过时的属性或状态值的问题。有一些策略可以解决这个问题，例如使用效果的依赖数组或 [`useRef`](https://blog.logrocket.com/react-reference-guide-hooks-api/#useref) Hook。

> The question is not ‘when does this effect run,’ the question is ‘with which state does this effect synchronize?’ ”
> – Ryan Florence

## Using `useEffect` for asynchronous tasks

advantages:

1. writing asynchronous code without `useEffect` that might block the UI
2.  developers can easily [overview the code](https://medium.com/better-programming/understanding-the-useeffect-dependency-array-2913da504c44) and quickly recognize code that is executed “outside the control flow,” which becomes relevant only after the first render cycle.

Don’t be afraid to use multiple `useEffect` statements in your component.

## useEffect executed within the component lifecycle

effects defined with useEffect are invoked after render. To be more specific, it runs both after the first render and after every update.

according to this [diagram](https://wavez.github.io/react-hooks-lifecycle/): 

![image-20230716155801286](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/hooks/image-20230716155801286.png)

## The useEffect control flow

 The following steps are carried out for a functional React component if at least one effect is defined:

1. The component will be re-rendered based on a state, prop, or context change
2. If one or more `useEffect` declarations exist for the component, React checks each `useEffect` to determine whether it fulfills the conditions to execute the implementation (the body of the callback function provided as first argument). In this case, “conditions” mean one or more dependencies have changed since the last render cycle

Dependencies are array items provided as the optional second argument of the `useEffect` call. Array values must be from the component scope (i.e., props, state, context, or values derived from the aforementioned):

1. After the execution of every effect, scheduling of new effects occurs based on every effect’s dependencies. If an effect does not specify a dependency array at all, it means that this effect is executed after every render cycle.
2. [Cleanup](https://blog.logrocket.com/understanding-react-useeffect-cleanup-function/) is an optional step for every effect if the body of the `useEffect` callback function (first argument) returns a so-called “cleanup callback function.” In this case, <mark>the cleanup function gets invoked before the execution of the effect, beginning with the second scheduling cycle. This also means that if there is no second execution of an effect scheduled, the cleanup function is invoked before the React component gets destroyed.</mark>

> 如果一个功能性的React组件定义了至少一个effect，将会执行以下步骤：
>
> 1. 组件将会根据状态（state）、属性（props）或上下文（context）的变化而重新渲染。
> 2. 如果组件存在一个或多个`useEffect`声明，React将检查每个`useEffect`以确定它是否满足执行实现的条件（作为第一个参数提供的回调函数体）。在这种情况下，“条件”意味着自上次渲染周期以来至少有一个依赖项发生了变化。
>
> 依赖项是作为`useEffect`调用的可选第二个参数提供的数组项。数组中的值必须来自组件作用域（例如，props、state、context或从前述内容派生的值）：
>
> 1. 在每个effect执行后，基于每个effect的依赖项，将调度新的effects。如果一个effect根本没有指定依赖项数组，这意味着该effect会在每次渲染周期后执行。
> 2. [清理](https://blog.logrocket.com/understanding-react-useeffect-cleanup-function/)是每个effect的可选步骤，如果`useEffect`的回调函数体（第一个参数）返回一个所谓的“清理回调函数”。在这种情况下，清理函数会在执行effect之前调用，从第二个调度周期开始。这也意味着，如果没有安排第二次执行effect，清理函数会在React组件被销毁之前被调用。

## Dependencies array

What items should be included in the dependency array? According to the [React docs](https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects), you must include all values from the component scope that change their values between re-renders.

All external values referenced inside of the `useEffect` callback function, <mark>such as props, state variables, or context variables</mark>, are dependencies of the effect.

React only executes the `useEffect` statement if at least one of the provided dependencies has changed since the previous run. In other words, with the dependency array, you make the execution dependent on certain conditions.

React仅在自上次运行以来提供的依赖项中至少有一个发生变化时才执行`useEffect`语句。换句话说，通过依赖项数组，您可以使执行取决于特定条件。

It’s also possible to add an empty dependency array. In this case, effects are only executed once; 

==empty array:== empty array as our second argument. the effect is only executed once after the first render and skipped for the following render cycles.

==missing array:==  `useEffect` statement is executed whenever one of the state variables change.

Remember that if at least one of the dependencies in the array is different from the previous render, the effect will be rerun.

## cleanup functions 

cleanup functions are not only invoked before destroying the React component. An effect’s cleanup function gets invoked every time right before the execution of the next scheduled effect.

清理函数不仅在销毁React组件之前被调用。在下一个预定的effect执行之前，清理函数将在每次执行之前被调用。

effects are scheduled after every render cycle.

## When not to use `useEffect`

1. Transforming data for rendering

   If you need to transform data before rendering, then you don’t need useEffect.直接在useeffect函数外部进行处理，或直接对数据处理，不需要用到useEffect

2. Handling user events

3. If you’re not connecting to any external system, you probably don’t need an Effect.

More detail in [here](https://blog.logrocket.com/useeffect-hook-complete-guide/#when-not-use-useeffect)

## refs

1. [useEffect - react dev](https://react.dev/reference/react/useEffect)

2. [A complete guide to the `useEffect` React Hook](https://blog.logrocket.com/useeffect-hook-complete-guide/)

*For more information on React Hooks, check out this [cheat sheet](https://blog.logrocket.com/react-hooks-cheat-sheet-unlock-solutions-to-common-problems-af4caf699e70/).*