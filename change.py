# -*- coding: utf-8 -*-
# @Time    : 2019-11-01 21:49
import sys
import os

def get_article_statement(url, blog_url):
    return [
        "\n",
        "> 本文作者： GeekerHua\n",
        "> 本文链接： {}/{}/\n".format(blog_url, url),
        "> 文章首发： 同步首发于 [语雀](https://www.yuque.com/geekerhua/blog/{url}) 及 [GeekerHua的blog](https://blog.geekerhua.com/{url}/)\n".format(url=url),
        "> 版权声明： 本博客所有文章除特别声明外，均采用 CC BY-NC-SA 4.0 许可协议。转载请注明出处！",
        "\n",
    ]

def change_to_hexo(file_path, revert=False):
    new_lines = []
    permalink = None
    with open(file_path) as f:
        lines = f.readlines()
        title = None
        changed = False
        empty_lines = []
        for line in lines:
            if (line.startswith('> 本文作者')):
                break
            if line.startswith('title'):
                title = line.split(':', 1)[1].strip()
            if changed or line.startswith('url:'):
                line = line.replace('url:', 'permalink:')
            if line.startswith('permalink:') or line.startswith('url:'):
                permalink = line.split(':')[1].strip()
            if changed or not line.startswith('# {}'.format(title)):
                if line == '\n':
                    empty_lines.append(line)
                else:
                    new_lines.extend(empty_lines)
                    empty_lines = []
                    new_lines.append(line)
            else:
                changed = True
        # new_lines.append('\n')

    with open(file_path, 'w') as f:
        f.writelines(new_lines)
        if not revert:
            f.writelines(get_article_statement(permalink, 'https://blog.geekerhua.com'))

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
        f.writelines(get_article_statement(permalink, 'https://www.yuque.com/geekerhua/blog'))


def walk_files(mode):
    for (root, dirs, files) in os.walk('source/_posts'):
        for file_name in files:
            if file_name.endswith('.md'):
                if mode == 'hexo':
                    change_to_hexo(os.path.join(root, file_name))
                elif mode == 'yuque':
                    change_to_yuque(os.path.join(root, file_name))
                elif mode == "revert":
                    change_to_hexo(os.path.join(root, file_name), True)

if __name__ == "__main__":
    walk_files(sys.argv[1])
    # change_to_hexo('_posts/mac/mac_setting.md')
