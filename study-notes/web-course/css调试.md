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