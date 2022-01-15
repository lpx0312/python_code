# 一切皆对象--》一切数据皆为对象

# 基本数据类型：  字符串  数字类型  布尔值
# 列表、字典、元组、集合、None 、字节串’‘

s = "hello world"
print(s.upper())

# 字符串s1也是一个实例化对象
s1 = str("hello world")   # 等价于 s = "hello world"
print(s1.upper())

# l = [11,22,33]
l = list([11,22,33])
l.append(44)
print(l)

# 类 也是需要开辟空间的，所以类也是一个对象  叫做类对象
# 通过类实例化创建的叫 实例对象


# # Person 也是一个对象，叫做类对象
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print("姓名:{},年龄:{}".format(self.name,self.age))
#
# # p 叫做 实例化对象
# p = Person("lpx",18)



class weapon:
    def __init__(self,name,av,color):
        self.name = name
        self.av = av
        self.color = color

jiguanqiang = weapon('激光枪',100,'red')

class Hero:
    def __init__(self,name,sex,hp,weapon,level=2,exp=2000,money=10000):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.weapon = weapon  # 武器


lpx = Hero('lpx','male',100,jiguanqiang)

print(lpx.weapon.name)






# 一切皆对象
s1 = 'hello'
s2 = 'hello'
s3 = 'hello 2'


# 理论上s1 s2，内存空间是不一样的，因为是不同的两个对象
# 但是python有个缓存，针对 字符串  数字   布尔值
# 会做内存优化，如果有相同的值的，不会再次开辟一个空间，
# 前提下是  同一作用域下
print(id(s1))   #2288371235632
print(id(s2))   #2288371235632
print(id(s3))   #2288373754032

a1 = 111
a2 = 111
a3 = 222
print(id(a1))   #140712545162336
print(id(a2))   #140712545162336
print(id(a3))   #140712545165888

f1 = True
f2 = False
f3 = True
print(id(f1))   #140712544880464
print(id(f2))   #140712544880496
print(id(f3))   #140712544880464











