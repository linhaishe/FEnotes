# Part 1

## JS Materials

The introduction of the class syntax was a controversial addition. Check out [Not Awesome: ES6 Classes](https://github.com/petsel/not-awesome-es6-classes) or [Is “Class” In ES6 The New “Bad” Part? on Medium](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65) for more details.

1. [egghead.io](https://egghead.io/)
2. [Mozilla's JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
3. [You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS)
4. [javascript.info](https://javascript.info/)
5. [Eloquent JavaScript](https://eloquentjavascript.net/) :takes you from the basics to interesting stuff quickly. It is a mixture of theory projects and exercises and covers general programming theory as well as the JavaScript language.
6. [Namaste 🙏 JavaScript](https://www.youtube.com/playlist?list=PLlasXeu85E9cQ32gLCvAvr9vNaUccPVNP) is another great and highly recommended free JavaScript tutorial in order to understand how JS works under the hood. Namaste JavaScript is a pure in-depth JavaScript course released for free on YouTube. It will cover the core concepts of JavaScript in detail and everything about how JS works behind the scenes inside the JavaScript engine.

## React Materials

The internet is full of React-related material. However, we use the new style of React for which a large majority of the material found online is outdated.

You may find the following links useful:

- The [official React documentation](https://react.dev/learn) is worth checking out at some point, although most of it will become relevant only later on in the course. Also, everything related to class-based components is irrelevant to us;
- Some courses on [Egghead.io](https://egghead.io/) like [Start learning React](https://egghead.io/courses/start-learning-react) are of high quality, and the recently updated [Beginner's Guide to React](https://egghead.io/courses/the-beginner-s-guide-to-reactjs) is also relatively good; both courses introduce concepts that will also be introduced later on in this course. **NB** The first one uses class components but the latter uses the new functional ones.

## Utilization of Large language models

Large language models such as [ChatGPT](https://chat.openai.com/auth/login), [Claude](https://claude.ai/) and [GitHub Copilot](https://github.com/features/copilot) have proven to be very useful in software development.

Personally, I mainly use Copilot, which integrates seamlessly with VS Code thanks to the [plugin](https://visualstudio.microsoft.com/github-copilot/).

Copilot is useful in a wide variety of scenarios. Copilot can be asked to generate code for an open file by describing the desired functionality in text:

# Part 2

[Create your own snippets](https://code.visualstudio.com/docs/editing/userdefinedsnippets#_create-your-own-snippets)

```
{
  "console.log": {
    "prefix": "clog",
    "body": [
      "console.log('$1')",
    ],
    "description": "Log output to console"
  }
}
```

## web workers

In today's browsers, it is possible to run parallelized code with the help of so-called [web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers). The event loop of an individual browser window is, however, still only handled by a [single thread](https://medium.com/techtrument/multithreading-javascript-46156179cf9a).

Web Workers are a simple means for web content to run scripts in background threads. The worker thread can perform tasks without interfering with the user interface. 

https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers#see_also

https://medium.com/techtrument/multithreading-javascript-46156179cf9a

## run server

https://github.com/typicode/json-server

```js
npm install json-server --save-dev
```

```js
npx json-server --port 3001 db.json
```

# Part 3

Representational State Transfer, aka REST, was introduced in 2000 in Roy Fielding's [dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). REST is an architectural style meant for building scalable web applications.

If you use Visual Studio Code, you can use the VS Code [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) plugin instead of Postman.

## Debugging Node applications

visit Visual Studio Code's [Debugging documentation](https://code.visualstudio.com/docs/editor/debugging).

## Chrome dev tools

Debugging is also possible with the Chrome developer console by starting your application with the command:

```bash
node --inspect index.js
```

![dev tools with green node logo icon](https://s2.loli.net/2025/08/24/tw5NO8uSLXDsEla.png)

You can access the debugger by clicking the green icon - the node logo - that appears in the Chrome developer console:

The [Jidoka](https://leanscape.io/principles-of-lean-13-jidoka/) (stop and fix) principle from Toyota Production Systems is very effective in this situation as well.

Recently many projects have adopted the Airbnb [Javascript style guide](https://github.com/airbnb/javascript) by taking Airbnb's [ESlint](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb) configuration into use.
