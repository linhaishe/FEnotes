# useState

States forms the heart and soul which makes React a go-to library for ease of use and smooth user experience.

## useState function

The React `useState` Hook allows you to have state variables in functional components. You pass the initial state to this function, and it returns a variable with the current state value (not necessarily the initial state) and another function to update this value.

## the value in useState hook

The useState Hook provides those two things:

1. A state variable to retain the data between renders.
2. A state setter function to update the variable and trigger React to render the component again.

```jsx
const [state, setState] = useState(initialValue);
```

useState can store any type of value.

Calling `React.useState` inside a function component generates a single piece of state associated with that component.

`React.useState`在函数组件内部形成一个作用域。每次函数组件被调用时，`React.useState`会创建一个新的状态变量，并将其与当前组件实例相关联。这个状态变量只在当前组件实例的作用域内可见，不会被其他组件实例所共享。这样可以确保每个组件实例都有自己的独立状态，并且状态的更新只会影响到当前组件实例。

useState对本地组件的状态非常有利，但是如果在大型项目里面，可能会需要用到状态管理工具。[A guide to choosing the right React state management solution](https://blog.logrocket.com/guide-choosing-right-react-state-management-solution/)

## Declaring state in useState

You can also use a function to [lazily initialize](https://blog.logrocket.com/lazy-loading-components-in-react-16-6-6cea535c0b52/) the variable. This is useful when the initial state is the result of an expensive computation

```javascript
const Message= () => {
   const messageState = useState( () => expensiveComputation() );
   /* ... */
}
```

The initial value will be assigned only on the initial render. <mark>**If it’s a function, it will be executed only on the initial render.**</mark>

why does `useState` return an array: 数组解构模式下方便命名。

```js
// Without using object destructuring
const messageState = useState( '' );
const message = messageState.state;
const setMessage = messageState

// Using object destructuring
const { state: message, setState: setMessage } = useState( '' );
const { state: list, setState: setList } = useState( [] );
```

## Declaring setter function in useState

the setter function is a function that takes a new value to update the state variable. 

 this update function doesn’t update the value right away. Instead, it enqueues the update operation.

When updating state based on its previous value, you need to pass a function to the setter function that updates the state.

```jsx
export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1); // setCount(0 + 1)
    setCount(count + 1); // setCount(0 + 1)
    setCount(count + 1); // setCount(0 + 1)
  }

  return (
    <button onClick={handleClick}>
      You pressed me {count} times
    </button>
  );
}
```

```jsx
export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount((c) => c + 1); // setCount(0 => 1)
    setCount((c) => c + 1); // setCount(1 => 2)
    setCount((c) => c + 1); // setCount(2 => 3)
  }

  return (
    <button onClick={handleClick}>
      You pressed me {count} times
    </button>
  );
}
```

## usestate中用object作为state variable的使用和注意事项

There are two things you need to keep in mind about updates when using objects:

- The importance of [immutability](https://blog.logrocket.com/immutability-react-should-you-mutate-objects/)
- And the fact that the setter returned by `useState` doesn’t [merge objects like `setState()` does](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-are-merged) in class components

About the first point, if you use the same value as the current state to update the state (React uses `Object.is()` for comparing), React won’t trigger a re-render.

setter function 中如果传入的引用类型是引用指针相同的数值，则会导致组件无法触发re-render，因为setter function会认为数据没有被修改。

### one-dimensional arrays / objects

```js
// 需要依赖原有的数据进行更新

onChange={e => {
  const val = e.target.value;
  setMessage(prevState => {
    return { ...prevState, message: val }
  });
}}

// the smae result as using Object.assign() (just remember to create a new object):
onChange={e => {
  const val = e.target.value;
  setMessage(prevState => {
    return Object.assign({}, prevState, { message: val });
  });
}}
```

### multi-dimensional arrays and nested objects

be careful when using state objects with a complex structure (nested objects). 

```js
// multi-dimensional arrays
[
  ['value1','value2'],
  ['value3','value4']
]

// You could use them to group all your state variables in one place. However, for that purpose, it would be better to use nested objects like this:
{
  'row1' : {
    'key1' : 'value1',
    'key2' : 'value2'
  },
  'row2' : {
    'key3' : 'value3',
    'key4' : 'value4'
  }
}
```

```js
const [messageObj, setMessage] = useState({
  author: '',
  message: {
    id: 1,
    text: ''
  }
});
```

```js
// Wrong
setMessage(prevState => ({
  ...prevState,
  text: 'My message'
}));

// Wrong
setMessage(prevState => ({
  ...prevState.message,
  text: 'My message'
}));

// Wrong
setMessage(prevState => ({
  ...prevState,
  message: {
    text: 'My message'
  }
}));
```

```js
// Correct
setMessage(prevState => ({
  ...prevState,           // copy all other field/objects
  message: {              // recreate the object that contains the field to update
    ...prevState.message, // copy all the fields of the object
    text: 'My message'    // overwrite the value of the field to update
  }
}));

// Correct
setMessage(prevState => ({
  author: 'Joe',          // overwrite the value of the field to update
  ...prevState.message    // copy all other field/objects
}));

// Correct
setMessage(prevState => ({
  author: 'Joe',          // update the value of the field
  message: {              // recreate the object that contains the field to update
    ...prevState.message, // copy all the fields of the object
    text: 'My message'    // overwrite the value of the field to update
  }
}));
```

In some cases, [cloning deeply nested objects](https://blog.logrocket.com/methods-for-deep-cloning-objects-in-javascript/) can be expensive because React may re-render parts of your applications that depend on fields that haven’t even changed.

For this reason, the first thing you need to consider is trying to flatten your state object(s). In particular, the React documentation recommends [splitting the state into multiple state variables](https://reactjs.org/docs/hooks-faq.html#should-i-use-one-or-many-state-variables) based on which values tend to change together.

If this is not possible, the recommendation is to use libraries that help you work with immutable objects, such as [immutable.js or immer](https://blog.logrocket.com/immer-and-immutable-js-how-do-they-compare/).

## Rules for using `useState`

`useState` abides by the same [rules that all Hooks follow](https://reactjs.org/docs/hooks-rules.html):

- Only call Hooks at the top level
- Only call Hooks from React functions

## refs

1. [State: A Component's Memory](https://react.dev/learn/state-a-components-memory)

2. [react.dev](https://react.dev/)

3. [useState in React: A complete guide](https://blog.logrocket.com/guide-usestate-react/)

4. [useState hook - behind the hood](Behind the hood implementation of useState react hook)

5. [useState react dev](https://react.dev/reference/react/useState)