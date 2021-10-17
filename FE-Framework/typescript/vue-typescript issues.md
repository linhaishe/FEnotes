# vue-typescript issues

## 1.问题1

**Type string trivially inferred from a string literal, remove type annotation (no-inferrable-types)**

```ts
function byGun(gunName: string = "M416", gunNum?: number = 1): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun();
```

究其原因可能是tslint觉得自己根据右边的"你好"判断出word的类型是string，所以，认为再写string是多此一举。

解决方法：**tslint.json添加"ignore-properties"。不推断类的属性（字段）**  代码如下:

```json
{
  "rulesDirectory": ["./src/views/About.vue"],
  "rules": {
    "no-inferrable-types": [true, "ignore-params", "ignore-properties"]
  }
}
```

## 2. 问题2
**Parameter cannot have question mark and initializer.**

```ts
function byGun(gunName: string = "M416", gunNum?: number = 1): void {
  console.log(`we gonna buy ${gunName} quantity of ${gunNum ? gunNum : 1} `);
}

byGun();
```

## 3.  问题3

**A 'set' accessor cannot have a return type annotation.**

```ts
set fullName(val): void {
    const arr = val.split(' ');
    this.firstName = arr[0];
  }
```

Setters do not support specifying a return type.

[From the language specification:](https://github.com/microsoft/TypeScript/blob/master/doc/spec-ARCHIVED.md#a2-expressions)

> *SetAccessor:*
>  `set` *PropertyName* `(` *BindingIdentifierOrPattern TypeAnnotation (optional)* `)` `{` *FunctionBody* `}`

```ts
//right
set fullName(val) {
    const arr = val.split(' ');
    this.firstName = arr[0];
  }
```

