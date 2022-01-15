
class Animal(object):
    def eat(self):
        print('eating....')
    def sleep(self):
        # 假设这里有100行代码
        print('sleeping....父类方法')

class Cat(Animal):
    def climbtree(self):
        print('爬树')

    def sleep(self):
        '''
        父类方法的重写
        '''
        if  True :
            print('条件成立，满足睡觉条件')
            # 执行父类方法的语法。。。。重点
            # # 方式一:写死了父类名，如果父类名改了，这里就用不了了，
            # # 不建议
            # Animal.sleep(self) # 类调用实例方法，必须传入参数，解释器不会自动传参
            # 方式二：
            # 关键字super代表父类,super()代表的是 父类对象，也相当于实例对象，所以就不用传self
            # 推荐
            # super()相当于 Animal() 是Animal的实例对象，然后在sleep() 就不用传self了
            super().sleep()
            print('自己的方法')

class Dog(Animal):
    def swiming(self):
        print('游泳')


c1 = Cat()
c1.eat()
c1.sleep()
