---
title: Super Pi进行CPU测试
date: 2018-07-07 13:57:27
tags: [cpu]
categories: [BenchMark]
---

## super pi 介绍

通过计算指定位数的圆周率π小数点的位数， 统计时间， 即可得知当前CPU的性能， 花费时间越短， 性能越优秀。

Linux下可以直接用shell的反正切函数去计算， 如下计算5000位所用时间， 命令如下：

```bash
time echo "scale=5000; 4*a(1)" | bc -l -q
```

> super pi默认只会使用一个cpu核心去运行， 这个样并不能测试出cpu的实际性能， 因此通常我们都是测试一个进程和多个进程的结果来衡量CPU的性能。

### 1. 单进程

只跑一个super pi 进行测试， 获取最终计算消耗的时间， 越少越好。

```shell
$: time echo "scale=5000; 4*a(1)" | bc -l -q
```

### 2. 多进程

 跑满所有CPU核心， 一个核心一个进程， 使用进程绑定， 获取所有进程结果的平均值。

```shell
#!/usr/bin/env bash
cpu_c= `cat /proc/cpuinfo | grep process | wc -l`
need_run_cpu_num=$(($cpu_c-1))
for cpu_seq in `seq 0 $need_run_cpu_num` ; do
      time echo "scale=${bits}; 4*a(1)" | taskset -c ${cpu_seq} bc -l -q &>1 | grep '^[rus]'
done
```

> 由于super pi 测试很快， 为了排除干扰， 提高准确性， 通常进行多测测试， 取平均值。 通常5000位大概需要花费20多秒的时间。

```bash
#!/usr/bin/env bash
for i in `seq $20` ; do
    time echo "scale=500000000; 4*a(1)"|bc -l -q &
done
```
