Note-part 2

1. 注意：如前一章所说的，当你使用 *console.log* 命令进行调试时，不要用Java的方式，将所有东西用'+'连在一起。

```js
console.log('props value is' + props)
//good
console.log('props value is', props)
```

注意，现在必须为*Note* 组件定义*key* 属性，而不是像前面那样为*li* 标签定义*key* 属性。

可以在单个文件中编写整个 React 应用。 虽然实践中很少这么用。 通常的做法是将每个组件在其自己的文件中，声明为一个*ES6-模块*。

2. 组件要单独放在一个文件里

应用的当前代码可以在 [GitHub](https://github.com/fullstack-hy2020/part2-notes/tree/part2-1)上找到。

```js
├──src
	├── components
	│   ├── Note.js
	│   └── Button.js
	├── index.js
	├── index.css
	├── App.js
```

*App*也是一个组件，所以让我们在它自己的模块中声明它。 因为它是应用的根组件，所以我们将它放在 *src* 目录中。

```react
import React from 'react'

const Note = ({ note }) => {
  return (
    <li>{note.content}</li>
  )
}

export default Note

//Node.js
```

```js
//index.js
import React from 'react'
import ReactDOM from 'react-dom'
import Note from './components/Note'
const App = ({ notes }) => {
  // ...
}
```

3. 总的状态最好都放在APP根组件下，即父组件内，方便数据共享。

<mark>为了让我们的页面在添加新便笺时更新，最好将便笺存储在*App* 组件的状态中。</mark> 让我们导入[useState](https://reactjs.org/docs/hooks-state.html)函数，并使用它定义一个状态，这个状态用props传进来的初始便笺数组作为状态初始化。

受控组件：因此*App* 组件现在[控制](https://reactjs.org/docs/forms.html#controlled-components) 了input 元素的行为。note:我可以理解为是受REACT控制的组件。

```react
const App = (props) => {
  const [notes, setNotes] = useState(props.notes)
  const [newNote, setNewNote] = useState(    'a new note...'  ) 
  const addNote = (event) => {
    event.preventDefault()
    console.log('button clicked', event.target)
  }

  return (
    <div>
      <h1>Notes</h1>
      <ul>
        {notes.map(note => 
          <Note key={note.id} note={note} />
        )}
      </ul>
      <form onSubmit={addNote}>
        <input value={newNote} />        
          <button type="submit">save</button>
      </form>   
    </div>
  )
}
```

4. 使用[axios](https://github.com/axios/axios)库来代替浏览器和服务器之间的通信。

```js
npm install axios
npm install json-server --save-dev
{
  // ... 
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "server": "json-server -p3001 --watch db.json"  },
}
npm run server
```

参数之间有细微的差别。*axios* 被安装为应用的运行时依赖项 (*--save*)，因为程序的执行需要库的存在。 而另一个， *json-server* 是作为开发依赖项(*--save-dev*)安装的，因为程序本身并不需要它。 它用于在软件开发过程中提供帮助。 

```js
npx json-server --port 3001 --watch db.json
```

默认情况下，*json-server*在端口3000上启动; 但是由于 create-react-app 项目设置了3000端口，因此我们必须为 json-server 定义一个备用端口，比如端口3001。

5. axios and promises

```react
import axios from 'axios'

const promise = axios.get('http://localhost:3001/notes')
console.log(promise)

const promise2 = axios.get('http://localhost:3001/foobar')
console.log(promise2)

const promise = axios.get('http://localhost:3001/notes')

//then用于访问promise表示的操作的结果
//then 用于处理promise 返回的 你对于response 的操作
promise.then(response => {
  console.log(response)
})
```

The following is printed to the console: 下面的代码打印到控制台:

![fullstack content](https://fullstackopen.com/static/ea48db35e4b6b6ee75bd0b7795ea958c/5a190/17e.png)

```react
axios
  .get('http://localhost:3001/notes')
  .then(response => {
    const notes = response.data
    console.log(notes)
  })
```

```react
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

//未使用useEffect
import axios from 'axios'

axios
  .get('http://localhost:3001/notes')
  .then(response => {
  const notes = response.data
  
  ReactDOM.render(
    <App notes={notes} />,
    document.getElementById('root')
  )
})
```

6. 使用useEffect获取服务器数据

```react
import React, { useState, useEffect } from 'react'
import axios from 'axios' 
import Note from './components/Note'

const App = () => {  
  const [notes, setNotes] = useState([])  
  const [newNote, setNewNote] = useState('')
  const [showAll, setShowAll] = useState(true)

  useEffect(() => {    
    console.log('effect')    
    axios      
      .get('http://localhost:3001/notes')      
      .then(response => {        
      console.log('promise fulfilled')        
      setNotes(response.data)      
    })  
  }, [])  
  console.log('render', notes.length, 'notes')
  // ...
}

ReactDOM.render(<App />, document.getElementById('root'))
```

因此，默认情况下，effect是*总是* 在组件渲染之后才运行。 然而，在我们的例子中，我们只想在第一次渲染的时候执行这个效果。

*useEffect*的第二个参数用于[指定effect运行的频率](https://reactjs.org/docs/hooks-reference.html#conditionally-firing-an-effect)。 如果第二个参数是一个空数组 *[]*，那么这个effect只在组件的第一次渲染时运行。

![fullstack content](https://fullstackopen.com/static/650087bbee40291069025432f1408a29/d4713/18e.png)

7. 创建新内容，并传输post给服务器

```react
addNote = event => {
  event.preventDefault()
  const noteObject = {
    content: newNote,
    date: new Date(),
    important: Math.random() > 0.5,
  }

  axios
    .post('http://localhost:3001/notes', noteObject)
    .then(response => {
      //这里的notes是空数组，没有数据
      setNotes(notes.concat(response.data))
      setNewNote('')    
  })
}
```

8.  [template string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) 语法

```js
console.log(`importance of ${id} needs to be toggled`)
```

9. 用put替换内容给服务器

```js
const toggleImportanceOf = id => {
  const url = `http://localhost:3001/notes/${id}`
  const note = notes.find(n => n.id === id)
  const changedNote = { ...note, important: !note.important }

  axios
    .put(url, changedNote)
    .then(response => {
    setNotes(notes.map(note => note.id !== id ? note : response.data))
  })
}
```

使用[对象展开object spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)语法创建新对象的代码

10. 将与后端的通信提取到单独的模块中

```js
//src/services  notes.js
import axios from 'axios'
const baseUrl = 'http://localhost:3001/notes'

const getAll = () => {
  return axios.get(baseUrl)
}

const create = newObject => {
  return axios.post(baseUrl, newObject)
}

const update = (id, newObject) => {
  return axios.put(`${baseUrl}/${id}`, newObject)
}

export default { 
  getAll: getAll, 
  create: create, 
  update: update 
}

//update

import axios from 'axios'
const baseUrl = 'http://localhost:3001/notes'

const getAll = () => {
  const request = axios.get(baseUrl)
  return request.then(response => response.data)
}

const create = newObject => {
  const request = axios.post(baseUrl, newObject)
  return request.then(response => response.data)
}

const update = (id, newObject) => {
  const request = axios.put(`${baseUrl}/${id}`, newObject)
  return request.then(response => response.data)
}

export default { 
  getAll: getAll, 
  create: create, 
  update: update 
}
```

```react
import noteService from './services/notes'
const App = () => {}

const App = () => {
  // ...

  useEffect(() => {
    noteService      
        .getAll()      
        .then(response => {        
        setNotes(response.data)      
    })  
  }, [])

  const toggleImportanceOf = id => {
    const note = notes.find(n => n.id === id)
    const changedNote = { ...note, important: !note.important }

    noteService      
        .update(id, changedNote)      
        .then(response => {        
        setNotes(notes.map(note => note.id !== id ? note : response.data))})}

  const addNote = (event) => {
    event.preventDefault()
    const noteObject = {
      content: newNote,
      date: new Date().toISOString(),
      important: Math.random() > 0.5
    }

    noteService      
        .create(noteObject)      
        .then(response => {        
        setNotes(notes.concat(response.data))        
        setNewNote('')      
    })  
  }

  // ...
}

export default App

//update
const App = () => {
  // ...

  useEffect(() => {
    noteService
      .getAll()
    //response.data 作为 initialNotes 传入
      .then(initialNotes => {        
        setNotes(initialNotes)      
    })
  }, [])

  const toggleImportanceOf = id => {
    const note = notes.find(n => n.id === id)
    const changedNote = { ...note, important: !note.important }

    noteService
      .update(id, changedNote)
      .then(returnedNote => {        
        setNotes(notes.map(note => note.id !== id ? note : returnedNote))      
    })
  }

  const addNote = (event) => {
    event.preventDefault()
    const noteObject = {
      content: newNote,
      date: new Date().toISOString(),
      important: Math.random() > 0.5
    }

    noteService
      .create(noteObject)
      .then(returnedNote => {        
        setNotes(notes.concat(returnedNote))        
        setNewNote('')
      })
  }

  // ...
}
```

如果我们只获得响应数据，而不是整个 HTTP 响应，那么使用这个模块会更好。 使用这个模块看起来是这样的:

```js
noteService
  .getAll()
//将response.data这个数据传给initialNotes变量
  .then(initialNotes => {
    setNotes(initialNotes)
  })
```

```js
const getAll = () => {
  const request = axios.get(baseUrl)
  return request.then(response => response.data)
}

//equal
var getAll = function getAll() {
  var request = axios.get(baseUrl);
  return request.then(function (response) {
    return response.data;
    //返回response.data这个数据
  });
};
```

11. promise and error

    <mark>*catch* 方法通常是通过将其置于Promise链的更深处来使用的。promise chain</mark>

```js
axios
  .get('http://example.com/probably_will_fail')
  .then(response => {
    console.log('success!')
  })
//都是用function作出自己想处理的程序
  .catch(error => {
    console.log('fail')
  })
```

```js
const toggleImportanceOf = id => {
  const note = notes.find(n => n.id === id)
  const changedNote = { ...note, important: !note.important }

  noteService
    .update(id, changedNote)
    .then(returnedNote => {
      setNotes(notes.map(note => note.id !== id ? note : returnedNote))
    })
    .catch(error => {      
      alert(`the note '${note.content}' was already deleted from server`)      			
      setNotes(notes.filter(n => n.id !== id))
  })
}
```

```js
//还可以then多次...
axios
  .put(`${baseUrl}/${id}`, newObject)
  .then(response => response.data)
  .then(changedNote => {
    // ...
  })
  .catch(error => {
    console.log('fail')
  })
```

c. Getting data 

#### json info

json 服务器 -> 作为服务器。

项目的根目录中创建db.json文件，存储数据内容。

#### json 安装

1. 使用命令 *npm install -g json-server*在您的机器上[安装](https://github.com/typicode/json-server#getting-started) JSON 服务器
2. 在应用的根目录使用 npx 命令运行*json-server*

```js
npx json-server --port 3001 --watch db.json
```

(默认情况下，*json-server*在端口3000上启动; 但是由于 create-react-app 项目设置了3000端口，因此我们必须为 json-server 定义一个备用端口，比如端口3001。)

#### json 数据查看

输入地址 http://localhost:3001/notes

#### get data from json

use promise & fetch function , not XHR

使用[axios](https://github.com/axios/axios)库来代替浏览器和服务器之间的通信。 它的功能类似于fetch，可以从服务器中获取数据。

```js
npm install axios

//将*json-server* 安装为开发依赖项(仅在开发过程中使用)

npm install json-server --save-dev

//在*package.json* 文件的*scripts*部分添加一个小的修改,在没有参数定义的情况下方便地使用如下命令从项目根目录启动 json-server

{
  // ... 
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "server": "json-server -p3001 --watch db.json"  },
}
```

#### run both react app and json server

Then let's run "json-server" and "react-app" by running the command below:
`$ json-server --watch db.json --port 3001`
`$ npm run start`

Axios 的 *get* 方法会返回一个[promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)。

```js
import axios from 'axios'

const promise = axios.get('http://localhost:3001/notes')
console.log(promise)

promise.then(response => {
  console.log(response)
})

//常用方法

axios.get('http://localhost:3001/notes').then(response => {
  const notes = response.data
  console.log(notes)
})

//简化后

axios
  .get('http://localhost:3001/notes')
  .then(response => {
    const notes = response.data
    console.log(notes)
  })
```

1. The promise is *pending提交中*: 这意味着最终值(下面两个中的一个)还不可用。
2. The promise is *fulfilled兑现*: 这意味着操作已经完成，最终的值是可用的，这通常是一个成功的操作。 这种状态有时也被称为*resolve*。
3. The promise is *rejected拒绝*:它意味着一个错误阻止了最终值，这通常表示一个失败操作。

如果我们想要访问承诺表示的操作的结果，那么必须为承诺注册一个事件处理。 这是通过 *then*方法实现的:

React 的 effect,在渲染完成后会立即执行。对状态更新函数的调用会触发组件的重新渲染.

**... 都是副作用？？？？？？？？**

```react
import React, { useState, useEffect } from 'react'
import axios from 'axios' 
import Note from './components/Note'

const App = () => {  
  const [notes, setNotes] = useState([])  
  const [newNote, setNewNote] = useState('')
  const [showAll, setShowAll] = useState(true)

  useEffect(() => {    
    console.log('effect')    
    axios      
      .get('http://localhost:3001/notes')      
      .then(response => {        
      console.log('promise fulfilled')        
      setNotes(response.data)      
    })  
  }, [])  
  console.log('render', notes.length, 'notes')
  // ...
}
```







