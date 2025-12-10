# component & props

# 1. 组件化思想

## 1.1 组件化开发的概念和优势

1. 概念：

   - 组件：组件是应用程序的构建块，它封装了特定的功能和行为，并提供一个可定义的接口供其他组件使用。
   - 独立性：每个组件都是相对独立的，可以独立开发、测试和维护，降低了系统复杂性。
   - 可重用性：组件可以在多个地方重复使用，避免了重复编写相似的代码，提高了开发效率和代码质量。
   - 组合性：组件可以通过组合和嵌套形成更复杂的组件和应用程序结构，提供了更灵活和可扩展的开发方式。

2. 优势：

   - 模块化：组件化开发促进了代码的模块化和可维护性，使开发人员能够更好地组织和管理代码。
   - 可复用性：通过将功能封装在组件中，可以在不同的项目中重复使用组件，减少了开发时间和工作量。
   - 并行开发：不同的团队成员可以同时开发不同的组件，提高了开发效率和协作能力。
   - 易于维护：组件的独立性和清晰的接口使得维护和修复bug变得更加容易，同时降低了对整个系统的影响范围。
   - 可测试性：组件可以被独立测试，使得单元测试和集成测试更加简单和可靠。

3. 缺点：

   - 过度组件化：过度组件化是指在应用程序的规模或复杂性不足以支持组件化开发时过度使用组件化的情况。这可能导致代码过度抽象、组件层级过深、过多的组件间通信等问题，增加了系统的复杂性和维护成本。过度细分的组件可能会增加系统的复杂性，同时也可能导致性能问题。因此，在进行组件化开发时，需要权衡组件的粒度和数量。

   - 性能开销：尽管组件化可以提高代码的可重用性和模块化，但在某些情况下，过多的组件嵌套和通信可能导致性能开销。在渲染大量组件或频繁更新组件时，可能会影响应用程序的性能。在这种情况下，需要进行性能优化，例如使用PureComponent或应用其他性能优化策略。

### 引起性能问题的情况和示例

1. 过多的组件嵌套：过多的组件嵌套可能导致组件层级过深，每一层都需要进行渲染和更新操作，这可能会增加渲染的时间和资源消耗。
2. 大量的无用渲染：组件嵌套中，如果某个组件的props没有变化，但其父组件进行了更新，导致该组件被重新渲染，这可能会引起无用的渲染和性能损耗。
3. 频繁的数据传递：如果组件之间频繁地传递大量的数据，特别是在组件层级较深的情况下，数据传递的成本会增加，可能影响性能。
4. 列表渲染中的不合理操作：在进行列表渲染时，如果没有正确使用列表渲染的优化技术（例如使用key属性），可能会导致性能下降，因为React可能需要进行更多的DOM操作。
5. 过度精细化的组件拆分：过度拆分组件，将组件拆分得过于精细，可能会导致组件数量庞大，增加了组件的创建、渲染和更新的开销。
6. 不合理的组件设计和状态管理：如果组件的设计不合理，可能导致不必要的状态更新和重新渲染。同时，不合理的状态管理可能会导致性能下降和组件间通信的开销增加。

### 优化措施

1. 合理控制组件嵌套层级，避免过深的层次结构。
   1. 拆分组件：将复杂的组件拆分为更小和更简单的子组件。根据功能和责任的划分，将不同的功能模块拆分为独立的组件，每个组件专注于单一的责任。
   2. 单一职责原则：每个组件应该专注于单一的功能或目的。如果一个组件包含过多的功能，会导致组件的嵌套层级增加。通过将功能分解到不同的组件中，可以降低嵌套层级。
   3. 容器组件（Container Components）和展示/UI组件（Presentational Components）分离：将容器逻辑和展示逻辑分离开来。容器组件负责数据获取和状态管理，而展示组件负责渲染UI。这种分离可以减少嵌套层级，同时提高代码的可读性和可维护性。
   4. 组件复用：通过提取可复用的组件，避免相似的功能在多个组件中重复实现。复用组件可以减少嵌套层级，并且提高代码的可维护性。
   5. 组件组合：合理利用组件的组合性，将多个简单组件组合成更高层次的组件。通过组合而非嵌套，可以减少嵌套层级，同时提高组件的复用性和灵活性。
   6. 路由和懒加载：对于大型应用程序，可以使用路由来将不同的功能区块分割到不同的页面或路由组件中。懒加载技术可以延迟加载路由组件，减少初始加载时的嵌套层级。
2. 使用性能优化技术，例如shouldComponentUpdate或React.memo来避免无用的渲染。
3. 调整数据传递方式，避免频繁传递大量数据。
4. 对列表渲染使用合适的优化技术，例如给列表项添加唯一的key属性。
5. 在进行组件拆分时，权衡组件的粒度，避免过度拆分。
6. 合理设计和管理组件的状态，避免不必要的状态更新和渲染。

```jsx
// （Container Components）

import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import UserProfile from './UserProfile';
import { fetchUserData } from './actions';

const UserProfileContainer = () => {
  const userData = useSelector(state => state.userData);
  const isLoading = useSelector(state => state.isLoading);
  const error = useSelector(state => state.error);
  const dispatch = useDispatch();

  useEffect(() => {
    // 获取用户数据
    dispatch(fetchUserData());
  }, [dispatch]);

  return (
    <UserProfile userData={userData} isLoading={isLoading} error={error} />
  );
};

export default UserProfileContainer;

```

```jsx
// UI组件（Presentational Components）

import React from 'react';

const UserProfile = ({ userData, isLoading, error }) => {
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>{userData.name}</h1>
      <p>{userData.bio}</p>
      {/* 其他用户信息的展示 */}
    </div>
  );
};

export default UserProfile;

```

## 1.2 组件的可重用性和封装性

1. 可重用性（Reusability）：
   - 可重用性指的是组件可以在不同的上下文和场景中被多次使用。
   - 可重用的组件可以减少代码冗余，提高代码的复用性，避免重复编写相似的代码。
   - 通过将通用功能和UI封装到可重用组件中，可以在不同的项目或模块中进行共享和复用。
   - 可重用组件应该具有独立的、明确的功能，与特定的业务逻辑或数据无关，以便在各种场景中都能使用。
2. 封装性（Encapsulation）：
   - 封装性指的是将组件的实现细节隐藏起来，仅暴露必要的接口供外部使用。
   - 通过封装组件的内部实现细节，可以降低组件的使用复杂度，提供简洁的接口供其他开发者使用。
   - 封装可以避免其他组件或模块直接访问组件的内部状态和方法，从而提高代码的可靠性和安全性。
   - 封装还可以隔离组件内部的实现变化，使组件的外部使用不受影响，提供更好的代码可维护性。
3. 增强组件的可重用性和封装性，可以采取以下方法
   - 抽象通用功能：将通用的功能逻辑抽象成可重用的组件，使其独立于具体的业务场景。
   - 参数化配置：通过组件的props来接受外部传递的配置和数据，使组件可以适应不同的使用场景。
   - 容器与展示分离：将容器逻辑与展示逻辑分离，使组件更易于理解和测试，并提高可重用性。
   - 可配置性和灵活性：为组件提供灵活的配置选项，以满足不同需求的定制化要求。
   - 封装私有状态和方法：将组件内部的状态和方法封装起来，仅暴露必要的接口，减少外部对内部实现的依赖。
   - 文档和示例：提供清晰的文档和示例代码，以便其他开发者能够理解和正确使用组件。
   - 单一职责原则：确保每个组件只关注单一的功能或目的，避免组件功能过于复杂，提高可重用性和封装性。

# 2. Class 组件与函数组件的使用与区别

class vs function

## 2.1 class component

- 使用ES6的class语法来定义组件。
- 继承自React.Component类。
- 使用render()方法返回组件的JSX结构。
- 可以使用state和生命周期方法。
- 可以使用this关键字访问组件的props和state。
- 支持组件的错误边界（Error Boundaries）。
- 支持shouldComponentUpdate()来进行性能优化。
- 可以使用其他ES6+语法（例如箭头函数、类属性等）。

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  componentDidMount() {
    // 组件挂载后的逻辑
  }

  handleClick() {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <h1>{this.props.title}</h1>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.handleClick()}>Increment</button>
      </div>
    );
  }
}
```

## 2.2 function component

- 使用函数声明来定义组件。
- 无状态（stateless）组件，不需要继承自特定的类。
- 使用返回JSX结构的函数体来描述组件的UI。
- 没有内部状态，无法使用this关键字访问props和state。
- 使用React Hooks来管理组件的状态和副作用。
- 通常使用箭头函数语法来声明函数组件。
- 相对于Class组件，函数组件更简洁、易于阅读和编写。

```jsx
import React, { useState } from 'react';

const MyComponent = (props) => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <h1>{props.title}</h1>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
};
```

## 2.3 diff

**相同点：**

组件是 React 可复用的最小代码片段，它们会返回要在页面中渲染的 React 元素。也正因为组件是 React 的最小编码单位，所以无论是函数组件还是类组件，在使用方式和最终呈现效果上都是完全一致的。

我们甚至可以将一个类组件改写成函数组件，或者把函数组件改写成一个类组件（虽然并不推荐这种重构行为）。从使用者的角度而言，很难从使用体验上区分两者，而且在现代浏览器中，闭包和类的性能只在极端场景下才会有明显的差别。所以，基本可认为两者作为组件是完全一致的。

**不同点**

|                          | 类组件(class)                                                | 函数组件(hooks)                                              |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 开发时的心智模型上的差异 | 基于面向对象编程的，它主打的是继承、生命周期等核心概念       | 内核是函数式编程，主打的是 immutable、没有副作用、引用透明等特 |
| 使用场景上（class劣势）  | 1. 如果存在需要使用生命周期的组件<br />2. 设计模式上，如果需要使用继承 | 由于 React Hooks 的推出，生命周期概念的淡出，函数组件可以完全取代类组件。其次继承并不是组件最佳的设计模式，官方更推崇“组合优于继承”的设计概念，所以类组件在这方面的优势也在淡出 |
| 性能优化                 | 类组件主要依靠 shouldComponentUpdate 阻断渲染来提升性能      | 而函数组件依靠 React.memo 缓存渲染结果来提升性能。           |
| 上手程度                 | 类组件更容易上手                                             | 从未来趋势上看，由于React Hooks 的推出，函数组件成了社区未来主推的方案 |
| 未来时间切片与并发模式   | 由于生命周期带来的复杂度，并不易于优化                       | 函数组件本身轻量简单，且在 Hooks 的基础上提供了比原先更细粒度的逻辑组织与复用，更能适应 React 的未来发展 |

```js
  useEffect(() => {
    const timeout = setTimeout(() => setVarA(varA + 1), 1000);
    return () => clearTimeout(timeout);
  }, [varA]);
```

| class component          | Function component          |
| ------------------------ | --------------------------- |
| constructor              | useState                    |
| getDerivedStateFromProps | useState里的update function |
| shouldComponentUpdate    | useMemo                     |
| render                   | render                      |
| componentDidMount        | useEffect                   |
| componentDidUpdate       | useEffect                   |
| componentWillUnmount     | useEffect 里的返回函数      |
| componentDidMatch        | -                           |
| getDerivedStateFromError | -                           |

# 3. 组件渲染、拆分、组合

## 3.1 组件渲染

### 3.1.1 JSX语法

JSX（JavaScript XML）是一种在JavaScript代码中编写类似于XML/HTML的语法扩展，用于描述React组件的UI结构。它允许在JavaScript中直接编写HTML标记和组件的结构，以更直观和声明性的方式创建用户界面。

JSX的特点和语法规则如下：

1. XML/HTML类似的语法：JSX使用类似于XML/HTML的标记语法，可以直接在JavaScript中编写标签和元素。
2. 标签和元素：使用尖括号（<>）包围标签或元素，例如`<div>...</div>`。
3. 嵌套：可以嵌套标签和元素，形成层次结构。
4. 表达式插值：使用花括号（{}）将JavaScript表达式嵌入到JSX中，例如`<p>Hello, {name}!</p>`，其中`name`是一个变量。
5. 属性：标签可以包含属性，属性使用类似于HTML的语法，例如`<img src="image.jpg" alt="Image" />`。
6. 类名和样式：使用`className`属性代替HTML中的`class`属性来指定CSS类名，使用`style`属性指定内联样式。
7. 注释：使用花括号（`{}`）将JavaScript注释嵌入到JSX中，例如`{/* This is a comment */}`。

```jsx
import React from 'react';

const MyComponent = () => {
  const name = 'John';
  const isActive = true;

  return (
    <div className="container">
      <h1>Hello, {name}!</h1>
      <p className={isActive ? 'active' : 'inactive'}>
        {isActive ? 'Active' : 'Inactive'}
      </p>
      {/* This is a comment */}
    </div>
  );
};
```

### 3.1.2 渲染组件的基本方法

在React中，渲染组件有几种基本的方法：

1. ReactDOM.render()：

   - 通过ReactDOM.render()方法将组件渲染到指定的DOM元素中。

     ```jsx
     import React from 'react';
     import ReactDOM from 'react-dom';
     import App from './App';
     
     ReactDOM.render(<App />, document.getElementById('root'));
     ```

2. React.createElement()：

   - 使用React.createElement()方法创建React元素，并将其渲染到指定的DOM元素中。这种方式比较底层

     ```jsx
     import React from 'react';
     import ReactDOM from 'react-dom';
     
     const element = React.createElement('h1', null, 'Hello, World!');
     ReactDOM.render(element, document.getElementById('root'));
     ```

3. 类组件和函数组件：

   - 将类组件或函数组件直接作为JSX的标签来使用，以渲染组件到指定的DOM元素中。

     ```jsx
     import React from 'react';
     import ReactDOM from 'react-dom';
     
     class App extends React.Component {
       render() {
         return <h1>Hello, World!</h1>;
       }
     }
     
     ReactDOM.render(<App />, document.getElementById('root'));
     ```

### 3.1.3 条件渲染和循环渲染

条件渲染和循环渲染是在React中根据特定条件或数据进行动态渲染的常见技术。下面分别介绍条件渲染和循环渲染的方法。

1. 条件渲染：
   - 条件渲染用于根据特定条件选择性地渲染组件或元素。
   - 最常见的方法是使用条件语句（如if语句或三元表达式）在组件的render()方法中进行条件判断，并返回不同的JSX内容。

```jsx
import React from 'react';

class ConditionalRender extends React.Component {
  render() {
    const isLoggedIn = this.props.isLoggedIn;

    return (
      <div>
        {isLoggedIn ? (
          <h1>Welcome, User!</h1>
        ) : (
          <h1>Please log in.</h1>
        )}
      </div>
    );
  }
}
```

2. 循环渲染：

- 循环渲染用于根据数据集合动态地渲染多个组件或元素。
- 使用数组的map()方法可以遍历数据集合，并返回由每个数据项对应的组件或元素构成的新数组。

```jsx
import React from 'react';

class ListRender extends React.Component {
  render() {
    const items = this.props.items;

    return (
      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    );
  }
}
```

3. 逻辑运算符（如逻辑与（`&&`）和逻辑或（`||`））进行渲染

```jsx
import React from 'react';

class ConditionalRender extends React.Component {
  render() {
    const isLoggedIn = this.props.isLoggedIn;
    const isAdmin = this.props.isAdmin;

    return (
      <div>
        {isLoggedIn && <h1>Welcome, User!</h1>}
        {isAdmin || <h1>You are not an admin.</h1>}
      </div>
    );
  }
}
```

如果isAdmin为false，则渲染`<h1>You are not an admin.</h1>`，否则不渲染。

## 3.2 组件拆分与组合
### 3.2.1 拆分组件的目的和原则

拆分组件是指将一个大型的组件拆分为多个小而独立的组件，以实现组件的复用、可维护性和可测试性。拆分组件的目的是使代码结构更清晰、可读性更好，并促进团队协作和开发效率。

以下是拆分组件的一些目的和原则：

1. 单一职责原则（Single Responsibility Principle）：每个组件应该专注于完成单一的任务或职责。拆分组件可以将复杂的功能划分为更小、更专注的单元，使得每个组件的职责更加清晰。
2. 可复用性（Reusability）：拆分组件可以将通用的功能或UI元素抽象成可复用的组件，使得这些组件可以在不同的场景中重复使用，提高开发效率。
3. 组件的可维护性（Maintainability）：将组件拆分为较小的部分可以降低代码的复杂性，使得每个组件更容易理解、调试和维护。当需要修改某个特定功能时，只需关注相关的组件，而不会影响到其他部分。
4. 解耦和模块化（Decoupling and Modularity）：拆分组件可以将不同的功能模块解耦，使得它们之间的依赖性降低。这样，当某个模块需要修改或替换时，只需关注该模块本身，而不会影响到其他模块。
5. 可测试性（Testability）：拆分组件可以使单元测试更加容易。每个小组件都可以独立测试，减少了测试的复杂性和依赖关系。
6. 层次分明（Hierarchical Clarity）：拆分组件可以形成更清晰的层次结构，使得整个应用的架构更易于理解和组织。不同层次的组件可以通过组合的方式构建复杂的UI结构。

在拆分组件时，需要根据具体的业务需求和UI设计，合理划分组件的边界，遵循单一职责原则，使得每个组件都具有清晰的目标和功能。同时，需要考虑组件之间的通信和数据传递方式，选择合适的组件间通信机制（如Props、Context、Redux等）来满足业务需求。

### 3.2.2 如何拆分复杂组件为简单组件

拆分复杂组件为简单组件是一种有效的方式，可以提高代码的可读性、可维护性和复用性。下面是一些常见的方法和技巧，可用于拆分复杂组件为简单组件：

1. 单一职责原则：确保每个组件只负责完成单一的任务或职责。识别复杂组件中的不同功能区块，将其拆分为独立的简单组件。
2. 分层拆分：将复杂组件分解为多个层次结构清晰的简单组件。每个简单组件都负责处理特定的功能或UI元素。
3. 提取可复用组件：识别和提取出可以在多个地方重复使用的功能或UI元素，并将其封装为独立的可复用组件。
4. 组件组合：通过组合多个简单组件来构建复杂组件。将复杂组件拆分为各个独立的功能单元，然后通过组件的嵌套和组合来实现复杂的功能。
5. 参数化组件：将复杂组件中的可变部分提取为组件的参数，使得组件可以根据不同的输入数据展示不同的内容或行为。
6. 提取逻辑：将复杂组件中的业务逻辑或数据处理逻辑提取出来，封装为独立的函数或自定义钩子，使得组件的代码更加清晰和可维护。
7. 逐步迭代：从复杂组件的整体结构入手，逐步将其拆分为简单组件。一开始可以选择拆分一小部分，逐步迭代和优化，直到达到理想的拆分程度。
8. 反馈循环：与团队成员或其他开发者一起进行代码审查和反馈。他们可能能够提供有价值的见解和意见，帮助优化组件的拆分和设计。
9. 测试和优化：在拆分后的简单组件中进行单元测试，确保它们的功能正常。根据需要对简单组件进行优化和性能调整，确保整体应用的性能和用户体验。

### 3.2.3 组合组件的方法和技巧

1. 使用Props进行数据传递：通过Props将数据和回调函数传递给子组件，使得子组件可以接收和处理父组件传递的数据。这样可以实现父子组件之间的通信和数据共享。
2. 嵌套组件：将一个组件嵌套在另一个组件的JSX中，以实现组件的嵌套和组合。通过这种方式，可以将多个简单组件组合成一个更复杂的组件，形成层次结构。
3. 子组件作为插槽（Slot）：使用特定的插槽组件作为父组件的子组件，允许父组件在指定位置插入自定义内容。这种技巧使得父组件更加灵活，可以根据需要自定义其内容。(Props.children)
4. 高阶组件（Higher-Order Components）：高阶组件是一个接受一个组件作为输入，并返回一个新组件的函数。通过高阶组件，可以在不修改原始组件的情况下，添加或修改其功能。这种方法使得组件的功能组合更加灵活。
5. 渲染属性（Render Props）：渲染属性是指将一个函数作为组件的子组件，通过该函数将组件内部的状态或逻辑暴露给父组件。父组件可以通过调用该函数，并接收其返回的内容来自定义子组件的渲染。
6. 使用组件库和UI框架：利用现有的组件库和UI框架，可以通过组合已有的组件来构建复杂的UI。这些组件库和UI框架通常提供了丰富的组件选项和灵活的组合方式，可以加快开发速度。
7. 抽象复用逻辑：如果多个组件之间存在共享的逻辑或行为，可以将这部分逻辑提取为一个独立的组件，然后在需要的地方使用。通过抽象复用逻辑，可以减少重复的代码，并提高代码的可维护性。

# 4. props的只读属性

- 理解 Props 的只读特性，避免在组件中直接修改 Props 的值/理解Props的只读特性以及其在组件中的应用

## 4.1 Props intro
### 4.1.1 解释什么是Props（属性）

在React中，Props是组件之间传递数据的一种机制。Props是组件的属性，用于从父组件向子组件传递数据。每个React组件都可以接收Props作为输入，并根据这些Props来渲染不同的内容或执行相应的行为。

Props是通过在父组件中使用组件标签的属性来传递给子组件的。父组件可以为子组件定义Props，并将其作为属性传递给子组件。子组件则可以在其代码中通过Props来访问和使用这些传递过来的属性值。

Props具有只读特性，意味着子组件无法直接修改从父组件传递过来的Props。它们被设计为一种单向数据流的机制，父组件作为数据的源头，通过Props向下传递数据给子组件。这种单向数据流的设计有助于保持组件的独立性和可维护性。

通过使用Props，可以将数据从父组件传递到子组件，并在子组件中使用这些数据来渲染UI、定义行为或控制组件的状态。Props可以包含任何类型的数据，包括字符串、数字、布尔值、对象、函数等。

总结来说，Props是React组件之间传递数据的一种机制，通过在父组件中定义和传递属性给子组件，实现了组件之间的数据传递和交互。这种单向数据流的设计方式使得React组件更加可组合、可重用和易于维护。

### 4.1.2 Props的作用和目的

1. 数据传递：Props允许在React组件之间传递数据。父组件可以通过定义Props，并将其作为属性传递给子组件，从而将数据传递给子组件。这样的数据传递机制使得组件之间可以共享和传递数据，实现了组件间的通信。
2. 动态内容：通过Props，可以使组件的内容动态化。父组件可以根据需要动态地改变Props的值，从而影响子组件的渲染结果。这使得组件能够根据不同的数据或条件呈现不同的内容，提供了灵活性和可重用性。
3. 组件配置：Props可以用于配置组件的行为和外观。通过将不同的配置参数传递给组件的Props，可以自定义组件的样式、状态和行为。这样的配置机制使得组件具有可定制性，适应不同的使用场景。
4. 数据注入：Props可以用于注入外部数据到组件中。父组件可以将数据从外部源（如API响应、状态管理库）获取，并通过Props传递给子组件，使子组件能够访问和使用这些数据。
5. 参数传递：通过Props，可以向组件传递参数。父组件可以将回调函数作为Props传递给子组件，子组件可以调用这些回调函数并传递参数，实现组件间的交互和事件处理。
6. 数据源管理：Props可以帮助组件维护其数据源的来源。通过Props，可以明确指定哪些数据是由父组件提供的，以及如何在组件内部使用这些数据。

总的来说，Props在React中起到了数据传递、动态内容呈现、组件配置、数据注入、参数传递和数据源管理等多个作用和目的。它是实现组件之间通信和数据交互的重要机制，使得React应用具有灵活性、可扩展性和可维护性。

## 4.2 Props的只读特性

Props在组件中是只读的，不允许在组件内部直接修改Props的值

Props被设计为一种向下传递数据的机制，用于从父组件向子组件传递数据，子组件只能读取Props的值，而不能修改它们

==React中的props为什么是只读的?==

==`props`就是汲取了纯函数的思想。props的不可以变性就保证的相同的输入，页面显示的内容是一样的，并且不会产生副作用==

1. 单向数据流：React遵循单向数据流的原则，数据的流动是自上而下的，即从父组件向子组件传递。Props的只读性确保了数据流的一致性和可控性，父组件作为数据的源头，可以通过Props向子组件传递数据，而子组件只能读取这些数据，而无法修改它们。这种单向数据流使得数据变化更易于追踪和管理，避免了数据的混乱和不一致性。
2. 组件的纯粹性：React鼓励组件的纯粹性，即组件的行为和渲染结果应该只依赖于输入（Props）和内部状态（State），而不依赖于其他外部因素。如果组件能够直接修改Props的值，那么它的行为将变得不确定，可能引入副作用，增加了组件的复杂性和不可预测性。通过保持Props的只读性，组件的行为和渲染结果更易于理解和预测，有助于组件的测试、调试和维护。
3. 性能优化：React使用虚拟DOM和Diff算法来进行高效的渲染。Props的只读性使得React可以进行优化，例如通过比较Props的值是否发生变化来判断是否需要重新渲染组件。如果Props是可变的，React需要深入比较Props的值，可能引入额外的开销和性能损失。通过保持Props的只读性，React可以进行浅比较，从而更快地确定是否需要重新渲染组件。
4. 函数式编程的原则：在函数式编程中，数据被视为不可变的，函数的输入应该保持不变性。将Props设置为只读符合函数式编程的原则，使得组件更易于理解、测试和推理。

将Props设置为只读有助于保持数据流的可控性，提高组件的独立性和性能优化，并符合函数式编程的原则。它是React框架设计中的一部分，旨在提供可维护、可靠和高效的组件开发体验。

`props`是组件之间沟通的一个接口，原则上来讲，它只能从父组件流向子组件。React具有浓重的函数式编程的思想。

提到函数式编程就要提一个概念：纯函数。它有几个特点：

- 给定相同的输入，总是返回相同的输出。
- 过程没有副作用。
- 不依赖外部状态。

# 5. pure component

## 5.1. PureComponent intro
### 5.1.1 什么是PureComponent

PureComponent是React中提供的一个优化性能的组件类，它是React.Component的一个变体。与普通的Component相比，PureComponent具有自动实现shouldComponentUpdate方法的功能，通过浅比较（shallow comparison）来判断是否重新渲染组件。

PureComponent的主要特点和作用如下：

1. 自动实现shouldComponentUpdate：PureComponent会自动比较组件的当前Props和状态（this.props和this.state）与前一个Props和状态的浅层比较。如果它们相等，则不会触发重新渲染，从而减少不必要的渲染开销。这样的比较是在React内部进行的，无需手动编写shouldComponentUpdate方法。
2. 性能优化：由于PureComponent自动实现了shouldComponentUpdate方法并进行浅比较，它可以避免在某些情况下不必要的渲染。当组件的Props和状态没有发生变化时，React不会触发组件的重新渲染，从而提高应用程序的性能。
3. 使用简便：使用PureComponent与使用普通Component基本一致，只需将组件类继承自React.PureComponent而不是React.Component。其他用法和生命周期方法都相同，无需特殊的配置或使用。

PureComponent的浅比较只能比较对象和数组的引用，对于深层次的对象比较可能无法正常工作。因此，在使用PureComponent时，需要确保传递给组件的对象和数组是不可变的，避免直接修改它们的值。

PureComponent是React提供的一个方便的性能优化工具，它通过自动实现shouldComponentUpdate方法和浅比较来减少组件的不必要渲染，提高应用程序的性能。在适当的场景下，使用PureComponent可以简化代码并提供更好的用户体验。

#### 使用举例

1. class component

```jsx
class MyComponent extends React.Component {
  state = {
    count: 0
  };

  shouldComponentUpdate(nextProps, nextState) {
    // 只有当count发生变化时才触发重新渲染
    if (this.state.count !== nextState.count) {
      return true;
    }
    return false;
  }

  handleClick = () => {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  }

  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <button onClick={this.handleClick}>Increment</button>
      </div>
    );
  }
}
```

2. function component

在函数式组件中，没有`shouldComponentUpdate`方法可供直接使用，因为函数式组件没有实例和生命周期方法。相反，使用React提供的`memo`高阶组件来包装函数组件，并进行浅比较来决定是否重新渲染组件。

在函数组件中，无法直接使用`PureComponent`，因为`PureComponent`是一个类组件的特性。

```jsx
import React, { memo } from 'react';

function MyComponent(props) {
  // 组件的渲染逻辑
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.content}</p>
    </div>
  );
}

export default memo(MyComponent);
```

```jsx
import React from 'react';

function MyComponent(props) {
  // 组件的渲染逻辑

  return (
    <div>
      {/* 组件的内容 */}
    </div>
  );
}

// 使用 React.memo 包装函数式组件
const MemoizedComponent = React.memo(MyComponent, (prevProps, nextProps) => {
  // 返回 true 表示 nextProps 等于 prevProps，不需要重新渲染
  // 返回 false 表示 nextProps 不等于 prevProps，需要重新渲染
  // 这里可以根据 props 的具体比较逻辑进行判断

  // 例如，只有当 count 发生变化时才重新渲染组件
  if (prevProps.count === nextProps.count) {
    return true;
  }
  return false;
});

```

在上面的示例中，`React.memo`函数用于包装`MyComponent`函数式组件，并传递一个比较函数作为第二个参数。比较函数接收两个参数：`prevProps`和`nextProps`，表示前一个和下一个Props的值。在比较函数中，根据需要进行Props的比较，并决定是否返回`true`（不需要重新渲染）或`false`（需要重新渲染）。

在这个例子中，我们只在`count`发生变化时重新渲染组件，其他的Props不会触发重新渲染。通过使用`React.memo`和自定义的比较函数，我们可以优化函数式组件的性能，避免不必要的重新渲染。

需要注意的是，`React.memo`的比较函数默认使用浅比较来比较对象和数组的引用。如果需要进行深层比较，可以使用自定义的深比较函数。同时，对于函数式组件中的状态更新，可以使用React的Hooks，例如`useState`和`useEffect`来实现类似的效果。

3. purecomponent

```jsx
class MyComponent extends React.PureComponent {
  state = {
    count: 0
  };

  handleClick = () => {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  };

  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <button onClick={this.handleClick}>Increment</button>
      </div>
    );
  }
}
```

`MyComponent`是一个继承自`React.PureComponent`的类组件。由于`MyComponent`继承自`PureComponent`，它自动具备了`shouldComponentUpdate`方法的功能。

在`MyComponent`中，有一个`count`的状态，并通过点击按钮来增加`count`的值。每次点击按钮时，`setState`方法会更新组件的状态，并触发重新渲染。由于`MyComponent`继承自`PureComponent`，它会自动进行浅比较，判断是否需要重新渲染。如果`count`的值没有发生变化，`PureComponent`会阻止重新渲染，从而提高性能。

使用`PureComponent`时，需要确保组件的Props和状态是不可变的，避免直接修改它们的值。如果Props或状态是可变的，即使值没有发生变化，浅比较也会返回`false`，导致组件重新渲染。

### 5.1.2 PureComponent与普通Component的区别

1. 自动浅比较：`PureComponent`自动实现了`shouldComponentUpdate`方法，并通过浅比较来决定是否重新渲染组件。它会对组件的Props和状态进行浅比较，只有在发生变化时才会触发重新渲染。而普通的`Component`需要手动编写`shouldComponentUpdate`方法来控制组件的更新。
2. 性能优化：由于`PureComponent`实现了自动的浅比较和更新判断，它可以减少不必要的重新渲染，提高应用程序的性能。对于那些具有稳定Props和状态的组件，使用`PureComponent`可以避免不必要的渲染操作，提升性能。
3. 属性和状态的更新：`PureComponent`对属性和状态的更新有一些限制。它依赖于浅比较，只有在属性和状态的引用发生变化时才会触发重新渲染。对于复杂的对象和数组，如果直接修改其内部值而不改变引用，`PureComponent`无法正确检测到变化。这时候，需要确保使用不可变的数据结构或手动进行深层比较。
4. 类组件 vs 函数组件：`PureComponent`适用于类组件，通过继承`React.PureComponent`来创建。而函数组件不能直接使用`PureComponent`，但可以使用`React.memo`来实现类似的浅比较和性能优化。

`PureComponent`是一个方便的性能优化工具，通过自动实现`shouldComponentUpdate`和浅比较来减少组件的不必要渲染。它适用于那些具有稳定Props和状态的组件，可以提高应用程序的性能和效率。在使用时需要注意对属性和状态的更新方式，并确保使用不可变的数据结构来保证比较的准确性。

## 5.2. PureComponent 原理

`PureComponent`的原理是通过继承`Component`并重写`shouldComponentUpdate`方法来实现的。

当使用`PureComponent`创建一个组件时，它会自动继承`Component`的所有功能，并且在内部实现了一个优化的`shouldComponentUpdate`方法。默认情况下，`shouldComponentUpdate`会比较组件的Props和状态的浅层次引用是否发生变化，以决定是否触发重新渲染。

具体的原理可以概括为以下几点：

1. `PureComponent`在内部维护了一个浅层次的Props和状态的快照（shallow copy），用于与新的Props和状态进行比较。
2. 在组件进行更新时，`PureComponent`会在`shouldComponentUpdate`方法中对比新的Props和状态与之前的快照是否发生变化。它会逐个比较Props和状态的每个属性，并使用浅比较（shallow comparison）来检查它们是否相等。
3. 如果所有的Props和状态的属性都相等（即没有发生变化），则`shouldComponentUpdate`返回`false`，告诉React不需要进行重新渲染。这样可以节省渲染的开销，提高性能。
4. 如果至少一个Props或状态的属性发生变化，`shouldComponentUpdate`返回`true`，React会继续进行组件的重新渲染。

需要注意的是，`PureComponent`仅执行浅比较，它只能比较对象和数组的引用是否相等。对于深层次的对象比较，或者引用类型的属性内容发生变化的情况，浅比较可能会导致误判。在这种情况下，需要特别注意传递给`PureComponent`的Props和状态的不可变性，或者考虑使用其他深层比较的方式。

总结起来，`PureComponent`通过继承`Component`并重写`shouldComponentUpdate`方法实现了自动的浅比较和性能优化。它通过比较组件的Props和状态的浅层次引用来判断是否需要重新渲染组件，从而减少不必要的渲染，提高应用程序的性能。

## 5.3 PureComponent 优点

1. 自动浅比较：`PureComponent`自动实现了`shouldComponentUpdate`方法，并对组件的Props和状态进行浅比较。只有当Props或状态发生变化时，才会触发重新渲染。这样可以避免不必要的渲染，提高组件的性能。
2. 减少渲染次数：由于自动浅比较的特性，`PureComponent`能够减少组件的渲染次数。当组件的Props或状态没有发生变化时，`PureComponent`会直接使用之前的渲染结果，避免了重新渲染的开销。
3. 简化代码：使用`PureComponent`可以简化代码，无需手动编写`shouldComponentUpdate`方法进行比较。它提供了一种更简洁的方式来实现组件的性能优化。
4. 默认性能优化：将普通的`Component`替换为`PureComponent`，可以获得一定的性能优化。`PureComponent`的浅比较能够自动处理Props和状态的变化，避免不必要的重新渲染。
5. 适用于大部分情况：`PureComponent`适用于大部分场景下的性能优化。对于具有稳定Props和状态的组件，使用`PureComponent`能够获得较好的性能提升。

尽管`PureComponent`能够提供性能优化，但它也有一些限制和注意事项，如对对象和数组的浅比较、Props类型的考虑等。在使用`PureComponent`时，需要确保其适用于组件的特定场景，并了解其工作原理和使用方式。对于一些特殊情况，可能需要手动编写`shouldComponentUpdate`方法来精确控制组件的更新逻辑。

## 5.4 PureComponent 缺点/限制

尽管`PureComponent`可以带来性能上的优势，但它也有一些限制和注意事项：

- 只适用于浅比较：`PureComponent`只进行浅比较，对于深层次的对象比较可能无法正常工作。它只比较引用类型的引用是否相同，而不会深入比较对象的内部值。如果组件的Props或状态包含了引用类型的数据，并且这些数据在每次渲染中都是新的，那么浅比较可能会误判为Props或状态发生了变化，导致不必要的重新渲染。
- 对象和数组的变更：由于浅比较只比较引用是否相同，对于修改了对象或数组内部值的情况，`PureComponent`无法感知到变化，仍然会误判为Props或状态没有发生变化。因此，使用`PureComponent`时需要确保传递给组件的对象是不可变的，避免直接修改它们的值。
- 函数引用的变化：如果组件的Props中包含函数引用，并且这些函数在每次渲染时都是新的，`PureComponent`也会误判为Props发生了变化，导致不必要的重新渲染。在这种情况下，可以使用`useCallback`等技术来缓存函数引用，以确保函数引用的稳定性。
- 需要考虑Props的类型：在使用`PureComponent`时，需要考虑传递给组件的Props的类型。如果Props中包含了不可变的数据类型，如字符串、数字等，那么`PureComponent`能够正常工作。但如果Props中包含了可变的引用类型数据，如对象、数组等，就需要注意浅比较的限制和可能的误判情况。
- 不适用于所有场景：`PureComponent`适用于大部分情况下的性能优化，但并不适用于所有场景。在某些特殊情况下，可能需要手动编写`shouldComponentUpdate`方法，以精确控制组件的更新逻辑。

## 5.5 PureComponent vs React.memo

`PureComponent`和`React.memo`都是用于性能优化的工具，但在使用上有一些区别：

1. 类型差异：`PureComponent`是一个类组件，而`React.memo`是一个高阶函数，可以用于包装函数组件。
2. 比较方式：`PureComponent`使用浅比较来确定是否进行重新渲染，而`React.memo`使用浅比较或自定义比较函数来确定是否重新渲染。
3. 适用范围：`PureComponent`适用于类组件，可以自动检测并优化渲染性能。`React.memo`适用于函数组件，通过对组件的输入进行比较来决定是否重新渲染。
4. 使用场景：`PureComponent`适用于具有稳定Props和状态的组件，并且可以减少不必要的重新渲染。`React.memo`适用于函数组件，可以缓存组件的渲染结果并在下一次渲染时比较输入是否发生变化，避免不必要的渲染。
5. 自定义比较函数：在某些情况下，`React.memo`可以使用自定义的比较函数来进行更精确的比较。通过指定自定义比较函数，可以根据组件的具体需求决定是否重新渲染。

> 在 `PureComponent` 中，你无法直接提供自定义的比较函数来替代默认的浅比较。`PureComponent` 使用浅比较来决定是否重新渲染组件，它会比较新旧 `props` 和 `state` 的引用是否相等，以决定是否触发重新渲染。
>
> 如果你需要自定义比较逻辑来决定 `PureComponent` 是否重新渲染，你可以通过重写 `shouldComponentUpdate` 方法来实现。你可以在 `shouldComponentUpdate` 方法中编写自定义的比较逻辑，并根据你的需求返回 `true` 或 `false`。

```jsx
// 自定义比较函数

import React from 'react';

function MyComponent(props) {
  // 组件的渲染逻辑

  // ...

  console.log('MyComponent render');

  return (
    // 组件的 JSX 结构
    // ...
  );
}

function areEqual(prevProps, nextProps) {
  // 自定义的比较逻辑
  // 返回 true 表示两次渲染的 props 相等，不需要重新渲染
  // 返回 false 表示两次渲染的 props 不相等，需要重新渲染

  // 例如，只比较 props 中的 name 字段
  return prevProps.name === nextProps.name;
}

export default React.memo(MyComponent, areEqual);

```

`PureComponent`适用于类组件，通过自动的浅比较来减少不必要的重新渲染。`React.memo`适用于函数组件，通过浅比较或自定义比较函数来确定是否重新渲染。两者都是为了优化性能而设计，但应根据组件的类型和需求选择合适的工具。

## 5.7 性能优化

1. 减少虚拟 DOM 的比较和更新：由于 `PureComponent` 在进行浅比较时，只会比较对象的引用是否相等，而不会深层次比较对象的内容。这使得在虚拟 DOM 的比较和更新过程中减少了对子组件树的递归比较。当组件的 `props` 和 `state` 没有发生变化时，`PureComponent` 可以快速判断组件不需要重新渲染，从而减少了虚拟 DOM 比较的时间和性能开销。
2. 自动比较：`PureComponent` 会自动进行比较，无需手动编写比较逻辑。它会根据新旧`props`和`state`的引用来判断是否重新渲染组件，减少了开发人员的工作量。
3. 更少的渲染操作：由于 `PureComponent` 可以避免不必要的重新渲染，它可以减少组件树中的渲染操作次数。渲染是一个相对昂贵的操作，它涉及创建和更新 DOM 元素、执行组件的生命周期方法等。通过减少渲染操作，`PureComponent` 提供了更高效的渲染性能，可以使应用程序更加流畅和响应快速。
4. 提高应用性能：通过减少不必要的重新渲染，`PureComponent` 可以有效地提高整个应用程序的性能。特别是在组件层级较深、组件数量较多的情况下，使用 `PureComponent` 可以减少组件的渲染和调和成本，提升应用的性能和响应速度。

`PureComponent` 只对浅层次的比较有效，如果组件的 `props` 或 `state` 中包含复杂的数据结构，如对象或数组，且这些数据结构的值发生变化，但引用并未改变，`PureComponent` 可能无法正确地检测到变化，导致不必要的重新渲染。在这种情况下，需要使用深比较或其他手段来确保组件的正确性和性能优化。























