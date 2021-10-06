当你在非布尔值上使用逻辑与`&&` 运算符或逻辑或`||` 运算符时，你会碰到短路效应

短路效应中，如果左边的值属于"truthy"，逻辑或运算符`||`会返回左边的值，否则会返回右边的值

```js
var result = ("" || "hello"); // result is "hello"
result = ("Hi" || "hello"); // result is "Hi"
```

另一方面，如果左边的值属于"falsy"，那么逻辑与运算符`&&` 会返回左边的值，否则会返回右边的值

```js
var result = ("" && "hello"); // result is ""
result = ("Hi" && "hello"); // result is "hello"
```

你修改逻辑运算符使得 shouldBeHello 变量值为 "Hello" 并使 shouldBe5 变量值为 5 吗？

逻辑或运算符`||`两边只要有一个为真就会返回`true`，一真则真

`true || true` 会返回 `true`.

`true || false` 会返回 `true`.

`false || true` 会返回 `true`.

`false || false` 会返回 `false`.

逻辑与运算符`&&`只有两边都为真才返回`true`，一假则假

`true && true` 会返回`true`.
`true && false` 会返回`false`.
`false && true` 会返回`false`.
`false && false` 会返回`false`.

但使用反斜杠`\`对引号进行转义会更好

```js
var sentence = 'This is my friend\'s dog';
// This is preferred
```

其他的转义字符比如`\n`能够在字符串中创建新行

```js
var sentence = 'This is one line\nThis is second line'
// -> This is one line
// -> This is second line
```

卡尔维诺

读过的书即使忘了它也还是有用的，他可能会在无形中塑造了你的思想，给了你一些启发。

你可能把读书看成了获取知识的一种手段，而读书本身不是一种目的。折射出来的是背后的知识焦虑。

大多数人认为一定要从书本里获取知识，不然这本书我就白读了。

博尔赫兹-博闻强记的富内斯

遗忘的重要性。

你读过的书和你见过的事情，只有你忘记了，你才能从中抽象出东西来，进行归类和思考。

如果你介意遗忘，那么你会无法把曾经得到的只是进行归类，就相当于没办法通过理性进入到你的思想当中。

罗新 有所不为的反叛里

对于生命来说，遗忘是比记忆更重要的，记忆就取决于遗忘，遗忘造成的物理时间的断裂才使得我们的记忆获得意义。遗忘相对于记忆的关系就相对于死亡和生命，只有有死亡你的生命才有意义。



编写一个range函数，该函数接受两个参数start和end，并返回一个包含从start到end(包括)的所有数字的数组。

接下来，编写一个sum函数，该函数接受一个数字数组并返回这些数字的和。运行前面的程序，看看它是否确实返回55。

最后，修改你的range函数，使用第三个可选参数，该参数指示用于构建数组的“step”值。如果没有给定step值，则数组元素将递增1，这与之前的行为相对应。

函数调用range(1,10,2)应该返回[1,3,5,7,9](https://www.hackerstart.cn/course/)。

确保它也适用于负step值，以便range(5, 2， -1)产生[5,4,3,2](https://www.hackerstart.cn/course/)。

例如，如果start是0，end是5，step是1。你的数组应该是[0,1,2,3,4,5](https://www.hackerstart.cn/course/)

如果start是0，end是5，step是2，那么数组应该是[0,2,4](https://www.hackerstart.cn/course/)

如果start是0，end是5，step是3，那么数组应该是[0,3](https://www.hackerstart.cn/course/)

如果start是5,end是0,step是-1，那么数组应该是[5,4,3,2,1](https://www.hackerstart.cn/course/)

如果start是5，end是0，step是-3，那么数组应该是[5,2](https://www.hackerstart.cn/course/)

```js

function range(start, end, step) {
  var arr = [];
    if (!step) {
        step = 1;
    }
    if (step < 0) {
        for (var i = start; i >= end; i += step) {
            arr.push(i);
        }
    }
    else {
        for (var j = start; j <= end; j += step) {
            arr.push(j);
        }
    }
    return arr;
}
function sum(array) {
    var total = 0;
    for (var i = 0; i < array.length; i++) {
        total += array[i];
    }
    return total;
}
console.log(range(1, 10));
// → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(range(5, 2, -1));
// → [5, 4, 3, 2]
console.log(sum(range(1, 10)));
// → 55

```

```js
var array = ['a', 'b', 'c'];

array.forEach(function(value, index) {
  console.log('Index ' + index + ' has value ' + value);
}

// -> Index 0 has value a
// -> Index 1 has value b
// -> Index 2 has value c
```

```js
var friendsObj = {};
var friends = ['John', 'Peter', 'Mary'];
friends.forEach(function(name, index) {
  
  friendsObj[index] = name;
  
});
console.log(friendsObj[0] === 'John');
// -> true
console.log(friendsObj[1] === 'Peter');
// -> true
console.log(friendsObj[2] === 'Mary');
// -> true
```

使用“filter”方法只保留含有字符“a”的单词,即。“apple”、“orange”和“pineapple”?

```js
var words = ['hello', 'sunshine', 'apple', 'orange', 'pineapple'];
var wordsWithA = words.filter(function (word) {
// 下面实现自己的代码
  var a = 'a';
  return word.toLowerCase().indexOf(a.toLowerCase()) > -1;
});
console.log(wordsWithA[0] === 'apple');
// true
console.log(wordsWithA[1] === 'orange');
// true
console.log(wordsWithA[2] === 'pineapple');
// true
```

```js

function createGrid(height, width) {
    var chessboard = '';
    // 你的代码写在这里
    for (var y = 0; y < height; y++) {
        for (var x = 0; x < width; x++) {
            if ((x + y) % 2 === 0)
                chessboard += " ";
            else
                chessboard += "#";
        }
        chessboard += "\n";
    }
    return chessboard.substring(0,chessboard.length-1);
}
console.log(createGrid(8, 8));
console.log(createGrid(3, 3) === " # \n# #\n # ");
console.log(createGrid(4, 3) === " # \n# #\n # \n# #");
```



战略上藐视敌人，战术上重视敌人。战略上，从人生的角度上，考试不重要，它绝对不会决定你的一生。但是眼前你非得把它考好，考好了，进学校了，才能说，考试算什么。

王阳明 科举

人要修养自己，没有科举就没有晋升之阶，