## 1. TypeScript 和 JavaScript 的主要区别是什么？

TypeScript 是 JavaScript 的**超集**，在 JS 的基础上增加了**静态类型系统**。

## 2. 什么是 TypeScript 的类型推断？

类型推断是指：**在没有显式声明类型时，TypeScript 会根据上下文自动推断变量或返回值的类型**。

## 3. 如何为函数定义返回类型？

在函数参数列表后使用冒号声明返回类型

## 4. 解释一下 TypeScript 中的联合类型（Union Types）和交叉类型（Intersection Types）

**联合类型（|）**：值可以是多种类型之一

**交叉类型（&）**：同时满足多个类型

## 5. 什么是 TypeScript 中的泛型（Generics）？如何使用泛型？

泛型允许在**定义时不指定具体类型，使用时再确定类型**。

## 6. 在 TypeScript 中，如何创建一个枚举类型（Enum）？



## 7. TypeScript 中的“never”类型是什么？它有什么用？

`never` 表示**永远不会发生的值**。

常见场景：

1. 永远抛异常的函数
2. 不可能走到的分支

```js
function error(): never {
  throw new Error('error');
}
```

## 8. 解释一下 TypeScript 中的“any”类型和“unknown”类型的区别。

| 类型    | 特点                     |
| ------- | ------------------------ |
| any     | 关闭类型检查             |
| unknown | 必须先做类型判断才能使用 |

## 9. 在 TypeScript 中，如何声明一个可选属性？


## 10. 你如何在 TypeScript 中声明一个类（Class）？

```js
class Person {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  sayHi() {
    console.log(this.name);
  }
}
// TS 支持 public / private / protected 修饰符。
```

## 11. TypeScript 中如何实现接口（Interface）？

```js
interface Flyable {
  fly(): void;
}

class Bird implements Flyable {
  fly() {}
}
```

## 12. ==解释一下“类型别名（Type Alias）”和“接口（Interface）”的区别。==

interface 和 type 都可以用来定义类型。
interface 更偏向于描述对象结构，支持声明合并，适合公共 API 和类的约束。
type 更灵活，可以定义联合类型、基础类型别名、条件类型和映射类型，适合复杂类型运算。
实际开发中，一般对象结构优先用 interface，其它情况用 type。

| 对比点   | interface | type     |
| -------- | --------- | -------- |
| 扩展     | extends   | &        |
| 声明合并 | 支持      | 不支持   |
| 使用场景 | 对象结构  | 任意类型 |

**对象结构用 interface**

**复杂类型用 type**

## 13. 在 TypeScript 中，如何使用模块（Module）？

## 14. 什么是 TypeScript 中的“声明文件（.d.ts）”？它有什么作用？

`.d.ts` 用于**为 JS 代码提供类型声明**。

作用：

- 让 TS 识别 JS 库的类型
- 不包含实现，只描述类型

常见于第三方库。

## 15. 在 TypeScript 中，如何处理函数重载？
## 16. 解释 TypeScript 中的“泛型约束”。

使用 `extends` 限制泛型类型范围：

```js
function getLength<T extends { length: number }>(obj: T) {
  return obj.length;
}
```

保证泛型具备某些能力。

## 17. 如何使用 TypeScript 中的“映射类型（Mapped Types）”？

通过遍历类型属性生成新类型：

```js
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

常用于：

- Readonly
- Partial
- Pick

## 18. TypeScript 中如何处理类的继承？

使用 `extends`：

```js
class Animal {
  move() {}
}

class Dog extends Animal {
  bark() {}
}
```

支持方法重写与 `super` 调用。

## 19. TypeScript 中的“类型守卫（Type Guards）”是什么？举个例子。

用于**在运行时缩小类型范围**。

常见方式：

- `typeof`
- `instanceof`
- 自定义断言

```
if (typeof x === 'string') {
  x.toUpperCase();
}
```

## 20. 解释 TypeScript 中的“类型推导”与“类型注解”之间的区别。

作为前端开发，TypeScript (TS) 的面试题通常不会只考定义，而是考你对**类型安全、工程化实践以及复杂逻辑建模**的理解。

我为你整理了从“基础核心”到“高级进阶”的经典面试连环炮：

------

### 1. 基础概念：`any` vs `unknown` vs `never`

这是考察你对 TS 类型系统边界的理解。

- **any**: 彻底放弃类型检查，它是所有类型的顶级类型，也是底层类型。
- **unknown**: 安全的顶级类型。你可以把任何值赋给 `unknown`，但在对其进行操作前，必须进行**类型守卫**（Type Guard）或**类型断言**。
- **never**: 表示永远不会出现的值的类型。常用于：
  - 总是抛出异常的函数返回值。
  - 死循环函数。
  - 在 `switch` 的 `default` 分支做**穷举合法性检查**。

------

### 2. 核心区别：`type` vs `interface`

这是一道必考题，重点在于**扩展性**。

| **特性**     | **Interface**                           | **Type Alias**                           |
| ------------ | --------------------------------------- | ---------------------------------------- |
| **定义范围** | 只能描述对象、函数                      | 可以描述对象、原始类型、联合类型、元组等 |
| **合并特性** | **同名自动合并**（Declaration Merging） | 不允许同名，只能通过 `&` 交叉            |
| **继承方式** | `extends`                               | `&` (Intersection)                       |
| **使用建议** | 优先用于公共 API、第三方库定义          | 用于复杂的逻辑运算、联合类型             |

------

### 3. 进阶技巧：什么是类型守卫（Type Guard）？

面试官会问：当一个变量是 `string | number` 时，你如何安全地调用 `toUpperCase()`？

- **typeof**: `if (typeof v === 'string')`

- **instanceof**: 用于类实例。

- **in**: `if ('name' in user)` 检查属性。

- **谓词函数 (is)**: 自定义函数返回 `arg is Type`。

-  

- 在 TypeScript 面试中，如果你能手写出这四种**类型守卫（Type Guard）**的具体代码，能极大体现你对代码健壮性的把控。

  以下是针对你提到的四种方式的详细代码示例：

  ------

  ### 1. `typeof`：处理基本类型

  这是最常用的方式，主要用于 `string`, `number`, `boolean`, `symbol` 等原始类型。

  TypeScript

  ```
  function formatInput(input: string | number) {
      if (typeof input === 'string') {
          // 在这个分支里，TS 自动将 input 推断为 string
          return input.toUpperCase(); 
      } else {
          // 在这个分支里，input 自动被推断为 number
          return input.toFixed(2);
      }
  }
  ```

  ------

  ### 2. `instanceof`：处理类（Class）实例

  当你需要区分两个不同的类对象时，`instanceof` 非常有效。

  TypeScript

  ```
  class Dog {
      bark() { console.log("汪汪！"); }
  }
  class Cat {
      meow() { console.log("喵喵~"); }
  }
  
  function makeNoise(animal: Dog | Cat) {
      if (animal instanceof Dog) {
          // 只有 Dog 类有 bark 方法
          animal.bark();
      } else {
          animal.meow();
      }
  }
  ```

  ------

  ### 3. `in`：处理对象属性

  当你处理的是普通接口（Interface）或对象字面量，且没有类构造函数时，可以使用 `in` 关键字检查属性是否存在。

  TypeScript

  ```
  interface Admin {
      name: string;
      privileges: string[];
  }
  interface Employee {
      name: string;
      startDate: Date;
  }
  
  function printInfo(user: Admin | Employee) {
      console.log("Name: " + user.name);
      
      // 检查 user 对象中是否存在 privileges 属性
      if ('privileges' in user) {
          console.log("Privileges: " + user.privileges.join(', '));
      }
      
      if ('startDate' in user) {
          console.log("Start Date: " + user.startDate);
      }
  }
  ```

  ------

  ### 4. 谓词函数 `is`：自定义复杂逻辑

  当你需要封装一套复杂的判断逻辑时，使用 `arg is Type` 告诉 TS 编译器：如果函数返回 `true`，那么这个变量就是该类型。

  TypeScript

  ```
  interface Bird {
      fly: () => void;
      legs: number;
  }
  interface Fish {
      swim: () => void;
      fins: number;
  }
  
  // 定义一个谓词函数
  function isFish(pet: Bird | Fish): pet is Fish {
      return (pet as Fish).swim !== undefined;
  }
  
  function move(pet: Bird | Fish) {
      if (isFish(pet)) {
          // 经过 isFish 判断后，此处 pet 被确定为 Fish 类型
          pet.swim();
      } else {
          pet.fly();
      }
  }
  ```

  ------

  ### 💡 面试加分点：为什么不直接用 `as`（类型断言）？

  在面试中你可以补充：

  > “虽然可以使用 `(input as string).toUpperCase()` 强行通过编译，但这只是‘欺骗’编译器，如果运行时 `input` 确实是 `number`，程序就会报错崩溃。而**类型守卫**（Type Guards）是真正的类型安全，它要求我们编写逻辑来确保运行时的安全性。”

  ### 进阶思考：Discriminated Unions（可辨识联合）

  在 React 开发中，最推荐的其实是**可辨识联合**（给每个接口加一个 `type` 字段）。

  TypeScript

  ```
  interface Success { type: 'success'; data: string; }
  interface Error { type: 'error'; message: string; }
  
  function handleResponse(res: Success | Error) {
      // 这种通过字面量值判断的方式在 TS 中非常高效且易读
      if (res.type === 'success') {
          console.log(res.data);
      }
  }
  ```

  **你想让我演示一下如何在 React 组件的 Props 中应用这些类型守卫，还是想了解 TS 中的“鸭子类型”辨析？**

------

### 4. 复杂类型：交叉类型 (`&`) vs 联合类型 (`|`)

- **联合类型**：表示“或”，值可以是 A 也可以是 B。

- **交叉类型**：表示“且”，通常用于合并多个对象类型。

  > **避坑指南**：如果是两个基本类型的交叉（如 `string & number`），结果是 `never`。

------

### 5. 高级特性：常用的泛型工具类型 (Utility Types)

你需要能脱口而出并解释它们的底层实现（`Mapped Types`）：

- **Partial**: 将所有属性变为可选。
- **Required**: 将所有属性变为必选。
- **Readonly**: 变为只读。
- **Pick<T, K>**: 从 T 中挑选出一组属性 K。
- **Omit<T, K>**: 从 T 中忽略一组属性 K。

------

### 6. 压轴题：如何理解 T 原理中的“协变”与“逆变”？

这属于区分“高级开发”和“普通开发”的题目。

- **协变 (Covariance)**：子类型可以赋值给父类型（TS 的对象类型默认是协变的）。
- **逆变 (Contravariance)**：在函数参数中，父类型可以赋值给子类型（为了保证调用时的安全）。
- **双向协变**：TS 在 `strictFunctionTypes: false` 时允许的情况，但通常不建议。

------

### 7. 工程化：`.d.ts` 文件是干什么的？

- 它是**类型声明文件**。
- 主要用于为没有 TS 源码的 JS 库提供类型定义（如 `@types/lodash`）。
- 它只包含类型信息，编译后会被剔除，不产生实际 JS 代码。

------

### 💡 模拟面试回答小贴士：

在回答时，结合你之前提到的项目经验（比如 **Rax 到 React 18 的迁移**）：

> “在迁移过程中，我们利用 TypeScript 重新建模了业务逻辑。通过定义严格的 **Interface** 替代了原本模糊的 JS 对象，配合 **Generics（泛型）** 实现了组件逻辑的复用，这不仅降低了排查 bug 的成本，也让代码在 IDE 里的自动补全体验提升了非常多。”

**你想看其中某一个特性的代码实现（比如怎么手写一个 `MyPick<T, K>`），还是想聊聊 TS 在 Monorepo 架构下的配置实践？**

## “鸭子类型”

在 TypeScript (TS) 的世界里，**“鸭子类型”（Duck Typing）**是一个非常核心的概念。TS 的官方术语称之为 **“结构化类型系统”（Structural Typing）**。

理解这个概念，是区分你是否真正掌握 TS 类型检查机制的关键。

------

### 1. 什么是“鸭子类型”？

这个名字来源于一个著名的谚语：

> “如果它走起来像鸭子，叫起来也像鸭子，那么它就是一只鸭子。”

在编程中，这意味着：**只要一个对象具有所需的属性和方法，它就可以被当作某种类型使用，而不必显式地声明它属于某个类或接口。**

------

### 2. TS 的结构化类型 vs 强类型语言的标称类型

为了让你看清区别，我们对比一下：

- **标称类型 (Nominal Typing)**：如 Java、C#。

  如果你定义了两个结构一模一样的类 `User` 和 `Customer`，你不能把 `Customer` 赋值给 `User`，因为它们的名字不同。

- **结构化类型 (Structural Typing)**：如 TypeScript。

  只要 `User` 和 `Customer` 的成员结构一致，它们就是兼容的。

#### 代码示例：

TypeScript

```
interface Point {
  x: number;
  y: number;
}

function logPoint(p: Point) {
  console.log(`${p.x}, ${p.y}`);
}

// 重点：这个对象没有显示声明实现 Point 接口
const obj = { x: 10, y: 20, z: 30 };

// 只要它包含了 x 和 y，TS 就认为它是合法的！
logPoint(obj); 
```

------

### 3. “鸭子类型”的两个核心规则

#### A. 属性“多给”没问题 (协变性)

如上面的例子，`obj` 多了一个属性 `z`。在函数调用时，TS 允许传入属性更多的对象，因为它满足了 `Point` 对 `x` 和 `y` 的基本要求。

#### B. 对象字面量的严格检查 (例外情况)

这是很多开发者困惑的地方。如果你直接把对象写在函数调用里，TS 会触发**严格属性检查**：

TypeScript

```
// 报错！因为你是直接写在参数里的，TS 认为你在写错代码。
logPoint({ x: 10, y: 20, z: 30 }); 

// 解决：先赋值给变量，再传入（利用鸭子类型特性的“收窄”）。
const tmp = { x: 10, y: 20, z: 30 };
logPoint(tmp); // 正常通过
```

------

### 4. 为什么要这么设计？（初衷）

TypeScript 诞生的初衷是为 JavaScript 提供类型支持。

- **JS 的本质**：JS 本身就是极度动态的，开发者经常在代码里“随手”创建一个对象传给某个函数。
- **兼容性**：如果要求所有 JS 对象都必须先定义 Class 或 Interface 才能使用，那么存量 JS 代码的迁移成本会高到无法接受。
- **灵活性**：结构化类型让组件和库之间的解耦更彻底。

------

### 5. 面试实战：鸭子类型可能带来的“坑”

面试官可能会问：**“既然结构一致就兼容，那怎么区分两个完全一样但含义不同的类型？”**

例如：`UserId` 和 `PostId` 都是 `number`，但我不希望把 `UserId` 传给处理 `PostId` 的函数。

**解决方案：Brand（烙印）类型 / 幽灵类型**

利用 TS 的交叉类型，强行制造差异。

TypeScript

```
type UserId = number & { __brand: "UserId" };
type PostId = number & { __brand: "PostId" };

let uid = 1 as UserId;
let pid = 2 as PostId;

// 报错：即便底层都是 number，但 __brand 不同。
// uid = pid; 
```

------

### 总结

- **鸭子类型**是 TS 灵活性的根源，它关注**“形状”**而非**“名称”**。
- 它让前端开发在享受类型安全的同时，保留了 JS 快速迭代的快感。
- 在你的项目（如 **Monorepo 组件库**）中，鸭子类型允许你轻松地让不同包之间的相似数据结构进行互操作，而不需要强制继承同一个基础接口。
