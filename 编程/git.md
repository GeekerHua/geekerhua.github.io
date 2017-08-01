# git
## Git使用
新建仓库

```zsh
git init
git add .
git commit -m "xxxx"
git remote add origin git@gitxxxxxxx.git
git push -u origin master
```
已存在的仓库

```zsh
git remote add origin git@github.com:phodal/github-roam.git
git push -u origin master
```
## tag(打标签)
- 提交代码
    - `git add .`
    - `git commit -m "fixed some bugs"`
- 添加标签
    -    `git tag -a 0.1.3 -m "Release version 0.1.3"`
- 提交标签
    -   `git push origin master`
    -   `git push origin --tags`
-   删除标签的命令
   -    `git tag -d 0.1.3`
- 删除远端服务器的标签
   -   `git push origin :refs/tags/0.1.3`

## git基本命令

命令   |   说明
--- | ---
$ git config --global user.name \"姓名\"   |   告诉git你是谁
$ git config --global user.email \"xxx@qq.com\"   |   告诉git你是谁
$ git config -l   |   查看配置信息

## clone制定版本
`git clone --depth=1 https://github.com/GeekerHua/LearnPython.git`

## 删除操作
- 删除本地与远程的分支链接
    - `git branch --delete --remotes origin/gh-pages`