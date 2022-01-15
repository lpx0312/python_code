# import time
#
#
# def consumer(name):
#     print("%s 准备学习啦!" % name)
#     while True:
#         lesson = yield
#
#         print("开始[%s]了,[%s]老师来讲课了!" % (lesson, name))
#
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     print(c.__next__())
#     print(c2.__next__())
#     print("同学们开始上课了!")
#     for i in range(3):
#         time.sleep(1)
#         print("到了两个同学!")
#         c.send(i)
#         c2.send(i)
#
# producer('h')
#
# # def hah(name):
# #     print("%s 准备学习啦!" % name)
# #     yield 1
# #
# # c = consumer('A')
# # c.__next__()



from collections.abc import Iterable,Iterator,Generator
#
# # 判断可迭代对象：Iterable（有__iter__方法)
print(isinstance([], Iterable)) # True
# print(isinstance({}, Iterable)) # True
# print(isinstance('abc', Iterable))  # True
# print(isinstance((x for x in range(10)), Iterable)) # True
# print(isinstance(100, Iterable))    # True
#
# # 判断可迭代器对象：Iterator（有__iter__和__next__方法)
# print(isinstance([], Iterator)) # False
# print(isinstance({}, Iterator)) # False
# print(isinstance('abc', Iterator))  # False
# print(isinstance((x for x in range(10)), Iterator)) # False
#
# g = ( i for i in range(5))
# print(g)
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())



class Fib(object):
    def __init__(self,max):
        self.n = 0
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):

        if self.n  < self.max:
            r = self.b
            self.a ,self.b = self.b ,self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

fib = Fib(10)
print(fib)
print(isinstance(fib, Iterable)) # True 是迭代对象 ，但是不是没有__next__方法不是迭代器
print(isinstance(fib, Iterator)) # True 加了__next__方法 就是迭代器对象了
print(isinstance(fib,Generator)) # False 不是生成器
print(next(fib))
# for i in fib:
#     print(i)
# print(len(fib)) # 迭代器也不能使用len


# # 这也就是为什么 列表不是一个 迭代器，但是能使用for循环的原因
# # for 循环本质:
# li  =  [1,2,3,4]
# list_iterator = li.__iter__()
# # <list_iterator object at 0x000001CA95E95AC0>  这里是list_iterator列表迭代器
# # 因为list本身不是迭代器，因为list中只有__iter__方法，只是迭代对象，并不是迭代器，但是却能调用__iter__方法，并返回一个list_iterator列表迭代器，
# # 后再经过循环，调用list_iterator.__next__方法，也就是next(list_iterator)得到里面的值。
# # 这也就是for循环的本质
# print(list_iterator)
# while 1:
#     try:
#         print(next(list_iterator))
#     except StopIteration:
#         break
#
# # for循环本质：需要循环的对象，必须是迭代对象，然后调用迭代对象的__iter__方法，
# # 后再循环调用__next__方法
# # 换句话说就是，能for循环的对象，要么是 迭代器对象（有__iter__和__next__方法），因为调用__iter__后返回的还是自己，且自己也是一个迭代器对象
# #                           要么就是 迭代对象，且调用__iter__方法后，返回的是迭代器对象，并不是本身




# from collections.abc import Iterator
# class A():
#     def __iter__(self):
#         print('A类的__iter__()方法被调用')
#
# class B():
#     def __iter__(self):
#         print('B类的__iter__()方法被调用')
#         return self
#     def __next__(self):
#         pass
# a = A()
# print('对A类对象调用iter()方法前，a是迭代器吗：', isinstance(a, Iterator))
# a1 = iter(a)   #使用iter方法调用，如果返回的不是 迭代器就会报错ter() returned non-iterator 但是__iter__()不会报错
# # a.__iter__()
# print('对A类对象调用iter()方法后，a1是迭代器吗：', isinstance(a1, Iterator))
#
# b = B()
# print('对B类对象调用iter()方法前，b是迭代器吗：', isinstance(b, Iterator))
# b1 = iter(b)
# print('对B类对象调用iter()方法后，b1是迭代器吗：', isinstance(b1, Iterator))




