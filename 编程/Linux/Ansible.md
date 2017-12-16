---
title: Ansible
date: 2017-10-26 10:11:32
tags: 运维
categories: Linux
---
# 介绍
Ansible是使用python进行编写，通过ssh远程批量部署主机的服务。服务端不需要安装任何软件，只需要客户端能够ssh连接客户端即可。

## Host Inventory 配置文件：
默认的文件是： /etc/ansible/hosts

### 常见的Hosts文件
```yaml
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```

## Ansible的Module
### 命令行中使用
> -m后面接调用module的名字
  -a后面接调用module的参数

```bash
$ #使用module copy拷贝管理员节点文件/etc/hosts到所有远程主机/tmp/hosts
$ ansible all -m copy -a "src=/etc/hosts dest=/tmp/hosts"
$ #使用module yum在远程主机web上安装httpd包
$ ansible web -m yum -a "name=httpd state=present"
```

### playbook中使用
通过命令ansible-doc也可以查看module的用法

**常用Module列表**

Module | 功能 | 常用命令
---- | ----- | -----
ping | 连接成功返回pong
debug | 相当于echo，用于调试 | msg <br>var
file | 设置文件(夹)属性 | path <br>owner <br>group <br>mode <br>state(touch/directory/link) <br>src <br>dest
copy | 本地文件拷贝到远端 | src <br>dest <br>owner <br>group <br>mode <br>backup <br>validate
template | 从本地拷贝文件到远端，并进行变量替换 | 同copy模块
user | 管理用于账户 | name <br>comment <br>uid <br>group <br>shell <br>groups <br>append <br>state <br> remove <br>……
yum | red hat系包管理工具 | name <br>state <br>enablerepo
service | 管理服务 | name <br>state <br>enable <br>args
firewalld | 管理防火墙中的服务和端口 | service <br>permanent <br>state <br>zone <br>port
shell | 执行shell命令,支持`$HOME<>|;&` | args(chdir、creates、executable)
command | 执行命令，不支持`$HOME<>|;&` | 几乎同shell


执行结果，如果相同，不再执行，返回ok，如果不同，返回状态changed。


# 进阶
## ansible的配置
* 主机清单文件”inventory”，
* extra module放置路径”library” ，
* 远程主机的临时文件位置” remote_tmp” ，
* 管理节点上临时文件的位置”local_tmp”
* 连接端口号”accelerate_port”
* 超时时间accelerate_timeout = 30

### ansible配置文件优先级(1.5及以上版本)
* ANSIBLE_CONFIG (an environment variable)
* ansible.cfg (in the current directory)
* .ansible.cfg (in the home directory)
* /etc/ansible/ansible.cfg

## Host inventory(主机清单)
1. 通过修改主机目录的配置文件
/etc/ansible/ansible.cfg
```conf
inventory = /etc/ansible/hosts
```

2. 命令行中传递主机目录配置文件
```bash
$ ansible-playbook -i hosts site.yml
$ ansible-playbook -inventory-file hosts site.yml
```

### 远程主机分组
 ```conf
 [a:children]
 ```
 a可以包含子组

### 远程主机连接参数和变量
1. 参数，写在主机名(ip)之后
* ansible_connection
* ansible_user
* http_port
* maxRequestsPerChild
* .....

2. 变量，为一个组指定变量
```conf
[atlanta]
host1
host2

[atlanta:vars]
ntp_server=ntp.atlanta.example.com
proxy=proxy.atlanta.example.com
```

### 按目录结构存储变量
涉及到两个目录，`group_vars`,`host_vars`，可以放到hosts同级目录。连个目录下放置的文件(.yml/.yaml/.json)或者文件夹名代表hosts组名。
也可以放到playbook目录下，拥有更高的优先级。

## Ansible的脚本

### 基本语法
```bash
# 执行
$ ansible-playbook deploy.yml
# 查看输出的细节
$ ansible-playbook playbook.yml  --verbose
# 查看该脚本影响哪些hosts
$ ansible-playbook playbook.yml --list-hosts
# 并行执行脚本
$ ansible-playbook playbook.yml -f 10
```





### 变量


### playbook中逻辑控制


### 重用playbook

## 更多ansible模块
sysbench --test=cpu --cpu-max-prime=10000 --num-threads=1 run
sysbench --test=cpu --cpu-max-prime=10000 --num-threads=4 run


sysbench --test=memory --memory-block-size=8K --memory-total-size=500G   --memory-oper=read --memory-access-mode=rnd run
sysbench --test=memory --memory-block-size=128K --memory-total-size=5T   --memory-oper=read --memory-access-mode=rnd run
sysbench --test=memory --memory-block-size=1M --memory-total-size=40T   --memory-oper=read --memory-access-mode=rnd run
sysbench --test=memory --memory-block-size=8K --memory-total-size=500G   --memory-oper=write --memory-access-mode=rnd run
sysbench --test=memory --memory-block-size=128K --memory-total-size=5T   --memory-oper=write --memory-access-mode=rnd run
sysbench --test=memory --memory-block-size=1M --memory-total-size=40T   --memory-oper=write --memory-access-mode=rnd run


