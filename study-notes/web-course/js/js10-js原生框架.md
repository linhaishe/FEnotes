#### 库框架的区别

库，一堆工具的组合，你可以理解为工具箱,jQuery就是一个库,框架，在库的基础之上，提供了一整套的解决方案,jquery，就是一个典型的单例模式的应用，因为在任何时候，你都是直接，`$('#id').方法()`，/这就可以直接调用。$在jq里，就是唯一的那个jq的实例。

shang.core.js

因为框架也好 、库也罢，基本上都有核心库，核心库的命名一般都 xx.cort.js 的这种。

#### 结构
实际的会更复杂，但大的结构，基本上都是这样。

注释

IIFE、闭包

对象字面量，

具体的业务逻辑

版本号

$，框架的实例的名，遵循jq

get

set

remove

生成随机数，业务代码

extend，继承

#### Singleton with a self executing function

```js
var User;
(function() {
	var instance;

	User = function User() {
		if (instance) {
			return instance;
		}

		instance = this;

		// all the functionality
		this.firstName = 'John';
		this.lastName = 'Doe';
        
        return instance;
	};
}());
```



