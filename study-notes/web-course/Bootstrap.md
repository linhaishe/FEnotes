## 一、Bootstrap介绍

[Bootstrap beginner](https://getbootstrap.net/docs/getting-started/introduction/)

[Bootstrap](https://www.altcademy.com/explain/bootstrap)是一个CSS框架，可让Web前端开发人员非常快速地为网站添加样式和结构。Bootstrap提供了一组有关间距、版式、颜色、交互行为等的标准。

CSS 框架本质上是一组用于 HTML 元素的结构化样式。Bootstrap 框架只是一个 CSS 文件，其中包含 Bootstrap 团队设计好的样式。

Bootstrap 3于2013年发布，至今仍很流行。在访问量最高的10万个网站中，有[15％](https://trends.builtwith.com/docinfo/Twitter-Bootstrap)是使用Bootstrap构建的。即使2017年发布了新版本的Bootstrap 4，也值得学习Bootstrap 3，因为许多公司仍在使用它。

除了Bootstrap 3外，还有其他选择，流行的包括[Foundation](https://foundation.zurb.com/)、[Bulma](https://bulma.io/)、[Semantic UI](https://semantic-ui.com/)，应该学会至少使用一个CSS框架。

- **安装**

  有多种方法可以在项目中添加Bootstrap。最简单的方法是链接到Bootstrap的官方CDN（content delivery network - 内容分发网络），CDN处理向客户端提供Bootstrap的CSS文件。另一种方法是将Bootstrap本地安装到项目中。如果没有联网，这很管用。你会了解每种方法的优缺点。

- **响应式网格系统** 

  可能Bootstrap最受欢迎的功能是其网格系统。需要足够了解它，才能轻松创建复杂的嵌套网格结构，常用于快速地为Web内容创建响应式布局。响应式布局意味着布局将根据查看设备的屏幕尺寸而改变。

- **Bootstrap的样式标准** 

  Bootstrap带有一套标准化的样式，用于排版、颜色、按钮、表单、表格、图像等。它还有大量的帮助器类供选择，可以将预定义的样式添加到元素中。

- **响应式CSS**

  将学习如何编写仅在特定屏幕宽度范围内有效的CSS。这称为响应式CSS，它是Bootstrap响应式网格的制作方式。知道这一点将能够为网页创建自定义响应样式。

- **使用浏览器devTools进行响应式开发** 

  使用响应式CSS时，在不同设备的屏幕尺寸上快速查看结果将很有用。大多数Web浏览器devtools都有一种设备模式，可以让你精确地执行此操作，使用此功能可以提高效率。

- **响应式网站克隆** 

  配备了Bootstrap 3，尝试构建响应式网页，选择几个简单的响应页面进行克隆。

## 二、Bootstrap安装

[安装教程](https://www.html.cn/bootstrap/getting-started/)

有几种方法可以使用 Bootstrap 框架。你可以下载文件并将其链接到 HTML，也可以使用[内容分发网络](https://baike.baidu.com/item/CDN)（CDN - Content Delivery Network）。

下载文件并将其存储在服务器上，只要服务器正常运行，用户就可以使用它们。

如果你使用 CDN，则可用性取决于 CDN 服务商。如果 CDN 服务商的服务器出现故障，你的网站将无法正确显示，因为阅读者无法从 CDN 获取 Bootstrap 文件。

在 CDN 和下载文件之间选择取决于工作环境。

### 使用本地文件

在本地开发时，需要联网才能使 CDN 链接正常工作。假若在没有联网特殊的情况下，需下载要该文件到本地。

要在本地使用 Bootstrap 文件，首先从 [Bootstrap官网](https://getbootstrap.com/)下载 Bootstrap 文件。单击"下载"按钮，将下载一个 zip 文件。解压缩文件夹，你会看到里面有三个文件夹，"css"，"fonts"和"js"。

创建一个**新项目**文件夹，用来保存此处使用的示例。

现在，我们只需要关注 CSS 文件。进入"css"文件夹并将"bootstrap.css"文件复制到你的新项目文件夹中。你应该在项目中有一个单独的文件夹（该文件夹命名为"css"），你可以在此文件夹中保存所有 CSS 文件。现在，你只需要在``标签中添加指向此 CSS 文件的链接。

```html
<head>
  <!-- Bootstrap -->
  <link rel="stylesheet" type="text/css" href="/css/bootstrap.css" />
  <!-- Custom CSS file -->
  <link rel="stylesheet" type="text/css" href="/css/custom.css" />
</head>
```

Bootstrap 链接标签之后添加自定义 CSS 文件链接标签。否则，由于级联效应，你写的用于覆盖 Bootstrap 样式的自定义样式将被忽略。 

### 使用 CDN

添加 Bootstrap 的另一种方法是使用 CDN。我们可以使用托管 Bootstrap 的 CDN 供应商 MaxCDN。转到[BootStrapCDN](https://www.bootstrapcdn.com/)以获取最新版本，中国境内网站推荐 [twitter-bootstrap | BootCDN ](https://www.bootcdn.cn/twitter-bootstrap/)。获得 href 链接后，你应该在``元素中放置一个链接标签，如下所示。

这与上述方法目的相同，你的浏览器将从 MaxCDN 的服务器获取 Bootstrap 文件。

```html
<head>
  <!-- Bootstrap CDN Link -->
  <link
    rel="stylesheet"
    type="text/css"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
  />
</head>
```

如果你决定使用 CDN 链接 Bootstrap 文件，则每当访问者访问你的网站时，你都需要依靠 CDN 服务商的可用性来提供文件。如果你的 CDN 服务商发生故障，你的网站将无法正常呈现。因此，首选在服务器上本地托管这些依赖项文件。因为只要你的服务器启动并运行，你就确定访问者将获得呈现你网站所需的所有文件。

总而言之，我建议在本地托管文件，原因如下：

1. 你确定只要你的服务器正在运行，就会提供该文件
2. 即使你未连接到 Internet，也可以继续开发

但有一点需要注意。本地托管需要你自己维护库，例如定期将 Bootstrap 的本地副本更新到最新版本。

### 压缩文件

你可以在下载 Bootstrap 中看到有一个"bootstrap.min.css"文件。此文件与"bootstrap.css"文件基本相同，只是它已被被压缩了。

压缩过程是删除空格的过程，因此能减小文件大小。使用 VS Code 打开这两个文件，你会看到"bootstrap.css"间隔很好并且缩进，而"bootstrap.min.css"则被压缩成一大段代码。

但它们真的是一码事。查看前三个规则集，你可以看到缩小的文件跟原始文件一样，只是其中的空格和新行被删除了。

```css
html {
  font-family: sans-serif;
  -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}

html{font-family:sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}
```

### View Port 设置

Bootstrap 是为了"移动优先"而设计的，这意味着它是基于移动设备构建的。要确保在移动设备上正确呈现，请将 veiwport 元标签添加到``元素中。

`width=device-width` 设置将你网站的宽度设置为你正在查看网站的设备的宽度。`initial-scale=1` 定义设备宽度（纵向模式下的设备宽度或横向模式下的设备高度）与 viewport 大小之间的比率。

换句话说，它设置初始缩放级别，将其设置为 1 表示网站的 1 个 CSS 像素等于屏幕的 1 个像素。这几乎就是你所有需要设置的，以使你的网站适应不同的屏幕尺寸（响应）。

```html
<head>
  ...
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
```

如果你希望让你的网站更像是原生移动网络，则可以禁用移动设备上的缩放功能。将 `user-scalable=no` 添加到 content 属性并设置`maximum-scale = 1`以防止用户放大。

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

> *注意：建议不要禁用缩放。只有在你的网站非常适合移动设备时才这样做。否则，你的用户无法自适应查看的内容。*

### CSS 重置

Bootstrap 也使用 「CSS 重置」，但它使用一个名为 Normalize.css 的重置而不是 Eric Myer，这是一个硬重置。标题相对其字体大小仍然保留，且外边距也保留。但应用的是标准样式，以便你的内容在不同浏览器中呈现一致。你可以在[此处](https://github.com/necolas/normalize.css/blob/master/normalize.css)查看整个 Normalize.css 文件。

## 三、响应式网格系统

Bootstrap 4 需要一个容器元素来包裹网站的内容。

我们可以使用以下两个容器类：

- .container 类用于固定宽度并支持响应式布局的容器。
- .container-fluid 类用于 100% 宽度，占据全部视口（viewport）的容器。

```HTML
<div class="container">
  <h1>我的第一个 Bootstrap 页面</h1>
  <p>这是一些文本。</p> 
</div>
```

```HTML
<div class="container-fluid">
  <h1>我的第一个 Bootstrap 页面</h1>
  <p>使用了 .container-fluid，100% 宽度，占据全部视口（viewport）的容器。</p> 
</div>
```

 随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多 12 列。Bootstrap 4 的网格系统是响应式的，列会根据屏幕大小自动重新排列

### 网格类

Bootstrap 4 网格系统有以下 5 个类:

- .col- 针对所有设备
- .col-sm- 平板 - 屏幕宽度等于或大于 576px
- .col-md- 桌面显示器 - 屏幕宽度等于或大于 768px)
- .col-lg- 大桌面显示器 - 屏幕宽度等于或大于 992px)
- .col-xl- 超大桌面显示器 - 屏幕宽度等于或大于 1200px)

### 网格系统规则

Bootstrap4 网格系统规则:

- 网格每一行需要放在设置了 `.container` (固定宽度) 或 `.container-fluid` (全屏宽度) 类的容器中，这样就可以自动设置一些外边距与内边距。
- 使用行来创建水平的列组。
- 内容需要放置在列中，并且只有列可以是行的直接子节点。
- 预定义的类如 **.row** 和 **.col-sm-4** 可用于快速制作网格布局。
- 列通过填充创建列内容之间的间隙。 这个间隙是通过 **.rows** 类上的负边距设置第一行和最后一列的偏移。
- **网格列是通过跨越指定的 12 个列来创建**。 例如，设置三个相等的列，需要使用用三个**.col-sm-4** 来设置。
- Bootstrap 3 和 Bootstrap 4 最大的区别在于 Bootstrap 4 现在使用 flexbox（弹性盒子） 而不是浮动。 Flexbox 的一大优势是，没有指定宽度的网格列将自动设置为**等宽与等高列** 。 如果您想了解有关Flexbox的更多信息，可以阅读我们的CSS Flexbox教程。



### 创建相等宽度的列，Bootstrap 自动布局

```html
<!-- 第一个例子：控制列的宽度及在不同的设备上如何显示 -->
<div class="row">
  <div class="col-*-*"></div>
</div>
<div class="row">
  <div class="col-*-*"></div>
  <div class="col-*-*"></div>
  <div class="col-*-*"></div>
</div>
 
<!-- 第二个例子：或让 Bootstrap 者自动处理布局 -->
<div class="row">
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
</div>
```

 **移动设备上，即屏幕宽度小于 576px 时，四个列将会上下堆叠排版** 

```html
<div class="row">
    <div class="col-sm-3" style="background-color:lavender;">.col-sm-3</div>
    <div class="col-sm-3" style="background-color:lavenderblush;">.col-sm-3</div>
    <div class="col-sm-3" style="background-color:lavender;">.col-sm-3</div>
    <div class="col-sm-3" style="background-color:lavenderblush;">.col-sm-3</div>
  </div>
</div>

<div class="row">
  <div class="col-sm-4">.col-sm-4</div>
  <div class="col-sm-8">.col-sm-8</div>
</div>
```

## 四、Bootstrap4 文字排版

[Bootstrap4 文字排版菜鸟教程]( https://www.runoob.com/bootstrap4/bootstrap4-typography.html )

Bootstrap 4 默认的 **font-size** 为 16px, **line-height** 为 1.5。

默认的 **font-family** 为 "Helvetica Neue", Helvetica, Arial, sans-serif。

所有的 `<P>` 元素 **margin-top: 0** 、 **margin-bottom: 1rem** (16px)。

| 类名                    | 描述                                                         |
| :---------------------- | :----------------------------------------------------------- |
| **.font-weight-bold**   | 加粗文本                                                     |
| **.font-weight-normal** | 普通文本                                                     |
| **.font-weight-light**  | 更细的文本                                                   |
| **.font-italic**        | 斜体文本                                                     |
| **.lead**               | 让段落更突出                                                 |
| **.small**              | 指定更小文本 (为父元素的 85% )                               |
| **.text-left**          | 左对齐                                                       |
| **.text-center**        | 居中                                                         |
| **.text-right**         | 右对齐                                                       |
| <h1> - <h6>             | Bootstrap 中定义了所有的 HTML 标题（h1 到 h6）的样式         |
| **.display**            | 控制标题的样式: .display-1, .display-2, .display-3, .display-4 |
| <small>                 | 创建字号更小的颜色更浅的文本                                 |
| <mark>                  | 高亮                                                         |
| <abbr>                  | 显示在文本底部的一条虚线边框                                 |
| <blockquote>            |                                                              |
| <dl>                    | data list                                                    |
| <code>                  | 放入代码片段                                                 |
| <kbd>                   | Keyboard Inputs                                              |
| <pre>                   | 定义 HTML <pre>元素的样式                                    |

## 五、color

test-color

| 类名                | 描述                             |
| ------------------- | -------------------------------- |
| **.text-muted**     | 柔和的文本                       |
| **.text-primary**   | 重要的文本                       |
| **.text-success**   | 执行成功的文本                   |
| **.text-info**      | 代表一些提示信息的文本           |
| **.text-warning**   | 警告文本                         |
| **.text-danger**    | 危险操作文本                     |
| **.text-secondary** | 副标题                           |
| **.text-dark**      | 深灰色文字                       |
| **.text-light**     | 浅灰色文本（白色背景上看不清楚） |
| **.text-white**     | 白色文本（白色背景上看不清楚）   |

bg-color

| 类名                     | 描述             |
| ------------------------ | ---------------- |
| .bg-primary text-white   | 重要的背景颜色   |
| .bg-success text-white   | 执行成功背景颜色 |
| .bg-info text-white      | 信息提示背景颜色 |
| .bg-warning text-white   | 警告背景颜色     |
| .bg-danger text-white    | 危险背景颜色     |
| .bg-secondary text-white | 副标题背景颜色   |
| .bg-dark text-white      | 深灰背景颜色     |
| .bg-light text-dark      | 浅灰背景颜色     |

## 六、 Bootstrap4 基础表格

 通过 **.table** 类来设置基础表格的样式 

| 类名            | 描述                               |
| --------------- | ---------------------------------- |
| .table          | 基础表格                           |
| .table-striped  | 条纹                               |
| .table-bordered | 为表格添加边框                     |
| .table-hover    | 每一行添加鼠标悬停效果（灰色背景） |

```css
//example 看到每个class 都会加上.table
<table class="table table-striped">
```

## 七、Bootstrap4 图像形状

| 类名              | 描述                       |
| ----------------- | -------------------------- |
| .rounded          | 图片显示圆角效果           |
| .rounded-circle   | 椭圆形图片                 |
| .img-thumbnail    | 设置图片缩略图(图片有边框) |
| .float-left/right | 图片左、右对齐             |
| .img-fluid        | 设置响应式图片             |





















