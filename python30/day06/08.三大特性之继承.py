# class Animal:什么都不继承默认是继承object
# 因为python3 可以默认，但是python不会默认，为了兼容性，
# 最好是加上object == class Animal(object):
class Animal(object):
    def eat(self):
        print('eating....')
    def sleep(self):
        print('sleeping....')

# 继承语法：class 类名(父类):
# 父类==基类==超类
#
class Cat(Animal):
    def climbtree(self):
        print('爬树')

class Dog(Animal):
    def swiming(self):
        print('游泳')

# 继承：解决代码重复的问题
a1 = Animal()
a1.eat()
a1.sleep()

c1 = Cat()
c1.eat()
c1.sleep()
c1.climbtree()

d1 = Dog()
d1.eat()
d1.sleep()
d1.swiming()
