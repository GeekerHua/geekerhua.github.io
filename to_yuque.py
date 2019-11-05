# -*- coding: utf-8 -*-
# @Time    : 2019-11-01 21:49

import os


def get_article_statement(url):
    return [
        "> 本文作者： GeekerHua\n",
        "> 本文链接： https://www.yuque.com/geekerhua/blog/{}\n".format(url),
        "> 文章首发： 同步首发于 [语雀](https://www.yuque.com/geekerhua/blog/{url}) 及 [GeekerHua的blog](https://blog.geekerhua.com/{url}/)\n".format(
            url=url),
        "> 版权声明： 本博客所有文章除特别声明外，均采用 CC BY-NC-SA 4.0 许可协议。转载请注明出处！",
    ]


def change_to_yuque(file_path):
    new_lines = []
    permalink = None
    with open(file_path) as f:
        lines = f.readlines()
        title = None
        changed = False
        for line in lines:
            if (line.startswith('> 本文作者')):
                break
            if line.startswith('title'):
                title = line.split(':', 1)[1].strip()
            if not changed and line.startswith('permalink:'):
                new_lines.append(line.replace('permalink:', 'url:'))
            else:
                new_lines.append(line)
            if line.startswith('permalink:') or line.startswith('url:'):
                permalink = line.split(':')[1].strip()
            if line.startswith('---') and title and not changed:
                new_lines.append('# {}\n'.format(title))
                changed = True
    with open(file_path, 'w') as f:
        f.writelines(new_lines)
        f.writelines(get_article_statement(permalink))


def walk_files():
    for (root, dirs, files) in os.walk('source/_posts'):
        for file_name in files:
            if file_name.endswith('.md'):
                change_to_yuque(os.path.join(root, file_name))


if __name__ == "__main__":
    walk_files()
    # change_to_yuque('_posts/mac/mac_setting.md')
