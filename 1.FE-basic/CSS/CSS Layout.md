# CSS Flexbox

[Flexbox Playground](https://demos.scotch.io/visual-guide-to-css3-flexbox-flexbox-playground/demos/)

[Flexbox tutorial](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)


## Background

Flex 是 Flexible Box 的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。注意，设为 Flex 布局以后，子元素的float、clear和vertical-align属性将失效。

### Flex布局适用范围

1. 任何一个容器都可以指定为 Flex 布局。

```css
.box{
display: flex;
}
```

2. 行内元素也可以使用 Flex 布局

```css
.box{
display: flex;
}
```

3. Webkit 内核的浏览器，必须加上-webkit前缀。

```css
.box{
display: inline-flex;
}
```

## Basics & Terminology

采用 Flex 布局的元素，称为 Flex 容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为 Flex 项目（flex item），简称"项目"。

![1.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkrg7hj30fn099gls.jpg)

- 水平的主轴（main axis）

	主轴的开始位置（与边框的交叉点）叫做main start，结束位置叫做main end

- 垂直的交叉轴（cross axis）

	交叉轴的开始位置叫做cross start，结束位置叫做cross end。

- 项目默认沿主轴排列。单个项目占据的主轴空间叫做main size，占据的交叉轴空间叫做cross size。

## 容器的属性

### flex-direction

属性决定主轴的方向（即项目的排列方向）

![2.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkp7xxj30m405nt8j.jpg)

```css
.box {
flex-direction: row | row-reverse | column | column-reverse;
}
```

值内容

- row（默认值）：主轴为水平方向，起点在左端。
- row-reverse：主轴为水平方向，起点在右端。
- column：主轴为垂直方向，起点在上沿。
- column-reverse：主轴为垂直方向，起点在下沿。

### flex-wrap

默认情况下，项目都排在一条线（又称"轴线"）上。flex-wrap属性定义，如果一条轴线排不下，如何换行。

```css
.box{
flex-wrap: nowrap | wrap | wrap-reverse;
}
```

值内容

1. nowrap（默认）：不换行。
2. 
   ![11.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1vityb0j30jg041t9p.jpg)

2. wrap-reverse：换行，第一行在下方。
3. 
   ![12.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1vivbqvj30jg04xdhw.jpg)

3. wrap-reverse：换行，第一行在下方。
4. 
   ![13.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1vivk76j30jg04x0uq.jpg)
   
   ![14.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1vit9lxj30m607ojr8.jpg)

### flex-flow

flex-flow属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。

```css
.box {
flex-flow: <flex-direction> || <flex-wrap>;
}
```

### justify-content

属性定义了项目在主轴上的对齐方式。

![15.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1viuea4j30hp0l7glq.jpg)

```css
.box {
justify-content: flex-start | flex-end | center | space-between | space-around;
}
```

值内容

- flex-start（默认值）：左对齐
- flex-end：右对齐
- center： 居中
- space-between：两端对齐，项目之间的间隔都相等。
- space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。

### align-items

属性定义项目在交叉轴上如何对齐。

![3.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lks0tmj30h50lumxc.jpg)

```css
.box {
align-items: flex-start | flex-end | center | baseline | stretch;
}
```

值内容

- flex-start：交叉轴的起点对齐。
- flex-end：交叉轴的终点对齐。
- center：交叉轴的中点对齐。
- baseline: 项目的第一行文字的基线对齐。
- stretch（默认值）：如果项目未设置高度或设为auto，将占满整个容器的高度。

### align-content

属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。

![4.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkrp3wj30h80lut8w.jpg)

```css
.box {
align-content: flex-start | flex-end | center | space-between | space-around | stretch;
}
```

值内容

- flex-start：与交叉轴的起点对齐。
- flex-end：与交叉轴的终点对齐。
- center：与交叉轴的中点对齐。
- space-between：与交叉轴两端对齐，轴线之间的间隔平均分布。
- space-around：每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。
- stretch（默认值）：轴线占满整个交叉轴。

## 项目的属性

### order
![5.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkq1olj30kv0dcdfr.jpg)

属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。

```css
.item {
order: <integer>;
}
```

### flex-grow

属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。

![6.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkq1z8j30ma05vjr7.jpg)

```css
.item {
flex-grow: <number>; /* default 0 */
}
```

如果所有项目的flex-grow属性都为1，则它们将等分剩余空间（如果有的话）。如果一个项目的flex-grow属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。

### flex-shrink

属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。

![7.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkx9jlj30jg041q4d.jpg)

```css
.item {
flex-shrink: <number>; /* default 1 */
}
```

1. 如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。

2. 负值对该属性无效。

### flex-basis

属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为auto，即项目的本来大小。

```css
.item {
flex-basis: <length> | auto; /* default auto */
}
```

它可以设为跟width或height属性一样的值（比如350px），则项目将占据固定空间。

### flex

属性是flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto。后两个属性可选。

```css
.item {
flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
}
```

该属性有两个快捷值：auto (1 1 auto) 和 none (0 0 auto)。

建议优先使用这个属性，而不是单独写三个分离的属性，因为浏览器会推算相关值。

### align-self

属性允许单个项目有与其他项目不一样的对齐方式，可覆盖align-items属性。默认值为auto，表示继承父元素的align-items属性，如果没有父元素，则等同于stretch。

该属性可能取6个值，除了auto，其他都与align-items属性完全一致。

![8.png](http://ww1.sinaimg.cn/large/005NUwyggy1gbj1lkv29cj30kn0augll.jpg)

```css
.item {
align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```

# CSS Grid

[CSS Grid tutorial](https://css-tricks.com/snippets/css/complete-guide-grid/)

# CSS Cell

