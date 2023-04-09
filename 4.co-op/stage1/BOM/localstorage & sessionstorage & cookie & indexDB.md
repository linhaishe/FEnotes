# localstorage & sessionstorage & cookie & indexDB

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

Cookie options:

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

# localstorage & sessionstorage & cookie & indexDB



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