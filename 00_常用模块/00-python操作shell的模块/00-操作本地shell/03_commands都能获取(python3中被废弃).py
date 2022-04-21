#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：03_commands都能获取.py
@Author  ：lipanxiang
@Date    ：2022/4/20 22:01 
'''



'''
commands.getstatusoutput(cmd) 方法的执行结果是一个元组，第一个结果是状态码，第二个是输出结果的字符串格式
缺点:python3中已经废弃【重点】
优点: 可以获取 结果状态码  和  结果字符串
'''

import commands
cmd = "cd /tmp && mkdir tt3 && ls"
res = commands.getstatusoutput(cmd)
print(res)
# (0, 'tt\ntt2\ntt3')
res = commands.getstatusoutput(cmd)
print(res)
# (256, 'mkdir: cannot create directory \xe2\x80\x98tt3\xe2\x80\x99: File exists')


# 下贱两种方法都不推荐。
status = commands.getstatus('cat /etc/hosts')
print(status)
#ls: cannot access cat /etc/hosts: No such file or directory

# 仅获取屏幕返回值
output = commands.getoutput('cat /etc/hosts')
print(output)
# 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
# ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
# 10.0.0.30   gitlab.lpx.com
