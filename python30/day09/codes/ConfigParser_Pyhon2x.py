#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''conf.ini
[db1]
conn = localhost
port = 3306
user = root
password = 123456
dbname = test

[db2]
conn = localhost
port = 3306
user = root
password = 123456
dbname = test1
'''


import ConfigParser
conf = ConfigParser.ConfigParser()
# 将conf.ini内容读取到conf对象中。
conf.read('conf.ini')

# 获取所有section头
print conf.sections()   # ['db1', 'db2']
# 获取指定db1的setion中所有option
print conf.options('db1')  # ['conn', 'port', 'user', 'password', 'dbname']
# 获取指定db1的setion的所有option和value
print conf.items('db1')    # [('conn', 'localhost'), ('port', '3306'), ('user', 'root'), ('password', '123456'), ('dbname', 'test')]
# 获取指定section中的指定option的value
print conf.get('db1', 'conn')


# 添加section
if not  conf.has_section('db3') :
     conf.add_section('db3')
# 添加section中的option的value值
conf.set('db3', 'conn', '127.0.0.1')
# 修改section中的option的value值
conf.set('db3', 'conn', '张三')
# 删除section
conf.remove_section('db2')
# 删除section中的option
conf.remove_option('db1', 'dbname')


# 将修改后的config重新写入文件中，也可以写到别的文件中
conf.write(open('conf.ini', 'w'))






# 判断section是否存在
print conf.has_section('PHP')  # True
print 'PHP' in conf.sections()  # True
# 判断section中的option是否存在
print conf.has_option('PHP', 'precision') # True  这种就不会报错，推荐使用这一种
# print 'precision' in conf.options('PHP')  # True 这种如果添加的section PHP不存在会报错

# 判断option在配置文件中是否存在，存在返回所在section的列表
def get_section(config,itemname):
     '''
     根据配置项名字，获取所在组section
     :paramn config： ConfigParser实例对象
     :param itemname:配置项名
     :return:返回所在组名的列表
     '''
     l = []
     for option in config.sections():
          if itemname in  config.options(option) :
               l.append(option)
     return  l