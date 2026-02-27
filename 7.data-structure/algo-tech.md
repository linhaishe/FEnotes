# Algo-tech

## 前缀和数组

### 一维数组

前缀和 = 用空间换时间，把“重复计算”变成“一次预处理”。

是一种用空间换时间的优化技巧。通过预处理构建累加数组，使得区间和查询从 O(n) 优化到 O(1)。常用于多次区间查询问题。

意思大致理解就是我先把所有和的数据全部算出来了，下次你再寻找的时候就可以直接获取了。实现o1的时间复杂度。

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

### 二维数组











