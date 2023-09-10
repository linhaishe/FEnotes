# useContent

stackblitz: https://stackblitz.com/edit/stackblitz-starters-k2dpsv?file=src%2FApp.tsx

# what is useContent

React Context is a way to manage state globally.a useful hook that allows components to access data without the need to rely on props.

It can be used together with the `useState` Hook to share state between deeply nested components more easily than with `useState` alone.

React Hooks aim to solve the difficulties of logic reuse (逻辑重用的困难) by enabling us to write components that have access to features like state, context, lifecycle methods, ref, etc. 

> React Context 是一种全局管理状态的方式，它是一个有用的钩子，允许组件访问数据，而无需依赖于 props。
>
> 它可以与 `useState` 钩子一起使用，以比仅使用 `useState` 更容易地在深度嵌套的组件之间共享状态。
>
> React Hooks 旨在通过使我们能够编写具有访问状态、上下文、生命周期方法、引用等功能的组件，来解决逻辑重用的困难。

----

problem

State should be held by the highest parent component in the stack that requires access to the state.

To illustrate, we have many nested components. The component at the top and bottom of the stack need access to the state.

To do this without Context, we will need to pass the state as "props" through each nested component. This is called "prop drilling".

> 状态应该由需要访问该状态的堆栈中的最顶层父组件来维护。
>
> 举个例子，我们有许多嵌套的组件。堆栈的顶部和底部的组件都需要访问状态。
>
> 如果不使用上下文（Context）来实现这一点，我们将需要通过每个嵌套组件将状态作为“props”传递。这被称为“prop drilling”（props钻取）。

# how to use

Using the context in React requires 3 simple steps: ==*creating*== the context,==*providing*== the context, and ==*consuming*== the context.

## creating the context

```jsx
// context.js
import { createContext } from 'react';

export const Context = createContext('Default Value');
```

==The factory function accepts one optional argument: the default value.==

If the consumer isn't wrapped inside the provider, but still tries to access the context value (using useContext(Context) or <Context.Consumer>), then the value of the context would be the default value argument supplied to createContext(defaultValue) factory function that had created the context.

## providing the context

`Context.Provider` component available on the context instance is used to provide the context to its child components, no matter how deep they are.

```jsx
import { Context } from './context';

function Main() {
  const value = 'My Context Value';
  return (
    <Context.Provider value={value}>
      <MyComponent />
    </Context.Provider>
  );
}
```

all the components that'd like later to consume the context have to be wrapped inside the provider component.

## consuming the context
### 1. use hooks(recommend)

```jsx
import { useContext } from 'react';
import { Context } from './context';

function MyComponent() {
  const value = useContext(Context);

  return <span>{value}</span>;
}
```

### 2. use Context.Consumer

```jsx
import { Context } from './context';

function MyComponent() {
  return (
    <Context.Consumer>
      {value => <span>{value}</span>}
    </Context.Consumer>
  );
}
```

==If the consumerisn't wrapped inside the provider==, but still tries to access the context value (using useContext(Context) or <Context.Consumer>),then the value of the context would be the default value argument supplied to createContext(defaultValue) factory function that had created the context.

# when do you need

## pros

The main idea of using the context is to allow your components to access global data and re-render when that global data is changed. Context solves the [props drilling problem](https://kentcdodds.com/blog/prop-drilling): when you have to pass down props from parents to children.

You can hold inside the context:

- global state
- theme
- application configuration
- authenticated user name
- user settings
- preferred language
- a collection of services


## cons

On the other side, you should think carefully before deciding to use context in your application.

First, ==integrating the context adds complexity.== Creating a context, wrapping everything in a provider, and using the `useContext()` in every consumer — increases complexity.

Secondly, ==adding context complicates unit testing of components.== During testing, you'll have to wrap the consumer components into a context provider. Including the components that are indirectly affected by the context — the ancestors of context consumers!

#### Caveats 

- `useContext()` call in a component is not affected by providers returned from the *same* component. The corresponding `<Context.Provider>` **needs to be \*above\*** the component doing the `useContext()` call.
- React **automatically re-renders** all the children that use a particular context starting from the provider that receives a different `value`. The previous and the next values are compared with the [`Object.is`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is) comparison. Skipping re-renders with [`memo`](https://react.dev/reference/react/memo) does not prevent the children receiving fresh context values.
- If your build system produces duplicates modules in the output (which can happen with symlinks), this can break context. Passing something via context only works if `SomeContext` that you use to provide context and `SomeContext` that you use to read it are ***exactly\* the same object**, as determined by a `===` comparison.

> - 在组件中使用 `useContext()` 不受同一组件返回的提供者的影响。相应的 `<Context.Provider>` **需要位于** 执行 `useContext()` 调用的组件之上。
> - React 会**自动重新渲染**使用特定上下文的所有子组件，从接收到不同 `value` 的提供者开始。之前和之后的值会使用 [`Object.is`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is) 比较进行比较。使用 [`memo`](https://react.dev/reference/react/memo) 跳过重新渲染不会阻止子组件接收新的上下文值。
> - 如果您的构建系统在输出中生成重复的模块（这可能会在符号链接中发生），这可能会破坏上下文。仅通过上下文传递内容仅在用于提供上下文的 `SomeContext` 和用于读取它的 `SomeContext` ***完全相同的对象** 的情况下有效，这由 `===` 比较确定。

# Conclusion

The context in React lets you supply child components with global data, no matter how deep they are in the components tree.

Using the context requires 3 steps: creating, providing, and consuming the context.

When integrating the context into your application, consider that it adds a good amount of complexity. Sometimes drilling the props through 2-3 levels in the hierarchy isn't a big problem.

At any time we want to have client data be available within a large number of React components, we should think of leveraging the Context API and the useContext hook.

# refs

1. [A Guide to React Context and useContext() Hook](https://dmitripavlutin.com/react-context-and-usecontext/)
2. [useContext](https://react.dev/reference/react/useContext)
3. [The React useContext Hook](https://www.telerik.com/blogs/react-usecontext-hook)
4. [React Hooks vs. Redux: Do Hooks and Context replace Redux?](https://blog.logrocket.com/react-hooks-vs-redux-hooks-context-replace-redux/)













