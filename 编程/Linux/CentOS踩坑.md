# yum源安装失败

```bash
One of the configured repositories failed (未知),
 and yum doesn't have enough cached data to continue. At this point the only
 safe thing yum can do is fail. There are a few ways to work "fix" this:
 ………………
 ```
1. 将`/etc/yum.repos.d/epel.repo`中的`mirrorlist`改为`baseurl`

> vi全局替换`:%s/mirrorlist/baseurl/g`

2. `/etc/resolv.conf`文件中增加`nameserver 8.8.8.8`

6214680013050263