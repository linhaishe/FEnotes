# useReducer

使用例子都在refs里，作者都写的很好，如果想要看写法和使用方式，可以参考refs的内容，忘记使用了的话记得看哈。

大概就是能把useState通过三个步骤转换成useReducer，两者的主要区别在于，useReducer更适合做复杂的状态的统一管理，useState适合做简单的状态的管理。

## what is useReducer

The `useReducer` Hook is used to store and update states, just like the `useState` Hook. It accepts a `reducer` function as its first parameter and the initial state as the second. `useReducer` returns an array that holds the current state value and a `dispatch` function to which you can pass an action and later invoke it. While this is similar to the pattern Redux uses, there are a few differences.

当组件中存在许多状态更新并分散在多个事件处理程序中时，会变得非常繁琐。对于这些情况，你可以将所有状态更新逻辑整合到组件外部，放在一个称为"reducer"的单一函数中。

It is common to see useState hook used for state management, However React also have another hook to manage component's state, Which is useReducer hook. In fact, useState is built on useReducer!

`const [state, dispatch] = useReducer(reducer, initialArg, init?)`

- Parameters 
  - reducer: The reducer function that specifies how the state gets updated. It must be pure, should take the state and action as arguments, and should return the next state. State and action can be of any types.
  - initialArg: The value from which the initial state is calculated. It can be a value of any type. How the initial state is calculated from it depends on the next init argument.
  - optional init: The initializer function that should return the initial state. If it’s not specified, the initial state is set to initialArg. Otherwise, the initial state is set to the result of calling init(initialArg).如果不传入第三个参数，则以第二个参数作为initial state,如果传入，则已第三个函数的返回值作为inital state.

<mark>the golden rules of Redux state management: the state should be updated by emitting actions. Never write directly to the state.</mark>

关于第三个参数：

Creating the initial state lazily
In programming, lazy initialization is the tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed.

As mentioned above, useReducer can accept a third parameter, which is an optional init function for creating the initial state lazily. It lets you extract logic for calculating the initial state outside of the reducer function, as seen below:

```js
const initFunc = (initialCount) => {
  if (initialCount !== 0) {
      initialCount=+0
  }
	return {count: initialCount};
}

// wherever our useReducer is located
const [state, dispatch] = useReducer(reducer, initialCount, initFunc);
```

## basic usage

```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  if (action.type === 'incremented_age') {
    return {
      age: state.age + 1
    };
  }
  throw Error('Unknown action.');
}

export default function Counter() {
  const [state, dispatch] = useReducer(reducer, { age: 42 });

  return (
    <>
      <button onClick={() => {
        dispatch({ type: 'incremented_age' })
      }}>
        Increment age
      </button>
      <p>Hello! You are {state.age}.</p>
    </>
  );
}
```

## when should i `useReducer()`

As stated above, The useReducer hook handles more complex logic regarding the state updates. So if you're state is a single `boolean`, `number`, or `string`, Then it's obvious to use useState hook. However if your state is an object (example: person's information) or an array (example: array of products ) useReducer will be more appropriate to use.

## `useState` vs. `useReducer`

1. `useState` 的底層其實是用 `useReducer` 做的

   [useState源码](https://github.com/facebook/react/blob/5f06576f51ece88d846d01abd2ddd575827c6127/packages/react-reconciler/src/ReactFiberHooks.js#L339)

2. 代码量：通常情况下，使用useState可以减少初始代码量。而使用useReducer，则需要编写一个reducer函数和派发actions的代码。然而，如果许多事件处理程序以类似的方式修改状态，useReducer可以帮助减少代码量。

3. 可读性：当状态更新较为简单时，useState非常易读。但是，当状态更新变得更加复杂时，它们可能会使组件代码变得臃肿，难以阅读。在这种情况下，useReducer可以将更新逻辑与事件处理程序的事件分开，从而提高代码的可读性。

4. 调试：当使用useState时，如果出现bug，很难确定哪里设置了错误的状态以及原因。而使用useReducer，你可以在reducer中添加console log来查看每个状态更新以及为什么发生（由于哪个action）。如果每个action都是正确的，你就知道错误在于reducer本身的逻辑。然而，你需要逐步执行比使用useState时更多的代码。

5. 测试：reducer是一个纯函数，不依赖于组件。这意味着你可以将其导出并单独进行隔离测试。虽然通常最好在更真实的环境中测试组件，但对于复杂的状态更新逻辑，可以通过断言你的reducer返回特定的状态来进行测试，以检查给定初始状态和action时的结果。

6. 个人偏好：有些人喜欢reducers，有些人不喜欢。这是可以理解的，这取决于个人偏好。你总是可以在useState和useReducer之间进行相互转换：它们是等价的！

7. [`useState` is a basic Hook](https://reactjs.org/docs/hooks-reference.html#basic-hooks) for managing simple state transformation, and [`useReducer` is an additional Hook](https://reactjs.org/docs/hooks-reference.html#additional-hooks) for managing more complex state logic.

## 如何写好reducer

1. Reducers必须是纯函数。

   类似于状态更新函数，reducers在渲染期间运行！（Actions在下一次渲染时排队执行。）这意味着reducers必须是纯函数——相同的输入始终产生相同的输出。它们不应发送请求、安排超时或执行任何副作用（影响组件外部的操作）。它们应该在不产生变异的情况下更新对象和数组。

2. 每个action描述了单个用户交互，即使这导致对数据进行多个更改。

   例如，如果用户在一个由reducer管理的包含五个字段的表单上按下“重置”按钮，与其分发五个单独的“设置字段”action，不如分发一个“重置表单”action更合理。如果在reducer中记录每个action，该日志应该足够清晰，让您能够重构交互或响应的发生顺序。这有助于调试！

## When not to use the useReducer Hook

Despite being able to use the `useReducer` Hook to handle complex state logic in our app, it’s important to note that there are some scenarios where a third-party state management library like [Redux may be a better option](https://blog.logrocket.com/why-use-redux-reasons-with-clear-examples-d21bffd5835/):

1. When your application needs a single source of truth
2. When you want a more predictable state
3. When state-lifting to the top-level component no longer suffices
4. When you need to persist state even after a page refresh

With all these benefits, it’s also worth noting that using a library like Redux, as opposed to using pure React with `useReducer`, comes with some tradeoffs. For example, Redux has a hefty learning curve that is minimized by [using Redux Toolkit](https://blog.logrocket.com/smarter-redux-redux-toolkit/), and it’s definitely not the fastest way to write code. Rather, it’s intended to give you an absolute and predictable way of managing state in your app.

## Bailing out of a dispatch（放弃调度
If the useReducer Hook returns the same value as the current state, React will bail out without rendering the children or firing effects because it uses the Object.is comparison algorithm.

如果`useReducer` Hook返回的值与当前状态相同，React将会中止渲染子组件或触发副作用，这是因为React使用了`Object.is`比较算法。

"Bailing out of a dispatch"的中文翻译是"放弃调度"。在React中，当使用`useReducer` Hook时，如果在dispatch一个action后，reducer函数返回的新状态与当前状态相同（使用`Object.is`比较算法进行比较），React会放弃对组件的重新渲染和触发副作用，以避免不必要的更新。这样的优化称为"放弃调度"。

## Recap

- To convert from `useState` to `useReducer`
  1. Dispatch actions from event handlers.
  2. Write a reducer function that returns the next state for a given state and action.
  3. Replace `useState` with `useReducer`.
- Reducers require you to write a bit more code, but they help with debugging and testing.
- Reducers must be pure.
- Each action describes a single user interaction.
- Use Immer if you want to write reducers in a mutating style.

## refs:

1. https://react-hooks-cheatsheet.com/usereducer
2. [React Hooks | 既生 useState 何生 useReducer ?](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/react-hooks-usestate-vs-usereducer-b14966ad37dd)
3. [useState vs useReducer: What are they and when to use them?](https://dev.to/m0nm/usestate-vs-usereducer-what-are-they-and-when-to-use-them-2c5c)
4. [A guide to the React useReducer Hook](https://blog.logrocket.com/react-usereducer-hook-ultimate-guide/#usestate-vs-usereducer)
5. [Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer#comparing-usestate-and-usereducer)
6. [useReducer](https://react.dev/reference/react/useReducer)