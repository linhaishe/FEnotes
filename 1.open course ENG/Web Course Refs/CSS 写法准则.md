# CSS 写法准则

就像 HTML 一样，在编写 CSS 时，你应该了解并遵循一些内部规则和行业最佳实践。

### Class 和 Id 命名

为 Class 和 Id 选择名称时，请始终使用有意义的名称。而不是表示不明的名称，始终使用反映相关元素目的的 ID 和类名称。应该首选具体且反映元素目的的名称，因为这些名称最容易理解且最不可能改变。使用有意义的名称可降低理解不同的可能性

不好的写法（无意义的写法）

```css
#yee-1901 {}
```

不好的写法

```css
.button-green {}
.clear {}
```

好的写法

```css
#gallery {}
#login {}
.video {}
```

尽可能使用尽可能短的 ID 和类名称。

不好的写法

```css
#navigation {}
.atr {}
```

好的写法

```css
#nav {}
.author {}
```

用连字符分隔 ID 和类名中的单词。除了连字符之外，不要通过任何字符（包括根本没有）连接选择器中的单词和缩写，以提高可读性。

不好的写法

```css
.demoimage {}
.error_status {}
```

好的写法

```css
.demo-image {}
.error-status {}
```

### 空格

在最后一个选择器和声明块之间使用空格。

不好的写法（没有空格）

```css
#video{
  margin-top: 1em;
}
```

不好的写法（不必要的换行）

```css
#video
{
  margin-top: 1em;
}
```

好的写法

```css
#video {
  margin-top: 1em;
}
```

出于一致性原因，始终在属性和值之间使用单个空格（但在属性和冒号之间没有空格）。

不好的写法

```css
h3 {
  font-weight:bold;
}
```

好的写法

```css
h3 {
  font-weight: bold;
}
```

换行分隔选择器和声明（声明是键值对）。始终为每个选择器和声明开始一个新行。

不好的写法

```css
h1, h2, h3 {
  font-weight: normal; line-height: 1.2;
}
```

好的写法

```css
h1,
h2,
h3 {
  font-weight: normal;
  line-height: 1.2;
}
```

换行分隔规则集。

不好的写法

```css
html {
  background: #fff;
}
body {
  margin: auto;
  width: 50%;
}
```

好的写法

```css
html {
  background: #fff;
}

body {
  margin: auto;
  width: 50%;
}
```

### 类型选择器

避免使用类型选择器限定 ID 和类名称。除非必要（例如使用帮助类），否则不要将元素名称与 ID 或类结合使用。

可接受但不推荐

```css
ul#example {}
div.error {}
```

好的写法

```css
#example {}
.error {}
```

### 简写属性

尽可能使用简写属性。

不好的写法

```css
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;
```

好的写法

```css
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

### 0s

除非需要，否则不要在 0 之后使用单位。

不好的写法

```css
margin: 0px;
padding: 0px;
```

好的写法

```css
margin: 0;
padding: 0;
```

省略值中的前导"0"。

不好的写法

```css
font-size: 0.8em;
```

好的写法

```css
font-size: .8em;
```

### 十六进制颜色

尽可能使用 3 个字符的十六进制表示法。

可接受但不推荐

```css
color: #eebbcc;
```

好的写法

```css
color: #ebc;
```