####  Functional programming 

Functional programming is a style of programming where solutions are simple, isolated functions, without any side effects outside of the function scope

` INPUT -> PROCESS -> OUTPUT `

Functional programming is about:

1) Isolated functions - there is no dependence on the state of the program, which includes global variables that are subject to change

2) Pure functions - the same input always gives the same output

3) Functions with limited side effects - any changes, or mutations, to the state of the program outside the function are carefully controlled


```javascript
const prepareTea = () => 'greenTea';

/**
 * Get given number of cups of tea.
 * @param {number} numOfCups Number of required cups of tea.
 * @return {Array<string>} Given amount of tea cups.
 **/
const getTea = (numOfCups) => {
  const teaCups = [];

  for(let cups = 1; cups <= numOfCups; cups += 1) {
    const teaCup = prepareTea();
    teaCups.push(teaCup);
  }

  return teaCups;
};

//const tea4TeamFCC = null;
const tea4TeamFCC = getTea(40);

console.log(tea4TeamFCC);
```
####  higher order functions
[高阶函数](https://jcouyang.gitbooks.io/functional-javascript/content/zh/!higher-order-function.html)
The functions that take a function as an argument, or return a function as a return value are called higher order functions.

####  lambda

When the functions are passed in to another function or returned from another function, then those functions which gets passed in or returned can be called a lambda. 

```javascript
/**
 * A long process to prepare green tea.
 * @return {string} A cup of green tea.
 **/
const prepareGreenTea = () => 'greenTea';

/**
 * A long process to prepare black tea.

 * @return {string} A cup of black tea.
 **/
const prepareBlackTea = () => 'blackTea';

/**
 * Get given number of cups of tea.
 * @param {function():string} prepareTea The type of tea preparing function.
 * @param {number} numOfCups Number of required cups of tea.
 * @return {Array<string>} Given amount of tea cups.
 **/
const getTea = (prepareTea, numOfCups) => {
  const teaCups = [];

  for(let cups = 1; cups <= numOfCups; cups += 1) {
    const teaCup = prepareTea();
    teaCups.push(teaCup);
  }

  return teaCups;
};

const tea4GreenTeamFCC = getTea(prepareGreenTea,27);
const tea4BlackTeamFCC = getTea(prepareBlackTea,13);

console.log(
  tea4GreenTeamFCC,
  tea4BlackTeamFCC
);

```

#### the Hazards of Using Imperative Code

Imperative programming 命令式编程

an imperative style in programming is one that gives the computer a set of statements to perform a task. 

declarative programming 声明式编程

functional programming is a form of declarative programming. You tell the computer what you want done by calling a method or function. 

example：

 `for` loop 

 `map` method which handles the details of iterating over an array. 

要看它在哪里执行。
如果是在window里执行，那它的this一般就是执行window了。
那这个`this.tabs = tabs`，就是挂载在window上了。因为每个函数都相当于是window的属性，

`Window.prototype.join=...`，这就是把Window当成构造函数了

在真正执行的时候，都指向new出来 的那个实例了

你只需要关注，这个var Window的变量，它具体怎么执行？

是直接调用？那this指向全局的window；如果是new一个Window的实例？那指向它的实例

`splice` changes the original array it is called on, so the second call to it used a modified array, and gave unexpected results.

Examine the code in the editor. It's using a method that has side effects in the program, causing incorrect behaviour. The final list of open tabs, stored in `finalTabs.tabs`, should be `['FB', 'Gitter', 'Reddit', 'Twitter', 'Medium', 'new tab', 'Netflix', 'YouTube', 'Vine', 'GMail', 'Work mail', 'Docs', 'freeCodeCamp', 'new tab']`

```javascript
// tabs is an array of titles of each site open within the window
var Window = function(tabs) {
  this.tabs = tabs; // we keep a record of the array inside the object
  //this.tabs = [];
};

// When you join two windows into one window
Window.prototype.join = function (otherWindow) {
  this.tabs = this.tabs.concat(otherWindow.tabs);
  //this.tabs = [] = tabs + otherwindows
  return this;
  //return this 是返回tabs
};

// When you open a new tab at the end
Window.prototype.tabOpen = function (tab) {
  this.tabs.push('new tab'); 
    // let's open a new tab for now
  return this;
};

// When you close a tab
Window.prototype.tabClose = function (index) {

  // Only change code below this line

  var tabsBeforeIndex = this.tabs.splice(0, index); // get the tabs before the tab
  var tabsAfterIndex = this.tabs.splice(1); // get the tabs after the tab

  this.tabs = tabsBeforeIndex.concat(tabsAfterIndex); // join them together

  // Only change code above this line

  return this;
 };

// Let's create three browser windows
var workWindow = new Window(['GMail', 'Inbox', 'Work mail', 'Docs', 'freeCodeCamp']); 
// Your mailbox, drive, and other work sites
var socialWindow = new Window(['FB', 'Gitter', 'Reddit', 'Twitter', 'Medium']); 
// Social sites
var videoWindow = new Window(['Netflix', 'YouTube', 'Vimeo', 'Vine']); 
//  Entertainment sites

// Now perform the tab opening, closing, and other operations
var finalTabs = socialWindow
                    .tabOpen() 
// Open a new tab for cat memes
                    .join(videoWindow.tabClose(2)) 
// Close third tab in video window, and join
                    .join(workWindow.tabClose(1).tabOpen());
console.log(finalTabs.tabs);

```

```javascript
//测试return this 的返回
var Window = function(tabs) {
  this.tabs = tabs; // we keep a record of the array inside the object
  //this.tabs = [];
};

// When you join two windows into one window
Window.prototype.join = function (otherWindow) {
  this.tabs = 1;
  //this.tabs = [] = tabs + otherwindows
  return this;
  //return this 返回整个function
};
```

```javascript
//以上返回tabs
//Window.prototype.join()
[object Object] {
  join: function (otherWindow) {
  this.tabs = 1;
  return this;
},
  tabs: 1
}
```

### Avoid Mutations and Side Effects Using Functional Programming

Recall that in functional programming, changing or altering things is called mutation, and the outcome is called a side effect. A function, ideally, should be a pure function, meaning that it does not cause any side effects.

### Pass Arguments to Avoid External Dependence in a Function

Another principle of functional programming is to always declare your dependencies explicitly.This means if a function depends on a variable or object being present, then pass that variable or object directly into the function as an argument.

1. The function is easier to test, you know exactly what input it takes, and it won't depend on anything else in your program.

2. This can give you more confidence when you alter, remove, or add new code. You would know what you can or cannot change and you can see where the potential traps are.

3. Finally, the function would always produce the same output for the same set of inputs, no matter what part of the code executes it.

so far , two distinct principles for functional programming:

1) Don't alter a variable or object - create new variables and objects and return them if need be from a function.

2) Declare function arguments - any computation inside a function depends only on the arguments, and not on any global object or variable.


```javascript
// the global variable
var fixedValue = 4;

// Add your code below this line
function incrementer(value) {
  return value + 1;
  // Add your code above this line
}

var newValue = incrementer(fixedValue); // Should equal 5
console.log(fixedValue); // Should print 4
```

### Refactor Global Variables Out of Functions

从函数中重构全局变量

`bookList` should not change and still equal `["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"]`.

Passed

`newBookList` should equal `["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae", "A Brief History of Time"]`.

Passed

`newerBookList` should equal `["The Hound of the Baskervilles", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"]`.

Passed

`newestBookList` should equal `["The Hound of the Baskervilles", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae", "A Brief History of Time"]`.

此题注意 es6 ... 的使用

[JavaScript ES6— The Spread Syntax (…)]( https://codeburst.io/javascript-es6-the-spread-syntax-f5c35525f754 )

```javascript
// the global variable
var bookList = ["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"];

/* This function should add a book to the list and return the list */
// New parameters should come before bookName

function add (arr,bookName) {
  let newArr = [...arr]
  newArr.push(bookName);
  return newArr;
  }

/* This function should remove a book from the list and return the list */
// New parameters should come before the bookName one

function remove (arr,bookName) {
  let newArr = [...arr];
    //获得给与的书名所在的索引
  var book_index = bookList.indexOf(bookName);
    //如果索引大于=0，则进行删除
  if (book_index >= 0) {
    newArr.splice(book_index, 1);
    return newArr;

    }
}

var newBookList = add(bookList, 'A Brief History of Time');
var newerBookList = remove(bookList, 'On The Electrodynamics of Moving Bodies');
var newestBookList = remove(add(bookList, 'A Brief History of Time'), 'On The Electrodynamics of Moving Bodies');

console.log(bookList);
console.log(newBookList);
console.log(newerBookList);
console.log(newestBookList);

```

## map Method

```javascript
var watchList = [
  {
    "Title": "Inception",
    "Year": "2010",
    "Rated": "PG-13",
    "Released": "16 Jul 2010",
    "Runtime": "148 min",
    "Genre": "Action, Adventure, Crime",
    "Director": "Christopher Nolan",
    "Writer": "Christopher Nolan",
    "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
    "Plot": "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
    "Language": "English, Japanese, French",
    "Country": "USA, UK",
    "Awards": "Won 4 Oscars. Another 143 wins & 198 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
    "Metascore": "74",
    "imdbRating": "8.8",
    "imdbVotes": "1,446,708",
    "imdbID": "tt1375666",
    "Type": "movie",
    "Response": "True"
  },
    ...

const ratings = watchList.map(item => ({
  title: item.Title,
  rating: item.imdbRating
}));

//const ratings = watchList.map(item => ({
//  title: item["Title"],
//  rating: item["imdbRating"]
//}));

//var ratings = [];
//for(var i=0; i < watchList.length; i++){
 // ratings.push({title: watchList[i]["Title"],  
 // rating: watchList[i]["imdbRating"]});
//}

console.log(JSON.stringify(ratings));
```

### callback function

```javascript
function sayHello() {
   return "Hello, ";
}
function greeting(helloMessage, name) {
  console.log(helloMessage() + name);
}
// Pass `sayHello` as an argument to `greeting` function
greeting(sayHello, "JavaScript!");
```

We are passing our `sayHello()` function as an argument to the `greeting()` function, this explains how we are treating the function as a `value`.

The function that we pass as an argument to another function, is called a **[Callback function](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)**. *`sayHello` is a Callback function.*

`new_s` should equal `[46, 130, 196, 10]`.

```javascript
var s = [23, 65, 98, 5];

Array.prototype.myMap = function(){

  var newArray = this.map(function(arr){
    return arr * 2;
  });
  return newArray;
};

var new_s = s.myMap();

console.log(new_s);

```

```javascript
// the global Array
var s = [23, 65, 98, 5];

Array.prototype.myMap = function(callback){
  var newArray = [];
  for(var i = 0 ; i < this.length;i++){
    newArray.push(callback(this[i]));
  }
  return newArray;

};

var new_s = s.myMap(function(item){
  return item * 2;
});

console.log(new_s);

```

filteredList should equal [{"title": "Inception","rating": "8.8"},{"title": "Interstellar","rating": "8.6"},{"title": "The Dark Knight","rating": "9.0"},{"title": "Batman Begins","rating": "8.3"}].

```javascript
//自己答案
var filteredList2 = watchList.filter(item => item.imdbRating >=8.0);

var filteredList = filteredList2.map(item2 =>({
  title:item2.Title,
  rating:item2.imdbRating
}));

console.log(filteredList);

//官方答案

var filteredList = watchList
  .map(movie => {
    return {
      title: movie.Title,
      rating: movie.imdbRating
    };
  })
  .filter(movie => {
    // return true it will keep the item
    // return false it will reject the item
    return parseFloat(movie.rating) >= 8.0;
  });

console.log(filteredList);
```

```javascript
var s = [23, 65, 98, 5];
//自己答案（官网答案之一
Array.prototype.myFilter = function(callback){
var newArray = [];
for(var i = 0;i<this.length;i++){
  if(callback(this[i]) == true){
    newArray.push(this[i])
  }
}
  return newArray;
};

//官方答案（之二
Array.prototype.myFilter = function(callback) {
  var newArray = [];
  this.forEach(function(x) {
    if (callback(x) == true) {
      newArray.push(x);
    }
  });
  return newArray;
};

var new_s = s.myFilter(function(item){
  return item % 2 === 1;
});

console.log(new_s);
```

 the `splice` method mutates the original array it is called on,the `slice` method does not mutate the original array, but returns a new one which can be saved into a variable. 

Splice , slice , concat,

`Concat` offers a way to add new items to the end of an array without any mutating side effects.

```javascript
var arr = [1, 2, 3];
arr.push([4, 5, 6]);
// arr is changed to [1, 2, 3, [4, 5, 6]]
// Not the functional programming way

function nonMutatingPush(original, newItem) {
  return original.push(newItem);
}
var first = [1, 2, 3];
var second = [4, 5];

console.log(nonMutatingPush(first, second));
//4

//first
//[1, 2, 3, [4, 5]]
```

```javascript
function nonMutatingPush(original, newItem) {
  // Add your code below this line
  return original.concat(newItem);

  // Add your code above this line
}
var first = [1, 2, 3];
var second = [4, 5];

console.log(nonMutatingPush(first, second));
//返回的是一个数组
//[ 1, 2, 3, 4, 5 ]

```

reduce()

```javascript

function getRating(watchList){
 //自己的答案
var directList = watchList
  .map(movie => {
    return {
      Director: movie.Director,
      rating:movie.imdbRating
    };
  })
.filter(function(direc){
  return direc.Director == 'Christopher Nolan'
});

var averageRating = directList.reduce(
    (accumulator, currentValue) => accumulator + (currentValue.rating)/4
    ,0
);

  return averageRating;
}
console.log(getRating(watchList));

//官方答案
//每个方法都会产生一个新的数组，map()在filter()筛选出的数组上进行操作，reduce()在map()后的数组上进行操作。原数组不产生任何变动。
function getRating(watchList){
  var averageRating =
  watchList
    // Use filter to find films directed by Christopher Nolan
    .filter(film => film.Director === "Christopher Nolan")
    // Use map to convert their ratings from strings to numbers
    .map(film => Number(film.imdbRating))
    // Use reduce to add together their ratings
    .reduce((sumOfRatings, rating) => sumOfRatings + rating) /
  // Divide by the number of Nolan films to get the average rating
  watchList.filter(film => film.Director === "Christopher Nolan").length;
  return averageRating;
}
console.log(getRating(watchList));
```

```javascript
const squareList = (arr) => {
//要设置一个变量值保存数组并返回
var newarr = 
 arr
 .filter(num => num % 1 === 0 && num >0 )
 .map(num => num * num)
  return newarr;
};

// test your code
const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);
```

### sort method

 The `sort` method sorts the elements of an array according to the callback function. 

```javascript
function ascendingOrder(arr) {
  return arr.sort(function(a, b) {
    return a - b;
  });
}
ascendingOrder([1, 5, 2, 3, 4]);
// Returns [1, 2, 3, 4, 5]

function reverseAlpha(arr) {
  return arr.sort(function(a, b) {
    return a === b ? 0 : a < b ? 1 : -1;
  });
}
reverseAlpha(['l', 'h', 'z', 'b', 's']);
// Returns ['z', 's', 'l', 'h', 'b']
```

 A side effect of the `sort` method is that it changes the order of the elements in the original array. In other words, it mutates the array in place. One way to avoid this is to first concatenate an empty array to the one being sorted (remember that `slice` and `concat` return a new array), then run the `sort` method. 

```javascript
var globalArray = [5, 6, 3, 2, 9];
function nonMutatingSort(arr) {
var newarr = arr.concat();
return newarr.sort();

}
nonMutatingSort(globalArray);

//官方答案
var globalArray = [5, 6, 3, 2, 9];
function nonMutatingSort(arr) {
  return [].concat(arr).sort(function(a, b) {
    return a - b;
  });
}
nonMutatingSort(globalArray);

```

###  split method  

 splits a string into an array of strings. 

```javascript
function splitify(str) {
  // Add your code below this line
  return str.split(/\W/);
  // Add your code above this line
}
splitify("Hello World,I-am code");

var otherString = "How9are7you2today";
var byDigits = otherString.split(/\d/);
// Sets byDigits to ["How", "are", "you", "today"]
```

### join Method

```javascript
function sentensify(str) {
  // Add your code below this line
  return str.split(/\W/).join(' ');
  // Add your code above this line
}
sentensify("May-the-force-be-with-you");
```

```javascript
// the global variable
var globalTitle = "Winter Is Coming";

// Add your code below this line
function urlSlug(title) {
var newstr = title
.toLowerCase()
.trim()
.split(/\W+/)
.join('-')

return newstr;
}
// Add your code above this line

var winterComing = urlSlug(globalTitle); // Should be "winter-is-coming"

```

```javascript
function urlSlug(title) {
  return title
    .toLowerCase()
    .trim()
    .split(/\s+/)
    .join("-");
}
```

### every Method

 The `every` method works with arrays to check if *every* element passes a particular test. It returns a Boolean value - `true` if all values meet the criteria, `false` if not. 

```javascript
function checkPositive(arr) {
return arr.every(num=>num>0)
}
checkPositive([1, 2, 3, -4, 5]);
```

### some Method

 The `some` method works with arrays to check if *any* element passes a particular test. It returns a Boolean value - `true` if any of the values meet the criteria, `false` if not. 

```javascript
function checkPositive(arr) {
return arr.some(num=>num>0);
}
checkPositive([1, 2, 3, -4, 5]);
```

### Currying and Partial Application

The arity => (the number of arguments that a function can take) of a function is the number of arguments it requires. Currying a function means to convert a function of N arity into N functions of arity 1. 

In mathematics and computer science, **currying** is the technique of translating the evaluation of a function that takes multiple arguments into evaluating a sequence of functions, each with a single argument. 

 In other words, it restructures a function so it takes one argument, then returns another function that takes the next argument, and so on. 

```javascript
//Un-curried function
function unCurried(x, y) {
  return x + y;
}

//Curried function
function curried(x) {
  return function(y) {
    return x + y;
  }
}
//Alternative using ES6
const curried = x => y => x + y

curried(1)(2) // Returns 3
//save each function call into a variable, which will hold the returned function reference that takes the next argument when it's available.
// Call a curried function in parts:
var funcForY = curried(1);
console.log(funcForY(2)); // Prints 3
```

```javascript
function add(x) {
  return function(y) {
    return function(z) {
      return x + y + z;
    };
  };
}

add(10)(20)(30);
```

