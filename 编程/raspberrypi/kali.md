
## [树莓派TF卡系统烧录](https://sspai.com/post/37356)

1. 查看设备
```bash
$ diskutil list
```

2. 卸载tf卡
```bash
$ diskutil unmountDisk /dev/disk2
```

3. 烧录镜像
```bash
$ sudo dd bs=4m if=/Users/hua/Downloads/kali-linux-2018.1a-rpi3-nexmon.img of=/dev/disk2
```

# kali

> - 默认用户名： root
> - 默认密码： toor

4. 修改apt 源
```bash
vi /etc/apt/sources.list
#阿里云
#deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
#deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
```

4. 切换中文显示
```bash
$ dpkg-reconfigure locales
```
- 选择字符编码：en_US.UTF-8、zh_CN.GBK、zh_CN.UTF-8
- 选择字符：zh_CN.UTF-8（记得用空格）
- 设置完后reboot
 LANG=zh_CN.UTF-8
 LANG="en_US.UTF-8"
 LANG=en_US.UTF-8

apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
<!-- gnome-tweak-tool -->

5. 安装google输入法安装
```bash
$ apt-get install fcitx-googlepinyin
```

6. 创建用户
```bash
useradd -m -U hua
passwd hua
usermod -a sudo hua
```

7. 存储卡扩展分区 
- https://blog.csdn.net/richermen/article/details/48445721
- https://www.cnblogs.com/PhoenixMY/p/5259162.html

```bash
apt-get install triggerhappy lua5.1  alsa-utils 
wget http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20180406+1_all.deb
dpkg -i raspi-config_20180406+1_all.deb
raspi-config
```
在终端输入raspi-config，连按两次确定键，重启即可。 


8. kail+树莓派的分辨率
修改/新建 /root/config.txt文件
```
framebuffer_width=1980
framebuffer_height=1080
hdmi_group=2
hdmi_mode=82
hdmi_ignore_edid=0xa5000080
```


## axel 多线程下载 
sudo apt-get install axel

## VPN
```bash
sudo apt-get install network-manager-pptp network-manager-pptp-gnome
```
找到 /etc/NetworkManager/NetworkManager.conf
把最后一行的managed=false改为managed=true
注意在新建PPTP VPN时在高级属性里选择“使用点到点加密(MPPE)”

## VNC
<!-- 　　sudo apt-get install vnc4server -->
    apt install tightvncserver

- tightvncserver
- vncserver :1 - geometry 1280x1080-depth 24
> 太卡，由于分辨率太高的问题.


## nload 
> 流量分析工具
- tab --- 切换网卡
- 回车 --- 切换ip

## hackbar
> 常用工具包, SQL injection,XSS,加密等

## ftp
apt install filezilla

## shellter
捆绑木马,加壳

## pig 虚拟网卡，DHC耗竭

## ettercap 流量欺骗

