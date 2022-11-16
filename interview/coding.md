# 高频手写题

## 1. 深拷贝

```js
const deepClone = (obj: any) => {
  if (obj === null) return null;
  // 如果传入的是数组，也拷贝到对象中
  let clone = { ...obj };
  // 递归实现对象深度拷贝
  Object.keys(clone).forEach(
    (key) =>
    (clone[key] =
     // 如果二维对象还存在，重新调用deepclone
      typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  
  return Array.isArray(obj) && obj.length
  // 对象转换成数组的方法，不是返回boolean，直接return 数组了
    ? (clone.length = obj.length) && Array.from(clone)
    : Array.isArray(obj)
      ? Array.from(obj)
      : clone;
};
```

## 2. 浅拷贝

```js
function shallowCopy(object) {
  // 只拷贝对象
  if (!object || typeof object !== "object") return;
  // 根据 object 的类型判断是新建一个数组还是对象
  let newObject = Array.isArray(object) ? [] : {};
  // 遍历 object，并且判断是 object 的属性才拷贝
  for (let key in object) {
    if (object.hasOwnProperty(key)) {
      newObject[key] = object[key];
    }
  }
  return newObject;
}
```

## 1. 实现一个 once 函数，记忆返回结果只执行一次

## 2. 如何实现一个函数 isPlainObject 判断是否为纯对象

## 3. 如何实现一个无限累加的 sum 函数

## 4. JS 如何实现一个同步的 sleep 函数

## 5. 实现一个函数用来解析 URL 的 querystring

## 6. JS 如何实现一个 sleep/delay 函数

## 7. 如何实现一个 sample 函数，从数组中随机取一个元素

## 8. 实现一个函数用来对 URL 的 querystring 进行编码

## 9. 实现一个数组扁平化的函数 flatten

## 10. 实现一个数组去重函数 unique

## 11. 如何实现页面文本不可复制

## 12. 如何实现一个数组洗牌函数 shuffle

## 13. JS 如何翻转一个字符串

## 14. 如何过滤数组中的 falsy value

## 15. 如何把一个数组随机打乱

## 16. 解构赋值一个数组，a 取第一项默认值为 3，c取剩下的值组成数组

## 17. 如何判断一个数组是否包含某个值

## 18. 如何判断字符串包含某个子串

## 19. 如何判断某一个值是数组

## 20. 如何统计当前页面出现的所有标签

## 21. 实现一个 inherits 函数进行继承

## 22. 关于块级作用域，以下代码输出多少，在何时间输出

## 23. 如何逆序一个字符串

## 24. 关于 this 与包装对象，以下输出多少

## 25. 关于类型转化，判断以下代码输出

## 26. 关于暂时性死域，判断以下代码输出

## 27. 关于词法作用域，判断以下代码输出

## 28. 关于 this，判断以下代码输出

## 29. 关于 new，判断以下代码输出

## 30. 关于简单的事件循环，判断以下代码输出

## 31. 给数字添加千位符

## 32. 如何实现一个深比较的函数 deepEqual

## 33. 使用 JS 如何生成一个随机字符串

## 34. 如何判断一个数值为整数

## 35. 什么是安全整数，如何判断一个整数是安全整数

## 36. 如何把字符串全部转化为小写格式

## 37. JS 中如何原生实现 instanceOf

```js
function _instanceof(L, R) {
  if (typeof L !== 'object') return false
  // L : 实例对象
  // R : 构造函数
  let O = R.prototype;
  L = L._proto_;
  while (true) {
    if (L === Null) {
      return false;
    }
    if (L === O) {
      return true;
    }
    L = L._proto_;
  }
}

// 测试
function Car(make, model, year) {
  this.make = make
  this.model = model
  this.year = year
}

const auto = new Car('Honda', 'Accord', 1998)
console.log(_instanceof(auto, Car)) // expected output: true

// 测试
console.log(_instanceof([1, 2], Array)) // expected output: true
console.log(_instanceof({ a: 1 }, Object)) // expected output: true
```

## 38. 如何取得一个数字的小数部分与整数部分