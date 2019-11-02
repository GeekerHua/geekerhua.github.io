---
title: Linux命令--ls
date: 2017-10-25 15:39:43
tags: [Linux, Shell]
categories: [linux]
permalink: shell_ls
---

> ls命令是用来列出制定路径的文件及文件夹。

## 格式

``` bash
ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]
```

## 常用参数

| 命令    | 描述                                               |
|---------|----------------------------------------------------|
| ls -alh | 以列表的形式，显示当前目录全部内容，并显示出容易理解的文件大小 |

## 命令参数

| 缩略参数 | 完整参数  | 描述
| --- | ---- | ----
| -a | –all | 列出目录下的所有文件，包括以 . 开头的隐含文件
| -A | | 同-a但不列出“.”(表示当前目录)和“..”(表示当前目录的父目录)。
| -c | | 配合 -lt：根据 ctime 排序及显示 ctime (文件状态最后更改的时间)配合 -l：显示 ctime 但根据名称排序否则：根据 ctime 排序
| -C | |每栏由上至下列出项目
|  | –color[=WHEN] | 控制是否使用色彩分辨文件。WHEN 可以是'never'、'always'或'auto'其中之一
| -d | –directory | 将目录象文件一样显示，而不是显示其下的文件。
| -D | –dired | 产生适合 Emacs 的 dired 模式使用的结果
| -f | | 对输出的文件不进行排序，-aU 选项生效，-lst 选项失效
| -g | | 类似 -l, 但不列出所有者
| -G | –no-group | 不列出任何有关组的信息
| -h | –human-readable | 以容易理解的格式列出文件大小 (例如 1K 234M 2G)
| –si | | 类似 -h, 但文件大小取 1000 的次方而不是 1024
| -H | –dereference-command-line | 使用命令列中的符号链接指示的真正目的地
|  | –indicator-style=方式 |指定在每个项目名称后加上指示符号<方式>：none (默认)，classify (-F)，file-type (-p)
| -i | –inode | 印出每个文件的 inode 号
| -I | –ignore=样式 | 不印出任何符合 shell 万用字符<样式>的项目
| -k | | 即 –block-size=1K, 以 k 字节的形式表示文件的大小。
| -l | |除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来。
| -L | –dereference | 当显示符号链接的文件信息时，显示符号链接所指示的对象而并非符号链接本身的信息
| -m | | 所有项目以逗号分隔，并填满整行行宽
| -o | | 类似 -l, 显示文件的除组信息外的详细信息。
| -r | –reverse |  依相反次序排列
| -R | –recursive | 同时列出所有子目录层
| -s | –size | 以块大小为单位列出所有文件的大小
| -S | | 根据文件大小排序
|  | –sort=WORD | 以下是可选用的 WORD 和它们代表的相应选项：extension -X status -c \n none -U time -t ; size -S atime -u ; time -t access -u ; version -v use -u
| -t | | 以文件修改时间排序
| -u | | 配合 -lt: 显示访问时间而且依访问时间排序；配合 -l: 显示访问时间但根据名称排序，否则：根据访问时间排序
| -U | | 不进行排序; 依文件系统原有的次序列出项目
| -v | |根据版本进行排序
| -w | –width=COLS | 自行指定屏幕宽度而不使用目前的数值
| -x | | 逐行列出项目而不是逐栏列出
| -X | | 根据扩展名排序
| -1 | |每行只列出一个文件
| | –help | 显示此帮助信息并离开
| | –version | 显示版本信息并离开
