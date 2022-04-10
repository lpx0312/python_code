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

# 第一步: 创建解释器
## 设置程序名
prog='copy'
## 设置用法
uasge="""
cp [OPTION]... [-T] SOURCE DEST
or:  cp [OPTION]... SOURCE... DIRECTORY
or:  cp [OPTION]... -t DIRECTORY SOURCE...
"""
## 设置help信息前的信息
description="Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY"
## 设置help信息后的信息
epilog="the message info after help info"
## 设置参数前缀，默认为 -
prefix_chars='-'
## formatter_class 设置help信息输出格式，暂时不用，
## parents：由ArgumentParser对象组成的列表，它们的arguments选项会被包含到新ArgumentParser对象中，暂时不用
## fromfile_prefix_chars：前缀字符，放在文件名之前
## argument_default：参数的全局默认值。例如，要禁止parse_args时的参数默认添加， parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
## conflict_handler：解决冲突的策略，默认情况下冲突会发生错误：可以设置为 argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser = argparse.ArgumentParser(prog=prog,usage=uasge,description=description,
                                 epilog=epilog,prefix_chars='-',fromfile_prefix_chars="@")




# 第二步: 添加参数选项
##  const：保存一个常量
## default：默认值
## type：参数类型
## required：是否必选

# 位置参数 解析时没有位置参数就会报错了。
parser.add_argument('src',type=str,default='',help='')
parser.add_argument('dest',type=str,default='')

# 可选参数
parser.add_argument('-f','--force',action = 'store_true',help='强制拷贝')
parser.add_argument('-r','--recursive',action = 'store_true',help='拷贝目录')

args = parser.parse_args('-r demodir demodir2'.split())
# args = parser.parse_args('1.mp4.lnk demodir'.split())
print(args)

## desk：可作为参数名
'''
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
'''

## choices：可供选择的值
'''
>>> parser = argparse.ArgumentParser(prog='doors.py')
>>> parser.add_argument('door', type=int, choices=range(1, 4))
>>> print(parser.parse_args(['3']))
Namespace(door=3)
>>> parser.parse_args(['4'])
usage: doors.py [-h] {1,2,3}
doors.py: error: argument door: invalid choice: 4 (choose from 1, 2, 3)
'''


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



# nargs：参数的数量 值可以为整数N(N个)，*(任意多个)，+(一个或更多)
r'''
# * N个 参数
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='*')
>>> parser.add_argument('--bar', nargs='*')
>>> parser.add_argument('baz', nargs='*')
>>> parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

# 值为？时，首先从命令行获得参数，若没有则从const获得，然后从default获得：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')
>>> parser.parse_args('XX --foo YY'.split())
Namespace(bar='XX', foo='YY')
>>> parser.parse_args('XX --foo'.split())
Namespace(bar='XX', foo='c')
>>> parser.parse_args(''.split())
Namespace(bar='d', foo='d')

## 参数是文件 
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
...                     default=sys.stdin)
>>> parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
...                     default=sys.stdout)
>>> parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile=<open file 'input.txt', mode 'r' at 0x...>,
          outfile=<open file 'output.txt', mode 'w' at 0x...>)
>>> parser.parse_args([])
Namespace(infile=<open file '<stdin>', mode 'r' at 0x...>,
          outfile=<open file '<stdout>', mode 'w' at 0x...>)
'''


