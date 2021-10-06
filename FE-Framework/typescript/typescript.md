## 一、TypeScript 是什么

[TypeScript](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2F) 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集，而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。

TypeScript 提供最新的和不断发展的 JavaScript 特性，包括那些来自 2015 年的 ECMAScript 和未来的提案中的特性，比如异步功能和 Decorators，以帮助建立健壮的组件。下图显示了 TypeScript 与 ES5、ES2015 和 ES2016 之间的关系：

![typescript-scope-new.png](https://segmentfault.com/img/bVbH9l8)

### 1.1 TypeScript 与 JavaScript 的区别

|                   TypeScript                   |                 JavaScript                 |
| :--------------------------------------------: | :----------------------------------------: |
| JavaScript 的超集用于解决大型项目的代码复杂性  |      一种脚本语言，用于创建动态网页。      |
|          可以在编译期间发现并纠正错误          |  作为一种解释型语言，只能在运行时发现错误  |
|           强类型，支持静态和动态类型           |          弱类型，没有静态类型选项          |
| 最终被编译成 JavaScript 代码，使浏览器可以理解 |           可以直接在浏览器中使用           |
|              支持模块、泛型和接口              |           不支持模块，泛型或接口           |
|          支持 ES3，ES4，ES5 和 ES6 等          |  不支持编译其他 ES3，ES4，ES5 或 ES6 功能  |
|       社区的支持仍在增长，而且还不是很大       | 大量的社区支持以及大量文档和解决问题的支持 |

### 1.2 获取 TypeScript

命令行的 TypeScript 编译器可以使用 Node.js 包来安装。

**1.安装 TypeScript**

```shell
$ npm install -g typescript
```

**2.编译 TypeScript 文件**

```shell
$ tsc helloworld.ts
# helloworld.ts => helloworld.js
```

当然，对于刚入门 TypeScript 的小伙伴，也可以不用安装 `typescript`，而是直接使用线上的 [TypeScript Playground](https://link.segmentfault.com/?url=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%2F) 来学习新的语法或新特性。

## 二、

ts 传入了不是规定的数据类型，还是可以进行编译，如果没有对编译器进行配置的话。

ts可以转换成不同版本的es 语法，es3/es6，这种也可以通过配置进行处理

