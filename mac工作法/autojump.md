> 经常在终端进行操作的时候，路径的频繁切换是一件很麻烦的事情。使用autojump能够快速的在经常使用的路径中切换，省了不少麻烦。

> [参考文章](http://www.jianshu.com/p/23aeb7c4d89b)

## 安装
```bash
$ brew install autojump
```

```bash
$ echo '[ -f /usr/local/etc/profile.d/autojump.sh  ] && . /usr/local/etc/profile.d/autojump.sh' >> .zshrc
$ source ~/.zshrc
```

## 常用方法
```bash
// 进入目录
j dir

// 子目录
jc child

// 打开目录
jo dir

// 打开子目录
jco

// 两个 inbox
> 30   /home/user/mail/inbox
> 10   /home/user/work/inbox
j in   //自动进入权重高的
j w in   //加个关键词呗
```