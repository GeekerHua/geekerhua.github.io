---
title: SSH
date: 2017-08-01 16:11:54
tags: Linux
categories: Linux工作法
---

## 安装
很多系统自带有，如果没有，使用以下命令安装
```bash
$ sudo apt-get install openssh-server
```
对于mac用户，系统进行了图形化处理，在共享设置中，开启远程登录功能即可

## 设置ssh免密登录

核心在于将客户机的`id_rsa.pub`公钥添加到服务器的`~/.ssh/authorized_keys`文件中,且许保证`.ssh`目录权限700，`.ssh/authorized_keys`文件权限600；
步骤如下

Server:
- ssh-keygen -t rsa   # 生成id_rsa和id_rsa.pub私钥和公钥
- 将客户端的id_rsa.pub添加到服务端.ssh/authorized_keys文件中。
- 可以免密登录了

## 快速设置

```bash
$ # 生成ssh key
$ ssh-keygen
$ # 拷贝ssh key到远程主机，ssh的时候就不需要输入密码了
$ ssh-copy-id remoteuser@remoteserver
$ # ssh的时候不会提示是否保存key
$ ssh-keyscan remote_servers >> ~/.ssh/known_hosts
```

## 基于SSH的服务

### SCP
> 远程拷贝文件,scp -r 的常用方法：

1. 使用该命令的前提条件要求目标主机已经成功安装openssh-server
```bash
$ 如没有安装使用 sudo apt-get install openssh-server 来安装
```
2. 使用格式：
    - scp -r `name`@`host`:`targetPath` `localPath`
    - scp -r `localPath` `name`@`host`:`targetPath`
> 其中`-r`用来复制文件夹，可使用`hostip`代替`name`@`host`



