---
title: Python常量的正确写法
date: 2017-06-12 12:45:26
tags: [Python]
categories: [Code]
permalink: 7EBCDAB8-CC7C-4972-B5AA-84B453444DD1
---

> Python内建的命名空间是支持小部分常量的， 例如True、 False、 None等， 但Python默认是没有提供直接定义常量的方法， 因此要想实现常量的功能需要人为实现。 一般有两种方法

## 一： 通过命名风格提醒使用者该变量代表的意义为常量

> 如长两名所有字母大写， 使用下划线连接各个单词， `MAX_OVERFLOW` 、 `TOTAL` 。 这是一种约定俗称的风格， 对应的值仍然可以改变。

## 二： 通过自定义的类实现常量功能

> 要求符合“命名全部大写”和“值一旦绑定便不可再修改”两个条件。 下面是一种较为常见的解决方法， 它通过对常量对应的值进行修改时或者命名不符合规范时抛出异常来满足以上常量的两个条件。

``` python
class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self. ConstError, "Can't change const.%s" % name
        if not name.isupper():
            raise self. ConstCaseError, 'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()

import constant
# 在这之后定义常量
constant. A = 'a'

```

## 使用

如此之后， 导入这个模块， 在这个模块中定义常量， 建议将所有常量都定义到这个模块中， 方便统一管理。 使用的时候，

* 如果对已经定义到常量进行修改会报 `ConstError` 错误；
* 如果定义的常量不是全大写， 会报 `ConstCaseError` 错误。

例如模块名为constant.py, 在其他文件中使用方法为：

``` python
import constant
constant. A = 'a'
constant. B_Play = 'xxx'
```
