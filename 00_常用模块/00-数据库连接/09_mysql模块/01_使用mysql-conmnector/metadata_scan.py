#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：metadata_scan.py
@Author  ：lipanxiang
@Date    ：2022/4/24 20:56 
'''
# 参考： https://blog.csdn.net/qq_41562433/article/details/82995098


# 源数据扫描
import sys
import argparse
import os
import mysql.connector

config={
    'host':'10.0.0.51',
    'port':'3306',
    'user':'mysqladmin',
    'password':'123456',
    'database': 'dev_metadata'
}

def ignore_dir(rootdir,path):
    ignore_lst=['/.git','/.idea']
    for ignore in ignore_lst:
        if ignore in os.path.join(path).replace(rootdir,''):
            return True
    return False

def ignore_file(file_name):
    file_ignore = ['.gitignore', '.gitkeep']
    if file_name in file_ignore:
        return True
    return False


def insert_mysql(total_file_path,projectName):
    # print('call insert_mysql')
    mydb = mysql.connector.connect(**config)
    mycursor = mydb.cursor()
    sql='insert into dev_icehck (project_name,path) VALUES (%s,%s)'
    mycursor.execute(sql,(projectName,total_file_path))
    mydb.commit()
    #print("{0}条数据插入成功".format(mycursor.rowcount))

def metadata_scan(rootdir,projectName):
    print('scan_code_rootdir:::{0}'.format(rootdir))
    paths=os.walk(rootdir,topdown=False)
    mfiles=[]
    for path, dir_lst , file_lst in paths:
        # 如果包含有隐藏文件的忽略掉。
        # print("path::::",path)
        if ignore_dir(rootdir,path):
            # print("path:::: 忽略", path)
            continue
        # 注意windows和linux斜线的不一样
        if "/metedata/" not in os.path.join(path):
            continue
        # 如果不包含,metedata目录 也跳过。
        for file in file_lst:
            if ignore_file(file):
                continue
            file_path=os.path.join(path,file)
            total_file_path = file_path[len(rootdir):]
            # print(total_file_path,projectName)
            insert_mysql(total_file_path,projectName)
            mfiles.append((total_file_path,projectName))
    print('scan_metadata_num:::{0}'.format(len(mfiles)))


def getargs():
    parser = argparse.ArgumentParser('源数据扫描', prefix_chars='-')
    parser.add_argument('-r','--rootdir',default='.', type=str, help='需要扫描的目录地址')
    parser.add_argument('-n','--projectName', type=str, help='工程名')
    args = parser.parse_args()
    return vars(args)

if __name__ == '__main__' :
    # python metadata_scan.py  --rootdir="/root/python_code" --projectName="hmos"
    args = getargs()
    rootdir = args.get('rootdir')
    projectName = args.get('projectName')
    print(args)
    if not rootdir or not projectName :
        print('metadata_scan.py args is failed')
        sys.exit(1)

    metadata_scan(rootdir, projectName)


