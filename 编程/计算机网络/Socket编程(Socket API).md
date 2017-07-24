# Socket编程(Socket API)
- 通信模型
	- 客户/服务器
- 标识通信端点(对外)
	- IP地址+端口号
- 操作系统/进程如何管理套接字(对内)
	- 套接字描述符
- 地址结构
	- sockaddr\_in 包含IP和端口号等。
- Socket API函数
	- WSAStartup
	- ……
	- WSACleanup
- Socket面向TCP/IP的服务类型
	- 面向TCP
		- SOCK\_STREAM
	- 面向UDP
		- SOCK\_DGRAM
	- 面向网络层
		- SOCK\_RAW
- 常用函数
	- startup
	- cleanup
	- socket(创建套接字)
	- closesocket（释放/关闭套接字）
	- bind(绑定套接字的本地IP地址和端口号)
	- listen(仅用于流套接字，TCP套接字坚挺模式)
	- connect(连接远端服务器)
	- accept(接收/提取一个连接请求TCP)
	- send、sendto(发送数据)
	- recv、recvfrom(接收数据)
	- setsockopt、getsockopt(设置/获取套接字选项参数)
- TCP客户端软件流程
	1. 确定服务器`IP地址`与`端口号`
	2. 创建套接字
	3. 分配本地端点地址(IP地址+端口号)
	4. 连接服务器(套接字)
	5. 遵循应用层协议进行通信
	6. 关闭/释放连接
- UDP客户端软件流程
	1. 确定服务器`IP地址`与`端口号`
	2. 创建套接字
	3. 分配本地端点地址(IP地址+端口号)
	4. 指定服务器端点地址，构造UDP数据报
	5. 遵循应用层协议进行通信
	6. 关闭/释放连接

