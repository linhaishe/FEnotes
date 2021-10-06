# 数据库概述

## 学习目标

- 掌握数据库的基本概念
- 了解数据库的发展历程
- 了解数据库的数据模型

## 学习内容

数据库的学问很多，建议大家专门学习一下数据库。

> 数据库是数据管理的有效技术，是计算机科学的重要分支。随着时代的发展，今天信息资源已经成为一种宝贵的财富。从校务管理系统到电子政务、商务系统，这些社会的方方面面都会产生庞大的数据，管理和使用这些数据成为当今相关从业者必不可少的一种技能。

- 基本概念

  - 数据 

    数据库中储存的基本对象。狭义的数据指的是对客观世界的数字化描述，而广义的理解认为数据的种类有很多，如文本（text）、图像（image）、音频（audio）、视频（video）等等。

  - 数据库 

    概念：顾名思义，是存放数据的仓库。严格来讲，数据库指长期储存在计算机内、结构化、有组织、可共享的大量数据的集合。 特点：数据按一定的数据模型组织、描述和储存，有较小的冗余(redundancy)、较高的数据独立性 (data independency) 和易扩展性 (scalability)，并可以为多个用户共享（永久储存、有组织、可共享）。

  - 数据库管理系统 

    概念：位于用户和操作系统之间的一层数据库管理软件。是计算机的基础软件。 主要功能：数据库（表）的增删改查、事务管理和运行管理、维护和其它功能（与其它软件系统的通信）

  - 数据库系统 

    概念：由数据库、数据库管理系统（及应用开发工具）、应用程序和数据库管理员组成的储存、管理、处理和维护数据的系统。注意：整个数据库系统中起决定性作用的是“数据库管理员”。

- 数据管理技术的发展

  - 人工管理阶段 20世纪50年代中期以前，计算机主要用于科学计算。由于软硬件落后、数据处理方式不成熟，当时的数据管理由人工完成。它有这些特点：数据不保存（使用时将数据输入，用完撤走）、无管理软件，管理工作交由程序员、数据共享性低、数据不具有独立性。
  - 文件系统阶段 20世纪50年代后期到60年代中期，由于硬件技术进步（有了磁盘、磁鼓等直接存取的设备），数据库管理软件（称文件系统）出现，有了批处理方式等等原因，数据库管理技术不同以往。此时的数据库管理系统被称为“文件系统”，它有如下特点：数据可以长期保存、有文件系统管理数据、数据共享性差、冗余度大、独立性差
  - 数据库系统阶段 20世纪60年代后期之后，计算机技术发展越来越成熟。硬件中出现了大容量硬盘，集成度更高、处理速度更快的处理器，软件发展日新月异，处理方式上出现了分布式处理。在此背景下，以文件系统作为数据管理的系统已经不能满足应用需求，当今的数据库系统迎运而生。

- 数据模型

  数据模型分概念模型、逻辑模型和物理模型。

  - 概念模型：按照用户的观点来对信息建模，主要用于数据库设计。
  - 逻辑模型：包括层次模型，网状模型、关系模型、面向对象数据模型和对象关系数据模型。
  - 物理模型：对数据最底层的抽象，它描述数据在系统内部（或磁盘）的表示方法和存取方法。

- 信息世界基本概念

  - 实体：客观存在并可相互区别的事物。比如：人、事、物、抽象的概念或联系（一个学生、一个工人、学生的选课）。
  - 属性：实体具有的某一特性。如学生实体的属性有：学号、姓名、性别、年龄等等。
  - 码：唯一表示实体的属性。

- 概念模型的表示方法

  最为常用的概念模型表示方法是：P.P.S.Chen 于1976 年提出的 `实体联系方法`。该方法用 `E-R` 图来表示，`E-R` 方法也称为 `E-R` 模型。

- 常用数据模型

  - 层次模型
  - 网状模型
  - 关系模型
  - 面向对象数据模型
  - 关系对象数据模型
  - 半结构化数据模型

- 关系型数据库

  关系型数据库是指支持关系模型的数据库系统，应用数学方法来处理数据库中的数据。在用户看来，关系型数据库中的数据结构是一张扁平的二维表。

  - 最早将这类方法用于数据处理的是 1962 年 CODASYL 发表的“信息代数”。
  - 1968 年David Child 在 IBM 7090 机上实现了集合数据论结构，但系统严格提出关系模型的是美国 IBM 公司的E.F.Codd。
  - 1970 年，E.F.Codd在美国计算机学会会刊《Communication of the ACM》上发表了题为“A Relational Model of Data for Shared Data Banks”的论文，开创了数据库系统的新纪元。
  - 20 世纪 70 年代末， IBM 公司的 San Jose 实验室在 IBM 370 机上研制出的关系数据库实验系统 System R 历时六年获得成功。
  - 1981 年，IBM公司有宣布了具有 System R 特性的新数据库软件产品 SQL/DS问世。

## 使用数据库的原因

1. 页面写死数据，假数据    页面常年不更换可以
2. 数据存在数组、json对象里面    刷新页面就没有了
3. 可以把数据存放在浏览器里面   换浏览器不行  不安全
4. 把数据放在硬盘里面  数据的操作管理比较麻烦

## 关系型数据库，非关系型数据库

- 关系型数据库
  - 存储方式：类似Excel表，所有的数据都是以表的形式存储，表和表之间存在着关系
  - 产品：mysql  Oracle
  - 好处：数据库稳定、数据的健壮性、有效度高
  - 坏处：为了存放关系、浪费了数据库空间
- 非关系型数据库（对象型数据库）
  - 存储方式：数据以键值对的方式存储
  - 产品：mongdb
  - 好处：因为不存放关系  数据库的查询、操作非常快
  - 用处：做大数据处理、大数据分析

## 推荐资料

- [What is database(DB)](https://searchsqlserver.techtarget.com/definition/database)
- [Database tutorial](https://www.quackit.com/database/tutorial/)
- [MySQL 教程-菜鸟教程](http://www.runoob.com/mysql/mysql-tutorial.html)

## 本节练习

- [完成sql bolt练习](https://sqlbolt.com/lesson/select_queries_introduction)

# 数据库三范式

## 学习目标

- 掌握关系型数据库的三大范式

## 学习内容

数据库范式是我们设计数据库时候所要遵循的一些规则，主要是为了让我们依据这些范式，从而设计出合理的**关系型数据库**。

目前[关系数据库](https://baike.baidu.com/item/关系数据库)有六种范式：第一范式（1NF）、第二范式（2NF）、第三范式（3NF）、巴斯-科德范式（BCNF）、[第四范式](https://baike.baidu.com/item/第四范式)(4NF）和[第五范式](https://baike.baidu.com/item/第五范式)（5NF，又称完美范式），这几个

我们叫三范式是因为一般来说，我们只需要满足前三个范式，就足够了。下面的内容没有学过数据库的同学可能会对一些专业名字产生疑惑，但是其实是很好理解的，因为这些范式都是从实际出发，大家结合例子看就比较容易明白。

- 第一范式（1NF）

  第一范式是指数据库表中的每一列都是**不可分割**的基本数据项，同一列中不能有多个值，即实体中的某个属性不能有多个值或者不能有重复的属性。

  如果出现重复的属性，就可能需要定义一个新的实体，新的实体由重复的属性构成，新实体与原实体之间为一对多关系。第一范式的模式要求属性值不可再分裂成更小部分，即属性项不能是属性组合或是由一组属性构成。

  <mark>简而言之，第一范式就是无重复的列,行不重复,列不可拆分。</mark>

  例如：

  ![img](http://ws4.sinaimg.cn/large/006tNbRwgy1fwi6p8l2rcj30c004hmx3.jpg)

  在这个表中，电话这个属性值被分割了，由于第一范式的要求是每一列属性都是不可分割的，所以这个表不满足第一范式，而且我们也不能在数据库中做出这样的表，我们把这个属性分割成两个属性就行了，如图：

  ![img](http://ws1.sinaimg.cn/large/006tNbRwgy1fwi6rrfha1j308w04gglj.jpg)

  那么我们为什么要这样呢，因为我们不这样的话，在数据库中我们也无法实现。

- 第二范式(2NF)

  第二范式(2NF)是在第一范式(1NF)的基础上建立起来的，即满足第二范式(2NF)必须先满足第一范式(1NF)。第二范式(2NF)要求数据库表中的每个实例或行必须可以被唯一地区分。为实现区分通常需要为表加上一个列，以存储各个实例的唯一标识。

  <mark>简而言之，每张表只描述一个实例。</mark>

  用户表只存用户的信息，订单表只存订单的信息，表相互关联。

  如果关系模型R为第一范式，**并且R中的每一个非主属性完全函数依赖于R的某个候选码**，则称R为第二范式模式，相信大家看到这里，肯定会对这些名词（非主属性、候选键，完全函数依赖）一头雾水，那么在往下讲之前，我们先来系统的学习一下这些名词的含义：

  **实体：**现实世界中客观存在并可以被区别的事物，比如：一辆车，一本书。通常是一个表中的一行

  **属性：**实体所具有的某一特性，比如：一辆车这个实体有价格这个属性。通常是一个表中的一列

  **码：**表中可以唯一确定一个实体的某个属性（或者属性组），如果这样的属性或者属性组不止一个，那么它们都叫候选码，我们从中挑一个作为我们使用的标示，那这个选出来的属性或者属性组就是码（主码）

  **全码：**如果一个实体的码包含了这个实体的所有属性，那么就叫全码

  **主属性：**候选码中的所有属性都是主属性

  **外码：**一个实体的某个属性是另一个实体的主码，但不是这个实体的主码

  以上是一些名词的解释。

  然后我们再来看看什么是**函数依赖**，**函数依赖**就是一个实体的属性B，可以通过属性A唯一的确定，那么我们就说属性B**函数依赖**于属性A，我们用A->B表示，比如：身份证号->姓名。

  那么什么是**完全函数依赖**呢？拿上面这个例子来说，姓名是**完全函数依赖**于身份证号的，如果我们的属性A变成了多个属性，也就是说A是一个属性集，而且也有A->B，但是呢，我们在A中可以找到一个子集C，也可以C->B，那么我们就说B是**部分函数依赖于**A的，反之，如果我们不能够在A中找到任何子集可以决定B，那么我们就说B**完全函数依赖于**A，所以我们可以这么说，当A是一个属性的时候，那肯定是**完全函数依赖**的，或者说，只有当A是一个属性集的时候，才会存在**部分函数依赖**的情况。

  在大家知道这些名词的含义之后，我们再来看一遍第二范式，**R中的每一个非主属性完全函数依赖于R的某个候选码**，这个就是说任何一个非主属性都不能部分依赖于任何一个候选码，我们来看一个表：这是一个课程表

  ![img](http://ws3.sinaimg.cn/large/006tNbRwgy1fwi9t0zdwpj30gu034q2y.jpg)

  首先，要判断符不符合第二范式，我们得先找出所有的候选码，姓名和课程就可以决定老师是谁，老师决定了，也就决定了老师的职称（这个叫做**传递依赖**，也就是老师职称传递依赖于（姓名、课程）），同时课程就可以决定教材了，然后姓名和课程一起，可以决定教师和上课时间，好，所以我们可以通过（姓名，课程）来决定这个实体，所以（姓名，课程）是候选码，同时呢，我们也可以通过（姓名，教室，上课时间）来确定这个实体，大家可以思考一下是不是，然后（姓名，教室，上课时间）也是一个**候选码**，现在我们有两个**候选码**：（姓名，课程）和（姓名，教室，上课时间），那么不包含在候选码中的属性就叫做**非主属性**，也就是老师，老师职称，教材。

  那么我们看非主属性是不是都完全依赖于某个码，非主属性教材它是部分依赖于（姓名，课程）的，因为单靠课程就可以决定教材是什么。所以这个表，不满足**第二范式**。

  那么不满足第二范式会有什么问题呢？我们思考一下，假如我们要在上面的那个表中加入一个新的课程数学，但是目前并没有任何学生选课，那么就无法加进到这个表中，学生属性是主属性，不能空，这个就叫做**插入异常**，这还不止。

  然后假如下个学期，小明该学习一年级语文（下）了，我们删除掉这个表中的那一行，然后我们就删除掉了额外的信息，思考一下，本来只是想删除小明和这个课的联系的，结果把这个课的所有信息全部删除掉了，下次再上一年级语文（上），该用哪个教材呀？这个就是**删除异常**。

  最后，如果我们需要修改表中的信息，我们得把课程：一年级语文（上）的教材修改一下，那么所有选择了这个课程的学生的那一行都需要修改，这得多费事呀，这是**更新异常**。

  好啦，我们说了一堆这个表的问题，那么如果是我们设计，我们怎么设计这个课程表呢？其实，我们只需要把那个部分依赖的部分记录到另一张表中去，就可以了，这里的课程->教材的依赖关系导致了部分依赖，所以我们这么修改：我们把原来的表分割成了两个表。

  ![img](http://ws2.sinaimg.cn/large/006tNbRwgy1fwiayckqnaj30fm02zmx5.jpg)

  ![img](http://ws3.sinaimg.cn/large/006tNbRwgy1fwiaymu3p8j30a002zwec.jpg)

  这样以后，上述的三个异常自然就消失了。

- 第三范式(3NF)

  **任何非主属性不依赖于其它非主属性（在2NF基础上消除传递依赖）**

  说白了，就是**消除非主属性对于候选码的传递依赖**。大家还记得刚才我们分析那个表格的时候说过传递依赖吗，就是老师->老师职称，老师和老师职称都不是主属性，但是存在传递依赖的关系，这有什么不好的呢，相信经过上面的分析之后，大家可以举一反三。

  1. 新来了一个老师，但是目前还没有安排他的课，这个时候，这个老师就存在于这个表中，这是**插入异常**。
  2. 一个老师休假了，目前没有课，那么这个表中也不存在老师的任何信息，像不存在一样，这是**删除异常**。
  3. 一个老师的职称变了，那么这个表中所有的这个老师的职称都得变，这是**更新异常**。

  那么我们怎么修改呢？同样的，把传递依赖的部分记录到另一个表中，这时候我们又多了一个表，如图：

  ![img](http://ws3.sinaimg.cn/large/006tNbRwgy1fwibh1tx30j307x031a9w.jpg)

  ![1099572-20170322190841127-96269272](http://ws3.sinaimg.cn/large/006tNbRwgy1fwibhna68xj30da02yq2v.jpg)

  这样之后呢，上述的三个异常也自然消失了。

- BC范式(BCNF)巴斯-科德范式

  注意，这个不是第四范式，这个只是对第三范式的一个补充，为什么第三范式需要补充呢？因为还有一种情况我们没有考虑到，那就是**主属性传递依赖于候选码**，第三范式是消除非主属性对候选码的传递依赖，那么大家可能会问了，为什么主属性也会传递依赖于候选码呢？大家先回顾一下上面的二、三范式，就会发现，其实它们全都是对非主属性的约束，那么如果没有非主属性怎么办呢？那二三范式自动就满足了，那满足了就一定是合理的吗？我们来看一个例子：

  有一个仓库管理关系（仓库ID，存储物品ID，管理员ID，数量），假设一个仓库只有一个管理员，一个管理员只能管理一个仓库，一个仓库可以存储多种物品。

  我们先来分析一下这个关系，找一下候选码，首先**仓库ID->管理员ID**，并且**管理员ID->仓库ID**，然后呢**（仓库ID，存储物品ID）->（数量，管理员ID）**，同理（**管理员ID，存储物品ID）->（数量，仓库ID）**。

  那么我们就可以看到候选码有两个（仓库ID，存储物品ID）和（管理员ID，存储物品ID）。所以现在是所有的属性全部都是主属性，没有非主属性，那么范式一，二，三现在全部满足。

  但是现在这个关系合理吗？我们还是看看能不能找到那三个异常。

  1. 新来一个仓库管理员，管理了一个仓库，但是现在仓库里面没有东西，那就无法往表格添加数据，因为主属性存储物品ID没有。（插入异常）
  2. 仓库被清空后，仓库管理员和仓库的信息也一同被清空了。（删除异常）
  3. 仓库更换了管理员，所有关于这个仓库的记录都得修改。（更新异常）

  可以看到，这个满足了前三范式的关系依旧存在问题，所以这个时候就需要BC范式了，它消除了**主属性之间的依赖关系**，那么可想而知，如果候选码是单个属性，那就不用考虑BC范式了，它是天然满足的。那么这个例子我们如何修改呢？还是一样，把依赖关系记录到另一个表中，这就有了一个新的表：

  仓库表：（仓库ID，管理员ID）

  仓库管理表：（仓库ID，存储物品ID，数量）

  这个关系也就满足了BC范式的要求了。

以上就是我们数据库三范式的全部内容了，希望大家多多思考其中的道理，然后就会发现这些范式很合理，这里我们用简短的语言总结一下各个范式的作用：

**第一范式（1NF）：**属性不可分

**第二范式（2NF）：**非主属性不部分依赖于码（非主属性完全依赖于码）

**第三范式（3NF）：**非主属性不传递依赖于候选码（非主属性之间不存在依赖关系）

**BC范式（BCNF）：**主属性不依赖于主属性

**注意后面的范式都是以前面的范式作为前提的**。

那么其实关系型数据库中还有第四范式和第五范式，大家有兴趣可以自己阅读资料自学。

## 推荐资料

- [数据库-第一范式、第二范式、第三范式、BC范式、第四范式简析](https://blog.csdn.net/dove_knowledge/article/details/71434960)
- [Database Normalization | Normal Forms](https://www.geeksforgeeks.org/database-normalization-normal-forms/)

# MongoDB

## 学习目标

- 掌握MongoDB的基本概念
- 掌握使用nodejs操作MongoDB的方法

## 学习内容

这一小节为大家介绍一个非关系型数据库[MongoDB](https://www.mongodb.com/)，以前关系型数据库是主流，但是现在非关系数据库(NoSQL = = Not Only SQL)也非常的火，因为传统的关系型数据库为了可靠性而牺牲了性能，非关系型数据库往往把性能放在第一位，非关系型数据库在拓展能力和易用性上比关系型数据库更好。

> MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。
>
> MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

#### 1.MongoDB安装

安装大家就查看[菜鸟教程的安装方法](http://www.runoob.com/mongodb/mongodb-window-install.html)就好啦，各种平台的都有，然后大家按照教程启动MongoDB服务器。

#### 2.MongoDB基础

MongoDB数据库把文档存在集合(collection)中。集合中的文档，如图![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/46412886.jpg)

所示，它们不需要相同的schema，每个文档都可以有不同的schema。 这使得MongoDB比传统的RDBMS更灵活， 因为你不用为预先定义schema而操心。 请大家记住MongoDB的这些名词的含义，Collection，Document。如果大家以前学习过关系型数据库的话，这里有一个对照表方便大家理解。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/2152350.jpg)

#### 3.在Node中使用MongoDB

我们直接在Node里使用mongodb，边用边学习MongoDB的知识。另外我也非常推荐大家去MongoDB官网学习，官网提供了官方的学习资料，非常好。大家可以先看看这个使用shell来使用MongoDB的[教程](https://docs.mongodb.com/manual/tutorial/getting-started/)

MongoDB官网提供的一个MongoDB API模块就是mongodb， 我们还是一步一步来，我们可以建立一个用于学习mongodb的文件夹，作为我们的项目目录，还是一样，先npm init -y初始化一下package.json文件，然后我们安装mongodb`npm i mongodb`，准备工作已经做好了，我们开始学习mongodb的基本增删改查用法。

创建一个app.js文件

```
const MongoClient = require('mongodb').MongoClient;

const url = 'mongodb://localhost:27017';

MongoClient.connect(url, function (err, client) {
    if(err) throw err;
    console.log("Connected successfully to server");

    client.close();
})
```

注意上面的url的端口号一般情况下都是这个，我们也可以在MongoDB服务器启动的时候看到

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/40720981.jpg)

**添加一个document**

首先我们写一个函数，用来添加document。

```
function insertDocuments(db, callback) {
    // Get the documents collection
    var collection = db.collection('documents');
    // Insert some documents
    collection.insertMany([
        { a: 1 }, { a: 2 }, { a: 3 }
    ], function (err, result) {
        if (err) throw err;
        console.log("Inserted 3 documents into the collection");
        callback(result);
    });
}
```

参数是一个database和一个回调函数，我们在获取到结果之后调用这个回调函数，并把结果当作参数穿进去。然后在连接上MongoDB之后调用这个insertDocuments

```
MongoClient.connect(url, function (err, client) {
    if (err) throw err;
    console.log("Connected successfully to server");
    const db = client.db(dbName);
    insertDocuments(db, function (results) {
        console.log(results);
        client.close();
    })
})
```

回调函数就是简单的打印一下这个结果，我们需要看一下这个结果里面有什么内容。

然后我们运行一下这个程序，看看结果。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/26101625.jpg)

这个结果的内容还是挺多的，我觉得去官网看看这个结果对象的属性总共有哪些，才好理解。

![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/83217143.jpg)

我们把这个属性表和我们的运行结果对比看就比较清楚了

- insertedCount 总共插入了多少条数据

- ops 插入的document的数组（包括_id）

- insertedIds 插入的documents的_id组成的对象

- connection 用于插入操作的连接对象，我们这里看不到

- result 是MongoDB返回的结果，可以理解为原始的结果。

- 查找所有的documents

  现在我们应该是已经添加好了数据了，我们用我们的命令行的客户端去查看一下吧

  命令行输入`mongo`就会启动客户端，默认进入本地的MongoDB 服务器

  我们可以用`show dbs`命令查看所有的database

  然后我们用`use myproject`命令进入到myproject数据库中

  然后`show collections`可以查看当前database下的所有collection

  然后`db.documents.find({})`可以查看documents这个collection里面的所有documents（此documents非前面的那个documents，这个是指一个记录，前面那个是表的名字叫documents）

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/9788327.jpg)

  看到了，我们的添加的数据了，非常好。

  然后我们需要用node做一样的事情。

  我们也是写一个查找的函数

  ```
  function findAllDocuments(db, callback) {
      const collection = db.collection('documents');
      collection.find({}).toArray(function (err, docs) {
          if(err) throw err;
          callback(docs);
      });
  }
  ```

  并在连接MongoDB之后使用

  ```
  MongoClient.connect(url, function (err, client) {
      if (err) throw err;
      console.log("Connected successfully to server");
      const db = client.db(dbName);
      findAllDocuments(db, function (result) {
          console.log(result);
          client.close();
      })
  })
  ```

  运行一下看看结果

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/38983686.jpg)

  成功了，返回了所有documents以及他们的_id。

- 带有过滤器查找documents

  跟刚才那个其实差不多，我们只需要描述一下我们要查的东西具有什么属性就好啦，比如我们要查documents中a属性是3的documents，那么我们就这么写

  ```
  function findDocuments(db, callback) {
      const collection = db.collection('documents');
      collection.find({a : 3}).toArray(function (err, docs) {
          if(err) throw err;
          callback(docs);
      });
  }
  ```

  基本跟原来查找所有的documents一样，就是多了一个`{a : 3}`是不是非常的方便。

  看看结果

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/56113868.jpg)

  不出意料

- 更新document

  写一个更新的函数

  ```
  function updateDocument(db, callback) {
      const collection = db.collection('documents');
      collection.updateOne({ a: 2 }, { $set: { b: 1 } }, function (err, result) {
          if (err) throw err;
          console.log('Update the document with the field a equal to 2');
          callback(result);
      })
  }
  ```

  它会找到a属性是2的document，然后更新它们的b属性，没有的话就添加一个b属性，我们调用一下看看

  ```
  MongoClient.connect(url, function (err, client) {
      if (err) throw err;
      console.log("Connected successfully to server");
      const db = client.db(dbName);
      updateDocument(db, function (result) {
          console.log(result);
          client.close();
      })
  })
  ```

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/66098888.jpg)

  这个result非常的长，就不完全接下来了，我们还是到官网上看看这个结果对象有哪些属性吧

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/96508195.jpg)

- 删除document

  我们现在删除一个document，它的a属性是3

  ```
  function removeDocument(db, callback) {
      const collection = db.collection('documents');
      collection.deleteOne({ a: 3 }, function (err, result) {
          if (err) throw err;
          console.log('Remove the document with the field a equal to 3');
          callback(result);
      })
  }
  ```

  一样的调用

  ```
  MongoClient.connect(url, function (err, client) {
      if (err) throw err;
      console.log("Connected successfully to server");
      const db = client.db(dbName);
      removeDocument(db, function (result) {
          console.log(result);
          client.close();
      })
  })
  ```

  看看结果

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/89581423.jpg)

  直接看属性吧，都比较好理解。

  ![img](http://xxionphotos.oss-cn-beijing.aliyuncs.com/18-6-20/6716494.jpg)

## 推荐资料（扩展学习）

- [MongoDB的应用](http://javascript.ruanyifeng.com/nodejs/mongodb.html)
- [菜鸟教程](http://www.runoob.com/mongodb/mongodb-tutorial.html)
- [MongoDB docs](https://docs.mongodb.com/)
- [MongoDB 对于 nodejs 的一个对象模型库mongoose](https://mongoosejs.com/)

## 本节练习

- 安装好MongoDB，跟随本教程完成MongoDB的练习，遇到问题学会看官方文档，完成后贴出代码

# 结构化查询语句

操作数据库需要一门专门的语言 sql语句

英语：**database management system**，[缩写](https://zh.wikipedia.org/wiki/缩写)：**DBMS**

1. 数据定义语言   DDL：(Data Definition Language, DDL SQL语言集中负责数据结构定义与[数据库对象](https://baike.baidu.com/item/数据库对象)定义的语言
2. 数据查询语言   DQL：Data Query Language 是用于从[数据库](https://zh.wikipedia.org/wiki/数据库)或[信息系统](https://zh.wikipedia.org/wiki/信息系统)中查询[数据](https://zh.wikipedia.org/wiki/数据)的[计算机语言](https://zh.wikipedia.org/wiki/计算机语言)。
3. 数据操作语言   DML：Data Manipulation Language：“CRUD”：分别为 Create, Retrieve, Update, Delete
4. 数据控制语言   DCL：Data Control Language：是一种可对资料访问权进行控制的指令，它可以控制特定用户账户对资料表、查看表、存储程序、用户自定义函数等数据库对象的控制权。

## RDBMS 术语

在我们开始学习MySQL 数据库前，让我们先了解下RDBMS的一些术语：

- **数据库:** 数据库是一些关联表的集合。
- **数据表:** 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
- **列:** 一列(数据元素) 包含了相同类型的数据, 例如邮政编码的数据。
- **行：**一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
- **冗余**：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
- **主键**：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
- **外键：**外键用于关联两个表。
- **复合键**：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
- **索引：**使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
- **参照完整性:** 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。

MySQL 为关系型数据库(Relational Database Management System), 这种所谓的"关系型"可以理解为"表格"的概念, 一个关系型数据库由一个或数个表格组成, 如图所示的一个表格:

![img](https://www.runoob.com/wp-content/uploads/2014/03/0921_1.jpg)

行 、列、表头、字段名、属性；一行 = 一条记录 = 一条数据 = 实体























