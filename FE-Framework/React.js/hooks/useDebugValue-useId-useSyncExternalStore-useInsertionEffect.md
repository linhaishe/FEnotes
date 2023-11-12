# useDebugValue

## defiend

`useDebugValue`的作用是，将你需要关心的变量动态地与其他同域变量一起显示在`DevTools`面板中，其体验，明显优于`console.log`。

`useDebugValue`适用于：调试（输出）自定义 Hook 中用到的状态值。

大家通常使用`console.log`来输出一些中间变量，并在浏览器的`console`面板中查看。

而`useDebugValue`的优势在于，用`useDebugValue`输出的值，是和 DevTools 中的 Hook 状态一起动态显示的，不需要在 DevTools 和 Console 面板中切换查看 Hook 状态和`console.log`输出。

```js
import { useEffect, useDebugValue, useState } from 'react';

export const useFetch = (url) => {
  useDebugValue(url);
  const [response, setResponse] = useState([]);
  const clown = '🤡';
  useDebugValue(`crazy ${clown}`);
  const [error, setError] = useState(null);
  const [httpResponse, setHttpResponse] = useState();
  useDebugValue(
    httpResponse ? 'status code ' + httpResponse.status : 'no response'
  );
  useDebugValue(error, (e) =>
    e ? `fetch failed due to ${e.message}` : 'fetch successful'
  );
  useEffect(() => {
    async function fetchFiles() {
      try {
        const response = await fetch(url);
        setHttpResponse(response);
        const json = await response.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    }
    fetchFiles();
  }, [setError, setResponse, url]);
  useDebugValue(response, (mp3s) =>
    mp3s.length > 0 ? mp3s.map((mp3) => mp3.label) : 'no mp3s loaded'
  );
  return [response, error];
};
```

1. 一切都有代价：使用 useDebugValue 在生产代码中频繁调用可能会对应用程序的性能产生负面影响。
2. 不建议在生产代码中保留 useDebugValue，但官方文档提到，可以在共享库中的自定义 Hooks 代码中留下它可能是可以接受的。
3. 我们目前无法根据环境变量有条件地渲染 useDebugValue，因为 Hooks 规则不允许在条件代码中调用 Hook。
4. useDebugValue 是另一种工具，只在开发自定义 Hooks 时使用它，并在将 Hook 推送到 Git 存储库之前将其删除。它确实是传统的 console.log 调用和调试断点的替代选择。

## refs

1. [Improve custom Hook debugging with `useDebugValue`](https://blog.logrocket.com/improve-custom-hook-debugging-with-usedebugvalue/)
2. [React Hooks 之 useDebugValue - 代替 console.log 来调试 Hook](https://segmentfault.com/a/1190000042535705)
3. https://blog.webdevsimplified.com/2021-11/use-debug-value/
4. https://react.dev/reference/react/useDebugValue

# useId

`useId` is a React Hook for generating unique IDs that can be passed to accessibility attributes.

```js
import { useId } from 'react';

function PasswordField() {
  const passwordHintId = useId();
  // ...
```

Caveats

1. useId is a Hook, so you can only call it at the top level of your component or your own Hooks. You can’t call it inside loops or conditions. If you need that, extract a new component and move the state into it.

2. useId should not be used to generate keys in a list. Keys should be generated from your data.

list 里的 keys，服务端并不会返回唯一的 key，也只能在组件外部生成唯一 key，针对因为 keys 的问题，出现图片留在页面上，但其实已经是别的图片了，因为 keys 没更新。

## refs

1. https://juejin.cn/post/7148349754789855239
2. https://react.dev/reference/react/useId
3. https://medium.com/@hetdesai03/a-complete-guide-to-useid-hook-in-react-18-22119ecfd87f
4. https://www.geeksforgeeks.org/reactjs-useid-hook/
5. https://webtips.dev/webtips/react-hooks/useid
6. https://blog.webdevsimplified.com/2022-06/use-id/

# useSyncExternalStore

The useSyncExternalStore is a custom hook available in React 18, that lets you subscribe to an external store and update your React component when the external store updates.

It is especially useful in subscribing to external stores that are not built on top of React state management.

```
import { useSyncExternalStore } from 'react';
import { todosStore } from './todoStore.js';

function TodosApp() {
  const todos = useSyncExternalStore(todosStore.subscribe, todosStore.getSnapshot);
  // ...
}
```

It returns the snapshot of the data in the store. You need to pass two functions as arguments:

1. The subscribe function should subscribe to the store and return a function that unsubscribes.
2. The getSnapshot function should read a snapshot of the data from the store.

## refs

1. https://milkmidi.medium.com/react-18-usesyncexternalstore-a427bf82c198
2. https://medium.com/@mrovinsky/how-to-use-usesyncexternalstore-a9926f8c7e60
3. https://deadsimplechat.com/blog/usesyncexternalstore-in-react/ 🌟🌟🌟🌟🌟
4. https://react.dev/reference/react/useSyncExternalStore#usesyncexternalstore
5. https://www.zhihu.com/question/502917860
6. https://lo-victoria.com/a-look-at-react-hooks-usesyncexternalstore
7. https://juejin.cn/post/7056588815170813965
8. https://blog.saeloun.com/2021/12/30/react-18-useSyncExternalStore-api/

# useInsertionEffect

Call `useInsertionEffect` to insert styles before any effects fire that may need to read layou

该签名与 useEffect 相同，但它在所有 DOM 突变之前同步触发。使用它在读取 useLayoutEffect 中的布局之前将样式注入 DOM。由于这个 hook 的作用域有限，所以这个 hook 不能访问 refs，也不能安排更新。
useInsertionEffect 应仅限于 css-in-js 库作者使用。优先考虑使用 useEffect 或 useLayoutEffect 来替代。

## refs

1. https://react.dev/reference/react/useInsertionEffect#useinsertioneffect
2. https://codesandbox.io/s/useinsertioneffect-9o9h9?file=/src/ThemeButton.js
3. https://medium.com/@stheodorejohn/useinsertioneffect-hook-in-react-a-comprehensive-guide-4448096cf227
4. https://blog.saeloun.com/2022/06/02/react-18-useInsertionEffect/

test
