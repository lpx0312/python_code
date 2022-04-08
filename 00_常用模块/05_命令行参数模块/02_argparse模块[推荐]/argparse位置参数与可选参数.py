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


