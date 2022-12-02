# uni-app cli开发方式配置eslint + commitlint + stylelint

团队的项目小程序所使用的框架最后确定使用Uni-app，官方的框架未配置eslint等相关规则，则需要我们手动去配置。由于是第一次搭建项目框架，需要学习的地方还有很多，如果有不足的可以友善提建议，和善沟通。

编译器软件：webstorm，电脑：MAC

查阅相关资料后，其实uni-app中用vue cli模式搭建项目，其实和普通的vue项目没有什么区别，所以此配置方法也适用于平常项目中。

## Setup Uni-app w vue-cli 

[官网就有，请移步官网。](https://uniapp.dcloud.net.cn/quickstart-cli.html)

## ESlint

> ESLint is an open source project that helps you find and fix problems with your JavaScript code. It doesn't matter if you're writing JavaScript in the browser or on the server, with or without a framework, ESLint can help your code live its best life.

### 1. Installing and Configuring ESLint

根据[eslint npm](https://www.npmjs.com/package/eslint)的教程，选择官网写好的初始化命令`npm init @eslint/config`进行安装和配置。会有相关的问题针对你的项目特性来安装对应的依赖。会自动在根目录下生成.`eslintre.js`配置文件。在rules中添加系列规则后，能正常检测出代码规范问题。

我们团队使用airbnb的code style,初始化命令根据我所选择的内容下载了这些依赖。

`eslint-plugin-vue@latest eslint-config-airbnb-base@latest eslint@^7.32.0 || ^8.2.0 eslint-plugin-import@^2.25.2`



<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4qczbrh0dj21140oqwmx.jpg" alt="image.png" style="zoom:50%;" />

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4qd21vz17j20n00sw436.jpg" alt="image.png" style="zoom:50%;" />

到这一步其实已经算是配置成功了，但我们还需要单独处理下vue文件的格式问题。可以看到`App.vue`文件下的`<script>`标签的缩进有问题，`export default`是处于一个顶格的状态，我们需要的是每级标签缩进为2，这边我们就需要通过新增`overrides`去覆盖原有的代码风格规则。并在`rules`中添加针对vue文件`script`标签的缩进规则。即可。

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rbcpra4bj20qk0oe0xb.jpg" alt="image.png" style="zoom: 50%;" />

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rblk9dr2j20l40pctcf.jpg" alt="image.png" style="zoom:50%;" />

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rbmgyxjsj20qw0s6gr8.jpg" alt="image.png" style="zoom: 50%;" />

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rbmgyxjsj20qw0s6gr8.jpg" alt="image.png" style="zoom: 50%;" />

```js
// .eslintrc.js
module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'plugin:vue/vue3-essential',
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: [
    'vue',
  ],
  rules: {
    semi: ['error', 'always'],
    quotes: ['error', 'single'],
    'vue/script-indent': [
      'error',
      2,
      {
        baseIndent: 1,
      },
    ],
  },
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        indent: 0,
      },
    },
  ],
};

```

针对vue 的eslint配置到此完成，团队可以根据自己的需求在rules中开启或关闭规则。

### 2. Configuring .eslintignore

有些文件我们是不希望ESlint进行代码风格检测的，这时候我们就需要创建` .eslintignore`，告诉ESLint不去检查这些文件。[link](https://eslint.org/docs/latest/user-guide/configuring/ignoring-code#the-eslintignore-file)

```
build/*.js
src/assets
public
dist
/node_modules
```

### 3. ESlint fix

[more command line](https://eslint.org/docs/latest/user-guide/command-line-interface)

list some basic usage:

Most users use [`npx`](https://docs.npmjs.com/cli/v8/commands/npx) to run ESLint on the command line like this:

`npx eslint [options] [file|dir|glob]*`

```cmd
# Run on two files
npx eslint file1.js file2.js

# Run on multiple files
npx eslint lib/**
```

Fix command:

`npx eslint file1.js file2.js --fix`

## Stylelint

> A mighty, modern linter that helps you avoid errors and enforce conventions in your styles.

### 1. Installing and Configuring Stylelint

1. npm install dependents 

   `npm install --save-dev stylelint stylelint-config-standard`

   建议扩展一个共享配置，包括你喜欢的语言或库的适当语法。例如，可以扩展`stylelint-config-standard-scss`的共享配置来检测SCSS。

   vue项目下还需要下载针对vue的依赖 `stylelint-config-recommended-vue`

2. Root dir下创建`stylelint.config.js`文件夹，初始化规则。

```js
module.exports = {
  root: true,
  extends: ['stylelint-config-standard', 'stylelint-config-recommended-vue', 'stylelint-config-standard-scss'],
  rules: {
    'comment-no-empty': true, // 禁止空注释
  },
  ignoreFiles: ['**/*.js', '**/*.jsx', '**/*.tsx', '**/*.ts'],
};
```

### 2. Configuring .stylelintignore

用法和`.eslintignore`相同，就不过多赘述。

```
/dist/*
/public/*
public/*
```

### 3. stylelint fix

Run Stylelint on all the SCSS files in your project:

`npx stylelint "**/*.scss"`

use Stylelint to lint both CSS and JavaScript files:

`npx stylelint "**/*.{css,js}"`

fix all vue and scss files:

`npx stylelint "**/*.{vue,scss}" --fix`

### 4. 一些报错和问题

#### 1. Class extends value undefined is not a constructor or null

  会报以下错误 `[stylelint gives error "Class extends value undefined is not a constructor or null"`

  安装postcss依赖解决问题。

  `npm i --save-dev postcss`

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4rdx7r017j21pm0bcdnz.jpg)

#### 2. 无法解析vue文件

vue文件中的script 和 style 标签中的代码检测失败。 stylelint 是不能直接解析 vue 文件、 html 文件等的，会报出一堆错误

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rf9an2i4j21ca100ap2.jpg" alt="image.png" style="zoom:50%;" />

需要用内置的自定义语法 `postcss-html` 来解析

`npm i --save-dev postcss-html`

添加`customSyntax: 'postcss-html',`

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4rfexyv2uj21a80jytfv.jpg)

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4rfdw1u6gj21j016swsm.jpg)

#### 3. vue中style标签的缩进问题

优化下。`overrides`下针对相关文件新增对应rules。

```js
module.exports = {
  root: true,
  extends: ['stylelint-config-standard', 'stylelint-config-recommended-vue', 'stylelint-config-standard-scss'],
  customSyntax: 'postcss-html',
  rules: {
    'comment-no-empty': true,
  },
  ignoreFiles: ['**/*.js', '**/*.jsx', '**/*.tsx', '**/*.ts'],
  overrides: [{
    files: ['*.vue', '**/*.vue', '*.html', '**/*.html'],
    extends: ['stylelint-config-recommended', 'stylelint-config-standard', 'stylelint-config-recommended-vue'],
    rules: {
      indentation: [2, { baseIndentLevel: 1 }],
    },
  }],
};
```

<mark>所有配置文件都要在创建在根目录下</mark>

**stylelint-order**，之前装过这个扩展插件，但是大家就选择性安装吧。

> 该插件的作用是强制你按照某个顺序编写 css。例如先写定位，再写盒模型，再写内容区样式，最后写 CSS3 相关属性。这样可以极大的保证我们代码的可读性。

### 5. refs

[如何为你的 Vue 项目添加配置 Stylelint ](https://www.cnblogs.com/BlackStorm/p/add-stylelint-to-your-vue-project.html)

[stylelint homepage](https://stylelint.io/)

[stylelint-order npm](https://www.npmjs.com/package/stylelint-order)

## Prettier

> Prettier is an opinionated code formatter.Building and enforcing a style guide.
>
> use **Prettier for formatting** and **linters for catching bugs**
>
> form https://prettier.io/docs/en/comparison.html

以前一直不晓得ESlint 和 prettier 的区别，一直感觉这两是一样的，但是看了很多教程，都推荐把prettier安装上，因为prettier负责format, eslint 负责 catch bugs。

### 1. install and init

Download [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extensions for VSCode.Install [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) (disables formatting for ESLint) and [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) (allows ESLint to show formatting errors as we type) npm

`npm install --save-dev prettier eslint-config-prettier eslint-plugin-prettier`

**eslint-config-prettier**

> Turns off all rules that are unnecessary or might conflict with [Prettier](https://github.com/prettier/prettier).
>
> This lets you use your favorite shareable config without letting its stylistic choices get in the way when using Prettier.
>
> Note that this config *only* turns rules *off,* so it only makes sense using it together with some other config.
>
> 通过使用eslint-config-prettier配置，能够关闭一些不必要的或者是与prettier冲突的lint选项。这样我们就不会看到一些error同时出现两次。使用的时候需要确保，这个配置在extends的最后一项。

**eslint-plugin-prettier**

> eslint-plugin-prettier插件会调用prettier对你的代码风格进行检查，其原理是先使用prettier对你的代码进行格式化，然后与格式化之前的代码进行对比，如果过出现了不一致，这个地方就会被prettier进行标记。

**prettier-eslint**

> Formats your JavaScript using [`prettier`](https://github.com/jlongster/prettier) followed by `eslint --fix`

**eslint-plugin-prettier插件安装后，prettier 和 eslint 相冲突的规则都会报错，请选择性安装**

Then, add `"prettier"` to the "extends" array in your `.eslintrc.*` file. Make sure to put it **last,** so it gets the chance to override other configs.

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4smd4twjmj20y808q76m.jpg)

### 2. format with prettier

`npx prettier --write .`

You may run `prettier --write app/` to format a certain directory, or `prettier --write app/components/Button.js` to format a certain file.

### 3. Refs

[Integrating Prettier + ESLint + Airbnb Style Guide In VSCode](https://echobind.com/post/integrating-prettier-eslint-airbnb-style-guide-in-vscode)

[使用ESLint+Prettier来统一前端代码风格](https://segmentfault.com/a/1190000015315545)

## Commitlint

> `commitlint` helps your team adhering to a commit convention. By supporting npm-installed configurations it makes sharing of commit conventions easy.
>
> (检查commit时候，commit message 的格式, 统一message风格)
>
> From [commitlint.js.org](https://commitlint.js.org/#/)

### 1. Install

`npm install @commitlint/cli @commitlint/config-conventional -D`

### 2. Configure

创建`commitlint.config.js`文件, 并写入`module.exports = {extends: ['@commitlint/config-conventional']}`

`echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js`

### 3. Ref

[Guide: Local setup](https://commitlint.js.org/#/guides-local-setup?id=guide-local-setup)

## Husky

> Husky improves your commits and more 🐶 *woof!*
>
> You can use it to **lint your commit messages**, **run tests**, **lint code**, etc... when you commit or push. Husky supports [all Git hooks](https://git-scm.com/docs/githooks).
>
> husky可以让我们向项目中方便添加git hooks, 在git push 之前会执行你所设定的命令，比如代码风格统一检查等。
>
> from [husky githun.io](https://typicode.github.io/husky/#/)

### 1. Install and init

`npx husky-init && npm install `

安装成功后，husky给我们一个创建了一个pre-commit的钩子的例子。在根目录的.husky文件夹中。

将commitlint加到husky的钩子中

`npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"' `

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4sjiz5orjj21240gk44u.jpg)

接下来我们可以尝试提交

`git add .`
`git commit -m "test" `

因为格式不对，出现报错。

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4sj2kx0qjj20uk0343zs.jpg)

### 2. Ref

[husky使用总结](https://zhuanlan.zhihu.com/p/366786798)

## lint-staged

> Linting makes more sense when run before committing your code. By doing so you can ensure no errors go into the repository and enforce code style. But running a lint process on a whole project is slow, and linting results can be irrelevant. Ultimately you only want to lint files that will be committed.
>
> 引入Lint-staged，一个仅仅过滤出Git代码暂存区文件(被committed的文件)的工具。
>
> from https://www.npmjs.com/package/lint-staged

### 1. Install and init

`npm install --save-dev lint-staged`

在package.json文件做如下修改

1. 在scripts中新增lint命令，新增lint-staged配置

```js
{
  "scripts": {
  	...
    "lint": "eslint --ext .js,.vue --fix ./src",
    "lint:style": "stylelint \"src/**/*.{vue,scss}\" --fix",
    "stylelint-check": "stylelint-config-prettier-check",
    "fix": "prettier --write  ./src",
  },
  ...
  "lint-staged": {
    "*.scss": [
      "prettier --write ./src",
      "stylelint \"src/**/*.{vue,scss}\" --fix",
      "git add"
    ],
    "*{.js,.vue}": [
      "prettier --write ./src",
      "stylelint \"src/**/*.vue\" --fix",
      "eslint --ext .js,.vue --fix ./src",
      "git add"
    ]
  }
}
```

2.在`./husky/pre-commit`把`npm test`修改为`npx lint-staged`

提交做测试看看

![image-20220802180812169](/Users/chenruo/Library/Application Support/typora-user-images/image-20220802180812169.png)

解决完报错，发现commit message 没有按照规则书写。

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h4skynl36wj21380kc46f.jpg)

修改commit message,成功提交。

![image-20220802181027105](/Users/chenruo/Library/Application Support/typora-user-images/image-20220802181027105.png)


## Questions

### webstrom中eslint,stylelint 错误代码未高亮的问题

要在preferences中进行设置，我发现每个项目都需要设置一次...

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4reawhdwdj20fu0c8wgl.jpg" alt="image.png" style="zoom:50%;" />

<img src="http://tva1.sinaimg.cn/large/6fc56815gy1h4rebfbmmyj21hs13i7em.jpg" alt="image.png" style="zoom: 33%;" />

<img src="/Users/chenruo/Library/Application Support/typora-user-images/image-20220801173209868.png" alt="image-20220801173209868" style="zoom:33%;" />

# react eslint airbnb typescript prettier

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h5690trc9cj222k0mak1c.jpg)

```
eslint-plugin-react@^7.28.0 
eslint-config-airbnb@latest 
eslint@^7.32.0 || ^8.2.0 
eslint-plugin-import@^2.25.3 
eslint-plugin-jsx-a11y@^6.5.1 
eslint-plugin-react-hooks@^4.3.0
eslint-plugin-promise@6.0.0
eslint-plugin-n@15.2.4
```

```
@typescript-eslint/eslint-plugin@^5.0.0
typescript@*

prettier 
eslint-plugin-prettier 
eslint-config-prettier 

```

```
@typescript-eslint/eslint-plugin
@typescript-eslint/parser 
typescript@*
eslint
eslint-config-airbnb
eslint-config-airbnb-typescript  
eslint-plugin-import
eslint-plugin-jsx-a11y 
eslint-plugin-promise 
eslint-plugin-n
eslint-plugin-react
eslint-plugin-react-hooks 
prettier 
eslint-plugin-prettier 
eslint-config-prettier 
--dev
```

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h56a5769btj219a0toqby.jpg)

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h56boee7lrj215c0fa79e.jpg)

![image.png](http://tva1.sinaimg.cn/large/6fc56815gy1h56btwmnhpj217g0f847q.jpg)