#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：argparse位置参数与可选参数.py
@Author  ：lipanxiang
@Date    ：2022/4/6 22:36 
'''


import argparse
import shutil
import os
import sys
import re

uasge="""
cp [OPTION]... [-T] SOURCE DEST
or:  cp [OPTION]... SOURCE... DIRECTORY
or:  cp [OPTION]... -t DIRECTORY SOURCE...
"""
description="Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY"


parser = argparse.ArgumentParser(prog='copy',usage=uasge,description=description,epilog="the message info after help info",prefix_chars='-')
# 位置参数
parser.add_argument('src',type=str,default='',help='')
parser.add_argument('dest',type=str,default='')

# 可选参数
parser.add_argument('-f','--force',action = 'store_true',help='强制拷贝')
parser.add_argument('-r','--recursive',action = 'store_true',help='拷贝目录')

args = parser.parse_args('-r demodir demodir2'.split())
# args = parser.parse_args('1.mp4.lnk demodir'.split())
print(args)


# 不符合要求
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
    print("ignore_rule",ignore_rule)
    print("suffix",suffix)
    suffix_ignore = False
    for rule in ignore_rule:
        print("rule",rule)
        res = re.search(rule, suffix, flags=0)
        # res = re.match(rule, suffix)
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
            # 获取文件后缀
            file_suffix = os.path.splitext(file_)[-1]
            print(file_suffix)

            # 【重点】 这里的正则 还是有问题，周末一定要恶补
            # if need_suffix_ignore(ignore,file_suffix) :
            #     print("file:{0} 需要忽略，不覆盖(不拷贝)")
            #     continue
            # 判断后缀是否在 re规则中，如果在就返回true，


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




def copyfileOrdir(src,dest,recursive,symlinks=False, ignore=None):
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
                    copydir2(src, dest, symlinks=False, ignore=("*.lnk", "*.txt"))
                else:
                    print('目标路径{0}是一个文件，报错退出'.format(dest))
                    sys.exit(1)
            else:
                shutil.copytree(src, dest, symlinks=True)
                print('目标路径不存在，直接创建对应{0}目录'.format(dest))
        else:
            print('源路径{0}是目录，未添加-r 递归参数'.format(src))
            sys.exit(1)

copyfileOrdir(args.src,args.dest,args.recursive)


# shutil.copytree("demodir","demodir2\\")



# if not args.r :
#     shutil.copyfile(args.SOURCE,args.DEST,args.r)
# else:
#     shutil.copytree(args.SOURCE,args.DEST,args.r)





# action 动作
r'''
1. store 保存参数值，可能会先将参数值转换成另一个数据类型。若没有显式指定动作，则默认为该动作。
2. store_const 保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值。这通常用于实现非布尔值的命令行标记。
3，store_ture/store_false 保存相应的布尔值。这两个动作被用于实现布尔开关。 【常用】
4. append 将值保存到一个列表中。若参数重复出现，则保存多个值。【常用】
>>> import argparse
>>> parse = argparse.ArgumentParser()
>>> parse.add_argument('-b',action = 'append')
_AppendAction(option_strings=['-b'], dest='b', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)
>>> parse.parse_args('-b  100 -b 200'.split())
Namespace(b=['100', '200'])

5. append_const 将一个定义在参数规格中的值保存到一个列表中。



6. version 打印关于程序的版本信息，然后退出
>>> import argparse
>>> parse = argparse.ArgumentParser(prog = 'the demo ')
>>> parse.add_argument('--version',action = 'version',version = '%(prog)s2.0')
_VersionAction(option_strings=['--version'], dest='version', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help="show program's version number and exit", metavar=None)
>>> parse.parse_args('--version'.split())
the demo 2.0

7. count统计参数出现的次数
>>> import argparse
>>> parse = argparse.ArgumentParser()
>>> parse.add_argument('-b',action = 'count')
_CountAction(option_strings=['-b'], dest='b', nargs=0, const=None, default=None, type=None, choices=None, help=None, metavar=None)
>>> parse.parse_args('-b -b'.split())
Namespace(b=2)

'''


