# 生成器：参考 https://www.cnblogs.com/wj-1314/p/8490822.html
# https://blog.csdn.net/hedan2013/article/details/56293173
# https://www.cnblogs.com/chenhuabin/p/11288797.html
def bar():
    print('111')
    yield 123
    print('222')
    yield 234
    print('333')
    yield 345


print(bar)  # <function bar at 0x000002007EBD4EE0>
iter = bar()       # 并不是像函数返回，而是返回一个生成器对象，而且也不会执行函数里面的代码

# print(iter.__next__())      # 111   123
# print(iter.__next__())    # 222   234
# print(iter.__next__())    # 333   345

list


# 生成器应用

# 方式1：数量少的情况下
# def func1():
#     return ["url1","url2","url3"]
# for url in func1():
#     print(url)

# # 方式2：
# def func2():
#     yield 'url1'
#     yield 'url2'
#     yield 'url3'
#
# g = func2() # 获取生成器对象
#
# n = 0
# for url in g:
#     n+=1
#     if url == 'url2':
#         break
# print(n)
#
# # 作业：基于yield实现一个斐波那契额数列的生成器

def fib(index):
    n,a,b = 0,0,1
    yield 0  # 用来返回索引为0的值

    while n<index:
        yield b
        a,b = b,a+b
        n = n + 1


# g = fib(10)
for n in fib(0):
    print(n)


# g2 =  (i+1 for i in range(1000))
#- for i in g2:
#     print(i)


def add(s, x):
    return s + x


def gen():
    for i in range(4):
        yield i


base = gen()
# for n in [1, 10]:
#     base = (add(i, n) for i in base)

# print(list(base))


# print([add(i, 10) for i in [add(i, 10) for i in base]])

print(list(add(i, 10) for i in (add(i, 10) for i in base)))

