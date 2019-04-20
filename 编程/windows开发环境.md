1、在hosts文件中配置git  域名

     首先  根据  http://ju.outofmemory.cn/entry/351783  贴子，找到Github 网站 最新的ip 及相应的DNS配置信息，如下：

             151.101.113.194 github.global.ssl.fastly.net 
             192.30.253.112 github.com 

    PS ：上面提到的贴子里说的要将DNS信息配置到本地的hosts文件（C:\Windows\System32\drivers\etc）中，但是依旧很慢。继续看下面

2、将1里获取的DNS 信息配置到Git 安装目录下的hosts文件中
