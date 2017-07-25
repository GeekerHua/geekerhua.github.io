mac是类Unix系统，拥有众多的终端工具。而类Unix系统都有属于它自己的终端工具管理软件。

系统 | 工具
----|----
Mac OS | homebrew
Ubuntu | apt-get
CentOS | yum

## [homebrew](http://brew.sh/index_zh-cn.html)
### homebrew的安装及卸载
- 安装
```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- 卸载
```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

> Homebrew下载的package存放的路径在哪里？
- `~/Library/Caches/Homebrew/`

#### 常用命令
- 安装package
```bash
$ brew install package名
```

- 卸载package
```bash
$ brew uninstall package名
```

- 更新已安装的package
```bash
$ brew update package名
```

## [brew cask](https://caskroom.github.io)
如果说`homebrew`是专门用于安装命令行程序的，那么`brew cask`就是专门用来安装带界面程序的。

安装
```bash
$ brew tap caskroom/cask
```

安装软件(比如chrome)
```bash
$ brew cask install google-chrome
```