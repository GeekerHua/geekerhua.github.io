# shell编程
# 基础
## 命令的下达
> 会用`\`+ `Enter`来进行换行操作，会继续输入，而不是截止这行

## alias 
> - 直接输入alias 会查看所有设置好的alias
> - `alias lm='ls -al'`能够设置别名

## 基础命令
###  open
> 用来打开文件、文件夹，使用方式在`open`后添加后缀

```bash
$ open -a finder    #打开finder
$ open -n -a qq     # 打开新的qq程序
$ open 'name'   # 打开文件
```
### LANG
>用来显示和设置全局语言的

```bash
$ echo $LANG    # 显示目前所支持的语言
$ echo LANG=en_US   # 修改语言为英文
# 汉语为 
zh_CN.UTF-8
```
### date
>用来显示当前时间

```bash
$ ~ date +%Y/%m/%d
2016/05/26
```
### cal 
>日历
```bash
$ cal 10 2019   # 显示2019年10的月历
```

### bc
> 最好用的计算器

### 重要热键
- Tab
    - 补全
 [Ctrl]-c
    - 停下程序
## man page 与 info page