# 使用 Chrome DevTools 进行响应式开发

如何正确高效的定位到程序中存在的问题，进行bug的调试，也是一项基本的技能。在我们进入任务卡编写更加复杂的代码之前，我们有必要先学习一下如何利用Chrome DevTools进行页面的调试。

几乎所有的现代浏览器都支持直接在浏览器中对页面进行**调试**，开发工具在浏览器中是一个单独的页面，以使我们调试起来更加方便。在这节中，我们以Chrome为例，因为Chrome的DevTools在调试方面的功能是最丰富的。

我们可以通过下列方式打开DevTools：

- 在页面空白处右键单击，选择**审查元素**。
- 点击`F12`(Windows系统)/`Cmd+Opt+I`(Mac OSX系统)。 DevTools打开后如下图所示：

![img](https://tws-challenge.github.io/javascriptFullStackPre-Course/assets/devtools1.png)

可以看到其中有以下几个模块：

- Element 标签页： 用于查看和编辑当前页面中的 HTML 和 CSS 元素。
- Network 标签页：用于查看 HTTP 请求的详细信息，如请求头、响应头及返回内容等。
- Source 标签页：用于查看和调试当前页面所加载的脚本的源文件。
- TimeLine 标签页： 用于查看脚本的执行时间、页面元素渲染时间等信息。
- Profiles 标签页：用于查看 CPU 执行时间与内存占用等信息。
- Resource 标签页：用于查看当前页面所请求的资源文件，如 HTML，CSS 样式文件等。
- Audits 标签页：用于优化前端页面，加速网页加载速度等。
- Console 标签页：用于显示脚本中所输出的调试信息，或运行测试脚本等。

下面我们重点讲解下其中我们最常使用的两个模块：

- Element模块 我们在DevTools中定位在Element模块，通过鼠标悬浮在某一个DOM节点上，那么在左侧的页面上改元素就会被高亮显示。

![img](https://tws-challenge.github.io/javascriptFullStackPre-Course/assets/devtools2.png)

在Element面板中，我们可以看到还有一个子面板叫Style，在Style面板中，可以看到某一个元素的所有定义的CSS属性，并且我们在Style面板中修改CSS属性可以在页面中即时生效。

![img](https://tws-challenge.github.io/javascriptFullStackPre-Course/assets/devtools3.png)

- Console模块 我们在DevTools中定位在Console模块，当前模块可以用来查看和调试当前页面所加载的脚本的源文件。换句话说，我们可以在Console模块中执行JavaScript脚本。

![img](https://tws-challenge.github.io/javascriptFullStackPre-Course/assets/devtools4.png)

> **提示：**在接下来Pre-Course中JavaScript基础的练习，建议大家都在浏览器DevTools中的Console面板进行练习。

若我们的页面中出现了一些错误，我们打开DevTools的Console面板也可以看到在该面板中是有页面的报错的。如下：
我们的JavaScript脚本为：

```
<script>
    var lastName = 'Hello';
    console.log(lastName + firstName);
</script>
```

那么在Console面板中就会收到以下报错：

![img](https://tws-challenge.github.io/javascriptFullStackPre-Course/assets/devtools5.png)

报错信息提示我们`firstName`未定义，并且出错的位置在`index.html`的第`14`行,那么我们就可以更加高效的对页面进行调试和bug的修改。

当然，Chrome DevTools的功能远比Element面板和Console面板中的内容更加强大，更多的DevTools使用技巧我们将在后续的任务卡中解锁。

# 推荐资料

- [Chrome DevTools 概览](https://leeon.gitbooks.io/devtools/content/learn_basic/overview.html)
- [前端开发Chrome调试技巧]( https://blog.csdn.net/nanjingshida/article/details/72775687 )
- [Chrome 开发者工具](http://www.css88.com/doc/chrome-devtools/)