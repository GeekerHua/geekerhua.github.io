---
title: RancherOS
date:  2019/5/7  9:37:11 PM
tags: [docker, OS]
categories: [OS]
---

## 介绍

## 安装

### 将系统写入tf卡

1. tf卡格式化成FAT32格式，然后卸载
2. [使用dd写入镜像](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)

    ```shell
    $: sudo dd bs=1m if=${path_of_your_image.img} of=/dev/${diskn} conv=sync
    ```

3. [扩展全部存储卡](https://www.cnrancher.com/docs/os/v1.x/en/installation/running-rancheros/server/raspberry-pi/)
