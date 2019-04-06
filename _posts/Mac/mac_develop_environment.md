---
title:  mac开发环境配置
date: 2017-01-12 20:18:28
tags: [Shell,环境配置]
categories: 编程
---

# [Homebrew](http://brew.sh/index_zh-cn.html)

> Shell神器,OS X 不可或缺的套件管理器。`Homebrew`较之于`Shell`,好比`CocoaPod`较之于`Xcode`。这么说,`Homebrew`的定位就应该相当明确了吧！

```ruby
# 安装
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```ruby
# 卸载
 ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

* 更新已安装的package
  * 先更新brew：$ `brew update`
  * 更新所有package：$ `brew upgarde`
* Homebrew下载的package存放的路径在哪里？
  * `/Library/Caches/Homebrew/`
  

Homebrew 可以很方便的安装需要的套件,方法如下：$ `brew install wget`。是不是很简单？

Homebrew 使 OS X 更完美。使用 gem 来安装 gems、用 brew 来搞定那些依赖包。

> Tips: 如果安装过程中提示错误,提示先卸载,但执行卸载命令又卸载不掉,说明有曾经安装失败过,有残留。解决方式删除`/usr/local`文件夹即可。

![Shell_Homebrew安装失败](http://7xtibb.com2.z0.glb.qiniucdn.com/2016-06-06-Shell_Homebrew安装失败.png)

## 优秀的命令工具
### 1.htop
> 带颜色的top工具，能够显示内存和CPU使用情况

```bash
brew install htop
```

### 2.[brew cask](https://caskroom.github.io)
> 一个基于终端的软件安装工具

```bash
brew tap caskroom/cask
```
- 安装软件(比如安装chrome)
```bash
brew cask install google-chrome
```

### 3.tree
> tree可以显示目录树,类似于ubuntu中的tree。

```bash
brew install tree
```
> tree命令在mac下并不太好用，中文显示乱码有个解决方法如下，这是一个自己写的tree功能，支持中文显示

```bash
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
```

### 4.[wget](http://baike.baidu.com/link?url=_4E-kuBinS_AItjdR3vsisJTYpRsOCav7kEUifcKfUsLGMAML6kPVKJK0tVd5tOhLP13C_BnTzI7yFHFENwiKq)
> wget是一个从网络上自动下载文件的自由工具，支持通过HTTP、HTTPS、FTP三个最常见的TCP/IP协议下载，并可以使用HTTP代理。wget名称的由来是“World Wide Web”与“get”的结合。

```bash
brew install wget
```

- - - - -
# xcode-selected
> Mac下很多工具都需要xcode-selected支持，比如git。
> 如果没有安装的话，在终端输入`git`，会提示安装xcode commond line 工具。安装即可。

- - - - -
# zsh
> Linux及Mac默认的shell是Bash，但功能最强大的shell确实zsh，mac自带zsh，只是没有设置为默认shell，且shell配置复杂。使用oh-my-zsh进行配置,简单又强大.配合iTerm 2一同使用,简单又强大。

- 安装
```bash
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

- 创建备份
```bash
cp ~/.zshrc ~/.zshrc.orig
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

- 把 zsh 设置成默认的 shell
```bash
chsh -s /bin/zsh
```

- 重启zsh

- - - - -
# ruby升级
> rvm是什么？为什么要安装rvm呢，因为rvm可以让你拥有多个版本的Ruby，并且可以在多个版本之间自由切换。

第一步安装rvm
```ruby
$ curl -L get.rvm.io | bash -s stable
$ source ~/.rvm/scripts/rvm
```
- 等待终端加载完毕,后输入：
```ruby
rvm -v
```

如果能显示版本好则安装成功了。
第二步：安装ruby
- 列出ruby可安装的版本信息
```ruby
rvm list known
```

- 安装一个ruby版本
```ruby
rvm install 2.1.4
```

如果想设置为默认版本，可以用这条命令来完成
```ruby
rvm use 2.1.4 --default
```
- 查看已安装的ruby
```ruby
rvm list
```
- 卸载一个已安装ruby版本
```ruby
rvm remove 2.1.4
```
- - - - -
# CocoaPods
> CocoaPods是Xcode的包管理工具，主要用在OC中，Swift中也能应用。帮助开发者管理iOS第三方框架的工具

- 1. 查看当前的ruby源: `gem source -l`
- 2. 修改ruby源
    - 删除旧源: gem sources --remove https://rubygems.org/
    - 添加新源:  https://gems.ruby-china.org/
    - 查看新源: gem source -l
- 3.安装CocoaPods: sudo gem install cocoapods (可能需要等待较长时间)
- 4.利用CocoaPods管理第三方框架
    - 打开Xcode新建项目
    - 利用终端进入新项目的根路径
    - 新建Podfile文件: vim Podfile, 在这个文件中描述需要依赖的第三方框架
     ```
    platform :ios, '8.0'
    pod 'UIView+AutoLayout', '~> 2.0'
    pod 'MJExtension'
     ```
- 5.解析Podfile文件
    - 建议先更新远程的框架信息: pod setup
    - 开始解析Podfile文件: pod install (可能需要等待较长时间)
        - pod install 换成pod install --verbose --no-repo-update这个命令，前面的命令被墙了 ,pod update 同理
    - 如果需要更新框架: pod update
- 6.其它用法
    - 使用pod search 关键词可以搜索支持CocoaPods的第三方框架 (并不是所有第三方框架都支持CocoaPods)
    - 建议在进行pod search、pod update、pod install之前都先进行pod setup
    - 如果在使用CocoaPods过程中遇到了莫名其妙的错误（比如NoMethodError），大部分原因是mac上的Ruby环境不是最新的。可以考虑更新Ruby环境: sudo gem update
- 直接在终端添加新依赖  $  pod ‘SVProgressHUD’, ‘~> 1.1.2’ > Podfile

- - - - -
# vim
> vim号称编辑器之神，拥有强大的功能和众多的插件。

## [中文帮助文件](http://sourceforge.net/projects/vimcdoc/files/latest/download)
- 安装http://sourceforge.net/projects/vimcdoc/files/latest/download
- 解压后进入文件夹,执行 `sudo ./vimcdoc.sh -i  ` #安装
> vim中文文档不会覆盖原英文文档，安装后vim默认使用中文文档。若想使用英文文档，可在vim中执行以下命令：

    - :set helplang=en  回车之后 :help 就是英文的help。
> 同理，使用以下命令可重新使用中文文档：

    - :set helplang=cn 回车之后 :help 就是中文的help。
- 在解包之后的文件夹中使用以下命令可以卸载vim中文文档：

    - $sudo ./vimcdoc.sh -u

- - - - -
# sublime text3
## [Package Control](https://sublime.wbond.net/packages/Package%20Control)
> 提到 Sublime Text，就不得不说 Package Control，就像 Linux 下的 apt-get 和 yum 一样，它是 Sublime Text 的包管理器，你用它可以轻松地找到你想要的插件和管理已有插件。

- 使用`control` + `~`打开控制台，将从官网[复制代码](https://sublime.wbond.net/installation#st3)粘贴到控制台并执行。
- 安装代码如下
   import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed\_packages\_path(); urllib.request.install\_opener( urllib.request.build\_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
### Package Control 常用命令
- 激活`cmd+shift+P`
- 安装插件 -\>  Package Control: Install Package xxx
- 显示所有已安装的插件 -\> List Packages 
- 移除一个指定的插件 -\> Remove Packages 
- 更新一个指定的插件 -\> Upgrade Package 
- 更新所有已安装的插件 -\> Upgrade/Overwrite All Packages 

## 常用插件
### javascript
- [emmet](http://docs.emmet.io)
    > [速查表](http://docs.emmet.io/cheat-sheet/)
    > [官方文档](http://docs.emmet.io/)

    - 安装
      - 按Ctrl+Shift+P命令板
      - 输入install然后选择install Package，然后输入emmet找到 Emmet Css Snippets，点击就可以自动完成安装。
- Better Completion

  - 自动补全Bootstrap 、JQuery、Less等
### Python
- SubLimener
    - 编码规范