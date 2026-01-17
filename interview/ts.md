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



