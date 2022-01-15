import  datetime

# date 类型   年月日
ret = datetime.date(2020,12,3)
print(ret)
print(type(ret))

print(ret.year)
print(ret.month)
print(ret.day)


# time类型   年月日
ret1 = datetime.time(9,44)
print(ret1)
print(type(ret1))
print(ret1.hour)
print(ret1.minute)
print(ret1.second)


# datetime类型  年月日  时分秒 都有
# 最重要
ret2 = datetime.datetime(2020,12,3)
print(ret2)
print(type(ret2))
print(ret2.year)

now  =  datetime.datetime.now()
print(now)  # 2021-02-13 09:48:08.179408
print(now.strftime("%Y-%m-%d %X"))  # 2021-02-13 09:50:30


# 四 timedelta
delta  =  datetime.timedelta(days=3)
print(now + delta)
print((now + delta).strftime("%Y-%m-%d %X"))