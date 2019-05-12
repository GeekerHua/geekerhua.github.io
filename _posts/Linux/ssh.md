---
title: SSH详解
date: 2017-08-01 16:11:54
tags: [Linux]
categories: [Linux满汉全席]
---

## 功效

ssh是一项基于非对称加密的传输协议， 通过ssh能够安全方便的远程连接服务器， 进行操作。 ssh默认使用22端口， 可以指定端口。

## 武吃

ssh连接默认每次连接需要输入密码， 但可以通过公钥认证进行免密登录。

### 1. 安装

很多系统自带有， 如果没有， 使用以下命令安装

```bash
# Debain系
$: sudo apt-get install openssh-server
# Redhat系
$: sudo yum install openssh-server
```

### 2. 登录

```bash
$: ssh user@host
```

然后输入用户密码， 即可登录成功。

> 如需指定端口， 可使用 `-p` 参数。

### 3. 免密登录（公钥登录）设置

> 免密登录的核心在于将Client的 `id_rsa.pub` 公钥添加到Server的 `~/.ssh/authorized_keys` 文件中， 且需保证 `.ssh` 目录权限700， `.ssh/authorized_keys` 文件权限600；

步骤如下：

#### 3.1 Server端：

开启sshd服务， 不同平台甚至同平台不同版本的启动方式都有所不同。 详细不同平台版本服务[Daemons](xxxxx)

```bash
systemctl satart sshd
```

默认情况下不需要修改sshd配置（/etc/ssh/sshd_config)， 但有时会涉及到最常用的三个修改：

| 修改项             | 配置项                      |
|-------------------|----------------------------|
| 是否允许root用户登录 | PermitRootLogin yes        |
| 是否允许使用密码登录 | PasswordAuthentication yes |
| 是否允许使用公钥登录 | PubkeyAuthentication yes   |

#### 3.2 Client端：

```bash
$: # 生成ssh key
$: ssh-keygen -t rsa
$: # 拷贝ssh pub_key到远程主机~/.ssh/authorized_keys中， ssh的时候就不需要输入密码了
$: ssh-copy-id remoteuser@remoteserver
$: # ssh的时候不会提示是否保存pub_key
$: ssh-keyscan remote_servers >> ~/.ssh/known_hosts
```

## 文吃

ssh使用非对称加密对传输进行加密， 因此在传输开始前需要建立加密通道。 ssh的设置文件位于 `/etc/ssh/sshd_config`

### 1. ssh连接流程

1. Client向远端Server发起ssh请求
2. Server端收到ssh请求， 将pub_key发送回Client端
3. Client收到服务端的pub_key后在当前Client用户的 `~/.ssh/known_hosts` 中寻找目标主机的信息， 如果没有， 则会将目标主机的公钥添加进去， 以便日后再次登录进行比较， 防止被人恶意篡改。
4. Client端生成一对公私钥， 并将公钥发送给Server端， 是的， 如果没有设置免密登录每次连接都会生成一对公私钥。 而之所以能够免密登录， 核心就在于每次ssh都使用同一套公私钥， 而服务端是会记录客户端的公钥的， 因此， 才会不需要输入密码。
5. Server端收到Client的公钥， 开始验证登录用户信息， 是否存在， 是否需要密码才能登录等。 然后使用Server的私钥进行加密发送给Client, 至此加密连接建立。
6. Client收到Server的输入密码请求， 使用Server的公钥进行解密， 然后使用Client的公钥对密码加密并发送。
7. Server端收到Client的加密信息， 使用Client的公钥进行解密， 并对密码进行比对， 成功则完成登录。

从上述过程可知， 在用户信息（包括密码）传输之前， 加密通道已经建立完成了。 因此之后的操作都是安全的。 唯一可能出现安全问题的是传输公钥的过程。 但即使被恶意篡改了， 由于Client和Server使用的并不是一套加密系统， 也只能Client连接伪Server而不能反过来让伪Server连接Client. 因此ssh连接还是非常安全可靠的。

### 2. 三套加密系统

#### 2.1 Server端加密：

在Server端sshd服务启动时， 会自动生成一对公钥和私钥， 默认保存在 `/etc/ssh/` 下， ssh支持多种加密协议， 支持rsa, dsa, ed25519, ecdsa四种加密方式， 该路径可以在config中进行设置。 当有客户端进行ssh连接该Server时， 就是使用这里的公钥和私钥加解密的。

#### 2.2 Client密码登录：

在未设置免密登录的情况下每次ssh连接都需要输入密码。 但这都是在加密通道建立之后。

#### 2.3 免密登录：

每个用户的 `~/.ssh` 文件夹下都会有连个文件， 一个是 `known_hosts` ， 记录曾经连接过的主机的公钥。 另一个是 `authorized_keys` , 用来记录授权免密登录的公钥， 使用该公钥对应私钥加密连接的Client都可以实现免密登录。 因此， 只要将Client的 `id_rsa.pub` 公钥内容添加到Server的authorized_keys中即可。 ssh有个快捷方法。 `ssh-copy-id remoteuser@remoteserver` 。

-----

## 甜品

### 1. SCP

> `cp` 是Linux下的拷贝命令， 只能进行本地拷贝操作， 想要进行远程拷贝， 在两台主机间传输文件就需要使用 `scp` 命令了， scp默认会对传输进行ssl加密， 而且命令相当简单。 `scp` 是基于 `ssh` 的命令， 因此， 使用前需要保证能够使用 `ssh` 进行通信。

 `scp` 的命令简单来说就是 `scp`  `src`  `des` ， `scp` 后接源文件路径， 然后接目标路径， 如果需要拷贝文件夹， 需要添加 `-r` 参数。 文件路径的表示为， 本地直接写相对或绝对路径， 远端为 `user@host:path` 。
示例如下：

- scp [-r] `user` @ `host` : `targetPath`  `localPath` # 远端targetPath拷贝到本地localPath
- scp [-r] `localPath`  `user` @ `host` : `targetPath` # 本地localPath拷贝到远端targetPath.

> 对于mac用户， 系统进行了图形化处理， 若想作为Server, 在共享设置中， 开启远程登录功能即可。 作为Client, 使用方法相同。

