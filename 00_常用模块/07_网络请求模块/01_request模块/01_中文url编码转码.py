#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except Exception as e :
    print('No python2')

# python 2 中文URL编码转化问题
# import urllib
# s2 = urllib.quote('武汉')
# print s2  # %E6%AD%A6%E6%B1%89
# print urllib.unquote(s2)  # 武汉


# qutoe和unqutoe被放到了urllib.parse中
# python 3 中文URL编码转换问题
## 编码quote
# 不推荐
from urllib.request import quote
print(quote('武汉'))

# 推荐
from urllib import parse
print(parse.quote('武汉'))

## 解码unquote
from urllib import parse
s = parse.quote('武汉')
s1 = parse.unquote(s)
print(s1)











