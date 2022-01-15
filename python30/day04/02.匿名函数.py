#!/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# def foo(x,y):
#     return x+y
#
# # python的匿名函数:
# # 调用一次，直接销毁，因为没有变量名，没有开辟空间
# # 格式：lambda  参数：函数体
# (lambda  x,y:x+y)(12,4)
#
# # 下面用法和foo没有区别 都一直有 变量指向函数所在空间，使用依次依旧不会销毁
# bar = lambda x,y:x+y
# print(bar(23.4))

# filter()函数用于 过滤序列，过滤不符合条件的序列
# 语法：filter(function,iterable)
# filter函数将返回一个list，但与map不同的是，filter函数只能有一个iterable作为输入
# 返回值：最后将判断函数返回True的元素放到新列表中

def foo2(x):
    return  x % 2 == 0

a = (1,2,3,4,5,6)

print(list(filter(foo2,a)))
print(list(filter(lambda x:x % 2 == 0,a)))

# map() 函数根据提供的函数对指定序列做映射
# 对列表做 统一操作
a = (1,2,3,4,5,6)
print(list(map(lambda x: x + 2, a)))l
# print(list(map(lambda x: x**2, a)))
# # 两个变量（多个iterable）操作【重点】
# print(list(map(lambda x, y: x + y, [1, 3, 5, 7], [2, 4, 6, 8, 10])))
#
# print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# #
# #
# # # reduce()函数对参数序列中的元素进行累积
# # # 语法
# #
# from functools import  reduce
#
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
#
#
#
#
