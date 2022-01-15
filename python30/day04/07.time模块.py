import time
# 模块，即一个py文件

# 三种时间形式
# 1.时间戳：计算机可以读懂
# 2.时间字符串：“2020-12-12” 人可以读懂
# 3.时间元祖：(年,月,日...)，可以单独取出

# <1> 当前时间戳float类型
import time
print(time.time())

# <2> 时间字符串
'''
%Y  年
%m  月
%d  日
%H  时
%M  分
%S  秒
%X  等同于%H:%M:%S
'''
# :%M:%s
# strtime没有加第二个参数，默认当前的时间的时间元祖
print(time.strftime("%Y-%m-%d  %H:%M:%S"))
print(time.strftime("%Y-%m-%d  %X"))


# <3> 时间元祖
# localtime 没有加参数，默认当前时间元祖
print(time.localtime())
print(type(time.localtime()))
t = time.localtime()
print(t[0]) # 年
print(t[1]) # 月
print(t[2]) # 日
print(t[3]) # 时
print(t[4]) # 分
print(t[5]) # 秒
print(t[6]) # tm_wday=1 周几  ，周一是0  周二是1
print(t[7]) # tm_yday=40  一年的第几天
# print(t[0]) #

# 时间转换
#
# 1.时间戳转化为时间字符串
# 获取时间元祖
# 3600=1h 这里3600*24代表1天  也是一个时间戳
ret = time.localtime(3600*24)
# print(ret)
# 时间元祖->字符串时间
print(time.strftime("%Y-%m-%d ",ret))

# 2.时间元祖转为时间戳
print(time.localtime())  # 当前时间元祖
print(time.mktime(time.localtime()))  #时间戳


# asctime 里面参数是 时间元祖
print(time.asctime())  # Tue Feb  9 12:41:46 2021 默认格式 不需要输入 格式化的格式
# ctime 里面参数是  时间戳
print(time.ctime())     # Tue Feb  9 12:41:46 2021

# 卡十秒
# time.sleep(10)


# # 输入某年某月某日，判断这一天是这一年的第几天？
# # https://www.runoob.com/python/python-exercise-example4.html
year = input("year:>>")
month = input("month:>>")
day = input("day:>>")
# 将年月日 拼凑为 时间字符串形式
str_time = "-".join([year,month,day])
# 将字符串 转化为 时间元祖
structTime = time.strptime(str_time, "%Y-%m-%d")
# 根据时间元祖，得到该时间 是 这一年的第几天
print("这一天是这一年的第{}天".format(structTime[7]))

# 如果没有学time模块，则需要使用下列方法来判断

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print('it is the %dth day.' % sum)

