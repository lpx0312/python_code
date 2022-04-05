#!/usr/bin/env python
# coding:utf-8

import argparse

parser = argparse.ArgumentParser('计算长方形的周长')
parser.add_argument('--length',default=10,type=int,help='长')
parser.add_argument('--width',default=20,type=int,help='宽')
args = parser.parse_args()

if __name__ == '__main__' :
    result = args.length * args.width
    print(result)

'''
D:\User\Desktop\gitea_python\python_code\00_常用模块\05_命令行参数模块\01_optparse模块>python first_argparse.py
200
'''