
# useImperativeHandle

> generally recommended to avoid this hook unless it is absolutely needed.

# defined

useImperativeHandle is a React Hook that lets you customize the handle exposed as a ref.

This hook enables imperative code which goes against the declarative nature of React which makes it quite unique.

```
useImperativeHandle(ref, createHandle, dependencies?)
```

- The first parameter is just the ref you are overriding
- the second parameter is a function which returns the new value for your ref.
- useImperativeHandle takes an optional third parameter which is a dependency array.
  - If you do not pass this third parameter to `useImperativeHandle` it will rerun the function you pass to `useImperativeHandle` and update your ref every time the component is rendered.

# useRef & React.forwardRef

see details in useRef chapter

```jsx
// useRef
function App() {
  const [value, setValue] = useState("")
  const inputRef = useRef()

  return (
    <>
      <input
        type="text"
        ref={inputRef}
        value={value}
        onChange={e => setValue(e.target.value)}
      >
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  )
}
```

```jsx
// React.forwardRef
function App() {
  const [value, setValue] = useState("")
  const inputRef = useRef()

  return (
    <>
      <CustomInput
        ref={inputRef}
        value={value}
        onChange={e => setValue(e.target.value)}
      >
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  )
}
```

```jsx
// custom hook
function CustomInput(props, ref) {
	return <input ref={ref} style={{ backgroundColor: "red" }} {...props} />
}

export default React.forwardRef(CustomInput)
```

# usage

With this code we are passing our ref from our `App` component into our `CustomInput` and our `CustomInput` is passing the ref down to our input so the ref inside our `App` component will point to the input inside our `CustomInput` component. This is the basic way that React.forwardRef is used, but sometimes this simple ref forwarding is not enough. That is where useImperativeHandle comes in.

ref只会被point to input element，如果ref组件中需要更多的ref指向不同的行动点/操作点则可以通过useImperativeHandle去实现。

 In essence the only thing this hook does is let you create a completely custom value for the ref you return from a custom component. This means you can do more than just assign a single element to your ref for example. 就可以赋值更多的element给ref。

```jsx
function CustomInput(props, ref) {
  useImperativeHandle(
    ref,
    () => {
      return { alertValue: () => alert(props.value) }
    },
    [props.value]
  )

  return <input ref={ref} style={{ backgroundColor: "red" }} {...props} />
}

export default React.forwardRef(CustomInput)
```

```jsx
function App() {
  const [value, setValue] = useState("")
  const inputRef = useRef()

  return (
    <>
      <CustomInput
        ref={inputRef}
        value={value}
        onChange={e => setValue(e.target.value)}
      >
      <button onClick={() => inputRef.current.alertHi()}>Alert</button>
    </>
  )
}
```

# cases

```jsx
function CustomModal({ open, onClose }, ref) {
  const closeRef = useRef();
  const confirmRef = useRef();
  const denyRef = useRef();

  useImperativeHandle(ref, () => {
    return {
      closeBtn: closeRef.current,
      confirmBtn: confirmRef.current,
      denyBtn: denyRef.current,
    }
  })

  if (!open) return null;

  return (
    <div>
      <button ref={closeRef} onClick={onClose}>
        &times;
      </button>
      <h1>Title</h1>
      <div>
        <button ref={confirmRef}>Confirm</button>
        <button ref={denyRef}>Deny</button>
      </div>
    </div>
  )
};

export default React.forwardRef(CustomModal)
```

```jsx
function App() {
  const [open, setOpen] = useState(false);
  const modalRef = useRef();

  return (
    <>
      <button onClick={() => setOpen(true)}>Open</button>
      <button onClick={() => modalRef.current.closeBtn.focus()}>
        Focus Close Btn
      </button>
      <button onClick={() => modalRef.current.confirmBtn.focus()}>
        Focus Confirm Btn
      </button>
      <button onClick={() => modalRef.current.denyBtn.focus()}>
        Focus Deny Btn
      </button>
      <CustomModal ref={modalRef} open={open} onClose={() => setOpen(false)} />
    </>
  )
}
```

# Pitfall

**Do not overuse refs.** You should only use refs for *imperative* behaviors that you can’t express as props: for example, scrolling to a node, focusing a node, triggering an animation, selecting text, and so on.

**If you can express something as a prop, you should not use a ref.** For example, instead of exposing an imperative handle like `{ open, close }` from a `Modal` component, it is better to take `isOpen` as a prop like `<Modal isOpen={isOpen} />`. [Effects](https://react.dev/learn/synchronizing-with-effects) can help you expose imperative behaviors via props.

# refs

1. [useImperativeHandle Hook Ultimate Guide](https://blog.webdevsimplified.com/2022-06/use-imperative-handle/)
2. [useImperativeHandle](https://react.dev/reference/react/useImperativeHandle)
   1. [最陌生的hooks: useImperativeHandle](https://segmentfault.com/a/1190000040758640)
3. https://medium.com/@yardenhochman/howto-useimperativehandle-hook-in-react-a356f3b3c159
4. https://medium.com/@ahsan-ali-mansoor/ultimate-guide-for-useimperativehandle-hook-6fbc955d6ea0