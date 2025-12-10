# useCallback & useMemo

## useCallBack

demo stackblitz: https://stackblitz.com/edit/stackblitz-starters-rcrmbp?file=src%2FApp.tsx

`useCallback` is a React Hook that lets you cache a function definition between re-renders(重复渲染).

These Hooks help developers improve the rendering performance of components, preserve objects between React component renderings, and help improve application performance.

```js
const cachedFn = useCallback(fn, dependencies)
```

### Parameters 
`fn:` The function value that you want to cache. It can take any arguments and return any values. React will return (not call!) your function back to you during the initial render. On next renders, React will give you the same function again if the dependencies have not changed since the last render. Otherwise, it will give you the function that you have passed during the current render, and store it in case it can be reused later. React will not call your function. The function is returned to you so you can decide when and whether to call it.

`dependencies:`The list of all reactive values referenced inside of the fn code. Reactive values include props, state, and all the variables and functions declared directly inside your component body. If your linter is configured for React, it will verify that every reactive value is correctly specified as a dependency. The list of dependencies must have a constant number of items and be written inline like [dep1, dep2, dep3]. React will compare each dependency with its previous value using the Object.is comparison algorithm.

```jsx
import { memo, useState } from "react";
import "./styles.css";

const Numbers = memo(({ nums, addRandom }) => {
  console.log("Numbers rendered");

  return (
    <div>
      <ul>
        {nums.map((num, i) => (
          <li key={i}>{num}</li>
        ))}
      </ul>
      <button onClick={addRandom}>Add random</button>
    </div>
  );
});

export default function App() {
  const [nums, setNums] = useState([]);
  const [count, setCount] = useState(0);

  const increaseCounter = () => {
    setCount(count + 1);
  };

  const addRandom = () => {
    let randNum = parseInt(Math.random() * 1000, 10);
    setNums([...nums, randNum]);
  };

  return (
    <div>
      <div>
        Count: {count} &nbsp;
        <button onClick={increaseCounter}>+</button>
      </div>
      <hr />
      <Numbers nums={nums} addRandom={addRandom} />
    </div>
  );
}
```

父组件内，button的点击，使子组件在props没有更新的情况下触发重复渲染。

The reason is that whenever the App component re-renders, it re-creates a function reference for the addRandom callback. The Numbers component gets re-rendered since the props are different!

原因是每当 App 组件重新渲染时，它都会为 addRandom 回调重新创建一个函数引用。由于props不同，Numbers 组件会重新渲染

```js
const addRandom = useCallback(() => {
  let randNum = parseInt(Math.random() * 1000, 10);
  setNums([...nums, randNum]);
}, [nums]);
```

==useCallback第二个参数，设置为空数组会有什么影响==

在 React 中，`useCallback` 是用来优化函数的 hook。它会返回一个记忆化的版本函数，只有当指定的依赖项发生变化时才会重新创建。如果传入的第二个参数是一个 空数组，后续的渲染，只会记住第一次渲染的。

第二个参数是一个依赖数组，用于指定在依赖项发生变化时重新创建回调函数。如果将第二个参数设置为空数组 `[]`，则表示回调函数不依赖任何值，即它在组件的整个生命周期中保持不变。

设置为空数组作为第二个参数会有以下影响：

1. **回调函数不会重新创建**: 因为没有任何依赖项，所以回调函数只会在组件首次渲染时创建一次，并在后续重新渲染中保持不变。这可以节省性能，特别是当回调函数被作为 prop 传递给子组件时，可以避免不必要的重复渲染。
2. **无法响应依赖项变化**: 如果某些依赖项的状态发生变化，由于回调函数不会重新创建，它将无法捕捉到这些变化。这意味着回调函数内部的逻辑可能无法正确地响应依赖项的变化。因此，当确信回调函数不依赖任何值时，才应该将第二个参数设置为空数组。

总结：将第二个参数设置为空数组可以优化性能，避免不必要的函数重新创建，但也会导致回调函数无法感知依赖项的变化。因此，在使用 `useCallback` 时，需要根据具体情况权衡利弊，确保选择正确的依赖项来实现预期的行为。

[What's the difference between `useCallback` with an empty array as inputs and `useCallback` without a second parameter?](https://stackoverflow.com/questions/55026139/whats-the-difference-between-usecallback-with-an-empty-array-as-inputs-and-u)

==如果不传入，会报错啦且没有用。==

If the second argument is omitted, the value will never be memoized, and the `useCallback` and the `useMemo` doesn't do anything.

## useMemo

demo stackblitz: https://stackblitz.com/edit/stackblitz-starters-ygxwdj?file=src%2FApp.tsx

`useMemo` is a React Hook that lets you cache the result of a calculation between re-renders.

The `useMemo` Hook typically returns a cached value until a dependency gets changed. 

`const cachedValue = useMemo(calculateValue, dependencies)`

`useMemo(() => calculateMagicNumber(count), [count]);`

```jsx
import { useState } from "react";
import "./styles.css";
export default function App() {
  const [nums, setNums] = useState([]);
  const [count, setCount] = useState(1);
  const increaseCounter = () => {
    setCount(count + 1);
  };
  const addRandom = () => {
    let randNum = parseInt(Math.random() * 1000, 10);
    setNums([...nums, randNum]);
  };
  const magicNum = calculateMagicNumber(count);
  return (
    <div>
      <div>
        Counter: {count} | Magic number: {magicNum} &nbsp;
        <button onClick={increaseCounter}>+</button>
      </div>
      <hr />
      <div>
        <ul>
          {nums.map((num, i) => (
            <li key={i}>{num}</li>
          ))}
        </ul>
        <button onClick={addRandom}>Add random</button>
      </div>
    </div>
  );
}
function calculateMagicNumber(n) {
  console.log("Costly calculation triggered.");
  let num = 1;
  for (let i = 0; i < n + 1000000000; i++) {
    num += 123000;
  }
  return parseInt(num - num * 0.22, 10);
}
```

The reason is that the Add random button also triggers a mandatory re-render which triggers the `calculateMagicNumber` slow function. 

```jsx
const magicNum = useMemo(() => calculateMagicNumber(count), [count]);
```

## diffs

两者 cons: Excessive usage can lead to memory-related performance issues

过度使用（指在代码中频繁或不必要地使用）可能会导致与内存相关的性能问题。在编程中，如果某个功能或方法被过度使用，可能会造成内存占用过大，导致程序运行变慢，甚至出现内存泄漏等问题。因此，开发者在编写代码时应该注意避免不必要的内存消耗和资源浪费，以确保程序的性能和稳定性。

| `useCallback` pros                                           | `useCallback` cons                                           |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Helps developers cache a function to avoid excessive re-renders of a child component | Adds excessive syntax for callback definition, so use of `useCallback` may complicate your code |
| Developers can improve the use of `memo` built-in’s performance enhancements (See the previous example) | Cannot be used to efficiently and properly cache a value as `useMemo` |
| Comes as an inbuilt, stable React core feature that we can use in production | The usage of this Hook may confuse React newcomers since it caches a function — not a simple value |
| Offers an easy function interface that accepts just two parameters: a function and dependencies array | Excessive usage can lead to memory-related performance issues |

| 优点                                                     | 缺点                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| 帮助开发者缓存函数以避免子组件过度重新渲染               | 添加大量的语法用于回调函数定义，使用`useCallback`可能会使代码复杂化 |
| 开发者可以提高`memo`内置性能优化的使用                   | 不能高效地和正确地缓存一个值，像`useMemo`那样                |
| 是内置的、稳定的React核心特性，可以在生产环境中使用      | 对于React新手来说，使用这个Hook可能会产生困惑，因为它缓存的是一个函数，而不是一个简单的值 |
| 提供了简单的函数接口，只需要两个参数：一个函数和依赖数组 | 过度使用可能导致与内存相关的性能问题                         |

| `useMemo` pros                                               | `useMemo` cons                                               |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Helps developers cache a value to avoid unwanted costly recalculations | Adds excessive syntax for compute function calls, so use of `useMemo` may complicate your code |
| Able to use with inbuilt `memo` when a child component uses a computed object that doesn’t need frequent re-computations | Can be used to cache a function, but it affects readability (Use `useCallback` for caching functions) |
| Comes as an inbuilt, stable React core feature that we can use in production | React newcomers may use this Hook for situations where caching isn’t needed, such as with simple calculations, frequently changed values, etc. As a result, code readability and app memory usage will get affected |
| Offers an easy function interface that accepts just two parameters: a function and dependencies array | Excessive usage can lead to memory-related performance issues |

| 优点                                                         | 缺点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 帮助开发者缓存值以避免不必要的昂贵计算                       | 添加大量的语法用于计算函数调用，使用`useMemo`可能会使代码复杂化 |
| 当子组件使用计算出的对象且不需要频繁重新计算时，可以与内置memo一起使用 | 可以用来缓存函数，但会影响代码的可读性（对于缓存函数，请使用`useCallback`） |
| 是内置的、稳定的React核心特性，可以在生产环境中使用          | React新手可能会在不需要缓存的情况下使用这个Hook，例如简单计算、频繁变化的值等，导致代码可读性和内存使用受到影响 |
| 提供了简单的函数接口，只需要两个参数：一个函数和依赖数组     | 过度使用可能导致与内存相关的性能问题                         |

## refs

1. [useCallback](https://react.dev/reference/react/useCallback)
2. [React useMemo vs. useCallback: A pragmatic guide](https://blog.logrocket.com/react-usememo-vs-usecallback/)
3. [How to useMemo and useCallback: you can remove most of them](https://www.developerway.com/posts/how-to-use-memo-use-callback)
4. [useMemo](https://react.dev/reference/react/useMemo)
