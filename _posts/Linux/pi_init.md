---
title: 树莓派初始化
date:  2019/5/11  9:21:46 PM
tags: [Linux, 树莓派]
categories: [Linux满汉全席]
---

## 局域网内树莓派到识别扫描

> 状态没有屏幕，但有网线

### 1. 使用arp进行设备扫描，如下图，是使用网线直连电脑到结果，可以直接识别hostname。

使用网线将树莓派与电脑进行连接，此时两台设备处于同一个局域内。使用arp工具扫描局域网设备

```shell
$ arp -a
raspberrypi.local (169.254.117.22) at b8:27:eb:42:a9:53 on en4 [ethernet]
? (192.168.0.1) at 78:44:fd:46:32:c0 on en0 ifscope [ethernet]
? (192.168.0.112) at f4:5c:89:9f:65:2b on en0 ifscope [ethernet]
? (192.168.0.114) at 5c:ad:cf:e9:31:a0 on en0 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en4 ifscope permanent [ethernet]
```

如上，第一个就是树莓派。知道ip就可以直接通过ssh进行连接。然后手动更改wifi密码，之后就可以连接到wifi了。

### 2. 使用[pi-oi](http://github.com/thoqbk/pi-oi)进行扫描,对wifi下到扫描效果很好

```shell
$ java -jar pi-oi.jar

PI-OI is finding your Pi ...
+-----------------------------------------------------------------------------------------+
| Address            | Host response                          | Could be a Pi    | Time   |
+-----------------------------------------------------------------------------------------+
| 192.168.0.116      | SSH-2.0-OpenSSH_6.7p1 Raspbian-5deb    |                  | 19s    |
+-----------------------------------------------------------------------------------------+
Tho Q Luong, http://github.com/thoqbk/pi-oi
```

## WIFI密码设置

### 1. 查看已经识别的wifi，记录ssid值

```shell
sudo iwlist wlan0 scan
```

### 2. 修改网络自动连接，/etc/network/interfaces

```shell
iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

### 3. 在`/etc/wpa_supplicant/wpa_supplicant.conf`文件中添加wifi配置, 可以配置多个wifi

```shell
network={
    ssid="TMWHCM"
    key_mgmt=WPA-PSK
    psk="68880961"
    priority=5
}
```

> priority 是指连接优先级，数字越大优先级越高（不可以是负数）。

### 4. 连接wifi，重启

```shell
sudo reboot
```

## [vnc远程桌面连接](http://shumeipai.nxez.com/2013/09/04/login-rpi-with-vnc.html)

能够访问网络了，当然是要把远程桌面开开才好用了，关键时刻很好用啊。

### 1. 安装

1.1 安装tightvncserver

```shell
$: apt install tightvncserver
```

1.2 设置密码

```shell
$: vncpasswd
```

### 2. 启动vnc服务

```shell
$: tightvncserver #- vncserver :1 - geometry 1280x1080-depth 24
```

> 指定尺寸

```shell
tightvncserver -geometry 800x600 :1
```

### 3. 终止vnc

```shell
tightvncserver -kill :1
```

### 4. 开机自启

4.1 将下方代码添加到`/etc/init.d/tightvncserver`

```shell
### BEGIN INIT INFO
# Provides:          tightvncserver
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop tightvncserver
### END INIT INFO

# More details see:
# http://www.penguintutor.com/linux/tightvnc

### Customize this entry
# Set the USER variable to the name of the user to start tightvncserver under
export USER='pi'
### End customization required

eval cd ~$USER

case "$1" in
start)
    # 启动命令行。此处自定义分辨率、控制台号码或其它参数。
    su $USER -c '/usr/bin/tightvncserver -depth 16 -geometry 800x600 :1'
    echo "Starting TightVNC server for $USER "
    ;;
stop)
    # 终止命令行。此处控制台号码与启动一致。
    su $USER -c '/usr/bin/tightvncserver -kill :1'
    echo "Tightvncserver stopped"
    ;;
*)
    echo "Usage: /etc/init.d/tightvncserver {start|stop}"
    exit 1
    ;;
esac
exit 0
```

4.2 可以设置开机自启，看个人需求

```shell
sudo chmod 755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults
```
