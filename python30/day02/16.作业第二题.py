
# 假设有下面这样的列表：
# names = [‘baicai’,‘zhurou’,‘fentiao’,‘fish’]
# 输出的结果为：‘I have baicai,zhurou,fentiao and fish’

names = ['baicai','zhurou','fentiao','fish']

print('I have %s,%s,%s and %s'%(names[0],names[1],names[2],names[3]))

# 重点：拓展 *列表
print('I have {},{},{} and {}'.format(*names))
print(*names)


# 重点：拓展 *字典
# 假设有下面这样的字典
# person = {"name":"lpx","age":25,"height":"180cm"}
# 输出结果为：'My name is lpx, 25 years old, 180 cm tall '

person = {"name":"lpx","age":25,"height":"180cm"}
print('My name is lpx, 25 years old, 180 cm tall'.format(*person))



