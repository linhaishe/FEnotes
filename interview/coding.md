# 高频手写题

## 1. 深拷贝

### 方法一： 只考虑了object / array 这两种类型

```js
// 只考虑了object / array 这两种类型
const deepClone = (obj) => {
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

### 方法二：考虑到了复杂类型和循环引用做了优化

```js
// 完整版
function deepCopy(obj) {
  if (obj === null || typeof obj !== "object") {
    return obj;
  }

  // 处理循环引用
  let visited = new WeakMap();
  if (visited.has(obj)) {
    return visited.get(obj);
  }

  let clone;
  if (obj instanceof Date) {
    clone = new Date(obj.getTime());
  } else if (obj instanceof RegExp) {
    clone = new RegExp(obj);
  } else if (obj instanceof Map) {
    clone = new Map();
    for (let [key, value] of obj) {
      clone.set(key, deepCopy(value));
    }
  } else if (obj instanceof Set) {
    clone = new Set();
    for (let value of obj) {
      clone.add(deepCopy(value));
    }
  } else {
    clone = new obj.constructor();
    for (let key in obj) {
      if (obj.hasOwnProperty(key)) {
        // 处理 Symbol 类型
        if (typeof key === "symbol") {
          clone[key] = deepCopy(obj[key]);
        } else {
          clone[key] = deepCopy(obj[key]);
        }
      }
    }
  }

  visited.set(obj, clone);
  return clone;
}

// 测试
let obj1 = { a: 1, b: 2, c: new Date(), d: /ewff/g };
let date = new Date();
let regexp = new RegExp("/ab+c/", "i");
let obj = {
  date: date,
  regexp: regexp,
  map: new Map([
    ["a", 1],
    ["b", 2]
  ]),
  set: new Set([1, 2, 3]),
  symbol: Symbol("foo")
};

let copiedObj = deepCopy(obj);

console.log(copiedObj.date === date); // false
console.log(copiedObj.regexp === regexp); // false
console.log(copiedObj.map === obj.map); // false
console.log(copiedObj.set === obj.set); // false
console.log(copiedObj.symbol === obj.symbol); // false

// 互相没有被影响
let cloneObj = deepCopy(obj);
obj.arr.push(5);
cloneObj.arr.push(8);
console.log("obj", obj);
console.log("copy", cloneObj);
```

```js
// 性能优化
function clone(target, map = new WeakMap()) {
  if (typeof target === "object") {
    const isArray = Array.isArray(target);
    let cloneTarget = isArray ? [] : {};

    if (map.get(target)) {
      return map.get(target);
    }
    map.set(target, cloneTarget);

    const keys = isArray ? undefined : Object.keys(target);
    forEach(keys || target, (value, key) => {
      if (keys) {
        key = value;
      }
      cloneTarget[key] = clone2(target[key], map);
    });

    return cloneTarget;
  } else {
    return target;
  }
}

// date and regexp
function deepCopy(obj) {
  if (obj === null || typeof obj !== "object") {
    return obj;
  }

  if (obj instanceof Date) {
    return new Date(obj.getTime());
  }

  if (obj instanceof RegExp) {
    return new RegExp(obj);
  }

  let clone = new obj.constructor();
  for (let key in obj) {
    clone[key] = deepCopy(obj[key]);
  }
  
  return clone;
}

let date = new Date();
let regexp = new RegExp("/ab+c/", "i");
let obj = {
  array: [1,2,3],
  jack:{
    name: 'jack',
    age: 18
  },
  date: date,
  regexp: regexp
};

let copiedObj = deepCopy(obj);

console.log(copiedObj.date === date); // false
console.log(copiedObj.regexp === regexp); // false
console.log(222, copiedObj);
```

https://juejin.cn/post/6844903929705136141#heading-2

## 2. 浅拷贝

浅拷贝只拷贝对象的第一层属性，不会拷贝嵌套对象中的属性。

浅拷贝只拷贝对象的第一层属性，不会拷贝嵌套对象中的属性。因此，如果对象中有引用类型属性，浅拷贝只会拷贝该引用类型属性的地址。

浅拷贝一般用于什么情况下

浅拷贝可以用于复制对象时只保留对象的第一层属性，而不会拷贝嵌套对象中的属性。

这种方法通常用于复制简单对象或数组时。例如，如果对象中只包含基本数据类型（如数字、字符串、布尔值），那么使用浅拷贝就可以创建一个新对象，该对象中的属性与源对象相同。

### 方法一：只考虑了对象的浅拷贝

```js
function shallowCopy(obj) {
  return Object.assign({}, obj);
}
```
### 方法二： 简单的浅拷贝，没有考虑复杂类型

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

### 方法三：考虑到了复杂类型的浅拷贝

```js
function shallowCopy(obj) {
  // 如果不是对象或数组，直接返回
  if (typeof obj !== "object" || obj === null) return obj;

  // 如果是数组，复制数组并返回
  if (obj instanceof Array) {
    return obj.slice();
  }

  // 如果是 Date、Map、Set、RegExp 等类型，直接返回
  if (
    obj instanceof Date ||
    obj instanceof Map ||
    obj instanceof Set ||
    obj instanceof RegExp
  ) {
    return obj;
  }

  // 如果是对象，创建一个新对象并复制属性
  let newObj = {};
  for (let key in obj) {
    newObj[key] = obj[key];
  }
  return newObj;
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