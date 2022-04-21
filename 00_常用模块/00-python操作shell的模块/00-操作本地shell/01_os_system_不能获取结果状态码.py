#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：os_system函数操作shell.py
@Author  ：lipanxiang
@Date    ：2022/4/20 20:39 
'''


'''
ret=os.system('command') 
返回值ret是: command 的shell命令的整体返回值，就算包含| 管道。相当于命令的 $?的值
而且执行的时候会打印命令的执行结果，报错也会打印出来
但是 命令的屏幕输出 os.system 获取不到 【缺点】
该方法:python3 好像已经被废弃，不建议使用【不推荐】
'''

import os
ret=os.system('ls')
#1.py  1.sh  2.py  3.py	anaconda-ks.cfg  ansible  ansible_code	fenfa.sh  install_tomcat.sh  jenkins2.303plugin.tar.gz	pipeline_ansible  shell_study.sh  t22  tt
print(ret)
#0

ret=os.system('ls | grep ".py"')
# 1.py
# 2.py
# 3.py
print(ret)
# 0

ret=os.system('l1 | grep ".py"')
# sh: l1: command not found
print(ret)
# 256

ret=os.system('ls | grep1 ".py"')
# sh: grep1: command not found
# ls: write error: Broken pipe
print(ret)
# 32512


'''
基于: os.system 的特性，我们也可以直接使用以下方式，仅仅来判断命令是否正常运行
'''
ret=os.system('ls 2>/dev/null | grep1 ".py" &>/dev/null ')
print(ret)
# 32512
ret=os.system('ls 2>/dev/null | grep ".py" &>/dev/null ')
print(ret)
# 0
