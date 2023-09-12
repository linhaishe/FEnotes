# useLayoutEffect

# useEffect & useLayoutEffect Defined

## useEffect

The `useEffect` Hook is a powerful tool in React that helps developers manage side effects in functional components. It runs ==asynchronously== after the browser repaints the screen.

This hook is commonly used for handling side effects such as fetching data, working with subscriptions, or interacting with the DOM.

Another important thing to remember is that the ==useEffect function is fired asynchronously to not block the browser paint process.==

you should choose the useEffect Hook for cases where you want to be unobtrusive in the dealings of the browser paint process.

> "useEffect" 钩子是 React 中的一个强大工具，帮助开发者在函数组件中管理副作用。它在浏览器重新绘制屏幕之后以异步方式运行。
>
> 这个钩子通常用于处理诸如获取数据、处理订阅或与 DOM 交互等副作用。
>
> 另一个重要的事情要记住是，"useEffect" 函数被异步触发，以避免阻塞浏览器绘制过程。
>
> 当你希望在处理浏览器绘制过程时保持不干扰时，应该选择使用 "useEffect" 钩子。

## useLayoutEffect

*The function passed to* `useLayoutEffect` *will be run before the browser updates the screen.*

The `useLayoutEffect` Hook is a variation of the `useEffect` Hook that runs ==synchronously== before the browser repaints the screen. It was designed to handle side effects that require immediate DOM layout updates.

==`useLayoutEffect` ensures that any changes made within the hook are applied synchronously before the browser repaints the screen.==While this might not seem ideal, it is highly encouraged in specific use cases, such as when measuring DOM elements, or animating or transitioning elements. ==For example, a DOM mutation that must be visible to the user should be fired synchronously before the next paint, preventing the user from receiving a visual inconsistency.==

> `useLayoutEffect` 钩子是 `useEffect` 钩子的一种变体，它在浏览器重新绘制屏幕之前以==同步方式==运行。它设计用于处理需要立即更新 DOM 布局的副作用。
>
> `useLayoutEffect` 确保在浏览器重新绘制屏幕之前，钩子内部所做的任何更改都会同步应用。尽管这可能在某些情况下不太理想，但在特定的使用案例中，如测量 DOM 元素或对元素进行动画或过渡时，这是极为鼓励的。例如，必须在下次绘制之前同步触发的 DOM 变化，以防止用户看到视觉不一致性。

# differs between useEffect and useLayoutEffect

`useEffect` and `useLayoutEffect` have the same signature. ==Essentially, the differences between useEffect and useLayoutEffect lie in when the two are fired and how they run.==

```js
useEffect(() => {
  // do something
}, [dependencies])

useLayoutEffect(() => {
  // do something
}, [dependencies])
```

## useEffect

useEffect调用触发的流程

1. The user performs an action, i.e., clicking the button
2. React updates the count state variable internally
3. React handles the DOM mutation
4. The browser then paints this DOM change to the browser’s screen
5. The useEffect function is fired only after the browser has painted the DOM change(s)

> 1. 用户执行一个操作，比如点击按钮。
> 2. React 在内部更新了计数状态变量。
> 3. React 处理 DOM 的变化。
> 4. 然后浏览器将这个 DOM 变化绘制到屏幕上。
> 5. `useEffect` 函数只在浏览器已经绘制完 DOM 变化后才会触发。

The function passed to `useEffect` will be fired only after the DOM changes are painted on the screen. The [official docs](https://react.dev/reference/react/useEffect) put it this way, “Even if your Effect was caused by an interaction (like a click), the browser may repaint the screen before processing the state updates inside your Effect”.

Another important thing to remember is that the ==useEffect function is fired asynchronously to not block the browser paint process.==

> `useEffect` 中传递的函数只会在 DOM 变化被绘制到屏幕上后才会触发。正如[官方文档](https://react.dev/reference/react/useEffect)所述，"即使你的 Effect 是由交互触发的（比如点击），浏览器可能会在处理 Effect 内部的状态更新之前重新绘制屏幕"。
>
> 另一个重要的事情要记住是，`useEffect` 函数是异步触发的，以避免阻塞浏览器的绘制过程。

## useLayoutEffect

If you replaced the `useEffect` Hook with `useLayoutEffect`, the following would happen:

1. The user performs an action, i.e., clicking the button
2. React updates the `count state` variable internally
3. React handles the DOM mutation
4. The `useLayoutEffect` function is fired
5. The browser waits for `useLayoutEffect` to finish, and only then does it paint this DOM change to the browser’s screen

The `useLayoutEffect` Hook doesn’t wait for the browser to paint the DOM changes. It triggers the function right after the DOM mutations are computed. Also, keep in mind that updates scheduled inside `useLayoutEffect` will be flushed synchronously and will block the browser paint process.

However, if your effect is mutating the DOM (via a DOM node ref) ***and\*** the DOM mutation will change the appearance of the DOM node between the time that it is rendered and your effect mutates it, then you **don't** want to use `useEffect`. You'll want to use `useLayoutEffect`.

> 如果你将 `useEffect` 钩子替换为 `useLayoutEffect`，会发生以下情况：
>
> 1. 用户执行一个操作，比如点击按钮。
> 2. React 在内部更新 `count state` 变量。
> 3. React 处理 DOM 的变化。
> 4. `useLayoutEffect` 函数被触发。
> 5. 浏览器等待 `useLayoutEffect` 完成，然后才将这个 DOM 变化绘制到屏幕上。
>
> `useLayoutEffect` 钩子不会等待浏览器绘制 DOM 变化。它会在计算完 DOM 变化后立即触发函数。此外，要记住，在 `useLayoutEffect` 中安排的更新将会同步执行，会阻塞浏览器的绘制过程。
>
> 然而，如果你的 Effect 在 DOM 上进行了变异（通过 DOM 节点引用），***并且*** DOM 的变化将在渲染和 Effect 进行变异之间改变 DOM 节点的外观，那么你**不应该**使用 `useEffect`，而应该使用 `useLayoutEffect`。

# Examples to differentiate useEffect and useLayoutEffect

We also demonstrated examples of both hooks regarding their firing, performance, and visual changes.

https://blog.logrocket.com/react-useeffect-vs-uselayouteffect-hooks-examples/#examples-differentiate-useeffect-uselayouteffect

## for firing

```js
useEffect(() => {
    console.log("USE EFFECT FUNCTION TRIGGERED"); // then
});

useEffect(() => {
    console.log("USE seconde EFFECT FUNCTION TRIGGERED"); // and then
});

useLayoutEffect(() => {
    console.log("USE LAYOUT EFFECT FUNCTION TRIGGERED"); // first log out
});
```

When there is more than one `useEffect` call within a component, the order of the effect calls is maintained. The first is triggered, then the second, and the sequence continues. 

The `useLayoutEffect` function is triggered synchronously before the DOM mutations are painted. However, the `useEffect` function is called after the DOM mutations are painted.

![UseEffect And UseLayoutEffect Sequencing Example](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/hooks/useeffect-uselayouteffect-sequencing-example.png)
```jsx
import { useState, useLayoutEffect } from "react";

const App = () => {
  const [name, setName] = useState("Leonardo");

  useLayoutEffect(() => {
    if (name === "Leonardo") {
      setName("Jose");
    }
  }, []);

  return (
    <div>
      <h1>Hello {name}</h1>
    </div>
  );
};
```

We can see that before our screen is updated, the name state is updated. The useLayoutEffect runs and updates the name state before the browser has a chance to paint.

## for performance

```jsx
// painte 200 buttons
... 
return (
...
<section
  style={{
    display: 'column',
    columnCount: '5',
    marginTop: '10px',
  }}
>
  {new Array(count).fill(count).map((c) => (
    <div
      style={{
        height: '20px',
        background: 'red',
        margin: '5px',
      }}
    >
      {c}
    </div>
  ))}
</section>
)
```

```jsx
// and also do a heavy computation 
...
useEffect(() => {
    // do nothing when count is zero
    if (!count) {
      return;
}
    // perform computation when count is updated.
    console.log("=== EFFECT STARTED === ");
    new Array(count).fi).forEach(val => console.log(val));
    console.log(`=== EFFECT COMPLETED === ${count}`);
}, [count]);
```

`useEffect` : the screen update happening before the heavy computation

`useLayoutEffect`: the computation will be triggered before the browser has painted the update. 

## for visual changes

In the real world, this is most of the time, except for when you’re reading layout from the DOM or doing something DOM-related that needs to be painted ASAP. In the next section, we’ll see an example in action.

`useLayoutEffect` truly shines when handling inconsistent visual changes.

https://blog.logrocket.com/react-useeffect-vs-uselayouteffect-hooks-examples/#examples-differentiate-useeffect-uselayouteffect

[Measuring layout before the browser repaints the screen](https://react.dev/reference/react/useLayoutEffect#measuring-layout-before-the-browser-repaints-the-screen)

# When to use useEffect and when to use useLayoutEffect

The useLayoutEffect hook is very powerful and can help us to make important DOM measurements. We can use it for things such as animations, measurements, mutations, etc. Remember that the useLayoutEffect runs synchronously, which means that the application won’t be visually updated until your effect finishes running.

Most of the time, the useEffect Hook should be your first choice because it runs asynchronously and doesn’t block the browser painting process, which can slow down your application. However, when you are completely sure that the code that you wish to use will visually affect your application, such as when using animations, transitions, or when you see some visual inconsistencies, use the useLayoutEffect Hook instead.

With `useEffect`, you get a flicker before the DOM changes are painted, which was related to how refs are passed on to custom Hooks. Initially, these refs start off as `null` before actually being set when the attached DOM node is rendered

If you rely on these refs to perform an animation as soon as the component mounts, then you’ll find an unpleasant flickering of browser paints happening before your animation kicks in. This is the case with `useEffect`, but not `useLayoutEffect`.

Even without this flicker, sometimes you may find `useLayoutEffect` produces animations that look buttery, cleaner, and faster than `useEffect`. Be sure to test both Hooks when working with complex user interface animations.

However, if your effect is mutating the DOM (via a DOM node ref) ***and\*** the DOM mutation will change the appearance of the DOM node between the time that it is rendered and your effect mutates it, then you **don't** want to use `useEffect`. You'll want to use `useLayoutEffect`.

大多数情况下，`useEffect`钩子应该是你的首选，因为它以异步方式运行，不会阻塞浏览器的绘制过程，从而可以避免减慢应用程序的运行。然而，在你完全确定所使用的代码会在视觉上影响应用程序时，比如在使用动画、过渡效果时，或者当出现视觉不一致的情况时，应该使用`useLayoutEffect`钩子。

使用`useEffect`时，在DOM更改被绘制之前，你会看到一次闪烁。这与如何将`ref`传递给自定义钩子有关。最初，这些`ref`在实际渲染附加的DOM节点之前会被设置为`null`。

如果你依赖这些`ref`来在组件挂载后立即执行动画，那么你会在动画开始之前看到不愉快的浏览器绘制闪烁。这在使用`useEffect`时会出现，但在使用`useLayoutEffect`时不会出现。

即使没有这种闪烁，有时候你可能会发现，与`useEffect`相比，`useLayoutEffect`产生的动画效果看起来更加流畅、更清晰、更快速。在处理复杂的用户界面动画时，务必同时测试这两种钩子。

# refs

1. [React Hooks Cheatsheet](https://react-hooks-cheatsheet.com/examples/fetching-data)
2. https://react.dev/reference/react/useLayoutEffect
3. https://www.telerik.com/blogs/uselayouteffect-powerful-hook
4. https://refine.dev/blog/uselayouteffect-vs-useeffect/#introduction
