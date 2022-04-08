#!/usr/bin/env python
# coding:utf-8

import argparse



# prefix_chars 设置参数的前缀 - ，不能设置为空，默认是 -，所以参数只能是 -length 或者--length
parser = argparse.ArgumentParser('计算长方形的周长',prefix_chars='-')

# 添加可选参数
parser.add_argument('-l','--length',default=10,type=int,help='长')
parser.add_argument('-w','--width',default=20,type=int,help='宽')
parser.add_argument('-f',action = 'store_true',help='长')
parser.add_argument('-r',action = 'store_true',help='长')

args = parser.parse_args()
print('args',args)

if __name__ == '__main__' :
    # result = args.length * args.width
    # print(result)

    import re

    ret4= re.match("\*.lnk","1.lnk")
    print(ret4)
    # print(type(ret4)) # <class 're.Match'>
    # print(ret4.group())
    # print(ret4.span())


# windows中最好加上r，不转移，否则三引号注释会报错
r""" 
# 第一种:使用默认参数
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py
args Namespace(length=10, width=20)

# 第二种: 使用短参数
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  -l 20  -w 30
args Namespace(length=20, width=30)
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  -l20  -w30
args Namespace(length=20, width=30)
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  -l=20  -w=30
args Namespace(length=20, width=30)


# 第三种: 使用长参数 : 推荐
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  --length 20  --width 30
args Namespace(length=20, width=30)
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  --length=20  --width=30
args Namespace(length=20, width=30)
- 这种报错
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py  --length20  --width30
usage: 计算长方形的周长 [-h] [-l LENGTH] [-w WIDTH]
计算长方形的周长: error: unrecognized arguments: --length20 --width30


帮助文档：
C:\Users\lipanx\Desktop\python_code\python_code\00_常用模块\05_命令行参数模块\02_argparse模块>python first_argparse.py -h
usage: 计算长方形的周长 [-h] [-l LENGTH] [-w WIDTH]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        长
  -w WIDTH, --width WIDTH
                        宽
"""