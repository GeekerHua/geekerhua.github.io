---
title: Bash拾遗
date:  2019/5/11  9:40:43 PM
tags: [Shell, Linux]
categories: [Linux满汉全席]
---

## 内建指令

> 优先执行的指令， 并将结果返回。

```shell
 使用 `command` 反引号， 或者 `$( command )` 的形式。
```

* 查看当前语言环境： `locale`
* 查看所有支持的语言环境： `locale -a`
* 设置语言环境： `LANG=zh_CN.UTF-8`

## declare变量宣告

> bash默认变量为字符串， 需要使用declare才能变成array、 数值类型

* declare number=$a*$b

## 变量操作

### 删除

* \# 代表： 从变数内容的最前面开始向右删除

  * \# ： 符合取代文字的『最短的』那一个
  * \

## ： 符合取代文字的『最长的』那一个

* \% 代表： 从后面向前删除变数内容

  * \% ： 符合取代文字的『最短的』那一个
  * \%% ： 符合取代文字的『最长的』那一个

### 替换

* ${变数/旧字串/新字串}

  * 若变数内容符合『旧字串』则『第一个旧字串会被新字串取代』

* ${变数//旧字串/新字串}

  * 若变数内容符合『旧字串』则『全部的旧字串会被新字串取代』

### 变量测试

| 变数设定方式     | str 没有设定       | str 为空字串      | str 已设定非为空字串 |
|------------------|--------------------|-------------------|----------------------|
| var=${str-expr}  | var=expr           | var=              | var=$str             |
| var=${str:-expr} | var=expr           | var=expr          | var=$str             |
| var=${str+expr}  | var=               | var=expr          | var=expr             |
| var=${str:+expr} | var=               | var               | var=expr            |
| var=${str=expr}  | str=expr  var=expr | str不变 var=      | str不变  var=$str    |
| var=${str:=expr} | str=expr var=expr  | str=expr var=expr | str不变 var=$str     |
| var=${str?expr}  | expr 输出至stderr  | var=              | var=$str             |
| var=${str:?expr} | expr 输出至stderr  | expr 输出至stderr | var=$str             |

## 标准输入

| 指令        | 说明                         |
|-------------|------------------------------|
| >, >>        | STDOUT                       |
| 2>, 2>>      | STDERR                       |
| > list 2>&1 | 正确错误都重定向到list文件中 |

## 命令执行的判断依据： ; , &&, ||

* `;` 不考虑指令相关性的连续指令下达
* `&&` 前一条命令执行成功， 则执行
* `||` 前一条命令执行失败， 则执行

> 常用组合

command1 && command2 || command3
相当于 command2 if command1 or command3

## 管道 `|` 常用工具

* grep | 查找
* cut | 截取
* wc | 行数、 word、 字符数量统计
* sort | 排序
* uniq | 去重
* tee |  双向重导向， 不影响屏幕的显示的同时， 保存一份到文件， -a是追加
* tr | 字符替换与删除
* col | tab-space互转
* join | 相同资料行合并
* paste | 将两行贴在一起， 且中间以[tab]键隔开
* expand | 将[tab] 按键转成空白键
* split | 文件分割
* xargs | 参数代换
* -减号 | 在管道命令中用来替换文件名， 省略文件名的作用

