# """
# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码）
# 要求只要登录成功一次，后续的函数都无需输入用户名和密码
# """


# # 第一种方法，不太好
# user = "lpx"
# mima = "lipanxiang"
# user1 = "lpx"
# mima1 = "lipanxiang"
# flag = False
#
# def renzheng(func):
#     def wrapper():
#         # 不加global 会报错 local variable 'flag' referenced before assignment
#         # python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，对该变量的引用自然就会出现没定义这样的错误了。
#         global flag
#         # print(flag)
#         if flag == True:
#             func()
#         else:
#             if user1 == user and mima1 == mima :
#                 flag = True
#                 print("账号密码输入正确")
#                 func()
#             else:
#                 print('账号和密码错误')
#     return  wrapper
# @renzheng
# def haha():
#     print("haha")
# haha()


# 方法二  推荐，使用字典可变类型来存储，不会报错local variable  referenced before assignment
# 使用字典来存储是否登录成功
cert_dict = {}
def cert(func):
    def wapper(*args,**kwargs):
        if cert_dict.get('status',False):
            print("{}:[{}]认证成功，已自动登录".format(func.__name__,cert_dict['user']))
        else:
            user,passwd = input("{} user>>>".format(func.__name__)).strip(),input("{}passwd>>>".format(func.__name__)).strip()
            if user.lower() == "lpx" and passwd.lower() == "123":
                cert_dict['user'] = user
                cert_dict['passwd'] = passwd
                cert_dict['status'] = True
                return func(*args,**kwargs)
            else:
                print('认证失败，无法修饰')
    return wapper

@cert
def first():
    print("first认证")

@cert
def second():
    print('second认证')

@cert
def three():
    print('three认证')


first()
second()
three()
