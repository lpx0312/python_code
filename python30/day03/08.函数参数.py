
# 一、按位置传参
# def add(x,y,z):
#     print(x)
#     print(y)
#     print(x+y)
# # add(5,3) # python会报错，add() missing 1 required positional argument: 'z'  形参与实参 数量不对
#
# def add(x,y):
#     print(x)
#     print(y)
#     print(x+y)
# add(5,3)


# # 二、关键字传参(精确，不跟位置相关，实参)
# def print_stu(name,age,height):
#     print("name",name)
#     print("age",age)
#     print("height",height)
# print_stu(name="lpx",age=26,height="173cm")
# # 混合传参时，关键字参数必须位于所有的位置参数之后
# # print_stu("lpx",age=26,height="173cm") #正确
# # print_stu(age=26,"lpx",height="173cm") # 报错


# # 三、默认参数
# # 形参上设置默认值，如果实参不传这个参数，就用默认的
# def print_stu(name,age,gender="man"):
#     print("name",name)
#     print("age",age)
#     print("gender",gender)
# # 班里男生多，只有女生的时候才传gender这个参数
# print_stu("韩框框",23,"woman")
# print_stu("alive",22)


# 四、不定长参数 ：
# *args（位置参数，接受位置实参赋值给args变量，其中args可以是任意名字，可以是*b）
# *args：将所有参数打包成 元祖 赋值给变量args
# **kwargs(关键字参数，接受关键字实参赋值给kwargs，其中kwargs可以是任意名字，可是**b)
# *kwargs：将所有参数打包成 字典 赋值给变量kwargs
# def add(x,y,z):
#     print(x+y)
# # add(5,3,2) 报错def add(x,y,z):

# # *args就是位置不定长参数，
# # 它把add传入的参数，打包成一个元祖，赋值给args变量
# def add(*args):
#     print(args)         # (5, 3, 4, 6)
#     print(type(args))   # <class 'tuple'>
#     num = 0
#     for i in args:
#         num += i
#     return num
# print(add(5, 3, 4, 6))


# # **kwargs 是关键字不定长参数，
# def print_stu(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key,value)
#
# print_stu(name="alvin",age=25,height="180cm")
# print_stu(name="alvin",age=25)

# # 其中name,age是这个函数必须要的参数
# # args和kwargs都是可有可没有的参数
# # args接受位置参数
# # kwargs接受关键字参数
# # 条件：必须要的参数name，age在最前面，
# # *args 位置参数写在 第二
# # **kwargs 关键字参数写在 最后
def foo(name,age,*args,**kwargs):
    print(name)
    print(age)
    print("args",args)
    print("kwargs",kwargs)

foo("li",23,"male",height="180cm")
# '''
# li
# args (23, 'male')
# kwargs {'height': '180cm'}
# '''


# # 五、值传递和引用传递【有点问题】
# # 传参的过程 == 变量赋值的过程
# # 比如下面：foo(a)相当于 将外面的a赋值给里面的a，  相当于 里面a=外面a 这就是相当于 两个a 指向了同一块内存空间
# # 类似 b=a 一样，  a b指向的内存空间是一样的
# def foo(a):
#     print("里面的a1：",id(a))#140712431391488
#     a = 10                  # 因为a是不可变类型，重新赋值，就是需要重新开辟一块内存空间，
#     print("里面的a2：",id(a))#140712431391488
# a = 100
# print("外面的a：",id(a)) # 140712431388608
# foo(a)
# print(a) # 100


# a=10
# b=a
# print(id(a)) # 140712383023040
# print(id(b)) # 140712383023040
# a=200
# print(id(a)) # 140712383029120
# print(id(b)) # 140712383023040



# def foo(x):
#     print("x1",id(x)) # 2335020207488
# # 因为x是列表是可变类型，更改里面的值的时候，并不会重新开辟内存空间，
# # 所以x更改了，而且x a指向同一块内存空间，则a也改变了
#     x.append(4)
#     print("x1",id(x)) # 2335020207488
#
# a = [1,2,3]
# print("a:",id(a))  # 2335020207488
# foo(a)      # 将a赋值给x，x=a 则a x 指向同一块内存空间
# print(a)    # [1, 2, 3, 4]

