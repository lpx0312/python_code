
# 浮点型：
# python中的小数有两种书写形式
#1.十进制形式
f1 = 3.14
print(f1)
print(type(f1)) #<class 'float'>

#2.指数形式
f2 = 3e2   #等同于3*10^2 = 300.0
print(f2)   #因为指数型也是浮点型，所以后面必须有小数点
print(type(f2))

f3 = 3e-2   # 等同于 3*1/(10^2)
print(f3)
print(type(f3))