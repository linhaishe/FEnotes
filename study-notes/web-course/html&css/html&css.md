### margin, padding

margin:会导致block之间产生间隙，间隙大小为marigin大小

```html
<html>
<head>
<style type="text/css">
div.bottommargin {
margin-bottom:80px;
border: 1px solid black;
}
</style>
</head>

<body>
<p>这个段落没有指定外边距。</p>
<div class="bottommargin">这个段落带有指定的下外边距。</div>
<p>这个段落没有指定外边距。</p>
</body>

</html>

```

padding：设置容器内容与容器边框的距离

padding会成为整个容器宽高的一部分

为了再添加padding的情况下，保持整个容器的大小不变，我们需要在容器的宽高中，减去所添加的padding的值。

https://juejin.im/post/59ef72f5f265da4320026f76

css的盒模型由content(内容)、padding(内边距)、border(边框)、margin(外边距)组成。但盒子的大小由content+padding+border这几部分决定，把margin算进去的那是盒子占据的位置，而不是盒子的大小

### CSS Box Sizing

<mark>没有很好理解和掌握需要多看实例</mark>

The CSS `box-sizing` property allows us to include the padding and border in an element's total width and height.

属性定义了 user agent 应该如何计算一个元素的总宽度和总高度。

If you set `box-sizing: border-box;` on an element padding and border are included in the width and height:

```html
<!DOCTYPE html>
<html>
<head>
<style> 
.div1 {
  width: 300px;
  height: 100px;
  border: 1px solid blue;
  box-sizing: border-box;
}

.div2 {
  width: 300px;
  height: 100px;  
  padding: 50px;
  border: 1px solid red;
  box-sizing: border-box;
}
</style>
</head>
<body>

<div class="div1">Both divs are the same size now!</div>
<br>
<div class="div2">Hooray!</div>

</body>
</html>

```

https://www.w3school.com.cn/tiy/t.asp?f=css3_box-sizing

https://www.w3schools.com/css/css3_box-sizing.asp

https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing

Background-image/repeat/position

img覆盖backgroung-image覆盖background-color

### 盒模型是

宽高内边距外边距背景图背景色等等css属性共同作用于html标签，所产生的结果

### 文档流

浏览器读取，并解析，绘制html标签的过程，css的定位，本质是html标签脱离文档流

### css定位

三种机制：

1. 普通流，

2. float, 

3. position:

- static

- relative:相对于原来的位置的定位，进行偏移。

```html
<style type="text/css">
div{
	width: 200px;
	height: 100px;
	background: #f00;
	margin:10px;
	font-size: 32px;
	color: #fff;
}

.pr{
	position: relative;
	left:100px;
	top:30px;
	background: #0f0;
}
</style>

<div>111</div>
<div>222</div>
<div class='pr'>333</div>
<div>444</div>
<div>555</div>
```

- absolute,相对于最近的可定位的父级元素进行定位，不保留原来的定位

```html
<style type="text/css">
div{
	width: 200px;
	height: 100px;
	background: #f00;
	margin:10px;
	font-size: 32px;
	color: #fff;
}

.pa{
	position: absolute;
	left:100px;
	top:30px;
	background: #00f;
}

</style>

<div>111</div>
<div>222</div>
<div class='pa'>333</div>
<div>444</div>
<div>555</div>
```

- fixed，视窗固定

### float

让html标签向左右移动，直到他的边框，碰到了另一个外边框或父容器的边为止。让html元素脱离文档流。让其所在的html标签不再参与各个容器的高度的计算

float CSS属性指定一个元素应沿其容器的左侧或右侧放置，允许文本和内联元素环绕它。该元素从网页的正常流动(文档流)中移除，尽管仍然保持部分的流动性

#### 浮动元素如何定位

正如我们前面提到的那样，当一个元素浮动之后，它会被移出正常的文档流，然后向左或者向右平移，一直平移直到碰到了所处的容器的边框，或者碰到**另外一个浮动的元素**。

在下面的图片中，有三个红色的正方形。其中有两个向左浮动，一个向右浮动。要注意到第二个向左浮动的正方形被放在第一个向左浮动的正方形的右边。如果还有更多的正方形这样浮动，它们会继续向右堆放，直到填满容器一整行，之后换行至下一行。

```html
<section>
  <div class="left">1</div>
  <div class="left">2</div>
  <div class="right">3</div>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     Morbi tristique sapien ac erat tincidunt, sit amet dignissim
     lectus vulputate. Donec id iaculis velit. Aliquam vel
     malesuada erat. Praesent non magna ac massa aliquet tincidunt
     vel in massa. Phasellus feugiat est vel leo finibus congue.</p>
</section>
```

```css
section {
  border: 1px solid blue;
}

div {
  margin: 5px;
  width: 50px;
  height: 50px;
}

.left {
  float: left;
  background: pink;
}

.right {
  float: right;
  background: cyan;
}
```

![Xnip2019-11-03_12-44-47.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8kr4o27fyj30u20hojt3.jpg)

问题：浮动元素定位问题，4和5没有设置浮动，按照我的理解，在3设置float：left时候，4应该向上移动到3的位置，5移动到4的位置，为什么box444和555的内容重叠了(pic1)？3设置为float:right之后，显示的是我所理解的浮动作用的效果。(pic2)

![Xnip2019-11-03_12-47-05.png](http://ww1.sinaimg.cn/large/005NUwygly1g8krjfe8n9j31ve0yg7c9.jpg)

![Xnip2019-11-03_12-53-15.png](http://ww1.sinaimg.cn/large/005NUwygly1g8krjffmvcj31w00sk44g.jpg)

**清除浮动**

Clear:left/right/none/both

个人理解：父元素div整体向左浮动float:left,当其中一个子元素清除浮动时，需要清除父元素设定的相同的浮动，即需要清除left，若清除right则没有响应。因为right属性没有设置。为了方便，会直接写clear:both，即不管它父元素设置left or right，都可以直接清除相关的浮动属性。

```html
<style type="text/css">
div{
	width: 100px;
	height: 50px;
	background: #f00;
	margin:10px;
	color: #fff;
	font-size: 22px;
	float: left;
}

.cle{
	clear:both;
}
</style>

<div>111</div>
<div>222</div>
<div class='cle'>333</div>
<div>444</div>
<div>555</div>
```

当一个容器没有高度，并且他的唯一子元素float的时候，容器高度消失，因为父元素没有得到子元素高度的支撑。

```html
<style type="text/css">
.wrap{
	width: 300px;
	/*height: 200px;*/
	background: #f00;
}
.wrap img{
	float: left;
}

/*添加 :after 伪元素 */
/* 用来在元素的内容的后面，添加新的内容 */
/*即wrap后面有个img，在img后面添加内容，仍然在div的范围中*/
.wrap:after{
	content:'.';
	clear: both;
	display: block;
	visibility: hidden;
	height: 0;
	overflow: hidden;
}
/*visibility:隐藏内容，但其会保留宽高*/
/*overflow:超出隐藏*/
</style>

<div class='wrap'>
	<img src="imgxxx.png" />
</div>
```

伪元素 :after元素的内容的后面添加内容

::before和::after下特有的content，用于在css渲染中向元素逻辑上的头部或尾部添加内容。这些添加不会出现在DOM中，即默认浮动，不会改变文档内容，不可复制，仅仅是在css渲染层加入。所以不要用:before或:after展示有实际意义的内容，尽量使用它们显示修饰性内容，例如图标。举例：网站有些联系电话，希望在它们前加一个icon

因为after，它也是个html容器，当它是清除了浮动的时候，就回到了普通文档流里，就可以计算它的高度了，那么这时，父容器就可以计算总的高度了，父容器自然就可以显示了。

行级容器：inline-block

宽高不起作用，默认横向排列

块级容器：block

宽高起作用，默认横向独占一行

