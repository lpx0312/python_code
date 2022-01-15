# 生成器是一个特殊的迭代器，也是一个特殊的函数

# 普通函数
def foo():
    print("foo功能")
    return 123
# print(foo) # <function foo at 0x00000280DC621EA0>
# ret = foo()
# print(ret)

#生成器

# def bar():
#     print("111")
#     yield 123
#     print("222")
#     yield 234
#     print("333")
#     yield 345


# print(bar) # <function bar at 0x00000285C99D1EA0>
# print(bar()) # <generator object bar at 0x00000256A9CDA938>
# gen = bar()
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# 生成器应用
# 方式1
# def func1():
#
#     return ["url1","url2","url3"]
#
# for url in func1():
#     print(url)

# 方式2

def func2():
    yield "url1"
    yield "url2"
    yield "url3"

gen = func2()
# from collections import Iterable,Iterator
# print(isinstance(gen,Iterator))
for url in gen:
    print(url)
for url in gen:
    print(url)










