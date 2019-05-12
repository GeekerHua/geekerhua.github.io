---
title: 终极Shell修行大法-不得不拥有
date: 2015-12-10 18:57:21
tags: [Shell, Linux]
categories: [Linux满汉全席]
---

## [Homebrew](http://brew.sh/index_zh-cn.html)

> Shell神器， OS X 不可或缺的套件管理器。 `Homebrew` 较之于 `Shell` , 好比 `CocoaPod` 较之于 `Xcode` 。 这么说， `Homebrew` 的定位就应该相当明确了吧！

### 1. 安装：

```ruby
$: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2. 卸载：

```ruby
$: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

### 3. 更新已安装的package

* 先更新brew: $: `brew update`
* 更新所有package: $: `brew upgarde`
* Homebrew下载的package存放的路径在哪里？

  * `/Library/Caches/Homebrew/`

Homebrew 可以很方便的安装需要的套件， 方法如下： $: `brew install wget` 。 是不是很简单？

Homebrew 使 OS X 更完美。 使用 gem 来安装 gems、 用 brew 来搞定那些依赖包。

> Tips:

* 如果安装过程中提示错误， 提示先卸载， 但执行卸载命令又卸载不掉， 说明有曾经安装失败过， 有残留。 解决方式删除 `/usr/local` 文件夹即可。

## [wget](http://baike.baidu.com/link?url=_4E-kuBinS_AItjdR3vsisJTYpRsOCav7kEUifcKfUsLGMAML6kPVKJK0tVd5tOhLP13C_BnTzI7yFHFENwiKq)

> wget是一个从网络上自动下载文件的自由工具， 支持通过HTTP、 HTTPS、 FTP三个最常见的TCP/IP协议下载， 并可以使用HTTP代理。 wget名称的由来是“World Wide Web"与“get"的结合。

* `Homebrew` 下安装： 在安装了 `Homebrew` 的情况下安装wget特别简单。 只需要： $: `brew install wget` 即可。 如果没安装 `Homebrew` 建议赶紧安装。
* 正常安装（特别复杂， 不建议直接安装）：

  1. [下载源码包](http://ftp.gnu.org/gnu/wget/wget-1.13.4.tar.gz)。 这里面找到最新版本， 直接下载安装就行了
  2. 到目录 `cd /usr/local/src` 解压： tar -zxvf wget-1.13.tar.gz
  3. `./configure` ， 这个过程第一次是不成功的， 然后提示你下载安装一个make, 安装make后， 再运行一下 `./configure` 。
  4. `make`
  5. `sudo make install`

## zsh

> 终极shell, Mac自带就有， 使用[ `oh-my-zsh` ](http://ohmyz.sh)进行配置， 简单又强大。 配合iTerm 2一同使用， 简单又强大。

* [iTerm 2 && Oh My Zsh博客](http://www.zhihu.com/question/20873070/answer/43230384)
* [终极shell](http://tieba.baidu.com/p/2818750493)

### 1. 下载一个 .oh-my-zsh 配置（推荐有）

```ruby
$: git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

### 2. 创建新配置（ 备份）

```ruby
$: cp~/.zshrc ~/.zshrc.orig
$: cp~/.oh-my-zsh/templates / zshrc.zsh - template~/.zshrc
```

### 3. 把 zsh 设置成默认的 shell

```ruby
$: chsh - s / bin / zsh
```

### 4. 重启 zsh(打开一个新的 terminal 窗口）

* 配置
* 主题： agnoster
* 字体： Powerline(把 iTerm 2 的设置里的 Profile 中的 Text 选项卡中里的 Regular Font 和 Non - ASCII Font 的字体都设置成 Powerline 的字体。 ）
* 推荐使用 14 pt Meslo LG S DZ Regular

> * [Powerline— Powerline beta documentation](https: //powerline.readthedocs.org/en/master/)
> * [powerline / fonts· GitHub](https: //github.com/powerline/fonts)

* 设置命令正确绿色高亮， 错误红色高亮

```ruby
$: git clone git: //github.com/jimmijj/zsh-syntax-highlighting ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
```

* 然后在~/.zshrc中插件那添加 `plugins=(zsh-syntax-highlighting)`

* 加强zsh的补全功能实现tab自动纠错
* 把这两句话添加到 `oh-my-zsh/lib/completion.zsh` (末尾）

```ruby
zstyle ':completion:incremental:*'
completer _complete _correct
zstyle ':completion:*'
completer _complete _prefix _correct _prefix _match _approximate
```

---

## zsh 好处

### 1. zsh 可以**补全参数**

当你敲指令敲到一般的时候， 不必在虚拟终端下Ctrl_Shift_T 打开一个新标签看手册了， 只需要一个`<Tab>`， zsh 会为你列出所有符合你已经输入部分的参数， 其后跟着参数说明， 你需要的只是看下其后的说明， 然后选中你需要的参数按下回车键。 视频中我们差一点就用纯tab 完成了一条dd 指令。

### 2. zsh 的**参数补全是智能补全**

简单的例子：
当你输入ls 指令按下`<Tab>` 的时候， zsh 会列出目录下所有的文件并让你交互式处理。
当你输入unzip 指令要求补全的时候， zsh 只会列出zip 文件
当你输入kill 指令要求补全的时候， zsh 会列出所有符合要求的进程并自动把参数转换为PID.
当你输入参数的一部分时（例如systemctl 的--type=, -t)， zsh 会列出其后所有的可能性供你选择。

### 3. zsh 可以**补全路径**

当你想到你的vim 插件目录下看看的时候， 你甚至连cd 都不需要输入， 你要做的只是/u/s/v/vimf/p`<Tab>``<Enter>`

### 4. zsh 可以**不额外安装autojump 在目录中快速跳转**

安装oh-my-zsh 后， 在你的plugins=() 中加入jump(事实上这个插件提供的是几个函数）。 之后mark dir 标记一个目录， 下次jump dir 就可以快速跳转到该目录。

### 5. zsh 可以**自动纠错指令**

当你输入了错误的指令时， 如果只是几个字母按错了， 一个`<Tab>` zsh 就会为你自动纠错。
你可以利用这个特性缩写指令， 例如把systemd-analyze 变成sys-an`<Tab>`。

### 6. zsh 可以**预先告知你指令中的错误**

zsh 会将错误的指令显示为红色， 正确的指令（或者函数、 alisa)会被显示为绿色。
至于目录和文件， 虚拟终端下， 存在的文件或目录会被显示为下划线形式， tty 下则是绿色， 不存在的都会被现实为普通的白色。
所以当你重定向> file, 如果file 带下划线， 你会事先明白你的操作会清空一个已经存在的文件而不是重定向到新文件。 这个特性对于新手来说是非常有用的。

### 7. zsh 可以**补全环境变量**

环境变量大多数都比较难记， 而且大小写都有， 感到很困难？ zsh 中一个tab 为你列出所有符合期望的环境变量， 你做的只是按上下左右键挑选一个即可。

### 8. zsh 有**多重定向**的功能

简单的例子：
当你指令后跟着“>/dev/null >1 >2" 的时候， zsh 明白你的意思是将stdout 分别重定向到三个流， 但是bash 就无法如此。
而当你后跟“>/dev/null 2>&1 &" 的时候， zsh 明白你的意思是将stdout 和stderr 都重定向到一个流。
zsh 会推断你的意图， 如果你是perl 用户， 你会很熟悉这种行为。

### 9. zsh 可以**提示通配符的作用范围**

不知道有多少人有过“rm -rf dir/<空格>* " 的悲剧——你想清空目录其下的文件并保留目录， 结果删除了当前目录下所有的文件。
zsh 会将被通配符作用的参数显示为深蓝色， 当你手贱在“dir/" 和“*" 之间敲了一个回车的时候， "/dir" 会立刻变白， 你会明白我的通配符无法作用于“dir/"， 从而预料到这条指令可能造成什么后果。
事实上： zsh 也有着防手贱的能力， 当你rm -rf dir/* 的时候， 即使带着-f 参数， zsh 仍然会询问你是否真的想这样做（但是不要认为zsh 总会这样）。

### 10. zsh 可以**有区分的提示指令历史**

在你的。 zshrc 的plugins=() 中添加history 插件， 简单的例子：
在目录A 下输入ls 按上箭头， zsh 会提示你所有在目录A 下执行的ls 指令——zsh 绝对不会补全一个在其他目录下指令的ls 指令的， 因为zsh 明白即使补全了， 这条指令也对你毫无用处。
当然这样做有好有坏， 如果你不喜欢这个特性， 不要启用history 插件。

### 11. zsh 内置了大量的**命令提示符样式**

.zshrc 的plugins=() 中添加theme 插件， 敲theme 指令回车可以随机选择， 后跟参数可以选择指定的样式， 例如theme gen`<Tab>``<Enter>` 会切换到gentoo 样式， 这也是新手美化过程中非常痛苦的一环。

### 12. zsh **可以alisa 参数**

相对于其他shell 的alisa 指令， zsh 中你可以为参数alisa 一个缩写！

### 13. zsh **脚本的语法更加顺手**

简单的例子： bash 中设置PATH, 你需要PATH 后跟长长的一串， 然而zsh 中可以写成
PATH=(
dir1
dir2
dir3
……
)

### 14. zsh 的**配置非常省心**

安装oh-my-zsh 后， 配置都已经被继承， 你可以很简单的配置好一个舒服的zsh——我的。 zshrc 除去成片的alisa 之外， 有效配置只有十几行。
