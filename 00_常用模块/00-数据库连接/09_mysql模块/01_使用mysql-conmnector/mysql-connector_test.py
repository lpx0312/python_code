#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：mysql-connector_test.py
@Author  ：lipanxiang
@Date    ：2022/4/24 13:52 
'''

# 安装模块
# python -m pip install mysql-connector

# 参考教程：
# https://www.cnblogs.com/-beyond/p/9798970.html
# https://www.runoob.com/python3/python-mysql-connector.html


import mysql.connector

mysql_config={
    'host':'10.0.0.51',
    "user":'mysqladmin',
    'password':'123456',
    'database':'standalonemcdb1.1_003'
}

# 接收参数：user, password, host, port=3306, unix_socket and database
# 返回一个MySQLConnection Object
mydb = mysql.connector.connect(**mysql_config)


# 创建一个命令执行客户端
cmd = mydb.cursor()

######## 创建数据表 ########
# sql="CREATE TABLE compent (xingtaiming1 VARCHAR(255), starttime datetime, xuhao int )"
# cmd.execute(sql)

######## select操作 ########
# # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
cmd.execute("select * from  compent")
#
# # 一、执行select操作，使用fetchall()一次性取回所有的结果集。取完之后在fetchall fetchone 都去取不到结果，类似于迭代器。
res = cmd.fetchall()
print(res)

# # 二、执行select操作，使用fetchone()每次只取一条记录
# res = cmd.fetchone()
# print(res)          # (bytearray(b'ohos_trunk'), datetime.datetime(2021, 5, 26, 21, 56), 1)
# res = cmd.fetchone()
# print(res)          # (bytearray(b'ohos_trunk2'), datetime.datetime(2021, 5, 26, 21, 56, 1), 2)
# res = cmd.fetchone()
# print(res)          # None


# # 三、执行select操作，使用fetchmany(num)指定每次返回的num条结果集
# res = cmd.fetchmany(2)
# print(res)             # [(bytearray(b'ohos_trunk'), datetime.datetime(2021, 5, 26, 21, 56), 1), (bytearray(b'ohos_trunk2'), datetime.datetime(2021, 5, 26, 21, 56, 1), 2)]


######### insert操作 ########
# # 执行原生SQL语句 INSERT INTO  compent ( xingtaiming1, starttime, xuhao ) VALUES ( 'ohos_trunk5', '2021-05-26 21:56:04', 5 );
# sql="INSERT INTO  compent ( xingtaiming1, starttime, xuhao ) VALUES ( '{0}', '{1}', {2} )".format('ohos_trunk7','2021-05-26 21:56:07',7)
# cmd.execute(sql)
# # 数据表内容有更新，必须使用到该语句
# mydb.commit()     # rowcount属性保存着受影响的记录数。
# print(cmd.rowcount, "记录插入成功。")



######## 占位符格式 ########
# # 注意: %s 必须单独  不能使用'' 引号引起来。
# sql="INSERT INTO  compent ( xingtaiming1, starttime, xuhao ) VALUES ( %s, %s, %s )"
# # print(cmd_str)
# cmd.execute( sql, ('ohos_trunk9','2021-05-26 21:56:09',9))
# print("执行成功")
# mydb.commit()

######### 批量insert操作 【重点】【########
# sql="INSERT INTO  compent ( xingtaiming1, starttime, xuhao ) VALUES ( %s, %s, %s )"
# # 注意数据必须是 列表 中套元祖
# data = [
#     ('ohos_trunk9', '2021-05-26 21:56:09', 9),
#     ('ohos_trunk10','2021-05-26 21:56:10',10),
#     ('ohos_trunk11','2021-05-26 21:56:11',11),
#     ('ohos_trunk12','2021-05-26 21:56:12',12)
# ]
# # 执行多条命令
# cmd.executemany(sql, data)
# # 数据表内容有更新，必须使用到该语句
# mydb.commit()     # rowcount属性保存着受影响的记录数。
# print("{0}条记录插入成功。".format(cmd.rowcount))


######### update操作 ########
# cmd_str="UPDATE  compent SET starttime=%s WHERE xingtaiming1 = %s"
# cmd.execute(cmd_str,('2021-05-26 00:00:00','ohos trunk'))
# mydb.commit()
# print("{0}条记录修改成功。".format(cmd.rowcount))

######### 批量update操作 ########
# cmd_str="UPDATE  compent SET starttime=%s WHERE xingtaiming1 = %s"
# # 注意数据必须是 列表 中套元祖
# data=[
#     ('2021-05-22 00:00:02', 'ohos_trunk2'),
#     ('2021-05-23 00:00:03', 'ohos_trunk3'),
#     ('2021-05-24 00:00:04', 'ohos_trunk4'),
#     ('2021-05-25 00:00:05', 'ohos_trunk5'),
#     ('2021-05-26 00:00:06', 'ohos_trunk6'),
#     ('2021-05-27 00:00:07', 'ohos_trunk7'),
#     ('2021-05-28 00:00:08', 'ohos_trunk8'),
#     ('2021-05-29 00:00:09', 'ohos_trunk9'),
# ]
# # 执行多条命令
# cmd.executemany(cmd_str,data)
# mydb.commit()
# print("{0}条记录修改成功。".format(cmd.rowcount))

######### 删除记录 ########
# sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
# cmd.execute(sql)
# mydb.commit()
# print(cmd.rowcount, " 条记录被修改")

######### 删除表 ########
# sql = "DROP TABLE IF EXISTS compent"  # 删除数据表 compent
# cmd.execute(sql)


# 2021-05-26 00:00:06
# import datetime
# now  =  datetime.datetime.now().strftime("%Y-%m-%d %X")
# print(now)
# # sql="INSERT INTO  compent ( xingtaiming1, starttime, xuhao ) VALUES ( %s, %s, %s )"
# sql  = "insert into compent  ( xingtaiming1, starttime, xuhao ) values (%s, %s, %s)"
# cmd.execute(sql,('hmos_trunk',now,99))
# mydb.commit()
# print(cmd.rowcount)


