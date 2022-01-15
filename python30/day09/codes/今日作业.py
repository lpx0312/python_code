# 作业： 基于yield语法实现一个斐波那契数列的生成器

# from collections.abc import Iterator,Iterable,Generator
#
# class Fib(object):
#     def __init__(self,max):
#         self.n = 0
#         self.a = 0
#         self.b = 1
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.n  < self.max:
#             r = self.b
#             self.a ,self.b = self.b ,self.a+self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# fib = Fib(10)
# print(fib)
# print(isinstance(fib, Iterable)) # True 是迭代对象 ，但是不是没有__next__方法不是迭代器
# print(isinstance(fib, Iterator)) # True 加了__next__方法 就是迭代器对象了
# print(isinstance(fib,Generator)) # False 不是生成器
# print(next(fib))

def fib(max):
    n,a,b = 0,0,1
    yield 0
    while n < max -1:
        num = b
        a ,b = b,a+b
        yield num
        n+=1
    return 'done'

f  = fib(3)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for i in f:
    print(i)