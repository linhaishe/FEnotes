# useTransition

React 18 新加的功能之一，就是 `Transition`， 作用在於將State分為 `緊急(Urgent)` 及 `非緊急(Non-urgent)` 兩種，Transition 對應的也就是 `非緊急的state` 更新。

它可以延遲渲染指定的元件，讓優先度較低或是比較要耗時的元件稍後渲染。

just setting the priority. 

`useTransition()` is the hook that lets you access concurrent mode features inside of the React component.

`useTransition` is a React Hook that lets you update the state without blocking the UI.

you can enable the concurrent mode — which allows you to mark UI updates as high or interruptible-low priority.

`const [isPending, startTransition] = useTransition()`

==I was thinking it should be called useLowPriority or useDeferredPriority or useInterruptable==

By default, all updates in React are considered urgent. That could create a problem when quick updates are slowed down by heavy updates.

However, starting React 18 and the new concurrency features, you can mark some updates as interruptible and non-urgent — so-called transitions.

![pics](https://s2.loli.net/2023/08/19/qhC3bkrFwfJ8xyK.png)

![image-20230819235052885](https://s2.loli.net/2023/08/19/69ICqGyNAtJfco4.png)

# Usage

```jsx
import { useTransition } from 'react';

function TabContainer() {
  const [isPending, startTransition] = useTransition();
  // ...
}
```

## Parameters 

`useTransition` does not take any parameters.

## Returns 

`useTransition` returns an array with exactly two items:

1. The `isPending` flag that tells you whether there is a pending transition.
2. The [`startTransition` function](https://react.dev/reference/react/useTransition#starttransition) that lets you mark a state update as a transition.

function inside startTransition is going to be low priority by default,  all of our state changes in react are high priority and they all run after the other until they're all finished.

```jsx
function TabContainer() {
  const [isPending, startTransition] = useTransition();
  const [tab, setTab] = useState('about');

  function selectTab(nextTab) {
    startTransition(() => {
      setTab(nextTab);
    });
  }
  // ...
}
```

# pros / cons

- ==The function you pass to `startTransition` must be synchronous.== React immediately executes this function, marking all state updates that happen while it executes as transitions. If you try to perform more state updates later (for example, in a timeout), they won’t be marked as transitions.
- A state update marked as a transition will be interrupted by other state updates. For example, if you update a chart component inside a transition, but then start typing into an input while the chart is in the middle of a re-render, React will restart the rendering work on the chart component after handling the input update.
- Transition updates can’t be used to control text inputs.
- If there are multiple ongoing transitions, React currently batches them together. This is a limitation that will likely be removed in a future release.

# cases

https://codesandbox.io/s/heavy-update-as-non-urgent-forked-k7spg5?file=/src/FilterList.js

# refs

1. [React 18 useTransition Hook Crash Course](https://www.youtube.com/watch?v=N5R6NL3UE7I)
2. [useTransition](https://react.dev/reference/react/useTransition)
3. [Don't Stop Me Now: How to Use React useTransition() hook](https://dmitripavlutin.com/react-usetransition/#3-heavy-ui-updates-as-transitions)
4. [译3](https://juejin.cn/post/7020621789172613157)
5. [Replacing render with createRoot](https://github.com/reactwg/react-18/discussions/5)
6. [筆記 + 使用心得React 18 的更新](https://ithelp.ithome.com.tw/articles/10309484)
7. [Day29-淺談 React 18 的優化和新的 API(Fiber、Suspense、useTransition、useDeferredValue)](https://ithelp.ithome.com.tw/articles/10281124)
8. [faker](https://fakerjs.dev/)