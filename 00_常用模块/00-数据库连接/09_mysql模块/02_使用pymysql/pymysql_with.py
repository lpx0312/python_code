#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：pymysql_with.py
@Author  ：lipanxiang
@Date    ：2022/4/25 23:18 
'''


import pymysql
# pymysql实现通过 with 简化数据库操作

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':

    mysql_config = {
        'host': '10.0.0.51',
        "user": 'mysqladmin',
        'password': '123456',
        'database': 'dev_metadata'
    }

    with DB(host=mysql_config.get('host'),user=mysql_config.get('user'),passwd=mysql_config.get('password'),db=mysql_config.get('database')) as db:
        db.execute('SELECT * FROM dev_icehck')
        print(db)
        for i in db:
            print(i)