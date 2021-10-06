## 块级格式化上下文

- 块级格式化上下文（Block Formatting Context）
  - 盒子在容器（包含块）内从上到下一个接一个地放置
  - 两个兄弟盒之间的竖直距离由 margin 属性决定
  - 同一个 BFC 内垂直 margin 会合并
  - 盒子的左外边缘挨着容器（包含块）的左边
- 块级格式化上下文（BFC）的特性如下：
  - 但是浮动元素后面的行级盒子会变短以避开浮动元素
  - BFC 的高度会包含其内的浮动元素
  - BFC 不会和浮动元素重叠
  - BFC 可以通过 overflow:hidden 等方法创建
- BFC的创建可通过如下方法：
  - 浮动框
  - 绝对定位框
  - 非块级的块容器（inline-block）
  - overflow属性为非visible的块框
- 那么BFC有哪些主要的作用呢？
  - 可以清楚浮动
  - 防止发生margin折叠
  - 更加方便的进行双栏布局
- 行级格式化上下文（Inline Formatting Context）
  - 盒子一个接一个水平放置盒之间的水平
  - margin，border和padding 都有效
  - 同一行的盒子所在的矩形区域叫行盒(Line box)
  - 当一个行盒放不下上下文内所有盒子时，会被分到多个垂直堆叠的行盒里
  - 行盒内的水平分布由'text-align'属性决定
  - 如果一个行级块无法分割(单词、inline-block)，该元素会被作为一个整体决定分布在哪一个行盒
- 浮动 - Float
  - 浮动元素从常规流中脱离，被漂浮在容器(包含块)左边或右边
  - 浮动盒会一直漂到其外边缘挨到容器边缘或另外的浮动盒
  - 浮动元素不会影响其后面的流内块级盒
  - 但是浮动元素后面的行级盒子会变短以避开浮动元素
- 清除浮动 - Clear
  - 指定元素哪一边不能与之前的浮动框相邻
  - 取值：left | right | both

## CSS布局

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548315554191-094db4f3-c923-489e-8c79-f231b16465f7.png)

- 二列布局：侧边栏固定宽度，内容栏自适应宽度
- 三列布局：两侧两列固定宽度，内容栏自适应宽度

**1. float+margin**

```scss
<style>
.left{
    width: 50px;
    float: left;
    border:1px solid red;
}
.right{
    width: 200px;
    float: right;
    border:1px solid red;
}
.content{
    border:1px solid red;
}
</style>
<div class="left">left</div>
<div class="right">right</div>
<div class="content">content</div>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548317087077-57e64e8c-9d60-44d2-9b73-42773bbdcb4c.png)

- 注意DOM文档的书写顺序，先写两侧栏，再写主面板，更换后则侧栏会被挤到下一列（圣杯布局和双飞翼布局都会用到）。
- 这种布局方式比较简单明了，但缺点是渲染时先渲染了侧边栏，而不是比较重要的主面板。

**2. position+margin**

```css
<style>
.left, .right {
    position: absolute;
    top: 0; 
    width: 200px;
    border: 1px solid red;
}
.left { 
    left: 0;
}
.right { 
    right: 0; 
}
.content { 
    margin: 0 200px;
    border: 1px solid red;
}
</style>
<div class="left">left</div>
<div class="content">content</div>
<div class="right">right</div>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548317647354-64254dc5-6f9b-403f-9a95-20a80d09c6b6.png)

- 本方法不限制DOM书写顺序，先写主面板会使主面板部分优先渲染（一般主面板会比侧栏内容重要）。
- 与上一种方法相比，本种方法是通过定位来实现侧栏的位置固定。
- 如果中间栏含有最小宽度限制，或是含有宽度的内部元素，则浏览器窗口小到一定程度，主面板与侧栏会发生重叠。

### **圣杯布局(float + 负margin)**

```css
<style>
.content {        
    float: left;       
    width: 100%; 
    background-color:red;
 }  
 .left {       
    float: left;        
    width: 190px;        
    margin-left: -100%;               
    position: relative;  
    left: -190px;  
    background-color: gray;  
}   
.right {        
    float: left;        
    width: 230px;        
    margin-left: -230px; 
    position: relative; 
    right: -230px;  
    background-color: gray;
 }
#body-content {        
    padding: 0 230px 0 190px;   
 }
</style>
 <div id="body-content">
    <div class="content">content</div>
    <div class="left">body-left</div>
    <div class="right">body-right</div>
</div>
```

- 布局步骤:
  1. 三者都设置向左浮动。
  2. 设置`content`宽度为100%，设置两侧栏的宽度。
  3. 设置 负边距，`body-left`设置负左边距为100%，`body-right`设置负左边距为负的自身宽度。
  4. 设置`content`的padding值给左右两个子面板留出空间。
  5. 设置两个子面板为相对定位，`body-left`的left值为负的`body-left`宽度，`body-right`的right值为负的`body-right`宽度。

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548318720163-fe886dde-785a-424f-b77f-b5d2935274da.png)

- DOM元素的书写顺序不得更改。
- 主面板部分优先渲染（一般主面板会比侧栏内容重要）。
- 当面板的main内容部分比两边的子面板宽度小的时候，布局就会乱掉。可以通过设置main的min-width属性或使用双飞翼布局避免问题。

### **双飞翼布局(float + 负margin )**

```css
<style>
.body-content {        
    float: left;       
    width: 100%;   
 }  
 .left {       
    float: left;        
    width: 190px;        
    margin-left: -100%;   
    background-color:gray;
}   
.right {        
    float: left;        
    width: 230px;        
    margin-left: -230px; 
    background-color:gray;
 }
.content {    
    margin: 0 230px 0 190px;
    background-color:red;
}
</style>
 <div class="body-content">
    <div class="content">content</div>
</div>
<div class="left">left</div>
<div class="right">right</div>
```

- 布局步骤:
  1. 三者都设置向左浮动。
  2. 设置main-wrap宽度为100%，设置两个侧栏的宽度。
  3. 设置 负边距，sub设置负左边距为100%，extra设置负左边距为负的自身宽度。
  4. 设置main的margin值给左右两个子面板留出空间。

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548323265676-096c10d6-0955-41c3-85c3-c4d1c7c77675.png)

- 主面板部分优先渲染（一般主面板会比侧栏内容重要）。
- 圣杯采用的是padding，而双飞翼采用的margin，解决了圣杯布局content的最小宽度不能小于左侧栏的缺点。
- 双飞翼布局不用设置相对布局，以及对应的left和right值。
- 通过引入相对布局，可以实现三栏布局的各种组合，例如对右侧栏设置position: relative; left: 190px;,可以实现left+right+content的布局。

## 其他资料

- [Flex 布局教程：语法篇 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html?utm_source=tuicool)
- [Flex 布局教程：实例篇 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/07/flex-examples.html)
- [学习CSS布局](http://zh.learnlayout.com/)