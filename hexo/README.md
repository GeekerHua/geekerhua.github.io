# 我的个人blog及笔记系统

> 这是我的个人blog及笔记系统的代码仓库

该系统使用hexo驱动，并借助于travis进行自动构建，博客静态文件及源码内容显示在同一个仓库下的两个branch。

- master分支是hexo生成静态文件后的代码。
- note分支为我的个人文件分支，note分支目录结构如下

```bash
.
├── LICENSE
├── README.md
├── .travis.yml
├── _posts
   ├── xxx.md
   ├── xxx.md
├── hexo
   ├── 404.html
   ├── about.md
   ├── tags.md
├── 其它
   ├── xxx.md
```

- `_posts`文件夹下的文章为发布的博客文章，
- hexo文件夹下的文件是hexo所需要的个性化文件，比如`404.html`,`_config.yml`等。
- `.travis.yml`为travis的配置文件