# info

原本的css不存在任何的逻辑,不能使用变量,不能直接运算,不能使用函数,不能嵌套。

[official site](https://lesscss.org/)

**不要为了用less用less**

# less和sass区别

1. 最早先出来sass，但是最早的sass语法不好用。
2. less，进行改进。在原本css的写法上进行增加。
3. sass看到这个情况，增加了一种写法，也是在原本css基础上进行。
4. less可以在浏览器运行。也可以在node上运行。
5. sass只能在服务器上运行需要安装ruby软件

# 引入方式

1. 在 Node.js 环境中使用 Less ：

```js
npm install -g less
> lessc styles.less styles.css
```

2. 在浏览器环境中使用 Less ：(不建议使用,必须运行在服务器的环境下maybe)

```html
<link rel="stylesheet/less" type="text/css" href="styles.less" />
<script src="//cdn.jsdelivr.net/npm/less@3.13" ></script>
```

3. 通过编辑器的插件自动转换

   a. Vscode install easy less

   b. 打开vscode里的 setting.json,填入以下信息，此信息来自easy less info中

   ```js
   {
     "less.compile": {
       //是否压缩
       "compress": true, // true => remove surplus whitespace
         //是否生成源map文件
       "sourceMap": true, // true => generate source maps (.css.map files)
         //是否生成css文件
       "out": false // false => DON'T output .css files (overridable per-file, see below)
     }
   }
   ```

   c. 在主html文件中创建link，引入的是less1.css文件，此时没有less1.css，我们需要通过写less1.less文件+编辑器插件自动转换成less1.css文件

   ```html
   <!--主html文件--> 
   <link rel="stylesheet" href="less1.css">
   ```

   d. 创建less1.less文件

   e. 保存后less1.css文件自动生成

   * .map文件一般都是配合压缩文件来使用，一般在生产环境会同时上传.min文件.map文件。平常加载项目的时候不会加载.map文件 只有在用户打开控制台的时候才会加载。程序员方便在前端查看代码修改bug。

4. 通过框架里面的自动化编译工具进行转换

   ​	之后的框架部分再说明

# less grammar

```less
@length:100px;
@len:50px;
//变量运算
div{
    width: @length + @len;
    height: @length + 20px;
    background: red;
    color: blue;
}

//变量用在选择器名称的情况下
@a:active;

.@{a}{
    width: @length;
}

//变量在拼接字符串的时候
//取出所有图片地址的相同部分
@url:'/http/uploads/';

div{
    background: url('@{url}1.png');
}
```

1. 变量: @变量名:值
2. 变量运算: 
   -  @a + @b
   - @a + 100px
   - @a - 20px
   - 减法要有空格。在css里面没有空格是连字符
3. 变量用在选择器名称的情况下
4. 变量在拼接字符串的时候如何使用
5. 混入mixins，多个样式的重复利用,把它当作重复的代码进行重复利用。

```less
.red{
    color: #fff;
    background: red;
}

//使得div拥有.red的属性
.div1{
    width: 100px;
    height: 100px;
    .red();
}

.div2{
    .red();
}

//定义函数
.border(@width,@style,@color){
    border:@width @style @color;
}

.div2{
  //调用函数
  //等于border: 1px solid red;
    .border(1px, solid, red)
}
.div3{
    .border(10px, dashed, yellow) 
}
```

6. 嵌套

```less
#div1{
    height: 100px;
    width: 100px;

    .header1{
        width: 100px;
        height: 100px;
        background: red;

        p{
            color: red;
        }
    }

    .header2{
        background: yellow;
      //伪类使用
        a{
            color: red;
            &:hover{
                color: blue;
            }
            &::before{
                content: '';
                display: block;
            }
        }
    }
}
```

7. 引入其他less文件

```css
`@import url('less3.less');`
p{color: red;}
```













