

# notes-back-up

# parts of Headers

## Headers

---------------------

1. HTTP 响应头中 Cache-Control，有时为首字母大写，有时为小写，哪个是正确写法: 都正确

2. 什么是伪头
Request Pseudo-Header Fields
https://www.rfc-editor.org/rfc/rfc9113.html#name-request-pseudo-header-field

在HTTP/2中，"请求伪头字段"（Request Pseudo-Header Fields）是一类特殊的头字段，它们用来传送对于请求来说非常重要的信息。这些伪头字段以冒号（:）开始，使其与常规的HTTP头字段区分开来。由于它们承载了关键的请求信息，它们被视为请求的一部分，但并不属于常规的HTTP头字段。HTTP/2定义了以下请求伪头字段：

:method - 表示HTTP方法（例如GET, POST等）。

:scheme - 指出了协议方案（例如http, https）。

:authority - 包含了服务器的权威部分，通常是域名和可能的端口号（例如example.com:443）。这个字段对应于HTTP/1.1中的Host头。

:path - 请求的路径和查询字符串（例如/index.html?page=12）。它不包括方案或域名部分，只有URI的路径和查询部分。

这些请求伪头字段对正确处理HTTP/2请求至关重要，它们必须正确设置和传输。任何HTTP/2请求都必须至少包含:method, :scheme, 和:path这三个请求伪头字段，除非该请求的目的是为了连接(authority)请求（使用OPTIONS方法的请求），在这种情况下，:authority字段是必需的，而:path则不是。不合规范的伪头字段使用可能会导致请求被拒绝。

在HTTP/2的上下文中，这些伪头字段的使用标志着与HTTP/1.x相比协议处理方式的转变，提供了更丰富的请求上下文信息，并进一步优化了传输。伪头字段不是由用户直接设置的，而是由客户端或浏览器在构造HTTP/2请求时自动生成并包含的。

3. 如何自定义 HTTP 头部
自定义HTTP头部通常涉及到向HTTP请求或响应中添加非标准的头部字段。这些自定义头部字段通常以X-为前缀，以表明它们是自定义的，尽管这一前缀的使用在新开发中已不再提倡。如果你正在开发一个需要传递额外信息的HTTP客户端或服务器，你可能希望使用自定义头部字段。在发送HTTP请求时，如果你使用的是JavaScript的fetch API，你可以通过设置Headers对象或使用普通的对象字面量来添加自定义头部。
```js
fetch('https://example.com/api/data', {
method: 'GET',
headers: {
'X-Custom-Header': 'CustomValue',
'Another-Custom-Header': 'AnotherValue'
}
});
```

此处一张header图，自定义的header用于多语言的处理

1. 观察自己常逛网站的 HTTP 请求头与响应头

2. <mark>通过 curl 与 httpbin 测试请求头部</mark> - WIP

---------------

## request header list
请求头相关key

1. age: Age 标头包含对象在代理缓存中停留的时间，以秒为单位。 Age 标头通常接近于0。 如果显示为 Age: 0 ，则表示该内容可能是从源服务器上获取的；否则，它通常是通过代理服务器当前日期与HTTP 响应中包含的 Date 通用标头之间的差值来计算得出的。
2. date: Date 通用 HTTP 标头包含了消息创建时的日期和时间。
警告： 在 fetch 规范中，Date 被列为禁止修改的标头，因此这段代码不会发送 Date 标头：
```js
fetch("https://httpbin.org/get", {
headers: {
Date: new Date().toUTCString(),
},
});
```

## Host 与 :authority

域名请求测试 --- WIP

## 内容协商

### Accept

- Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8
- \# 为了便于理解，我使用括号进行分组，括号仅仅是为了理解！ Accept: (text/html), (application/xhtml+xml), (application/xml;q=0.9), (*/*;q=0.8)
- , 拥有比 ; 更高的优先级，根据, 分组，而不是根据 ; 分组
- 其中 q 为 quality，意为权重，默认为 1。0-1。

### Accept-Language

### Accept-Encoding

- The Accept-Encoding request HTTP header indicates the content encoding (usually a compression algorithm) that the client can understand.
- Accept-Encoding表示Http响应是否进行压缩，会将客户端（e.g. 浏览器）能够理解的内容编码方式（通常是某种压缩算法）通知给服务端。
  Accept-Encoding用来标识客户端能够理解的内容编码方式。 Content-Encoding用来标识主体进行了何种方式的内容编码转换。
- Accept-Encoding: gzip/br/zstd/compress

### 反爬

- 在浏览器中会自动发送 Accept、Accept-Encoding 以及 Accept-Language 三个请求头，如上所示。 因此一些安全性要求较高的网站，将通过以上三个请求头是否存在判断请求方是浏览器还是爬虫。如果不存在以上请求头，则直接拒绝请求。

## Content-Type

指定 Body 的媒体资源类型，如果是请求头，则代表请求体的资源类型，如果是响应头，则代表响应体的资源类型。

### 请求头中的 Content-Type

`Content-Type: application/json`。

除此之外，在 API 中常见以下几种请求头中的 Content-Type：

- `application``/json`：请求体为 JSON
- `application/x-www-form-urlencoded`：请求体为以 `&` 分割的字符串，如 `a=3&b=4`
- `multipart/form-data`：请求体以 Boundary 分割

### 响应头中的 Content-Type

当响应头中含有 Content-Type 时，它指明 Response Body 的媒体资源类型。
因为我们可以通过 HTTP 去请求各种各样的资源，因此 Content-Type 基本上可以是所有 MIME 类型。
而在前端中，涉及到的响应头中的 Content-Type 为以下几种：
- text/html
- text/css
- application/javascript
- image/png
- image/jpeg
- image/webp
- image/svg+xml

在操作系统中你也会看到一个 excel/ppt/psd，他也是有 MIME Type 的，但可能在 Content-Type 中很少见到

## User-Agent

`User-Agent` 请求头是用以表明客户端的特征字符串，一般也会简称为 `UA`。

![image-20240603222701288](https://s2.loli.net/2024/06/03/ArV7e3dU9tgyPqw.png)

### 浏览器如何判断 PC/Mobile

既然在 UA 中包含了操作系统信息，便可使用它判断是否移动端。

通过判断 API `navigator.userAgent` 可获取该浏览器发送请求时的 User-Agent 请求头，对于 Android/iPhone 可以匹配以下正则。

```JavaScript
const appleIphone = /iPhone/i;
const appleIpod = /iPod/i;
const appleTablet = /iPad/i;
const androidPhone = /\bAndroid(?:.+)Mobile\b/i; // Match 'Android' AND 'Mobile'
const androidTablet = /Android/i;
```

当然，不要重复造轮子，推荐一个库: <https://github.com/kaimallea/isMobile>

```JavaScript
import isMobile from "ismobilejs";
const mobile = isMobile();
```

## 内容协商

同时 UA 请求头，也可用作内容协商，见 [User-Agent](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Content_negotiation#user-agent_首部)。

HTTP 服务器端根据请求头中的 `User-Agent` 返回不同的内容。有以下实际应用场景

- UA 判断是否移动端，据此返回移动端网站或者PC网站
- UA 判断是否搜索引擎爬虫，据此返回是否经 SEO 优化好的内容，比如 [prerender](https://github.com/prerender/prerender)
- UA 判断是否浏览器环境，据此返回不同内容

试举一例，比如 <https://ifconfig.me> 用于返回请求端的公网 IP 地址，通过 curl 与浏览器访问，完全是不同的页面。

```Bash
# 判断 UA 是否浏览器环境，如果是，返回 html 页面，这与直接打开该网址效果相同

$ curl https://ifconfig.me -H "User-Agent: chrome"



# 如果不是浏览器环境，直接返回 IP 地址

$ curl https://ifconfig.me

171.221.136.154
```

## Referer

> `Referer` 的正确拼法应该是 `Referrer`，但刚开始拼错，后来一直都没改。

`Referer` 请求头指当前请求页面的来源地址。

### 防防盗链

那如何防止防盗链呢？

既然防盗链的原理是判断 `Referer` 请求头，那岂不是不发既可以了？

确实如此，并且浏览器可以通过 `Referrer-Policy` 响应头控制是否发送 `Referer` 请求头。

```Bash
# 不发送 referer 请求头

Referrer-Policy: no-referrer
```

也可以将它置于 HTML 中

```HTML
<meta name="referrer" content="origin" />
<meta name="referrer" content="no-referrer" />
```

在山月的工具网站 [MDTU](https://markdown.devtool.tech/app) 中便通过 `no-referrer` 策略来避免防盗链，你可以将某个防盗链的图片使用 Markdown 格式添加至该工具编辑器中，发现任何防盗链图片都可以正常显示。

# 缓存

## 强缓存

强制缓存（又称为浏览器缓存或 HTTP 缓存）是 Web 技术的一部分，用于提升 Web 应用程序的性能。通过缓存机制，浏览器可以存储一部分资源（如 HTML 页面、图像、CSS 文件、JavaScript 文件等），以减少向服务器发送重复的请求，从而加快页面加载速度，减轻服务器负担。

强制缓存主要通过 HTTP 头部中的缓存控制字段来实现，以下是关键的 HTTP 头字段及其作用：

1. **Expires**：
   - 这个头字段指定资源的过期时间，即在此时间之前，浏览器可以直接使用缓存，而不必向服务器发送请求。
   - 例子：`Expires: Wed, 21 Oct 2021 07:28:00 GMT`
2. **Cache-Control**：
   - 这是一个更现代、更灵活的缓存控制机制，通过一系列指令来控制缓存行为。
   - 常见指令：
     - `max-age=<seconds>`：资源在 `<seconds>` 秒内有效。
     - `no-cache`：每次使用资源前都必须向服务器验证。
     - `no-store`：资源不应被缓存。
     - `public`：资源可以被任何缓存存储。
     - `private`：资源只能被用户的浏览器缓存。
   - 例子：`Cache-Control: max-age=3600, public`

### 强制缓存的工作流程

1. 浏览器第一次请求资源时，服务器返回资源并带有缓存控制头部。
2. 浏览器根据这些头部决定缓存资源及缓存多长时间。
3. 在缓存有效期内，浏览器直接从缓存中取资源，而不与服务器通信。
4. 缓存过期后，浏览器会向服务器验证资源是否更新。如果资源没有更新，服务器会返回 `304 Not Modified` 状态，浏览器继续使用缓存资源。

### 强制缓存示例

服务器响应头：

```
arduino
复制代码
HTTP/1.1 200 OK
Cache-Control: max-age=3600
ETag: "abc123"
```

浏览器后续请求：

```
sql
复制代码
GET /resource HTTP/1.1
If-None-Match: "abc123"
```

如果资源未变，服务器响应：

```
mathematica
复制代码
HTTP/1.1 304 Not Modified
```

这种机制显著提升了 Web 应用的性能，减少了带宽消耗和服务器压力，同时提供了版本控制和缓存更新的能力。

## 协商缓存

再次请求时，需要向服务器校验新鲜度，如果资源是新鲜的，返回 304，从浏览器获取资源

1. **ETag**：
   - 实体标签（Entity Tag），用于资源的版本控制。服务器会生成一个唯一的标识符（通常是资源内容的哈希值），每次资源变化时标识符也会变化。
   - 例子：`ETag: "123456"`
2. **Last-Modified**：
   - 表示资源的最后修改时间。浏览器可以通过 `If-Modified-Since` 请求头来询问服务器资源是否自该时间之后被修改过。
   - 例子：`Last-Modified: Wed, 21 Oct 2020 07:28:00 GMT`
3. **Pragma**：
   - 这是一个较旧的 HTTP 1.0 头字段，用于控制缓存行为。
   - 常用值：`Pragma: no-cache`（效果类似于 `Cache-Control: no-cache`）

- `Last-Modified`/`If-Modified-Since`，匹配 Response Header 的 `Last-Modified` 与 Request Header 的 `If-Modified-Since` 是否一致
- `Etag`/`If-None-Match`，匹配 Response Header 的 `Etag` 与 Request Header 的 `If-None-Match` 是否一致

-----

要验证某个网站资源是否启用了强制缓存，可以通过以下几种方法：

### 使用浏览器开发者工具

1. **打开开发者工具**：
   - 在大多数浏览器中（如 Chrome、Firefox），按 `F12` 或 `Ctrl+Shift+I` 打开开发者工具。
2. **访问网络（Network）面板**：
   - 在开发者工具中，找到并点击“Network”标签。
3. **加载资源**：
   - 访问你想要检查的页面并刷新，确保资源被加载。
4. **检查资源请求**：
   - 在“Network”面板中，找到你要检查的资源。点击资源查看详细信息。
5. **查看响应头**：
   - 在资源详细信息的“Headers”标签中，查看服务器返回的响应头信息。查找 `Cache-Control`、`Expires`、`ETag`、`Last-Modified` 等字段。

### 示例：

假设你在检查某个 CSS 文件 `styles.css`，以下是可能的响应头信息及其解释：

#### 响应头示例

```
HTTP/1.1 200 OK
Date: Tue, 04 Jun 2024 12:00:00 GMT
Cache-Control: max-age=3600, public
Expires: Tue, 04 Jun 2024 13:00:00 GMT
ETag: "abcdef123456"
Last-Modified: Mon, 03 Jun 2024 12:00:00 GMT
Content-Type: text/css
```

- `Cache-Control: max-age=3600, public`：表示该资源可以被缓存 3600 秒（1 小时）。
- `Expires: Tue, 04 Jun 2024 13:00:00 GMT`：指定资源的过期时间。
- `ETag: "abcdef123456"`：资源的唯一标识符，用于版本控制。
- `Last-Modified: Mon, 03 Jun 2024 12:00:00 GMT`：资源的最后修改时间。

### 使用命令行工具

1. **使用 `curl`**：

   - `curl` 是一个命令行工具，可以用来查看 HTTP 请求和响应头信息。

   - 运行以下命令以获取响应头：

     ```
     sh
     复制代码
     curl -I https://example.com/path/to/resource
     ```

   - 例如：

     ```
     sh
     复制代码
     curl -I https://example.com/styles.css
     ```

   - 输出示例：

     ```
     yaml
     复制代码
     HTTP/1.1 200 OK
     Date: Tue, 04 Jun 2024 12:00:00 GMT
     Cache-Control: max-age=3600, public
     Expires: Tue, 04 Jun 2024 13:00:00 GMT
     ETag: "abcdef123456"
     Last-Modified: Mon, 03 Jun 2024 12:00:00 GMT
     Content-Type: text/css
     ```

2. **使用 `wget`**：

   - `wget` 也是一个命令行工具，可以获取 HTTP 请求和响应头信息。

   - 运行以下命令以获取响应头：

     ```
     wget --server-response --spider https://example.com/path/to/resource
     ```
     
   - 例如：

     ```
     wget --server-response --spider https://example.com/styles.css
     ```
     
   - 输出示例：
   
     ```
     Spider mode enabled. Check if remote file exists.
     --2024-06-04 12:00:00--  https://example.com/styles.css
     Resolving example.com (example.com)... 93.184.216.34
     Connecting to example.com (example.com)|93.184.216.34|:443... connected.
     HTTP request sent, awaiting response...
       HTTP/1.1 200 OK
       Date: Tue, 04 Jun 2024 12:00:00 GMT
       Cache-Control: max-age=3600, public
       Expires: Tue, 04 Jun 2024 13:00:00 GMT
       ETag: "abcdef123456"
       Last-Modified: Mon, 03 Jun 2024 12:00:00 GMT
       Content-Type: text/css
     ```

### 结论

通过浏览器开发者工具和命令行工具（如 `curl` 和 `wget`），你可以轻松地检查某个网站资源的缓存设置，确认是否启用了强制缓存及其具体配置。

### 协商缓存如何校验新鲜度

协商缓存（Conditional Caching）是HTTP协议中的一种缓存机制，它允许客户端和服务器之间协商以确定缓存内容的有效性和新鲜度。这种机制可以减少不必要的数据传输，提高网络性能。协商缓存主要使用以下两种HTTP头来校验缓存的新鲜度：

1. **ETag（实体标签，Entity Tag）**：
   - **ETag 头**：服务器为每个资源生成一个唯一的标识符（ETag），并在响应头中返回。例如：`ETag: "abc123"`.
   - **If-None-Match 头**：客户端在后续请求中将之前获取到的ETag值通过这个头发送给服务器。例如：`If-None-Match: "abc123"`.
   - **服务器行为**：服务器检查客户端发送的ETag值是否与当前资源的ETag匹配。如果匹配，则表示资源未改变，服务器返回HTTP 304 Not Modified响应；如果不匹配，服务器返回新的资源和新的ETag。
2. **Last-Modified 和 If-Modified-Since**：
   - **Last-Modified 头**：服务器在响应头中返回资源的最后修改时间。例如：`Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT`.
   - **If-Modified-Since 头**：客户端在后续请求中将之前获取到的最后修改时间通过这个头发送给服务器。例如：`If-Modified-Since: Wed, 21 Oct 2015 07:28:00 GMT`.
   - **服务器行为**：服务器检查客户端发送的时间戳是否与当前资源的最后修改时间一致。如果一致，则表示资源未改变，服务器返回HTTP 304 Not Modified响应；如果不一致，服务器返回新的资源和新的Last-Modified时间。

#### 工作流程

1. **初始请求**：
   - 客户端请求资源。
   - 服务器返回资源，同时附带ETag和Last-Modified头。
2. **后续请求**：
   - 客户端再次请求相同资源时，带上If-None-Match和/或If-Modified-Since头。
   - 服务器根据头信息检查资源是否有更新。

#### 例子

1. **初次请求**：

   ```
   yaml
   复制代码
   GET /resource HTTP/1.1
   Host: example.com
   
   HTTP/1.1 200 OK
   ETag: "abc123"
   Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT
   Content-Type: application/json
   Content-Length: 1234
   
   { ... JSON data ... }
   ```

2. **后续请求**：

   ```
   mathematica
   复制代码
   GET /resource HTTP/1.1
   Host: example.com
   If-None-Match: "abc123"
   If-Modified-Since: Wed, 21 Oct 2015 07:28:00 GMT
   
   HTTP/1.1 304 Not Modified
   ```

通过这种方式，协商缓存可以有效减少带宽消耗和服务器负载，同时确保客户端获取到最新的资源。
