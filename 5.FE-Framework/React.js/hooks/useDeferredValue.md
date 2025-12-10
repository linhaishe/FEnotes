# useDeferredValue

Demo: https://stackblitz.com/edit/stackblitz-starters-ndbgfs?file=src%2FApp.tsx

# Definition

> `useDeferredValue` lets you defer re-rendering a non-urgent part of the tree. It is similar to debouncing, but has a few advantages compared to it. There is no fixed time delay, so React will attempt the deferred render right after the first render is reflected on the screen. The deferred render is interruptible and doesn't block user input.
>
> `useDeferredValue` 允许您延迟重新渲染树中不紧急的部分。它类似于防抖动（debouncing），但与之相比具有一些优点。它没有固定的时间延迟，因此 React 会尝试在第一次渲染在屏幕上反映之后立即执行延迟渲染。延迟渲染是可中断的，不会阻塞用户输入。

The `useDeferredValue` hook allows us to fix this slow render problem by implementing a delay before some information is calculated. 

`useDeferredValue` is a React Hook that lets you defer updating a part of the UI.

useDeferredValue is a React hook that accepts a value and returns a new copy of the value that will defer to more urgent updates.

This delay allows React to prioritize other updates that are more important for the user feedback, such as typing or scrolling.

 **useDeferredValue** 可以让我们延迟渲染不紧急的部分，类似于防抖但没有固定的延迟时间，延迟的渲染会在紧急的部分先出现在浏览器屏幕以后才开始，并且可中断不会阻塞用户输入。

# usage

`const deferredValue = useDeferredValue(value);`

#### Parameters 

- `value`: The value you want to defer. It can have any type.

#### Returns 

During the initial render, the returned deferred value will be the same as the value you provided. During updates, React will first attempt a re-render with the old value (so it will return the old value), and then try another re-render in background with the new value (so it will return the updated value).

> 在初始渲染时，返回的延迟值将与您提供的值相同。在更新期间，React 首先尝试使用旧值进行重新渲染（因此它将返回旧值），然后在后台尝试使用新值进行另一次重新渲染（因此它将返回更新后的值）。

# pros / cons

#### Caveats 

- The values you pass to `useDeferredValue` should either be primitive values (like strings and numbers) or objects created outside of rendering. If you create a new object during rendering and immediately pass it to `useDeferredValue`, it will be different on every render, causing unnecessary background re-renders.
- When `useDeferredValue` receives a different value (compared with [`Object.is`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is)), in addition to the current render (when it still uses the previous value), it schedules a re-render in the background with the new value. The background re-render is interruptible: if there’s another update to the `value`, React will restart the background re-render from scratch. For example, if the user is typing into an input faster than a chart receiving its deferred value can re-render, the chart will only re-render after the user stops typing.
- `useDeferredValue` is integrated with [``.](https://react.dev/reference/react/Suspense) If the background update caused by a new value suspends the UI, the user will not see the fallback. They will see the old deferred value until the data loads.
- `useDeferredValue` does not by itself prevent extra network requests.
- There is no fixed delay caused by `useDeferredValue` itself. As soon as React finishes the original re-render, React will immediately start working on the background re-render with the new deferred value. Any updates caused by events (like typing) will interrupt the background re-render and get prioritized over it.
- The background re-render caused by `useDeferredValue` does not fire Effects until it’s committed to the screen. If the background re-render suspends, its Effects will run after the data loads and the UI updates.

> - 您传递给 `useDeferredValue` 的值应该是原始值（比如字符串和数字）或在渲染外部创建的对象。如果您在渲染期间创建一个新对象并立即传递给 `useDeferredValue`，它将在每次渲染时都不同，导致不必要的后台重新渲染。
> - 当 `useDeferredValue` 接收到一个不同的值（与 [`Object.is`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is) 进行比较），除了当前渲染（当它仍然使用先前的值时），它会在后台计划一个使用新值的重新渲染。后台重新渲染是可中断的：如果 `value` 有另一个更新，React 将从头开始重新启动后台重新渲染。例如，如果用户在输入中键入速度比图表接收其延迟值的重新渲染更快，那么图表只会在用户停止输入后重新渲染。
> - `useDeferredValue` 与 [``](https://react.dev/reference/react/Suspense) 集成。如果由于新值引起的后台更新使 UI 暂停，用户将看不到回退。他们将看到旧的延迟值，直到数据加载完成。
> - `useDeferredValue` 本身不会阻止额外的网络请求。
> - `useDeferredValue` 本身不会引起固定的延迟。一旦 React 完成原始的重新渲染，它将立即开始使用新的延迟值进行后台重新渲染。由事件（如键入）引起的任何更新都将中断后台重新渲染，并优先于它。
> - 由 `useDeferredValue` 引起的后台重新渲染不会在提交到屏幕之前触发 Effects。如果后台重新渲染暂停，它的 Effects 将在数据加载完成并更新 UI 后运行。

## useDeferredValue vs. useTransition

`useTransition`直接控制`更新状态的代码`，而`useDeferredValue`控制一个受状态变化影响的值。它们做的是同样的事,帮助提高用户体验(UX)，不应该同时使用这两者。

相反，如果你可以访问`更新操作`，并且有一些`更新操作`应该以较低的优先级处理，就使用`useTransition`。如果你没有这种权限，就使用`useDeferredValue`。

和防抖的区别：防抖有固定时间，但是这个没有。

# refs

1. [漫谈 React 系列(五)：一起聊一聊 useDeferredValue](https://juejin.cn/post/7083466010505773093)
2. [Day30-還想學更多嗎?推薦 Youtube 上面免費的 React 學習資源](https://ithelp.ithome.com.tw/articles/10281474)
3. [React 18 useDeferredValue Hook Crash Course](https://www.youtube.com/watch?v=jCGMedd6IWA)
4. [Why Do You Need `useDeferredValue`?](https://blog.webdevsimplified.com/2022-05/use-deferred-value/)
5. [useDeferredValue](https://react.dev/reference/react/useDeferredValue)
6. [React 18中的useTransition和useDeferredValue使用](https://segmentfault.com/a/1190000043554384)

*you should check out my [complete useState hook article](https://blog.webdevsimplified.com/2020-04/use-state) and [complete useMemo hook article](https://blog.webdevsimplified.com/2020-05/memoization-in-react#usememo) before reading further.*