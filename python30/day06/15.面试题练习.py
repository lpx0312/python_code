# 第一题：
# class A(object):
#     x = 100
#     def foo(self):
#         print(self.x)
#
# class B(A):
#     x = 10
#     def __init__(self,x):
#         self.x =  x
#
#     def bar(self):
#         print(self.x)
#
# b = B(1)
# # b 调用了 父类的foo，所以父类中foo(self)，b调用了这个实例方法，所以这个self就是b，
# # print(self.x) ==》 print(b.x)
# b.foo()       # 1

#
# # 第二题：
# # __init__ 跟普通函数一样，也会被继承
# class A(object):
#
#     def __init__(self,x):
#         self.x=x
#
#     x=100
#
#     def foo(self):
#         self.bar()
#
#     def bar(self):
#         print("x", self.x)
#
# class B(A):
#     X=10
#     def bar(self):
#         print(self.x)
#
# b = B(1)
# b.foo()  # 1


# # # 第三题
# # 不用其他变量，交换两个变量
# a = 10
# b = 100
# print('a={},b={}'.format(a,b))
# # 方式一：经典，使用所有语言
# # a = a - b
# # b = a + b
# # a = b - a
# # 方式二：不太懂
# # a, b = b, a
# # 方式三：不太懂
# a = a ^ b
# b = a ^ b
# a = a ^ b
#
# print('a={},b={}'.format(a,b))


# # # 第四题：和原来不一样，不建议详看，有问题
# a, b, c, d = 1, 1, 1000, 1000
# print(a is b, c is d)
#
# def foo():
#     e = 1000
#     f = 1000
#     print(e is f, e is d)
#     g = 1
#     print(g is a)
#
# foo()
#
# # True True
# # True True
# # True
#
# # Linux中python2执行的结果
# # (True, True)
# # (True, False)
# # True