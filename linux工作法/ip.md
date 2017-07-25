# IP绑定

## 第一种方式静态修改.
 
进入 /etc/network/ 目录下.修改interfaces文件.
```bash
# The primary network interface
auto eth0
iface eth0 inet static
address 110.25.*.*
netmask 255.255.255.0
gateway 110.25.*.1
#auto eth0:0
#iface eth0:0 inet static
#address 110.25.*.*
#netmask 255.255.255.0
```
注释部分是自己添加的.eth0:0类似于数组下标.接下来想绑定多个就可以以此类推eth0:1,eth0:2,eth0:3........
 
## 第二种方式是动态修改.

这里直接使用 ifconfig 命令
```bash
$ sudo ifconfig eth0:0 110.25.*.* broadcast 110.25.*.255 netmask 255.255.255.0 
```

第一种方式在你修改重启之后不会失效.这种方式稍微操作不当,则会造成远程无法连接。 第二种方式虽然只对当前生效,重启之后就会失效.但是不会因为操作不当给自己造成的不便。

