# 仅执行一次的任务`at`
at用来执行一次性的任务,执行at需要`atd`的支持。

## at一次性工作排程(定时任务)
使用at可以在指定时间执行一次任务。
```bash
$ at now + 2 minutes  <== 2分钟后执行
at> xxxxx
at> <EOT>  <== ctrl + d 结束输入

$ at -l <== 列出所有的任务, 相当去 atq 
$ at -c 4 <== 列出4号任务的详情
$ at -d <== 结束一个任务, 相当于 atrm
```

## atd的启动
```bash
$ /etc/init.d/atd start  // atd启动
$ chkconfig atd on       // atd开机自启

$ systemctl status atd // ubuntu命令
```

## at的权限
两个稳点决定用户权限
- /etc/at.allow   // 允许的用户，先查找这个文件，找不到再查找第二个文件。
- /etc/at.deny    // 禁止的用户
创建的命令会记录到`/var/spool/at/`中

## batch空闲时执行
使用batch，可以在指定时间且CPU负载低于0.8时自动执行。
> batch空闲时执行


# 循环执行的定时任务cron
crontab可以进行例行性的任务执行，需要`crond`这个服务支持。

## 权限
- /etc/cron.allow   // 允许的用户，先查找这个文件，找不到再查找第二个文件。
- /etc/cron.deny    // 禁止的用户
> 创建的命令会记录到`/var/spool/cron/`中
> cron 运行的每一项工作都会被纪录到 /var/log/cron 这个登录档中

## 命令
```bash
$ crontab [-u username] [-l|-e|-r]
选项与参数：
-u  ：只有 root 才能进行这个任务，亦即帮其他使用者创建/移除 crontab 工作排程；
-e  ：编辑 crontab 的工作内容
-l  ：查阅 crontab 的工作内容
-r  ：移除所有的 crontab 的工作内容，若仅要移除一项，请用 -e 去编辑。
```
> m h  dom mon dow   command 每一行都是这6个字段


# anacron(#todo 待完善)