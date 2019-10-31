# git

## Git使用

新建仓库

``` bash
git init
git add .
git commit -m "xxxx"
git remote add origin git@gitxxxxxxx.git
git push -u origin master
```

已存在的仓库

``` bash
git remote add origin git@github.com:phodal/github-roam.git
git push -u origin master
```

## tag(打标签)

- 提交代码
    - `git add .`
    - `git commit -m "fixed some bugs"`
- 添加标签
    - `git tag -a 0.1.3 -m "Release version 0.1.3"`
- 提交标签
    - `git push origin master`
    - `git push origin --tags`
-   删除标签的命令

   - `git tag -d 0.1.3`

- 删除远端服务器的标签

   - `git push origin :refs/tags/0.1.3`

## git基本命令

| 命令                                            | 说明        |
|-------------------------------------------------|-------------|
| $ git config --global user.name `"姓名"` | 告诉git你是谁 |
| $ git config --global user.email `"xxx@qq.com"` | 告诉git你是谁 |
| $ git config -l                                 | 查看配置信息  |

## clone指定版本

 `git clone --depth=1 https://github.com/xxx/xxx.git`

## 删除操作

- 删除本地与远程的分支链接
    - `git branch --delete --remotes origin/gh-pages`

------
# pro-git

* 查看尚未暂存的文件变更: git diff
* 查看暂存区文件变更: git diff --cached / git diff --staged
* 删除文件追踪， 但保留文件到硬盘: git rm --cached xxx
* 重新提交： git commit --amend
* 取消暂存： git reset HEAD <file>...
* 撤销对文件的修改： git checkout -- <file>...
* 创建附注标签： git tag -a v1.4 -m 'my version 1.4 [SHA]'
* 查看标签： git tag
* 查看标签信息: git show xxx
* 推送指定标签： git push origin [tagname]
* 推送全部标签： git push origin --tags
* checkout标签(在某个tag处创建新分支)： git checkout -b [branchname] [tagname]
* git别名： git config --global alias.ci commit
* 凭证存储： git config --global credential.helper cache

## 推送

* 设置跟踪分支： git checkout --track origin/serverfix
* 本地分支与远程分支不同名： git checkout -b sf origin/serverfix
* 设置已有本地跟踪或修改： git branch -u origin/serverfix
* 上游快捷方式： @{u} 可以引用origin/master    ???

* 删除远程分支： git push origin --delete serverfix

## 危险操作

* git reset --hard
* git checkout -- <file>

