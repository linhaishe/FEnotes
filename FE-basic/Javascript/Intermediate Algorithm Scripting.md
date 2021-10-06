## Intermediate Algorithm Scripting

#### test 1

self answer

```javascript
function sumAll(arr) {
    var min = Math.min(...arr);
    var max = Math.max(...arr);
	var newarr = [];
    for(var i = min ; i <= max ; i++){
        newarr.push(i)
    }
	var ans = newarr.reduce((acc,cur)=>acc + cur);
	return ans;
}
sumAll([1, 4]);
//return 10
sumAll([10, 5]) 
//should return 45.
```

##### other ans

```javascript
function sumAll(arr) {
  var sum = 0;
  for (var i = Math.min(...arr); i <= Math.max(...arr); i++) {
    sum += i;
  }
  return sum;
}
```

#### test 2

```js
function diffArray(arr1, arr2) {
  var newArr = [];

  function onlyInFirst(first, second) {
    // Looping through an array to find elements that don't exist in another array
    for (var i = 0; i < first.length; i++) {
      if (second.indexOf(first[i]) === -1) {
        // Pushing the elements unique to first to newArr
        newArr.push(first[i]);
      }
    }
  }

  onlyInFirst(arr1, arr2);
  onlyInFirst(arr2, arr1);

  return newArr;
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
```



#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1
#### test 1