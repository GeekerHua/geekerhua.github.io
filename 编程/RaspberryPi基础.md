# RaspberryPi基础
# 树莓派实用命令
## 修改root密码(忘记root密码)
> sudo passwd `root`
> $ 输入 密码

## 支持中文处理
> 树莓派默认不支持中文，初次安装需要设置中文支持，否则会显示乱码
- XWindow界面中文支持

```bash
$ sudo apt-get install ttf-wqy-zenhei

```
## 中文输入法
> 输入法，一款是SCIM，令一款是Rime(鼠须管)
- SCIM安装

```bash
$ sudo apt-get install scim-pinyin
```

- 接着运行`sudo raspi-config`
- 选择`change_locale`，在Default locale for the system environment:中选择zh_CN.UTF-8。然后重启机器，就发现整个环境变成中文的了。

##  设置WIFI
> 使用终端直接添加WIFI账号和密码，自动连接WIFI。

  参考博客
> - [树莓派3命令行配置wifi无线连接和蓝牙连接](https://www.embbnux.com/2016/04/10/raspberry_pi_3_wifi_and_bluetooth_setting_on_console/)
> - [让你的树莓派连上WiFi](http://ju.outofmemory.cn/entry/106824)

### 搜索WIFI
`iwlist scan` 

### 添加WIFI信息

- `vim /etc/network/interfaces`
- 添加WIFI信息

```bash
allow-hotplug wlan0
iface wlan0 inet manual
wpa-essid “无线网络名称”
wpa-psk “密码”
```

- `reboot`
###  多个WIFI的配置

```bash
# 编辑wifi文件
sudo vim /etc/wpa_supplicant/wpa_supplicant.conf
# 在该文件最后添加下面的话
network={
  ssid="WIFINAME"
  psk="password"
}
# 引号部分分别为wifi的名字和密码
# 保存文件后几秒钟应该就会自动连接到该wifi
# 查看是否连接成功
ifconfig wlan0
```

### 硬盘的挂载
－手动挂在和卸载
- 挂载硬盘与取消挂载硬盘。
