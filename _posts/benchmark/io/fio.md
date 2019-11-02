---
title: fio磁盘测试
date: 2018-07-07 13:56:10
tags: [io]
categories: [benchmark]
permalink: fio
---

## 1.fio 介绍

fio是一个基于命令行的磁盘测试工具， 能够准确的反映出磁盘的性能。 fio是C语言写的， 所以可以通过源码在不同平台进行编译安装。
<https://github.com/axboe/fio>

## 2. 安装

fio的安装需要一些依赖包， 而且fio测试需要指定引擎， 比如linux下常用引擎为 `libaio` ， windows下有专用的 `windowsaio` 。

### 2.1 libaio

libaio是fio的测试引擎

``` bash
$: yum install -y libaio libaio-devel
```

or

``` bash
$: wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/libaio-0.3.109-13.el7.x86_64.rpm
$: wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/libaio-devel-0.3.109-13.el7.x86_64.rpm
$: rpm -ivh libaio-0.3.109-13.el7.x86_64.rpm
$: rpm -ivh libaio-devel-0.3.109-13.el7.x86_64.rpm
```

### 2.2 下载fio源码包

``` bash
$: wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/fio-2.21.tar.gz
```

### 2.3 安装gcc编译器

``` bash
$: yum install -y gcc

```

### 2.4 安装fio

``` bash
$: tar zxvf fio-2.21.tar.gz
cd fio-fio-2.21
./configure && make && make install
```

## 3. 测试

### 3.1 参数介绍

``` bash
ioengine : 引擎
bs :block size, 测试区块大小
iodepth : 测试深度
direct=1
filename : 测试文件路径， 指定位置为要测试的磁盘
group_reporting=1
runtime : 测试时间
rwmixread : 读写混合测试， 读的比例
rw : 测试类型， 顺序读， 顺序写， 随机读， 随机写， 随机读写等
numjobs :

```

### 3.2 参数选择

1. 测试IOPS时， `bs=4k` ， `iodepth=128` , rw选择随机读、 写
2. 测试bandWidth时， `bs=1024k` , `iodepth=64` , rw选择顺序读、 写
3. 测试latency时， `bs=4k` , `iodepth=1` , rw选择随机读、 写

### 3.3 案例

**多路随机写磁盘测试**

``` bash
$: fio -filename=/dev/sdc -direct=1 -iodepth=128  -thread -rw=randwrite -ioengine=libaio -bs=4k -size=10G  -numjobs=1  -runtime=300 -group_reporting  -name=iotest
```

**2. 单路随机读写测试， 读占70%。**

``` bash
$: fio -filename=/dev/sdc -direct=1 -iodepth=1  -thread -rw=randrw rwmixread=70 -ioengine=libaio -bs=4k -size=10G  -numjobs=1  -runtime=300 -group_reporting  -name=iotest
```

### 3.4 多块盘测试

多块磁盘测试方法与单盘相同， 有几块磁盘就同时跑几个fio测试， 测试结束后， 结果相加即为IOPS或BandWidth结果。

## 4. 结果分析

![fio/2019-11-1-23-19-4.png](http://img.geekerhua.com/blog/fio/2019-11-1-23-19-4.png)
