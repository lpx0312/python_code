
class Animal(object):
    def eat(self):
        print('eating....')
    def sleep(self):
        print('sleeping...')

class Cat(Animal):
    def climbtree(self):
        print('爬树')

class Dog(Animal):
    def swiming(self):
        print('游泳')


# 类似于 接口
class  Fly:
    def fly(self):
        print('fly......')

# 蝙蝠
class Bat(Animal,Fly):
    pass

# 燕子
class YanZi(Animal,Fly):
    pass

# 麻雀
class MaQue(Animal,Fly):
    pass

# C3法则：用来优先查找 哪个父类
# 后续详解


b1 = Bat()


