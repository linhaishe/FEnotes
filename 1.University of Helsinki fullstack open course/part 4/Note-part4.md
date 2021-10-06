npm install express

npn install mongoose

npm install dotenv

npm install --save-dev nodemon

npm install cors

```
const cors = require('cors')
app.use(cors())
```

npm install eslint --save-dev

在这之后，我们可以使用如下命令初始化默认的 ESlint 配置:

```bash
node_modules/.bin/eslint --init
```

```js
//windows下输入
.\node_modules\.bin\eslint --init
```

建议为 linting 创建一个单独的 npm 脚本:

```json
{
  // ...
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    // ...
    "lint": "eslint ."
  },
  // ...
}
```

现在 *npm run lint* 命令将检查项目中的每个文件。

postman

```js
{
"title": "test-title1",
"author": "test-author1",
"url": "test-url1",
"likes": 2
}
```

npm install --save-dev jest

**Windows 用户: 如果项目目录的路径所包含的目录名称含有空格，** Jest 可能无法工作。

```js
const blogs = [ 
    { _id: '5a422a851b54a676234d17f7', title: 'React patterns', author: 'Michael Chan', url: 'https://reactpatterns.com/', likes: 7, __v: 0 }, 
    { _id: '5a422aa71b54a676234d17f8', title: 'Go To Statement Considered Harmful', author: 'Edsger W. Dijkstra', url: 'http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html', likes: 5, __v: 0 }, 
    { _id: '5a422b3a1b54a676234d17f9', title: 'Canonical string reduction', author: 'Edsger W. Dijkstra', url: 'http://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD808.html', likes: 12, __v: 0 }, 
    { _id: '5a422b891b54a676234d17fa', title: 'First class tests', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2017/05/05/TestDefinitions.htmll', likes: 10, __v: 0 }, 
    { _id: '5a422ba71b54a676234d17fb', title: 'TDD harms architecture', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2017/03/03/TDD-Harms-Architecture.html', likes: 0, __v: 0 }, 
    { _id: '5a422bc61b54a676234d17fc', title: 'Type wars', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2016/05/01/TypeWars.html', likes: 2, __v: 0 }
]
    const authorLikesArr = blogs.map(function(item){
        return {
            author:item.author,
            likes:item.likes
        }
    })
console.log("authorLikesArr",authorLikesArr);
    const newArr=[]
    //[{author: "Michael Chan", likes: 7}]
    authorLikesArr.forEach(item=>{
        //newaArr是一个一个从authorLikesArr中push上去的
        //dataItem是一个对象
        //item,代表参数,authorLikesArr里的值
        const dataItem =item
        //{author: "Michael Chan", likes: 7}
        console.log("dataItem1",dataItem);
        if(newArr.length>0){
            //newArr:[{author: "Michael Chan", likes: 7}]
          console.log("newArr.length",newArr.length);
            const filterValue = newArr.filter(v=>{
              //过滤出所需要的的dataItem的值
              //即[{author: "Michael Chan", likes: 7}], 
                //	0: [{author: "Robert C. Martin", likes: 10},
				//	1: {author: "Robert C. Martin", likes: 0},
				//	2: {author: "Robert C. Martin", likes: 2}]
                return v.author == dataItem.author
              console.log("newArrnewArr1",newArr);
              console.log("dataItem2",dataItem);
            })
            if(filterValue.length>0){
              console.log("filterValuefilterValue1",filterValue);
                //即"filterValuefilterValue1",
                //[{author: "Michael Chan", likes: 7}]
                //n代表newArr,此时的newArr只偶遇一个对象或筛选出相同author的值
                //	0: [{author: "Robert C. Martin", likes: 10},
				//	1: {author: "Robert C. Martin", likes: 0},
				//	2: {author: "Robert C. Martin", likes: 2}]
                newArr.forEach(n=>{
                    if( n.author ==filterValue[0].author){
                        n.likes =  filterValue[0].likes +dataItem.likes
                       console.log("newArrnewArr2",newArr);
                       console.log("filterValuefilterValue2",filterValue);
                    } 
                })
            }else{
                //如果
                newArr.push(dataItem)
                console.log("filterValuefilterValue2",filterValue);
              console.log("newArrnewArr2",newArr);
                console.log("newArr.push2",newArr);
            }
        }else{
            newArr.push(dataItem)
           
              console.log("newArrnewArr1",newArr);
            console.log("newArr.push1",newArr);

        }
        
    })
    const topLikesNum = newArr.map((item)=>item.likes)
    const topLike = topLikesNum.indexOf(Math.max(...topLikesNum))
    const topLikeAuthor = {
        author:newArr[topLike].author,
        likes:newArr[topLike].likes
    }
    console.log(topLikeAuthor);
```

![image-20210118131043856](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210118131043856.png)

![image-20210118131104082](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210118131104082.png)

```js
const blogs = [ 
    { _id: '5a422a851b54a676234d17f7', title: 'React patterns', author: 'Michael Chan', url: 'https://reactpatterns.com/', likes: 7, __v: 0 }, 
    { _id: '5a422aa71b54a676234d17f8', title: 'Go To Statement Considered Harmful', author: 'Edsger W. Dijkstra', url: 'http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html', likes: 5, __v: 0 }, 
    { _id: '5a422b3a1b54a676234d17f9', title: 'Canonical string reduction', author: 'Edsger W. Dijkstra', url: 'http://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD808.html', likes: 12, __v: 0 }, 
    { _id: '5a422b891b54a676234d17fa', title: 'First class tests', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2017/05/05/TestDefinitions.htmll', likes: 10, __v: 0 }, 
    { _id: '5a422ba71b54a676234d17fb', title: 'TDD harms architecture', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2017/03/03/TDD-Harms-Architecture.html', likes: 0, __v: 0 }, 
    { _id: '5a422bc61b54a676234d17fc', title: 'Type wars', author: 'Robert C. Martin', url: 'http://blog.cleancoder.com/uncle-bob/2016/05/01/TypeWars.html', likes: 2, __v: 0 }
]

const authorLikesArr = blogs.map(function(item){
        return {
            author:item.author,
            likes:item.likes
        }
    })

const newArr=[]

authorLikesArr.forEach(item=>{
    //一个一个遍历后，一个一个push
    const dataItem =item
    newArr.push(dataItem)
    console.log("newArrnewArr",newArr)
})

authorLikesArr 
(6) [{…}, {…}, {…}, {…}, {…}, {…}]
0: {author: "Michael Chan", likes: 7}
1: {author: "Edsger W. Dijkstra", likes: 5}
2: {author: "Edsger W. Dijkstra", likes: 12}
3: {author: "Robert C. Martin", likes: 10}
4: {author: "Robert C. Martin", likes: 0}
5: {author: "Robert C. Martin", likes: 2}
```

```js
const dataItem = 
{
  author: "Michael Chan",
  likes: 7
}

const newArr = 
[{
  author: "Michael Chan",
  likes: 7
}, 
{
  author: "Edsger W. Dijkstra",
  likes: 5
}, 
{
  author: "Edsger W. Dijkstra",
  likes: 12
},  
{
  author: "Robert C. Martin",
  likes: 10
}, 
{
  author: "Robert C. Martin",
  likes: 0
}, 
{
  author: "Robert C. Martin",
  likes: 2
}]

const filterValue = newArr.filter(v=>{
                return v.author == dataItem.author
            })
```

```js
const dataItem = 
{
  author: "Michael Chan",
  likes: 7
}
//dataitem只出现一次
const newArr = 
[{
  author: "Michael Chan",
  likes: 7
}, 
{
  author: "Edsger W. Dijkstra",
  likes: 5
}]

const filterValue = newArr.filter(v=>{
   return v.author == dataItem.author
})

if(filterValue.length>0){
newArr.forEach(n=>{
if( n.author ==filterValue[0].author){
n.likes =  filterValue[0].likes +dataItem.likes
} 
})
}else{
newArr.push(dataItem)
}

console.log(newArr)
```

```
authorLikesArr 
(6) [{…}, {…}, {…}, {…}, {…}, {…}]
0: {author: "Michael Chan", likes: 7}
1: {author: "Edsger W. Dijkstra", likes: 5}
2: {author: "Edsger W. Dijkstra", likes: 12}
3: {author: "Robert C. Martin", likes: 10}
4: {author: "Robert C. Martin", likes: 0}
5: {author: "Robert C. Martin", likes: 2}
```

```
dataItem
{author: "Michael Chan", likes: 7}
{author: "Edsger W. Dijkstra", likes: 5}
{author: "Edsger W. Dijkstra", likes: 12}
{author: "Robert C. Martin", likes: 10}
{author: "Robert C. Martin", likes: 0}
{author: "Robert C. Martin", likes: 2}
```

```js
const dataItem = {author: "Robert C. Martin", likes: 2}

//dataitem只出现一次
const newArr = [{author: "Michael Chan", likes: 7},
                {author: "Edsger W. Dijkstra", likes: 17},
               {author: "Robert C. Martin", likes: 10}]

const filterValue = newArr.filter(v=>{
   return v.author == dataItem.author
})

console.log("filterValue",filterValue)


if(filterValue.length>0){
newArr.forEach(n=>{
if( n.author ==filterValue[0].author){
n.likes =  filterValue[0].likes +dataItem.likes
} 
})
}else{
newArr.push(dataItem)
}

console.log("newArr",newArr)
```

![image-20210120170359996](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210120170359996.png)

![image-20210120170430929](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210120170430929.png)



## testing the backend

change 

```js
  "scripts": {
    "start": "node index.js",
    "lint": "eslint .",
    "test": "jest --verbose"
  }
```

into 

```js
  "scripts": {
    "start": "NODE_ENV=production node index.js",
    "dev": "NODE_ENV=development nodemon index.js",
    "lint": "eslint .",
    "test": "NODE_ENV=test jest --verbose --runInBand"
  }
```

