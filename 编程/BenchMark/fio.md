## fio 介绍

fio是一个基于命令行的磁盘测试工具，能够准确的反映出磁盘的性能。

## 1.准备

安装

```shell
fio安装：

wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/fio-2.21.tar.gz

wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/libaio-0.3.109-13.el7.x86_64.rpm

wget http://common-pkgs.oss-cn-beijing.aliyuncs.com/fio/libaio-devel-0.3.109-13.el7.x86_64.rpm

rpm -ivh libaio-0.3.109-13.el7.x86_64.rpm

rpm -ivh libaio-devel-0.3.109-13.el7.x86_64.rpm

tar zxvf fio-2.21.tar.gz

cd fio-fio-2.21

yum install -y gcc

./configure && make && make install
```





## 2.测试

```shell
测试随机写IOPS命令：
$ fio -filename=/dev/sdc -direct=1 -iodepth=128  -thread -rw=randwrite -ioengine=libaio -bs=4k -size=10G  -numjobs=1  -runtime=1000 -group_reporting  -name=iotest
```

```shell
# 测试顺序写带宽
$ fio -direct=1 -iodepth=64 -rw=write -ioengine=libaio -bs=1024k -size=10G -numjobs=1 -runtime=300 -group_reporting  -name=Write_PPS_Testing -filename=/dev/vdb 
```

## 3.结果分析



