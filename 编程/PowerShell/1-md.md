# 1.交互界面
## 1.1 运行程序、脚本和已有的工具

1. 可执行类型的文件，可以不用输入扩展名：Program.exe arguments
2. 运行命令中包含空格的命令使用单引号(')将命令括起来。并在前边加上(&)与符号，这在powershell中称为调用操作：& 'C:\Program Files\Program\Program.exe' arguments
3. 运行当前目录命令，文件前加(.\)
4. 在当前目录下运行命令命中包含空格的命令，同时加上(&)和(.\)：& '.\Program.exe' arguments

## 1.3 自定义shell、配置文件与提示符
相当于Bash的.bashrc定制Bash的一些交互界面

## 1.4 查找实现指令任务的命令
cmdlets指令统一使用`动词-名词的`模式。动词取自一个标准的动词集合。
> 当想执行一条命令，却不知道用什么命令来执行时使用`Get-Command`命令。

`Get-Command`后接的指令
命令 | 功能
---- | ----
CommandName | 获取指令的概要信息
`*text*` | 搜索包括"text"的所有命令
-Verb Get | 搜索所有使用Get动词的命令
-Noun Service | 搜索所有与服务有关的命令(指定名词)


## 1.5 获取命令帮助
`Get_Help`后接的指令
命令 | 功能
CommandName 或 CommandName -? | 获取概要帮助信息
CommandName-Detailed | 帮助信息详情
CommandName -Full | 详细的帮助信息
CommandName -Examples | 例子信息

----
## 常用cmdlets
* Get-Command
* Get-Help
* Get-Member

## 1.7 Powershell之外调用Powershell脚本
Powershell "& 'full path to script' arguments"

## 常用命令

命令 | 功能 | 说明
--- | ---- | ----
Get_date | 获取系统日期和时间
$lastExitcode | 检测最后命令状态码 | 数字型
$? | 最后命令是否成功 | 布尔型
Get-History(history) | 获取控制台输入历史
Start-Transcript [path] | 记录日志全文到path(可选)
Sopt-Transcript | 停止记录日志
Format-List | 将输入以列表方式显示出来 | 三个格式化命令之一
Format-Table | 将输入以表格方式显示出来 | 三个格式化命令之一
Format-Wide |  | 三个格式化命令之一
