---
title: Linux命令4：mkdir
date: 2017-10-25 16:19:43
tags: [Linux, Shell]
categories: [linux]
---

## mkdir

> mkdir 命令用来创建指定的名称的目录，要求创建目录的用户在当前目录中具有写权限，并且指定的目录名不能是当前目录中已有的目录。

## 常用参数

| 缩略参数 | 完整参数  | 描述 | 例子
| --- | --- | --- | ---
| -m | --mode=模式 | 设定权限<模式> (类似 chmod)，而不是 rwxrwxrwx 减 umask | `mkdir -m 777 test` 创建权限为777的test目录
| -p | --parents | 可以是一个路径名称。此时若路径中的某些目录尚不存在,加上此选项后,系统将自动建立好那些尚不存在的目录,即一次可以建立多个目录; | `mkdir -p test1/test2` 递归创建test2目录
| -v | --verbose | 每次创建新目录都显示信息
| |  --help  | 显示此帮助信息并退出
| |  --version | 输出版本信息并退出

## 实例
创建项目的目录结构
`mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}`

``` bash
[root@localhost test]# mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}
mkdir: 已创建目录 “scf”
mkdir: 已创建目录 “scf/lib”
mkdir: 已创建目录 “scf/bin”
mkdir: 已创建目录 “scf/doc”
mkdir: 已创建目录 “scf/doc/info”
mkdir: 已创建目录 “scf/doc/product”
mkdir: 已创建目录 “scf/logs”
mkdir: 已创建目录 “scf/logs/info”
mkdir: 已创建目录 “scf/logs/product”
mkdir: 已创建目录 “scf/service”
mkdir: 已创建目录 “scf/service/deploy”
mkdir: 已创建目录 “scf/service/deploy/info”
mkdir: 已创建目录 “scf/service/deploy/product”
[root@localhost test]# tree scf/
scf/
├─ bin
├─ doc
│   ├─ info
│   └─ product
├─ lib
├─ logs
│   ├─ info
│   └─ product
└─ service
    └── deploy
        ├─ info
        └─ product

12 directories, 0 files
[root@localhost test]#

```
