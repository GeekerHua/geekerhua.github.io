## 常用设置文件

* /etc/httpd/conf/httpd.conf (主要设定档)
* /etc/httpd/conf.d/*.conf (很多的额外参数档，副档名是.conf)
* /usr/lib64/httpd/modules/, /etc/httpd/modules/ Apache支持的外挂模组
* /var/www/html/ Apache首页所在目录
* /var/www/error/ 服务器设定错误
* /var/www/icons/ Apache预留的小图标
* /var/www/cgi-bin/ 预留给执行的CGI程序放置的目录
* /var/log/httpd/ 日志
* /usr/sbin/apachectl Apache主要执行文件
* /usr/sbin/httpd Apache二进制程序
* /usr/bin/htpasswd (Apache密码保护)

MySQL
* /etc/my.cnf MySQL设定档
* /var/lib/mysql/ MySQL资料库位置

PHP
* /etc/httpd/conf.d/php.conf php设定档
* /etc/php.ini 主要php设定档
* /usr/lib64/httpd/modules/libphp5.so PHP这个软体提供给Apache使用的模组！
* /etc/php.d/mysql.ini, /usr/lib64/php/modules/mysql.so php是否支持MySQL界面，由php-mysql提供
* /usr/bin/phpize, /usr/include/php/ PHP加速器预留，由php-devel提供