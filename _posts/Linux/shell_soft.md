---
title: 常用的shell下的工具
date:  2019/7/6 23:03:07
tags: [shell]
categories: [linux]
permalink: shell_soft
---

## pandoc-文件转换

### 从HTML格式转换为reStructuredText格式

``` bash
pandoc -t rst myFile.html -o myFile.rst
```

## ffmpeg-音视频转换

[ffmpeg-官方链接](https://ffmpeg.org/ffmpeg.html)

### 使用FFmpeg把一个AVI格式的视频文件转换为一个Ogg格式的视频文件

``` bash
ffmpeg -i myVideo.avi myvideo.ogg
```

## LibreOffice-工作文档转换

[Home | LibreOffice - Free Office Suite - Fun Project - Fantastic People](http://libreoffice.org/)

### 使用LibreOffice把一组幻灯片转换成PDF， 你可以使用如下命令行内容：

``` bash
soffice --headless --convert-to pdf mySlides.odp
```

### 将某文件夹中所有的微软Word文档转换为LibreOffice Writer文件格式

``` bash
soffice --headless --convert-to odt *.docx
```

## you-get

> you-get可以下载多个网站的视频文件， 类似于mac下的软件 `Downie` 。

使用homebrew进行安装

``` bash
$: brew install you-get
```

* 下载视频

``` bash
$: you-get URL
```

* 显示可下载的格式及大小

``` bash
$: you-get -i URL
```

## autojump

> 经常在终端进行操作的时候，路径的频繁切换是一件很麻烦的事情。使用autojump能够快速的在经常使用的路径中切换，省了不少麻烦。

> [参考文章](http://www.jianshu.com/p/23aeb7c4d89b)

### 安装

``` bash
$: brew install autojump
```

``` bash
$: echo '[ -f /usr/local/etc/profile.d/autojump.sh  ] && . /usr/local/etc/profile.d/autojump.sh' >> .zshrc
$: source ~/.zshrc
```

### 常用方法

``` bash
// 进入目录
j dir

// 子目录
jc child

// 打开目录
jo dir

// 打开子目录
jco

// 两个 inbox
> 30   /home/user/mail/inbox
> 10   /home/user/work/inbox
j in   //自动进入权重高的
j w in   //加个关键词呗
```
