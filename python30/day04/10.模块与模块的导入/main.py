
# 方式1
# import cal
#
# cal.add()
# cal.mul()

# 方式2:

# def add():
# 	print("main add")
#
# from cal import add as a
# from cal import sub
#
# add()
# sub()
# a()

# 方式3: 不推荐

# from cal import *
#
# add()
# mul()


# 知识点2:  __name__ == '__main__'

# import cal
# import cal

# print("main __name__:",__name__)  # "__main__"
# print(type(__name__)) # <class 'str'>


import cal

if __name__ == '__main__':
    # 逻辑代码
    cal.add()
    # images.foo()




