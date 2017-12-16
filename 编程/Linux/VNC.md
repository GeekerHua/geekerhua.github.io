# ssh
默认情况下，ssh连接需要输入密码，这种情况下，加密连接如下。
1. 服务端启动sshd，并随机生成一对公私钥，默认放置于/etc/ssh/ssh_host_*;
2. 客户端请求连接服务端;
3. 然后将服务端启动时生成的公钥传(明文)给客户端;
4. 客户端收到服务端的公钥后，将其存入`~/.ssh/known_hosts`中，如果以前有，则比对是否相同;
5. 客户端回传用户的公钥资料到服务端。
6. 连接成功，开始双向加密;
7. 要求客户端输入密码来连接服务端。

## 涉及到的文件
文件 | 说明
---- | ----
~/.ssh/known_hosts | 远端的公钥，每个一行，格式: IP publick_key
~/.ssh/id_rsa | 本机私钥
~/.ssh/id_rsa.pub | 本机公钥
~/.ssh/authorized_keys | 免密登录客户端的公钥存放文件

## 服务端
/etc/init.d/sshd restart

## 客户端
### 常用指令

ssh-copy-id "${User}"@"${IP}"
ssh-keyscan ${IP} >> ~/.ssh/known_hosts

ssh -f student@127.0.0.1 find / &> ~/find1. log

## sftp

## scp
两个常用参数 -p:保留原本档案的权限。-r:复制文件夹

```bash
scp [-r] file user@ip:file
scp [-r] user@ip:file file
```
