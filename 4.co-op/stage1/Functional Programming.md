# Functional Programming

函数式编程是一种编程范式，其中函数被视为一等公民，即函数可以像变量一样被传递、存储和操作。FP强调的是不可变数据和纯函数，即不产生副作用的函数。

## 函数式编程的基本概念

### 1. 纯函数和副作用

在函数式编程中，纯函数是指不依赖于外部状态和副作用的函数，即对于相同的输入，始终产生相同的输出，不会对其他部分产生影响。而副作用则是指函数除了返回一个值以外，还会对外部环境产生影响，例如修改全局变量、文件操作、网络请求等。

下面是一个纯函数的例子：

```js
function add(a, b) {
  return a + b;
}
```

这个函数接受两个参数，然后返回它们的和。无论何时调用它，对于相同的输入，始终会产生相同的输出，不会对其他部分产生任何影响，因此是一个纯函数。

而下面是一个具有副作用的函数的例子：

```js
let counter = 0;

function increment() {
  counter++;
  console.log(counter);
}
```

这个函数不仅返回一个值（这里没有返回值），还会修改全局变量`counter`，并且还会输出一些信息。这种函数会对外部环境产生影响，因此是具有副作用的函数。

纯函数和具有副作用的函数之间的区别在于函数是否依赖于外部状态和是否产生副作用。在函数式编程中，推荐使用纯函数来实现功能，以避免出现不可预期的行为和副作用。

### 2. 不可变性和可变性

在函数式编程中，不可变性是指数据在创建后不可更改，而可变性则是指数据可以在创建后随时更改。在函数式编程中，不可变性是非常重要的概念，因为它可以确保函数不会对数据产生副作用，从而使程序更加可靠和可维护。

下面是一个可变性的例子：

```js
let myArray = [1, 2, 3];
myArray.push(4);
console.log(myArray); // [1, 2, 3, 4]
```

这个例子创建了一个数组`myArray`，然后通过`push`方法向其中添加了一个元素。由于数组是可变的，因此这个操作可以成功地改变数组的内容，使得数组中添加了一个元素。

下面是一个不可变性的例子：

```js
let myArray = [1, 2, 3];
let newArray = myArray.concat(4);
console.log(myArray); // [1, 2, 3]
console.log(newArray); // [1, 2, 3, 4]
```

这个例子同样创建了一个数组`myArray`，但是通过`concat`方法创建了一个新的数组`newArray`，该数组包含了`myArray`中的所有元素以及一个新的元素4。由于数组是不可变的，因此`concat`方法没有改变原始数组`myArray`的内容，而是创建了一个新的数组`newArray`。

总之，不可变性和可变性之间的区别在于数据是否可以更改。在函数式编程中，推荐使用不可变的数据结构和操作，以确保函数不会对数据产生副作用，从而使程序更加可靠和可维护。

### 3. 函数组合和管道

function composition, function pipeline

函数组合和管道是函数式编程中常用的概念，用于将多个函数组合在一起以实现复杂的操作。

函数组合是将两个或多个函数组合在一起，形成一个新的函数，该函数将先执行第一个函数，然后将其结果作为参数传递给第二个函数，以此类推。

```js
function addOne(x) {
  return x + 1;
}

function multiplyByTwo(x) {
  return x * 2;
}

const addOneAndMultiplyByTwo = (x) => multiplyByTwo(addOne(x));

console.log(addOneAndMultiplyByTwo(2)); // 6
```

这个例子定义了两个函数`addOne`和`multiplyByTwo`，然后通过函数组合创建了一个新函数`addOneAndMultiplyByTwo`，该函数将先对参数进行加一操作，然后再对结果进行乘二操作。

管道是将多个函数组合在一起，形成一个管道，该管道将先执行第一个函数，然后将其结果作为参数传递给第二个函数，以此类推，最终得到一个结果。下面是一个管道的例子：

```js
function addOne(x) {
  return x + 1;
}

function multiplyByTwo(x) {
  return x * 2;
}

function subtractThree(x) {
  return x - 3;
}

const pipeline = [addOne, multiplyByTwo, subtractThree];

const result = pipeline.reduce((acc, fn) => fn(acc), 2);

console.log(result); // 1
```

定义了三个函数`addOne`、`multiplyByTwo`和`subtractThree`，然后将它们放在一个数组中，通过`reduce`方法依次执行它们，从而实现了一个管道。在这个例子中，初始值为2，通过管道得到了最终的结果1。

函数组合和管道是函数式编程中常用的概念，它们可以将多个函数组合在一起以实现复杂的操作。函数组合通过将多个函数组合在一起形成一个新的函数，而管道则通过依次执行多个函数得到最终的结果。

### 4. 惰性求值和延迟执行

惰性求值和延迟执行是函数式编程中的两个常用概念，它们都与函数的执行时机相关。

惰性求值指的是在需要使用函数返回值时才去执行函数。它可以提高程序的性能，避免不必要的计算。在 JavaScript 中，惰性求值通常使用函数返回函数的方式来实现。下面是一个惰性求值的例子：

```js
function createExpensiveOperation() {
  console.log('Performing expensive operation...');
  return function() {
    console.log('Returning result of expensive operation...');
    return 42;
  }
}

const expensiveOperation = createExpensiveOperation();

console.log('Before using expensive operation');
console.log(expensiveOperation()); // Performing expensive operation...  Returning result of expensive operation... 42
console.log('After using expensive operation');
console.log(expensiveOperation()); // Returning result of expensive operation... 42
```

在这个例子中，`createExpensiveOperation`函数定义了一个昂贵的操作，并返回了一个函数。当调用`createExpensiveOperation`函数时，并不会立即执行昂贵的操作，而是返回一个函数，该函数会在需要时执行昂贵的操作。

延迟执行是指将一个操作推迟到最后可能的时刻执行，这通常用于优化程序的性能。在 JavaScript 中，延迟执行通常使用函数柯里化（currying）来实现。下面是一个延迟执行的例子：

```js
function add(x) {
  return function(y) {
    return x + y;
  }
}

const addTwo = add(2);

console.log('Before using addTwo');
console.log(addTwo(3)); // 5
console.log(addTwo(4)); // 6
console.log('After using addTwo');
```

在这个例子中，`add`函数定义了一个加法操作，并返回了一个函数。当调用`add`函数时，只会传递第一个参数，并返回一个函数，该函数会在以后的调用中使用第二个参数执行加法操作。在这种方式下，加法操作被推迟到最后可能的时刻执行。

惰性求值和延迟执行是函数式编程中的两个常用概念。惰性求值可以通过函数返回函数的方式实现，延迟执行通常使用函数柯里化实现。这两个概念都可以用于优化程序的性能。

## 一些函数方法

### 1. Map 

   将数组中的每个元素映射到一个新的值，并返回一个新的数组。

```js
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(number => number * 2);
console.log(doubledNumbers); // [2, 4, 6, 8, 10]
```

```js
function map(array, callback) {
  const newArray = [];

  for (let i = 0; i < array.length; i++) {
    newArray.push(callback(array[i], i, array));
  }

  return newArray;
}

const array = [1, 2, 3, 4, 5];

const mappedArray = map(array, function(item) {
  return item * 2;
});

console.log(mappedArray); // [2, 4, 6, 8, 10]
console.log(array); // [1, 2, 3, 4, 5]
```

```js
// 手写实现
Array.prototype.myMap = function(callback) {
  const newArray = [];

  for (let i = 0; i < this.length; i++) {
    newArray.push(callback(this[i], i, this));
  }

  return newArray;
};

const array = [1, 2, 3, 4, 5];

const mappedArray = array.myMap(function(item) {
  return item * 2;
});

console.log(mappedArray); // [2, 4, 6, 8, 10]
console.log(array); // [1, 2, 3, 4, 5]
```

方法接收一个回调函数作为参数，该回调函数接收三个参数：当前元素、当前元素的索引和原数组。函数内部创建了一个空的新数组`newArray`，然后使用`for`循环遍历当前数组中的每个元素，对每个元素都执行一次回调函数，并将回调函数的返回值添加到`newArray`中。最后，函数返回新数组`newArray`，而原始数组不会被修改。

#### QA

1. `this`关键字在`myMap()`方法内部指向了数组`myArray`。

2. 内部的callback接受了三个参数，可是外部的callback只接受了一个形参item呢？

在`Array.prototype.myMap()`方法中，我们定义了一个内部的回调函数`callback`，它接受了三个参数：`currentValue`（当前元素的值）、`index`（当前元素的索引）和`array`（原数组对象）。

然而，在使用`myMap()`方法时，我们只需要传递一个回调函数作为参数，该回调函数只接受一个参数`item`（当前元素的值），而不需要显式地指定回调函数的其他两个参数（即`index`和`array`）。这是因为，JavaScript引擎在每次迭代数组时，都会自动传递`index`和`array`参数给回调函数。

这是因为，`Array.prototype.myMap()`方法中定义的回调函数会作为一个函数对象，在每次迭代数组时都会被调用。在调用回调函数时，JavaScript引擎会自动传递当前元素的值作为第一个参数（即`currentValue`），当前元素的索引作为第二个参数（即`index`），以及原数组对象作为第三个参数（即`array`）。因此，我们只需要在定义回调函数时，指定一个参数来接受当前元素的值即可。

3. JavaScript引擎在每次迭代数组时，为什么都会自动传递index和array参数给回调函数

JavaScript引擎在每次迭代数组时，都会自动传递`index`和`array`参数给回调函数，这是因为`Array.prototype.myMap()`方法是内置的JavaScript方法，它在设计时就已经考虑了这个特性，以便让开发者能够更方便地访问当前元素的索引和原数组对象。

当我们在调用`myMap()`方法时，JavaScript引擎会遍历当前数组，并在每次迭代时，调用回调函数来处理当前元素。在每次调用回调函数时，JavaScript引擎会自动传递当前元素的值作为第一个参数（即`currentValue`）、当前元素的索引作为第二个参数（即`index`），以及原数组对象作为第三个参数（即`array`）。这种行为是内置在JavaScript引擎中的，因此我们不需要在调用回调函数时手动传递这些参数。

这个特性也使得`Array.prototype.myMap()`方法的回调函数具有了更大的灵活性。我们可以使用当前元素的索引来访问数组中的其他元素，或者使用原数组对象来访问数组的长度、属性等。这些操作都可以通过回调函数中的`index`和`array`参数来实现。

### 2. Reduce 

用于将数组中的所有元素归约为单个值。

> *accumulator: 累加器
>
> accumulator is the value returned from the previous iteration. It will be initialValue for the first iteration. currentValue is array item in the current iteration.(accumulator (which is a temporary result)).
>
> The value resulting from the previous call to `callbackFn`. On first call, `initialValue` if specified, otherwise the value of `array[0]`. --- MDN

```js
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((total, number) => total + number, 0);
console.log(sum); // 15
```

```js
// 手写reduce
Array.prototype.myReduce = function(callback, initialValue) {
  let accumulator = initialValue !== undefined ? initialValue : this[0];
  for (let i = initialValue !== undefined ? 0 : 1; i < this.length; i++) {
    accumulator = callback(accumulator, this[i], i, this); 
    // callback(accumulator, this[i], i, this)  回调函数将当前元素和accumulator作计算处理(相加或者起其他你指定的方式)，并使用return语句将新的accumulator值返回。reduce()方法会将这个新的accumulator值作为下一次迭代的参数传递给回调函数，以此类推，直到所有元素都被迭代完毕。
  }
  return accumulator;
}

const arr = [1, 2, 3, 4, 5];
const sum = arr.myReduce((accumulator, currentValue) => accumulator + currentValue);
console.log(sum); // 15

const product = arr.myReduce((accumulator, currentValue) => accumulator * currentValue, 1);
console.log(product); // 120
```

`myReduce()`的方法，它接受两个参数：一个回调函数`callback`和一个可选的初始值`initialValue`。`callback`函数接受四个参数：累加器`accumulator`、当前元素的值`currentValue`、当前元素的索引`index`和原数组对象`array`。`myReduce()`方法会返回最终的累加结果。

首先需要初始化一个累加器`accumulator`，如果有传入初始值`initialValue`，则将`accumulator`初始化为该值，否则将其初始化为数组中的第一个元素。接下来，我们使用一个循环来遍历数组中的元素，对于每个元素，都会调用回调函数`callback`来将该元素的值累加到累加器中。在调用`callback`函数时，我们会传递当前累加器的值、当前元素的值、当前元素的索引和原数组对象作为参数，以便让回调函数可以访问这些值。最后，`myReduce()`方法会返回最终的累加结果。

#### 使用`reduce()`方法时，有几个需要注意的地方：

1. 累加器的初始值

`reduce()`方法的第二个参数可以用来指定累加器的初始值。如果不指定初始值，那么第一次调用回调函数时，累加器的值将是数组中的第一个元素。如果数组为空并且没有提供初始值，`reduce()`方法会抛出一个`TypeError`错误。

因此，建议在使用`reduce()`方法时，始终提供一个初始值，以确保累加器的初始值是可控的，并且在空数组的情况下也能正常工作。

2. 回调函数的参数

`reduce()`方法的回调函数接受四个参数：累加器`accumulator`、当前元素的值`currentValue`、当前元素的索引`index`和原数组对象`array`。在回调函数中，可以使用这些参数来完成各种操作。但是需要注意的是，回调函数的前两个参数是必需的，而后两个参数是可选的。如果不需要使用后两个参数，可以省略它们，但是需要注意在回调函数中不要尝试访问它们，否则会引发错误。

3. 回调函数的返回值

`reduce()`方法的回调函数必须返回一个值，以便将该值用作下一次累加器的值。如果回调函数没有返回值，或者返回值为`undefined`，则`reduce()`方法会将当前累加器的值传递给下一次迭代，而不是使用回调函数的返回值。因此，在编写回调函数时，需要确保它始终返回一个值。

```js
const arr = [1, 2, 3, 4, 5];

const result = arr.reduce((acc, val) => {
  if (val % 2 === 0) {
    acc.push(val);
  }
  // return acc; // 确保返回新数组 
  // Uncaught TypeError: Cannot read properties of undefined (reading 'push')
}, []);

console.log(result); // undefined
```

回调函数只会在数组中的偶数元素上执行，并将它们添加到一个新的数组中。然而，由于回调函数没有显式地返回这个新数组，而是返回了`undefined`，因此`reduce()`方法只是将每个偶数元素添加到当前的累加器值中，并返回了`undefined`。

为了避免这种情况，需要确保回调函数始终返回一个值。在上面的例子中，可以在回调函数的末尾添加`return acc;`语句，以确保回调函数返回新的数组。

### 3. forEach 

`forEach()`方法可以用于迭代一个数组的每个元素，并为每个元素执行回调函数。

```js
const strings = ['foo', 'bar', 'baz'];
strings.forEach(string => console.log(string));
// foo
// bar
// baz
```

```js
Array.prototype.myForEach = function(callback) {
  for (let i = 0; i < this.length; i++) {
    callback(this[i], i, this);
  }
};
```

### 4. Pick 

`pick()`函数通常用于从一个对象中选取指定的属性，并返回一个新的对象，只包含选取的属性。

```js
const user = { name: 'John', age: 30, email: 'john@example.com' };
const pickedUser = pick(user, ['name', 'email']);
console.log(pickedUser); // { name: 'John', email: 'john@example.com' }
```

```js
function pick(obj, keys) {
  return keys.reduce((acc, key) => {
    if (obj.hasOwnProperty(key)) {
      acc[key] = obj[key];
    }
    return acc;
  }, {});
}

const obj = { name: 'Alice', age: 25, city: 'New York' };
const picked = pick(obj, ['name', 'city']);

console.log(picked); // { name: 'Alice', city: 'New York' }
```

### 5. Filter 

   用于从数组中筛选出符合条件的元素，并返回一个新的数组。

```js
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(number => number % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

```js
// 手写实现
Array.prototype.myFilter = function(callback) {
  const newArray = [];

  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this)) {
      newArray.push(this[i]);
    }
  }

  return newArray;
};

const array = [1, 2, 3, 4, 5];

const mappedArray = array.myFilter(function(item) {
  return item > 3;
});

console.log(mappedArray); 
console.log(array);
```

### 6. Find 

用于从数组中查找符合条件的元素，并返回该元素的值。如果数组中有多个符合条件的元素，find方法只会返回第一个元素。

```js
const numbers = [1, 2, 3, 4, 5];
const greaterThanThree = numbers.find(number => number > 3);
console.log(greaterThanThree); // 4
```

```js
// 手写实现
Array.prototype.myFind = function(callback) {
  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this)) {
      return this[i];
    }
  }
};

const array = [1, 2, 3, 4, 5];
const mappedArray = array.myFind(function(item) {
  return item > 3;
});

console.log(mappedArray); // [4]
console.log(array); // [1, 2, 3, 4, 5]
```

Flow、compose和curry是用于将函数组合起来并生成新的函数。

### 7. Flow 

将多个函数组合起来，将一个值作为输入传入第一个函数，然后将第一个函数的输出作为输入传入第二个函数，以此类推，最终返回最后一个函数的输出结果。

```js
// 将两个函数组合起来，将一个数字乘以2，再加上3
const timesTwo = num => num * 2;
const plusThree = num => num + 3;
const timesTwoPlusThree = flow(timesTwo, plusThree);

console.log(timesTwoPlusThree(4)); // 11
```

```js
function flow(...funcs) {
  return function(arg) {
    return funcs.reduce((result, func) => func(result), arg);
  }
}
```

```js
function flow(...funcs) {
  return function(arg) {
    let result = arg;
    for (let i = 0; i < funcs.length; i++) {
      result = funcs[i](result);
    }
    return result;
  }
}
```

```js
function double(x) {
  return x * 2;
}

function square(x) {
  return x * x;
}

const doubleThenSquare = flow(double, square);

console.log(doubleThenSquare(3)); // 36
```

通过一个循环迭代所有的传入函数，并将它们的结果传递给下一个函数，从而组合它们的功能，使用`...`运算符将传入的函数作为可变参数传递给`flow`函数，并返回一个新的函数，该函数将调用所有传入的函数，并将它们的结果组合起来。

### 8. Compose 

与Flow方法类似，但是是将函数从右到左依次组合起来，将最后一个函数的输出作为输入传入倒数第二个函数，以此类推，最终返回第一个函数的输出结果。

```js
// 将两个函数组合起来，将一个数字乘以2，再加上3
const timesTwo = num => num * 2;
const plusThree = num => num + 3;
const timesTwoPlusThree = compose(plusThree, timesTwo);

console.log(timesTwoPlusThree(4)); // 11
```

```js
function compose(...funcs) {
  return function(arg) {
    let result = arg;
    for (let i = funcs.length - 1; i >= 0; i--) {
      result = funcs[i](result);
    }
    return result;
  }
}

  return function(arg) {
    return funcs.reduceRight((result, fn) => {
      return fn(result);
    }, arg);
  }
}
```

### 9. Curry 

用于将一个函数变为柯里化函数，即将一个函数接受多个参数的能力变为接受单个参数的能力。

```js
// 将一个函数接受两个参数的能力变为接受单个参数的能力
const add = (a, b) => a + b;
const curriedAdd = curry(add);

console.log(curriedAdd(2)(3)); // 5
```

```js
// 在柯里化函数中，每次调用返回一个新函数，直到最后一次调用返回函数的计算结果。
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...args2) {
        return curried.apply(this, args.concat(args2));
      }
    }
  }
}
```

这个函数接受一个函数作为参数，并返回一个新的函数。新函数将在调用时检查其接收的参数数量，如果参数数量已经等于原始函数需要的参数数量，则直接调用原始函数；否则返回另一个函数，该函数将继续接收新的参数，直到参数数量足够为止。

```js
function add(x, y, z) {
  return x + y + z;
}

const curriedAdd = curry(add);
const add5 = curriedAdd(5);
const add5And6 = add5(6);

console.log(add5And6(7)); // 18
```

### 10. 使用Flow、Compose和Curry这些函数式编程工具需要注意：

1. 函数的顺序 在使用Flow和Compose时，需要注意函数的顺序。Flow方法将函数从左到右依次组合起来，Compose方法将函数从右到左依次组合起来。因此，需要根据具体的需求选择合适的方法，并确保函数的顺序正确。
2. 函数的纯净性 函数式编程强调函数的纯净性，即函数的输出只与输入有关，不会对外部环境产生影响。在使用Flow、Compose和Curry时，需要确保组合后的函数仍然是纯净函数，避免出现副作用。
3. 参数的数量 在使用Curry时，需要注意函数的参数数量。将一个函数柯里化后，每次调用只接受一个参数。如果函数的参数数量较多，需要多次调用柯里化后的函数才能得到最终的结果。因此，需要根据具体的需求选择合适的函数和参数数量。
4. 性能问题 在使用Flow、Compose和Curry时，需要注意性能问题。组合多个函数可能会导致性能下降，特别是在处理大量数据时。因此，需要根据具体的需求选择合适的函数组合方式，并进行性能优化。