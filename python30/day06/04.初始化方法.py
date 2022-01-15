

# # 一、先构建对象在属性赋值
#
# # 声明一个类
# class Student:
#     '''
#
#     '''
#     banji = 's30'
#
#
#     def study(self):
#         print("学习")
#
#
# s1 =  Student()
# s1.name = "li"
# s1.age = 18
# s1.ID = 123
#
# s2 = Student()


# 二、初始化方式赋值属性

class Student:
    '''
    这是一个学生类
    '''
    # __init__ 这个初始化方法，是解释器自动调用，
    def __init__(self,name,age,ID):
        '''
        Student类的初始化方法
        :param name:  姓名
        :param age: 年龄
        :param ID: 学号
        '''
        self.name  =  name
        self.age = age
        self.ID = ID

    # 实例方法
    def stuy(self):
        print('学习')

s1  =  Student(name="lpx",age = 18,ID=10010)
print(s1.name)  # lpx
#  Student()执行流程：
# 1.使用类中的__new__方法开辟内存空间，
# 2.然后再调用__init__方法，__init__方法的self就是new开辟的空间地址


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print("姓名:{},年龄:{}".format(self.name,self.age))


p1 = Person("lpx",18)
p1.print_info()