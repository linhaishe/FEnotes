Chapter 1: Structure

## main content

### HTML

HTML stands for HyperText Markup Language

### element

HTML 文档由 HTML 元素定义，HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。

### HTML元素语法

HTML 元素以开始标签起始
HTML 元素以结束标签终止
元素的内容是开始标签与结束标签之间的内容
某些 HTML 元素具有空内容（empty content）
空元素在开始标签中进行关闭（以开始标签的结束而结束）
大多数 HTML 元素可拥有属性

### tags

Elements are usually made up of two tags: an opening tag and a closing tag. (The closing tag has an extra forward slash in it.) 

### attribute

`<body>`

`<head>`

`<title>`

`<main>`

## summary

HTML pages are text documents.

HTML uses tags (characters that sit inside angled brackets) to give the information they surround special meaning.

Tags are often referred to as elements.

Tags usually come in pairs. 

Opening tags can carry attributes, which tell us more about the content of that element.

Attributes require a name and a value.

# Chapter 2 : Text

## structure markup

1. `<h></h>`

```html
<h1> this is a main heading</h1>
<h2> this is a level 2 heading</h2>
<h6>this is a level 6 heading</h6>
an <h1>  element is the largest, and the contents of 
an <h6>  element is the smallest.
```

2. `<p></p>`

`<p> type your content here</p>`

a browser will show each paragraph on a new line with some space between it and any subsequent paragraphs.

3. `<b></b>`

Bold,make some keywords in bold
`<b> we can make characters appear bold </b>`
`<p> this is how we make a word appear <b> in bold </b></p>`

4. `<i></i>`

Italic
`<i>we can make characters appear italic</i>`
`<p> this is how we make a word appear <i> in italic </i></p>`

5. `<sup></sup>`

superscript(定义上标字

`<p> on the 4<sup>th</sup>of September you will learn about E-MC<sup>2</sup></p>`

	<p> on the 4<sup>th</sup>of September you will learn about E-MC<sup>2</sup></p>

6. `<sub></sub>`

subscript(定义下标字

`<p> the amount of CO<sub>2</sub> in the atmosphere grew by 2ppm in 2009 </p>`

<p> the amount of CO<sub>2</sub> in the atmosphere grew by 2ppm in 2009 </p>
7. white space <mark>example</mark>

8. empty elements

`<br/>`

line breaks空行/回车

```html
<p>The Earth <br/>gets one hundred tons heavier every day<br/>due to falling space dust</p>
```

<p>The Earth <br/>gets one hundred tons heavier every day<br/>due to falling space dust</p>
`<hr/>`

horizental rules 横线

```html
<p> Venus is the only planet that rotates clockwise.</p>
<hr/>
<p>Jupiter is bigger than all the other planes combined.</p>
```

<p> Venus is the only planet that rotates clockwise.</p>
<hr/>
<p>Jupiter is bigger than all the other planes combined.</p>
## semantic markup

There are some text elements that are not intended to affect the structure of your web pages, but they do add extra information to the pages — they are known as semantic markup.

1. `<strong></strong>`

strong importance

	<p><strong>Beware:</strong> Pickpockets operate in this area.</p>

2. `<em></em>`

emphasis,show in italic

<p>I <em>think</em> Ivy was the first.</p>
3. `<blockquote></blockquote>`

The <blockquote> element is used for longer quotes that take up an entire paragraph. Note how the <p>  element is still used inside the <blockquote> element. 

<blockquote cite="http://en.wikipedia.org/wiki/Winnie-the-Pooh">
  <p>Did you ever stop to think, and forget to start again?</p>
</blockquote>

4. `<q></q>`

quote
The <q> element is used for shorter quotes that sit within a paragraph. Browsers are supposed to put quotes around the <q>  element, however Internet Explorer does not — therefore many people avoid using the <q>  element.

<p>As A.A. Milne said, <q>Some people talk to nimals. Not many listen though. That's the problem.</q></p>
5. `<abbr>`

abbreviations，If you use an abbreviation or an acronym, then the <abbr>element can be used. A title attribute on the opening tag is used to specify the full term.
不是很明白这样的element的作用是什么，和直接打字有什么区别么，可以试一下，也许是将鼠标放在附近就可以显示全称

<p><abbr title="Professor">Prof</abbr> Stephen Hawking is a theoretical physicist and cosmologist.</p>
<p><acronym title="National Aeronautics and Space Administration">NASA</acronym> do some crazy space stuff.</p>
6. `<cite></cite>`

When you are referencing a piece of work such as a book, film or research paper,

<p><cite>A Brief History of Time</cite> by Stephen Hawking has sold over ten million copies worldwide.</p>
7. `<dfn></dfn>`

defining,The <dfn>  element is used to indicate the defining instance of a new term.
Some browsers show the content of the <dfn>  element in italics. Safari and Chrome do not change its appearance.

<p>A <dfn>black hole</dfn> is a region of space from which nothing, not even light, can escape.</p>
8. `<address>`

The <address>  element has quite a specific use: to contain contact details for the author of the page
<address>
 <p><a href="mailto:homer@example.org">
   homer@example.org</a></p>
 <p>742 Evergreen Terrace, Springfield.</p>
</address>

9. `<ins>`

insert

The <ins>  element can be used to show content that has been inserted into a document
The content of a <ins>  element is usually underlined, 

<p>It was the <del>worst</del> <ins>best</ins> idea  she had ever had.</p>
10. `<del>`

deleted

while the <del>  element can show text that has been deleted from it.

while the content of a <del>  element usually has a line through it.

11. `<s>`

The <s> element indicates something that is no longer accurate or relevant(but that should not be deleted).
<p>Laptop computer:</p>
<p><s>Was $995</s></p>
<p>Now only $375</p>
12. `<u></u>`

underline

Older versions of HTML had a `<u>` element for content that was underlined, but this is being phased out.

13. `<bdo>`

标签定义页面中文本排序的显示方向，用于想要改变排序的文本。
 ltr 和 rtl 两个属性值，分别表示：从左到右显示文本和从右到左显示文本。

<bdo> 标签必须配合 dir 属性使用。
<bdo dir="rtl">该段落文字从右到左显示。</bdo>

Summary

HTML elements are used to describe the structure of the page (e.g. headings, subheadings, paragraphs)

They also provide semantic information (e.g. where emphasis should be placed, the definition of any acronyms used, when given text is a quotation).

# Chapter 3 : Lists

## Ordered lists

`<ol><li>`

<ol>
 <li>Chop potatoes into quarters</li>
 <li>Simmer in salted water for 15-20minutes until tender</li>
 <li>Heat milk, butter and nutmeg</li>
 <li>Drain potatoes and mash</li>
 <li>Mix in the milk mixture</li>
</ol>
## Unordered lists

`<ul><li>`

<ul>
 <li>1kg King Edward potatoes</li>
 <li>100ml milk</li>
 <li>50g salted butter</li>
 <li>Freshly grated nutmeg</li>
 <li>Salt and pepper to taste</li>
</ul>

## Definition lists

`<dl><dt><dd>`

definition list , definition term , definition data

<dl>
 <dt>Coffee</dt>
 <dd>- black hot drink</dd>
 <dt>Milk</dt>
 <dd>- white cold drink</dd>
 </dl> 

## Nested lists

嵌套联系表,You can put a second list inside an <li>  element to create a sub-list or nested list.

<ul>
 <li>Mousses</li>
 <li>Pastries
  <ul>
   <li>Croissant</li>
   <li>Mille-feuille</li>
   <li>Palmier</li>
   <li>Profiterole</li>
  </ul>
 </li>
 <li>Tarts</li>
</ul>

# Chapter 4: links

## Links from one website to another

`<a href=""></a>`,AbsoLute urLs

<a href="http://www.w3cschool.cn">这是一个链接</a>

<p>Movie Reviews:
 <ul>
  <li><a href="http://www.empireonline.com">
    Empire</a></li>
  <li><a href="http://www.metacritic.com">
    Metacritic</a></li>
  <li><a href="http://www.rottentomatoes.com">
    Rotten Tomatoes</a></li>
  <li><a href="http://www.variety.com">
    Variety</a></li>
 </ul>
</p>

## Links from one page to another on the same website

relative URL.

You can use a shorthand known as a relative URL.When linking to other pages within the same site, you can use relative URLs

<p>
 <ul>
  <li><a href="index.html">Home</a></li>
  <li><a href="about-us.html">About</a></li>
  <li><a href="movies.html">Movies</a></li>
  <li><a href="contact.html">Contact</a></li>
 </ul>
</p>

## Links from one part of a web page to another part of the same page

![same page.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ic15to5lj30r00nwgq0.jpg)

## Links from one part of a web page to another part of the another page

Screen readers do this by reading the link text, or what's between the anchor (a) tags. Having a list of "click here" or "read more" links isn't helpful. Instead, you should use brief but descriptive text within the a tags to provide more meaning for these users.

![another page.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ic2r3s1vj31bu0ai41g.jpg)

## Links that start up your email program and address a new email to someone

`<a href="mailto:jon@example.org">Email Jon</a>`

## Links that open in a new browser window

If you want a link to open in a new window, you can use the target attribute on the opening<a> tag. The value of this attribute should be _blank.

```html
<--!-->(opens in new window)</--!-->
<a href="http://www.imdb.com" target="_blank">Internet Movie Database</a> 
<--!-->(open in the same window)</--!-->
<a href="http://www.imdb.com" target="_self">Internet Movie Database</a> 
<--!-->(return to top)</--!-->
<a href="http://www.imdb.com" target="_top">Internet Movie Database</a> 

<a href="http://www.imdb.com" target="_parent">Internet Movie Database</a> 
```

<a href="http://www.imdb.com" target="_blank">Internet Movie Database</a> (opens in new window)

# Chapter 5: Images

## Adding images

1. <img>

- empty element
  (which means there is no closing tag)

- src
  This tells the browser where it can find the image file

- alt

  This provides a text description of the image which describes the image if you cannot see it.

- title

  Most browsers will display the content of this attribute in a tootip when the user hovers over the image

2. responsive image

![responsive image.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icasvpt5j30ay08st93.jpg)

```html
<img src="images/quokka.jpg" alt="A family of quokka" 
title="The quokka is an Australian marsupial that is similar in size to the domestic cat." />
```

3. retina

The simplest way to make your images appear "retina" (and optimize them for retina displays) is to define their width and height values as only half of what the original file is.

![retina img.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icc3kd14j30qe07gwf7.jpg)

## height and width

```html
<img src="images/quokka.jpg" alt="A family of quokka" width="600" height="450" />
```

## where to place image in your code

![where to place image in your code1.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icdpuzmcj30az0dzn1i.jpg)
![where to place image in your code2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icdpr690j30al0biaat.jpg)

## aligning images horizontally

align(removed / should use css to control)

![aligning images horizontally1.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icems2uqj30bf07yt9d.jpg)
![aligning images horizontally2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8icemwj70j30bn06wtbs.jpg)

html5: fIgure and figure Caption

`<figure><figcaption>`

Images often come with captions. HTML5 has introduced a new <figure> element to contain images and their caption so that the two are associated. 
You can have more than one image inside the <figure>  element as long as they all share the same caption.

![figurefigcaption.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ichbds1pj30br0ep10z.jpg)

## filter

filter: none | blur() | brightness() | contrast() | drop-shadow() | grayscale() | hue-rotate() | invert() | opacity() | saturate() | sepia() | url();

[sample adress](https://www.w3schools.com/cssref/playit.asp?filename=playcss_filter&preval=opacity(30%25))

# Chapter 6: Tables

## basic table structure

`<table>`

`<tr> table row`

`<td>table dataa`

<table>
    <tr>
        <td>15</td>
        <td>33</td>
        <td>44</td>
    </tr>
    <tr>
        <td>15</td>
        <td>33</td>
        <td>44</td>
    </tr>
    <tr>
        <td>15</td>
        <td>33</td>
        <td>44</td>
    </tr>
</table>

## table headings

`<th>`

Even if a cell has no content, you should still use a <td> or <th>  element to represent the presence of an empty cell otherwise the table will not render correctly

![table headings.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8idnd5480j30ar0csgm6.jpg)



## table elements

<table>	定义表格

<th>	定义表格的表头

<tr>	定义表格的行

<td>	定义表格单元

<caption>	定义表格标题

<colgroup>	定义表格列的组

<col>	定义用于表格列的属性

<thead>	定义表格的页眉

<tbody>	定义表格的主体

<tfoot>	定义表格的页脚

<cellspacing> <cellpadding>,单元格距离属性

![table elements.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8idoj91j4j30lu0zcmzw.jpg)

![example2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8idpqg3t3j30j40w418w.jpg)

## spanning

spanning columns/跨列/colspan,spanning rows/跨行/rowspan

![spanning2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8idqdlkv8j30aq0edq42.jpg)
![spanning1.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8idqdxyqbj30an0e875f.jpg)

# Chapter 7: form

## Form structure and attribute

form 作用：给后台发送数据

action  提交数据的地址

method  提交数据的方式  

get  默认   数据在地址栏显示  不安全

post  数据不在地址栏显示   相对安全

1. form

   always carry the action attribute and will  usually have a method  and id  attribute too.

2. action (attribute

   Its value is the URL for the page on the server that will receive the information in the form when it is submitted.
   
3. method（ using one of two methods: get or post） (attribute

   - get(function)

     short forms (such as search boxes)，when you are just retrieving data from the web server

   - post(function)

     allows users to upload a file is very long contains sensitive data(e.g. passwords)，adds information to, or deletes information from, a database

     ![method.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsdgacslj30b609ht92.jpg)

4. id (attribute

   identify the form distinctly from other elements on the page

![Form structure and attribute.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsdgg37pj30xg0t2dl1.jpg)

## adding text

Input 的新型html5的内容，例如(number, time,date,email,url,search)，在不同的页面会有不同的显示，所以在页面中很少使用，在手机端使用会比较多，唤醒的键盘不一样。如果type=number,在手机端会直接唤醒数字键盘。

### text input

1. <input>

2. type="text"(attribute

   it creates a single-line text input.

3. name(attribute
   The value of this attribute identifies the form control and is sent along with the information they enter to the server.

4. size(attribute

   be used in old code / css should be used to control this / just know about this things

5. maxlength(attribute 

   limit the number

   For example, if you were asking for a year, the max length attribute could have a value of 4.

![text input.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsqh0oiej30au08z74g.jpg)

### password input

1. type="password"

2. name,size, maxlength

![password input.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsqgzuvmj30az0a0dgc.jpg)

### text area

The <textarea> element is used to create a mutli-line text input.you should use CSS to control the width and height looking at older code, you may see the cols and rows attributes used with this element.

![text area.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsrbopmyj30df0cd0tm.jpg)

type=range

## making choices

### radio button

单选按钮

1. type="radio"

   Radio buttons allow users to pick just one of a number of options.

2. name

   the value of the name  attribute should be the same 

3. value

   The value of each of the buttons in a group should be different 

4. checked

   The checked  attribute can be used to indicate which value (if any) should be selected when the page loads

5. note

   Once a radio button has been selected it cannot be deselected. 

![radio button.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsuh1w42j30cy0b33zf.jpg)

### checkbox

1. type="checkbox"

   Checkboxes allow users to select (and unselect) one or more options in answer to a question.

2. name

   the value of the name  attribute should be the same 

3. value

4. checked

![checkbox.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lsxzuyk5j30d30bjab7.jpg)

### drop down list box

1. `<select>`

   A drop down list box (also known as a select box) allows users to select one option from a drop down list. 

2. name

   The name  attribute indicates the name of the form control being sent to the server, 

3. `<option>`

   The words between the opening `<option>`  and closing `</option>`  tags will be shown to the user in the drop down box.

4. value

5. selected

   If this attribute is not used,the first option will be shown when the page loads. If the user does not select an option, then the first item will be sent to the server as the value for this control.

6. two key factors in choosing which to use:

- If users need to see all options at a glance, radio buttons are better suited.

- If there is a very long list of options (such as a list of countries), drop down list boxes work better.

![drop down list box.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lt8cdhk6j30d30by75m.jpg)

### multiple select box

1. size

   Its value should be the number of options you want to show at once. 

2. multiple

   You can allow users to select multiple options from this list by adding the multiple  attribute with a value of multiple

![multiple select box.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8luthttppj30d50f8tbd.jpg)

### file input box

![file input box.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lv0q0x8cj30di08wdgf.jpg)

## submitting forms

### submit button

Method : get / post

`<form action="www.baidu.com" method="get"`

`<input type="submit" name="submit" value="Send" />`

`<button>  Register Now </button>`

![submit button.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lv0q2l2fj30cz0axt9g.jpg)

### image button

![image button.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8lv0q23enj30d50b7t9l.jpg)

### button and hidden controls

For example, a web page author might use a hidden field to indicate which page the user was on when they submitted a form.

![button and hidden controls.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzvbcb3wj30cv0atjrr.jpg)

![button and hidden controls2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzvba7f5j306f07zt92.jpg)



### labelling form controls

表单应清晰易懂，我们可以使用``元素为输入添加标签。`for` 属性需要一个值，该值与你要标记的 input 的 id 值相同。当用户选择该标签时，浏览器会自动将焦点转到和标签 相关的表单控件上。

```html
<label for="email">Email</label>
<input type="email" name="email" id="email">
<!--
你还可以这样使用 label 来封包 input，以省略使用 for 和 id。
-->
<label>
  Email
  <input type="email" name="email" />
</label>
```

`<label>`

for attribute

The for attribute states which form control the label belongs to.Note how the radio buttons use the id attribute. The value of the id attribute uniquely identifies an element from all other elements on a page. 

![label.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzwu7eimj30ta0f2q4w.jpg)

### fieldset legend grouping form elements

`<fieldset><legend> `grouping form elements

要将表单组合在一起（如登录表单），请使用`<fieldset>`元素。Fieldset 附带一个默认边框，你可以使用 css 设置样式。你可以在 fieldset 中包含`<legend>`元素，以便为表单添加标题。

将 legend 元素作为 fieldset 中的第一个元素。

The next form topic covers accessibility of radio buttons. Each choice is given a label with a for attribute tying to the id of the corresponding item as covered in the last challenge. Since radio buttons often come in a group where the user must choose one, there's a way to semantically show the choices are part of a set.

The fieldset tag surrounds the entire grouping of radio buttons to achieve this. It often uses a legend tag to provide a description for the grouping, which is read by screen readers for each choice in the fieldset element.

The fieldset wrapper and legend tag are not necessary when the choices are self-explanatory, like a gender selection. Using a label with the for attribute for each radio button is sufficient.

```html
<form>
  <fieldset>
    <legend>Login</legend>
    <label>
      Email
      <input type="email" name="email">
    </label>
    <label>
      Password
      <input type="password" name="password">
    </label>
  </fieldset>
</form>
```



![legend.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzwua2unj30kc0ek0v7.jpg)

### 禁用表单

有时，你可能希望显示表单，有时候希望禁用它，例如当用户提交表单时。你希望阻止用户编辑或多次单击提交。你可以向``元素添加禁用属性以禁用它们。或者，如果你使用 fieldset 将表单组合在一起，则可以在开始 fieldset 标签中添加 disabled。

```html
<label>
  Email
  <input type="email" name="email" disabled />
</label>

<fieldset disabled>
  <legend>Login</legend>
  <label>
    Email
    <input type="email" name="email" />
  </label>
  <label>
    Password
    <input type="password" name="password" />
  </label>
  <input type="submit" />
</fieldset>
```

### date picker

![pickdate.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzyb83ncj31580lcjvi.jpg)

HTML5 datetime Attribute

Continuing with the date theme, HTML5 also introduced the time element along with a datetime attribute to standardize times. This is an inline element that can wrap a date or time on a page. A valid format of that date is held by the datetime attribute. This is the value accessed by assistive devices. It helps avoid confusion by stating a standardized version of a time, even if it's written in an informal or colloquial manner in the text.

![HTML5 datetime Attribute.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8mzybbw1wj31cg0v2aiy.jpg)

### html5 

#### form validation

1. required attribute

   which can be used on any form element that the user is expected to fill in. 

You have probably seen forms on the web that give users messages if the form control has not been filled in correctly; this is known as form validation.

对于表单中所需的输入，如电子邮件、密码。我们可以将`required`属性添加到输入标签。如果 input 具有电子邮件类型， 浏览器将检查是否输入有效的电子邮件。

![html5 form validation.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n00fsj2ij30d20dbgnd.jpg)

#### date-input

![html5-date-input.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n00fua95j30d00bejs3.jpg)

#### email&url-input

![html5-email&url-input.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n00fu3pyj30c509bta3.jpg)

![html5-email&url-input2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n00fttbjj30bn09ojsj.jpg)

#### search-input

1. placeholder

   value is text that will be shown in the text box until the user clicks in that area. 

![html5-search-input.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n00fzvo3j30bl09kwey.jpg)

# Chapter 8: Extra Markup

## doctype

DOCTYPE declaration to tell a browser which version of HTML the page is using 

![doctype.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04n9biej309s0acmxk.jpg)

## comments in html

If you want to add a comment to your code that will not be visible in the user's browser, you can add the text between these characters:
`<!-- the comment you wanna left-->`

## id-attribute

It is used to uniquely identify that element from other elements on the 
page. 

Its value should start with a letter or an underscore (not a number or any other character).

It is important that no two elements on the same page 

![id-attribute.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04nfb8qj30bv0d3414.jpg)

## class-attribute

Sometimes, rather than uniquely identifying one element within a document, you will want a way to identify several elements as being different from the other elements on the page.

![class-attribute.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04ng2p4j30bk0cwwhv.jpg)

## block-elements

Some elements will always appear to start on a new line in the browser window. These are known as block level elements. 

块元素是一个元素，占用了全部宽度，在前后都是换行符。

Examples of block elements are`<h1>`, `<p>`, `<ul>`, and `<li>`.

![block-elements.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04n86dvj305t03f0gj.jpg)

![block-elements2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04nni2aj30bq0cjtao.jpg)

## inline-elements

Some elements will always appear to continue on the same line as their neighbouring elements. These are known as inline elements.

内联元素只需要必要的宽度，不强制换行。

Examples of inline elements are `<a>` , `<b>` , `<em>` , and `<img> `,`<span>`

![inline-elements.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04ncfmxj305e02h0hc.jpg)

![inline-elements2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04nf2z2j30bv0b9dh7.jpg)

## Grouping text & element in a block

`<div>` / document division 定义了文档的区域，块级 (block-level) start on a new line helpful to add a comment after the closing`<div>` 标签可以把文档分割为独立的、不同的部分。


HTML `<div>` 元素是块级元素，它是可用于组合其他 HTML 元素的容器。

`<div>` 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。


如果与 CSS 一同使用，`<div>` 元素可用于对大的内容块设置样式属性。

`<div>` 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 `<table>` 元素进行文档布局不是表格的正确用法。`<table>` 元素的作用是显示表格化的数据。

![Grouping text in BLOCK.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04ngct7j30bv0de75i.jpg)

## grouping-inline-elements

`<span>`

用来组合文档中的行内元素， 内联元素(inline) an inline equivalent of the `<div>`HTML `<span>` 元素是内联元素，可用作文本的容器

`<span>` 元素也没有特定的含义。

当与 CSS 一同使用时，`<span> `元素可用于为部分文本设置样式属性。

![grouping-inline-elements.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04nj1j7j30bo0bm3z7.jpg)

### span 和 div 

`<div>` `<span>`是 HTML 中常用的元素，不具有实际意义。它们只是用于构建数据的容器，不固定表示任何内容，用于将元素分组，方便进行样式编辑，使用 class 或 id 属性进行区分

```html
<div class="men">
  <!-- You can nest block elements in block elements -->
  <!-- paragraphs have blue backgrounds -->
  <p>something about men</p>
  <p>something about men</p>
</div>
<div class="women">
  <!-- paragraphs have pink backgrounds -->
  <p>something about women</p>
  <p>something about women</p>
</div>
```

```html
<p>Toothpaste <span class="price">$ 3.99</span></p>
<p>Toothbrush <span class="price">$ 1.99</span></p>
<p>Mouth wash <span class="price">$ 2.99</span></p>
```



## iframe

<span id="jump">iframe</span>

iframe标签的目的是为了我们能够将其他的Web文档嵌入到当前文档中。一些常用的第三方内容提供商都采用该技术，如Disqus的评论系统、在线视频提供商的视频，后台管理系统等。在页面中嵌套另一个页面。

```html
<iframe src="https://baidu.com"
        name="tap-to-baidu"
        width="500" height="500" frameborder="0"
        scrolling="auto"
        allowfullscreen sandbox>
  <p><a href="https://baidu.com">
    Fallback link for browsers that don't support iframes
  </a></p>
</iframe>
<--!-->iframe+a link 实现后台导航功能 a 用target连接到 iframe name 属性 ，名称一样即可切换</--!-->
<ul>
  <li><a href="#" target="tap-to-baidu">跳转到百度</a></li>
</ul>
```

以上示例中iframe的常用属性介绍如下：

- allowfullscreen，若设置为true，iframe则可以使用全屏的接口在当前页面采用全屏页面显示。
- frameborder，边框，如果设置为1，则在当前页面和iframe嵌入的页面之间有1px的边框，若设置为0，代表删除边框。
- scr，代表该iframe所需要链接的文档的地址。
- width和width，代表iframe的宽度和高度。
- 后备段落，和audio/video一样，当浏览器不支持iframe标签时，会显示后备段落中的内容。
- sandbox，沙盒，体现了现代浏览器对安全性的设置。为了最大程度上减少网站被黑客的攻击，尽量始终使用sandbox属性。未沙盒化的内容可以做的不安全的事情太多，比如：执行JavaScript、提交表单等。

`1. <iframe>` 标签规定一个内联框架。

一个内联框架被用来在当前 HTML 文档中嵌入另一个文档。通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。
`<iframe>`= inline frame 内嵌的框架

2. scrolling 滚动条,yes,no,auto,默认为auto,自动拥有滚动条

3. frameborder

   设置属性值为 "0" 移除 iframe 的边框

4. seamless
   	be applied to an iframe where scrollbars are not desired

![iframe.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n04nuog5j30bl0fldo9.jpg)




## informations about your pages

`<meta>`
description
keywords
robots
author
pragma
expires

![informations about your pages.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n096wvxsj30bt0baq3j.jpg)

## escape characters

![escape characters.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n096xs02j30gt0fgjs7.jpg)



# Chapter 9: flash video audio

## adding Video To Your Pages

1. `<video>`

2. src

3. poster

4. width,height

5. controls

6. autoplay

7. loop 

   video should start playing again once it has ended.

8. prelode

   - none 

     The browser should not load the video until the user presses play.

   - auto 

     The browser should download the video when the page loads.

   - metadata
     The browser should just collect information such as the size, first frame, track list, and duration.

![adding Video To Your Pages.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0b9eemhj30au08xweq.jpg)

## multiple-video-sources

1. `<source>`

2. src

3. type

   tell the browser what format the video is

4. codecs
   Note the use of single quotes, as well as double
   
5.   .play() 播放

     .pause() 暂停

     .volume 音量 0-1之间

     .requestFullscreen() 全屏  esc退出

     .currentTime  当前播放时间

     .duration  全部时间

     .requestPictureInPicture() 画中画

![multiple-video-sources.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0b9i4vuj30av0f9jt5.jpg)

## adding-html5-audio

preload loop autoplay controls src

`<audio>`

`<audio>.play()`可以启动audio播放功能

multiple-audio-sources

![adding-html5-audio.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0b9gq8tj30am0bbjry.jpg)

![multiple-audio-sources.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0b9gimvj30aw0b00t6.jpg)

# Chapter 10:Introduing CSS

CSS allows you to create rules that control the way that each individual box (and the contents of that box) is presented.

- CSS规则如下图所示![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-7-1/38720560.jpg)
- CSS associates Style rules with HTML elements

![CSS associates Style rules with HTML elements.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0ctsaejj30kl0g6t9v.jpg)

### CSS properties affect how elements are displayed

![CSS properties affect how elements are displayed.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0ctthyyj30ik0gjq44.jpg)

### CSS selectors 

CSS 选择器

![CSS selectors.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n0cu9ajaj30xa12ujzy.jpg)

### comments

```css
/*这是个注释*/        
p{        
text-align:center;       
/*这是另一个注释*/        
color:black;        
font-family:arial;       
}
```

### insert CSS 如何插入样式表

1. 外部样式表 using external css

```css
<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
```

2. 内部样式表 using internal css

```css
<head>
<style>
hr {color:sienna;}
p {margin-left:20px;}
body {background-image:url("images/back40.gif");}
</style>
</head>
```

3. 内联样式

```css
<p style="color:sienna;margin-left:20px">这是一个段落。</p>
```

4. 多重样式

### Higher Specificity

级联规则有一个例外，那就是特异性。如果规则集的选择器具有比定位相同元素的另一个规则集更高的特异性。具有较高特异性选择器的规则集将具有优先级。不管它在样式表中的什么位置。

- 多重样式优先级顺序

下列是一份优先级逐级增加的选择器列表，其中数字 7 拥有最高的优先权：

- 通用选择器（*）
- 元素(类型)选择器
- 类选择器
- 属性选择器
- 伪类
- ID 选择器
- 内联样式(直接在 HTML 元素标签中写 CSS 样式 具有比 Class、ID 和元素选择器的任意组合更高的特异性。)

- !important规则

当 !important 规则被应用在一个样式声明中时，该样式声明会覆盖CSS中任何其他的声明，无论它处在声明列表中的哪里。

- 使用的经验法则
  1. Always 要优化考虑使用样式规则的优先级来解决问题而不是 !important
  2. Only 只在需要覆盖全站或外部 css（例如引用的 ExtJs 或者 YUI）的特定页面中使用 !important
  3. Never 永远不要在全站范围的 css 上使用 !important
  4. Never 永远不要在你的插件中使用 !important

有时，我们可能想组合选择器来定位某些元素。在这种情况下，通过组合选择器中每个单独选择器的特异性来计算总的特异性。特异性将通过「ID –类别–元素」进行衡量。

选择器（例如 `p` ）的组合特异性为 0 – 0 – 1。 选择器（例如`.text p` ）的组合特异性为 0 – 1 – 1。 选择器（例如`#special .text p` ）的组合特异性为 1-1-1 。 选择器（例如`#special .normal .text p` ）的组合特异性为 1-2-1 。

`#special .normal .text p` 比`#special .text p` 具有更高的特异性。 `#special .text p` 具有比`.text p` 更高的特异性。 `.text p` 比 `p` 具有更高的特异性。

# Chapter 11: color

## Foreground Color

1. rgb values

   rgb(100,100,90)

2. hex codes

   `#ee3e80`

3. color names

   DarkCyan	

![Foreground Color.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55fxjimj30c20c6765.jpg)

## Background Color

![Background Color.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55fxu7kj30bj0dh0v7.jpg)

## Understanding Color

![Understanding Color.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55grgv1j32801e0dzj.jpg)

## contrast

p253,https://snook.ca/technical/colour_contrast/colour.html#fg=33FF33,bg=333333

![contrast.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55g1c1dj310m182aen.jpg)

## Opacity / rgba

1. alpha value

   a number between 0.0 and 1.0 (so a value of 0.5 is 50% opacity and 0.15 is 15% opacity).

   ![alpha value.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55fv97mj30bn0b874b.jpg)

2. 悬停效果

```css
img
 {
 opacity:0.4;
 filter:alpha(opacity=40); /* For IE8 and earlier */
 }
 img:hover
 {
 opacity:1.0;
 filter:alpha(opacity=100); /* For IE8 and earlier */
 }
```

3. rgba

```css
p.two {background-color:rgba(255,0,0,0.3);} /* 红 */
```

Difference :

opacity会让文字等内容变透明，rgba不会改变内容的颜色适用于制作弹出框

## HSL / hsla

https://www.w3cschool.cn/html/html-colors.html（色卡

1. hue

   This is expressed as an angle (between 0 and 360 degrees).

2. saturation

   This is expressed as a percentage.

3. lightness

   This is expressed as a percentage with 0% being white, 50% being normal, and 100% being black.

4. alpha

   This is expressed as a number between 0 and 1.0. For example, 0.5 represents 50% transparency, and 0.75 represents 75% transparency.

![HSL hsla.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n55g5gsxj310e17kgre.jpg)

![HSL hsla 2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8n59peos3j30bi0csju7.jpg)

# Chapter 12: TEXT

## Typeface Terminology

![Typeface Terminology.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4motouj30x00qw0wi.jpg)

## Typeface
### Specifying Typefaces

Serif

Sans-Serif

Monospace

Weight

Style

Stretch

Cursive

Fantasy

### Techniques That Offer a Wider Choice of Typefaces

font-family

font-face 服务器端字体

Service-based Font-Face

Images

SIFR

CUFON

### More Font Choice P279
Understanding font formats

@font-face

font-family

src

format

## font-family

[**Google字体无法访问的替代方案及常用前端公共库 CDN 服务**](http://www.piaoyi.org/network/Google-fonts.googleapis.com-china-cdn.html)

一个不错的在线库是[Google Fonts](https://www.google.com/fonts)。使用自定义字体时，值名称需要用引号括起来。

```html
<title>Hacker Start</title>
  <!--Add your code below-->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans" 
        rel="stylesheet"/>
  <style>
    h1 {
      /*Add your code below*/
      font-family: "Open Sans";
    }
  </style>
```

使用外部字体系列（例如 Google 提供的字体）时，最好添加备用字体。当 Google 字体服务器没有响应用不了的时候，浏览器将改用后备字体。

```css
body {
        font-family: Georgia, Times, serif;}
      h1, h2 {
        font-family: Arial, Verdana, sans-serif;}
      .credits {
        font-family: "Courier New", Courier, monospace;}
```

## font-size

```css
body {
  font-family: Arial, Verdana, sans-serif;
  font-size: 12px;}
h1 {
  font-size: 200%;}
h2 {
  font-size: 1.3em;}
```

- pixel 

  Pixels are commonly used because they allow web designers very precise control over how much space their text takes up. The number of pixels is followed by the letters px.

- percentages 

  The default size of text in browsers is 16px. So a size of 75% would be the equivalent of 12px, and 200% would be 32px.

- ems
  An em is equivalent to the width of a letter m.

为了更好的用户体验，最小的字体给到12px即可。默认继承父类的字体样式。

![font-size.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4mne98j31c20pawhp.jpg)

## font-weight

` {font-weight: bold/normal;}`

一般默认500，600加粗,将`h1-h6` `b` `<strong>`等标签清楚样式，成为样式格式化,一般会在项目的时候清除掉。

## font-style

`{font-style: italic;}`
value

- normal
- italic,使文本以字体为斜体展示
- oblique,使文本倾斜展示

## text-transform
UpperCase, capitalize & LowerCase

`h1 {text-transform: uppercase;}`
`h2 {text-transform: lowercase;}`
`.credits {text-transform: capitalize;`

## text-decoration
Underline & Strike
none
underline
overline
line-through
blink,文本动态闪烁

```css
.credits {
  text-decoration: underline;
}
a {
text-decoration: none;
}
```

## line-height
Leading 行间距

`p {line-height: 1.4em;}`

## letter-spacing, word-spacing

![letter-spacing.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4mkoxjj30l20cg0ty.jpg)

## text-align(search align

left

right

center

justify:内容文字多了之后，出现换行效果，右边会产生空隙，为了美观，选择两端对齐，将字符间距平均拉开，撑满边框。

This indicates that every line in a paragraph, except the last line,should be set to take up the full width of the containing box.两边对齐

![text-align.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4mij32j30e208cjrv.jpg)

## vertical-align
Vertical Alignment

baseline,sub,super,top,text-top,middle,bottom,text-bottom

![vertical-align.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4mkkqrj30jc096q3u.jpg)

## text-indent
Indenting Text

向左缩进

```css
h1 {
    background-image: url("images/logo.gif");
    background-repeat: no-repeat;
    text-indent: -9999px;
}
```

向右缩进

`.credits {text-indent: 20px;}`

## text-shadow
`p.three {background-color: #cccccc;color: #ffffff;text-shadow: -2px -2px -7px #111111;}`
The first length indicates how far to the left or right the shadowshould fall.
The second value indicates the distance to the top or bottom that the shadow should fall.
The third value is optional andspecifies the amount of blur that should be applied to the drop shadow.
The fourth value is the color ofthe drop shadow.

## text-overflow

`overflow:hidden;`

`tex-overflow:ellipsis` 超出框外的文本显示省略号

`white-space:nowrap`文本不换行


## :first-letter, :first-line
`p.intro:first-letter {font-size: 200%;}`
`p.intro:first-line {font-weight: bold;}`

## :link, :visited
a:link {color: deeppink;text-decoration: none;}
a:visited {color: black;}
a:link - 正常，未访问过的链接
a:visited - 用户已访问过的链接
a:hover - 当用户鼠标放在链接上时
a:active - 链接被点击的那一刻
a:hover 必须被置于 a:link 和 a:visited 之后，才是有效的。
a:active 必须被置于 a:hover 之后，才是有效的。
伪类的名称不区分大小写。

## Responding to Users(pseudo-classes(伪类
:hover, :active, 
a:hover {color: deeppink;text-decoration: underline;}
a:active {color: darkcyan;}
a.red:visited {color:#FF0000;} 
`<a class="red" href="https://www.w3cschool.cn/css/css-syntax.html">CSS Syntax</a>`
:focus
When pseudo-classes(伪类 are used, they should appear in this order: :link, :visited, :hover,:focus, :active.
CSS伪类是用来添加一些选择器的特殊效果。
anchor伪类
pseudo-element(CSS 伪元素

## attribute Selectors 

特性选择器

![attribute Selectors.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8nd4mtblej30zo18on45.jpg)

# Chapter 13: Boxes

## abstract

![abstract.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c4a59j30gr08ajrh.jpg)

![abstract2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c7cl7j30yq0skgod.jpg)

## Box dimensions

1. width, height

`div.box {height: 300px;width: 300px;background-color: #bbbbaa;}`
`p {height: 75%;width: 75%;background-color: #0088dd;}`

2. Limiting Width 

   min-width, max-width 

   `td.description {min-width: 450px;max-width: 650px;text-align: left;padding: 5px;margin: 0px;}`

3. Limiting Height
   min-height, max-height
   `h2, p {width: 400px; font-size: 90%;line-height: 1.2em;}`
   `h2 {color: #0088dd;border-bottom: 1px solid #0088dd;}`
   `p {min-height: 10px;max-height: 30px;}`

   

   height: 设置元素的高度。
   line-height: 设置行高。
   max-height: 设置元素的最大高度。
   max-width: 设置元素的最大宽度。
   min-height: 设置元素的最小高度。
   min-width: 设置元素的最小宽度。
   width: 设置元素的宽度。

## border

1. border-width
   `p.one {border-width: 2px;}`
   `p.two {border-width: thick;}`
   `p.three {border-width: 1px 4px 12px 4px;}`

2. border-style
   border-top-style/border-left-style/border-right-style/border-bottom-style
   solid/dotted/dashed/double/groove/ridge/inset/hidden / none
   border-style

   属性可以有1-4个值：
   `border-style:dotted solid double dashed;`
   上边框是 dotted
   右边框是 solid
   底边框是 double
   左边框是 dashed

   `border-style:dotted solid double;`
   上边框是 dotted
   左、右边框是 solid
   底边框是 double

   `border-style:dotted solid;`
   上、底边框是 dotted
   左、右边框是 solid

   `border-style:dotted;`
   四面边框是 dotted

3. border-color
   `p.one { border-color: #0088dd;}`
   `p.two { border-color: #bbbbaa #111111 #ee3e80 #0088dd;}`
   一次可以接受最多 4 个颜色值

4. border-image

   ![border-image.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c53jhj30gi0bidfy.jpg)

5. box-shadow

   `box-shadow: inset 0 0 10px #777777;} `

   Horizontal offset
   Vertical offset
   Blur distance
   Spread of shadow
   https://learn.freecodecamp.org/responsive-web-design/applied-visual-design/add-a-box-shadow-to-a-card-like-element/
   box-shadow property takes values for offset-x, offset-y, blur-radius, spread-radius and a color value in that order. The blur-radius and spread-radius values are optional.

6. shorthand
   border
   `p {width: 250px;border: 3px dotted #0088dd;}`
   `border:5px solid red;`

## padding

`p {width: 275px;border: 2px solid #0088dd;}`
`p.example {padding: 10px;}`

Padding（填充）属性定义元素边框与元素内容之间的空间。

Padding属性，可以有一到四个值。
单边内边距属性
`padding-top:25px; `
`padding-bottom:25px;`
`padding-right:50px;`
`padding-left:50px;`

`padding:25px 50px 75px 100px;`

上填充为25px
右填充为50px
下填充为75px
左填充为100px

`padding:25px 50px 75px;`

上填充为25px
左右填充为50px
下填充为75px

`padding:25px 50px;`

上下填充为25px
左右填充为50px

`padding:25px;`

所有的填充都是25px

## margin

`p {width: 200px;border: 2px solid #0088dd;padding: 10px;}`
`p.example {margin: 20px;}`
auto 设置浏览器边距。这样做的结果会依赖于浏览器
length定义一个固定的margin（使用像素，pt，em等）
%: 定义一个使用百分比的边距
Margin可以使用负值，重叠的内容。
set an element's margin to a negative value, the element will grow larger.

行内元素没有`margin-top`和`margin-bottom`属性

很多元素都有默认的margin或者padding,所以做项目之前需要全部清除网页自带的样式

## content

`body {text-align: center;}`
`p {width: 300px;padding: 50px;border: 20px solid #0088dd;}`
`p.example {margin: 10px auto 10px auto;text-align: left;}`

overflow
Hidden,scroll,auto
`p.one {overflow: hidden;}`
`p.two {overflow: scroll;}`

Auto will only show a scrollbar when any content is clipped.

Scroll will however always show the scrollbar even if all content fits and you cant scroll it.

## display & visibility

1. Change in-line / block 
   display
   inline/block/inline-block/none
   `li {display: inline; margin-right: 10px;}`
   `li.coming-soon {display: none;}`

   第三个值`inline-block`允许你保存块元素属性，但行为相似于行内元素。与行内元素不同，你可以在行内块元素上设置高度，宽度，上外边距和下外边距，左右外边距。如果将显示值设置为`none`，则不会呈现此元素。请注意，所有嵌套元素也不会呈现。
   
   `display: inline`和`display: inline-block`之间的主要区别在于 inline-block 允许在元素上设置宽度和高度。并且行内块元素将识别顶部和底部外边距和内边距，但行内元素不会。
   
   行内元素不能设置上外边距和下外边距。
   
2. hiding boxes
   visibility,hidden,visible
   visibility:collapse(针对于表格使用)

   `li {display: inline; margin-right: 10px;}`
   `li.coming-soon {visibility: hidden;}`

```css
<style>
tr.collapse {visibility:collapse;}
</style>
</head>
<body>

<table border="1">
<tr>
<td>Peter</td>
<td>Griffin</td>
</tr>
<tr class="collapse">
<td>Lois</td>
<td>Griffin</td>
</tr>
</table>
```

3. display:none,visibility:hidden

   `visibility:hidden`

   可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。

   `display:none`

   可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。

## rounded corners

1. border-radius
   `border-radius: 5px, 10px, 5px, 10px;`
   `p {border: 5px solid #cccccc;padding: 20px;width: 275px; text-align: center;border-radius: 10px;-moz-border-radius: 10px;-webkit-border-radius: 10px;}`

2. elliptical shapes 椭圆形

   ![椭圆形.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5bxqv5ij30qa0vi0w2.jpg)

3. border-radius: 50%;

   ![border-radius.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c88zqj31040a877i.jpg)


## Outlines

轮廓（outline）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

轮廓（outline）属性指定了样式，颜色和外边框的宽度。

轮廓（outline）属性的位置让它不像边框那样参与到文档流中，因此轮廓出现或消失时不会影响文档流，即不会导致文档的重新显示。

outline-color
outline-style
outline-width
inherit
outline
`outline:green dotted thick`

## transform

transform property is skewX(), which skews the selected element along its X (horizontal) axis by a given degree.

![transform.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c58nrj30i009dmx9.jpg)

skewY,skewY() property skews an element along the Y (vertical) axis.

![transform1.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o58c3qmwj30du09e0st.jpg)

一个盒子实际所占有的宽度（或高度）是由“内容+内边距+边框+外边距”组成的。
`width:250px;`
`padding:10px;`
`border:5px solid gray;`
`margin:10px; `
元素的总宽度为300px

## CSS Box Sizing

<mark>没有很好理解和掌握需要多看实例</mark>

The CSS `box-sizing` property allows us to include the padding and border in an element's total width and height.

属性定义了 user agent 应该如何计算一个元素的总宽度和总高度。

第二个`box-sizing`值包括元素宽度和边框还有内边距。因此，如果你有一个宽度为 200px 的元素，边框 2px 和两边填充 20px，实际内容宽度将是`156px = 200px - 20px - 20px - 2px - 2px`，其中元素的实际宽度将只是 200px。添加边距将增加盒子的总大小。

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

## 盒模型

宽高内边距外边距背景图背景色等等css属性共同作用于html标签，所产生的结果

# Chapter 14: Lists,Tables & Forms

## list-style-type

1. Unordered Lists
   None/disc 实心圆/circle 空心圆/square 实心方块

2. Ordered Lists

   `ol {list-style-type: lower-roman;}`

   Decimal 1 2 3/ 
   decimal-leading-zero01 02 03/
   lower-alphaa b c/
   upper-alphaA B C/
   lower-romani. ii. Iii/
   upper-romanI II III


## list-style-image

`ul {list-style-image: url("images/star.png");}`
指定列表项标记的图像

![list-style-image.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ctinfvj30ki0i8djc.jpg)

## list-style-position
inside
outside
`ul.illuminations {list-style-position: outside;}`
`ul.season {list-style-position: inside;}`

![list-style-position.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ctpkjnj30vc0qen62.jpg)

## list-style

list shorthand
`ul {list-style: inside circle;width: 300px;}`

![list-style.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ctejtwj30fa08074j.jpg)

## empty-cells

show
hide
inherit
If you have one table nested inside another, the inherit value instructs the table cells toobey the rules of the containing table.

Border on Empty Cells
`table.one {empty-cells: show;}`
`table.two {empty-cells: hide;}`

![empty-cells.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ctk0n2j30lg0xy0w1.jpg)

## border-spacing, border-collapse
`table.one {border-spacing: 5px 15px;}`
`table.two {border-collapse: collapse;}`
可以实现细边框

![border-spacing.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ctg0nwj30l40xon14.jpg)

## Styling text inputs

![Styling text inputs.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ephsu8j30ki0uwdjm.jpg)

## Styling submit buttons

![Styling submit buttons.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5epogj5j30no14aq90.jpg)

## Styling Fieldsets & Legends

![Styling Fieldsets & & Legends.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5epkmtnj30o60voaed.jpg)

## cursor 光标样式
`a {cursor: move;}`
Auto/crosshair/default/pointer/move/text/wait/help/url("cursor.gif");

![cursor.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5epc5zbj30j40duq3u.jpg)


# Chapter 15: Layout

## position

1.position-static

position:static

normal-flow		

you do not need a CSS property to indicate

static 定义：元素默认值，没有定位，遵循正常的文档流对象，不会受到 top、bottom、left、right 偏移量的影响

2.position:relative 

相对定位

Relative Positioning		

`p.example { position: relative; top: 10px; left: 100px;}`	

定义：相对定位，当前元素的位置是相对其正常位置进行定位。元素通过偏移量属性：top、bottom、left、right进行规定

![Relative Positioning.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5gs18euj309m07madc.jpg)

3.position-absolute

position:absolute 绝对定位

`h1 { position: absolute; top: 0px; left: 500px; width: 250px;}`

`p { width: 450px;}`

定义：绝对定位，当前元素的位置相对于父元素（没有父元素默认是<html>元素）的位置,会根据最近的定位父级进行定位。
absolute 定位使元素的位置与文档流无关，因此不占据空间。所以它们可以覆盖页面上的其它元素。

absolute 定位的元素和其他元素重叠。

4.Position-fixed

position:fixed

when a user scrolls down the page, it stays in the exact same place

`h1 { position: fixed; top: 0px; left: 50px; padding: 10px; margin: 0px; width: 100%; background-color: #efefef;}`

`p.example { margin-top: 100px;}`

定义：当前元素相对于浏览器的窗口的位置，元素通过偏移量属性：top、bottom、left、right进行规定，元素位置相对于浏览器窗口是固定位置，即使窗口是滚动的，它也不会移动。Fixed定位使元素的位置与文档流无关，因此不占据空间。Fixed定位的元素和其他元素重叠。

5.overlapping element

z-index

If you want to control which element sits on top，堆叠顺序（哪个元素应该放在前面，或后面）
`h1 { position: fixed; top: 0px; left: 0px; margin: 0px; padding: 10px; width: 100%; background-color: #efefef; z-index: 10;}`

`p { position: relative; top: 70px; left: 70px;}`

```css
img 
{ 
position:absolute; 
left:0px; 
top:0px; 
z-index:-1; 
}
```

Its value is a number, and the higher the number the closer that element is to the front.

![overlapping element.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5gs25x7j30do06w77n.jpg)

## Float

1. float

```css
blockquote { 
  float: right;    
  width: 275px;    
  font-size: 130%;    
  font-style: italic;    
  font-family: Georgia, Times, serif;    
  margin: 0px 0px 10px 10px;    
  padding: 10px;    
  border-top: 1px solid #665544;    
  border-bottom: 1px solid #665544;
}
```

当元素浮动时，它会自动将 display 值更改为 `block`。因此，如果要浮动`<span>`元素，其 display 值将从`inline`更改为`block`。

1. 单独为span写上float属性，会改变span的状态，变成类似inline-block,inline->inline-block
2. 半浮动
3. 子级浮动，如果父级没有设置高度，父级的高度会塌陷，解决办法，父级加高度，或者，清除浮动



浮动元素从常规流中脱离，被漂浮在容器(包含块)左边或右边

浮动盒会一直漂到其外边缘挨到容器边缘或另外的浮动盒

浮动元素不会影响其后面的流内块级盒

但是浮动元素后面的行级盒子会变短以避开浮动元素
left 
right 
none 
inherit

2. sticky

定义：粘性定位的元素是依赖于用户的滚动，在 position:relative 与 position:fixed 定位之间切换。它的行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置。

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

## Clearing Floats

clear

含义
指定元素哪一边不能与之前的浮动框相邻
取值
left
right
both
none

### 包含浮动

处理浮动的另一种方法是将它们包含在父元素中，并清除父元素中的浮动。这种技术称为`clearfix`，可以在许多其他网站上看到。`Clearfix`将需要一些代码来进行设置，但后面更容易使用。为此，你需要将浮动元素嵌套在另一个元素中。我们将为此容器元素定义类属性为`clearfix`。

```css
.clearfix:before, .clearfix:after {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
}
.clearfix {
  clear: both;
  *zoom: 1;
}
```

> `:before*`和`:after`是伪选择器（查看[伪元素| MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-elements)定义），允许我们在元素之前和之后定义样式，或者让我们在元素之前和之后插入内容。我们稍后会看到更多的伪选择器。在我们的例子中，我们在`clearfix`元素之前和之后插入空内容，然后将声明设置为`clear: both`。
>
> `* zoom: 1`是 Internet Explorer 5 - 7 的特殊定义，它给出了元素"布局"。对于 IE 5 - 7 来说这是一件特别的事情，在其他任何地方都没用，所以不用太关注。

要将它应用于我们的第一个带有两个 section 的示例，我们首先需要在带有类属性为 `clearfix` 的 div 中包含这些部分。

```html
<header>...</header>
<div class="clearfix">
  <section id="section1">...</section>
  <section id="section2">...</section>
</div>
<footer>...</footer>
```

```css
.clearfix:before, .clearfix:after {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
}
.clearfix {
  clear: both;
  *zoom: 1;
}
#section1{
  float: left;
  margin: 0 1% 24px 1%;
  width 64%;
}
#section2{
  float: right;
  margin: 0 1% 24px 1%;
  width 31%;
}
```



## liquid layout

![liquid layout.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5i5g5g4j32801e0k5t.jpg)
![liquid layout2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5i50vlyj32801e0gqv.jpg)
![liquid layout3.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5i5hi3ej32801e0h1o.jpg)

## example

1. `<div> 元素进行布局`

   ![元素进行布局.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5j4z33zj30fn08bwef.jpg)

```html
<!DOCTYPE html>
<html>
<body>

<div id="container" style="width:500px">

<div id="header" style="background-color:#FFA500;">
<h1 style="margin-bottom:0;">Main Title of Web Page</h1></div>

<div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
<b>Menu</b><br>
HTML<br>
CSS<br>
JavaScript</div>

<div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
Content goes here</div>

<div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
Copyright © W3Cschools.com</div>

</div>

</body>
</html>
```

2. `<table> 标签创建布局`

   ![标签创建布局.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5j4xxwnj30k409x748.jpg)

```html
<!DOCTYPE html>
<html>
<body>

<table width="500" border="0">
<tr>
<td colspan="2" style="background-color:#FFA500;">
<h1>Main Title of Web Page</h1>
</td>
</tr>

<tr>
<td style="background-color:#FFD700;width:100px;">
<b>Menu</b><br>
HTML<br>
CSS<br>
JavaScript
</td>
<td style="background-color:#EEEEEE;height:200px;width:400px;">
Content goes here</td>
</tr>

<tr>
<td colspan="2" style="background-color:#FFA500;text-align:center;">
Copyright © W3Cschools.com</td>
</tr>
</table>

</body>
</html>
```

## Summary

具体来说，设置“relative”的元素，会根据它原本的正常位置进行定位,比如设定top或者left属性，元素就会从正常位置偏移到设定值指定的位置,“absolute”就要特别些，是看父元素是否设置“relative”,“absolute”的子元素在“relative”的父元素内根据设定的值定位,如果父元素都没有设置“relative”,那该元素相对<body>进行定位

# Chapter 16: Images

## controlling sizes of images in css

you can use these names as values for the class attribute.
for example:small / medium / large
img.small {width: 100px;height: 100px;}

## Aligning images

`img.align-left {float: left;margin-right: 10px;}`
`img.align-right {float: right;margin-left: 10px;}`
`img.align-right {float: right;margin-left: 10px;}`
![Aligning images.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5kdjum2j309g04xdfz.jpg)

## Centering images
two common ways

1. On the containing element,you can use the text-align property with a value of center.

2. On the image itself, you can use the use the margin property and set the values of the left and right margins to auto.

3. also be used with the HTML5 <figure> element,

![Centering images.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5kdldsbj30fs0bomyd.jpg)

## Background Images

### CSS2.1

- `background-color`         使用的背景颜色。
- `background-image`       使用的背景图像。url( )
- `background-repeat`      如何重复背景图像。repeat / no-repeat
- `background-attachment`  背景图像是否固定或者随着页面的其余部分滚动。scroll / fixed
- `background-position`    背景图像的位置。top center etc.

### CSS3

- `background-size`        背景图片的尺寸。cover / contain
- `background-origin`     背景图片的定位区域。specifies the origin position (the background positioning area) of a background image. [click here to note position](##background-origin)

[sample](https://www.w3schools.com/cssref/playit.asp?filename=playcss_background-origin)

- `background-clip`        背景的绘制区域。

img覆盖backgroung-image覆盖background-color

```css
body {background-image: url("https://wx2.sinaimg.cn/mw690/0085y3gIly1gpm0q6dqsnj331s14o1kx.jpg");}
p {background-image: url("https://wx2.sinaimg.cn/mw690/0085y3gIly1gpm0q6dqsnj331s14o1kx.jpg");}

/*这里面的图片不会显示，因为没有设置宽高*/
```

CSS3 will also support the use of multiple background images by repeating the background shorthand. Because few browsers supported this property at the time of writing, it was not commonly used.

我必须告诉你一个重点。背景和背景图图片不是 HTML 元素。因此，它们不占用 HTML 中的任何空间。要使用任何背景或背景图片，你要定位的元素必须已具有宽度和高度。如果你的元素具有 HTML 内容，这将自然发生。或者，你可以通过 CSS 宽度，高度或内边距属性添加宽度和高度。

如果你的元素没有任何内容，则不会占用网页中的任何空间，因此你的背景或背景图片将不会显示。

![Background Images.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5vieu1qj309g03qwg8.jpg)
![Background Images2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5vij3i5j309a03n3zn.jpg)
![Background Images3.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5vifsdcj30se0lqju3.jpg)

## Repeating Images

1. background-repeat

   **repeat-x/repeat-y/no-repeat/**
   Repeated horizontally / repeated vertically / only shown once

2. background-attachment

   **fixed/scroll**

   whether a background image should stay in one position or move as the user scrolls up and down the page.
   
   `body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-attachment: fixed;}`

## Background Position

1. background-position-percentage
   

`body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-position: 50% 50%;}`

2. Background Position

   `body {background-image: url("images/tulip.gif");background-repeat: no-repeat;background-position: center top;}`

   left top / center / bottom ; center top / center / bottom ; right top / center / bottom

![Background Position.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5w2mvpdj30fi0q6ab2.jpg)

## background size

arrtr : auto, contain , cover

背景大小可让你定义背景图像的大小。通常，你的背景图像保留其原始大小。正如你可以看到鸭子卡通的例子。

使用`background-size`属性，你可以根据需要拉伸和缩小背景图像。`background-size`属性接受长度值和高度值。这两个关键字值可以覆盖。

设置背景大小为`contain`将确保背景图像的尺寸不会超过元素的宽度和高度。它将尽可能大地缩放图像，而不会裁剪或拉伸图像，受到元素尺寸的限制。

设置背景大小`cover`将确保背景图像覆盖元素的整个区域，而不会更改图像的宽高比。它会在不拉伸图像的情况下尽可能大地缩放图像。如果图像的比例与元素不同，则将裁剪部分图像。

你还可以为 background-size 提供长度值，绝对值和百分比。

```css
/* One value sets the width of the image (height becomes 'auto') */
background-size: 50%;

/* Two values. First value: width of the image; Second value: height */
background-size: 50% auto;
```

## shorthand

background: [background-color] [background-image] [background-repeat] [background-attachment] [background-position] / [ background-size] [background-origin] [background-clip];

```css
/* background：颜色 地址 平铺方式  x位置 y位置 */

.example {
  background: aquamarine 
              url(img.png) 
              no-repeat 
              scroll 
              center center / 50% 
              content-box content-box;
}
```

`body {background: #ffffff url("images/tulip.gif") no-repeat top right;}`

1: background-color
2: background-image
3: background-repeat
4: background-attachment
5: background-position

## background-origin
图片渲染的位置
padding-box,content-box,border-box

| Value       | Description                                                  | Play it                                                      |
| :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| padding-box | Default value. The background image starts from the upper left corner of the padding edge | [Play it »](https://www.w3schools.com/cssref/playit.asp?filename=playcss_background-origin) |
| border-box  | The background image starts from the upper left corner of the border | [Play it »](https://www.w3schools.com/cssref/playit.asp?filename=playcss_background-origin&preval=border-box) |
| content-box | The background image starts from the upper left corner of the content | [Play it »](https://www.w3schools.com/cssref/playit.asp?filename=playcss_background-origin&preval=content-box) |
| initial     | Sets this property to its default value. [Read about *initial*](https://www.w3schools.com/cssref/css_initial.asp) | [Play it »](https://www.w3schools.com/cssref/playit.asp?filename=playcss_background-origin&preval=initial) |
| inherit     | Inherits this property from its parent element. [Read about *inherit*](https://www.w3schools.com/cssref/css_inherit.asp) |                                                              |

## background-clip
((背景裁剪))   图片裁剪  裁剪掉的位置空下来 占位置
padding-box,content-box,border-box

多背景设置
background:url 平铺方式 位置

### 图片填充整个页面

```css
body {
  background: url(../images/loginPage.jpeg) no-repeat center center;
  background-size: cover;
  background-attachment: fixed;
  background-color: white;
  background: white url(../images/loginPage.jpeg) no-repeat fixed center center;
  
}
```



## image rollovers & sprites

## Contrast of background images

High Contrast
Low Contrast
Screen 屏蔽

# Chapter 17: HTML5 Layout

## Traditional HTML Layouts

p432!

![Traditional HTML Layouts.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5wr00bgj30vq178wle.jpg)

![Traditional HTML Layouts2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5wr2363j30vc12u44g.jpg)

## 结构元素

作用：方便搜索引擎爬虫分辨网页每个分区结构是什么

- header
- Navigation
- article
- section
- aseide
- footer

## Headers & Footers

**purpose**

The main header or footer that appears at the top or bottom of every page on thesite.

A header or footer for an individual <article> or <section> within the page.

Header shares the embedded landmark feature you saw with main, allowing assistive technologies to quickly navigate to that content.header只负责做landmark & navigate的东西

使用`<header>`元素来包含代表一组介绍性或辅助导航的内容。它可能包含一些标题元素（h1、h2 ...），但也包含其他元素，如 Logo、搜索表单等。

`<header>`看起来与`<head>`非常相似，但它们的用途完全不同。`<head>`元素用于提供有关文档的一般信息（元数据 metadata），包括其标题、以及其 JS 脚本和 CSS 样式的链接。它由浏览器去使用和处理，不在页面上呈现。

`<header>`元素是一个包含页面标题元素的结构元素，它是一个块元素，它位于`<body>`元素中。

`<footer>`元素表示根元素的页脚。页脚通常包含有关该部分的作者、版权数据或相关文档的链接的信息。它也可以是具有其他导航链接的站点页脚。

![Headers & Footers.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5wqne4uj30vw0vewhl.jpg)

## main

`<main></main>`

1. function

   The main element is used to wrap (you guessed it) the main content, and there should be only one per page. It's meant to surround the information that's related to the central topic of your page. It's not meant to include items that repeat across pages, like navigation links or banners.

2. position
   The main tags should be between the closing header tag and the opening footer tag.

## Navigation

`<nav>`元素表示链接到其他页面或页面中的一部分，它是带有导航链接的部分。`<nav>`仅用于主要导航部分，例如页眉页面，页面页脚或目录。一个关闭的导航链接不应使用`<nav>`，例如指向网站其他部分或外部网站的段落中的链接。

Linking Around Block-Level Elements

`<nav> </nav>`

![Navigation.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5wqofn3j30xc0ia75x.jpg)

## article

表示页面中的自包含内容，都是可独立分发或重用的。当你拿出它放在任何地方时它应该是完全合理的。示例包括：论坛帖子，杂志或报纸文章或博客条目。

`<article> </article>`

```html
<article>
  <p>paragraphs about something</p>
  <p>paragraphs about something</p>
</article>
```

![article.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5wr8m9ij31ac11cn67.jpg)

`<aside>`

通常，你会在网页的一侧看到垂直的内容列。这可以使用`<aside>`元素表示。`<aside>`元素表示文档的一部分，其内容与文档的主要内容相关。`<aside>`是一个像所有其他结构元素一样的块元素。这意味着它将占用页面的整个宽度或嵌套的元素。现在，不要过于担心这一点，因为我们将在后面的章节中讨论如何使用 CSS 手动定位元素。

![aside.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ydxbmpj319q0vegte.jpg)

`<section>`

表示文档的通用部分，例如一类主题内容的分组，通常带有标题。section 中的内容最好是相关的。

```html
<section>
  <h1>Section Title</h1>
  <article></article>
  <article></article>
</section>
```

在`<section>`，`<article>`和`<div>`之间进行选择时。考虑一下你正在处理的内容。如果你仅以样式目的对内容进行分组，请使用`<div>`。如果你的内容是独立的并添加到页面大纲中，请使用`<article>`。如果要将相关内容组合在一起并添加到页面中，请使用`<section>`。

![section.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ye16xaj31ac150gun.jpg)

`<hgroup>`

![hgroup.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ydpu73j319w0fcgoa.jpg)

`<figure><figcaption>`

![figcaption.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ydrmjyj310g0kcwhv.jpg)

The <figure> element should also contain a <figcaption> element which provides a text decription for the content of the <figure> element. In
this example, you can see a <figure> has been added inside the <article> element.

`<div>`

![div.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8o5ydvtzoj311u0ug7ae.jpg)

**distinguish**

`<div>` - groups content
`<section>` - groups related content
`<article>` - groups independent, self-contained content

For example, if a book is the article, then each chapter is a section. When there's no relationship between groups of content, then use a div.

Html5 新的表单控件,email ,tel, calendar, time, date ,url, search 


## Css layout

二列布局：侧边栏固定宽度，内容栏自适应宽度
三列布局：两侧两列固定宽度，内容栏自适应宽度

### float+margin

```css
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

注意事项
注意DOM文档的书写顺序，先写两侧栏，再写主面板，更换后则侧栏会被挤到下一列（圣杯布局和双飞翼布局都会用到）。
这种布局方式比较简单明了，但缺点是渲染时先渲染了侧边栏，而不是比较重要的主面板。

### position+margin

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

注意事项
本方法不限制DOM书写顺序，先写主面板会使主面板部分优先渲染（一般主面板会比侧栏内容重要）。
与上一种方法相比，本种方法是通过定位来实现侧栏的位置固定。
如果中间栏含有最小宽度限制，或是含有宽度的内部元素，则浏览器窗口小到一定程度，主面板与侧栏会发生重叠。

### 圣杯布局(float + 负margin)

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

布局步骤:
三者都设置向左浮动。
设置content宽度为100%，设置两侧栏的宽度。
设置 负边距，body-left设置负左边距为100%，body-right设置负左边距为负的自身宽度。
设置content的padding值给左右两个子面板留出空间。
设置两个子面板为相对定位，body-left的left值为负的body-left宽度，body-right的right值为负的body-right宽度。
注意事项
DOM元素的书写顺序不得更改。
主面板部分优先渲染（一般主面板会比侧栏内容重要）。
当面板的main内容部分比两边的子面板宽度小的时候，布局就会乱掉。可以通过设置main的min-width属性或使用双飞翼布局避免问题。

### 双飞翼布局(float + 负margin )

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

布局步骤：
三者都设置向左浮动。
设置main-wrap宽度为100%，设置两个侧栏的宽度。
设置 负边距，sub设置负左边距为100%，extra设置负左边距为负的自身宽度。
设置main的margin值给左右两个子面板留出空间。
注意事项
主面板部分优先渲染（一般主面板会比侧栏内容重要）。
圣杯采用的是padding，而双飞翼采用的margin，解决了圣杯布局content的最小宽度不能小于左侧栏的缺点。
双飞翼布局不用设置相对布局，以及对应的left和right值。
通过引入相对布局，可以实现三栏布局的各种组合，例如对右侧栏设置position: relative; left: 190px;,可以实现left+right+content的布局。

# Chapter 18: Process & Design

Main content

Target Audience

individuals

Companies

why people visit your website

What Your Visitors are Trying to Achieve

What Information Your Visitors Need

How Often People Will Visit Your Site

Site Maps

site WireFrames 线框图

Getting your message across using design

content

prioritizing

organizing

Visual hierarchy

size

color

style

grouping and Similarity

Designing Navigation

# Chapter 19: Practical Information Index

Main content

Search Engine Optimization SEO

ON PAGE SEO

How to Identify Keywords and Phrases

Analytics: Learning about your Visitors

How Many People Are Coming to Your Site?

What Are Your Visitors Looking At?

Where Are Your Visitors Coming From?

Domain Names & Hosting

FTP & Third Party Tools

# Chapter 20. canvas

Ref:

1. [segmentfault](https://segmentfault.com/a/1190000021644615)
2. [H5系列之canvas](https://www.huaweicloud.com/articles/56fc5a60024721a029d0a3f5d2572bc3.html)

| First Header         | Second Header                                               |
| -------------------- | ----------------------------------------------------------- |
| 获取画布             | var oC=document.querySelector('canvas');                    |
| 获取画笔             | var gd=oC.getContent('2)                                    |
| 把笔移动到某个起始点 | gd.moveTo(x,y)                                              |
| 描述轨迹             | gd.lineTo(x,y)                                              |
| 开始新的轨迹         | gd.beginPath();                                             |
| 轨迹收尾相连         | gd.closePath();                                             |
| 线的颜色             | gd.strokeStyle='颜色'                                       |
| 线的宽度             | gd.lineWith=数字;                                           |
| 描线                 | gd.stroke();                                                |
| 填充的颜色,          | gd.fillStyle='颜色'                                         |
| 填充                 | gd.fill();                                                  |
| 矩形                 | gd.rect(x,y,w,h);                                           |
| 线性的矩形,          | gd.strokeRect(x,y,w,h);                                     |
| 填充的矩形,          | gd.fillRect(x,y,w,h);                                       |
| 圆弧                 | `arc(x, y, radius, startAngle, endAngle [, anticlockwise])` |
| 橡皮                 | gd.clearReact(x,y,w,h)                                      |



## 创建画布，设置画布尺寸

A canvas is a rectangular area on an HTML page. By default, a canvas has no border and no content.

```html
<canvas id="myCanvas" width="200" height="100"></canvas>
```

Always specify an id attribute (to be referred to in a script), and a width and height attribute to define the size of the canvas. To add a border, use the style attribute.

如果想要全屏幕显示

```css
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
```

```html
<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;"></canvas>
```

## Canvas的坐标系统

Canvas的坐标以左上角为原点，水平向右为X轴，垂直向下为Y轴，以像素为单位，所以每个点都是非负整数。

![0955404EF3FA6CE8E2CF4573F8CE26A0.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grcxvh98k5j6072040jrc02.jpg)

## 绘制图形

### 基本思路逻辑流程

```js
    //获取了画布
    var oC=document.querySelector('canvas');
    //获取一支笔   官方：获取画布的上下文 
    var gd=oC.getContext('2d');
    //把笔移动到画画的位置上  这个点就是起始点
    gd.beginPath();//开始一个新的路径
    gd.moveTo(100,100);
    gd.lineTo(100,300);
    gd.strokeStyle='blue';
    gd.stroke();

    gd.beginPath();
    gd.moveTo(300,100);
    gd.lineTo(300,300);
    gd.strokeStyle='red';
    gd.stroke();
```

### 一、矩形

#### 1. 实心矩形（`fillRect`）

绘制实心矩形最简单的是用 `fillRect(x, y, width, height)` 方法，参数中 `x, y` 表示矩形左上角的坐标；`width`、`height` 分别表示矩形的宽、高。

```js
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// 设置填充颜色
ctx.fillStyle = 'skyblue';
// 绘制实心矩形
ctx.fillRect(20, 20, 150, 100);
```

#### 2、空心矩形（`strokeRect`）

与绘制实心矩形类似的是使用 `strokeRect(x, y, width, height)` 方法绘制空心矩形。参数与 `fillText` 方法一致。

```js
// 设置线宽
ctx.lineWidth = 5;
// 设置绘制颜色
ctx.strokeStyle = 'chocolate';
// 绘制空心矩形
ctx.strokeRect(20, 20, 150, 100);
```

#### 3、清空矩形区域（`clearRect`）

```js
ctx.fillStyle = 'skyblue';
//填充矩形内部颜色
ctx.fillRect(20, 20, 150, 100);
// 清除画布中的矩形区域，清除一定的区域，即矩形内部的某块矩形，形成空心的效果
ctx.clearRect(25, 25, 140, 90);
```

![DEBC6644DA5E3808A90D13B00B7869B5.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grczttiokrj61hw0xq0yd02.jpg)

### 二、文字（Text）

#### 1、实心文字（fillText）

实心文字可以使用 `fillText(text, x, y [, maxWidth])` 方法，参数中 `text` 表示绘制的文字；`x, y` 为文字起点的坐标；`maxWidth` 为可选参数，表示文字的最大宽度，如果文字超过该最大宽度那么浏览器将会通过调整字间距、字体或者压缩文字来适应最大宽度。

```js
// 设置绘制颜色
ctx.fillStyle = 'purple';
// 设置字体
ctx.font = '30px Arial';
// 绘制实心颜色
ctx.fillText('Hello World', 220, 50);
```

### 三、路径（Path）

通过Path我们可以定义一段段路径（或直线、或曲线）来组合出我们想要的图形。

使用Path也可以绘制矩形，和 `fillRect`、`strokeRect`一样的效果，但是多一个步骤。使用 `rect(x, y, width, height)` 方法可以向当前路径添加一个矩形，该方法只会改变路径但不会直接渲染出矩形，所以还需要执行 `fill()` 或 `stroke()` 方法：

```js
ctx.rect(200, 20, 200, 100);
ctx.lineWidth = 3;
ctx.strokeStyle = 'deeppink';
ctx.stroke();

ctx.rect(200, 20, 200, 100);
ctx.fillStyle = 'deeppink';
ctx.fill();
```



![image-20210610105151909](/Users/chenruo/Library/Application Support/typora-user-images/image-20210610105151909.png)

#### 2、三角形

或者在绘制最后一边的时候可以使用`ctx.closePath()`，使路径闭合。

![AD7E958C83657E7A348342A052E65FF6.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grczlxqggnj61h60zm79h02.jpg)

```js
// 开始绘制路径
ctx.beginPath();
// 移动至起点
ctx.moveTo(100, 20);
// 绘制线段
ctx.lineTo(200, 20);
ctx.lineTo(150, 150);
ctx.lineTo(100, 20);
// 绘制路径
ctx.stroke();
```

```js
ctx.beginPath();
ctx.moveTo(200, 20);
ctx.lineTo(300, 20);
ctx.lineTo(250, 150);
// 闭合路径
ctx.closePath();
// 设置填充颜色
ctx.fillStyle = 'coral';
// 填充路径
ctx.fill();
```

#### 3、弧线

##### （1）标准圆弧

Canvas中没有专门绘制圆的方法，而是使用更加通用的方法`arc(x, y, radius, startAngle, endAngle [, anticlockwise])` 绘制弧线，参数中 `x, y` 为圆心坐标；`radius` 为圆的半径； `startAngle` 为弧的初始角度；`endAngle` 为弧的结束角度；`anticlockwise` 表示是否以逆时针方向绘制路径。例如绘制圆，可以写成：

```js
ctx.beginPath();
ctx.arc(300, 300, 60, 0, Math.PI * 2, true);
ctx.stroke();
```

![A97610CDB2300244D6F084C9DEBB50B7.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grczo33tefj61ho0nydjf02.jpg)

### 四、图片（Image）



我们也可以将图片绘制到canvas上面，使用 `drawImage()` 方法。`drawImage()`方法有三个重载：

```
drawImage(image, dx, dy);
drawImage(image, dx, dy, dWidth, dHeight);
drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
```

各参数的含义为：

**image：** 被绘制到canvas上面的图片源，支持多种类型：[CSSImageValue](https://developer.mozilla.org/en-US/docs/Web/API/CSSImageValue), [HTMLImageElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement), [SVGImageElement](https://developer.mozilla.org/en-US/docs/Web/API/SVGImageElement), [HTMLVideoElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement), [HTMLCanvasElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement), [ImageBitmap](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap), [OffscreenCanvas](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas)

**dx：** 在canvas上水平方向绘制的起点

**dy：** 在canvas上垂直方向绘制的起点

**dWidth：** 在canvas上绘制图片的宽度

**dHeight：** 在canvas上绘制图片的高度

**sx：** 原始图片上水平方向裁剪的起点

**sy：** 原始图片上垂直方向裁剪的起点

**sWidth：** 原始图片上水平方向裁剪的宽度

**sHeight：** 原始图片上垂直方向裁剪的高度

前两个重载比较好理解，就是在canvas上绘制出完整的源图片，并且可以通过设置宽高控制图片的缩放。第三个重载即在canvas上绘制出源图片的一部分，可以形象表示为：

![drawImage](https://segmentfault.com/img/remote/1460000021644630)

图片源以 `HTMLImageElement` 为例，在canvas上绘制图片可以这么实现：

**html：**

```html
<img id="source" style="display: none;" src="https://unsplash.it/500/300?image=1074" alt="source">
```

**js：**

```js
const image = document.getElementById('source');
image.addEventListener('load', e => {
  ctx.drawImage(image, 50, 150, 500, 300);
});
```

[w3c Example](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_canvas_tut_img)

![24B3A8DF453399E51ED03C39A9E5B1D9.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grd2m9u7grj61xe12mak202.jpg)

**note:** 在使用canvas时，图片的加载时间过长会导致画布出来而图片没有出来的情况，解决方案：

1. Window.onload
2. Img.onerror / img.onload

```js
  window.onload = function () {
    var oC = document.querySelector("canvas");
    // var oImg=document.getElementById('img1');
    // oImg.style.display='none';
    var gd = oC.getContext("2d");

    gd.drawImage(oImg, 0, 0);
  };
```

```js
  var oC = document.querySelector("canvas");
  var gd = oC.getContext("2d");

  var oImg = new Image();
  oImg.src = "image/1.jpg";

  oImg.onload = function () {
    gd.drawImage(oImg, 200, 500, 150, 350, 0, 0, 600, 600);
  };
  oImg.onerror = function () {
    console.log("失败了");
  };
```

```html
  <body>
    <!-- img 600x823 -->
    <canvas
      id="myCanvas"
      width="640"
      height="960"
      style="border: 1px solid #000000"
    ></canvas>
    <img
      id="source"
      src="http://ww1.sinaimg.cn/large/005NUwyggy1grd76cn73aj60go0mvjsp02.jpg"
      alt="source"
    />
  </body>
</html>
<script>
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");

  const image = document.getElementById("source");
  //图片加载完毕后进行画图
  image.addEventListener("load", (e) => {
    //将图片按比例放大，并填满画布
    ctx.drawImage(image, 0, 0, 600, 823, 0, 0, 640, 960);
  });
</script>

```

### 五、保存图片

根据用户上传的图片压缩质量

`canvas.toDataURL(type, encoderOptions);`

[ref](https://www.jianshu.com/p/17d7e5ddf10a)

```js
var fullQuality = canvas.toDataURL("image/jpeg", 1.0);
// data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...9oADAMBAAIRAxEAPwD/AD/6AP/Z"
var mediumQuality = canvas.toDataURL("image/jpeg", 0.5);
var lowQuality = canvas.toDataURL("image/jpeg", 0.1);
```

console.log(url)

![0681B0890B7B9913DC969A355F34E653.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgx3use3sj60i008iwgn02.jpg)

```js
//保存图片
  oBtn.onclick = function () {
    //toDataURL，根据canvas的导出成设定的图片类型，image/png，image/jpg...,后面的数字参数为图片质量,默认是1
    //保存成一个地址
    var url = oC.toDataURL("image/png", 0.4);
    var oImg = new Image();
    oImg.src = url;
    oImg.onload = function () {
      document.body.appendChild(oImg);
    };
    //console.log(url);
  };

  function getBase64(url) {
    //通过构造函数创建img实例，在赋予src值后就会立刻下载图片，相比createElement()创建<img>省去了append(),也避免了文档冗余和污染
    var Img = new Image(),
      dataURl = "";
    Img.src = url;
    Img.onload = function () {
      //要先确保图片完整获取到，这是个异步事件
      var canvas = document.createElement("canvas"),
        width = Img.width,
        height = Img.height;
      canvas.width = width;
      canvas.height = height;
      //将图片绘制到canvas中
      canvas.getContext("2d").drawImage(Img, 0, 0, width, height);
      //转换图片为dataURL
      dataURL = canvas.toDataURL("image/jpeg");
    };
  }
```

![84CBE1F8FB8F474E2CA473D015C06D3B.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grgxyn5xl8j61d40d0q5c02.jpg)

Input files中的属性可以获得文件的信息，通过文件的信息判断用户上传的文件是否是我们规定的内容

```html
<input type="file" id="f1" />

<script>
var oF = document.getElementById("f1");
console.log(oF.files[0].type)
</script>
```



# CSS3

## transition

CSS transitions 可以决定哪些属性发生动画效果 (明确地列出这些属性)，何时开始 (设置 delay），持续多久 (设置 duration) 以及如何动画 (定义*timing function*，比如匀速地或先快后慢)。

 linear 匀速,ease  缓慢开始-加速-缓慢结束,ease-in 缓慢开始-加速,ease-out 加速-缓慢结束

[transition MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

[example](https://codepen.io/linhaishe/pen/KKaBNOB)

```css
div {
    transition: <property> <duration> <timing-function> <delay>;
}
```

`transition-duration: 0.5s`

`transition-timing-function:ease,linear,step-end,steps(4, end)`

`transition-delay: 2s`

https://www.w3cschool.cn/css3/2h6g5xoy.html

## Gradients

不是所有浏览器都兼容，需要加浏览器的内核标志 -webkit- -ms- 等，-webkit-linear-gradient(...)

### 线性渐变

向下/向上/向左/向右/对角方向（Linear Gradients）

#### syntax

```css
background: linear-gradient(direction, color-stop1, color-stop2, ...);
background: linear-gradient(angle, color-stop1, color-stop2);
```

在渐变之前添加了一种后备颜色来处理旧浏览器。默认情况下，渐变从上到下，我们可以通过在颜色值之前指定方向来更改方向。你可以使用数字值或度值。对于从左到右的渐变，我们可以使用"向右"，从左上角到右下角，我们使用"到右下角"。度数可以从 0 到 360.在值的末尾使用"deg"，如"135deg"。

```css
div {
  background: #64e3ee;
  background: linear-gradient(#64e3ee, #002bff);
}
```

```css
div {
  background: #64e3ee;
  background: linear-gradient(135deg, #64e3ee, #002bff);
}
```

#### 重复性的线性渐变

```css
div{
  width:100px;
  height:100px;
  background: repeating-linear-gradient(#64e3ee 10px, #002bff 20px);
}
```

### 径向渐变

由它们的中心定义（Radial Gradients）`radial-gradient（）`函数创建径向渐变背景。它类似于线性渐变，第一个颜色值是以起点为中心，第二个值是向外变化的颜色。默认是椭圆形状。

#### syntax

```css
background: radial-gradient(center, shape size, start-color, ..., last-color);
```

```css
div {
  background: #64e3ee;
  background: radial-gradient(#64e3ee, #002bff);
}

height:300px;
width:200px;

div {
  background: #64e3ee;
  background: radial-gradient(center , circle , #64e3ee, #002bff);
}
```



##  Create a custom CSS Variable

自定义css属性

```html
<style>
    .penguin{
        --penguin-skin:black;
        --penguin-belly:gray;
        --penguin-beak:yellow;
        
        position:relative;
        margin:auto;
        display:block;
        margin-top:5%;
        width:300px;
        height:300px;
    }
    
    .penguin-top{
        top:10%;
        left:35%;
        backgroud:var(--penguin-skin,gray);
        width:50%;
        height:45%;
        border-radius:70% 70% 60% 60%;
    }
</style>
```

## Typography Responsive

viewport units 

Instead of using em or px to size text, you can use viewport units for responsive typography. Viewport units, like percentages, are relative units, but they are based off different items. Viewport units are relative to the viewport dimensions (width or height) of a device, and percentages are relative to the size of the parent container element.

vw: 10vw would be 10% of the viewport's width.

vh: 3vh would be 3% of the viewport's height.

vmin: 70vmin would be 70% of the viewport's smaller dimension (height vs. width).

vmax: 100vmax would be 100% of the viewport's bigger dimension (height vs. width).

## transform

[transform2D](https://eyesofkids.gitbooks.io/css3/content/contents/transform2d.html)

```css
transform: rotate(45deg) translateX(200px);
/*//先写的后执行,此图案先平移后旋转*/
```

[transform3D](https://eyesofkids.gitbooks.io/css3/content/contents/transform3d.html)

变形的过程中，盒子模型其实没有发生变化，只是看起来变了，位置没有发生变化。变形只会引起页面重绘，不会使页面重排，页面性能得到提升。

## <mark>CSS Grid</mark>

### `display:grid;`

Turn any HTML element into a grid container by setting its display property to grid. This gives you the ability to use all the other properties associated with CSS Grid.

### `grid-template-columns`
`grid-template-rows`

```html
<style>
    .container {
        grid-template-columns: 100px 100px 100px;
        grid-template-rows:50px 50px;
    }
</style>
```

```html
<style>
.container {
    font-size: 40px;
    width:100%;
    background:lightgray;
    display:grid;
    grid-template-columns:50%;
}
</style>
<div class="container">
    <div class="d1">1</div>
    <div class="d2">2</div>
    <div class="d3">3</div>
    <div class="d4">4</div>
    <div class="d5">5</div>
</div>
<p>
    会占div位置的50%,(灰色部分)图1
</p>
```

![会占div位置的50%,(灰色部分).png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g15n3888j30v40dygn4.jpg)

```html
<style>
.container {
    font-size: 40px;
    width:100%;
    background:lightgray;
    display:grid;
    grid-template-columns:100px 100px 100px;
}
</style>
<div class="container">
    <div class="d1">1</div>
    <div class="d2">2</div>
    <div class="d3">3</div>
    <div class="d4">4</div>
    <div class="d5">5</div>
</div>
<p>
多出来的列数会自动换到下一行,you need to define the structure of the grid as well. To add some columns to the grid, use the grid-template-columns property on a grid container as demonstrated,设定每一列的宽度值，如果有两列的话就只写两个值，三列的话就设置三个值。
</p>
```

![gird-template-2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g19xl0iaj30zs0k6wh3.jpg)
![grid-template-3.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g19xku3nj31cq0jggop.jpg)

### Change the Size of Columns and Rows

fr: sets the column or row to a fraction of the available space,
auto: sets the column or row to the width or height of its content automatically,
%: adjusts the column or row to the percent width of its container.

`grid-template-columns: auto 50px 10% 2fr 1fr;`

The first column is as wide as its content, 

the second column is 50px,

the third column is 10% of its container, 

and for the last two columns; the remaining space is divided into three sections, two are allocated for the fourth column, and one for the fifth.

![Change the Size of Columns and Rows-1.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g1j23ng6j30kq07ugll.jpg)
![Change the Size of Columns and Rows-2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g1j28lxjj30xk0i0whh.jpg)

### grid-column/row-gap

**[CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) 起初是用 [`grid-gap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-gap) 属性来定义的，目前逐渐被 `gap` 替代。但是，为了兼容那些不支持 `gap` 属性的浏览器，你需要像上面的例子一样，使用带有前缀的属性 ** 

<https://developer.mozilla.org/zh-CN/docs/Web/CSS/gap>

grid-column-gap: 10px;
grid-row-gap:5px;

grid-gap
shorthand

one value
create a gap between all rows and columns

two value
use the first one to set the gap between the rows and the second value for the columns

```html
<div id="grid">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
```

```css
#grid {
  display: grid;
  height: 200px;
  grid-template: repeat(3, 1fr) / repeat(3, 1fr);
  gap: 20px 5px;
}

#grid > div {
  background-color: lime;
}
```

### grid-column/row

<https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column>

<https://www.w3schools.com/cssref/tryit.asp?filename=trycss_grid-column>

Use grid-column to Control Spacing

<mark>**3x3 grid**</mark>

![3x3 grid.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g218i6rrj30ie0he0sx.jpg)

 **grid-column** CSS 属性is a [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties) property for [`grid-column-start`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-column-start) and [`grid-column-end`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-column-end)

The hypothetical horizontal and vertical lines that create the grid are referred to as lines. These lines are numbered starting with 1 at the top left corner of the grid and move right for columns and down for rows, counting upward.grid-column property in conjunction with the line numbers you want the item to start and stop at.

`grid-column: 4 ;`为单个值的时候，表明说是在那个格子里，这个就是在第四列的格子里。

`grid-column: 2 / -1;`负号表示从相反方向，即右边开始数列数，即，左数第二根和最右边第一根(即最后一根)

`grid-column: 1 / span 2;`占两个格子

```html
<style>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}

.item1 {
  grid-column: 4 ;
}

.item2 {
  grid-column: 2 ;

}
</style>

<div class="grid-container">
  <div class="item1">1</div>
  <div class="item2">2</div>
  <div class="item3">3</div>  
  <div class="item4">4</div>
  <div class="item5">5</div>
  <div class="item6">6</div>
  <div class="item7">7</div>
</div>
```

![grid column.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1g8g2hziomdj30i20e0wf8.jpg)

![grid-column2-4.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g2qbo94aj30v40d0dhq.jpg)
![gridrow2-4.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8g2qbp66gj30x20jg771.jpg)

### justify & align

`justify-self`

stretch, which will make the content fill the whole width of the cell. This CSS Grid property accepts other values as well:

start: aligns the content at the left of the cell,

center: aligns the content in the center of the cell,

end: aligns the content at the right of the cell.

![justify-self.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6c24w50j30vy0ceta7.jpg)

`align-self`

stretch, which will make the content fill the whole width of the cell. This CSS Grid property accepts other values as well:

start: aligns the content at the left of the cell,

center: aligns the content in the center of the cell,

end: aligns the content at the right of the cell.

![align-self.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6c24zgsj30w20cc0u9.jpg)

`justify-items`

![justify-items.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6c28li9j30w40lejux.jpg)

`align-items`

### grid-template-areas

group cells of your grid together into an area and give the area a custom name. 

use a period (.) to designate an empty cell in the grid.

![grid-template-areas.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6ezjwijj30im06ut98.jpg)
![grid-template-areas2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6ezr26tj30lo0sg0ws.jpg)

### grid-area

`.item1 { grid-area: header; }`

you can place an item in your custom area by referencing the name you gave it.

![grid-area.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6hrqculj31aa0xwn3t.jpg)

`item1 { grid-area: 1/1/2/4; }`

grid-area: 
horizontal line to start at / vertical line to start at / horizontal line to end at / vertical line to end at;

![grid-area2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6hrl8x7j31800pagp5.jpg)

### repeat Function

grid-template-columns: repeat(2, 1fr 50px) 20px;

grid-template-columns: 1fr 50px 1fr 50px 20px;

grid-template-rows: repeat(100, 50px);

create the 100 row grid, each row at 50px tall.

specify the number of times you want your column or row to be repeated, followed by a comma and the value you want to repeat.

1fr 50px is repeated twice followed by 20px.

![repeat Function.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6l4lgzmj30xm0eajt6.jpg)

### minmax Function

It's used to limit the size of items when the grid container changes size. To do this you need to specify the acceptable size range for your item. 

grid-template-columns: 100px minmax(50px, 200px);

set to create two columns; the first is 100px wide, and the second has the minimum width of 50px and the maximum width of 200px.

set to repeat 3 columns with the minimum width of 90px and maximum width of 1fr.

![minmax Function.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6ov8onqj31520fgmz9.jpg)

### auto-fill

This allows you to automatically insert as many rows or columns of your desired size as possible depending on the size of the container. You can create flexible layouts when combining auto-fill with minmax.会随着窗口有响应式

If your container can't fit all your items on one row, it will move them down to a new one.

![auto-fill.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6qa7k6vj312e0nodji.jpg)

### auto-fit

The only difference is that when the container's size exceeds the size of all the items combined, auto-fill keeps inserting empty rows or columns and pushes your items to the side, while auto-fit collapses those empty rows or columns and stretches your items to fit the size of the container.

If your container can't fit all your items on one row, it will move them down to a new one.

第一个有autofit则会自动换行，第二个没有则会跑出窗外

![auto-fit.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8h6qa3s7hj30bs0kq3yr.jpg)

### Responsive Layouts with media and grid

<mark>example</mark>

# Others

## 附件

HTML 标签列表(字母排序)
https://www.w3cschool.cn/htmltags/html-reference.html

CSS学习参考书籍推荐
https://www.w3cschool.cn/html/html-css.html

## 免费HTML模板下载

https://www.w3cschool.cn/html/html-template.html

## 其他补充

## 块级格式化上下文（Block Formatting Context）
1. 表现

   盒子在容器（包含块）内从上到下一个接一个地放置
   两个兄弟盒之间的竖直距离由 margin 属性决定
   同一个 BFC 内垂直 margin 会合并
   盒子的左外边缘挨着容器（包含块）的左边

2. 特性

   但是浮动元素后面的行级盒子会变短以避开浮动元素
   BFC 的高度会包含其内的浮动元素
   BFC 不会和浮动元素重叠
   BFC 可以通过 overflow:hidden 等方法创建

3. 创建方法

   浮动框
   绝对定位框
   非块级的块容器（inline-block）
   overflow属性为非visible的块框

## 行级格式化上下文（Inline Formatting Context）

表现

盒子一个接一个水平放置盒之间的水平
margin，border和padding 都有效
同一行的盒子所在的矩形区域叫行盒(Line box)
当一个行盒放不下上下文内所有盒子时，会被分到多个垂直堆叠的行盒里
行盒内的水平分布由'text-align'属性决定
如果一个行级块无法分割(单词、inline-block)，该元素会被作为一个整体决定分布在哪一个行盒

## @keyframes and animation Properties

**animation properties**

1. animation-duration

2. animation-name

3. animation-fill-mode:forwards

   animation 动画停止在用户动作结束后
   the style applied to an element when the animation has finished

   ![animation-fill-mode.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ob6j82ntj309m0azdfx.jpg)

4. animation-iteration-count: infinite
   allows you to control how many times you would like to loop through the animation.

   ![animation-iteration-coun.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ob6jb7ncj30hk0yiq61.jpg)

5. animation-timing-function

   controls how quickly an animated element changes over the duration of the animation. 

   a. ease：starts slow, speeds up in the middle, and then slows down again in the end
   b. ease-out：quick in the beginning then slows down

   c. ease-in：which is slow in the beginning, then speeds up at the end,
   d. linear：applies a constant animation speed throughout.

   

   animation-timing-function: cubic-bezier(0.25, 0.25, 0.75, 0.75);
   https://learn.freecodecamp.org/responsive-web-design/applied-visual-design/learn-how-bezier-curves-work
   https://learn.freecodecamp.org/responsive-web-design/applied-visual-design/use-a-bezier-curve-to-move-a-graphic
   https://learn.freecodecamp.org/responsive-web-design/applied-visual-design/make-motion-more-natural-using-a-bezier-curve/

   

   ![animation-timing-function.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8ob6jdgmsj30ky10iadw.jpg)

   多个动画用逗号分割，animation的简写顺序不影响

   Just space-separate all the individual values. The order doesn’t matter except when using both duration and delay, they need to be in that order. In the example below 1s = duration, 2s = delay, 3 = iterations. 
   
   ```css
   animation: test 1s 2s 3 alternate backwards
   ```

   ```css
animation: 
   pulse 3s ease infinite alternate, 
nudge 5s linear infinite alternate;
   ```
   
   [animation example](https://codepen.io/team/css-tricks/pen/c6d27fda8e1244d44bf04728049d7c1d?editors=1100)
   
   [**animation**](https://css-tricks.com/almanac/properties/a/animation/)
   
   [**Keyframe Animation Syntax**](https://css-tricks.com/snippets/css/keyframe-animation-syntax/)
   
   [MDN animation](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation)
   
   | `animation-timing-function` | ease, ease-out, ease-in, ease-in-out, linear, cubic-bezier(x1, y1, x2, y2) (e.g. cubic-bezier(0.5, 0.2, 0.3, 1.0)) |
   | --------------------------- | ------------------------------------------------------------ |
   | `animation-duration`        | Xs or Xms                                                    |
   | `animation-delay`           | Xs or Xms                                                    |
   | `animation-iteration-count` | X                                                            |
   | `animation-fill-mode`       | forwards, backwards, both, none                              |
   | `animation-direction`       | normal, alternate                                            |
   | `animation-play-state`      | paused, running, running                                     |

animation-name: declares the name of the @keyframes at-rule to manipulate.
animation-duration: the length of time it takes for an animation to complete one cycle.
animation-timing-function: establishes preset acceleration curves such as ease or linear.
animation-delay: the time between the element being loaded and the start of the animation sequence (cool examples).
animation-direction: sets the direction of the animation after the cycle. Its default resets on each cycle.
animation-iteration-count: the number of times the animation should be performed.
animation-fill-mode: sets which values are applied before/after the animation.
For example, you can set the last state of the animation to remain on screen, or you can set it to switch back to before when the animation began.
animation-play-state: pause/play the animation.

6. @keyframes

syntax

```css
@keyframes 动画的名称{
   from{ }
   to{ }
}

@keyframes 动画的名称{
     1%{}
     2%{}
		100%{}
} 
```

rule controls what happens during that animation.

percentages ranging from 0% to 100%, 0% is how the element displays in the opening scene. The CSS properties for 100% is how the element appears at the end, 

![2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8oba5l5p8j307o071dfm.jpg)
![3.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8oba5mnxnj30770e0jrg.jpg)

设置鼠标hover的时候背景颜色改变

![4.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obaj9bswj30gp0bi0su.jpg)

鼠标滑动，体积变大

![5.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obaj7usfj30qg0gw40q.jpg)

elements have a specified position, such as fixed or relative, the CSS offset properties right, left, top, and bottom can be used in animation rules to create movement.

![6.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obb1d4pej30fw1000w1.jpg)

注意div在只剩一个percentage的情况下的位置移动

![7.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obb1bs6wj30hk0vmwgx.jpg)

## accesskey attribute

function

HTML offers the accesskey attribute to specify a shortcut key to activate or bring focus to an element. This can make navigation more efficient for keyboard-only users.

HTML5 allows this attribute to be used on any element, but it's particularly useful when it's used with interactive ones. This includes links, buttons, and form controls.

![accesskey attribute.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obbm5c6sj30ki02qglm.jpg)
![accesskey attribute2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obbmb7aaj30ri0viwj8.jpg)

## tabindex attribute
1. functions

   When it's on a tag, it indicates that element can be focused on. 

   The value (an integer that's positive, negative, or zero) determines the behavior.

2. negative value

   an element is focusable, but is not reachable by the keyboard.

   This method is generally used to bring focus to content programmatically (like when a div used for a pop-up window is activated), and is beyond the scope of these challenges.

3. positive value

   tabindex属性还指定元素的确切Tab键顺序。 当属性的值设置为1或更高的正数时，可以实现这一点。

   设置tabindex =“1”将首先将键盘焦点放在该元素上。 然后它循环显示指定的tabindex值（2,3等）的序列，然后移动到默认值和tabindex =“0”项。

   重要的是要注意，当以这种方式设置Tab键顺序时，它会覆盖默认顺序（使用HTML源）。 这可能会使期望从页面顶部开始导航的用户感到困惑。 在某些情况下，这种技术可能是必要的，但就可访问性而言，在应用之前要小心。

   ![positive value.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obbxqchrj30re0i4jtv.jpg)

4. others
   automatically receive keyboard focus when a user tabs through a page. It's in the same order as the elements come in the HTML source markup

   ![positive value2.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obbxobicj31ce040aax.jpg)

## @media

Media Queries are a new technique introduced in CSS3 that change the presentation of content based on different viewport sizes. The viewport is a user's visible area of a web page, and is different depending on the device used to access the site.Remember, the CSS inside the media query is applied only if the media type matches that of the device being used.

![media.png](http://ww1.sinaimg.cn/large/005NUwyggy1g8obbxsjgzj30r80eeta1.jpg)

```css
@media only screen and (max-width: 600px) {
  body {
    background-color: lightblue;
  }
}
```

Change the background color of the <body> element to "lightblue" when the browser window is 600px wide or less: 

### 语法

要在`.css`样式表中使用媒体查询，我们从`@media`关键字开始，并定义可选的媒体类型和零个或多个功能。

```css
@media type and (feature) {
  .foo {
    font-size: 15px;
    /* ... */
  }
}
```

`@media`块中的规则仅在媒体查询表达式（类型和特征）为真时才会激活。例如，只有当窗口的最小宽度在所有媒体类型上至少为 768px 或更大时，Bootstrap 程序小设备列才会激活。媒体查询可以这样写：

```css
@media all and (min-width: 768px) {
  .col-sm-1 {
    width: 8.333333%;
  }
  .col-sm-2 {
    width: 16.666666%;
  }
  /* so on... */
}
```

这就是 bootstrap 列类能够根据查看内容的窗口宽度进行更改的方式。

### 媒体类型

你可以通过包含媒体类型来定义要应用 css 的媒体类型。接受的类型包括`all，print,screen，speech`。如果你不包含类型，则将隐含`all`类型。`print`用于在打印预览模式下在屏幕上查看的文档。`screen`用于彩色电脑屏幕。`speech`用于语音合成器。

### 逻辑运算符

如果希望在所有条件均为真时媒体查询为真，请使用`and`将它们连接在一起。例如，如果你想要`screen`，当窗口大于 768px 并且屏幕是彩色屏幕时：

```css
@media screen and (min-width: 768px) and (color) {
  /* css rules */
}
```

如果你希望有多个满意的条件，例如当屏幕在彩色屏幕上小于特定大小，或者在单色屏幕上大于特定大小时，你可以使用`,`连接它们：

```css
@media (max-width: 600px) and (color), (min-width: 800px) and (monochrome) {
  /* css rules */
}
```

最后，你可以使用`not`反转整个查询的条件。如果它是真的，它将变为假，如果它是假的，它将成为真实。当存在由逗号分隔的多个条件时，`not`会仅适用于它所处的表达式。

```css
@media not all and (color) {
  /* ... */
}
/* is evaluated like this */
@media not (all and (color)) {
  /* ... */
}

@media not speech and (color), print and (color) {
  /* ... */
}
/* is evaluated like this */
@media (not (speech and (color))), print and (color) {
  /* ... */
}
```

### 媒体功能

有许多媒体功能，但我们用来使 CSS 响应的是`width`。其他包括`height，aspect-ratio，color，resolution`等。大多数功能都可以使用最小值和最大值。为了演示如何设置自己的响应式 CSS 规则，我们可以使用 Bootstrap 示例。由于 Bootstrap 首先是移动的，因此超小屏幕的列宽是默认设置，不包含在媒体查询中。这解释了为什么`col-xs- *`设置将传播到更大的屏幕宽度。遵循 CSS 的级联规则，应在较小的屏幕宽度之后放置较大屏幕宽度的规则，以便在满足媒体查询条件时，它们将覆盖较小屏幕尺寸的规则。

```css
/* Extra small devices (phones, less than 768px) */
/* No media query since this is the default in Bootstrap */
.col-xs-1 {
  width: 8.333333%;
}

/* Small devices (tablets, 768px and up) */
@media (min-width: 768px) {
  .col-sm-1 {
    width: 8.333333%;
  }
}

/* Medium devices (desktops, 992px and up) */
@media (min-width: 992px) {
  .col-md-1 {
    width: 8.333333%;
  }
}

/* Large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) {
  .col-lg-1 {
    width: 8.333333%;
  }
}
```

**例子**

制作自己的自定义响应 CSS 非常简单，只需设置所需的媒体查询并添加 CSS 规则即可。例如，我们创建了一个更改背景颜色的小方框，内部文本将根据屏幕的宽度进行不同的对齐。

```css
<div class="foo">
  <p>The weather is good outside</p>
</div>
.foo {
  background: red;
  text-align: left;
  color: white;
}

@media (min-width: 768px) {
  .foo {
    background: green;
    text-align: center;
  }
}

@media (min-width: 992px) {
  .foo {
    background: blue;
    text-align: right;
  }
}
```

![bootstrap-media](https://tva1.sinaimg.cn/large/006y8mN6ly1g73jtptmg2j30wi02djr6.jpg)

### Getchas

编写响应式 CSS 有一点需要注意的是，媒体查询也遵循级联规则。对于最小宽度语句，你应该在较小的最小宽度值之后放置较大的最小宽度值的规则集。因此，较大屏幕的规则将覆盖较小屏幕的规则。反之亦然，最大宽度。

```css
@media (min-width: 768px) {
  .foo {
    background: green;
  }
}

@media (min-width: 992px) {
  .foo {
    background: blue;
  }
}

@media (min-width: 1200px) {
  .foo {
    background: red;
  }
}

@media (max-width: 1119px) {
  .bar {
    ...;
  }
}

@media (max-width: 991px) {
  .bar {
    ...;
  }
}

@media (max-width: 767px) {
  .bar {
    ...;
  }
}
```

## Horizontal Align

块元素水平对齐

1. margin

如果宽度是100％，对齐是没有效果的。

```css
.center 
{ 
margin:auto;
width:70%; 
background-color:#b0e0e6; 
}
```

2. position

使用绝对定位

```css
.right 
{ 
position:absolute; 
right:0px; 
width:300px; 
background-color:#b0e0e6; 
}
```

3. float

```css
.right 
{ 
float:right; 
width:300px; 
background-color:#b0e0e6; 
}
```

4. padding

```css
.center {
    padding: 70px 0;
    border: 3px solid green;
}

.center {
    padding: 70px 0;
    border: 3px solid green;
    text-align: center;
}
```

内联元素对齐

## 导航栏

## 垂直导航栏

`list-style-type:none` - 移除列表前小标志。一个导航栏并不需要列表标记

移除浏览器的默认设置将边距和填充设置为0

display:block - 显示块元素的链接，让整体变为可点击链接区域（不只是文本），它允许我们指定宽度

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul
{
list-style-type:none;
margin:0;
padding:0;
}
  a{
    list-style:none;
  }
</style>
</head>
<body>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#news">News</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>
</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul
{
list-style-type:none;
margin:0;
padding:0;
}
a:link,a:visited
{
display:block;
font-weight:bold;
color:#FFFFFF;
background-color:#98bf21;
width:120px;
text-align:center;
padding:4px;
text-decoration:none;
text-transform:uppercase;
}
a:hover,a:active
{
background-color:#7A991A;
}
</style>
</head>

<body>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#news">News</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>
</body>
</html>
```

## 水平导航栏

### 内联

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul
{
list-style-type:none;
margin:0;
padding:0;
}
li
{
display:inline;
}
</style>
</head>

<body>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#news">News</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>

</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul
{
list-style-type:none;
margin:0;
padding:0;
padding-top:6px;
padding-bottom:6px;
}
li
{
display:inline;
}
a:link,a:visited
{
font-weight:bold;
color:#FFFFFF;
background-color:#98bf21;
text-align:center;
padding:6px;
text-decoration:none;
text-transform:uppercase;
}
a:hover,a:active
{
background-color:#7A991A;
}

</style>
</head>

<body>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#news">News</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>

<p><b>Note:</b> If you only set the padding for a elements (and not ul), the links will go outside the ul element. Therefore, we have added a top and bottom padding for the ul element.</p>
</body>
</html>
```

### 浮动

但如果你想链接到具有相同的大小，你必须使用浮动的方法。

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
      }
      li {
        float: left;
      }
      a {
        display: block;
        width: 60px;
        background-color: #dddddd;
      }
    </style>
  </head>

  <body>
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#news">News</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#about">About</a></li>
    </ul>

    <p>
      <b>Note:</b> If a !DOCTYPE is not specified, floating items can produce
      unexpected results.
    </p>

    <p>
      A background color is added to the links to show the link area. The whole
      link area is clickable, not just the text.
    </p>

    <p>
      <b>Note:</b> overflow:hidden is added to the ul element to prevent li
      elements from going outside of the list.
    </p>
  </body>
</html>

```

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul
{
list-style-type:none;
margin:0;
padding:0;
overflow:hidden;
}
li
{
float:left;
}
a:link,a:visited
{
display:block;
width:120px;
font-weight:bold;
color:#FFFFFF;
background-color:#98bf21;
text-align:center;
padding:4px;
text-decoration:none;
text-transform:uppercase;
}
a:hover,a:active
{
background-color:#7A991A;
}

</style>
</head>

<body>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#news">News</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#about">About</a></li>
</ul>
</body>
</html>
```

## note

float:left - 使用浮动块元素的幻灯片彼此相邻

display:block - 显示块元素的链接，让整体变为可点击链接区域（不只是文本），它允许我们指定宽度

width:60px - 块元素默认情况下是最大宽度。我们要指定一个60像素的宽度

display:inline - 默认情况下，<li>元素是块元素。在这里，我们删除换行符之前和之后每个列表项，以显示一行。

元素是块元素。在这里，我们删除换行符之前和之后每个列表项，以显示一行 。

## 下拉菜单

[下拉菜单](https://www.w3cschool.cn/css/xohvqfmc.html)
## 图片廊

https://wx3.sinaimg.cn/mw690/6364aedfly1g1dq3ac04nj20u00u0h02.jpg