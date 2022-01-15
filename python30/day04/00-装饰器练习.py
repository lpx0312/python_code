# 不带返回值得装饰器，通用写法




# def fly(func):
#     def inner(*args,**kwargs):
#         print('函数之前添加 ++++ 飞')
#         ret = func(*args,**kwargs)
#         print('函数之前添加 ++++ 睡')
#         return ret
#     return inner
#
#
#
# @fly
# def person(jineng):
#     print(jineng)
#
# person(jineng="chi")



def log(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        print("{}被执行了".format(func.__name__))
        return  ret
    return  inner

@log
def wahaha():
    pass
@log
def qqxing():
    pass

wahaha()
qqxing()


def log(func):
    def inner(*args,**kwargs):
        print('添加日志模块前')
        ret =  func(*args,**kwargs)
        print('添加日志模块后')
        return  ret
    return inner
def login(func):
    def inner(*args,**kwargs):
        print('login模块前')
        ret =  func(*args,**kwargs)
        print('login模块后')
        return  ret
    return inner

@login
@log
def func():
    print('func------')

func()
'''
login模块前
添加日志模块前
func------
添加日志模块后
login模块后
'''

# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。

values = [11, 22, 33,44,55,66,77,88,99,90]
l1 = [ i for i in values if i>66]
l2 = [ i for i in values if i<66]

values = [11, 22, 33,44,55,66,77,88,99,90]

from collections import defaultdict

dic=defaultdict(list)

for i in values:
    if i>66:
        dic['bigger than 66'].append(i)
    elif i<66:
        dic['smaller than 66'].append(i)
print(dic) # defaultdict(<class 'list'>是整个类型的
print(dict(dic))  # 得到结果后，需要将其转化为正常的dict类型


import random
import string
string.digits

def checkcode(num,alpha=True):
    l=[]
    ret = string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation  if alpha else string.digits+string.punctuation
    for i in range(num):
       l.append(random.choice(ret))
    return ''.join(l)
print(checkcode(6,False))

def send_bag(money,n):
    money *= 100
    ret = random.sample(range(1,money),n-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    l=[]
    for i in range(len(ret)-1):
        cha = ret[i+1]-ret[i]
        val = cha/100
        l.append(val)
    return  l
lst = send_bag(10,5)
print(lst)