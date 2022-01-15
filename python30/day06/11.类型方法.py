#
# class Animal(object):
#     def eat(self):
#         print('eating....')
#     def sleep(self):
#         print('sleeping...')
#
# class Dog(Animal):
#     def swiming(self):
#         print('游泳')
#
#
# a1 = Animal()
# d1 = Dog()
# d2 = Dog()
#
# # isinstance(实例对象,类名)
# # 判断实例对象是不是这个类中的实例
# # isinstance 会判断父类
# print(isinstance(a1,Animal)) # True
# print(isinstance(a1,Dog)) # False
# print(isinstance(d1,Animal)) # True
# print(isinstance(d1,Dog)) # True
#
# # type 查看实例对象的 类型
# print(type(d1)) # <class '__main__.Dog'>
# print(type(a1)) # <class '__main__.Animal'>
#
# # 判断两个实例对象 是不是 来自于 同一个类 实例化出来的
# # type 不会判断 父类
# print(type(a1) == type(d1)) # False
# print(type(d1) == type(d2)) # True
#
#
#
#
#
