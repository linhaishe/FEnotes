## 1. vue介绍

### 特点

1. 渐进式：可以在一个库和一套完整框架之间自如伸缩。可以是库，可以是框架。
2. 易用   只要会HTML、CSS、JavaScript就可以。
3. 生态系统完善      
4. 体积小
5. 超快虚拟DOM，在js里面，最费性能的是DOM操作。在更改或者渲染数据的时候，先改的是虚拟dom。等虚拟dom操作完毕，再统一渲染一次
6. 响应式的数据驱动，数据的双向绑定

### 模块框架库插件区别

| 名称 | 内容                                                         |
| ---- | ------------------------------------------------------------ |
| 框架 | 只要用了框架，整个项目，必须按照框架的语法去写。约束程序员的开发方式。 |
| 库   | 一堆功能的集合  引进库以后可以再想用的时候用他的功能，不会约  束项目的开发，想用就用。 |
| 插件 | 基于某个语言，扩展这个语言的功能。一般都是具体的某一个功能，比如jquery日历 |
| 模块 | 在项目开发的过程中。一个功能，封装成一个模块。模块是使用方式的不同。 |

[vue official site](https://cn.vuejs.org/v2/guide/)

```html
<!-- 开发环境版本，包含了有帮助的命令行警告 -->
<!-- 适合新手上手,会有信息命令提示 -->

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>

<!-- 生产环境版本，优化了尺寸和速度 -->
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

## 2. 如何引入

1. cdn
2. 安装相应软件
3. npm 引入 vue-cli

## 3. 基本样式

1. 导入开发版本的vue.js,引入script
2. 创建vue实例对象，设置el和data属性

```js
var app = new Vue({
  el: "#app",
  data: {
    message: "Hello Vue yoyo!",
  },
});
```

3. 使用简介版的语法将数据渲染到页面上

```html
<div id="app">{{ message }}</div>
```

## 4. el挂载点

el是用来设置vue实例挂载的元素

通过css选择器，设置vue实例管理的元素。el中命名的元素的内部，可以不断嵌套内容，内容会被data中同名的数据进行替换。

```js
var app = new Vue({
  el: "#app",
  data: {
    message: "Hello Vue yoyo!",
  },
});
```

```html
    <div id="app">
      {{ message }}
      <span>{{ message }}</span>
    </div>
```

### vue实例的作用范围

vue会管理el选项命中的元素及其内部的后代元素

1. 通过css选择器，设置vue实例管理的元素。el中命名的元素的内部，可以不断嵌套内容，内容会被data中同名的数据进行替换。
2. 只支持双标签，因为我们要在标签内添加元素
3. 不能将el挂载点挂在body或html上
4. 建议el挂载点挂在div上，可以使用其他选择器，但是建议使用id选择器

![5908A2E65960509FC3DBA910D0755558.jpg](http://ww1.sinaimg.cn/large/005NUwygly1grokekqtu8j30vq096jt1.jpg)

## 🐒vue的生命周期

## 5. data属性

1. vue中用到的数据定义在data中
2. data中可以写复杂类型的数据
3. 渲染复杂类型数据时，遵守js语法即可

## 6. vue-指令

是指以v-开头的一组特殊语法

### v-text

1. 设置标签的文本值(text-content)
2. 如果将v-text写在标签内，那么标签内的内容会被全部覆盖，即使标签内写了其他的data属性。
3. 使用差值表达式{{}}可以替换指定内容
4. 差值表达式{{}}可以放函数
5. 内部支持写表达式

```html
    <div id="app">
      {{ message }}
      <span>{{ message }}</span>
      <h2 v-text="message+'!'"></h2>
      <h2>深圳{{ message +"!"}}</h2>
    </div>
```

### v-html

1. 设置标签的innetHTML
2. n内容中有html结构会被解析为标签
3. v-text指令无论内容是什么，只会解析为文本
4. 解析文本只用v-text,需要解析html结构使用v-html

```html
<div id="app">
<p v-html="content"></p>
</div>
```

```js
var app = new Vue({
  el: "#app",
  data: {
    //content: "Hello Vue",
    content: "<a href='#'>Hello Vue</a>"
  },
});
```

### v-on

1. 为元素绑定事件
2. 事件名不需要写on
3. 指令可以简写为@
4. 绑定方法写在method属性中
5. 方法内部通过this关键字可以访问定义在data中的数据
6. 传递自定义参数，事件绑定的方法写成函数调用的形式，可以传入自定义参数。定义方法时，需要定义形参来接受传参。
7. 事件修饰符。事件后面跟上<mark>.修饰符</mark>可以对事件进行限制。例如.enter可以限制出发的案件为回车
8. 事件修饰符官网参考：[事件修饰符](https://cn.vuejs.org/v2/guide/events.html#%E4%BA%8B%E4%BB%B6%E4%BF%AE%E9%A5%B0%E7%AC%A6)

```html
<div id="app">
<input type="button" value="事件绑定" v-on:click="doIt"></input>
<input type="button" value="事件绑定" v-on:mouseenter="doIt"></input>
<input type="button" value="事件绑定" @mouseenter="doIt"></input>
</div>
```

```js
var app = new Vue({
  el: "#app",
  methods: {
    doIt: function(){
    //logic
    }
  },
});
```

事件修饰符官网参考：[事件修饰符](https://cn.vuejs.org/v2/guide/events.html#%E4%BA%8B%E4%BB%B6%E4%BF%AE%E9%A5%B0%E7%AC%A6)

- `.stop`
- `.prevent`
- `.capture`
- `.self`
- `.once`
- `.passive`（告诉浏览器你不想阻止事件的默认行为）

```html
<!-- 阻止单击事件继续传播,阻止事件冒泡 -->
<a v-on:click.stop="doThis"></a>

<!-- 提交事件不再重载页面，阻止浏览器默认事件 -->
<form v-on:submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a v-on:click.stop.prevent="doThat"></a>

<!-- 点击事件将只会触发一次 -->
<a v-on:click.once="doThis"></a>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div v-on:click.self="doThat">...</div>
```

使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用 `v-on:click.prevent.self` 会阻止**所有的点击**，而 `v-on:click.self.prevent` 只会阻止对元素自身的点击。

### v-show

1. 根据表达值的真假，切换元素显示和隐藏
2. 指令后面的内容，最终都会解析为布尔值
3. 值为true元素显示，值为false元素隐藏

```html
<div id="app">
<input type="button" value="切换显示状态" @click="changIsShow" />
<input type="button" value="年龄累加" @click="addAge" />

<img src="" v-show="true"></img>
<img src="" v-show="isShow"></img>
<img src="" v-show="age>=18"></img>
</div>
```

```js
var app = new Vue({
  el: "#app",
  data: {
    isShow: false,
    age: 17,
  },
  methods: {
    changIsShow: function () {
      this.isShow = !this.isShow;
    },
    addAge: function () {
      this.age++;
    },
  },
});

```

### v-if

1. 根据表达值的真假，切换元素的显示和隐藏
2. 操作的是DOM元素来切换显示状态
3. 频繁切换使用v-show，反之使用v-if，前者的切换性能消耗小

```html
<div id="app">
<p src="" v-if="true"></p>
<p src="" v-if="isShow"></p>
<p src="" v-if="age>=18">使用表达式判断</p>
</div>
```

```js
var app = new Vue({
  el: "#app",
  data: {
    isShow: false,
    age: 17,
  },
  methods: {
    changIsShow: function () {
      this.isShow = !this.isShow;
    },
    addAge: function () {
      this.age++;
    },
  },
});
```

### v-bind

1. 设置元素的属性
2. 完整的写法 `v-bind:属性名`
3. 简写`:src="imgSrc"`
4. 需要动态的增删class建议使用对象的方式

```html
    <div id="app">
      <img v-bind:src="imgSrc" alt="" />
      <img v-bind:title="imgTitle+'!!!'" alt="" />
      <img v-bind:class="isActive?'active:''" alt="" />
      <img v-bind:class="{active:isActive}" alt="" />
    </div>
    
		<div id="app">
      <img :src="imgSrc" alt="" />
      <img :title="imgTitle+'!!!'" alt="" />
      <img :class="isActive?'active:''" alt="" />
      <!--需要动态的增删class建议使用对象的方式-->
      <img :class="{active:isActive}" alt="" />
    </div>
    
       <div id="app">
      <img v-bind:src="imgSrc" alt="" height="300px" width="300px" />
      <br />
      <img
        :src="imgSrc"
        :title="imgTitle+'!!!'"
        :class="isActive?'active':''"
        alt=""
        height="300px"
        width="300px"
        @click="toogleActive"
      />
      <br />
      <img
        :src="imgSrc"
        :title="imgTitle+'!!!'"
        :class="{active:isActive}"
        alt=""
        height="300px"
        width="300px"
        @click="toogleActive"
      />

      <br />
      <!-- <img v-bind:class="isActive?'active:''" alt="" />
      <img v-bind:class="{active:isActive}" alt="" /> -->
    </div>
 
    
```

```js
var app = new Vue({
  el: "#app",
  data: {
    imgSrc:
      "https://images.unsplash.com/photo-1565538420870-da08ff96a207?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2250&q=80",
    isActive: false,
    imgTitle: "lovely pic",
  },
  methods: {
    toogleActive: function () {
      this.isActive = !this.isActive;
    },
  },
});

```

### v-for

1. 根据数据列表生成列表结构
2. 数组经常和v-for结合使用
3. 语法是`v-for="(vegName,index) in vegs"`
4. Item 和 index 可以和其他指令一起使用
5. 数组长度的更新会同步到页面上，是响应式的。

```html
    <div id="app">
      <input type="button" value="添加数据" @click="add" />
      <input type="button" value="移除数据" @click="remove" />
      <h2 v-for="(vegObj,index) in vegs" v-bind:title="vegObj.name">
        第{{index+1}} 个水果:{{vegObj.name}}
      </h2>
      <h2 v-for="item in arr">中国的城市{{item}}</h2>
    </div>
```

```js
      var app = new Vue({
        el: "#app",
        data: {
          arr: ["北京", "shanghai", "guangzhou", "shenzhen"],
          vegs: [{ name: "banana" }, { name: "apple" }],
        },
        methods: {
          add: function () {
            this.vegs.push({ name: "orange" });
          },
          remove: function () {
            this.vegs.shift();
          },
        },
      });
```

### v-model

1. 便捷的设置和获取表单元素的值
2. 绑定的数据会和表单元素值相关联
3. 获取和设置表单元素的值(双向数据绑定)：更改两边的一边的值，那么另一边的值也会同步更新。
4. 多选必须是数组来接收数据

```html
    <div id="app">
      <input type="button" value="修改msg的值" @click="setMsg" />
      <input type="text" v-model="message" @keyup.enter="getMsg" />
      <h2>{{message}}</h2>
    </div>
```

```js
      var app = new Vue({
        el: "#app",
        data: {
          message: "输入框文本同步更新为message",
        },
        methods: {
          getMsg: function () {
            alert(this.message);
          },
          setMsg: function () {
            this.message = "已修改";
          },
        },
      });

```

### v-keyup.keycode

1. @事件.键码,有按键码别名的尽量使用别名
2. @事件.对应的英文 up right down left
3. ctrl 要用键码
4. ctrl相当于 ctrlKey
5. 自定义别名Vue.config.keyCodes.ctrl1 = 17

**组合键使用**

```
<!-- Alt + C -->
<input v-on:keyup.alt.67="clear">

<!-- Ctrl + Click -->
<div v-on:click.ctrl="doSomething">Do something</div>
```

**按键码别名**

- `.enter`
- `.tab`
- `.delete` (捕获“删除”和“退格”键)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`

**[按键修饰符](https://cn.vuejs.org/v2/guide/events.html#按键修饰符)**

```
<!-- 只有在 `key` 是 `Enter` 时调用 `vm.submit()` -->
<input v-on:keyup.enter="submit">
```

## 7. 🐒计算属性和侦听器

计算属性一般没有set方法，只作为只读属性。

![image.png](http://tva1.sinaimg.cn/large/005NUwyggy1gzyab53tdhj31c40z6qfm.jpg)

![image.png](http://tva1.sinaimg.cn/large/005NUwyggy1gzyabpam6wj31280ikgpe.jpg)

[计算属性和侦听器](https://cn.vuejs.org/v2/guide/computed.html)

| 计算方式       | 区别                                                         |
| -------------- | ------------------------------------------------------------ |
| 表达式方法调用 | 一般不建议用。是要绑定的任意数据改变，都会重新调用。比较浪费性能，没有缓存 |
| computed       | 大部分都用计算，性能得到优化，会缓存数据。                   |
| watch          | 可以进行异步操作。                                           |

[例子html part](https://github.com/linhaishe/hello-vue/blob/main/shopChart.html)

[例子js part](https://github.com/linhaishe/hello-vue/blob/main/js/shopChart.js)

## 8. 组件

## 9. productionTip

`Vue.config.productionTip = false`

设置为false以阻止vue在启动时生成生产提示

## 10. 根组件渲染

```js
//main.js 文件中的内容

//引入vue模块 如果直接写模块名 从node_module找
import Vue from 'vue'
//app最大的根组件
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  //el:'#app'
  //意思是先渲染完虚拟dom树然后再找#app进行关联和挂载
  render: (h)=>h(App),
}).$mount('#app'); //手动挂载
```

![D3279CE7AADFEB021161D76AD80BED53.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grt4hgshtej61060rgjug02.jpg)

## 12. 组件中的name属性

方便调试

```
<script>
  import HelloWorld from './components/HelloWorld.vue'
  import Event from './utils/event'

  export default {
    name: 'App',
    components: {
      HelloWorld
    },
    data:function(){
      return {
        msg:"今天好热"
      }
    },
    methods:{
      send(){
        Event.$emit('aaa',this.msg)
      }
    }
  }
```

## 13. Style scoped

```css
/*规定样式只作用于当前组件*/
<style scoped></style>
/*不加scoped 则是修改全局属性*/
```

## 14. Router

[router official site](https://router.vuejs.org/zh/installation.html)

### 1. hash 和 history 的区别

在下载的时候会提示,use history mode for router?，如果选择不使用history模式，则会选择hash模式进行路由开发

多个路由切换的最下面要写`<router-view />`,才能进行路由切换

### 1. 动态路由

App.vue中写所有路由的组件，用router-link包裹

```vue
//App.vue
<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ path: '/', query: { a: 1, b: 2 } }"
        >query传数据：{ path: '/', query: { a: 1 } },类似get</router-link
      >
      <br />
      <router-link
        :to="{
          path: '/about',
          name: 'About',
          params: { id: 'foo', b: 222 },
        }"
        >params传数据：{ path: '/about', name: 'About', params: { a: 1, b: 222 }
        },类似post</router-link
      >
      <br />
      <router-link to="/list?aa=11&bb=22">/list?aa=11&bb=22</router-link> <br />
      <router-link to="/list/data1/data2">/list/data1/data2</router-link>
    </div>
    <router-view />
  </div>
</template>
```

Index.js文件中控制所有路由

```js
//index.js
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/list",
    name: "Testand",
    component: () => import("../views/Test&.vue"),
  },

  {
    path: "/about/:id",
    name: "About",
    // beforeEnter(to, from, next) {
    //   console.log(to);
    //   console.log(from);
    //   next();
    // },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/About.vue"),
    children: [
      {
        path: "",
        name: "TestA",
        component: () => import("../views/TestA.vue"),
      },
      {
        path: "profile",
        name: "TestB",
        component: () => import("../views/TestB.vue"),
        // beforeEnter(to, from, next) {
        //   console.log(to);
        //   console.log(from);
        //   next();
        // },
      },
      {
        path: "posts",
        name: "TestC",
        component: () => import("../views/TestC.vue"),
      },
    ],
  },
  {
    path: "/list/:data1/:data2",
    name: "List",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/List.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;

```

### 2. 路由传参

```vue
 <router-link :to="{ path: '/', query: { a: 1, b: 2 } }"
        >query传数据：{ path: '/', query: { a: 1 } },类似get</router-link
      >
      <br />
      <router-link
        :to="{
          path: '/about',
          name: 'About',
          params: { id: 'foo', b: 222 },
        }"
        >params传数据：{ path: '/about', name: 'About', params: { a: 1, b: 222 }
        },类似post</router-link
      >
      <br />
      <router-link to="/list?aa=11&bb=22">/list?aa=11&bb=22</router-link> <br />
      <router-link to="/list/data1/data2">/list/data1/data2</router-link>
```

### 3. 嵌套路由

```vue
    //about.vue
		<p>
      <router-link to="/about/foo">/user/foo</router-link> |
      <router-link to="/about/foo/profile">/user/foo/profile</router-link> |
      <router-link to="/about/foo/posts">/user/foo/posts</router-link>
    </p>
    <router-view></router-view>
```

```js
//index.js
  {
    path: "/about/:id",
    name: "About",
    component: () => import("../views/About.vue"),
    children: [
      {
        //可以写路由全路径/"/about/:id，也可以写缩写"",表示父路由的根目录下
        path: "",
        name: "TestA",
        component: () => import("../views/TestA.vue"),
      },
      {
        // //可以写路由全路径/"/about/profile
        path: "profile",
        name: "TestB",
        component: () => import("../views/TestB.vue"),
      },
      {
        path: "posts",
        name: "TestC",
        component: () => import("../views/TestC.vue"),
      },
    ],
  },

```

### 4. 通过js跳转页面并传参

` this.$router.push({path,name,params,query}}) `

`this.$router.push('/xxx') `

` this.$router.back();`

` this.$router.forward();` 

` this.$router.go();`

```vue
<!--Home.vue-->
<template>
  <div class="home">
    <button @click="goAbout">去about</button>
    <h1>This is a Home page</h1>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    //HelloWorld,
  },
  mounted() {
    console.log(this.$route.query);
  },
  methods: {
    goAbout() {
      this.$router.push({
        path: "/about",
        name: "About",
        params: { name: "heather" },
      });
    },
  },
};
</script>

```



### 5. 路由守卫

a. 在路由配置里面 index.js,beforeEnter(to,from,next){}

```js
//index.js
  {
    path: "/about/:id",
    name: "About",
    // beforeEnter(to, from, next) {
    //   console.log(to);
    //   console.log(from);
    //   next();
    // },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/About.vue"),
    children: [
      {
        path: "",
        name: "TestA",
        component: () => import("../views/TestA.vue"),
      },
      {
        path: "profile",
        name: "TestB",
        component: () => import("../views/TestB.vue"),
        //这里写路由守卫，在对应的路由下写路由守卫，beforeEnter
        beforeEnter(to, from, next) {
          console.log(to);
          console.log(from);
          next();
        },
      },
      {
        path: "posts",
        name: "TestC",
        component: () => import("../views/TestC.vue"),
      },
    ],
  },
```

b. 在组件里面,beforeRouteEnter(to,from,next){}

```vue
<script>
  //About.vue
export default {
  name: "About",
  methods: {
    goList() {
      this.$router.push({
        path: "/list/data1/data2",
        name: "List",
        params: { name: "heather" },
      });
    },
    refresh() {
      this.$router.go(0);
    },
  },
  mounted() {
    console.log("about params data", this.$route.params);
    console.log("about params data", this.$route);
  },
  beforeRouteEnter(to, from, next) {
    console.log(to);
    console.log(from);
    next();
  },
};
</script>
```



### 6. 路由的两种模式

1. 一种是历史记录 类似文件路径的格式
2. 一种是hash锚点的形式

区别：

1. 地址不相同，hash看的是#xxxx,history是 /xxx/xxx
2. 对于hash，onhashchange->hash变了，会加载对应的模块
3. 对于history，history.pushState  监控历史记录状态
4. 平时用那种模式要看后台。history必须要后台支持是因为，有一种开发模式叫做restFUl开发模式

## 15. 按钮标签名的替换

加tag="标签名" 属性

## 16. css exact

router-link-exact-active, router-link-active

有了exact后，设定的点击的link才会有样式改变。

```css
#nav a.router-link-exact-active {
  color: #42b983;
}
```

```vue
<router-link :to="{ path: '/', query: { a: 1, b: 2 } }">query传数据：{ path: '/', query: { a: 1 } },类似get</router-link>
```

## 17. VUEX

### info

它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。管理共享状态。

## 18. axios

不用juqery 的 ajax ， 因为它都是操作dom树的，不建议在bue中使用。

Ajax i/o system,做前后台交互，本质还是ajax

```js
      this.$axios({
        url: "/",
        method: "get",
        data: {
          username: "heather",
          password: 123,
        },
      }).then((res) => console.log(res.config.data))..catch((err)=>{}) 

```

```js
    //cors的配置
        app.all('*',function(req,res,next){
            if(req.path !== '/' && !req.path.includes('.')){
            res.set({
            'Access-Control-Allow-Credentials': true, //允许后端发送cookie
            'Access-Control-Allow-Origin': req.headers.origin || '*', //任意域名都可以访问,或者基于我请求头里面的域
            'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type', //设置请求头格式和类型
            'Access-Control-Allow-Methods': 'PUT,POST,GET,DELETE,OPTIONS',//允许支持的请求方式
            'Content-Type': 'application/json; charset=utf-8'//默认与允许的文本格式json和编码格式
            })
            }
            req.method === 'OPTIONS' ? res.status(204).end() : next()
        })
```



## xx. Bug

报错：

[vue-router] missing param for named route "About": Expected "id" to be defined

```js
 //index.js 
{
    path: "/about/:id",
    name: "About",
		component: () => import("../views/About.vue"),
}
```

```vue
<!--App.vue-->
<!--路由组件-->
      <router-link
        :to="{
          path: '/about',
          name: 'About',
          params: { b: 222 },
        }"
        >params传数据：{ path: '/about', name: 'About', params: { a: 1, b: 222 }
        }</router-link
      >

```

原因：由于路径使用的是动态路由` path: "/about/:id"`,传输的数据中规定需要有动态id的值，所以在传递的时候必须要传递,否则会报错。将id设置为之后的所需的路径值比如例子中的id:'foo',因为路径都在foo后动态传输数据。




















## 面试题

### 1. vue是什么样的框架，你对他有什么了解。他有什么特点。相对于其他框架有什么区别
### 2. v-show和v-if区别

1. 显示隐藏的控制方式不同，

2.  v-show  通过display来控制。

3. v-if   通过节点的添加和删除

4. 如果是频繁的显示隐藏。v-show

5. 如果是不频繁的操作，建议使用v-if 因为如果是false不用创建元素插入

6. v-show  可以缓存一些数据

7. v-if 不能缓存

###  什么是数据的双向绑定

1. html里面的数据 和new Vue({data:}) 进行了相互绑定。

2. 页面变了 data就会变， data变了，页面跟着变

3. 视图层  数据层（data）

### 什么是虚拟dom

### 什么是mvvm

mvc

m model  数据层

v view   视图层

c controller 控制层

mvvm 
1. m model  数据层
2. v view   视图层

c变成了vm
vm view-model  数据和视图双向绑定





