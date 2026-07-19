> Ref:
>
> https://www.w3schools.com/go/go_getting_started.php

# Syntax

```go
package main
import ("fmt")

func main() {
  fmt.Println("Hello World!")
}

// go run test.go
```

# Comments

**Multi-line Comments**

```go
package main
import ("fmt")

func main() {
  /* The code below will print Hello World
  to the screen, and it is amazing */
  fmt.Println("Hello World!")
}
```

**single-line comment**

```go
package main
import ("fmt")

func main() {
  fmt.Println("Hello World!") // This is a comment
}
```

# Variables

- `int`- stores integers (whole numbers), such as 123 or -123
- `float32`- stores floating point numbers, with decimals, such as 19.99 or -19.99
- `string` - stores text, such as "Hello World". String values are surrounded by double quotes
- `bool`- stores values with two states: true or false

## two ways to declare

- `var variablename type = value`
- `variablename := value`

| var                                                          | :=                                                           |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Can be used **inside** and **outside** of functions          | Can only be used **inside** functions                        |
| Variable declaration and value assignment **can be done separately** | Variable declaration and value assignment **cannot be done separately** (must be done in the same line) |

```go
package main
import ("fmt")

func main() {
  var student1 string = "John" //type is string
  var student2 = "Jane" //type is inferred
  x := 2 //type is inferred

  fmt.Println(student1)
  fmt.Println(student2)
  fmt.Println(x)
}
```

```go
package main
import ("fmt")

func main() {
  var a string
  var b int
  var c bool

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
}

// a is ""
// b is 0
// c is false
```

```go
package main
import ("fmt")

func main() {
  var student1 string
  student1 = "John"
  fmt.Println(student1)
}
```

```go
// wrong
package main
import ("fmt")

a := 1

func main() {
  fmt.Println(a)
}
```

## Multiple Variable Declaration

```go
package main
import ("fmt")

func main() {
  var a, b, c, d int = 1, 3, 5, 7 
  // type keyword, it is only possible to declare one type of variable per line.

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
  fmt.Println(d)
}
```

```go
package main
import ("fmt")

func main() {
  var a, b = 6, "Hello" // without type keyword
  c, d := 7, "World!"

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
  fmt.Println(d)
}
```

```go
package main
import ("fmt")

func main() {
   var (
     a int
     b int = 1
     c string = "hello"
   )

  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
}
```

## Variable Naming Rules

- A variable name must start with a letter or an underscore character (_)
- A variable name cannot start with a digit
- A variable name can only contain alpha-numeric characters and underscores (`a-z, A-Z`, `0-9`, and `_` )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- There is no limit on the length of the variable name
- A variable name cannot contain spaces
- The variable name cannot be any Go keywords

### Camel Case

Each word, except the first, starts with a capital letter:

`myVariableName = "John"`

------

### Pascal Case

Each word starts with a capital letter:

`MyVariableName = "John"`

------

### Snake Case

Each word is separated by an underscore character:

`my_variable_name = "John"`

# Constants

`const CONSTNAME type = value`

- Constant names follow the same naming rules as [variables](https://www.w3schools.com/go/go_variable_naming_rules.php)
- Constant names are usually written in uppercase letters (for easy identification and differentiation from variables)
- Constants can be declared both inside and outside of a function

==**Constants: Unchangeable and Read-only**==

```go
package main
import ("fmt")

const PI = 3.14

func main() {
  fmt.Println(PI)
}
```

### two types of constants

- Typed constants
- Untyped constants

```go
package main
import ("fmt")

const A int = 1

func main() {
  fmt.Println(A)
}
```

```go
package main
import ("fmt")

const A = 1

func main() {
  fmt.Println(A)
}
```

```go
package main
import ("fmt")

const (
  A int = 1
  B = 3.14
  C = "Hi!"
)

func main() {
  fmt.Println(A)
  fmt.Println(B)
  fmt.Println(C)
}
```

```go
package main
import ("fmt")

// error
func main() {
  const A = 1
  A = 2
  fmt.Println(A)
}
```

# Output Functions

| **函数**        | **空格处理规则**                                             | **自动换行 (\n)**               | **支持格式化占位符 (如 %d, %s)** | **典型应用场景**                                           |
| --------------- | ------------------------------------------------------------ | ------------------------------- | -------------------------------- | ---------------------------------------------------------- |
| **`Print()`**   | 仅在**非字符串**参数之间自动添加空格。如果都是字符串，会紧贴在一起。 | ❌ 否（需手动加 `\n`）           | ❌ 否                             | 连续拼接输出、控制台进度条等不需要换行的场景。             |
| **`Println()`** | **所有**参数之间都会自动添加一个空格。                       | 是（结尾自动换行）              | ❌ 否                             | 最常用的普通打印，省去了手动加空格和换行符的麻烦。         |
| **`Printf()`**  | 完全取决于你在格式化字符串中如何编写，**不会**自动加空格。   | ❌ 否（需手动在模板末尾加 `\n`） | **是**（核心功能）               | 需要精确控制输出格式，如保留两位小数（`%.2f`）或排版对齐。 |

- `Print()`

  The `Print()` function prints its arguments with their default format.

- `Println()`

  The `Println()` function is similar to `Print()` with the difference that a whitespace is added between the arguments, and a newline is added at the end:

- `Printf()`

  The `Printf()` function first formats its argument based on the given formatting verb and then prints them.

| Verb | Description                            |
| :--- | :------------------------------------- |
| %v   | Prints the value in the default format |
| %#v  | Prints the value in Go-syntax format   |
| %T   | Prints the type of the value           |
| %%   | Prints the % sign                      |

```go
package main
import ("fmt")

func main() {
  var i,j string = "Hello","World"

  fmt.Print(i)
  fmt.Print(j)
  // HelloWorld
  
  fmt.Print(i, " ", j)
  // Hello World
}

```

```go
package main
import ("fmt")

func main() {
  var i,j string = "Hello","World"

  fmt.Println(i,j) // Hello World

}
```

```go
package main
import ("fmt")

func main() {
  var i string = "Hello"
  var j int = 15

  fmt.Printf("i has value: %v and type: %T\n", i, i)
  fmt.Printf("j has value: %v and type: %T", j, j)
}

// i has value: Hello and type: string
// j has value: 15 and type: int
```

```go
package main
import ("fmt")

func main() {
  var i = 15.5
  var txt = "Hello World!"

  fmt.Printf("%v\n", i)
  fmt.Printf("%#v\n", i)
  fmt.Printf("%v%%\n", i)
  fmt.Printf("%T\n", i)

  fmt.Printf("%v\n", txt)
  fmt.Printf("%#v\n", txt)
  fmt.Printf("%T\n", txt)
}

// 15.5
// 15.5
// 15.5%
// float64
// Hello World!
// "Hello World!"
// string
```



# Data Types

- **bool**: represents a boolean value and is either true or false
- **Numeric**: represents `integer` types, `floating point` values, and complex types
- **string**: represents a string value

```go
package main
import ("fmt")

func main() {
  var a bool = true     // Boolean
  var b int = 5         // Integer
  var c float32 = 3.14  // Floating point number
  var d string = "Hi!"  // String

  fmt.Println("Boolean: ", a)
  fmt.Println("Integer: ", b)
  fmt.Println("Float:   ", c)
  fmt.Println("String:  ", d)
}
```

## integer

- Signed Integers

  Signed integers, declared with one of the `int` keywords, can store both positive and negative values:

- Unsigned Integers

  Unsigned integers, declared with one of the `uint` keywords, can only store non-negative values:


| Type    | Size                                                         | Range                                                        |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| `int`   | Depends on platform: 32 bits in 32 bit systems and 64 bit in 64 bit systems | -2147483648 to 2147483647 in 32 bit systems and -9223372036854775808 to 9223372036854775807 in 64 bit systems |
| `int8`  | 8 bits/1 byte                                                | -128 to 127                                                  |
| `int16` | 16 bits/2 byte                                               | -32768 to 32767                                              |
| `int32` | 32 bits/4 byte                                               | -2147483648 to 2147483647                                    |
| `int64` | 64 bits/8 byte                                               | -9223372036854775808 to 9223372036854775807                  |

```go
package main
import ("fmt")

func main() {
  var x int = 500
  var y int = -4500
  fmt.Printf("Type: %T, value: %v", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
package main
import ("fmt")

func main() {
  var x uint = 500
  var y uint = 4500
  fmt.Printf("Type: %T, value: %v", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
// ./prog.go:5:7: constant 1000 overflows int8
package main
import ("fmt")

func main() {
  var x int8 = 1000
  fmt.Printf("Type: %T, value: %v", x, x)
}
```

## Float

| Type      | Size    | Range                   |
| :-------- | :------ | :---------------------- |
| `float32` | 32 bits | -3.4e+38 to 3.4e+38.    |
| `float64` | 64 bits | -1.7e+308 to +1.7e+308. |

```go
package main
import ("fmt")

func main() {
  var x float32 = 123.78
  var y float32 = 3.4e+38
  fmt.Printf("Type: %T, value: %v\n", x, x)
  fmt.Printf("Type: %T, value: %v", y, y)
}
```

```go
package main
import ("fmt")

func main() {
  var x float64 = 1.7e+308
  fmt.Printf("Type: %T, value: %v", x, x)
}
```

# Arrays

1. With the `var` keyword:

```go
var array_name = [length]datatype{values} // here length is defined
var array_name = [...]datatype{values} // here length is inferred
```

2. With the `:=` sign:

```go
array_name := [length]datatype{values} // here length is defined
array_name := [...]datatype{values} // here length is inferred
```

```go
package main
import ("fmt")

func main() {
  var arr1 = [3]int{1,2,3}
  arr2 := [5]int{4,5,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
}

// [1 2 3]
// [4 5 6 7 8]

func main() { // with inferred lengths:
  var arr1 = [...]int{1,2,3}
  arr2 := [...]int{4,5,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
}

// [1 2 3]
// [4 5 6 7 8]


func main() {
  var cars = [4]string{"Volvo", "BMW", "Ford", "Mazda"}
  fmt.Print(cars)
}

// [Volvo BMW Ford Mazda]

// Access Elements of an Array
func main() {
  prices := [3]int{10,20,30}

  fmt.Println(prices[0])
  fmt.Println(prices[2])
}

// 10
// 30

// Change Elements of an Array
func main() {
  prices := [3]int{10,20,30}

  prices[2] = 50
  fmt.Println(prices)
}

// Array Initialization
func main() {
  arr1 := [5]int{} //not initialized
  arr2 := [5]int{1,2} //partially initialized
  arr3 := [5]int{1,2,3,4,5} //fully initialized

  fmt.Println(arr1)
  fmt.Println(arr2)
  fmt.Println(arr3)
}

// Initialize Only Specific Elements
func main() {
  arr1 := [5]int{1:10,2:40}

  fmt.Println(arr1)
}
// [0 10 40 0 0]

// Find the Length of an Array
func main() {
  arr1 := [4]string{"Volvo", "BMW", "Ford", "Mazda"}
  arr2 := [...]int{1,2,3,4,5,6}

  fmt.Println(len(arr1))
  fmt.Println(len(arr2))
}
```

# Slices

Like arrays, slices are also used to store multiple values of the same type in a single variable.

However, unlike arrays, the length of a slice can grow and shrink as you see fit.

## Create a Slice

### With `[]datatype{values}`

`slice_name := []datatype{values}`

```go
myslice := []int{}

myslice := []int{1,2,3}
```

- `len()` function - returns the length of the slice (the number of elements in the slice)
- `cap()` function - returns the capacity of the slice (the number of elements the slice can grow or shrink to)

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{}
  fmt.Println(len(myslice1))
  fmt.Println(cap(myslice1))
  fmt.Println(myslice1)

  myslice2 := []string{"Go", "Slices", "Are", "Powerful"}
  fmt.Println(len(myslice2))
  fmt.Println(cap(myslice2))
  fmt.Println(myslice2)
}

// 0
// 0
// []
// 4
// 4
// [Go Slices Are Powerful]
```

### Create a Slice From an Array

```go
var myarray = [length]datatype{values} // An array
myslice := myarray[start:end] // A slice made from the array
```

```go
package main
import ("fmt")

func main() {
  arr1 := [6]int{10, 11, 12, 13, 14,15}
  myslice := arr1[2:4]

  fmt.Printf("myslice = %v\n", myslice)
  fmt.Printf("length = %d\n", len(myslice))
  fmt.Printf("capacity = %d\n", cap(myslice))
}

// myslice = [12 13]
// length = 2
// capacity = 4
```

### Create a Slice With The make() Function

The `make()` function can also be used to create a slice.

`slice_name := make([]type, length, capacity)`

> **Note:** If the *capacity* parameter is not defined, it will be equal to *length*.

```go
package main
import ("fmt")

func main() {
  myslice1 := make([]int, 5, 10)
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  // with omitted capacity
  myslice2 := make([]int, 5)
  fmt.Printf("myslice2 = %v\n", myslice2)
  fmt.Printf("length = %d\n", len(myslice2))
  fmt.Printf("capacity = %d\n", cap(myslice2))
}

// myslice1 = [0 0 0 0 0]
// length = 5
// capacity = 10
// myslice2 = [0 0 0 0 0]
// length = 5
// capacity = 5
```

## Access, Change, Append and Copy Slices

### Access

```go
package main
import ("fmt")

func main() {
  prices := []int{10,20,30}

  fmt.Println(prices[0])
  fmt.Println(prices[2])
}
```

### Change

```go
package main
import ("fmt")

func main() {
  prices := []int{10,20,30}
  prices[2] = 50
  fmt.Println(prices[0])
  fmt.Println(prices[2])
}
```

### Append

#### Append element

`slice_name = append(slice_name, element1, element2, ...)`

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{1, 2, 3, 4, 5, 6}
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = append(myslice1, 20, 21)
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))
}

// myslice1 = [1 2 3 4 5 6]
// length = 6
// capacity = 6
// myslice1 = [1 2 3 4 5 6 20 21]
// length = 8
// capacity = 12
```

#### Append sclice

`slice3 = append(slice1, slice2...)`

> **Note:** The **'...'** after *slice2* is **necessary** when appending the elements of one slice to another.

```go
package main
import ("fmt")

func main() {
  myslice1 := []int{1,2,3}
  myslice2 := []int{4,5,6}
  myslice3 := append(myslice1, myslice2...)

  fmt.Printf("myslice3=%v\n", myslice3)
  fmt.Printf("length=%d\n", len(myslice3))
  fmt.Printf("capacity=%d\n", cap(myslice3))
}

// myslice3=[1 2 3 4 5 6]
// length=6
// capacity=6
```

### Change The Length of a Slice

```go
package main
import ("fmt")

func main() {
  arr1 := [6]int{9, 10, 11, 12, 13, 14} // An array
  myslice1 := arr1[1:5] // Slice array 原数组不会被修改
  fmt.Printf("myslice1 = %v\n", myslice1) 
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = arr1[1:3] // Change length by re-slicing the array
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))

  myslice1 = append(myslice1, 20, 21, 22, 23) // Change length by appending items
  fmt.Printf("myslice1 = %v\n", myslice1)
  fmt.Printf("length = %d\n", len(myslice1))
  fmt.Printf("capacity = %d\n", cap(myslice1))
}

// myslice1 = [10 11 12 13]
// length = 4
// capacity = 5
// myslice1 = [10 11]
// length = 2
// capacity = 5
// myslice1 = [10 11 20 21 22 23]
// length = 6
// capacity = 10
```

### Memory Efficiency

 When using slices, Go loads all the underlying elements into the memory.

If the array is large and you need only a few elements, it is better to copy those elements using the `copy()` function.

The `copy()` function creates a new underlying array with only the required elements for the slice. This will reduce the memory used for the program. 

`copy(dest, src)`

```go
package main
import ("fmt")

func main() {
  numbers := []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
  // Original slice
  fmt.Printf("numbers = %v\n", numbers)
  fmt.Printf("length = %d\n", len(numbers))
  fmt.Printf("capacity = %d\n", cap(numbers))

  // Create copy with only needed numbers
  neededNumbers := numbers[:len(numbers)-10]
  numbersCopy := make([]int, len(neededNumbers))
  copy(numbersCopy, neededNumbers)

  fmt.Printf("numbersCopy = %v\n", numbersCopy)
  fmt.Printf("length = %d\n", len(numbersCopy))
  fmt.Printf("capacity = %d\n", cap(numbersCopy))
}

// Original slice
numbers = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
length = 15
capacity = 15
// New slice
numbersCopy = [1 2 3 4 5]
length = 5
capacity = 5
```

# Operators

## Arithmetic Operators

| Operator | Name           | Description                            | Example |
| :------- | :------------- | :------------------------------------- | :------ |
| +        | Addition       | Adds together two values               | x + y   |
| -        | Subtraction    | Subtracts one value from another       | x - y   |
| *        | Multiplication | Multiplies two values                  | x * y   |
| /        | Division       | Divides one value by another           | x / y   |
| %        | Modulus        | Returns the division remainder         | x % y   |
| ++       | Increment      | Increases the value of a variable by 1 | x++     |
| --       | Decrement      | Decreases the value of a variable by 1 | x--     |

```go
package main

import "fmt"

func main() {
    var a = '1' + 25
    fmt.Println(a)        // 输出数字: 74
    fmt.Printf("%c\n", a) // 输出对应的字符: J
}
// 字符 '1' 在 ASCII 码表中对应的十进制数字是 49。
```

## Assignment Operators

| Operator | Example | Same As    |
| :------- | :------ | :--------- |
| =        | x = 5   | x = 5      |
| +=       | x += 3  | x = x + 3  |
| -=       | x -= 3  | x = x - 3  |
| *=       | x *= 3  | x = x * 3  |
| /=       | x /= 3  | x = x / 3  |
| %=       | x %= 3  | x = x % 3  |
| &=       | x &= 3  | x = x & 3  |
| \|=      | x \|= 3 | x = x \| 3 |
| ^=       | x ^= 3  | x = x ^ 3  |
| >>=      | x >>= 3 | x = x >> 3 |
| <<=      | x <<= 3 | x = x << 3 |

## Comparison Operators

| Operator | Name                     | Example |
| :------- | :----------------------- | :------ |
| ==       | Equal to                 | x == y  |
| !=       | Not equal                | x != y  |
| >        | Greater than             | x > y   |
| <        | Less than                | x < y   |
| >=       | Greater than or equal to | x >= y  |
| <=       | Less than or equal to    | x <= y  |

## Logical Operators

| Operator | Name        | Description                                             | Example            |
| :------- | :---------- | :------------------------------------------------------ | :----------------- |
| &&       | Logical and | Returns true if both statements are true                | x < 5 && x < 10    |
| \|\|     | Logical or  | Returns true if one of the statements is true           | x < 5 \|\| x < 4   |
| !        | Logical not | Reverse the result, returns false if the result is true | !(x < 5 && x < 10) |

## Bitwise Operators

| Operator | Name                 | Description                                                  | Example |
| :------- | :------------------- | :----------------------------------------------------------- | :------ |
| &        | AND                  | Sets each bit to 1 if both bits are 1                        | x & y   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                   | x \| y  |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1              | x ^ b   |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right                | x << 2  |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2  |

# Conditions

## if Statement

```go
if condition {
  // code to be executed if condition is true
}
```

```go
if condition {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```

```go
if condition1 {
   // code to be executed if condition1 is true
} else if condition2 {
   // code to be executed if condition1 is false and condition2 is true
} else {
   // code to be executed if condition1 and condition2 are both false
}
```

```go
if condition1 {
   // code to be executed if condition1 is true
  if condition2 {
     // code to be executed if both condition1 and condition2 are true
  }
}
```

```go
package main
import ("fmt")

func main() {
  if 20 > 18 {
    fmt.Println("20 is greater than 18")
  }
}

func main() {
  x:= 20
  y:= 18
  if x > y {
    fmt.Println("x is greater than y")
  }
}
```

```go
func main() {
  time := 20
  if (time < 18) {
    fmt.Println("Good day.")
  } else {
    fmt.Println("Good evening.")
  }
}
```

```go
func main() {
  time := 22
  if time < 10 {
    fmt.Println("Good morning.")
  } else if time < 20 {
    fmt.Println("Good day.")
  } else {
    fmt.Println("Good evening.")
  }
}
```

```go
func main() {
  num := 20
  if num >= 10 {
    fmt.Println("Num is more than 10.")
    if num > 15 {
      fmt.Println("Num is also more than 15.")
     }
  } else {
    fmt.Println("Num is less than 10.")
  }
}
```

# switch Statement

- The expression is evaluated once
- The value of the `switch` expression is compared with the values of each `case`
- If there is a match, the associated block of code is executed
- The `default` keyword is optional. It specifies some code to run if there is no `case` match

## Single-case

All the `case` values should have the same type

```go
switch expression {
case x:
   // code block
case y:
   // code block
case z:
...
default:
   // code block
}
```

```go
package main
import ("fmt")

func main() {
  day := 4

  switch day {
  case 1:
    fmt.Println("Monday")
  case 2:
    fmt.Println("Tuesday")
  case 3:
    fmt.Println("Wednesday")
  case 4:
    fmt.Println("Thursday")
  case 5:
    fmt.Println("Friday")
  case 6:
    fmt.Println("Saturday")
  case 7:
    fmt.Println("Sunday")
  }
}
```

```go
package main
import ("fmt")

func main() {
  a := 3

  switch a {
  case 1:
    fmt.Println("a is one")
  case "b":
    fmt.Println("a is b") // ./prog.go:11:2: cannot use "b" (type untyped string) as type int
  }
}
```

## Multi-case

```go
switch expression {
case x,y:
   // code block if expression is evaluated to x or y
case v,w:
   // code block if expression is evaluated to v or w
case z:
...
default:
   // code block if expression is not found in any cases
}
```

```go
func main() {
   day := 5

   switch day {
   case 1,3,5:
    fmt.Println("Odd weekday")
   case 2,4:
     fmt.Println("Even weekday")
   case 6,7:
    fmt.Println("Weekend")
  default:
    fmt.Println("Invalid day of day number")
  }
}
```

# For Loops

The `for` loop loops through a block of code a specified number of times.

The `for` loop is the only loop available in Go.

Each execution of a loop is called an **iteration**.

```go
for statement1; statement2; statement3 {
   // code to be executed for each iteration
}
```

**statement1** Initializes the loop counter value.

**statement2** Evaluated for each loop iteration. If it evaluates to TRUE, the loop continues. If it evaluates to FALSE, the loop ends.

**statement3** Increases the loop counter value.

```go
package main
import ("fmt")

func main() {
  for i:=0; i < 5; i++ {
    fmt.Println(i)
  }
}
```

## continue / break Statement

```go
func main() {
  for i:=0; i < 5; i++ {
    if i == 3 {
      continue
    }
   fmt.Println(i)
  }
}

// 0
// 1
// 2
// 4

func main() {
  for i:=0; i < 5; i++ {
    if i == 3 {
      break
    }
   fmt.Println(i)
  }
}

// 0
// 1
// 2

func main() {
  adj := [2]string{"big", "tasty"}
  fruits := [3]string{"apple", "orange", "banana"}
  for i:=0; i < len(adj); i++ {
    for j:=0; j < len(fruits); j++ {
      fmt.Println(adj[i],fruits[j])
    }
  }
}

// big apple
// big orange
// big banana
// tasty apple
// tasty orange
// tasty banana
```

## Range Keyword

The `range` keyword is used to more easily iterate through the elements of an array, slice or map. It returns both the index and the value.

```go
for index, value := range array|slice|map {
   // code to be executed for each iteration
}
```

```go
package main
import ("fmt")

func main() {
  fruits := [3]string{"apple", "orange", "banana"}
  for idx, val := range fruits {
     fmt.Printf("%v\t%v\n", idx, val)
  }
}

// 0      apple
// 1      orange
// 2      banana
```

```go
// Tip: To only show the value or the index, you can omit the other output using an underscore (_).

func main() {
  fruits := [3]string{"apple", "orange", "banana"}
  for _, val := range fruits {
     fmt.Printf("%v\n", val)
  }
}

func main() {
  fruits := [3]string{"apple", "orange", "banana"}

  for idx, _ := range fruits {
     fmt.Printf("%v\n", idx)
  }
}
```

# Functions

```go
func FunctionName() {
  // code to be executed
}
```

```go
func FunctionName(param1 type, param2 type, param3 type) {
  // code to be executed
}
```

```go
func FunctionName(param1 type, param2 type) type {
  // code to be executed
  return output
}
```

## Naming Rules for Go Functions

- A function name must start with a letter
- A function name can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_` )
- Function names are case-sensitive
- A function name cannot contain spaces
- If the function name consists of multiple words, techniques introduced for [multi-word variable naming](https://www.w3schools.com/go/go_variable_naming_rules.php) can be used

**Tip:** Give the function a name that reflects what the function does!

```go
func myMessage() {
  fmt.Println("I just got executed!")
}

func main() {
  myMessage() // call the function
}
```

```go
// Parameters and Arguments
package main
import ("fmt")

func familyName(fname string) {
  fmt.Println("Hello", fname, "Refsnes")
}

func main() {
  familyName("Liam")
  familyName("Jenny")
  familyName("Anja")
}
```

```go
// Parameters and Arguments
func familyName(fname string, age int) {
  fmt.Println("Hello", age, "year old", fname, "Refsnes")
}

func main() {
  familyName("Liam", 3)
  familyName("Jenny", 14)
  familyName("Anja", 30)
}
```

> **Note:** When you are working with multiple parameters, the function call must have the same number of arguments as there are parameters, and the arguments must be passed in the same order.

```go
// Return Value
func myFunction(x int, y int) int {
  return x + y
}

func main() {
  fmt.Println(myFunction(1, 2))
}
```

```go
// Named Return Values
func myFunction(x int, y int) (result int) {
  result = x + y
  return // or return result
}

func main() {
  fmt.Println(myFunction(1, 2))
}
```

```go
// Multiple Return Values
func myFunction(x int, y string) (result int, txt1 string) {
  result = x + x
  txt1 = y + " World!"
  return
}

func main() {
  fmt.Println(myFunction(5, "Hello"))
}
```

## Recursion Functions

```go
package main
import ("fmt")

func testcount(x int) int {
  if x == 11 {
    return 0 // 立即结束当前函数，并把结果扔回去
  }
  fmt.Println(x)
  return testcount(x + 1)
}

func main(){
  testcount(1)
}
```

# Struct

A struct (short for structure) is used to create a collection of members of different data types, into a single variable.

While arrays are used to store multiple values of the same data type into a single variable, structs are used to store multiple values of different data types into a single variable.

A struct can be useful for grouping data together to create records.

## Declare a Struct

use the `type` and `struct` keywords:

```go
type struct_name struct {
  member1 datatype;
  member2 datatype;
  member3 datatype;
  ...
}
```

```go
type Person struct {
  name string
  age int
  job string
  salary int
}
```

```go
// Access Struct Members
package main
import ("fmt")

type Person struct {
  name string
  age int
  job string
  salary int
}

func main() {
  var pers1 Person
  var pers2 Person

  // Pers1 specification
  pers1.name = "Hege"
  pers1.age = 45
  pers1.job = "Teacher"
  pers1.salary = 6000

  // Pers2 specification
  pers2.name = "Cecilie"
  pers2.age = 24
  pers2.job = "Marketing"
  pers2.salary = 4500

  // Access and print Pers1 info
  fmt.Println("Name: ", pers1.name)
  fmt.Println("Age: ", pers1.age)
  fmt.Println("Job: ", pers1.job)
  fmt.Println("Salary: ", pers1.salary)

  // Access and print Pers2 info
  fmt.Println("Name: ", pers2.name)
  fmt.Println("Age: ", pers2.age)
  fmt.Println("Job: ", pers2.job)
  fmt.Println("Salary: ", pers2.salary)
}

// Name: Hege
// Age: 45
// Job: Teacher
// Salary: 6000
// Name: Cecilie
// Age: 24
// Job: Marketing
// Salary: 4500
```

```go
// Pass Struct as Function Arguments
package main
import ("fmt")

type Person struct {
  name string
  age int
  job string
  salary int
}

func main() {
  var pers1 Person
  var pers2 Person

  // Pers1 specification
  pers1.name = "Hege"
  pers1.age = 45
  pers1.job = "Teacher"
  pers1.salary = 6000

  // Pers2 specification
  pers2.name = "Cecilie"
  pers2.age = 24
  pers2.job = "Marketing"
  pers2.salary = 4500

  // Print Pers1 info by calling a function
  printPerson(pers1)

  // Print Pers2 info by calling a function
  printPerson(pers2)
}

func printPerson(pers Person) { // type assertion
  fmt.Println("Name: ", pers.name)
  fmt.Println("Age: ", pers.age)
  fmt.Println("Job: ", pers.job)
  fmt.Println("Salary: ", pers.salary)
}

// Name: Hege
// Age: 45
// Job: Teacher
// Salary: 6000
// Name: Cecilie
// Age: 24
// Job: Marketing
// Salary: 4500
```

# Maps

Maps are used to store data values in key:value pairs.

Each element in a map is a key:value pair.

A map is an unordered and changeable collection that does not allow duplicates.

The length of a map is the number of its elements. You can find it using the `len()` function.

The default value of a map is nil.

Maps hold references to an underlying hash table.

Go has multiple ways for creating maps.

## Create Maps

### Allowed Key Types

The map key can be of any data type for which the equality operator (`==`) is defined. These include:

- Booleans
- Numbers
- Strings
- Arrays
- Pointers
- Structs
- Interfaces (as long as the dynamic type supports equality)

Invalid key types are:

- Slices
- Maps
- Functions

These types are invalid because the equality operator (`==`) is not defined for them.

------

### Allowed Value Types

The map values can be **any** type.

### Create Maps Using `var` and `:=`

```go
var a = map[KeyType]ValueType{key1:value1, key2:value2,...}
b := map[KeyType]ValueType{key1:value1, key2:value2,...}
```

```go
package main
import ("fmt")

func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
  b := map[string]int{"Oslo": 1, "Bergen": 2, "Trondheim": 3, "Stavanger": 4}

  fmt.Printf("a\t%v\n", a)
  fmt.Printf("b\t%v\n", b)
}

// a   map[brand:Ford model:Mustang year:1964]
// b   map[Bergen:2 Oslo:1 Stavanger:4 Trondheim:3]
```

### Create Maps Using the `make()` Function:

```go
var a = make(map[KeyType]ValueType)
b := make(map[KeyType]ValueType)
```

```go
func main() {
  var a = make(map[string]string) // The map is empty now
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"
                                 // a is no longer empty
  b := make(map[string]int)
  b["Oslo"] = 1
  b["Bergen"] = 2
  b["Trondheim"] = 3
  b["Stavanger"] = 4

  fmt.Printf("a\t%v\n", a)
  fmt.Printf("b\t%v\n", b)
}

// a   map[brand:Ford model:Mustang year:1964]
// b   map[Bergen:2 Oslo:1 Stavanger:4 Trondheim:3]
```

### Create an Empty Map

```go
var a map[KeyType]ValueType
```

```go
package main
import ("fmt")

func main() {
  var a = make(map[string]string)
  var b map[string]string

  fmt.Println(a == nil) // fasle 
  fmt.Println(b == nil) // true
}
```

## Access Map Elements

`value = map_name[key]`

```go
func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Printf(a["brand"])
}
```

## Update and Add

`map_name[key] = value`

```go
package main
import ("fmt")

func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Println(a)

  a["year"] = "1970" // Updating an element
  a["color"] = "red" // Adding an element

  fmt.Println(a)
}
```

## Remove

`delete(map_name, key)`

```go
func main() {
  var a = make(map[string]string)
  a["brand"] = "Ford"
  a["model"] = "Mustang"
  a["year"] = "1964"

  fmt.Println(a)

  delete(a,"year")

  fmt.Println(a)
}
```

## Check

`val, ok :=map_name[key]`

```go
func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964", "day":""}

  val1, ok1 := a["brand"] // Checking for existing key and its value
  val2, ok2 := a["color"] // Checking for non-existing key and its value
  val3, ok3 := a["day"]   // Checking for existing key and its value
  _, ok4 := a["model"]    // Only checking for existing key and not its value

  fmt.Println(val1, ok1)
  fmt.Println(val2, ok2)
  fmt.Println(val3, ok3)
  fmt.Println(ok4)
}

// Ford true
//  false
//  true
// true
```

## Iterate Over

use `range` to iterate over maps.

```go
package main
import ("fmt")

func main() {
  a := map[string]int{"one": 1, "two": 2, "three": 3, "four": 4}

  for k, v := range a {
    fmt.Printf("%v : %v, ", k, v)
  }
}
```

Maps are unordered data structures. If you need to iterate over a map in a specific order, you must have a separate data structure that specifies that order.

```go
// Iterate Over Maps in a Specific Order

package main
import ("fmt")

func main() {
  a := map[string]int{"one": 1, "two": 2, "three": 3, "four": 4}

  var b []string             // defining the order
  b = append(b, "one", "two", "three", "four")

  for k, v := range a {        // loop with no order
    fmt.Printf("%v : %v, ", k, v)
  }

  fmt.Println()

  for _, element := range b {  // loop with the defined order
    fmt.Printf("%v : %v, ", element, a[element])
  }
}

// two : 2, three : 3, four : 4, one : 1,
// one : 1, two : 2, three : 3, four : 4,
```

Maps are references to hash tables.

If two map variables refer to the same hash table, changing the content of one variable affect the content of the other.

```go
func main() {
  var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
  b := a

  fmt.Println(a)
  fmt.Println(b)

  b["year"] = "1970"
  fmt.Println("After change to b:")

  fmt.Println(a)
  fmt.Println(b)
}

// map[brand:Ford model:Mustang year:1964]
// map[brand:Ford model:Mustang year:1964]
// After change to b:
// map[brand:Ford model:Mustang year:1970]
// map[brand:Ford model:Mustang year:1970]
```













