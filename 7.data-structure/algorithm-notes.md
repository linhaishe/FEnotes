# 双指针 / 数组

## 左右指针

## 快慢指针

### Sliding Window Algorithm

滑动窗口

Refs: https://labuladong.online/zh/algo/essential-technique/sliding-window-framework/

> 滑动窗口可以归为快慢双指针，一快一慢两个指针前后相随，中间的部分就是窗口。**滑动窗口算法技巧主要用来解决子数组问题，比如让你寻找符合某个条件的最长/最短子数组**。

1、什么时候应该移动 right 扩大窗口？窗口加入字符时，应该更新哪些数据？

窗口不包含数据的时候，我们尝试扩大窗口，拥有更多字符去涵盖所需的数据。

2、什么时候窗口应该暂停扩大，开始移动 left 缩小窗口？从窗口移出字符时，应该更新哪些数据？

当窗口已经涵盖所有需要内容的时候

3、什么时候应该更新结果？

缩小窗口的时候，尝试更新结果（ 分情况，也许是缩小也许是扩大。

初始化，left = 0 , right = 0, 左闭右开

```js
// 滑动窗口算法伪码框架
var slidingWindow = function(s) {
    // 用合适的数据结构记录窗口中的数据，根据具体场景变通
    // 比如说，我想记录窗口中元素出现的次数，就用 map
    // 如果我想记录窗口中的元素和，就可以只用一个 int
    var window = ...;

    var left = 0, right = 0;
    while (right < s.length) {
        // c 是将移入窗口的字符
        var c = s[right];
        window.add(c);
        // 增大窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        // *** debug 输出的位置 ***
        // 注意在最终的解法代码中不要 print
        // 因为 IO 操作很耗时，可能导致超时
        console.log("window: [%d, %d)\n", left, right);
        // *********************

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            var d = s[left];
            window.remove(d);
            // 缩小窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
};
```

### leetcode - 76 🔴

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"　

```js
var minWindow = function (s, t) {
  let need = {},
    window = {};
  // 统计字符串 t 中每个字符出现的次数，存到 need 对象里
  // out put need {A: 1, B: 1, C: 1}
  for (let c of t) {
    need[c] = (need[c] || 0) + 1;
  }

  let left = 0,
    right = 0;
  let valid = 0; // 有多少种字符单种类出现的次数是否已经「达标」，不是所有字符次数
  // 记录最小覆盖子串的起始索引及长度
  let start = 0,
    len = Infinity;
  while (right < s.length) {
    // c 是将移入窗口的字符
    let c = s[right];
    // 扩大窗口
    right++;
    // 进行窗口内数据的一系列更新,如果进入到窗口，计数增加
    if (need[c]) {
      window[c] = (window[c] || 0) + 1;
      if (window[c] === need[c]) {
        valid++;
      }
    }

    // 判断左侧窗口是否要收缩，窗口含有所需字符就开始收缩
    while (valid === Object.keys(need).length) {
      // 在这里更新最小覆盖子串
      if (right - left < len) {
        start = left;
        len = right - left; // len更新，不会是infinite,第一次的时候永远是true,因为永远小于infinite
      }
      // d 是将移出窗口的字符
      let d = s[left];
      // 缩小窗口
      left++;
      // 进行窗口内数据的一系列更新
      if (need[d]) {
        if (window[d] === need[d]) {
          valid--;
        }
        window[d]--;
      }
    }
  }
  // 返回最小覆盖子串
  return len === Infinity ? "" : s.substring(start, start + len);
};

```

**`Infinity` 不是一种数据类型，而是 JavaScript 里的一个“数值（number）常量”**，**完全可以、而且经常这样用**。

```js
typeof Infinity  // "number"
// -Infinity   // 负无穷大
```

为什么是 `window[c] === need[c]` 才 `valid++`

`valid` 对每个字符，只会在「达标」时 +1，在「失去达标」时 −1。`valid` 是一个“达标字符种类计数器”，对每种字符而言，只在它从不达标变为刚好达标时加 1，在从达标变为不达标时减 1，因此不会被重复累加。

```js
t = "AABC"
need = { A: 2, B: 1, C: 1 }

// 第一次遇到 A,没达标, valid 不动
window = { A: 1 }
need[A] = 2

// 第二次遇到 A,刚好达标,valid++
window = { A: 2 }
need[A] = 2

// 再来一个 A,已经超了,不再加 valid
window = { A: 3 }
need[A] = 2

```

