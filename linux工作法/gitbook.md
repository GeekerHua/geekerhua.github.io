# GitBook
gitBook是一个基于markdown和git的书写工具，更加适合书写电子书，因为基于markdown，所以具有良好的书写体验与阅读体验，还能轻松导出pdf、epub、mobi格式，还能以网页形式在线阅读。基于git进行管理能够对内容进行版本管理，进行共享等。

## 安装cli命令行工具
GitBook cli工具是基于node写的，因此需要使用node进行安装。node安装方法自行搜索。
```bash
$ npm install gitbook-cli -g
```

## 初始化
```bash
$ gitbook init
```
初始化结束会有两个文件；
- 一个是`README.md`，是这本电子书的介绍。
- 一个是`SUMMARY.md` ,是这本书的目录结构，只有该文件中记录的文件才会在电子书中显示，否则不显示。
`SUMMARY.md`文件格式如下

```markdown
# Summary
## 基础
* [Introduction](README.md)
…………
```

## 本地生成网页
使用以下命令会在同名文件夹下生成`_book`文件夹，通过该文件夹下的`index.html`即可访问网页版。
```bash
$ gitbook build
```


## 启动本地服务
使用以下命令可自动生成`_book`的本地电子书，并在4000端口开启本地服务,访问`localhost:40000`即可使用浏览器打开。
```bash
$ gitbook serve
```

# GitBook.com
[官网](https://www.gitbook.com)
gitbook.com使用了git进行数据托管，并且可以和github进行关联，实现双相同步。创建在gitboo.com的书可以同时关联到github的项目上，一个更新，另一个会自动更新。

## 与GitHub进行同步
gitbook.com的使用方式与github十分类似，不做介绍。只介绍与GitHub的无缝同步。

gitbook.com[官方的介绍](https://help.gitbook.com/github/can-i-host-on-github.html)很简单。

1. 在github中创建一个需要同步的代码仓库，为便于识别最好使用同名仓库。
2. 在gitbook的项目setting界面点击左侧的GitHub。
    ![2017725101932](http://img.geekerhua.com/blog/gitbook/2017725101932.jpg)
3. 右侧提示链接GitHub，并在GitHub中安装GitBook的插件。
4. 在GitHub中设置需要授权访问的仓库。
    ![2017725101948](http://img.geekerhua.com/blog/gitbook/2017725101948.jpg)
5. 安装好后，在gitbook的设置界面应该能看到这样的显示。
    ![201772510200](http://img.geekerhua.com/blog/gitbook/201772510200.jpg)
6. 点击`Select a Repository`选择需要关联到那个GitHub仓库。
7. 如果两个仓库代码不一致，会有如下提示，想以哪一个网站为准，就点击那个logo。第一次同步肯定点左边的GitBook啦。然后就同步完成了。
    ![2017725102013](http://img.geekerhua.com/blog/gitbook/2017725102013.jpg)
8. 到此，与GitHub的关联结束，以后就两个平台数据同步更新了。

> 其它：GitBook有个官方的编辑器，能够友好的组织、编辑和预览电子书。GitBook Editor。
最新版本已经升级到7.0.0+，但该版本必须联网才能使用。建议安装6.6.2的版本，可以离线编辑，并同步到GitBook官网。

