Notes-part 1

1. 组件内可以写辅助函数

```react
const Hello = (props) => {
    //组件内可以写辅助函数
  const bornYear = () => {    
      const yearNow = new Date().getFullYear()    
      return yearNow - props.age  
  }
  
  return (
    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>
      <p>So you were probably born in {bornYear()}</p>    
    </div>
  )
}
```

2. Destructuring

<mark>传递给组件的props现在直接解构为变量 name 和 age。</mark>

<mark>这意味着不需要将整个 props 对象赋值给一个名为*props* 的变量中，然后再将其属性分配到变量 name 和 age 中：</mark>

```react
const Hello = ({ name, age }) => {
```

3. useState 函数

```react
import React, { useState } from 'react'
const [ counter, setCounter ] = useState(0)
```

函数调用将*state* 添加到组件，并将其值用0进行初始化。 该函数返回一个包含两个元素的数组。 我们使用前面所讲的解构赋值语法将元素分配给变量 *counter* 和 *setCounter* 。

*counter* 变量被赋予的初始值*state* 为零。 变量 setCounter 被分配给一个函数，该函数将用于*修改 state*。

4. 事件处理

<mark>事件处理程序应该是一个*函数* 或一个*函数引用*</mark>,事件处理程序不能是对函数的调用，它必须是函数或对函数的引用

事件处理器实际上被定义成了一个*函数调用*。 在很多情况下这是可行的，但在这种特殊情况下就不行了。 一开始*counter* 变量的值是0。 当 React 第一次渲染时，它执行函数调用*setCounter(0+1)*，并将组件状态的值更改为1。

这将导致组件重新渲染，react 将再次执行 setCounter 函数调用，并且状态将发生变化，从而导致另一个重新运行...
(状态不断变化，导致变成无限模式)

```react
//报错
<button onClick={setCounter(counter + 1)}> 
  plus
</button>
//right
<button onClick={() => setCounter(counter + 1)}> 
  plus
</button>

//函数引用
const increaseByOne = () => setCounter(counter + 1)    
const setToZero = () => setCounter(0)

<button onClick={increaseByOne}>plus</button>
<button onClick={setToZero}>zero</button>
```

5. 编写小型可重复使用的组件

```react
const Button = (props) => {
  return (
    <button onClick={props.handleClick}>
      {props.text}
    </button>
  )
}

<Button handleClick={increaseByOne} text='plus'/>      
```

6. <mark>复杂状态下，最简单和最好的方法是多次使用 useState 函数来创建单独的状态“片段”。</mark>

```react
const [left, setLeft] = useState(0)
const [right, setRight] = useState(0)
const [allClicks, setAll] = useState([])
```

7. spread options

```js
var click = {left:0,right:0}
var newClick = {...click,left:click.left+1}
console.log(newClick)
//{ left: 1, right: 0 }
```

8. React 中状态不可直接修改

```js
//wrong
const handleLeftClick = () => {
  clicks.left++
  setClicks(clicks)
}


//right
const handleLeftClick = () =>
  setClicks({ ...clicks, left: clicks.left + 1 })

const handleRightClick = () =>
  setClicks({ ...clicks, right: clicks.right + 1 })
```

9. <mark>hook 只能从定义 React component 的函数体内部调用:</mark>

```react
const App = () => {
  // these are ok
  const [age, setAge] = useState(0)
  const [name, setName] = useState('Juha Tauriainen')

  if ( age > 10 ) {
    // this does not work!
    const [foobar, setFoobar] = useState(null)
  }

  for ( let i = 0; i < age; i++ ) {
    // also this is not good
    const [rightWay, setRightWay] = useState(false)
  }

  const notGood = () => {
    // and this is also illegal
    const [x, setX] = useState(-1000)
  }

  return (
    //...
  )
}
```

10. Function that returns a function（part 1 ，node 4）

```react
const App = () => {
  const [value, setValue] = useState(10)

  const hello = () => {   
      const handler = () => console.log('hello world')    
      return handler  
  }
  return (
    <div>
      {value}
      <button onClick={hello()}>button</button>
    </div>
  )
}

<button onClick={hello('world')}>button</button>      


```

