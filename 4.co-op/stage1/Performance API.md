# Performance API

Performance API（性能API）是一种Web API，它允许开发人员测量和分析Web应用程序的性能，例如加载时间、响应时间、资源使用情况等等。它是现代浏览器提供的Web平台API的一部分。


## Performance API 概述

### 1. Performance 对象

> window.performance 是W3C性能小组引入的新的API，目前IE9以上的浏览器都支持。

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230403214549741.png" style="zoom:50%;" />

一个performance对象的完整结构包括：

1. memory字段代表JavaScript对内存的占用。
2. navigation字段统计的是一些网页导航相关的数据：
3. redirectCount:重定向的数量（只读），但是这个接口有同源策略限制，即仅能检测同源的重定向；
4. type 返回值应该是0,1,2 中的一个。分别对应三个枚举值:
   - 0 : TYPE_NAVIGATE (用户通过常规导航方式访问页面，比如点一个链接，或者一般的get方式)
   - 1 : TYPE_RELOAD (用户通过刷新，包括JS调用刷新接口等方式访问页面)
   - 2 : TYPE_BACK_FORWARD (用户通过后退按钮访问本页面) 最重要的是timing字段的统计数据，它包含了网络、解析等一系列的时间数据。

### 2. performance.timing 对象

#### 简介

它提供了关于页面加载和渲染时间的详细信息。它包含了与页面生命周期相关的各种时间戳，这些时间戳可以用来测量页面加载的各个阶段以及用户体验。

> 🚮**已弃用:** 不再推荐使用该特性。虽然一些浏览器仍然支持它，但也许已从相关的 web 标准中移除，也许正准备移除或出于兼容性而保留。请尽量不要使用该特性，并更新现有的代码；

> ⚠️**警告：** 该属性在 [Navigation Timing Level 2 specification](https://w3c.github.io/navigation-timing/#obsolete) 中已经被废弃，请使用 [`PerformanceNavigationTiming`](https://developer.mozilla.org/zh-CN/docs/Web/API/PerformanceNavigationTiming) 替代。

`PerformanceTiming` 被废弃了，它的替代对象是 `PerformanceEntry` 和 `PerformanceResourceTiming` 接口。这两个接口提供了与 `PerformanceTiming` 相似的信息，但使用更加灵活和标准化。

- `PerformanceEntry` 接口提供了许多与性能相关的数据，如启动时间、结束时间、持续时间和名称等。
- `PerformanceResourceTiming` 接口继承自 `PerformanceEntry` 接口，提供了更多关于网络资源请求和响应的信息，如 DNS 查询、TCP 连接、SSL/TLS 握手、HTTP 请求和响应等。

这些新的接口提供了更加准确和可靠的性能信息，同时支持跨平台和跨浏览器的使用。

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406002139242.png" alt="image-20230406002139242" style="zoom:50%;" />

------

#### timing的整体结构

| 属性名                       | 描述                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| `startTime`                  | 有些浏览器实现为`navigationStart`。该属性返回浏览器开始导航的时间戳，通常是用户输入网址或点击链接的时间。如果当前文档为空，则`navigationStart`的值等于`fetchStart`。 |
| `redirectStart`              | 如果页面是由`redirect`而来，则代表`redirect`开始的时间节点   |
| `redirectEnd`                | 如果页面是由`redirect`而来，则代表`redirect`结束的时间节点   |
| `unloadEventStart`           | 如果前一个文档和请求的文档是同一个域的，则代表浏览器`unload`前一个文档的开始时间节点。否则为0 |
| `unloadEventEnd`             | 如果前一个文档和请求的文档是同一个域的，则代表浏览器`unload`前一个文档的结束时间节点。否则为0 |
| `fetchStart`                 | 在浏览器发起任何请求之前的时间值，包括检查缓存等操作         |
| `domainLookupStart`          | DNS查询开始的时间节点，如果浏览器没有进行DNS查询（比如使用了cache），则值等于`fetchStart` |
| `domainLookupEnd`            | DNS查询结束的时间节点，如果浏览器没有进行DNS查询（比如使用了cache），则值等于`fetchStart` |
| `connectStart`               | TCP建立连接开始的时间节点，如果浏览器没有进行TCP连接（比如使用持久化连接`webscoket`），则值等于`domainLookupEnd` |
| `connectEnd`                 | TCP建立连接成功的时间节点，如果浏览器没有进行TCP连接（比如使用持久化连接`webscoket`），则值等于`domainLookupEnd` |
| `secureConnectionStart`      | 可选。如果页面使用HTTPS，它的值是安全连接握手之前的时刻。如果该属性不可用，则返回`undefined`。如果该属性可用，但没有使用HTTPS，则返回0 |
| `requestStart`               | 浏览器发起请求的时间节点，包括请求服务器、缓存、本地资源等   |
| `responseStart`              | 浏览器收到从服务器端（或缓存、本地资源）响应回的第一个字节数据的时刻 |
| `responseEnd`                | 浏览器收到从服务器端（或缓存、本地资源）响应回的最后一个字节数据的时刻 |
| `domLoading`                 | 浏览器开始解析HTML文档的时间节点                             |
| `domInteractive`             | HTML文档解析完成且内嵌资源还未加载的时间节点                 |
| `domContentLoadedEventStart` | `DOMContentLoaded`事件开始的时间节点                         |
| `domContentLoadedEventEnd`   | `DOMContentLoaded`事件结束的时间节点                         |
| `domComplete`                | HTML文档解析完毕的时间节点                                   |

---------

#### 使用注意⚠️

| 问题           | 解决方案                                                     |
| -------------- | ------------------------------------------------------------ |
| 浏览器兼容性   | 先检查浏览器是否支持 `performance.timing` 接口，同时需要对不同浏览器进行特别处理 |
| 受其他因素影响 | 通过计算的时间戳之差得出的只是一个近似值，可能存在误差，需要考虑页面加载时间受到很多因素的影响，如网络速度、服务器响应时间、缓存情况等等 |
| DOM操作        | 计算 `loadEventEnd` 和 `navigationStart` 的时间戳之差并不包括DOM操作时间，需要考虑这部分时间对页面加载时间的影响，并在计算时进行排除 |
| 避免阻塞       | 在测量页面加载时间时，应该尽可能避免阻塞其他操作，可以使用异步加载等技术来减少阻塞时间 |
| 慎用同步获取   | 在获取 `performance.timing` 的数据时，需要注意这些数据可能是异步获取的，需要使用异步的方式获取 `performance.timing` 的数据 |

### 3. PerformanceEntry 对象

在 Performance API 中，`PerformanceEntry` 对象代表了一个性能条目，它包含了有关某个特定的测量对象（如页面、资源、事件等）的信息。

`PerformanceEntry` 对象本身只是一个用于描述某个性能条目（如资源加载、页面导航等）的数据结构，它存储了该性能条目的各项性能数据，但是并没有提供实际的性能分析工具或方法。因此，`PerformanceEntry` 对象仅仅是一个中间数据格式，不能单独使用。我们通常需要将收集到的 `PerformanceEntry` 对象传递给其他性能分析工具，如 `PerformanceObserver` 或其他第三方性能监测库，才可以对其进行进一步处理和优化。

每个 `PerformanceEntry` 对象都包含了以下共同属性：

- `name`：表示该条目的名称；
- `entryType`：表示该条目的类型，通常是一个字符串，例如 "navigation"、"resource" 或 "measure"；
- `startTime`：表示该条目的起始时间戳；
- `duration`：表示该条目持续的时间。

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230405170548099.png" alt="image-20230405170548099" style="zoom: 50%;" />

```ts
[Exposed=(Window,Worker)]
interface PerformanceEntry {
  readonly    attribute DOMString           name;
  readonly    attribute DOMString           entryType;
  readonly    attribute DOMHighResTimeStamp startTime;
  readonly    attribute DOMHighResTimeStamp duration;
  [Default] object toJSON();
};
```

基于不同的类型，`PerformanceEntry` 对象还可能包含其他特定的属性。例如，对于 `Resource Timing` 来说，`PerformanceEntry` 对象包括了以下额外的属性：

- `initiatorType`：表示发起该资源请求的类型，例如 "img"、"script" 等；
- `nextHopProtocol`：表示该资源的传输协议，例如 "http/1.1"、"h2" 等；
- `encodedBodySize`：表示该资源的编码后大小；
- `decodedBodySize`：表示该资源的解码后大小；
- `transferSize`：表示该资源的传输大小。

以下仅列举了常见的性能指标类型及其对应的属性，实际上还有一些其他的指标类型和属性，可以根据实际需求来选择使用。

| 条目类型                   | 描述                                                         | 属性                                                         |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `frame`                    | 页面中每个 iframe 的性能数据                                 | `name`, `entryType`, `startTime`, `duration`, `id`, `domContentLoadedEventStart`, `domContentLoadedEventEnd` |
| `navigation`               | 浏览器的页面导航数据                                         | `name`, `entryType`, `startTime`, `duration`, `navigationStart`, `fetchStart`, `domainLookupStart` |
| `resource`                 | 加载页面中所有资源的性能数据                                 | `name`, `entryType`, `startTime`, `duration`, `initiatorType`, `nextHopProtocol`, `transferSize` |
| `measure`                  | 自定义性能计算                                               | `name`, `entryType`, `startTime`, `duration`                 |
| `mark`                     | 标记点，用于标记某个时间点                                   | `name`, `entryType`, `startTime`                             |
| `paint`                    | 页面中的重要渲染事件，如 `first-paint` 和 `first-contentful-paint` | `name`, `entryType`, `startTime`, `duration`                 |
| `longtask`                 | 页面中的长任务数据，通常表示执行时间超过 50 毫秒的任务       | `name`, `entryType`, `startTime`, `duration`, `attribution`, `entry` |
| `first-input`              | 表示首次输入延迟 (First Input Delay, FID)。它度量从用户首次与页面交互（例如，点击链接、按钮等）到浏览器实际响应该事件之间的时间差。 | `name`,`startTime`,`duration`,`processingStart`,`target`<br />,`cancelable`,`composed`,`startTimeStamp` |
| `largest-contentful-paint` | 表示最大内容渲染时间 (Largest Contentful Paint, LCP)。它度量从页面开始加载到最大的文本块或图像元素被渲染出来的时间。 | `name`<br>`startTime`<br>`duration`<br>`element`<br>`url`<br>`hadRecentInput` |
| `layout-shift`             | 表示布局位移 (Layout Shift)。它度量页面在加载期间发生的突然布局位移的数量和严重程度。 | `name`<br>`startTime`<br>`value`<br>`hadRecentInput`<br>`sources` |
| `element`                  | 表示指定元素的性能度量。可以使用 `Performance.mark()` 和 `Performance.measure()` 方法在代码中手动记录该元素的度量。 | `name`<br>`startTime`<br>`duration`<br>`element`<br>`entryTypes` |

```js
// 可以使用 PerformanceObserver 来监控指定类型的 PerformanceEntry 对象
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  // 对不同类型的性能指标进行处理
  entries.forEach((entry) => {
    if (entry.entryType === 'navigation') {
      // 处理导航性能指标
    } else if (entry.entryType === 'resource') {
      // 处理资源性能指标
    } else if (entry.entryType === 'paint') {
      // 处理绘制性能指标
    } else if (entry.entryType === 'mark') {
      // 处理标记性能指标
    } else if (entry.entryType === 'measure') {
      // 处理时间段性能指标
    } else if (entry.entryType === 'userTiming') {
      // 处理用户自定义性能指标
    } else if (entry.entryType === 'longtask') {
      // 处理长任务性能指标
    }
  });
});

// 监听 longtask 和 resource 类型的性能指标
observer.observe({
  entryTypes: ["longtask", "resource"],
  bufferred: true
});
```

```js
// 使用performance.getEntriesByType来获取每种 entryType 的 PerformanceEntry 对象数组
const markEntries = performance.getEntriesByType("mark");
const measureEntries = performance.getEntriesByType("measure");
const navigationEntries = performance.getEntriesByType("navigation");
const resourceEntries = performance.getEntriesByType("resource");
const longtaskEntries = performance.getEntriesByType("longtask
```

https://www.w3.org/wiki/Web_Performance/EntryType

https://www.w3.org/TR/paint-timing/#performancepainttiming

https://developer.mozilla.org/zh-CN/docs/Web/API/PerformanceEntry

### 4. `PerformanceResourceTiming` 接口

可通过 `window.performance.getEntriesByType("resource")`获取

`PerformanceResourceTiming` 是一个接口，它继承自 `PerformanceEntry`，用于描述一个资源的时间性能信息，例如：CSS，JavaScript，图片，音频或视频等。

当资源加载完成时，浏览器会自动创建一个 `PerformanceResourceTiming` 对象，并将其添加到 `performance.getEntries()` 中。该对象包含了资源加载的性能指标，例如响应时间、DNS解析时间、TCP连接时间、SSL握手时间、HTTP请求时间、HTTP响应时间、数据传输时间等。

开发人员可以通过 `PerformanceResourceTiming` 接口的各种属性和方法，对资源的性能进行分析和优化，例如计算资源加载时间，查看DNS解析时间，分析网络传输性能等。

`PerformanceResourceTiming` 还继承了 `PerformanceEntry` 接口的属性，如 `name`、`entryType`、`startTime` 和 `duration` 等。

| 属性名                | 类型                  | 描述                                                   |
| --------------------- | --------------------- | ------------------------------------------------------ |
| connectEnd            | `DOMHighResTimeStamp` | 最后一个 HTTP 响应包被接收到的时间                     |
| connectStart          | `DOMHighResTimeStamp` | 开始建立连接请求的时间                                 |
| decodedBodySize       | `number`              | 已接收的响应体的大小（单位：字节），不包括响应头的大小 |
| domainLookupEnd       | `DOMHighResTimeStamp` | DNS 查询结束时间                                       |
| domainLookupStart     | `DOMHighResTimeStamp` | DNS 查询开始时间                                       |
| duration              | `DOMHighResTimeStamp` | 完成网络请求所花费的时间                               |
| encodedBodySize       | `number`              | 响应体的大小（单位：字节），包括响应头的大小           |
| entryType             | `string`              | 条目类型，值为 "resource"                              |
| fetchStart            | `DOMHighResTimeStamp` | 开始发起网络请求的时间                                 |
| initiatorType         | `string`              | 发起请求的类型，比如 "img" 或 "script"                 |
| name                  | `string`              | 请求的 URL                                             |
| nextHopProtocol       | `string`              | 采用的网络协议                                         |
| redirectEnd           | `DOMHighResTimeStamp` | 最后一个重定向结束时间                                 |
| redirectStart         | `DOMHighResTimeStamp` | 第一个重定向开始时间                                   |
| requestStart          | `DOMHighResTimeStamp` | 开始发送请求的时间                                     |
| responseEnd           | `DOMHighResTimeStamp` | 接收到最后一个响应字节的时间                           |
| responseStart         | `DOMHighResTimeStamp` | 接收到第一个响应字节的时间                             |
| secureConnectionStart | `DOMHighResTimeStamp` | 安全连接开始时间                                       |
| serverTiming          | `object`              | 响应头中的 Server-Timing 信息                          |
| startTime             | `DOMHighResTimeStamp` | PerformanceResourceTiming 对象的创建时间               |
| transferSize          | `number`              | 在网络上发送的数据量（单位：字节），包括响应头的大小   |
| workerStart           | `DOMHighResTimeStamp` | Service Worker 开始处理请求的时间                      |

### 5. PerformanceNavigationTiming 接口

![image-20230406000306587](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406000306587.png)

![image-20230405233719216](/Users/chenruo/Library/Application Support/typora-user-images/image-20230405233719216.png)

`PerformanceNavigationTiming` 接口确实同时继承了 `PerformanceResourceTiming` 接口和 `PerformanceEntry` 接口的所有属性和方法。

`PerformanceResourceTiming` 接口和 `PerformanceNavigationTiming` 接口都是 `PerformanceEntry` 接口的子接口。

`PerformanceResourceTiming` 接口记录了单个资源的加载时间信息，包括了发出资源请求的开始时间、接收到资源响应的时间、开始下载资源的时间、下载资源结束的时间等。

而 `PerformanceNavigationTiming` 接口则记录了整个页面导航的时间信息，包括了页面开始导航的时间、重定向的时间、DNS 查询的时间、建立连接的时间、发送请求和接收响应的时间、解析 DOM 的时间等。

`PerformanceNavigationTiming` 对象是通过 `performance.getEntriesByType('navigation')` 方法获取的。

`PerformanceNavigationTiming` 接口提供了以下属性：

通过这些属性，您可以获得有关页面导航过程的详细信息，例如 DNS 查询、TCP 连接、SSL/TLS 握手、HTTP 请求和响应、DOM 解析和渲染等过程的时间戳。这些信息可以用于分析和优化页面性能。

| 属性名                       | 描述                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| `navigationStart`            | 页面的初始导航开始时间                                       |
| `unloadEventStart`           | 页面卸载事件的开始时间，表示上一个页面的卸载时间             |
| `unloadEventEnd`             | 页面卸载事件的结束时间，表示上一个页面的卸载时间             |
| `redirectStart`              | 重定向事件的开始时间，表示页面进行重定向的时间               |
| `redirectEnd`                | 重定向事件的结束时间，表示页面进行重定向的时间               |
| `fetchStart`                 | 浏览器开始检索页面的时间                                     |
| `domainLookupStart`          | DNS 解析的开始时间                                           |
| `domainLookupEnd`            | DNS 解析的结束时间                                           |
| `connectStart`               | HTTP 连接建立的开始时间                                      |
| `connectEnd`                 | HTTP 连接建立的结束时间                                      |
| `secureConnectionStart`      | HTTPS 连接建立的开始时间                                     |
| `requestStart`               | 发送请求的时间                                               |
| `responseStart`              | 接收响应的开始时间                                           |
| `responseEnd`                | 接收响应的结束时间                                           |
| `domLoading`                 | 页面开始加载到 DOM 开始加载的时间                            |
| `domInteractive`             | DOM 解析完成的时间                                           |
| `domContentLoadedEventStart` | DOMContentLoaded 事件的开始时间                              |
| `domContentLoadedEventEnd`   | DOMContentLoaded 事件的结束时间                              |
| `domComplete`                | 页面开始加载到 DOM 加载完成的时间                            |
| `loadEventStart`             | load 事件的开始时间，表示页面完成加载的时间                  |
| `loadEventEnd`               | load 事件的结束时间，表示页面完成加载的时间                  |
| `type`                       | 页面的类型，可以是 `navigate`（初始导航）、`reload`（刷新）、`back_forward`（前进/后退）等 |
| `redirectCount`              | 页面进行重定向的次数                                         |

### 6. PerformanceObserver 对象

`PerformanceObserver` 是一个用于监听和收集 Web 应用程序性能数据的接口，它提供了一种简单但有效的方法来获取各种性能条目的详细信息，并在指定条件满足时发送通知。通过 `PerformanceObserver` 接口，我们可以实时监测应用程序的性能表现，并对其进行分析和优化。

`PerformanceObserver` 接口提供了以下几个重要的方法：

- `PerformanceObserver.observe()`: 用于启动 `PerformanceObserver` 实例，并设置它要监听的指定类型的性能条目。该方法接受一个配置对象作为参数，其中包括要监听的性能条目类型、回调函数等。
- `PerformanceObserver.disconnect()`: 用于停止 `PerformanceObserver` 实例的监听操作，并释放其中的资源。
- `PerformanceObserver.takeRecords()`: 用于获取当前已经被收集到的所有性能条目，并清空原有的记录缓存。该方法返回一个 `PerformanceEntryList` 对象，其中包含所有被收集到的性能条目。

#### PerformanceObserver.observe()

https://codepen.io/linhaishe/pen/MWqNQOJ?editors=0111

PerformanceObserver.observe() 用于开始观察性能。使用该方法创建一个 PerformanceObserver 对象，并指定一个或多个 entryTypes（如measure、mark、navigation等）以监听相关的性能事件。当性能事件被触发时，相应的性能条目将被添加到浏览器的性能缓冲区中，以便稍后进行处理。这个方法需要传递一个回调函数，用于处理从性能缓冲区中获取的条目。在回调函数中，可以使用 PerformanceObserverEntryList 对象的 getEntries() 方法获取所有的性能条目。

PerformanceObserver.takeRecords() 方法用于获取 PerformanceObserver 监听的性能条目。当调用该方法时，所有已存储的条目将从性能缓冲区中移除，并返回一个包含这些条目的 PerformanceEntry 对象数组。这个方法不需要传递回调函数，因为它只是返回已缓存的性能条目。

因此，PerformanceObserver.observe() 方法用于开始监听性能事件并收集性能条目，而 PerformanceObserver.takeRecords() 方法用于获取已经存储的性能条目并进行处理。

```js
const observer = new PerformanceObserver((list) => {
  console.log(list.getEntries());
});

observer.observe({ entryTypes: ['mark', 'measure'] });
```

```jsx
// PerformanceObserver.observe()

import { useState, useEffect } from 'react';

function usePerformanceObserver(entryType) {
  const [performanceEntries, setPerformanceEntries] = useState([]);

  useEffect(() => {
    const observer = new PerformanceObserver((list) => {
      setPerformanceEntries(list.getEntries());
    });

    observer.observe({ entryTypes: [entryType] });

    return () => observer.disconnect();
  }, [entryType]);

  return performanceEntries;
}

function App() {
  const performanceEntries = usePerformanceObserver('measure');

  useEffect(() => {
    // 在代码中执行一些操作，例如计算函数的执行时间
    function myFunction() {
      console.time('myFunction');
      // 代码
      console.timeEnd('myFunction');
    }

    myFunction();
  }, []);

  return (
    <div>
      <h1>Performance Entries:</h1>
      <ul>
        {performanceEntries.map((entry, index) => (
          <li key={index}>
            {entry.name} took {entry.duration}ms to complete.
          </li>
        ))}
      </ul>
    </div>
  );
}

```

在这个例子中，我们首先定义了一个自定义的 usePerformanceObserver 钩子，该钩子使用 PerformanceObserver 来监听 measure 类型的性能事件，并返回一个包含所有性能条目的状态。在 App 组件中，我们使用该钩子来获取 measure 类型的性能条目，并将它们呈现在页面上。

我们还在 App 组件的 useEffect 钩子中执行了一个名为 myFunction 的函数，该函数使用 console.time() 和 console.timeEnd() 来测量代码的执行时间，并在浏览器的性能缓冲区中生成一个名为 "myFunction" 的性能条目。PerformanceObserver 将监听此条目，并在条目被添加到性能缓冲区时更新状态，并在页面上呈现性能条目。

注意，我们在 useEffect 的依赖项数组中传递了一个空数组，以确保 myFunction 函数只会在组件挂载时执行一次，而不是在每次重新渲染时都执行。这可以确保我们只会测量一次代码的执行时间，并避免在每次重新渲染时重复添加相同的性能条目。

#### PerformanceObserver.takeRecords()

https://codepen.io/linhaishe/pen/xxyKzaP?editors=0011

在这个示例中，我们定义了一个名为 usePerformanceObserver 的自定义钩子，该钩子使用 PerformanceObserver 来监听 measure 类型的性能事件。我们使用两个 useEffect 钩子来同时使用 PerformanceObserver.observe() 和 PerformanceObserver.takeRecords() 方法：

- 第一个 useEffect 钩子用于创建 PerformanceObserver 并开始监听性能事件，这与前一个示例中的 usePerformanceObserver 钩子相同。
- 第二个 useEffect 钩子用于定期从性能缓冲区中获取已存储的条目，并将它们添加到状态中。这个例子中我们每5秒执行一次，可以根据需要进行调整。

在 App 组件中，我们使用 usePerformanceObserver 钩子来获取所有 measure 类型的性能条目，并将它们呈现在页面上。我们还在 useEffect 钩子中执行了一个名为 myFunction 的函数，该函数使用 console.time() 和 console.timeEnd() 来测量代码的执行时间，并在浏览器的性能缓冲区中生成一个名为 "myFunction" 的性能条目。PerformanceObserver 将监听此条目，并在每次 PerformanceObserver.takeRecords() 方法被调用时，将其添加到已存储的性能条目中。

我们需要在第二个 useEffect 钩子中访问 PerformanceObserver.takeRecords() 方法，因此我们将 PerformanceObserver 对象保存在状态中并传递给 useEffect 的依赖项数组中。这样做可以确保我们在每次重新渲染时都使用相同

`useEffect` 钩子中调用了一个 `myFunction` 函数，该函数使用 `console.time()` 和 `console.timeEnd()` 记录了函数执行的时间，并使用 `performance.measure()` 创建了一个自定义测量点。`usePerformanceObserver()` 钩子在这个测量点完成后会触发，并将这个测量点的信息添加到 `performanceEntries` 中

 `myFunction()` 函数将创建两个标记 `start-myFunction` 和 `end-myFunction`，并使用这两个标记来创建测量点 `myFunction`。`usePerformanceObserver()` 钩子会在这个测量点完成后触发，并将测量点信息添加到 `performanceEntries` 中

```js
// 创建一个新的 PerformanceObserver 对象
const observer = new PerformanceObserver((list) => {
  // 获取所有的性能条目
  const entries = list.getEntries();
  
  // 处理每个条目
  entries.forEach((entry) => {
    console.log(`${entry.name} took ${entry.duration}ms to complete.`);
  });
});

// 开始观察性能
observer.observe({ entryTypes: ['measure'] });

// 在代码中执行一些操作，例如计算函数的执行时间
function myFunction() {
  console.time('myFunction');
  // 代码
  console.timeEnd('myFunction');
}

myFunction();

// 获取性能条目并输出结果
const entries = observer.takeRecords();
entries.forEach((entry) => {
  console.log(`${entry.name} took ${entry.duration}ms to complete.`);
});
```

