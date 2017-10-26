---
title: Python装饰器
date: 2017-08-07 09:12:59
tags: Python
categories: 编程
---

## 方法装饰器

```python
import functools

def log(text_func):
    if hasattr(text_func,'__call__'):
        # 下边这句话是让调用者房名的func.__name__显示成实际方法，而不是wrapper
        @functools.wraps(text_func)
        def wrapper(*args, **kwargs):
            print 'call %s()' % (text_func.__name__)
            result = text_func(*args, **kwargs)
            print result
            return result
        return wrapper
    else:
        def decordor(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print '%s call %s()' % (text_func, func.__name__)
                result = func(*args, **kwargs)
                print result
                return result
            return wrapper
        return decordor
        
@log('excute')
def now():
    print '2016-08-07'
    # 函数方法名
    print now.__name__
    return '333'

@log
def now2():
    print '2016-08-07'
    print now.__name__
    return '333'

```


## 类装饰器

```python
import functools

class Foo(object):
    def __init__(self, txt):
        self.txt = txt
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print ('class decorator runing')
            print func.__name__
            print self.txt
            print ('class decorator ending')
            return func(*args, **kwargs)
        return wrapper

@Foo('22')
def bar():
    print '-'*10
    print bar.__name__
    print ('bar')
    lambda x: x +2

bar()

```