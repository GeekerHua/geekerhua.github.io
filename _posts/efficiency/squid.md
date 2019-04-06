---
title: squid+stunnel 科学上网
date: 2017-08-24 14:12:18
tags: [vpn, 科学上网]
categories: 效率
---

# squid+stunnel 合理的进行科学上网


科学上网的方法有多重，有很多第三方提供的免费方案，这些方案优缺点暂时不予讨论。实际工作生活中还是会有需要自己搭建的情况，这次介绍的是使用squid进行搭建。

## 总结

### 优点

- 搭建简单方便，能够进行更好的权限控制。
- squid具有缓存功能，必要的时候可以提高访问速度。
- 使用stunnel能够对通信进行加密，更加安全。
- squid可以实现正向代理，透明代理，反向代理，能够实现多种需求。
- 将squid搭建在网关即可实现透明代理，下边的所以机器都免配置使用，方便快捷。

### 缺点

- 需要使用stunnel进行通讯加密，client和server都不要启动stunnel，不是用stunnel进行加密，访问被墙的网站ip会被秒封。
- 每个client都需要开启stunnel，就像使用shadowsocks一样。

### 大概流程

1. server端搭建squid代理服务
2. 生成TLS/SSL证书
3. server端搭建stunnel进行加密
4. client端搭建stunnel进行认证
5. client使用代理

## server端搭建

### 搭建squid服务

1. 安装squid服务

   > centos: yum install -y squid
   > ubuntu: apt-get install -y squid

2. 修改squid配置(/etc/squid/squid.conf)， **目前没有加权限控制**

    ```ini
    acl SSL_ports port 443
    acl CONNECT method CONNECT
    http_access deny !Safe_ports
    http_access deny CONNECT !SSL_ports
    http_access allow localhost manager
    http_access deny manager
    http_access allow localnet
    http_access allow localhost
    # http_access allow deny	# 注释掉这一行
    http_access allow all	# 这行最重要，开放所有访问
    http_port 3128	# 监听3128端口，使用312端口实现代理
    cache_dir ufs /var/spool/squid 100 16 256
    coredump_dir /var/spool/squid
    refresh_pattern ^ftp:		1440	20%	10080
    refresh_pattern ^gopher:	1440	0%	1440
    refresh_pattern -i (/cgi-bin/|\?) 0	0%	0
    refresh_pattern .		0	20%	4320
    dns_nameservers 8.8.8.8	# dns解析服务器
    cache_mem 1024 MB	# 缓存大小
    http_reply_access allow all	# 允许所有请求返回
    ```

3.  启动服务

    ```shel
    # squid -z  # 进行初始化操作
    # service squid start # 启动squid代理服务
    ```


4. 防火墙开启3128端口，基于云计算的虚拟机直接在控制面板设置即可。

至此，基于squid的代理服务器已经搭建好了，在需要使用这个代理的client上设置该主机的公网ip，及刚才指定的端口`3128`即可使用代理访问互联网。

但是，当你使用chrome进行调试的时候就会发现，第一个网页能够打开，但该网页的个别图片请求失败了。刷新下，发现彻底打不开了，提示连接被拒绝。这是因为没有加密，GFW探测到我们的请求返回的是被禁止的内容，就会把访问中断，并把我们的代理ip暂时列入黑名单，因此接下来的所有请求都会失败，这个黑名单时间大概也就几分钟。为了达到数据加密，防止辛辛苦苦搭建的服务被墙，我们接下来使用stunnel服务进行连接加密。

### 搭建stunnel服务

1. 安装stunnel服务

   > centos: yum install -y squid
   >
   > ubuntu: apt-get install -y squid
   >
   > mac: brew install squid

2. 生成TLS/SSL证书

   > openssl req -new -x509 -days 3650 -nodes -out stunnel.pem -keyout stunnel.pem

3. 将证书`stunnel.pem` copy到`/etc/stunnel/`目录下

4. 修改stunnel配置(/etc/stunnle/stunnle.conf)

5. 防火墙开启3129端口，关闭3128端口。基于云计算的虚拟机直接在控制面板设置即可。

    ```ini
    ; 设置工作目录
    ;chroot = /var/run/stunnel/
    ; 设置stunnel的pid文件路径（在chroot下）
    pid = /stunnel.pid
    ; 设置stunnel工作的用户（组）
    setuid = root
    setgid = root
    
    ; 开启日志等级：emerg (0), alert (1), crit (2), err (3), warning (4), notice (5), info (6), or debug (7)
    ; 默认为5
    debug = 7
    ; 日志文件路径（我的server的版本有个bug，这个文件也被放在chroot路径下了，client的版本则是独立的=。=#）
    output = /stunnel.log
    
    ; 证书文件，就是在本文2.2中用openssl生成的自签名证书（server端必须设置这两项）
    cert = /etc/stunnel/stunnel.pem
    ; 私钥文件
    key = /etc/stunnel/stunnel.pem
    
    ; 设置stunnel服务，可以设置多个服务，监听同的端口，并发给不同的server。
    ; 自定义服务名squid-proxy
    [squid-proxy]
    ; 服务监听的端口，client要连接这个端口与server通信
    accept = 3129
    ; 服务要连接的端口，连接到squid的3128端口，将数据发给squid
    connect = 3128
    
    ; **************************************************************************
    ; * 下面这些配置我都注释掉了，但也需要了解下 *
    ; **************************************************************************
    
    ; 设置是否对传输数据进行压缩，默认不开启。
    ; 这是跟openssl相关的，如果你的openssl没有zlib，开启这个设置会导致启动失败（failed to initialize compression method）
    ;compression = zlib
    
    ; 设置ssl版本,这个也是跟安装的openssl有关的
    ;sslVersion = TLSv1
    
    ; Authentication stuff needs to be configured to prevent MITM attacks
    ; It is important to understand that this option was solely designed for access control and not for authorization
    ; It is not enabled by default!
    ; 下面这些配置用来定义是否信任对方发过来的证书。就好比浏览器访问https的时候，浏览器默认会信任那些由权威CA机构签发的证书，
    ; 对于那些自签名证书，浏览器就会弹出对话框提醒用户这个证书可能不安全，是否要信任该证书。
    ; 这是有效防止中间人攻击的手段
    ; verify 等级2表示需要验证对方发过来的证书（默认0，不需要验证，都信任）
    ; 因为这个配置是server端的，我们不需要理会client的证书（client也不会没事发证书过来啦）
    ;verify = 2
    ; CAfile 表示受信的证书文件，即如果对方发过来的证书在这个CAfile里，那么就是受信任的证书；否则不信任该证书，断开连接。
    ;CAfile = /etc/stunnel/stunnel-client.pem
    ```



## client端

1. 通server端一样安装stunnel服务。
2. 修改stunnel配置文件，将代理的公网ip写入下列配置文件的 `connect`项中。
3. 将在server中生成的证书文件copy到指定目录如`/etc/stunnel/`，并将路径写到配置中的`CAfile`。

    ```ini
    ; stunnel工作目录
    ;chroot = /var/run/stunnel/
    ; stunnel工作的用户组
    ;setuid = root
    ;setgid = root
    ; stunnel工作时候的pid
    pid = /stunnel.pid
    
    ; 日志等级
    debug = 7
    ; 日志文件
    output = /var/log/stunnel/stunnel.log
    
    ; 表示以client模式启动stunnel，默认client = no，即server模式
    client = yes
    
    ; 定义一个服务
    [squid-proxy]
    ; 监听3128端口，那么用户浏览器的代理设置就是 stunnel-client-ip:3128
    accept = 3128
    ; 要连接到的stunnel server的ip与端口
    connect = xx.xx.xx.xx:3129
    
    ; 需要验证对方发过来的证书
    verify = 2
    ; 用来进行证书验证的文件（里面有stunnel server的证书）
    CAfile = /etc/stunnel/stunnel-server.pem
    
    ; 客户端不需要传递自己的证书，所以注释掉
    ;cert = /etc/stunnel/stunnel.pem

    ```



## 使用代理

由于没有使用权限认证，只是使用了证书认证，因此只需要在代理设置中使用`127.0.0.1`端口`3128`进行代理即可，推荐还是增加squid权限认证比较安全。

## 参考链接

> [squid + stunnel >> 跨越长城，科学上网！](https://www.hawu.me/operation/886>)
