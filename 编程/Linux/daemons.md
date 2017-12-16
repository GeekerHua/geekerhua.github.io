# daemon 守护程序

## System V的init式管理
所有的启动脚本都放到/etc/init.d/下。

* 启动：/etc/init.d/daemon start
* 关闭：/etc/init.d/daemon stop
* 重启：/etc/init.d/daemon restart
* 状态：/etc/init.d/daemon status

### 执行等级分类
0-6共7个等级，各个执行等级的启动脚本是透过`/etc/rc.d/rc[0-6]/SXXdaemon`连结到`/etc/init.d/daemon` 。连结档名(SXXdaemon)的功能为： S为启动该服务，XX是数字，为启动的顺序。


查看服务于端口号对应
`cat /etc/services`

### daemon启动脚本与启动方式
daemon相关的文件放到哪里了？
* /etc/init.d/* : 启动脚本放置处，centos实际放到了/etc/rc.d/init.d/中
* /etc/sysconfig/* : 各服务的初始化环境设定档
* /etc/* : 各服务各自的设定档
* /var/lib/* : 各服务产生的资料库
* /var/run/* : 各服务的程序PID记录处

除了使用/etc/init.d/*的方式启动，还可以使用`service`的方式启动，service本质也是init.d下的服务。

### 设定开机自启服务
* 预设要启动： chkconfig daemon on
* 预设不要启动： chkconfig daemon off
* 查看预设启动状态： chkconfig --list daemon

### 建立自己的服务
```bash
#!/bin/bash
# chkconfig: 35 80 70
# description: this is description
echo 'Nothing'
```

```bash
chkconfig --add xxx
chkconfig --level 2345 xxx on
```

## systemd
### 设定档目录
* /usr/lib/systemd/system/ : 每个服务最主要的启动脚本设定,相当于/etc/init.d
* /run/systemd/system/ : 系统执行过程中产生的服务脚本，优先级高于上一个
* /etc/systemd/system/ : 类似/etc/rc.d/tc5.d/Sxx ，优先级最高
    * 该目录下会有很多连接，系统自动启动

### 使用systemctl指令管理

`systemctl [command] [unit]`

command | 解释
----- | -----
start | 立刻启动后面接的unit
stop | 立刻关闭后面接的unit
restart | 立刻关闭后启动后面接的unit，亦即执行stop 再start 的意思
reload | 不关闭后面接的unit 的情况下，重新载入设定档，让设定生效
enable | 设定下次开机时，后面接的unit 会被启动
disable | 设定下次开机时，后面接的unit 不会被启动
status | 目前后面接的这个unit 的状态，会列出有没有正在执行、开机预设执行否、登录等资讯等！
is-active | 目前有没有正在运作中
is-enabled | 开机时有没有预设要启用这个unit

#### systemctl设定档相关目录
* /usr/lib/systemd/system/xxx.service : 官方预设设定档
* /etc/systemd/system/xxx.service.d/custom.conf : 在/etc/system底下建立与设定档相同档名的目录，但是要加上.d的副档名。然后在该目录下建立设定档即可。设定档最好附档名取名为.conf较佳！在这个目录下的档案会『累加其他设定』进入/usr/lib/systemd/system/vsftpd.service内喔！
* /etc/systemd/system/ vsftpd.service.wants /*：此目录内的档案为连结档，设定相依服务的连结。意思是启动了vsftpd.service之后，最好再加上这目录底下建议的服务。
* /etc/systemd/system/ vsftpd.service.requires /*：此目录内的档案为连结档，设定相依服务的连结。意思是在启动vsftpd.service之前，需要事先启动哪些服务的意思。
