# -*- coding: utf-8 -*-
# @Time    : 2019-11-01 21:49

import os


def change_to_yuque(file_path):
    new_lines = []
    with open(file_path) as f:
        lines = f.readlines()
        title = None
        changed = False
        for line in lines:
            if line.startswith('title'):
                title = line.split(':', 1)[1].strip()
            if not changed and line.startswith('permalink:'):
                new_lines.append(line.replace('permalink:', 'url:'))
            else:
                new_lines.append(line)
            if line.startswith('---') and title and not changed:
                new_lines.append('# {}\n'.format(title))
                changed = True
    with open(file_path, 'w') as f:
        f.writelines(new_lines)


def walk_files():
    for (root, dirs, files) in os.walk('source/_posts'):
        for file_name in files:
            if file_name.endswith('.md'):
                change_to_yuque(os.path.join(root, file_name))


if __name__ == "__main__":
    walk_files()
    # change_to_yuque('_posts/mac/mac_setting.md')
