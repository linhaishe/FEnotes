# refs:

1. [廖雪峰的 Git 在线教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

2. [Git 的基础内容的学习](http://jlord.us/git-it/)

# intro

git是分布式版本控制系统，每台电脑可以保存一套完整的的版本库，可以不需要联网。

1. 可以保存每一次修改的东西
2. 可以记录每个版本
3. 安全性高，中央服务器代码没了，其他服务器的代码还在
4. 强大的分支功能，速度快

svn是集中式版本控制系统，从中央服务器下载最新代码，更改提交代码。需要网络支持。中央服务器代码没了全部的代码都没了。

相关理解

readme （讀我檔案）通常是用來解釋一個程式的功用、使用方法以及如何貢獻程式碼（但有時候這部份也會另外用一個 CONTRIBUTING.md 來說明）。

.gitignore 則是要忽略的檔案清單，這是用來告訴 Git，當在做版本控制記錄的時候，不要理會這些檔案。例如，當某個檔案中包含密碼的時候，我們就不希望 Git 記錄它們下來。

License（著作權聲明）是用來聲明一個程式可以、或不可以被怎麼樣的使用。你可以到choosealicense.com 參考一些範例。

# 一、GIT

## 1. 查看是否安装git

在终端输入git version查看是否安装了GIT

首先在自己的电脑上安装Git，通过git --version是否显示Git版本号，判断本机Git是否安装成功。然后，配置用户名和邮箱信息（git config）

## 2. 设置git用户名和邮箱

```js
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

## 3. 查看用户名和邮箱

```js
git config --global user.name
git config --global user.email
```

因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。你也许会担心，如果有人故意冒充别人怎么办？这个不必担心，首先我们相信大家都是善良无知的群众，其次，真的有冒充的也是有办法可查的。

注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

## 4. 检查已有的配置信息

`git config --list`

Git安装及钥匙的生成

https://blog.csdn.net/u011645059/article/details/20999005

## 5. 查看是否设置密钥

让git和github产生关联，创建ssh key，使用公共密钥产生联系。

**for windows**

1. Ssh-keygen -t rsa -C "登入注册用的邮箱"
2. 一路回车
3. 用记事本打开id_rsa.pub文件，复制全部，拿到公共密钥
4. 进入github设置页面，title随便写，点开ssh，粘贴密钥内容

**for Mac**

`$ cd ~/.ssh`

如没设置则会出现not such file,cd后有一个空格

$ ls

出现后查看文件列表

id_rsa

id_rsa.pub

cat id_rsa.pub

查看密码

Mac下git通过SSH进行免密码安全连接github

https://blog.csdn.net/phunxm/article/details/45083335

![502BBDB21C6F5DCE8575D1CEC1674A07.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grt61963nmj60uw0kctc602.jpg)

# 二、创建版本库

版本库又名仓库，英文名repository,，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

$ mkdir hello-world （创建文件夹）
$ cd hello-world （进入文件夹）
$ pwd （显示当前目录路径）
/Users/michael/hello-world

如果你使用Windows系统，为了避免遇到各种莫名其妙的问题，请确保目录名（包括父目录）不包含中文。

## 一. github创建仓库

流程不赘述

## 二. 本地创建仓库

github创建仓库后不选择readme，则会提示本地创建仓库的具体流程。

![C78200E5265C9BF18300FA3238F9BDA5.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grt6zsr8mwj60x20ro41n02.jpg)

### 1. 创建仓库

**git init**

把这个目录变成Git可以管理的仓库,告诉GIT初始化你现在所在的资料夹，开始追踪。查看文件所在的路径,为资料夹加上git功能。

```
$ git init
Initialized empty Git repository in /Users/michael/hellow-world/.git/
```

如果你没有看到.git目录，那是因为这个目录默认是隐藏的，用ls -ah命令就可以看见。

### 2. 把文件添加到版本库

编写文件、放到git目录下

**git add**

每次修改，如果不用git add到暂存区，那就不会加入到commit中。

```
$ git add readme.txt
```

### 3. 添加注释

**git commit**

```js
$ git commit -m "wrote a readme file" //注意空格

//返回的数据
[master (root-commit) eaadf4e] wrote a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 readme.txt
```

#### git commit -m 含义解释

-m

面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。

`git commit -m"created readme"`

1 file changed

1个文件被改动（我们新添加的readme.txt文件）

2 insertions

插入了两行内容（readme.txt有两行内容）。

```js
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."
```

#### commit同时提交多个文件

`git add .`即可

### 4. 和远程仓库建立连接

```js
git remote add origin http://github.com/linhaishe/demo2.git
```

### 5. 提交修改

```js
git push -u origin master
```



# 三、文件创建修改和删除

## 一、版本回退

### git log

查看历史记录、显示从最近到最远的提交日志，可以查看提交历史，以便确定要回退到哪个版本

显示简化版参数:`git log --pretty=oneline`

拿到需要回退的commit id

![0A1DCCE5F521ECD0954180A134627705.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1grtblx9jmpj610w0nq77w02.jpg)

### git reset

#### 从缓存区回退版本

`$ git reset HEAD filename`

`$ git reset HEAD a.txt`

#### 从远程仓库回退版本

`$ git reset --hard 版本号（commit_id）`

`$ git reset --hard HEAD`：表示当前版本，也就是最新的提交

`$ git reset --hard HEAD^` : 表示回退到上个版本

`$ git reset --hard HEAD^^` : 表示回退到上上个版本

`$ git reset --hard HEAD~100` : 往上100个版本

把暂存区的修改撤销掉（unstage），重新放回工作区

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

## 二、回退后反悔了

只要上面的命令行窗口还没有被关掉

到那个add twoline的commit id是96a56811......

$ git reset --hard 1094a
HEAD is now at 83b0afe append GPL

git reflog

查看命令历史，以便确定要回到未来的哪个版本

## 三、工作区和暂存区

1. 工作区（Working Directory）

   就是你在电脑里能看到的目录，比如我的`learngit`文件夹就是一个工作区：

![](https://www.liaoxuefeng.com/files/attachments/919021113952544/0)

2. 版本库（Repository）

   工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。stage是缓存区
   
   前面讲了我们把文件往Git版本库里添加的时候，是分两步执行的：
   
   第一步是用`git add`把文件添加进去，实际上就是把文件修改添加到暂存区即，stage；
   
   第二步是用`git commit`提交更改，实际上就是把暂存区的所有内容提交到当前分支。
   
   第三步git push 将当前分支的内容提交到远程分支。

![](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

### git diff

比较的是工作区文件与暂存区文件的区别（上次git add 的内容）

### git diff --cached 

比较的是暂存区的文件与仓库分支里（上次git commit 后的内容）的区别

### git diff --staged

git diff比较的是工作目录中当前文件和暂存区域快照之间的差异， 也就是修改之后还没有暂存起来的变化内容。若要查看已暂存的将要添加到下次提交里的内容，可以用 git diff --cached 命令。

请注意，git diff 本身只显示尚未暂存的改动，而不是自上次提交以来所做的所有改动。 所以有时候你一下子暂存了所有更新过的文件后，运行 git diff 后却什么也没有，就是这个原因。

# 四、分支管理

## 一、创建与合并分支

Git鼓励大量使用分支，因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在master分支上工作效果是一样的，但过程更安全。

### git branch

git branch命令会列出所有分支，当前分支前面会标一个*号。

查看有多少分支

* dev
  master

### git branch -r

查看远程名和分支名

### git branch `<name>（分支名）`

创建分支

### git checkout `<name>（分支名）`

切换分支,这里的checkout不是撤回的作用，是切换

### git checkout -b `<name>（分支名）`

创建+切换分支：

```
$ git checkout -b dev
Switched to a new branch 'dev'
```

相当于以下两条命令：

```
$ git branch dev
$ git checkout dev
Switched to branch 'dev'
```

### git merge `<name>`

合并某分支到当前分支

### git branch -d `<name>`

删除分支，删除分支的时候，路径不能在所删除的分支里，必须切换分支，才能删除。

```
git branch -d dev
Deleted branch dev (was b17d20e).
```

大概流程：创建分支、切换到新创建的分支、在新的分支上进行修改提交、切换回master分支、新的分支和master合并、删除新分支留下master分支、修改依然保存。

### git checkout gh-pages`<BRANCHNAME>`

分支名；首先，切換到想要 合併merge 進去的 分支branch，也就是 'gh-pages' 想要合并到那个分支就先去到那个分支的路径里。

### git merge `<BRANCHNAME>`

告訴 Git 你想要 合併merge 那個 分支branch 進來，也就是你的 功能feature 分支branch，名字是 'add-username'。把`<BRANCHNAME>`分支合并到当前分支，如果你当前在master分支，则会将`<BRANCHNAME>`合并到mater中。

### git branch -d `<BRANCHNAME>`

把剛剛已經 合併merged 的 功能feature 分支branch 刪掉。（删除本地分支

### git push `<REMOTENAME>` --delete `<BRANCHNAME>`

删除remote的分支

### git pull `<REMOTENAME>`` <BRANCHNAME>`

從遠端remote 分支branch 收取Pull

## 二、分支管理策略

1. Fast forward 模式

   这种模式下，删除分支后，会丢掉分支信息。

2. --no-ff 模式

   Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。表示禁用Fast forward

   `git merge --no-ff -m "merge with no-ff" dev`

合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

## 三、解决分支冲突

大概流程

1. 创建新分支，在featurel1 分支上修改readme.txt 文件，并提交
2. 切换分支，在master 分支上 修改 readme.txt文件，并提交
3. 合并，出现冲突
4. 直接打开readme.txt 文件，可以直接查看冲突原因，解决冲突，再次进行合并，在master分支下提交合并分支。
5. 最后删除 featurel1 分支

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。

用git log --graph命令可以看到分支合并图。

### bug分支

工作区有内容，需要创建分支解决bug，需要将工作区的内容进行缓存。工作只进行到一半，还没法提交，预计完成还需1天时间。但是，必须在两个小时内修复该bug，怎么办。使用stash功能，将工作区内容缓存起来，创建分支解决bug。

一般情况下，工作区还有内容没有commit提交的时候，不要创建分支。

### git stash

把当前工作现场“储藏”起来，等以后恢复现场后继续工作

1. git stash 把当前工作现场“储藏”起来，等以后恢复现场后继续工作
2. 用git status查看工作区，就是干净的（除非有没有被Git管理的文件），因此可以放心地创建分支来修复bug。
3. 首先确定要在哪个分支上修复bug，假定需要在master分支上修复，就从master创建临时分支
4. 修复完成后，切换到master分支，并完成合并，最后删除issue-101分支：
5. git stash list命令 ，查看原本的工作现场
6. 工作现场恢复方式
7. 再用git stash list查看，就看不到任何stash内容了
8. 恢复的时候，先用git stash list查看，然后恢复指定的stash，用命令 $ git stash apply stash@{0}

### git stash apply

但是恢复后，stash内容并不删除，你需要用git stash drop来删除

### git stash drop

在git stash apply运行后，运行git stash drop，则删除stash的内容

### git stash pop

恢复的同时把stash内容也删了，同时操作了两个命令，不用分开写apply和drop的命令了。

# 五、多人合作

(不完善)

## git remote

查看远程库的信息

## git remote -v

查看远程库的更详细的信息

如果没有推送权限，就看不到push的地址。显示了可以fetch抓取和推送push的origin的地址，在收取更新前先检查remote是否有变动

## git fetch --dry-run

推送分支，推送到自己的仓库

把该分支上的所有本地提交推送到远程库。推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上

## git push origin master

## git push origin dev

## git pull

把最新的提交从origin/dev抓下来

# 六、其他命令介绍

## cd ..

(1). 返回上一级目录：cd .. (cd 与 .. 之间有一空格)。

(2). 进入某一目录：cd git (进入 git 目录)。

(3). 显示当前路径：pwd

## git checkout -- filename

撤销修改，在工作区的修改全部撤销

撤销后的两种情况

1. 一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

2. 一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次git commit或git add时的状态。

git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

## rm <file>

`$ rm test.txt`，并且`git commit`

`rm -r dir`

-f 表示强制删除，不显示提示信息。

文件就从版本库中被删除了

先手动删除文件，然后使用`git rm <file>`和git add`<file>`效果是一样的。

## git status

查看冲突的文件,查看现有路径下的git状态。

nothing to commit,working tree clean

## git log --graph

可以看到分支合并图

## $ git log --graph --pretty=oneline --abbrev-commit

可以看到简化的分支合并图

## mkdir dir

新建文件夹

### mkdir directory...

当有三个圆点跟在一个命令的参数后面， 这意味着那个参数可以重复

mkdir dir1 dir2 dir3

会创建三个目录，名为 dir1, dir2, dir3

### mv item... directory

mv file1 file2 dir1

移动 file1 和 file2 到目录 dir1 中。dir1 必须已经存在。

## cp – Copy files and directories

### cp item1 item2

复制单个文件或目录”item1”到文件或目录”item2”

### cp item... directory

复制多个项目（文件或目录）到一个目录下。

## rm – Remove files and directories

rm item...

## touch file

新建文件

## vi + 文件名

编辑文件

按Esc键以确保您退出编辑模式，然后:wq（冒号W Q，才能保存成功

具体步骤

（1）vi+文件名，新建一个文件并进入编辑状态（如果文件已存在，则直接进入编辑状态） 

（2）在命令模式下，我们可以直接按 i ,此时就会切换到编辑模式，如下图，下方有个insert，此时可以直接修改文本内容。 

（3）在编辑模式下，按 esc 就可以切换到命令模式。 ：wq 

在按enter键就返回主界面 

## cat file # 

查看文件内容，适合比较短的文件

## less file # 

查看文件内容，有快捷键，可以看比较长的文件

## file file1

查看文件类型 fiie

## du -k file

查看文件大小

## du -m file

查看文件大小

## pwd

查看当前目录

## cd Desktop

切换目录

cd ..(有空格

返回上一级目录

进入D盘

$ cd D:

复制结束，按esc后，输入:q!退出vim

---

# 七、密钥相关

廖雪峰的教程和gitit教程内容有点区分，在关联远程库的时候gitit使用的是http,而廖雪峰用的是ssh，我先弄得廖雪峰的然后弄得gitit，导致仓库一直不能关联，搜了一下午的教程，设置了ssh密钥等等，最后把url链接换成ssh，通过密钥后关联了仓库。真是哭了，用了一天的时间。

https://blog.csdn.net/u011645059/article/details/20999005 （设置成功

[Changing a remote's URL SSH-HTTP](https://help.github.com/en/articles/changing-a-remotes-url)

登陆GitHub，创建一个新的仓库

$ git clone git@github.com:michaelliao/gitskills.git

SSH警告

ssh 密钥设置 都回车空格了

$ makdir ~/hello-world    //创建一个项目hello-world
$ cd ~/hello-world    //打开这个项目
$ git init    //初始化 
$ touch README
$ git add README   //更新README文件
$ git commit -m 'first commit'//提交更新，并注释信息“first commit” 
$ git remote add origin git@github.com:defnngj/hello-world.git   //连接远程github项目 
$ git push -u origin master   //将本地项目更新到github项目上去

ssh 和 https 地址区别

GitHub给出的地址不止一个，还可以用https://github.com/michaelliao/gitskills.git这样的地址。实际上，Git支持多种协议，默认的git://使用ssh，但也可以使用https等其他协议。

使用https除了速度慢以外，还有个最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用https。但通过ssh支持的原生git协议速度最快。