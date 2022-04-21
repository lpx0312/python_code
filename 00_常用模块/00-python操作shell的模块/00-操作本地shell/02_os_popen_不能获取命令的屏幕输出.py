#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：os_popen函数操作shell.py
@Author  ：lipanxiang
@Date    ：2022/4/20 21:21 
'''


'''
f=os.popen('command') 返回值是 一个文件对象
ret=f.read()  # ret就是 命令执行的屏幕输出
优点: 可以获取command的 屏幕输出
缺点: 但是不能获取 shell命令的结果状态码 也就是 $?
该方法:python3 好像已经被废弃，不建议使用【不推荐】
'''


# command在屏幕上 有打印的
import os
# 返回的是一个文件对象
f=os.popen("ls -l")
# 通过文件的read()读取所返回的内容
print(f.read())

'''
total 213568
-rw-r--r--   1 root root       486 Nov  2 22:34 1.py
-rw-r--r--   1 root root       389 Apr 14 20:45 1.sh
-rw-r--r--   1 root root       482 Nov  2 22:36 2.py
-rw-r--r--   1 root root      1234 Nov  3 00:43 3.py
-rw-------.  1 root root      1441 Jul 26  2021 anaconda-ks.cfg
drwxr-xr-x   3 root root        30 Oct 11  2021 ansible
drwxr-xr-x  11 root root       301 Apr 14 20:56 ansible_code
-rw-r--r--   1 root root       385 Oct 11  2021 fenfa.sh
-rw-r--r--   1 root root      2341 Oct  3  2021 install_tomcat.sh
-rw-r--r--   1 root root 218659557 Oct 10  2021 jenkins2.303plugin.tar.gz
drwxr-xr-x   3 root root        18 Oct 11  2021 pipeline_ansible
-rw-r--r--   1 root root        25 Mar 31 22:42 shell_study.sh
drwxr-xr-x   3 root root        28 Apr  8 00:17 t22
drwxr-xr-x   2 root root        31 Apr  8 00:28 tt
'''


# command在屏幕上 没有打印内容
import os
f = os.popen("touch b.txt")
print(f.read())
ret=f.read()
if ret :
    print("cunzai")
else:
    print("bucunzai")
