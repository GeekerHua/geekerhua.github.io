---
title: Python枚举的实现
date: 2017-06-14 13:05:26
tags: [Python]
categories: [编程]
---

在Python3.4版本之前， 默认是没有枚举的， 我们经常使用的Python2.x的版本， 如果想实现枚举的功能该怎么办呢？ 代码是人写出来的， 这难不倒我们的， 因此利用动态语言的特性， 就出现了下面的众多中的枚举实现。

## 枚举的实现

### 1. 使用类属性

```Python

>>> class Seasons:

...     Spring = 0
...     Summer = 1
...     Autumn = 2
...     Winter = 3
...

>>> print Seasons. Spring

```

上边的例子可以简化成：

```Python

>>> class Seasons:

...     Spring, Summer, Autumn, Winter = range(4)
```

### 2. 借助函数

```Python

>>> def enum(*posarg, **keysarg):

...     return type("Enum", (object, ), dict(zip(posarg, xrange(len(posarg))), **keysarg))
...

>>> Seasons = enum("Spring", "Summer", "Autumn", "Wunter"=1)
>>> Seasons. Spring

0
```

### 3. 使用 `collections.namedtuple`

```Python

>>> Seasons = namedtuple('Seasons', 'Spring Summer Autumn Winter')._make(range(4))
>>> print Seasons. Spring

0
```

Python中枚举的替代方法远不止这些， 就不一一列举了。 但这些替代实现有哪些不合理的地方呢？

## 枚举实现的缺陷

### 1. 允许枚举值重复

以 `collections.namedtuple` 为例， 下面的例子中枚举值 `Spring` 与 `Autumn` 相等， 但却不会提示任何错误。

```Python

>>> Seasons._replace(Spring = 2)

Seasons(Spring = 2, Summer = 1, Autumn = 2, Winter = 3) # Spring和Autumn的值相等， 都为2
```

### 2. 支持无意义的操作

```Python

>>> Seasons. Summer + Seasons. Autumn == Seasons. Winter

True # Seasons. Summer+Seasons. Autumn相加无任何实际意义
```

## 2.7后的替代方案----[flufl.enum](http://Pythonhosted.org/flufl.enum/docs/using.html)模块（第三方）

> 它包含两种枚举类：

* 一种是Enum, 只要保证枚举值唯一即可， 对值的类型没有限制；
* 另一种是IntEnum, 其枚举值为int型

```Python
from flufl.enum import Enum

>>> class Seasons(Enum):

...:     Spring = 'Spring'
...:     Summer = '2'
...:     Autumn = 3
...:     Winter = 4
...:

>>> Seasons. Autumn

3

>> >
>>> Weak = Enum('Weak', 'Monday Wednesday')
>>> Weak. Monday

2
```

可使用 `value` 来获取枚举元素的值

```Python

>>> Weak. Monday

0

>>> getattr(Weak, 'Wedsday').value

1
```

 `flufl.enum` 不支持枚举元素的比较。

## 迟来的官方支持----Enum(>=3.4)

直到Python3.4版本， 官方才加入了枚举Enum. 其实现主要参考了 `flufl.enum` 。
