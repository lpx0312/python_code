
'''
高阶函数：
    1.函数作为参数的函数（形参为函数的函数）
    2.返回值为函数的函数
满足其一就成为 高阶函数
'''


# # 一切皆数据，函数亦是变量
# # 特别注意:
# # 定义一个foo函数，foo变量指向函数体的内存空间
def foo():
    print("foo")
print(callable(foo)) # True callable 查看变量是否能被调用，也就意味着这个变量是否是函数，
foo = 100 # foo有赋值了，100开辟一个空间，foo变量又指向了100，则函数体的指向就小时了
# print(callable(foo)) #False
# # print(foo())  # 所以是  调用的是 100() 会报错



# 形参为函数的函数
# def  bar():
#     print("bar")
# def foo():
#     print("foo")
# def func(f):
#     f()
# func(bar)

# 案例：计时案例
import  time

def  bar():
    time.sleep(3) # 因为执行太快，所以加个2s 来显示
    print("bar功能")

def foo():
    time.sleep(2) # 因为执行太快，所以加个2s 来显示
    print("foo功能")

# 专门测 功能的运行时间
# 不用再每个函数中写这个功能
def timer(f):
    start = time.time()
    f()
    end = time.time()
    print("花费时间",end-start)

timer(foo)


# 计算每个功能的运算时间



# 返回值为函数的函数
