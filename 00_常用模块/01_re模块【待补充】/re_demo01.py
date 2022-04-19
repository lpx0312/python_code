#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：re_demo01.py
@Author  ：lipanxiang
@Date    ：2022/4/8 21:06 
'''

"""
不良内容过滤
"""
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


def main2():
    res = re.search("\.py$","111.py")
    print(res)

if __name__ == '__main__':
    main2()








