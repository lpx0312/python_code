#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：copytree使用.py
@Author  ：lipanxiang
@Date    ：2022/4/9 0:00 
'''
# 不符合要求

import os
import sys
import shutil


# 不太符合要求
def copydir(src, dest, symlinks=False, ignore=None):
    '''
    主要用于复制src文件夹中所有内容到 dest文件夹中。但是有个问题，如果源文件夹中存在 a文件夹，目标文件夹中也存在a文件夹，则copytree还是会报错
    # 来源：https://qastack.cn/programming/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
    # 试下 https://www.itranslater.com/qa/details/2326185655103128576 这个
    '''
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def need_suffix_ignore(ignore_rule,suffix):
    '''判断文件后缀 是否被 ignore规则匹配,如果被忽略了就返回 True，否则返回 False'''
    suffix_ignore = False
    for rule in ignore_rule:
        res = re.search(rule, suffix)
        print("res",res)
        if res:
            suffix_ignore = True
            break
    return suffix_ignore



# 参考文档：https://www.itranslater.com/qa/details/2326185655103128576
# 语法：shutil.copytree(oripath, despath, ignore= shutil.ignore_patterns("*.xls", "*.doc"))  这个ignore 也可以试着实现一下。
def copydir2(src, dest, symlinks=False, ignore=None):
    '''
    满足要求: 将src中的文件和文件夹，直接覆盖dest文件夹内的内容。(包含子文件夹中的内容也合并了，可以自己手动控制的，控制下src_dir就可以了。)
    但是没有满足，直接覆盖整个文件夹的目的，但是这种需求完全没有必要，这种可以直接
    '''
    print("ignore",ignore)
    for src_dir, dirs, files in os.walk(src):
        # demodir\ ['22'] ['1.mp4.lnk', '2.txt', '3.txt', '4.txt']
        # demodir\22 [] ['10.txt']
        print(src_dir,dirs,files)

        # 跳过合并 子目录，每个系统的判断可能不一样
        if not src_dir.endswith('\\') and  src_dir.find('\\') != -1  :
            print('src_dir',src_dir)
            continue

        # 可能不准确，单具体目前想不起来特殊例子
        dst_dir = src_dir.replace(src, dest, 1)

        # 把所有文件夹都创建出来。
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for file_ in files:

            # 在这里可以实现，ignore，类似于
            file_suffix = os.path.splitext(file_)[-1]
            if not file_suffix or need_suffix_ignore(ignore,file_suffix) :
                print("file:{0} 需要忽略，不覆盖(不拷贝)".format(file_))
                continue

            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # 判断两个文件是否相同 相同就跳过，
                if os.path.samefile(src_file, dst_file):
                    continue
                # 两个文件不相同就删除 ，目标文件夹中的不同的文件
                os.remove(dst_file)

            # 这里是 直接复制文件到目标目录中
            shutil.copy2(src_file, dst_dir)
            # 也可以移动到 目标目录中，可以设置一个参数，来固定
            # shutil.move(src_file, dst_dir)



def copyfileOrdir(src,dest,recursive=False,symlinks=False, ignore=None):
    '''
    src:源文件/目录路径
    dest:目标文件/目录路径
    recursive: 是否递归，如果前面src是目录的话，这里就必须设置为True
    ignore:是否忽略，复制某些文件。(功能目前还不全面)
    '''
    if os.path.isfile(src) :
        print('源文件是文件,包含快捷键，是否包含软链接还需要验证')
        shutil.copy(src,dest)
    elif os.path.isdir(src) :
        print('源文件是文件夹')
        # 如果添加了-r 参数,
        if recursive  :
            # 目标路径存在
            if os.path.exists(dest) :
                # 目标路径是一个目录
                if os.path.isdir(dest):
                    # shutil.copytree(args.SOURCE, args.DEST, symlinks=True)
                    copydir2(src, dest, symlinks=False, ignore=("\.lnk$", "\.txt$"))
                else:
                    print('目标路径{0}是一个文件，报错退出'.format(dest))
                    sys.exit(1)
            else:
                shutil.copytree(src, dest, symlinks=symlinks)
                print('目标路径不存在，直接创建对应{0}目录'.format(dest))
        else:
            print('源路径{0}是目录，未添加-r 递归参数'.format(src))
            sys.exit(1)


# copyfileOrdir(args.src,args.dest,args.recursive)

