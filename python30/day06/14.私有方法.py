
class Animal(object):
    def eat(self):
        print('eating....')
    def __sleep(self):        # 方法存储名：_Animal__sleep
        print('父类slee....')
    # 第二种：c1.test()=>self._Animal__sleep()=>打印 父类sleep
    def test(self):
        self.__sleep()        # 变形操作：self._Animal__sleep

class Cat(Animal):

    def __sleep(self):      # 方法存储名：_Cat__sleep
        print('子类sleep')
    # # 第一种：c1.test()=》self._Cat__sleep()=> 打印 子类sleep
    # def test(self):
    #     self.__sleep() # 变形操作：self._Cat__sleep



c1 = Cat()
# c1.__sleep()
print(dir(c1))
c1.test()


# 结论 ： 在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的:

