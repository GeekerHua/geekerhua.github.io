---
title: Git与Git工作流
date: 2016-06-02 18:57:21
tags: [git]
categories: [code]
permalink: git_workflow
---

## Git 基础用法

SVN与Git(集中式VS分布式）

* 集中式

* 分布式

#### 工作区

> 电脑中能够看到的目录就是工作区。

#### 版本库

> 工作区有一个隐藏目录 `.git` ， 这个不算工作区， 而是Git的版本库。

* Git的版本库里存了很多东西， 其中最重要的就是称为stage(或者叫index)的暂存区， 还有Git为我们自动创建的第一个分支 `master` ， 以及指向 `master` 的一个指针叫HEAD.

* git add -> 将变化提交到了暂存区
* git commit -> 将暂存区的所有修改都提交到分支， 并清空暂存区

### 全局设置

| 指令                                          | 功能           |
|-----------------------------------------------|----------------|
| $ git config --global user.name "姓名“        | 告诉git你是谁   |
| $ git config --global user.email "xxx@qq.com" | 告诉git怎么联系你 |
| $ git config -l                               | 查看配置信息     |

### 初始化代码仓库

| 指令                  | 功能                         |
|-----------------------|------------------------------|
| $ git commit --amend  | 修改最后一次提交的注释          |
| $ git init --bare     | 初始化空白的代码仓库， 协同开发使用 |
| $ git add .--all     | 将所有变化添加到暂存区          |
| $ git commit -m "注释“ | 将暂存区内容提交至代码库         |
| $ git init            | 初始化代码库                   |

### 查看信息

| 指令               | 功能                         |
|--------------------|------------------------------|
| $ git status       | 查看所有文件状态               |
| $ git status 文件名 | 查看指定文件的状态              |
| $ git log          | 查看版本库日志（按字母 q 可以退出） |
| $ git log 文件名    | 查看指定文件的修订记录          |

### 版本回撤

| 指令                           | 功能                                       |
|--------------------------------|--------------------------------------------|
| $ git reset --hard HEAD^       | 回撤到上一个版本                             |
| $ git reset --hard HEAD^^      | 回撤到上上一个版本                            |
| $ git reset --hard 版本号（前6位） | 切换到任意版本                               |
| $ git checkout 文件名           | 撤销某一个文件当前的修改（恢复到最近一次记录点状态） |
| $ git reflog                   | 查看分支引用记录， 能够查阅所有的版本号           |

### 分支操作

| 指令                     | 功能                                                                    |
|--------------------------|-------------------------------------------------------------------------|
| $ git branch             | 查看本地分支                                                              |
| $ git branch -r          | 查看远程分支                                                              |
| $ git branch [name]      | 创建本地分支（注意不会自动切换分支）                                           |
| $ git checkout [name]    | 切换分支                                                                 |
| $ git checkout -b [name] | 创建新分支并立即切换到新分支                                                |
| $ git branch -d [name]   | 只能删除已经合并过的分支 `没有合并的分支不能删除,如果要强行删除分支，可以使用 -D 选项` |
| $ git merge [name]       | 合并分支                                                                 |
| $ git push origin [name] | 创建远程分支 `本质上是将本地的分支 push 到远程` |

### 远程操作

| 指令            | 功能                       |
|-----------------|----------------------------|
| $ git pull      | 将远程代码库的变化更新到本地   |
| $ git push      | 将本地修改内容推送到远程代码仓库 |
| $ git clone url | 将远程代码库克隆到本地        |

> 两篇入门教程， 自行学习进修
> [猴子都能懂的Git入门](https://backlogtool.com/git-guide/cn/intro/intro1_1.html)
> [Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

## [Git工作流](http://blog.jobbole.com/76843/)

> 如何有效的进行项目流程管理和高效的开发协同。

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git_workflow.png)

### [集中式工作流](http://blog.jobbole.com/76847/)

> 使用过SVN与Subversion这类集中式版本控制系统的人刚刚转到分布式版本控制可能会很不熟悉， 但Git也能做到像SVN一样的集中式版本控制， 即以中央仓库作为项目所有修改的单点实体。

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflow-svn.png)

#### 对比SVN与Git对比进行集中式版本控制

* SVN缺省开发分支叫 `trunk` , git叫 `master`
* SVN的 `commit` 操作相当于git的 `push` 操作
* SVN的 `update` 操作相当于git的 `pull` 操作

但这样的工作流并没有突出git的优势

### [功能分支工作流](http://blog.jobbole.com/76857/)

> 功能分支工作流以集中式工作流为基础， 不同的是为各个新功能分配一个专门的分支来开发。 这样可以在把新功能集成到正式项目前， 用Pull Requests的方式讨论变更。

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflow-feature_branch.png)

#### 功能分支工作流优点

* 每个新功能开发都在一个专门的分支， 而不是在master分支， 不会弄乱主干分支
* 功能开发隔离使 `pull requests工作流` 成为可能
* 使用 `pull requests` 可以很好地进行 `Code Review`

### [Gitflow工作流](http://blog.jobbole.com/76867/)

> Gitflow工作流通过为功能开发、 发布准备和维护分配独立的分支， 让发布迭代过程更流畅。 严格的分支模型也为大型项目提供了一些非常必要的结构

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-gitflow.png)

**[目前iOS开发大体上遵循这种工作流](https://www.jianshu.com/p/7dddf0e9f1ef)**
![](https://upload-images.jianshu.io/upload_images/296122-5de3d3e00962f911.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### [Forking工作流](http://blog.jobbole.com/76861/)

> Forking工作流是分布式工作流， 充分利用了Git在分支和克隆上的优势。 可以安全可靠地管理大团队的开发者（developer)， 并能接受不信任贡献者（contributor)的提交。

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflow-forking.png)

* Forking工作流的一个主要优势是， 贡献的代码可以被集成， 而不需要所有人都能push代码到仅有的中央仓库中。 开发者push到自己的服务端仓库， 而只有项目维护者才能push到正式仓库。 这样项目维护者可以接受任何开发者的提交， 但无需给他正式代码库的写权限
* GitHub中每个代码仓库都有三个选项， 分别是Star、 Watch、 Fork,

![屏幕快照 2016-04-11 下午11.20.38.png](quiver-image-url/F81C279EDF5AD53780259EB087CD4F84.png)

#### 流程如下

* 项目维护者初始化正式仓库

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-1.png)

* 开发者fork正式仓库

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-2.png)

* 开发者克隆自己fork出来的仓库

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-3.png)

* 开发者开发自己的功能

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-4.png)

* 开发者发布自己的功能

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-5.png)

* 项目维护者集成开发者的功能

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-6.png)

* 开发者和正式仓库做同步

  + ![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/git-workflows-forking-7.png)

### [Pull Requests](http://blog.jobbole.com/76854/)

> Pull Requests是Bitbucket上方便开发者之间协作的功能。 提供了一个用户友好的Web界面， 在集成提交的变更到正式项目前可以对变更进行讨论。 GitHub也有这个功能。
> Pull Request可以和功能分支工作流、 Gitflow工作流或Forking工作流一起使用。

![屏幕快照 2016-04-11 下午11.21.45.png](quiver-image-url/8E87744F9F2DAF716E5CF4E727C2A4C8.png)

![](https://raw.githubusercontent.com/quickhack/translations/master/git-workflows-and-tutorials/images/pull-request.png)

## [Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html#rd?sukey=ecafc0a7cc4a741b1e6e4fadd82915cefdf73cbbe70d0626a8bce92a8162402a53d6fb99492db71ab5fb4ae3ff50d974)

> 通常我们是这样提交代码的

``` bash
$: git commit -m "hello world"
```

> 但这样的提交注释并没有卵用， 当你log提交记录的时候， 还是会看的云里雾里， 更不用说是利用了。 现在通用的效果比较好的Commit messag规范是 `Angular规范` 。

### commit message的作用

* 提供更多的历史信息， 方便快速浏览

> 比如， 下面的命令显示上次发布后的变动， 每个commit占据一行。 你只看行首， 就知道某次 commit 的目的。

``` bash
$: git log <last tag> HEAD --pretty=format:%s
```

* 可以过滤某些commit(比如文档改动）， 便于快速查找信息。

> 比如， 下面的命令仅仅显示本次发布新增加的功能。

``` bash
$: git log <last release> HEAD --grep feature
```

* 可以直接从commit生成Change log.

> Change Log 是发布新版本时， 用来说明与上一个版本差异的文档。

![Git_workflow/2019-11-3-16-15-33.png](http://img.geekerhua.com/blog/Git_workflow/2019-11-3-16-15-33.png)

### Commit message 的格式

> 每次提交， Commit message 都包括三个部分： Header, Body 和 Footer.

``` bash
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```

> 其中， Header 是必需的， Body 和 Footer 可以省略。

#### Header

Header部分只有一行， 包括三个字段： type(必需）、 scope(可选）和subject(必需）。

##### type

> type用于说明 commit 的类别， 只允许使用下面7个标识。

* feat: 新功能（feature)
* fix: 修补bug
* docs: 文档（documentation)
* style: 格式（不影响代码运行的变动）
* refactor: 重构（即不是新增功能， 也不是修改bug的代码变动）
* test: 增加测试
* chore: 构建过程或辅助工具的变动

##### scope

> scope用于说明 commit 影响的范围， 比如数据层、 控制层、 视图层等等， 视项目不同而不同。

##### subject

> subject是 commit 目的的简短描述， 不超过50个字符。

* 以动词开头， 使用第一人称现在时， 比如change, 而不是changed或changes
* 第一个字母小写
* 结尾不加句号（.）

#### Body

> Body 部分是对本次 commit 的详细描述， 可以分成多行。 下面是一个范例。

**有两个注意点**

1. 使用第一人称现在时， 比如使用change而不是changed或changes.
2. 应该说明代码变动的动机， 以及与以前行为的对比。

#### Footer

##### 不兼容变动

> 如果当前代码与上一个版本不兼容， 则 Footer 部分以 `BREAKING CHANGE` 开头， 后面是对变动的描述、 以及变动理由和迁移方法。

##### 关闭 Issue

> 如果当前 commit 针对某个issue, 那么可以在 Footer 部分关闭这个 issue 。

``` bash
Closes #234

Closes #123, #245, #992
```

#### Revert

> 还有一种特殊情况， 如果当前 commit 用于撤销以前的 commit, 则必须以revert: 开头， 后面跟着被撤销 Commit 的 Header.

``` bash
revert: feat(pencil): add 'graphiteWidth' option
This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
```

> Body部分的格式是固定的， 必须写成This reverts commit &lt; hash>.， 其中的hash是被撤销 commit 的 SHA 标识符。

如果当前 commit 与被撤销的 commit, 在同一个发布（release)里面， 那么它们都不会出现在 Change log 里面。 如果两者在不同的发布， 那么当前 commit, 会出现在 Change log 的Reverts小标题下面。
