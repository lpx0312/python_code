
# 斐波那契数列：[0,1,1,2,3,5,8,13,21,....]

class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b #这次结果作为下次的初始值
            self.n = self.n + 1
            return r
        raise StopIteration()


fib = Fib(5)

# while 1:
#     try:
#         print(fib.next())
#     except StopIteration:
#         break
# 如何支持for循环
# print(fib.__ iter__() == fib)

for i in fib:
    print(i)
# 迭代器不支持重复循环
# fib.__next__()
for i in fib:
    print(i)




# from collections import Iterable,Iterator
# # print(isinstance([1,2,3].__iter__(),Iterator))
# # print(isinstance(fib,Iterator))
# # python迭代器协议：对象类实现__iter__方法以及__next__方法就是迭代器对象
#
#
# # 迭代器应用
#
# f = open("test.py")
# print(isinstance(f,Iterable)) # True
#
# # f.read()
# for line in f:
#     print(line)







