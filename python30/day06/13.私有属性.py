

# # 一、为什么要有私有的属性和方法
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# zhangsan = Student('zhangsan',66)
# lisi = Student('lisi',88)
#
# zhangsan.score = 100
# print(zhangsan.score)  # 100
# # 不安全,在外部可以取到数据，而且可以修改。


# # 二、私有方法属性的表示方法
# # 已双下划线开头的，就是代表私有的，和其他语言的 private类似
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name   # self.__name 就是变成了python的私有属性
#         self.score = score
# zhangsan = Student('zhangsan',66)
# lisi = Student('lisi',88)
#
# # 外部 就  取不到 这个属性了
# print(zhangsan.__name) # 报错
# # 现在不仅不能改了，而且还不能查，但是大部分情况都 是 不让改，但是可以查



# 三、

class Student(object):
    def __init__(self,name,score):
        self.__name = name   # self.__name 就是变成了python的私有属性
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self,value):
        # 为什么既让查  又让改，为什么还要私有化，
        # 因为可以在这个内部，判断什么时候让改，什么时候让查
        # 或者  isinstance(value,int)
        if type(value) == int  and value > 0 and value < 100 :
            self.__score = value
        else:
            raise  ValueError('设置分数不合法')# python主动抛错



zhangsan = Student('zhangsan',66)

# print(zhangsan.get_score())
# zhangsan.set_score(88)
# print(zhangsan.get_score())
zhangsan.set_score(88)
print(zhangsan.get_score())


# ['_Student__name', '_Student__score', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_score', 'set_score']
# # 其中 '_Student__name', '_Student__score'
# # 私有化的实质：面试常考
# # self.__name 私有化过程其实就是 把__name 改成了_Student__score
# # 所以外部就 找不到__name了，但是依旧可以查到  zhangsan._Student__score
# #
print(dir(zhangsan))
print(zhangsan._Student__score)
zhangsan._Student__score = 10000
print(zhangsan.get_score())

