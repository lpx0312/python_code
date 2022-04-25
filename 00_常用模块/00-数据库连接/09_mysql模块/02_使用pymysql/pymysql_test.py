#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：pymysql_test.py
@Author  ：lipanxiang
@Date    ：2022/4/25 14:40 
'''

# 参考教程:
# https://www.runoob.com/python3/python3-mysql.html
# https://zhuanlan.zhihu.com/p/31732617
# https://blog.csdn.net/kejiayuan0806/article/details/124318464
# 缺点pymysql 仅支持 python3+
# pymysql兼容mysql可以参考： https://blog.csdn.net/Jerry_1126/article/details/80872379
# https://www.cnblogs.com/hiwuchong/p/9096542.html 【重点】



mysql_config={
    'host':'10.0.0.51',
    "user":'mysqladmin',
    'password':'123456',
    'database':'dev_metadata'
}


import pymysql
# 打开数据库连接
db = pymysql.connect(**mysql_config)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()







###########  创建表 #############
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)



###########  select操作 #############
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT * FROM dev_icehck")
#
# # 使用 fetchone() 方法获取单条数据.
# # 使用 fetchmany(2) 方法 获取指定条的数据
# # 使用 fetchall() 方法获取所有数据
# data = cursor.fetchone()
# print(data)




###########  insert操作 #############
# sql = "INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES (%s, %s, %s, %s, %s)"
# data=[
#     ('li', 'px', 18, 'm', 1.01),
#     ('w', 'y', 19, 'w', 1.02)
# ]
# # execute     单行执行sql
# # executemany 批量执行sql
#
# try :
#     cursor.executemany(sql,data)
#     # 报错修改和新增: 提交当前事务
#     db.commit()
# except :
#     # 发生错误时回滚。
#     db.rollback()


###########  UPDATE操作 #############
# sql = "UPDATE EMPLOYEE SET AGE=100 WHERE FIRST_NAME='li'"
# try :
#     cursor.execute(sql)
#     # 报错修改和新增: 提交当前事务
#     db.commit()
# except :
#     # 发生错误时回滚。
#     db.rollback()



###########  DELETE操作 #############
# sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = 'li'"
# try :
#     cursor.execute(sql)
#     # 报错修改和新增: 提交当前事务
#     db.commit()
# except :
#     # 发生错误时回滚。
#     db.rollback()





# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()