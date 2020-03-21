---
title: githug实战
date:  2020/3/21 17:48:28
tags: [git]
categories: [code]
permalink: 4E9B4D94-AC1E-4E27-AF1C-7B8A722A8B11
---

## level 1 init

A new directory, `git_hug` , has been created; initialize an empty repository in it.

``` shell
$: git init
```

## level 2 config

Set up your git name and email, this is important so that your commits can be identified.

```shell
$: git config user.name "GeekerHua"
$: git config user.email "geekerhua@sina.com"
```

## level 3 add

There is a file in your folder called `README`, you should add it to your staging area
Note: You start each level with a new repo. Don't look for files from the previous one.

```shell
$: git add README
```

## level 4 commit

The `README` file has been added to your staging area, now commit it.

```shell
$: git commit -m 'add README'
```

## level 5 clone

Clone the repository at https://github.com/Gazler/cloneme.

```shell
$: git clone https://github.com/Gazler/cloneme
```

## level 6 clone_to_folder

Clone the repository at https://github.com/Gazler/cloneme to `my_cloned_repo`.

```shell
$: git clone https://github.com/Gazler/cloneme my_cloned_repo
```

## level 7 ignore

The text editor 'vim' creates files ending in `.swp` (swap files) for all files that are currently open.  We don't want them creeping into the repository.  Make this repository ignore those swap files which are ending in `.swp`.

```shell
$: echo '*.swp' >> .gitignore
```

## level 8 include

Notice a few files with the '.a' extension.  We want git to ignore all but the 'lib.a' file.

```shell
$: echo '*.a' >> .gitignore
$: echo '!lib.a' >> .gitignore
```

## level 9 status

There are some files in this repository, one of the files is untracked, which file is it?

```shell
$: git status
$: githug
$: database.yml
```

## level 10 status

There are some files in this repository, how many of the files will be committed?

```shell
$: git status
$: githug
$: 2
```

## level 11 rm

A file has been removed from the working tree, however the file was not removed from the repository.  Find out what this file was and remove it.

```shell
$: git rm deleteme.rb
```

## level 12 rm_cached

A file has accidentally been added to your staging area, find out which file and remove it from the staging area.  *NOTE* Do not remove the file from the file system, only from git.

```shell
$: git rm --cached deleteme.rb
```

## level 13 stash

You've made some changes and want to work on them later. You should save them, but don't commit them.

```shell
$: git stash
```

## level 14 rename

We have a file called `oldfile.txt`. We want to rename it to `newfile.txt` and stage this change.

```shell
$: git mv oldfile.txt newfile.txt
```

## level 15 restructure

You added some files to your repository, but now realize that your project needs to be restructured.  Make a new folder named `src` and using Git move all of the .html files into this folder.

```shell
$: mkdir src
$: git mv *.html src
```

## level 16 log

You will be asked for the hash of most recent commit.  You will need to investigate the logs of the repository for this.

```shell
$: git log
$: 5fcfd97e96df4f5c57e6da9c86db7cac5a18525a
```

## level 17 tag

We have a git repo and we want to tag the current commit with `new_tag`.

```shell
$: git tag -a
```

## level 18 push_tags

There are tags in the repository that aren't pushed into remote repository. Push them now.

```shell
$: git push --tags
```

## level 19 commit_amend

The `README` file has been committed, but it looks like the file `forgotten_file.rb` was missing from the commit.  Add the file and amend your previous commit to include it.

```shell
$: git add forgotten_file.rb
$: git commit --amend
```

## level 20 commit_in_future

Commit your changes with the future date (e.g. tomorrow).

```shell
$: git commit -m 'change date' --date='Wed Mar 28 22:32:36 2020 +0800'
```

## level 21 reset

There are two files to be committed.  The goal was to add each file as a separate commit, however both were added by accident.  Unstage the file `to_commit_second.rb` using the reset command (don't commit anything).

```shell
$: git reset HEAD to_commit_second.rb
```

## level 22 reset_soft

You committed too soon. Now you want to undo the last commit, while keeping the index.

```shell
$: git reset --soft HEAD^
```

## level 23 checkout_file

A file has been modified, but you don't want to keep the modification.  Checkout the `config.rb` file from the last commit.

```shell
$: git checkout -- config.rb
```

## level 24 remote

This project has a remote repository.  Identify it.

```shell
$: git remote -v
$: my_remote_repo
```

## level 25 remote_url

The remote repositories have a url associated to them.  Please enter the url of remote_location.

```shell
$: git remote -v
$: https://github.com/githug/not_a_repo
```

## level 26 pull

You need to pull changes from your origin repository.

```shell
$: git pull origin master
```

## level 27 remote_add

Add a remote repository called `origin` with the url https://github.com/githug/githug

```shell
$: git remote add origin https://github.com/githug/githug
```

## level 28 push

Your local master branch has diverged from the remote origin/master branch. Rebase your commit onto origin/master and push it to remote.

```shell
$: git rebase origin/master
$: git push
```

## level 29 diff

There have been modifications to the `app.rb` file since your last commit.  Find out which line has changed.

```shell
$: git diff app.rb
$: 26
```

## level 30 blame

Someone has put a password inside the file `config.rb` find out who it was.

```shell
$: git blame config.rb
$: Spider Man
```

## level 31 branch

You want to work on a piece of code that has the potential to break things, create the branch test_code.

```shell
$: git checkout -b test_code
```

## level 32 checkout

Create and switch to a new branch called my_branch.  You will need to create a branch like you did in the previous level.

```shell
$: git checkout -b my_branch
```

## level 33 checkout_tag

You need to fix a bug in the version 1.2 of your app. Checkout the tag `v1.2`.

```shell
$: git checkout v1.2
```

## level 34 checkout_tag_over_branch

You need to fix a bug in the version 1.2 of your app. Checkout the tag `v1.2` (Note: There is also a branch named `v1.2`).

```shell
$: git checkout tags/v1.2
```

## level 35 branch_at

You forgot to branch at the previous commit and made a commit on top of it. Create branch test_branch at the commit before the last.

```shell
$: git branch test_branch b5af165fe186c9d67eb264721247f925eb0bbbf0
```

## level 36 delete_branch

You have created too many branches for your project. There is an old branch in your repo called 'delete_me', you should delete it.

```shell
$: git branch -d delete_me
```

## level 37 push_branch

You've made some changes to a local branch and want to share it, but aren't yet ready to merge it with the 'master' branch.  Push only 'test_branch' to the remote repository

```shell
$: git checkout test_branch
$: git push --set-upstream origin test_branch
```

## level 38 merge

We have a file in the branch 'feature'; Let's merge it to the master branch.

```shell
$: git merge feature
```

## level 39 fetch

Looks like a new branch was pushed into our remote repository. Get the changes without merging them with the local repository

```shell
$: git fetch
```

## level 40 rebase

We are using a git rebase workflow and the feature branch is ready to go into master. Let's rebase the feature branch onto our master branch.

```shell
$: git checkout feature
$: git rebase master
```

## level 41 rebase_onto

You have created your branch from `wrong_branch` and already made some commits, and you realise that you needed to create your branch from `master`. Rebase your commits onto `master` branch so that you don't have `wrong_branch` commits.

```shell
$: git rebase --onto=master wrong_branch readme-update
```

## level 42 [repack](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-41.html)

Optimise how your repository is packaged ensuring that redundant packs are removed.

```shell
$: git repack
$: git repack -d
```

## level 43 cherry-pick

Your new feature isn't worth the time and you're going to delete it. But it has one commit that fills in `README` file, and you want this commit to be on the master as well.

```shell
$: git cherry-pick ca32a6d
```

## level 44 grep

Your project's deadline approaches, you should evaluate how many TODOs are left in your code

```shell
$: git grep TODO
```

## level 45 rename_commit

Correct the typo in the message of your first (non-root) commit.

```shell
$: git rebase -i 70f5d36
```

## level 46 squash

You have committed several times but would like all those changes to be one commit.

```shell
$: git rebase -i 156eac5
```

## level 47 [merge_squash](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-46.html)

Merge all commits from the long-feature-branch as a single commit.

```shell
$: git merge --squash long-feature-branch
$: git commit -m 'merge_wquash from long-feature-branch'
```

## level 48 [reorder](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-47.html)

You have committed several times but in the wrong order. Please reorder your commits.

## level 49 [bisect](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-48.html)

A bug was introduced somewhere along the way.  You know that running `ruby prog.rb 5` should output 15.  You can also run `make test`.  What are the first 7 chars of the hash of the commit that introduced the bug.

## level 50 [stage_lines](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-49.html)

You've made changes within a single file that belong to two different features, but neither of the changes are yet staged. Stage only the changes belonging to the first feature.

```shell
$: git add feature.rb --edit
```

## level 51 [find_old_branch](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-50.html)

You have been working on a branch but got distracted by a major issue and forgot the name of it. Switch back to that branch.

```shell
$: git reflog
```

## level 52 [revert](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-51.html)

You have committed several times but want to undo the middle commit.
All commits have been pushed, so you can't change existing history.

```shell
$: git revert 1fca878
```

## level 53 [restore](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-52.html)

You decided to delete your latest commit by running `git reset --hard HEAD^`.  (Not a smart thing to do.)  You then change your mind, and want that commit back.  Restore the deleted commit.

```shell
$: git reset ce90cf5 --hard
```

## level 54 [conflict](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-53.html)

You need to merge mybranch into the current branch (master). But there may be some incorrect changes in mybranch which may cause conflicts. Solve any merge-conflicts you come across and finish the merge.

```shell
$: git merge mybranch
```

## level 55 [submodule](https://wiki.jikexueyuan.com/project/githug-walkthrough/level-54.html)

You want to include the files from the following repo: `https://github.com/jackmaney/githug-include-me` into a the folder `./githug-include-me`. Do this without manually cloning the repo or copying the files from the repo into this repo.

```shell
$: git submodule add https://github.com/jackmaney/githug-include-me
```
