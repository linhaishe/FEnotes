# refs:

1. [Solidity中文文档（官方文档的中文翻译](https://solidity-cn.readthedocs.io/zh/develop/introduction-to-smart-contracts.html)
2. [崔棉大师solidity教程 web3技术教学博主](https://space.bilibili.com/286084162)，我看他视频学到了很多

# 数值类型

在Solidity编程语言中，"256位正整数"指的是一种特定的整数类型，即 `uint256`。Solidity是一种面向以太坊智能合约开发的编程语言，它支持多种不同位宽的整数类型，包括有符号和无符号的整数类型。

具体来说：

- `uint` 或 `uint256` 代表一个无符号整数，它占用 256 位（32 字节）的存储空间，取值范围是从 0 到 2256−12^{256} - 12256−1。
- 由于它是无符号的，因此它只能表示非负整数。

Solidity 中的整数类型有多种不同的位宽，例如 `uint8`，`uint16`，`uint32`，...，一直到 `uint256`。每个类型的位宽不同，表示的数值范围也不同。

以下是一些常见的无符号整数类型及其取值范围：

- `uint8`: 取值范围为 0 到 255。
- `uint16`: 取值范围为 0 到 65,535。
- `uint32`: 取值范围为 0 到 4,294,967,295。
- `uint256`: 取值范围为 0 到 2256−12^{256} - 12256−1。

在 Solidity 代码中使用 `uint256` 的示例如下：

```solidity
pragma solidity ^0.8.0;

contract Example {
    uint256 public largeNumber;

    constructor() {
        largeNumber = 1234567890123456789012345678901234567890;
    }

    function setLargeNumber(uint256 _newNumber) public {
        largeNumber = _newNumber;
    }

    function getLargeNumber() public view returns (uint256) {
        return largeNumber;
    }
}

```

在这个示例中，largeNumber 是一个 uint256 类型的状态变量，它能够存储一个非常大的无符号整数。

```solidity
// 定义一个外部可见的、只读的函数 enumToUint
function enumToUint() external view returns (uint) {
    // 将枚举类型转换为无符号整数并返回
    return uint(action);
}
```

在 Solidity 中，`uint` 不是一个方法，而是一个类型。具体来说，`uint` 是 `uint256` 的简写，表示 256 位无符号整数。

这里是一些相关的解释和例子：

**Solidity 中的类型转换**

在 Solidity 中，枚举（enum）类型可以显式转换为无符号整数类型（`uint`）。这使得枚举的值可以在需要整数的地方使用。

```solidity
  // Enum
  // 将uint 0， 1， 2表示为Buy, Hold, Sell
  enum ActionSet { Buy, Hold, Sell }
  // 创建enum变量 action
  ActionSet action = ActionSet.Buy;

  // enum可以和uint显式的转换
  function enumToUint() external view returns(uint){
      return uint(action);
  }
```

# 函数类型

![image-20240617132921473](https://s2.loli.net/2024/06/17/aVRhK2ZX87xzoOm.png)

在 Solidity 中，`internal` 关键字用于表示函数只能在合约内部或从派生合约中调用。对于 SafeMath Library 中的 `add` 函数，最适合填写的关键字是 `pure`。这是因为 `add` 函数只执行了加法运算，没有读取或修改区块链上的状态。

### 填写后的代码

```solidity
function add(uint256 a, uint256 b) internal pure returns (uint256) {
  uint256 c = a + b;
  assert(c >= a);  // 本行代码意为：若c不大于等于a，则说明加法运算溢出，抛出异常
  return c;
}
```

### 解释

- `internal`：表示该函数只能在合约内部或从派生合约中调用。
- `pure`：表示该函数不读取或修改区块链上的状态。由于 `add` 函数只是执行了加法运算并进行了一次断言检查，它没有读取或修改任何存储变量，因此应该使用 `pure` 关键字。

### 总结

最终，完整的函数定义如下：

```solidity
function add(uint256 a, uint256 b) internal pure returns (uint256) {
  uint256 c = a + b;
  assert(c >= a);  // 本行代码意为：若c不大于等于a，则说明加法运算溢出，抛出异常
  return c;
}
```

这样可以保证函数的正确性和最佳性能。

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;
contract FunctionTypes{
  uint256 public number = 5;

  constructor() payable {}

  // 函数类型
  // function (<parameter types>) {internal|external} [pure|view|payable] [returns (<return types>)]
  // 默认function
  function add() external pure {
      number = number + 1; // 会报错，因为修改了链上的数据了
  }
}
```

