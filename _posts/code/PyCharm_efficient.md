---
title: PyCharm_高效指南
date: 2017-08-01 15:16:50
tags: [Python, IDE]
categories: [code]
permalink: pycharm_efficient
---

Pycharm是JetBrains家族的产物， 整个JetBrains的产品风格都是统一的， 因此， 熟悉了一款产品的模式， 大体上， 整个家族其他产品也能够轻松的驾驭。

## 在一个窗口程序中打开多个项目

简单来说就是在左侧的 `Project` 中可以显示多个项目而不是只显示一个项目文件夹及 `External Libraries` 。 我们知道使用Pycharm打开一个新的项目目录， 需要如下操作 `File -> Open` , 然后会让选择一个文件夹打开， 当选择完文件加后， 会有如下显示：

![pyCharm_efficient/2019-11-3-16-11-25.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-11-25.png)

* 第一项 `Open in new window` 会重新打开一个窗口， 新选择的项目在新的窗口中打开。
* 第二项 `Open in current window` 会用选择的项目替换掉当前窗口的项目， 最终只有新选择的项目是打开的。
* 第二项的辅助选项 `Add to currently opened projects` , 勾选上这一项， 最终结果是， 两个项目并存在同一个窗口中， 当然可以重复操作， 添加任意多个项目。 每一个文件夹均是一个项目， 拥有独立的git管理功能。 效果如下：

![pyCharm_efficient/2019-11-3-16-11-59.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-11-59.png)

## 函数参数类型代码提示

我们在方法内部使用形参时， 通常编辑器（IDE)并不知道该参数的类型， 因此很多变量的方法、 属性也不会有自动提示， 为了解决这个问题， PyCharm内建支持方法的参数及返回值提示功能。 书写格式如下：

``` python
def readFile(fileName, mode='r', lines=False):
    """
    :type fileName: str
    :type mode: str
    :type lines: bool
    :rtype str | list[str]
    """
```

当按住⌘按键同时移动鼠标到类型上， 是会有提示的， 而且如果是类， 还可以点击跳转到类所在的文件， 这样在该方法中PyCharm便能够确定该参数的类型， 并能够在参数类型不匹配时进行警告提示。

> PyCharm支持的类型写法如下

![pyCharm_efficient/2019-11-3-16-12-35.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-12-35.png)

## Python解释器的设置

无论是使用原生python版本还是pyenv管理的python亦或者virtual enviroment管理的python, PyCharm都能够很好的支持。
在偏好设置中 `Preferences` 中的 `Project` 中， 可以设置制定项目的Python解释器， 并且还可以列出当前Python环境下所安装的包， 以及包的版本， 最新版本， 方便进行升级管理。

![pyCharm_efficient/2019-11-3-16-12-57.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-12-57.png)

## 集成数据库

PyCharm默认集成了强大好用的数据库， 支持众多中关系型数据库。
默认情况下在控制界面的右侧， 点击 `Database` 即可打开数据库管理选项卡， 点击加好按钮可以添加数据库， 第一次使用需要安装插件支持。 输入必须的资料， 就可以愉快的在PyCharm中操作数据库了。

![pyCharm_efficient/2019-11-3-16-13-33.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-13-33.png)

## Debug环境变量的设置

我们经常会将同一套代码跑在不同的环境中， 比如生产环境、 测试环境， 本地环境、 线上环境等， 将一些具有决定性的字段写在环境变量中仿佛是一个更好的解决方法呢， 能够在不修改代码的情况下， 更改代码的执行环境， 甚至是控制代码的功能。

在菜单中选择 `Run -> Edit Configurations` 添加一个新的 `Configuration` , 并在 `Environment variables` 中添加需要的环境变量， 程序运行时就可以获取到该变量， 你可以添加多个 `Configuration` 来对应不同的环境变量值。

![pyCharm_efficient/2019-11-3-16-13-55.png](http://img.geekerhua.com/blog/pyCharm_efficient/2019-11-3-16-13-55.png)
