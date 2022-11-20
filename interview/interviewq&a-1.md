# 零、html/css

## 1. 选择器优先级关系

   内联样式 > ID 选择器 > 类选择器 = 属性选择器 = 伪类选择器 > 标签选择器 = 伪元素选择器

## 2. 清除浮动的方法

   1. 后面不需要浮动的块元素。加clear：both;

   2. <mark>让父级触发BFC</mark>（Block Formatting Context-块级格式化上下文）效果BFC格式化成最开始的样式，标准文档流。使得其浮动元素会被父级计算高度，从而也就避免了高度塌陷。

      [Example](https://codepen.io/linhaishe/pen/VwPXQVz?editors=1000)

      [深入理解：overflow:hidden——溢出,坍塌,清除浮动](https://blog.csdn.net/Hukaihe/article/details/51298665)

      触发方式：

      - 浮动元素：float值为left、right
      - display的值为inline-block、inltable-cell、table-caption、table、inline-table、flex、inline-flex、grid、inline-grid
      - overflow值不为 visible，为 auto、scroll、hidden
      - position的值为absolute或fixed

   3. 利用伪元素

      <img src="http://tva1.sinaimg.cn/large/005NUwygly1h7l024gm14j30v40tkadp.jpg" alt="image-20210906160312195.png" style="zoom: 33%;" />
      
      refs: https://www.cnblogs.com/SallyShan/p/11470549.html

## 3. w3c盒模型和ie盒模型的区别？

`box-sizing property`

**W3C盒模型**：width就等于内容区的width -> `box-sizing: content-box`

**IE盒模型/标准盒模型**：width = margin + border + padding + content -> `box-sizing: border-box`

如果你希望所有元素都使用替代模式，而且确实很常用，设置 box-sizing 在 `<html> `元素上，然后设置所有元素继承该属性。

```css
html {
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}
```

## 4. 介绍 CSS 隐藏页面中某个元素的几种方法

1. `display: none`

    通过 CSS 操控 display，移出文档流

2. `opacity: 0`

    透明度为0，仍在文档流中，当作用于其上的事件(如点击)仍有效

3. `visibility: hidden`

    透明度为0，仍在文档流中，**但作用于其上的事件(如点击)无效**，这也是 `visibility:hidden` 与 `opacity: 0` 的区别

4. `content-visibility: hidden;`

    移出文档流，但是再次显示时消耗性能低

5. 绝对定位于当前页面的不可见位置

    ```css
    position: absolute;
    top: -9000px;
    left: -9000px;  
    ```

6. `font-size: 0;` 字体大小设置为 0

7. `clip-path`: 通过裁剪的形式

```css
.hide {
  clip-path: polygon(0px 0px,0px 0px,0px 0px,0px 0px);
}
```

## 5. 什么是媒体查询，JS 可以监听媒体查询吗

## 6. `flex:1`是什么

它表示 flex 项目扩展并填充可用空间。

https://www.zhangxinxu.com/wordpress/2019/12/css-flex-basis/

https://www.51cto.com/article/683878.html

https://ishadeed.com/article/css-flex-property/

在Flex布局中，一个Flex子项的宽度是由元素自身尺寸，`flex-basis`设置的基础尺寸，以及外部填充（`flex-grow`）或收缩（`flex-shrink`）规则3者共同决定的。基础尺寸由CSS `flex-basis`属性，`width`等属性以及`box-sizing`盒模型共同决定；

`flex: 1  ===  flex: 1 1 0%`

```css
flex-grow: 1;
flex-shrink: 1;
flex-basis: 0%;
```

1. flex-grow : 1;    ➜ The div will grow in same proportion as the window-size       

2. flex-shrink : 1;  ➜ The div will shrink in same proportion as the window-size 

3. flex-basis : 0;   ➜ The div does not have a starting value as such and will take up screen as per the screen size available for

   这个div没有一个起始值，它将根据可用的屏幕尺寸占用屏幕。

   e.g: - if 3 divs are in the wrapper then each div will take 33%.


![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h865ix62qlj30co053js6.jpg)on IE it is `1 1 0px`

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h865n2smfgj30bb04bq3f.jpg)In Chrome Ver 84

## 7. em/px/rem/vh/vw区别?

### 总结

px：绝对单位，页面按精确像素展示

em：相对单位，基准点为父节点字体的大小，如果自身定义了font-size按自身来计算，整个页面内1em不是一个固定的值

rem：相对单位，可理解为root em, 相对根节点html的字体大小来计算

vh、vw：主要用于页面视口大小布局，在页面布局上更加方便简单

在`css`单位中，可以分为长度单位、绝对单位，如下表所指示

| CSS单位      |                                        |
| ------------ | -------------------------------------- |
| 相对长度单位 | em、ex、ch、rem、vw、vh、vmin、vmax、% |
| 绝对长度单位 | cm、mm、in、px、pt、pc                 |

这里我们主要讲述px、em、rem、vh/vw

### px
px，（pixel：像素）表示像素，所谓像素就是呈现在我们显示器上的一个个小点，每个像素点都是大小等同的，所以像素为计量单位被分在了绝对长度单位中，有些人会把px认为是相对长度，原因在于在移动端中存在设备像素比，px实际显示的大小是不确定的，这里之所以认为px为绝对单位，在于px的大小和元素的其他属性无关。

### em
em是相对长度单位。它的名字由來是一個英文字母`m`的寬度，故叫em。相对于当前对象内文本的字体尺寸。如当前对行内文本的字体尺寸未被人为设置，则相对于浏览器的默认字体尺寸（1em = 16px）、为了简化 font-size 的换算，我们需要在css中的 body 选择器中声明`font-size = 62.5%` 或者 `font-size: 10px` ，这就使 em 值变为 16px * 62.5% = 10px；这样 12px = 1.2em, 10px = 1em, 也就是说只需要将你的原来的px 数值除以 10，然后换上 em 作为单位就行了

**特点：**

- em 的值并不是固定的
- em 会继承父级元素的字体大小
- em 是相对长度单位。相对于当前对象内文本的字体尺寸。如当前对行内文本的字体尺寸未被人为设置，则相对于浏览器的默认字体尺寸
- 任意浏览器的默认字体高都是 16px

```html
<div class="big">
  我是14px=1.4rem<div class="small">我是12px=1.2rem</div>
</div>
```

```css
html {
  font-size: 10px;
} /*  公式16px*62.5%=10px  */

.big {
  font-size: 1.4rem;
}

.small {
  font-size: 1.2rem;
}
```

### rem
rem，相对单位，==相对的只是HTML根元素`font-size`的值==

同理，如果想要简化`font-size`的转化，我们可以在根元素`html`中加入`font-size: 62.5%`

```css
html {
  font-size: 62.5%;  
} /*  公式 16px * 62.5% = 10px  */ 
```

这样页面中 1rem =10px、1.2rem =12px、1.4rem =14px、1.6rem =16px;使得视觉、使用、书写都得到了极大的帮助。

特点：

1. rem单位可谓集相对大小和绝对大小的优点于一身
2. 和em不同的是rem总是相对于根元素，而不像em一样使用级联的方式来计算尺寸

### vh、vw
vw ，vw = view width; vh = view height。就是根据窗口的宽度，分成100等份，100vw就表示满宽，50vw就表示一半宽。（vw 始终是针对窗口的宽），同理，vh则为窗口的高度

这里的窗口分成几种情况：

在桌面端，指的是浏览器的可视区域

移动端指的就是布局视口

像vw、vh，比较容易混淆的一个单位是%，不过百分比宽泛的讲是相对于父元素：

对于普通定位元素就是我们理解的父元素
对于position: absolute;的元素是相对于已定位的父元素
对于position: fixed;的元素是相对于 ViewPort（可视窗口）

## 8. 设备像素、css像素、设备独立像素、dpr、ppi 之间的区别？

无缩放情况下，1个CSS像素等于1个设备独立像素

设备像素由屏幕生产之后就不发生改变，而设备独立像素是一个虚拟单位会发生改变

PC端中，1个设备独立像素 = 1个设备像素 （在100%，未缩放的情况下）

在移动端中，标准屏幕（160ppi）下 1个设备独立像素 = 1个设备像素

设备像素比（dpr） = 设备像素 / 设备独立像素

每英寸像素（ppi），值越大，图像越清晰

## 9. 你对BFC的理解？

<mark>让父级触发BFC</mark>（Block Formatting Context-块级格式化上下文）效果BFC格式化成最开始的样式，标准文档流。使得其浮动元素会被父级计算高度，从而也就避免了高度塌陷。

## 10. ==元素水平垂直居中的方法有哪些？如果元素不定宽高呢？==
### 内联元素居中布局

水平居中

- 行内元素可设置：text-align: center
- flex布局设置父元素：display: flex; justify-content: center

```css
.content {
  border: 1px solid red;
  height: 100px;
  text-align: center;
  /*   display: flex;
  justify-content: center; */
}

<div class="content">水平居中</div>
```

垂直居中

- 单行文本父元素确认高度：height = line-height
- 多行文本父元素确认高度：display: table-cell; vertical-align: middle
- 水平+垂直居中： display: flex; justify-content: center;  align-items: center;

```css
<div class="content">垂直居中单行文本</div>

.content {
  border: 1px solid red;
  height: 100px;
  display: flex;
  justify-content: center;
}
```

```css
<div class="content">垂直居中单行文本</div>

.content {
  border: 1px solid red;
  height: 100px;
  display: table-cell;
  vertical-align: middle;
}
```

```css
<div class="content">垂直居中单行文本</div>

.content {
  border: 1px solid red;
  height: 100px;
  line-height: 100px;
}
```

```css
<div class="content">
dddergvrgvrsfvtegbsdffergvrsvbwergfvrbvwdfwrgbbrtvsrgsbvdddergvrgvrsfvtegbsdffergvrsvbwergfvrbvwdfwrgbbrtvsrgsbvdddergvrgvr
</div>

.content {
  border: 1px solid red;
  height: 100px;
  word-break: break-all;
  display: table-cell; 
  vertical-align: middle
}
```

### 块级元素居中布局

#### 水平居中

##### 1. 定宽: margin: 0 auto

##### 2. 绝对定位+left:50%+margin:负自身一半

 `margin: auto;` 其实相当于 `margin: auto auto auto auto;`，`margin: 0 auto;`相当于`margin: 0 auto 0 auto;`

==margin: auto / margin: 0 auto实现的原理需要注意==

#### 垂直居中

##### 1. 利用定位+margin:auto

```css
.father {
  width: 500px;
  height: 300px;
  border: 1px solid #0a3b98;
  position: relative;
}
.son {
  width: 100px;
  height: 40px;
  background: #f0a238;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
}

```

```html
<div class="father">
  <div class="son"></div>
</div>
```

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h863lggki1j30te0i8gly.jpg" alt="image.png" style="zoom:33%;" />

##### 2. 利用定位+margin:负值

```css
.father {
  position: relative;
  width: 200px;
  height: 200px;
  background: skyblue;
}
.son {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -50px;
  margin-top: -50px;
  width: 100px;
  height: 100px;
  background: red;
}

```

```html
<div class="father">
  <div class="son"></div>
</div>
```

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h863o4pazaj30bw0bq3yh.jpg" alt="image.png" style="zoom:33%;" />

##### 3. 利用定位+transform

```css
.father {
  position: relative;
  width: 200px;
  height: 200px;
  background: pink;
}
.son {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100px;
  height: 100px;
  background: green;
}

```

##### 4. table布局

```css
.father {
  display: table-cell;
  width: 200px;
  height: 200px;
  background: skyblue;
  vertical-align: middle;
  text-align: center;
}
.son {
  display: inline-block;
  width: 100px;
  height: 100px;
  background: red;
}

```

##### 5. flex布局

```css
.father {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
  background: skyblue;
}
.son {
  width: 100px;
  height: 100px;
  background: red;
}

```

##### 6. grid布局

```css
.father {
  display: grid;
  align-items: center;
  justify-content: center;
  width: 200px;
  height: 200px;
  background: skyblue;
}
.son {
  width: 10px;
  height: 10px;
  border: 1px solid red;
}
```

## 19. ==如何实现单行／多行文本溢出的省略样式？==

### 1. 单行文本溢出省略

```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
```

```js
p {
  overflow: hidden;
  line-height: 40px;
  width: 400px;
  height: 40px;
  border: 1px solid red;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

```html
<p>
  这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本这是一些文本
</p> 
```

实现方式也很简单，涉及的css属性有：

1. `text-overflow`：规定当文本溢出时，显示省略符号来代表被修剪的文本。具有以下属性：

​	`clip`：当对象内文本溢出部分裁切掉

​	`ellipsis`：当对象内文本溢出时显示省略标记（...）

​	`text-overflow`只有在设置了`overflow:hidden`和`white-space:nowrap`才能够生效的

​	<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8agb6k3oxj31cy176try.jpg" alt="image.png" style="zoom:33%;" />

2. `white-space`：设置文字是否换行

   `white-space:nowrap`，作用是设置文本不换行，是`overflow:hidden`和`text-overflow:ellipsis`生效的基础

   ==pre-wrap这些没看懂==

| 值       | 描述                                                         |
| :------- | :----------------------------------------------------------- |
| normal   | 默认。空白会被浏览器忽略。                                   |
| pre      | 空白会被浏览器保留。其行为方式类似 HTML 中的 `<pre>` 标签。  |
| nowrap   | 文本不会换行，文本会在在同一行上继续，直到遇到 `<br>`标签为止。 |
| pre-wrap | 保留空白符序列，但是正常地进行换行。                         |
| pre-line | 合并空白符序列，但是保留换行符。                             |

3. `overflow`：文字长度超出限定宽度，则隐藏超出的内容

`overflow设为hidden`，普通情况用在块级元素的外层隐藏内部溢出元素，或者配合下面两个属性实现文本溢出省略

### 2. 多行文本溢出省略

```css
.demo {
  width: 400px;
  border: 1px solid red;
  display: -webkit-box;
  overflow: hidden;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis; 
}
```

```html
<div class='demo'>这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本</div>
```

- `display: -webkit-box`：和1结合使用，将对象作为弹性伸缩盒子模型显示
- `-webkit-line-clamp: 2`：用来限制在一个块元素显示的文本的行数，为了实现该效果，它需要组合其他的WebKit属性）
- `-webkit-box-orient: vertical`：和1结合使用 ，设置或检索伸缩盒对象的子元素的排列方式
- `overflow: hidden`：文本溢出限定的宽度就隐藏内容
- `text-overflow: ellipsis`：多行文本的情况下，用省略号“…”隐藏溢出范围的文本

需要注意的是，如果文本为一段很长的英文或者数字，则需要添加`word-wrap: break-word`属性

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8agqwqbdrj31ac0sw13o.jpg" alt="image.png" style="zoom:33%;" />

~~1. 基于高度截断~~ 效果差，不建议用于回答

~~伪元素 + 定位~~

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8agdch7t7j30si09maah.jpg" alt="image.png" style="zoom:33%;" />

```css
.demo {
  position: relative;
  line-height: 20px;
  height: 40px;
  overflow: hidden;
  border: 1px solid red;
}

.demo::after {
  content: "...";
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 0 20px 0 10px;
}
```

```html
<div class='demo'>这是一段很长的文本</div>
```

- 兼容性好，对各大主流浏览器有好的支持
- 响应式截断，根据不同宽度做出调整

一般文本存在英文的时候，可以设置`word-break: break-all`使一个单词能够在换行时进行拆分

```css
<div class='mulLineTruncate3'>
hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohel
</div>

/* 1:单行文本溢出 */
.textTruncate1 {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

/* 2:按行数-多行文本溢出(兼容性不好) */
.mulLineTruncate2 {
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

/* 3:按高度-多行文本溢出(没有省略号) */
.mulLineTruncate3 {
  max-height: 40px;
  overflow: hidden;
  line-height: 20px;
}

/* 4:解决3方案没有省略号的情况 */
.mulLineTruncate4 {
  border: 1px solid red;
  position: relative;
  max-height: 40px;
  overflow: hidden;
  line-height: 20px;
  word-wrap: break-word;
}
.mulLineTruncate4::after {
  position: absolute;
  right: 0;
  bottom: 0;
  padding: 0 20px 0 10px;
  content: "...";
}

.mulLineTruncate5 {
  position: relative;
  max-height: 40px;
  overflow: hidden;
  line-height: 20px;
  &::after {
    position: absolute;
    right: 0;
    bottom: 0;
    padding: 0 20px 0 10px;
    content: "...";
  }
}
```

## 11. ==如何实现两栏布局，右侧自适应？三栏布局中间自适应呢？==

## 12. flexbox（弹性盒布局模型），以及适用场景？

[intro](https://vue3js.cn/interview/css/flexbox.html)

**[Flexbox](https://www.geeksforgeeks.org/introduction-to-css-flexbox/):** The CSS Flexbox offers a ==**one-dimensional layout**==. It is helpful in allocating and aligning the space among items in a container (made of grids). It works with all kinds of display devices and screen sizes.

**[Grid](https://www.geeksforgeeks.org/css-grid-property/): **CSS Grid Layout, is a ==**two-dimensional**== grid-based layout system with rows and columns, making it easier to design web pages without having to use floats and positioning. Like tables, grid layout allow us to align elements into columns and rows.

## 13. 介绍一下grid网格布局

[intro](https://vue3js.cn/interview/css/grid.html#%E4%B8%80%E3%80%81%E6%98%AF%E4%BB%80%E4%B9%88)

## 14. ==CSS3新增了哪些新特性？==

https://juejin.cn/post/6844903486618861575

选择器、Transition,Transform和Animation、边框、背景

## 15. ==CSS3动画有哪些？==

`css`实现动画的方式，有如下几种：

- transition 实现渐变动画
- transform 转变动画
- animation 实现自定义动画

| 属性               | 含义                                                         |
| ------------------ | ------------------------------------------------------------ |
| transition（过度） | 用于设置元素的样式过度，和animation有着类似的效果，但细节上有很大的不同 |
| transform（变形）  | 用于元素进行旋转、缩放、移动或倾斜，和设置样式的动画并没有什么关系，就相当于color一样用来设置元素的“外表” |
| translate（移动）  | 只是transform的一个属性值，即移动                            |
| animation（动画）  | 用于设置动画属性，他是一个简写的属性，包含6个属性            |

## 16. 怎么理解回流跟重绘？什么场景下会触发？

在`HTML`中，每个元素都可以理解成一个盒子，在浏览器解析过程中，会涉及到回流与重绘：

- 回流：布局引擎会根据各种样式计算每个盒子在页面上的大小与位置
- 重绘：当计算好盒模型的位置、大小及其他属性后，浏览器根据每个盒子特性进行绘制

==**触发回流一定会触发重绘，反之不一定**==

在页面初始渲染阶段，回流不可避免的触发，可以理解成页面一开始是空白的元素，后面添加了新的元素使页面布局发生改变

当我们对 `DOM` 的修改引发了 `DOM`几何尺寸的变化（比如修改元素的宽、高或隐藏元素等）时，浏览器需要重新计算元素的几何属性，然后再将计算的结果绘制出来

当我们对 `DOM`的修改导致了样式的变化（`color`或`background-color`），却并未影响其几何属性时，浏览器不需重新计算元素的几何属性、直接为该元素绘制新的样式，这里就仅仅触发了重绘

### 回流触发时机

回流这一阶段主要是计算节点的位置和几何信息，那么当页面布局和几何信息发生变化的时候，就需要回流。

- 添加或删除可见的DOM元素
- 元素的位置发生变化
- 元素的尺寸发生变化（包括外边距、内边框、边框大小、高度和宽度等）
- 内容发生变化，比如文本变化或图片被另一个不同尺寸的图片所替代
- 页面一开始渲染的时候（这避免不了）
- 浏览器的窗口尺寸变化（因为回流是根据视口的大小来计算元素的位置和大小的）

### 重绘触发时机

1. 颜色的修改
2. 文本方向的修改
3. 阴影的修改

## 17. 什么是响应式设计？响应式设计的基本原理是什么？如何做？

响应式网站设计（Responsive Web design）是一种网络页面设计布局，页面的设计与开发应当根据用户行为以及设备环境(系统平台、屏幕尺寸、屏幕定向等)进行相应的响应和调整

**总结方式：**

- 弹性盒子（包括图片、表格、视频）和媒体查询等技术
- 使用百分比布局创建流式布局的弹性UI，同时使用媒体查询限制元素的尺寸和内容变更范围
- 使用相对单位使得内容自适应调节
- 选择断点，针对不同断点实现不同布局和内容展示

实现响应式布局的方式有如下：

- 媒体查询
- 百分比
- vw/vh
- rem

响应式布局优点可以看到：

- 面对不同分辨率设备灵活性强
- 能够快捷解决多设备显示适应问题

缺点：

- 仅适用布局、信息、框架并不复杂的部门类型网站
- 兼容各种设备工作量大，效率低下
- 代码累赘，会出现隐藏无用的元素，加载时间加长
- 其实这是一种折中性质的设计解决方案，多方面因素影响而达不到最佳效果
- 一定程度上改变了网站原有的布局结构，会出现用户混淆的情况

## 18. 如果要做优化，CSS提高性能的方法有哪些？

- 内联首屏关键CSS
- 异步加载CSS
- 资源压缩
- 合理使用选择器
- 减少使用昂贵的属性
- 不要使用@import
- 减少重排操作，以及减少不必要的重绘
- 了解哪些属性可以继承而来，避免对这些属性重复编写
- cssSprite，合成所有icon图片，用宽高加上backgroud-position的背景图方式显现出我们要的icon图，减少了http请求
- 把小的icon图片转成base64编码
- CSS3动画或者过渡尽量使用transform和opacity来实现动画，不要使用left和top属性

## 20. 如何使用css完成视差滚动效果?

https://vue3js.cn/interview/css/visual_scrolling.html

## 21. CSS如何画一个三角形？原理是什么？

https://vue3js.cn/interview/css/triangle.html

## 22. 让Chrome支持小于12px 的文字方式有哪些？区别？

常见的解决方案有：

1. `Zoom` 非标属性，有兼容问题，缩放会改变了元素占据的空间大小，触发重排
   - zoom:50%，表示缩小到原来的一半
   - zoom:0.5，表示缩小到原来的一半

2. `-webkit-transform:scale()` 大部分现代浏览器支持，并且对英文、数字、中文也能够生效，缩放不会改变了元素占据的空间大小，页面布局不会发生变化

3. `-webkit-text-size-adjust:none`对谷歌浏览器有版本要求，在27之后，就取消了该属性的支持，并且只对英文、数字生效
   - percentage：字体显示的大小；
   - auto：默认，字体大小会根据设备/浏览器来自动调整；
   - none:字体大小不会自动调整

```html
<style type="text/css">
    .span1{
        font-size: 12px;
        display: inline-block;
        zoom: 0.8;
    }
    .span2{
        display: inline-block;
        font-size: 12px;
    }
</style>
<body>
    <span class="span1">测试10px</span>
    <span class="span2">测试12px</span>
</body>
```

```html
<style type="text/css">
    .span1{
        font-size: 12px;
        display: inline-block;
        -webkit-transform:scale(0.8);
    }
    .span2{
        display: inline-block;
        font-size: 12px;
    }
</style>
<body>
    <span class="span1">测试10px</span>
    <span class="span2">测试12px</span>
</body>
```

```css
html { -webkit-text-size-adjust: none; }
```

## 23. 对css预编语言的理解？有哪些区别?

https://vue3js.cn/interview/css/sass_less_stylus.html#%E4%BA%8C%E3%80%81%E6%9C%89%E5%93%AA%E4%BA%9B


# 一、JS

## 一、数据类型

### 1. JavaScript有哪些数据类型，它们的区别？

JavaScript共有八种数据类型，分别是 Undefined、Null、Boolean、Number、String、Object、Symbol、BigInt。 其中 Symbol 和 BigInt 是ES6 中新增的数据类型： 

un sos bnb
#### Symbol & BigInt
- Symbol 代表创建后独一无二且不可变的数据类型，它主要是为了解决可能出现的全局变量冲突的问题。 

- BigInt 是一种数字类型的数据，它可以表示任意精度格式的整数，使用 BigInt 可以安全地存储和操作大整数，即使这个数已经超出了 Number 能够表示的安全整数范围。

#### 可分为原始数据类型和引用数据类型

- 栈：原始数据类型（Undefined、Null、Boolean、Number、String） 

- 堆：引用数据类型（对象、数组和函数）

### 2. 数据类型检测方式

#### a. typeof

Array , object , null typeof -> object

缺点：引用类型无法判断

```js
console.log(typeof 2);               // number
console.log(typeof true);            // boolean
console.log(typeof 'str');           // string
console.log(typeof function(){});    // function
console.log(typeof undefined);       // undefined

console.log(typeof {});              // object
console.log(typeof []);              // object    
console.log(typeof null);            // object
```

#### b. instanceof

instanceof可以正确判断对象的类型，其内部运行机制是判断在其原型链中能否找到该类型的原型。

缺点：instanceof只能正确判断引用数据类型，而不能判断基本数据类型。

instanceof 运算符可以用来测试一个对象在其原型链中是否存在一个构造函数的 prototype 属性。

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 

console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

#### c. constructor

constructor有两个作用，一是判断数据的类型，二是对象实例通过 constrcutor 对象访问它的构造函数。需要注意，如果创建一个对象来改变它的原型，constructor就不能用来判断数据类型了

```js
console.log((2).constructor === Number); // true
console.log((true).constructor === Boolean); // true
console.log(('str').constructor === String); // true
console.log(([]).constructor === Array); // true
console.log((function() {}).constructor === Function); // true
console.log(({}).constructor === Object); // true
```

```js
function Fn(){};

Fn.prototype = new Array();

var f = new Fn();

console.log(f.constructor === Fn);    // false
console.log(f.constructor === Array); // true
```

#### d. Object.prototype.toString.call()

Object.prototype.toString.call() 使用 Object 对象的原型方法 toString 来判断数据类型

```js
var a = Object.prototype.toString;
 
console.log(a.call(2));
console.log(a.call(true));
console.log(a.call('str'));
console.log(a.call([]));
console.log(a.call(function(){}));
console.log(a.call({}));
console.log(a.call(undefined));
console.log(a.call(null));
```

同样是检测对象obj调用toString方法，obj.toString()的结 果和Object.prototype. tostring.cal(obj)的结果不一样，这是为什么?

这是因为toString是Object的原型方法，而Array、 function等类型作为Object的实例,都重写了toString方法。不同的对象类型调用toString方法时，根据原型链的知识，调用的是对应的重写之后的toString方法(function类型返回内容为函数体的字符串，Array类型返回元素组成的字符串)，而不会去调用Object.上原型toString方法(返回对象的具体类型)， 所以采用obj.toString()不能得到其对象类型，只能将obj转换为字符串类型;因此，在想要得到对象的具体类型时，应该调用Object原型上的toString方法。

#### e. 自创

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

### 3. 检测数组的方式有哪些

```js
Object.prototype.toString.call(obj).slice(8,-1) === 'Array';
obj.__proto__ === Array.prototype;
Array.isArrray(obj);
obj instanceof Array
Array.prototype.isPrototypeOf(obj)
```

### 4. 数组常用的方法

会影响原数组 ⭕️，不会影响原数组 ❌。

1. 操作方法

   - 增

     - `push()`: 方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度 ⭕️
     - `unshift()`: 在数组开头添加任意多个值，然后返回新的数组长度 ⭕️
     - `splice()`: 传入三个参数，分别是开始位置、0（要删除的元素数量）、插入的元素，返回空数组 ⭕️
     - `concat()`: 首先会创建一个当前数组的副本，然后再把它的参数添加到副本末尾，最后返回这个新构建的数组 ❌

   - 删

     - `pop()`: 用于删除数组的最后一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `shift()`: 用于删除数组的第一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `splice()`: 传入两个参数，分别是开始位置，删除元素的数量，返回包含删除元素的数组 ⭕️
     - `slice()`: 不影响原数组：创建一个包含原有数组中一个或多个元素的新数组 ❌

   - 改

     `splice()`: 传入三个参数，分别是开始位置，要删除元素的数量，要插入的任意多个元素，返回删除元素的数组，对原数组产生影响 ⭕️

   - 查

     - `indexOf()`: 返回要查找的元素在数组中的位置，如果没找到则返回 -1❌
     - `includes()`: 返回要查找的元素在数组中的位置，找到返回`true`，否则`false` ❌
     - `find()`: 返回第一个匹配的元素 ❌
     - `findIndex()`: ❌

2. 转换方法：`join()`: 接收一个参数，即字符串分隔符，返回包含所有项的字符串 ❌

3. 排序方法：

   - `reverse()`: 顾名思义，将数组元素方向反转 ⭕️
   - `sort()`: 接受一个比较函数，用于判断哪个值应该排在前面 ⭕️

4. 迭代/遍历方法

- `some()`: 对数组每一项都运行传入的函数，如果有一项函数返回 true ，则这个方法返回 true ❌

- `every()`: 对数组每一项都运行传入的函数，如果对每一项函数都返回 true ，则这个方法返回 true ❌

- `forEach()`: 对数组每一项都运行传入的函数，没有返回值 ❌

- `filter()`: 对数组每一项都运行传入的函数，函数返回 `true` 的项会组成数组之后返回 ❌

- `map()`: 对数组每一项都运行传入的函数，返回由每次函数调用的结果构成的数组 ❌

- `reduce()`: ❌

### 5. 数组遍历方法

| **方法**                  | **是否改变原数组** | **特点**                                                     |
| ------------------------- | ------------------ | ------------------------------------------------------------ |
| forEach()                 | 否                 | 数组方法，不改变原数组，没有返回值                           |
| map()                     | 否                 | 数组方法，不改变原数组，有返回值，可链式调用                 |
| filter()                  | 否                 | 数组方法，过滤数组，返回包含符合条件的元素的数组，可链式调用 |
| for...of...               | 否                 | for...of遍历具有Iterator迭代器的对象的属性，返回的是数组的元素、对象的属性值，不能遍历普通的obj对象，将异步循环变成同步循环 |
| every() 和 some()         | 否                 | 数组方法，some()只要有一个是true，便返回true；而every()只要有一个是false，便返回false. |
| find() 和 findIndex()     | 否                 | 数组方法，find()返回的是第一个符合条件的值；findIndex()返回的是第一个返回条件的值的索引值 |
| reduce() 和 reduceRight() | 否                 | 数组方法，reduce()对数组正序操作；reduceRight()对数组逆序操作 |


### 6. 字符串的操作方法

1. 操作方法

   - 增

     - concat():用于将一个或多个字符串拼接成一个新字符串

   - 删

     这里的删的意思并不是说删除原字符串的内容，而是创建字符串的一个副本，再进行操作

     - slice()
     - substr()
     - substring()

   - 改

     - trim()、trimLeft()、trimRight()
     - repeat()
     - padStart()、padEnd()
     - toLowerCase()、 toUpperCase()

   - 查

     - chatAt():返回给定索引位置的字符，由传给方法的整数参数指定
     - indexOf():从字符串开头去搜索传入的字符串，并返回位置（如果没找到，则返回 -1 ）
     - startWith():从字符串中搜索传入的字符串，并返回一个表示是否包含的布尔值
     - includes():从字符串中搜索传入的字符串，并返回一个表示是否包含的布尔值

2. 转换方法

   - Split:把字符串按照指定的分割符，拆分成数组中的每一项

3. 模版匹配方法

   - match():接收一个参数，可以是一个正则表达式字符串，也可以是一个`RegExp`对象，返回数组
   - search():接收一个参数，可以是一个正则表达式字符串，也可以是一个`RegExp`对象，找到则返回匹配索引，否则返回 -1
   - replace():接收两个参数，第一个参数为匹配的内容，第二个参数为替换的元素（可用函数

### 7. ⚡️检测对象的方式有哪些

```js
Object.prototype.toString.call({}) === 'Object';
obj instanceof object
console.log(({}).constructor === Object); // true
```

### 8. null和undefined区别

- 首先 Undefined 和 Null 都是基本数据类型，这两个基本数据类型分别都只有一个值，就是 undefined 和 null。 

- undefined 代表的含义是未定义，null 代表的含义是空对象。一般变量声明了但还没有定义的时候会返回 undefined，null主要用于赋值给一些可能会返回对象的变量，作为初始化。 

- undefined 在 JavaScript 中不是一个保留字，这意味着可以使用 undefined 来作为一个变量名，但是这样的做法是非常危险的，它会影响对 undefined 值的判断。我们可以通过一些方法获得安全的 undefined 值，比如说 void 0。

- 当对这两种类型使用 typeof 进行判断时，Null 类型化会返回 “object”，这是一个历史遗留的问题。当使用双等号对两种类型的值进行比较时会返回 true，使用三个等号时会返回 false。

### 9. intanceof 操作符的实现原理及实现 

instanceof 运算符用于判断构造函数的 prototype 属性是否出现在对象的原型链中的任何位置。

```js
function _instanceof(L, R) {
  if (typeof L !== 'object') return false
  // L : 实例对象
  // R : 构造函数
  let O = R.prototype;
  L = L._proto_;
  while (true) {
    if (L === null) {
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

let a = { name: '冯总' }
console.log(instance_of(a, Object));//true
```

```js
function myInstanceof(left, right) {
  // 获取对象的原型
  let proto = Object.getPrototypeOf(left)
  // 获取构造函数的 prototype 对象
  let prototype = right.prototype; 
 
  // 判断构造函数的 prototype 对象是否在对象的原型链上
  while (true) {
    if (!proto) return false;
    if (proto === prototype) return true;
    // 如果没有找到，就继续从其原型上找，Object.getPrototypeOf方法用来获取指定对象的原型
    proto = Object.getPrototypeOf(proto);
  }
}
```

```js
Object.prototype.toString({})       // "[object Object]"
Object.prototype.toString.call({})  // 同上结果，加上call也ok
Object.prototype.toString.call(1)    // "[object Number]"
Object.prototype.toString.call('1')  // "[object String]"
Object.prototype.toString.call(true)  // "[object Boolean]"
Object.prototype.toString.call(function(){})  // "[object Function]"
Object.prototype.toString.call(null)   //"[object Null]"
Object.prototype.toString.call(undefined) //"[object Undefined]"
Object.prototype.toString.call(/123/g)    //"[object RegExp]"
Object.prototype.toString.call(new Date()) //"[object Date]"
Object.prototype.toString.call([])       //"[object Array]"
Object.prototype.toString.call(document)  //"[object HTMLDocument]"
Object.prototype.toString.call(window)   //"[object Window]"
```

### 10. 为什么`0.1+0.2 ! == 0.3`，如何让其相等

[Javascript 数字精度丢失的问题](https://vue3js.cn/interview/JavaScript/loss_accuracy.html#%E4%B8%80%E3%80%81%E5%9C%BA%E6%99%AF%E5%A4%8D%E7%8E%B0)

计算机是通过二进制的方式存储数据的，所以计算机计算0.1+0.2的时候，实际上是计算的两个数的二进制的和。

0.1，0.2 表示为二进制会有精度的损失，比较时可引入一个很小的数值 `Number.EPSILON` 容忍误差，其值为 2^-52。

在ES6中，提供了`Number.EPSILON`属性，而它的值就是2^-52.

判断`0.1 + 0.2 - 0.3`是否小于`Number.EPSILON`，如果小于，就可以判断为`0.1 + 0.2 === 0.3`

```js
function equal(a, b) {
  return Math.abs(a - b) < Number.EPSILON;
}

console.log(numberepsilon(0.1 + 0.2, 0.3)); // true
```

### 11. 如何获取安全的 undefined 值？ 

因为 undefined 是一个标识符，所以可以被当作变量来使用和赋值，但是这样会影响 undefined 的正常判断。表达式 `void ___ `没有返回值，因此返回结果是 undefined。void 并不改变表达式的结果，只是让表达式不返回值。因此可以用 void 0 来获得 undefined。

### 12. typeof NaN 的结果是什么？

NaN 指“不是一个数字”（not a number），NaN 是一个“警戒值”（sentinel value，有特殊用途的常规值），用于指出数字类型中的错误情况，即“执行数学运算没有成功，这是失败后返回的结果”。

```js
typeof NaN; // "number"
```

NaN 是一个特殊值，它和自身不相等，是唯一一个非自反（自反，reflexive，即 `x === x `不成立）的值。而 NaN !== NaN 为 true。

### 13. isNaN 和 Number.isNaN 函数的区别？ 

- 函数 isNaN 接收参数后，会尝试将这个参数转换为数值，任何不能被转换为数值的的值都会返回 true，因此非数字值传入也会返回 true ，会影响 NaN 的判断。 (is not a number 是否 不是数字，不是数字-true, 是数字false)。
- 函数 Number.isNaN 会首先判断传入参数是否为数字，如果是数字再继续判断是否为 NaN ，不会进行数据类型的转换，这种方法对于 NaN 的判断更为准确。

```js
isNaN(1);
isNaN("1");
Number.isNaN("123");
```

### 14. == 操作符的强制类型转换规则？ 

对于 == 来说，如果对比双方的类型不一样，就会进行类型转换。假如对比 x 和 y 是否相同，就会进行如下判断流程： 

1. 首先会判断两者类型是否相同，相同的话就比较两者的大小； 
2. 类型不相同的话，就会进行类型转换； 
3. 会先判断是否在对比 null 和 undefined，是的话就会返回 true 
4. 判断两者类型是否为 string 和 number，是的话就会将字符串转换为 number

```js
1 == '1'
      ↓
1 ==  1
```

5. 判断其中一方是否为 boolean，是的话就会把 boolean 转为 number 再进行判断

```js
'1' == true
        ↓
'1' ==  1
        ↓
 1  ==  1
```

6. 判断其中一方是否为 object 且另一方为 string、number 或者 symbol，是的话就会把 object 转为原始类型再进行判断

```js
'1' == { name: 'js' }
        ↓
'1' == '[object Object]'
```

![image](http://ww1.sinaimg.cn/large/005NUwyggy1gu01mn6mg6j60rx0bujsf02.jpg)

### 15. 谈谈 Javascript 中的类型转换机制

常见的类型转换有：

- 强制转换（显示转换）
- 自动转换（隐式转换）

1. Number()

![number()](http://tva1.sinaimg.cn/large/005NUwygly1h7ndy9bjjqj30kx082myl.jpg)

2. String()

![string()](http://tva1.sinaimg.cn/large/005NUwygly1h7ndynt2dgj30kn072gmy.jpg)

3. Boolean()

![boolean()](https://static.vue-js.com/53bdad10-6692-11eb-ab90-d9ae814b240d.png)

- `+` **操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==` **操作符**

### 16. 其他值到字符串的转换规则

1. Null 和 Undefined 类型 ，null 转换为 "null"，undefined 转换为 "undefined"， 
2. Boolean 类型，true 转换为 "true"，false 转换为 "false"。 
3. Number 类型的值直接转换，不过那些极小和极大的数字会使用指数形式。
4.  Symbol 类型的值直接转换，但是只允许显式强制类型转换，使用隐式强制类型转换会产生错误。 
5. 对普通对象来说，除非自行定义 toString() 方法，否则会调用 toString()（Object.prototype.toString()）来返回内部属性 [[Class]] 的值，如"[object Object]"。如果对象有自己的 toString() 方法，字符串化时就会调用该方法并使用其返回值。

### 17. 其他值到数字值的转换规则

1. Null 类型的值转换为 0。 
2. Undefined 类型的值转换为 NaN。 
3. Boolean 类型的值，true 转换为 1，false 转换为 0。 
4. String 类型的值转换如同使用 Number() 函数进行转换，如果包含非数字值则转换为 NaN，空字符串为 0。 
5. Symbol 类型的值不能转换为数字，会报错。 
6. 对象（包括数组）会首先被转换为相应的基本类型值，如果返回的是非数字的基本类型值，则再遵循以上规则将其强制转换为数字。

为了将值转换为相应的基本类型值，抽象操作 ToPrimitive 会首先（通过内部操作 DefaultValue）检查该值是否有valueOf()方法。如果有并且返回基本类型值，就使用该值进行强制类型转换。如果没有就使用 toString() 的返回值（如果存在）来进行强制类型转换。 如果 valueOf() 和 toString() 均不返回基本类型值，会产生 TypeError 错误。

### 18. 其他值到布尔类型的值的转换规则？ 

以下这些是假值： 

1. undefined 

2. null 

3. false 

4. +0、-0 和 NaN

5. ""

   假值的布尔强制类型转换结果为 false。从逻辑上说，假值列表以外的都应该是真值。

### 19. || 和 && 操作符的返回值？ 

|| 和 && 首先会对第一个操作数执行条件判断，如果其不是布尔值就先强制转换为布尔类型，然后再执行条件判断。 

**逻辑或（||）总结：**

1. 只要第一个值的布尔值为false，那么永远返回第二个值。
2. 逻辑或属于短路操作，第一个值为true时，不再操作第二个值，且返回第一个值。

**逻辑与（&&）总结：**

1. 只要第一个值的布尔值为true，那么永远返回第二个值。
2. 逻辑与属于短路操作，第一个值为false时，不再操作第二个值，且返回第一个值。

```js
// 只要第一个值的布尔值为false，那么永远返回第二个值，不管第二个值的布尔值是true还是false。
console.log(0 || '我是string，boolean值为true');          // 返回字符串
console.log(NaN || '我是string，boolean值为true');        // 返回字符串
console.log('' || '我是string，boolean值为true');         // 返回字符串
console.log(null || '我是string，boolean值为true');       // 返回字符串
console.log(undefined || '我是string，boolean值为true');  // 返回字符串
console.log(0 || 'NaN');           // 返回 NaN
console.log(NaN || '');            // 返回 '' 空字符串
console.log('' || null);           // 返回 null
console.log(null || 'undefined');  // 返回 undefined
console.log(undefined || 0);       // 返回 0

// 逻辑或短路操作
var obj = {};
console.log(obj || NaN);      // 返回 obj
console.log(obj || number);   // 返回 obj
console.log( 0 || number);    // 报错，number未定义
// 只要第一个值的布尔值为true，不再操作第二个值，直接返回第一个值，number变量未定义也不会报错。
```

```js
var obj = {};
var str = 'Riny';

/* 当第一个值的布尔值为true 返回第二个值 */
console.log(obj && 0);          // 返回 0
console.log(obj && NaN);        // 返回 NaN
console.log(obj && '');         // 返回 '' 空字符串
console.log(obj && undefined);  // 返回 undefined
console.log(obj && null);       // 返回 null

/* 当第一个值的布尔值为true 返回第二个值 */
console.log(obj && str);        // 返回 字符串
```

```js
const a = 3;
const b = -2;

console.log(a > 0 && b > 0);
```

### 20. Object.is() 与比较操作符 “=== ”、“ ==” 的区别？ 

- 使用双等号（==）进行相等判断时，如果两边的类型不一致，则会进行强制类型转化后再进行比较。 
- 使用三等号（===）进行相等判断时，如果两边的类型不一致时，不会做强制类型准换，直接返回 false。 
- 使用 Object.is 来进行相等判断时，一般情况下和三等号的判断相同，它处理了一些特殊的情况，比如 -0 和 +0 不再相等，两个 NaN 是相等的。

### 21. 什么是 JavaScript 中的包装类型

在 JavaScript 中，基本类型是没有属性和方法的，但是为了便于操作基本类型的值，在调用基本类型的属性或方法时 JavaScript 会在后台隐式地将基本类型的值转换为对象，如：

```js
const a = "abc";
a.length; // 3
a.toUpperCase(); // "ABC"
```

在访问'abc'.length时，JavaScript 将'abc'在后台转换成String('abc')，然后再访问其length属性。 JavaScript也可以使用Object函数显式地将基本类型转换为包装类型：

```js
var a = 'abc'
Object(a) // String {"abc"}
```

也可以使用valueOf方法将包装类型倒转成基本类型：

```js
var a = 'abc'
var b = Object(a)
var c = b.valueOf() // 'abc'
```

```js
var a = new Boolean( false );
if (!a) {
	console.log( "Oops" ); // never runs
}
```

### 22. JavaScript 中如何进行隐式类型转换？

- `+`**操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==`**操作符**

### 23. + 操作符什么时候用于字符串的拼接？ 

根据 ES5 规范，如果某个操作数是字符串或者能够通过以下步骤转换为字符串的话，+ 将进行拼接操作。如果其中一个操作数是对象（包括数组），则首先对其调用 ToPrimitive 抽象操作，该抽象操作再调用 [[DefaultValue]]，以数字作为上下文。如果不能转换为字符串，则会将其转换为数字类型来进行计算。 简单来说就是，如果 + 的其中一个操作数是字符串（或者通过以上步骤最终得到字符串），则执行字符串拼接，否则执行数字加法。 那么对于除了加法的运算符来说，只要其中一方是数字，那么另一方就会被转为数字。

###  24. 为什么会有BigInt的提案？ 

JavaScript中Number.MAX_SAFE_INTEGER表示最⼤安全数字，计算结果是9007199254740991，即在这个数范围内不会出现精度丢失（⼩数除外）。但是⼀旦超过这个范围，js就会出现计算不准确的情况，这在⼤数计算的时候不得不依靠⼀些第三⽅库进⾏解决，因此官⽅提出了BigInt来解决此问题。

### 25. object.assign和扩展运算法是深拷贝还是浅拷贝，两者区别

1. 扩展运算符

```js
let outObj = {
  inObj: {a: 1, b: 2}
}
let newObj = {...outObj}
newObj.inObj.a = 2
console.log(outObj) // {inObj: {a: 2, b: 2}}
```

2. Object.assign():

```js
let outObj = {
  inObj: {a: 1, b: 2}
}
let newObj = Object.assign({}, outObj)
newObj.inObj.a = 2
console.log(outObj) // {inObj: {a: 2, b: 2}}
```

可以看到，两者都是浅拷贝。 

- `Object.assign()`方法接收的第一个参数作为目标对象，后面的所有参数作为源对象。然后把所有的源对象合并到目标对象中。它会修改了一个对象，因此会触发 ES6 setter。 
- 扩展操作符（…）使用它时，数组或对象中的每一个值都会被拷贝到一个新的数组或对象中。它不复制继承的属性或类的属性，但是它会复制ES6的 symbols 属性。

### 26. ⚡️如何判断一个对象是空对象

- 使用JSON自带的JSON.stringify方法来判断：

```js
if (JSON.stringify(Obj) == "{}") {
  console.log("空对象");
}
```

- 使用ES6新增的方法Object.keys()来判断：

```js
if (Object.keys(Obj).length === 0) {
  console.log("空对象");
}
```

- for...in...

```js
function isEmpty(obj) {
  for (var prop in obj) {
    if (obj.hasOwnProperty(prop)) return false;
  }
  return true;
}
```

### 27. typeof null 的结果是什么，为什么？

typeof null 的结果是Object。 因为历史遗留问题。

在 JavaScript 第一个版本中，所有值都存储在 32 位的单元中，每个单元包含一个小的 类型标签(1-3 bits) 以及当前要存储值的真实数据。类型标签存储在每个单元的低位中，共有五种数据类型

```
000: object   - 当前存储的数据指向一个对象。
  1: int      - 当前存储的数据是一个 31 位的有符号整数。
010: double   - 当前存储的数据指向一个双精度的浮点数。
100: string   - 当前存储的数据指向一个字符串。
110: boolean  - 当前存储的数据是布尔值。
```

如果最低位是 1，则类型标签标志位的长度只有一位；如果最低位是 0，则类型标签标志位的长度占三位，为存储其他四种数据类型提供了额外两个 bit 的长度。

有两种特殊数据类型： 

- undefined的值是 (-2)30(一个超出整数范围的数字)； 
- null 的值是机器码 NULL 指针(null 指针的值全是 0) 那也就是说null的类型标签也是000，和Object的类型标签一样，所以会被判定为Object

### 28. typeof 与 instanceof 区别

- `typeof`会返回一个变量的基本类型，`instanceof`返回的是一个布尔值
- `instanceof` 可以准确地判断复杂引用数据类型，但是不能正确判断基础数据类型
- 而` typeof` 也存在弊端，它虽然可以判断基础数据类型（`null` 除外），但是引用数据类型中，除了` function` 类型以外，其他的判断类型都是object

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 
 
console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

### 29. 什么是事件代理/事件委托？应用场景？

就是把一个元素响应事件（`click`、`keydown`......）的函数委托到另一个元素

事件委托，会把一个或者一组元素的事件委托到它的父层或者更外层元素上，真正绑定事件的是外层元素，而不是目标元素

适合事件委托的事件有：`click`，`mousedown`，`mouseup`，`keydown`，`keyup`，`keypress`

从上面应用场景中，我们就可以看到使用事件委托存在两大优点：

- 减少整个页面所需的内存，提升整体性能
- 动态绑定，减少重复工作

但是使用事件委托也是存在局限性：

- `focus`、`blur`这些事件没有事件冒泡机制，所以无法进行委托绑定事件
- `mousemove`、`mouseout`这样的事件，虽然有事件冒泡，但是只能不断通过位置去计算定位，对性能消耗高，因此也是不适合于事件委托的

如果把所有事件都用事件代理，可能会出现事件误判，即本不该被触发的事件被绑定上了事件

### 30. 事件捕捉/事件冒泡

#### 1. 冒泡（bubbling）

**当一个事件发生在一个元素上，它会首先运行在该元素上的处理程序，然后运行其父元素上的处理程序，然后一直向上到其他祖先上的处理程序。**

用于停止冒泡的方法是 `event.stopPropagation()`。

`event.stopPropagation()` 停止向上移动，但是当前元素上的其他处理程序都会继续运行。

 `event.stopImmediatePropagation()` 方法，可以用于停止冒泡，并阻止当前元素上的处理程序运行。使用该方法之后，其他处理程序就不会被执行。

==阻止浏览器默认行为==：event.preventDefault()

#### 2. 捕获（capturing）

**事件首先通过祖先链向下到达元素（捕获阶段），然后到达目标（目标阶段），最后上升（冒泡阶段），在途中调用处理程序。**

### 31. Object.keys() 与 Object.getOwnPropertyNames() 有何区别

- `Object.keys`: 列出可枚举的属性值
- `Object.getOwnPropertyNames`: 列出所有属性值(包括可枚举与不可枚举)

### 32. 如何把对象转化为 key/value 的二维数组

**方法一：**

`Object.entries({ a: 3 });`

**方法二：**

```js
const obj = {
  city: "New Delhi",
  maxTemp: 32,
  minTemp: 21,
  humidity: 78,
  aqi: 456,
  day: "Tuesday"
};

const objectToArray = (obj = {}) => {
  const res = [];
  const keys = Object.keys(obj);
  for (key of keys) {
    res.push([key, obj[key]]);
  }
  
  return res;
};

console.log(objectToArray(obj));
```

### 33. 在 JS 中如何监听 Object 某个属性值的变化

[这章节对`Object.defineProperty`和`Proxy`有相关讲解](# 1. Vue的基本原理)

在 JS 中可以使用两种方式监听属性值变化

- Proxy
- Object.defineProperty

### 34. 列举 Number、String、Array、Object、Promise 有哪些 API

## 二、ES6

### 1. let, const, var区别

块级作用域，重复声明，变量提升，暂时性死区

ES6规定，`let/const` 命令会使区块形成封闭的作用域。若在声明之前使用变量，就会报错。
总之，在代码块内，使用 `let` 命令声明变量之前，该变量都是不可用的。
这在语法上，称为 **“暂时性死区”**（ temporal dead zone，简称 **TDZ**）。

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7nmhw2phaj316e0ja41z.jpg)

### 2. const 对象的属性可以更改吗

const保证的并不是变量的值不能改动，而是变量指向的那个内存地址不能改动。对于基本类型的数据（数值、字符串、布尔值），其值就保存在变量指向的那个内存地址，因此等同于常量。

但对于引用类型的数据（主要是对象和数组）来说，变量指向数据的内存地址，保存的只是一个指针，const只能保证这个指针是固定不变的，至于它指向的数据结构是不是可变的，就完全不能控制了。

### 3. 如果new一个箭头函数会怎样

箭头函数是ES6中的提出来的，它没有prototype，也没有自己的this指向，更不可以使用arguments参数，所以不能New一个箭头函数。

new操作符的实现步骤如下：

1. 创建一个对象
2. 将构造函数的作用域赋给新对象（也就是将对象的proto属性指向构造函数的prototype属性）
3. 指向构造函数中的代码，构造函数中的this指向该对象（也就是为这个对象添加属性和方法）返回新的对象

所以，上面的第二、三步，箭头函数都是没有办法执行的。

### 4. 箭头函数和普通函数的区别

- 箭头函数没有自己的this
- call()、apply()、bind()等方法不能改变箭头函数中this的指向
- 箭头函数不能作为构造函数使用
- 箭头函数没有prototype

### 5. 箭头函数的this指向哪里

箭头函数并没有属于⾃⼰的this，它所谓的this是捕获其所在上下⽂的 this 值，作为⾃⼰的 this 值，并且由于没有属于⾃⼰的this。

### 6. 扩展运算符的作用

#### 和rest参数的区别：

- **当用在函数定义时的形参前面时，称为rest参数；当函数调用时，用于接收不确定的参数。**
- **当与解构赋值组合使用时，称为rest参数，用于接收剩余的值,存储在数组中。**
- **当用在字符串或数组前面时称为扩展运算符，将数组或字符串进行拆解。**

```js
// 1. 对象扩展运算符: 复制，或者覆盖原有的属性
let bar = { a: 1, b: 2 };
let baz = { ...bar }; // { a: 1, b: 2 }

// 2. 数组扩展运算符: 可以展开数组，但是只能展开一层
console.log(...[1, 2, 3]) // 1 2 3
console.log(...[1, [2, 3, 4], 5]) // 1 [2, 3, 4] 5

// 3. 将数组转换为参数序列
function add(x, y) {
  return x + y;
}
const numbers = [1, 2];
add(...numbers) // 3

// 4. 合并数组
const arr1 = ['two', 'three'];
const arr2 = ['one', ...arr1, 'four', 'five']; // ["one", "two", "three", "four", "five"]

// 5. 扩展运算符与解构赋值结合起来，用于生成数组
const [first, ...rest] = [1, 2, 3, 4, 5];
first // 1
rest  // [2, 3, 4, 5]

// 如果将扩展运算符用于数组赋值，只能放在参数的最后一位，否则会报错
const [...rest, last] = [1, 2, 3, 4, 5];         // 报错
const [first, ...rest, last] = [1, 2, 3, 4, 5];  // 报错

// 6. 将类数组转化为真正的数组
// arguments对象 用于替换es5中的Array.prototype.slice.call(arguments)写法。
function foo() {
  const args = [...arguments];
}
```

### 7. 对rest参数的理解

1. 扩展运算符被用在函数形参上时，**它还可以把一个分离的参数序列整合成一个数组**。
2. 可以把函数的多个入参收敛进一个数组里。这一点**经常用于获取函数的多余参数，或者像上面这样处理函数参数个数不确定的情况。**

```js
function mutiple(...args) {
  let result = 1;
  for (var val of args) {
    result *= val;
  }
  return result;
}
mutiple(1, 2, 3, 4) // 24

function mutiple(...args) {
  console.log(args)
}
mutiple(1, 2, 3, 4) // [1, 2, 3, 4]
```

#### rest参数和argument的区别

arguments是一个类数组,本质是对象;方便处理函数传参。

而rest参数m,是真正的数组,可以正常调用数组的所有方法.所以在某些场景中,无需将arguments转为真正的数组,可以直接使用rest参数代替。

```js
function sumArgu() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
}
console.log(sumArgu(1, 2, 3)); // 6

function sumRest(...m) {
  var total = 0;
  for (var i of m) {
    total += i;
  }
  return total;
}
console.log(sumRest(1, 2, 3)); // 6
```

### 8. 对象与数组的解构的理解

```js
const [a, b, c] = [1, 2, 3]

const stu = {
  name: 'Bob',
  age: 24
}
const { name, age } = stu
```

### 9. 如何提取高度嵌套的对象里的指定属性

可以用解构

```js
const school = {
   classes: {
      stu: {
         name: 'Bob',
         age: 24,
      }
   }
}
const { classes: { stu: { name } }} = school
```

### 10. es6中模板语法与字符串的处理

```js
var finalString = `my name is ${name}, I work as a ${career} I love ${hobby[0]} and ${hobby[1]}`
```

### 11. proxy实现什么功能

[这章节对`Object.defineProperty`和`Proxy`有相关讲解](# 1. Vue的基本原理)

`Object.defineProperty` 无法监听到数组、对象的修改，`Proxy`可以。

在 Vue3.0 中通过 `Proxy` 来替换原本的 `Object.defineProperty` 来实现数据响应式。

```js
let onWatch = (obj, setBind, getLogger) => {
  let handler = {
    get(target, property, receiver) {
      getLogger(target, property);
      return Reflect.get(target, property, receiver);
    },
    set(target, property, value, receiver) {
      setBind(value, property);
      return Reflect.set(target, property, value);
    }
  };
  return new Proxy(obj, handler);
};
let obj = { a: 1 };
let p = onWatch(
  obj,
  (v, property) => {
    console.log(`监听到属性${property}改变为${v}`);
  },
  (target, property) => {
    console.log(`'${property}' = ${target[property]}`);
  }
);
p.a = 2; // "监听到属性a改变为2"
p.a; // 'a' = 2
```

### 12. 深拷贝和浅拷贝

- 浅拷贝是拷贝一层，属性为对象时，浅拷贝是复制，两个对象指向同一个地址
- 深拷贝是递归拷贝深层次，属性为对象时，深拷贝是新开栈，两个对象指向不同的地址

<mark>浅拷贝</mark>，如果属性是基本类型，拷贝的就是基本类型的值。如果属性是引用类型，拷贝的就是内存地址，即浅拷贝是拷贝一层，深层次的引用类型则共享内存地址。

- `Object.assign`
- `Array.prototype.slice()`, `Array.prototype.concat()`
- 使用拓展运算符实现的复制

<mark>深拷贝</mark>，深拷贝开辟一个新的栈，两个对象属完成相同，但是对应两个不同的地址，修改一个对象的属性，不会改变另一个对象的属性

常见的深拷贝方式有：

- _.cloneDeep()
- jQuery.extend()
- JSON.stringify()
- 手写循环递归

### 13. this对象的理解

`this` 关键字是函数运行时自动生成的一个内部对象，只能在函数内部使用，总指向调用它的对象。

## 三、JS基础 

### 1. new操作符的实现原理
   - new关键字会首先创建一个空对象
   - 将这个空对象的原型对象指向构造函数的原型属性，从而继承原型上的方法
   - 将this指向这个空对象，执行构造函数中的代码，以获取私有属性
   - 如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象

### 2. Map和Object的区别

|          | Map                                                          | Object                                                       |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 意外的键 | Map默认情况不包含任何键，只包含显式插入的键。                | Object 有一个原型, 原型链上的键名有可能和自己在对象上的设置的键名产生冲突。 |
| 键的类型 | Map的键可以是任意值，包括函数、对象或任意基本类型。          | Object 的键必须是 String 或是Symbol。                        |
| 键的顺序 | Map 中的 key 是有序的。因此，当迭代的时候， Map 对象以插入的顺序返回键值。 | Object 的键是无序的                                          |
| Size     | Map 的键值对个数可以轻易地通过size 属性获取                  | Object 的键值对个数只能手动计算                              |
| 迭代     | Map 是 iterable 的，所以可以直接被迭代。                     | 迭代Object需要以某种方式获取它的键然后才能迭代。             |
| 性能     | 在频繁增删键值对的场景下表现更好。                           | 在频繁添加和删除键值对的场景下未作出优化。                   |

### 3. Map和WeakMap的区别

- Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。
- WeakMap 结构与 Map 结构类似，也是用于生成键值对的集合。但是 WeakMap 只接受对象作为键名（ null 除外），不接受其他类型的值作为键名。而且 WeakMap 的键名所指向的对象，不计入垃圾回收机制。

**==Map==**

本质上就是键值对的集合，实际上Map是一个数组，它的每一个数据也都是一个数组。

```js
const map = [
  ["name", "张三"],
  ["age", 18]
];

const map = new Map([
  ["foo", 1],
  ["bar", 2]
]);

```

Map数据结构有以下操作方法：

- **size**： `map.size` 返回Map结构的成员总数。
- **set(key,value)**：设置键名key对应的键值value，然后返回整个Map结构，如果key已经有值，则键值会被更新，否则就新生成该键。（因为返回的是当前Map对象，所以可以链式调用）
- **get(key)**：该方法读取key对应的键值，如果找不到key，返回undefined。
- **has(key)**：该方法返回一个布尔值，表示某个键是否在当前Map对象中。
- **delete(key)**：该方法删除某个键，返回true，如果删除失败，返回false。
- **clear()**：map.clear()清除所有成员，没有返回值。

Map结构原生提供是三个遍历器生成函数和一个遍历方法

- keys()：返回键名的遍历器。
- values()：返回键值的遍历器。
- entries()：返回所有成员的遍历器。
- forEach()：遍历Map的所有成员。

**==WeakMap==**

WeakMap 对象也是一组键值对的集合，其中的键是弱引用的。其键必须是对象，原始数据类型不能作为key值，而值可以是任意的。

该对象也有以下几种方法：

- **set(key,value)**：设置键名key对应的键值value，然后返回整个Map结构，如果key已经有值，则键值会被更新，否则就新生成该键。（因为返回的是当前Map对象，所以可以链式调用）
- **get(key)**：该方法读取key对应的键值，如果找不到key，返回undefined。
- **has(key)**：该方法返回一个布尔值，表示某个键是否在当前Map对象中。
- **delete(key)**：该方法删除某个键，返回true，如果删除失败，返回false。

其clear()方法已经被弃用，所以可以通过创建一个空的WeakMap并替换原对象来实现清除。

WeakMap的设计目的在于，有时想在某个对象上面存放一些数据，但是这会形成对于这个对象的引用。一旦不再需要这两个对象，就必须手动删除这个引用，否则垃圾回收机制就不会释放对象占用的内存。

而WeakMap的**键名所引用的对象都是弱引用**，即垃圾回收机制不将该引用考虑在内。因此，只要所引用的对象的其他引用都被清除，垃圾回收机制就会释放该对象所占用的内存。也就是说，一旦不再需要，WeakMap 里面的**键名对象和所对应的键值对会自动消失，不用手动删除引用**。

### 4. JavaScript有哪些内置对象

js 中的内置对象主要指的是在程序执行前存在全局作用域里的由 js 定义的一些全局值属性、函数和用来实例化其他对象的构造函数对象。一般经常用到的如全局变量值 NaN、undefined，全局函数如 parseInt()、parseFloat() 用来实例化对象的构造函数如 Date、Object 等，还有提供数学计算的单体内置对象如 Math 对象。

### 5. 常用的正则表达式有哪些?

### 6. 对JSON的理解

JSON 是一种基于文本的轻量级的数据交换格式。它可以被任何的编程语言读取和作为数据格式来传递。

JSON 中对象格式更加严格，比如说在 JSON 中属性值不能为函数，不能出现 NaN 这样的属性值等，因此大多数的 js 对象是不符合 JSON 对象的格式的。

### 7. JavaScript脚本延迟加载的方式有哪些

延迟加载就是等页面加载完成之后再加载 JavaScript 文件。 js 延迟加载有助于提高页面加载速度。

一般有以下几种方式：

- **defer 属性：**给 js 脚本添加 defer 属性，这个属性会让脚本的加载与文档的解析同步解析，然后在文档解析完成后再执行这个脚本文件，这样的话就能使页面的渲染不被阻塞。多个设置了 defer 属性的脚本按规范来说最后是顺序执行的，但是在一些浏览器中可能不是这样。
- **async 属性：**给 js 脚本添加 async 属性，这个属性会使脚本异步加载，不会阻塞页面的解析过程，但是当脚本加载完成后立即执行 js 脚本，这个时候如果文档没有解析完成的话同样会阻塞。多个 async 属性的脚本的执行顺序是不可预测的，一般不会按照代码的顺序依次执行。
- **动态创建 DOM 方式：**动态创建 DOM 标签的方式，可以对文档的加载事件进行监听，当文档加载完成后再动态的创建 script 标签来引入 js 脚本。
- **使用 setTimeout 延迟方法：**设置一个定时器来延迟加载js脚本文件
- **让 JS 最后加载：**将 js 脚本放在文档的底部，来使 js 脚本尽可能的在最后来加载执行。

### 8. JavaScript类数组对象的定义?

一个拥有 length 属性和若干索引属性的对象就可以被称为类数组对象，类数组对象和数组类似，但是不能调用数组的方法。常见的类数组对象有 arguments 和 DOM 方法的返回结果，还有一个函数也可以被看作是类数组对象，因为它含有 length 属性值，代表可接收的参数个数。

常见的类数组转换为数组的方法有这样几种

```js
// 通过 call 调用数组的 slice 方法来实现转换
Array.prototype.slice.call(arrayLike);

// 通过 call 调用数组的 splice 方法来实现转换
Array.prototype.splice.call(arrayLike, 0);

// 通过 apply 调用数组的 concat 方法来实现转换
Array.prototype.concat.apply([], arrayLike);

// 通过 Array.from 方法来实现转换
Array.from(arrayLike);
```

### 12. 为什么函数的arguments参数是类数组而不是数组？如何遍历类数组？

`arguments`是一个对象，它的属性是从 0 开始依次递增的数字，还有`callee`和`length`等属性，与数组相似；但是它却没有数组常见的方法属性，如`forEach`, `reduce`等，所以叫它们类数组。

```js
// 1. 将数组的方法应用到类数组上，这时候就可以使用call和apply方法，如：
function foo(){ 
  Array.prototype.forEach.call(arguments, a => console.log(a))
}

// 2. 使用Array.from方法将类数组转化成数组:
function foo(){ 
  const arrArgs = Array.from(arguments) 
  arrArgs.forEach(a => console.log(a))
}

// 3. 使用展开运算符将类数组转化成数组
function foo(){ 
    const arrArgs = [...arguments] 
    arrArgs.forEach(a => console.log(a)) 
}
```



### 10. Unicode、 UTF-8、UTF-16、UTF-32的区别.

### 11. 常见的位运算符有哪些?其计算规则是什么

### 13. 什么是DOM和BOM?

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7po61fusnj30sz06jju0.jpg)

- DOM 指的是文档对象模型，它指的是把文档当做一个对象，这个对象主要定义了处理网页内容的方法和接口。
- BOM 指的是浏览器对象模型，它指的是把浏览器当做一个对象来对待，这个对象主要定义了与浏览器进行交互的法和接口。BOM的核心是 window，而 window 对象具有双重角色，它既是通过 js 访问浏览器窗口的一个接口，又是一个 Global（全局）对象。这意味着在网页中定义的任何对象，变量和函数，都作为全局对象的一个属性或者方法存在。window 对象含有 location 对象、navigator 对象、screen 对象等子对象，并且 DOM 的最根本的对象 document 对象也是 BOM 的 window 对象的子对象。

### 14. 常见的DOM操作有哪些

节点的增删改查

```js
getElementById // 按照 id 查询
getElementsByTagName // 按照标签名查询
getElementsByClassName // 按照类名查询
querySelectorAll // 按照 css 选择器查询

// 按照 id 查询
var imooc = document.getElementById('imooc') // 查询到 id 为 imooc 的元素
// 按照标签名查询
var pList = document.getElementsByTagName('p')  // 查询到标签为 p 的集合
console.log(divList.length)
console.log(divList[0])
// 按照类名查询
var moocList = document.getElementsByClassName('mooc') // 查询到类名为 mooc 的集合
// 按照 css 选择器查询
var pList = document.querySelectorAll('.mooc') // 查询到类名为 mooc 的集合
```

```js
// 首先获取父节点
var container = document.getElementById('container')
// 创建新节点
var targetSpan = document.createElement('span')
// 设置 span 节点的内容
targetSpan.innerHTML = 'hello world'
// 把新创建的元素塞进父节点里去
container.appendChild(targetSpan)
```

```js
// 获取目标元素的父元素
var container = document.getElementById('container')
// 获取目标元素
var targetNode = document.getElementById('title')
// 删除目标元素
container.removeChild(targetNode)
```

```js
// 获取父元素
var container = document.getElementById('container')   
 
// 获取两个需要被交换的元素
var title = document.getElementById('title')
var content = document.getElementById('content')
// 交换两个元素，把 content 置于 title 前面
container.insertBefore(content, title)
```

### 15. 说说你对BOM的理解，常见的BOM对象你了解哪些？

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7po61fusnj30sz06jju0.jpg)

**1. Window**

- `moveBy(x,y)`：从当前位置水平移动窗体x个像素，垂直移动窗体y个像素，x为负数，将向左移动窗体，y为负数，将向上移动窗体
- `moveTo(x,y)`：移动窗体左上角到相对于屏幕左上角的(x,y)点
- `resizeBy(w,h)`：相对窗体当前的大小，宽度调整w个像素，高度调整h个像素。如果参数为负值，将缩小窗体，反之扩大窗体
- `resizeTo(w,h)`：把窗体宽度调整为w个像素，高度调整为h个像素
- `scrollTo(x,y)`：如果有滚动条，将横向滚动条移动到相对于窗体宽度为x个像素的位置，将纵向滚动条移动到相对于窗体高度为y个像素的位置
- `scrollBy(x,y)`： 如果有滚动条，将横向滚动条向左移动x个像素，将纵向滚动条向下移动y个像素

**2. location**

| 属性名   | 例子                                                   | 说明                                |
| -------- | ------------------------------------------------------ | ----------------------------------- |
| hash     | "#contents"                                            | utl中#后面的字符，没有则返回空串    |
| host     | www.wrox.com:80                                        | 服务器名称和端口号                  |
| hostname | www.wrox.com                                           | 域名，不带端口号                    |
| href     | http://www.wrox.com:80/WileyCDA/?q=javascript#contents | 完整url                             |
| pathname | "/WileyCDA/"                                           | 服务器下面的文件路径                |
| port     | 80                                                     | url的端口号，没有则为空             |
| protocol | http:                                                  | 使用的协议                          |
| search   | ?q=javascript                                          | url的查询字符串，通常为？后面的内容 |

**3. navigator**

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7poa5b1fkj30qt0iu43k.jpg" alt="image.png" style="zoom:50%;" />

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7poaae43xj30on0imdkh.jpg" alt="image.png" style="zoom:50%;" />

**4. screen**

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h7po9y88gij30p00a6tar.jpg)

**5. history**

- `history.forward()`：向前跳转一个页面
- `history.back()`：向后跳转一个页面
- `history.length`：获取历史记录数

### 16. escape、 encodeURI、encodeURIComponent的区别

### 17. JavaScript为什么要进行变量提升，他导致了什么问题？

- 解析和预编译过程中的声明提升可以提高性能，让函数可以在执行时预先为变量分配栈空间
- 声明提升还可以提高JS代码的容错性，使一些不规范的代码也可以正常执行

```js
// 在这个函数中，原本是要打印出外层的tmp变量，但是因为变量提升的问题，内层定义的tmp被提到函数内部的最顶部，相当于覆盖了外层的tmp，所以打印结果为undefined。

var tmp = new Date();

function fn(){
	console.log(tmp);
	if(false){
		var tmp = 'hello world';
	}
}

fn();  // undefined
```

```js
// 由于遍历时定义的i会变量提升成为一个全局变量，在函数结束之后不会被销毁，所以打印出来11。
var tmp = 'hello world';

for (var i = 0; i < tmp.length; i++) {
	console.log(tmp[i]);
}

console.log(i); // 11
```

### 18. 什么是尾调用，使用尾调用有什么好处？

尾调用指的是函数的最后一步调用另一个函数。代码执行是基于执行栈的，所以当在一个函数里调用另一个函数时，会保留当前的执行上下文，然后再新建另外一个执行上下文加入栈中。使用尾调用的话，因为已经是函数的最后一步，所以这时可以不必再保留当前的执行上下文，从而节省了内存，这就是尾调用优化。但是 ES6 的尾调用优化只在严格模式下开启，正常模式是无效的

### 19. ES6 Module与CommonJS模块有什么异同

**区别： **

- CommonJS是对模块的浅拷⻉，ES6 Module是对模块的引⽤，即ES6 Module只存只读，不能改变其值，也就是指针指向不能变，类似const；
- import的接⼝是read-only（只读状态），不能修改其变量值。 即不能修改其变量的指针指向，但可以改变变量内部指针指向，可以对commonJS对重新赋值（改变指针指向），但是对ES6 Module赋值会编译报错。 

**共同点： **

- CommonJS和ES6 Module都可以对引⼊的对象进⾏赋值，即对对象内部属性的值进⾏改变。

### 21. use strict是什么意思?使用它区别是什么

use strict 是一种 ECMAscript5 添加的（严格模式）运行模式，这种模式使得 Javascript 在更严格的条件下运行。设立严格模式的目的如下：

- 消除 Javascript 语法的不合理、不严谨之处，减少怪异行为;
- 消除代码运行的不安全之处，保证代码运行的安全；
- 提高编译器效率，增加运行速度；
- 为未来新版本的 Javascript 做好铺垫。

区别：

- 禁止使用 with 语句。
- 禁止 this 关键字指向全局对象。
- 对象不能有重名的属性

### 23. 强类型语言和弱类型语言的区别

- **强类型语言**：强类型语言也称为强类型定义语言，是一种总是强制类型定义的语言，要求变量的使用要严格符合定义，所有变量都必须先定义后使用。Java和C++等语言都是强制类型定义的，也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，那么它就永远是这个数据类型了。例如你有一个整数，如果不显式地进行转换，你不能将其视为一个字符串。
- **弱类型语言**：弱类型语言也称为弱类型定义语言，与强类型定义相反。JavaScript语言就属于弱类型语言。简单理解就是一种变量类型可以被忽略的语言。比如JavaScript是弱类型定义的，在JavaScript中就可以将字符串'12'和整数3进行连接得到字符串'123'，在相加的时候会进行强制类型转换。

两者对比：强类型语言在速度上可能略逊色于弱类型语言，但是强类型语言带来的严谨性可以有效地帮助避免许多错误。

### 24. 解释性语言和编译型语言的区品

（1）解释型语言

使用专门的解释器对源程序逐行解释成特定平台的机器码并立即执行。是代码在执行时才被解释器一行行动态翻译和执行，而不是在执行之前就完成翻译。解释型语言不需要事先编译，其直接将源代码解释成机器码并立即执行，所以只要某一平台提供了相应的解释器即可运行该程序。其特点总结如下

- 解释型语言每次运行都需要将源代码解释称机器码并执行，效率较低；
- 只要平台提供相应的解释器，就可以运行源代码，所以可以方便源程序移植；
- JavaScript、Python等属于解释型语言。

（2）编译型语言

使用专门的编译器，针对特定的平台，将高级语言源代码一次性的编译成可被该平台硬件执行的机器码，并包装成该平台所能识别的可执行性程序的格式。在编译型语言写的程序执行之前，需要一个专门的编译过程，把源代码编译成机器语言的文件，如exe格式的文件，以后要再运行时，直接使用编译结果即可，如直接运行exe文件。因为只需编译一次，以后运行时不需要编译，所以编译型语言执行效率高。其特点总结如下：

- 一次性的编译成平台相关的机器语言文件，运行时脱离开发环境，运行效率高；
- 与特定平台相关，一般无法移植到其他平台；
- C、C++等属于编译型语言。

**两者主要区别在于：**前者源程序编译后即可在该平台运行，后者是在运行期间才编译。所以前者运行速度快，后者跨平台性好。

### 25. for..in和for.. .of的区别 forin forof

for…of 是ES6新增的遍历方式，允许遍历一个含有iterator接口的数据结构（数组、对象等）并且返回各项的值，和ES3中的for…in的区别如下 

for…of 遍历获取的是对象的键值，for…in 获取的是对象的键名； 

for… in 会遍历对象的整个原型链，性能非常差不推荐使用，而 for … of 只遍历当前对象不会遍历原型链； 

对于数组的遍历，for…in 会返回数组中所有可枚举的属性(包括原型链上可枚举的属性)，for…of 只返回数组的下标对应的属性值； 

总结：==for...in 循环主要是为了遍历对象而生，不适用于遍历数组；for...of 循环可以用来遍历数组、类数组对象，字符串、Set、Map 以及 Generator 对象。==

### 26. 如何使用for.. .of遍历对象

for…of是作为ES6新增的遍历方式，允许遍历一个含有iterator接口的数据结构（数组、对象等）并且返回各项的值，普通的对象用for..of遍历是会报错的。

如果需要遍历的对象是类数组对象，用Array.from转成数组即可。

```js
var obj = {
  0: "one",
  1: "two",
  length: 2
};

obj = Array.from(obj);

for (var k of obj) {
  console.log(k);
}
```

```js
//方法一：
var obj = {
  a: 1,
  b: 2,
  c: 3
};

obj[Symbol.iterator] = function () {
  var keys = Object.keys(this);
  var count = 0;
  return {
    next() {
      if (count < keys.length) {
        return { value: obj[keys[count++]], done: false };
      } else {
        return { value: undefined, done: true };
      }
    }
  };
};

for (var k of obj) {
  console.log(k);
}

// 方法二
var obj = {
  a: 1,
  b: 2,
  c: 3
};

obj[Symbol.iterator] = function* () {
  var keys = Object.keys(obj);
  for (var k of keys) {
    yield [k, obj[k]];
  }
};

for (var [k, v] of obj) {
  console.log(k, v);
}
```

### 33. 如何遍历一个对象

1. for in
2. object.keys()
3. object.entries()

### 32. JS 如何检测到对象中有循环引用

```js
function cycle(obj, parent) {
  //表示调用的父级数组
  var parentArr = parent || [obj];
  for (var i in obj) {
    if (typeof obj[i] === "object") {
      //判断是否有循环引用
      parentArr.forEach((pObj) => {
        if (pObj === obj[i]) {
          obj[i] = "[cycle]";
        }
      });
      cycle(obj[i], [...parentArr, obj[i]]);
    }
  }
  return obj;
}
```

### 22. ==如何判断一个对象是否属于某个类?==

- 第一种方式，使用 instanceof 运算符来判断构造函数的 prototype 属性是否出现在对象的原型链中的任何位置。
- 第二种方式，通过对象的 constructor 属性来判断，对象的 constructor 属性指向该对象的构造函数，但是这种方式不是很安全，因为 constructor 属性可以被改写。
- 第三种方式，如果需要判断的是某个内置的引用类型的话，可以使用 Object.prototype.toString() 方法来打印对象的[[Class]] 属性来进行判断。

### 30. 什么是纯函数

[What Is a Pure Function in JavaScript?](https://www.freecodecamp.org/news/what-is-a-pure-function-in-javascript-acb887375dfe/)

[純粹的好，Pure Function 知道](https://medium.com/frochu/%E7%B4%94%E7%B2%B9%E7%9A%84%E5%A5%BD-pure-function-%E7%9F%A5%E9%81%93-574d5c0d7819)

[4. 你对函数式编程的理解？优缺点？](# 4. 你对函数式编程的理解？优缺点？)

redux中的reducer就是纯函数

1. 输出仅由输入决定，每一个固定的输入总是返回相同的输出
2. 不产生副作用

```js
// impure function
let intercept = 2;
function math(x) {
  return 3 * x + intercept;
}
const result = math(4); // 14

// pure function, 这个有点像柯里化
function math(itr) {
  return function (x) {
    return 3 * x + itr;
  };
}
const result = math(2)(4); // 14
```

### 31. Number 中最大数、最大安全整数、EPSILON 都是多少，原理是什么
### 34. 什么是 TypedArray

[ArrayBuffer，二进制数组](https://zh.javascript.info/arraybuffer-binary-arrays)

### 35. js 中什么是可选链操作符，如何访问数组

[可选链操作符 - MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

[Optional chaining (?.)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

`?.` 操作符，可以嵌套获取对象的属性值。通过获取对象属性获得的值可能是 undefined 或 null 时，可选链操作符提供了一种方法来简化被连接对象的值访问。

```js
const o = {};

// 添加可选链之前
o && o.a && o.a.b && o.a.b.c && o.a.b.c.d;

// 添加可选链之后
o?.a?.b?.c?.d;

const obj = { a: [1, 2], b() {} };
// 访问数组
obj?.a?.[0];
//使用方法
obj?.b?.();
```

### 36. eventLoop事件循环

`JavaScript`是一门单线程的语言，意味着同一时间内只能做一件事，但是这并不意味着单线程就是阻塞，而实现单线程非阻塞的方法就是事件循环

JavaScript 中的事件循环是一个持续运行的过程，它不断监听call stack（调用栈）。它的主要功能是检查调用栈是否为空。如果调用栈为空，事件循环继续执行任务队列中等待的所有回调。在任务队列中，任务大致分为两类，即微任务和宏任务

宏任务：setTimeout、setInterval、DOM事件、AJAX请求

微任务：Promise, async/await

![](https://miro.medium.com/max/4800/1*_0CnS0bHNX7HMBLri3gNng.gif)

### 37. 对闭包的理解

闭包是一个函数, 其可以记住并访问外部变量。

闭包是指有权访问另一个函数作用域中变量的函数，创建闭包的最常见的方式就是在一个函数内创建另一个函数，创建的函数可以访问到当前函数的局部变量。

```js
function init() {
    var name = "Mozilla"; // name 是一个被 init 创建的局部变量
    function displayName() { // displayName() 是内部函数，一个闭包
        alert(name); // 使用了父函数中声明的变量
    }
    displayName();
}
init();
```

在函数被创建时, 函数的隐藏属性 [[Environment]] 会记住函数被创建时的位置, 即当时的词法环境 Lexical Environment这样, 无论在哪里调用函数, 都会去到 [[Environment]] 所引用的词法环境，当查找变量时, 先在词法环境内部查找, 当没有找到局部变量时, 前往当前词法环境所记录的外部词法环境查找。

**使用场景**

==封装私有变量和处理回调函数==

==例如计数器、延迟调用、回调等闭包的应用，其核心思想还是创建私有变量和延长变量的生命周期==

- 创建私有变量
- 延长变量的生命周期

从作用域的角度理解，每创建一个函数会创建一个作用域，闭包里面的函数没有要释放，但是在外层却返回了本函数，导致变量不能被释放而留存下来，应用就是对于有存储变量的需求可以用

1. 柯里化函数：目的在于避免频繁调用具有相同参数函数的同时，又能够轻松的重用

2. 使用闭包模拟私有方法：在`JavaScript`中，没有支持声明私有变量，但我们可以使用闭包来模拟私有方法

   通过使用闭包来定义公共函数，并令其可以访问私有函数和变量，这种方式也叫模块方式

   两个计数器 `Counter1` 和 `Counter2` 是维护它们各自的独立性的，每次调用其中一个计数器时，通过改变这个变量的值，会改变这个闭包的词法环境，不会影响另一个闭包中的变量

3. 创建私有变量：闭包的第一个用途是使我们在函数外部能够访问到函数内部的变量。通过使用闭包，可以通过在外部调用闭包函数，从而在外部访问到函数内部的变量，可以使用这种方法来创建私有变量

4. 闭包的另一个用途是使已经运行结束的函数上下文中的变量对象继续留在内存中，因为闭包函数保留了这个变量对象的引用，所以这个变量对象不会被回收。

**闭包注意事项**

   **缺点：**

   - 常驻内存，增加内存使用量。
   - 使用不当会很容易造成内存泄露。

如果不是某些特定任务需要使用闭包，在其它函数中创建函数是不明智的，因为闭包在处理速度和内存消耗方面对脚本性能具有负面影响

在创建新的对象或者类时，方法通常应该关联于对象的原型，而不是定义到对象的构造器中。原因在于每个对象的创建，方法都会被重新赋值。

我们知道[闭包](https://so.csdn.net/so/search?q=闭包&spm=1001.2101.3001.7020)延展了局部变量的生命周期，使得外部操作局部变量成为可能，一般来讲函数在调用执行后函数就会被释放，但如果函数中产生了闭包，就会导致函数执行完毕后，函数内部的局部变量没有被释放，使得占用内存时间会变长，容易造成==内存泄漏==。

**解决办法**

1. 能不用闭包就不用
2. 及时释放

### 38. 对作用域、作用域链的理解

#### **作用域**

**作用域：函数和变量能被访问的区域，分有全局作用域、函数作用域、块级作用域。**

- 全局作用域：任何不在函数中或是大括号中声明的变量，都是在全局作用域下，全局作用域下声明的变量可以在程序的任意位置访问
- 函数作用域：函数作用域也叫局部作用域，如果一个变量是在函数内部声明的它就在一个函数作用域下面。这些变量只能在函数内部访问，不能在函数以外去访问
- 块级作用域：ES6引入了`let`和`const`关键字,和`var`关键字不同，在大括号中使用`let`和`const`声明的变量存在于块级作用域中。在大括号之外不能访问这些变量

#### **作用域链**

当在`Javascript`中使用一个变量的时候，首先`Javascript`引擎会尝试在当前作用域下去寻找该变量，如果没找到，再到它的上层作用域寻找，以此类推直到找到该变量或是已经到了全局作用域

### 39. 对执行上下文的理解

- 全局执行上下文：只有一个，浏览器中的全局对象就是 `window`对象，`this` 指向这个全局对象
- 函数执行上下文：存在无数个，只有在函数被调用的时候才会被创建，每次调用函数都会创建一个新的执行上下文
- 执行栈，也叫调用栈，具有 LIFO（后进先出）结构，用于存储在代码执行期间创建的所有执行上下文

### 40. call() 和apply()、bind()的区别?

它们的作用一模一样，区别仅在于传入参数的形式的不同。

- apply 接受两个参数，第一个参数指定了函数体内 this 对象的指向，第二个参数为一个带下标的集合，这个集合可以为数组，也可以为类数组，apply 方法把这个集合中的元素作为参数传递给被调用的函数。
- call 传入的参数数量不固定，跟 apply 相同的是，第一个参数也是代表函数体内的 this 指向，从第二个参数开始往后，每个参数被依次传入函数。
- bind与call的参数相同，只不过返回的是函数，需要进行调用。

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h6z37e4p7uj20xc0s2gs9.jpg" alt="image.png" style="zoom:33%;" /><img src="http://tva1.sinaimg.cn/large/6fc56815gy1h6z3dinhgdj215c0ykdsg.jpg" alt="image.png" style="zoom:33%;" />

### 41. 实现call、apply 及bind函数

- [【Q031】js 中如何实现 bind](https://github.com/shfshanyue/Daily-Question/issues/32)
- [【Q032】js 中什么是 softbind，如何实现](https://github.com/shfshanyue/Daily-Question/issues/33)
- [【Q656】JS 中如何实现 call/apply (代码集合)](https://github.com/shfshanyue/Daily-Question/issues/674)

#### 1. call 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 判断传入上下文对象是否存在，如果不存在，则设置为 window 。
- 处理传入的参数，截取第一个参数后的所有参数。
- 将函数作为上下文对象的一个属性。
- 使用上下文对象来调用这个方法，并保存返回结果。
- 删除刚才新增的属性。
- 返回结果。

```js
Function.prototype.myCall = function (context) {
  // 判断调用对象
  if (typeof this !== "function") {
    console.error("type error");
  }
  // 获取参数
  let args = [...arguments].slice(1),
    result = null;
  // 判断 context 是否传入，如果未传入则设置为 window
  context = context || window;
  // 将调用函数设为对象的方法
  context.fn = this;
  // 调用函数
  result = context.fn(...args);
  // 将属性删除
  delete context.fn;
  return result;
};

```

#### 2. apply 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 判断传入上下文对象是否存在，如果不存在，则设置为 window 。
- 将函数作为上下文对象的一个属性。
- 判断参数值是否传入
- 使用上下文对象来调用这个方法，并保存返回结果。
- 删除刚才新增的属性
- 返回结果

```js
Function.prototype.myApply = function (context) {
  // 判断调用对象是否为函数
  if (typeof this !== "function") {
    throw new TypeError("Error");
  }
  let result = null;
  // 判断 context 是否存在，如果未传入则为 window
  context = context || window;
  // 将函数设为对象的方法
  context.fn = this;
  // 调用方法
  if (arguments[1]) {
    result = context.fn(...arguments[1]);
  } else {
    result = context.fn();
  }
  // 将属性删除
  delete context.fn;
  return result;
};

```

#### 3. bind 函数的实现步骤

- 判断调用对象是否为函数，即使是定义在函数的原型上的，但是可能出现使用 call 等方式调用的情况。
- 保存当前函数的引用，获取其余传入参数值。
- 创建一个函数返回
- 函数内部使用 apply 来绑定函数调用，需要判断函数作为构造函数的情况，这个时候需要传入当前函数的 this 给 apply 调用，其余情况都传入指定的上下文对象。

```js
Function.prototype.myBind = function (context) {
  // 判断调用对象是否为函数
  if (typeof this !== "function") {
    throw new TypeError("Error");
  }
  // 获取参数
  var args = [...arguments].slice(1),
    fn = this;
  return function Fn() {
    // 根据调用方式，传入不同绑定值
    return fn.apply(
      this instanceof Fn ? this : context,
      args.concat(...arguments)
    );
  };
};

```

### 42. js 中什么是 softbind，如何实现

bind 函数多次调用会已第一次绑定的 this 为准，softbind以最后一次绑定传入的 this 为准；

```js
Function.prototype.softBind = function (obj, ...rest) {
  const fn = this;
  const bound = function (...args) {
    const o = !this || this === (window || global) ? obj : this;
    return fn.apply(o, [...rest, ...args]);
  };

  bound.prototype = Object.create(fn.prototype);
  return bound;
};

```

## 四、原型与原型链

### 1. 对原型、原型链的理解

**原型**

在JavaScript中是使用构造函数来新建一个对象的，每一个构造函数的内部都有一个 prototype 属性，它的属性值是一个对象，这个对象包含了可以由该构造函数的所有实例共享的属性和方法。在这个对象的内部将包含一个指针，这个指针指向构造函数的 prototype 属性对应的值，在 ES5 中这个指针被称为对象的原型。

**获取原型的方法：**

1.  `__proto__ `属性来访问这个属性，但是最好不要使用这个属性，因为它不是规范中规定的。
2. ES5 中新增了一个 Object.getPrototypeOf() 方法，可以通过这个方法来获取对象的原型。

**原型链（构造函数，原型，实例的关系）**

每个构造函数都有一个原型对象，原型有一个属性指回构造函数，而实例有一个内部指针指向原型。这样就在实例和原型之间构造了一条原型链。

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7s351qy4lj30wq0ksgo3.jpg" alt="image.png" style="zoom: 50%;" /><img src="http://tva1.sinaimg.cn/large/005NUwygly1h8aogs0sksj30h60lpgqm.jpg" alt="image.png" style="zoom: 50%;" />

### 2. 原型修改、重写

```js
function Person(name) {
  this.name = name;
}
// 修改原型
Person.prototype.getName = function () {};
var p = new Person("hello");
console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // true
// 重写原型
Person.prototype = {
  getName: function () {}
};
var p = new Person("hello");
console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // false
```

可以看到修改原型的时候p的构造函数不是指向Person了，因为直接给Person的原型对象直接用对象赋值时，它的构造函数指向的了根构造函数Object，所以这时候`p.constructor === Object` ，而不是`p.constructor === Person`。要想成立，就要用constructor指回来：

```js
Person.prototype = {
  getName: function () {}
};
var p = new Person("hello");
p.constructor = Person;
console.log(p.__proto__ === Person.prototype); // true
console.log(p.__proto__ === p.constructor.prototype); // true
```

### 3. 原型链指向

```js
p.__proto__; // Person.prototype
Person.prototype.__proto__; // Object.prototype
p.__proto__.__proto__; //Object.prototype
p.__proto__.constructor.prototype.__proto__; // Object.prototype
Person.prototype.constructor.prototype.__proto__; // Object.prototype
p1.__proto__.constructor; // Person
Person.prototype.constructor; // Person
```

### 4. 原型链的终点是什么?如何打印出原型链的终点？

由于`Object`是构造函数，原型链终点是`Object.prototype.__proto__`，而`Object.prototype.__proto__ === null // true`，所以，==原型链的终点是`null`。==

原型链上的所有原型都是对象，所有的对象最终都是由`Object`构造的，而`Object.prototype`的下一级是`Object.prototype.__proto__`。

### 5. 如何获得对象非原型链上的属性?

使用`hasOwnProperty()`方法来判断属性是否属于原型链的属性：

```js
function iterate(obj) {
  var res = [];
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) res.push(key + ": " + obj[key]);
  }
  return res;
}
```

### 6. 在 ES6 Class 中，super 的过程中做了什么

派生类的方法可以通过 super 关键字引用它们的原型。这个关键字只能在派生类中使用，而且仅限于类构造函数、实例方法和静态方法内部。在类构造函数中使用super可以调用父类构造函数。

## 七、异步编程 Promise

### 1. 异步编程的实现方式?

JavaScript中的异步机制可以分为以下几种：

- **回调函数**的方式，使用回调函数的方式有一个缺点是，多个回调函数嵌套的时候会造成回调函数地狱，上下两层的回调函数间的代码耦合度太高，不利于代码的可维护。
- **Promise**的方式，使用 Promise 的方式可以将嵌套的回调函数作为链式调用。但是使用这种方法，有时会造成多个 then 的链式调用，可能会造成代码的语义不够明确。
- **generator**的方式，它可以在函数的执行过程中，将函数的执行权转移出去，在函数外部还可以将执行权转移回来。当遇到异步函数执行的时候，将函数执行权转移出去，当异步函数执行完毕时再将执行权给转移回来。因此在 generator 内部对于异步操作的方式，可以以同步的顺序来书写。使用这种方式需要考虑的问题是何时将函数的控制权转移回来，因此需要有一个自动执行 generator 的机制，比如说 co 模块等方式来实现 generator 的自动执行。
- **async 函数**的方式，async 函数是 generator 和 promise 实现的一个自动执行的语法糖，它内部自带执行器，当函数内部执行到一个 await 语句的时候，如果语句返回一个 promise 对象，那么函数将会等待 promise 对象的状态变为 resolve 后再继续向下执行。因此可以将异步逻辑，转化为同步的顺序来书写，并且这个函数可以自动执行。

### 2. setTimeout、Promise、 Async/Await的区别

### 3. 如何实现一个简单的 Promise

[如何实现一个简单的 Promise](https://github.com/shfshanyue/Daily-Question/issues/23)

```js
class myPromise {
  static PENDING = "pending";
  static FULFILLED = "fulfilled";
  static REJECTED = "rejected";

  static resolve(value) {
    if (value && value.then) {
      return value;
    }
    return new myPromise((resolve) => resolve(value));
  }

  static reject(value) {
    return new myPromise((_, reject) => reject(value));
  }

  constructor(fn) {
    this.status = myPromise.PENDING;
    this.result = null;

    this.resFns = [];
    this.rejFns = [];

    const resolve = (value) => {
      if (this.status === myPromise.PENDING) {
        setTimeout(() => {
          this.status = myPromise.FULFILLED;
          this.result = value;
          this.resFns.forEach(({ fn, resolve, reject }) => resolve(fn(value)));
        });
      }
    };

    const reject = (reason) => {
      if (this.status === myPromise.PENDING) {
        setTimeout(() => {
          this.status = myPromise.REJECTED;
          this.result = reason;
          this.rejFns.forEach(({ fn, resolve, reject }) => reject(fn(reason)));
        });
      }
    };

    try {
      fn(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  then(resFn, rejFn) {
    resFn = typeof resFn === "function" ? resFn : (value) => value;
    rejFn = typeof rejFn === "function" ? rejFn : (reason) => reason;

    const _promise = {
      [myPromise.PENDING]: () => {
        return new myPromise((resolve, reject) => {
          this.resFns.push({ fn: resFn, resolve, reject });
          this.rejFns.push({ fn: rejFn, resolve, reject });
        });
      },
      [myPromise.FULFILLED]: () => myPromise.resolve(resFn(this.result)),
      [myPromise.REJECTED]: () => myPromise.reject(rejFn(this.result))
    }[this.status];

    return _promise();
  }

  catch(fn) {
    return this.then(undefined, fn);
  }

  finally(cb) {
    return this.then(cb, cb);
  }
}

```

### 3. 对Promise的理解

Promise是异步编程的一种解决方案，它是一个对象，可以获取异步操作的消息，他的出现大大改善了异步编程的困境，避免了地狱回调，它比传统的解决方案回调函数和事件更合理和更强大。

所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。从语法上说，Promise 是一个对象，从它可以获取异步操作的消息。Promise 提供统一的 API，各种异步操作都可以用同样的方法进行处理。

（1）Promise的实例有**三个状态**:

- Pending（进行中）
- Resolved（已完成）
- Rejected（已拒绝）

当把一件事情交给promise时，它的状态就是Pending，任务完成了状态就变成了Resolved、没有完成失败了就变成了Rejected。

（2）Promise的实例有**两个过程**：

- pending -> fulfilled : Resolved（已完成）
- pending -> rejected：Rejected（已拒绝）

注意：一旦从进行状态变成为其他状态就永远不能更改状态了。

**Promise的特点：**

- 对象的状态不受外界影响。promise对象代表一个异步操作，有三种状态，`pending`（进行中）、`fulfilled`（已成功）、`rejected`（已失败）。只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态，这也是promise这个名字的由来——“**承诺**”；
- 一旦状态改变就不会再变，任何时候都可以得到这个结果。promise对象的状态改变，只有两种可能：从`pending`变为`fulfilled`，从`pending`变为`rejected`。这时就称为`resolved`（已定型）。如果改变已经发生了，你再对promise对象添加回调函数，也会立即得到这个结果。这与事件（event）完全不同，事件的特点是：如果你错过了它，再去监听是得不到结果的。

**Promise的缺点：**

- 无法取消Promise，一旦新建它就会立即执行，无法中途取消。
- 如果不设置回调函数，Promise内部抛出的错误，不会反应到外部。
- 当处于pending状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）。

**总结：**

Promise 对象是异步编程的一种解决方案，最早由社区提出。Promise 是一个构造函数，接收一个函数作为参数，返回一个 Promise 实例。一个 Promise 实例有三种状态，分别是pending、resolved 和 rejected，分别代表了进行中、已成功和已失败。实例的状态只能由 pending 转变 resolved 或者rejected 状态，并且状态一经改变，就凝固了，无法再被改变了。

状态的改变是通过 resolve() 和 reject() 函数来实现的，可以在异步操作结束后调用这两个函数改变 Promise 实例的状态，它的原型上定义了一个 then 方法，使用这个 then 方法可以为两个状态的改变注册回调函数。这个回调函数属于微任务，会在本轮事件循环的末尾执行。

**注意：**在构造 `Promise` 的时候，构造函数内部的代码是立即执行的

### 4. Promise的基本用法

Promise有五个常用的方法：then()、catch()、all()、race()、finally。

```js
function testPromise(ready) {
  return new Promise(function (resolve, reject) {
    if (ready) {
      resolve("hello world");
    } else {
      reject("No thanks");
    }
  });
}
// 方法调用
testPromise(true).then(
  function (msg) {
    console.log(msg);
  },
  function (error) {
    console.log(error);
  }
);

```

### 5. Promise解决了什么问题

解决了地狱回调的问题

### 6. Promise. all和Promise.race的区别的使用场景

1. Promise.all

   Promise.all可以将多个Promise实例包装成一个新的Promise实例。同时，成功和失败的返回值是不同的，成功的时候返回的是一个结果数组，而失败的时候则返回最先被reject失败状态的值。

   Promise.all中传入的是数组，返回的也是是数组，并且会将进行映射，传入的promise对象返回的值是按照顺序在数组中排列的，但是注意的是他们执行的顺序并不是按照顺序的，除非可迭代对象为空。

   需要注意，Promise.all获得的成功结果的数组里面的数据顺序和Promise.all接收到的数组顺序是一致的，这样当遇到发送多个请求并根据请求顺序获取和使用数据的场景，就可以使用Promise.all来解决。

2. Promise.race
   顾名思义，Promse.race就是赛跑的意思，意思就是说，Promise.race([p1, p2, p3])里面哪个结果获得的快，就返回那个结果，不管结果本身是成功状态还是失败状态。

   当要做一件事，超过多长时间就不做了，可以用这个方法来解决：

   `Promise.race([promise1,timeOutPromise(5000)]).then(res=>{})`

### 7. 对async/await的理解

async/await其实是Generator 的语法糖，它能实现的效果都能用then链来实现，它是为优化then链而开发出来的。从字面上来看，async是“异步”的简写，await则为等待，所以很好理解async 用于申明一个 function 是异步的，而 await 用于等待一个异步方法执行完成。当然语法上强制规定await只能出现在asnyc函数中。

async 函数返回的是一个 Promise 对象，所以在最外层不能用 await 获取其返回值的情况下，当然应该用原来的方式：then() 链来处理这个 Promise 对象。

```js
async function testAsy() {
  return "hello world";
}
let result = testAsy();
console.log(result);
result.then((v) => {
  console.log(v); // hello world
});

```

### 8. await到底在等啥?

一般来说，都认为 await 是在等待一个 async 函数完成。不过按语法说明，await 等待的是一个表达式，这个表达式的计算结果是 Promise 对象或者其它值（换句话说，就是没有特殊限定）

await 表达式的运算结果取决于它等的是什么。

- 如果它等到的不是一个 Promise 对象，那 await 表达式的运算结果就是它等到的东西。
- 如果它等到的是一个 Promise 对象，await 就忙起来了，它会阻塞后面的代码，等着 Promise 对象 resolve，然后得到 resolve 的值，作为 await 表达式的运算结果。

### 9. async/await的优势

单一的 Promise 链并不能发现 async/await 的优势，但是，如果需要处理由多个 Promise 组成的 then 链的时候，优势就能体现出来了（很有意思，Promise 通过 then 链来解决多层回调的问题，现在又用 async/await 来进一步优化它）。

### 10. async/await对比Promise的优势

- 代码读起来更加同步，Promise虽然摆脱了回调地狱，但是then的链式调⽤也会带来额外的阅读负担 
- Promise传递中间值⾮常麻烦，⽽async/await⼏乎是同步的写法，⾮常优雅 
- 错误处理友好，async/await可以⽤成熟的try/catch，Promise的错误捕获⾮常冗余 
- 调试友好，Promise的调试很差，由于没有代码块，你不能在⼀个返回表达式的箭头函数中设置断点，如果你在⼀个.then代码块中使⽤调试器的步进(step-over)功能，调试器并不会进⼊后续的.then代码块，因为调试器只能跟踪同步代码的每⼀步。

### 11. async/await如何捕获异常
### 12. ==并发与并行的区别?==

- 并发是宏观概念，我分别有任务 A 和任务 B，在一段时间内通过任务间的切换完成了这两个任务，这种情况就可以称之为并发。
- 并行是微观概念，假设 CPU 中存在两个核心，那么我就可以同时完成任务 A、B。同时完成多个任务的情况就可以称之为并行。

### 13. 什么是回调函数？回调函数有什么缺点？如何解决毁掉地狱的问题？

回调地狱的根本问题就是：

1. 嵌套函数存在耦合性，一旦有所改动，就会牵一发而动全身
2. 嵌套函数一多，就很难处理错误
3. 不能使用 `try catch` 捕获错误
4. 不能直接 `return`

### 14. setTimeout、setInterval、requestAnimationFrame 各有什么特点？

异步编程当然少不了定时器了，常见的定时器函数有 `setTimeout`、`setInterval`、`requestAnimationFrame`。最常用的是`setTimeout`，很多人认为 `setTimeout` 是延时多久，那就应该是多久后执行。

其实这个观点是错误的，因为 JS 是单线程执行的，如果前面的代码影响了性能，就会导致 `setTimeout` 不会按期执行。当然了，可以通过代码去修正 `setTimeout`，从而使定时器相对准确。

```js
let period = 60 * 1000 * 60 * 2;
let startTime = new Date().getTime();
let count = 0;
let end = new Date().getTime() + period;
let interval = 1000;
let currentInterval = interval;
function loop() {
  count++;
  // 代码执行所消耗的时间
  let offset = new Date().getTime() - (startTime + count * interval);
  let diff = end - new Date().getTime();
  let h = Math.floor(diff / (60 * 1000 * 60));
  let hdiff = diff % (60 * 1000 * 60);
  let m = Math.floor(hdiff / (60 * 1000));
  let mdiff = hdiff % (60 * 1000);
  let s = mdiff / 1000;
  let sCeil = Math.ceil(s);
  let sFloor = Math.floor(s);
  // 得到下一次循环所消耗的时间
  currentInterval = interval - offset;
  console.log(
    "时：" + h,
    "分：" + m,
    "毫秒：" + s,
    "秒向上取整：" + sCeil,
    "代码执行时间：" + offset,
    "下次循环间隔" + currentInterval
  );
  setTimeout(loop, currentInterval);
}
setTimeout(loop, currentInterval);

```

如果有循环定时器的需求，其实完全可以通过 `requestAnimationFrame` 来实现：

```js
function setInterval(callback, interval) {
  let timer;
  const now = Date.now;
  let startTime = now();
  let endTime = startTime;
  const loop = () => {
    timer = window.requestAnimationFrame(loop);
    endTime = now();
    if (endTime - startTime >= interval) {
      startTime = endTime = now();
      callback(timer);
    }
  };
  timer = window.requestAnimationFrame(loop);
  
  return timer;
}

let a = 0;

setInterval((timer) => {
  console.log(1);
  a++;
  if (a === 3) cancelAnimationFrame(timer);
}, 1000);

```

首先 `requestAnimationFrame` 自带函数节流功能，基本可以保证在 16.6 毫秒内只执行一次（不掉帧的情况下），并且该函数的延时效果是精确的，没有其他定时器时间不准的问题，当然你也可以通过该函数来实现 `setTimeout`。

### 15. 如何实现 promise.map，限制 promise 并发数

实现一个 promise.map，进行并发数控制，有以下测试用例

```js
pMap([1, 2, 3, 4, 5], (x) => Promise.resolve(x + 1));

pMap([Promise.resolve(1), Promise.resolve(2)], (x) => x + 1);

// 注意输出时间控制
pMap([1, 1, 1, 1, 1, 1, 1, 1], (x) => sleep(1000), { concurrency: 2 });
```

```js
function pMap(list, mapper, concurrency = Infinity) {
  // list 为 Iterator，先转化为 Array
  list = Array.from(list);
  return new Promise((resolve, reject) => {
    let currentIndex = 0;
    let result = [];
    let resolveCount = 0;
    let len = list.length;
    function next() {
      const index = currentIndex;
      currentIndex++;
      Promise.resolve(list[index])
        .then((o) => mapper(o, index))
        .then((o) => {
          result[index] = o;
          resolveCount++;
          if (resolveCount === len) {
            resolve(result);
          }
          if (currentIndex < len) {
            next();
          }
        });
    }
    for (let i = 0; i < concurrency && i < len; i++) {
      next();
    }
  });
}

```

### 16. 如何实现一个 async/await

参考 `@bebel/runtime` 的实现代码如下，可在 [asyncToGenerator.js](https://cdn.jsdelivr.net/npm/@babel/runtime@7.13.9/helpers/esm/asyncToGenerator.js)查看源代码

```js
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
  try {
    var info = gen[key](arg);
    var value = info.value;
  } catch (error) {
    reject(error);
    return;
  }

  if (info.done) {
    resolve(value);
  } else {
    Promise.resolve(value).then(_next, _throw);
  }
}

export default function _asyncToGenerator(fn) {
  return function () {
    var self = this,
      args = arguments;
    return new Promise(function (resolve, reject) {
      var gen = fn.apply(self, args);

      function _next(value) {
        asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
      }

      function _throw(err) {
        asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
      }

      _next(undefined);
    });
  };
}

```

### 17. 如何使用 async/await 实现 Promise.all 的效果
### 18. 有没有用过 Promise.allSettled() ，它是干什么的

接收一个可迭代对象，其中每个成员都是`Promise`。在所有给定的`Promise`都已经`fulfilled`或`rejected`后返回一个`Promise`，并带有一个对象数组，每个对象表示对应的`Promise`结果 相较于`Promise.all`，后者会在任何一个`Promise`为`rejected`时立即结束 简单实现。

### 19. fetch 中 crendentials 指什么意思，可以取什么值

·`redentials` 指在使用 `fetch` 发送请求时是否应当发送 `cookie`

- `omit`: 从不发送 `cookie`.
- `same-origin`: 同源时发送 `cookie` (浏览器默认值)
- `include`: 同源与跨域时都发送 `cookie`

### 20. 如何实现 Promise.race

```js
Promise.race = (promiseArray) => {
  return new Promise((resolve, reject) => {
    promiseArray.forEach((item) => {
      Promise.resolve(item).then(
        (val) => {
          resolve(val);
        },
        (reason) => {
          reject(reason);
        }
      );
    });
  });
};
```

### 21. 异步加载 JS 脚本时，async 与 defer 有何区别

> 以下图片取自 whatwg 的规范，可以说是最权威的图文解释了，详细参考[原文](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element)

![async 与 defer 区别](https://html.spec.whatwg.org/images/asyncdefer.svg)

在*正常情况下*，即 `<script>` 没有任何额外属性标记的情况下，有几点共识

1. JS 的脚本分为**加载、解析、执行**几个步骤，简单对应到图中就是 `fetch` (加载) 和 `execution` (解析并执行)
2. **JS 的脚本加载(fetch)且执行(execution)会阻塞 DOM 的渲染**，因此 JS 一般放到最后头

而 `defer` 与 `async` 的区别如下:

- 相同点: **异步加载 (fetch)**
- 不同点:
  - async 加载(fetch)完成后立即执行 (execution)，因此可能会阻塞 DOM 解析；
  - defer 加载(fetch)完成后延迟到 DOM 解析完成后才会执行(execution)**，但会在事件 `DomContentLoaded` 之前

### 22. setTimeout为什么最小只能设置4ms，如何实现一个0ms的setTimeout?

1. [为什么 setTimeout 有最小时延 4ms ?](https://juejin.cn/post/6846687590616137742)
2. [如何实现一个 0ms 的 setTimeout?](https://zhuanlan.zhihu.com/p/379637806)

### 23. return promise 与 return await promise 有何区别

最终返回得到的结果是相同的，但是有些顺序的变化。

```js
async function p1() {
  return 3;
}

async function p2() {
  return Promise.resolve(3);
}

async function p3() {
  return await Promise.resolve(3);
}

// Output: p1、p3、p2
p3().then((o) => console.log(o, "p3"));
p2().then((o) => console.log(o, "p2"));
p1().then((o) => console.log(o, "p1"));
```

### 24. 了解 promiseA+ 规范吗

[原文](https://promisesaplus.com/)

[Promise/A+ 规范](https://tsejx.github.io/javascript-guidebook/standard-built-in-objects/control-abstraction-objects/promise-standard/)

### 25. ajax、 axios、 fetch的区别

**（1）AJAX**

本身虽然简单，但常常会涉及到一些问题：如==CSRF攻击==、==XSS攻击==

Ajax 即“AsynchronousJavascriptAndXML”（异步 JavaScript 和 XML），是指一种创建交互式[网页](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E7%BD%91%E9%A1%B5)应用的网页开发技术。它是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。通过在后台与服务器进行少量数据交换，Ajax 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。传统的网页（不使用 Ajax）如果需要更新内容，必须重载整个网页页面。其缺点如下：

- 本身是针对MVC编程，不符合前端MVVM的浪潮
- 基于原生XHR开发，XHR本身的架构不清晰
- 不符合关注分离（Separation of Concerns）的原则
- 配置和调用方式非常混乱，而且基于事件的异步模型不友好。

**（2）Fetch**

fetch号称是AJAX的替代品，是在ES6出现的，使用了ES6中的promise对象。Fetch是基于promise设计的。Fetch的代码结构比起ajax简单多。==**fetch不是ajax的进一步封装，而是原生js，没有使用XMLHttpRequest对象**。==

fetch的优点：

- 语法简洁，更加语义化
- 基于标准 Promise 实现，支持 async/await
- 更加底层，提供的API丰富（request, response）
- 脱离了XHR，是ES规范里新的实现方式

fetch的缺点：

- fetch只对网络请求报错，对400，500都当做成功的请求，服务器返回 400，500 错误码时并不会 reject，只有网络错误这些导致请求不能完成时，fetch 才会被 reject。
- fetch默认不会带cookie，需要添加配置项：` fetch(url, {credentials: 'include'})`
- fetch不支持abort，不支持超时控制，使用setTimeout及Promise.reject的实现的超时控制并不能阻止请求过程继续在后台运行，造成了流量的浪费
- fetch没有办法原生监测请求的进度，而XHR可以

**（3）Axios**

Axios 是一种基于Promise封装的HTTP客户端，其特点如下：

- 浏览器端发起XMLHttpRequests请求
- node端发起http请求
- 支持Promise API
- 监听请求和返回
- 对请求和返回进行转化
- 取消请求
- 自动转换json数据
- 客户端支持抵御XSRF攻击

### 26. axios封装

https://vue3js.cn/interview/vue/axiosCode.html#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%B8%AA%E7%AE%80%E6%98%93%E7%89%88axios

https://vue3js.cn/interview/vue/axios.html#%E4%B8%80%E3%80%81axios%E6%98%AF%E4%BB%80%E4%B9%88

### 27. ajax

即异步的`JavaScript` 和`XML`，是一种创建交互式网页应用的网页开发技术，可以在不重新加载整个网页的情况下，与服务器交换数据，并且更新部分网页

`Ajax`的原理简单来说通过`XmlHttpRequest`对象来向服务器发异步请求，从服务器获得数据，然后用`JavaScript`来操作`DOM`而更新页面

```js
//封装一个ajax请求
function ajax(options) {
    //创建XMLHttpRequest对象
    const xhr = new XMLHttpRequest()


    //初始化参数的内容
    options = options || {}
    options.type = (options.type || 'GET').toUpperCase()
    options.dataType = options.dataType || 'json'
    const params = options.data

    //发送请求
    if (options.type === 'GET') {
        xhr.open('GET', options.url + '?' + params, true)
        xhr.send(null)
    } else if (options.type === 'POST') {
        xhr.open('POST', options.url, true)
        xhr.send(params)

    //接收请求
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            let status = xhr.status
            if (status >= 200 && status < 300) {
                options.success && options.success(xhr.responseText, xhr.responseXML)
            } else {
                options.fail && options.fail(status)
            }
        }
    }
}
```

### 28. JSONP 的原理是什么, 如何实现

**以下是Jsonp解决跨域：**

根据浏览器同源策略，所谓同源就是协议、主机、端口号都相同时成为同源。a 域的js不能直接访问 b域名的信息，但是script 标签的src属性可以跨域引用文件，jsonp是请求之后后台包装好一段json，并且把数据放在一个callback函数，返回一个js文件，动态引入这个文件，下载完成js之后，会去调用这个callback通过这样访问数据。

为了实现跨域请求，可以通过script标签实现跨域请求，然后再服务端输出JSON数据并执行回调callback函数，从而解决跨域数据请求。**jsonp的核心则是动态添加`<script>`标签来调用服务器提供的js脚本。**

首先在客户端注册一个callback，然后把callback的名字传给服务器。此时，服务器先生成json数据，然后以javascript语法的方式，生成function，function名字就是传递上来I带参数jsonp。最后将json数据直接以入参的方式，放置function中，这样就生成js语法的文档，返回给客户端。客户端浏览器，解析script标签，并执行返回javascript文档，此时数据作为参数，传入了客户端预先定义好的callback函数里。简单的说，就是利用script标签没有跨域限制的“漏洞”来达到与第三方通讯的目的。

总结一下，json 是一种数据格式，jsonp 是一种数据调用的方式，带callback的json就是jsonp。

**缺点：这种方式只支持get方式。**

### 29. 什么是跨域

==违背同源策略就是跨域==

==同源：协议、域名、端口号必须完全相同。不来自同一个服务则是不同源。==

a.com 向 b.com发请求则是域名不同

### 30. Postman为什么不会跨域

跨域这个情况只会出现在浏览器页面里，因为实际上是浏览器由于安全原因限制了这些请求的访问。在postman里面，实际上每发出一个请求，都是在独立请求一个资源，而不是在一个网站返回的页面里，再去请求另外一个网站/端口的资源。自然也就不会造成跨域了。

> Postman doesn't care about SOP, it's a dev tool not a browser

[`CORS`](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) (Cross-Origin Resource Sharing) and `SOP` (Same-Origin Policy) are server-side configurations that **clients decide to enforce or not**.

Related to clients

- Most **Browsers** *do enforce* it to prevent issues related to [`CSRF`](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attack.
- Most **Development tools** *don't care* about it.

跨域是指的当前资源访问其他资源时发起的http请求由于安全原因（由于同源策略，域名、协议。端口中只要有一个不同就不同源），浏览器限制了这些请求的正常访问，特别需要注意的是这些发生在浏览器中。

### 31. 如何解决跨域

#### 1. JSONP

1. JSONP是什么

   JSONP (JSON with Padding)

   本质和ajax没有任何关系,本质是html的非同源策略和函数的传参。动态创建script标签，在本地准备全局函数，用来接收引过来的调用传的值，是一个非官方的跨域解决方案，~~纯粹凭借程序员的聪明才智开发出来~~，==只支持get请求==

2. JSONP 怎么工作的？

   在网页有一些标签天生具有跨域能力，比如：img, link, iframe, script

   JSONP就是利用**`script`**标签的跨域能力来发送请求的

3. JSONP的使用

   - 动态的创建一个script标签

   ```
   var script = document.createElement("script");
   ```

   - 设置script的src，设置回调函数

   ```js
   script.src = "http://locallhost:3000/textAJAX?callback=abc"
   ```

#### 2. CORS

1. CORS是什么？

   CORS (Cross-Origin Resource Sharing), 跨域资源共享。CORS 是==官方==的跨域解决方案，它的特点是不需要在客户端做任何特殊的操作，完全**在服务器中进行处理**，支持 get 和 post 等多种请求。跨域资源共享标准新增了一组 HTTP首部字段（响应头），允许服务器声明哪些源站通过浏览器有权限访问哪些资源。

2. CORS怎么工作的？

   CORS 是通过设置一个响应头来告诉浏览器，该请求允许跨域，浏览器收到该响应以后就会对响应放行。

3. CORS 的使用

   主要是服务端的设置

   ```js
   app.all("/cors-server", (request, response) => {
     //设置响应头
     response.setHeader("Access-Control-Allow-Origin", "*");
     response.setHeader("Access-Control-Allow-Headers", "*");
     response.setHeader("Access-Control-Allow-Method", "*");
     // response.setHeader("Access-Control-Allow-Origin", "http://127.0.0.1:5500");
   
     response.send("hello CORS");
   });
   ```

   ps: `Access-Control-Allow-Origin` 设置为`*`其实意义不大，可以说是形同虚设，实际应用中，上线前我们会将Access-Control-Allow-Origin 值设为我们目标host

#### 3. Proxy

代理（Proxy）也称网络代理，是一种特殊的网络服务，允许一个（一般为客户端）通过这个服务与另一个网络终端（一般为服务器）进行非直接的连接。一些网关、路由器等网络设备具备网络代理功能。一般认为代理服务有利于保障网络终端的隐私或安全，防止攻击。

##### 方案一:通过vue-cli脚手架工具搭建项目, 通过webpack为我们起一个本地服务器作为请求的代理对象

如果是通过vue-cli脚手架工具搭建项目，我们可以通过webpack为我们起一个本地服务器作为请求的代理对象

通过该服务器转发请求至目标服务器，得到结果再转发给前端，但是最终发布上线时如果web应用和接口服务器不在一起仍会跨域

在vue.config.js文件，新增以下代码

```js
amodule.exports = {
  devServer: {
    host: "127.0.0.1",
    port: 8084,
    open: true, // vue项目启动时自动打开浏览器
    proxy: {
      "/api": {
        // '/api'是代理标识，用于告诉node，url前面是/api的就是使用代理的
        target: "http://xxx.xxx.xx.xx:8080", //目标地址，一般是指后台服务器地址
        changeOrigin: true, //是否跨域
        pathRewrite: {
          // pathRewrite 的作用是把实际Request Url中的'/api'用""代替
          "^/api": ""
        }
      }
    }
  }
};

```

通过`axios`发送请求中，配置请求的根路径

```js
axios.defaults.baseURL = '/api'
```

##### 方案二:通过服务端实现代理请求转发

此外，还可通过服务端实现代理请求转发

以`express`框架为例

```js
var express = require("express");
const proxy = require("http-proxy-middleware");
const app = express();
app.use(express.static(__dirname + "/"));
app.use(
  "/api",
  proxy({ target: "http://localhost:4000", changeOrigin: false })
);
module.exports = app;
```

##### 方案三: 通过配置`nginx`实现代理

通过配置`nginx`实现代理

```nginx
server {
    listen    80;
    # server_name www.josephxia.com;
    location / {
        root  /var/www/html;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html;
    }
    location /api {
        proxy_pass  http://127.0.0.1:3000;
        proxy_redirect   off;
        proxy_set_header  Host       $host;
        proxy_set_header  X-Real-IP     $remote_addr;
        proxy_set_header  X-Forwarded-For  $proxy_add_x_forwarded_for;
    }
}
```

### 30. 什么是 CSRF 攻击

https://vue3js.cn/interview/JavaScript/security.html#%E4%B8%80%E3%80%81%E6%98%AF%E4%BB%80%E4%B9%88

跨站请求伪造（英语：Cross-site request forgery），也被称为 one-click attack 或者 session riding，通常缩写为 CSRF 或者 XSRF， 是一种挟制用户在当前已登录的 Web 应用程序上执行非本意的操作的攻击方法。跟跨网站脚本（XSS）相比，XSS 利用的是用户对指定网站的信任，CSRF 利用的是网站对用户网页浏览器的信任。

CSRF (Cross-site request forgery)，跨站请求伪造，又称为 `one-click attack`，顾名思义，通过恶意引导用户一次点击劫持 cookie 进行攻击。

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h88e1pdd2xj30ht08y0wi.jpg)

1. 使用 JSON API。当进行 CSRF 攻击时，请求体通过 `<form>` 构建，请求头为 `application/www-form-urlencoded`。它难以发送 JSON 数据被服务器所理解。
2. CSRF Token。生成一个随机的 token，切勿放在 cookie 中，每次请求手动携带该 token 进行校验。
3. SameSite Cookie。设置为 Lax 或者 Strict，禁止发送第三方 Cookie。

4. [理解 CSRF(opens new window)](https://github.com/pillarjs/understanding-csrf/blob/master/README_zh.md)
5. [Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### 31. XSS攻击


Cross-Site Scripting（跨站脚本攻击）简称 XSS，是一种代码注入攻击。攻击者通过在目标网站上注入恶意脚本，使之在用户的浏览器上运行。利用这些恶意脚本，攻击者可获取用户的敏感信息如 Cookie、SessionID 等，进而危害数据安全。

为了和 CSS 区分，这里把攻击的第一个字母改成了 X，于是叫做 XSS。

XSS 的本质是：恶意代码未经过滤，与网站正常的代码混在一起；浏览器无法分辨哪些脚本是可信的，导致恶意脚本被执行。

而由于直接在用户的终端执行，恶意代码能够直接获取用户的信息，或者利用这些信息冒充用户向网站发起攻击者定义的请求。

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h88e3nwdtdj30jf0b3jtj.jpg)

## 八、面向对象

### 1. 对象创建的方式有哪些?
### 2. 对象继承的方式有哪些?

## 九、垃圾回收机制

### 1. 浏览器的垃圾回收机制
### 2. 哪些情况会导致内存泄漏

[JavaScript 中内存泄漏的几种情况](https://vue3js.cn/interview/JavaScript/memory_leak.html#%E4%B8%89%E3%80%81%E5%B8%B8%E8%A7%81%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%E6%83%85%E5%86%B5)

http://www.ruanyifeng.com/blog/2017/04/memory-leak.html
https://zh.wikipedia.org/wiki

1. 意外的全局变量
2. 定时器不及时销毁也常会造成内存泄露
3. 闭包，维持函数内局部变量，使其得不到释放
4. 没有清理对`DOM`元素的引用同样造成内存泄露
5. 包括使用事件监听addEventListener监听的时候，在不监听的情况下使用removeEventListener取消对事件监听

### 3. 举例说明你对尾递归的理解，有哪些应用场景
### 4. WeakMap 与垃圾回收有何关系

## 十、其他

### 1. 说说你对正则表达式的理解？应用场景？
### 2. 说说JavaScript中的事件模型
### 3. ⚡️Javascript本地存储的方式有哪些？区别及应用场景？

#### 区别

关于`cookie`、`sessionStorage`、`localStorage`三者的区别主要如下：

- 存储大小：`cookie`数据大小不能超过`4k`，`sessionStorage`和`localStorage`虽然也有存储大小的限制，但比`cookie`大得多，可以达到5M或更大
- 有效时间：`localStorage`存储持久数据，浏览器关闭后数据不丢失除非主动删除数据； `sessionStorage`数据在当前浏览器窗口关闭后自动删除；`cookie`设置的`cookie`过期时间之前一直有效，即使窗口或浏览器关闭
- 数据与服务器之间的交互方式，`cookie`的数据会自动的传递到服务器，服务器端也可以写`cookie`到客户端； `sessionStorage`和`localStorage`不会自动把数据发给服务器，仅在本地保存

#### 应用场景

- 标记用户与跟踪用户行为的情况，推荐使用`cookie`
- 适合长期保存在本地的数据（令牌），推荐使用`localStorage`
- 敏感账号一次性登录，推荐使用`sessionStorage`
- 存储大量数据的情况、在线文档（富文本编辑器）保存编辑历史的情况，推荐使用`indexedDB`

`javaScript`本地缓存的方法我们主要讲述以下四种：

- cookie
- sessionStorage
- localStorage
- indexedDB

#### a. cookie

`Cookie`，类型为「小型文本文件」，指某些网站为了辨别用户身份而储存在用户本地终端上的数据。是为了解决 `HTTP`无状态导致的问题

作为一段一般不超过 4KB 的小型文本数据，它由一个名称（Name）、一个值（Value）和其它几个用于控制 `cookie`有效期、安全性、使用范围的可选属性组成

但是`cookie`在每次请求中都会被发送，如果不使用 `HTTPS`并对其加密，其保存的信息很容易被窃取，导致安全风险。举个例子，在一些使用 `cookie`保持登录态的网站上，如果 `cookie`被窃取，他人很容易利用你的 `cookie`来假扮成你登录网站

关于`cookie`常用的属性如下：

关于`cookie`常用的属性如下：

```js
document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";
```

- expires 用于设置 Cookie 的过期时间

```js
expires=Wed, 21 Oct 2015 07:28:00 GMT
```

- max-Age 用于设置在 Cookie 失效之前需要经过的秒数（优先级比`Expires`高）

```
max-Age=604800
```

- `;max-age=max-age-in-seconds` (e.g., `60*60*24*365` or 31536000 for a year)
- `;expires=date-in-GMTString-format` If neither `expires` nor `max-age` specified it will expire at the end of session.

- `Domain`指定了 `Cookie` 可以送达的主机名
- `Path`指定了一个 `URL`路径，这个路径必须出现在要请求的资源的路径中才可以发送 `Cookie` 首部

```js
Path=/docs   # /docs/Web/ 下的资源会带 Cookie 首部
```

- 标记为 `Secure`的 `Cookie`只应通过被`HTTPS`协议加密过的请求发送给服务端

通过上述，我们可以看到`cookie`又开始的作用并不是为了缓存而设计出来，只是借用了`cookie`的特性实现缓存

关于`cookie`的使用如下：

```js
document.cookie = '名字=值';
```

关于`cookie`的修改，首先要确定`domain`和`path`属性都是相同的才可以，其中有一个不同得时候都会创建出一个新的`cookie`

```js
Set-Cookie:name=aa; domain=aa.net; path=/  # 服务端设置
document.cookie =name=bb; domain=aa.net; path=/  # 客户端设置
```

最后`cookie`的删除，最常用的方法就是给`cookie`设置一个过期的事件，这样`cookie`过期后会被浏览器删除

#### b. localStorage

`HTML5`新方法，IE8及以上浏览器都兼容

特点

- 生命周期：持久化的本地存储，除非主动删除数据，否则数据是永远不会过期的
- 存储的信息在同一域中是共享的
- 当本页操作（新增、修改、删除）了`localStorage`的时候，本页面不会触发`storage`事件,但是别的页面会触发`storage`事件。
- 大小：5M（跟浏览器厂商有关系）
- `localStorage`本质上是对字符串的读取，如果存储内容多的话会消耗内存空间，会导致页面变卡
- 受同源策略的限制

下面再看看关于`localStorage`的使用

设置

```js
localStorage.setItem('username','cfangxu');
```

获取

```js
localStorage.getItem('username')
```

获取键名

```js
localStorage.key(0) //获取第一个键名
```

删除

```js
localStorage.removeItem('username')
```

一次性清除所有存储

```js
localStorage.clear()
```

`localStorage` 也不是完美的，它有两个缺点：

- 无法像`Cookie`一样设置过期时间
- 只能存入字符串，无法直接存对象

```js
localStorage.setItem('key', {name: 'value'});
console.log(localStorage.getItem('key')); // '[object, Object]'
```

#### c. sessionStorage

`sessionStorage`和 `localStorage`使用方法基本一致，唯一不同的是生命周期，一旦页面（会话）关闭，`sessionStorage` 将会删除数据。

#### d. indexedDB

`indexedDB`是一种低级API，用于客户端存储大量结构化数据(包括, 文件/ blobs)。该API使用索引来实现对该数据的高性能搜索

虽然 `Web Storage`对于存储较少量的数据很有用，但对于存储更大量的结构化数据来说，这种方法不太有用。`IndexedDB`提供了一个解决方案

优点：

- 储存量理论上没有上限
- 所有操作都是异步的，相比 `LocalStorage` 同步操作性能更高，尤其是数据量较大时
- 原生支持储存`JS`的对象
- 是个正经的数据库，意味着数据库能干的事它都能干

缺点：

- 操作非常繁琐
- 本身有一定门槛

关于`indexedDB`的使用基本使用步骤如下：

- 打开数据库并且开始一个事务
- 创建一个 `object store`
- 构建一个请求来执行一些数据库操作，像增加或提取数据等。
- 通过监听正确类型的 `DOM` 事件以等待操作完成。
- 在操作结果上进行一些操作（可以在 `request`对象中找到）

关于使用`indexdb`的使用会比较繁琐，大家可以通过使用`Godb.js`库进行缓存，最大化的降低操作难度

### 4. 你对函数式编程的理解？优缺点？

#### intro

函数式编程是一种"编程范式"（programming paradigm），一种编写程序的方法论

主要的编程范式有三种：命令式编程，声明式编程和函数式编程

相比命令式编程，函数式编程更加强调程序执行的结果而非执行的过程，倡导利用若干简单的执行单元让计算结果不断渐进，逐层推导复杂的运算，而非设计一个复杂的执行过程。

简单来讲，就是要把过程逻辑写成函数，定义好输入参数，只关心它的输出结果。

```js
// 命令式编程
var array = [0, 1, 2, 3]
for(let i = 0; i < array.length; i++) {
    array[i] = Math.pow(array[i], 2)
}

// 函数式方式
[0, 1, 2, 3].map(num => Math.pow(num, 2))
```

**优点**

- 更好的管理状态：因为它的宗旨是无状态，或者说更少的状态，能最大化的减少这些未知、优化代码、减少出错情况
- 更简单的复用：固定输入->固定输出，没有其他外部变量影响，并且无副作用。这样代码复用时，完全不需要考虑它的内部实现和外部影响
- 更优雅的组合：往大的说，网页是由各个组件组成的。往小的说，一个函数也可能是由多个小函数组成的。更强的复用性，带来更强大的组合性
- 隐性好处。减少代码量，提高维护性

**缺点**

- 性能：函数式编程相对于指令式编程，性能绝对是一个短板，因为它往往会对一个方法进行过度包装，从而产生上下文切换的性能开销
- 资源占用：在 JS 中为了实现对象状态的不可变，往往会创建新的对象，因此，它对垃圾回收所产生的压力远远超过其他编程方式
- 递归陷阱：在函数式编程中，为了实现迭代，通常会采用递归操作

#### a. 纯函数

函数式编程旨在尽可能的提高代码的无状态性和不变性。要做到这一点，就要学会使用无副作用的函数，也就是纯函数

纯函数是对给定的输入返还相同输出的函数，并且要求你所有的数据都是不可变的，即纯函数=无状态+数据不可变

特性：

- 函数内部传入指定的值，就会返回确定唯一的值
- 不会造成超出作用域的变化，例如修改全局变量或引用传递的参数

优势：

- 使用纯函数，我们可以产生可测试的代码

```js
test('double(2) 等于 4', () => {
  expect(double(2)).toBe(4);
})
```

- 不依赖外部环境计算，不会产生副作用，提高函数的复用性
- 可读性更强 ，函数不管是否是纯函数 都会有一个语义化的名称，更便于阅读
- 可以组装成复杂任务的可能性。符合模块化概念及单一职责原则

#### b. 高阶函数

高级函数，就是以函数作为输入或者输出的函数被称为高阶函数。

```js
// 通过高阶函数抽象过程，注重结果。
const forEach = function (arr, fn) {
  for (let i = 0; i < arr.length; i++) {
    fn(arr[i]);
  }
};

let arr = [1, 2, 3];

forEach(arr, (item) => {
  console.log(item);
});
```

```js
// 高阶函数存在缓存的特性，主要是利用闭包作用
const once = (fn) => {
  let done = false;
  return function () {
    if (!done) {
      fn.apply(this, fn);
    } else {
      console.log("该函数已经执行");
    }
    done = true;
  };
};

```

#### c. 柯里化

柯里化是把一个多参数函数转化成一个嵌套的一元函数的过程

```js
// 二元函数
let fn = (x,y)=>x+y;

const curry = function (fn) {
  return function (x) {
    return function (y) {
      return fn(x, y);
    };
  };
};
let myfn = curry(fn);
console.log(myfn(1)(2));

// 多参数柯里化；
const curry = function (fn) {
  return function curriedFn(...args) {
    if (args.length < fn.length) {
      return function () {
        return curriedFn(...args.concat([...arguments]));
      };
    }
    return fn(...args);
  };
};
const fn = (x, y, z, a) => x + y + z + a;
const myfn = curry(fn);
console.log(myfn(1)(2)(3)(1));
```

关于柯里化函数的意义如下：

- 让纯函数更纯，每次接受一个参数，松散解耦
- 惰性执行

#### d. 组合函数与管道函数

**组合函数与管道函数的意义在于：可以把很多小函数组合起来完成更复杂的逻辑**

**组合函数，目的是将多个函数组合成一个函数**

**而管道函数，执行顺序是从左到右执行的**

```js
function afn(a) {
  return a * 2;
}

function bfn(b) {
  return b * 3;
}

const compose = (a, b) => (c) => a(b(c));

let myfn = compose(afn, bfn);
console.log(myfn(2));
// 可以看到compose实现一个简单的功能：形成了一个新的函数，而这个函数就是一条从 bfn -> afn 的流水线
```

```js
// compose执行是从右到左的
const compose = (...fns)=>val=>fns.reverse().reduce((acc,fn)=>fn(acc),val);
```

```js
// 而管道函数，执行顺序是从左到右执行的
const pipe = (...fns)=>val=>fns.reduce((acc,fn)=>fn(acc),val);
```

### 5. ⚡️Javascript中如何实现函数缓存？函数缓存有哪些应用场景？

==实现函数缓存主要依靠闭包、柯里化、高阶函数。==

函数缓存，就是将函数运算过的结果进行缓存，本质上就是用空间（缓存存储）换时间（计算过程），常用于缓存数据计算结果和缓存对象。缓存只是一个临时的数据存储，它保存数据，以便将来对该数据的请求能够更快地得到处理

```js
const add = (a,b) => a+b;
const calc = memoize(add); // 函数缓存
calc(10,20); // 30
calc(10,20); // 30 缓存

// 高阶函数缓存
const memoize = function (func, content) {
  let cache = Object.create(null);
  content = content || this;
  return (...key) => {
    if (!cache[key]) {
      cache[key] = func.apply(content, key);
    }
    return cache[key];
  };
};

// 柯里化
var add2 = function (x) {
  //**返回函数**
  return function (y) {
    return x + y;
  };
};
add2(3)(4); //7

// 闭包可以理解成，函数 + 函数体内可访问的变量总和
// add函数本身，以及其内部可访问的变量，即 a = 1，这两个组合在⼀起就形成了闭包
(function () {
  var a = 1;
  function add() {
    const b = 2;
    let sum = b + a;
    console.log(sum); // 3
  }
  add();
})();

```

### 6. 什么是 Iterable 对象，与 Array 有什么区别

实现了 `[Symbol.iterator]` 属性的对象即是 `Iterable` 对象，然后可以使用操作符 `for...of` 进行迭代

https://javascript.info/iterable

### 7. js 如何全部替代一个子串为另一个子串

假设有一个字符串 `hello. hello. hello.` 需要替换为 `AAA`，即把 `hello.` 替换为 `A`

- `str.split('foo').join('bar')`
- `str.replaceAll('foo', 'bar')`，在 `ESNext` 中，目前支持性不好

### 8. 如何判断一个元素是否在可视区域中？

https://vue3js.cn/interview/JavaScript/visible.html#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8as2q72hmj30f60bcq5d.jpg" alt="image.png" style="zoom: 50%;" />

在日常开发中，我们经常需要判断目标元素是否在视窗之内或者和视窗的距离小于一个值（例如 100 px），从而实现一些常用的功能，例如：

- 图片的懒加载
- 列表的无限滚动
- 计算广告元素的曝光情况
- 可点击链接的预加载

判断一个元素是否在可视区域，我们常用的有三种办法：

- offsetTop、scrollTop
- getBoundingClientRect
- Intersection Observer

### 9. ==大文件上传如何做断点续传？==

https://vue3js.cn/interview/JavaScript/continue_to_upload.html#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF

吐了，我不会。🤮

### 10. ==如何实现上拉加载，下拉刷新？==

https://vue3js.cn/interview/JavaScript/pull_up_loading_pull_down_refresh.html#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80

#### 上拉加载

上拉加载的本质是页面触底，或者快要触底时的动作

`scrollTop + clientHeight >= scrollHeight`

```js
let clientHeight = document.documentElement.clientHeight; //浏览器高度
let scrollHeight = document.body.scrollHeight;
let scrollTop = document.documentElement.scrollTop;

let distance = 50; //距离视窗还用50的时候，开始触发；

if (scrollTop + clientHeight >= scrollHeight - distance) {
  console.log("开始加载数据");
}
```

#### 下拉刷新

下拉刷新的本质是页面本身置于顶部时，用户下拉时需要触发的动作

关于下拉刷新的原生实现，主要分成三步：

- 监听原生`touchstart`事件，记录其初始位置的值，`e.touches[0].pageY`；
- 监听原生`touchmove`事件，记录并计算当前滑动的位置值与初始位置值的差值，大于`0`表示向下拉动，并借助CSS3的`translateY`属性使元素跟随手势向下滑动对应的差值，同时也应设置一个允许滑动的最大值；
- 监听原生`touchend`事件，若此时元素滑动达到最大值，则触发`callback`，同时将`translateY`重设为`0`，元素回到初始位置

### 11. ==什么是单点登录？如何实现？==

单点登录（Single Sign On），简称为 SSO，是目前比较流行的企业业务整合的解决方案之一

SSO的定义是在多个应用系统中，用户只需要登录一次就可以访问所有相互信任的应用系统

SSO 一般都需要一个独立的认证中心（passport），子系统的登录均得通过`passport`，子系统本身将不参与登录操作

当一个系统成功登录以后，`passport`将会颁发一个令牌给各个子系统，子系统可以拿着令牌会获取各自的受保护资源，为了减少频繁认证，各个子系统在被`passport`授权以后，会建立一个局部会话，在一定时间内可以无需再次向`passport`发起认证

![img](https://static.vue-js.com/2b9b0e70-8c4b-11eb-85f6-6fac77c0c9b3.png)

上图有四个系统，分别是`Application1`、`Application2`、`Application3`、和`SSO`，当`Application1`、`Application2`、`Application3`需要登录时，将跳到`SSO`系统，`SSO`系统完成登录，其他的应用系统也就随之登录了

淘宝、天猫都属于阿里旗下，当用户登录淘宝后，再打开天猫，系统便自动帮用户登录了天猫，这种现象就属于单点登录

#### a. 同域名下的单点登录

`cookie`的`domain`属性设置为当前域的父域，并且父域的`cookie`会被子域所共享。`path`属性默认为`web`应用的上下文路径

利用 `Cookie` 的这个特点，没错，我们只需要将`Cookie`的`domain`属性设置为父域的域名（主域名），同时将 `Cookie`的`path`属性设置为根路径，将 `Session ID`（或 `Token`）保存到父域中。这样所有的子域应用就都可以访问到这个`Cookie`

不过这要求应用系统的域名需建立在一个共同的主域名之下，如 `tieba.baidu.com` 和 `map.baidu.com`，它们都建立在 `baidu.com`这个主域名之下，那么它们就可以通过这种方式来实现单点登录

#### b. 不同域名下的单点登录(一)

如果是不同域的情况下，`Cookie`是不共享的，这里我们可以部署一个认证中心，用于专门处理登录请求的独立的 `Web`服务

用户统一在认证中心进行登录，登录成功后，认证中心记录用户的登录状态，并将 `token` 写入 `Cookie`（注意这个 `Cookie`是认证中心的，应用系统是访问不到的）

应用系统检查当前请求有没有 `Token`，如果没有，说明用户在当前系统中尚未登录，那么就将页面跳转至认证中心

由于这个操作会将认证中心的 `Cookie` 自动带过去，因此，认证中心能够根据 `Cookie` 知道用户是否已经登录过了

如果认证中心发现用户尚未登录，则返回登录页面，等待用户登录

如果发现用户已经登录过了，就不会让用户再次登录了，而是会跳转回目标 `URL`，并在跳转前生成一个 `Token`，拼接在目标`URL` 的后面，回传给目标应用系统

应用系统拿到 `Token`之后，还需要向认证中心确认下 `Token` 的合法性，防止用户伪造。确认无误后，应用系统记录用户的登录状态，并将 `Token`写入`Cookie`，然后给本次访问放行。（注意这个 `Cookie` 是当前应用系统的）当用户再次访问当前应用系统时，就会自动带上这个 `Token`，应用系统验证 Token 发现用户已登录，于是就不会有认证中心什么事了

此种实现方式相对复杂，支持跨域，扩展性好，是单点登录的标准做法

#### c. 不同域名下的单点登录(二)

可以选择将 `Session ID` （或 `Token` ）保存到浏览器的 `LocalStorage` 中，让前端在每次向后端发送请求时，主动将`LocalStorage`的数据传递给服务端

这些都是由前端来控制的，后端需要做的仅仅是在用户登录成功后，将 `Session ID`（或 `Token`）放在响应体中传递给前端

单点登录完全可以在前端实现。前端拿到 `Session ID`（或 `Token` ）后，除了将它写入自己的 `LocalStorage` 中之外，还可以通过特殊手段将它写入多个其他域下的 `LocalStorage` 中

前端通过 `iframe`+`postMessage()` 方式，将同一份 `Token` 写入到了多个域下的 `LocalStorage` 中，前端每次在向后端发送请求之前，都会主动从 `LocalStorage` 中读取`Token`并在请求中携带，这样就实现了同一份`Token` 被多个域所共享

此种实现方式完全由前端控制，几乎不需要后端参与，同样支持跨域

```js
// 获取 token
var token = result.data.token;

// 动态创建一个不可见的iframe，在iframe中加载一个跨域HTML
var iframe = document.createElement("iframe");
iframe.src = "http://app1.com/localstorage.html";
document.body.append(iframe);
// 使用postMessage()方法将token传递给iframe
setTimeout(function () {
  iframe.contentWindow.postMessage(token, "http://app1.com");
}, 4000);
setTimeout(function () {
  iframe.remove();
}, 6000);

// 在这个iframe所加载的HTML中绑定一个事件监听器，当事件被触发时，把接收到的token数据写入localStorage
window.addEventListener(
  "message",
  function (event) {
    localStorage.setItem("token", event.data);
  },
  false
);
```

### 12. 浏览器的剪切板中如何监听复制事件

在 HTML 元素上

```html
<input oncopy="cb" />
```

在 JS 中获取具体元素

```js
document.querySelector("p").oncopy = cb;
document.oncopy = cb;
```

或者

```js
document.querySelector("p").addEventListener("copy", cb);
document.addEventListener("copy", cb);
```

### 13. 在前端开发中，如何获取浏览器的唯一标识

根据 `canvas` 可以获取浏览器指纹信息

1. 绘制 `canvas`，获取 `base64` 的 dataurl
2. 对 dataurl 这个字符串进行 `md5` 摘要计算，得到指纹信息

若在生产环境使用，可以使用 [fingerprintjs2 (opens new window)](https://github.com/Valve/fingerprintjs2)，根据业务需求，如单设备是否可跨浏览器，以此选择合适的 `component`

### 14. 有没有用 npm 发布过 package，如何发布

1. 注册 npm 账号 https://www.npmjs.com/
2. 本地通过命令行 `npm login` 登陆
3. 进入到项目目录下（与 package.json 同级），在 package.json 中指定发布文件、文件夹

```json
{
  "name": "pkg-xxx",
  "version": "0.0.1",
  "main": "lib/index.js",
  "module": "esm/index.js",
  "typings": "types/index.d.ts",
  "files": [
    "CHANGELOG.md",
    "lib",
    "esm",
    "dist",
    "types",
  ],
  ...
}
```

执行 `npm publish --registry=https://registry.npmjs.org/` 即可发布

### 15. js 代码压缩 minify 的原理是什么

我们知道 `javascript` 代码经压缩 (uglify) 后，可以使体积变得更小，那它代码压缩的原理是什么。如果你来做这么一个功能的话，你会怎么去压缩一段 `js` 代码的体积。

https://github.com/shfshanyue/Daily-Question/issues/138

我不会😂

### 16. 如何在 url 中传递数组

在 URL 中如何传递数组这种复杂的数据，完全**取决于项目中前后端成员关于复杂数据在 URL 中传输的约定**，一般情况下可以使用以下方式来传递数组

```js
a=3&a=4&a=5

a=3,4,5

a[]=3&a[]=4&a[]=5

a[0]=3&a[1]=4&a[2]=5
```

但同样，需要后端开发者写一个 `querystring.parse` 来对指定的格式解析进行支持，同时也有对各种复杂 qs 支持较好的 package，比如：[qs: 据说是对 querystring 复杂对象解析最好的库](https://github.com/ljharb/qs#parsing-arrays)

### 17. 如何实现 compose 函数，进行函数合成

https://github.com/shfshanyue/Daily-Question/issues/182

### 18. 前端中遇到过处理二进制的场景吗
### 19. js 中什么是可选链操作符，如何访问数组

`?.` 操作符，可以嵌套获取对象的属性值。通过获取对象属性获得的值可能是 undefined 或 null 时，可选链操作符提供了一种方法来简化被连接对象的值访问。

```js
const o = {};

// 添加可选链之前
o && o.a && o.a.b && o.a.b.c && o.a.b.c.d;

// 添加可选链之后
o?.a?.b?.c?.d;
```

### 21. 如何裁剪图片 (情景：选择头像)

使用`ctx.arc()`和`ctx.clip()`进行裁剪`ctx.arc(x, y, radius, startAngle, endAngle)`; `ctx.clip()`; `ctx.drawImage(img, x, y, width, height)`

```js
var path = "https://static-zh.wxb.com.cn/customer/form/2020/11/1758696796d.jpg";
function clipImage(path) {
  const canvas = document.createElement("canvas");
  canvas.width = 200;
  canvas.height = 100;
  const ctx = canvas.getContext("2d");
  const img = document.createElement("img");
  img.src = path;
  img.setAttribute("crossOrigin", "Anonymous");
  img.onload = function () {
    ctx.drawImage(this, 0, 0, 200, 100);
    console.log(canvas.toDataURL());
  };
}
clipImage(path);

```

### 22. 有没有遇到 js 捕捉不到异常堆栈信息的情况

# 二、Vue

[一些面试题](https://slbyml.github.io/QA/vue.html#%E7%AE%80%E8%BF%B0vue%E7%9A%84%E5%93%8D%E5%BA%94%E5%BC%8F%E5%8E%9F%E7%90%86)

## 一、Vue基础

### 1. Vue的基本原理

当一个Vue实例创建时，Vue会遍历data中的属性，用 Object.defineProperty（vue3.0使用proxy）将它们转为 getter/setter，并且在内部追踪相关依赖，在属性被访问和修改时通知变化。 每个组件实例都有相应的 watcher 程序实例，它会在组件渲染的过程中把属性记录为依赖，之后当依赖项的setter被调用时，会通知watcher重新计算，从而致使它关联的组件得以更新。

Vue 将遍历此对象所有的 property，并使用 Object.defineProperty 把这些 property 全部转为 getter/setter。

每个组件实例都对应一个 **watcher** 实例，它会在组件渲染的过程中把“接触”过的数据 property 记录为依赖。之后当依赖项的 setter 触发时，会通知 watcher，从而使它关联的组件重新渲染。

```js
var obj = {}
//第一种情况：enumerable设置为false，不能被枚举。
Object.defineProperty(obj,"newKey",{
    value:"hello",
    writable:false,
    enumerable:false
});
```

   ![](https://cdn.nlark.com/yuque/0/2021/png/1500604/1620128979608-f7465ffc-9411-43e3-a6bc-96ab44dd77df.png)

```ini
const p = new Proxy(target, handler);
```

- `target`： 所要拦截的目标对象（可以是任何类型的对象，包括原生数组，函数，甚至另一个代理）
- `handler`：一个对象，定义要拦截的行为

```javascript
const p = new Proxy({}, {
    get(target, propKey) {
        return '哈哈，你被我拦截了';
    }
});

console.log(p.name);
// 哈哈，你被我拦截了
```

### 2. 双向数据绑定的原理

Vue.js 是采用**数据劫持**结合**发布者-订阅者模式**的方式，通过Object.defineProperty()来劫持各个属性的setter，getter，在数据变动时发布消息给订阅者，触发相应的监听回调。

   ![](https://static.vue-js.com/e5369850-3ac9-11eb-85f6-6fac77c0c9b3.png)

   <img src="http://ww1.sinaimg.cn/large/005NUwyggy1gu5l5twqptj61nx1acdsi02.jpg" alt="Draft-29.jpg" style="zoom: 33%;" />

   [Link](https://vue3js.cn/interview/vue/bind.html#%E4%BA%8C%E3%80%81%E5%8F%8C%E5%90%91%E7%BB%91%E5%AE%9A%E7%9A%84%E5%8E%9F%E7%90%86%E6%98%AF%E4%BB%80%E4%B9%88)

Vue.js 是采用**数据劫持**结合**发布者-订阅者模式**的方式，通过Object.defineProperty()来劫持各个属性的setter，getter，在数据变动时发布消息给订阅者，触发相应的监听回调。

  1. `new Vue()`首先执行初始化，对`data`执行响应化处理，这个过程发生`Observe`中
  2. 同时对模板执行编译，找到其中动态绑定的数据，从`data`中获取并初始化视图，这个过程发生在`Compile`中
  3. 同时定义⼀个更新函数和`Watcher`，将来对应数据变化时`Watcher`会调用更新函数
  4. 由于`data`的某个`key`在⼀个视图中可能出现多次，所以每个`key`都需要⼀个管家`Dep`来管理多个`Watcher`
  5. 将来data中数据⼀旦发生变化，会首先找到对应的`Dep`，通知所有`Watcher`执行更新函数

------

Vue.js 是采用**数据劫持**结合**发布者-订阅者模式**的方式，通过Object.defineProperty()来劫持各个属性的setter，getter，在数据变动时发布消息给订阅者，触发相应的监听回调。

1. 需要observe的数据对象进行递归遍历，包括子属性对象的属性，都加上setter和getter这样的话，给这个对象的某个值赋值，就会触发setter，那么就能监听到了数据变化

2. compile解析模板指令，将模板中的变量替换成数据，然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者，一旦数据有变动，收到通知，更新视图

3. Watcher订阅者是Observer和Compile之间通信的桥梁，主要做的事情是: 

   ① 在自身实例化时往属性订阅器(dep)里面添加自己 

   ② 自身必须有一个update()方法 

   ③ 待属性变动dep.notice()通知时，能调用自身的update()方法，并触发Compile中绑定的回调，则功成身退。

4. MVVM(MVVM是Model-View-ViewModel的简写)作为数据绑定的入口，整合Observer、Compile和Watcher三者，通过Observer来监听自己的model数据变化，通过Compile来解析编译模板指令，最终利用Watcher搭起Observer和Compile之间的通信桥梁，达到数据变化 -> 视图更新；视图交互变化(input) -> 数据model变更的双向绑定效果。

### 3. 使用Object.defineProperty()来进行数据劫持有什么缺点

不能修改属性(数组，对象)，无法触发组件的重新渲染。

### 4. vue如何监听对象或者数组某个属性的变化

当在项目中直接设置数组的某一项的值，或者直接设置对象的某个属性值，这个时候，你会发现页面并没有更新。这是因为Object.defineProperty()限制，监听不到变化。

解决方式：

1. `this.$set(你要改变的数组/对象，你要改变的位置/key，你要改成什么value)`

   ```js
   this.$set(this.arr, 0, "OBKoro1"); // 改变数组
   this.$set(this.obj, "c", "OBKoro1"); // 改变对象
   ```

2. 调用以下几个数组的方法

   ```js
   splice()、 push()、pop()、shift()、unshift()、sort()、reverse()
   ```

   vue源码里缓存了array的原型链，然后重写了这几个方法，触发这几个方法的时候会observer数据，意思是使用这些方法不用再进行额外的操作，视图自动进行更新。 推荐使用splice方法会比较好自定义,因为splice可以在数组的任何位置进行删除/添加操作

**vm.$set 的实现原理是：**

- 如果目标是数组，直接使用数组的 splice 方法触发相应式；
- 如果目标是对象，会先判读属性是否存在、对象是否是响应式，最终如果要对属性进行响应式处理，则是通过调用`defineReactive `方法进行响应式处理（ `defineReactive `方法就是 Vue 在初始化对象时，给对象属性采用 `Object.defineProperty` 动态添加 `getter` 和 `setter` 的功能所调用的方法）

### 5. Vue中给data中的对象属性添加一个新属性时会发生什么？如何解决？

$set()方法相当于手动的去把obj.b处理成一个响应式的属性，此时视图也会跟着改变了。

### 6. Vue中给对象添加新属性界面不刷新?

原因是一开始`obj`的`foo`属性被设成了响应式数据，而`bar`是后面新增的属性，并没有通过`Object.defineProperty`设置成响应式数据。

`Vue` 不允许在已经创建的实例上动态添加新的响应式属性，若想实现数据与视图同步更新，可采取下面三种解决方案：

- Vue.set()
- Object.assign()
- $forcecUpdated()

### 6. Vue中封装的数组方法有哪些，其如何实现页面更新

在Vue中，对响应式处理利用的是Object.defineProperty对数据进行拦截，而这个方法并不能监听到数组内部变化，数组长度变化，数组的截取变化等，所以需要对这些操作进行hack，让Vue能监听到其中的变化。

**简单来说就是，重写了数组中的那些原生方法，首先获取到这个数组的`__ob__`，也就是它的Observer对象，如果有新的值，就调用observeArray继续对新的值观察变化（也就是通过`target__proto__ == arrayMethods`来改变了数组实例的型），然后手动调用notify，通知渲染watcher，执行update。**

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h816ehgmzkj30k207k3zu.jpg)

```js
// 缓存数组原型
const arrayProto = Array.prototype;
// 实现 arrayMethods.__proto__ === Array.prototype
export const arrayMethods = Object.create(arrayProto);
// 需要进行功能拓展的方法
const methodsToPatch = [
  "push",
  "pop",
  "shift",
  "unshift",
  "splice",
  "sort",
  "reverse"
];

/**
 * Intercept mutating methods and emit events
 */
methodsToPatch.forEach(function(method) {
  // 缓存原生数组方法
  const original = arrayProto[method];
  def(arrayMethods, method, function mutator(...args) {
    // 执行并缓存原生数组功能
    const result = original.apply(this, args);
    // 响应式处理
    const ob = this.__ob__;
    let inserted;
    switch (method) {
    // push、unshift会新增索引，所以要手动observer
      case "push":
      case "unshift":
        inserted = args;
        break;
      // splice方法，如果传入了第三个参数，也会有索引加入，也要手动observer。
      case "splice":
        inserted = args.slice(2);
        break;
    }
    // 
    if (inserted) ob.observeArray(inserted);// 获取插入的值，并设置响应式监听
    // notify change
    ob.dep.notify();// 通知依赖更新
    // 返回原生数组方法的执行结果
    return result;
  });
});
```

### 7. data为什么是一个函数而不是对象

Vue组件可能存在多个实例，如果使用对象形式定义data，则会导致它们共用一个data对象，那么状态变更将会影响所有组件实例，这是不合理的；采用函数形式定义，在initData时会将其作为工厂函数返回全新data对象，有效规避多实例之间状态污染问题。而在Vue根实例创建过程中则不存在该限制，也是因为根实例只能有一个，不需要担心这种情况。

### 8. Vue data中某一个属性的值发生改变后，视图会==立即==同步执行重新渲染吗。

不会立即同步执行重新渲染。Vue 实现响应式并不是数据发生变化之后 DOM 立即变化，而是按一定的策略进行 DOM 的更新。Vue 在更新 DOM 时是异步执行的。只要侦听到数据变化， Vue 将开启一个队列，并缓冲在同一事件循环中发生的所有数据变更。

如果同一个watcher被多次触发，只会被推入到队列中一次。这种在缓冲时去除重复数据对于避免不必要的计算和 DOM 操作是非常重要的。然后，在下一个的事件循环tick中，Vue 刷新队列并执行实际（已去重的）工作。

### 9. MVVM、MVC、MVP的区别

   Model -> `person{age:18,name:"li"}`

   Controller / viewmodel-> `person.name = 'Homer';person.age = 51;`

   ![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/5/27/16af72cd60c25062~tplv-t2oaga2asx-watermark.awebp)

   ![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/5/27/16af920a988c5f66~tplv-t2oaga2asx-watermark.awebp)

   MVVM模式的优点:

   - 低耦合:View可以独立于Model变化和修改,一个ViewModel可以绑定到不同的View上,当View变化的时候Model可以不变,当Model变化的时候View也可以不变。
   - 可重用性: 可以把一些视图逻辑放在一个ViewModel里面,让很多View重用这段视图逻辑。
   - 独立开发: 开发人员可以专注于业务逻辑和数据的开发,设计人员可以专注于页面的设计。

### 10. MVVM的优缺点?

- 降低代码耦合
- 提高可测试性
- 自动更新DOM
- Bug难调试
- 大型的图形应用程序，viewmodel的构建和维护成本会比较高

**优点: **

- 分离视图（View）和模型（Model），降低代码耦合，提⾼视图或者逻辑的重⽤性: ⽐如视图（View）可以独⽴于Model变化和修改，⼀个ViewModel可以绑定不同的"View"上，当View变化的时候Model不可以不变，当Model变化的时候View也可以不变。你可以把⼀些视图逻辑放在⼀个ViewModel⾥⾯，让很多view重⽤这段视图逻辑 
- 提⾼可测试性: ViewModel的存在可以帮助开发者更好地编写测试代码 
- ⾃动更新dom: 利⽤双向绑定,数据更新后视图⾃动更新,让开发者从繁琐的⼿动dom中解放 

**缺点: **

- Bug很难被调试: 因为使⽤双向绑定的模式，当你看到界⾯异常了，有可能是你View的代码有Bug，也可能是Model的代码有问题。数据绑定使得⼀个位置的Bug被快速传递到别的位置，要定位原始出问题的地⽅就变得不那么容易了。另外，数据绑定的声明是指令式地写在View的模版当中的，这些内容是没办法去打断点debug的 
- ⼀个⼤的模块中model也会很⼤，虽然使⽤⽅便了也很容易保证了数据的⼀致性，当时⻓期持有，不释放内存就造成了花费更多的内存 
- 对于⼤型的图形应⽤程序，视图状态较多，ViewModel的构建和维护的成本都会⽐较⾼。

### 11. Computed和Watch的区别

   - computed 计算属性 : 依赖其它属性值，并且 computed 的值有缓存，只有它依赖的属性值发生改变，下一次获取 computed 的值时才会重新计算 computed 的值。 

   - watch 侦听器 : 更多的是观察的作用，无缓存性，类似于某些数据的监听回调，每当监听的数据变化时都会执行回调进行后续操作。

使用场景：

- 当需要进行数值计算,并且依赖于其它数据时，应该使用 computed，因为可以利用 computed 的缓存特性，避免每次获取值时都要重新计算。 
- 当需要在数据变化时执行异步或开销较大的操作时，应该使用 watch，使用 watch 选项允许执行异步操作 ( 访问一个 API )，限制执行该操作的频率，并在得到最终结果前，设置中间状态。这些都是计算属性无法做到的。

### 12. Computed和Methods的区别

- computed 计算属性 : 依赖其它属性值，并且 computed 的值有缓存，只有它依赖的属性值发生改变，下一次获取 computed 的值时才会重新计算 computed 的值。 
- method 调用总会执行该函数。

### 13. ⚡️slot是什么?有什么作用?原理是什么

插槽slot是子组件的一个模板标签元素，而这一个标签元素是否显示，以及怎么显示是由父组件决定的。slot又分三类，默认插槽，具名插槽和作用域插槽。

- 默认插槽：又名匿名插槽，当slot没有指定name属性值的时候一个默认显示插槽，一个组件内只有有一个匿名插槽。
- 具名插槽：带有具体名字的插槽，也就是带有name属性的slot，一个组件可以出现多个具名插槽。
- 作用域插槽：默认插槽、具名插槽的一个变体，可以是匿名插槽，也可以是具名插槽，该插槽的不同点是在子组件渲染作用域插槽时，可以将子组件内部的数据传递给父组件，让父组件根据子组件的传递过来的数据决定如何渲染该插槽。

实现原理：当子组件vm实例化时，获取到父组件传入的slot标签的内容，存放在`vm.$slot`中，默认插槽为`vm.$slot.default`，具名插槽为`vm.$slot.xxx`，xxx 为插槽名，当组件执行渲染函数时候，遇到slot标签，使用`$slot`中的内容进行替换，此时可以为插槽传递数据，若存在数据，则可称该插槽为作用域插槽。



<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20221110173531986.png" alt="image-20221110173531986" style="zoom:50%;" />

上面是slot-test组件，下面是对slot-test组件的使用 

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h806007cvyj30l80ko423.jpg" alt="image.png" style="zoom:50%;" />

![image-20221110173612085](/Users/chenruo/Library/Application Support/typora-user-images/image-20221110173612085.png)

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8064j0krqj314m0kyzw8.jpg" alt="image.png" style="zoom:50%;" />

### 14. 过滤器的作用，如何实现一个过滤器

根据过滤器的名称，过滤器是用来过滤数据的，在Vue中使用filters来过滤数据，filters不会修改数据，而是过滤数据，改变用户看到的输出（计算属性 computed ，方法 methods 都是通过修改数据来处理数据格式的输出显示）。

使用场景

1. 需要格式化数据的情况，比如需要处理时间、价格等数据格式的输出 / 显示。
2. 比如后端返回一个 年月日的日期字符串，前端需要展示为 多少天前 的数据格式，此时就可以用fliters过滤器来处理数据。

过滤器是一个函数，它会把表达式中的值始终当作函数的第一个参数。过滤器用在插值表达式 {{ }} 和 v-bind 表达式 中，然后放在操作符“ | ”后面进行指示。

例如，在显示金额，给商品价格添加单位：

```vue
<li>商品价格：{{item.price | filterPrice}}</li>

 filters: {
    filterPrice (price) {
      return price ? ('￥' + price) : '--'
    }
  }
```

### 15. ⚡️如何保存页面的当前的状态

既然是要保持页面的状态（其实也就是组件的状态），那么会出现以下两种情况：


- 前组件会被卸载

- 前组件不会被卸载

那么可以按照这两种情况分别得到以下方法：

#### **组件会被卸载：**

##### 1. 将状态存储在LocalStorage / SessionStorage

只需要在组件即将被销毁的生命周期 componentWillUnmount （react）中在 LocalStorage / SessionStorage 中把当前组件的 state 通过 JSON.stringify() 储存下来就可以了。在这里面需要注意的是组件更新状态的时机。

比如从 B 组件跳转到 A 组件的时候，A 组件需要更新自身的状态。但是如果从别的组件跳转到 B 组件的时候，实际上是希望 B 组件重新渲染的，也就是不要从 Storage 中读取信息。所以需要在 Storage 中的状态加入一个 flag 属性，用来控制 A 组件是否读取 Storage 中的状态。

**优点**

- 兼容性好，不需要额外库或工具。
- 简单快捷，基本可以满足大部分需求。

**缺点**

- 状态通过 JSON 方法储存（相当于深拷贝），如果状态中有特殊情况（比如 Date 对象、Regexp 对象等）的时候会得到字符串而不是原来的值。（具体参考用 JSON 深拷贝的缺点）

- 如果 B 组件后退或者下一页跳转并不是前组件，那么 flag 判断会失效，导致从其他页面进入 A 组件页面时 A 组件会重新读取 Storage，会造成很奇怪的现象

##### 2. 路由传值

通过 react-router 的 Link 组件的 prop —— to 可以实现路由间传递参数的效果。

在这里需要用到 state 参数，在 B 组件中通过 history.location.state 就可以拿到 state 值，保存它。返回 A 组件时再次携带 state 达到路由状态保持的效果。

**优点**

- 简单快捷，不会污染 LocalStorage / SessionStorage。
- 可以传递 Date、RegExp 等特殊对象（不用担心 JSON.stringify / parse 的不足）

**缺点**

- 如果 A 组件可以跳转至多个组件，那么在每一个跳转组件内都要写相同的逻辑。

#### **组件不会被卸载：**
##### 单页面渲染

要切换的组件作为子组件全屏渲染，父组件中正常储存页面状态。

**优点**

- 代码量少
- 不需要考虑状态传递过程中的错误

**缺点**

- 增加 A 组件维护成本
- 需要传入额外的 prop 到 B 组件
- 无法利用路由定位页面

除此之外，在Vue中，还可以是用keep-alive来缓存页面，当组件在keep-alive内被切换时组件的**activated、deactivated**这两个生命周期钩子函数会被执行、被包裹在keep-alive中的组件的状态将会被保留。

### 16. 常见的事件修饰符及其作用

1. `.stop`：等同于 JavaScript 中的 event.stopPropagation() ，防止事件冒泡；
2. `.prevent` ：等同于 JavaScript 中的 event.preventDefault() ，防止执行预设的行为（如果事件可取消，则取消该事件，而不停止事件的进一步传播）；
3. `.capture `：与事件冒泡的方向相反，事件捕获由外到内；
4. `.self `：只会触发自己范围内的事件，不包含子元素；
5. `.once `：只会触发一次。

```vue
<div id="app">
  <div class="inner" @click="divHandler">
    <!-- 事件修饰符stop可以阻止事件冒泡-->
    <input type="button" value="你猜点击会不会冒泡" @click.stop="btnHnadler">
  </div>
</div>
```

### 17. `v-if`、 `v-show`、 `v-html` 的原理

1. `v-if`会调用addIfCondition方法，生成vnode的时候会忽略对应节点，render的时候就不会渲染；
2. `v-show`会生成vnode，render的时候也会渲染成真实节点，只是在render过程中会在节点的属性中修改show属性值，也就是常说的display;
3. `v-html`会先移除节点下的所有节点，调用html方法，通过addProp添加innerHTML属性，归根结底还是设置innerHTML为`v-html`的值。

### 18. `v-if`和`v-show`的区别

- **手段**：v-if是动态的向DOM树内添加或者删除DOM元素；v-show是通过设置DOM元素的display样式属性控制显隐；
- **编译过程**：v-if切换有一个局部编译/卸载的过程，切换过程中合适地销毁和重建内部的事件监听和子组件；v-show只是简单的基于css切换；
- **编译条件**：v-if是惰性的，如果初始条件为假，则什么也不做；只有在条件第一次变为真时才开始局部编译; v-show是在任何条件下，无论首次条件是否为真，都被编译，然后被缓存，而且DOM元素保留；
- **性能消耗**：v-if有更高的切换消耗；v-show有更高的初始渲染消耗；
- **使用场景**：v-if适合运营条件不大可能改变；v-show适合频繁切换。

### 19. `v-if`和`v-for`哪个优先级更高? 如果同时出现，应该如何优化？

`v-for`优先于`v-if`被解析，如果同时出现，每次渲染都会**先执行循环再判断条件**，无论如何循环都不可避免，浪费了性能。

永远不要把 `v-if` 和 `v-for` 同时用在同一个元素上，带来性能方面的浪费（每次渲染都会先循环再进行条件判断）

要避免出现这种情况，则在外层嵌套template，在这一层进行v-if判断，然后在内部进行v-for循环。

如果条件出现在循环内部，可通过计算属性提前过滤掉那些不需要显示的项。

### 20. v-model是如何实现的，语法糖实际上是什么

1. 作用在表单元素上: 

   动态绑定了 input 的 value 指向了 messgae 变量，并且在触发 input 事件的时候去动态把 message设置为目标值

   ```vue
   <input v-model="sth" />
   //  等同于
   <input 
       v-bind:value="message" 
       v-on:input="message=$event.target.value"
   >
   //$event 指代当前触发的事件对象;
   //$event.target 指代当前触发的事件对象的dom;
   //$event.target.value 就是当前dom的value值;
   //在@input方法中，value => sth;
   //在:value中,sth => value;
   ```

2. 作用在组件上: 在自定义组件中，

   v-model 默认会利用名为 value 的 prop和名为 input 的事件

   本质是一个父子组件通信的语法糖，通过prop和$.emit实现。因此父组件 v-model 语法糖本质上可以修改为：

   ```vue
   <child :value="message"  @input="function(e){message = e}"></child>
   ```

   ```vue
   // 父组件
   <aa-input v-model="aa"></aa-input>
   // 等价于
   <aa-input v-bind:value="aa" v-on:input="aa=$event.target.value"></aa-input>
   
   // 子组件：
   <input v-bind:value="aa" v-on:input="onmessage"></aa-input>
   
   props:{value:aa,}
   methods:{
       onmessage(e){
           $emit('input',e.target.value)
       }
   }
   ```


### 21. v-model可以被用在自定义组件上吗？如果可以，如何使用？

```vue
<custom-input
  v-bind:value="searchText"
  v-on:input="searchText = $event"
></custom-input>
```

### 22. v-model的实现原理

vue中v-model可以实现数据的双向绑定，但是为什么这个指令就可以实现数据的双向绑定呢？其实v-model是vue的一个语法糖。即利用v-model绑定数据后，既绑定了数据，又添加了一个input事件监听。

实现原理：

- v-bind绑定响应数据
- 触发input事件并传递数据

```vue
<input v-model="text"></input>
// 等价于：
<input :value="text" @input="text = $event.target.value"></input>
// 组件中使用：
<custom-input :value="text" @input="$event"></custom-input>
// 根据v-model原理模拟：
<input type="text" id="ipt1">
<input type="text" id="ipt2">
<script>
    var ipt1=document.getElementById('ipt1');
    var ipt2=document.getElementById('ipt2');
    ipt1.addEventListener("input",function(){
        ipt2.value=ipt1.value;
    })
</script>
```

### 23. 对keep-alive的理解，它是如何实现的，具体缓存的是什么？

如果需要在组件切换的时候，保存一些组件的状态防止多次渲染，就可以使用 keep-alive 组件包裹需要保存的组件。

keep-alive有以下三个属性：

- include 字符串或正则表达式，只有名称匹配的组件会被匹配；
- exclude 字符串或正则表达式，任何名称匹配的组件都不会被缓存；
- max 数字，最多可以缓存多少组件实例。

**注意：keep-alive 包裹动态组件时，会缓存不活动的组件实例。**

**使用场景**

使用原则：当我们在某些场景下不需要让页面重新加载时我们可以使用`keep-alive`

当我们从`首页`–>`列表页`–>`商详页`–>`再返回`，这时候列表页应该是需要`keep-alive`

从`首页`–>`列表页`–>`商详页`–>`返回到列表页(需要缓存)`–>`返回到首页(需要缓存)`–>`再次进入列表页(不需要缓存)`，这时候可以按需来控制页面的`keep-alive`

1. 路由中设置`keepAlive`属性判断是否需要缓存

```js
{
  path: 'list',
  name: 'itemList', // 列表页
  component (resolve) {
    require(['@/pages/item/list'], resolve)
 },
 meta: {
  keepAlive: true,
  title: '列表页'
 }
}
```

2. 组件使用`<keep-alive>`

```vue
<div id="app" class='wrapper'>
  <keep-alive>
    <!-- 需要缓存的视图组件 -->
    <router-view v-if="$route.meta.keepAlive"></router-view>
  </keep-alive>
  <!-- 不需要缓存的视图组件 -->
  <router-view v-if="!$route.meta.keepAlive"></router-view>
</div>
```

**主要流程**

1. 判断组件 name ，不在 include 或者在 exclude 中，直接返回 vnode，说明该组件不被缓存。
2. 获取组件实例 key ，如果有获取实例的 key，否则重新生成。
3. key生成规则，cid +"∶∶"+ tag ，仅靠cid是不够的，因为相同的构造函数可以注册为不同的本地组件。
4. 如果缓存对象内存在，则直接从缓存对象中获取组件实例给 vnode ，不存在则添加到缓存对象中。 5.最大缓存数量，当缓存组件数量超过 max 值时，清除 keys 数组内第一个组件。

```js
const patternTypes: Array<Function> = [String, RegExp, Array] // 接收：字符串，正则，数组

export default {
  name: 'keep-alive',
  abstract: true, // 抽象组件，是一个抽象组件：它自身不会渲染一个 DOM 元素，也不会出现在父组件链中。

  props: {
    include: patternTypes, // 匹配的组件，缓存
    exclude: patternTypes, // 不去匹配的组件，不缓存
    max: [String, Number], // 缓存组件的最大实例数量, 由于缓存的是组件实例（vnode），数量过多的时候，会占用过多的内存，可以用max指定上限
  },

  created() {
    // 用于初始化缓存虚拟DOM数组和vnode的key
    this.cache = Object.create(null)
    this.keys = []
  },

  destroyed() {
    // 销毁缓存cache的组件实例
    for (const key in this.cache) {
      pruneCacheEntry(this.cache, key, this.keys)
    }
  },

  mounted() {
    // prune 削减精简[v.]
    // 去监控include和exclude的改变，根据最新的include和exclude的内容，来实时削减缓存的组件的内容
    this.$watch('include', (val) => {
      pruneCache(this, (name) => matches(val, name))
    })
    this.$watch('exclude', (val) => {
      pruneCache(this, (name) => !matches(val, name))
    })
  },
}
```

**render函数：**

1. 会在 keep-alive 组件内部去写自己的内容，所以可以去获取默认 slot 的内容，然后根据这个去获取组件
2. keep-alive 只对第一个组件有效，所以获取第一个子组件。
3. 和 keep-alive 搭配使用的一般有：动态组件 和router-view

```js
render () {
 //
function getFirstComponentChild(children: ?Array<VNode>): ?VNode {
  if (Array.isArray(children)) {
    for (let i = 0; i < children.length; i++) {
      const c = children[i];
      if (isDef(c) && (isDef(c.componentOptions) || isAsyncPlaceholder(c))) {
        return c;
      }
    }
  }
}
const slot = this.$slots.default; // 获取默认插槽
const vnode: VNode = getFirstComponentChild(slot); // 获取第一个子组件
const componentOptions: ?VNodeComponentOptions =
  vnode && vnode.componentOptions; // 组件参数
if (componentOptions) {
  // 是否有组件参数
  // check pattern
  const name: ?string = getComponentName(componentOptions); // 获取组件名
  const { include, exclude } = this;
  if (
    // not included
    (include && (!name || !matches(include, name))) ||
    // excluded
    (exclude && name && matches(exclude, name))
  ) {
    // 如果不匹配当前组件的名字和include以及exclude
    // 那么直接返回组件的实例
    return vnode;
  }

  const { cache, keys } = this;

  // 获取这个组件的key
  const key: ?string =
    vnode.key == null
      ? // same constructor may get registered as different local components
        // so cid alone is not enough (#3269)
        componentOptions.Ctor.cid +
        (componentOptions.tag ? `::${componentOptions.tag}` : "")
      : vnode.key;

  if (cache[key]) {
    // LRU缓存策略执行
    vnode.componentInstance = cache[key].componentInstance; // 组件初次渲染的时候componentInstance为undefined

    // make current key freshest
    remove(keys, key);
    keys.push(key);
    // 根据LRU缓存策略执行，将key从原来的位置移除，然后将这个key值放到最后面
  } else {
    // 在缓存列表里面没有的话，则加入，同时判断当前加入之后，是否超过了max所设定的范围，如果是，则去除
    // 使用时间间隔最长的一个
    cache[key] = vnode;
    keys.push(key);
    // prune oldest entry
    if (this.max && keys.length > parseInt(this.max)) {
      pruneCacheEntry(cache, keys[0], keys, this._vnode);
    }
  }
  // 将组件的keepAlive属性设置为true
  vnode.data.keepAlive = true; // 作用：判断是否要执行组件的created、mounted生命周期函数
}
return vnode || (slot && slot[0]);
}
```

keep-alive 具体是通过 cache 数组缓存所有组件的 vnode 实例。当 cache 内原有组件被使用时会将该组件 key 从 keys 数组中删除，然后 push 到 keys数组最后，以便清除最不常用组件。

实现步骤：
1、获取 keep-alive 下第一个子组件的实例对象，通过他去获取这个组件的组件名
2、通过当前组件名去匹配原来 include 和 exclude，判断当前组件是否需要缓存，不需要缓存，直接返回当前组件的实例vNode
3、需要缓存，判断他当前是否在缓存数组里面：

- 存在，则将他原来位置上的 key 给移除，同时将这个组件的 key 放到数组最后面（LRU）
- 不存在，将组件 key 放入数组，然后判断当前 key数组是否超过 max 所设置的范围，超过，那么削减未使用时间最长的一个组件的 key 
  4
- 最后将这个组件的 keepAlive 设置为 true

(3) keep-alive 本身的创建过程和 patch 过程
缓存渲染的时候，会根据 vnode.componentInstance（首次渲染 vnode.componentInstance 为 undefined） 和 keepAlive 属性判断不会执行组件的 created、mounted 等钩子函数，而是对缓存的组件执行 patch 过程∶ 直接把缓存的 DOM 对象直接插入到目标元素中，完成了数据更新的情况下的渲染过程。

首次渲染
组件的首次渲染∶判断组件的 abstract 属性，才往父组件里面挂载 DOM

```js
// core/instance/lifecycle
function initLifecycle (vm: Component) {
  const options = vm.$options

  // locate first non-abstract parent
  let parent = options.parent
  if (parent && !options.abstract) { // 判断组件的abstract属性，才往父组件里面挂载DOM
    while (parent.$options.abstract && parent.$parent) {
      parent = parent.$parent
    }
    parent.$children.push(vm)
  }

  vm.$parent = parent
  vm.$root = parent ? parent.$root : vm

  vm.$children = []
  vm.$refs = {}

  vm._watcher = null
  vm._inactive = null
  vm._directInactive = false
  vm._isMounted = false
  vm._isDestroyed = false
  vm._isBeingDestroyed = false
}
```

- 判断当前 keepAlive 和 componentInstance 是否存在来判断是否要执行组件 prepatch 还是执行创建 componentlnstance

```js
// core/vdom/create-component
init (vnode: VNodeWithData, hydrating: boolean): ?boolean {
    if (
      vnode.componentInstance &&
      !vnode.componentInstance._isDestroyed &&
      vnode.data.keepAlive
    ) { // componentInstance在初次是undefined!!!
      // kept-alive components, treat as a patch
      const mountedNode: any = vnode // work around flow
      componentVNodeHooks.prepatch(mountedNode, mountedNode) // prepatch函数执行的是组件更新的过程
    } else {
      const child = vnode.componentInstance = createComponentInstanceForVnode(
        vnode,
        activeInstance
      )
      child.$mount(hydrating ? vnode.elm : undefined, hydrating)
    }
  },
```

prepatch 操作就不会在执行组件的 mounted 和 created 生命周期函数，而是直接将 DOM 插入

**（4）LRU （least recently used）缓存策略**

LRU 缓存策略∶ 从内存中找出最久未使用的数据并置换新的数据。

LRU（Least rencently used）算法根据数据的历史访问记录来进行淘汰数据，其核心思想是**"如果数据最近被访问过，那么将来被访问的几率也更高"**。 最常见的实现是使用一个链表保存缓存数据，详细算法实现如下∶ 

- 新数据插入到链表头部
- 每当缓存命中（即缓存数据被访问），则将数据移到链表头部
- 链表满的时候，将链表尾部的数据丢弃。

### 24. ==Vue.observable你有了解过吗？==

> `Vue.observable`，让一个对象变成响应式数据。`Vue` 内部会用它来处理 `data` 函数返回的对象

返回的对象可以直接用于渲染函数和计算属性内，并且会在发生变更时触发相应的更新。也可以作为最小化的跨组件状态存储器

```js
Vue.observable({ count : 1})
```

其作用等同于

```js
new vue({ count : 1})
```

在 Vue 2.x 中，被传入的对象会直接被 Vue.observable 变更，它和被返回的对象是同一个对象

在 Vue 3.x 中，则会返回一个可响应的代理，而对源对象直接进行变更仍然是不可响应的

**使用场景**

在非父子组件通信时，可以使用通常的`bus`或者使用`vuex`，但是实现的功能不是太复杂，而使用上面两个又有点繁琐。这时，`observable`就是一个很好的选择

```js
// 引入vue
import Vue from 'vue
// 创建state对象，使用observable让state对象可响应
export let state = Vue.observable({
  name: '张三',
  'age': 38
})
// 创建对应的方法
export let mutations = {
  changeName(name) {
    state.name = name
  },
  setAge(age) {
    state.age = age
  }
}
```

```vue
<template>
  <div>
    姓名：{{ name }}
    年龄：{{ age }}
    <button @click="changeName('李四')">改变姓名</button>
    <button @click="setAge(18)">改变年龄</button>
  </div>
</template>

<script>
import { state, mutations } from '@/store'
export default {
  // 在计算属性中拿到值
  computed: {
    name() {
      return state.name
    },
    age() {
      return state.age
    }
  },
  // 调用mutations里面的方法，更新数据
  methods: {
    changeName: mutations.changeName,
    setAge: mutations.setAge
  }
}
</script>
```

### 24. ⚡️$nextTick原理及作用

官方对其的定义

> 在下次 DOM 更新循环结束之后执行延迟回调。在修改数据之后立即使用这个方法，获取更新后的 DOM

**作用，在以下情况下，会用到nextTick：**

- 在数据变化后执行的某个操作，而这个操作需要使用随数据变化而变化的DOM结构的时候，这个操作就需要方法在`nextTick()`的回调函数中。
- 在vue生命周期中，如果在created()钩子进行DOM操作，也一定要放在`nextTick()`的回调函数中。

因为在created()钩子函数中，页面的DOM还未渲染，这时候也没办法操作DOM，所以，此时如果想要操作DOM，必须将操作的代码放在`nextTick()`的回调函数中。

**原理**

**Vue 的 nextTick 其本质是对 JavaScript 执行原理 EventLoop 的一种应用。**

nextTick 的核心是利用了如 Promise 、MutationObserver、setImmediate、setTimeout的原生 JavaScript 方法来模拟对应的微/宏任务的实现，本质是为了利用 JavaScript 的这些异步回调任务队列来实现 Vue 框架中自己的异步回调队列。

nextTick 不仅是 Vue 内部的异步队列的调用方法，同时也允许开发者在实际项目中使用这个方法来满足实际应用中对 DOM 更新数据时机的后续逻辑处理

nextTick 是典型的将底层 JavaScript 执行原理应用到具体案例中的示例，引入异步更新队列机制的原因∶

- 如果是同步更新，则多次对一个或多个属性赋值，会频繁触发 UI/DOM 的渲染，可以减少一些无用渲染
- 同时由于 VirtualDOM 的引入，每一次状态发生变化后，状态变化的信号会发送给组件，组件内部使用 VirtualDOM 进行计算得出需要更新的具体的 DOM 节点，然后对 DOM 进行更新操作，每次更新状态后的渲染过程需要更多的计算，而这种无用功也将浪费更多的性能，所以异步渲染变得更加至关重要

Vue采用了数据驱动视图的思想，但是在一些情况下，仍然需要操作DOM。有时候，可能遇到这样的情况，DOM1的数据发生了变化，而DOM2需要从DOM1中获取数据，那这时就会发现DOM2的视图并没有更新，这时就需要用到了`nextTick`了。

由于Vue的DOM操作是异步的，所以，在上面的情况中，就要将DOM2获取数据的操作写在`$nextTick`中。

在下次 DOM 更新循环结束之后执行延迟回调。在修改数据之后立即使用这个方法，获取更新后的 DOM

eventLoop,本质是使用js的异步回调队列实现vue框架中自己的异步回调

Vue是异步执行dom更新的，一旦观察到数据变化，Vue就会开启一个队列，然后把在同一个事件循环 (event loop) 当中观察到数据变化的 watcher 推送进这个队列。如果这个watcher被触发多次，只会被推送到队列一次。这种缓冲行为可以有效的去掉重复数据造成的不必要的计算和DOM操作。而在下一个事件循环时，Vue会清空队列，并进行必要的DOM更新。

```vue
this.$nextTick(() => {
    // 获取数据的操作...
})
```

### 25. 什么是mixin?

分为**局部混入**跟**全局混入**，全局混入会影响到每个组件实例，一般用于写插件。

- Mixin 使我们能够为 Vue 组件编写可插拔和可重用的功能。
- 如果希望在多个组件之间重用一组组件选项，例如生命周期 hook方法等，则可以将其编写为 mixin，并在组件中简单的引用它。
- 然后将 mixin 的内容合并到组件中。如果你要在 mixin 中定义生命周期 hook，那么它在执行时将优化于组件自已的 hook。

**使用场景**

在日常的开发中，我们经常会遇到在不同的组件中经常会需要用到一些相同或者相似的代码，这些代码的功能相对独立

这时，可以通过`Vue`的`mixin`功能将相同或者相似的代码提出来。

定义一个`modal`弹窗组件，内部通过`isShowing`来控制显示

```js
const Modal = {
  template: "#modal",
  data() {
    return {
      isShowing: false
    };
  },
  methods: {
    toggleShow() {
      this.isShowing = !this.isShowing;
    }
  }
};

```

定义一个`tooltip`提示框，内部通过`isShowing`来控制显示

```js
1const Tooltip = {
  template: "#tooltip",
  data() {
    return {
      isShowing: false
    };
  },
  methods: {
    toggleShow() {
      this.isShowing = !this.isShowing;
    }
  }
};
```

通过观察上面两个组件，发现两者的逻辑是相同，代码控制显示也是相同的，这时候`mixin`就派上用场了

首先抽出共同代码，编写一个`mixin`

```js
const toggle = {
  data() {
    return {
      isShowing: false
    };
  },
  methods: {
    toggleShow() {
      this.isShowing = !this.isShowing;
    }
  }
};

```

两个组件在使用上，只需要引入`mixin`

```js
const Modal = {
  template: "#modal",
  mixins: [toggle]
};

const Tooltip = {
  template: "#tooltip",
  mixins: [toggle]
};

```

### 26. mixin和mixins区别

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h83j5m54tzj319k0tcqan.jpg" alt="image.png" style="zoom:50%;" />

`mixin` 用于全局混入，会影响到每个组件实例，通常插件都是这样做初始化的。

```vue
Vue.mixin({
    beforeCreate() {
        // ...逻辑
        // 这种方式会影响到每个组件的 beforeCreate 钩子函数
    }
})
```

虽然文档不建议在应用中直接使用 `mixin`，但是如果不滥用的话也是很有帮助的，比如可以全局混入封装好的 `ajax` 或者一些工具函数等等。

`mixins` 应该是最常使用的扩展组件的方式了。如果多个组件中有相同的业务逻辑，就可以将这些逻辑剥离出来，通过 `mixins` 混入代码，比如上拉下拉加载数据这种逻辑等等。

另外需要注意的是 `mixins` 混入的钩子函数会先于组件内的钩子函数执行，并且在遇到同名选项的时候也会有选择性的进行合并。

### 27. extend有什么作用

这个 API 很少用到，作用是扩展组件生成一个构造器，通常会与 $mount 一起使用。

```vue
// 创建组件构造器
let Component = Vue.extend({
  template: '<div>test</div>'
})
// 挂载到 #app 上
new Component().$mount('#app')
// 除了上面的方式，还可以用来扩展已有的组件
let SuperComponent = Vue.extend(Component)
new SuperComponent({
    created() {
        console.log(1)
    }
})
new SuperComponent().$mount('#app')
```

### 28. 简述 mixin、extends 的覆盖逻辑

[Extend and Mixins](https://class-component.vuejs.org/guide/extend-and-mixins.html#extend)

[extends](https://cn.vuejs.org/api/options-composition.html#extends)

**（1）mixin 和 extends**

mixin 和 extends 均是用于合并、拓展组件的，两者均通过 mergeOptions 方法实现合并。

- mixins 接收一个混入对象的数组，其中混入对象可以像正常的实例对象一样包含实例选项，这些选项会被合并到最终的选项中。Mixin 钩子按照传入顺序依次调用，并在调用组件自身的钩子之前被调用。
- extends 主要是为了便于扩展单文件组件，接收一个对象或构造函数。

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h817zwolv3j31hy0xo467.jpg" alt="image.png" style="zoom:33%;" />

**（2）mergeOptions 的执行过程**

- 规范化选项（normalizeProps、normalizelnject、normalizeDirectives)
- 对未合并的选项，进行判断

```js
if(!child._base) {
    if(child.extends) {
        parent = mergeOptions(parent, child.extends, vm)
    }
    if(child.mixins) {
        for(let i = 0, l = child.mixins.length; i < l; i++){
            parent = mergeOptions(parent, child.mixins[i], vm)
        }
    }
}
```

- 合并处理。根据一个通用 Vue 实例所包含的选项进行分类逐一判断合并，如 props、data、 methods、watch、computed、生命周期等，将合并结果存储在新定义的 options 对象里。
- 返回合并结果 options。

### 29. ⚡️描述下Vue自定义指令

**应用场景**

- 表单防止重复提交
- 图片懒加载
- 一键 Copy的功能

---

在 Vue2.0 中，代码复用和抽象的主要形式是组件。然而，有的情况下，你仍然需要对普通 DOM 元素进行底层操作，这时候就会用到自定义指令。

一般需要对DOM元素进行底层操作时使用，尽量只用来操作 DOM展示，不修改内部的值。当使用自定义指令直接修改 value 值时绑定v-model的值也不会同步更新；如必须修改可以在自定义指令中使用keydown事件，在vue组件中使用 change事件，回调中修改vue数据; 

**（1）自定义指令基本内容**

- 全局定义：`Vue.directive("focus",{})`
- 局部定义：`directives:{focus:{}}`
- 钩子函数：指令定义对象提供钩子函数

​      o bind：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置。

​      o inSerted：被绑定元素插入父节点时调用（仅保证父节点存在，但不一定已被插入文档中）。

​      o update：所在组件的VNode更新时调用，但是可能发生在其子VNode更新之前调用。指令的值可能发生了改变，也可能没有。但是可以通过比较更新前后的值来忽略不必要的模板更新。

​      o ComponentUpdate：指令所在组件的 VNode及其子VNode全部更新后调用。

​      o unbind：只调用一次，指令与元素解绑时调用。

- 钩子函数参数

​      o el：绑定元素

​      o bing： 指令核心对象，描述指令全部信息属性

​      o name

​      o value

​      o oldValue

​      o expression

​      o arg

​      o modifers

​      o vnode  虚拟节点

​      o oldVnode：上一个虚拟节点（更新钩子函数中才有用）

**（2）使用场景**

- 普通DOM元素进行底层操作的时候，可以使用自定义指令
- 自定义指令是用来操作DOM的。尽管Vue推崇数据驱动视图的理念，但并非所有情况都适合数据驱动。自定义指令就是一种有效的补充和扩展，不仅可用于定义任何的DOM操作，并且是可复用的。

**（3）使用案例**

初级应用：

- 鼠标聚焦
- 下拉菜单
- 相对时间转换
- 滚动动画

高级应用：

- 自定义指令实现图片懒加载
- 自定义指令集成第三方插件

### 30. 子组件可以直接改变父组件的数据吗？

子组件不可以直接改变父组件的数据。这样做主要是为了维护父子组件的单向数据流。每次父级组件发生更新时，子组件中所有的 prop 都将会刷新为最新的值。如果这样做了，Vue 会在浏览器的控制台中发出警告。

Vue提倡单向数据流，即父级 props 的更新会流向子组件，但是反过来则不行。这是为了防止意外的改变父组件状态，使得应用的数据流变得难以理解，导致数据流混乱。如果破坏了单向数据流，当应用复杂时，debug 的成本会非常高。

只能通过 **$emit** 派发一个自定义事件，父组件接收到后，由父组件修改

### 31. ⚡️==Vue是如何收集依赖的?==

在初始化 Vue 的每个组件时，会对组件的 data 进行初始化，就会将由普通对象变成响应式对象，在这个过程中便会进行依赖收集的相关逻辑，如下所示∶

```javascript
function defieneReactive (obj, key, val){
  const dep = new Dep();
  ...
  Object.defineProperty(obj, key, {
    ...
    get: function reactiveGetter () {
      if(Dep.target){
        dep.depend();
        ...
      }
      return val
    }
    ...
  })
}
```

以上只保留了关键代码，主要就是 `const dep = new Dep()`实例化一个 Dep 的实例，然后在 get 函数中通过 `dep.depend()` 进行依赖收集。

**（1）Dep**

Dep是整个依赖收集的核心，其关键代码如下：

```javascript
class Dep {
  static target;
  subs;

  constructor () {
    ...
    this.subs = [];
  }
  addSub (sub) {
    this.subs.push(sub)
  }
  removeSub (sub) {
    remove(this.sub, sub)
  }
  depend () {
    if(Dep.target){
      Dep.target.addDep(this)
    }
  }
  notify () {
    const subs = this.subds.slice();
    for(let i = 0;i < subs.length; i++){
      subs[i].update()
    }
  }
}
```

Dep 是一个 class ，其中有一个关 键的静态属性 static，它指向了一个全局唯一 Watcher，保证了同一时间全局只有一个 watcher 被计算，另一个属性 subs 则是一个 Watcher 的数组，所以 Dep 实际上就是对 Watcher 的管理，再看看 Watcher 的相关代码∶

**（2）Watcher**

```javascript
class Watcher {
  getter;
  ...
  constructor (vm, expression){
    ...
    this.getter = expression;
    this.get();
  }
  get () {
    pushTarget(this);
    value = this.getter.call(vm, vm)
    ...
    return value
  }
  addDep (dep){
        ...
    dep.addSub(this)
  }
  ...
}
function pushTarget (_target) {
  Dep.target = _target
}
```

Watcher 是一个 class，它定义了一些方法，其中和依赖收集相关的主要有 get、addDep 等。

**（3）过程**

在实例化 Vue 时，依赖收集的相关过程如下∶

初 始 化 状 态 initState ， 这 中 间 便 会 通 过 defineReactive 将数据变成响应式对象，其中的 getter 部分便是用来依赖收集的。

初始化最终会走 mount 过程，其中会实例化 Watcher ，进入 Watcher 中，便会执行 this.get() 方法，

```javascript
updateComponent = () => {
  vm._update(vm._render())
}
new Watcher(vm, updateComponent)
```

get 方法中的 pushTarget 实际上就是把 Dep.target 赋值为当前的 watcher。

`this.getter.call（vm，vm）`，这里的 getter 会执行 vm._render() 方法，在这个过程中便会触发数据对象的 getter。那么每个对象值的 getter 都持有一个 dep，在触发 getter 的时候会调用 dep.depend() 方法，也就会执行 Dep.target.addDep(this)。刚才 Dep.target 已经被赋值为 watcher，于是便会执行 addDep 方法，然后走到 dep.addSub() 方法，便将当前的 watcher 订阅到这个数据持有的 dep 的 subs 中，这个目的是为后续数据变化时候能通知到哪些 subs 做准备。所以在 vm._render() 过程中，会触发所有数据的 getter，这样便已经完成了一个依赖收集的过程

### 32. ==assets和static的区别==

**相同点：** `assets` 和 `static` 两个都是存放静态资源文件。项目中所需要的资源文件图片，字体图标，样式文件等都可以放在这两个文件下，这是相同点

**不相同点：**

`assets` 中存放的静态资源文件在项目打包时，也就是运行 `npm run build` 时会将 `assets` 中放置的静态资源文件进行打包上传，所谓打包简单点可以理解为压缩体积，代码格式化。而压缩后的静态资源文件最终也都会放置在 `static` 文件中跟着 `index.html` 一同上传至服务器。

`static` 中放置的静态资源文件就不会要走打包压缩格式化等流程，而是直接进入打包好的目录，直接上传至服务器。因为避免了压缩直接进行上传，在打包时会提高一定的效率，但是 `static` 中的资源文件由于没有进行压缩等操作，所以文件的体积也就相对于 `assets` 中打包后的文件提交较大点。在服务器中就会占据更大的空间。

**建议：** 将项目中 `template`需要的样式文件js文件等都可以放置在 `assets` 中，走打包这一流程。减少体积。而项目中引入的第三方的资源文件如`iconfoont.css` 等文件可以放置在 `static` 中，因为这些引入的第三方文件已经经过处理，不再需要处理，直接上传。

### 33. delete和Vue.delete删除数组的区别

- `delete` 只是被删除的元素变成了 `empty/undefined` 其他的元素的键值还是不变。
- `Vue.delete` 直接删除了数组改变了数组的键值。

### 34. Vue模版编译原理

vue中的模板template无法被浏览器解析并渲染，因为这不属于浏览器的标准，不是正确的HTML语法，所有需要将template转化成一个JavaScript函数，这样浏览器就可以执行这一个函数并渲染出对应的HTML元素，就可以让视图跑起来了，这一个转化的过程，就成为模板编译。模板编译又分三个阶段，解析parse，优化optimize，生成generate，最终生成可执行函数render。

- **解析阶段**：使用大量的正则表达式对template字符串进行解析，将标签、指令、属性等转化为抽象语法树AST。
- **优化阶段**：遍历AST，找到其中的一些静态节点并进行标记，方便在页面重渲染的时候进行diff比较时，直接跳过这一些静态节点，优化runtime的性能。
- **生成阶段**：将最终的AST转化为render函数字符串。

### 35. Vue template 到 render 的过程

- 把模板编译为render函数
- 实例进行挂载, 根据根节点render函数的调用，递归的生成虚拟dom
- 对比虚拟dom，渲染到真实dom
- 组件内部data发生变化，组件和子组件引用data作为props重新调用render函数，生成虚拟dom, 对比虚拟dom，渲染到真实dom

vue的模版编译过程主要如下：**template -> ast -> render函数**

vue 在模版编译版本的码中会执行 compileToFunctions 将template转化为render函数：

```javascript
// 将模板编译为render函数
const { render, staticRenderFns } = compileToFunctions(template,options//省略}, this)
```

CompileToFunctions中的主要逻辑如下∶

**（1）调用parse方法将template转化为ast（抽象语法树）**

```javascript
const ast = parse(template.trim(), options)
```

- **parse的目标**：把tamplate转换为AST树，它是一种用 JavaScript对象的形式来描述整个模板。
- **解析过程**：利用正则表达式顺序解析模板，当解析到开始标签、闭合标签、文本的时候都会分别执行对应的 回调函数，来达到构造AST树的目的。

AST元素节点总共三种类型：type为1表示普通元素、2为表达式、3为纯文本

**（2）对静态节点做优化**

```javascript
optimize(ast,options)
```

这个过程主要分析出哪些是静态节点，给其打一个标记，为后续更新渲染可以直接跳过静态节点做优化

深度遍历AST，查看每个子树的节点元素是否为静态节点或者静态节点根。如果为静态节点，他们生成的DOM永远不会改变，这对运行时模板更新起到了极大的优化作用。

**（3）生成代码**

```javascript
const code = generate(ast, options)
```

generate将ast抽象语法树编译成 render字符串并将静态部分放到 staticRenderFns 中，最后通过 `new Function(`` render``)` 生成render函数。

### 36. template和jsx的有什么分别?

复杂组件，结构和逻辑习惯

对于 runtime 来说，只需要保证组件存在 render 函数即可，而有了预编译之后，只需要保证构建过程中生成 render 函数就可以。在 webpack 中，使用`vue-loader`编译.vue文件，内部依赖的`vue-template-compiler`模块，在 webpack 构建过程中，将template预编译成 render 函数。与 react 类似，在添加了jsx的语法糖解析器`babel-plugin-transform-vue-jsx`之后，就可以直接手写render函数。

所以，template和jsx的都是render的一种表现形式，不同的是：JSX相对于template而言，具有更高的灵活性，在复杂的组件中，更具有优势，而 template 虽然显得有些呆滞。但是 template 在代码结构上更符合视图与逻辑分离的习惯，更简单、更直观、更好维护。

### 37. SPA（单页应用）首屏加载速度慢怎么解决

首屏时间（First Contentful Paint），指的是浏览器从响应用户输入网址地址，到首屏内容渲染完成的时间，此时整个网页不一定要全部渲染完成，但需要展示当前视窗需要的内容

#### 加载慢的原因

- 网络延时问题
- 资源文件体积是否过大
- 资源是否重复发送请求去加载了
- 加载脚本的时候，渲染内容堵塞了
- 
#### 方案

[方案](https://vue3js.cn/interview/vue/first_page_time.html#%E4%B8%89%E3%80%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
1. 减小入口文件积
2. 静态资源本地缓存
3. UI框架按需加载
4. 图片资源的压缩
5. 组件重复打包
6. 开启GZip压缩
7. 使用SSR

### 37. ==对SSR的理解==

`Server-Side Rendering` 我们称其为`SSR`，意为服务端渲染

SSR也就是服务端渲染，也就是将Vue在客户端把标签渲染成HTML的工作放在服务端完成，然后再把html直接返回给客户端

- seo：搜索引擎优先爬取页面`HTML`结构，使用`ssr`时，服务端已经生成了和业务想关联的`HTML`，有利于`seo`
- 首屏呈现渲染：用户无需等待页面所有`js`加载完成就可以看到页面视图（压力来到了服务器，所以需要权衡哪些用服务端渲染，哪些交给客户端）

**SSR的优势：**

1. 更好的SEO
2. 首屏加载速度更快

**SSR的缺点：**

1. 开发条件会受到限制，服务器端渲染只支持beforeCreate和created两个钩子；
2. 当需要一些外部扩展库时需要特殊处理，服务端渲染应用程序也需要处于Node.js的运行环境；
3. 更多的服务端负载。

### 38. 对SPA单页面的理解，它的优缺点分别是什么?

- 用户体验好，只刷新部分数据，服务器压力小，前后端职责分离
- 初次加载消耗多，路由不能使用浏览器的前进后退，seo难度大

SPA（ single-page application ）仅在 Web 页面初始化时加载相应的 HTML、JavaScript 和 CSS。一旦页面加载完成，SPA 不会因为用户的操作而进行页面的重新加载或跳转；取而代之的是利用路由机制实现 HTML 内容的变换，UI 与用户的交互，避免页面的重新加载。

**优点：**

1. 用户体验好、快，内容的改变不需要重新加载整个页面，避免了不必要的跳转和重复渲染；
2. 基于上面一点，SPA 相对对服务器压力小；
3. 前后端职责分离，架构清晰，前端进行交互逻辑，后端负责数据处理；

**缺点：**

1. 初次加载耗时多：为实现单页 Web 应用功能及显示效果，需要在加载页面的时候将 JavaScript、CSS 统一加载，部分页面按需加载；
2. 前进后退路由管理：由于单页应用在一个页面中显示所有的内容，所以不能使用浏览器的前进后退功能，所有的页面切换需要自己建立堆栈管理；
3. SEO 难度较大：由于所有的内容都在一个页面中动态替换显示，所以在 SEO 上其有着天然的弱势。

### 39. Vue单页应用与多页应用的区别

- SPA单页面应用（SinglePage Web Application），指只有一个主页面的应用，一开始只需要加载一次js、css等相关资源。所有内容都包含在主页面，对每一个功能模块组件化。单页应用跳转，就是切换相关组件，仅仅刷新局部资源。
- MPA多页面应用 （MultiPage Application），指有多个独立页面的应用，每个页面必须重复加载js、css等相关资源。多页应用跳转，需要整页资源刷新。

数据传递，资源文件，结构

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h816g611roj30sq0v8jxp.jpg" alt="image.png" style="zoom: 50%;" />

### 40. vue初始化页面闪动问题

使用vue开发时，在vue初始化之前，由于div是不归vue管的，所以我们写的代码在还没有解析的情况下会容易出现花屏现象，看到类似于{{message}}的字样，虽然一般情况下这个时间很短暂，但是还是有必要让解决这个问题的。

**1. 方法一：为初始化实例的跟标签添加v-cloak属性**

v-cloak原理是先通过样式隐藏内容，然后在内存中进行值的替换，将替换的内容再反馈给界面，数据渲染完成之后，v-cloak 属性会被自动去除。

和 CSS 规则如 [v-cloak] { display: none } 一起用时，这个指令可以隐藏未编译的 Mustache 标签直到实例准备完毕。也就是说v-cloak指令可以像CSS选择器一样绑定一套CSS样式然后这套CSS会一直生效到实例编译结束。

首先：在css里加上以下代码：

```vue
<template>
  <keep-alive include="index">
      <router-view v-cloak></router-view>
    </keep-alive>
</template>
```

```css
<style>
  /* 隐藏Vue代码，所有的组件设置成隐藏 */
  [v-cloak]:not(body) {
    display: none;
  }
</style>
```

**2. 方法二：在根元素加上`style="display: none;" :style="{display: 'block'}"`**

如果没有彻底解决问题，则在根元素加上`style="display: none;" :style="{display: 'block'}"`

原理：

vue在渲染之前，style="display: none;"让页面不显示

vue渲染完成了，:style="display: block;"让页面显示

**3. 方法三：可以添加一个loading遮罩层，等初始化或者挂载完成mount周期函数里移除遮罩层。**

**4. 方法四：使用 v-text 和 v-html 指令来替代`{{ }}`**

vue中我们会将数据包在两个大括号中，然后放到HTML里，但是在vue内部，所有的双括号会被编译成textNode的一个v-text指令。
而使用v-text的好处就是永远更好的性能，更重要的是可以避免FOUC (Flash of Uncompiled Content) ，也就是上面与遇到的问题。

```vue
<div id="app">
  v-text:<span v-text="hello"></span> <br />
  v-html:<span v-html="hello"></span>
</div>
```

```vue
<span v-text="msg"></span>
<!-- same as -->
<span>{{msg}}</span>
```





### 41. 对Vue组件化的理解/组件化的好处

1. 组件是独立和可复用的代码组织单元。组件系统是Vue核心特性之一，它使开发者使用小型、独立和通常可复用的组件构建大型应用；
2. 组件化开发能大幅提高应用开发效率、测试性、复用性等；
3. 组件使用按分类有：页面组件、业务组件、通用组件；
4. vue的组件是基于配置的，我们通常编写的组件是组件配置而非组件，框架后续会生成其构造函数，它们基于VueComponent，扩展于Vue；
5. vue中常见组件化技术有：属性prop，自定义事件，插槽等，它们主要用于组件通信、扩展等；6.合理的划分组件，有助于提升应用性能；
6. 组件应该是高内聚、低耦合的；
7. 遵循单向数据流的原则。

### 42. 对vue设计原则的理解

1. **渐进式JavaScript框架**：与其它大型框架不同的是，Vue被设计为可以自底向上逐层应用。Vue的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue也完全能够为复杂的单页应用提供驱动。
2. **易用性**：vue提供数据响应式、声明式模板语法和基于配置的组件系统等核心特性。这些使我们只需要关注应用的核心业务即可，只要会写js、html和css就能轻松编写vue应用。
3. **灵活性**：渐进式框架的最大优点就是灵活性，如果应用足够小，我们可能仅需要vue核心特性即可完成功能；随着应用规模不断扩大，我们才可能逐渐引入路由、状态管理、vue-cli等库和工具，不管是应用体积还是学习难度都是一个逐渐增加的平和曲线。
4. **高效性：**超快的虚拟DOM和diﬀ算法使我们的应用拥有最佳的性能表现。追求高效的过程还在继续，vue3中引入Proxy对数据响应式改进以及编译器中对于静态内容编译的改进都会让vue更加高效。

### 43. Vue的性能优化有哪些

**（1）编码阶段**

- 尽量减少data中的数据，data中的数据都会增加getter和setter，会收集对应的watcher
- v-if和v-for不能连用
- 如果需要使用v-for给每项元素绑定事件时使用事件代理
- SPA 页面采用keep-alive缓存组件
- 在更多的情况下，使用v-if替代v-show
- key保证唯一
- 使用路由懒加载、异步组件
- 防抖、节流
- 第三方模块按需导入
- 长列表滚动到可视区域动态加载
- 图片懒加载

**（2）SEO优化**

- 预渲染
- 服务端渲染SSR

**（3）打包优化**

- 压缩代码
- Tree Shaking/Scope Hoisting
- 使用cdn加载第三方模块
- 多线程打包happypack
- splitChunks抽离公共文件
- sourceMap优化

**（4）用户体验**

- 骨架屏
- PWA
- 还可以使用缓存(客户端缓存、服务端缓存)优化、服务端开启gzip压缩等。

### 44. 常见的Vue性能优化方法

- 路由懒加载
- Keep alive
- 使用v-show复用DOM
- v-for 遍历避免同时使用 v-if
- 长列表性能优化
- 事件的销毁
- 图片懒加载
- 第三方插件按需引入
- 无状态的组件标记为函数式组件
- 子组件分隔
- 变量本地化
- SSR

```js
// 1. 路由懒加载
const router = new VueRouter({ routes: [
  	{ path: '/foo', component: () => import('./Foo.vue') }
  ]
})
```

```vue
// 2. keep-alive缓存页面
<template>
  <div id="app">
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>
```

```vue
// 3. 使用v-show复用DOM
<template>
  <div class="cell">
     <!--这种情况用v-show复用DOM，比v-if效果好-->
     <div v-show="value" class="on">
        <Heavy :n="10000"/>
     </div>
     <section v-show="!value" class="off">
        <Heavy :n="10000"/>
     </section>
  </div>
</template>
```

```vue
// 4. v-for 遍历避免同时使用 v-if
<template>
  <ul>
		<li v-for="user in activeUsers" :key="user.id">
			{{ user.name }}
		</li>
	</ul>
</template>

<script>
export default { 
  computed: {
		activeUsers: function () {
			return this.users.filter(function (user) { 
        return user.isActive
      })
		}
	}
}
</script>
```

```vue
// 5. 长列表性能优化
// 如果列表是纯粹的数据展示，不会有任何改变，就不需要做响应化
export default { 
	data: () => ({
		users: []
	}),
	async created() {
		const users = await axios.get("/api/users"); 
		this.users = Object.freeze(users);
	}	
};

// 如果是大数据长列表，可采用虚拟滚动，只渲染少部分区域的内容
<recycle-scroller class="items" :items="items" :item-size="24">
	<template v-slot="{ item }">
 		<FetchItemView :item="item" @vote="voteItem(item)"/>
  </template>
</recycle-scroller>
```

```js
// 6. 事件的销毁
// Vue 组件销毁时，会自动解绑它的全部指令及事件监听器，但是仅限于组件本身的事件。
created() {
	this.timer = setInterval(this.refresh, 2000)
},
beforeDestroy() { 
	clearInterval(this.timer)
}
```

```js
// 7. 图片懒加载
// 对于图片过多的页面，为了加速页面加载速度，所以很多时候我们需要将页面内未出现在可视区域内的图片先不做加载， 等到滚动到可视区域后再去加载。
<img v-lazy="/static/img/1.png">
```

```js
// 8. 第三方插件按需引入
// 像element-ui这样的第三方组件库可以按需引入避免体积太大。
import Vue from 'vue';
import { Button, Select } from 'element-ui';


Vue.use(Button) Vue.use(Select)
```

```vue
// 9. 无状态的组件标记为函数式组件
<template functional>
	<div class="cell">
		<div v-if="props.value" class="on"></div>
		<section v-else class="off"></section>
	</div>
</template>


<script>
	export default { props: ['value'] }
</script>
```

```vue
// 10. 子组件分隔
<template>
	<div>
		<ChildComp/>
	</div>
</template>

<script>
	export default { 
    components: {
			ChildComp: { 
        methods: {
					heavy () { /* 耗时任务 */ }
				},
				render (h) {
					return h('div', this.heavy())
				}
			}
		}
	}
</script>
```

```vue
// 11. 变量本地化
<template>
	<div :style="{ opacity: start / 300 }">
		{{ result }}
	</div>
</template>

<script>
import { heavy } from '@/utils'

export default { 
  props: ['start'], 
  computed: {
		base () { 
      return 42 
    }, 
    result () {
			const base = this.base // 不要频繁引用this.base
			let result = this.start
			for (let i = 0; i < 1000; i++) { 
        result += heavy(base)
			}
			return result
		}
	}
}
</script>
```

### 45. 对React和Vue的理解，它们的异同

核心库，构建工具，虚拟DOM，数据传递，组件化

数据流，模板写法，高阶组件，diff算法

**相似之处：**

1. 都将注意力集中保持在核心库，而将其他功能如路由和全局状态管理交给相关的库；
2. 都有自己的构建工具，能让你得到一个根据最佳实践设置的项目模板；
3. 都使用了Virtual DOM（虚拟DOM）提高重绘性能；
4. 都有props的概念，允许组件间的数据传递；
5. 都鼓励组件化应用，将应用分拆成一个个功能明确的模块，提高复用性。

**不同之处 ：**

1. 数据流

   Vue默认支持数据双向绑定，而React一直提倡单向数据流 

2. 虚拟DOM

   - Vue2.x开始引入"Virtual DOM"，消除了和React在这方面的差异，但是在具体的细节还是有各自的特点。 
   - Vue宣称可以更快地计算出Virtual DOM的差异，这是由于它在渲染过程中，会跟踪每一个组件的依赖关系，不需要重新渲染整个组件树。
   - 对于React而言，每当应用的状态被改变时，全部子组件都会重新渲染。当然，这可以通过`PureComponent/shouldComponentUpdate`这个生命周期方法来进行控制，但Vue将此视为默认的优化。

3. 组件化

   - React与Vue最大的不同是模板的编写。
   - Vue鼓励写近似常规HTML的模板。写起来很接近标准 HTML元素，只是多了一些属性。
   - React推荐你所有的模板通用JavaScript的语法扩展——JSX书写。具体来讲：React中render函数是支持闭包特性的，所以import的组件在render中可以直接调用。但是在Vue中，由于模板中使用的数据都必须挂在 this 上进行一次中转，所以 import 一个组件完了之后，还需要在 components 中再声明下。

4. 监听数据变化的实现原理不同

   - Vue 通过 getter/setter 以及一些函数的劫持，能精确知道数据变化，不需要特别的优化就能达到很好的性能
   - React 默认是通过比较引用的方式进行的，如果不优化（PureComponent/shouldComponentUpdate）可能导致大量不必要的vDOM的重新渲染。这是因为 Vue 使用的是可变数据，而React更强调数据的不可变。

5. 高阶组件

   react可以通过高阶组件（HOC）来扩展，而Vue需要通过mixins来扩展。高阶组件就是高阶函数，而React的组件本身就是纯粹的函数，所以高阶函数对React来说易如反掌。相反Vue.js使用HTML模板创建视图组件，这时模板无法有效的编译，因此Vue不能采用HOC来实现。

6. 构建工具
   两者都有自己的构建工具：
   React ==> Create React APP
   Vue ==> vue-cli

7. 跨平台
   React ==> React Native
   Vue ==> Weex

### 46. Vue的优点

轻量级框架，简单易学国人开发，双向数据绑定，组件化，虚拟dom，运行速度快

- 轻量级框架：只关注视图层，是一个构建数据的视图集合，大小只有几十 `kb` ；
- 简单易学：国人开发，中文文档，不存在语言障碍 ，易于理解和学习；
- 双向数据绑定：保留了 `angular` 的特点，在数据操作方面更为简单；
- 组件化：保留了 `react` 的优点，实现了 `html` 的封装和重用，在构建单页面应用方面有着独特的优势；
- 视图，数据，结构分离：使数据的更改更为简单，不需要进行逻辑代码的修改，只需要操作数据就能完成相关操作；
- 虚拟DOM：`dom` 操作是非常耗费性能的，不再使用原生的 `dom` 操作节点，极大解放 `dom` 操作，但具体操作的还是 `dom` 不过是换了另一种方式；
- 运行速度更快：相比较于 `react` 而言，同样是操作虚拟 `dom`，就性能而言， `vue` 存在很大的优势。

### 47. 说下你的Vue项目的目录结构，如果是大型项目你该怎么划分结构和划分组件呢？

https://vue3js.cn/interview/vue/structure.html#%E4%B8%80%E3%80%81%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E5%88%92%E5%88%86

### 48. Vue要做权限管理该怎么做？控制到按钮级别的权限怎么做？

https://vue3js.cn/interview/vue/permission.html#%E4%BA%8C%E3%80%81%E5%A6%82%E4%BD%95%E5%81%9A

接口权限目前一般采用`jwt`的形式来验证，没有通过的话一般返回`401`，跳转到登录页面重新进行登录

登录完拿到`token`，将`token`存起来，通过`axios`请求拦截器进行拦截，每次请求的时候头部携带`token`

### 49. vue项目本地开发完成后部署到服务器后报404是什么原因呢？

https://vue3js.cn/interview/vue/404.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88

### 50. 你是怎么处理vue项目中的错误的？

https://vue3js.cn/interview/vue/error.html#%E4%B8%80%E3%80%81%E9%94%99%E8%AF%AF%E7%B1%BB%E5%9E%8B



## 二、生命周期

### 1. 说一下Vue的生命周期   

Vue 实例有⼀个完整的⽣命周期，也就是从开始创建、初始化数据、编译模版、挂载Dom -> 渲染、更新 -> 渲染、卸载 等⼀系列过程，称这是Vue的⽣命周期。 

1. **beforeCreate（创建前）**：数据观测和初始化事件还未开始，此时 data 的响应式追踪、event/watcher 都还没有被设置，也就是说不能访问到data、computed、watch、methods上的方法和数据。
2. **created（创建后）** ：实例创建完成，实例上配置的 options 包括 data、computed、watch、methods 等都配置完成，但是此时渲染得节点还未挂载到 DOM，所以不能访问到 `$el` 属性。
3. **beforeMount（挂载前）**：在挂载开始之前被调用，相关的render函数首次被调用。实例已完成以下的配置：编译模板，把data里面的数据和模板生成html。此时还没有挂载html到页面上。
4. **mounted（挂载后）**：在el被新创建的 vm.$el 替换，并挂载到实例上去之后调用。实例已完成以下的配置：用上面编译好的html内容替换el属性指向的DOM对象。完成模板中的html渲染到html 页面中。此过程中进行ajax交互。
5. **beforeUpdate（更新前）**：响应式数据更新时调用，此时虽然响应式数据更新了，但是对应的真实 DOM 还没有被渲染。
6. **updated（更新后）** ：在由于数据更改导致的虚拟DOM重新渲染和打补丁之后调用。此时 DOM 已经根据响应式数据的变化更新了。调用时，组件 DOM已经更新，所以可以执行依赖于DOM的操作。然而在大多数情况下，应该避免在此期间更改状态，因为这可能会导致更新无限循环。该钩子在服务器端渲染期间不被调用。
7. **beforeDestroy（销毁前）**：实例销毁之前调用。这一步，实例仍然完全可用，`this` 仍能获取到实例。
8. **destroyed（销毁后）**：实例销毁后调用，调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。该钩子在服务端渲染期间不被调用。

另外还有 `keep-alive` 独有的生命周期，分别为 `activated` 和 `deactivated` 。用 `keep-alive` 包裹的组件在切换时不会进行销毁，而是缓存到内存中并执行 `deactivated` 钩子函数，命中缓存渲染后会执行 `activated` 钩子函数。

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h82hnpqa4pj30u017ah1f.jpg)

### 2. ==Vue子组件和父组件执行顺序==

**加载渲染过程：**

1. 父组件 beforeCreate

2. 父组件 created

3. 父组件 beforeMount

4. 子组件 beforeCreate

5. 子组件 created

6. 子组件 beforeMount

7. 子组件 mounted

8. 父组件 mounted

**更新过程：**

1. 父组件 beforeUpdate

2.  子组件 beforeUpdate

3. 子组件 updated

4. 父组件 updated

**销毁过程：**

1. 父组件 beforeDestroy

2. 子组件 beforeDestroy

3. 子组件 destroyed

4. 父组件 destoryed

### 3. created和mounted的区别

- created: 在模板渲染成html前调用，即通常初始化某些属性值，然后再渲染成视图。
- mounted: 在模板渲染成html后调用，通常是初始化页面完成后，再对html的dom节点进行一些需要的操作。

### 4. 一般在哪个生命周期请求异步数据

我们可以在钩子函数==created==、==beforeMount==、==mounted== 中进行调用，因为在这三个钩子函数中，data 已经创建，可以将服务端端返回的数据进行赋值。

推荐在 created 钩子函数中调用异步请求，因为在 created 钩子函数中调用异步请求有以下优点：

- 能更快获取到服务端数据，减少页面加载时间，用户体验更好；
- SSR不支持 beforeMount 、mounted 钩子函数，放在 created 中有助于一致性。

放在`mounted`中的请求有可能导致页面闪动（因为此时页面`dom`结构已经生成），但如果在页面加载前完成请求，则不会出现此情况。建议对页面内容的改动放在`created`生命周期当中。

### 5. keep-alive中的生命周期哪些

keep-alive是 Vue 提供的一个内置组件，用来对组件进行缓存——在组件切换过程中将状态保留在内存中，防止重复渲染DOM。

如果为一个组件包裹了 keep-alive，那么它会多出两个生命周期：deactivated、activated。同时，beforeDestroy 和 destroyed 就不会再被触发了，因为组件不会被真正销毁。

当组件被换掉时，会被缓存到内存中、触发 deactivated 生命周期；当组件被切回来时，再去缓存里找这个组件、触发 activated钩子函数。

### 6. Vue实例挂载的过程中发生了什么?

- `new Vue`的时候调用会调用`_init`方法
  - 定义 `$set`、`$get` 、`$delete`、`$watch` 等方法
  - 定义 `$on`、`$off`、`$emit`、`$off`等事件
  - 定义 `_update`、`$forceUpdate`、`$destroy`生命周期
- 调用`$mount`进行页面的挂载
- 挂载的时候主要是通过`mountComponent`方法
- 定义`updateComponent`更新函数
- 执行`render`生成虚拟`DOM`
- `_update`将虚拟`DOM`生成真实`DOM`结构，并且渲染到页面中

## 三、组件通信

### 总结

1. **父子组件间通信**
   - `props`  / `$emit` : 子组件通过 props 属性来接受父组件的数据，然后父组件在子组件上注册监听事件，子组件通过 emit 触发事件来向父组件发送数据。
   - `ref` / `$refs` : 通过 ref 属性给子组件设置一个名字。父组件通过 $refs 组件名来获得子组件，子组件通过 $parent 获得父组件，这样也可以实现通信。
   - 依赖注入(`project` / `inject`) : 使用 provide/inject，在父组件中通过 provide提供变量，在子组件中通过 inject 来将变量注入到组件中。不论子组件有多深，只要调用了 inject 那么就可以注入 provide中的数据。
   - `$attrs / $listeners`
2. **兄弟组件间通信**
   - eventBus：它的本质是通过创建一个空的 Vue 实例来作为消息传递的对象，通信的组件引入这个实例，通信的组件通过在这个实例上监听和触发事件，来实现消息的传递。
   - 通过 `$parent`/`$refs` 来获取到兄弟组件，也可以进行通信。
3. **任意组件之间/子孙组件**
   - 使用 eventBus ，其实就是创建一个事件中心，相当于中转站，可以用它来传递事件和接收事件。
   - 依赖注入(`project` / `inject`) : 使用 provide/inject，在父组件中通过 provide提供变量，在子组件中通过 inject 来将变量注入到组件中。不论子组件有多深，只要调用了 inject 那么就可以注入 provide中的数据。
   - `$attrs / $listeners`

如果业务逻辑复杂，很多组件之间需要同时处理一些公共的数据，这个时候采用上面这一些方法可能不利于项目的维护。这个时候可以使用 vuex ，vuex 的思想就是将这一些公共的数据抽离出来，将它作为一个全局的变量来管理，然后其他组件就可以对这个公共数据进行读写操作，这样达到了解耦的目的。

### 1. `props`  / `$emit`

父组件通过`props`向子组件传递数据，子组件通过`$emit`和父组件通信

#### 1. 父组件向子组件传值

- `props`只能是父组件向子组件进行传值，`props`使得父子组件之间形成了一个单向下行绑定。子组件的数据会随着父组件不断更新。
- `props` 可以显示定义一个或一个以上的数据，对于接收的数据，可以是各种数据类型，同样也可以传递一个函数。
- `props`属性名规则：若在`props`中使用驼峰形式，模板中需要使用短横线的形式

```vue
// 父组件
<template>
  <div id="father">
    <son :msg="msgData" :fn="myFunction"></son>
  </div>
</template>

<script>
import son from "./son.vue";
export default {
  name: father,
  data() {
    msgData: "父组件数据";
  },
  methods: {
    myFunction() {
      console.log("vue");
    }
  },
  components: {
    son
  }
};
</script>
```

```vue
// 子组件
<template>
  <div id="son">
    <p>{{msg}}</p>
    <button @click="fn">按钮</button>
  </div>
</template>

<script>
export default {
  name: "son",
  props: ["msg", "fn"]
};
</script>
```

#### 2. 子组件向父组件传值

- `$emit`绑定一个自定义事件，当这个事件被执行的时就会将参数传递给父组件，而父组件通过`v-on`监听并接收参数。

```vue
// 父组件
<template>
  <div class="section">
    <com-article :articles="articleList" @onEmitIndex="onEmitIndex"></com-article>
    <p>{{currentIndex}}</p>
  </div>
</template>

<script>
import comArticle from "./test/article.vue";
export default {
  name: "comArticle",
  components: { comArticle },
  data() {
    return {
      currentIndex: -1,
      articleList: ["红楼梦", "西游记", "三国演义"]
    };
  },
  methods: {
    onEmitIndex(idx) {
      this.currentIndex = idx;
    }
  }
};
</script>
```

```vue
// 子组件
<template>
  <div>
    <div v-for="(item, index) in articles" :key="index" @click="emitIndex(index)">{{item}}</div>
  </div>
</template>

<script>
export default {
  props: ["articles"],
  methods: {
    emitIndex(index) {
      this.$emit("onEmitIndex", index); // 触发父组件的方法，并传递参数index
    }
  }
};
</script>
```

### 2. eventBus (`$emit` / `$on`) 

`eventBus`事件总线适用于**父子组件**、**非父子件**之间的通信。

代码中，这就相当于将`num`值存贮在了事件总线中，在其他组件中可以直接访问。事件总线就相当于一个桥梁，不用组件通过它来通信。

虽然看起来比较简单，但是这种方法也有不变之处，如果项目过大，使用这种方式进行通信，后期维护起来会很困难。

**（1）创建事件中心管理组件之间的通信**

```js
// event-bus.js

import Vue from 'vue'
export const EventBus = new Vue()
```

**（2）发送事件**

假设有两个兄弟组件`firstCom`和`secondCom`：

```vue
<template>
  <div>
    <first-com></first-com>
    <second-com></second-com>
  </div>
</template>

<script>
import firstCom from './firstCom.vue'
import secondCom from './secondCom.vue'
export default {
  components: { firstCom, secondCom }
}
</script>
```

在`firstCom`组件中发送事件：

```vue
<template>
  <div>
    <button @click="add">加法</button>    
  </div>
</template>

<script>
import { EventBus } from './event-bus.js' // 引入事件中心

export default {
  data() {
    return {
      num: 0
    };
  },
  methods: {
    add() {
      EventBus.$emit("addition", {
        num: this.num++
      });
    }
  }
};
</script>
```

**（3）接收事件**

在`secondCom`组件中发送事件：

```vue
<template>
  <div>求和: {{count}}</div>
</template>

<script>
import { EventBus } from './event-bus.js'
export default {
  data() {
    return {
      count: 0
    };
  },
  mounted() {
    EventBus.$on("addition", (param) => {
      this.count = this.count + param.num;
    });
  }
};
</script>
```

### 3. 依赖注入(`project` / `inject`)

==**注意：** 依赖注入所提供的属性是**非响应式**的。==

这种方式就是Vue中的**依赖注入**，该方法用于**父子组件之间的通信**。当然这里所说的父子不一定是真正的父子，也可以是祖孙组件，在层数很深的情况下，可以使用这种方法来进行传值。就不用一层一层的传递了。

`project / inject`是Vue提供的两个钩子，和`data`、`methods`是同级的。并且`project`的书写形式和`data`一样。

- `project` 钩子用来发送数据或方法
- `inject` 钩子用来接收数据或方法

```js
provide() {
 return {
    num: this.num
  };
}
```

```js
inject: ['num']
```

```js
provide() {
 return {
    app: this
  };
}
data() {
 return {
    num: 1
  };
}

inject: ['app']
console.log(this.app.num)
```

### 4. `ref` / `$refs`

`ref`： 这个属性用在子组件上，它的引用就指向了子组件的实例。可以通过实例来访问组件的数据和方法。

```js
// 在子组件中：
export default {
  data () {
    return {
      name: 'JavaScript'
    }
  },
  methods: {
    sayHello () {
      console.log('hello')
    }
  }
}
```

```vue
// 在父组件中：
<template>
  <child ref="child"></child>
</template>
<script>
  import child from './child.vue'
  export default {
    components: { child },
    mounted () {
      console.log(this.$refs.child.name);  // JavaScript
      this.$refs.child.sayHello();  // hello
    }
  }
</script>
```

### 5. `$parent` / `$children`

- 使用`$parent`可以让组件访问父组件的实例（访问的是上一级父组件的属性和方法）
- 使用`$children`可以让组件访问子组件的实例，但是，==`$children`并不能保证顺序，并且访问的数据也不是响应式的==。

```vue
// 在子组件中：
<template>
  <div>
    <span>{{message}}</span>
    <p>获取父组件的值为:  {{parentVal}}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Vue'
    }
  },
  computed:{
    parentVal(){
      return this.$parent.msg;
    }
  }
}
</script>
```

```vue
// 父组件中
<template>
  <div class="hello_world">
    <div>{{msg}}</div>
    <child></child>
    <button @click="change">点击改变子组件值</button>
  </div>
</template>

<script>
import child from './child.vue'
export default {
  components: { child },
  data() {
    return {
      msg: 'Welcome'
    }
  },
  methods: {
    change() {
      // 获取到子组件
      this.$children[0].message = 'JavaScript'
    }
  }
}
</script>
```

在上面的代码中，子组件获取到了父组件的`parentVal`值，父组件改变了子组件中`message`的值。

**需要注意：**

- 通过`$parent`访问到的是上一级父组件的实例，可以使用`$root`来访问根组件的实例
- 在组件中使用`$children`拿到的是所有的子组件的实例，它是一个数组，并且是无序的
- 在根组件`#app`上拿`$parent`得到的是`new Vue()`的实例，在这实例上再拿`$parent`得到的是`undefined`，而在最底层的子组件拿`$children`是个空数组
- `$children` 的值是**数组**，而`$parent`是个**对象**

### 6. ==`$attrs` / `$listeners`==

考虑一种场景，如果A是B组件的父组件，B是C组件的父组件。如果想要组件A给组件C传递数据，这种隔代的数据，该使用哪种方式呢？

如果是用`props/$emit`来一级一级的传递，确实可以完成，但是比较复杂；如果使用事件总线，在多人开发或者项目较大的时候，维护起来很麻烦；如果使用Vuex，的确也可以，但是如果仅仅是传递数据，那可能就有点浪费了。

针对上述情况，Vue引入了`$attrs / $listeners`，实现组件之间的跨代通信。

先来看一下`inheritAttrs`，它的默认值true，继承所有的父组件属性除`props`之外的所有属性；`inheritAttrs：false` 只继承class属性 。

- `$attrs`：继承所有的父组件属性（除了prop传递的属性、class 和 style ），一般用在子组件的子元素上
- `$listeners`：该属性是一个对象，里面包含了作用在这个组件上的所有监听器，可以配合 `v-on="$listeners"` 将所有的事件监听器指向这个组件的某个特定的子元素。（相当于子组件继承父组件的事件）

```vue
// A组件（APP.vue）：
<template>
	<div id="app">
  	//此处监听了两个事件，可以在B组件或者C组件中直接触发
  	<child1 :p-child1="child1" :p-child2="child2" @test1="onTest1" @test2="onTest2"></child1>
	</div>
</template>

<script>
import Child1 from "./Child1.vue";
export default {
  components: { Child1 },
  methods: {
    onTest1() {
      console.log("test1 running");
    },
    onTest2() {
      console.log("test2 running");
    }
  }
};
</script>
```

```vue
// B组件（Child1.vue）：
<template>
  <div class="child-1">
    <p>props: {{pChild1}}</p>
    <p>$attrs: {{$attrs}}</p>
    <child2 v-bind="$attrs" v-on="$listeners"></child2>
  </div>
</template>

<script>
import Child2 from "./Child2.vue";
export default {
  props: ["pChild1"],
  components: { Child2 },
  inheritAttrs: false,
  mounted() {
    this.$emit("test1"); // 触发APP.vue中的test1方法
  }
};

</script>
```

```vue
// C 组件 (Child2.vue)：
<template>
  <div class="child-2">
    <p>props: {{pChild2}}</p>
    <p>$attrs: {{$attrs}}</p>
  </div>
</template>
<script>
export default {
  props: ["pChild2"],
  inheritAttrs: false,
  mounted() {
    this.$emit("test2"); // 触发APP.vue中的test2方法
  }
};
</script>
```

在上述代码中：

- C组件中能直接触发test的原因在于 B组件调用C组件时 使用 v-on 绑定了`$listeners` 属性
- 在B组件中通过v-bind 绑定`$attrs`属性，C组件可以直接获取到A组件中传递下来的props（除了B组件中props声明的）

### 7. vueX

## 四、路由

### 1. Vue-Router 的懒加载如何实现

```js
// 非懒加载
import List from '@/components/list.vue'
const router = new VueRouter({
  routes: [
    { path: '/list', component: List }
  ]
})
```

1. **方案一(常用)：使用箭头函数+import动态加载**

```js
const List = () => import('@/components/list.vue')
const router = new VueRouter({
  routes: [
    { path: '/list', component: List }
  ]
})
```

2. **方案二：使用箭头函数+require动态加载**

```js
const router = new Router({
  routes: [
   {
     path: '/list',
     component: resolve => require(['@/components/list'], resolve)
   }
  ]
})
```

3. **方案三：使用webpack的require.ensure技术，也可以实现按需加载。 这种情况下，多个路由指定相同的chunkName，会合并打包成一个js文件。**

```js
// r就是resolve
const List = r => require.ensure([], () => r(require('@/components/list')), 'list');
// 路由也是正常的写法  这种是官方推荐的写的 按模块划分懒加载 
const router = new Router({
  routes: [
  {
    path: '/list',
    component: List,
    name: 'list'
  }
 ]
}))
```

### 2. 路由的hash和history模式的区别

Vue-Router有两种模式：**hash模式**和**history模式**。默认的路由模式是hash模式。

#### 1. hash模式

**简介：** hash模式是开发中默认的模式，它的URL带着一个#，例如：http://www.abc.com/#/vue，它的hash值就是`#/vue`。

**特点**：hash值会出现在URL里面，但是不会出现在HTTP请求中，对后端完全没有影响。所以改变hash值，不会重新加载页面。这种模式的浏览器支持度很好，低版本的IE浏览器也支持这种模式。hash路由被称为是前端路由，已经成为SPA（单页面应用）的标配。

**原理：** hash模式的主要原理就是**onhashchange()事件**：

```js
window.onhashchange = function(event){
	console.log(event.oldURL, event.newURL);
	let hash = location.hash.slice(1);
}
```

使用onhashchange()事件的好处就是，在页面的hash值发生变化时，无需向后端发起请求，window就可以监听事件的改变，并按规则加载相应的代码。除此之外，hash值变化对应的URL都会被浏览器记录下来，这样浏览器就能实现页面的前进和后退。虽然是没有请求后端服务器，但是页面的hash值和对应的URL关联起来了。

#### 2. history模式

**简介：** history模式的URL中没有#，它使用的是传统的路由分发模式，即用户在输入一个URL时，服务器会接收这个请求，并解析这个URL，然后做出相应的逻辑处理。

**特点：** 当使用history模式时，URL就像这样：http://abc.com/user/id。相比hash模式更加好看。但是，history模式需要后台配置支持。如果后台没有正确配置，访问时会返回404。

**API：** history api可以分为两大部分，切换历史状态和修改历史状态：

- **修改历史状态**：包括了 HTML5 History Interface 中新增的 `pushState()` 和 `replaceState()` 方法，这两个方法应用于浏览器的历史记录栈，提供了对历史记录进行修改的功能。只是当他们进行修改时，虽然修改了url，但浏览器不会立即向后端发送请求。如果要做到改变url但又不刷新页面的效果，就需要前端用上这两个API。
- **切换历史状态：** 包括`forward()`、`back()`、`go()`三个方法，对应浏览器的前进，后退，跳转操作。

虽然history模式丢弃了丑陋的#。但是，它也有自己的缺点，就是在刷新页面的时候，如果没有相应的路由或资源，就会刷出404来。

如果想要切换到history模式，就要进行以下配置（后端也要进行配置）：

```js
const router = new VueRouter({
  mode: 'history',
  routes: [...]
})
```

#### 3. 两种模式对比
调用 history.pushState() 相比于直接修改 hash，存在以下优势:

1. pushState() 设置的新 URL 可以是与当前 URL 同源的任意 URL；而 hash 只可修改 # 后面的部分，因此只能设置与当前 URL 同文档的 URL；
2. pushState() 设置的新 URL 可以与当前 URL 一模一样，这样也会把记录添加到栈中；而 hash 设置的新值必须与原来不一样才会触发动作将记录添加到栈中；
3. pushState() 通过 stateObject 参数可以添加任意类型的数据到记录中；而 hash 只可添加短字符串；
4. pushState() 可额外设置 title 属性供后续使用。
5. hash模式下，仅hash符号之前的url会被包含在请求中，后端如果没有做到对路由的全覆盖，也不会返回404错误；history模式下，前端的url必须和实际向后端发起请求的url一致，如果没有对用的路由处理，将返回404错误。

hash模式和history模式都有各自的优势和缺陷，还是要根据实际情况选择性的使用。

### 3. 如何获取页面的hash变化

1. **监听$route的变化**

   ```js
   // 监听,当路由发生变化的时候执行
   watch: {
     $route: {
       handler: function(val, oldVal){
         console.log(val);
       },
       // 深度观察监听
       deep: true
     }
   },
   ```

2. **window.location.hash读取#值**

   window.location.hash 的值可读可写，读取来判断状态是否改变，写入时可以在不重载网页的前提下，添加一条历史访问记录。

### 4. `$route` 和 `$router` 的区别

**| `this.$route`**：当前激活的路由的信息对象。每个对象都是局部的，可以获取当前路由的 path, name, params, query 等属性。

**| `this.$router`**：全局的 router 实例。通过 vue 根实例中注入 router 实例，然后再注入到每个子组件，从而让整个应用都有路由功能。其中包含了很多属性和对象（比如 history 对象），任何页面也都可以调用其 push(), replace(), go() 等方法。

1. `$route` 是“路由信息对象”，包括 path，params，hash，query，fullPath，matched，name 等路由信息参数
2. `$router` 是“路由实例”对象包括了路由的跳转方法，钩子函数等。

### 5. 如何定义动态路由?如何获取传过来的动态参数?

1. **param方式**
   - 配置路由格式：`/router/:id`
   - 传递的方式：在path后面跟上对应的值
   - 传递后形成的路径：`/router/123`

```vue
// 1、 param路由定义
//在APP.vue中
<router-link :to="'/user/'+userId" replace>用户</router-link>    

// 在index.js
{
   path: '/user/:userid',
   component: User,
},

// 2、param路由跳转
// 方法1：
<router-link :to="{ name: 'users', params: { uname: wade }}">按钮</router-link>

// 方法2：
this.$router.push({name:'users',params:{uname:wade}})

// 方法3：
this.$router.push('/user/' + wade)

// 3、param参数获取
通过 $route.params.userid 获取传递的值
```

2. **query方式**
   - 配置路由格式：`/router`，也就是普通配置
   - 传递的方式：对象中使用query的key作为传递方式
   - 传递后形成的路径：`/route?id=123`

1）query路由定义

```js
//方式1：直接在router-link 标签上以对象的形式
<router-link :to="{path:'/profile',query:{name:'why',age:28,height:188}}">档案</router-link>

// 方式2：写成按钮以点击事件形式
<button @click='profileClick'>我的</button>    

profileClick(){
  this.$router.push({
    path: "/profile",
    query: {
        name: "kobi",
        age: "28",
        height: 198
    }
  });
}
```

2）query路由跳转

```js
// 方法1：
<router-link :to="{ name: 'users', query: { uname: james }}">按钮</router-link>

// 方法2：
this.$router.push({ name: 'users', query:{ uname:james }})

// 方法3：
<router-link :to="{ path: '/user', query: { uname:james }}">按钮</router-link>

// 方法4：
this.$router.push({ path: '/user', query:{ uname:james }})

// 方法5：
this.$router.push('/user?uname=' + jsmes)
```

3）query参数获取

通过`$route.query`获取传递的值

### 6. ==Vue-router路由钩子在生命周期的体现==

#### A、Vue-Router导航守卫

有的时候，需要通过路由来进行一些操作，比如最常见的登录权限验证，当用户满足条件时，才让其进入导航，否则就取消跳转，并跳到登录页面让其登录。为此有很多种方法可以植入路由的导航过程：全局的，单个路由独享的，或者组件级的。

##### 1. 全局路由钩子

全局有三个路由钩子：

- `router.beforeEach`全局前置守卫 进入路由之前

- `router.beforeResolve` 全局解析守卫（2.5.0+）在 beforeRouteEnter 调用之后调用

- `router.afterEach` 全局后置钩子 进入路由之后

具体使用∶

1. beforeEach（判断是否登录了，没登录就跳转到登录页）

2. afterEach（跳转之后滚动条回到顶部）

```js
router.beforeEach((to, from, next) => {
  let ifInfo = Vue.prototype.$common.getSession("userData"); // 判断是否登录的存储信息
  if (!ifInfo) {
    // sessionStorage里没有储存user信息
    if (to.path == "/") {
      //如果是登录页面路径，就直接next()
      next();
    } else {
      //不然就跳转到登录
      Message.warning("请重新登录！");
      window.location.href = Vue.prototype.$loginUrl;
    }
  } else {
    return next();
  }
});

```

```js
router.afterEach((to, from) => {
  // 跳转之后滚动条回到顶部
  window.scrollTo(0, 0);
});
```

##### 2. 单个路由独享钩子

**beforeEnter**

如果不想全局配置守卫的话，可以为某些路由单独配置守卫，有三个参数∶ to、from、next

```js
export default [
  {
    path: "/",
    name: "login",
    component: login,
    beforeEnter: (to, from, next) => {
      console.log("即将进入登录页面");
      next();
    }
  }
];

```

##### 3. 组件内钩子

`beforeRouteUpdate`、`beforeRouteEnter`、`beforeRouteLeave`

这三个钩子都有三个参数∶to、from、next

- beforeRouteEnter∶ 进入组件前触发
- beforeRouteUpdate∶ 当前地址改变并且改组件被复用时触发，举例来说，带有动态参数的路径foo/∶id，在 /foo/1 和 /foo/2 之间跳转的时候，由于会渲染同样的foa组件，这个钩子在这种情况下就会被调用
- beforeRouteLeave∶ 离开组件被调用

注意点，`beforeRouteEnter`组件内还访问不到this，因为该守卫执行前组件实例还没有被创建，需要传一个回调给 `next` 来访问，例如：

```js
beforeRouteEnter(to, from, next) {      
  next(target => {        
      if (from.path == '/classProcess') {          
          target.isFromProcess = true        
      }      
  })    
}
```

#### B、==Vue路由钩子在生命周期函数的体现==

1. 完整的路由导航解析流程（不包括其他生命周期）

- 触发进入其他路由。
- 调用要离开路由的组件守卫beforeRouteLeave
- 调用局前置守卫∶ beforeEach
- 在重用的组件里调用 beforeRouteUpdate
- 调用路由独享守卫 beforeEnter。
- 解析异步路由组件。
- 在将要进入的路由组件中调用 beforeRouteEnter
- 调用全局解析守卫 beforeResolve
- 导航被确认。
- 调用全局后置钩子的 afterEach 钩子。
- 触发DOM更新（mounted）。
- 执行beforeRouteEnter 守卫中传给 next 的回调函数

2. 触发钩子的完整顺序

路由导航、keep-alive、和组件生命周期钩子结合起来的，触发顺序，假设是从a组件离开，第一次进入b组件∶

- beforeRouteLeave：路由组件的组件离开路由前钩子，可取消路由离开。
- beforeEach：路由全局前置守卫，可用于登录验证、全局路由loading等。
- beforeEnter：路由独享守卫
- beforeRouteEnter：路由组件的组件进入路由前钩子。
- beforeResolve：路由全局解析守卫
- afterEach：路由全局后置钩子
- beforeCreate：组件生命周期，不能访问tAis。
- created;组件生命周期，可以访问tAis，不能访问dom。
- beforeMount：组件生命周期
- deactivated：离开缓存组件a，或者触发a的beforeDestroy和destroyed组件销毁钩子。
- mounted：访问/操作dom。
- activated：进入缓存组件，进入a的嵌套子组件（如果有的话）。
- 执行beforeRouteEnter回调函数next。

3. 导航行为被触发到导航完成的整个过程

- 导航行为被触发，此时导航未被确认。
- 在失活的组件里调用离开守卫 beforeRouteLeave。
- 调用全局的 beforeEach守卫。
- 在重用的组件里调用 beforeRouteUpdate 守卫(2.2+)。
- 在路由配置里调用 beforeEnteY。 
- 解析异步路由组件（如果有）。
- 在被激活的组件里调用 beforeRouteEnter。
- 调用全局的 beforeResolve 守卫（2.5+），标示解析阶段完成。
- 导航被确认。
- 调用全局的 afterEach 钩子。
- 非重用组件，开始组件实例的生命周期：beforeCreate&created、beforeMount&mounted
- 触发 DOM 更新。
- 用创建好的实例调用 beforeRouteEnter守卫中传给 next 的回调函数。
- 导航完成

### 7. Vue-router跳转和location.href有什么区别

- 使用 `location.href= /url `来跳转，简单方便，但是刷新了页面；
- 使用 `history.pushState( /url )` ，无刷新页面，静态跳转；
- 引进 router ，然后使用 `router.push( /url )` 来跳转，使用了 `diff` 算法，实现了按需加载，减少了 dom 的消耗。其实使用 router 跳转和使用 `history.pushState()` 没什么差别的，因为vue-router就是用了 `history.pushState()` ，尤其是在history模式下。

### 8. params和query的区别

**用法**：query要用path来引入，params要用name来引入，接收参数都是类似的，分别是 `this.$route.query.name` 和 `this.$route.params.name` 。

**url地址显示**：query更加类似于ajax中get传参，params则类似于post，说的再简单一点，前者在浏览器地址栏中显示参数，后者则不显示

**注意**：query刷新不会丢失query里面的数据 params刷新会丢失 params里面的数据。

### 9. Vue-router导航守卫有哪些

- 全局前置/钩子：beforeEach、beforeResolve、afterEach
- 路由独享的守卫：beforeEnter
- 组件内的守卫：beforeRouteEnter、beforeRouteUpdate、beforeRouteLeave

### 10. ⚡️对前端路由的理解

在前端技术早期，一个 url 对应一个页面，如果要从 A 页面切换到 B 页面，那么必然伴随着页面的刷新。这个体验并不好，不过在最初也是无奈之举——用户只有在刷新页面的情况下，才可以重新去请求数据。

后来，改变发生了——Ajax 出现了，它允许人们在不刷新页面的情况下发起请求；与之共生的，还有“不刷新页面即可更新页面内容”这种需求。在这样的背景下，出现了 **SPA（单页面应用**）。

SPA极大地提升了用户体验，它允许页面在不刷新的情况下更新页面内容，使内容的切换更加流畅。但是在 SPA 诞生之初，人们并没有考虑到“定位”这个问题——在内容切换前后，页面的 URL 都是一样的，这就带来了两个问题：

- SPA 其实并不知道当前的页面“进展到了哪一步”。可能在一个站点下经过了反复的“前进”才终于唤出了某一块内容，但是此时只要刷新一下页面，一切就会被清零，必须重复之前的操作、才可以重新对内容进行定位——SPA 并不会“记住”你的操作。
- 由于有且仅有一个 URL 给页面做映射，这对 SEO 也不够友好，搜索引擎无法收集全面的信息

为了解决这个问题，前端路由出现了。

前端路由可以帮助我们在仅有一个页面的情况下，“记住”用户当前走到了哪一步——为 SPA 中的各个视图匹配一个唯一标识。这意味着用户前进、后退触发的新内容，都会映射到不同的 URL 上去。此时即便他刷新页面，因为当前的 URL 可以标识出他所处的位置，因此内容也不会丢失。

那么如何实现这个目的呢？首先要解决两个问题：

- 当用户刷新页面时，浏览器会默认根据当前 URL 对资源进行重新定位（发送请求）。这个动作对 SPA 是不必要的，因为我们的 SPA 作为单页面，无论如何也只会有一个资源与之对应。此时若走正常的请求-刷新流程，反而会使用户的前进后退操作无法被记录。
- 单页面应用对服务端来说，就是一个URL、一套资源，那么如何做到用“不同的URL”来映射不同的视图内容呢？

从这两个问题来看，服务端已经完全救不了这个场景了。所以要靠咱们前端自力更生，不然怎么叫“前端路由”呢？作为前端，可以提供这样的解决思路：

- 拦截用户的刷新操作，避免服务端盲目响应、返回不符合预期的资源内容。把刷新这个动作完全放到前端逻辑里消化掉。
- 感知 URL 的变化。这里不是说要改造 URL、凭空制造出 N 个 URL 来。而是说 URL 还是那个 URL，只不过我们可以给它做一些微小的处理——这些处理并不会影响 URL 本身的性质，不会影响服务器对它的识别，只有我们前端感知的到。一旦我们感知到了，我们就根据这些变化、用 JS 去给它生成不同的内容。

## 五、VueX

### 1. Vuex的原理

Vuex为Vue Components建立起了一个完整的生态圈，包括开发中的API调用一环。 

**（1）核心流程中的主要功能：**

- Vue Components 是 vue 组件，组件会触发（dispatch）一些事件或动作，也就是图中的 Actions;
- 在组件中发出的动作，肯定是想获取或者改变数据的，但是在 vuex 中，数据是集中管理的，不能直接去更改数据，所以会把这个动作提交（Commit）到 Mutations 中;
- 然后 Mutations 就去改变（Mutate）State 中的数据;
- 当 State 中的数据被改变之后，就会重新渲染（Render）到 Vue Components 中去，组件展示更新后的数据，完成一个流程。

**（2）各模块在核心流程中的主要功能：**

- `Vue Components`∶ Vue组件。HTML页面上，负责接收用户操作等交互行为，执行dispatch方法触发对应action进行回应。
- `dispatch`∶操作行为触发方法，是唯一能执行action的方法。
- `actions`∶ 操作行为处理模块。负责处理Vue Components接收到的所有交互行为。包含同步/异步操作，支持多个同名方法，按照注册的顺序依次触发。向后台API请求的操作就在这个模块中进行，包括触发其他action以及提交mutation的操作。该模块提供了Promise的封装，以支持action的链式触发。
- `commit`∶状态改变提交操作方法。对mutation进行提交，是唯一能执行mutation的方法。
- `mutations`∶状态改变操作方法。是Vuex修改state的唯一推荐方法，其他修改方式在严格模式下将会报错。该方法只能进行同步操作，且方法名只能全局唯一。操作之中会有一些hook暴露出来，以进行state的监控等。
- `state`∶ 页面状态管理容器对象。集中存储Vuecomponents中data对象的零散数据，全局唯一，以进行统一的状态管理。页面显示所需的数据从该对象中进行读取，利用Vue的细粒度数据响应机制来进行高效的状态更新。
- `getters`∶ state对象读取方法。图中没有单独列出该模块，应该被包含在了render中，Vue Components通过该方法读取全局state对象。

**总结：**

Vuex 实现了一个单向数据流，在全局拥有一个 State 存放数据，当组件要更改 State 中的数据时，必须通过 Mutation 提交修改信息， Mutation 同时提供了订阅者模式供外部插件调用获取 State 数据的更新。而当所有异步操作(常见于调用后端接口异步获取更新数据)或批量的同步操作需要走 Action ，但 Action 也是无法直接修改 State 的，还是需要通过Mutation 来修改State的数据。最后，根据 State 的变化，渲染到视图上。   

![vuex2.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gu5tw21u1bj61nx1acwn002.jpg)

### 2. Vuex中action和mutation的区别

**mutation中的操作是一系列的==同步函数==，用于修改state中的变量的的状态。**

当使用vuex时需要通过commit来提交需要操作的内容。mutation 非常类似于事件：每个 mutation 都有一个字符串的事件类型 (type) 和 一个回调函数 (handler)。这个回调函数就是实际进行状态更改的地方，并且它会接受 state 作为第一个参数。

```js
const store = new Vuex.Store({
  state: {
    count: 1
  },
  mutations: {
    increment(state) {
      state.count++; // 变更状态
    }
  }
});

// 当触发一个类型为 increment 的 mutation 时，需要调用此函数：
store.commit('increment')
```

**而Action类似于mutation，不同点在于：**

- Action 可以包含任意==异步操作==。
- Action 提交的是 mutation，而不是直接变更状态。

```js
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    increment(context) {
      context.commit("increment");
    }
  }
});
```

Action 函数接受一个与 store 实例具有相同方法和属性的 context 对象，因此你可以调用 context.commit 提交一个 mutation，或者通过 context.state 和 context.getters 来获取 state 和 getters。

所以，两者的不同点如下：

- Mutation专注于修改State，理论上是修改State的唯一途径；Action业务代码、异步请求。
- Mutation：必须同步执行；Action：可以异步，但不能直接操作State。
- 在视图更新时，先触发actions，actions再触发mutation
- mutation的参数是state，它包含store中的数据；store的参数是context，它是 state 的父级，包含 state、getters

### 3. Vuex和localStorage的区别

   存储的方式(内存，文件)，数据响应，永久性

**（1）最重要的区别**

- vuex存储在内存中
- localstorage 则以文件的方式存储在本地，只能存储字符串类型的数据，存储对象需要JSON的stringify和parse方法进行处理。 读取内存比读取硬盘速度要快

**（2）应用场景**

- Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。vuex用于组件之间的传值。
- localstorage是本地存储，是将数据存储到浏览器的方法，一般是在跨页面传递数据时使用 。
- Vuex能做到数据的响应式，localstorage不能

**（3）永久性**

刷新页面时vuex存储的值会丢失，localstorage不会。

**注意：**对于不变的数据确实可以用localstorage可以代替vuex，但是当两个组件共用一个数据源（对象或数组）时，如果其中一个组件改变了该数据源，希望另一个组件响应该变化时，localstorage无法做到，原因就是区别1。

### 4. Redux和Vuex有什么区别，它们的共同思想

**（1）Redux 和 Vuex区别**

- Vuex改进了Redux中的Action和Reducer函数，以mutations变化函数取代Reducer，无需switch，只需在对应的mutation函数里改变state值即可
- Vuex由于Vue自动重新渲染的特性，无需订阅重新渲染函数，只要生成新的State即可
- Vuex数据流的顺序是∶View调用store.commit提交对应的请求到Store中对应的mutation函数->store改变（vue检测到数据变化自动渲染）

通俗点理解就是，vuex 弱化 dispatch，通过commit进行 store状态的一次更变;取消了action概念，不必传入特定的 action形式进行指定变更;弱化reducer，基于commit参数直接对数据进行转变，使得框架更加简易; 

**（2）共同思想**

- 单—的数据源 
- 变化可以预测

本质上：redux与vuex都是对mvvm思想的服务，将数据从视图中抽离的一种方案;

形式上：vuex借鉴了redux，将store作为全局的数据中心，进行mode管理;

### 5. 为什么要用Vuex或者Redux

由于传参的方法对于多层嵌套的组件将会非常繁琐，并且对于兄弟组件间的状态传递无能为力。我们经常会采用父子组件直接引用或者通过事件来变更和同步状态的多份拷贝。以上的这些模式非常脆弱，通常会导致代码无法维护。

所以需要把组件的共享状态抽取出来，以一个全局单例模式管理。在这种模式下，组件树构成了一个巨大的"视图"，不管在树的哪个位置，任何组件都能获取状态或者触发行为。

另外，通过定义和隔离状态管理中的各种概念并强制遵守一定的规则，代码将会变得更结构化且易维护。

### 6. Vuex有哪几种属性? 

有五种，分别是 State、 Getter、Mutation 、Action、 Module

1. state => 基本数据(数据源存放地)
2. getters => 从基本数据派生出来的数据
3. mutations => 提交更改数据的方法，同步
4. actions => 像一个装饰器，包裹mutations，使之可以异步。
5. modules => 模块化Vuex

### 7. Vuex和单纯的全局对象有什么区别?

   响应式，不能直接更新对应状态

- Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。
- 不能直接改变 store 中的状态。改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样可以方便地跟踪每一个状态的变化，从而能够实现一些工具帮助更好地了解我们的应用。

### 8. 为什么Vuex的mutation中不能做异步操作？

  - Vuex中所有的状态更新的唯一途径都是mutation，异步操作通过 Action 来提交 mutation实现，这样可以**方便地跟踪每一个状态的变化**，从而能够实现一些工具帮助更好地了解我们的应用。
- 每个mutation执行完成后都会对应到一个新的状态变更，这样devtools就可以打个快照存下来，然后就可以实现 time-travel 了。如果mutation支持异步操作，就没有办法知道状态是何时更新的，无法很好的进行状态的追踪，给调试带来困难。

### 9. Vuex的严格模式是什么，有什么作用，如何开启？

在严格模式下，无论何时发生了状态变更且不是由mutation函数引起的，将会抛出错误。这能保证所有的状态变更都能被调试工具跟踪到。

在Vuex.Store 构造器选项中开启,如下:

```js
const store = new Vuex.Store({
    strict:true,
})
```

### 10. ==如何在组件中批量使用Vuex的getter属性==

使用mapGetters辅助函数, 利用对象展开运算符将getter混入computed 对象中

```js
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["total", "discountTotal"])
  }
};
```

### 11. ==如何在组件中重复使用Vuex的mutation==

使用mapMutations辅助函数,在组件中这么使用，然后调用`this.setNumber(10)`相当调用`this.$store.commit('SET_NUMBER',10)`

```js
import { mapMutations } from 'vuex'
methods:{
  ...mapMutations({
      setNumber:'SET_NUMBER',
  })
}
```

## 六、Vue 3.0

### 1. Vue3.0有什么更新

   [link](https://vue3js.cn/interview/vue/vue3_vue2.html#%E4%BA%8C%E3%80%81vue3%E6%96%B0%E5%A2%9E%E7%89%B9%E6%80%A7)

   更小更快(优化)更友好（ts,composition api,开放更多底层功能）+响应性

**（1）监测机制的改变**

- 3.0 将带来基于代理 Proxy的 observer 实现，提供全语言覆盖的反应性跟踪。
- 消除了 Vue 2 当中基于 Object.defineProperty 的实现所存在的很多限制：

**（2）只能监测属性，不能监测对象**

- 检测属性的添加和删除；
- 检测数组索引和长度的变更；
- 支持 Map、Set、WeakMap 和 WeakSet。

**（3）模板**

- 作用域插槽，2.x 的机制导致作用域插槽变了，父组件会重新渲染，而 3.0 把作用域插槽改成了函数的方式，这样只会影响子组件的重新渲染，提升了渲染的性能。
- 同时，对于 render 函数的方面，vue3.0 也会进行一系列更改来方便习惯直接使用 api 来生成 vdom 。

**（4）对象式的组件声明方式**

- vue2.x 中的组件是通过声明的方式传入一系列 option，和 TypeScript 的结合需要通过一些装饰器的方式来做，虽然能实现功能，但是比较麻烦。
- 3.0 修改了组件的声明方式，改成了类式的写法，这样使得和 TypeScript 的结合变得很容易

**（5）其它方面的更改**

- 支持自定义渲染器，从而使得 weex 可以通过自定义渲染器的方式来扩展，而不是直接 fork 源码来改的方式。
- 支持 Fragment（多个根节点）和 Protal（在 dom 其他部分渲染组建内容）组件，针对一些特殊的场景做了处理。
- 基于 tree shaking 优化，提供了更多的内置功能。

### 2. defineProperty和proxy的区别

Vue 在实例初始化时遍历 data 中的所有属性，并使用 Object.defineProperty 把这些属性全部转为 getter/setter。这样当追踪数据发生变化时，setter 会被自动调用。

Object.defineProperty 是 ES5 中一个无法 shim 的特性，这也就是 Vue 不支持 IE8 以及更低版本浏览器的原因。

但是这样做有以下问题：

1. 添加或删除对象的属性时，Vue 检测不到。因为添加或删除的对象没有在初始化进行响应式处理，只能通过`$set` 来调用`Object.defineProperty()`处理。
2. 无法监控到数组下标和长度的变化。

Vue3 使用 Proxy 来监控数据的变化。Proxy 是 ES6 中提供的功能，其作用为：用于定义基本操作的自定义行为（如属性查找，赋值，枚举，函数调用等）。==相对于`Object.defineProperty()`，其有以下特点==：

1. Proxy 直接代理整个对象而非对象属性，这样只需做一层代理就可以监听同级结构下的所有属性变化，包括新增属性和删除属性。
2. Proxy 可以监听数组的变化。

### 3. Vue3.0为什么要用proxy?

1. 可以提高实例初始化启动速度，优化数据响应式系统，由全部监听改为惰性监听（lazy by default)。
2. 数据响应式系统全语言特性支持，添加数组索引修改监听，对象的属性增加和删除。

在 Vue2 中， 0bject.defineProperty 会改变原始数据，而 Proxy 是创建对象的虚拟表示，并提供 set 、get 和 deleteProperty 等处理器，这些处理器可在访问或修改原始对象上的属性时进行拦截，有以下特点∶

- 不需用使用 `Vue.$set` 或 `Vue.$delete` 触发响应式。
- 全方位的数组变化检测，消除了Vue2 无效的边界情况。
- 支持 Map，Set，WeakMap 和 WeakSet。

 Proxy 实现的响应式原理与 Vue2的实现原理相同，实现方式大同小异∶ 

- get 收集依赖
- Set、delete 等触发依赖
- 对于集合类型，就是对集合对象的方法做一层包装：原方法执行后执行依赖相关的收集或触发逻辑。

### 4. Vue 3.0中的Vue Composition API?

在 Vue2 中，代码是 Options API 风格的，也就是通过填充 (option) data、methods、computed 等属性来完成一个 Vue 组件。这种风格使得 Vue 相对于 React极为容易上手，同时也造成了几个问题：

1. 由于 Options API 不够灵活的开发方式，使得Vue开发缺乏优雅的方法来在组件间共用代码。
2. Vue 组件过于依赖`this`上下文，Vue 背后的一些小技巧使得 Vue 组件的开发看起来与 JavaScript 的开发原则相悖，比如在`methods` 中的`this`竟然指向组件实例来不指向`methods`所在的对象。这也使得 TypeScript 在Vue2 中很不好用。

于是在 Vue3 中，舍弃了 Options API，转而投向 Composition API。Composition API本质上是将 Options API 背后的机制暴露给用户直接使用，这样用户就拥有了更多的灵活性，也使得 Vue3 更适合于 TypeScript 结合。

Vue Composition API 使得 Vue3 的开发风格更接近于原生 JavaScript，带给开发者更多地灵活性。

   - 逻辑组织
   - 逻辑复用
   - 在逻辑组织和逻辑复用方面，`Composition API`是优于`Options API`
   - 因为`Composition API`几乎是函数，会有更好的类型推断。
   - `Composition API`对 `tree-shaking` 友好，代码也更容易压缩
   - `Composition API`中见不到`this`的使用，减少了`this`指向不明的情况
   - 如果是小型组件，可以继续使用`Options API`，也是十分友好的

### 5. Composition API与 React Hook很像，区别是什么？

从React Hook的实现角度看，React Hook是根据useState调用的顺序来确定下一次重渲染时的state是来源于哪个useState，所以出现了以下限制

- 不能在循环、条件、嵌套函数中调用Hook
- 必须确保总是在你的React函数的顶层调用Hook
- useEffect、useMemo等函数必须手动确定依赖关系

而Composition API是基于Vue的响应式系统实现的，与React Hook的相比

- 声明在setup函数内，一次组件实例化只调用一次setup，而React Hook每次重渲染都需要调用Hook，使得React的GC比Vue更有压力，性能也相对于Vue来说也较慢
- Compositon API的调用不需要顾虑调用顺序，也可以在循环、条件、嵌套函数中使用
- 响应式系统自动实现了依赖收集，进而组件的部分的性能优化由Vue内部自己完成，而React Hook需要手动传入依赖，而且必须必须保证依赖的顺序，让useEffect、useMemo等函数正确的捕获依赖变量，否则会由于依赖不正确使得组件性能下降。

虽然Compositon API看起来比React Hook好用，但是其设计思想也是借鉴React Hook的。

### 6. Vue3.0性能提升主要是通过哪几方面体现的？

https://vue3js.cn/interview/vue3/performance.html#%E4%B8%80%E3%80%81%E7%BC%96%E8%AF%91%E9%98%B6%E6%AE%B5

### 7. Vue 3.0中Treeshaking特性？举例说明一下?

https://vue3js.cn/interview/vue3/treeshaking.html#%E4%BA%8C%E3%80%81%E5%A6%82%E4%BD%95%E5%81%9A

## 七、虚拟DOM

### 1. 对虚拟DOM的理解?

从本质上来说，Virtual Dom是一个JavaScript对象，通过对象的方式来表示DOM结构。将页面的状态抽象为JS对象的形式，配合不同的渲染工具，使跨平台渲染成为可能。通过事务处理机制，将多次DOM修改的结果一次性的更新到页面上，从而有效的减少页面渲染的次数，减少修改DOM的重绘重排次数，提高渲染性能。

虚拟DOM是对DOM的抽象，这个对象是更加轻量级的对 DOM的描述。它设计的最初目的，就是更好的跨平台，比如Node.js就没有DOM，如果想实现SSR，那么一个方式就是借助虚拟DOM，因为虚拟DOM本身是js对象。 在代码渲染到页面之前，vue会把代码转换成一个对象（虚拟 DOM）。以对象的形式来描述真实DOM结构，最终渲染到页面。在每次数据发生变化前，虚拟DOM都会缓存一份，变化之时，现在的虚拟DOM会与缓存的虚拟DOM进行比较。在vue内部封装了diff算法，通过这个算法来进行比较，渲染时修改改变的变化，原先没有发生改变的通过原先的数据进行渲染。

另外现代前端框架的一个基本要求就是无须手动操作DOM，一方面是因为手动操作DOM无法保证程序性能，多人协作的项目中如果review不严格，可能会有开发者写出性能较低的代码，另一方面更重要的是省略手动DOM操作可以大大提高开发效率。

### 2. 虚拟DOM的解析过程

- 首先对将要插入到文档中的 DOM 树结构进行分析，使用 js 对象将其表示出来，比如一个元素对象，包含 TagName、props 和 Children 这些属性。然后将这个 js 对象树给保存下来，最后再将 DOM 片段插入到文档中。
- 当页面的状态发生改变，需要对页面的 DOM 的结构进行调整的时候，首先根据变更的状态，重新构建起一棵对象树，然后将这棵新的对象树和旧的对象树进行比较，记录下两棵树的的差异。
- 最后将记录的有差异的地方应用到真正的 DOM 树中去，这样视图就更新了。

### 3. 为什么要用虚拟DOM

   - 虚拟 DOM 最大的优势1----是 diff 算法，减少 JavaScript 操作真实 DOM 的带来的性能消耗。

   - 虚拟 DOM 最大的优势2----在于抽象了原本的渲染过程，实现了跨平台的能力，而不仅仅局限于浏览器的 DOM，可以是安卓和 IOS 的原生组件，可以是近期很火热的小程序，也可以是各种GUI

**（1）保证性能下限，在不进行手动优化的情况下，提供过得去的性能**

看一下页面渲染的流程：解析HTML -> 生成DOM -> 生成 CSSOM -> Layout -> Paint -> Compiler
下面对比一下修改DOM时真实DOM操作和Virtual DOM的过程，来看一下它们重排重绘的性能消耗∶

1. 真实DOM∶ 生成HTML字符串＋重建所有的DOM元素
2. 虚拟DOM∶ 生成vNode+ DOMDiff＋必要的dom更新

Virtual DOM的更新DOM的准备工作耗费更多的时间，也就是JS层面，相比于更多的DOM操作它的消费是极其便宜的。尤雨溪在社区论坛中说道∶ 框架给你的保证是，你不需要手动优化的情况下，依然可以给你提供过得去的性能。

**（2）跨平台**

Virtual DOM本质上是JavaScript的对象，它可以很方便的跨平台操作，比如服务端渲染、uniapp等。

### 4. 虚拟DOM真的比真实DOM性能好吗

- 首次渲染大量DOM时，由于多了一层虚拟DOM的计算，会比innerHTML插入慢。
- 正如它能保证性能下限，在真实DOM操作的时候进行针对性的优化时，还是更快的。

### 5. ==vue - DIFF算法的原理==

`diff` 算法是一种通过同层的树节点进行比较的高效算法

`diff`整体策略为：深度优先，同层比较

其有两个特点：

- 比较只会在同层级进行, 不会跨层级比较
- 在diff比较的过程中，循环从两边向中间比较

`diff` 算法在很多场景下都有应用，在 `vue` 中，作用于虚拟 `dom` 渲染成真实 `dom` 的新旧 `VNode` 节点比较

   - 当数据发生改变时，订阅者`watcher`就会调用`patch`给真实的`DOM`打补丁

   - 通过`isSameVnode`进行判断，相同则调用`patchVnode`方法

     patchVnode做了以下操作：

     - 找到对应的真实`dom`，称为`el`
     - 如果都有都有文本节点且不相等，将`el`文本节点设置为`Vnode`的文本节点
     - 如果`oldVnode`有子节点而`VNode`没有，则删除`el`子节点
     - 如果`oldVnode`没有子节点而`VNode`有，则将`VNode`的子节点真实化后添加到`el`
     - 如果两者都有子节点，则执行`updateChildren`函数比较子节点

     updateChildren主要做了以下操作：

     - 设置新旧`VNode`的头尾指针
     - 新旧头尾指针进行比较，循环向中间靠拢，根据情况调用`patchVnode`进行`patch`重复流程、调用`createElem`创建一个新节点，从哈希表寻找 `key`一致的`VNode` 节点再分情况操作

-----------

在新老虚拟DOM对比时：

- 首先，对比节点本身，判断是否为同一节点，如果不为相同节点，则删除该节点重新创建节点进行替换
- 如果为相同节点，进行patchVnode，判断如何对该节点的子节点进行处理，先判断一方有子节点一方没有子节点的情况(如果新的children没有子节点，将旧的子节点移除)
- 比较如果都有子节点，则进行updateChildren，判断如何对这些新老节点的子节点进行操作（diff核心）。
- 匹配时，找到相同的子节点，递归比较子节点

在diff中，只对同层的子节点进行比较，放弃跨级的节点比较，使得时间复杂从O(n3)降低值O(n)，也就是说，只有当新旧children都为多个子节点时才需要用核心的Diff算法进行同层级比较。

### 6. Vue中key的作用

diff 算法需要比对虚拟 dom 的修改，然后异步的渲染到页面中，当出现大量相同的标签时，vnode 会首先判断 key 和标签名是否一致，如果一致再去判断子节点一致，使用 key 可以帮助 diff 算法提升判断的速度，在页面重新渲染时更快消耗更少。

   > key是给每一个vnode的唯一id，也是diff的一种优化策略，可以根据key，更准确， 更快的找到对应的vnode节点

key 是为 Vue 中 vnode 的唯一标记，通过这个 key，diff 操作可以更准确、更快速

1. 更准确：因为带 key 就不是就地复用了，在 sameNode 函数a.key === b.key对比中可以避免就地复用的情况。所以会更加准确。
2. 更快速：利用 key 的唯一性生成 map 对象来获取对应节点，比遍历方式更快

### 7. 为什么不建议用index作为key?

因为不管数组的顺序怎么颠倒，index 都是 0, 1, 2...这样排列，导致 Vue 会复用错误的旧子节点，做很多额外的工作。

导致的问题就是以前的数据和重新渲染后的数据随着 key 值的变化从而没法建立关联关系，这就失去了 key 值存在的意义

# 三、React

### 简单介绍react

- 单项数据流
- diff算法
- 不操作真实DOM

React是Facebook开发的一款JS库,React不是一个MVC框架，它是构建易于可重复调用的web组件，侧重于UI, 也就是view层

其次React是==单向的从数据到视图的渲染，非双向数据绑定==

不直接操作DOM对象，而是通过虚拟DOM进行==diff算法==以最小的步骤作用到真实的DOM上。

不直接操作DOM，大多数时间只是对 virtual DOM 进行编程

### 单项数据流

单向数据流这种模式十分适合跟 React 搭配使用。它的主要思想是组件不会改变接收的数据。它们只会监听数据的变化，当数据发生变化时它们会使用接收到的新值，而不是去修改已有的值。当组件的更新机制触发后，它们只是使用新值进行重新渲染而已。

## 一、✨组件基础

### 1. React事件机制

是 `React`模拟原生 `DOM`事件所有能力的一个事件对象。即浏览器原生事件的跨浏览器包装器。举例onClick,事件没有绑定在真实DOM上，而是通过事件代理，绑定在最外层。减少内存消耗，组件卸载销毁的时候统一订阅和移除事件。（阻止事件发生不能用stopPropogation,而是要用prevent default ）

- 阻止合成事件间的冒泡，用e.stopPropagation()
- 阻止合成事件与最外层 document 上的事件间的冒泡，用e.nativeEvent.stopImmediatePropagation()
- 阻止合成事件与除最外层document上的原生事件上的冒泡，通过判断e.target来避免

### 2. React的事件和普通的HTML事件有什么不同。

   命名方式，事件阻止方式

### 3. React组件中怎么做事件代理?它的原理是什么？

   事件冒泡，绑定到root上(17.0.0版本)

   原理：1. 事件委派 2. 自动绑定

   - 事件委派：React会把所有的事件绑定到结构的最外层，使用统一的事件监听器，这个事件监听器上维持了一个映射来保存所有组件内部事件监听和处理函数。 

   - 自动绑定：React组件中，每个方法的上下文都会指向该组件的实例，即自动绑定this为当前组件。

### 4. React高阶组件、Render props、hooks有什么区别，为什么不断迭代？

### 5. 对React-Fiber的理解，它解决了什么问题？

[github interview](https://vue3js.cn/interview/React/Fiber.html#三、如何解决)

 `JavaScript`引擎和页面渲染引擎两个线程是互斥的，js线程长时间占用主线程，渲染层会不断等待，会造成用户界面卡顿。

### 6. React.Component和React.PureComponent的区别。

   PureComponent表示一个纯组件，会自动调用shouldComponentUpdate,这个生命周期进行的是浅比较，当组件更新时，如果组件的props或者state都没有改变，render函数就不会触发。省去虚拟DOM的生成和对比过程，达到提升性能的目的。可以用来优化React程序，减少render函数执行的次数，从而提高组件的性能。

### 7. Component, Element, Instance之间的区别和联系

### 8. React.createClass和extends Component的区别?

   1. 语法区别

      ```jsx
      import React from 'react';
      
      const Contacts = React.createClass({  
        render() {
          return (
            <div></div>
          );
        }
      });
      
      export default Contacts;  
      ```

      ```jsx
      import React from 'react';
      
      class Contacts extends React.Component {  
        constructor(props) {
          super(props);
        }
        render() {
          return (
            <div></div>
          );
        }
      }
      
      export default Contacts;  
      ```

      

   2. propType 和 getDefaultProps,propType/defaultProps

   3. this区别,React.createClass会绑定class，而extends不会

      

### 9. React高阶组件是什么，和普通组件的区别，适用什么场景？

在`React`中，高阶组件即接受一个或多个组件作为参数并且返回一个组件，本质也就是一个函数，并不是一个组件。



在实际应用中，常常用于与核心业务无关但又在多个模块使用的功能，如权限控制、日志记录、数据校验、异常处理、统计上报等

### 10. 对componentWillReceiveProps的理解

    在这个生命周期中，可以在子组件的render函数执行前获取新的props，从而更新子组件自己的state。

### 11. 哪些方法会触发React重新渲染?

   - setState(),传入null的时候不会触发render
   - 父组件重新渲染

### 12. React如何判断什么时候重新渲染组件？

   - 类组件调用 setState 修改状态（一定会重新渲染）
   - 函数组件通过`useState hook`修改状态(不一定，根据数组是否进行监听判断)
   - `useState` 会判断当前值有无发生改变确定是否执行`render`方法，一旦父组件发生渲染，子组件也会渲染

### 13. React声明组件有哪几种方法，有什么不同？

   函数式，es6类式，es5原生createClass

   This，props，hooks

### 14. 对有状态组件和无状态组件的理解及使用场景

### 15. 对React中Fragment的理解，它的使用场景

### 16. React如何获取组件对应的DOM元素?

    Ref,createRef，
    
    `<p ref="info">span</p>`
    
    `<p ref={ele => this.info = ele}></p>`
    
    ref 16之前的版本字符串方式或者函数式
    
    createRef 16的版本

### 17. React中可以在render访问refs吗?为什么？

不可以，render 阶段 DOM 还没有生成，无法获取 DOM。DOM 的获取需要在 pre-commit 阶段和 commit 阶段。

### 18. 对React的插槽(Portals)的理解，如何使用，有哪些使用场景？

### 19. 在React中如何避免不必要的render?

   - shouldComponentUpdate

   - PureComponent

   - React.memo:用来缓存组件的渲染，避免不必要的更新，其实也是一个高阶组件，与 `PureComponent` 十分类似。但不同的是， `React.memo` 只能用于函数组件

     ```jsx
     const Funcomponent = ()=> {
         return (
             <div>
                 Hiya!! I am a Funtional component
             </div>
         )
     }
     const MemodFuncComponent = React.memo(Funcomponent)
     ```

### 20. 对React-Intl的理解，它的工作原理

### 21. 对React context的理解

Context 提供了一种在组件之间共享此类值的方式，而不必显式地通过组件树的逐层传递 props。

### 22. 为什么React并不推荐优先考虑使用context

### 23. React中什么是受控组件和非控组件?应用场景？

   - 受控组件，简单来讲，就是受我们控制的组件，组件的状态全程响应外部数据。组件添加value值和onChange事件

   - 非受控组件，简单来讲，就是不受我们控制的组件。一般情况是在初始化的时候接受外部数据，然后自己在内部存储其自身状态。通过ref获取数据

   ![](https://static.vue-js.com/f28aed20-df2f-11eb-ab90-d9ae814b240d.png)

### 24. React中refs的作用是什么?有哪些应用场景？

 Refs 提供了一种方式，用于访问在 render 方法中创建的 React 元素或 DOM 节点。过多使用`refs`，会使组件的实例或者是`DOM`结构暴露，违反组件封装的原则

   但下面的场景使用`refs`非常有用：

   - 对Dom元素的焦点控制、内容选择、控制
   - 对Dom元素的内容设置及媒体播放
   - 对Dom元素的操作和对组件实例的操作
   - 集成第三方 DOM 库
   - 用于获取当前节点最新的值

### 25. React中除了在构造函数中绑定this，还有别的方式吗？

### 26. React组件的构造函数有什么作用?

   - 通过将对象分配给this.state来初始化本地状态

   - 将事件处理程序方法绑定到实例上

### 27. React.forwardRef是什么?它有什么作用？

 React.forwardRef 会创建一个React组件，这个组件能够将其接受的 ref 属性转发到其组件树下的另一个组件中。

   - 转发 refs 到 DOM 组件 
   - 在高阶组件中转发 refs

### 28. 类组件与函数组件有什么异同?

### 29. 说说React Jsx转换成真实DOM过程？

### 30. React事件绑定的方式有哪些？区别？

### 31. React构建组件的方式有哪些？区别？

## 二、✨数据管理

### 1. React setState调用的原理

   关于`state`方法的定义是从`React.Component`中继承，定义的源码如下：

   ```js
   Component.prototype.setState = function(partialState, callback) {
     invariant(
       typeof partialState === 'object' ||
         typeof partialState === 'function' ||
         partialState == null,
       'setState(...): takes an object of state variables to update or a ' +
         'function which returns an object of state variables.',
     );
     this.updater.enqueueSetState(this, partialState, callback, 'setState');
   };
   ```

### 2. React setState调用之后发生了什么?是同步还是异步？

1. 当每次 setState 时，组件会重新渲染
2. 当在函数式组件中 setState 时，如果两次设置的 state 相同时，组件将不会重新渲染
3. 当在事件处理函数中，多次调用 setState，React 将会批量进行渲染
4. 当在事件处理函数外，多次调用 setState，React 将不会重新渲染
5. 在 React18 之后，同一函数多次调用 setState，React 都将会批量进行渲染

   - 在组件生命周期或React合成事件中，setState是异步

     因为react可以控制。

   - 在setTimeout或者原生dom事件中，setState是同步，因为react无法控制原生事件。

### 3. React中的setState批量更新的过程是什么？

   放入队列，合成一次，即使多次触发，只保留最后一次的更新

### 4. React中有使用过getDefaultProps吗？它有什么作用？

   通过实现组件的getDefaultProps，对属性设置默认值（ES5的写法

### 5. React中setState的第二个参数作用是什么？

### 6. React中的setState和replaceState的区别是什么？

 1. 参数都相同
 2. 用法不同⬇️

  - setState 是修改其中的部分状态，相当于 Object.assign，只是覆盖，不会减少原来的状态。
  - replaceState 是完全替换原来的状态，相当于赋值，将原来的 state 替换为另一个对象，如果新状态属性减少，那么 state 中就没有这个状态了。

### 7. 在React中组件的this. state和setState/useState()有什么区别？

  初始化状态和修改状态

![image-20210907162638708.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l07v04ulj31go0w2tks.jpg)

### 8. state是怎么注入到组件的，从reducer到组件经历了什么样的过程？

  通过connect和mapStateToProps将state注入到组件中。

### 9. React组件的state和props有什么区别?

  相同点：

  - 两者都是 JavaScript 对象
  - 两者都是用于保存信息
  - props 和 state 都能触发渲染更新

  区别：

  - props 是外部传递给组件的，而 state 是在组件内被组件自己管理的，一般在 constructor 中初始化
  - props 在组件内部是不可修改的，但 state 在组件内部可以进行修改
  - state 是多变的、可以修改

### 10. React中的props为什么是只读的?

    this.props就是汲取了纯函数的思想。props的不可以变性就保证的相同的输入，页面显示的内容是一样的，并且不会产生副作用

### 11. 在React中组件的props改变时更新组件有哪些方法？

getDerivedStateFromProps

componentWillReceiveProps

### 12. React中怎么检验props?验证props的目的是什么？

### 13. state 和 props有什么区别？

### 14. super()和super(props)有什么区别？

### 15. 说说React中的setState执行机制


## 三、✨生命周期

### 1. React的生命周期有哪些?

   ![](https://cdn.nlark.com/yuque/0/2021/png/1500604/1611914193870-a5a93315-a094-40aa-959a-e3e3c58c8a96.png)

![image-20210906144816223.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l08g6kesj310a0lg0we.jpg)

   ![image-20210907110123380.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l08rj395j31bw0o27b4.jpg)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/791da7c43d3c4f45862f909ce38c882c~tplv-k3u1fbpfcp-watermark.awebp)   

React常见生命周期的过程大致如下： 

   1. 挂载阶段，首先执行constructor构造方法，来创建组件
   2. 创建完成之后，就会执行render方法，该方法会返回需要渲染的内容 
   3. 随后，React会将需要渲染的内容挂载到DOM树上 
   4.  挂载完成之后就会执行componentDidMount生命周期函数
   5. 如果我们给组件创建一个props（用于组件通信）、调用setState（更改state中的数据）、调用forceUpdate（强制更新组件）时，都会重新调用render函数 
   6. render函数重新执行之后，就会重新进行DOM树的挂载
   7. 挂载完成之后就会执行componentDidUpdate生命周期函数 
   8. 当移除组件时，就会执行componentWillUnmount生命周期函数

### 2. React废弃了哪些生命周期?为什么?

   - componentWillMount
   - componentWillReceiveProps
   - componentWillUpdate

   被废弃的三个函数都是在render之前，因为fiber的出现，很可能因为高优先级任务的出现而打断现有任务导致它们会被执行多次。

### 3. getDerivedStateFromProps React 16.X中props改变后在哪个生命周期中处理？

   在getDerivedStateFromProps中进行处理。

第二种场景是一些组件需要在用户输入时有一个中间状态，当触发某个操作时再把中间结果提交给上层。以一个 `input`为例，在过去我们通过 `componentWillReceiveProps`在上层组件触发重绘时把数据同步到 `state`：

   ```js
   static getDerivedStateFromProps(nextProps, prevState) {
       const {type} = nextProps;
       // 当传入的type发生变化的时候，更新state
       if (type !== prevState.type) {
           return {
               type,
           };
       }
       // 否则，对于state不进行任何操作
       return null;
   }
   ```

### 4. React性能优化在哪个生命周期?优化的原理是什么？

shouldComponentUpdate提供了两个参数nextProps和nextState，表示下一次props和下一次state的值，当函数返回false时候，render()方法不执行，组件也就不会渲染，返回true时，组件照常重渲染。此方法就是拿当前props中值和下一次props中的值进行对比，数据相等时，返回false，反之返回true。

需要注意，在进行新旧对比的时候，是浅对比，也就是说如果比较的数据时引用数据类型，只要数据的引用的地址没变，即使内容变了，也会被判定为true。

   ```js
   shouldComponentUpdate(nexrProps) {
       if (this.props.num === nexrProps.num) {
           return false
       }
       return true;
   }
   ```

### 5. state和props触发更新的生命周期分别有什么区别？

### 6. React中发起网络请求应该在哪个生命周期中进行？为什么？

   componentwillMount->会执行两次，服务端，客户端

   componentDidMount

   componentDidMount方法中的代码，是在组件已经完全挂载到网页上才会调用被执行，所以可以保证数据的加载。此外，在这方法中调用setState方法，会触发重新渲染。所以，官方设计这个方法就是用来加载外部数据用的，或处理其他的副作用代码。与组件上的数据无关的加载，也可以在constructor里做，但constructor是做组件state初绐化工作，并不是做加载数据这工作的，constructor里也不能setState，还有加载的时间太长或者出错，页面就无法加载出来。所以有副作用的代码都会集中在componentDidMount方法里。

### 7. React 16中新生命周期有哪些

   1. React16新的生命周期弃用了componentWillMount、componentWillReceiveProps，componentWillUpdate
   2. 新增了getDerivedStateFromProps、getSnapshotBeforeUpdate来代替弃用的三个钩子函数（componentWillMount、componentWillReceiveProps，componentWillUpdate）
   3. React16并没有删除这三个钩子函数，但是不能和新增的钩子函数（getDerivedStateFromProps、getSnapshotBeforeUpdate）混用，React17将会删除componentWillMount、componentWillReceiveProps，componentWillUpdate
   4. 新增了对错误的处理（componentDidCatch）

   

## 四、✨组件通信

### 1. 父子组件的通信方式?

props/事件触发

### 2. 跨级组件的通信方式?

   Context,redux/mobx,props

### 3. 非嵌套关系组件的通信方式?

   Subscribe, redux/mobx,通过共同的父节点

### 4. 如何解决props层级过深的问题

   使用contextApi,redux/mobx

### 5. 组件通信的方式有哪些

⽗组件向⼦组件通讯: ⽗组件可以向⼦组件通过传 props 的⽅式，向⼦组件进⾏通讯 

● ⼦组件向⽗组件通讯: props+回调的⽅式，⽗组件向⼦组件传递props进⾏通讯，此props为作⽤域为⽗组件⾃身的函 数，⼦组件调⽤该函数，将⼦组件想要传递的信息，作为参数，传递到⽗组件的作⽤域中 

● 兄弟组件通信: 找到这两个兄弟节点共同的⽗节点,结合上⾯两种⽅式由⽗节点转发信息进⾏通信 

● 跨层级通信: Context 设计⽬的是为了共享那些对于⼀个组件树⽽⾔是“全局”的数据，例如当前认证的⽤户、主题或⾸选语⾔，对于跨越多层的全局数据通过 Context 通信再适合不过 

● 发布订阅模式: 发布者发布事件，订阅者监听事件并做出反应,我们可以通过引⼊event模块进⾏通信 

● 全局状态管理⼯具: 借助Redux或者Mobx等全局状态管理⼯具进⾏通信,这种⼯具会维护⼀个全局状态中⼼Store,并根据不同的事件产⽣新的状态

## 五、路由 Router

### 1. React- Router的实现原理是什么?
### 2. 如何配置React- Router实现路由切换
### 3. React-Router怎么设置重定向?
### 4. react-router里的Link标签和a标签.
### 5. React-Router如何获取URL的参数和...
### 6. React- Router 4怎样在路由变化时重...
### 7. React-Router的路由有几种模式?
### 8. React- Router 4的Switch有什么用? 

### 9. 说说React Router有几种模式？实现原理？

## 六、✨Redux 

<img src="http://ww1.sinaimg.cn/large/005NUwyggy1gt4z7z98z3j60zk0k078s02.jpg" alt="redux原理图.png" style="zoom:33%;" />

### 1. 对Redux的理解，主要解决什么问题

单纯的Redux只是一个状态机，是没有UI呈现的，react- redux作用是将Redux的状态机和React的UI呈现绑定在一起，当你dispatch action改变state的时候，会自动更新页面。

### 2. Redux原理及工作流程

   - 首先，用户（通过View）发出Action，触发方式就用到了dispatch方法 

   - 然后，Store自动调用Reducer，并且传入两个参数：当前State和收到的Action，Reducer会返回新的State 

   - State—旦有变化，Store就会调用监听函数，来更新View

### 3. Redux中异步的请求怎么处理

   使用redux-thunk,redux-saga

### 4. Redux怎么实现属性传递，介绍下原理   ![image-20210906140838237.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l096xpdrj30y20aqwhh.jpg)

### 5. Redux中间件是什么?接受几个参数?柯里化函数两端的参数具体是什么？

   - redux-thunk：用于异步操作

   - redux-logger：用于日志记录

     Redux 的中间件提供的是位于 action 被发起之后，到达 reducer 之前的扩展点，换而言之，原本 view -> action -> reducer -> store 的数据流加上中间件后变成了 view -> action -> middleware -> reducer -> store ，在这一环节可以做一些"副作用"的操作，如异步请求、打印日志等。

### 6. Redux请求中间件如何处理并发

### 7. Redux状态管理器和变量挂载到winddow中有什么区别？

   两者都是存储数据以供后期使用。但是Redux状态更改可回溯——Time travel，数据多了的时候可以很清晰的知道改动在哪里发生，完整的提供了一套状态管理模式。

### 8. mobx和redux有什么区别?

   共同点：

   1. 为了解决状态管理混乱
   2. 操作更新状态方式统一
   3. 支持将store与react组件连接

   区别：

   1. redux将数据保存在单一的store中，mobx将数据保存在分散的多个store中
   2. mobx中有更多的抽象和封装，调试会比较困难，同时结果也难以预测;而redux提供能够进行时间回溯的开发工具，同时其纯函数以及更少的抽象，让调试变得更加的容易
   3. redux使用不可变状态，这意味着状态是只读的，不能直接去修改它，而是应该返回一个新的状态，同时使用纯函数;mobx中的状态是可变的，可以直接对其进行修改

9. Redux和Vuex有什么区别，它们的共同思想

   vuex 弱化 dispatch，通过commit进行 store状态的一次更变；取消了action概念，不必传入特定的 action形式进行指定变更；弱化reducer，基于commit参数直接对数据进行转变，使得框架更加简易;

   redux与vuex都是对mvvm思想的服务，将数据从视图中抽离的一种方案

### 10. Redux中间件是怎么拿到store和action?然后怎么处理？

![image-20210906142540730.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l09klkdxj310m0b00xy.jpg)

### 11. Redux中的connect有什么作用

connect负责连接React和Redux，可以获取整个store tree上的所有state，可以监听store tree的变化。

### 12. 在 redux 中如何发送请求

### 13. 在 redux 中如何写一个记录状态变更的日志插

### 14. 项目结构中redux是如何划分的？

#### 按角色组织（MVC）

```markdown
reducers/
  todoReducer.js
  filterReducer.js
actions/
  todoAction.js
  filterActions.js
components/
  todoList.js
  todoItem.js
  filter.js
containers/
  todoListContainer.js
  todoItemContainer.js
  filterContainer.js
```

角色如下：

- reducers
- actions
- components
- containers

#### 按功能组织

```markdown
todoList/
  actions.js
  actionTypes.js
  index.js
  reducer.js
  views/
    components.js
    containers.js
filter/
  actions.js
  actionTypes.js
  index.js
  reducer.js
  views/
    components.js
    container.js
```

### 15.说说对Redux中间件的理解？常用的中间件有哪些？实现原理？

### 16. 说说你对Redux的理解？其工作原理？

1. 遵循三大基本原则

- 单一数据源
- state 是只读的
- 使用纯函数来执行修改

## 七、✨Hooks

### 1. 对React Hook的理解，它的实现原理是什么？

   Hook是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。通过自定义hook，可以复用代码逻辑。

   `Hook` 是 React 16.8 的新增特性。它可以让你在不编写 `class` 的情况下使用 `state` 以及其他的 `React` 特性，在以前，函数组件也被称为无状态的组件，只负责渲染的一些工作。因此，现在的函数组件也可以是有状态的组件，内部也可以维护自身的状态以及做一些逻辑方面的处理。

Hooks 主要是利用闭包来保存状态，使用链表保存一系列Hooks，将链表中的第一个Hook与Fiber 关联。

   - useState

   - useEffect

   - useReducer

   - useCallback

   - useMemo

   - useRef


### 2. 为什么useState要使用数组而不是对象

   useState 返回的是 array 而不是 object 的原因就是为了降低使用的复杂度，返回数组的话可以直接根据顺序解构，而返回对象的话要想使用多次就需要定义别名了。

### 3. React Hooks解决了哪些问题?

   1. 可以使用 Hook 从组件中提取状态逻辑，使得这些逻辑可以单独测试并复用。
   2. `hooks`能够更容易解决状态相关的重用的问题

通过对上面的初步认识，可以看到`hooks`能够更容易解决状态相关的重用的问题：

   - 每调用useHook一次都会生成一份独立的状态
   - 通过自定义hook能够更好的封装我们的功能

编写`hooks`为函数式编程，每个功能都包裹在函数中，整体风格更清爽，更优雅

hooks`的出现，使函数组件的功能得到了扩充，拥有了类组件相似的功能，在我们日常使用中，使用`hooks`能够解决大多数问题，并且还拥有代码复用机制，因此优先考虑`hooks

### 4. React Hook的使用限制有哪些?

   1. 不要在循环、条件或嵌套函数中调用 Hook；

   2. 在 React 的函数组件中调用 Hook。

### 5. useEffect与useLayoutEffect的区别

      1. 都是处理副作用的
      2. useEffect 在 React 的渲染过程中是被异步调用的，用于绝大多数场景；而 useLayoutEffect 会在所有的 DOM 变更之后同步调用，主要用于处理 DOM 操作、调整样式、避免页面闪烁等问题。
      3. useLayoutEffect 和 componentDidMount 和 componentDidUpdate 触发时机一致（都在在 DOM 修改后且浏览器渲染之前）；
   4. useLayoutEffect 要比 useEffect 更早的触发执行；
   5. useLayoutEffect 会阻塞浏览器渲染，切记执行同步的耗时操作

### 6. React Hooks在平时开发中需要注意的

   1. 不要在循环，条件或嵌套函数中调用Hook，必须始终在 React函数的顶层使用Hook

   2. 使用useState时候，使用push，pop，splice等直接更改数组对象的坑

   3. useState设置状态的时候，只有第一次生效，后期需要更新状态，必须通过useEffect

   4. 善用useCallback

      死循环产生的解决，父组件传递给子组件事件句柄时，如果我们没有任何参数变动可能会选用useMemo。但是每一次父组件渲染子组件即使没变化也会跟着渲染一次。

   5. 不要滥用useContext

      因为会破坏组件独立性，可以使用基于useContext封装的状态管理工具。

### 7. React Hooks和生命周期的关系?

   Hooks 组件（使用了Hooks的函数组件）有生命周期，而函数组件（未使用Hooks的函数组件）是没有生命周期的。  ![image-20210906144816223.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l09v49n8j310a0lg0we.jpg)

### 8. useCallback 和 useMemo的区别

![image-20210908132743370.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l0a60iuaj312k0jc79k.jpg)

useMemo 和 useCallback 接收的参数都是一样,第一个参数为回调 第二个参数为要依赖的数据

共同作用：

1.仅仅 依赖数据 发生变化, 才会重新计算结果，也就是起到缓存的作用。

两者区别：

1.useMemo 计算结果是 return 回来的值, 主要用于 缓存计算结果的值 ，应用场景如： 需要 计算的状态

2.useCallback 计算结果是 函数, 主要用于 缓存函数，应用场景如: 需要缓存的函数，因为函数式组件每次任何一个 state 的变化 整个组件 都会被重新刷新，一些函数是没有必要被重新刷新的，此时就应该缓存起来，提高性能，和减少资源浪费。

注意： 不要滥用会造成性能浪费，react中减少render就能提高性能，所以这个仅仅只针对缓存能减少重复渲染时使用和缓存计算结果。

---

`useMemo` 和 `useCallback` 是 React 性能优化的一个手段之一。

`useMemo` 会记住回调函数返回的值，只有当它的依赖项改变的时候，才会重新计算。`useMemo` 应该用在一些计算量比较大的场景下，或者是使用它来缓存一些 JSX 对象来避免重渲染。

`useCallback` 其实是 `useMemo` 的语法糖，只不过它是用来缓存函数的，比如一个事件的回调函数。常见的使用场景是，一个较复杂的组件接收一个事件的回调函数，使用 `useCallback` 包装来避免函数的重新创建，从而导致函数的引用发生改变，引起复杂组件的重渲染（前提是该组件使用了 `React.memo` 或者是 `shouldComponentUpdate` API 来优化过）。

但是其实 `useCallback` 有一个非常大的问题，比如在回调函数中，依赖了一个 state，你就不得不在依赖项中添加这个 state，而恰巧这个 state 是频繁变化的值，就会导致回调函数每次都会重新创建，失去了缓存的意义。所以最近 React 团队创建了一个 [RFC](https://github.com/reactjs/rfcs/pull/220) 专门来讨论这个问题。后面 React 会新增一个命名为 `useEvent` 的新 hooks 来解决这个问题。

### 9. react hooks 如何替代或部分替代 redux 功能

### 10. 如何实现一个 react hook，你有没有自己写过一个

### 11. useEffect 中如何使用 async/await

### 12. 为什么不能在表达式里面定义 react hooks

### 13. 在 React hooks 中如何模拟 forceUpdate

### 14. 在 React Hooks 中实现 usePreviouseValue 取上次渲染的值

## 八、✨虚拟DOM

### 1. 对虚拟DOM的理解？虚拟DOM主要做了什么？其本身是什么？

从本质上来说，Virtual Dom是一个JavaScript对象，通过对象的方式来表示DOM结构。将页面的状态抽象为JS对象的形式，配合不同的渲染工具，使跨平台渲染成为可能。通过事务处理机制，将多次DOM修改的结果一次性的更新到页面上，从而有效的减少页面渲染的次数，减少修改DOM的重绘重排次数，提高渲染性能。

### 2. React diff 算法的原理是什么?

`diff`算法就是更高效地通过对比新旧`Virtual DOM`来找出真正的`Dom`变化之处。

`react`中`diff`算法主要遵循三个层级的策略：

- tree层级
- component 层级
- element 层级

![image-20210906152637422.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l0ah4m4fj30ze0aqgp8.jpg)

### 3. React key是干嘛用的为什么要加? key主要解决那一类的问题？

Keys 是 React 用于追踪哪些列表中元素被修改、被添加或者被移除的辅助标识。在开发过程中，我们需要保证某个元素的 key 在其同级元素中具有唯一性。

### 4. 虚拟DOM的引入与直接操作原生DOM,相比，哪一个效率更高？

### 5. React与Vue的diff算法有何不同?

![image-20210907130534095.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l0ar46ztj31980qy4b3.jpg)

## 九、其他

### 1. React组件命名推荐的方式是哪个?

   TodoApp

### 2. react最新版本解决了什么问题，增加了哪些东西？

![image-20210906152927763.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l0b2m8bpj30zs0fq451.jpg)

   关于hooks，增加了很多hooks,使函数组件更容易操作

### 3. react实现一个全局的dialog

### 4. React数据持久化有什么实践吗?

  redux-persist。redux-persist会将redux的store中的数据缓存到浏览器的localStorage中。

### 5. 对React和Vue的理解，它们的异同

![image-20210906153501793.png](http://tva1.sinaimg.cn/large/005NUwygly1h7l0bc2ceyj30z209041j.jpg)  

  数据流，虚拟Dom，组件化写法不同

### 6. 可以使用TypeScript写React应用吗?

### 7. React设计思路，它的理念是什么?

### 8. React中props .children和React.Children的区别

   在React中，当涉及组件嵌套，在父组件中使用props.children把所有子组件显示出来。

   如果想把父组件中的属性传给所有的子组件，需要使用React.Children方法。

### 9. React的状态提升是什么?使用场景有哪些？

   概括来说就是将多个组件需要共享的状态提升到它们最近的父组件上，在父组件上改变这个状态然后通过props分发给子组件。

### 10. React中constructor和getlnitialState的区别

两者都是用来初始化state的。前者是ES6中的语法，后者是ES5中的语法，新版本的React中已经废弃了该方法。

### 11. React的严格模式如何使用，有什么用处？

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7l0c2qyivj30i80hs41j.jpg" alt="image-20210906154354133.png" style="zoom: 50%;" />

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7l0ca7p6vj30k809e75v.jpg" alt="image-20210906154407089.png" style="zoom: 50%;" />

### 12. 在React中遍历的方法有哪些?

数组->map,forEach,对象->map ,for in

### 13. 在React中页面重新加载时怎样保留数据？

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7l0civkoaj31040j67df.jpg" alt="image-20210906154605356.png" style="zoom:50%;" />

### 14. 同时引用这三个库react.js、react-dom.js,babel.js他们有是那么作用？

- react：包含react所必须的核心代码 

- react-dom：react渲染在不同平台所需要的核心代码 
- babel：将jsx转换成React代码的工具

### 15. React必须使用JSX吗?

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h7l0cqtsk5j310y09ajty.jpg" alt="image-20210906154803293.png" style="zoom:50%;" />

### 16. 为什么使用jsx的组件中没有看到使用react却需要引入react？

### 17. 在React中怎么使用async/await?

async/await是ES7标准中的新特性。如果是使用React官方的脚手架创建的项目，就可以直接使用。

### 18. React.Children.map和js的map有什么区别？

JavaScript中的map不会对为null或者undefined的数据进行处理，而React.Children.map中的map可以处理React.Children为null或者undefined的情况。

### 19. 对React SSR的理解

### 20. 为什么React要用JSX?

JSX 是一个 JavaScript 的语法扩展，或者说是一个类似于 XML 的 ECMAScript 语法扩展。它本身没有太多的语法定义，也不期望引入更多的标准。React 团队并不想引入 JavaScript 本身以外的开发体系。而是希望通过合理的关注点分离保持组件开发的纯粹性。

### 21. HOC相比mixins有什么优点?

### 22. React中的高阶组件运用了什么设计模式？

装饰模式。装饰模式的特点是不需要改变被装饰对象 本身，而只是在外面套一个外壳接口。JavaScript 目前已经有了原生装饰器的提案

### 23. 了解 React 中的 ErrorBoundary 吗，它有那些使用场景

[https://vue3js.cn/interview/React/capture error.html#一、是什么]

嵌套的比较深的组件存在出错的风险，组件自身没有容错机制，会逐层交给外层组件处理。这个过程会导致整个组件树销毁。页面结果就是白屏。而且生产环境不会报出有效的错误信息，不好定位问题。 使用 ErrorBoundary 就是在可能出错的组件上套一层组件，在这个新的组件中去容错

在react项目中去编写组件内JavaScript代码错误会导致 React的内部状态被破坏，导致整个应用崩溃,错误边界是一种 React 组件，这种组件可以捕获发生在其子组件树任何位置的 JavaScript 错误，并打印这些错误，同时展示降级 UI，而并不会渲染那些发生崩溃的子组件树,错误边界在渲染期间、生命周期方法和整个组件树的构造函数中捕获错误。

### 24. 如何使用 react hooks 实现一个计数器的组件

```jsx
import { useEffect, useState } from "react";
import "./styles.css";

function CounterWithTimeout() {
  const [count, setCount] = useState(0);
  useEffect(
    () =>
      setTimeout(() => {
        setCount(count + 1);
      }, 1000),
    [count]
  );
  return <h1>{count}</h1>;
}

function CounterWithInterval() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => {
      setCount(count + 1);
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, [count]);

  return <h1>{count}</h1>;
}

export default function App() {
  return (
    <div>
      <CounterWithTimeout />
      <CounterWithInterval />
    </div>
  );
}
```

### 25. 如何使用 react hooks 实现 useFetch 请求数

### 据

```jsx
const useHackerNewsApi = () => {
  const [data, setData] = useState({ hits: [] });
  const [url, setUrl] = useState(
    '<https://hn.algolia.com/api/v1/search?query=redux>',
  );
  const [isLoading, setIsLoading] = useState(false);
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setIsError(false);
      setIsLoading(true);

      try {
        const result = await axios(url);

        setData(result.data);
      } catch (error) {
        setIsError(true);
      }

      setIsLoading(false);
    };

    fetchData();
  }, [url]);

  return [{ data, isLoading, isError }, setUrl];
}

```

### 26. react 如何使用 render prop component 请求数据

### 27. React Portal 有哪些使用场景

### 28. 如果使用 SSR，可以在 created/componentWillMount 中访问 localStorage 吗

### 29. 在 React 项目中 immutable 是优化性能的

### 30. 在 React 应用中如何排查性能问题

### 31. 在 SSR 项目中如何判断当前环境时服务器端还是浏览器端

### 32. 什么是服务器渲染 (SSR)

### 33. 说说React服务端渲染怎么做？原理是什么？

### 33. 在 React 中如何实现代码分割 (code splitting)

在 React 应用中，我们通常的做法是直接将某个模块导入到页面中，这样做导致的结果是打包出来的包体积过大。尤其是在引入了体积巨大的第三个库的情况下，打包后的包体积会十分巨大。因此，我们需要关注我们的应用中所包含的代码，以避免因体积过大而导致加载时间过长。

对代码进行分割能够“懒加载”当前用户所需要的内容，能够显著提高应用的性能。尽管并没有减少应用的整体代码体积，但可以避免加载用户永远不需要的代码，并在初始加载的时候可以减少所需加载的代码量。

https://juejin.cn/post/7056393253246992392

- import() 是 Webpack 提供的用于分割代码的一个方法。该方法的返回结果是Promise，当文件加载完成后悔将模块导出给 promise.then 方法的回调。
- React.lazy
- import() + React Loadable
- UmiJS 按需加载

### 34. 在 React 中如何做好性能优化

- 代码分割
- React.memo()、shouldComponentUpdate()等防止不必要的渲染
- Fragments 避免额外标记
- 错误边界避免组件在出错时破坏整个应用
- 使用 `react-query`，对请求响应进行缓存、重发等，避免多次请求，减少网络 IO 消耗及优化渲染次数
- 使用 `useDebounce`，对值及事件处理函数进行防抖，避免状态频繁变动，优化渲染次数
- 使用 `useImmer`
- 避免使用内联函数
- 使用 Immutable
- 懒加载组件
- 事件绑定方式(`constructor`中`bind`事件与定义阶段使用箭头函数绑定这两种形式只会生成一个方法实例，性能方面会有所改善
- 服务端渲染

### 35. 在 React 中发现状态更新时卡顿，此时应该如何定位及优化

### 36. immer 的原理是什么，为什么它的性能更高

### 37. 同一页面三个组件请求同一个 API 发送了三次请求，如何优化

### 38. 说说你是如何提高组件的渲染效率的？在React中如何避免不必要的render？

- shouldComponentUpdate
- PureComponent
- React.memo

### 39. 说说你对immutable的理解？如何应用在react项目中？

### 40. 说说react中引入css的方式有哪几种？区别？

### 41. 说说对高阶组件的理解？应用场景?

# 四、小程序

## 1. 你对微信小程序的理解？优缺点？
## 2. 微信小程序的生命周期函数有哪些？

###  应用的生命周期

| 生命周期               | 说明                                    |
| ---------------------- | --------------------------------------- |
| onLaunch               | 小程序初始化完成时触发，全局只触发一次  |
| onShow                 | 小程序启动，或从后台进入前台显示时触发  |
| onHide                 | 小程序从前台进入后台时触发              |
| onError                | 小程序发生脚本错误或 API 调用报错时触发 |
| onPageNotFound         | 小程序要打开的页面不存在时触发          |
| onUnhandledRejection() | 小程序有未处理的 Promise 拒绝时触发     |
| onThemeChange          | 系统切换主题时触发                      |

- ⽤户⾸次打开⼩程序，触发 onLaunch（全局只触发⼀次）
- ⼩程序初始化完成后，触发onShow⽅法，监听⼩程序显示
- ⼩程序从前台进⼊后台，触发 onHide⽅法
- ⼩程序从后台进⼊前台显示，触发 onShow⽅法
- ⼩程序后台运⾏⼀定时间，或系统资源占⽤过⾼，会被销毁

### 页面的生命周期

| 生命周期 | 说明                              | 作用                           |
| -------- | --------------------------------- | ------------------------------ |
| onLoad   | 生命周期回调—监听页面加载         | 发送请求获取数据               |
| onShow   | 生命周期回调—监听页面显示         | 请求数据                       |
| onReady  | 生命周期回调—监听页面初次渲染完成 | 获取页面元素（少用）           |
| onHide   | 生命周期回调—监听页面隐藏         | 终止任务，如定时器或者播放音乐 |
| onUnload | 生命周期回调—监听页面卸载         | 终止任务                       |

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86yiav2wfj311e0iq41y.jpg" alt="image.png" style="zoom:33%;" />

### 组件的生命周期

| 生命周期 | 说明                              |
| -------- | --------------------------------- |
| created  | 生命周期回调—监听页面加载         |
| attached | 生命周期回调—监听页面显示         |
| ready    | 生命周期回调—监听页面初次渲染完成 |
| moved    | 生命周期回调—监听页面隐藏         |
| detached | 生命周期回调—监听页面卸载         |
| error    | 每当组件方法抛出错误时执行        |

### 组件所在页面的生命周期

| 生命周期 | 说明                       |
| -------- | -------------------------- |
| show     | 组件所在的页面被展示时执行 |
| hide     | 组件所在的页面被隐藏时执行 |

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86yj2y8r3j310w11admw.jpg" alt="image.png" style="zoom:50%;" />

1. ⼩程序注册完成后，加载⻚⾯，触发onLoad⽅法
2. ⻚⾯载⼊后触发onShow⽅法，显示⻚⾯
3. ⾸次显示⻚⾯，会触发onReady⽅法，渲染⻚⾯元素和样式，⼀个⻚⾯只会调⽤⼀次
4. 当⼩程序后台运⾏或跳转到其他⻚⾯时，触发onHide⽅法
5. 当⼩程序有后台进⼊到前台运⾏或重新进⼊⻚⾯时，触发onShow⽅法
6. 当使⽤重定向⽅法 wx.redirectTo() 或关闭当前⻚返回上⼀⻚wx.navigateBack()，触发onUnload
7. 当存在也应用生命周期和页面周期的时候，相关的执行顺序如下：

打开小程序：(App)onLaunch --> (App)onShow --> (Pages)onLoad --> (Pages)onShow --> (pages)onRead

进入下一个页面：(Pages)onHide --> (Next)onLoad --> (Next)onShow --> (Next)onReady

返回上一个页面：(curr)onUnload --> (pre)onShow

离开小程序：(App)onHide

再次进入：小程序未销毁 --> (App)onShow(执行上面的顺序），小程序被销毁，（App)onLaunch重新开始执行。

## 3. 微信小程序中路由跳转的方式有哪些？区别？

- `wx.navigateTo(Object)`

  用于保留当前页面、跳转到应用内的某个页面，使用 wx.navigateBack可以返回到原页面。

  对于页面不是特别多的小程序，通常推荐使用 `wx.navigateTo`进行跳转， 以便返回原页面，以提高加载速度。当页面特别多时，则不推荐使用

- `wx.redirectTo(Object)`

  用于关闭当前页面，跳转到应用内的某个页面。

  重定向，当页面过多时，被保留页面会挤占微信分配给小程序的内存，或是达到微信所限制的 10 层页面栈的情况下，我们应该考虑选择 `wx.redirectTo`

  这样的跳转，可以避免跳转前页面占据运行内存，但返回时页面需要重新加载，增加了返回页面的显示时间

- `wx.switchTab(Object)`

  跳转到 tabBar页面，并关闭其他所有非 tabBar 页面

- `wx.navigateBack(Object)`

  `wx.navigateBack()` 用于关闭当前页面，并返回上一页面或多级页面，开发者可通过 `getCurrentPages()` 获取当前的页面栈，决定需要返回几层则设置对象的`delta`属性即可

- `wx.reLaunch(Object)`

  关闭所有页面，打开到应用内的某个页面，返回的时候跳到首页

**关于上述五种跳转方式，做下总结：**

`navigateTo` 保留当前页面，跳转到应用内的某个页面，使用 `wx.navigateBack` 可以返回到原页

`redirectTo` 关闭当前页面，跳转到应用内的某个页面

`switchTa `跳转到 tabBar 页面，同时关闭其他非 tabBar 页面

`navigateBack` 返回上一页面

`reLanch` 关闭所有页面，打开到应用内的某个页面

**其中关于它们的页面栈的关系如下：**

`avigateTo` 新页面入栈

`redirectTo` 当前页面出栈，新页面入栈

`navigateBack` 页面不断出栈，直到目标返回页，新页面入栈

`switchTab` 页面全部出栈，只留下新的 Tab 页面

`reLanch` 页面全部出栈，只留下新的页面

## 4. 提高微信小程序的应用速度的手段有哪些？

**小程序启动加载性能**：

- 控制代码包的大小
- 分包加载
- 首屏体验（预请求，利用缓存，避免白屏，及时反馈

**小程序渲染性能**：

- 避免不当的使用setData
- 使用自定义组件

### 加载

提升体验最直接的方法是控制小程序包的大小，常见手段有如下：

1. 代码包的体积压缩可以通过勾选开发者工具中“上传代码时，压缩代码”选项
2. 及时清理无用的代码和资源文件
3. 减少资源包中的图片等资源的数量和大小（理论上除了小icon，其他图片资源从网络下载），图片资源压缩率有限

并且可以采取分包加载的操作，将用户访问率高的页面放在主包里，将访问率低的页面放入子包里，按需加载

当用户点击到子包的目录时，还是有一个代码包下载的过程，这会感觉到明显的卡顿，所以子包也不建议拆的太大，当然我们可以采用子包预加载技术，并不需要等到用户点击到子包页面后在下载子包

### 渲染

关于微信小程序首屏渲染优化的手段如下：

1. 请求可以在页面onLoad就加载，不需要等页面ready后在异步请求数据

2. 尽量减少不必要的https请求，可使用 getStorageSync() 及 setStorageSync() 方法将数据存储在本地

3. 可以在前置页面将一些有用的字段带到当前页，进行首次渲染（列表页的某些数据--> 详情页），没有数据的模块可以进行骨架屏的占位

在微信小程序中，提高页面的多次渲染效率主要在于正确使用setData：

1. 不要过于频繁调用setData，应考虑将多次setData合并成一次setData调用

2. 数据通信的性能与数据量正相关，因而如果有一些数据字段不在界面中展示且数据结构比较复杂或包含长字符串，则不应使用setData来设置这些数据

3. 与界面渲染无关的数据最好不要设置在data中，可以考虑设置在page对象的其他字段下

除此之外，对于一些独立的模块我们尽可能抽离出来，这是因为自定义组件的更新并不会影响页面上其他元素的更新

各个组件也将具有各自独立的逻辑空间。每个组件都分别拥有自己的独立的数据、setData调用

## 5. 微信小程序的登录流程？

### 登陆流程

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86yucbt56j30ua0t4dtk.jpg" alt="image.png" style="zoom:33%;" />

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86yvbhs0nj314k1184qp.jpg" alt="image.png" style="zoom:50%;" />

- 通过 wx.login() 获取到用户的code判断用户是否授权读取用户信息，调用wx.getUserInfo 读取用户数据
- 由于小程序后台授权域名无法授权微信的域名，所以需要自身后端调用微信服务器获取用户信息
- 通过 wx.request() 方法请求业务方服务器，后端把 appid , appsecret 和 code 一起发送到微信服务器。 appid 和 appsecret 都是微信提供的，可以在管理员后台找到
- 微信服务器返回了 openid 及本次登录的会话密钥 session_key
- 后端从数据库中查找 openid ，如果没有查到记录，说明该用户没有注册，如果有记录，则继续往下走
- session_key 是对用户数据进行加密签名的密钥。为了自身应用安全，session_key 不应该在网络上传输
- 然后生成 session并返回给小程序
- 小程序把 session 存到 storage 里面
- 下次请求时，先从 storage 里面读取，然后带给服务端
- 服务端对比 session 对应的记录，然后校验有效期

### 判断登录态是否过期

实际业务中，我们还需要登录态是否过期，通常的做法是在登录态（临时令牌）中保存有效期数据，该有效期数据应该在服务端校验登录态时和约定的时间（如服务端本地的系统时间或时间服务器上的标准时间）做对比

这种方法需要将本地存储的登录态发送到小程序的服务端，服务端判断为无效登录态时再返回需重新执行登录过程的消息给小程

另一种方式可以通过调用`wx.checkSession`检查微信登陆态是否过期：

- 如果过期，则发起完整的登录流程
- 如果不过期，则继续使用本地保存的自定义登录态

这种方式的好处是不需要小程序服务端来参与校验，而是在小程序端调用AP，流程如下所示：

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86yxjzympj30r20uutkp.jpg" alt="image.png" style="zoom: 50%;" />

## 6. 微信小程序的发布流程？
## 7. 微信小程序的支付流程？

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h86z0oscy1j31941041fr.jpg" alt="image.png" style="zoom:50%;" />

1. 打开某小程序，点击直接下单
2. wx.login获取用户临时登录凭证code，发送到后端服务器换取openId
3. 在下单时，小程序需要将购买的商品Id，商品数量，以及用户的openId传送到服务器
4. 服务器在接收到商品Id、商品数量、openId后，生成服务期订单数据，同时经过一定的签名算法，向微信支付发送请求，获取预付单信息(prepay_id)，同时将获取的数据再次进行相应规则的签名，向小程序端响应必要的信息
5. 小程序端在获取对应的参数后，调用wx.requestPayment()发起微信支付，唤醒支付工作台，进行支付
6. 接下来的一些列操作都是由用户来操作的包括了微信支付密码，指纹等验证，确认支付之后执行鉴权调起支付
7. 鉴权调起支付：在微信后台进行鉴权，微信后台直接返回给前端支付的结果，前端收到返回数据后对支付结果进行展示
8. 推送支付结果：微信后台在给前端返回支付的结果后，也会向后台也返回一个支付结果，后台通过这个支付结果来更新订单的状态

```JS
wx.requestPayment({
  // 时间戳
  timeStamp: '',
  // 随机字符串
  nonceStr: '',
  // 统一下单接口返回的 prepay_id 参数值
  package: '',
  // 签名类型
  signType: '',
  // 签名
  paySign: '',
  // 调用成功回调
  success () {},
  // 失败回调
  fail () {},
  // 接口调用结束回调
  complete () {}
})
```

refs:

- https://pay.weixin.qq.com/wiki/doc/apiv3/open/pay/chapter2_8_0.shtml
- https://juejin.cn/post/6844903895970349064

## 8. 微信小程序的实现原理？

https://vue3js.cn/interview/applet/WebView_jscore.html#%E4%B8%80%E3%80%81%E8%83%8C%E6%99%AF

# 正则表达式

# node

1. 简述 node/v8 中的垃圾回收机制

# 文件上传

1. 前端如何实现文件上传功能
2. 前端上传文件时如何读取文件内容

# 项目相关

1. 你们项目的测试覆盖率是怎么做的
2. 如何查看你们 JS 项目中应采用的 node 版本
3. 如何删除项目中没有使用到的 package
4. 关于模块化，什么是 amd 和 umd
5. 什么是 commonjs2
6. 现代化前端框架中如何进行调试







