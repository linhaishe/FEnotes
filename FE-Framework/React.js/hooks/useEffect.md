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

## Dependencies array

What items should be included in the dependency array? According to the [React docs](https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects), you must include all values from the component scope that change their values between re-renders.

All external values referenced inside of the `useEffect` callback function, <mark>such as props, state variables, or context variables</mark>, are dependencies of the effect.

React only executes the `useEffect` statement if at least one of the provided dependencies has changed since the previous run. In other words, with the dependency array, you make the execution dependent on certain conditions.

React仅在自上次运行以来提供的依赖项中至少有一个发生变化时才执行`useEffect`语句。换句话说，通过依赖项数组，您可以使执行取决于特定条件。

It’s also possible to add an empty dependency array. In this case, effects are only executed once; 

empty array: empty array as our second argument. the effect is only executed once after the first render and skipped for the following render cycles.

missing array:  `useEffect` statement is executed whenever one of the state variables change.

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

[useEffect - react dev](https://react.dev/reference/react/useEffect)

[A complete guide to the `useEffect` React Hook](https://blog.logrocket.com/useeffect-hook-complete-guide/)

*For more information on React Hooks, check out this [cheat sheet](https://blog.logrocket.com/react-hooks-cheat-sheet-unlock-solutions-to-common-problems-af4caf699e70/).*