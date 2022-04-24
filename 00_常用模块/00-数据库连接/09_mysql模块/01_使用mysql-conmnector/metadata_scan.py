#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：metadata_scan.py
@Author  ：lipanxiang
@Date    ：2022/4/24 20:56 
'''


# 源数据扫描
import sys
import argparse
import os

def ignore_dir(rootdir,path):
    ignore_lst=['/.git/','/.idea/']
    for ignore in ignore_lst:
        if ignore in os.path.join(path).replace(rootdir,''):
            return True
    return False

def metadata_scan(rootdir,projectName):
    paths=os.walk(rootdir,topdown=False)
    print(paths)
    for path, dir_lst , file_lst in paths:
        # 如果包含有隐藏文件的忽略掉。
        if ignore_dir(rootdir,path):
            continue
        if '/metedate/' not in os.path.join(path):
            continue
        # 如果不包含,metedata目录 也跳过。
        for i in file_lst:
            file_abs_path=os.path.join(path,file_lst)





def getargs():
    parser = argparse.ArgumentParser('源数据扫描', prefix_chars='-')
    parser.add_argument('-r','--rootdir',default='.', type=str, help='需要扫描的目录地址')
    parser.add_argument('-n','--projectName', type=str, help='工程名')
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__' :
    # python metadata_scan.py  --rootdir="/mnt/disk" --projectName="hmos
    args = getargs()
    rootdir = args.get('rootdir')
    projectName = args.get('projectName')
    if not rootdir or not projectName :
        print('metadata_scan.py args is failed')
        sys.exit(1)

    metadata_scan(rootdir, projectName)


