# Algo-tech

## 前缀和数组

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

// 求 [1,3]

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

const matrix = [
  [0 0, 0, 0, 0, 0]
  [0 3, 0, 1, 4, 2],
  [0 d, 6, 3, b, 1],
  [0 1, 2, 0, 1, 5],
  [0 4, 1, 0, 1, 7],
  [0 c, 0, 3, a, 5],
];
```

![image-20260228140032257](https://i.postimg.cc/Q8qWg1cN/image-20260228140032257.png?dl=1)





