# Lodash

主要记录一些看不懂的方法，和一些面试频率蛮高的方法

## differenceBy

`[iteratee=_.identity]` *(Array|Function|Object|string)*: iteratee 调用每个元素。

```js
_.differenceBy([3.1, 2.2, 1.3], [4.4, 2.5], Math.floor);
// => [3.1, 1.3]
 
// The `_.property` iteratee shorthand.
_.differenceBy([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], 'x');
// => [{ 'x': 2 }] 
```

`_.differenceBy()` 是 lodash 中的一个方法，用于比较两个数组，返回第一个数组中在第二个数组中不存在的元素集合。它可以接受一个可迭代对象，一个或多个值，或一个迭代函数作为参数。

该方法的第一个参数是要进行差异比较的数组，第二个参数是要排除的数组，第三个参数是一个迭代函数或一个字符串。如果提供了迭代函数，它将用于比较数组中的每个元素。如果提供了字符串，则将使用该字符串来获取每个元素的属性值，然后进行比较。

例如，`_.differenceBy([3.1, 2.2, 1.3], [4.4, 2.5], Math.floor)` 将返回一个数组 `[3.1, 1.3]`，因为 `Math.floor(3.1)` 等于3和 `Math.floor(2.2)` 等于 2，而 `Math.floor(4.4)` 和 `Math.floor(2.5)` 为4和2，所以 3.1 和 1.3 在第二个数组中不存在。

另外一个例子是 `_.differenceBy([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], 'x')`。这个例子将返回一个包含一个对象 `{ 'x': 2 }` 的数组，因为只有 `{ 'x': 2 }` 在第二个数组中不存在，而 `{ 'x': 1 }` 存在于第二个数组中。在这个例子中，我们使用了字符串 `'x'` 作为迭代函数，因此比较每个对象的 `x` 属性值。

## _.differenceWith(array, [values], [comparator])

`comparator]` *(Function)*: comparator 调用每个元素。

```js
var objects = [{ 'x': 1, 'y': 2 }, { 'x': 2, 'y': 1 }];
 
_.differenceWith(objects, [{ 'x': 1, 'y': 2 }], _.isEqual);
// => [{ 'x': 2, 'y': 1 }]
```

## `_.dropRightWhile(array, [predicate=_.identity])`

`dropRightWhile` 方法只会删除符合删除条件的元素，而不是把所有与删除条件不符合的元素全部保留。

Elements are dropped until `predicate` returns falsey.

predicate 会传入3个参数： (value, index, array)。

1. `array` *(Array)*: 要查询的数组。
2. `[predicate=_.identity]` *(Function)*: 这个函数会在每一次迭代调用。

```js
var users = [
  { 'user': 'barney',  'active': true },
  { 'user': 'fred',    'active': false },
  { 'user': 'pebbles', 'active': false }
];
 
_.dropRightWhile(users, function(o) { return !o.active; });
// => objects for ['barney']
 
// The `_.matches` iteratee shorthand.
// 删除用户数组中所有 "user" 属性为 "pebbles" 且 "active" 属性为 false 的对象。因此，在删除后将剩下 { 'user': 'barney',  'active': true } 和 { 'user': 'fred', 'active': false } 这两个对象。
_.dropRightWhile(users, { 'user': 'pebbles', 'active': false });
// => objects for ['barney', 'fred']
 
// The `_.matchesProperty` iteratee shorthand.
// 删除用户数组中所有 "active" 属性值为 false 的对象。因此，在删除后只剩下 { 'user': 'barney',  'active': true } 这个对象。
_.dropRightWhile(users, ['active', false]);
// => objects for ['barney']
 
// The `_.property` iteratee shorthand.
_.dropRightWhile(users, 'active');
// => objects for ['barney', 'fred', 'pebbles']
```

这里的最后一个例子为什么返回所有数据？？？？

## `_.dropWhile(array, [predicate=_.identity])`

```js
var users = [
  { 'user': 'barney',  'active': true },
  { 'user': 'fred',    'active': false },
  { 'user': 'pebbles', 'active': false },
  {  'user': 'widdle' }
];

// The `_.property` iteratee shorthand.
_.dropRightWhile(users,'active');
// => objects for ['fred', 'pebbles', 'widdle']
```

## `_.flattenDeep(array)`

有空去看下源码

## `_.pullAllBy(array, values, [iteratee=_.identity])`

#### 参数

1. `array` *(Array)*: 要修改的数组。
2. `values` *(Array)*: 要移除值的数组。
3. `[iteratee=_.identity]` *(Array|Function|Object|string)*: iteratee（迭代器）调用每个元素。

```js
var array = [{ 'x': 1 }, { 'x': 2 }, { 'x': 3 }, { 'x': 1 }];
 
_.pullAllBy(array, [{ 'x': 1 }, { 'x': 3 }], 'x');
console.log(array);
// => [{ 'x': 2 }]
```

我们想要从`array`数组中移除所有具有`'x'`属性值为`1`或`3`的对象。我们传递了一个包含这两个对象的数组作为`values`参数，并将`'x'`作为`iteratee`参数传递，这样lodash会根据对象的`'x'`属性进行匹配。因此，`{ 'x': 1 }`和`{ 'x': 3 }`这两个对象将被从`array`数组中移除。

## `_.sortedUniq(array)`

*(Array)*: 返回一个新的不重复的数组。

## `_.sortedUniqBy(array, [iteratee])`

## _.uniq(array)

创建一个去重后的`array`数组副本。使用了[`SameValueZero`](http://ecma-international.org/ecma-262/6.0/#sec-samevaluezero) 做等值比较。只有第一次出现的元素才会被保留。

## `_.without(array, [values])`

*(Array)*: 返回过滤值后的新数组。

## `_.xor([arrays])`

*Array)*: 返回过滤值后的新数组。

tbc.