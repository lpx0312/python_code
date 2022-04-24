#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：00_不用six模块如何兼容py2和3.py
@Author  ：lipanxiang
@Date    ：2022/4/21 21:14 
'''

# 参考教程
# https://www.wenjiangs.com/article/compatible-with-python-2-and-3.html


# 兼容python2 和 python3 的打印
from distutils.log import warn as printf
printf("hello world")


# 兼容2和3 的 urllib模块
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

# 兼容2和3 的zip
try:
    from itertools import izip as zip
except ImportError:
    pass

# 兼容StringIO模块
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO


try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET


g = urlopen('http://news.google.com/news?topic=h&output=rss')
f = StringIO(g.read())
g.close()
tree = ET.parse(f)
f.close()
for elmt in tree.getiterator():
    if elmt.tag == 'title' and not elmt.text.startswith('Top Stories'):
        printf('- %s' % elmt.text)