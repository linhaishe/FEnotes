
# useRef

## what is useRef

Most developers find React very comfortable and scalable because of its provision of hooks.React allows for developer discretion, and more so than most UI libraries,

They kept the library open for situations beyond the ones they were specifically designing for and situations the model may not work for. We’ll cover anti-patterns later in this article.

These escape hatches are refs, which allow us to access DOM properties directly.

`useRef()` hook creates references.

Calling `const reference = useRef(initialValue)` with the initial value returns a special object named reference. The reference object has a property `current`: you can use this property to read the reference value `reference.current`, or update `reference.current = newValue`.

Between the component re-renderings, the value of the reference is persisted.

Updating a reference, contrary to updating state, doesn't trigger component re-rendering.

References can also access DOM elements. Assign the reference to `ref` attribute of the element you'd like to access: `<div ref={reference}>Element</div>` — and the element is available at `reference.current` after the component mounting.

it is used to reference an object inside a functional component and preserves the referenced object's state between re-renders.

- The value of the referenced object remains the same between re-renders.
- Updating the value of the referenced object doesn’t trigger a re-render.

```jsx
import { useRef } from ‘react’

const myComponent = () => {
   const refObj = useRef(initialValue)

    return (
    //…
    )
}

// In the snippet above, we have an object refObj we want to reference in an application, to access the value or update the value, we can call the current property like this:
// inside a function
const handleRefUpdate = () => {
    // accessing the referenced object’s value
    const value = refObj.current

    // updating the referenced object’s value
   refObj.current = newValue
}
```

```jsx
import { useRef } from 'react';
const AppDemo8 = () => {
  const ref1 = useRef();
  const ref2 = useRef(2021);
  console.log("render");
  console.log(ref1, ref2);
  return (
    <div>
      <h2>{ref1.current}</h2>
      <h2>{ref2.current}</h2>
    </div>
  );
};
```

![useRef Values Are Stored in the Current Property](https://blog.logrocket.com/wp-content/uploads/2021/05/values-stored-current-property.png)

We initialized two references (aka refs) by calling. The Hook call returns an object that has a property `current`, which stores the actual value. If you pass an argument `initialValue` to `useRef(initialValue)`, then this value is stored in `current`.

## Differences between `useRef` and `createRef`

// todo add use cases

## Accessing DOM elements

### use cases

#### Focus control

```jsx
import React, { useEffect, useRef, useState } from "react";
const InputModal = ({ initialValue }) => {
  const [value, setValue] = useState(initialValue);
  const inputRef = useRef(null);
  useEffect(() => {
    inputRef.current.focus();
  }, [])
  const onChange = (e) => {
    setValue(e.target.value);
  };
  const onSubmit = (e) => {
    e.preventDefault();
  };
  return (
    <div className="modal--overlay">
      <div className="modal">
        <h1>Insert a new value</h1>
        <form action="?" onSubmit={onSubmit}>
          <input ref={inputRef} type="text" onChange={onChange} value={value} />
          <button>Save new value</button>
        </form>
      </div>
    </div>
  );
};
export default InputModal;
```

#### Detect if an element is contained

````jsx
import React, { useEffect, useRef, useState } from "react";
const InputModal = ({ initialValue, onClose, onSubmit }) => {
  const [value, setValue] = useState(initialValue);
  const inputRef = useRef(null);
  const modalRef = useRef(null);
  useEffect(() => {
    inputRef.current.focus();
    document.body.addEventListener("click", onClickOutside);
    return () => document.removeEventListener("click", onClickOutside);
  }, []);
  const onClickOutside = (e) => {
    const element = e.target;
    if (modalRef.current && !modalRef.current.contains(element)) {
      e.preventDefault();
      e.stopPropagation();
      onClose();
    }
  };
  const onChange = (e) => {
    setValue(e.target.value);
  };
  const onSub = (e) => {
    e.preventDefault();
    onSubmit(value);
    onClose();
  };
  return (
    <div className="modal--overlay">
      <div className="modal" ref={modalRef}>
        <h1>Insert a new value</h1>
        <form action="?" onSubmit={onSub}>
          <input ref={inputRef} type="text" onChange={onChange} value={value} />
          <button>Save new value</button>
        </form>
      </div>
    </div>
  );
};
export default InputModal;
````

```jsx
import React, { useEffect} from 'react'
 
export default function useClickAway(ref: any, callback: Function) {
   useEffect(() => {
     function handleClickAway(event: any) {
       if (ref.current && !ref.current.contains(event.target)) {
         callback();
       }
     }
 document.addEventListener("mousedown", handleClickAway);
     return () => {
       document.removeEventListener("mousedown", handleClickAway);
     };
   }, [ref]);
 };
```

```jsx
import React, { useRef } from "react";
//.. Other importations
export default function Storefront() {
  const targetElement = useRef(null)
  const alertClickAway = () => {
   alert("Clicked outside product 1")
 }
 useClickAway(targetElement, alertClickAway)
 //.. Other functions
 return (
       {//.. Other parts of the application}
       <div className="gallery">
         <div className="col" ref={targetElement}>
           <img src="https://i.postimg.cc/G207QNV7/image.png" alt="Product 1" />
           <p>iWatch Series 6</p>
           <div className="btns">
             <button>
               <img src="https://api.iconify.design/flat-color-icons:like.svg?color=%23888888" alt="like" />
             </button>
             <button>
               <img 
                  src="https://api.iconify.design/icon-park:buy.svg?color=%23888888"
                  alt="add" />
            </button>
           </div>
         </div>
 )
}
```

### using`forwardRef`

React provides an inbuilt solution for this called forwardRef, which allows you to define internally what element the ref will point at:

```jsx
import React from 'react'

const LabelledInput = (props) => {
  const { id, label, value, onChange } = props

  return (
    <div class="labelled--input">
      <label for={id}>{label}</label>
      <input id={id} onChange={onChange} value={value} />
    </div>
  )
}

export default LabelledInput
```

The issue now is that passing a ref to this component will return its instance, a React component reference, and not the `input` element we want to focus on, like in our first example. 

```jsx
import React from 'react'

const LabelledInput = (props, ref) => {
  const { id, label, value, onChange } = props

  return (
    <div class="labelled--input">
      <label for={id}>{label}</label>
      <input id={id} onChange={onChange} value={value} ref={ref}/>
    </div>
  )
}

export default React.forwardRef(LabelledInput)
```

```jsx
// ...
const inputRef = useRef(null);

<form action="?" onSubmit={onSubmit}>
  <LabelledInput
    label="quantity"
    ref={inputRef}
    type="text"
    onChange={onChange}
    value={value}
  />
  <button>Save new value</button>
</form>
```

Accessing functional components: DOM elements, which should not be mistaken for functional components, can be referenced using the Ref attribute. Because, unlike class components or DOM elements, functional components do not have instances. For example:

```jsx
import {useRef} from ‘react’

const FunctionalComponent = () => {
  return (<h1>Hello World<>)
}

const myComponent = () => {
	const elementRef = useRef()
    return (
        <FunctionalComponent ref={elementRef} />
    )
}
```

Because the component `FunctionalComponent` does not have instances, the ref in the code snippet above will not work. Instead, we can convert the `FunctionalComponent` into a class component or use `forwardRef` in the `FunctionalComponent` component.

## Referencing a value with a ref(store value/state)

You can store inside a reference infrastructure data of side effects: timer ids, socket ids, etc.

This constitutes the second use case of `useRef` besides utilizing it as a generic container persisting data throughout the component lifecycle.

Another common use case is when you need the state value of the previous render cycle.

```jsx
import { useRef, useState, useEffect } from 'react';

function Stopwatch() {
  const timerIdRef = useRef(0);
  const [count, setCount] = useState(0);

  const startHandler = () => {
    if (timerIdRef.current) { return; }
    timerIdRef.current = setInterval(() => setCount(c => c+1), 1000);
  };

  const stopHandler = () => {
    clearInterval(timerIdRef.current);
    timerIdRef.current = 0;
  };

  useEffect(() => {
    return () => clearInterval(timerIdRef.current);
  }, []);

  return (
    <div>
      <div>Timer: {count}s</div>
      <div>
        <button onClick={startHandler}>Start</button>
        <button onClick={stopHandler}>Stop</button>
      </div>
    </div>
  );
}
```

refs: https://dmitripavlutin.com/react-useref/#12-use-case-implementing-a-stopwatch

## useState vs useRef

```jsx
const AppDemo9 = () => {
  const countRef = useRef(0);
  console.log("render");
  return (
    <div className="App">
      <h2>count: {countRef.current}</h2>
      <button
        onClick={() => {
          countRef.current = countRef.current + 1;
          console.log(countRef.current);
        }}
      >
        increase count
      </button>
    </div>
  );
};
```

The values of refs persist (specifically the `current` property) throughout render cycles. It’s not a bug; it’s a feature.

Consider situations where you want to update a component’s data (i.e., its state variables) to trigger a render in order to update the UI. You could also have situations where you want the same behavior with one exception: you do not want to trigger a render cycle because this could lead to bugs, awkward user experience (e.g., flickers), or performance problems.

You can think of refs as [instance variables of class-based components](https://reactjs.org/docs/hooks-faq.html#is-there-something-like-instance-variables). A ref is a generic container to store any kind of data, such as primitive data or objects.

这里没看懂

The differences between useRef and useState at a glance
The following differences have already been discussed in detail but are presented here again in a succinctly summarized form:

- Both preserve their data during render cycles and UI updates, but only the useState Hook with its updater function causes re-renders
- useRef returns an object with a current property holding the actual value. In contrast, useState returns an array with two elements: the first item constitutes the state, and the second item represents the state updater function
- useRef‘s current property is mutable, but useState‘s state variable not. In contrast to the current property of useRef, you should not directly assign values to the state variable of useState. Instead, always use the updater function (i.e., the second array item). As the React team recommends in the documentation for setState in class-based components (but still true for function components), treat state like an immutable variable
- useState and useRef can be considered data Hooks, but only useRef can be used in yet another field of application: to gain direct access to React components or DOM elements

## When should you use `useRef` Hook?

<mark>only use a ref when you need to imperatively call a function for a behavior React doesn’t allow you to control.</mark>

仅当您需要为 React 不允许您控制的行为强制调用函数时才使用 ref。

There are some instances where you would want to use the `useRef` Hook, including the following:

- Accessing DOM elements: You can use the `useRef` Hook when you need to interact with a specific DOM element in your component, such as setting the focus on an input field or measuring an element’s size
- Storing values that don’t trigger re-renders: When you have a value that changes frequently but doesn’t trigger a re-render, you can use `useRef` to store that value. For example, if you have a timer in your component, you could use `useRef` to store the current time without triggering a re-render
- Caching expensive computations: If you need to avoid repeating an expensive computation on every render, you can use `useRef` to store the result of that computation
- Interacting with input elements: Accessing input elements and performing functionality like focus, change tracking or auto-completion are made possible by using refs.
- Interacting with third-party UI libraries: Ref can be used to interact with elements created by third-party UI libraries that might be tricky to access using standard DOM methods. For instance, if you use a third-party library to generate sliders, you can use ref to access the sliders' DOM element without being informed of the structure of the slider library's source code.
- Media playback: You may also access media assets like images, audio, or videos using refs and interact with how they are rendered. For instance, auto-playing videos or lazy loading of images when an element enters the viewport.
- Complex animation triggering: Traditionally, CSS keyframes or a timeout are used to determine when to initiate animations. In some situations, which can be more complicated, you can use refs to observe DOM elements and determine when to start an animation.
- In some situations, such as the following, you shouldn't use references:
- Declarative cases: Even in situations with simple solutions where using refs works, there is no need to write more expensive code to do the same task. For instance, using conditional rendering to hide or show DOM elements instead of refs.
- Elements affecting state: Occasionally, the concept of using refs is so intriguing that you overlook the impact of modifications made to an element on the application's lifecycle. You should have in mind that changes to refs do not cause re-rendering and that refs maintain the value of their objects across renderings. Therefore, it is advisable to avoid using refs in situations when state changes need to trigger a re-render.
- Accessing functional components: DOM elements, which should not be mistaken for functional components, can be referenced using the Ref attribute. Because, unlike class components or DOM elements, functional components do not have instances. For example:

But,能不用useRef的时候就不要用～，cus it’s easy to use them where they’re not needed.

## Avoiding React ref anti-patterns

"anti-patterns" 在中文中的意思是“反模式”，它指的是编程中常见的不良实践或设计模式，可能会导致代码难以理解、难以维护、低效或出现错误。因此，在编程中应该避免使用反模式，而是采用最佳实践来编写高质量、可维护的代码。

There’s more than one way to achieve the same thing inside a React component, so it’s easy to fall into an [anti-pattern](https://blog.logrocket.com/product-management/strategic-roadmap-examples-antipatterns/). 

A simpler way to put that is when you need to call a function, and that function has no association with a React method or artifact, use a ref.

```jsx
import React, { useRef } from "react";
const Form = () => {
  const [storedValue, setStoredValue] = useState("");
  const inputRef = useRef(null);
  const onSubmit = (e) => {
    e.preventDefault();
    setStoredValue(inputRef.current.value);
  };
  return (
    <div className="modal">
      <form action="?" onSubmit={onSubmit}>
        <input ref={inputRef} type="text" />
        <button>Submit</button>
      </form>
    </div>
  );
};
```

```jsx
return (
  <input
    type="text"
    onChange={e => setValue(e.target.value)}
    value={value}
  />
)
```

如果要在提交时发送一个值，这种方法确实可以工作，但问题在于，由于我们知道refs提供了React提供的视图模型的逃生通道，因此我们可以太容易地嗅探DOM元素的值或属性，这些值或属性可以通过React的接口访问。控制输入值意味着我们可以始终检查它的值。我们不需要在这里使用refs来访问文本框的值。我们可以使用React本身提供的值。

只有在需要强制调用一个函数来控制React不允许控制的行为时才使用ref。在我们的非受控输入中，我们创建了一个ref，但没有进行强制调用。然后，该函数应该存在，但实际上我可以控制输入的值，因此这个条件并没有满足。

## Updating references restriction

The function scope of the functional component should either calculate the output or invoke hooks.

That's why updating a reference (as well as updating state) shouldn't be performed inside the immediate scope of the component's function.

The reference must be updated either inside a `useEffect()` callback or inside handlers (event handlers, timer handlers, etc).

```jsx
import { useRef, useEffect } from 'react';

function MyComponent({ prop }) {
  const myRef = useRef(0);

  useEffect(() => {
    myRef.current++; // Good!

    setTimeout(() => {
      myRef.current++; // Good!
    }, 1000);
  }, []);

  const handler = () => {
    myRef.current++; // Good!
  };

  myRef.current++; // Bad!

  if (prop) {
    myRef.current++; // Bad!
  }

  return <button onClick={handler}>My button</button>;
}
```

## use cases

usePreviousvaluehook

### useEffectSkipFirstRender()

```jsx
const useEffectSkipFirstRender = (callback, dependencies) => {
  const renderRef = React.useRef(false);
 
  React.useEffect( () => {
   if(!renderRef.current) {
     renderRef.current = true;
     return;  
   }
   callback();
  }, dependencies);
}
```

### `usePrevious` Hook.

```jsx
const AppDemo13 = () => {
  console.log("render");
  const [count, setCount] = useState(0);
  // Get the previous value (was passed into hook on last render)
  const ref = useRef();
  // Store current value in ref
  useEffect(() => {
    console.log("useEffect");
    ref.current = count;
  }, [count]); // Only re-run if value changes
  return (
    <div className="App">
      <h1>
        Now: {count}, before: {ref.current}
      </h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};
```

It’s important to note that all refs need to get updated either inside a useEffect callback or inside handlers. Mutating the ref during rendering, i.e., from places other than those just mentioned, might introduce bugs. The same applies to useState, too.

## sum

this article addresses the `useState` and `useRef` Hooks. It should be clear at this point that there is no such thing as a good or a bad Hook. You need both Hooks for your React applications because they are designed for different applications.

If you want to update data and cause a UI update, `useState` is your Hook. If you need some kind of data container throughout the component’s lifecycle without causing render cycles on mutating your variable, then `useRef` is your solution.

## refs

1. [Avoiding React ref anti-patterns](https://blog.logrocket.com/complete-guide-react-refs/)
2. https://blog.logrocket.com/usestate-vs-useref/
3. https://refine.dev/blog/react-useref-hook-and-ref/
4. https://react.dev/reference/react/useRef
5. https://medium.com/hannah-lin/react-hook-%E7%AD%86%E8%A8%98-useref-c628cbf0d7fb
6. https://dmitripavlutin.com/react-useref/