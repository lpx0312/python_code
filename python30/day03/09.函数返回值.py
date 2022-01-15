
# 函数调用 ：返回值 = 函数名（参数）
#
def add(x,y):
    return x+y  # 函数结束语句
    # print("OK") # 不会执行
ret = add(12,4)
print(ret)

# 2.return 任何函数都有一个返回值
def add2 (x,y):
    print(x+y)
    # return  None 不写 默认返回 None
add2(2,3)

# 3.返回多个值:使用元祖
def foo():
    return 100,200,300
# print(foo()) # (100, 200)

# a,b = foo()  # 分别接收
# print(a,b)

a,*b = foo() # 使用* 接收
print(a)    # 100
print(b)    # [200, 300]


