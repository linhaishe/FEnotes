# Performance API

![image-20230408184929657](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230408184929657.png)

Performance API 包括 Performance Timeline API，它们一起构成了范围广泛的方法，可以获取有关网页性能的有用指标。

ref: https://css-tricks.com/breaking-performance-api/

## performance timeline

performance timeline API 可以让我们访问几乎所有来自整个performance API 的测量和值。这是一种使用单个 API 就能掌握大量信息的方式，这也是本文开头的图表将它们几乎显示在同一水平线上的原因。

浏览器的性能时间轴（Performance Timeline）是浏览器开发者工具的一部分，用于收集和展示网页的性能数据。它提供了一个交互式的时间轴，记录了网页的主要活动，包括DOM构建、CSS样式计算、JavaScript执行、网络请求和渲染等过程，以及这些活动在时间轴上的耗时。通过分析这些性能数据，开发者可以找到网页中的性能瓶颈，优化网页的性能，提升用户体验。浏览器的性能时间轴是开发者工具中非常实用的性能分析工具之一。

## Performance API 概述

The Performance API is a group of standards used to measure the performance of web applications.

Performance API（性能API）是一种Web API，它允许开发人员测量和分析Web应用程序的性能，例如加载时间、响应时间、资源使用情况等等。它是现代浏览器提供的Web平台API的一部分。

Each performance metric is represented by a single [`PerformanceEntry`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry). A performance entry has a `name`, a `duration`, a `startTime`, and a `type`. All performance metrics extend the `PerformanceEntry` interface and qualify it further.

### 1. Performance

#### info

Performance 接口可以获取到当前页面中与性能相关的信息。它是 High Resolution Time API 的一部分，同时也融合了 Performance Timeline API、Navigation Timing API、 User Timing API 和 Resource Timing API。

通过调用只读属性 `Window.performance` 来获得

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230403214549741.png" style="zoom: 50%;" />

一个performance对象的完整结构包括：

1. memory字段代表JavaScript对内存的占用。
2. navigation字段统计的是一些网页导航相关的数据：
3. redirectCount:重定向的数量（只读），但是这个接口有同源策略限制，即仅能检测同源的重定向；
4. type 返回值应该是0,1,2 中的一个。分别对应三个枚举值:
   - 0 : TYPE_NAVIGATE (用户通过常规导航方式访问页面，比如点一个链接，或者一般的get方式)
   - 1 : TYPE_RELOAD (用户通过刷新，包括JS调用刷新接口等方式访问页面)
   - 2 : TYPE_BACK_FORWARD (用户通过后退按钮访问本页面) 最重要的是timing字段的统计数据，它包含了网络、解析等一系列的时间数据。

#### Instance methods

`getEntriesByType()` , `getEntriesByName()`,  `getEntries()`

- 都是用于返回当前存在于给定类型的性能时间线中的 PerformanceEntry 对象数组
- 这三个方法根本不支持以下条目类型，即使可能存在这些类型的条目也不会返回
  - "element" (PerformanceElementTiming)
  - "event" (PerformanceEventTiming)
  - "largest-contentful-paint" (LargestContentfulPaint)
  - "layout-shift" (LayoutShift)
  - "longtask" (PerformanceLongTaskTiming)

```js
// 使用performance.getEntriesByType来获取每种 entryType 的 PerformanceEntry 对象数组
const markEntries = performance.getEntriesByType("mark");
const debugMarks = performance.getEntriesByName("debug-mark", "mark");
const entries = performance.getEntries();
```

### 2. PerformanceTiming

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

### 3. PerformanceEntry

#### Info

在 Performance API 中，`PerformanceEntry` 对象代表了一个性能条目，它包含了有关某个特定的测量对象（如页面、资源、事件等）的信息。

`PerformanceEntry` 对象本身只是一个用于描述某个性能条目（如资源加载、页面导航等）的数据结构，它存储了该性能条目的各项性能数据，但是并没有提供实际的性能分析工具或方法。因此，`PerformanceEntry` 对象仅仅是一个中间数据格式，不能单独使用。我们通常需要将收集到的 `PerformanceEntry` 对象传递给其他性能分析工具，如 `PerformanceObserver` 或其他第三方性能监测库，才可以对其进行进一步处理和优化。

PerformanceEntry 实例将始终是以下子类之一：

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406220610455.png" alt="image-20230406220610455" style="zoom: 33%;" />

#### entry type for each metric interface

| 指标                        | `entryType`                | 描述                                                         |                                                              |
| --------------------------- | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LargestContentfulPaint      | `largest-contentful-paint` | 网页加载过程中最大的可见元素的加载时间。                     |                                                              |
| LayoutShift                 | `layout-shift`             | 网页布局的稳定性，即网页内容在加载过程中是否出现了视觉上的位移。 |                                                              |
| PerformanceElementTiming    | `element`                  | 单个元素的性能信息，如元素的加载、解析和渲染等时间。         |                                                              |
| PerformanceEventTiming      | `event`                    | 事件的性能信息，如事件的处理时间和响应时间等。               |                                                              |
| PerformanceLongTaskTiming   | `longtask`                 | 长任务的性能信息，如 JavaScript 执行时间较长的任务等。       |                                                              |
| PerformanceMark             | `mark`                     | 时间戳标记，用于测量两个时间点之间的耗时。                   | User Timing API                                              |
| PerformanceMeasure          | `measure`                  | 时间测量标记，用于测量一个任务的耗时。                       |                                                              |
| PerformancePaintTiming      | `paint`                    | 网页的绘制时间，如首次绘制时间、首次有意义绘制时间等。       | First Paint (FP)<br />First Contentful Paint (FCP)<br />Largest Contentful Paint (LCP)<br />First Meaningful Paint (FMP) |
| PerformanceResourceTiming   | `resource`                 | 资源的性能信息，如资源的加载时间、大小、类型等。             |                                                              |
| PerformanceNavigationTiming | `navigation`               | 页面导航的性能信息，如 DNS 解析时间、TCP 连接时间、DOM 构建时间等。 |                                                              |
| TaskAttributionTiming       | `task`                     | 任务的性能信息，如任务的执行时间和归属信息等。               |                                                              |

<img src="https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406230528275.png" alt="image-20230406230528275" style="zoom:50%;" />

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

| 条目类型                   | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| `frame`                    | 页面中每个 iframe 的性能数据                                 |
| `navigation`               | 浏览器的页面导航数据                                         |
| `resource`                 | 加载页面中所有资源的性能数据                                 |
| `measure`                  | 自定义性能计算                                               |
| `mark`                     | 标记点，用于标记某个时间点                                   |
| `paint`                    | 页面中的重要渲染事件，如 `first-paint` 和 `first-contentful-paint` |
| `longtask`                 | 页面中的长任务数据，通常表示执行时间超过 50 毫秒的任务       |
| `first-input`              | 表示首次输入延迟 (First Input Delay, FID)。它度量从用户首次与页面交互（例如，点击链接、按钮等）到浏览器实际响应该事件之间的时间差。 |
| `largest-contentful-paint` | 表示最大内容渲染时间 (Largest Contentful Paint, LCP)。它度量从页面开始加载到最大的文本块或图像元素被渲染出来的时间。 |
| `layout-shift`             | 表示布局位移 (Layout Shift)。它度量页面在加载期间发生的突然布局位移的数量和严重程度。 |
| `element`                  | 表示指定元素的性能度量。可以使用 `Performance.mark()` 和 `Performance.measure()` 方法在代码中手动记录该元素的度量。 |

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

https://www.w3.org/wiki/Web_Performance/EntryType

https://www.w3.org/TR/paint-timing/#performancepainttiming

https://developer.mozilla.org/zh-CN/docs/Web/API/PerformanceEntry

### 4. PerformanceObserver

`PerformanceObserver` 是一个用于监听和收集 Web 应用程序性能数据的接口，它提供了一种简单但有效的方法来获取各种性能条目的详细信息，并在指定条件满足时发送通知。通过 `PerformanceObserver` 接口，我们可以实时监测应用程序的性能表现，并对其进行分析和优化。

The [`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver) interface enables you to listen for various types of performance entry as they are recorded.

`PerformanceObserver` 接口提供了以下几个重要的方法：

- `PerformanceObserver.observe()`: 用于启动 `PerformanceObserver` 实例，并设置它要监听的指定类型的性能条目。该方法接受一个配置对象作为参数，其中包括要监听的性能条目类型、回调函数等。
- `PerformanceObserver.disconnect()`: 用于停止 `PerformanceObserver` 实例的监听操作，并释放其中的资源。
- `PerformanceObserver.takeRecords()`: 用于获取当前已经被收集到的所有性能条目，并清空原有的记录缓存。该方法返回一个 `PerformanceEntryList` 对象，其中包含所有被收集到的性能条目。

#### PerformanceObserver.observe()

```js
// An object with the following possible members: buffered,durationThreshold,entryTypes,type
observe(options)
```

https://codepen.io/linhaishe/pen/MWqNQOJ?editors=0111

`PerformanceObserver.observe()` 用于开始观察性能。使用该方法创建一个 PerformanceObserver 对象，并指定一个或多个 entryTypes（如measure、mark、navigation等）以监听相关的性能事件。当性能事件被触发时，相应的性能条目将被添加到浏览器的性能缓冲区中，以便稍后进行处理。这个方法需要传递一个回调函数，用于处理从性能缓冲区中获取的条目。在回调函数中，可以使用 PerformanceObserverEntryList 对象的 `getEntries()` 方法获取所有的性能条目。

`PerformanceObserver.takeRecords() `方法用于获取 PerformanceObserver 监听的性能条目。当调用该方法时，所有已存储的条目将从性能缓冲区中移除，并返回一个包含这些条目的 PerformanceEntry 对象数组。这个方法不需要传递回调函数，因为它只是返回已缓存的性能条目。

`PerformanceObserver.observe()` 方法用于开始监听性能事件并收集性能条目，而` PerformanceObserver.takeRecords() `方法用于获取已经存储的性能条目并进行处理。

```js
const observer = new PerformanceObserver((list) => {
  console.log(list.getEntries());
});

observer.observe({ entryTypes: ['mark', 'measure'] });
```

```js
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1]; // Use the latest LCP candidate
  console.log("LCP:", lastEntry.startTime);
  console.log(lastEntry);
});
observer.observe({ type: "largest-contentful-paint", buffered: true });
```



#### PerformanceObserver.takeRecords()

https://codepen.io/linhaishe/pen/xxyKzaP?editors=0011

在这个示例中，我们定义了一个名为 usePerformanceObserver 的自定义钩子，该钩子使用 PerformanceObserver 来监听 measure 类型的性能事件。我们使用两个 useEffect 钩子来同时使用 PerformanceObserver.observe() 和 PerformanceObserver.takeRecords() 方法：

- 第一个 useEffect 钩子用于创建 PerformanceObserver 并开始监听性能事件，这与前一个示例中的 usePerformanceObserver 钩子相同。
- 第二个 useEffect 钩子用于定期从性能缓冲区中获取已存储的条目，并将它们添加到状态中。这个例子中我们每5秒执行一次，可以根据需要进行调整。

在 App 组件中，我们使用 usePerformanceObserver 钩子来获取所有 measure 类型的性能条目，并将它们呈现在页面上。我们还在 useEffect 钩子中执行了一个名为 myFunction 的函数，该函数使用 `console.time()` 和 `console.timeEnd() `来测量代码的执行时间，并在浏览器的性能缓冲区中生成一个名为 "myFunction" 的性能条目。PerformanceObserver 将监听此条目，并在每次 PerformanceObserver.takeRecords() 方法被调用时，将其添加到已存储的性能条目中。

我们需要在第二个 useEffect 钩子中访问` PerformanceObserver.takeRecords()` 方法，因此我们将 PerformanceObserver 对象保存在状态中并传递给 useEffect 的依赖项数组中。这样做可以确保我们在每次重新渲染时都使用相同

`useEffect` 钩子中调用了一个 `myFunction` 函数，该函数使用 `console.time()` 和 `console.timeEnd()` 记录了函数执行的时间，并使用 `performance.measure()` 创建了一个自定义测量点。`usePerformanceObserver()` 钩子在这个测量点完成后会触发，并将这个测量点的信息添加到 `performanceEntries` 中

 `myFunction()` 函数将创建两个标记 `start-myFunction` 和 `end-myFunction`，并使用这两个标记来创建测量点 `myFunction`。`usePerformanceObserver()` 钩子会在这个测量点完成后触发，并将测量点信息添加到 `performanceEntries` 中

### 5. PerformanceObserverEntryList

The PerformanceObserverEntryList interface is a list of performance events that were explicitly observed via the observe() method.

`PerformanceObserverEntryList.getEntries()`
Returns a list of all explicitly observed PerformanceEntry objects.

`PerformanceObserverEntryList.getEntriesByType()`
Returns a list of all explicitly observed PerformanceEntry objects of the given entry type.

`PerformanceObserverEntryList.getEntriesByName()`
Returns a list of all explicitly observed PerformanceEntry objects based on the given name and entry type.

```js
const observer = new PerformanceObserver((list, obs) => {
  // Log all entries
  let perfEntries = list.getEntries();
  perfEntries.forEach((entry) => {
    console.log(`${entry.name}'s duration: ${entry.duration}`);
  });

  // Log entries named "debugging" with type "measure"
  perfEntries = list.getEntriesByName("debugging", "measure");
  perfEntries.forEach((entry) => {
    console.log(`${entry.name}'s duration: ${entry.duration}`);
  });

  // Log entries with type "mark"
  perfEntries = list.getEntriesByType("mark");
  perfEntries.forEach((entry) => {
    console.log(`${entry.name}'s startTime: ${entry.startTime}`);
  });
});

// Subscribe to various performance event types
observer.observe({
  entryTypes: ["mark", "measure", "navigation", "resource"],
});
```

```js
function perfObserver(list, observer) {
  list.getEntries().forEach((entry) => {
    if (entry.entryType === "mark") {
      console.log(`${entry.name}'s startTime: ${entry.startTime}`);
    }
    if (entry.entryType === "measure") {
      console.log(`${entry.name}'s duration: ${entry.duration}`);
    }
  });
}
const observer = new PerformanceObserver(perfObserver);
observer.observe({ entryTypes: ["measure", "mark"] });
```

### 6. PerformanceResourceTiming

`PerformanceResourceTiming` 接口记录了单个资源的加载时间信息，包括了发出资源请求的开始时间、接收到资源响应的时间、开始下载资源的时间、下载资源结束的时间等。

可通过 `window.performance.getEntriesByType("resource")`获取

`PerformanceResourceTiming` 是一个接口，它继承自 `PerformanceEntry`，用于描述一个资源的时间性能信息，例如：CSS，JavaScript，图片，音频或视频等。

当资源加载完成时，浏览器会自动创建一个 `PerformanceResourceTiming` 对象，并将其添加到 `performance.getEntries()` 中。该对象包含了资源加载的性能指标，例如响应时间、DNS解析时间、TCP连接时间、SSL握手时间、HTTP请求时间、HTTP响应时间、数据传输时间等。

开发人员可以通过 `PerformanceResourceTiming` 接口的各种属性和方法，对资源的性能进行分析和优化，例如计算资源加载时间，查看DNS解析时间，分析网络传输性能等。

`PerformanceResourceTiming` 还继承了 `PerformanceEntry` 接口的属性，如 `name`、`entryType`、`startTime` 和 `duration` 等。

![image-20230408173426796](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230408173426796.png)

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

### 7. PerformanceNavigationTiming

`PerformanceNavigationTiming` 接口则记录了整个页面导航的时间信息，包括了页面开始导航的时间、重定向的时间、DNS 查询的时间、建立连接的时间、发送请求和接收响应的时间、解析 DOM 的时间等。

![image-20230406000306587](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406000306587.png)

![image-20230406215817434](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406215817434.png)

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

### 8. PerformanceElementTiming

The PerformanceElementTiming interface contains render timing information for image and text node elements the developer annotated with an elementtiming attribute for observation.

The aim of the Element Timing API is to give web developers or analytics tools the ability to measure rendering timestamps of critical elements on a page.

The author flags an element for observation by adding the elementtiming attribute on the element.

使用`PerformanceElementTiming`接口进行测量时，需要在相关元素节点上添加`elementtiming`属性，同时通过`PerformanceObserver`接口来观察和收集性能数据。

`PerformanceElementTiming`接口目前只支持对`<img>`、`<embed>`、`<object>`、`<video>`、`<audio>`这几种HTML元素节点进行性能测量

```js
<img src="image.jpg" elementtiming="big-image" />
<p elementtiming="text" id="text-id">text here</p>
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(entry);
  });
});
observer.observe({ type: "element", buffered: true });
```

### 9. PerformanceEventTiming

#### info

The `PerformanceEventTiming` interface of the Event Timing API provides insights into the latency of certain event types triggered by user interaction.

You typically work with PerformanceEventTiming objects by creating a PerformanceObserver instance and then calling its observe() method, passing in <mark> "event" or "first-input"</mark> as the value of the type option.

By default, PerformanceEventTiming entries are exposed when their <mark>duration is 104ms or greater. </mark>

![image-20230406234828376](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230406234828376.png)

To get a list of all exposed events, you can also look up keys in the performance.eventCounts map:

`const exposedEventsList = [...performance.eventCounts.keys()];`

```js
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    // Full duration
    const duration = entry.duration;

    // Input delay (before processing event)
    const delay = entry.processingStart - entry.startTime;

    // Synchronous event processing time
    // (between start and end dispatch)
    const eventHandlerTime = entry.processingEnd - entry.processingStart;
    console.log(`Total duration: ${duration}`);
    console.log(`Event delay: ${delay}`);
    console.log(`Event handler duration: ${eventHandlerTime}`);
  });
});

// Register the observer for events
observer.observe({ type: "event", buffered: true });
```

You can also set a different durationThreshold. The default is 104ms and the minimum possible duration threshold is 16ms.

`observer.observe({ type: "event", durationThreshold: 16, buffered: true });`

#### First Input Delay (FID)

First Input Delay（FID）是一项度量用户首次与页面交互（例如，点击按钮或选择下拉菜单）的时间指标。它测量从用户首次与页面交互到浏览器实际响应该交互的时间间隔。

通常，FID的计算需要考虑两个因素：首次交互和响应时间。首次交互是指用户首次与页面交互的时间，可以是点击按钮、键入文本或选择下拉列表等。响应时间是指浏览器处理该交互所需的时间，包括JavaScript执行时间、布局和样式计算等。

### 10. User Timing API 

由两个主要组件组成：performance.mark() 和 performance.measure()。

User Timing 接口是浏览器提供的一个用于测量应用性能的API。它允许开发者在浏览器性能时间线中创建针对特定应用的时间戳(Chrome DevTools 中的 Performance 面板可以看到代码中添加的 Performance Mark 和 Performance Measure)，从而可以精确地测量某些操作的执行时间，并识别性能瓶颈。Performance Mark 和 Performance Measure 是 User Timing API 中两个最重要的概念。


Performance Mark：Performance Mark 是 User Timing API 中的事件类型之一。它允许开发者在应用的任意位置添加一个自定义标记，并为该标记指定一个名称。使用 Performance Mark，开发者可以在代码中添加多个标记来表示应用运行时的关键节点，然后通过这些标记来测量应用的性能瓶颈。

`performance.mark(markName);`


Performance Measure：Performance Measure 是 User Timing API 中的另一个事件类型。它允许开发者创建一个时间测量事件，并指定这个时间测量事件的起点和终点。使用 Performance Measure，开发者可以在代码中添加多个时间测量事件，从而精确地测量某些操作的执行时间，并计算出整个应用的性能指标。

`performance.measure(name, startMark, endMark);`

```jsx
function MyComponent(props) {
  useEffect(() => {
    // 添加 Performance Mark
    performance.mark("my-component-start");

    // 组件需要执行的代码
    const result = doSomething();

    // 添加 Performance Mark
    performance.mark("my-component-end");
    performance.measure("my-component-duration", "my-component-start", "my-component-end");

    console.log(`MyComponent rendered in ${result} ms.`);
  }, [props]);

  return (
    // code
  );
}
```

### 11. PerformanceLongTaskTiming

Long Tasks 接口是用于检测浏览器中长任务的API，它可以让开发者了解到在页面渲染过程中哪些任务会阻塞主线程，从而导致页面性能下降。Long Tasks 接口主要涉及到以下两个概念：

Long Task：指执行时间超过 50 毫秒的任何任务。Long Task 对于用户体验来说通常都是不理想的，因为这些任务会阻塞主线程，从而延长页面的响应时间。


```js
// 创建 LongTaskObserver 实例
const observer = new PerformanceObserver((list) => {
  // 遍历所有 Long Task 并输出到控制台
  for (const entry of list.getEntries()) {
    console.log("Long Task:", entry);
  }
});

// 启动 LongTaskObserver
observer.observe({ entryTypes: ["longtask"] });
```

PerformanceObserver 可以通过观察 PerformanceEntry 对象的 duration 和 startTime 属性，来捕获长任务数据。但是它无法确定是哪个具体函数导致了这些长任务。

要确定长任务的来源，可以使用开发者工具中的 Performance 分析功能，并查看相关函数的耗时和时间轴。也可以使用类似于 trace 功能的工具来自动跟踪每个函数的执行时间，然后输出长时间执行的函数。还有其他一些类似的工具可以帮助你自动化函数追踪，例如：Visual Studio Code 的 CPU Profiling 和 Node.js 的 v8-profiler。

### 12. TaskAttributionTiming

The TaskAttributionTiming interface returns information about the work involved in a long task and its associate frame context. The frame context, also called the container, is the iframe, embed or object that is being implicated, on the whole, for a long task.
You usually work with TaskAttributionTiming objects when observing long tasks.

Long tasks refer to "culprit browsing context container", or "the container" for short, which is the top-level page, <iframe>, <embed> or <object> that the task occurred within.

For tasks that don't occur within the top-level page and for figuring out which container is responsible for the long task, the TaskAttributionTiming interface provides the containerId, containerName and containerSrc properties, which may provide more information about the source of the task.

对于不在顶级页面中发生的任务以及用于确定长任务源的情况，TaskAttributionTiming 接口提供了 containerId、containerName 和 containerSrc 属性，这些属性可以提供关于任务来源的更多信息。

顶级页面是指浏览器地址栏中显示的页面，例如在浏览器地址栏输入` www.example.com`，那么该页面就是顶级页面。如果该页面中嵌套了其他页面或者iframe，那么这些嵌套的页面或者iframe就不是顶级页面。

举个例子，假设 `www.example.com`中嵌套了一个iframe，iframe 中又嵌套了一个 `www.sub-example.com` 的页面，那么 `www.sub-example.com` 不是顶级页面，而是嵌套在iframe中的页面。如果这个iframe中发生了一个长任务，TaskAttributionTiming 接口提供的 containerId、containerName 和 containerSrc 属性可以帮助确定该长任务的源是哪个iframe。

### 13. PerformancePaintTiming

Paint Timing API是浏览器提供的API之一，它用于测量页面的渲染性能。该API可以捕获在呈现过程中发生的重要事件，并以有意义的方式返回这些事件的时间戳，从而有助于开发人员分析网页的渲染性能。

Paint Timing API包含以下指标：

- FP(first-paint)，从页面加载开始到第一个像素绘制到屏幕上的时间
- FCP(first-contentful-paint)，从页面加载开始到页面内容的任何部分在屏幕上完成渲染的时间
- LCP(largest-contentful-paint)，从页面加载开始到最大文本块或图像元素在屏幕上完成渲染的时间
- CLS(layout-shift)，从页面加载开始和其[生命周期状态](https://developers.google.com/web/updates/2018/07/page-lifecycle-api)变为隐藏期间发生的所有意外布局偏移的累积分数

| 指标                       | 含义                                                         |
| -------------------------- | ------------------------------------------------------------ |
| `first-paint`              | 首次像素渲染时间，即浏览器首次绘制文档的时间，其实把 FP 理解成白屏时间也是没问题的。 |
| `first-contentful-paint`   | 首次有内容渲染的时间，即浏览器首次绘制页面中的任何文本、图像、背景图像或非空 SVG |
| `first-meaningful-paint`   | 首次有意义的渲染时间，即页面开始呈现有意义的内容的时间（例如，当一个页面加载了一张图片和一些文本内容时，用户看到文本内容的时间点） |
| `cumulative-layout-shift`  | 累计布局位移，即页面中所有元素在加载过程中发生的任何可见移动的累计分数 |
| `largest-contentful-paint` | 页面中最大的有意义绘制的时间，例如大图像或大块的文本         |

![image-20230408132301396](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230408132301396.png)

### 14. LargestContentfulPaint

LCP(largest-contentful-paint)，从页面加载开始到最大文本块或图像元素在屏幕上完成渲染的时间。LCP 指标会根据页面[首次开始加载](https://w3c.github.io/hr-time/#timeorigin-attribute)的时间点来报告可视区域内可见的最大[图像或文本块](https://web.dev/lcp/#what-elements-are-considered)完成渲染的相对时间。

![image-20230408132416540](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230408132416540.png)

FCP 和 LCP 的区别是：FCP 只要任意内容绘制完成就触发，LCP 是最大内容渲染完成时触发。

LCP 考察的元素类型为：

- `<img>`元素
- 内嵌在`<svg>`元素内的`<image>`元素
- `<video>`元素（使用封面图像）
- 通过[`url()`](https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fdocs%2FWeb%2FCSS%2Furl())函数（而非使用 [CSS 渐变](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Images/Using_CSS_gradients)）加载的带有背景图像的元素
- 包含文本节点或其他行内级文本元素子元素的[块级元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Block-level_elements)。`<p>`等

```js
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1]; // Use the latest LCP candidate
  console.log("LCP:", lastEntry.startTime);
  console.log(lastEntry);
});
observer.observe({ type: "largest-contentful-paint", buffered: true });
```

### 15. LayoutShift

The LayoutShift interface of the Performance API provides insights into the layout stability of web pages based on movements of the elements on the page.

A layout shift happens when any element that is visible in the viewport changes its position between two frames. These elements are described as being unstable, indicating a lack of visual stability.

The Layout Instability API provides a way to measure and report on these layout shifts. All tools for debugging layout shifts, including those in the browser's developer tools, use this API. The API can also be used to observe and debug layout shifts by logging the information to the console, to send the data to a server endpoint, or to web page analytics.

Layout Shift（布局偏移）是指当页面正在加载时，页面的元素位置发生了变化，从而导致用户感知到的视觉不稳定。布局偏移可能会破坏用户体验，特别是在阅读文本或填写表单等场景下。

Layout Shift 是一个 Web 性能指标，用于评估页面的视觉稳定性。它由两个指标计算得出：布局偏移距离和布局偏移时间。布局偏移距离指的是发生布局偏移的元素在屏幕上发生的移动距离，通常以像素为单位。布局偏移时间指的是从页面开始加载到布局偏移结束的时间，通常以毫秒为单位。

```js
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    // Count layout shifts without recent user input only
    if (!entry.hadRecentInput) {
      console.log("LayoutShift value:", entry.value);
      if (entry.sources) {
        for (const { node, currentRect, previousRect } of entry.sources)
          console.log("LayoutShift source:", node, {
            currentRect,
            previousRect,
          });
      }
    }
  }
});

observer.observe({ type: "layout-shift", buffered: true });
```

### 16. Frame Timing API

Measures frames, which represent a loop of the amount of work a browser needs to do to process things like DOM events, resizing, scrolling and CSS animations.

This work is **NO LONGER BEING PURSUED**. It's left here for historical purposes. 被废弃

```js
if (window.performance && window.performance.timing && window.performance.getEntriesByType) {
  // 获取性能条目
  var performanceEntries = performance.getEntriesByType("frame");
  for (var i = 0; i < performanceEntries.length; i++) {
    var startTime = performanceEntries[i].startTime;
    var duration = performanceEntries[i].duration;
    console.log("Frame " + i + " started at " + startTime + " and lasted " + duration + " milliseconds.");
  }
}
```

The PerformanceFrameTiming interface exposes timing information about the processing costs of the browser event loop. To limit the exposed information the interface is restricted to reporting slow frames only, which are already observable through other means (e.g. requestAnimationFrame), and the user agent is allowed to set and exercise own thresholds for delivery of slow frame events.

相关性能可以通过requestAnimationFrame进行测量。

# Performance API 实践



![image-20230407232847292](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230407232847292.png)

![image-20230407232903335](https://raw.githubusercontent.com/linhaishe/blogImageBackup/main/performance-api/image-20230407232903335.png)

## 性能采集

### 1. 获取白屏时间

FP(first-paint)，从页面加载开始到第一个像素绘制到屏幕上的时间。其实把 FP 理解成白屏时间也是没问题的。

### 2. 获取首屏渲染时间

首屏渲染时间计算过程：

1. 利用 MutationObserver 监听 document 对象，每当 DOM 元素属性发生变更时，触发事件。
2. 判断该 DOM 元素是否在首屏内，如果在，则在 `requestAnimationFrame()` 回调函数中调用 `performance.now()` 获取当前时间，作为它的绘制时间。
3. 将最后一个 DOM 元素的绘制时间和首屏中所有加载的图片时间作对比，将最大值作为首屏渲染时间。

https://stackblitz.com/edit/react-ts-gszu5i?file=App.tsx

### 3. 获取接口请求耗时

https://codepen.io/linhaishe/pen/MWPYpvX?editors=0011

https://codepen.io/linhaishe/pen/yLRyXXa?editors=0012

### 4. FPS

FPS 指的是“每秒帧数”（Frames Per Second），是衡量视频、游戏等多媒体应用程序流畅度的一个指标。它表示在每秒钟内，显示设备能够更新多少次屏幕图像。如果 FPS 越高，说明应用程序的动画和图像会更加流畅自然，反之则会更加卡顿和不自然。

利用 requestAnimationFrame() 我们可以计算当前页面的 FPS。

先记录一个初始时间，然后每次触发 requestAnimationFrame() 时，就将帧数加 1。过去一秒后用帧数/流逝的时间就能得到当前帧率。

当连续三个低于 20 的 FPS 出现时，我们可以断定页面出现了卡顿，详情请看 [如何监控网页的卡顿](https://zhuanlan.zhihu.com/p/39292837)。

https://codepen.io/linhaishe/pen/qBJEPqN?editors=0011

Ref: [前端监控 SDK 的一些技术要点原理分析](https://github.com/woai3c/Front-end-articles/issues/26)

# Performance API 的限制和注意事项

1. 浏览器支持度：虽然现代浏览器大多数都支持 Performance API，但是不同浏览器可能存在差异，例如某些浏览器可能不支持某些 Performance API 提供的功能或属性。
2. 浏览器兼容性问题：不同浏览器的性能统计结果可能存在差异，例如同一份代码在 Chrome 和 Firefox 浏览器上可能会得到不同的性能数据。
3. 跨域限制：Performance API 在某些情况下可能受到跨域限制，例如如果尝试获取其他域名下的资源的性能数据时，可能会遇到跨域问题。
4. 误差和不精确性：Performance API 提供的数据都是估算值，可能会存在误差和不精确性。例如，对于某些 API，浏览器可能只提供毫秒级别的精度。
5. 性能开销：使用 Performance API 会产生一定的性能开销，尤其是在对于大型网站和复杂应用程序的性能分析时，可能会增加额外的性能负担。
6. `Date.now()` 和 `performance.now()`

在性能测量时，`Date.now()` 和 `performance.now()`都可以用来获取当前时间，但它们有一些重要的区别。

`Date.now()`方法返回当前时间距离1970年1月1日午夜UTC（Coordinated Universal Time）之间的毫秒数，也就是时间戳。它的精度通常为1毫秒，并且受到系统时钟的影响，这意味着当系统时钟被修改时，`Date.now()`返回的值可能会受到影响。

`performance.now()`方法返回自页面加载以来的毫秒数，精度通常为5微秒（即0.005毫秒），它是基于高精度的时间戳，而不是系统时钟。由于它的精度更高，因此更适合用于测量较小的时间间隔，例如函数执行时间或动画帧率。

需要注意的是，`performance.now()`只能在现代浏览器中使用，而`Date.now()`则是通用的 JavaScript 方法，可在任何支持 JavaScript 的环境中使用。

因此，如果需要高精度的性能测量，应该使用`performance.now()`方法，否则可以使用`Date.now()`方法。

# 性能优化

## 前端性能优化的概述

前端性能优化是指通过各种手段来提高网站或应用程序在浏览器中的加载速度、响应速度以及用户体验的整体效果。这是一个复杂而广泛的领域，包括许多方面的技术和方法。

前端性能优化的目标是缩短网页的加载时间，提高用户的体验，同时减少对服务器的请求负载，以及减少用户的设备资源消耗。一般来说，前端性能优化的目标包括以下几个方面：

1. 减少网络请求：通过合并、压缩文件、缓存等手段减少 HTTP 请求的数量，减少页面的大小和加载时间。
2. 减少页面体积：优化 HTML、CSS、JavaScript 代码，使其尽量精简，减少页面的大小和加载时间。
3. 加快页面渲染：通过一系列的技术手段，如优化 CSS 样式、JavaScript 执行效率、缩减 DOM 树、优化图片加载等，加快页面的渲染速度。
4. 提高用户体验：通过提高页面响应速度、减少页面卡顿和闪烁等方式，提高用户体验。
5. 兼容性：针对不同的浏览器和设备，做出适当的兼容性处理，确保页面在不同的浏览器和设备上都能够正常展示。

前端性能优化的方法有很多，具体的优化策略需要根据具体的业务场景和用户需求来选择和优化。常用的一些优化方法包括使用 CDN、合并、压缩文件、缓存、使用异步加载、使用预加载和懒加载、优化图片、减少 DOM 操作等。

## 性能优化的实践技巧

1. 压缩代码和文件：压缩JavaScript、CSS和HTML等静态资源可以减少它们的大小，加快加载速度。
2. 减少HTTP请求：通过合并文件和使用雪碧图等技术，可以减少HTTP请求次数，从而减少页面加载时间。
3. 使用CDN：将静态资源部署在CDN上可以提高页面加载速度，减轻服务器压力。
4. 减少DOM操作：减少DOM操作可以降低页面重绘和回流的次数，从而提高页面性能。
5. 使用缓存：合理使用浏览器缓存和服务器缓存可以加快页面加载速度。
6. 异步加载：使用异步加载技术，如defer和async等，可以加快页面的加载速度。
7. 减少重绘和回流：通过使用CSS动画代替JavaScript动画、使用transform和opacity等属性来减少重绘和回流。
8. 图片优化：优化图片大小、格式和质量等可以减少页面加载时间。
9. 懒加载：使用懒加载技术可以先加载页面的核心内容，减少页面加载时间。
10. 资源预加载：使用预加载技术可以在页面加载时提前加载所需的资源，加快页面响应速度。
11. 节流防抖：通常用于处理一些频繁触发的事件，比如窗口的滚动事件、输入框的输入事件等等。在实际开发中，可以根据具体的需求来选择合适的技巧进行优化，从而提升页面的性能和用户体验。
