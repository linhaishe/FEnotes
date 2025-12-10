# Stage 1 ALL

# ==BOM==

# BOM介绍

## 1. 什么是BOM

在JavaScript中，BOM是指“Browser Object Model”，即浏览器对象模型。它是JavaScript与浏览器交互的接口，提供了一组用于操作浏览器窗口、文档、历史记录、位置等浏览器相关对象的API。如浏览器历史记录、浏览器窗口大小、屏幕显示、定时器、Cookie等。

## 2. BOM的作用和用途

BOM的作用和用途主要有以下几点：

a. 操作浏览器窗口：BOM提供了可以通过JavaScript代码控制浏览器窗口大小、位置、状态栏、工具栏等属性的API。

b. 操作浏览器文档：BOM提供了可以通过JavaScript代码访问和操作当前文档的API，例如获取和修改文档内容、创建和删除文档元素等。

c. 操作浏览器历史记录：BOM提供了可以通过JavaScript代码操作浏览器历史记录的API，例如在历史记录中前进或后退、改变当前页面的URL等。

d. 操作浏览器位置：BOM提供了可以通过JavaScript代码获取和设置当前页面的位置信息的API，例如获取当前页面的经纬度、获取当前页面的地址等。

## 3. BOM的优缺点

优点：

1. BOM 提供了丰富的浏览器操作和信息获取功能，开发者可以通过 BOM API 来控制浏览器窗口、历史记录、定时器、屏幕显示等非标准化对象。
2. BOM 的 API 可以方便地获取浏览器的相关信息，比如浏览器的类型、版本、语言、分辨率等，可以帮助开发者更好地优化页面。
3. BOM 是浏览器提供的对象模型，与 DOM（文档对象模型）相互配合，可以实现浏览器与页面的交互，如表单提交、AJAX 等操作。
4. 提供了丰富的浏览器操作和信息获取功能，使得开发者能够更加灵活地控制浏览器行为。
5. 可以通过BOM操作浏览器窗口大小和位置，实现一些特定的需求。
6. 提供了操作浏览器历史记录的方法，实现浏览器前进和后退等功能。
7. 提供了定时器的方法，可以按照一定时间间隔执行特定的代码。
8. 可以获取浏览器的信息，如浏览器类型、版本、语言、分辨率等。

缺点：

a. BOM的API在不同浏览器之间存在差异，因此编写跨浏览器的代码需要额外的注意。

b. BOM的API对浏览器的性能和安全性有一定的影响，不当使用可能导致性能问题和安全漏洞。

c. BOM的API不包含对JavaScript语言本身的扩展，因此不适用于非浏览器环境下的JavaScript应用程序。

d. BOM的某些功能容易被滥用，从而导致页面性能问题或者安全问题。

e. BOM只能在浏览器环境中使用，不能在其他环境（如Node.js）中使用。

# window对象

BOM (浏览器对象模型) 中的 `window` 对象是 JavaScript 中的全局对象，window对象表示整个浏览器窗口，它包含了许多属性和方法，如document、navigator、history、setTimeout等。

虽然每个窗口或标签页都有一个对应的window对象，但是不同窗口或标签页之间的window对象是相互独立的，它们之间不能直接访问和操作。如果需要在不同窗口或标签页之间进行通信，可以使用一些技术，如消息传递、共享数据存储等。

1. 全局作用域：`window` 对象包含了所有 JavaScript 全局变量和函数。在浏览器中定义的全局变量和函数都是 `window` 对象的属性和方法。
2. 窗口控制：`window` 对象提供了控制当前浏览器窗口或标签页的方法和属性。例如，可以使用 `window.open()` 方法打开一个新的浏览器窗口。
3. 文档控制：`window` 对象提供了与当前文档交互的方法和属性。例如，可以使用 `window.document` 属性来访问当前文档对象。
4. 定时器：`window` 对象提供了 `setTimeout()` 和 `setInterval()` 方法，可以用来执行一些异步操作，例如延迟执行某个函数。
5. 浏览器信息：`window` 对象提供了许多属性和方法，用于获取浏览器信息，例如浏览器名称、版本和分辨率等。

- window对象的属性和方法

  [MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/Window#%E5%B1%9E%E6%80%A7)

- window对象控制浏览器窗口

  - window.open(url, name, specs, replace)：打开一个新窗口，并返回该窗口的引用。
  - window.close()：关闭当前窗口。
  - window.resizeTo(width, height)：调整窗口大小到指定的宽度和高度。
  - window.moveTo(x, y)：将窗口移动到指定的屏幕坐标位置。
  - window.location.href：获取或设置当前窗口的URL地址。
  - window.document：获取当前窗口所包含的文档对象。

- window对象控制浏览器的导航行为

  - window.location.href：获取或设置当前窗口的URL地址。
  - window.location.assign(url)：将当前窗口的URL地址设置为指定的url，并跳转到该URL。
  - window.location.replace(url)：用指定的URL替换当前窗口的历史记录中的当前条目，并在浏览器的历史记录中创建一个新的记录，使得用户不能使用“后退”按钮返回到前一个页面。
  - window.location.reload()：重新加载当前页面。


# location对象

## location对象的概念和作用

`location`对象是 JavaScript 中一个预定义的全局对象，表示当前页面的 URL 地址和相关信息。它提供了许多有用的属性和方法，用于获取和操作当前页面的 URL 地址。

window对象和location对象是 BOM（浏览器对象模型）中的两个重要对象，它们之间有一定的关系。

可以通过window.location或location的方式来访问和修改当前文档的URL。window.location.href和location.href都可以返回当前文档的完整URL，它们是等价的。window.location.assign()和location.assign()都可以用来加载一个新的URL，并在浏览器的历史记录中添加一个新的记录。

因此，可以说location对象是window对象的一部分(下同)，同时也是window对象中的一个属性，用来表示当前文档的URL。在使用BOM操作时，我们通常需要同时使用window对象和location对象来实现我们的需求。

## location对象的属性和方法

- `location.href`：获取当前页面的完整 URL 地址。
- `location.protocol`：获取当前页面的协议（例如：http 或 https）。
- `location.host`：获取当前页面的主机名（包括端口号）。
- `location.hostname`：获取当前页面的主机名（不包括端口号）。
- `location.port`：获取当前页面的端口号。
- `location.pathname`：获取当前页面的路径部分。
- `location.search`：获取当前页面的查询字符串部分。
- `location.hash`：获取当前页面的锚点部分。
- `location.assign(url)`：用于加载一个新的文档。
- `location.reload()`：用于重新加载当前文档。
- `location.replace(url)`：用于替换当前文档，不会在浏览器历史记录中创建新条目。

# history对象

## history对象的概念和作用

`history` 对象是 JavaScript 中一个预定义的全局对象，表示浏览器的历史记录。它提供了一些有用的方法和属性，用于操作浏览器的历史记录，实现前进、后退等操作。

## history对象的属性和方法

1. history.back()：在浏览器历史记录中后退一页。
2. history.forward()：在浏览器历史记录中前进一页。
3. history.go(n)：在浏览器历史记录中向前或向后跳转n个页面，其中n可以是负数。
4. history.pushState(stateObj, title, url)：将新的URL添加到浏览器历史记录中，但不会导致页面刷新。
5. history.replaceState(stateObj, title, url)：将当前页面的URL替换为新的URL，但不会导致页面刷新。

# navigator对象

## navigator对象的概念和作用

`navigator` 对象是 JavaScript 中一个预定义的全局对象，提供了有关浏览器的信息，例如浏览器的名称、版本、操作系统等信息。通过 `navigator` 对象，我们可以检测当前浏览器的特性，编写出更加兼容不同浏览器的 JavaScript 代码。

## navigator对象的属性和方法

1. `navigator.userAgent`：返回当前浏览器的用户代理字符串，包含浏览器名称、版本、操作系统等信息。
2. `navigator.appName`：返回当前浏览器的名称，例如 "Netscape" 或 "Microsoft Internet Explorer"。
3. `navigator.appVersion`：返回当前浏览器的版本，例如 "5.0 (Windows; en-US)"。
4. `navigator.platform`：返回当前浏览器的操作系统平台，例如 "Win32" 或 "MacIntel"。
5. `navigator.language`：返回当前浏览器的首选语言，例如 "en-US" 或 "zh-CN"。
6. `navigator.geolocation` 方法可以检测当前浏览器是否支持地理位置定位功能。

# screen对象

## screen对象的概念和作用

`screen` 对象是 JavaScript 中一个预定义的全局对象，代表当前浏览器所在的屏幕。`screen` 对象提供了有关当前屏幕的信息，例如屏幕的宽度、高度、可见区域大小等信息。通过 `screen` 对象，我们可以根据不同屏幕的大小和分辨率，动态调整页面布局，以适应不同的设备。

## screen对象的属性和方法

1. `screen.width`：返回屏幕的宽度，单位为像素。
2. `screen.height`：返回屏幕的高度，单位为像素。
3. `screen.availWidth`：返回屏幕可用区域的宽度，单位为像素。
4. `screen.availHeight`：返回屏幕可用区域的高度，单位为像素。
5. `screen.pixelDepth`：返回屏幕的颜色深度，单位为位数。
6. `screen.orientation`：返回屏幕的方向，例如 "landscape-primary" 或 "portrait-secondary"。

# 安全问题

1. 弹出窗口被浏览器屏蔽

   浏览器通常会默认屏蔽弹出窗口。如果网站滥用弹出窗口，可能会被浏览器识别为恶意行为而被屏蔽。

2. 跨域脚本攻击（XSS）

   由于浏览器存在同源策略（Same-Origin Policy），因此在跨域访问时，BOM 操作可能会导致安全问题。

   a. 在一个 iframe 中嵌入一个来自其他域名的页面，如果页面中存在恶意代码，则可能通过 BOM 操作来窃取用户的敏感信息。

   b. 如果我们使用 `location.href` 来修改 URL，而这个 URL 包含恶意脚本，那么这些恶意脚本可能会在用户浏览该页面时执行。

   因此，我们需要确保 URL 是安全的，并对用户输入进行验证和过滤。

3. 误操作

   BOM 操作可能会被用于欺骗用户，例如通过弹出窗口来模拟登录页面，以达到盗取用户密码的目的。

4. 脚本注入

   由于 BOM 操作可以在浏览器中执行任意脚本，因此可能会被用于进行脚本注入攻击，例如将恶意脚本注入到页面中，以达到窃取用户信息或者控制用户计算机的目的。

# 兼容性问题

BOM（浏览器对象模型）是由各个浏览器厂商自行实现的一组 JavaScript API，因此不同的浏览器可能会有一些不同的实现细节，从而导致 BOM 的兼容性问题。

1. 属性和方法的兼容性

   不同浏览器对 BOM 中的属性和方法的实现可能存在差异，例如 IE 和 Firefox 对于 window.innerHeight 和 window.innerWidth 的实现就不同。因此，在编写代码时，需要根据浏览器类型进行兼容性处理。

2. 事件的兼容性

   不同浏览器对事件的处理方式也可能存在差异。例如，在 IE 中，可以使用 window.attachEvent() 来绑定事件，而在其他浏览器中则需要使用 window.addEventListener()。因此，为了确保代码在各种浏览器中都能正常运行，需要根据浏览器类型来选择不同的事件绑定方式。

3. 对象的兼容性

   有些浏览器可能会对 BOM 中的某些对象进行扩展或者修改，从而导致在其他浏览器中无法使用。例如，IE 中提供了 ActiveXObject 对象来访问浏览器的各种功能，而在其他浏览器中则没有这个对象。

为了解决这些兼容性问题，我们可以使用一些兼容性库或者框架，例如 jQuery、Modernizr 等，它们可以屏蔽底层浏览器差异，并提供一致的跨浏览器的 API 接口。此外，在编写代码时，也应该注意遵守一些兼容性的最佳实践，例如避免使用浏览器特定的特性，尽量使用标准的 API 接口等等。

# BOM和DOM

## BOM和DOM的关系和区别

BOM（浏览器对象模型）和DOM（文档对象模型）都是用来描述浏览器中的文档的模型，但是它们的作用不同，有一些区别。

BOM是浏览器提供的一组JavaScript API，用来描述浏览器窗口或标签页以及浏览器本身的状态和功能。BOM包括了window、navigator、location、history等对象，这些对象都是浏览器提供的全局对象，用来描述浏览器的各种状态和行为。BOM主要用来操作浏览器的窗口、页面导航、历史记录、定时器等功能。

DOM则是描述文档的结构、内容和样式的一组API，通过DOM可以访问和操作文档中的元素、属性、文本内容和样式等。DOM主要用来操作HTML、XML等文档，可以用来添加、修改、删除文档的元素和属性，以及操作文档的事件和样式等。

BOM和DOM的关系在于，它们都是JavaScript操作浏览器中的文档的接口，而且它们的对象都是全局对象，可以通过JavaScript代码直接访问和操作。但是它们的作用和目标不同，BOM主要用来操作浏览器的窗口和功能，而DOM主要用来操作文档的结构和内容。DOM和BOM虽然都是浏览器提供的对象模型，但它们并不是标准，不同浏览器之间可能会存在一些差异。

## 如何在BOM和DOM之间进行通信和交互

1. 使用window对象：BOM中的window对象是操作浏览器窗口和页面的入口点，它包含了document、location、history等对象，可以通过window对象来访问和操作这些对象。同时，DOM中的文档对象也可以通过window对象来访问，如window.document、window.frames等。
2. 使用iframe元素：在DOM中，可以使用iframe元素来在文档中嵌入其他文档或网页。在嵌入的文档中，可以通过window.parent对象来访问父文档的window对象，从而实现与父文档的通信和交互。
3. 使用postMessage方法：postMessage是HTML5新增的方法，用于在不同窗口或标签页之间进行跨域通信。可以通过postMessage方法向其他窗口发送消息，并通过事件监听器来接收响应。
4. 使用cookie和localStorage：cookie和localStorage是BOM中提供的两个数据存储方式，可以在不同窗口或标签页之间共享数据。可以在一个窗口中使用cookie或localStorage存储数据，在另一个窗口中通过读取cookie或localStorage来获取数据。

BOM和DOM之间的通信和交互需要注意安全问题，特别是跨域通信时需要考虑安全策略和防止恶意攻击。同时，不同浏览器对BOM和DOM的实现可能存在差异，需要进行兼容性处理。

# 性能优化

BOM 操作的性能问题主要表现在以下两个方面：

1. DOM 操作的阻塞

   BOM 操作通常需要与 DOM 操作配合使用，如果 DOM 操作过于频繁或者复杂，可能会阻塞浏览器的渲染进程，导致页面卡顿或者崩溃。

2. 大量计算的开销

   BOM 操作可能会涉及到大量的计算和操作，例如浏览器窗口大小的计算、浏览器标识的解析等，这些计算和操作可能会对页面的性能产生不良影响。

为了避免 BOM 操作的性能问题，我们可以采取以下几个策略：

1. 减少 DOM 操作的频率和复杂度

   在使用 BOM 操作的时候，尽量减少 DOM 操作的频率和复杂度，避免过多的操作阻塞浏览器的渲染进程。例如，在执行一系列的 DOM 操作之前，可以将这些操作合并成一个批量操作，然后一次性执行。

2. 缓存计算结果

   对于需要频繁计算的操作，可以将计算结果缓存起来，避免重复计算。例如，在获取浏览器窗口大小的时候，可以将结果缓存起来，在窗口大小没有发生变化的情况下，直接使用缓存结果。

3. 避免频繁访问 BOM 属性和方法

   在访问 BOM 属性和方法的时候，尽量避免频繁的访问和调用。例如，在获取浏览器标识的时候，可以将标识缓存起来，避免重复调用。

4. 使用异步操作

   对于需要耗时的操作，可以将操作异步化，避免阻塞页面的渲染进程。例如，在加载大量图片的时候，可以使用异步加载的方式，避免阻塞页面的渲染。

5. 避免使用重绘和重排

   在操作 BOM 时，会触发浏览器的重绘和重排，而这些操作通常是比较耗时的。为了避免这种情况，我们应该尽可能减少重绘和重排的次数。

为了避免 BOM 操作的性能问题，我们需要尽可能地减少与浏览器的交互次数，批量处理数据，避免使用循环，减少重绘和重排的次数，以及减少 DOM 操作的次数。

# ==History API==

# 什么是History API？

History API 提供了访问浏览器会话历史记录的功能，通过全局对象 history。它暴露了有用的方法和属性，可以在用户的历史记录中前后导航，并操纵历史记录栈的内容。

History API 是浏览器提供的一组接口，用于操作浏览器的历史记录，包括向前或向后导航、添加或修改历史记录等。使用 History API 可以实现前端路由、单页应用等功能，可以提高页面的性能和用户体验。

# History API的基本用法

![img](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/history-api/history-20230409164701141.png)

| 方法/事件/属性                                  | 描述                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| `history.pushState(stateObject, title, URL)`    | 添加一条新的历史记录，同时修改 URL 和浏览器的地址栏，但不会刷新页面。该方法会触发 `popstate` 事件。 |
| `history.replaceState(stateObject, title, URL)` | 用指定的状态对象、标题和 URL 替换当前历史记录条目。该方法不会添加新条目到历史记录栈中，而是修改当前历史记录条目的内容和 URL。该方法也会触发 `popstate` 事件。 |
| `window.onpopstate` 事件                        | 当浏览器历史记录栈中的活动记录改变时，该事件将被触发。       |
| `history.back()`;`history.go(-1);`              | 将浏览器回退到上一个历史记录，相当于点击浏览器的后退按钮。   |
| `history.forward()`;`history.go(1);`            | 将浏览器前进到下一个历史记录，相当于点击浏览器的前进按钮。   |
| `history.go(0)`; `history.go();`                | refreshing the page                                          |
| `go(n)`                                         | 根据当前页面在历史记录中的位置，移动到相对位置为 `n` 的页面。 |
| `length`                                        | 表示历史记录中页面的数量。                                   |
| `state`                                         | 返回当前页面的状态对象，即最后一个 `pushState()` 或 `replaceState()` 的第一个参数。 |

`pushState` /`replaceState`方法的第一个参数 stateObj 是一个 JavaScript 对象，用于保存当前历史记录的状态信息。当用户通过浏览器的前进或后退按钮返回到该历史记录时，该对象会作为 popstate 事件的 state 属性传递给事件处理函数。事件的 state 属性包含历史记录条目的状态对象的副本。状态对象可以是任何可序列化的内容。因为 Firefox 会将状态对象保存到用户的磁盘上，以便在用户重新启动浏览器后可以恢复它们，所以我们对状态对象的序列化表示强制施加了 640k 字符的大小限制。如果您传递一个其序列化表示超过此限制的状态对象给 pushState()，该方法将抛出异常。

`title`一般不写了,but at the time of writing, every browser simply ignores it.

```js
window.addEventListener("popstate", function(event) {
  if (event.state && event.state.message) {
    const message = event.state.message;
      alert(message);
      }
  });
```

# History API与SEO

## History API与SEO

SEO（Search Engine Optimization，搜索引擎优化）是一种通过优化网站结构、内容和链接等方式，使得网站在搜索引擎中获得更好的排名，从而提高网站的流量和曝光度的技术。SEO 通常是为了让搜索引擎更好地理解网站的内容和结构，从而提高网站在搜索结果中的排名。

1. 使用 History API 可以实现前端路由，使得用户在操作网站时，不需要重新加载整个页面，而只需要更新部分内容。这种方式可以提高用户体验，但对于搜索引擎来说，可能会造成一些困扰，因为搜索引擎更习惯于通过 URL 来索引网页内容，而不是通过 JavaScript 来实现页面的更新。因此，如果使用了前端路由，需要采取一些措施来让搜索引擎更好地理解网站的内容和结构，比如使用动态 URL、添加页面标题和描述、使用 sitemap 等。
2. 如果网站使用了 History API 来更新页面内容，而没有合理地配置页面标题、描述等元信息，那么搜索引擎可能会难以理解网站的内容和结构，从而降低网站的排名和曝光度。因此，使用 History API 的网站需要特别注意页面的元信息的设置，以便让搜索引擎更好地理解网站的内容和结构。

# 使用History API的注意事项

## 安全问题

1. 避免将敏感信息存储在历史记录的状态对象中，因为这些信息可能会被保存到用户的磁盘上，从而导致信息泄露。
2. 避免使用历史记录来存储密码、令牌等敏感信息，因为这些信息可能会被其他网站访问到。
3. 避免使用 `replaceState()` 方法来模拟页面跳转，因为这样会使页面的跳转行为与用户预期不符，从而引起混淆和安全问题。
4. 避免使用 `history.go(-1)` 或 `history.back()` 方法来跳转到前一个页面，因为这样可能会使用户离开当前网站，从而降低用户体验和安全性。
5. 避免使用 `history.pushState()` 和 `history.replaceState()` 来改变页面的 URL，而不是使用服务器端重定向或者页面跳转，因为这样可能会使用户无法复制或分享页面 URL，从而降低网站的可用性。
6. 避免通过 JavaScript 改变页面的 URL 来欺骗用户，例如将一个恶意网站的 URL 伪装成另一个网站的 URL，从而引导用户访问恶意网站。
7. 在使用 pushState() 和 replaceState() 方法时，需要注意 URL 的格式和安全性

## 浏览器兼容性

1. 在 Safari 5.0 和 Chrome 5.0 以前的版本中，不支持状态对象的序列化和反序列化，因此在使用 `pushState()` 或 `replaceState()` 方法时，需要确保状态对象可以被序列化为字符串。
2. 在 Firefox 4.0 和 Chrome 5.0 以前的版本中，使用 `pushState()` 和 `replaceState()` 方法后，浏览器地址栏中的 URL 不会发生改变，需要使用其他技术来修改 URL。
3. 在 IE 10 以前的版本中，不支持 `pushState()` 和 `replaceState()` 方法，需要使用其他技术来实现历史记录的管理。
4. 在移动设备上，例如 iOS 和 Android，因为设备的资源有限，所以对历史记录的管理可能存在一些限制和差异，需要注意兼容性问题。
5. 对于不支持 History API 的浏览器，可以使用 hash 路由来模拟路由。

## 性能问题

1. 频繁调用 `pushState()` 和 `replaceState()` 方法可能会影响性能。因为每次调用这些方法都会创建一个新的历史记录条目，如果调用次数过多，会导致历史记录栈变得很大，占用大量内存，同时也会增加页面的加载和渲染时间。因此，应该尽量避免频繁调用这些方法，只在必要时使用。
2. 在使用状态对象时，需要注意对象的大小。因为状态对象需要被序列化和保存到本地存储中，如果对象过大，会增加序列化和反序列化的时间和内存消耗，超过640k会抛出异常。同时，状态对象也会被保存在本地存储中，如果保存的历史记录过多，也会占用大量的存储空间。因此，在使用状态对象时，应该尽量保持对象的简单和小巧。
3. 在监听历史记录变化时，需要注意监听器的数量和复杂度。因为每个监听器都会被触发，如果监听器数量过多，会增加页面的加载和渲染时间，同时也会增加 CPU 的负担。因此，在编写监听器时，应该尽量保持监听器数量的少和简单，只监听必要的事件。

# 示例应用

- 实现单页应用
- 实现浏览器历史记录管理

# 如何处理在浏览器中使用的 hash 和 history 模式

# ==localstorage & sessionstorage & cookie & indexDB==

# WEB Storage API

The [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API) is a set of mechanisms that enable browsers to store key-value pairs. It is designed to be much more intuitive than using cookies.

The key-value pairs represent storage objects, which are similar to objects except they remain intact during page loads, and are always strings. You can access these values like an object or using the `getItem()` method (more on that later).

Web Storage API 是浏览器提供的一组机制，用于在浏览器中存储和检索数据。它使用键值对来存储数据，并且可以存储大量的数据，最大可达到 5MB。Web Storage API 包括两种类型的存储：localStorage 和 sessionStorage。

localStorage 存储的数据可以在同一个域名的不同页面间共享，直到用户清除浏览器缓存或使用代码清除 localStorage 中的数据为止。而 sessionStorage 存储的数据仅在同一标签页中有效，在用户关闭标签页或浏览器后，数据会被自动清除。

通过 Web Storage API，开发者可以轻松地将数据存储在用户的浏览器中，而无需使用 cookies 或向服务器发送大量请求。这在开发需要缓存数据或离线应用程序时非常有用。

# localstorage & sessionstorage

LocalStorage而言，数据是保存在浏览器的本地存储中的，所以确实只能在同一台设备上的同一款浏览器中访问和处理数据。不同的浏览器之间是无法共享LocalStorage中的数据的。

1. 容量较大：LocalStorage 的容量一般为 5MB 左右，比 Cookie 能够存储的数据量大得多。

2. 数据持久化：LocalStorage 存储的数据是持久化的，即使用户关闭浏览器后再次访问页面，数据仍然存在。

3. 安全性高：LocalStorage 存储的数据只能被同源的脚本访问，保证了数据的安全性。

   同源的脚本指的是在同一来源（Origin）下运行的脚本，同源指的是协议（如http、https）、域名和端口号三者相同。

   在Web安全中，浏览器遵循同源策略（Same-Origin Policy），它限制了来自不同源的脚本的相互交互。同源策略要求脚本只能读取和修改同一来源下的数据，而无法访问其他来源的数据。这样可以防止恶意网站窃取用户的敏感信息，保障用户的信息安全。

   LocalStorage 也受到同源策略的限制，即只有在同一来源下的脚本才能访问和修改LocalStorage中的数据，如果脚本的来源和LocalStorage中数据的来源不一致，则无法访问和修改LocalStorage中的数据。这也保证了LocalStorage中存储的数据的安全性。

4. 速度快：LocalStorage 存储的数据是在本地浏览器中进行读写，速度相对较快。

5. 可以存储字符串类型数据：LocalStorage 只能存储字符串类型的数据，如果需要存储其他类型的数据，需要将其转换为字符串类型再存储。

需要注意的是，LocalStorage 存储的数据是有限的，容量也是有限的，一般为 5MB 左右，如果需要存储大量的数据，可能需要考虑其他的存储方案。同时，LocalStorage 中的数据只能在同一个浏览器会话中共享，不同的浏览器之间无法共享数据。

## function access

localstorage & sessionstorage Properties and methods are the same

`localStorage.setItem(key, value) `方法设置一个键值对。

`localStorage.getItem(key)`方法获取一个键对应的值。

`localStorage.removeItem(key)` 方法删除一个键值对。

`localStorage.clear()` 方法清除所有的键值对。

`localStorage.key(index);` get the name of a key 

## object-like access

```js
// set key
localStorage.test = 2;

// get key
alert( localStorage.test ); // 2

// remove key
delete localStorage.test;
```

## Strings only

Please note that both key and value must be strings.

If they were any other type, like a number, or an object, they would get converted to a string automatically:

```javascript
localStorage.user = {name: "John"};
alert(localStorage.user); // [object Object]
```

We can use `JSON` to store objects though:

```javascript
localStorage.user = JSON.stringify({name: "John"});

// sometime later
let user = JSON.parse( localStorage.user );
alert( user.name ); // John
```

Also it is possible to stringify the whole storage object, e.g. for debugging purposes:

```javascript
// added formatting options to JSON.stringify to make the object look nicer
alert( JSON.stringify(localStorage, null, 2) );
```

## diff

| 特性             | localStorage                 | sessionStorage                                               |
| ---------------- | ---------------------------- | ------------------------------------------------------------ |
| 存储容量         | 最大可达到 5 MB              | 最大可达到 5 MB                                              |
| 生命周期         | Survives browser restart     | Survives page refresh (but not tab close)                    |
| 跨窗口共享       | 可以在同一域名的不同窗口共享 | 仅在同一标签页的窗口间共享<br />Visible within a browser tab, including iframes from the same origin |
| 跨域名访问       | 不允许跨域名访问             | 不允许跨域名访问                                             |
| 存储位置         | 浏览器的本地文件系统中       | 浏览器的会话存储区                                           |
| 与 HTTP 请求关系 | 不会发送给服务器             | 不会发送给服务器，仅存在于浏览器的 JavaScript 中             |

localStorage 的存储位置是在客户端的浏览器中，具体存储位置可能因浏览器而异。一般来说，localStorage 的数据存储在浏览器的本地文件系统中，通常是存储在用户配置文件夹或缓存文件夹中的一个 SQLite 数据库中，而且该数据库通常是由浏览器厂商提供的。在 Google Chrome 中，localStorage 数据默认存储在 Chrome 用户配置文件夹的 Local Storage 子文件夹中，而在 Firefox 中，localStorage 数据默认存储在用户配置文件夹的 webappsstore.sqlite 文件中。但是，这些存储位置都是由浏览器厂商提供的默认实现，具体实现可能因浏览器而异，也可能因操作系统、浏览器版本和用户配置而异。

## Storage event

使用 Storage event，我们可以实现在多个窗口之间共享同一份 Storage 数据，并实时响应数据的变化。

在同一浏览器选项卡中，localStorage 和 sessionStorage 的修改是实时更新的，因为它们都是存储在浏览器进程的内存中。所以，如果在同一选项卡中修改了 localStorage 或 sessionStorage，其他窗口中的 Storage 对象都可以立即访问到修改后的值，不需要监听 Storage event。

但是，当我们在一个窗口中修改了 localStorage 或 sessionStorage，其他窗口中的 Storage 对象无法立即获取到修改后的值，因为它们存储在不同的 JavaScript 运行环境中。为了实现多个窗口之间共享同一份 Storage 数据并实时响应数据的变化，需要使用 Storage event 监听 Storage 对象的变化，并在事件触发时更新其他窗口中的 Storage 数据。

另外需要注意的是，虽然在同一浏览器选项卡中的窗口之间可以共享 Storage 数据，但是它们是相互独立的，每个窗口都有自己的 JavaScript 运行环境，修改 Storage 数据时也不会互相影响。因此，需要使用 Storage event 监听其他窗口中的 Storage 数据的变化，并在事件触发时及时更新当前窗口的数据。

```js
window.addEventListener('storage', function(event) {
  // Storage 数据发生变化，执行相应的操作
    if (event.key === 'key') {
    // Storage 数据发生变化，更新本窗口中的数据
    var newValue = event.newValue;
    // do something with newValue
});
```

Storage event 仅在同一浏览器选项卡中的窗口之间触发，且事件的发起者（即修改 Storage 数据的窗口）不会接收到事件。同时，在 Safari 浏览器中，如果事件的发起者与监听者是同一窗口，则不会触发 Storage event。此外，由于 Storage event 可能会频繁触发，因此在使用时需要考虑性能问题。

The important thing is: the event triggers on all `window` objects where the storage is accessible, except the one that caused it.

# cookie

Cookie是一种用于在网站之间传递信息的小型文本文件。

HTTP cookie，简称cookie，是**用户浏览网站时由网络服务器创建并由用户的网页浏览器存放在用户计算机或其他设备上的小文本文件**。 Cookie使Web服务器能够在用户的设备上存储状态信息（如添加到在线商店购物车中的商品）或跟踪用户的浏览活动（如点击特定按钮、登录或记录历史）。

## 使用方法

Cookie的使用方法很简单。当用户访问一个网站时，服务器可以将一个包含有用信息的Cookie发送到用户的Web浏览器。该信息可以是用户ID、购物车内容、用户喜好等。当用户浏览其他页面时，浏览器会自动将cookie发送回服务器。服务器可以使用cookie来识别用户并提供个性化的服务。

```js
// wiite
document.cookie = "user=John"; // update only cookie named 'user'
// get
document.cookie

// special characters (spaces), need encoding
let name = "my name";
let value = "John Smith"

// encodes the cookie as my%20name=John%20Smith
document.cookie = encodeURIComponent(name) + '=' + encodeURIComponent(value);

alert(document.cookie); // ...; my%20name=John%20Smith
```

`document.cookie` provides access to cookies.

- Write operations modify only cookies mentioned in it.
- Name/value must be encoded.
- One cookie may not exceed 4KB in size. The number of cookies allowed on a domain is around 20+ (varies by browser).

### Cookie options:

| 属性名   | 描述                                                        |
| -------- | ----------------------------------------------------------- |
| Domain   | 定义 cookie 的有效域名。                                    |
| Expires  | 定义 cookie 的过期时间。(使用的是UTC或GMT时间格式)          |
| HttpOnly | 设置 cookie 只能通过 HTTP 和 HTTPS 协议访问，防止脚本攻击。 |
| Max-Age  | 定义 cookie 的最大生命周期。                                |
| Path     | 定义 cookie 的有效路径。                                    |
| Secure   | 设置 cookie 只能通过 HTTPS 协议传输。                       |
| SameSite | 控制 cookie 的跨站点访问。                                  |
| Value    | 存储在 cookie 中的值。                                      |
| Name     | cookie 的名称。                                             |

- `path=/`, by default current path, makes the cookie visible only under that path.

  If a cookie is set with `path=/admin`, it’s visible at pages `/admin` and `/admin/something`, but not at `/home` or `/adminpage`.

  Usually, we should set `path` to the root: `path=/` to make the cookie accessible from all website pages.

- `domain=site.com`, by default a cookie is visible on the current domain only. If the domain is set explicitly, the cookie becomes visible on subdomains.

```js
// if we set a cookie at site.com website...
document.cookie = "user=John"

// ...we won't see it at forum.site.com
alert(document.cookie); // no user

// 设置domain=site.com后，子域名也可以查看cookie

// at site.com
// make the cookie accessible on any subdomain *.site.com:
document.cookie = "user=John; domain=site.com"

// later

// at forum.site.com
alert(document.cookie); // has cookie user=John
```

- `expires` or `max-age` sets the cookie expiration time. Without them the cookie dies when the browser is closed.

```js
  // expires=Tue, 19 Jan 2038 03:14:07 GMT
  
  // +1 day from now
  let date = new Date(Date.now() + 86400e3);
  date = date.toUTCString();
  document.cookie = "user=John; expires=" + date;
  
  // max-age=3600
  // cookie will die in +1 hour from now
  document.cookie = "user=John; max-age=3600";
  
  // delete cookie (let it expire right now)
  document.cookie = "user=John; max-age=0";
```

- `secure` makes the cookie HTTPS-only.

- `samesite` forbids the browser to send the cookie with requests coming from outside the site. This helps to prevent XSRF attacks.

Additionally:

- Third-party cookies may be forbidden by the browser, e.g. Safari does that by default.
- When setting a tracking cookie for EU citizens, GDPR requires to ask for permission.

Cookie可以在本地或远程存储数据，这取决于将Cookie设置为什么类型。在设置Cookie时，可以使用Domain参数将其设置为可跨域存储。例如，如果您要在域名example.com下的所有子域名中共享Cookie，则可以将Domain参数设置为".example.com"。这样，无论用户访问的是哪个子域名，Cookie都可以被读取和写入。

此外，Cookie还可以通过在HTTP请求中发送到服务器来进行远程存储。服务器可以解析请求头中的Cookie，并根据其中包含的信息采取相应的操作，例如验证用户身份或存储用户偏好设置

## Cookie functions

### [getCookie(name)](https://javascript.info/cookie#getcookie-name)

The shortest way to access a cookie is to use a [regular expression](https://javascript.info/regular-expressions).

The function `getCookie(name)` returns the cookie with the given `name`:

```javascript
// returns the cookie with the given name,
// or undefined if not found
function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
```

Here `new RegExp` is generated dynamically, to match `; name=<value>`.

Please note that a cookie value is encoded, so `getCookie` uses a built-in `decodeURIComponent` function to decode it.

### [setCookie(name, value, options)](https://javascript.info/cookie#setcookie-name-value-options)

Sets the cookie’s `name` to the given `value` with `path=/` by default (can be modified to add other defaults):

```javascript
function setCookie(name, value, options = {}) {

  options = {
    path: '/',
    // add other defaults here if necessary
    ...options
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

// Example of use:
setCookie('user', 'John', {secure: true, 'max-age': 3600});
```

### [deleteCookie(name)](https://javascript.info/cookie#deletecookie-name)

To delete a cookie, we can call it with a negative expiration date:

```javascript
function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}
```

**Updating or deleting must use same path and domain**

Please note: when we update or delete a cookie, we should use exactly the same path and domain options as when we set it.

Together: [cookie.js](https://javascript.info/article/cookie/cookie.js).


## 类型

Cookie有两种类型：会话cookie和持久cookie。

会话cookie只在用户关闭浏览器时存在，而持久cookie可以存储在用户计算机上并在浏览器关闭后仍然存在。持久cookie通常用于存储用户偏好设置、用户名和密码等信息，以便用户下次访问网站时可以更快速地登录。

## 存储位置

Cookie的存储位置取决于使用的Web浏览器和操作系统。通常，它们被存储在用户计算机的临时文件夹中。

以下是常见Web浏览器中cookie的存储位置：

- Chrome：在Windows上，Chrome的cookie文件存储在“C:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Cookies”中；在Mac上，cookie存储在“~/Library/Application Support/Google/Chrome/Default/Cookies”中。
- Firefox：在Windows上，Firefox的cookie文件存储在“C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\profile_folder\cookies.sqlite”中；在Mac上，cookie存储在“~/Library/Application Support/Firefox/Profiles/profile_folder/cookies.sqlite”中。
- Safari：在Mac上，Safari的cookie存储在“~/Library/Cookies/Cookies.plist”中。

请注意，存储cookie的位置可能会因操作系统版本、浏览器版本或用户自定义设置而有所不同。

# indexDB

IndexedDB是一种浏览器内置的NoSQL数据库，用于存储客户端数据，例如浏览器应用程序中的大量数据和离线缓存。IndexedDB支持复杂的查询和索引，并且可以在不影响应用程序性能的情况下处理大量数据。还支持离线访问和缓存，因此用户可以在离线状态下使用应用程序。

IndexedDB的API是异步的，这意味着它使用回调或Promises处理结果。它提供了一组强大的功能，例如复杂查询、索引、范围查询和游标，以便轻松地检索和管理存储在数据库中的数据。

IndexedDB is a database that is built into a browser, much more powerful than localStorage.

- Stores almost any kind of values by keys, multiple key types.(可以通过键来存储几乎任何类型的值，支持多种键类型)

- Supports transactions for reliability.(提供了可靠的数据存储机制)

  这些操作要么全部完成，要么全部失败。可以确保在多个操作中的任何一个失败时，数据不会被永久地改变。这可以防止数据损坏或丢失，并保证数据库的一致性。因此，IndexedDB提供了可靠的数据存储机制。

- Supports key range queries, indexes.(它支持键范围查询和索引)

- Can store much bigger volumes of data than localStorage.



[Jsinfo](https://javascript.info/indexeddb)

[idb npm](https://www.npmjs.com/package/idb)

使用过程

1. 打开(链接)db
2. 获取store对象
3. 对象store进行crud的操作

# Diff for four



| 特性         | localStorage | sessionStorage | Cookie     | IndexedDB    |
| ------------ | ------------ | -------------- | ---------- | ------------ |
| 存储容量     | 5MB          | 5MB            | 4KB        | 大于5MB      |
| 生命周期     | 没有过期时间 | 页面关闭时清除 | 可设置     | 没有过期时间 |
| 存储位置     | 浏览器       | 浏览器         | 客户端     | 浏览器       |
| 跨域支持     | 否           | 否             | 是         | 是           |
| 与服务器通信 | 否           | 否             | 是         | 是           |
| 访问限制     | 无           | 同源策略限制   | 无         | 无           |
| 应用场景     | 单个页面数据 | 单个页面数据   | 跨页面数据 | 大数据存储   |

|               | LocalStorage                                                 | SessionStorage                                               | Cookie                                                       | IndexedDB                                                    |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Scope         | Local                                                        | Local                                                        | Can be used for local or remote                              | Local                                                        |
| Size          | Up to 10MB                                                   | Up to 10MB                                                   | Up to 4KB                                                    | No fixed limit                                               |
| Expiration    | Never                                                        | When the browser session ends                                | Can be set by the server or manually                         | Never                                                        |
| Accessibility | Can be accessed by any window or tab in the same origin      | Can only be accessed by the window or tab that created it    | Can be accessed by any window or tab in the same origin      | Can be accessed by any window or tab in the same origin      |
| Use Case      | Storing data that needs to persist beyond the current session or page reload | Storing data that needs to be available only during the current session or page reload | Storing small amounts of data that needs to be sent to the server with each request | Storing large amounts of structured data for offline use or to reduce server load |

|          | LocalStorage                                     | SessionStorage                                 | Cookie                                   | IndexedDB                                        |
| -------- | ------------------------------------------------ | ---------------------------------------------- | ---------------------------------------- | ------------------------------------------------ |
| 范围     | 本地                                             | 本地                                           | 可用于本地或远程                         | 本地                                             |
| 大小     | 最多10MB                                         | 最多10MB                                       | 最多4KB                                  | 没有固定限制                                     |
| 过期时间 | 永不过期                                         | 当浏览器会话结束时                             | 可由服务器或手动设置                     | 永不过期                                         |
| 可访问性 | 可被同源下任何窗口或标签访问                     | 仅可被创建它的窗口或标签访问                   | 可被同源下任何窗口或标签访问             | 可被同源下任何窗口或标签访问                     |
| 用途     | 存储需要在当前会话或页面重新加载后仍然存在的数据 | 存储只需在当前会话或页面重新加载期间可用的数据 | 存储每个请求都需要发送到服务器的少量数据 | 存储用于离线使用或减轻服务器负载的大量结构化数据 |

localStorage和sessionStorage适合存储少量数据，cookie适合用于身份验证和跟踪用户行为，而IndexedDB适合存储大量数据和复杂的数据类型。根据不同的使用场景，选择不同的存储方法。

1. LocalStorage：它允许您在浏览器的本地存储中存储键值对，即使用户关闭浏览器，数据也会持久存在。该数据可由同源下的任何窗口或标签访问。
2. SessionStorage：它允许您在浏览器的会话存储中存储键值对，该数据仅在当前会话或页面重新加载期间可用。该数据仅可由创建它的窗口或标签访问。
3. Cookie：它允许您在浏览器中存储少量数据，该数据将随每个请求发送到服务器。Cookie可用于本地或远程存储，并可由同源下的任何窗口或标签访问。
4. IndexedDB：它是一种先进的存储机制，允许您在浏览器中存储结构化数据以供离线使用或减轻服务器负载。它没有固定的大小限制，并可由同源下的任何窗口或标签访问。

# Cookie Security Pitfalls

## CSRF

CSRF跨站点请求伪造(Cross—Site Request Forgery)。当目标网站目标用户浏览器渲染HTML文档的过程中，出现了不被预期的脚本指令并执行时，XSS就发生了。

![image-20230416113738701](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416113738701.png)

![image-20230416161024263](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416161024263.png)

![image-20230416161052635](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416161052635.png)

![image-20230416160949575](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416160949575.png)

![image-20230416161128026](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416161128026.png)

![image-20230416161143765](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416161143765.png)

### csrf攻击的根本原因

是因为web服务器对用户信息的验证不够，例子中的对用户身份的验证只是验证了当前用户的session是否存在，无法保证某次请求是这个用户触发的。

### 防御

1. 尽量使用POST，相对程度上能降低攻击的风险。

2. 加入验证码。能够确保是用户行为。

3. 验证referer: referer能记录当前请求的来源地址。但是也会被窜改

4. Anti CSRF Token:

   黑客可以拿到用户的信息，是因为用户的信息放在了cookie中，容易被人获取。

   我们可以在form表单，或http请求头中传递token，token存在服务端，服务端通过拦截器验证有效性，校验失败的拒绝请求。

   token一般放在head区域使用js去调取或者表单里面。

   服务端生成token后会把token放在session 或者 reddis 缓存中，前端在post请求的时候会把，token一并发送给服务端，服务端进行相关验证。验证后销毁。

   ![image-20230416115312399](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416115312399.png)

   ![image-20230416115504020](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416115504020.png)

5. 加入自定义Header

   逻辑和第四点相同，区别在于第四种有可能是通过form表单传输的，但是第五点一定是通过header里面传输的。

## Cross-site scripting（XSS）

当目标网站目标用户浏览器渲染HTML文档的过程中，出现了不被预期的脚本指令并执行时，XSS就发生了。攻击者通过插入的脚本获取用户的信息。

![image-20230416120340599](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416120340599.png)

危害：

1. 挂马
2. 盗取用户的cookie
3. DDOS(拒绝服务)客户端浏览器
4. 钓鱼攻击，高级的钓鱼技巧
5. 删除目标、呃恶意篡改数据、嫁祸
6. 劫持用户Web行为，甚至进一步渗透内网
7. 爆发web2.0 蠕虫
8. 蠕虫式的DDOS攻击
9. 蠕虫式挂马攻击、刷广告、刷流量、破坏网上数据。

XSS的种类

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154050516.png" alt="image-20230416154050516" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154150714.png" alt="image-20230416154150714" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154211353.png" alt="image-20230416154211353" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154225212.png" alt="image-20230416154225212" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154432168.png" alt="image-20230416154432168" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154439889.png" alt="image-20230416154439889" style="zoom: 50%;" />

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/webstorage/image-20230416154518033.png" alt="image-20230416154518033" style="zoom:33%;" />

### 根本原因

我们对url的参数或者是用户提交输入的地方没有做一个充分的过滤，有一些不合法的参数，或者输入的内容，传输到web服务器。用户在访问页面的时候，浏览器会执行相关的代码。

### 防御

1. 对输入(和URL参数)进行过滤，对输出进行编码。Cookie设置http-only等。

2. 输入处理

   包括用户输入、URL参数、POST请求、Ajax

   黑名单过滤：列出不能出现的脚本清单，一旦遇到惊醒处理（富文本）/白名单过滤（用户名，密码等）：列出我们可以接受的内容，比如用户名，规定大小6-14位，只能字母数字下划线，其他都是非法的。

3. 输出处理

   对潜在的不安全的字符串做一个编码和转译。根据上下文进行转移。比如(html entity) `<` 转译为 `&lt;`

4. Cookie 设置为 http-only

Ref:

1. https://www.youtube.com/watch?v=gEPii2y3ISQ
2. https://www.youtube.com/watch?v=QJzkifQ-Cuk
3. [Sanitize untrusted HTML (to prevent XSS) with a configuration specified by a Whitelist.](https://www.npmjs.com/package/xss)
4. https://www.rfc-editor.org/
5. [[XSS 1] 從攻擊自己網站學 XSS (Cross-Site Scripting)](https://medium.com/hannah-lin/%E5%BE%9E%E6%94%BB%E6%93%8A%E8%87%AA%E5%B7%B1%E7%B6%B2%E7%AB%99%E5%AD%B8-xss-cross-site-scripting-%E5%8E%9F%E7%90%86%E7%AF%87-fec3d1864e42)
6. https://www.freecodecamp.org/chinese/news/what-is-cross-site-request-forgery/
7. https://tech.meituan.com/2018/10/11/fe-security-csrf.html
8. https://www.freecodecamp.org/chinese/news/everything-you-need-to-know-about-cookies-for-web-development/

# JWT vs Cookie

## JWT

> JWT 是一种 Token，它的全名是 JSON Web Token。它由服务端产生后，交付给客户端使用，Token 中会夹带取多资讯，包含用户的验证资料或其他。

JWT 的表现形式是一个纯粹的字串，这个字串有三个部分，分别为 Header、Payload、Signature，这三个部分会串接起来，用 . 来分隔，形成这样的格式：`{Header}.{Payload}.{Signature}`，实际范例如下：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.B3GHLnjMFsZJc3K97UIWN68E8WovKxO0Qp6Ye4sVLzo
```

其中Header和payload使用 Base64 进行编码，Signature则是对Header、payload和一个密钥(HS256)进行加密得到的。

## jwt的验证流程

JWT 的验证原理是基于数字签名的验证。当客户端收到一个 JWT 后，需要先对其进行解码，然后使用相同的密钥对 JWT 中的签名进行验证，确保 JWT 的真实性和完整性。验证过程如下：

1. Client登入，Server认证成功之后送一组JWT到Client。
2. Client储存JWT在local，通常是放在localstorage。
3. 当使用者想要访问受到保护的route或是资源的时候，需要在header的Authorization加入Bearer模式
4. Server的Router将会检查Authorization
5. JWT可夹带使用者讯息，因此减少了访问资料库的动作
6. JWT不会使用到Cookie，因此可以使用任意网域的服务
7. 使用者的状态不再储存到Server，所以是一种无状态验证机制

## 使用方式

WT（JSON Web Token）可以通过多种方式进行传输，以下是一些常见的方式：

1. HTTP 头部（Header）：JWT 可以作为 HTTP 头部中的 Authorization 字段的值进行传输。例如：

```js
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

2. URL 查询参数（Query Parameter）：JWT 可以作为 URL 的查询参数进行传输。（不建议）例如：

```js
http://example.com/path?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

3. 表单数据（Form Data）：JWT 可以作为表单数据的值进行传输。
4. HTTP Cookie：JWT 可以存储在 HTTP Cookie 中进行传输。但是這樣就無法進行跨域

## diff

1. JWT 是一种资料格式；Cookie 是一种储存方式。
2. Cookie 的 value 可以储存任何字串，包含 JWT。
4. 针对身分验证用途，服务端通常不储存产生的 JWT，但使用 Cookie 时，通常会在服务端储存一份 Session 资料。

ref:

1. https://devindeving.blogspot.com/2022/01/jwt-concept-vs-cookie.html
2. https://blog.yyisyou.tw/5d272c64/
3. https://juejin.cn/post/6844904034181070861

# ==函数==

> 函数是一组有组织的、可重用的代码，用于执行单个相关操作。默认情况下，所有函数都返回一个值。

## a. 参数

> 函数参数是指在函数定义时声明的变量，用于接收函数调用时传入的值。函数参数的作用是让函数更加灵活和通用，可以接受不同的输入，并根据输入来执行不同的操作。

### 1. 函数参数类型

- 参数值类型

> 函数的参数是不具有类型限制的

1. 基本数据类型：包括字符串、数字、布尔值和 undefined。
2. 对象类型：包括对象、数组、函数、日期、正则表达式等。
3. null：虽然 null 是一个对象类型，但是在 JavaScript 中被认为是一个独立的基本数据类型。
4. Symbol：这是在 ES6 中引入的一种新的数据类型，它表示唯一的、不可变的值。

需要注意的是，在 JavaScript 中，函数的参数是不具有类型限制的，即使你在定义函数时指定了参数的类型，但实际上仍然可以传入其他类型的值。因此，在使用函数参数时，需要自行处理参数类型的问题，以确保函数的正确性和可靠性。

- 形参，实参

在调用函数时，可以传递实参来给形参赋值。如果函数有多个参数，实参之间用逗号分隔。

### 2. 传值 vs 传引用

1. 传值（by value）：将原始数据类型（例如字符串、数字、布尔值等）作为参数传递给函数时，函数会创建一个新的变量来存储传入的值，并将该变量传递给函数。在函数内部对该变量的修改不会影响到原始变量的值。
2. 传引用（by reference）：将对象类型（例如数组、对象、函数等）作为参数传递给函数时，实际上传递的是该对象在内存中的引用地址，函数参数和原始参数引用的是同一个对象，因此在函数内部对该对象的修改会影响到原始对象的值。

```JavaScript
function changeProperty(obj) {
  obj.prop = 'new value';
}

let myObj = { prop: 'old value' };
console.log(myObj.prop); // 输出 old value
changeProperty(myObj);
console.log(myObj.prop); // 输出 new value
```

### 3. 函数参数的默认值

> 函数参数的默认值是指在函数定义时，为参数指定一个默认值，这样在函数调用时如果没有传入该参数，就会使用该默认值。

#### a. 如何设置默认值

（解构设置默认值）

1. “默认值赋值”（default value assignment）

```JavaScript
function myFunc(param1 = defaultValue1, param2 = defaultValue2) {
  // 函数体
}
```

2. 使用解构赋值和默认值赋值

```js
function greet({ name = 'World', greeting = 'Hello' } = {}) {
  console.log(`${greeting}, ${name}!`);
}
```

#### b. 默认值和 undefined 的区别

如果使用默认值的参数在函数调用时传递了一个 undefined 值，则该参数将使用默认值而不是 undefined 值。这是默认值和 undefined 的区别。传入undefined可以作为一个占位使用，如果某个参数不需要传的时候，可以传递undefined。

```JavaScript
function myFunc(param1 = 'default value') {
  console.log(param1);
}

myFunc(); // 输出 'default value'
myFunc(undefined); // 输出 'default value'
myFunc(null); // 输出 null
myFunc('other value'); // 输出 'other value'
```

### 4. 可变参数(不定参数)

不定参数（也称为可变参数）指在函数定义时不确定参数数量，使用 rest 参数将所有参数收集为一个数组。在函数体内使用该数组进行处理。

需要注意的是，不定参数必须是函数的最后一个参数。如果将其放在函数定义中的其他参数之前，那么在调用函数时，这些参数将被视为 undefined。因此，rest 参数应该始终放在函数定义中的最后一个参数位置。

```JavaScript
function myFunc(...args) {
  console.log(args);
}

myFunc(); // 输出 []
myFunc(1, 2, 3); // 输出 [1, 2, 3]
myFunc('a', 'b', 'c'); // 输出 ['a', 'b', 'c']
```

#### rest 参数

rest 参数是指在函数定义中使用三个点 `...` 语法来表示可以接收任意数量的参数，并将这些参数存储在一个数组中。rest 参数必须作为最后一个参数出现，因为它会将函数中剩余的参数收集到一个数组中。

```JavaScript
function myFunc(a, b, ...rest) {
  console.log(a, b, rest);
}

myFunc(1, 2, 3, 4, 5); // 输出 1, 2, [3, 4, 5]
```

#### spread 参数

如果希望将数组中的每个元素作为单独的参数进行传递，则可以使用扩展运算符（...）来展开数组

```JavaScript
function myFunc(a, b, c) {
  console.log(a, b, c);
}

const arr = [1, 2, 3];
myFunc(...arr); // 输出 1, 2, 3
```

#### rest 和 argument 的区别

1. rest 参数是一个真正的数组，而 arguments 对象只是一个类数组对象。
2. rest 参数只包含传递给函数的实际参数，而 arguments 对象包含所有传递给函数的参数，包括函数定义时声明的参数和调用时传递的参数。
3. rest 参数可以使用 ES6 的数组方法进行处理，例如 forEach、map、filter 等，而 arguments 对象不支持这些数组方法，需要先将其转换为数组才能使用。

```JavaScript
function myFunc(...rest) {
  console.log(rest);
  console.log(arguments);
}

myFunc(1, 2, 3, 4); // 输出 [1, 2, 3, 4] 和 { '0': 1, '1': 2, '2': 3, '3': 4 }
```

### 5. 函数参数的解构

函数参数的解构是指在函数定义时使用对象解构或数组解构来获取函数参数中的某些值。通过解构，可以将需要的值从对象或数组中提取出来，使代码更加简洁易懂。

#### 使用对象解构

在函数定义时，可以使用对象解构来获取函数参数中的某些值

```JavaScript
function myFunc({ name, age }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person = { name: 'Alice', age: 20 };
myFunc(person); // 输出 "My name is Alice, and I'm 20 years old."
```

在上面的例子中，函数 myFunc 接收一个对象作为参数，并使用对象解构来获取 name 和 age 属性的值。在调用函数时，传递了一个包含 name 和 age 属性的对象作为参数。

#### 如何使用数组解构

在函数定义时，也可以使用数组解构来获取函数参数中的某些值，例如：

```JavaScript
function myFunc([first, second]) {
  console.log(`The first item is ${first}, and the second item is ${second}.`);
}

const arr = ['apple', 'orange', 'banana'];
myFunc(arr); // 输出 "The first item is apple, and the second item is orange."
```

在上面的例子中，函数 myFunc 接收一个数组作为参数，并使用数组解构来获取第一个和第二个元素的值。在调用函数时，传递了一个包含多个元素的数组作为参数。

#### 如何在函数参数中使用解构

除了在函数定义时使用解构来获取参数值之外，在函数调用时也可以使用解构来传递参数值，例如：

```JavaScript
function myFunc({ name, age }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person = { name: 'Bob', age: 30 };
myFunc(person); // 输出 "My name is Bob, and I'm 30 years old."

// 使用解构来传递参数值
myFunc({ name: 'Alice', age: 20 }); // 输出 "My name is Alice, and I'm 20 years old."
```

在上面的例子中，在第一次调用函数时，传递了一个包含 name 和 age 属性的对象作为参数。在第二次调用函数时，使用对象解构和对象字面量的方式传递参数值。

需要注意的是，在使用解构时，如果参数对象中不存在解构所需的属性，那么对应的变量将被赋值为 undefined。如果需要给变量设置默认值，可以使用解构赋值的方式，例如：

```JavaScript
function myFunc({ name = 'unknown', age = 0 }) {
  console.log(`My name is ${name}, and I'm ${age} years old.`);
}

const person1 = { name: 'Bob' };
myFunc(person1); // 输出 "My name is Bob, and I'm 0 years old."

const person2 = { age: 30 };
myFunc(person2); // 输出 "My name is unknown, and I'm 30 years old."
```

### 6. 箭头函数的参数

- 在箭头函数中，如果只有一个参数，可以省略参数括号；如果有多个参数，则需要使用括号
- 如果参数需要默认值，则可以使用 ES6 中的默认参数语法。
- 箭头函数的参数没有自己的 arguments 对象。如果需要访问函数的参数，可以使用 rest 参数语法。

```JavaScript
 const func = (...args) => {
  console.log(args);
}

func(1, 2, 3); // 输出 [1, 2, 3]
```

### 7. 参数顺序

- 参数的顺序可能会影响函数的行为

- 如果函数参数有固定的顺序，但是中间的参数不想传递，可以通过在需要跳过的参数位置上使用 undefined 来实现。

- 如果不传递任何值或者传递 null 等 falsy 值时，函数会将该参数解释为缺失参数，而不是跳过该参数。因此，为了明确地跳过某个中间参数，需要显式地将其设置为 undefined。

可以考虑使用对象参数的方式，将参数封装为一个对象，这样你就可以只传递需要的参数，而不需要按照固定顺序传递所有参数。

```JavaScript
function greet({ message = "Hello", name = "World", age = null } = {}) {
  console.log(message + " " + name);
  if (age) {
    console.log("You are " + age + " years old.");
  }
}
// 使用 "= {}" 的默认参数值是为了确保当没有传入参数时，options 参数被解构时不会出现 undefined 错误。
greet(); // 输出 "Hello World"
greet({ name: "Tom" }); // 输出 "Hello Tom"
greet({ message: "Hi", name: "Alice" }); // 输出 "Hi Alice"
greet({ name: "Bob", age: 20 }); // 输出 "Hello Bob" 和 "You are 20 years old."
```

### 8. 通过参数创建函数（柯里化）

> 在 JavaScript 中，可以使用柯里化（currying）技术来通过参数创建函数。柯里化是一种将函数转换为接受一系列参数的函数序列的技术，每个序列中的函数只接受单个参数。

> 更通俗的讲法是，柯里化是将多元函数简化为一元函数

```JavaScript
function add(a, b) {
  return a + b;
}

function curryAdd(a) {
  return function(b) {
    return a + b;
  };
}

const add1 = curryAdd(1);
console.log(add1(2)); // 输出 3
console.log(add1(3)); // 输出 4
```

在 React 中，柯里化可以应用于很多场景，以下是几个常见的使用场景：

1. 高阶组件（Higher-Order Component，HOC）：HOC 是一个函数，它接受一个组件作为参数，并返回一个增强后的组件。HOC 可以用来实现一些横切关注点（cross-cutting concerns），例如日志、权限控制等。柯里化可以帮助我们将 HOC 的参数和返回值分别作为柯里化函数的前后两个参数，这样可以使 HOC 更加清晰和易于组合。
2. 函数式组件：函数式组件是一个只接受 props 参数并返回 React 元素的函数。柯里化可以用来将函数式组件转换为接受其他参数的函数，例如接受样式和事件处理函数等参数。这样可以使函数式组件更具通用性和可复用性。
3. 钩子函数（Hooks）：钩子函数是 React 16.8 引入的一种新的组件状态管理方式，它允许我们在函数式组件中使用状态和其他 React 特性。柯里化可以用来将钩子函数的参数分解为多个参数，这样可以使钩子函数更加清晰和易于测试。
4. 命名参数：React 组件的 props 是一个包含多个属性的对象，柯里化可以用来将这些属性拆分为多个参数，这样可以使组件的调用更具有可读性和可维护性。

## b. 返回值

JavaScript 函数的返回值是指在函数执行完毕后返回给调用者的值。函数可以返回任何 JavaScript 数据类型，包括数字、字符串、对象、数组和布尔值等。

函数的返回值通常通过 `return` 语句指定。如果函数没有指定 `return` 语句，则默认返回 `undefined` 值。

`return` 语句会立即结束函数的执行，并返回指定的值，因此函数中 `return` 语句后面的代码不会被执行。

```JavaScript
// 函数也可以返回一个对象或数组等复杂数据类型
function getPerson() {
  return {
    name: 'John',
    age: 30,
    gender: 'male'
  };
}

var person = getPerson(); 
```

## c. 闭包

> 闭包是指在一个函数内部定义的函数，它可以访问到该函数的私有变量以及在该函数作用域之外定义的变量。
>
> 闭包（Closure）是指函数和函数内部能访问到的变量（即自由变量）的组合。在JavaScript中，函数嵌套函数的情况非常常见，如果内部函数能够访问外部函数的变量，即使外部函数执行完毕，内部函数依然能够访问到这些变量，这种情况就称为闭包。

```JavaScript
function outer() {
  var count = 0;
  function inner() {
    count++;
    console.log(count);
  }
  return inner;
}

var increment = outer();
increment(); // 输出1
increment(); // 输出2
increment(); // 输出3
```

闭包只能取得包含函数中任何变量最后一个值，保存的是整个变量对象，不是某个特殊变量。

```JavaScript
// 只会返回10，即使是遍历函数，最终结果是10，不会返回各自不同的索引值
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(){
      return i;
    };
  }
  return result; 
} 

//强制返回各自不同的索引值
function createFunctions(){
  var result = new Array();
  for (var i=0; i < 10; i++){
    result[i] = function(num){
      return function(){
        return num;
      };
    }(i);
  }
  return result;
}
```

闭包常见的应用包括：

1. 模块化开发：通过闭包来实现类似于私有变量的效果，防止变量被外部访问和修改。
2. 防抖和节流：通过闭包来实现防抖和节流等函数式编程的方法，提高程序的性能。
3. 实现回调函数：通过闭包来实现回调函数，可以让函数在异步执行时能够访问到原始的数据和环境。

在使用闭包时，需要注意以下几点：

1. 内存泄漏：由于闭包会保留外部函数的变量引用，如果不正确地使用闭包，可能会导致内存泄漏。因此，当闭包不再使用时，应该及时释放相关资源。

2. 变量共享：由于闭包可以访问外部函数的变量，因此多个闭包可能会共享同一个变量，这可能会导致不可预期的结果。为了避免这种情况，应该尽量避免使用全局变量，并在使用闭包时注意变量的作用域。闭包导致函数依赖函数外的状态，可能导致函数变得不够纯

   ```js
   function createMultiplier(factor) {
     return function(num) {
       return num * factor;
     }
   }
   
   const double = createMultiplier(2);
   console.log(double(3)); // 输出 6
   
   const triple = createMultiplier(3);
   console.log(triple(3)); // 输出 9
   
   const quadruple = createMultiplier(4);
   console.log(quadruple(3)); // 输出 12
   
   factor = 5;
   console.log(double(3)); // 输出 6，而不是 15
   
   ```

   `createMultiplier` 函数返回了一个闭包 `multiplier`，这个闭包可以访问外部的变量 `factor`。在执行 `double(3)` 的时候，`factor` 变量被设置为 2，并且返回 6。当执行 `triple(3)` 的时候，`factor` 变量被设置为 3，并且返回 9。

   但是，如果在执行 `factor = 5` 之后再次调用 `double(3)`，返回的值仍然是 6，而不是 15。这是因为 `multiplier` 函数依赖于外部变量 `factor` 的状态，而不是函数的输入参数。因此，当外部变量 `factor` 被修改时，会影响到函数 `multiplier` 的行为，导致函数的不纯。这种不纯的行为可能会导致代码难以理解、维护和调试。

3. 性能问题：由于闭包会保留外部函数的变量引用，因此它的创建和销毁过程比普通函数要复杂。如果在循环中频繁使用闭包，可能会导致性能问题。为了避免这种情况，应该尽量避免在循环中使用闭包，并在需要使用时，尽量使用函数式编程的方法，如防抖、节流等。

4. 变量命名冲突：由于闭包可以访问外部函数的变量，因此在使用闭包时，应该避免变量命名冲突。为了避免这种情况，可以使用模块化编程的方法，将变量封装在模块内部，避免变量名冲突。

## d. 作用域

#### 作用域的基础知识

##### 什么是作用域？

作用域是指程序中定义变量的可访问范围。在JavaScript中，作用域由执行上下文和作用域链组成。执行上下文是指当前执行代码的环境，而作用域链是指在当前执行上下文中，可以访问的变量的链式结构。

##### 作用域链是什么

它由当前执行上下文的变量对象和其外部环境的变量对象构成。当代码在当前执行上下文中查找变量时，如果在当前的变量对象中找不到变量，就会在外部环境的变量对象中继续查找，直到找到该变量或者查找到全局对象。

##### 全局作用域和局部作用域

全局作用域是指在代码的任何地方都可以访问的变量，它定义在全局对象中。而局部作用域是指在特定的代码块或函数中定义的变量，只能在该代码块或函数内部访问。

在JavaScript中，每个函数都会创建一个新的局部作用域，而全局作用域则是整个程序的顶层作用域。通过合理的使用作用域和作用域链，可以避免变量名冲突，提高程序的可读性和可维护性。

#### 作用域链和执行上下文

##### 执行上下文是什么

执行上下文是 JavaScript 中用于管理代码执行的一种内部数据结构。每当 JavaScript 引擎执行一段代码时，都会创建一个执行上下文来存储该代码的相关信息，如变量、函数声明、作用域链等。执行上下文是 JavaScript 实现作用域和闭包的关键。

执行上下文是最外围的执行环境，宿主不同，表示的执行环境的对象也不一样。web中，global context是windows object,When an execution context has executed all of its code, it is destroyed销毁, taking with it all of the variables and functions defined within it

内部环境可以通过作用域链访问所有的外部环境，但外部环境不能访问内部环境中的任何变量和函数。

当代码在一个环境中执行时候，会创建变量对象的一个作用域链。作用域链的作用，保证对执行环境有权访问的所有变量和函数的有序访问。

##### 创建执行上下文的过程

1. 创建变量对象（Variable Object，VO）：变量对象是执行上下文中的一个重要概念，它用于存储该上下文中定义的变量、函数声明等信息。对于全局执行上下文来说，变量对象就是全局对象（Window），对于函数执行上下文来说，变量对象则包括了函数的参数、函数声明和内部声明的变量。
2. 建立作用域链（Scope Chain）：作用域链是用于解析标识符（变量名、函数名等）的一种机制，它由当前执行上下文的变量对象和所有外层执行上下文的变量对象组成，形成一个链式结构。当代码在当前执行上下文中访问一个变量时，JavaScript引擎会先查找当前执行上下文的变量对象，如果没找到，则在作用域链中查找。
3. 确定this指向：this指向在执行上下文创建时确定，它的值取决于函数调用方式。

##### 执行上下文栈

执行上下文栈（Execution Context Stack）是用于管理执行上下文的一种数据结构，也称为调用栈（Call Stack）。JavaScript引擎在执行代码时，会将每个执行上下文压入执行上下文栈中，当一个执行上下文执行完毕后，它会从执行上下文栈中弹出，控制权回到上一个执行上下文。

##### 作用域链的形成过程

1. 执行上下文在创建时会将当前变量对象添加到作用域链的最前端，这样当前执行上下文就可以访问到自己的变量。
2. 当代码在当前执行上下文中访问一个变量时，JavaScript引擎会先查找当前执行上下文的变量对象，如果没找到，则在作用域链中查找。作用域链的查找方向是由当前执行上下文的作用域链决定的，也就是说作用域链中靠前的变量对象拥有更高的优先级。如果在整个作用域链中都没找到该变量，则认为该变量未定义。

#### 词法作用域和动态作用域

词法作用域（Lexical Scope）和动态作用域（Dynamic Scope）是两种不同的作用域规则，它们决定了变量的可见范围和访问顺序。

词法作用域指的是作用域在代码编写时就已经确定好了，在代码的词法分析阶段就已经确定了，即在代码块中声明的变量的作用域在代码块内部。这种作用域是静态的，也就是说它的作用域范围在代码运行之前就已经确定好了。

动态作用域指的是作用域在程序运行时才能确定，它是根据函数调用栈来确定的，即当前正在执行的函数的作用域。这种作用域是动态的，也就是说它的作用域范围是随着程序运行时变化的。

JavaScript使用词法作用域。在JavaScript中，函数作用域是词法作用域，变量的作用域在函数定义时就已经确定好了，无论在何处调用函数，都会在函数内部找到相应的变量。这种作用域使得代码的行为更加可预测和易于理解。

#### ES6中的作用域

##### 块级作用域

S6中的作用域和之前的JavaScript版本中的作用域是相同的，都是基于词法作用域的。

但是，ES6中引入了块级作用域。在ES6之前，JavaScript中只有全局作用域和函数作用域，而没有块级作用域。块级作用域指的是在代码块内部定义的变量只在该块内部有效，超出该块范围就失效了。

##### const / let / var作用域的区别

ES6引入了两个新的关键字来声明块级作用域的变量：let和const。使用let或const声明的变量只在当前代码块内部有效，不会污染外部的作用域。在同一作用域中可以重复声明同名的let变量，但不可以重复声明同名的const变量。变量提升的部分也会不同。

##### arrow function的作用域

ES6中也引入了箭头函数，箭头函数与普通函数不同，它没有自己的this和arguments，它的this和外层函数的this是相同的。这种特殊的函数作用域也被称为词法作用域。

普通函数也是词法作用域。词法作用域指的是变量的作用域由它在代码中声明的位置所决定，与函数被调用的方式无关。在 JavaScript 中，函数的作用域是在函数声明时确定的，而不是在函数调用时确定的。因此，在函数内部声明的变量只能在函数内部访问，除非通过函数的返回值将变量传递到函数外部。

箭头函数的特殊之处在于它的 this 值是词法上绑定的，也就是说，箭头函数的 this 值由外层作用域中的 this 值决定，而不是由函数被调用时的上下文决定。

##### 模板字面量中的作用域

模板字面量（Template literals）是 ES6 引入的一种字符串表达方式，可以使用反引号 `` 包裹字符串，并且支持在字符串中使用变量、表达式等语法。

在模板字面量中，变量和表达式可以通过 `${}` 语法嵌入到字符串中。这些变量和表达式的作用域和普通的 JavaScript 变量和表达式的作用域一样，都是在当前的代码块中。

举个例子：

```JavaScript
let name = "Tom";
console.log(`Hello, ${name}!`);
```

在这个例子中，模板字面量的作用域就是当前的代码块，也就是全局作用域。因为 `name` 变量是在全局作用域中定义的，所以在模板字面量中可以直接使用。

如果在模板字面量中使用的变量或表达式是在某个函数中定义的，那么它们的作用域就是这个函数的作用域。例如：

```JavaScript
function sayHello(name) {
  console.log(`Hello, ${name}!`);
}

sayHello("Tom");
```

在这个例子中，模板字面量 `${name}` 中的 `name` 变量就是在 `sayHello` 函数中定义的，因此它的作用域就是 `sayHello` 函数的作用域。

## e. 递归与尾递归

### 递归

> 递归是指一个函数在其定义中调用自身的过程。

#### 递归的基本原理

基本原理是将问题分解为更小的子问题，直到问题变得足够小，可以通过简单的方式来解决。这样做可以使代码更简洁，易于理解。

- 递归必须包含一个基本情况，这个基本情况通常是指递归到一定程度时不再需要递归。
- 递归算法通常包含两个部分：基本情况和递归情况。

```JavaScript
   // 阶乘
   // n! = n * (n-1) * (n-2) * ... * 2 * 1
   function factorial(n) {
     if (n === 0) {   // base case
       return 1;
     } else {
       return n * factorial(n - 1);   // recursive case
     }
   }
   
   factorial(5);   // returns 120
```

在上面的例子中，函数 `factorial` 是递归函数。当传入值为0时，函数将返回1，这是递归的基本结束条件，也称为“基本情况”（base case）。

否则，它将通过调用自己来计算 `(n-1)` 的阶乘，并将结果乘以`n`。 这是递归的“递归情况”（recursive case）。

```JavaScript
   // 斐波那契数列
   function fibonacci(n) {
     if (n < 2) { // base case
       return n;
     } else {
       return fibonacci(n-1) + fibonacci(n-2); // recursive case
     }
   }
   
   console.log(fibonacci(6)); // Output: 8
```

#### 实现递归算法的方法

   -  递归函数的定义和调用。
   - 使用条件判断语句来判断递归结束的条件。
   - 确定递归函数的参数和返回值类型。
   - 使用递归函数来处理递归情况。

#### 递归的优缺点

   - 优点：递归能够简化问题的处理，使代码更加简洁、易读。
   - 缺点：递归调用会产生额外的函数调用开销，可能导致栈溢出等问题。

#### 递归应用场景

   - 树形结构的操作：树形结构是递归的典型例子。许多操作，如遍历、搜索、插入和删除等，都可以使用递归来实现。
   - 排列组合问题：对于一些排列组合的问题，例如汉诺塔问题、n皇后问题等，递归是一种有效的求解方法。
   - 分治算法：分治算法也是递归的一种应用。在分治算法中，原问题被划分为若干个规模较小的子问题，然后递归地解决每个子问题，并将解合并成原问题的解。
   - 动态规划：动态规划问题通常可以通过递归算法来解决。在动态规划中，问题通常被分解为若干个子问题，然后递归地解决每个子问题，并将解合并成原问题的解。
   - 数学计算：递归在数学计算中也有广泛的应用。例如，计算阶乘、斐波那契数列等都可以使用递归来实现。

#### 如何避免递归问题

   - 尝试使用循环来代替递归。某些递归问题可以通过循环解决，因为循环不涉及函数调用和栈操作，所以通常比递归更高效并且不会产生栈溢出的风险。
   - 对于必须使用递归的问题，可以考虑使用尾递归。尾递归是指递归函数的最后一步是调用自身，这样就可以避免在调用子函数之前积累大量的栈帧。许多编程语言都支持尾递归优化，包括Scheme和Erlang等函数式编程语言。
   - 增加栈空间的大小。如果无法避免使用递归，并且递归深度较大，则可以通过增加栈空间的大小来避免栈溢出。许多编程语言都支持向递归函数传递额外参数以控制栈大小，例如Python的sys.setrecursionlimit()函数可以设置递归深度的上限。
   - 优化递归算法。有些递归算法可以进行优化，例如记忆化搜索、分治等技巧，以减少递归深度和计算量。

#### 递归的注意事项

   - 递归的边界条件：递归必须有一个边界条件，当满足该条件时，递归终止。如果没有边界条件或者边界条件不正确，递归将会无限进行，导致栈溢出。
   - 递归的递推公式：递归必须有一个递推公式，该公式描述了如何将一个问题分解成子问题。如果递推公式不正确，递归可能会产生无限循环或者结果不正确。
   - 递归的性能问题：递归可能导致栈溢出或者效率低下。因此，在使用递归时，应该考虑使用尾递归或迭代实现，避免过多的栈空间消耗和函数调用开销。
   - 递归的调试问题：递归代码通常比较难以调试，因为它会产生多层嵌套的函数调用。可以使用打印或者调试工具等方式，对递归进行调试。
   - 递归的可读性问题：递归可能导致代码变得比较复杂，因为它涉及到多层嵌套的函数调用。可以通过给函数命名、添加注释、使用尾递归等方式，提高代码的可读性。

### 尾递归

尾递归是指在函数的最后一步中调用自身，并且返回值是该函数的返回值。尾递归可以被优化为迭代，从而减少函数调用时的内存消耗和栈溢出的风险。在 JavaScript 中，尾递归可以使用 ES6 的严格模式（strict mode）来实现。

#### 1. 什么是尾递归？

##### a. 尾递归的定义及其特点

尾递归是指一个函数在执行的最后一步调用自身，并且该调用的返回值直接被当前函数所返回。也就是说，函数调用发生在当前函数的尾部（最后一行代码），因此称为尾递归。尾递归和普通的递归不同，普通递归会在递归调用结束之后还需要进行一些操作，而尾递归的递归调用是整个函数的最后一步，不存在后续操作。

尾递归的特点是可以被优化为迭代循环，从而减少函数调用时的内存消耗和栈溢出的风险，因为在优化后，尾递归的调用会被替换为循环，从而避免了不必要的函数调用栈的生成。

1. 最后一步是对自身的调用：尾递归函数在执行的最后一步中调用自身，并且没有其他操作。
2. 函数调用不会增加栈的大小：尾递归的调用会被优化为迭代，从而减少函数调用时的内存消耗和栈溢出的风险。
3. 返回值是递归调用的返回值：尾递归函数的返回值是最后一次递归调用的返回值，不需要对递归调用的返回值进行其他操作。

（牺牲时间换空间，牺牲空间换时间）

```JavaScript
// 这个函数在执行时会产生多次递归调用，每次调用都会在栈中占用一定的内存空间。由于递归的缺陷，当 n 很大的时候，函数的性能会急剧下降，甚至可能导致栈溢出。
function fibonacci(n) {
  if (n <= 1) {
    return n;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

// tail recursion
function fibonacci(n, a = 0, b = 1) {
  if (n === 0) return a;
  if (n === 1) return b;
  return fibonacci(n - 1, b, a + b);
}

function fibonacci(n, a = 1, b = 1) {
  if (n <= 1) {
    return b;
  } else {
    return fibonacci(n - 1, b, a + b);
  }
}

// 这个函数使用了尾递归的方式来计算斐波那契数列。由于尾递归的特点是函数调用时不需要额外的栈空间，因此可以避免栈溢出的问题，并且在性能上比递归更优秀。在这个函数中，我们使用了两个参数 a 和 b 来保存当前的斐波那契数列的值，然后在下一次函数调用时将它们更新为下一个斐波那契数列的值。
```

1. 如果 n 的值小于等于 1，函数直接返回 b 的值，因为斐波那契数列的第一项和第二项都为 1。
2. 如果 n 的值大于 1，则调用 fibonacci 函数，并将参数 n-1、b 和 a+b 传入函数中。此时，函数的最后一步操作为调用自身，并且返回值为函数的返回值，因此可以使用尾递归进行优化。
3. 在递归调用中，a 和 b 的值分别为斐波那契数列中当前项的前两项，a + b 的值为当前项，因此可以保证每次调用时，都是在计算下一个斐波那契数。
4. 当递归调用结束后，函数返回最后一项的值。

##### b. 尾递归的优势和劣势

#### 2. 尾递归与递归的区别

##### 递归的定义及其特点

递归是指一个函数调用自身的过程。在递归中，函数会将一个问题拆分为更小的子问题，直到达到某个结束条件，然后逐层返回结果。递归函数一般有两个重要的组成部分：基本情况和递归情况。基本情况指的是递归结束的条件，递归情况指的是函数调用自身来解决更小的子问题。

递归的特点包括：

- 简洁：使用递归可以简化一些算法和代码实现，使得代码更加易读和易懂。
- 灵活：递归可以解决很多问题，特别是在处理树形结构、链表等数据结构时，递归的效果尤为明显。
- 可读性强：递归能够清晰地表达问题的解法，提高代码可读性。

##### 递归和尾递归的区别和联系

递归和尾递归都是函数调用自身的过程，但是它们在实现方式和效率上有所不同。

1. 区别：

（1）递归是指一个函数在执行过程中调用了自身，但不是所有的递归都是尾递归。在普通递归中，函数的最后一步操作是调用自身之外的操作，会在调用栈中堆积多层调用，占用大量内存。而在尾递归中，函数的最后一步操作是调用自身，相当于循环，每次调用都会覆盖上一次调用的栈帧，不会堆积多层调用。

（2）尾递归的特点是在函数返回时调用自身，且返回值为函数的返回值，这样可以避免在调用栈中堆积多层调用，减少内存消耗和运行时间。

1. 联系：

（1）尾递归是一种特殊的递归，它们都是函数自身调用自身，具有相同的语法形式。

（2）尾递归可以转化为循环来实现，而循环也可以转化为尾递归来实现。

（3）递归和尾递归都可以实现相同的功能

#### 3. 尾递归的实现方式

##### a. 使用 ES6 的严格模式实现尾递归

要使用 ES6 的严格模式实现尾递归，需要确保函数满足以下几个条件：

1. 函数必须是一个纯函数，即不依赖外部变量或状态，只接受参数并返回结果。
2. 函数的最后一步操作必须是对自身的调用，并将其结果作为返回值，确保没有其他操作会修改返回结果。
3. 在调用自身前，所有的变量都已经被计算出来，不再需要再次访问它们。这可以通过将所有变量都作为参数传递给函数来实现。

```JavaScript
// 阶乘函数的尾递归
'use strict';

function factorial(n, acc = 1) {
  if (n <= 1) return acc;
  return factorial(n - 1, n * acc);
}

console.log(factorial(5)); // 输出 120
```

在这个示例中，函数 `factorial` 接收两个参数。第一个参数 `n` 表示要计算阶乘的数，第二个参数 `acc` 表示当前已经计算出的阶乘结果。如果 `n` 小于等于 1，那么函数直接返回当前的阶乘结果；否则，它会继续调用自身，将 `n-1` 和 `n*acc` 作为新的参数传递进去。

这个函数利用了 ES6 中的默认参数语法，将 `acc` 参数设置为初始值 1。这样，在第一次调用时，不需要额外传递任何参数。因此，这个函数可以像普通的函数一样调用，而不需要使用特殊的方式来处理尾递归。

通过这种方式，我们可以避免创建不必要的调用帧，从而避免堆栈溢出。

##### b. 尾递归的转化为迭代的实现方式

尾递归函数可以通过迭代的方式来实现，这样可以避免由于递归调用而导致的栈溢出问题。

```JavaScript
function factorial(n) {
  let acc = 1;
  for (let i = n; i > 0; i--) {
    acc *= i;
  }
  return acc;
}

console.log(factorial(5)); // 120
```

在这个示例中，我们使用 `for` 循环来迭代求解阶乘。在每次循环中，我们将 `i` 的值乘以累积值 `acc`，然后将结果存储回 `acc` 中。当循环结束后，我们返回结果。

需要注意的是，通过迭代实现尾递归可以避免函数调用栈溢出的问题，因为我们不再创建新的函数执行上下文。此外，迭代通常比递归更快，因为它们避免了创建和销毁大量的函数执行上下文。

#### 4. 尾递归优化的方法和技巧

1. 循环/迭代函数代替递归

将递归调用转换为循环，这样可以避免调用栈溢出的问题。具体实现方式是使用一个循环来模拟递归调用的过程，并在每次循环迭代中更新参数，直到满足退出条件。

1. 使用尾递归消除器

尾递归消除器是一个工具，可以自动将尾递归函数转换为等效的非递归形式，从而避免调用栈溢出的问题。该工具可以根据语言规范中的尾递归优化规则进行转换，同时还可以进行一些额外的代码优化操作。

1. 使用尾递归优化编译器

一些编程语言的编译器已经内置了尾递归优化功能，例如Erlang、Scheme等函数式编程语言。这些编译器能够自动将尾递归函数转换为迭代形式，从而避免调用栈溢出的问题。如果使用这些语言编写代码，可以直接调用编译器进行尾递归优化，不需要手动处理代码。

#### 5. 尾递归的应用场景

1. 数字运算等

a) 数学计算

对于一些数学计算问题，通常可以使用递归算法进行求解。例如，计算斐波那契数列、阶乘等问题都可以使用递归算法。由于这些问题的输入规模较大，可能会导致递归调用的深度也很大，此时可以使用尾递归优化来避免栈溢出的问题。

b) 数据结构处理

一些数据结构的操作也可以使用递归算法进行实现，例如二叉树的遍历、图的遍历等。由于这些数据结构的深度也很大，可能会导致递归调用的深度也很大，此时可以使用尾递归优化来提高代码性能和可靠性。

c) 状态机

状态机是一种常用的计算模型，用于描述系统在不同状态之间的转换关系。状态机的实现通常利用递归算法来解析输入流，但是如果递归深度太大，也会出现栈溢出的问题。此时可以使用尾递归优化来消除栈空间的使用。

尾递归在一些递归深度比较大的问题中具有重要的应用价值，可以提高代码的性能和可靠性。

1. 在函数式编程中的应用

- 高阶函数

在函数式编程中，高阶函数是一个非常重要的概念，它可以将函数作为参数或返回值来实现更加灵活的编程。高阶函数通常采用递归算法实现，如果递归深度比较大，就需要使用尾递归优化来避免栈溢出的问题。

- 函数组合

函数组合是函数式编程中另一个重要的概念，它可以将多个函数组合成一个新的函数来实现复杂的计算功能。函数组合通常也采用递归算法实现，因此也需要使用尾递归优化来提高代码性能和可靠性。

- 模式匹配

模式匹配是函数式编程中一种特殊的语法结构，用于匹配不同的数据类型并执行相应的操作。模式匹配通常也采用递归算法实现，因此也需要使用尾递归优化来避免栈溢出的问题。

- 列表处理

在函数式编程中，列表是一种非常常见的数据结构，经常用于存储和处理数据。列表的操作通常也采用递归算法实现，因此也需要使用尾递归优化来提高代码性能和可靠性。

#### 6. JavaScript 中的尾递归库和工具

- trampoline 和 thunk 函数
- Lodash 和 Ramda 等 JavaScript 库中的尾递归实现方式

## f. 普通函数、匿名函数、类函数、箭头函数

普通函数是指使用 `function` 关键字定义的一种函数。它可以接受参数，并且可以有返回值，可以在任何地方被调用。示例：

```JavaScript
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 输出 5
```

匿名函数是指没有函数名的函数，它通常是作为其他函数的参数传递，或者是赋值给一个变量。示例：

```JavaScript
const add = function(a, b) {
  return a + b;
};

console.log(add(2, 3)); // 输出 5
```

类函数是 ES6 引入的一种函数，它通过 `class` 关键字定义。类函数有一个构造函数和一些方法，可以用来创建对象。示例：

```JavaScript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHi() {
    console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

const john = new Person('John', 30);
john.sayHi(); // 输出 "Hi, my name is John and I'm 30 years old."
```

箭头函数是 ES6 引入的一种函数，它使用 `=>` 符号定义。箭头函数是匿名函数的一种特殊形式，它可以使用简洁的语法来定义函数，并且不需要使用 `function` 关键字。箭头函数没有自己的 `this`，它会使用定义时的 `this`。示例：

```JavaScript
const add = (a, b) => a + b;
console.log(add(2, 3)); // 输出 5

const person = {
  name: 'John',
  age: 30,
  sayHi: () => {
    console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old.`);
  }
};

person.sayHi(); // 输出 "Hi, my name is undefined and I'm undefined years old."
```

总结：

- 普通函数、匿名函数和类函数是三种常见的函数定义方式，用于实现不同的功能。
- 箭头函数是一种匿名函数的特殊形式，它使用简洁的语法定义函数，并且没有自己的 `this`。

## g. this指向

`this` 关键字是函数运行时自动生成的一个内部对象，只能在函数内部使用，总指向调用它的对象。

JavaScript中的`this`关键字指的是当前执行上下文的上下文对象。它的指向是在函数被调用时动态绑定的，具体取决于函数的调用方式和上下文。以下是关于`this`指向的知识内容框架：

### `this`的指向方式

- 默认绑定：在函数中直接调用，指向全局对象（在浏览器中为`window`对象，在Node.js中为`global`对象）。
- 隐式绑定：函数作为对象的方法调用时，`this`指向调用该方法的对象。
- 显式绑定：通过`call`、`apply`或`bind`方法指定函数执行时的上下文。
- new绑定：当一个函数被使用`new`关键字调用时，`this`指向新创建的实例对象。
- 箭头函数中的`this`：箭头函数没有自己的`this`绑定，它的`this`是外层作用域中的`this`。
- 如果函数使用了严格模式（'use strict'），那么在该函数中的 this 将不会指向全局对象。
- 当函数作为事件处理函数时，this 指向触发事件的元素。

需要特别注意的是，在 JavaScript 中，this 的值是在函数被调用时才确定的，而不是在函数被定义时就确定的。因此，在使用 this 关键字时，需要注意当前代码执行的上下文环境以及 this 的具体指向。

### 全局函数/匿名函数的this

全局函数中this = window,函数被作为某个对象的方法调用时，this等于那个对象。匿名函数的执行环境具有全局性，其this通常指向windows

```JavaScript
let message = {
  name:'john',
  regularFunction: function(){
    console.log(this)
    console.log('hello' + this.name);
    //hello john
  },
  arrowFunction:()=>console.log('hi'+this.name)
  //hi
}

message.regularFunction();
message.arrowFunction();
cnosole.log(this.name)// empty string
cnosole.log(this) // window object
```

### 箭头函数的this

箭头函数并没有属于⾃⼰的this，它所谓的this是捕获其所在上下⽂的 this 值，作为⾃⼰的 this 值。

箭头函数体内的 this 对象，就是定义该函数时所在的作用域指向的对象，而不是使用时所在的作用域指向的对象。

箭头函数的this对象是定义时所在的对象，而不是使用时所在的对象，所以指向的是the window

```JavaScript
var name = “The Window”;
var object = {
  name : “My Object”,
   //匿名函数
  getNameFunc : function(){
    return function(){
        //这个this指向全局，因为匿名函数的执行环境具有全局性，this.name会指向第一个出现的name
      return this.name;
    };
  } 
};
object.getNameFunc()() 
//”The Window” (in non-strict mode) 
```

在定义匿名函数之前，我们把对象赋值给了一个名叫`that`的变量，而在定义了闭包之后，闭包也可以访问这个变量，因为它是我们在包含函数中特意声明的一个变量，即使在函数返回之后，that也仍然引用着object,所以调用`object`,`getNameFunc()()`就返回了，`my object`.

```JavaScript
var name = “The Window”;
var object = {
  name : “My Object”,
  getNameFunc : function(){
    var that = this;
    return function(){
      return that.name;
    };
  } 
};
object.getNameFunc()()  //”My Object” 
```

# ==类型==

## 数据类型

JavaScript 中常见数据类型有Number、String、Boolean、Object、Array、Json、Function、Date、RegExp、Error、undefined、Null等十几种。ES6还有新增的数据类型有BigInt、Symbol、Set、Map等。

### Symbol BigInt Set Map

- `Symbol` 代表创建后独一无二且不可变的数据类型，它主要是为了解决可能出现的全局变量冲突的问题。 

- `BigInt` 是一种数字类型的数据，它可以表示任意精度格式的整数，使用 BigInt 可以安全地存储和操作大整数，即使这个数已经超出了 Number 能够表示的安全整数范围。

- `Set` 是ES6新增的一种新集合类型，Set 在很多方面都像是加强的Map，这是因为他们的大多数API和行为都是共有的。Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。

- `Map` 是一个带键的数据项的集合，就像一个对象一样。但是它们直接最大的差别是 Map 允许任何类型的键。

### 可分为原始数据类型和引用数据类型

- 栈：原始数据类型（Undefined、Null、Boolean、Number、String） 

- 堆：引用数据类型（对象、数组和函数）

### 包装类型

在 JavaScript 中，基本类型是没有属性和方法的，但是为了便于操作基本类型的值，在调用基本类型的属性或方法时 JavaScript 会在后台隐式地将基本类型的值转换为对象，如：

```js
const a = "abc";
a.length; // 3
a.toUpperCase(); // "ABC"
```

在访问`'abc'.length`时，JavaScript 将'abc'在后台转换成`String('abc')`，然后再访问其length属性。 JavaScript也可以使用Object函数显式地将基本类型转换为包装类型：

```js
var a = 'abc'
Object(a) // String {"abc"}
```

也可以使用valueOf方法将包装类型倒转成基本类型：

```js
var a = 'abc'
var b = Object(a)
var c = b.valueOf() // 'abc'
```

```js
var a = new Boolean( false );
if (!a) {
	console.log( "Oops" ); // never runs
}
```

## 类型判断

### 数据类型检测方式

#### a. typeof

Array , object , null typeof -> object

缺点：引用类型无法判断

```js
console.log(typeof 2);               // number
console.log(typeof true);            // boolean
console.log(typeof 'str');           // string
console.log(typeof function(){});    // function
console.log(typeof undefined);       // undefined

console.log(typeof {});              // object
console.log(typeof []);              // object    
console.log(typeof null);            // object
```

#### b. instanceof

instanceof可以正确判断对象的类型，其内部运行机制是判断在其原型链中能否找到该类型的原型。

缺点：instanceof只能正确判断引用数据类型，而不能判断基本数据类型。

instanceof 运算符可以用来测试一个对象在其原型链中是否存在一个构造函数的 prototype 属性。

```js
console.log(2 instanceof Number);                    // false
console.log(true instanceof Boolean);                // false 
console.log('str' instanceof String);                // false 

console.log([] instanceof Array);                    // true
console.log(function(){} instanceof Function);       // true
console.log({} instanceof Object);                   // true
```

#### c. constructor

constructor有两个作用，一是判断数据的类型，二是对象实例通过 constrcutor 对象访问它的构造函数。需要注意，如果创建一个对象来改变它的原型，constructor就不能用来判断数据类型了

```js
console.log((2).constructor === Number); // true
console.log((true).constructor === Boolean); // true
console.log(('str').constructor === String); // true
console.log(([]).constructor === Array); // true
console.log((function() {}).constructor === Function); // true
console.log(({}).constructor === Object); // true
```

```js
function Fn(){};

Fn.prototype = new Array();

var f = new Fn();

console.log(f.constructor === Fn);    // false
console.log(f.constructor === Array); // true
```

#### d. Object.prototype.toString.call()

Object.prototype.toString.call() 使用 Object 对象的原型方法 toString 来判断数据类型

```js
var a = Object.prototype.toString;
 
console.log(a.call(2));
console.log(a.call(true));
console.log(a.call('str'));
console.log(a.call([]));
console.log(a.call(function(){}));
console.log(a.call({}));
console.log(a.call(undefined));
console.log(a.call(null));
```

同样是检测对象obj调用toString方法，`obj.toString()`的结 果和`Object.prototype. toString.cal(obj)`的结果不一样，这是为什么?

这是因为toString是Object的原型方法，而Array、 Function等类型作为Object的实例,都重写了toString方法。不同的对象类型调用toString方法时，根据原型链的知识，调用的是对应的重写之后的toString方法(function类型返回内容为函数体的字符串，Array类型返回元素组成的字符串)，而不会去调用Object上原型toString方法(返回对象的具体类型)， 所以采用`obj.toString()`不能得到其对象类型，只能将obj转换为字符串类型;因此，在想要得到对象的具体类型时，应该调用Object原型上的toString方法。

#### e. 自创

```js
function getType(obj){
  let type  = typeof obj;
  if (type !== "object") {    // 先进行typeof判断，如果是基础数据类型，直接返回
    return type;
  }
  // 对于typeof返回结果是object的，再进行如下的判断，正则返回结果
  return Object.prototype.toString.call(obj).replace(/^\[object (\S+)\]$/, '$1'); 
}

getType([])     // "Array" typeof []是object，因此toString返回
getType('123')  // "string" typeof 直接返回
getType(window) // "Window" toString返回
getType(null)   // "Null"首字母大写，typeof null是object，需toString来判断
getType(undefined)   // "undefined" typeof 直接返回
getType()            // "undefined" typeof 直接返回
getType(function(){}) // "function" typeof能判断，因此首字母小写
getType(/123/g)      //"RegExp" toString返回
```

## 类型转换

常见的类型转换有：

- 强制转换（显示转换）
- 自动转换（隐式转换）

1. Number()

![number()](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/005NUwygly1h7ndy9bjjqj30kx082myl.jpg)

2. String()

![string()](http://tva1.sinaimg.cn/large/005NUwygly1h7ndynt2dgj30kn072gmy.jpg)

3. Boolean()

![boolean()](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/53bdad10-6692-11eb-ab90-d9ae814b240d.png)

- `+` **操作符**
- `-`、`*`、`\` **操作符** `NaN` 也是一个数字
- `==`  **操作符**

# ==熟悉常用类型api==

## a. Date

### Date() constructor

Date() 构造函数可以创建 Date 实例或返回表示当前时间的字符串。

**Note:** `Date()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new), but with different effects.

```js
new Date();
Date();
```

Calling `new Date()` (the `Date()` constructor) returns a [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object. If called with an invalid date string, or if the date to be constructed will have a UNIX timestamp less than `-8,640,000,000,000,000` or greater than `8,640,000,000,000,000` milliseconds, it returns a `Date` object whose [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString) method returns the literal string `Invalid Date`.

Calling the `Date()` function (without the `new` keyword) returns a string representation of the current date and time, exactly as `new Date().toString()` does. Any arguments given in a `Date()` function call (without the `new` keyword) are ignored; regardless of whether it's called with an invalid date string — or even called with any arbitrary object or other primitive as an argument — it always returns a string representation of the current date and time.

### Methods

See MDN.

## b. array

### 数组常用的方法

会影响原数组 ⭕️，不会影响原数组 ❌。

1. 操作方法

   - 增

     - `push()`: 方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度 ⭕️
     - `unshift()`: 在数组开头添加任意多个值，然后返回新的数组长度 ⭕️
     - `splice()`: 传入三个参数，分别是开始位置、0（要删除的元素数量）、插入的元素，返回空数组 ⭕️
     - `concat()`: 首先会创建一个当前数组的副本，然后再把它的参数添加到副本末尾，最后返回这个新构建的数组 ❌

   - 删

     - `pop()`: 用于删除数组的最后一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `shift()`: 用于删除数组的第一项，同时减少数组的`length` 值，返回被删除的项 ⭕️
     - `splice()`: 传入两个参数，分别是开始位置，删除元素的数量，返回包含删除元素的数组 ⭕️
     - `slice()`: 不影响原数组：创建一个包含原有数组中一个或多个元素的新数组 ❌

   - 改

     `splice()`: 传入三个参数，分别是开始位置，要删除元素的数量，要插入的任意多个元素，返回删除元素的数组，对原数组产生影响 ⭕️

   - 查

     - `indexOf()`: 返回要查找的元素在数组中的位置，如果没找到则返回 -1❌
     - `includes()`: 返回要查找的元素在数组中的位置，找到返回`true`，否则`false` ❌
     - `find()`: 返回第一个匹配的元素 ❌
     - `findIndex()`: ❌

2. 转换方法：`join()`: 接收一个参数，即字符串分隔符，返回包含所有项的字符串 ❌

3. 排序方法：

   - `reverse()`: 顾名思义，将数组元素方向反转 ⭕️
   - `sort()`: 接受一个比较函数，用于判断哪个值应该排在前面 ⭕️

4. 迭代/遍历方法

- `some()`: 对数组每一项都运行传入的函数，如果有一项函数返回 true ，则这个方法返回 true ❌

- `every()`: 对数组每一项都运行传入的函数，如果对每一项函数都返回 true ，则这个方法返回 true ❌

- `forEach()`: 对数组每一项都运行传入的函数，没有返回值 ❌

- `filter()`: 对数组每一项都运行传入的函数，函数返回 `true` 的项会组成数组之后返回 ❌

- `map()`: 对数组每一项都运行传入的函数，返回由每次函数调用的结果构成的数组 ❌

- `reduce()`: 对数组中的每个元素按序执行一个由您提供的 reducer 函数，每一次运行 reducer 会将先前元素的计算结果作为参数传入，最后将其结果汇总为单个返回值。❌

### 数组遍历方法

`forEach`、`map`共同点：

1. 只能遍历数组并参数都一样
2. 不改变原函数（引用类型除外）
3. 无法中断循环；return 只是结束本地循环，进入下一次循环
4. break 或 continue 都将会报错

| **方法**                      | **是否改变原数组** | **特点**                                                     |
| ----------------------------- | ------------------ | ------------------------------------------------------------ |
| `forEach()`                   | 否                 | 数组方法，不改变原数组，没有返回值。                         |
| `map()`                       | 否                 | 数组方法，不改变原数组，有返回值，可链式调用。               |
| `filter()`                    | 否                 | 数组方法，过滤数组，返回包含符合条件的元素的数组，可链式调用 |
| `for...of...`                 | 否                 | for...of遍历具有Iterator迭代器的对象的属性，返回的是数组的元素、对象的属性值，不能遍历普通的obj对象，将异步循环变成同步循环 |
| `every()` 和 `some()`         | 否                 | 数组方法，some()只要有一个是true，便返回true；而every()只要有一个是false，便返回false. |
| `find()` 和 `findIndex()`     | 否                 | 数组方法，find()返回的是第一个符合条件的值；findIndex()返回的是第一个返回条件的值的索引值 |
| `reduce()` 和 `reduceRight()` | 否                 | 数组方法，reduce()对数组正序操作；reduceRight()对数组逆序操作 |

### forEach() / map() / for...of 跳出循环

在 forEach 中，不能使用 continue 和 break ，都会报错。可以使用 return 或 return false 跳出循环，但是效果与 for 中 continue 一样。 这种方法无法一次结束所有循环。

如何在forEach/map中跳出循环的总结：

1. 使用抛出异常来中断 forEach/map
2. 使用别的循环代替
   - 使用传统 for 循环
   - 使用数组 every/some 循环

forEach/map 中使用循环的注意事项:

1. 碰到需要终止的循环，避免使用 forEach 可以使用 for/for in循环
2. es6针对数组可以使用 every/some/find等方式
3. forEach/map 循环只能通 return 中断当次循环无法跳出循环
4. forEach/map 循环中使用 continue/break 报错
5. 如果非要使用 forEach/map 中断循环使用抛出异常

注意

- for/for...of： break跳出本次循环；continue结束本次循环执行下一次循环，没有return。
- for...in：会忽略break || continue。没有return。

```js
try {
  [1, 2, 3, 4, 5, 6].forEach((val, index) => {
    console.log(val);
    if (val === 3) {
      console.log("满足条件后的操作");
      throw new Error();
    }
    console.log("满足条件后不再执行", val);
  });
} catch (e) {
  console.log("可以不处理");
}
console.log("继续执行");

```

- `forEach()`

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.forEach((x) => {
  if (x === 4) {
    return;
  }
  newArr.push(x * 2);
});

```

在 forEach 中，不能使用 continue 和 break ，可以使用 return 或 return false 跳出循环，效果与 for 中 continue 一样。 注意该方法无法一次结束所有循环。

使用 `forEach()` 方法遍历了数组中的每一项，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `return` 语句，==跳出回调函数，并继续执行 `forEach()` 方法的下一次迭代。==(只是跳出，没有结束)

是因为 `forEach()` 方法有一个特定的用途，即对数组中的每一项执行一个操作。它不是一个循环，==所以不能使用 `break` 或 `continue` 语句来控制循环的执行。== ==Uncaught SyntaxError: Illegal break statement==

如果你想要在 `forEach()` 方法中使用 `break` 语句，那么你可以使用 `some()` 方法代替。`some()` 方法也会迭代数组的每一项，并对每一项执行一个回调函数。但是，它会在回调函数返回 `true` 的时候终止循环，并返回 `true`。

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

arr.some(x => {
  if (x === 4) {
    return true;
  }
  newArr.push(x * 2);
});
```

- `map()`

在 `map()` 方法的回调函数中使用 `break` 语句是不合法的。这是因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。它不是一个循环，所以不能使用 `break` 或 `continue` 语句来控制循环的执行。

如果你想要在 `map()` 方法中使用 `break` 语句，那么你可以使用一个普通的循环代替。

```js
const arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
  const newArr = arr.map((x) => {
    if (x === 4) {
      break; // Uncaught SyntaxError: Illegal break statement
      // continue // Uncaught SyntaxError: Illegal continue statement: no surrounding iteration statement
    }
    return x * 2;
  });
}

```

在这个例子中，我们在一个循环中调用了 `map()` 方法，并在回调函数中检查每一项是否为 `4`。如果一项是 `4`，那么就会执行 `break` 语句，终止循环。

但是，这种方法并不是很好，因为 `map()` 方法有一个特定的用途，即对数组中的每一项执行一个操作，并返回一个新的数组。如果你想要终止循环，那么更好的方法是使用 `for` 循环或者 `forEach()` 方法，而不是 `map()` 方法。

- for...of...

```js
const arr = [1, 2, 3, 4, 5];
const newArr = [];

for (let i = 0; i < arr.length; i++) {
  if (arr[i] === 4) {
    break;
  }
  newArr.push(arr[i] * 2);
}
```

# ==内存泄露 & 垃圾回收 & JavaScript 解释执行过程==

# 垃圾回收

## intro

垃圾回收是指一种自动的内存管理机制，可以帮助程序员管理内存。在使用垃圾回收机制的编程语言中，开发人员不需要手动去释放已经不再使用的内存空间，因为垃圾回收器会在程序运行时自动检测并回收这些空间。垃圾回收器通常会跟踪哪些内存块仍然被程序的其他部分引用，只有那些不再被引用的内存块才会被标记为可回收的垃圾，并在适当的时候被回收，从而避免了内存泄漏和内存溢出等问题。常见的垃圾回收机制包括标记-清除法、引用计数和复制算法等。

JavaScript是使用垃圾回收的语言，也就是说执行环境负责在代码执行时管理内存。垃圾回收语言通过算法来自动管理内存，开发人员只需要关注内存的使用情况。而非垃圾回收语言需要开发人员显式地管理内存，包括告诉编译器哪些内存块不再需要、或者使用引用计数等技术。无论使用何种方式管理内存，都需要开发人员注意内存泄漏问题，以确保内存使用的高效和应用程序的稳定性。

## 标记清理（mark-and-sweep）

标记清理（Mark and Sweep）是JavaScript最常用的垃圾回收策略之一。它的基本思想是通过标记那些仍然被引用的内存块，然后清理那些未被标记的内存块来进行垃圾回收。

简单阐述：

JavaScript 中最常用的垃圾回收策略：标记清理算法。该算法通过标记所有全局变量（即“根”），并检查其所有子对象，以确定哪些内存块可以被认为是活跃的（即不是垃圾）。未被标记的内存块被视为垃圾并可以被垃圾回收器释放和返回给操作系统。同时，该段落还提到了在 JavaScript 中，未被使用的引用是可能导致内存泄漏的常见问题，需要特别注意。

详细阐述：

1. 垃圾回收器构建一个“根”列表。根通常是在代码中保留引用的全局变量。在JavaScript中，“window”对象就是一个可以作为根的全局变量的例子。window对象始终存在，因此垃圾回收器可以将其及其所有子级视为始终存在的（即非垃圾）。 
2. 检查并标记所有根为活动状态（即非垃圾）。所有子级也要递归检查。从根可以到达的所有内容都不被视为垃圾。 
3. 所有未标记为活动状态的内存块现在可以视为垃圾。回收器现在可以释放该内存并将其返回给操作系统。

## 引用计数

引用计数是另一种垃圾回收策略，其基本思想是为每个内存块维护一个计数器，表示当前有多少个指针指向该内存块。每当新建一个指向该内存块的指针时，计数器加一，每当一个指针被销毁或者不再指向该内存块时，计数器减一。当计数器为0时，该内存块被回收并返回给操作系统。

引用计数策略在某些情况下可能更有效率，因为回收垃圾的时间可以更加可控。但是，引用计数也存在一些问题。

1. 循环引用问题。

   如果两个或多个对象相互引用，即使它们不再被应用程序使用，它们的引用计数仍将为1，因此垃圾回收器将无法清除它们。

2. 引用计数的性能开销问题

   因为需要在运行时维护计数器。这也意味着，如果没有及时正确地更新引用计数，可能会导致内存泄漏的问题。在实践中，许多编程语言都采用了标记清除的垃圾回收策略，因为它更加可靠，适用于大多数应用程序的情况。

```js
let a = {name: 'John'};
let b = a;
let c = a;
a = null;
```

# 内存泄漏

## 定义

内存泄漏是指程序在动态分配内存后，没有被正确释放，导致这部分内存不能被再次使用的现象。简单来说，就是指程序在运行时分配了一些内存以供使用，但是在使用完毕后没有及时释放，导致这部分内存无法再被其他程序或者线程使用，最终会导致系统资源浪费和系统运行缓慢等问题。

简单来讲就是，假设某个变量占用100M的内存，而你又用不到这个变量，但是这个变量没有被手动的回收或自动回收，即仍然占用100M的内存空间，这就是一种内存的浪费，即内存泄漏。

## 现象

1. 程序运行速度变慢
由于内存泄漏会导致内存的占用不断增加，最终会导致系统内存不足或者交换空间不足，从而导致程序运行速度变慢。

2. 内存泄漏警告提示
一些编程语言和开发工具可以检测到内存泄漏，会在程序运行时给出警告提示。

3. 内存溢出错误
内存泄漏会导致内存占用不断增加，当内存被消耗殆尽时，程序就会引发内存溢出错误，导致程序崩溃。

4. 系统资源浪费
由于内存泄漏导致系统资源的占用不断增加，如果不及时处理，就会导致系统资源的浪费。

## 原因

1. Accidental global variables 
Global variables are always available from the root and will never get garbage collected. Some mistakes cause variables leak from the local scope into the global scope when in non-strict mode:

- assigning value to the undeclared variable,
- using 'this' that points to the global object.

```js
function createGlobalVariables() {
  leaking1 = 'I leak into the global scope'; // assigning value to the undeclared variable
  this.leaking2 = 'I also leak into the global scope'; // 'this' points to the global object
};
createGlobalVariables();
window.leaking1; // 'I leak into the global scope'
window.leaking2; // 'I also leak into the global scope'
```

How to prevent it: Strict mode ("use strict") will help you prevent memory leaks and trigger console errors in the example above.

2. Closures

Function-scoped variables will be cleaned up after the function has exited the call stack and if there aren't any references left outside of the function pointing at them. The closure will keep the variables referenced and alive although the function has finished executing and its execution context and variable environment are long gone.

```js
function outer() {
  const potentiallyHugeArray = [];

  return function inner() {
    potentiallyHugeArray.push('Hello'); // function inner is closed over the potentiallyHugeArray variable
    console.log('Hello');
  };
};
const sayHello = outer(); // contains definition of the function inner

function repeat(fn, num) {
  for (let i = 0; i < num; i++){
    fn();
  }
}
repeat(sayHello, 10); // each sayHello call pushes another 'Hello' to the potentiallyHugeArray

// now imagine repeat(sayHello, 100000)
```

3. Timers
```js
function setCallback() {
  const data = {
    counter: 0,
    hugeString: new Array(100000).join('x')
  };

  return function cb() {
    data.counter++; // data object is now part of the callback's scope
    console.log(data.counter);
  }
}

setInterval(setCallback(), 1000); // how do we stop it?
```

```js
function setCallback() {
  // 'unpacking' the data object
  let counter = 0;
  const hugeString = new Array(100000).join('x'); // gets removed when the setCallback returns

  return function cb() {
    counter++; // only counter is part of the callback's scope
    console.log(counter);
  }
}

const timerId = setInterval(setCallback(), 1000); // saving the interval ID

// doing something ...

clearInterval(timerId); // stopping the timer i.e. if button pressed
```

How to prevent it: Especially if the callback's lifespan is undefined or indefinite:

being aware of the objects referenced from the timer's callback,
using the handle returned from the timer to cancel it when necessary.

4. Event listeners

Active event listener will prevent all variables captured in its scope from being garbage collected. Once added, the event listener will remain in effect until:

explicitly removed with removeEventListener()
the associated DOM element is removed.

```js
function listener() {
  doSomething(hugeString);
}

document.addEventListener('keyup', listener); // named function can be referenced here...
document.removeEventListener('keyup', listener); // ...and here
```
```js
document.addEventListener('keyup', function listener() {
  doSomething(hugeString);
}, {once: true}); // listener will be removed after running once
```

5. Cache

If we keep appending memory to the cache without getting rid of the unused objects and without some logic that limits the size, the cache can grow infinitely.

```js
let user_1 = { name: "Peter", id: 12345 };
let user_2 = { name: "Mark", id: 54321 };
const mapCache = new Map();

function cache(obj){
  if (!mapCache.has(obj)){
    const value = `${obj.name} has an id of ${obj.id}`;
    mapCache.set(obj, value);

    return [value, 'computed'];
  }

  return [mapCache.get(obj), 'cached'];
}

cache(user_1); // ['Peter has an id of 12345', 'computed']
cache(user_1); // ['Peter has an id of 12345', 'cached']
cache(user_2); // ['Mark has an id of 54321', 'computed']

console.log(mapCache); // ((…) => "Peter has an id of 12345", (…) => "Mark has an id of 54321")
user_1 = null; // removing the inactive user

// Garbage Collector
console.log(mapCache); // ((…) => "Peter has an id of 12345", (…) => "Mark has an id of 54321") // first entry is still in cache
```

**Possible solution:** To work around this issue, we can use `WeakMap`

5. Detached DOM elements

If a DOM node has direct references from JavaScript, it will prevent it from being garbage collected, even after the node is removed from the DOM tree.

In the following example, we created a `div` element and appended it to the `document.body`. The `removeChild()` doesn’t work as expected, and the Heap Snapshot will show detached HTMLDivElement since there is a variable still pointing to the `div`.

```js
function createElement() {
  const div = document.createElement('div');
  div.id = 'detached';
  return div;
}

// this will keep referencing the DOM element even after deleteElement() is called
const detachedDiv = createElement();

document.body.appendChild(detachedDiv);

function deleteElement() {
  document.body.removeChild(document.getElementById('detached'));
}

deleteElement(); // Heap snapshot will show detached div#detached
```

**How to prevent it?** One possible solutions is to move DOM references into the local scope. In the example below, the variable pointing to the DOM element is removed after the function `appendElement()` is finished.

```js
function createElement() {...} // same as above

// DOM references are inside the function scope

function appendElement() {
  const detachedDiv = createElement();
  document.body.appendChild(detachedDiv);
}

appendElement();

function deleteElement() {
  document.body.removeChild(document.getElementById('detached'));
}

deleteElement(); // no detached div#detached elements in the Heap Snapshot
```



## 排除方法

ref: 

1. https://www.ditdot.hr/en/causes-of-memory-leaks-in-javascript-and-how-to-avoid-them
2. https://auth0.com/blog/four-types-of-leaks-in-your-javascript-code-and-how-to-get-rid-of-them/
3. https://blog.logrocket.com/escape-memory-leaks-javascript/
4. https://medium.com/preezma/memory-leaks-in-javascript-and-how-to-avoid-them-63916a02f68
5. https://pjchender.dev/webdev/google-developer-memory-leak/

# JavaScript 解释执行过程

https://pythontutor.com/visualize.html#mode=display

Call Stack & Execution Context Explained



![image-20230411223429653](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/image-20230411223429653.png)

1. https://www.ruanyifeng.com/blog/2014/10/event-loop.html

## intro

JavaScript 是一种解释型语言，这意味着在执行 JavaScript 代码时，不会像编译型语言一样，先将代码编译成二进制代码再执行，而是逐行解释执行。当 JavaScript 代码被运行时，JavaScript 引擎会解释代码并直接执行它，一次只执行一行代码，而不是整个程序。这意味着 JavaScript 开发人员可以更快地修改和测试代码，而无需重新编译代码。但与编译型语言相比，解释型语言在运行时通常会比较慢。

JavaScript 是一种解释性语言，它的解释执行过程包括以下步骤：

1. 词法分析

在解释执行之前，JavaScript 引擎会先对代码进行词法分析。词法分析器会将代码分解成一个个词法单元（Token），每个词法单元代表一个关键字、标识符、运算符或其他语言特定的符号。

1. 语法分析

接下来，JavaScript 引擎会将词法单元转换成一个个语法树节点。语法树节点代表了代码的语法结构，包括表达式、语句、声明等。

1. 执行代码

JavaScript 引擎会按照语法树节点的顺序依次执行代码。对于每个节点，JavaScript 引擎会执行相应的操作，比如运算、函数调用等。在执行代码的过程中，JavaScript 引擎会根据需要创建变量、对象等，并将它们存储在内存中。

1. 垃圾回收

在代码执行过程中，JavaScript 引擎会定期进行垃圾回收。垃圾回收器会扫描内存中的对象，并找出那些不再被引用的对象。这些对象会被标记为可回收的，垃圾回收器会在之后释放它们占用的内存。

1. 事件循环

JavaScript 运行在单线程环境中，但它可以处理异步事件。事件循环机制负责处理异步事件，确保它们按照正确的顺序被处理。在事件循环中，JavaScript 引擎会不断地从事件队列中取出事件，并执行相应的回调函数。

总的来说，JavaScript 的解释执行过程可以分为词法分析、语法分析、执行代码、垃圾回收和事件循环等阶段。理解这些阶段可以帮助开发者更好地理解 JavaScript 的执行机制，以及如何编写高效的 JavaScript 代码。



----

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/image-20230411224659020.png" alt="image-20230411224659020" style="zoom:33%;" />

https://www.youtube.com/watch?v=iLWTnMzWtj4

as soon as the js program has run, the whole global execution context(全局执行上下文) has been created.

1. memory creation phase (line to line)

   the first phase, js skims the whole program,and allocates memory to all the variables and functions,and assign undefiend for value, and whole code for functions.

2. code execution phase (execution of context)

   run the whole js  program line by line. 会把值分配给之前memory中存好的变量

   whenever a new function is invoked, an altogether new execution context is created. 

   when the whole functin executed, the whole excution context for the function will be deleted 

when the whole program finished ,the whole global execution context will be deleted.

![image-20230411225954909](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/image-20230411225954909.png)

call stack maintains the order execution of execution of contexts.

CALL STACK maintains the ORDER of execution Contexts. It CREATES Context whenever a Program is executed or a Function is invoked and it pops out of the Call Stack when a Function or Program ENDS.

call stack  = exxcution context stack = program stack = control stack = runtime stack = machine stack

![image-20230411230734986](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/regexp/image-20230411230734986.png)

Call Stack 和 Execution Context 是理解 JavaScript 解释执行过程的重要概念。在 JavaScript 中，每当一个函数被调用，一个新的 Execution Context 就会被创建，然后被推入 Call Stack 中。当函数执行完成后，对应的 Execution Context 会被弹出 Call Stack。以下是这两个概念的详细解释：

Call Stack（调用栈）

Call Stack 是一种数据结构，用于存储函数调用的位置。当一个函数被调用时，它的 Execution Context 被创建并推入 Call Stack 的顶部。当函数执行完成时，对应的 Execution Context 会被弹出 Call Stack。这个过程是递归的，因为一个函数可以在它的执行过程中调用其他函数。这些函数会被推入 Call Stack 的顶部，直到它们执行完成并被弹出。

Execution Context（执行上下文）

Execution Context 是 JavaScript 中一个抽象的概念，它描述了函数的执行环境。每个 Execution Context 包含三个重要的属性：

1. Variable Environment（变量环境）：包含当前函数执行过程中所有的变量、函数声明和函数参数。它的作用是为 JavaScript 引擎提供一个查询变量的途径。
2. Lexical Environment（词法环境）：类似于变量环境，但是包含了更多的信息。它描述了当前函数执行过程中的词法作用域。这意味着它包含了函数外部的作用域以及函数内部的作用域。
3. This Binding（this 绑定）：用于确定当前函数中 this 关键字的值。

Execution Context 还包含了其他一些属性，比如：

- Function arguments（函数参数）
- Function declaration（函数声明）
- Outer environment reference（外部环境引用）

# 性能优化

# ==尾递归优化的逻辑和原理==

```js
function factorial(n) {
    if (n < 2) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

此方法存在的问题：

这个函数会在执行的瞬间在内存中持有n份factorial函数的上下文，相应地我们就付出了n份内存的代价。显而易见，这样的程序在空间复杂度的考量上是极不友好的。同时，伴随着每次函数执行成功，返回、出栈，也会对CPU造成一定的压力。

```js
// 尾递归优化
function factorial(n, result = 1) {
    if (n < 2) {
        return result;
    }
    return factorial(n - 1, n * result);
}
```
其执行速度就跟普通的循环没什么区别了，并且递归的深度也不受任何限制，也不用担心调用栈溢出或内存耗尽。

像上面第二种写法，在方法结束时出现的表达式，仅仅是自身的函数调用的递归，就是尾递归。

尾递归代码就是一种典型的尾调用，只是因为调用的函数也是自身，所以同时命中了递归的概念


> 尾调用(tail-call)是指一个函数里的最后一个动作是返回一个函数的调用结果的情形，即最后一步新调用的返回值直接被当前函数的返回结果。

> 传统模式的编译器对于尾调用的处理方式就像处理其他普通函数调用一样，总会在调用时创建一个新的栈帧（stack frame）并将其推入调用栈顶部，用于表示该次函数调用。

## 优化原理

尾递归优化是指在函数调用栈中，将递归函数实现成尾递归的形式，使得计算仅占用常量栈空间。

它的基本原理是：当递归函数调用时，如果已经没有剩余的操作需要执行，那么当前的栈帧就再也没有用处了。尾递归通过在递归调用时利用上一个栈帧来存储当前的状态，避免创建新的栈帧，从而实现了空间的优化。

以求阶乘为例，普通递归函数在计算n!时需要创建n个栈帧，而采用尾递归优化后，只需要一个栈帧就可以完成计算。因此，尾递归优化可以极大地节省计算资源，提高程序效率。

## 函数栈的作用

栈 - 后入先出 - 保持入口环境

```js
function main() {
    //...
    foo1();
    //...
    foo2();
    //...
    return;
}

main();
```
上面是一个简单的示例代码，我们现在简单在大脑里面模拟一下这个 main 函数调用的整个过程，`$`字符用于表示占地：

1. 首先我们建立一个函数栈。 `$main` 函数调用，将 `main` 函数压进函数栈里面。`$ main`

2. 做完了一些操作以后，调用 foo1 函数，foo1 函数入栈。`$` main foo1 foo1 函数返回并出栈。`$ main`

3. 做完一些操作以后，调用 foo2 函数，foo2 函数入栈。`$` main foo2 foo2 函数返回并出栈。`$ main`

4. 做完余下的操作以后，main函数返回并出栈。`$`

上面这个过程说明了函数栈的作用是什么？就是第 4 和第 6 步的作用，让 foo1 和 foo2 函数执行完了以后能够在回到 main 函数调用 foo1 和 foo2 原来的地方。这就是栈，这种”后入先出“的数据结构的意义所在。

尾递归 - 优化函数的调用栈

ref:
1. https://www.freecodecamp.org/chinese/news/js-tail-recursion/
2. https://zhuanlan.zhihu.com/p/36587160


# 事件冒泡

Event Bubbling is a concept in the DOM (Document Object Model). It happens when an element receives an event, and that event bubbles up (or you can say is transmitted or propagated) to its parent and ancestor elements in the DOM tree until it gets to the root element.

When elements receive events, such events propagate to their parents and ancestors upward in the DOM tree. This is the concept of Event Bubbling, and it allows parent elements to handle events that occur on their children's elements.

Event objects also have the stopPropagation method which you can use to stop the bubbling of an event. This is useful in cases where you want an element to receive a click event only when it is clicked and not when any of its children elements are clicked.

stopPropagation and preventDefault are methods of the event object for stopping default behaviors. Here is an article on the difference between these methods.

事件冒泡是 DOM（文档对象模型）中的一个概念。当一个元素接收到一个事件时，该事件会向上冒泡（或者说传递或者传播）到其父元素和祖先元素直到它到达根元素。

当元素接收事件时，这些事件会向上在 DOM 树中传播到其父元素和祖先元素。这就是事件冒泡的概念，它允许父元素处理发生在子元素上的事件。

事件对象也有 stopPropagation 方法，可以用它来阻止事件的冒泡。这在某些情况下非常有用，例如当你想让一个元素只在被单击时才接收点击事件，而不是在任何其子元素被单击时都接收事件。

stopPropagation 和 preventDefault 是事件对象的方法，用于停止默认行为

`event.preventDefault()`
This method prevents default actions that browsers make when an event is triggered.

```html
<script>
const form = document.getElementById('form')

form.addEventListener('submit', (event) => {
  event.preventDefault()
  
  // process data and submit a request manually
})

const form = document.getElementById('form')

form.addEventListener('submit', (event) => {
  event.preventDefault()
  
  // process data and submit a request manually
})
</script>

<a id="link" href="https://google.com">Google</a>

```
`stopPropagation`
Propagation is the act of spreading something, in this case, events. The stopPropagation method is used to prevent the spreading of events when an event is triggered on an element.

Propagation 是指传播某些事物的行为，而在这里指的是事件。stopPropagation 方法用于在元素触发事件时防止事件继续传播。

# 事件委托

事件委托（Event Delegation）是一种常用的JavaScript事件处理技巧，也称为事件代理。其原理是利用DOM元素的事件冒泡机制，将需要绑定的事件委托给父元素或祖先元素来处理。这个技巧可以减少事件绑定的次数，节省内存，提高性能。在动态添加或删除DOM元素时，使用事件委托可以避免频繁地绑定和解绑事件。例如，使用事件委托，你可以在父元素上绑定一个点击事件，而不必为子元素逐一绑定点击事件，这样可以减少很多重复工作

事件委托是一种有用的模式，它允许编写更清晰的代码，并使用类似的逻辑创建较少的事件监听器。

该算法如下：

1. 将单个处理程序放置在容器上。 
2. 在处理程序中，检查源元素 event.target。 
3. 如果事件发生在我们感兴趣的元素内部，则处理该事件。

Event Delegation is a useful pattern that allows you to write cleaner code, and create fewer event listeners with similar logic.

The algorithm:

Put a single handler on the container.
In the handler – check the source element event.target.
If the event happened inside an element that interests us, then handle the event.


refs：
1. https://javascript.info/event-delegation#summary
2. https://www.freecodecamp.org/news/event-delegation-javascript/
3. https://www.freecodecamp.org/news/manage-default-behavior-in-browser/
4. https://www.freecodecamp.org/news/event-bubbling-in-javascript/#how-to-stop-event-bubbling

# 最佳实践

# 使用设计模式减少冗余代码

这个不是一两天能看完的吧 😄

《JavaScript 设计模式与开发实践》

# ==函数避免 Side Effect==

## side effect

A few more classic cases of the side effects are,

| Classic Cases of Side Effects | Definition                 |
| ----------------------------- | -------------------------- |
| Mutating the input itself     | 改变输入本身               |
| Querying/Updating DOM         | 查询/更新DOM               |
| Logging(even in the console)  | 记录日志（甚至在控制台中） |
| Making an XHR/fetch call      | 进行XHR/fetch调用          |

## 方式

函数避免产生副作用（side effect）的方法主要有以下几种：

| 技术       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| 纯函数     | 在输入相同的情况下，始终返回相同的结果，不会修改传入的参数或引起其他的副作用。 |
| 不可变数据 | 一旦创建，就不能被修改的数据结构。使用不可变数据可以防止函数修改数据结构或共享的状态。 |
| 函数式编程 | 强调函数的纯粹性和不可变数据，使用函数来处理数据，而不是直接修改数据。 |
| 命令式编程 | 基于语句的编程范式，通常涉及修改变量和状态。为了避免副作用，可以使用更为函数式的编程风格。 |

在函数式编程中，函数通常被设计为避免产生副作用。因此，大部分函数调用的结果都是从输入参数中派生出的值。没有副作用使得进行形式化验证更加容易，并且倾向于使用更简单的测试方法。

函数式编程是一种构建应用程序的过程，主要由纯函数组成，避免共享状态、对数据的变异和副作用。它是一种声明式的编程方式，而不是命令式的，应用程序状态从一个函数流向下一个函数。

函数可以避免 Side Effect。函数是一种封装代码的方式，它可以将数据和操作封装在一起。通过传递参数的方式，函数可以接收输入并返回输出，而不会改变外部的状态或环境。使用纯函数（Pure Function）可以完全避免 Side Effect，因为它们不会修改任何外部的状态或环境。如果函数没有 Side Effect，那么它们将更容易进行测试、调试和维护，也更容易实现函数的复用性。

In functional programming, functions are often designed to avoid side effects, with the result of most function calls being a derived value from the input parameters. The lack of side effects makes it easier to do formal verifications, and tends to lean towards an easier method of testing.

Functional programming is the process of building applications, composing it primarily of pure functions, avoiding shared state, mutations on data and side effects. It is declarative rather than imperative, and application state flows from one function to the next.

## 纯函数

为了简化起见，我们可以认为纯函数是一种仅由其输入确定输出且对外部世界没有可观察影响的函数。它们提供的主要优点（在我看来）是可预测性，如果你给它们相同的输入值，它们总是会返回相同的输出。

| Criteria    | Definition                                                   |
| ----------- | ------------------------------------------------------------ |
| Predictable | 确定相同输入时产生可预测输出                                 |
| Readable    | 任何阅读该函数作为独立单元的人都能完全理解其目的             |
| Reusable    | 可以在源代码的多个位置重复使用该函数，而不会改变其和调用者的行为 |
| Testable    | 我们可以将其作为独立单元进行测试                             |

### 幂等函数

`Idempotent function` (幂等函数) 是指一个函数执行多次所得到的结果和执行一次所得到的结果是相同的。更具体地说，如果对于某个函数 f(x)，当使用 x 作为输入时，多次执行 `f(f(f(...f(x)...)))` 所得到的结果与单次执行所得到的结果一致，则称该函数是` idempotent function`。

例如，在计算机科学中，HTTP PUT 和 DELETE 方法通常被认为是 idempotent 方法，因为无论执行多少次请求，其结果都是相同的。即使再次执行这些请求，也不会对服务端产生任何副作用。

`Idempotent function`在抽象代数和函数式编程中也有重要的应用

### 幂等函数和纯函数的区别

幂等函数指的是一种函数，无论调用多少次，其返回结果都相同，不会产生副作用。也就是说，对于相同的输入，每次调用该函数都会返回相同的输出，并且不会对系统状态造成任何影响。

而纯函数是指一个函数，除了其返回值以外，没有其他对系统状态产生影响的行为。也就是说，纯函数不会修改外部变量或者产生任何副作用，也不依赖于任何外部状态。

可以说，幂等函数是纯函数的一个子集，因为幂等函数也是不会产生副作用的函数，但是幂等函数的返回值可能受到外部状态的影响，而纯函数则不会。

## 不可改变数据 Immutability

不可变对象是在创建后无法通过属性操作或赋值进行修改的对象。可变对象是可以修改的对象。

### 方式： 

1. const
2. Object.freeze()
3. 第三方工具库:  [immutable.js](https://immutable-js.github.io/immutable-js/) and [mori](https://swannodette.github.io/mori/).

`const` declares a variable that cannot be reassigned after it has been created.

immutable objects can still be achieved in JavaScript by using the [Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze),which prevents the modification of the object one-level deep, thus making it partially immutable.

`const` 和 `Object.freeze()` 都是只能阻止对象第一层的数据不被改变。

ref:
1. https://thejs.dev/jmitchell/what-are-side-effects-and-what-you-can-do-about-them-jws
2. https://www.linkedin.com/advice/0/what-some-common-sources-side-effects-functional
3. https://blog.greenroots.info/what-are-pure-functions-and-side-effects-in-javascript
4. https://stackoverflow.com/questions/67450779/how-to-avoid-side-effects-javascript
5. https://dev.to/vonheikemen/dealing-with-side-effects-and-pure-functions-in-javascript-16mg
6. https://medium.com/m/global-identity-2?redirectUrl=https%3A%2F%2Fjavascript.plainenglish.io%2Fhow-to-avoid-side-effects-using-pure-functions-in-javascript-366acaafb60c
   

# 异常监控 & 兜底

异常监控和兜底都是为了确保系统的稳定性和可靠性，以便在出现异常情况时能够及时处理，确保系统能够持续运行并提供正常的服务。

异常监控可以帮助开发人员和运维人员及时发现系统中的异常情况，例如应用程序崩溃、数据库连接错误等，这些异常可能导致系统故障或数据丢失。通过及时发现和处理异常情况，可以减少系统故障的风险，提高系统的稳定性和可靠性。

兜底是指在系统出现故障或异常情况时，系统能够自动切换到备用的方案或机制，以确保系统的持续运行。例如，在电商系统中，如果支付系统出现故障，系统可以自动切换到另一个支付系统，以保证用户的订单能够正常完成。

ref:

1. https://juejin.cn/post/7112243495347175432#heading-14
2. https://www.cnblogs.com/moqiutao/p/14746734.html
3. https://levelup.gitconnected.com/the-definite-guide-to-handling-errors-gracefully-in-javascript-58424d9c60e6
4. https://rollbar.com/blog/guide-to-frontend-error-handling/
5. https://blog.bitsrc.io/best-practices-in-handling-errors-in-web-components-fb4fdb5eccb
6. https://zhuanlan.zhihu.com/p/80287643
7. https://scoutapm.com/blog/frontend-performance-monitoring

# ==Promise & Generator & async-await==

## Generator functions

Generator（生成器）是 ECMAScript 6 中新增的一种函数类型，通过 function* 关键字定义，可以用来控制迭代过程，并且可以在迭代过程中暂停或继续执行。Generator 函数使用起来像一个可迭代对象，可以使用 for ... of 循环或者 next() 方法进行迭代，每次迭代返回一个包含当前值和 done 属性的对象。最大特点就是可以交出函数的执行权（即暂停执行）

```js
function* myGenerator() {
  yield 'hello';
  yield 'world';
}

const iterator = myGenerator();
console.log(iterator.next()); // { value: 'hello', done: false }
console.log(iterator.next()); // { value: 'world', done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```
我们先定义了一个 Generator 函数 myGenerator，其中使用了 yield 关键字来定义要迭代的值。然后我们使用 Generator 函数创建了一个迭代器 iterator，并使用 next() 方法迭代，每次迭代返回一个包含当前值和 done 属性的对象。

```js
function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();

let one = generator.next().value;
// ---
one
1
generator.next().value
2
generator.next().value
3 // 可以拿到值
generator.next().value
undefined
```

cant get 3, It’s because for..of iteration ignores the last value, when done: true. So, if we want all results to be shown by for..of, we must return them with yield:

```js
function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();

for(let value of generator) {
  console.log(value); // 1, then 2
}
ConsoleLog.js:12 1
ConsoleLog.js:12 2
undefined // 拿不到3
```

```js
function* generateSequence() {
  yield 1;
  yield 2;
  yield 3;
}

let generator = generateSequence();

for(let value of generator) {
  alert(value); // 1, then 2, then 3
}
```
As generators are iterable, we can call all related functionality, e.g. the spread syntax ...:

```js
function* generateSequence() {
  yield 1;
  yield 2;
  yield 3;
}

let sequence = [0, ...generateSequence()];

alert(sequence); // 0, 1, 2, 3
```

### "yield" is a two-way street

"yield" 它不仅将结果返回给外部，还可以将值传递到generator内部。

That’s because yield is a two-way street: it not only returns the result to the outside, but also can pass the value inside the generator.
To do so, we should call generator.next(arg), with an argument. That argument becomes the result of yield.

调用 generator.next(arg)，并带上一个参数。这个参数会成为 yield 的结果。

```js
function* gen() {
  // Pass a question to the outer code and wait for an answer
  let result = yield "2 + 2 = ?"; // (*)

  alert(result);
}

let generator = gen();

let question = generator.next().value; // <-- yield returns the value

generator.next(4); // --> pass the result into the generator
```
==The first call generator.next() should be always made without an argument (the argument is ignored if passed).==

It starts the execution and returns the result of the first yield "2+2=?". At this point the generator pauses the execution, while staying on the line (*).
Then, as shown at the picture above, the result of yield gets into the question variable in the calling code.
On generator.next(4), the generator resumes, and 4 gets in as the result: let result = 4.
Please note, the outer code does not have to immediately call next(4). It may take time. That’s not a problem: the generator will wait.

```js
function* gen(x){
  var y = yield x + 2;
  return y;
}

var g = gen(1);
g.next() // { value: 3, done: false }
g.next(6) // { value: 6, done: true }
```
上面代码中，第一个 next 方法的 value 属性，返回表达式 x + 2 的值（3）。第二个 next 方法带有参数2，这个参数可以传入 Generator 函数，作为上个阶段异步任务的返回结果，被函数体内的变量 y 接收。因此，这一步的 value 属性，返回的就是6（变量 y 的值）。
就是相当于直接修改了yeild后面的值
### generator.throw
As we observed in the examples above, the outer code may pass a value into the generator, as the result of yield.
…But it can also initiate (throw) an error there. That’s natural, as an error is a kind of result.
```js
function* gen() {
  try {
    let result = yield "2 + 2 = ?"; // (1)

    console.log("The execution does not reach here, because the exception is thrown above");
  } catch(e) {
    console.log(e); // shows the error
  }
}

let generator = gen();

let question = generator.next().value;

generator.throw(new Error("The answer is not found in my database")); // (2)
```
Generator 函数体外，使用指针对象的 throw 方法抛出的错误，可以被函数体内的 try ... catch 代码块捕获。这意味着，出错的代码与处理错误的代码，实现了时间和空间上的分离，这对于异步编程无疑是很重要的。

```js
function* generate() {
  let result = yield "2 + 2 = ?"; // Error in this line
}

let generator = generate();

let question = generator.next().value;

try {
  generator.throw(new Error("The answer is not found in my database"));
} catch(e) {
  alert(e); // shows the error
}
```
### generator.return

generator.return(value) finishes the generator execution and return the given value.

```js
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();

g.next();        // { value: 1, done: false }
g.return('foo'); // { value: "foo", done: true }
g.next();        // { value: undefined, done: true }
```

### 迭代

在 JavaScript 中，Generator 对象默认只能被迭代一次。每次调用 `next()` 方法都会执行 Generator 函数中的代码，直到遇到 `yield` 关键字或者函数结束为止。当函数执行结束或者遇到 `return` 语句时，Generator 对象的迭代器状态就会变成 `done`，即迭代结束。

如果需要多次迭代 Generator 对象，可以通过将 Generator 函数的返回值设置为一个可迭代对象来实现。例如，可以使用 `yield*` 关键字将另一个 Generator 对象插入到当前 Generator 函数中，使得当前 Generator 对象可以迭代多次。

```js
javascriptCopy code
function* myGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const iterable = {
  [Symbol.iterator]: function* () {
    yield* myGenerator();
  },
};

for (const value of iterable) {
  console.log(value);
}

// Output:
// 1
// 2
// 3

for (const value of iterable) {
  console.log(value);
}

// Output:
// 1
// 2
// 3
```

在上面的示例代码中，我们定义了一个 Generator 函数 `myGenerator`，它可以生成 1、2、3 这三个数值。然后，我们通过定义一个可迭代对象 `iterable`，将 `myGenerator` 插入到其中，并使用 `for...of` 循环来迭代 `iterable`。由于 `iterable` 是一个可迭代对象，因此我们可以对其进行多次迭代，从而实现多次迭代 Generator 对象的效果。

### Summary

Generators are created by generator functions function* f(…) {…}.
Inside generators (only) there exists a yield operator.
The outer code and the generator may exchange results via next/yield calls.

refs: 
1. https://javascript.info/generators
2. https://www.ruanyifeng.com/blog/2015/04/generator.html

### Usage

```js
function* gen(){
  var url = 'https://jsonplaceholder.typicode.com/todos/1';
  var result = yield fetch(url);
}

var g = gen();
var result = g.next(); // 初始化运行

result.value.then(function(data){
  return data.json();
}).then(function(data){
  g.next(data); // 传值，改值，才能拿到数据
});
```

### shortage

1. 复杂性高：相较于普通的回调函数，使用 Generator 函数需要更复杂的代码结构和更高的抽象能力。不熟悉 Generator 函数的开发者可能会感到难以理解和使用。
2. 性能问题：Generator 函数的执行过程中需要保存状态，并利用 yield 暂停函数执行，这样会引入额外的性能开销，可能在某些场景下影响性能表现。Generator 是基于协程实现的，需要一些上下文切换的开销，这可能会影响性能。
3. 兼容性问题：Generator 函数并不是所有的浏览器都支持，在部分较旧的浏览器版本和环境下可能需要进行额外的兼容处理。
4. 可读性差： Generator 可以创建复杂的控制流和异步操作，但由于它们的实现通常需要使用许多 yield 关键字和 next() 方法，这会导致代码可读性较差。
5. 可维护性差：由于 Generator 可以控制异步流程，因此它们通常会导致代码变得复杂，难以维护。
6. 只能使用一次：Generator 只能被迭代一次，而且一旦迭代完成，就不能再重复使用。这意味着如果需要多次使用，需要重新创建一个新的 Generator 对象。
7. 无法中途取消：Generator 通常是在执行异步任务时创建的，一旦创建后，就无法中途取消任务。这可能会导致一些意外的结果，如内存泄漏等问题。

## Async & Await

`async/await` 是 JavaScript 中处理异步操作的一种方式。它是 ES2017 （ES8）引入的新特性，建立在 Promise 之上，可以让异步代码看起来像同步代码，更加易读和易维护。

在 JavaScript 中，async/await 就是一种语法糖，它简化了 Promise 的使用方式，使得异步操作的代码更加清晰、易读。async/await 的本质仍然是 Promise，它只是通过一种更加直观的方式来表达 Promise 的链式调用。

`async/await` 是一个语法糖，它本质上是基于 Promise 的一种封装。`async` 用于声明一个函数为异步函数，这个函数会自动返回一个 Promise 对象，可以使用 `await` 关键字来等待一个 Promise 对象的结果，并将其赋值给一个变量。使用 `try/catch` 可以处理异步操作的异常。

以下是一个使用 `async/await` 处理异步操作的示例：

```js
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

fetchData();
```

在上面的示例中，`fetchData` 函数被声明为异步函数，使用 `await` 关键字等待 `fetch` 返回的 Promise 对象和 `response.json()` 返回的 Promise 对象，分别将它们的结果赋值给 `response` 和 `data` 变量。`try/catch` 用于处理可能发生的异常。

使用 `async/await` 可以让异步代码看起来更加简洁、易读和易维护。但需要注意，`async/await` 本质上仍然是基于 Promise 的异步编程，因此需要理解 Promise 的基本概念和用法。

## diff

|          | Promise                                                      | Generator                                                    | async-await                                                |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 执行方式 | 通过 then 方法或 async/await 调用 resolve/reject 函数        | 通过 next 方法控制执行流程                                   | 通过 async/await 语法糖实现异步操作                        |
| 执行结果 | 异步操作结果可以是 resolved（已完成）、rejected（已拒绝）或 pending | 不返回具体的结果，而是通过 yield 暂停函数执行并返回一个可控制的迭代器 | 异步操作结果可以是 resolved（已完成）或 rejected（已拒绝） |
| 错误处理 | 通过 catch 方法或 async/await 中的 try/catch 捕获错误        | 在执行器函数中手动抛出错误并在调用方使用 try/catch 捕获      | 通过 try/catch 捕获错误                                    |
| 可读性   | 需要编写回调函数或链式调用，可读性较差                       | 可以在函数内部使用 yield 控制执行流程，可读性较好            | 语法糖实现，可读性较好                                     |
| 并发性   | 可以使用 Promise.all 或 Promise.race 实现并发操作            | 不支持并发执行多个异步操作；可以使用 co 库或自行实现并发控制 | 可以使用 Promise.all 或 Promise.race 实现并发操作          |

需要注意的是，Promise 和 async-await 都是基于回调函数的异步编程的改进，而 Generator 则是一种全新的异步编程方式。在实际开发中，选择使用哪种方式应根据具体的场景和需求来决定。



使用 async/await，我们可以使用类似于同步代码的方式来编写异步代码，代码的可读性得到了极大的提升，而且也方便了错误的处理。同时，async/await 还可以避免回调地狱和链式调用的问题，使得代码的结构更加清晰。

# ==Fetch vs XHR==

## Fetch
Fetch 是 JavaScript 中的一种网络请求 API，可以用于从网络上获取数据。它比传统的 XMLHttpRequest 更易于使用和理解，并支持跨域请求。使用 fetch() 方法发起网络请求，然后使用 then() 和 catch() 方法处理响应。

fetch号称是AJAX的替代品，是在ES6出现的，使用了ES6中的promise对象。Fetch是基于promise设计的。Fetch的代码结构比起ajax简单多。==**fetch不是ajax的进一步封装，而是原生js，没有使用XMLHttpRequest对象**。==

The Fetch API provides an interface for fetching resources (including across the network). It is a more powerful and flexible replacement for XMLHttpRequest.

The fetch() method starts the process of fetching a resource from a server.
The fetch() method returns a Promise that resolves to a Response object.

```js
async function logJSONData() {
  const response = await fetch("http://example.com/movies.json");
  const jsonData = await response.json();
  console.log(jsonData);
}
```
https://javascript.info/fetch
https://javascript.info/fetch-api
https://developer.mozilla.org/en-US/docs/Web/API/fetch

- fetch只对网络请求报错，对400，500都当做成功的请求，服务器返回 400，500 错误码时并不会 reject，只有网络错误这些导致请求不能完成时，fetch 才会被 reject。
- fetch默认不会带cookie，需要添加配置项：` fetch(url, {credentials: 'include'})`
- fetch不支持abort，不支持超时控制，使用setTimeout及Promise.reject的实现的超时控制并不能阻止请求过程继续在后台运行，造成了流量的浪费
- fetch没有办法原生监测请求的进度，而XHR可以

## XHR
XMLHttpRequest is a built-in browser object that allows to make HTTP requests in JavaScript.

XMLHttpRequest（XHR）是一个 Web API，用于在浏览器和服务器之间进行异步通信。XHR 可以在不重新加载页面的情况下从服务器获取数据，并允许我们在页面上更新部分内容，而不是整个页面。

```js
function ajax(options) {
  //创建XMLHttpRequest对象
  const xhr = new XMLHttpRequest();

  //初始化参数的内容
  options = options || {};
  options.type = (options.type || "GET").toUpperCase();
  options.dataType = options.dataType || "json";
  const params = options.data;

  //发送请求
  if (options.type === "GET") {
    xhr.open("GET", options.url + (params ? ("?" + params) : ""), true);
    xhr.send(null);
  } else if (options.type === "POST") {
    const contentType = options.dataType === "json"
      ? "application/json"
      : "application/x-www-form-urlencoded";
    const postData = options.dataType === "json"
      ? JSON.stringify(params)
      : params;
    xhr.open("POST", options.url, true);
    xhr.setRequestHeader("Content-Type", contentType);
    xhr.send(postData);
  }

  //接收请求
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      const status = xhr.status;
      if (status >= 200 && status < 300) {
        let responseText = xhr.responseText;
        if (options.dataType === "json") {
          responseText = JSON.parse(responseText);
        }
        options.success && options.success(responseText, xhr);
      } else {
        options.fail && options.fail(status);
      }
    }
  };
}

```

xhr.onreadystatechange 事件会在 XMLHttpRequest 对象的状态发生变化时被触发。XMLHttpRequest 对象的状态是由 readyState 属性来表示的。readyState 属性有 5 种可能的值，分别是：

1. 0 (uninitialized)：已创建 XMLHttpRequest 对象，但尚未调用 open() 方法。
2. 1 (opened)：已经调用 open() 方法，但尚未调用 send() 方法。
3. 2 (headers_received)：已经调用 send() 方法，并且已经接收到了响应头。
4. 3 (loading)：已经接收到响应头，并正在接收响应体（response body）。
5. 4 (done)：已经接收到完整的响应，且可以在客户端使用。

在使用 xhr.onreadystatechange 事件时，通常只需要检查 readyState 的值是否为 4，表示请求已完成并成功接收到响应。此时可以通过 status 属性来获取服务器返回的状态码（如 200 表示请求成功，404 表示请求的资源不存在等），通过 responseText 或者 responseXML 属性获取服务器返回的数据。

```js
ajax({
  url: '/api/getUserInfo',
  type: 'GET',
  dataType: 'json',
  data: {
    id: 123
  },
  success: function (response, xhr) {
    console.log(response); // 处理响应结果
  },
  fail: function (status) {
    console.log(status); // 处理错误情况
  }
});
```



## diff

| 特点       | Fetch                                                        | XHR                                                          |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| API 设计   | Promise API，简单易用，支持链式调用，语法简洁易读。          | 基于事件的 API，使用起来稍微复杂一些，需要手动处理多个回调函数。 |
| 请求类型   | 基于 Promise，可以使用 async/await 和其他 Promise 方法来处理响应结果 | 基于回调函数，需要使用回调函数来处理响应结果                 |
| 凭证信息   | 默认情况下不发送 cookies 和 HTTP 认证信息，但可以通过设置 credentials 选项来启用 | 可以通过设置 withCredentials 属性来启用                      |
| 取消请求   | 支持通过 AbortController 和 AbortSignal 接口来取消请求       | 可以通过 abort() 方法来取消请求                              |
| 错误处理   | 可以使用 try-catch 和 catch() 方法来处理异常                 | 可以使用 onerror 和 onabort 事件来处理异常                   |
| 浏览器支持 | 需要比较新的浏览器支持，但支持程度在逐渐提高                 | 较老的浏览器也支持，但一些新特性可能不支持                   |
| 请求头处理 | 请求头和请求体分离，可以用 Headers 对象来设置请求头。        | 直接通过 setRequestHeader() 方法设置请求头。                 |
| CORS支持   | 原生支持跨域请求，但是在某些情况下仍然会受到跨域限制。       | 需要额外设置                                                 |

取消请求

abortController对象的signal属性被用作fetch请求的一个参数，以便绑定fetch请求。在需要取消fetch请求时，可以调用abort()方法。

需要注意的是，一旦fetch请求被取消，将不会再触发then()或catch()方法。另外，如果同一个AbortController对象用于多个fetch请求，那么它们都将被取消。

```js
const abortController = new AbortController();
const signal = abortController.signal;

fetch(url, {
  signal: signal,
  // 其他 fetch 配置项
}).then(response => {
  // 处理响应
}).catch(error => {
  // 处理错误
});

// 取消请求
abortController.abort();
```

XMLHttpRequest（XHR）对象的取消请求比Fetch API稍微复杂一些。XHR对象不直接提供取消请求的方法，但可以通过调用XHR对象的abort()方法来实现取消请求。

调用XHR对象的abort()方法将终止当前请求并关闭连接。在调用abort()方法后，会触发XHR对象的onreadystatechange事件，将readyState属性设置为0，status属性设置为0。

下面是一个简单的示例代码：

```js
const xhr = new XMLHttpRequest();
xhr.open('GET', url, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      // 处理响应
    } else {
      // 处理错误
    }
  }
};
xhr.send();

// 取消请求
xhr.abort();

```

调用了XHR对象的abort()方法来取消请求。需要注意的是，取消请求将会终止当前的请求，但并不会取消之前已经发送的请求。因此，如果需要在发送请求之前检查是否需要取消请求，需要在调用send()方法之前进行处理。

```js
const xhr = new XMLHttpRequest();
xhr.open('GET', url, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      // 处理响应
    } else {
      // 处理错误
    }
  }
};
xhr.onerror = function() {
  // 处理网络错误
};
xhr.send();

```

设置请求头

```js
const headers = new Headers();
headers.append('Content-Type', 'application/json');

const data = {
  name: 'John',
  age: 30
};

const options = {
  method: 'POST',
  headers: headers,
  body: JSON.stringify(data)
};

fetch('https://example.com/api/users', options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

在这个示例中，首先创建了一个Headers对象，并使用append()方法向其中添加了一个Content-Type头，指示请求体的格式为JSON。

然后，创建一个options对象，设置了请求的方法为POST、请求头为刚才创建的Headers对象、请求体为一个JavaScript对象，该对象通过JSON.stringify()方法进行序列化为JSON格式的字符串。

最后，使用fetch()方法发起请求，并将options对象作为第二个参数传入。在响应返回后，使用json()方法将响应体解析为JavaScript对象，并在控制台中打印出来。

需要注意的是，Headers对象中的头名是不区分大小写的，即'Content-Type'和'content-type'是等效的。

```js
const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};

xhr.open('GET', 'https://example.com/api/users', true);
xhr.setRequestHeader('Authorization', 'Bearer ' + accessToken);
xhr.send();
```

在这个示例中，首先创建了一个XMLHttpRequest对象。然后，通过setRequestHeader()方法设置了Authorization头，值为'Bearer ' + accessToken，其中accessToken是一个字符串，代表访问令牌。

接着，调用open()方法打开一个GET请求，指定了请求的URL和异步请求的方式。

最后，调用send()方法发送请求，并在onreadystatechange事件中处理响应。如果状态码为200，表示请求成功，将响应体输出到控制台中。

需要注意的是，setRequestHeader()方法需要在调用open()方法之后、调用send()方法之前调用。如果需要设置多个请求头，可以多次调用setRequestHeader()方法。同样地，头名也是不区分大小写的。

CORS

Fetch 原生支持跨域请求，但是在某些情况下仍然会受到跨域限制。Fetch 是基于浏览器的原生 API，使用了现代的跨域请求技术，如 CORS（跨域资源共享），因此默认情况下支持跨域请求。

但是，如果请求的目标服务器未在响应头中明确允许跨域请求，则浏览器将拒绝响应。在这种情况下，您将收到一个 CORS 错误，错误消息可能会因浏览器而异。

为了避免这种情况，目标服务器必须在响应头中包含以下内容之一：

- Access-Control-Allow-Origin: *
- Access-Control-Allow-Origin: <origin>

第一个选项表示目标服务器允许来自任何域的跨域请求。第二个选项表示目标服务器只允许来自特定来源的跨域请求，该来源必须在响应头中指定。

需要注意的是，Fetch API 不会自动携带用户凭证信息（例如 cookies）到跨域服务器，除非目标服务器明确允许。在默认情况下，Fetch API 发出跨域请求时不会发送凭证信息。如果您需要发送凭证信息，可以使用 `credentials` 选项设置为 `"include"`，例如：

```js
fetch('https://example.com/api/users', {
  credentials: 'include'
})
.then(response => {
  console.log(response);
})
.catch(error => {
  console.error(error);
});
```

在这个示例中，`credentials` 选项设置为 `'include'`，表示在跨域请求中发送凭证信息。如果目标服务器未明确允许，则浏览器仍将拒绝响应。

XMLHttpRequest (XHR) 可以通过 CORS (Cross-Origin Resource Sharing) 实现跨域请求。

CORS 是一种机制，允许 Web 应用服务器进行跨域访问控制。具体来说，CORS 允许一个网页的资源请求来自于不同的域名，其核心思想是使用额外的 HTTP 头来告诉浏览器，允许跨域访问该资源。

在 XHR 中使用 CORS，需要设置 `withCredentials` 属性为 `true`。`withCredentials` 属性指示是否应该在发送请求时使用凭据 (如 cookie 或授权头)。要启用 CORS，还需要设置 `Access-Control-Allow-Origin` 和其他相关响应头。

以下是一个 CORS 请求的例子：

```js
const xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.open('GET', 'https://example.com/api/data');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onload = function() {
  if (xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```

在上面的例子中，设置 `withCredentials` 属性为 `true` 以启用跨域请求，设置请求头 `Content-Type` 为 `application/json`。在服务端响应中，需要设置 `Access-Control-Allow-Origin` 头来允许来自某个源的跨域请求。

需要注意的是，如果要在客户端进行跨域请求，服务端必须允许跨域请求。否则，浏览器将阻止跨域请求，导致请求失败。

`credentials` 是 Fetch API 的一个选项，它是一个枚举类型，用于指定请求中是否包括凭证（例如 cookie、HTTP 认证等）。

默认情况下，Fetch API 不会在请求中包含凭证信息，这意味着不会自动将 cookie、HTTP 认证等信息发送到服务器端。如果需要在请求中包含凭证信息，可以使用 `credentials` 选项来指定。

`credentials` 选项有三个值：

- `omit`：默认值，不包含凭证信息。
- `same-origin`：仅在请求 URL 与当前页面 URL 同源时包含凭证信息。
- `include`：始终包含凭证信息，即使跨域请求。

以下是一个使用 `credentials` 选项的示例：

```js

fetch('https://example.com/api', {
  credentials: 'include'
})
  .then(response => {
    // 处理响应结果
  })
  .catch(error => {
    // 处理错误
  });
```

在上面的示例中，`credentials` 选项被设置为 `'include'`，表示始终包含凭证信息。

# ==Proxy vs Reflect==

https://javascript.info/proxy

Proxy 和 Reflect 是 ES6 引入的两个新特性，它们可以帮助我们更加方便、灵活地处理对象的操作和行为。

代理（Proxy）和反射（Reflect）是 JavaScript 中允许开发人员以独特方式操作对象的两个特性。

代理是一个对象，允许您拦截并自定义对另一个对象执行的操作。当访问代理对象的属性或方法时，代理会拦截操作并可以对其进行自定义处理。代理对象可以用来实现数据绑定、访问控制等功能。

反射是一组内置的方法，可以让您在运行时操作对象的属性和方法。Reflect 对象提供了许多方法，如 Reflect.get()、Reflect.set()、Reflect.has() 等，可以替代传统的对象操作方法，提供更严谨的语法和错误处理。

虽然两者都可以用来操作对象，但它们的使用场景略有不同。代理通常用于实现高级功能，如数据绑定、访问控制等，而反射则用于对象操作的基础功能，例如读取、设置属性等。

## Proxy

Proxy 是一种用于创建对象代理的机制，可以在对象操作前后拦截并自定义处理。它通过在目标对象之前架设一层拦截器，可以对目标对象的读取、赋值、删除、函数调用等操作进行拦截和自定义处理。我们可以通过 Proxy 对象的 `get()`、`set()`、`deleteProperty()` 等方法拦截这些操作，并在其中添加自定义逻辑。

`let proxy = new Proxy(target, handler)`

```js
const validator = {
  set(target, property, value) {
    if (property === 'age') {
      if (typeof value !== 'number' || value <= 0 || value > 120) {
        throw new TypeError('Invalid age')
      }
    }
    target[property] = value
  }
}

const person = new Proxy({}, validator)

person.age = 30 // 正常赋值
console.log(person.age) // 30

person.age = 'foo' // 校验失败，抛出异常

```

## Reflect

Reflect is a built-in object that simplifies creation of Proxy.

Reflect 是一个内置对象，可以简化 Proxy 的创建。

| Operation           | `Reflect` call                      | Internal method |
| :------------------ | :---------------------------------- | :-------------- |
| `obj[prop]`         | `Reflect.get(obj, prop)`            | `[[Get]]`       |
| `obj[prop] = value` | `Reflect.set(obj, prop, value)`     | `[[Set]]`       |
| `delete obj[prop]`  | `Reflect.deleteProperty(obj, prop)` | `[[Delete]]`    |
| `new F(value)`      | `Reflect.construct(F, value)`       | `[[Construct]]` |
| …                   | …                                   | …               |

Reflect 是一个新的全局对象，提供了一组与 Proxy 对象拦截器方法一一对应的静态方法。Reflect 的静态方法与 Proxy 对象拦截器方法的名称和功能基本一致，例如 `Reflect.get()` 方法与 `Proxy` 对象的 `get()` 方法功能相同。使用 Reflect 方法可以更加灵活和方便地执行一些操作，例如在不确定一个对象是否有某个方法时，我们可以使用 `Reflect.has()` 方法来判断，而不需要使用 `obj.hasOwnProperty()` 方法。

```js
const log = {
  set(target, property, value) {
    console.log(`SET ${property} = ${value}`)
    return Reflect.set(target, property, value)
  },
  get(target, property) {
    console.log(`GET ${property} = ${Reflect.get(target, property)}`)
    return Reflect.get(target, property)
  }
}

const obj = new Proxy({}, log)

obj.a = 123 // SET a = 123
console.log(obj.a) // GET a = 123, 123

```



## diff

Proxy有以下限制：

1. 无法代理内部属性，例如一些内置对象(Map, Set, Date, Promise等)的内部属性被称为"internal slots"，Proxy无法拦截这些属性的访问和修改。
2. 私有属性也无法被代理，因为它们也是使用内部属性实现的。
3. 原始对象和代理对象是不同的对象，如果将原始对象用作键值，然后代理它，那么代理对象无法被找到。
4. 代理无法拦截严格相等运算符(===)，因为严格相等运算符只能比较对象和它们自身是否相等，不能比较代理对象和原始对象是否相等。

| 特性                     | Proxy                                           | Reflect                                           |
| ------------------------ | ----------------------------------------------- | ------------------------------------------------- |
| 用途                     | 创建代理对象                                    | 提供操作对象的方法                                |
| 是否可拦截原型链上的操作 | 是                                              | 否                                                |
| 是否可取消拦截操作       | 是                                              | 否                                                |
| 可拦截的操作类型         | get, set, apply等                               | 与Proxy一致                                       |
| 操作返回值               | 可自定义                                        | 固定为Boolean类型                                 |
| 是否可直接调用           | 否，需要通过代理对象来调用                      | 是，可以直接调用方法                              |
| 与Object的关系           | Proxy可以代理任何对象，包括原生对象和自定义对象 | Reflect只能用于操作对象，不具有创建代理对象的功能 |



| 特性       | Proxy                                      | Reflect                                                      |
| ---------- | ------------------------------------------ | ------------------------------------------------------------ |
| 用途       | 创建代理对象，可以拦截和改变目标对象的行为 | 提供了操作对象的方法，不会改变对象行为                       |
| 对象操作   | 可以代理对象的访问、赋值、删除等操作       | 可以操作对象的属性、方法、访问器等                           |
| 拦截方法   | 支持多个拦截方法，例如get、set、has等方法  | 不支持对象拦截，只支持方法拦截                               |
| 错误处理   | 支持抛出TypeError等错误                    | 不支持抛出TypeError等错误                                    |
| 返回值处理 | 有返回值，返回代理对象的代理结果           | 大部分方法返回布尔值或抛出异常，只有Reflect.construct()、Reflect.apply()、Reflect.defineProperty()等方法返回一个新的对象或修改原始对象 |
| 代理处理   | 需要在代理处理函数中处理代理对象           | 可以直接对对象进行元编程操作                                 |
| 性能       | 通常比Reflect性能差                        | 通常比Proxy性能好                                            |

# ==Map vs Set==

Map 是一种以键值对的形式存储数据的集合。其中，键可以是任何类型的值（包括对象、函数等），值也可以是任何类型的值。与 JavaScript 中的普通对象相比，Map 对象支持更多的操作方法，例如迭代、批量操作等。Map 中的键是唯一的，可以通过 get() 和 set() 方法访问和修改对应的值。

Set 是一种存储唯一值的集合，其中的值可以是任何类型的值。与数组相比，Set 保证了其中的值是唯一的，且可以进行更高效的操作，例如查找、删除等。Set 中的值是唯一的，可以使用 add() 和 delete() 方法添加和删除值。

两者的使用场景有所不同。Map 主要用于存储具有一定结构的数据，例如用键值对存储的配置信息、对象之间的关系等；而 Set 则主要用于存储一组唯一的值，例如存储用户的标签、去重等。

需要注意的是，Map 和 Set 都是可迭代的对象，可以使用 for...of 循环遍历其中的元素。同时，它们都支持批量操作方法，例如 Map 的 set() 方法可以接受一个数组或另一个 Map 对象作为参数，从而快速初始化一个 Map。

## Map

Map – is a collection of keyed values.

JavaScript 中的 Map 是一种数据结构，用于存储键值对，其中键可以是任何 JavaScript 对象（包括原始类型、对象和函数），值也可以是任何 JavaScript 对象。

与普通的 JavaScript 对象不同，Map 允许使用对象作为键，并且可以迭代其元素。Map 还提供了一些有用的方法，如 set(key, value)、get(key)、has(key) 和 delete(key)，这些方法可以用来添加、获取、检查和删除键值对。另外，Map 的键和值是有序的，因此它可以按照插入的顺序迭代元素。

与数组相比，Map 可以提供更灵活的键和更快的查找速度，但是它的缺点是占用更多的内存。Map 在许多情况下都可以用来替代普通的 JavaScript 对象，尤其是当需要使用对象作为键时。

| 方法                | 描述                                                         |      |
| :------------------ | :----------------------------------------------------------- | :--- |
| new Map([iterable]) | 创建一个 Map 对象，可选地使用可迭代对象（例如数组）进行初始化，包含一组 [key, value] 键值对。 |      |
| map.set(key, value) | 存储一个键值对，使用给定的 key 和 value，返回 map 对象本身。 |      |
| map.get(key)        | 返回与给定 key 关联的值，如果 key 不存在则返回 undefined。   |      |
| map.has(key)        | 如果 key 存在则返回 true，否则返回 false。                   |      |
| map.delete(key)     | 删除指定 key 对应的元素，返回一个布尔值，如果 key 存在则为 true，否则为 false。 |      |
| map.clear()         | 删除 Map 中的所有元素。                                      |      |

```js
// 使用数组初始化 Map，其中每个子数组都包含一个键和一个对象
const myMap = new Map([
  ['apple', { color: 'red', price: 1 }],
  ['banana', { color: 'yellow', price: 2 }],
  ['orange', { color: 'orange', price: 3 }]
]);

// 获取 Map 中的值
console.log(myMap.get('banana').color); // 输出 'yellow'
```

## Set

Set – is a collection of unique values.

Methods and properties:

| 方法                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| new Set([iterable]) | 创建一个 Set 对象，可选地使用可迭代对象（例如数组）进行初始化，包含一组元素。 |
| set.add(value)      | 添加一个元素到 Set 中，如果该元素已存在则不进行任何操作，返回 set 对象本身。 |
| set.delete(value)   | 删除 Set 中的指定元素，返回一个布尔值，如果元素存在则为 true，否则为 false。 |
| set.has(value)      | 如果 Set 中存在给定元素则返回 true，否则返回 false。         |
| set.clear()         | 删除 Set 中的所有元素。                                      |
| set.size            | 返回 Set 中元素的数量。                                      |

# WeakMap vs WeakSet

The first difference between `Map` and `WeakMap` is that keys must be objects, not primitive values:

需要注意的是，由于 WeakMap 的键必须是对象，并且在没有其他引用时会被自动删除，因此 WeakMap 通常用于实现私有属性、缓存和垃圾回收等场景。而 Map 则适用于通用的键值对存储场景。

总体来说，Map 适用于存储任意类型的数据，并且需要在整个生命周期内保留键值对，而 WeakMap 适用于存储对象，并且需要在对象被销毁时自动删除键值对。

WeakMap is Map-like collection that allows only objects as keys and removes them together with associated value once they become inaccessible by other means.

WeakSet is Set-like collection that stores only objects and removes them once they become inaccessible by other means.

Their main advantages are that they have weak reference to objects, so they can easily be removed by garbage collector.

That comes at the cost of not having support for clear, size, keys, values…

WeakMap 和 WeakSet 被用作“辅助”数据结构，以补充“主要”对象存储。一旦对象从主存储中移除，如果它仅作为 WeakMap 的键或在 WeakSet 中找到，它将自动清除。

https://javascript.info/map-set#set

https://javascript.info/weakmap-weakset



| 特性     | Map                                                  | WeakMap                                              |
| :------- | :--------------------------------------------------- | :--------------------------------------------------- |
| 键类型   | 任何 JavaScript 对象（包括原始类型、对象和函数）     | 只能是对象（不包括原始类型和函数）                   |
| 垃圾回收 | 不会自动回收被引用的键，会一直占用内存               | 只要键不再被引用，垃圾回收机制就会自动将其回收       |
| 迭代     | 支持迭代器和 for-of 循环                             | 不支持迭代器和 for-of 循环                           |
| 大小     | 可以获取 size 属性来获取 Map 的大小                  | 没有 size 属性，不能获取 WeakMap 的大小              |
| 性能     | 存储大量数据时占用内存较多，但在查找和操作数据时较快 | 存储大量数据时占用内存较少，但在查找和操作数据时较慢 |
| 垃圾回收 | 不会被垃圾回收                                       | 可以被垃圾回收                                       |

# 模板字符串

Template literals 是一种在 JavaScript 中用于创建字符串的语法，它允许在字符串中插入表达式以生成动态内容。模板字符串由一对反引号（`）包围，插入表达式时使用 ${expression} 语法。例如：

```js
const name = 'Alice';
const greeting = `Hello, ${name}!`;
console.log(greeting); // 输出: Hello, Alice!
```

使用模板字符串的优点包括：

1. 更方便的字符串拼接：使用模板字符串可以避免传统字符串拼接时需要使用加号（+）来连接多个字符串和变量，使得代码更加简洁易懂。
2. 可读性更高：使用模板字符串可以将代码的结构清晰地呈现出来，从而使代码更易于阅读和理解。
3. 支持多行字符串：传统字符串必须使用反斜杠（\）来表示换行符，而使用模板字符串可以轻松地表示多行字符串。

# ==Functional Programming==

函数式编程是一种编程范式，其中函数被视为一等公民，即函数可以像变量一样被传递、存储和操作。FP强调的是不可变数据和纯函数，即不产生副作用的函数。

## 函数式编程的基本概念

### 1. 纯函数和副作用

在函数式编程中，纯函数是指不依赖于外部状态和副作用的函数，即对于相同的输入，始终产生相同的输出，不会对其他部分产生影响。而副作用则是指函数除了返回一个值以外，还会对外部环境产生影响，例如修改全局变量、文件操作、网络请求等。

下面是一个纯函数的例子：

```js
function add(a, b) {
  return a + b;
}
```

这个函数接受两个参数，然后返回它们的和。无论何时调用它，对于相同的输入，始终会产生相同的输出，不会对其他部分产生任何影响，因此是一个纯函数。

而下面是一个具有副作用的函数的例子：

```js
let counter = 0;

function increment() {
  counter++;
  console.log(counter);
}
```

这个函数不仅返回一个值（这里没有返回值），还会修改全局变量`counter`，并且还会输出一些信息。这种函数会对外部环境产生影响，因此是具有副作用的函数。

纯函数和具有副作用的函数之间的区别在于函数是否依赖于外部状态和是否产生副作用。在函数式编程中，推荐使用纯函数来实现功能，以避免出现不可预期的行为和副作用。

### 2. 不可变性和可变性

在函数式编程中，不可变性是指数据在创建后不可更改，而可变性则是指数据可以在创建后随时更改。在函数式编程中，不可变性是非常重要的概念，因为它可以确保函数不会对数据产生副作用，从而使程序更加可靠和可维护。

下面是一个可变性的例子：

```js
let myArray = [1, 2, 3];
myArray.push(4);
console.log(myArray); // [1, 2, 3, 4]
```

这个例子创建了一个数组`myArray`，然后通过`push`方法向其中添加了一个元素。由于数组是可变的，因此这个操作可以成功地改变数组的内容，使得数组中添加了一个元素。

下面是一个不可变性的例子：

```js
let myArray = [1, 2, 3];
let newArray = myArray.concat(4);
console.log(myArray); // [1, 2, 3]
console.log(newArray); // [1, 2, 3, 4]
```

这个例子同样创建了一个数组`myArray`，但是通过`concat`方法创建了一个新的数组`newArray`，该数组包含了`myArray`中的所有元素以及一个新的元素4。由于数组是不可变的，因此`concat`方法没有改变原始数组`myArray`的内容，而是创建了一个新的数组`newArray`。

总之，不可变性和可变性之间的区别在于数据是否可以更改。在函数式编程中，推荐使用不可变的数据结构和操作，以确保函数不会对数据产生副作用，从而使程序更加可靠和可维护。

### 3. 函数组合和管道

function composition, function pipeline

函数组合和管道是函数式编程中常用的概念，用于将多个函数组合在一起以实现复杂的操作。

函数组合是将两个或多个函数组合在一起，形成一个新的函数，该函数将先执行第一个函数，然后将其结果作为参数传递给第二个函数，以此类推。

```js
function addOne(x) {
  return x + 1;
}

function multiplyByTwo(x) {
  return x * 2;
}

const addOneAndMultiplyByTwo = (x) => multiplyByTwo(addOne(x));

console.log(addOneAndMultiplyByTwo(2)); // 6
```

这个例子定义了两个函数`addOne`和`multiplyByTwo`，然后通过函数组合创建了一个新函数`addOneAndMultiplyByTwo`，该函数将先对参数进行加一操作，然后再对结果进行乘二操作。

管道是将多个函数组合在一起，形成一个管道，该管道将先执行第一个函数，然后将其结果作为参数传递给第二个函数，以此类推，最终得到一个结果。下面是一个管道的例子：

```js
function addOne(x) {
  return x + 1;
}

function multiplyByTwo(x) {
  return x * 2;
}

function subtractThree(x) {
  return x - 3;
}

const pipeline = [addOne, multiplyByTwo, subtractThree];

const result = pipeline.reduce((acc, fn) => fn(acc), 2);

console.log(result); // 1
```

定义了三个函数`addOne`、`multiplyByTwo`和`subtractThree`，然后将它们放在一个数组中，通过`reduce`方法依次执行它们，从而实现了一个管道。在这个例子中，初始值为2，通过管道得到了最终的结果1。

函数组合和管道是函数式编程中常用的概念，它们可以将多个函数组合在一起以实现复杂的操作。函数组合通过将多个函数组合在一起形成一个新的函数，而管道则通过依次执行多个函数得到最终的结果。

### 4. 惰性求值和延迟执行

惰性求值和延迟执行是函数式编程中的两个常用概念，它们都与函数的执行时机相关。

惰性求值指的是在需要使用函数返回值时才去执行函数。它可以提高程序的性能，避免不必要的计算。在 JavaScript 中，惰性求值通常使用函数返回函数的方式来实现。下面是一个惰性求值的例子：

```js
function createExpensiveOperation() {
  console.log('Performing expensive operation...');
  return function() {
    console.log('Returning result of expensive operation...');
    return 42;
  }
}

const expensiveOperation = createExpensiveOperation();

console.log('Before using expensive operation');
console.log(expensiveOperation()); // Performing expensive operation...  Returning result of expensive operation... 42
console.log('After using expensive operation');
console.log(expensiveOperation()); // Returning result of expensive operation... 42
```

在这个例子中，`createExpensiveOperation`函数定义了一个昂贵的操作，并返回了一个函数。当调用`createExpensiveOperation`函数时，并不会立即执行昂贵的操作，而是返回一个函数，该函数会在需要时执行昂贵的操作。

延迟执行是指将一个操作推迟到最后可能的时刻执行，这通常用于优化程序的性能。在 JavaScript 中，延迟执行通常使用函数柯里化（currying）来实现。下面是一个延迟执行的例子：

```js
function add(x) {
  return function(y) {
    return x + y;
  }
}

const addTwo = add(2);

console.log('Before using addTwo');
console.log(addTwo(3)); // 5
console.log(addTwo(4)); // 6
console.log('After using addTwo');
```

在这个例子中，`add`函数定义了一个加法操作，并返回了一个函数。当调用`add`函数时，只会传递第一个参数，并返回一个函数，该函数会在以后的调用中使用第二个参数执行加法操作。在这种方式下，加法操作被推迟到最后可能的时刻执行。

惰性求值和延迟执行是函数式编程中的两个常用概念。惰性求值可以通过函数返回函数的方式实现，延迟执行通常使用函数柯里化实现。这两个概念都可以用于优化程序的性能。

## 一些函数方法

### 1. Map 

   将数组中的每个元素映射到一个新的值，并返回一个新的数组。

```js
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(number => number * 2);
console.log(doubledNumbers); // [2, 4, 6, 8, 10]
```

```js
function map(array, callback) {
  const newArray = [];

  for (let i = 0; i < array.length; i++) {
    newArray.push(callback(array[i], i, array));
  }

  return newArray;
}

const array = [1, 2, 3, 4, 5];

const mappedArray = map(array, function(item) {
  return item * 2;
});

console.log(mappedArray); // [2, 4, 6, 8, 10]
console.log(array); // [1, 2, 3, 4, 5]
```

```js
// 手写实现
Array.prototype.myMap = function(callback) {
  const newArray = [];

  for (let i = 0; i < this.length; i++) {
    newArray.push(callback(this[i], i, this));
  }

  return newArray;
};

const array = [1, 2, 3, 4, 5];

const mappedArray = array.myMap(function(item) {
  return item * 2;
});

console.log(mappedArray); // [2, 4, 6, 8, 10]
console.log(array); // [1, 2, 3, 4, 5]
```

方法接收一个回调函数作为参数，该回调函数接收三个参数：当前元素、当前元素的索引和原数组。函数内部创建了一个空的新数组`newArray`，然后使用`for`循环遍历当前数组中的每个元素，对每个元素都执行一次回调函数，并将回调函数的返回值添加到`newArray`中。最后，函数返回新数组`newArray`，而原始数组不会被修改。

#### QA

1. `this`关键字在`myMap()`方法内部指向了数组`myArray`。

2. 内部的callback接受了三个参数，可是外部的callback只接受了一个形参item呢？

在`Array.prototype.myMap()`方法中，我们定义了一个内部的回调函数`callback`，它接受了三个参数：`currentValue`（当前元素的值）、`index`（当前元素的索引）和`array`（原数组对象）。

然而，在使用`myMap()`方法时，我们只需要传递一个回调函数作为参数，该回调函数只接受一个参数`item`（当前元素的值），而不需要显式地指定回调函数的其他两个参数（即`index`和`array`）。这是因为，JavaScript引擎在每次迭代数组时，都会自动传递`index`和`array`参数给回调函数。

这是因为，`Array.prototype.myMap()`方法中定义的回调函数会作为一个函数对象，在每次迭代数组时都会被调用。在调用回调函数时，JavaScript引擎会自动传递当前元素的值作为第一个参数（即`currentValue`），当前元素的索引作为第二个参数（即`index`），以及原数组对象作为第三个参数（即`array`）。因此，我们只需要在定义回调函数时，指定一个参数来接受当前元素的值即可。

3. JavaScript引擎在每次迭代数组时，为什么都会自动传递index和array参数给回调函数

JavaScript引擎在每次迭代数组时，都会自动传递`index`和`array`参数给回调函数，这是因为`Array.prototype.myMap()`方法是内置的JavaScript方法，它在设计时就已经考虑了这个特性，以便让开发者能够更方便地访问当前元素的索引和原数组对象。

当我们在调用`myMap()`方法时，JavaScript引擎会遍历当前数组，并在每次迭代时，调用回调函数来处理当前元素。在每次调用回调函数时，JavaScript引擎会自动传递当前元素的值作为第一个参数（即`currentValue`）、当前元素的索引作为第二个参数（即`index`），以及原数组对象作为第三个参数（即`array`）。这种行为是内置在JavaScript引擎中的，因此我们不需要在调用回调函数时手动传递这些参数。

这个特性也使得`Array.prototype.myMap()`方法的回调函数具有了更大的灵活性。我们可以使用当前元素的索引来访问数组中的其他元素，或者使用原数组对象来访问数组的长度、属性等。这些操作都可以通过回调函数中的`index`和`array`参数来实现。

### 2. Reduce 

用于将数组中的所有元素归约为单个值。

> *accumulator: 累加器
>
> accumulator is the value returned from the previous iteration. It will be initialValue for the first iteration. currentValue is array item in the current iteration.(accumulator (which is a temporary result)).
>
> The value resulting from the previous call to `callbackFn`. On first call, `initialValue` if specified, otherwise the value of `array[0]`. --- MDN

```js
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((total, number) => total + number, 0);
console.log(sum); // 15
```

```js
// 手写reduce
Array.prototype.myReduce = function(callback, initialValue) {
  let accumulator = initialValue !== undefined ? initialValue : this[0];
  for (let i = initialValue !== undefined ? 0 : 1; i < this.length; i++) {
    accumulator = callback(accumulator, this[i], i, this); 
    // callback(accumulator, this[i], i, this)  回调函数将当前元素和accumulator作计算处理(相加或者起其他你指定的方式)，并使用return语句将新的accumulator值返回。reduce()方法会将这个新的accumulator值作为下一次迭代的参数传递给回调函数，以此类推，直到所有元素都被迭代完毕。
  }
  return accumulator;
}

const arr = [1, 2, 3, 4, 5];
const sum = arr.myReduce((accumulator, currentValue) => accumulator + currentValue);
console.log(sum); // 15

const product = arr.myReduce((accumulator, currentValue) => accumulator * currentValue, 1);
console.log(product); // 120
```

`myReduce()`的方法，它接受两个参数：一个回调函数`callback`和一个可选的初始值`initialValue`。`callback`函数接受四个参数：累加器`accumulator`、当前元素的值`currentValue`、当前元素的索引`index`和原数组对象`array`。`myReduce()`方法会返回最终的累加结果。

首先需要初始化一个累加器`accumulator`，如果有传入初始值`initialValue`，则将`accumulator`初始化为该值，否则将其初始化为数组中的第一个元素。接下来，我们使用一个循环来遍历数组中的元素，对于每个元素，都会调用回调函数`callback`来将该元素的值累加到累加器中。在调用`callback`函数时，我们会传递当前累加器的值、当前元素的值、当前元素的索引和原数组对象作为参数，以便让回调函数可以访问这些值。最后，`myReduce()`方法会返回最终的累加结果。

#### 使用`reduce()`方法时，有几个需要注意的地方：

1. 累加器的初始值

`reduce()`方法的第二个参数可以用来指定累加器的初始值。如果不指定初始值，那么第一次调用回调函数时，累加器的值将是数组中的第一个元素。如果数组为空并且没有提供初始值，`reduce()`方法会抛出一个`TypeError`错误。

因此，建议在使用`reduce()`方法时，始终提供一个初始值，以确保累加器的初始值是可控的，并且在空数组的情况下也能正常工作。

2. 回调函数的参数

`reduce()`方法的回调函数接受四个参数：累加器`accumulator`、当前元素的值`currentValue`、当前元素的索引`index`和原数组对象`array`。在回调函数中，可以使用这些参数来完成各种操作。但是需要注意的是，回调函数的前两个参数是必需的，而后两个参数是可选的。如果不需要使用后两个参数，可以省略它们，但是需要注意在回调函数中不要尝试访问它们，否则会引发错误。

3. 回调函数的返回值

`reduce()`方法的回调函数必须返回一个值，以便将该值用作下一次累加器的值。如果回调函数没有返回值，或者返回值为`undefined`，则`reduce()`方法会将当前累加器的值传递给下一次迭代，而不是使用回调函数的返回值。因此，在编写回调函数时，需要确保它始终返回一个值。

```js
const arr = [1, 2, 3, 4, 5];

const result = arr.reduce((acc, val) => {
  if (val % 2 === 0) {
    acc.push(val);
  }
  // return acc; // 确保返回新数组 
  // Uncaught TypeError: Cannot read properties of undefined (reading 'push')
}, []);

console.log(result); // undefined
```

回调函数只会在数组中的偶数元素上执行，并将它们添加到一个新的数组中。然而，由于回调函数没有显式地返回这个新数组，而是返回了`undefined`，因此`reduce()`方法只是将每个偶数元素添加到当前的累加器值中，并返回了`undefined`。

为了避免这种情况，需要确保回调函数始终返回一个值。在上面的例子中，可以在回调函数的末尾添加`return acc;`语句，以确保回调函数返回新的数组。

### 3. forEach 

`forEach()`方法可以用于迭代一个数组的每个元素，并为每个元素执行回调函数。

```js
const strings = ['foo', 'bar', 'baz'];
strings.forEach(string => console.log(string));
// foo
// bar
// baz
```

```js
Array.prototype.myForEach = function(callback) {
  for (let i = 0; i < this.length; i++) {
    callback(this[i], i, this);
  }
};
```

### 4. Pick 

`pick()`函数通常用于从一个对象中选取指定的属性，并返回一个新的对象，只包含选取的属性。

```js
const user = { name: 'John', age: 30, email: 'john@example.com' };
const pickedUser = pick(user, ['name', 'email']);
console.log(pickedUser); // { name: 'John', email: 'john@example.com' }
```

```js
function pick(obj, keys) {
  return keys.reduce((acc, key) => {
    if (obj.hasOwnProperty(key)) {
      acc[key] = obj[key];
    }
    return acc;
  }, {});
}

const obj = { name: 'Alice', age: 25, city: 'New York' };
const picked = pick(obj, ['name', 'city']);

console.log(picked); // { name: 'Alice', city: 'New York' }
```

### 5. Filter 

   用于从数组中筛选出符合条件的元素，并返回一个新的数组。

```js
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(number => number % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

```js
// 手写实现
Array.prototype.myFilter = function(callback) {
  const newArray = [];

  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this)) {
      newArray.push(this[i]);
    }
  }

  return newArray;
};

const array = [1, 2, 3, 4, 5];

const mappedArray = array.myFilter(function(item) {
  return item > 3;
});

console.log(mappedArray); 
console.log(array);
```

### 6. Find 

用于从数组中查找符合条件的元素，并返回该元素的值。如果数组中有多个符合条件的元素，find方法只会返回第一个元素。

```js
const numbers = [1, 2, 3, 4, 5];
const greaterThanThree = numbers.find(number => number > 3);
console.log(greaterThanThree); // 4
```

```js
// 手写实现
Array.prototype.myFind = function(callback) {
  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this)) {
      return this[i];
    }
  }
};

const array = [1, 2, 3, 4, 5];
const mappedArray = array.myFind(function(item) {
  return item > 3;
});

console.log(mappedArray); // [4]
console.log(array); // [1, 2, 3, 4, 5]
```

Flow、compose和curry是用于将函数组合起来并生成新的函数。

### 7. Flow 

将多个函数组合起来，将一个值作为输入传入第一个函数，然后将第一个函数的输出作为输入传入第二个函数，以此类推，最终返回最后一个函数的输出结果。

```js
// 将两个函数组合起来，将一个数字乘以2，再加上3
const timesTwo = num => num * 2;
const plusThree = num => num + 3;
const timesTwoPlusThree = flow(timesTwo, plusThree);

console.log(timesTwoPlusThree(4)); // 11
```

```js
function flow(...funcs) {
  return function(arg) {
    return funcs.reduce((result, func) => func(result), arg);
  }
}
```

```js
function flow(...funcs) {
  return function(arg) {
    let result = arg;
    for (let i = 0; i < funcs.length; i++) {
      result = funcs[i](result);
    }
    return result;
  }
}
```

```js
function double(x) {
  return x * 2;
}

function square(x) {
  return x * x;
}

const doubleThenSquare = flow(double, square);

console.log(doubleThenSquare(3)); // 36
```

通过一个循环迭代所有的传入函数，并将它们的结果传递给下一个函数，从而组合它们的功能，使用`...`运算符将传入的函数作为可变参数传递给`flow`函数，并返回一个新的函数，该函数将调用所有传入的函数，并将它们的结果组合起来。

### 8. Compose 

与Flow方法类似，但是是将函数从右到左依次组合起来，将最后一个函数的输出作为输入传入倒数第二个函数，以此类推，最终返回第一个函数的输出结果。

```js
// 将两个函数组合起来，将一个数字乘以2，再加上3
const timesTwo = num => num * 2;
const plusThree = num => num + 3;
const timesTwoPlusThree = compose(plusThree, timesTwo);

console.log(timesTwoPlusThree(4)); // 11
```

```js
function compose(...funcs) {
  return function(arg) {
    let result = arg;
    for (let i = funcs.length - 1; i >= 0; i--) {
      result = funcs[i](result);
    }
    return result;
  }
}

  return function(arg) {
    return funcs.reduceRight((result, fn) => {
      return fn(result);
    }, arg);
  }
}
```

### 9. Curry 

用于将一个函数变为柯里化函数，即将一个函数接受多个参数的能力变为接受单个参数的能力。

```js
// 将一个函数接受两个参数的能力变为接受单个参数的能力
const add = (a, b) => a + b;
const curriedAdd = curry(add);

console.log(curriedAdd(2)(3)); // 5
```

```js
// 在柯里化函数中，每次调用返回一个新函数，直到最后一次调用返回函数的计算结果。
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...args2) {
        return curried.apply(this, args.concat(args2));
      }
    }
  }
}
```

这个函数接受一个函数作为参数，并返回一个新的函数。新函数将在调用时检查其接收的参数数量，如果参数数量已经等于原始函数需要的参数数量，则直接调用原始函数；否则返回另一个函数，该函数将继续接收新的参数，直到参数数量足够为止。

```js
function add(x, y, z) {
  return x + y + z;
}

const curriedAdd = curry(add);
const add5 = curriedAdd(5);
const add5And6 = add5(6);

console.log(add5And6(7)); // 18
```

### 10. 使用Flow、Compose和Curry这些函数式编程工具需要注意：

1. 函数的顺序 在使用Flow和Compose时，需要注意函数的顺序。Flow方法将函数从左到右依次组合起来，Compose方法将函数从右到左依次组合起来。因此，需要根据具体的需求选择合适的方法，并确保函数的顺序正确。
2. 函数的纯净性 函数式编程强调函数的纯净性，即函数的输出只与输入有关，不会对外部环境产生影响。在使用Flow、Compose和Curry时，需要确保组合后的函数仍然是纯净函数，避免出现副作用。
3. 参数的数量 在使用Curry时，需要注意函数的参数数量。将一个函数柯里化后，每次调用只接受一个参数。如果函数的参数数量较多，需要多次调用柯里化后的函数才能得到最终的结果。因此，需要根据具体的需求选择合适的函数和参数数量。
4. 性能问题 在使用Flow、Compose和Curry时，需要注意性能问题。组合多个函数可能会导致性能下降，特别是在处理大量数据时。因此，需要根据具体的需求选择合适的函数组合方式，并进行性能优化。
