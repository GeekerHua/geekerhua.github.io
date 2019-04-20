---
title: hexo搭建自动化blog系统
date:  2019/4/18  13:21:26
tags: [blog, hexo]
categories: [other]
---



# hexo + github + travis 搭建省心的blog

 **目标**: 

1. 使用hexo搭建一套blog系统。
2. 使用github pages 展示我们的静态blog。
3. 借助travis实现blog的自动渲染及部署，真正省心。



## 通过本教程能够学到如下知识点

1. hexo的搭建与使用技巧。
2. github pages的使用及coding pages的使用。
3. 域名绑定与解析。
4. 个人开通免费的https。
5. 打造个人完整的blog及笔记体系。



## 主流的个人blog分析

1. [ Jekyll](http://jekyllrb.com/docs/quickstart/)， 基于ruby，GitHub Pages支持的构建工具。但是UI比较丑，没有较好的文档。基于ruby增加了一定的难度。
2. [hexo](https://hexo.io/zh-cn/)，基于node，对大部分程序员来说都很友好。有很多主题供选择，构建速度非常块，配置简单。

**静态网站和动态网站相比有如下好处**：

- 省钱。静态网站占用的系统资源少。如果挂到github pages上，只要注册一个域名就可以了。
- 速度快。不经过php解析器，不用数据库，速度自然比动态网站快
- 安全。由于静态网站的简洁，免疫很多web攻击方式。
- 服务器端配置简单。只需要一个web server（apache、nginx）。
- 非常容易维护。

## 搭建[hexo](https://hexo.io/zh-cn/)本地blog系统

官网给出了相当简单了例子。

```shell
npm install hexo-cli -g
hexo init blog
cd blog
npm install
hexo server
```

只需要这几行代码就可以搭建出一个初步的blog，但真实丑的不忍直视，这主要是默认的主题比较丑，换个主题，增加一些插件就好了。

### 1. 基础设置

修改``__config.yml`文件，这个文件定义了如下内容：

1. 使用哪个主题
2. 网站名称
3. 语言
4. 时区
5. 各个资源文件夹名称
6. 书写规范
7. 部署设置
8. 文章分页情况
9. 一些插件的设置

### 2. 主题设置

主题的设置也是用了``__config.yml` 文件，在`themes/主题/__config.yml`。这里定义了打两个个性化内容

包括logo，icon，背景图，友情链接，分享设置，个人联系方式，站长统计等。这些配置都是基于这个主题的功能实现的，当然我们也可以根据个人的喜好进行定制化。



## 部署到GitHub Pages。



## 自定义域名及HTTPS



## 使用travis进行自动化部署





