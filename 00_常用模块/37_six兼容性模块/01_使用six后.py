#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：01_使用six后.py
@Author  ：lipanxiang
@Date    ：2022/4/22 8:33 
'''

def import_utf8():
    import six
    print("six")

import six
# import_utf8()
print(six.PY2)
# 解决python2中打印返回中文，python3返回b'\xe5\x91\xb5\xe5\x91\xb5\xe5\x91\xb5\xe5\x91\xb5\n'的问题
def convert_to_unicode(text):
    """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
    if six.PY3:
        if isinstance(text, str):
            return text
        elif isinstance(text, bytes):
            return text.decode("utf-8", "ignore")
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    elif six.PY2:
        if isinstance(text, str):
            return text.decode("utf-8", "ignore")
        elif isinstance(text, unicode):
            return text
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    else:
        raise ValueError("Not running on Python2 or Python 3?")



# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# html = convert_to_unicode(response.read())
# print(html)
#
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()
# print(html)