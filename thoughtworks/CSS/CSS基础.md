# CSS基础

## 学习目标

- 了解什么是CSS
- 了解CSS中的基本规则
- 掌握CSS中的基本单位

## 学习内容

#### CSS 概述

- CSS 指层叠样式表 (Cascading Style Sheets)
- 样式定义如何显示 HTML 元素
- 样式通常存储在样式表中
- 把样式添加到 HTML 4.0 中，是为了解决内容与表现分离的问题
- 外部样式表可以极大提高工作效率
- 外部样式表通常存储在 CSS 文件中
- 多个样式定义可层叠为一
- 和HTML类似，CSS也不是严格意义上的编程语言，它是一种样式表语言，也就是说，它允许有选择性地为 HTML 文档的元素添加样式。
- CSS规则如下图所示![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-1/38720560.jpg)
- 选择器（Selector）

HTML 元素的名称位于规则集开始。它选择了一个或多个需要添加样式的元素（在这个例子中就是 p 元素）。要给不同元素添加样式只需要更改选择器就行了。

- 声明（Declaration）

一个单独的规则比如 color: red; 这指定了你想要添加样式元素的属性。

- 属性（Properties）

这是你改变 HTML 元素样式的方法。（在这个例子中 color 就是 <p> 元素的属性。）在 CSS 中，你通过选择合适的属性来改变你的规则。

- 属性值（Property value）

在属性的右边，冒号后面，我们拥有属性值，用于从指定的属性里的非常多的外观中选择一个值（我们除了 red 之外还有很多属性值可以用于 color ）。

###### 注意其他重要的语法：

- 每个规则集（除了选择器的部分）都应该包含在成对的大括号里（{}）。
- 在每个声明里，你应该用冒号（:）分离开属性与属性值。
- 在每个规则集里，你应该用分号（;）分离开各个声明。

#### 如何在HTML中引用CSS？

- 想要在HTML文档中应用CSS，有三种方法：
  - 外链：

```html
<link rel="stylesheet" type="text/css" href="/path/to/style.css">
```

- 嵌入：

  ```html
  html
    <style type="text/css">
      li { margin: 0; list-style: none; }
      p { margin: 1em 0; }
    </style>
  ```

- 内联：

```html
<p style="margin:1em 0">Example Content</p>
```

##### 当同一个 HTML 元素被不止一个样式定义时，会使用哪个样式呢？

一般而言，所有的样式会根据下面的规则层叠于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。

1. 浏览器缺省设置
2. 外部样式表
3. 内部样式表（位于 <head> 标签内部）
4. 内联样式（在 HTML 元素内部）

#### CSS注释

- 在CSS中可以通过 / *我是注释* / 这样的形式添加注释，示例如下

```css
/* 设置按钮宽度 */
.form button {
  width: 240px;
}
```

#### CSS中基本长度单位

- 绝对单位：

  - px：像素，对应显示器的一个像素点
  - in：英寸
  - 英寸cm：厘米
  - 厘米mm：毫米
  - 毫米pt：磅 (1 pt 等于 1/72 英寸)
  - 英寸pc：1pc 等于 12pt

- 相对单位： - em：相对于该元素的一个 font-size - rem：相对于 html 元素的 font-size - vh：浏览器窗口高度的 1% - vw：浏览器窗口宽度的 1% - vmin：vh 和 vw 中的较小者 - vmax：vh 和 vw 中的较大者

  

  #### CSS中的颜色

- 关键字，如：red → 红色，blue → 蓝色等

- Hex，用三位16进制的数字来表示，分别代表rgb三色的值大小，从 0 到 ff，以此代表0-255，如：#4286f4

- RGB & RGBA，rgb分别代表红色、绿色、蓝色，值分别为0-255，其中a代表透明度，如：rgb(66, 134, 244), rgba(66, 134, 244,0.5), 

- HSL & HSLA，代表色相、饱和度和亮度，色相是色彩的基本属性,就是平常所说的颜色名称，如红色、黄色等，以0-360度衡量，饱和度(S)是指色彩的纯度,越高色彩越纯,低则逐渐变灰，亮度越高颜色越亮，饱和度和亮度使用0%-100%的范围，其中a代表透明度，值为0-1，如：hsl(120, 100%, 50%)

## 推荐资料(扩展学习)

- [CSS 教程 - W3school](http://www.w3school.com.cn/css/index.asp)
- [七个你可能不了解的CSS单位](https://www.w3cplus.com/css/7-css-units-you-might-not-know-about.html)

# CSS选择器

## 学习目标

- 掌握通配选择器、标签选择器、id选择器、类选择器四种简单选择器的用法
- 掌握属性选择器的基本用法
- 了解伪类的基本用法
- 掌握选择器之间的组合关系

## 学习内容

- 选择器用来从页面中选择元素，以给它们定义样式。

###### 通配选择器

```css
 /* 匹配所有元素 */
 * {
   box-sizing: inherit;
 }
```

###### 标签选择器

```css
 /* 匹配所有P元素 */
 p {
   margin: 1em 0;
 }
```

###### id选择器

```html
  <!-- HTML -->
  <p id="example">Just test content</p>
  
  <!-- CSS -->
  <style type="text/css">
    /* 匹配id为example的元素
     * 注意：id 值在一个 HTML 中必须唯一
     */
    #example {
      font-size: 2em;
      line-height: 1.6;
      color: red;
    }
  </style>
```

###### 类选择器

```html
  <!-- HTML -->
  <p class="error">Error message</p>
  <!-- 可以给一个元素指定多个class，用空格隔开 -->
  <p class="error icon">Another error message</p>
  
  <!-- CSS -->
  <style type="text/css">
    .error {
      color: orange;
    }
    .icon {
      background: url(error.png) no-repeat 0 0;
    }
  </style>
```

- **以上学到的：通配选择器、标签选择器、ID选择器、类选择器都属于简单选择器，除去简单选择器，还有复杂选择器，主要包括分别如下**。

###### 属性选择器

```html
  <!-- HTML -->
  <p>
    <label>用户名：</label>
    <input name="username" value="tw" disabled>
  </p>
  <p>
    <label>密码：</label>
    <input type="password" required>
  </p>
  
  <!-- CSS -->
  <style>
    /* 选中所有的禁用的输入框 */
    input[disabled] {
      background: #ddd;
      color: #999;
      cursor: not-allowed;
    }
    /* 选中所有输入框类型为"密码"的元素 */
    input[type="password"] {
      border-color: red;
      color: red;
    }
  
  </style>
```

###### 伪类选择器

伪类用于选择DOM树之外的信息，或是不能用简单选择器进行表示的信息。前者包含那些匹配指定状态的元素，比如:visited，:active；后者包含那些满足一定逻辑条件的DOM树中的元素，比如:first-child，:first-of-type，:target。

| 属性         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| :active      | 向被激活的元素添加样式。                                     |
| :focus       | 向拥有键盘输入焦点的元素添加样式。                           |
| :hover       | 当鼠标悬浮在元素上方时，向元素添加样式。                     |
| :link        | 向未被访问的链接添加样式。                                   |
| :visited     | 向已被访问的链接添加样式。                                   |
| :first-child | 向元素的第一个子元素添加样式。                               |
| :lang        | 向带有指定 lang 属性的元素添加样式。                         |
| :checked     | 可以用来定义选中（checked）的元素，比如单选按钮（radio）或多选按钮（checkbox） |

- 基于DOM之外的信息去（比如根据用户和网页的交互）选择元素，示例如下：

  ```css
     a:link    { ... }   /* 未访问过的链接 */
     a:visited { ... }   /* 已访问过的链接 */
     
     a:hover   { ... }   /* 鼠标移到链接上的样式 */
     a:active  { ... }   /* 鼠标在连接上按下时的样式 */
     a:focus   { ... }   /* 获得焦点时的样式 */
     
     <!-- 伪类的代码示例 -->
     <!-- HTML -->
     <nav>
       <ul>
         <li><a href="http://w3.org">W3C</a>
         <li><a href="http://example.com">example.com</a>
         <li><a href="http://www.360.com">360</a>
       </ul>
     </nav>
     
     <label>搜索：<input name="q" type="search"></label>
     
     <!-- CSS -->
     <style>
       a:link {
         color: black;
       }
       a:visited {
         color: gray;
       }
       a:hover {
         color: orange;
       }
       a:active {
         color: red;
       }
       :focus {
         outline: 2px solid red;
       }
     </style>
  ```

###### 伪元素选择器

伪元素为DOM树没有定义的虚拟元素。不同于其他选择器，它不以元素为最小选择单元，它选择的是元素指定内容。比如`::before`表示选择元素内容的之前内容，也就是""；`::selection`表示选择元素被选中的内容。

在CSS3中，伪类与伪元素在语法上也有所区别，伪元素修改为以`::`开头。但因为历史原因，浏览器对以`:`开头的伪元素也继续支持，但建议规范书写为`::`开头。

| 属性           | 描述                           |
| -------------- | ------------------------------ |
| ::first-letter | 选择指定元素的第一个单词       |
| ::first-line   | 选择指定元素的第一行           |
| ::after        | 在指定元素的内容前面插入内容   |
| ::before       | 在指定元素的内容后面插入内容   |
| ::selection    | 选择指定元素中被用户选中的内容 |

```css
<h1>这是h1</h1>
<h2>这是h2</h2>

<!-- CSS -->
<style>
h1::before{
    content:"h1后插入内容"
}
h2::after{
    content:"none"
}
</style>
```

- 注意：

1. 伪元素要配合content属性一起使用
2. 伪元素不会出现在DOM中，所以不能通过js来操作，仅仅是在 CSS 渲染层加入
3. 伪元素的特效通常要使用:hover伪类样式来激活

###### **不同的选择器之间也可以组合。常用的选择器组合示例如下。**

###### 直接组合 EF

```css
     <!-- HTML -->
     <p class="warning">这是一条警告信息</p>
     <div class="warning icon">这是另外一条警告信息</div>
     
     <!-- CSS -->
     /* 标签选择器和类选择器组合 */
     p.warning { color: orange; }
```

###### 后代组合 E F

```html
      <!-- HTML -->
      <article>
        <h1>一级标题</h1>
        <p>第一段第一段。</p>
        <section>
          <h2>二级标题</h2>
          <p>第二段第二段。</p>
        </section>
      </article>
      
      <!-- CSS -->
      <style>
        /* 后代选择器 */
        /* 选中 article 标签下的 所有 p 元素 */
        article p {
          color: coral;
        }
        /* 选中 article 标签下的 section 标签下的 所有 h2 元素*/
        article section h2 {
          border-bottom: 1px dashed #999;
        }
      </style>
```

###### 亲子组合 E > F

```html
      <!-- HTML -->
      <article>
        <h1>一级标题</h1>
        <p>第一段第一段。</p>
        <section>
          <h2>二级标题</h2>
          <p>第二段第二段。</p>
        </section>
      </article>
      
      <!-- CSS -->
      <style>
        /* 亲子选择器 */
        /* 亲子选择器和后代选择器不同的就是：后代选择器可以选中嵌套在标签内部任意层级的标签元素，而亲子选择器只能选中当前标签向内一层的元素，即亲子选择器只能匹配直接后代，通俗一点，就是只能匹配儿子辈，不能匹配孙子辈。*/
        article > p {
          color: limegreen;
        }
      </style>
```

###### 还可以同时为一组选择器定义样式

```css
      /* 下面的选择器将会同时将CSS规则应用在body/h1/h2/h3/h4/h5/h6/ul/ol/li上 */
      body, h1, h2, h3, h4, h5, h6, ul, ol, li {
        margin: 0;
        padding: 0;
      }
      
      [type="checkbox"], [type="radio"] {
        box-sizing: border-box;
        padding: 0;
      }
```

## 推荐资料(扩展学习)

- [CSS选择器笔记](http://www.ruanyifeng.com/blog/2009/03/css_selectors.html)
- [30个你必须熟记的CSS选择器](https://code.tutsplus.com/zh-hans/tutorials/the-30-css-selectors-you-must-memorize--net-16048)

# CSS样式

## 学习目标

- 掌握CSS中字头匹配的算法
- 了解所有的通用字体族
- 掌握基本的CSS属性设置

## 学习内容

#### CSS字体

###### 1. font-family

在CSS中代表字体族，使用逗号可分隔字体族名称，字体初始值由浏览器设置决定，可继承，示例如下所示。

```html
  <!-- HTML -->
  <h1>我是一级标题</h1>
  <p>我是段落，我是段落，我是段落......</p>
  
  <!-- CSS -->
  <style>
    h1 {
      font-family: Helvetica, sans-serif;
    }
    body {
      font-family: Georgia, serif;
    }
  </style>
```

- 字体匹配算法简介如下：
  1. 浏览器先获取一个系统字体列表
  2. 对于元素中每一个字符，使用 font-family 属性及其它属性进行匹配，如果能匹配就暂定该字体
  3. 如果步骤2没有匹配上，选择下一个可选的 font-family 执行步骤2
  4. 如果匹配到一个字体，但是字体中没有该字符，继续对下一个可选的 font-family 执行步骤2
  5. 如果还没有匹配到字体，使用浏览器默认字体
- 通用字体族
  - Serif 衬线体：Georgia、宋体
  - Sans-Serif 无衬线体：Arial、Helvetica、黑体、微软雅黑
  - Cursive 手写体：Caflisch Script、楷体
  - Fantasy 梦幻字体：Comic Sans MS, Papyrus, Zapfino
  - Monospace 等宽字体：Consolas、Courier、中文字体
- 在使用font-family时，英文字体放在中文字体前面，最后总是添加通用字体族。

###### 2. font-size：

- 定义文字的大小，可使用px，百分比，em等作为单位
- 取值：
  - 绝对值：xx-small | x-small | small | medium | large | x-large | xx-large
  - 相对值：larger | smaller
  - 长度
  - 百分数，相对于父元素计算值
- 初始值为medium（有浏览器设置决定，一般为16px），可继承。
- 长度单位em：一般都是相对于元素的font-size计算值的，用在font-size属性上时，是相对于父元素的font-size计算值

###### 3. font-style：

- 定义文字是以倾斜体还是正常方式显示的。
- 取值： `normal` - 文本正常显示 | `italic` - 文本斜体显示 | `oblique` - 文本倾斜显示
- 初识值为normal，可继承

###### 4. font-weight：

- 定义文字的粗细程度
- 取值：normal | bold | bolder | lighter | 100 | 200 | ... | 900
- 初始值为 normal，可继承

###### 5. line-height：

- 定义元素所属的行所占的高度
- 初始值为normal（具体值由浏览器决定），可继承
- 取值：<长度> | <数字> | <百分比>
- 段落文字一般取值为1.4 ~ 1.8

**font缩写：font的众多属性可以集中在一条属性中写，如：**

```css
  h1 {
    /* 斜体 粗细 大小/行高 字体族 */
    font: bold 14px/1.7 Helvetica, sans-serif;
  }
```

#### CSS文本

###### 1. text-align:

- 定义文本在容器内的对齐方式
- 取值：left：左对齐 | right：右对齐 | center：居中 | justify：两端对齐
- 初始值由HTML的dir属性决定，可继承

###### 2. letter-spacing：

- 定义指定字符之间的间距
- 取值：normal | <length>
- 初始值为normal，可继承

###### 3. word-spacing：

- 定义指定单词之间的间距
- 取值：normal | <length>
- 初始值为normal，可以继承

###### 4. text-indent：

- 定义指定文本缩进
- 取值：normal | <length> | <percentage>
- 初始值为0，可继承

###### 5. text-decoration：

- 定义了文本的一些装饰效果，比如下划线、删除线等
- 初始值为none，可继承
- 其它值：underline（下划线） | line-through（删除线） | overline（上划线） | blink（文本闪烁）

###### 6. white-space：

- 定义指定空白字符如何处理
- 取值：normal | nowrap | pre

###### 7. word-break：

- 定义指定是否允许在单词中间换行
- 取值：normal | break-all | keep-all

#### CSS背景

###### 1. background-color

- 背景色
- 默认值是 transparent
- background-color 不能继承，其默认值是 transparent。transparent 有“透明”之意。也就是说，如果一个元素没有指定背景色，那么背景就是透明的，这样其祖先元素的背景才能可见。

###### 2. background-image

- 背景图像
- 如果需要设置一个背景图像，必须为这个属性设置一个 URL 值：`body {background-image: url(/i/eg_bg_04.gif);}`

###### 3. background-repeat

- 默认图像在水平垂直方向上都平铺
- 其他值：repeat-x 在水平方向重复 | repeat-y 在垂直方向重复 | no-repeat 则不允许图像在任何方向上平铺

###### 4. background-position

- 背景定位
- 取值：top、bottom、left、right 和 center | 还可以使用长度值，如 100px 或 5cm，最后也可以使用百分数值
- 一般成对出现，单个时默认第二个值是center：

| 单一关键字 | 等价的关键字                   |
| ---------- | ------------------------------ |
| center     | center center                  |
| top        | top center 或 center top       |
| bottom     | bottom center 或 center bottom |
| right      | right center 或 center right   |
| left       | left center 或 center left     |

###### 4. background-attachment

- 背景关联，防止背景滚动
- 默认情况：如果文档比较长，那么当文档向下滚动时，背景图像也会随之滚动。当文档滚动到超过图像的位置时，图像就会消失。
- 取值：fixed 可以声明图像相对于可视区是固定的

#### CSS链接

###### 链接的样式

- 链接的四种状态：
  1. a:link - 普通的、未被访问的链接
  2. a:visited - 用户已访问的链接
  3. a:hover - 鼠标指针位于链接的上方
  4. a:active - 链接被点击的时刻

```css
a:link {color:#FF0000;}	/* 未被访问的链接 */
a:visited {color:#00FF00;}	/* 已被访问的链接 */
a:hover {color:#FF00FF;}	/* 鼠标指针移动到链接上 */
a:active {color:#0000FF;}	/* 正在被点击的链接 */
```

**注意：** 当为链接的不同状态设置样式时，请按照以下次序规则： a:hover 必须位于 a:link 和 a:visited 之后 a:active 必须位于 a:hover 之后

#### CSS表格

###### 1. border

- 边框
- 使用：border:边框宽度 样式 颜色 例（border: 1px solid blue;）
- 样式：dotted | dashed | solid | double | groove | ridge | inset | outset

```html
<style type="text/css">
p.dotted {border-style: dotted}
p.dashed {border-style: dashed}
p.solid {border-style: solid}
p.double {border-style: double}
p.groove {border-style: groove}
p.ridge {border-style: ridge}
p.inset {border-style: inset}
p.outset {border-style: outset}
</style>

<body>
<p class="dotted">A dotted border</p>

<p class="dashed">A dashed border</p>

<p class="solid">A solid border</p>

<p class="double">A double border</p>

<p class="groove">A groove border</p>

<p class="ridge">A ridge border</p>

<p class="inset">An inset border</p>

<p class="outset">An outset border</p>
</body>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548135856564-d596a221-cfaf-4c42-91db-7e830e1afe4f.png)

###### 2. border-collapse

- 折叠边框
- 默认值：separate 边框会被分开，不会忽略 border-spacing 和 empty-cells 属性。
- 其他值：collapse 边框会合并为一个单一的边框。会忽略 border-spacing 和 empty-cells 属性 | inherit 规定应该从父元素继承 border-collapse 属性的值

###### 3. vertical-align

- 表格文本对齐

| 值          | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| baseline    | 默认。元素放置在父元素的基线上。                             |
| sub         | 垂直对齐文本的下标。                                         |
| super       | 垂直对齐文本的上标                                           |
| top         | 把元素的顶端与行中最高元素的顶端对齐                         |
| text-top    | 把元素的顶端与父元素字体的顶端对齐                           |
| middle      | 把此元素放置在父元素的中部。                                 |
| bottom      | 把元素的顶端与行中最低的元素的顶端对齐。                     |
| text-bottom | 把元素的底端与父元素字体的底端对齐。                         |
| %           | 使用 "line-height" 属性的百分比值来排列此元素。允许使用负值。 |
| inherit     | 规定应该从父元素继承 vertical-align 属性的值。               |

#### CSS轮廓

###### outline

- 轮廓是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用
- 可以按顺序设置如下属性：{outline：outline-color outline-style outline-width}

| 属性          | 描述                             |
| ------------- | -------------------------------- |
| outline       | 在一个声明中设置所有的轮廓属性。 |
| outline-color | 设置轮廓的颜色。                 |
| outline-style | 设置轮廓的样式。                 |
| outline-width | 设置轮廓的宽度。                 |

## 推荐资料 (扩展学习)

- [CSS样式 - W3school](http://www.w3school.com.cn/css/css_background.asp)

# 层叠与继承

## 学习目标

- 掌握CSS中的选择器特异度的概念和计算方法
- 掌握提高CSS属性优先级的方法
- 了解页面中具体哪条样式起作用的方法
- 掌握常见CSS属性的初始值

## 学习内容

我们知道文档中的一个元素可能同时被多个css选择器选中，每个选择器都有一些css规则，这就是层叠。这些规则有可能不矛盾的，自然这些规则将会同时起效，然而有些规则是相互冲突的, 为此需要为每条规则制定特殊性，当发生冲突的时候必须选出一条最高特殊性的规则来应用。特殊性的值表述为4个部分：0，0，0，0。

- 一个选择器的具体特殊性如下确定：
  1. 对于内联样式为：1，0，0，0。
  2. 对于选择器中的ID属性值，加0，1，0，0。
  3. 对于选择器中的类属性值、属性选择、或伪类，加0，0，1，0。
  4. 对于选择器中的元素和伪元素，加0，0，0，1。
  5. 通配符选择器（*），加0，0，0，0。

特殊属性计算值：

```css
h1 {color: red;}/*specificity=0,0,0,1*/
p em {color:purple;}/*specificity=0,0,0,2*/
.grade{color:purple;}/*specificity=0,0,1,0*/
*.bright{color:yellow;}/*specificity=0,0,1,0*/
div#header [href]{color:black;}/*specificity=0,1,1,1 包涵一个属性选择器*/
```

- 如下例子，当不同的CSS选择器都选中了某一个元素，那么哪条规则生效呢？

```css
  <!-- HTML -->
  <article>
    <h1 class="title">我是一级标题</h1>
  </article>
  
  <!-- CSS -->
  <style>
    .title {
      color: blue;
    }
    article h1 {
      color: red;
    }
  </style>

// .title 等级是0010
// article h1等级是0002
// 因此 颜色为blue
```

- CSS中通过特异度来解决样式的冲突，特异度的概念是指，当有两个或者以上拥有相同重要性的css选择器里的声明代码要应用于同一个元素来改变其相同的属性的时候，则特异度最高的选择器的声明代码将优先应用于该元素。CSS特异度示例如下：![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-1/79936261.jpg)

- 简单选择器的特异度级别：（级别越高，优先级越高）
  - Level 0：*
  - Level 1：标签选择器、伪元素
  - Level 2：类、伪类、伪元素
  - Level 3：id
  - Level 4：内联
- 样式的覆盖规则：
  - 根据引入方式确定优先级：优先级由高到低依次为：“内联属性”——>“嵌入”——>“外链”
  - 在同一级别后写的属性覆盖先写的：即就是在文件上代码行号更高的优先级更高
  - 加有“！important”的样式，优先级最高：即无论哪一种情况，只要在样式上加了important,那么该样式的优先级最高。
- CSS样式的来源主要以下三方面：
  - 浏览器对HTML定义的默认样式。
  - 用户定义的样式。
  - 开发者定义的样式，可以有三种形式：
    1. 定义在外部文件（外链样式）：本教程中案例主要是通过这种形式定义样式。
    2. 在页面的头部定义（内联样式）：通过这种形式定义的样式只在本页面内生效。
    3. 定义在特定的元素身上（行内样式）：这种形式多用于测试，可维护性较差。

用户定义的样式表会覆盖浏览器定义的默认样式，然后网页开发者定义的样式又会覆盖用户样式。作为网页的开发者只需要关注开发者样式。

- 那么具体是哪条声明起作用呢？规则如下：
  - 找出匹配到的该属性所有声明
  - 根据规则来源，优先级从低到高：
    1. 浏览器预设
    2. 用户设置
    3. 页面开发者
    4. 含 !important 的网页样式
    5. 含 !important 的用户设置样式
  - 同一来源中，按照特异度排序，越特殊优先级越高
  - 特异度一样时，按照样式书写顺序，后面的优先级高
- 初始值，在CSS中，每个属性都有一个初试值，background-color 的初始值为 transparent，margin-left 的初始值为 0，当然我们也可以将改变过后的值显式的重置为初识值，比如：background-color: initial

# 盒模型

## 学习目标

- 理解CSS盒模型的具体概念
- 掌握margin折叠的发生情况和避免情况
- 掌握CSS盒模型相关的各属性

## 学习内容

- 在一个文档中，每个元素都被表示为一个矩形的盒子。每个盒子都有四个边：外边距边、边框边、内填充边与内容边。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-1/18196405.jpg)

**盒模型允许在其它元素和周围元素边框之间的空间放置元素，针对不同的四边分别的说明如下：**

- Margin（外边距）- 清除边框外的区域，外边距是透明的
- Border（边框）- 围绕在内边距和内容外的边框
- Padding（内边距）- 清除内容周围的区域，内边距是透明的
- Content（内容）- 盒子的内容，可用来显示文本和各类型多媒体文件

**盒模型中的 width：**

- 指定content box的宽度
- 百分数相对于父容器（包含块）的content box宽度

**盒模型中的height：**

- 指定content box高度
- 百分数相对于父容器（包含块）的content box
- 高度只有当包含块的高度不依赖该元素时，百分比高度才生效

**盒模型中的padding：**

- 指内边距
- padding-top, padding-right, padding-bottom, padding-left
- 缩写：padding: top值, right值, bottom值, left值;（上-右-下-左）

**盒模型中的margin：**

- 指外边距
- margin-top, margin-right, margin-bottom, margin-left
-  缩写：margin: top值, right值, bottom值, left值;（上-右-下-左）

**margin折叠**

- 在CSS中，两个或多个相邻的普通文档流中的盒子（可能是父子元素，也可能是兄弟元素）在垂直方向上的外边距会发生叠加，这种情况下形成的外边距称之为margin折叠。
- 以下情况会发生margin折叠：
  - 都属于普通文档流的块级盒子且参与到相同的块级格式化上下文中
  - 没有被padding、border、clear和line box分隔开
  - 都属于垂直相邻盒子边缘：
    - 盒子的 margin-top 和它第一个普通文档流子元素的 margin-top
    - 盒子的 margin-bottom 和它下一个普通文档流兄弟的 margin-top
    - 盒子的 margin-bottom 和它父元素的 margin-bottom
    - 盒子的 margin-top 和 margin-bottom，且没有创建一个新的块级格式上下文，且有被计算为0的min-height，被计算为0或auto的height，且没有普通流子元素
- 那么如何避免margin折叠呢？（如前面所讲，margin折叠满足4个条件：两个或多个、相邻、普通文档流和垂直方向，因此只要破坏其中的任何一点就可以避免margin折叠了。）
  - 浮动元素不会与任何元素发生叠加，也包括它的子元素
  - 创建了 BFC 的元素不会和它的子元素发生外边距叠加
  - 绝对定位元素和其他任何元素之间不发生外边距叠加，也包括它的子元素
  - inline-block 元素和其他任何元素之间不发生外边距叠加，也包括它的子元素
  - 普通流中的块级元素的 margin-bottom 永远和它相邻的下一个块级元素的 margin-top 叠加，除非相邻的兄弟元素 clear
  - 普通流中的块级元素（没有 border-top、没有 padding-top）的 margin-top 和它的第一个普通流中的子元素（没有clear）发生 margin-top 叠加
  - 普通流中的块级元素（height为 auto、min-height为0、没有 border-bottom、没有 padding-bottom）和它的最后一个普通流中的子元素（没有自身发生margin叠加或clear）发生 margin-bottom叠加
  - 如果一个元素的 min-height 为0、没有 border、没有padding、高度为0或者auto、不包含子元素，那么它自身的外边距会发生叠加

**box-sizing：**

- 定义改变盒模型的计算方式 `border-box | content-box`
- border-box：这种情况下的内容宽度或高度包含了元素的border、padding、内容的宽度或高度（此处的内容宽度或高度＝盒子的宽度或高度—边框—内距）

```css
// 设置给某一个div 的css样式
width: 100px;
height: 100px;
border: 1px solid;
padding: 0px 10px;
box-sizing: border-box;
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548227083588-51b7177e-c7b3-4864-82a4-f162e4acd9a5.png)

- content-box：元素的宽度和高度（width/height）等于元素边框宽度（border）加上元素内边距（padding）加上元素内容宽度或高度（content width/ height），也就是元素 `width/height = border + padding + content width / height`

```css
// 设置给某一个div 的css样式
width: 100px;
height: 100px;
border: 1px solid;
padding: 0px 10px;
box-sizing: content-box;
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548227245759-a708d7b2-6d02-4103-98d3-82628ed6c1df.png)

- 一些专家甚至建议所有的Web开发者们将所有的元素的box-sizing都设为border-box。
- 初始值：content-box

**border：**

- 边框的三个要素：
  - border-width：<length> | thin | medium | thick 
  - border-style: none | solid | dashed | dotted | double
  - border-color: <color>
- 四个方向：
  - border-left
  - border-top
  - border-right
  - border-bottom

**overflow：**

- 指的是溢出控制
- 取值：visible | hidden | scroll | auto

| 值      | 描述                                                     |
| ------- | -------------------------------------------------------- |
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。             |
| hidden  | 内容会被修剪，并且其余内容是不可见的。                   |
| scroll  | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto    | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。                 |

- 初始值：visible

**visibility：**

- 该属性的目的是控制元素展示情况
- 取值：visible | hidden | collapse

| 值       | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| visible  | 默认值。元素是可见的。                                       |
| hidden   | 元素是不可见的。                                             |
| collapse | 当在表格元素中使用时，此值可删除一行或一列，但是它不会影响表格的布局。被行或列占据的空间会留给其他内容使用。如果此值被用在其他的元素上，会呈现为 "hidden"。 |
| inherit  | 规定应该从父元素继承 visibility 属性的值。                   |

- 初始值：visible

# CSS布局

## 学习目标

- 掌握CSS中的定位模式
- 理解块级格式化上下文的概念及其特性
- 理解块级格式化上下文的创建及其作用
- 掌握元素float的具体使用方法
- 掌握清除元素浮动的方法

## 学习内容

- 定位就是当前元素相对于其他元素的位置，当前元素应该出现在哪里，这里的其他元素可以指父元素、浏览器窗口本身。
- 偏移量：偏移量包含 top、right、bottom、left四个属性

##### Position(定位)

- **static** 定义：元素默认值，没有定位，遵循正常的文档流对象，不会受到 top、bottom、left、right 偏移量的影响

```html
<style>
.static {
    position: static;
    border: 1px solid red;
}
</style>

<h2>position: static;</h2>
<p>使用 position: static; 定位的元素，无特殊定位，遵循正常的文档流对象:</p>
<div class="static">
该元素使用了 position: static;
</div>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548294652338-60fde536-44dc-4833-9e70-be8c6f99a6bd.png)

###### **absolute**

- 定义：绝对定位，当前元素的位置相对于父元素（没有父元素默认是`<html>`元素）的位置

```html
<style>
.absolute{
	position:absolute;
	left:100px;
	top:70px;
	border: 1px solid red;
}
</style>
<div class="absolute">这是一个绝对定位了的标题</div>
<p>用绝对定位(position:absolute)</p>
<p>标题下面放置距离左边的页面100 px和距离页面的顶部70 px的元素</p>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548297637957-a6badf6e-8095-4766-93c0-45054db333c4.png)

- absolute 定位使元素的位置与文档流无关，因此不占据空间。
- absolute 定位的元素和其他元素重叠。

###### **fixed**

- 定义：绝对定位，当前元素相对于浏览器的窗口的位置，元素通过偏移量属性：top、bottom、left、right进行规定

```html
<style>
.fixed
{
	position:fixed;
	top:10px;
	right:10px;
	border:1px solid red;
}
</style>
<p class="fixed">这是一个position:fixed定位的元素</p>
<p>元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动：</p>
<p>元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动：</p>
	<p>元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动：</p>
	<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
	<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
	<p>元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动：</p>
	<p>元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动：</p>
</body>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548299025662-ac14cdeb-0764-4ec8-adea-b8adc32bf96d.png)

- 元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动
- Fixed定位使元素的位置与文档流无关，因此不占据空间。
- Fixed定位的元素和其他元素重叠。

###### **relative**

- 定义：相对定位，当前元素的位置是相对其正常位置进行定位。元素通过偏移量属性：top、bottom、left、right进行规定

```html
<style>
.relative
{
	position:relative;
	top:-40px;
	border:1px solid red
}
</style>
<h2>这是一个没有定位的标题</h2>
<h2 class="relative">这个元素是通过position:relative定位的</h2>
<h2>这是一个没有定位的标题</h2>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548299817149-fe6919cf-f55b-4b74-bd8e-92ef0e8b92e9.png)

###### **sticky**

- 定义：粘性定位的元素是依赖于用户的滚动，在 position:relative 与 position:fixed 定位之间切换。它的行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置。

```html
<style>
.sticky {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  padding: 5px;
  border: 1px solid red;
}
</style>
<p>尝试滚动页面。</p>
<div class="sticky">通过position:sticky 定位</div>
<div style="padding-bottom:2000px">
  <p>滚动我</p>
  <p>来回滚动我</p>
  <p>滚动我</p>
  <p>来回滚动我</p>
  <p>滚动我</p>
  <p>来回滚动我</p>
</div>
```

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548300263879-158a2dec-784a-44ba-87ce-30e539cdbb53.png)

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548300270650-f047f437-ecb4-4510-bbd6-f9329031d6de.png)

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

###### CSS布局

![img](https://s3.cn-north-1.amazonaws.com.cn/tws-upload/images/1548315554191-094db4f3-c923-489e-8c79-f231b16465f7.png)

- 二列布局：侧边栏固定宽度，内容栏自适应宽度
- 三列布局：两侧两列固定宽度，内容栏自适应宽度

**1. float+margin**

```html
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

```html
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

###### **圣杯布局(float + 负margin)**

```html
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

###### **双飞翼布局(float + 负margin )**

```html
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

## 推荐资料（扩展学习）

- [Flex 布局教程：语法篇 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html?utm_source=tuicool)
- [Flex 布局教程：实例篇 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/07/flex-examples.html)
- [学习CSS布局](http://zh.learnlayout.com/)
- [CSS 教程 - W3school](http://www.w3school.com.cn/css/index.asp)

# CSS调试

## 学习目标

- 掌握基本的CSS调试技巧

## 学习内容

- 和HTML一样，CSS是宽容的，即在CSS中，如果一个声明是无效的（包含语法错误，或者浏览器不支持该特性），浏览器会完全忽略它，然后转向它找到的下一个，但是并不会对其进行报错。
- 对于选择器也是一样的，如果选择器是无效的，那么它就不会选择到任何元素，而整个规则也不会再做任何事情，浏览器只会继续执行下一个规则，同时也会产生和设计稿的偏差。
- 现在所有的浏览器都有内置的页面开发者工具，如：Chrome的DevTools ，Firefox的page inspector tool。
- 通过在Chrome 中右键选择“审查元素”即可打开Devtools，或者单击F12(Windows系统)/Cmd+Opt+I(Mac OSX系统)。打开后的DevTools如下图所示。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/68781339.jpg)

- 可以看到其中有以下几个模块：

  - Element 标签页： 用于查看和编辑当前页面中的 HTML 和 CSS 元素。
  - Network 标签页：用于查看 HTTP 请求的详细信息，如请求头、响应头及返回内容等。
  - Source 标签页：用于查看和调试当前页面所加载的脚本的源文件。
  - TimeLine 标签页： 用于查看脚本的执行时间、页面元素渲染时间等信息。
  - Profiles 标签页：用于查看 CPU 执行时间与内存占用等信息。
  - Resource 标签页：用于查看当前页面所请求的资源文件，如 HTML，CSS 样式文件等。Audits 标签页：用于优化前端页面，加速网页加载速度等。
  - Console 标签页：用于显示脚本中所输出的调试信息，或运行测试脚本等。

- 下面我们重点讲解下其中我们最常使用的两个模块：

  - Element模块

    - 我们在DevTools中定位在Element模块，通过鼠标悬浮在某一个DOM节点上，那么在左侧的页面上改元素就会被高亮显示。

    ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/43163660.jpg)

    - 在Element面板中，我们可以看到还有一个子面板叫Style，在Style面板中，可以看到某一个元素的所有定义的CSS属性，并且我们在Style面板中修改CSS属性可以在页面中即时生效。

    ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/90220629.jpg)

  - Console模块

    - 我们在DevTools中定位在Console模块，当前模块可以用来查看和调试当前页面所加载的脚本的源文件。换句话说，我们可以在Console模块中执行JavaScript脚本。

    ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/22453939.jpg)

- 若我们的页面中出现了一些错误，我们打开DevTools的Console面板也可以看到在该面板中是有页面的报错的。如下：

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/64479792.jpg)

- 当然，Chrome DevTools的功能远比Element面板和Console面板中的内容更加强大，更多的DevTools使用技巧我们将在后续的任务卡中解锁。

- CSS 验证

  - 和HTML验证器（http://jigsaw.w3.org/css-validator/）可以验证HTML的规范程度一样，也存在CSS验证器（http://jigsaw.w3.org/css-validator/），我么可以在特定的URL上验证CSS，或者通过上传本地文件，或者直接使用CSS属性进行输入验证。

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-2/66654145.jpg)

## 推荐资料(扩展学习)

- [调试 CSS 的方法](http://web.jobbole.com/87818/)