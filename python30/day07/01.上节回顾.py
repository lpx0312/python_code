#
'''
面向过程
面向对象

类是一个不存在的，是抽象出来的
类：类是具有相同属性和方法的抽象
对象：属性和方法


一个对象，可以属于 多个类

类和实例对象：
类的声明：
#类名建议首字母大写

# 类属性是所有对象都相同的属性
# 实例属性是 每个对象不一定相同的属性，eg 姓名和年龄
class 类名(object)：
    类属性 = 值

    def __init__(self,*args,**kwargs):
        实例属性 = 值
        pass





# 实例属性是单独开辟的空间
# 每个属性都自己单独开辟空间

'''

class Person(object):
    # 类属性
    # 类属性的私有化
    __legs_nums =  2   # 转换为  _Person__legs_nums存储

    yanjing = 2

    # 实例方法，判断标准就是是否有self
    # 其中 __init__ 是 一种 特殊的实例方法
    def __init__(self,name,age,gander):
        # 这里添加实例属性
        self.name = name
        self.age = age
        # 实例属性的私有化
        self.__gander = gander

    # 普通实例方法
    def foo(self):
        print('foo')

    # 静态方法：不需要使用到 有关对象的信息，也就不需要传入self
    @staticmethod
    def mul(x,y):
            return x*y

    # 类方法
    @classmethod
    def sleep(cls):
        print('类方法ID：{}'.format(id(cls)))


# 类名() ：类的实例化过程
zs = Person('lpx',18,'男')
# print(Person.legs_nums)
print(dir(Person))


# 实例对象查找变量的范围：【重点】
print(zs.name)
zs.yanjing = 4
# 实例对象不能改变类属性  【重点】
print(zs.yanjing)  # 4
print(Person.yanjing) # 2



# 一、实例方法
# 一般实例方法，是有 实例对象调用，
# 但是 类对象也可以调用实例方法
zs.foo()  # 实例对象 调用 实例方法时，则解释器会默认把 这个实例对象，当做self参数，传给实例方法

# 类对象调用实例方法 [不推荐]
# 类对象调用实例方法的时候，解释器不会引用self
# 这里是把 将 实例方法，当做 函数调用，需要自行传参数
Person.foo(Person)


# 二、静态方法
# 静态方法，本身就是 为了不需要使用到 对象而生的，故不推荐使用实例对象来调用
# 实例对象.静态方法()
# 类对象.静态方法()
zs.mul(2,3)  # 不推荐
Person.mul(2,3)  # 推荐

# 三、类方法
# 类对象.类方法()  # 推荐
# 实例对象.类方法()  # 不推荐

Person.sleep()   # ==》sleep的参数 cls 就是 Person这个类对象
print('Person ID:{}'.format(id(Person)))

zs.sleep()       # ==》这里的sleep的参数 cls是 zs实例对象的类对象对象。也就是Person，则cls 就是 Person
print(dir(zs))


## 私有属性
##  __name ==》解释器默认：将__name 变形为  __类名_name

## 私有方法
##