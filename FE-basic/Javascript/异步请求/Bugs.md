# react

### 1. 无限死循环

“Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.”

由于两边都存在redirect的路径，来回互相跳转，导致报错，将第二个redirect注释掉即可跳转。

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20210817160639441.png" alt="image-20210817160639441" style="zoom:33%;" />

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20210817161628482.png" alt="image-20210817161628482" style="zoom:33%;" />

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20210817161646547.png" alt="image-20210817161646547" style="zoom:33%;" />

### 2. node后台启动

显示连接失败是因为后台没有启动

![image-20210822150213920](/Users/chenruo/Library/Application Support/typora-user-images/image-20210822150213920.png)

### 3. 请求时注意baseurl是https还是http

通过https://172.17.26.222:6789请求，出现报错。

是因为请求协议的问题，因为我当前请求是https的协议，而我的工程https协议也可以访问。所以我将请求协议由https换成了http。即可完成请求。

![image-20210822152355610](/Users/chenruo/Library/Application Support/typora-user-images/image-20210822152355610.png)

![image-20210822152449571](/Users/chenruo/Library/Application Support/typora-user-images/image-20210822152449571.png)

### 4. CORS error

![image-20210822161101583](/Users/chenruo/Library/Application Support/typora-user-images/image-20210822161101583.png)

### 5. 配置代理

 