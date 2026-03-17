# 数组-双指针

## 快慢指针

一般用于数组原地修改

1. 原地修改数组 leetcode 26/80/27
2. 原地修改链表 83 

```js
var removeDuplicates = function(nums) {
    if (nums.length === 0) {
        return 0;
    }
    let slow = 0, fast = 0;
    while (fast < nums.length) {
        if (nums[fast] !== nums[slow]) {
            slow++;
            // 维护 nums[0..slow] 无重复
            nums[slow] = nums[fast];
        }
        fast++;
    }
    // 数组长度为索引 + 1
    return slow + 1;
};
```

2. 滑动窗口

## 左右指针

# 前缀和数组

> 前缀和技巧适用于快速、频繁地计算一个索引区间内的元素之和。

### 一维数组

前缀和 = 用空间换时间，把“重复计算”变成“一次预处理”。

是一种用空间换时间的优化技巧。通过预处理构建累加数组，使得区间和查询从 O(n) 优化到 O(1)。常用于多次区间查询问题。

意思大致理解就是我先把所有和的数据全部算出来了，下次你再寻找的时候就可以直接获取了。实现o1的时间复杂度。

如果每次计算子矩形之和都用“暴力遍历”的方法（一个个数字相加），时间复杂度是 `O(M \times N)`。如果我们需要频繁查询，效率会非常低。我们的目标是通过**一次预计算**，让后续所有的区域求和查询都能在 **O(1)（常数时间）**内完成。

==区间` [left, right]` 的和 = `prefix[right + 1]` - `prefix[left]`==

```js
let prefix = new Array(nums.length + 1).fill(0);

for (let i = 0; i < nums.length; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
}

function sumRange(left, right) {
    return prefix[right + 1] - prefix[left];
}
```

```js
// 原数组：
index: 0 1 2 3 4
nums:  2 4 6 8 10
prefix: [0,0,0,0,0,0]

// 构造 prefix：
prefix: [0, 2, 6, 12, 20, 30]

// 求 [1,3] index 1-3

prefix[4] - prefix[1] 
= (2+4+6+8) - (2)
= 4+6+8
```

### 二维矩阵

<img src="https://i.postimg.cc/XVQphLGn/image-20260301171702024.png?dl=1" alt="image-20260301171702024" style="zoom: 67%;" />

```js
// sums 矩阵
0 0 0

0 A A+B

0 A+C A+B+C+D
```

![image-20260228134650561](https://i.postimg.cc/JmgFVkf8/image-20260228134650561.png?dl=1)

假设我们有一个原始矩阵 `matrix`，我们先创建一个预处理矩阵 `sums`，其中 `sums[i][j]` 表示从矩阵左上角 `(0, 0)` 到右下角 `(i-1, j-1)` 这个矩形范围内所有元素的累加和。

当你调用 `sumRegion(row1, col1, row2, col2)` 想要获取目标区域（下图中的 **D** 区域）的和时，你可以利用已经算好的大矩形，减去多余的部分：

1. **大总和**：从 `(0,0)` 到 `(row2, col2)` 的总和。
2. **减去上方**：减去 `(0,0)` 到 `(row1-1, col2)` 的和（图中的 A + B）。
3. **减去左边**：减去 `(0,0)` 到 `(row2, col1-1)` 的和（图中的 A + C）。
4. **补回重叠**：因为 A 区域被减了两次，所以要把它加回来。

第一步：造盾（求前缀和矩阵）

**口诀：左边 + 上边 - 斜角 + 自己**

- **左边**：`sums[i][j-1]`（已经算好的左侧矩形）
- **上边**：`sums[i-1][j]`（已经算好的上方矩形）
- **减斜角**：`- sums[i-1][j-1]`（因为左边和上边都包含了这个重叠的斜角部分，多算了一次，得减掉）
- **加自己**：`+ matrix[i-1][j-1]`（把当前这块砖加上）

`sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i-1][j-1]`

第二步：切肉（求子矩形面积）

**口诀：大矩形 - 上边条 - 左边条 + 重叠角**

1. **大矩形**：右下角那个点对应的总和。
2. **减去不需要的**：
   - 减去**上边**多出来的长条。
   - 减去**左边**多出来的长条。
3. **补回来**：当你减去上边和左边时，**左上角那个小矩形被减了两次**，所以要加回来一次。

| **位置名称**       | **原始矩阵 matrix 坐标** | **对应的 Sums 矩阵坐标** |
| ------------------ | ------------------------ | ------------------------ |
| **右下角点**       | `(row2, col2)`           | `[row2 + 1][col2 + 1]`   |
| **上边界的前一行** | `row1 - 1`               | `[row1]`                 |
| **左边界的前一列** | `col1 - 1`               | `[col1]`                 |

```js
return sums[row2 + 1][col2 + 1] // 大矩形
     - sums[row1][col2 + 1]     // 减去上边条
     - sums[row2 + 1][col1]     // 减去左边条
     + sums[row1][col1];        // 补回重叠角
```

以你提供的输入为例：

- **初始矩阵**：

  ```
  i	0  1  2  3  4
  ---------------
  	3  0  1  4  2 
  	5  6  3  2  1
  	1  2  0  1  5
  	4  1  0  1  7
  	1  0  3  0  5
  ```

- **查询 `sumRegion(2, 1, 4, 3)`**：

  即计算从第 2 行第 1 列到第 4 行第 3 列的矩形。

  - 对应的元素是：

    ```
    2  0  1
    1  0  1
    0  3  0
    ```

  - 相加结果：`2+0+1 + 1+0+1 + 0+3+0 = 8`。

```js
Array.from({ length: n }, () => []) // 是 JS 中创建独立多维数组的最简便写法。

// 1. 先创建一个外层数组（行）
const sums = new Array(rows + 1); 

for (let i = 0; i < sums.length; i++) {
    // 2. 给每一行创建一个独立的新数组（列）
    sums[i] = new Array(cols + 1).fill(0); 
}
```

```js
class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
        const rows = matrix.length;
        if (rows === 0 || matrix[0].length === 0) return;
        const cols = matrix[0].length;

        // 创建一个 (rows + 1) x (cols + 1) 的前缀和矩阵，初始化为 0
        // sums[i][j] 代表从 matrix[0][0] 到 matrix[i-1][j-1] 的矩形和
        this.sums = Array.from({ length: rows + 1 }, () => new Array(cols + 1).fill(0));

        for (let x = 1; x <= rows; x++) {
            for (let y = 1; y <= cols; y++) {
                // 计算当前位置的前缀和
                // 当前值 + 上方和 + 左方和 - 重复计算的左上方和
                this.sums[x][y] = matrix[x - 1][y - 1] 
                                + this.sums[x - 1][y] 
                                + this.sums[x][y - 1] 
                                - this.sums[x - 1][y - 1];
            }
        }
    }

    /** * @param {number} row1 
     * @param {number} col1 
     * @param {number} row2 
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1, col1, row2, col2) {
        // 使用容斥原理：大矩形 - 上方矩形 - 左方矩形 + 重复减去的左上方矩形
        // 注意：由于 sums 索引比 matrix 大 1，所以这里的索引需要相应偏移
        return this.sums[row2 + 1][col2 + 1] // 5 4 - a
             - this.sums[row1][col2 + 1] // 2 4 - b
             - this.sums[row2 + 1][col1] // 5 1 - c
             + this.sums[row1][col1]; // 2 1 - d
    }
}

/**
 * 测试用例
 */
const matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
];

const nm = new NumMatrix(matrix);
console.log(nm.sumRegion(2, 1, 4, 3)); // 输出: 8
console.log(nm.sumRegion(1, 1, 2, 2)); // 输出: 11
console.log(nm.sumRegion(1, 2, 2, 4)); // 输出: 12

const sums = [
  [0 0, 0, 0, 0, 0]
  [0 3, 0, 1, 4, 2],
  [0 d, 6, 3, b, 1],
  [0 1, 2, 0, 1, 5], // 这个2的位置坐标
  [0 4, 1, 0, 1, 7],
  [0 c, 0, 3, a, 5],
];

// 在原来的matrix上多增加了一列一排，在那个的基础上计算出abcd的坐标位置即可。所以sumRegion(3,2,5,4)
// (row1 + 1) (col1 + 1) (row2 + 1) (col2 + 1)
// 2的位置坐标是 (row1 + 1) (col1 + 1) ， a的位置坐标(row2 + 1) (col2 + 1)
// 进行推算
// a = row2 + 1 , col2 + 1
// b = row1 + 1 - 1 , col2 + 1
// c = row2 + 1, (col1 + 1 - 1)
// d = (row1 + 1 - 1) (col1 + 1 -1)
```

![image-20260228140032257](https://i.postimg.cc/Q8qWg1cN/image-20260228140032257.png?dl=1)

但是，前缀和技巧有几个局限性。

**第一个局限性：使用前缀和技巧的前提是原数组 `nums` 不会发生变化**。

如果原数组中的某个元素改变了，那么 `preSum` 数组中该元素后面的值就会失效，需要重新花费 *O*(*n*) 的时间计算 `preSum` 数组，这就和普通的暴力解法没太大区别了。

**第二个局限性：前缀和技巧只适用于存在逆运算的场景**。

比方说求和的场景，你知道 x+6=10*x*+6=10，那么可以推导出 x=10−6=4*x*=10−6=4，求乘积的场景也是类似的，你知道 x∗6=12*x*∗6=12，那么可以推导出 x=12/6=2*x*=12/6=2，这就叫存在逆运算，都可以使用前缀和技巧。

但有些场景是没有逆运算的，比方说求最大值的场景，你知道 max(x,8)=8*ma**x*(*x*,8)=8，此时你无法推导出 x*x* 的值。

想要同时解决这两个问题，就需要更高级的数据结构，最通用的解决方案是 [线段树](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/)

### 前缀积

#### 1. 算出“左侧积累” (prefix)

`prefix[i]` 代表从开头一直乘到 `i` 的结果。

- `nums`: `[2, 3, 4, 5]`
- `prefix`: `[2, 6, 24, 120]` (分别是 2, 2*3, 2*3*4...)

#### 2. 算出“右侧积累” (suffix)

`suffix[i]` 代表从末尾一直乘回 `i` 的结果。

- `nums`: `[2, 3, 4, 5]`
- `suffix`: `[120, 60, 20, 5]` (分别是 2*3*4*5, 3*4*5, 4*5, 5)

#### 3. 左右合体 (res)

现在我们要算第 `i` 个位置（比如 `nums[1]`，也就是数字 `3`）：

- 它的**左边**所有人积是 `prefix[0]` (即 `2`)
- 它的**右边**所有人积是 `suffix[2]` (即 `4*5 = 20`)
- **结果** = `2 * 20 = 40`。你看，数字 `3` 就这样被绕过去了。

```js
var productExceptSelf = function(nums) {
    let n = nums.length;
    // 从左到右的前缀积，prefix[i] 是 nums[0..i] 的元素积
    let prefix = new Array(n);
    prefix[0] = nums[0];
    for (let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i - 1] * nums[i];
    }
    // 从右到左的前缀积，suffix[i] 是 nums[i..n-1] 的元素积
    let suffix = new Array(n);
    suffix[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffix[i] = suffix[i + 1] * nums[i];
    }
    // 结果数组
    let res = new Array(n);
    res[0] = suffix[1]; // 数组的最左边和最右边，代码通过手动赋值来规避
    res[n - 1] = prefix[n - 2]; // 最右边，代表从第 1 个数到倒数第 2 个数的积
    for (let i = 1; i < n - 1; i++) { // 跳过第一个和最后一个
        // 除了 nums[i] 自己的元素积就是 nums[i] 左侧和右侧所有元素之积
        res[i] = prefix[i - 1] * suffix[i + 1];
    }
    return res;
};

// 用“除法”来求区间积
```

# 差分数组

> **差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减**。

如果你用 `for` 循环去修改区间，时间复杂度是 `O(N)`。如果有 10 万次修改，程序就慢死了。 但用差分数组，**每次修改只需要改两个数**，时间复杂度是 $O(1)$。最后只在查询结果时做一次 `O(N)` 的累加即可。

原数组不是 diff，本质上是 diff 的前缀和。`nums[k] = diff[0] + diff[1] + ... + diff[k]`

每个 nums[k] 都包含前面所有 diff 的累加。

```js
let nums = [0, 0, 0, 0, 0];

// 1️⃣ 创建差分对象
let diff = new Difference(nums);

// 2️⃣ 进行区间修改
diff.increment(1, 3, 2);   // [1,3] +2
diff.increment(2, 4, 3);   // [2,4] +3
diff.increment(0, 2, -2);  // [0,2] -2

// 3️⃣ 还原结果
let result = diff.result();

console.log(result);
```

```js
// 原数组 = 差分数组的前缀和

class Difference {
    constructor(nums) {
        // 差分数组
        this.diff = new Array(nums.length);
        // 根据初始数组构造差分数组
        this.diff[0] = nums[0];
        for (let i = 1; i < nums.length; i++) {
            this.diff[i] = nums[i] - nums[i - 1];
        }
    }

    // 给闭区间 [i, j] 增加 val（可以是负数）
    increment(i, j, val) {
        this.diff[i] += val; // 只记录变化点，从哪里开始变化
        if (j + 1 < this.diff.length) { // 不是遍历，是if位置，最后需要减。
            this.diff[j + 1] -= val;
        }
    }

    // 返回结果数组
    result() {
        let res = new Array(this.diff.length);
        // 根据差分数组构造结果数组
        res[0] = this.diff[0];
        for (let i = 1; i < this.diff.length; i++) {
            res[i] = res[i - 1] + this.diff[i];
        }
        return res;
    }
}
```













