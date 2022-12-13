##  0. 自我介绍

（自我介绍时间最好在两分钟左右）

面试官你好，我是李春娴，有3年多的工作经验，在工作中我做了体检管理后台系统和一些Toc向小程序；在工作中协调项目开发过程中遇到的问题，分析需求文档，定制开发计划等。个人技术栈以react为主，对vue也有相应的了解。平常自己除了日常的工作之外，也会在一些博主博客下进行学习，在公司也做过一些学习分享的活动，对于前端一些基础的像数据结构、工程化、机网相关的知识也在列计划学习和进阶。谢谢。

模板

面试官你好，我是李春娴，有3年多的工作经验，在工作中我主要做体检管理后台系统和xx小程序，它们都是tob/toc的，（形态是什么），个人技术栈以react为主，对vue也有相应的了解。平常自己除了日常的工作之外，也会在一些知名的博主博客下进行学习，自己平常也喜欢做笔记，在公司也做过一些学习分享的活动，对于前端一些基础的像数据结构和算法、工程化、机网相关的知识也在列计划学习和进阶。谢谢面试官。

## 1. 懒加载

我们的管理台有一个是图片板块，需要管理用户上传的图片。运营需要审核。

懒加载的实现重点在于确定用户需要加载哪张图片，在浏览器中，可视区域内的资源就是用户需要的资源。所以当图片出现在可视区域时，获取图片的真实地址并赋值给图片即可。

图片懒加载是一种优化网页性能的技术，它的目的是延迟图片的加载，以提高网页的访问速度。

通常情况下，当用户访问一个网页时，网页会向服务器发送请求，并加载所有的图片资源。这样会导致网页加载速度变慢，影响用户体验。

图片懒加载的思路是，只有当图片出现在用户的视野中时，才向服务器发送请求，加载图片资源。这样，可以避免在用户没有看到某张图片时，就浪费带宽和资源去加载它。

实现图片懒加载的步骤如下：

1. 使用 JavaScript 动态修改图片的 src 属性。
2. 监听页面的滚动事件，判断图片是否出现在用户的视野中。
3. 当图片出现在用户的视野中时，向服务器发送请求，加载图片资源。

```js
// 修改图片的 src 属性
function lazyLoadImage(image) {
  // 获取图片的真实地址
  var src = image.getAttribute('data-src');
  // 修改图片的 src 属性
  image.setAttribute('src', src);
}

// 监听页面的滚动事件
window.addEventListener('scroll', function() {
  // 获取所有的图片元素
  var images = document.querySelectorAll('img[data-src]');

  // 遍历所有的图片元素
  for (var i = 0; i < images.length; i++) {
    var image = images[i];
    // 判断图片是否出现在用户的视野中
    if (isInViewport(image)) {
      // 加载图片
      lazyLoadImage(image);
    }
  }
});

```

上面的例子中，isInViewport() 函数用来判断图片是否出现在用户的视野中。代码如下

```js
function isInViewport(image) {
  // 获取图片的位置和尺寸信息
  var rect = image.getBoundingClientRect();

  // 视口的高度和宽度
  var viewportHeight = window.innerHeight;
  var viewportWidth = window.innerWidth;

  // 判断图片是否出现在视口中
  return (
    // 图片的顶部是否出现在视口中
    rect.top >= 0 &&
    rect.top <= viewportHeight ||
    // 图片的底部是否出现在视口中
    rect.bottom >= 0 &&
    rect.bottom <= viewportHeight
  );
}

```

在页面中使用图片懒加载的方式，可以在 img 标签中添加 data-src 属性，将图片的真实地址作为属性的值。

```js
<img src="loading.gif" data-src="image.jpg" alt="图片">
```

上面的例子中，src 属性的值为一个 loading.gif 图片，表示图片正在加载中。当图片出现在用户的视野中时，才会将 data-src 属性的值（即 image.jpg）设置为 src 属性的值，从而加载真实的图片。

如果需要实现更复杂的图片懒加载功能，可以使用相关的框架或库，比如 lazyload.js、IntersectionObserver 等。这些框架和库可以提供更多的配置选项和回调函数，以便实现更精细的控制。

---



- **减少无用资源的加载**：使用懒加载明显减少了服务器的压力和流量，同时也减小了浏览器的负担。
- **提升用户体验**: 如果同时加载较多图片，可能需要等待的时间较长，这样影响了用户体验，而使用懒加载就能大大的提高用户体验。
- **防止加载过多图片而影响其他资源文件的加载** ：会影响网站应用的正常使用。

图片的加载是由src引起的，当对src赋值时，浏览器就会请求图片资源。根据这个原理，我们使用HTML5 的data-xxx属性来储存图片的路径，在需要加载图片的时候，将data-xxx中图片的路径赋值给src，这样就实现了图片的按需加载，即懒加载。

注意：data-xxx 中的xxx可以自定义，这里我们使用data-src来定义。

使用原生JavaScript实现懒加载：

**知识点：**

（1）window.innerHeight 是浏览器可视区的高度

（2）document.body.scrollTop || document.documentElement.scrollTop 是浏览器滚动的过的距离

（3）imgs.offsetTop 是元素顶部距离文档顶部的高度（包括滚动条的距离）

（4）图片加载条件：img.offsetTop < window.innerHeight + document.body.scrollTop;

## 2. 虚拟滚动

有10万数据需要展示的时候，我们需要一下将它全部加载出来。可能有时候会需要分页，但是有时候产品会需要将它全部加载出来。

主要的处理思路是 A按需渲染 和 B模拟滚动。

### A. 按需渲染：

如果全部渲染会卡顿，所以同一时间只渲染我们看的见的这些DOM节点的时候，浏览器需要渲染的节点就会非常非常少了，这会极大的降低渲染时长。

按需渲染会遇到的问题

#### 1. 视口能渲染的列表元素的数量

   - 视口的高度我们已经知道了（父元素的高度），假设偏移量为0，我们从第一个元素开始渲染，那么它能装几个列表元素呢？这里就需要我们给每一个列表元素设置一个高度。通过累加高度计算找到第一个加完它的高度后总高度超出视口高度的列表元素。

#### 2. 如何判断该渲染哪几个元素？当用户没有滚动时，偏移量为0，我们知道从第一个元素开始渲染。那么假如当用户累计滚动了x像素后，又该从哪个元素开始渲染呢？

   - <img src="http://tva1.sinaimg.cn/large/005NUwygly1h8winl9b7uj310i0zqqj1.jpg" alt="image.png" style="zoom:50%;" />

#### 3. 列表元素要怎么渲染我想要渲染的内容

   - 对于每一个列表元素，我们调用一个~~`itemElementGenerator`~~元素DOM创建函数来创建DOM，它接受对应的列表项作为参数，返回一个DOM元素。该DOM元素会被作为列表元素加载到视口元素中。

   - 渲染方法主要依赖于用户的总滚动量~~`virtualOffset`~~，每一~~个`virtualOffset`~~总滚动量都对应着一个固定的渲染帧。 我们先计算出可视的子列表，再计算出偏移量。最后根据该子列表生成DOM，替换掉视口元素中的DOM。

     ```js
        this.renderList = this._list.slice(headIndex, tailIndex + 1)
     
         const $listWp = document.createElement("div")
         this.renderList.forEach((item) => {
           const $el = this.itemElementGenerator(item)
           // appendChild添加
           $listWp.appendChild($el)
         })
         $listWp.style.transform = `translateY(-${this.renderOffset}px)`
         this.$list.innerHTML = ''
         this.$list.appendChild($listWp)
       }
     ```

### B. 模拟滚动

我们只渲染能看见的元素，这就意味着我们没有原生滚动的功能。我们需要去模拟滚动行为，在用户滚动滑轮或者滑动屏幕时，相应的滚动列表。我们这里的滚动列表不是真正的滚动列表，==而是根据滚动的位置重新渲染可见的列表元素==。当这个操作时间跨度足够小时，它看起来就像是在滚动一样。

我们监听视口的滚轮事件，该事件对象有一个属性叫做deltaY，记录的是滚轮滚动的方向以及滚动量。向下为正，向上为负。

```js
class VirtualScroll {
  constructor(/* ... */) {
    // ...
    this.bindEvents()
  }
  bindEvents() {
    let y = 0
    const updateOffset = (e) => {
      e.preventDefault()
      y += e.deltaY
    }
    this.$list.addEventListener("wheel", updateOffset)
  }
}
```

滚动记录以及渲染方法都已经实现，那么最后一步就很简单了，就是在滚动记录变更时执行渲染方法。

### C. 性能优化

1. 首先事件触发频率，我们需要做一下节流。
   - 将更新用户总滚动量的操作剥离了出来，因为它会涉及到`render`操作。但是记录偏移量我们可以一直触发。 所以我们把更新总滚动量的操作频率通过节流函数降低。
     - ~~但是，滑动的时候会有点不丝滑。页面的FPS降到了30左右，页面的滚动流畅度就没有那么丝滑了。但是也是没有明显卡顿的。~~
2. 每次滚动都要重新渲染，我们需要控制一下这个重新渲染的频率，消耗太高了。

- 解决方法就是我们在可视元素列表前后预先多渲染几个列表元素。这样我们在少量滚动时可以偏移这些已渲染的元素而不是重新渲染，当滚动量超过缓存元素时，再进行重新渲染。比起重新渲染，修改列表的样式属性消耗就小多了
- 只需要改动列表的translateY就好了。注意这里我们不用y和margin-top两个属性，因为transform拥有更好的动画体验。

https://juejin.cn/post/6844904183582162957

https://blog.logrocket.com/virtual-scrolling-core-principles-and-basic-implementation-in-react/

1. 监听滚轮事件/触摸事件，记录列表的总偏移量。
2. 根据总偏移量计算列表的可视元素起始索引。
3. 从起始索引渲染元素至视口底部。
4. 当总偏移量更新时，重新渲染可视元素列表。
5. 为可视元素列表前后加入缓冲元素。
6. 在滚动量比较小时，直接修改可视元素列表的偏移量。
7. 在滚动量比较大时（比如拖动滚动条），会重新渲染整个列表。
8. 事件节流。

### D. 优化结果

我们从最开始的40%的脚本执行耗时降到了现在的13%。效果还是蛮显著的，当然还有更多的优化空间，比如我们现在采用的是全部列表重新替换掉，其实这中间有很多一样或者相似的DOM，我们可以复用部分DOM，从而减少创建DOM的时间。

## 3. 封装要注意的问题

封装方法指的是将一段代码进行封装，使其成为一个独立的函数或方法，以便在需要时重复使用。在封装方法的时候，需要注意以下几点：

1. 方法应该是独立的，不依赖于外部环境，以便在任何地方都能够被调用。

2. 方法应该是可重复使用的，可以在多个不同的场景中被调用。

3. 方法应该是可扩展的，方便在未来根据需要进行扩展和更新。

4. 方法应该具有良好的可读性，使得其他人能够快速理解和使用。

5. 方法应该具有良好的性能，不会造成系统的性能瓶颈。

6. 方法应该具有良好的错误处理机制，能够在出现错误时及时处理并报告错误信息。

## 3. 请求封装

将请求封装成函数可以使得代码更加模块化，并且可以统一处理请求的报错提示与响应。对用户的状态进行判断可以根据用户的状态跳转到不同的路由，提供更好的用户体验。例如，当用户未登录时，可以跳转到登录页面，而不是显示错误提示。

https://zhuanlan.zhihu.com/p/136035219

```js
import { useState, useEffect } from 'react';

// 定义请求函数
function useRequest(url, options) {
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    fetch(url, options)
      .then(res => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error(res.statusText);
        }
      })
      .then(data => {
        setResponse(data);
        setIsLoading(false);
      })
      .catch(err => {
        setError(err);
        setIsLoading(false);
      });
  }, [url, options]);

  return { response, error, isLoading };
}

// 使用请求函数
function App() {
  const { response, error, isLoading } = useRequest(
    'https://example.com/api/v1/users',
    {}
  );

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>{error.message}</p>;
  }

  return <pre>{JSON.stringify(response, null, 2)}</pre>;
}

```



### **创建三个文件(index.js/interceptor.js/request.js)**

```text
/**
 * index.js
 * api地址管理
 */
export default {
    login:'/user/login',
    getInfo:'/user/getInfo'
}
```

index.js实际上和axios封装没有关系，因为它也属于API这一层，所以我一起创建了，我个人习惯把项目所有url抽取到这里集中管理。

### **封装interceptor**

interceptor作用就是拦截，可以针对请求参数和响应结果进行拦截处理，一般在项目当中，我们主要会针对接口常规报错、网络报错、系统超时、权限认证等做拦截处理。

此处我们对通过create创建实例，设置baseUrl，timeout，然后在设置request和response的拦截。

### **封装axios**

创建request文件，针对axios做适合业务发展的封装，很多时候架构师做公共机制都是为了迎合自身项目需要，而并非一味求大做全，所以这个大家要适当调整，比如我们只用get/post请求。

request.js主要针对axios做二次封装，目的同样是为了拦截所有前端请求，这样可以做前端loading效果、mock、错误拦截、错误弹框显示、数据适配、参数适配、环境适配等工作。

## 4. 选取的文本内容及位置封装

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8swc7wi7oj31b60u8qf3.jpg" alt="image.png" style="zoom: 50%;" />

## 4. 搜索栏和表格组件，过滤搜索封装

定义了三个组件：`SearchBar`、`Table` 和 `TableSearchBox`。`SearchBar` 组件用于显示搜索栏，`Table` 组件用于显示表格，`TableSearchBox` 组件是整个应用的主组件。 在 `SearchBar` 组件中，我们使用了 `useState` Hook 来管理搜索框中的内容，并定义了两个事件处理函数：`handleChange` 和 `handleSubmit`。`handleChange` 函数用于更新搜索框中的内容，`handleSubmit` 函数用于在用户提交搜索请求时触发回调函数。

在 `Table` 组件中，我们使用了搜索框中的内容来过滤表格中的数据。具体来说，我们定义了一个 `filteredData` 变量，用于保存过滤后的数据。然后，在渲染表格时，使用这个变量来替换原始的数据。

最后，在 `TableSearchBox` 组件中，我们使用了 `useState` 和 `useEffect` Hooks 来管理搜索框中的内容和表格中的数据。我们在组件挂载时发起了一个请求，获取了表格的数据。然后，我们定义了一个 `handleSearch` 函数，用于在用户提交搜索请求时更新过滤条件。

在组件渲染时，我们通过调用 `SearchBar` 和 `Table` 组件来显示搜索栏和表格，并将 `handleSearch` 函数作为 `SearchBar` 组件的 `onSearch` 属性传递进去。

通过这些操作，我们实现了一个简单的搜索功能，用户可以在搜索框中输入关键字，然后，用户可以通过提交搜索请求来过滤表格中的数据。在表格中，只会显示名称中包含搜索关键字的行。

当然，上面的例子只是一个简单的示例，在实际应用中，可能需要根据需要对搜索和过滤功能进行更多的封装，以提供更好的用户体验。例如，==可以使用 debounce 技术来减少请求的频率，避免网络负载过大。此外，还可以实现分页功能，以支持大量数据的展示。==

```jsx
import React, { useState } from 'react';

// 定义搜索栏组件
function SearchBar(props) {
  const [query, setQuery] = useState('');

  function handleChange(event) {
    setQuery(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();
    props.onSearch(query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={query} onChange={handleChange} />
      <button type="submit">Search</button>
    </form>
  );
}

// 定义表格组件
function Table(props) {
  const { data, filter } = props;

  const filteredData = data.filter(item => {
    return item.name.toLowerCase().includes(filter.toLowerCase());
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        {filteredData.map(item => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.email}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

// 定义主组件
function App() {
  const [filter, setFilter] = useState('');
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://example.com/api/v1/users')
      .then(res => res.json())
      .then(data => setData(data));
  }, []);

  function handleSearch(query) {
    setFilter(query);
  }

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <Table data={data} filter={filter} />
    </div>
  );
}

```

https://juejin.cn/post/7147858832692084767#heading-14

搜索栏和表格组件，并用 hook 封装搜索，过滤功能

拿到所有的数据，useState存起来，拿到用户的搜索内容，通过useState存起来的所有数据中进行filter，seresult去设置result

https://www.freecodecamp.org/chinese/news/build-a-search-filter-using-react-and-react-hooks/

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8f5bvo9m6j316y0wsgve.jpg" alt="image.png" style="zoom: 33%;" />

## 6. 分页远程搜索，设置默认值组件封装

分页滚动搜索框组件， 实现远程分页滚动搜索，设置默认值等功能

### 1. 为什么需要做这个需求：

分页滚动搜索框组件，用户可以在搜索框中输入关键字进行搜索，同时，可以通过滚动滚动条加载下一页的数据。

### 2. 处理思路

在表格组件中添加了一个滚动事件处理函数，用于实现远程分页滚动功能。在处理函数中，判断滚动条是否到达底部，如果是，则触发一个回调函数，用于加载下一页的数据。

首先，我们定义了一些状态变量，用于保存当前的页码、每页的数据量、总的数据量和加载中的状态。

然后，我们定义了一个 `fetchData` 函数，用于发起请求并加载数据。

然后，通过给 `SearchBar` 组件的 `defaultValue` 属性赋初始值来设置默认值。例如，如果我们希望在渲染搜索栏时默认显示 "hello"，其中，`defaultValue` 属性指定了默认值，在渲染时就会显示在搜索栏的输入框中。如果不想设置默认值，可以直接省略 `defaultValue` 属性，这样搜索栏的输入框就会显示空值。

最后，我们定义了一个 `handleLoadMore` 函数，判断滚动条是否到达底部，用于在触发滚动事件时加载下一页的数据。

~~然后，我们将 `handleLoadMore` 函数作为 `Table` 组件的 `onLoadMore` 属性传递进去，以便在触发滚动事件时执行相应的操作。~~

通过上面的步骤，我们就实现了一个分页滚动搜索框组件，用户可以在搜索框中输入关键字进行搜索，同时，可以通过滚动滚动条加载下一页的数据。

当然，上面的例子仅供参考，在实际应用中，可能需要根据需要进行修改和完善，以提供更好的用户体验。

例如，可以使用 debounce 技术来减少请求的频率，避免网络负载过大。此外，还可以实现自定义的 loading 效果，以提示用户数据正在加载中。

```jsx
import React, { useState, useEffect, useRef } from 'react';

// 定义搜索栏组件
function SearchBar(props) {
  const { defaultValue, onSearch } = props;
  const [query, setQuery] = useState(defaultValue);

  function handleChange(event) {
    setQuery(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={query} onChange={handleChange} />
      <button type="submit">Search</button>
    </form>
  );
}

// 定义表格组件
function Table(props) {
  const { data, filter, onLoadMore } = props;

  const filteredData = data.filter(item => {
    return item.name.toLowerCase().includes(filter.toLowerCase());
  });

  // 保存滚动容器的 DOM 节点
  const scrollContainer = useRef(null);

  // 处理滚动事件
  function handleScroll(event) {
    // 判断是否到达底部
    if (scrollContainer.current.scrollHeight - scrollContainer.current.scrollTop === scrollContainer.current.clientHeight) {
      // 触发回调函数
      onLoadMore();
    }
  }

  return (
    <div ref={scrollContainer} onScroll={handleScroll}>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map(item => (
            <tr key={item.id}>
              <td>{item.name}</td>
              <td>{item.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// 定义主组件
function App() {
  const [filter, setFilter] = useState('');
  const [data, setData] = useState([]);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);

  // 在组件挂载时加载数据
  useEffect(() => {
    fetchData();
  }, []);

  // 定义 fetchData 函数
  function fetchData() {
    setLoading(true);
    fetch(`https://example.com/api/v1/users?page=${page}&pageSize=${pageSize}`)
      .then(res => res.json())
      .then(data => {
        setData(data.items);
        setTotal(data.total);
        setLoading(false);
      });
  }

  // 定义 handleLoadMore 函数
  function handleLoadMore() {
    // 判断是否还有更多数据
    if (data.length < total) {
      // 设置下一页的页码
      setPage(page + 1);
      // 加载下一页的数据
      fetchData();
    }
  }

  function handleSearch(query) {
    setFilter(query);
  }

  return (
    <div>
      <SearchBar onSearch={handleSearch} defaultValue={filter} />
      <Table data={data} filter={filter} onLoadMore={handleLoadMore}/>
    </div>
   )

```

https://juejin.cn/post/7147858832692084767#heading-6

<img src="http://tva1.sinaimg.cn/large/005NUwygly1h8swisvi7vj31b219swwv.jpg" alt="image.png" style="zoom:33%;" />

最后就是滚动自动加载的逻辑，通过 scrollHeight - scrollTop <= clientHeight + threshold 结果判断是否触底。

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20221205171812038.png" alt="image-20221205171812038" style="zoom: 50%;" />

https://juejin.cn/post/7030405236657225735

## 7. 如何调研移动端适配方案viewport

项目中如何设置viewport:

如果项目中我独立开发配置，完全可以利用webpack配置插件的方式支持vw适配，不用自己去手动写 vw.

设置 viewport 是通过在 HTML 页面的 `<head>` 标签中添加一个 `<meta>` 标签来实现的。例如，你可以这样设置 viewport：

```
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

在这个例子中，我们通过设置 `<meta>` 标签的 `name` 属性为 `viewport` 来指定这是一个 viewport 标签。然后，通过设置 `content` 属性来指定 viewport 的具体内容。

viewport 和 rem 方案的优缺点

viewport 方案：

优点：

- 简单易用，可以通过设置 viewport 的宽度来控制网页的布局，方便开发者进行调试。
- 可以通过设置 viewport 的缩放比例来实现网页的自适应，从而让网页在不同的设备上都能保持较好的用户体验。

缺点：

- 对于高清屏幕的设备，网页的字体会显得过小，不够清晰，容易造成视觉困扰。
- 如果页面中包含多个不同尺寸的图片

rem 方案：

优点：

- 相对单位，可以根据屏幕尺寸的变化自动调整元素的尺寸，从而实现网页的自适应。
- 可以通过 JavaScript 动态设置 HTML 元素的 font-size 属性，来控制页面中所有元素的尺寸。这样可以提高页面的可维护性和可扩展性。

缺点：

- 如果页面中包含多个不同尺寸的图片，需要使用媒体查询来进行特殊处理。
- 如果使用 JavaScript 来动态设置 HTML 元素的 font-size 属性，会导致页面在加载过程中出现短暂的白屏现象，不够优雅。
- 对于高清屏幕的设备，页面的字体会显得过大。

总的来说，viewport 和 rem 方案都是移动端和 PC 端的样式兼容的常用方法。它们各有优缺点，在实际项目中需要根据页面的特点和需求来选择合适的方案。

如果页面结构比较复杂，需要对不同设备的屏幕尺寸进行精细的控制，可以使用 rem 方案。

如果页面结构比较简单，只需要适配常见的移动端和 PC 端，可以使用 viewport 方案。

https://juejin.cn/post/6844903988488306701

去查看现如今有哪几种技术方案。然后根据项目复杂程度自行选用技术方案。

由于viewport单位得到众多浏览器的兼容，==lib-flexible这个过渡方案已经可以放弃使用==，不管是现在的版本还是以前的版本，都存有一定的问题。建议大家开始使用viewport来替代此方。

lib-flexible 是一个用于实现移动端适配的库，它通过动态计算 HTML 根元素的字体大小来实现页面的缩放。

然而，lib-flexible 存在一些问题。

1. 首先，由于它通过修改 HTML 根元素的字体大小来实现缩放，因此会导致页面布局发生变化，可能会影响页面的可读性和用户体验。

2. 其次，lib-flexible 会在页面加载完成后立即执行，因此可能会导致页面的渲染延迟，影响页面的加载速度。

3. 最后，lib-flexible 只能处理纵向的屏幕尺寸，对于横屏设备无能为力。

rem是根据html的最终font-size进行响应： 1rem === finalDocElementFontSize（重点！） 。对于大部分机型，docElementFontSize和finalDocElementFontSize是相等的，但是有些网页在某些情况下打开的话，会得到docElementFontSize和finalDocElementFontSize不相等的情况。

最后使用viewport方案

vw 作为布局单位，从底层根本上解决了不同尺寸屏幕的适配问题，因为每个屏幕的百分比是固定的、可预测、可控制的。 viewport 相关概念如下：https://www.jianshu.com/p/4cdd8fbd7487

vw
适配思路（如上）
原理
利用 CSS 视窗的特性，总宽度为 100vw，每一份为一个单位 1vw，设置 1rem 单位为 10vw
缺点
因为是根据视图的宽度计算，所以不适用平板和PC
影响力：2018年出的方案，目前 H5 适配主流

## 8. 抽离常用函数封装为npm包

1. 创建一个空文件夹，用于存放 npm 包的代码。
2. 在该文件夹中创建一个名为 `package.json` 的文件，并在该文件中添加包的基本信息。例如：

```js
{
  "name": "my-common-utils",
  "version": "1.0.0",
  "description": "A collection of common utility functions",
  "main": "index.js",
  "scripts": {
    "test": "echo 'Error: no test specified' && exit 1"
  },
  "keywords": [
    "utils",
    "common"
  ],
  "author": "John Doe",
  "license": "MIT"
}
```

3. 在该文件夹中创建一个名为 `index.js` 的文件，并在该文件中定义要封装的函数。例如：

```js
// index.js

function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  return a / b;
}

module.exports = {
  add,
  subtract,
  multiply,
  divide
};
```

4. 在命令行中进入到该文件夹，然后运行 `npm publish` 命令发布该 npm 包。

5. 在其它项目中安装该 npm 包，即可使用封装的函数。例如：

```js
// 安装 npm 包
$ npm install my-common-utils

// 在项目中使用
const { add, subtract, multiply, divide } = require('my-common-utils');

console.log(add(1, 2));    // => 3
console.log(subtract(1, 2)); // => -1
console.log(multiply(1, 2)); // => 2
console.log(divide(1, 2));   // => 0.5
```

以上步骤是把常用函数封装成 npm

https://juejin.cn/post/7131406856240496647#heading-2

1. 用dumi搭建项目，这就需要用到dumi默认支持的father来打包。
2. 组件开发
3. 组件发布，注册市场账号，dumi已配置发布前默认打包，所以我们忽略打包环节

```
npm publish
# or 指定发布源
npm publish --registry http://registry.npmjs.org
```

发布之后就可以在npmjs官网上**查看自己的组件库**了，其他开发者也就可以使用这个组件库了。

## 9. 小程序分包限制，首屏优化

### 1. 为什么分包：

小程序的分包功能可以让开发者将一个大型小程序拆分成多个包，分别发布、更新和管理。这有助于提高小程序的下载速度和启动速度，并减少用户等待时间。

分包也能够让开发者更灵活地管理小程序的资源，例如，将不同的页面和功能放在不同的包中，方便维护和更新。例如，一个商城小程序可以将首页、商品分类、购物车和我的四个功能放在不同的包中，每个包都有自己的页面和资源。

另外，分包还能够帮助开发者更好地管理小程序的体积。例如，如果一个小程序的体积超过了限制，开发者可以通过分包来将小程序拆分成多个包，然后再分别上传，以避免超出体积限制的问题。

总之，分包可以为小程序带来诸多好处，例如提高下载速度和启动速度、提供更好的资源管理能力和支持大型小程序的开发等。

### 2. 如何分包：

~~非常简单，由于Taro是通过webpack方式进行构建打包的，所以无需考虑过度引用分包的问题。~~

分包的过程包括两部分：创建分包和配置分包。

首先，在小程序的开发者工具中，打开项目，点击左侧的“项目”菜单，然后选择“添加分包”。在弹出的对话框中，输入分包的名称和路径，然后点击“确定”按钮，即可创建分包。

接下来，开发者需要在小程序的 app.json 文件中配置分包。例如，下面是一个简单的例子，展示了如何配置一个名为 pages1 的分包：

```js
{
  "pages": [
    "pages/index/index",
    "pages/logs/logs"
  ],
  "subPackages": [
    {
      "root": "pages1",
      "pages": [
        "index/index",
        "logs/logs"
      ]
    }
  ]
}

```

上面的代码中，我们首先在 `pages` 数组中定义了主包中的页面，然后在 `subPackages` 数组中定义了一个名为 `pages1` 的分包。注意，在分包的页面路径中，不需要指定分包的根目录，例如，上面的代码中，分包中的页面 `index/index` 实际上位于 `pages1/index/index` 目录下。

通过上面的配置，我们就可以在分包配置完成后，小程序的开发者就可以开始在分包中添加页面和资源了。例如，我们可以在 `pages1` 分包中新建一个名为 `index.wxml` 的页面，并在其中添加一些文本和图片，来展示分包的效果。

```js
<!-- pages1/index/index.wxml -->
<view>
  <text>This is a page in the subpackage.</text>
  <image src="../../images/image.png" />
</view>

```

在页面中，你可以使用相对路径来引用分包中的图片和其他资源。例如，在上面的例子中，我们使用了 `../../` 前缀来表示当前目录的父目录的父目录，即分包的根目录，然后再加上图片的文件名，来引用图片。

最后，我们需要在小程序的主包中，添加一个页面，用来跳转到分包中的页面。

页面中，我们可以使用 `wx.navigateTo` 方法来跳转到分包中的页面。例如，下面的代码演示了如何从主包的首页跳转到 `pages1` 分包中的 `index/index` 页面：

```js
// pages/index/index.js
Page({
  onTap: function() {
    wx.navigateTo({
      url: '../../pages1/index/index'
    });
  }
});

```

上面的代码中，我们在首页的点击事件处理函数中调用了 `wx.navigateTo` 方法，并指定了分包中的页面路径，即 `../../pages1/index/index`。注意，在路径中，我们需要使用两个 `../` 前缀，来表示当前目录的父目录的父目录，也就是主包的根目录，然后再加上分包的名称和页面的相对路径，即可跳转到分包中的页面。

通过上面的步骤，我们就可以完成小程序的分包配置了。开发者可以按照需要，创建多个分包，并在主包和分包之间跳转，来实现大型小程序的开发。

### 3. 分包思想

C端分包采用的思想是：只提供给这个用户访问到的路径作为一个包。

在小程序启动时，默认会下载主包并启动主包内页面，当用户进入分包内某个页面时，客户端会把对应分包下载下来，下载完成后再进行展示。

用户在进入第一个页面的时候，就已经知道这个用户的可访问路径。这时候可以把用户可能访问的路径完整链路的放入一个包内。

如购课页用户只会访问到购课页相关的订单页、选课页、地址页、售后页，并不会访问到邀请有奖和其他活动页面，所以这就可以把购课页相关的页面放入一个包。

如果订单页多业务通用，则将订单页单独抽离出一个包。

### 4. 遇到的问题：

页面放入分包后，会对原有的页面路径改变，造成用户访问原来的页面404

1. 兜底方案1：保留原有的页面路径在主包中，只保留跳转逻辑代码，用户进入后可直接跳入到相应分包页面。
2. 兜底方案2：在入口文件app.ts didShow(小程序的onLaunch)加入路径页面判断跳转，跳转进入分包页面。

基于小程序更新机制，发布新版本小程序之后，无法立刻影响所有现网用户

1. 最差情况下是24小时完成全部版本下发更新(官方)
2. 在小程序入口增加UpdateManager管理更新

https://juejin.cn/post/6996569710548484109

https://docs.taro.zone/docs/compile-optimized

https://blog.csdn.net/yunchong_zhao/article/details/122584730

https://docs.taro.zone/docs/mini-split-chunks-plugin

## 10. 微信storage api 存token

微信小程序提供了一个 `wx.setStorage` 方法，可以用来设置一个键值对的数据。例如，下面的代码展示了如何使用 `wx.setStorage` 方法来存储一个 `token`：

```js
// 存储 token
wx.setStorage({
  key: 'token',
  data: 'abcdefg'
});
```

上面的代码中，我们通过调用 `wx.setStorage` 方法，并指定 `key` 和 `data` 两个参数，来存储一个名为 `token` 的键值对。其中，`key` 表示要存储的数据的名称，`data` 表示要存储的数据。

在存储完成后，小程序会将数据保存到本地，并且在用户关闭小程序再次打开时，还能够读取到之前存储的数据。例如，下面的代码展示了如何使用 `wx.getStorage` 方法来读取存储的 `token`：

```js
// 读取 token
wx.getStorage({
  key: 'token',
  success: function (res) {
    console.log(res.data);
  }
});
```

上面的代码中，我们通过调用 `wx.getStorage` 方法，并指定 `key` 参数，来读取存储的 `token` 数据。其中，`key` 表示要读取的数据的名称，`success` 回调函数用来处理读取成功的情况，读取的数据保存在 `res.data` 中。

通过使用 `wx.setStorage` 和 `wx.getStorage` 方法，开发者可以在小程序中方便地存储和读取数据，例如，用户的登录信息、小程序的配置信息等。

此外，微信小程序还提供了一些其他的存储方法，例如：

- `wx.setStorageSync` 方法：用于同步设置键值对的数据。
- `wx.getStorageSync` 方法：用于同步读取存储的数据。
- `wx.removeStorage` 方法：用于移除键值对的数据。
- `wx.clearStorage` 方法：用于清除所有的数据。

开发者可以根据自己的需要，选择适当的存储方法来使用。例如，如果不需要考虑性能，可以使用异步的 `wx.setStorage` 方法来存储数据；如果需要保证数据的实时性，可以使用同步的 `wx.setStorageSync` 方法来存储数据。

https://delaprada.com/2021/01/26/%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%E7%99%BB%E5%BD%95%E9%89%B4%E6%9D%83%E4%B8%8E%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF/

整个流程简单来说分为以下7步：

1. 前端调用`wx.login()`获取临时登录凭证`code`，并回传到开发者服务器。
2. 服务器调用[auth.code2Session](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html)换取**用户唯一标识OpenID和会话密钥session_key**。
3. 服务器端根据`OpenID`或`session_key`生成自定义登录态（可以理解为是`token`），将`token`响应给前端。
4. 前端将`token`存入`Storage`中。
5. 当前端之后向后端发起请求时，就会带上`token`。
6. 后台通过`token`（或者其他类型密钥），解密获取`OpenID`，判断是哪个用户的行为，做出响应的逻辑处理（比如操作数据库等）。
7. 后台响应数据给前端。

![image-20221202155911661](/Users/chenruo/Library/Application Support/typora-user-images/image-20221202155911661.png)

## 1. 你的优势是什么

喜欢软件开发和编写代码。
热衷于维护高质量、安全和性能优化的代码。
具有创造性和批判性思维。

## 2. 觉得比较难的功能开发是哪一块

一开始没搞懂，去网上看了个答案，一试发现这个广为流传的答案是有坑的，于是自己看 issue
发现还有一个小细节，然后解决了，谁知道还是在某种 edge case有问题，于是自己看规范看源码，搞定。

我们蒜厂主站重度使用了 CodeMirror 这个轮子（我在它上面封装了七八个模块），然而这个轮子的文档写得并不好，很多时候我们会遇到一些需求，而这些需求文档里又写得非常模糊，这就比较头疼了。所以很多时候，我就要去不断地从文档的字里行间猜测，并结合源码一步一步地去跟踪，去尝试解决这个问题。但有时候确实超出了我的能力范围，那么我就会把我的问题提炼成一个小 demo，到 StackOverflow 去问，或者问一些同样用这个轮子的作者，甚至干脆去 issue 里问作者。

重度使用mock.js mock数据的时候，文档其实有些地方写的不是很清楚，遇到一个问题是我根据语法mock出来数据的时候，数据都是同一个，不是随机且不同的，但我们需要随机的数据让模拟看起来更真实。

所以很多时候，我就要去不断地从文档的字里行间猜测，并结合源码一步一步地去跟踪，去尝试解决这个问题。

但有时候确实超出了我的能力范围，那么我就会把我的问题提炼成一个小 demo，到 StackOverflow 去问，或者问一些同样用这个轮子的作者，甚至干脆去 issue 里问作者。

Optimistic ui

为了让客户更快的去感受我们app的一个响应的感觉，本地组件的state加上后端的query回来的数据之后我们再更新本地state的东西。ui变了，但是数据没变。如果数据没对上，我们就重置就好了。

## 3. 你做过的项目/解决过的问题， 最让你自豪的有哪些

==主要做的一个亮点：==

写了一个脚本，获取所有翻译目录下的包含中文未翻译的文件形成excel，写了一个小工具去帮助前端高效率对接翻译人员。

```js
const fs = require('fs'); // 引入 fs 模块
const path = require('path'); // 引入 path 模块

// 定义要扫描的目录
const directory = './';

// 定义要扫描的文件类型
const fileTypes = ['.txt', '.md'];

// 获取目录下的所有文件
const files = fs.readdirSync(directory);

// 遍历所有文件，找到所有中文文件
const chineseFiles = files.filter(file => {
  // 获取文件的绝对路径
  const filePath = path.join(directory, file);

  // 判断文件是否为中文文件
  return fileTypes.includes(path.extname(filePath)) && /[\u4e00-\u9fa5]/.test(filePath);
});

// 输出所有中文文件的名称
console.log(chineseFiles);

```

## 4. 作为前端遇到最难的开发问题是什么

我个人感觉就是在深度的提升很难，比如 WebGL 的渲染优化，单纯使用第三方库很简单，但是当业务需求在低配的硬件上去优化渲染，这个时候就会很麻烦，就我个人而已技术积累不够就感觉很困难。还有就是可能因为是前端，对于算法方面或多或少会有点渣。

组件复用问题。由于我们一开始没有先做通用组件，所以造成了一些重复的实现，这些重复的实现又会变成潜在的 bug。////// 所以下一步打算打造自己的通用组件。

## 6. 你提到有个通用组件提取，具体做了哪些工作呢

在封装某个组件的时候，看这两个组件的使用功能上有什么共同点，又有什么不同点，把共同点提取出来之后写在封装组件中，在针对不同点进行细微的处理。

## 8. i18n怎么实现多语言切换

i18n（国际化）是一种将网站、应用程序或其他产品翻译成多种语言的方法。在实现 i18n 的过程中，通常需要满足以下几个步骤：

1. 首先，需要定义所有要支持的语言，并为每种语言创建一个语言文件。语言文件中包含了所有要翻译的字符串，并为每个字符串指定了对应的翻译。例如，在英语语言文件中，可能会定义一个名为 `hello` 的字符串，并将它翻译成 `Hello, world!`；在中文语言文件中，可能会定义一个名为 `hello` 的字符串，并将它翻译成 `你好，世界！`。
2. 然后，需要在应用程序中提供一种方法来切换语言。通常来说，应用程序会提供一个语言选择器，供用户选择所需的语言。例如，可能会在应用程序的顶部菜单中添加一个下拉菜单
3. 当用户选择语言时，应用程序就会根据用户的选择加载对应的语言文件，并将字符串的翻译应用到应用程序中。例如，如果用户选择了中文，应用程序就会加载中文语言文件，并将所有定义在语言文件中的字符串都替换成对应的翻译。
4. 在应用程序中，开发者可以使用某种国际化框架来实现 i18n 功能。例如，在 React 中，可以使用 `react-intl` 插件来实现国际化；在 Angular 中，可以使用 `@angular/localize` 模块来实现国际化。这些框架会提供一系列的方法和工具，帮助开发者更方便地处理 i18n 相关的问题。
5. 在应用程序中，开发者需要在组件中正确使用 i18n 功能，来实现字符串的翻译。例如，在 React 中，可以使用 `FormattedMessage` 组件来处理字符串的翻译；

==主要做的一个亮点：==

写了一个脚本，获取所有翻译目录下的包含中文未翻译的文件形成excel，写了一个小工具去帮助前端高效率对接翻译人员。

定义要扫描的目录

定义要扫描的文件类型

定义一个递归函数，用来遍历目录下的所有子目录

读取文件内容 const content = fs.readFileSync(filePath, 'utf-8');

```js
// 定义要扫描的目录
const directory = './';

// 定义一个递归函数，用来遍历目录下的所有子目录
function traverse(directory) {
  // 获取目录下的所有文件和子目录
  const items = fs.readdirSync(directory);

  // 遍历每一个文件和子目录
  items.forEach(item => {
    // 获取文件的绝对路径
    const itemPath = path.join(directory, item);

    // 如果当前项是一个文件夹，则递归遍历该文件夹
    if (fs.statSync(itemPath).isDirectory()) {
      traverse(itemPath);
    } else {
      // 如果当前项是一个文件，则读取文件内容
      const content = fs.readFileSync(itemPath, 'utf-8');

			// 判断文件内容中是否包含中文
      const regex = /[\u4e00-\u9fa5]/;
      if (regex.test(content)) {
        // 如果包含中文，则将文件名和中文内容保存到结果数组中
        results.push({
          fileName: item,
          content: content
        });
      }
    }
  });
}

// 定义一个结果数组，用来保存扫描到的中文文件
const results = [];

// 遍历目录
traverse(directory);

// 创建一个 excel 文档
const workbook = new exceljs.Workbook();

// 在文档中添加一个工作表
const worksheet = workbook.addWorksheet('Sheet1');

// 将数据写入工作表
worksheet.addRows(excelData);

// 保存文档
await workbook.xlsx.writeFile('exported-data.xlsx');
```

```js
const fs = require('fs'); // 引入 fs 模块
const path = require('path'); // 引入 path 模块

// 定义要扫描的目录
const directory = './';

// 定义要扫描的文件类型
const fileTypes = ['.txt', '.md'];

// 获取目录下的所有文件
const files = fs.readdirSync(directory);

// 遍历所有文件，找到所有中文文件
const chineseFiles = files.filter(file => {
  // 获取文件的绝对路径
  const filePath = path.join(directory, file);

  // 判断文件是否为中文文件
  return fileTypes.includes(path.extname(filePath)) && /[\u4e00-\u9fa5]/.test(filePath);
});

// 输出所有中文文件的名称
console.log(chineseFiles);

```

在上面的代码中，我们通过 `fs.readdirSync` 方法获取了目录下的所有文件，然后通过 `filter` 方法筛选出所有中文文件，最后输出所有中文文件的名称。

这只是一个简单的例子，实际情况可能会更复杂。例如，可能需要递归遍历目录下的所有子目录，或者需要处理更多的文件类型，等等。但是，上面的代码已经提供了一个基本的思路。复杂的处理方式：

1. 首先，需要定义一个函数，用来递归遍历目录下的所有子目录

```js
// 定义一个递归函数，用来遍历目录下的所有子目录
function traverse(directory) {
  // 获取目录下的所有文件和子目录
  const items = fs.readdirSync(directory);

  // 遍历每一个文件和子目录
  items.forEach(item => {
    // 获取文件的绝对路径
    const itemPath = path.join(directory, item);

    // 如果当前项是一个文件夹，则递归遍历该文件夹
    if (fs.statSync(itemPath).isDirectory()) {
      traverse(itemPath);
    }
  });
}

```

2. 然后，需要在递归遍历过程中，收集所有中文文件。可以在上面的函数中，增加一个参数 `files`，用来保存所有文件，并在遍历每一个文件时，判断是否为中文文件。
3. 最后，可以在遍历完所有文件后，输出所有中文文件的名称。

```js
// 定义要扫描的目录
const directory = './';

// 定义要扫描的文件类型
const fileTypes = ['.txt', '.md'];

// 定义一个递归函数，用来遍历目录下的所有子目录
function traverse(directory, files = []) {
  // 获取目录下的所有文件和子目录
  const items = fs.readdirSync(directory);

  // 遍历每一个文件和子目录
  items.forEach(item => {
    // 获取文件的绝对路径
    const itemPath = path.join(directory, item);

    // 如果当前项是一个文件夹，则递归遍历该文件夹
    if (fs.statSync(

```

2. 为了将所有中文文件的名称输出成 excel 格式，可以使用 `exceljs` 库。安装该库的方法如下：

```js
npm install exceljs --save
```

安装完成后，可以在代码中引入该库，并利用它来创建 excel 文档。例如：

```js
const exceljs = require('exceljs');

// 创建一个 excel 文档
const workbook = new exceljs.Workbook();

// 在文档中添加一个工作表
const worksheet = workbook.addWorksheet('Sheet1');

// 将所有中文文件的名称写入工作表
worksheet.addRows(chineseFiles);

// 保存文档
await workbook.xlsx.writeFile('chinese-files.xlsx');
```

为了在获取到文件后，将文件内容生成固定的 excel 格式，可以按照如下步骤来实现：

1. 首先，需要使用 `fs` 模块读取文件的内容，例如：

```js
// 定义要读取的文件路径
const filePath = './my-file.txt';

// 读取文件内容
const content = fs.readFileSync(filePath, 'utf-8');
```

1. 然后，需要对文件内容进行处理，将它转换成固定的 excel 格式。例如，如果文件内容是一个 JSON 格式的字符串，可以使用 `JSON.parse` 方法将其转换成对象，然后再将对象转换成 excel 格式。例如：

```js
// 将文件内容转换成对象
const data = JSON.parse(content);

// 将对象转换成 excel 格式
const excelData = data.map(item => [
  item.name,
  item.age,
  item.gender
]);
```

1. 最后，可以使用 `exceljs` 库将 excel 格式的数据写入 excel 文档。例如：

```
const exceljs = require('exceljs');
```

```
// 创建一个 excel 文档
const workbook = new exceljs.Workbook();

// 在文档中添加一个工作表
const worksheet = workbook.addWorksheet('Sheet1');

// 将数据写入工作表
worksheet.addRows(excelData);

// 保存文档
await workbook.xlsx.writeFile('exported-data.xlsx');
```

在上面的代码中，我们首先引入了 `exceljs` 库，然后使用它创建了一个 excel 文档，并在该文档中添加了一个工作表。接着，我们将 excel 格式的数据写入工作表，并保存文档。这样，就可以将文件内容生成固定的 excel 格式。

当然，这只是一个简单的示例，实际情况可能会更复杂。例如，可能需要对文件内容进行更复杂的处理，或者需要在 excel 文档中添加更多的工作表，等等。但是，上面的代码已经提供了一个基本的思路，可以帮助开发者理解如何在前端开发中将文件内容生成固定的 excel

在上面的代码中，我们首先引入了 `i18n` 库，然后调用了 `configure` 方法来初始化一个 `i18n` 对象。该方法接收一个配置对象，其中包含了多语言配置信息。例如，`locales` 属性指定了项目支持的语言列表，`directory` 属性指定了多语言资源文件的存放目录。

1. 接着，可以在项目中使用 `i18n` 对象的 `__` 方法来获取多语言资源。

```js
const i18n = require('i18n');

// 初始化 i18n 对象
i18n.configure({
  locales: ['en', 'zh-CN'],
  directory: __dirname + '/locales'
});

```



**安装插件 vue-i18n**

**创建语言包对象**

**组合对象**
**创建 i18n 实例**

**挂载对象**

https://blog.csdn.net/mynewdays/article/details/123960033

## 9. mock怎么使用的

mockJS实现拦截，是模拟了XMLHttpRequest对象。重写open、send等方法，方法调用时，只是普通函数的调用，不会发送真正的请求。

https://github.com/nuysoft/Mock/wiki/Getting-Started

## 10. vuex数据持久化

vuex-persistedstate 使用浏览器的本地存储（ local storage ）对状态（ state ）进行持久化。这意味着刷新页面或关闭标签页都不会删除你的数据。

Vuex 是一个专门为 Vue.js 应用程序开发的状态管理模式。它通过统一的状态树（Store）来管理应用程序的状态，从而实现状态的持久化。

Vuex 的数据持久化可以通过以下几种方式实现：

- 使用 vuex-persistedstate 插件。vuex-persistedstate 插件可以将 Vuex 的状态保存到浏览器的本地存储中，从而实现数据的持久化。使用该插件的方法如下：

```js
Copy code
// 安装插件
npm install vuex-persistedstate

// 在 Vuex 的 Store 中引入插件
import createPersistedState from 'vuex-persistedstate'

const store = new Vuex.Store({
  plugins: [createPersistedState()]
})
```

- 使用 localStorage。localStorage 是浏览器的本地存储，可以用来保存应用程序的状态。可以在 Vuex Store 的变更监听器（mutation 的观察者）中实现对 localStorage 的访问，从而实现数据持久化。代码如下：

```js
Copy code
const store = new Vuex.Store({
  state: {
    // 状态
  },
  mutations: {
    // 变更监听器
    updateState(state, payload) {
      // 更新状态
      state = Object.assign(state, payload)
      // 将状态保存到 localStorage
      window.localStorage.setItem('state', JSON.stringify(state))
    }
  }
})
```

- 使用 vuex-orm-localforage 插件。vuex-orm-localforage 插件可以将 Vuex 的状态保存到浏览器的 localForage 中，从而实现数据持久化。使用该插件的方法如下：

```js
// 安装插件
npm install vuex-orm-localforage

// 在 Vuex 的 Store 中引入插件
import createPersistedState from 'vuex-orm-localforage'

const store = new Vuex.Store({
  plugins: [createPersistedState()]
})
```

https://juejin.cn/post/7033927217511923743

## 11. redux 数据持久化

- 使用 redux-persist 插件。redux-persist 插件可以将 Redux 的状态保存到浏览器的本地存储中，从而实现数据的持久化。使用该插件的方法如下：

```
Copy code
// 安装插件
npm install redux-persist

// 在 Redux 的 Store 中引入插件
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage' // 指定存储方式（本地存储）

const persistConfig = {
  key: 'root', // 状态树的键名
  storage, // 存储方式
}

// 将插件应用到 reducer 上
const persistedReducer = persistReducer(persistConfig, rootReducer)

// 创建 Redux Store
const store = createStore(persistedReducer)

// 创建持久化存储器
const persistor = persistStore(store)
```

## 11. rsa非对称加密 前端

在上面的例子中，我们使用了 Web Cryptography API 来实现 RSA 非对称加密。Web Cryptography API 是一个用于实现密码学算法的标准接口，它提供了生成密钥对、导出密钥、加密数据、解密数据等功能。

另外，还有一些 JavaScript 库可以提供 RSA 非对称加密的功能，例如 Forge、crypto-js 等。使用这些库也可以实现 RSA 非对称加密，但是具体实现方式会有所不同。

总之，前端可以使用 JavaScript 和 Web Cryptography API 来实现 RSA 非对称加密，也可以使用一些 JavaScript 库来实现 RSA 非对称加密。不管使用哪种方法，实现 RSA 非对称加密的基本流程都是相似的，包括生成密钥对、加密数据、解密数据等。不过，每种方法的细节都有所不同，应该根据具体情况选择适合的方法来实现 RSA 非对称加密。

Web Cryptography API 是一个用于实现密码学算法的标准接口，它提供了生成密钥对、导出密钥、加密数据、解密数据等功能。

而 jsencrypt 是一个 JavaScript 库，它提供了实现 RSA 非对称加密的功能。它的功能与 Web Cryptography API 类似，但实现方式和细节有所不同。

两者的主要区别是：

- Web Cryptography API 是一个标准接口，可以跨平台使用，并支持多种浏览器。但它的功能比较有限，不支持一些特殊的加密方式。
- jsencrypt 是一个 JavaScript 库，只能在浏览器端使用。但它的功能比较丰富，可以实现一些特殊的加密方式。

因此，两者的适用场景有所不同。如果希望在多种平台和浏览器上实现 RSA 非对称加密，可以使用 Web Cryptography API。如果希望实现更复杂的加密方式，可以使用 jsencrypt。实际使用时应该根据具体情况选择适合的方法。

```js
// 生成密钥对
const keyPair = await window.crypto.subtle.generateKey(
  {
    name: 'RSA-OAEP',
    modulusLength: 2048,
    publicExponent: new Uint8Array([0x01, 0x00, 0x01]),
    hash: 'SHA-256',
  },
  true,
  ['encrypt', 'decrypt']
);

// 获取公开密钥
const publicKey = await window.crypto.subtle.exportKey('jwk', keyPair.publicKey);

// 获取私朁密钥
const privateKey = await window.crypto.subtle.exportKey('jwk', keyPair.privateKey);

// 加密数据
const encryptedData = await window.crypto.subtle.encrypt(
  {
    name: 'RSA-OAEP',
    hash: 'SHA-256',
  },
  keyPair.publicKey,
  data // 要加密的数据
);

// 解密数据
const decryptedData = await window.crypto.subtle.decrypt(
  {
    name: 'RSA-OAEP',
    hash: 'SHA-256',
  },
  keyPair.privateKey,
  encryptedData // 加密后的数据
);

```



![image-20221202160404739](/Users/chenruo/Library/Application Support/typora-user-images/image-20221202160404739.png)

![image-20221202160539573](/Users/chenruo/Library/Application Support/typora-user-images/image-20221202160539573.png)

https://juejin.cn/post/7075542251228626951

https://blog.csdn.net/junxuezheng/article/details/109824552

## 12. 上传图片后如何预览图片

把文件上传原理说一遍 上传后拿到FileList对象，。。。使用`base64`编码形式内容来显示文件
    
```html
<!DOCTYPE html>
<html>

<head>
    <title>image preview demo</title>
</head>

<body>
    <label for="file">file: </label>
    <input id="file" type="file">
    <img id="preview" src="" alt="demo" style="display: none;width: 200px;">
</body>

<script>
    var file = document.getElementById("file")
    var img = document.getElementById("preview")
    file.onchange = (evt) => {
        // 获取其中的第一个文件
        if (file.files.length > 0) {
            var reader = new FileReader()
            // reader处理的方式是异步的，所以要监听onload事件
            reader.onload = () => {
                img.style.display = "block"
                img.src = reader.result
            }
            // 读取文件内容
            // 其中的result字段就是需要的base64编码的内容
            reader.readAsDataURL(file.files[0])

        } else {
            img.style.display = "none"
        }
    }
</script>

</html>

```

## 13. 文件上传的原理

https://vue3js.cn/interview/NodeJS/file_upload.html

因为浏览器限制，浏览器不能直接操作文件系统的，需要通过浏览器所暴露出来的统一接口，由用户主动授权发起来访问文件动作，然后读取文件内容进指定内存里，最后执行提交请求操作，将内存里的文件内容数据上传到服务端，服务端解析前端传来的数据信息后存入文件里

对于文件上传，我们需要设置请求头为`content-type:multipart/form-data`

1. Input file 
2. FileList 对象

选中文件通过 HTMLInputElement.files 属性返回了一个 FileList 对象,这个对象是一个包含了许多 file 文件的列表。每个 file 对象包含了信息

3. FileReader or 对象 URL
   当我们获取到文件对象信息 files 了以后，我们要如何将他在页面上预览出来，这里提供了两种方法：FileReader 或者 对象 URL。

   1. FileReader 实现了一种异步的读取机制。他必须先通过 FileReader() 构造函数创建出一个 fileReader 实例。该实例实现了一下几个方法和事件（部分）：

      readerAsDataURL(file): 读取文件并以数据 URI 形式保存在 result 属性中

      load 事件：在文件加载成功后触发 load 事件

      error 事件：在文件加载失败后触发 error 事件

      progress 事件：在读取文件的过程中触发 progress 事件，该事件可以近似（间隔性触发，不是实时响应）监听文件上传进度。该方法有三个属性：lengthComputable（进度信息是否可用）, loaded（已经加载了多少）, total总共有多少。

   2. 对象 URL 指的是引用保存在 File 或 Blob 中的数据 URL。使用对象 URL 的时候不用像 FIleReader 一样要先把数据读取到 JavaScript 中，他可以引用 内存中 URL 地址而使用。

## 14. 校验图片

```js
/**
 * 图片上传校验
 * @param file
 * @param width
 * @param height
 * @param callBackMethod：回调方法
 * @author yys
 */
function checkImages(file, width, height, callBackMethod) {
  if (file.value) {
    /**
     * 0、参数准备
     *      fileStream：文件流
     *      fileSize：文件大小
     *      fileName：文件名称
     */
    var fileStream = file.files[0];
    var fileSize = fileStream.size;
    var fileName = fileStream.name;

    /**
     * 1、校验图片格式(png/jpg/git)
     */
    var reg = /\.(git|jpg|jpeg|png|GIF|JPG|PNG)$/;
    if (!reg.test(fileName)) {
      alert("图片格式限制[png/jpg/jpeg/git]~~");
      return;
    }

    /**
     * 2、校验图片大小(2M)
     *      fileSize：单位(B)
     */
    if (fileSize / 1024 > 2048) {
      alert("图片大小限制[2M]~~");
      return;
    }

    /**
     * 3、校验图片尺寸
     */
    var reader = new FileReader();
    reader.onload = function (e) {
      var data = e.target.result;
      // 加载图片获取图片真实宽度和高度
      var image = new Image();
      image.onload = function () {
        var realWidth = image.width,
          realHeight = image.height;
        if (width != realWidth || height != realHeight) {
          alert(
            "图片尺寸限制[" +
              width +
              "*" +
              height +
              "]，当前图片尺寸为[" +
              realWidth +
              "*" +
              realHeight +
              "]~~"
          );
          return;
        } else {
          // 校验通过 - 执行回调方法
          // setImagePreview - 图片预览等后续操作
          eval(callBackMethod)();
          // eval(callBackMethod)(width, height);
        }
      };
      image.src = data;
    };
    reader.readAsDataURL(fileStream);
  }
}

```

## 15. 小程序字体怎么响应

https://blog.csdn.net/w390058785/article/details/80562776

![image.png](http://tva1.sinaimg.cn/large/005NUwygly1h8f2so72qvj315g066adm.jpg)

## 16. Express

是一个基于 Node.js 平台的 web 应用框架。它提供了一组强大的特性，帮助你创建各种 web 应用和 API。

中间件（middleware）是指在请求和响应之间处理请求的函数。它能够访问请求对象（request object）、响应对象（response object）和应用程序的请求/响应循环（request/response cycle）。这允许它们改变请求和响应的数据，或者添加其他的处理逻辑。

例如，一个中间件函数可以用来验证用户身份，只有通过验证的用户才能访问应用程序的特定功能。或者，一个中间件函数可以用来处理所有请求的日志记录，以便了解应用程序的使用情况。

总之，中间件的作用是扩展应用程序的功能，使其更强大，同时提高代码的可维护性和可读性。

```js
const express = require('express');
const app = express();

// 定义一个中间件函数
function logger(req, res, next) {
  console.log(`${req.method} request received for ${req.url}`);
  next(); // 调用 next() 函数，将控制权交给下一个中间件函数
}

// 使用中间件
app.use(logger);

// 定义路由
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

// 启动服务器
const port = 3000;
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

```

上面的代码定义了一个名为 `logger` 的中间件函数，它接收请求对象、响应对象和 `next` 函数。在函数内部，它记录了请求的方法和 URL，然后调用了 `next` 函数，表示该中间件已经完成了它的工作，并将控制权交给了下一个中间件。

我们使用 `app.use()` 方法来注册中间件，这样所有的请求都会经过它。最后，我们定义了一个路由处理函数，响应所有请求。

当客户端向服务器发出请求时，请求会被传递给 `logger` 中间件函数，它会记录请求信息，然后调用 `next` 函数，交给下一个中间件，也就是路由处理函数。路由处理函数完成了响应.我们只定义了一个中间件函数，并使用了它。实际应用中，你可以定义多个中间件函数，并按照顺序注册它们，以便对请求进行不同的处理。

例如，你可以在 `logger` 中间件函数之后再注册一个用来验证用户身份的中间件函数，然后在验证通过的情况下再处理请求。

```js
const express = require('express');
const app = express();

// 定义中间件函数
function logger(req, res, next) {
  console.log(`${req.method} request received for ${req.url}`);
  next();
}

function authenticate(req, res, next) {
  // 检查用户身份
  if (authenticated) {
    // 验证通过，继续处理请求
    next();
  } else {
    // 验证失败，返回错误信息
    res.status(401).send('Authentication required');
  }
}

// 注册中间件
app.use(logger);
app.use(authenticate);

// 定义路由
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

// 启动服务器
const port = 3000;
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

```

我们注册了两个中间件函数：`logger` 和 `authenticate`。对于每个请求，它们都会按照注册的顺序依次执行，先处理日志记录，再验证用户身份。如果用户验证通过，就会调用 `next` 函数，让请求继续。

你可以根据需要，定义任意多个中间件函数，并按照顺序注册它们，来实现不同的处理逻辑。例如，你可以定义一个用来检查输入参数的中间件函数，然后再定义一个用来读取数据库的中间件函数，以便返回给客户端。

另外，中间件函数不仅仅能够用于处理所有请求，你还可以给它指定一个路径，表示它只能处理指定路径的请求。例如，下面的代码只会在请求路径为 `/hello` 时，调用 `hello` 中间件函数：

```js
app.use('/hello', hello);
```

总之，使用中间件函数能够让你更方便地扩展应用程序的功能，并使代码更具可维护性和可读性。

## 17 pc 和小程序兼容

移动端和 PC 端的样式兼容主要有以下几种方法：

- 使用媒体查询。媒体查询是 CSS3 中的一个特性，它允许我们根据媒体类型和设备特征来定义不同的样式。可以使用媒体查询来实现移动端和 PC 端的样式兼容，代码如下：

```
/* 移动端样式 */
@media screen and (max-width: 640px) {
  /* 样式定义 */
}

/* PC 端样式 */
@media screen and (min-width: 641px) {
  /* 样式定义 */
}
```

- 使用 Flexbox 布局。Flexbox 布局是 CSS3 中的一种布局模型，它可以让元素在父容器中的排列方式更加灵活。可以使用 Flexbox 布局来实现移动端和 PC 端的样式兼容，代码如下：

```
/* 父容器 */
.container {
  display: flex; /* 设置为 Flexbox 布局 */
  flex-direction: column; /* 设置元素的排列方式 */
}

/* 子元素 */
.item {
  flex: 1; /* 设置元素的尺寸 */
}
```

- 使用百分比单位。百分比单位可以让元素的尺寸和容器的尺寸保持一定的比例。可以使用百分比单位来实现移动端和 PC 端的样式兼容，代码如下：

```
Copy code
/* 容器 */
.container {
  width: 100%; /* 设置容器的宽度 */
}

/* 元素 */
.item {
```

- 使用响应式设计。响应式设计是一种设计方法，它能够让网页在不同的设备和屏幕尺寸下都能保持良好的用户体验。可以通过媒体查询、百分比单位、Flexbox 布局等方法来实现响应式设计，从而实现移动端和 PC 端的样式兼容。

## 18. 如何用webpack进行打包

Webpack 是一个模块打包工具，可以将多个模块合并成一个文件，方便在浏览器中运行。通常情况下，使用 webpack 进行打包的步骤如下：

1. 安装 webpack，这一步需要使用 npm 命令，具体方法可以参考 webpack 官网的说明。
2. 在项目的根目录下，创建一个名为 webpack.config.js 的配置文件，用来配置 webpack 打包的相关参数。
3. 在配置文件中，配置 webpack 打包的入口文件和输出文件。
4. 在配置文件中，配置 webpack 的加载器和插件。
5. 在项目的根目录下，执行 webpack 命令，开始打包。

下面是一个简单的 webpack 配置文件的例子，可以作为参考：

```js
const path = require('path');

module.exports = {
  // 配置打包的入口文件
  entry: './src/index.js',
  // 配置打包的输出文件
  output: {
    // 输出文件的文件名
    filename: 'bundle.js',
    // 输出文件的路径
    path: path.resolve(__dirname, 'dist')
  },
  // 配置加载器
  module: {
    rules: [
      // 处理 CSS 文件的加载器
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      // 处理图片文件的加载器
{
test: /.(png|jpg|jpeg|gif)$/,
use: [
{
loader: 'file-loader',
options: {
// 指定输出的图片文件名
name: '[name].[ext]',
// 指定输出的图片文件的路径
outputPath: 'images/'
}
}
]
}
]
},
// 配置插件
plugins: [
// 压缩 JavaScript 文件的插件
new UglifyJSPlugin()
]
};
```

上面的例子中，entry 属性指定了打包的入口文件是 src/index.js，output 属性指定了打包后的文件名是 bundle.js，输出路径是 dist 目录。

module 属性配置了一个加载器，用来处理 CSS 和图片文件的加载。

plugins 属性配置了一个插件，用来压缩 JavaScript 文件。

执行 webpack 命令后，会根据配置文件中的参数，将所有的模块合并成一个 bundle.js 文件，并输出到 dist 目录中。

当然，webpack 配置文件可以配置很多参数，实际项目中可以根据需要，进行更细致的配置。

## 19. viewport如何设置和使用

viewport 是一个 HTML 标签，它可以用来告诉浏览器如何渲染网页。当访问移动端的网页时，通常需要在页面的 head 标签中添加 viewport 标签，来控制网页的显示效果。

在移动端，浏览器默认会按照设备的实际宽度来渲染网页。这样的话，如果网页的宽度比设备的宽度大，则会出现横向滚动条；如果网页的宽度比设备的宽度小，则会出现空白区域。

为了避免这种情况，可以使用 viewport 标签来控制网页的显示效果。常用的 viewport 标签如下：

```js
Copy code
<!-- 宽度为设备宽度，缩放比例为 1 -->
<meta name="viewport" content="width=device-width,initial-scale=1">

<!-- 宽度为设备宽度，不允许用户缩放网页 -->
<meta name="viewport" content="width=device-width,user-scalable=no">

<!-- 宽度为设备宽度，缩放比例为 1，不允许用户缩放网页 -->
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
<!-- 宽度为设备宽度，缩放比例为 0.5，不允许用户缩放网页 -->
<meta name="viewport" content="width=device-width,initial-scale=0.5,user-scalable=no">
```

上面的例子中，width 属性指定了网页的宽度，initial-scale 属性指定了网页的缩放比例，user-scalable 属性指定了用户是否能够缩放网页。

可以根据实际需要，选择合适的 viewport 标签来控制网页的显示效果。通常情况下，移动端的网页会使用如下的 viewport 标签：

```js
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
```

这样的话，网页的宽度会自动设置为设备的宽度，缩放比例为 1，用户不能缩放网页。这样可以避免出现横向滚动条或空白区域，提高网页的显示效果。

当然，需要注意的是，使用 viewport 标签会对网页的布局造成一定的影响。如果需要使用 viewport 标签，则需要结合网页的实际情况，选择合适的标签来进行设置。

### 如何根据设备设置viewport值

可以使用 JavaScript 代码来根据设备的宽度来设置 viewport 的值。例如，在页面加载完成后，可以通过 window.innerWidth 属性来获取设备的宽度，然后根据宽度的值来决定 viewport 的值。

```js
// 当页面加载完成后
window.addEventListener('load', function() {
  // 获取设备的宽度
  var deviceWidth = window.innerWidth;

  // 如果设备宽度大于 1200px，则设置 viewport 的值为 1200px
  if (deviceWidth > 1200) {
    deviceWidth = 1200;
  }

  // 设置 viewport
  document.querySelector('meta[name=viewport]')
    .setAttribute('content', 'width=' + deviceWidth + ',initial-scale=1,user-scalable=no');
});

```

首先通过 window.innerWidth 属性来获取设备的宽度，然后判断宽度是否大于 1200px。如果设备宽度大于 1200px，则将宽度设置为 1200px。最后，通过 document.querySelector() 方法来获取 viewport 标签，然后通过 setAttribute() 方法来设置 viewport 的值。

通过上面的代码，可以根据设备的宽度来设置 viewport 的值，避免在不同设备上出现布局错误的问题。当然，具体的代码实现可以根据实际需要进行调整。

## 20. 洋葱模型

洋葱模型是一种软件架构模型，它描述了如何将一个系统分成多个不同的层次，并通过这些层次来进行模块化开发。

洋葱模型通常由多个层次组成，每个层次都具有不同的功能。例如，一个系统可能包括以下几个层次：

- 应用层：包含了与用户直接交互的业务逻辑和界面逻辑。
- 服务层：提供了与业务相关的服务，例如数据库操作、文件系统操作等。
- 中间件层：提供了与硬件相关的服务，例如网络通信、线程池管理等。
- 系统层：提供了与操作系统相关的服务，例如文件 I/O、进程管理等。

洋葱模型的优点在于，它提供了一种结构化的方法来设计系统，可以清晰地划分各个层次的职责，有助于开发人员更好地理解系统的结构，并方便系统的迭代和维护。

当然，洋葱模型也有一些缺点。例如，多层次的系统可能会导致系统的复杂度增加，并降低系统的性能。此外，多层次的系统也可能会导致更多的维护成本和沟通问题。因此，使用洋葱模型时需要权衡利弊，根据实际情况进行选择。

## 问招聘的

1. 薪资构成
2. 团队前端构成

![IMG_4683.PNG](http://tva1.sinaimg.cn/large/6fc56815gy1h72lfihp4ej21vo0v9h1q.jpg)
