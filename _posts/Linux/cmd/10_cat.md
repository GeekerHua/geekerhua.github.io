---
title: Linux命令10：cat
date: 2017-11-16 15:00:56
tags: Linux
categories: Linux命令
---

## cat

> cat命令的用途是连接文件或标准输入并打印。这个命令常用来显示文件内容，或者将几个文件连接起来显示，或者从标准输入读取内容并显示，它常与重定向符号配合使用。

1. 一次显示整个文件:cat filename
2. 从键盘创建一个文件:cat > filename 只能创建新文件,不能编辑已有文件.
3. 将几个文件合并为一个文件:cat file1 file2 > file

## 常用参数

| 缩略参数 | 完整参数  | 描述
| --- | --- | ---
| -A | --show-all | 等价于 -vET
| -b | --number-nonblank | 对非空输出行编号
| -e | | 等价于 -vE
| -E | --show-ends | 在每行结束处显示 $
| -n | --number | 对输出的所有行编号,由1开始对所有输出的行数编号
| -s | --squeeze-blank | 有连续两行以上的空白行，就代换为一行的空白行
| -t | | 与 -vT 等价
| -T | --show-tabs  | 将跳格字符显示为 ^I
| -v | --show-nonprinting | 使用 ^ 和 M- 引用，除了 LFD 和 TAB 之外