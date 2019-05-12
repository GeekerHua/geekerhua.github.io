---
title: Linux命令9：touch
date: 2017-11-16 14:55:25
tags: [Linux, Shell]
categories: [Linux满汉全席]
---

## touch

> 用来修改文件时间戳，或者新建一个不存在的文件

## 常用参数

| 缩略参数 | 完整参数  | 描述
| --- | --- | ---
| -a | --time=atime 或 --time=access 或 --time=use | 只更改存取时间。
| -c | --no-create | 不建立任何文档。
| -d |  |　使用指定的日期时间，而非现在的时间。
| -f |  |　此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题。
| -m | --time=mtime 或 --time=modify |　只更改变动时间。
| -r |  |　把指定文档或目录的日期时间，统统设成和参考文档或目录的日期时间相同。
| -t |  |　使用指定的日期时间，而非现在的时间。
