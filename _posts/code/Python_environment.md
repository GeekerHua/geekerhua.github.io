---
title:  pyenv管理多版本python
date: 2017-02-6 13:46:28
tags: [环境配置, Python]
categories: [code]
permalink: python_develop_environment
---

在工作中不同项目对Python的版本有着不同的要求， Python2与Python3的差异， 是的很多时候我们要同时使用者两种环境来做对比。 众所周知， ipython的交互性设计能带来很大的方便。 最理想的状态下就是能够随时切换Python的版本， 且Python2与Python3能够并存， 并且都能拥有自己的ipython和自己的pip包管理工具。

对于mac电脑来说， 会自带Python2， 该Python在 `/usr/bin/python` ， 这个Python可以使用， 安装插件， 但无法删除。 mac的很多功能都依赖与Python, 因此， 不建议对这个Python进行修改， 安装包等操作。 如果一不小心， 出现问题， 系统就会崩溃。

对于已经从Python官网上下载并安装的情况， 最好把这个Python进行删除。

## 准备

### 删除Python官网下载的Python

1. 删除Python框架
2. sudo rm - rf / Library / Frameworks / Python.framework / Versions / x.x
3. 删除Python程序
4. sudo rm - rf" / Applications / Python x.x "
5. 删除 / usr / local / bin目录下的Python连接

> x.x为Python的版本号

### mac自带Python安装pip

mac自带的Python是没有安装pip的， 已不建议安装。 如果需要安装，
mac里面Python自带easy_install的， 最快的应该就是在terminal里面执行 `sudo easy_install pip` ， 网络好几秒就ok. 运行完可以用pip help测试一下是否安装成功， 成功安装后， 直接pip install numpy或者其他包就可以了。

## [pyenv](https://github.com/yyuu/pyenv/)（最正规的好用的多版本管理工具）

> [参考](http://www.jianshu.com/p/a23448208d9a)

这个pyenv会管理不同版本的Python, 可以随时切换全局的Python版本， 可以Python2与Python3并存， 并且能够指定项目的Python版本。

### 1. 安装pyenv

``` bash
$: brew install pyenv
```

### 2. 添加到环境变量

``` bash
$: echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

> 如果用的是bash, 则将 `.zshrc` 修改为 `.bashrc`

### 3. 应用zsh(bash)设置

``` bash
$: source ~/.zshrc
$: exec $SHELL -l     # 输入命令重启 Shell, 然后就可以重启pyenv
```

### 4. 安装python

``` bash
$: pyenv install 3.6.0 # 安装3.6.0版本
```

### 5. 重建索引

``` bash
$: pyenv rehash
```

### 6. 设置全局pyhon版本

``` bash
$: pyenv global 2.7.13 3.6.0
```

### 7. 指定项目python版本

``` bash
$: pyenv local 3.5.2
```

> 装好后， 如需使用python3的pip, 则使用pip3， 使用python2的pip, 则使用pip或pip2.ipython同理。
> pyenv管理的python位于 `~/.pyenv/versions/` 中， 并且全都在 `~/.pyenv/shims/` 中以软连接的形式存在， 因此， 无论版本怎么切换， `which python` 的结果都应该是 `~/.pyenv/shims/ipython`

## 其他命令

``` bash
$: pyenv version   # 查看当前生效python版本
$: pyenv versions  # 查看已安装版本
$: pyenv install --list # 查看可用版本
```

---

## 安装常见问题

### 1. 安装时出现 `zipimport.ZipImportError: can't decompress data; zlib not available` 错误[官方的解释](https://github.com/yyuu/pyenv/wiki/Common-build-problems)

解决方法1：
$: brew install readline xz
$: CFLAGS = "-I$(xcrun --show-sdk-path)/usr/include"

解决方法2：
1、 安装依赖zlib、 zlib - devel
2、 重新编译安装Python

1. / configure
2. 编辑Modules / Setup文件
3. 找到下面这句， 去掉注释
4. `# zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz`
5. 重新编译安装： make & make install

## sublime支持python3直接运行并显示中文

新建编译环境， 输入以下内容

``` json
{
    "cmd": ["$: which python3 的路径“, "-u", "$file"],
    "env": { "PYTHONIOENCODING": "utf8" }   # 使Python3支持中文
}
```

选择新建的编译环境进行编译。
