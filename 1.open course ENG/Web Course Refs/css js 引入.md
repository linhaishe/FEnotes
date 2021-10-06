## css 引入

**如何在HTML中引用CSS**

- 想要在HTML文档中应用CSS，有三种方法：
  
1. 外链：
  
    ```html
    <link rel="stylesheet" href="/path/to/style.css">
    ```

2. 嵌入：

  ```html
   <style type="text/css">
      li { margin: 0; list-style: none; }
      p { margin: 1em 0; }
    </style>
  ```
  
3. 内联：

    ```html
    <p style="margin:1em 0">Example Content</p>
    ```

当同一个 HTML 元素被不止一个样式定义时，会使用哪个样式呢？

一般而言，所有的样式会根据下面的规则层叠于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。

1. 浏览器缺省设置
2. 外部样式表
3. 内部样式表（位于 `<head>` 标签内部）
4. 内联样式（在 HTML 元素内部）

## js 引入

**1. 内部引用**

- 通过HTML文档内的`script`标签加载JavaScript代码。示例如下：

```html
    <script type="text/javascript">
      document.write("Hello World!");
    </script>
```

通过此方式就可以在当前页面中引入`script`标签中的JavaScript代码。

**2. 外部引用**

- 也是使用HTML文档的`script`标签，但是要使用`script`标签的`src`属性，指向外部JavaScript文件的路径。示例如下：

```html
    <script src="./main.js" />
```

由于HTML文档是由上向下对页面元素进行解析的，所以在一个HTML文档中，所有的``元素都会按照它们在页面中出现的顺序依次被解析，默认情况下，只有在解析完前面的``元素中的代码之后，才会开始解析后面的``元素中的代码，所以为防止网页加载缓慢，也可以把非关键的JavaScript放到网页最后，即主要内容后面，``元素的前面。示例如下：

```html
    // other code ...    
        <script type="text/javascript" src="./main.js"></script>
      </body>
    </html>
```

- 使用内部引用的方法在HTML中嵌入JavaScript代码虽然没有问题，但一般认为最好的做法还是尽可能使用外部文件来包含JavaScript代码。不过，并不存在必须使用外部文件的硬性规定，但支持使用外部文件的人多会强调如下优点：
  1. 可维护性：遍及不同HTML页面的JavaScript会造成维护问题。但把所有JavaScript文件都放在一个文件夹中，维护起来就轻松多了。而且开发人员因此也能够在不触及HTML标签的情况下，集中精力编辑JavaScript代码。
  2. 可缓存：浏览器能够根据具体的设置缓存链接的所有外部JavaScript文件。也就是说，如果有两个页面都使用同一个文件，那么这个文件只需下载一次。因此，最终结果就是能够加快页面加载的速度。
  3. 适应未来：统一定义JavaScript代码，方便查看，同时使代码更安全，可以压缩，也可以加密某个JavaScript文件。