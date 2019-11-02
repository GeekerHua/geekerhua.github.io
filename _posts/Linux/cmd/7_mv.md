---
title: Linux命令--mv
date: 2017-11-16 14:33:16
tags: [Linux, Shell]
categories: [linux]
permalink: shell_mv
---

> 移动或者修改文件名称

## 常用参数

| 缩略参数 | 完整参数  | 描述
| --- | --- | ---
| -b |  | 若需覆盖文件，则覆盖前先行备份
| -f |  | 强制的意思，如果目标文件已经存在，不会询问而直接覆盖
| -i |  | 若目标文件 (destination) 已经存在时，就会询问是否覆盖！交互式操作
| -u| --update | 若目标文件已经存在，且 source 比较新，才会更新(update)
| -t| --target-directory=DIRECTORY | 即指定mv的目标目录，该选项适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后
| | --help   |  显示此帮助信息并退出
| | --version | 输出版本信息并退出
