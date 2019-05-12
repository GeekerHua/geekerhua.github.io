---
title: samba
date: 2017-08-01 16:12:02
tags: [Linux]
categories: [Linux满汉全席]
---

## 安装（如果需要）

```bash
$: sudo apt-get install samba samba-common
```

##  设置共享目录

新建权限为777的文件夹， 用来当共享文件夹。

```bash
$: chmod -m 777 /home/share
```

## 修改samba的配置文件

```bash
$: vi /etc/samba/smb.conf
```

在末尾添加如下代码

```yuml
[share]

    path = /home/share
    available = yes
    browseable = yes
    writable = yes# public = yes.#不需要密码

```

## 创建samba账户

```bash
$: touch /etc/samba/smbpasswd
$: sudo smbpasswd -a name
```

## 重启samba

```bash
$: /etc/init.d/smbd restart
```

或使用service进行管理

```bash
$: service smbd start
```
