## 功能
Linux与Windows互通数据， 分享打印机。

SAMBA的两个服务
* nmbd：这个daemon用来管理工作群组，NetBIOS name解析，UDP接口137、138，负责名称解析任务；
* smbd：这个daemon用来管理SAMBA主机分享的目录、文件、打印机等。开放端口为139或445。

## SAMBA服务端
### 所需要的软件
软件 | 说明
--- | ----
samba | 这个软体主要提供了SMB伺服器所需的各项服务程式(smbd及nmbd)、的文件档、以及其他与SAMBA相关的logrotate设定档及开机预设选项档案等；
samba-client | 这个软体则提供了当Linux做为SAMBA Client端时，所需要的工具指令，例如挂载SAMBA档案格式的mount.cifs、取得类似网芳相关树状图的smbtree等等；
samba-common | 这个软体提供的则是伺服器与用户端都会使用到的资料，包括SAMBA的主要设定档(smb.conf)、语法检验指令(testparm)等等；

### 所需要的设定档
应用 | 说明
---- | ----
/etc/samba/smb.conf | 这是Samba的主要设定档，基本上，咱们的Samba就仅有这个设定档而已，且这个设定档本身就是很详细的说明文件了，请用vim去查阅它吧！主要的设定项目分为伺服器的相关设定(global)，如工作群组、NetBIOS名称与密码等级等，以及分享的目录等相关设定，如实际目录、分享资源名称与权限等等两大部分。
/etc/samba/lmhosts | 早期的NetBIOS name需额外设定，因此需要这个lmhosts的NetBIOS name对应的IP档。事实上它有点像是/etc/hosts的功能！只不过这个lmhosts对应的主机名称是NetBIOS name喔！不要跟/etc/hosts搞混了！目前Samba预设会去使用你的本机名称(hostname)作为你的NetBIOS name，因此这个档案不设定也无所谓。
/etc/sysconfig/samba | 提供启动smbd, nmbd时，你还想要加入的相关服务参数。
/etc/samba/smbusers | 由于Windows与Linux在管理员与访客的帐号名称不一致，例如： administrator (windows)及root(linux)，为了对应这两者之间的帐号关系，可使用这个档案来设定
var/lib/samba/private/{passdb.tdb,secrets.tdb} | 管理Samba的使用者帐号/密码时，会用到的资料库档案；
/usr/share/doc/samba-<版本> | 这个目录包含了SAMBA的所有相关的技术手册喔！也就是说，当你安装好了SAMBA之后，你的系统里面就已经含有相当丰富而完整的SAMBA使用手册了！值得高兴吧！^_^，所以，赶紧自行参考喔！

### 常用指令档
指令 | 说明
/usr/sbin/{smbd,nmbd} | 伺服器功能，就是最重要的权限管理(smbd)以及NetBIOS name查询(nmbd)两个重要的服务程式；
/usr/bin/{tdbdump,tdbtool} | 伺服器功能，在Samba 3.0以后的版本中，使用者的帐号与密码参数已经转为使用资料库了！Samba使用的资料库名称为TDB (Trivial DataBase)。既然是使用资料库，当然要使用资料库的控制指令来处理啰。tdbdump可以察看资料库的内容，tdbtool则可以进入资料库操作介面直接手动修改帐密参数。不过，你得要安装tdb-tools这个软体才行；
/usr/bin/smbstatus | 伺服器功能，可以列出目前Samba的连线状况，包括每一条Samba连线的PID,分享的资源，使用的用户来源等等，让你轻松管理Samba啦；
/usr/bin/{smbpasswd,pdbedit} | 伺服器功能，在管理Samba的使用者帐号密码时，早期是使用smbpasswd这个指令，不过因为后来使用TDB资料库了，因此建议使用新的pdbedit指令来管理用户资料；
/usr/bin/testparm | 伺服器功能，这个指令主要在检验设定档smb.conf的语法正确与否，当你编辑过smb.conf时，请务必使用这个指令来检查一次，避免因为打字错误引起的困扰啊！
/sbin/mount.cifs | 用户端功能，在Windows上面我们可以设定『网路磁碟机』来连接到自己的主机上面。在Linux上面，我们则是透过mount (mount.cifs)来将远端主机分享的档案与目录挂载到自己的Linux主机上面哪！
/usr/bin/smbclient | 用户端功能，当你的Linux主机想要藉由『网路上的芳邻』的功能来查看别台电脑所分享出来的目录与装置时，就可以使用smbclient来查看啦！这个指令也可以使用在自己的SAMBA主机上面，用来查看是否设定成功哩！
/usr/bin/nmblookup | 用户端功能，有点类似nslookup啦！重点在查出NetBIOS name就是了。
/usr/bin/smbtree | 用户端功能，这玩意就有点像Windows系统的网路上的芳邻显示的结果，可以显示类似『靠近我的电脑』之类的资料，能够查到工作群组与电脑名称的树状目录分布图！

### smb.conf设置
1. 伺服器整体设定方面：在smb.conf当中设定好工作群组、NetBIOS主机名、密码使用状态(无密码分享或本机密码)等等；
2. 规划准备分享的目录参数：在smb.conf内设定好预计要分享的目录或装置以及可供使用的帐号资料；
3. 建立所需要的档案系统：根据步骤2的设定，在Linux档案系统当中建立好分享出去的档案或装置，以及相关的权限参数；
4. 建立可用Samba的帐号：根据步骤2的设定，建立所需的Linux实体帐号，再以pdbedit建立使用Samba的密码；
5. 启动服务：启动Samba的smbd, nmbd服务，开始运转哩！


## SAMBA用户端



## PDC( Primary Domain Controller, PDC)服务器