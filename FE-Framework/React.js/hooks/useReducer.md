# useReducer

当组件中存在许多状态更新并分散在多个事件处理程序中时，会变得非常繁琐。对于这些情况，你可以将所有状态更新逻辑整合到组件外部，放在一个称为"reducer"的单一函数中。

It is common to see useState hook used for state management, However React also have another hook to manage component's state, Which is useReducer hook. In fact, useState is built on useReducer!

## 1. when should i useReducer()

As stated above, The useReducer hook handles more complex logic regarding the state updates. So if you're state is a single `boolean`, `number`, or `string`, Then it's obvious to use useState hook. However if your state is an object (example: person's information) or an array (example: array of products ) useReducer will be more appropriate to use.

## 2. diff with useState

1. `useState` 的底層其實是用 `useReducer` 做的

   [useState源码](https://github.com/facebook/react/blob/5f06576f51ece88d846d01abd2ddd575827c6127/packages/react-reconciler/src/ReactFiberHooks.js#L339)

2. 代码量：通常情况下，使用useState可以减少初始代码量。而使用useReducer，则需要编写一个reducer函数和派发actions的代码。然而，如果许多事件处理程序以类似的方式修改状态，useReducer可以帮助减少代码量。

3. 可读性：当状态更新较为简单时，useState非常易读。但是，当状态更新变得更加复杂时，它们可能会使组件代码变得臃肿，难以阅读。在这种情况下，useReducer可以将更新逻辑与事件处理程序的事件分开，从而提高代码的可读性。

4. 调试：当使用useState时，如果出现bug，很难确定哪里设置了错误的状态以及原因。而使用useReducer，你可以在reducer中添加console log来查看每个状态更新以及为什么发生（由于哪个action）。如果每个action都是正确的，你就知道错误在于reducer本身的逻辑。然而，你需要逐步执行比使用useState时更多的代码。

5. 测试：reducer是一个纯函数，不依赖于组件。这意味着你可以将其导出并单独进行隔离测试。虽然通常最好在更真实的环境中测试组件，但对于复杂的状态更新逻辑，可以通过断言你的reducer返回特定的状态来进行测试，以检查给定初始状态和action时的结果。

6. 个人偏好：有些人喜欢reducers，有些人不喜欢。这是可以理解的，这取决于个人偏好。你总是可以在useState和useReducer之间进行相互转换：它们是等价的！

## 3. 如何写好reducer

1. Reducers必须是纯函数。

   类似于状态更新函数，reducers在渲染期间运行！（Actions在下一次渲染时排队执行。）这意味着reducers必须是纯函数——相同的输入始终产生相同的输出。它们不应发送请求、安排超时或执行任何副作用（影响组件外部的操作）。它们应该在不产生变异的情况下更新对象和数组。

2. 每个action描述了单个用户交互，即使这导致对数据进行多个更改。

   例如，如果用户在一个由reducer管理的包含五个字段的表单上按下“重置”按钮，与其分发五个单独的“设置字段”action，不如分发一个“重置表单”action更合理。如果在reducer中记录每个action，该日志应该足够清晰，让您能够重构交互或响应的发生顺序。这有助于调试！

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

1. [React Hooks | 既生 useState 何生 useReducer ?](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/react-hooks-usestate-vs-usereducer-b14966ad37dd)
2. [useState vs useReducer: What are they and when to use them?](https://dev.to/m0nm/usestate-vs-usereducer-what-are-they-and-when-to-use-them-2c5c)
3. [A guide to the React useReducer Hook](https://blog.logrocket.com/react-usereducer-hook-ultimate-guide/#usestate-vs-usereducer)
4. [Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer#comparing-usestate-and-usereducer)
5. [useReducer](https://react.dev/reference/react/useReducer)