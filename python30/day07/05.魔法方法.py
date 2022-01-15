# # 1.初始化方法 和构造方法
# # __init__
# class Animal(object):
#     # 开辟内存空间,如果不写，解释器会默认执行，一般最不要重写
#     # 除了特殊情况eg单例，
#     def __new__(cls, *args, **kwargs):
#         # 开辟空间
#         print('构造方法')
#         obj = super().__new__(cls)
#         print(id(obj))
#         return  obj
#
#     def __init__(self,name):
#         print(id(self))
#         print('初始化方法')
#         self.name = name
#
# a1 = Animal('dog')
# #如果重写__new__ 啥也没写，则不会开辟内存空间，会报错
# # AttributeError: 'NoneType' object has no attribute 'name'
# print(a1.name)


# # 二.__str__
# # 打印时 被调用
# class C(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     # print(对象)时 显示的内容
#     # <__main__.C object at 0x000001B0A3FFB160>
#     # 设置的后，print(对象)==> 姓名：lpx ,年龄:18
#     def __str__(self):
#         #返回一定字符串
#         return "姓名：{} ,年龄:{}".format(self.name,self.age)
#
# lpx = C('lpx',18)
# zj = C('zj',20)
# print(lpx)
# print(zj)
# print(dir(lpx))

# # 三、析构方法
# class F(object):
#     def __del__(self):
#         print('删除对象时调用')
#
# import time
# f = F()     # 必须创建对象开辟空间，因为如果不开辟空间的话，根本就不会删除对象或者说销毁空间的
# # python 默认是在程序结束的时候 才会删除对象或者说  清理空间
# time.sleep(100)
# # 只有在100s后才会默认执行 __del__方法来删除对象
# # 所以为什么要讲析构方法 __del__呢？
# # 因为有的时候，我们不想等到程序结束在删除对象，
# # 如果子sleep前手动del f对象
# # del f  可以在删除的时候  直接调用__del__方法

# class  Filehandle(object):
#     file = 'a.txt'
#     # 初始化的时候 进行打开文件
#     def __init__(self):
#         self.f = open(self.file)
#
#     # 在程序结束的时候 关闭打开的文件
#     # 或者手动删除  实例对象的时候  关闭打开的文件
#     def __del__(self):
#         print('关闭已打开的文件')
#         self.f.close()
#
# fh = Filehandle()
# print(fh.f.read())


# # 四、item的魔法方法
# class G(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     # 在使用  实例对象['属性名']  时 调用  eg：g['name']
#     def __getitem__(self, item):
#         print('__getitem__被调用')
#         if hasattr(self,item):
#             return getattr(self,item)
#         else:
#             print("属性值不存在")
#
#     # 在给 实例对象['属性名'] =  value 时 调用， eg ： g['name'] = 'lll'
#     def __setitem__(self, key, value):
#         print('__setitem__被调用')
#         if hasattr(self,key):
#             setattr(self,key,value)
#         else:
#             print('属性不存在 不能更改')
#
#     # 在删除 del 实例对象['属性名'] 时 调用 ，eg ： del g['name']
#     def __delitem__(self, key):
#         delattr(self,key)
#         print('__delitem__被调用')

# # g["name"]这种方式取值，如果不写 getitem 等方法是不能使用的
# # g = G('lpx',22)
# # print('g["name"]:::{}'.format(g['name']))
# # g['name'] = 'lll'
# # print('g["name"]:::{}'.format(g['name']))
# # del g['name']
# # print('g["name"]:::{}'.format(g['name']))



# 五 属性的魔法方法












# 五 属性的魔法方法

# 5.1 __getattribute__和__getattr__使用情况说明

# 第一种：如果属性本身在实例对象中存在
# 只调用__getattribute__方法（属性访问拦截器）;

# 第二种：如果属性本身不存在，
# 还是优先调用__getattribute__，因为属性不存在，则程序直接报错，如果重写了__getattr__方法，则会直接在调用__getattr__，

##### 重点不管是__getattribute__还是__getattr__ 方法，
##### 其内部如果存在 self.属性名 或者self.方法名() 获取属性或方法，都会出现无限递归错误，#####
## 报错案例：https://blog.csdn.net/yitiaodashu/article/details/78974596
## 参考2： https://www.cnblogs.com/yimai-series/p/12124620.html

class ClassA(object):

    def __init__(self, classname,shuxing):
        self.classname = classname
        self.shuxing = shuxing

    def __getattr__(self, attr):
        print('{}属性不存在'.format(attr))
        # return  None


    # 1.不管什么属性，先在__getattribute__里面找，找不到再到__getattr__里面找，
    # 2.如果不写__getattr__方法，如果找不到属性，也就会直接报错，所以object.__getattribute__(self, attr)什么都不会返回
    #  如果写了__getattr_方法，就会再去__getattr__方法里面去找。，
    def __getattribute__(self, attr):
        #拦截shuxing属性
        if attr == 'shuxing':
            return  'shuxing不可被访问'
        print('attr ： {}  Action：__getattribute__'.format(attr))
        return object.__getattribute__(self, attr)
        # return  self.__dict__[attr]  # 不能使用这一种 会报错





insA = ClassA('num1','age')
print("result:{}".format(insA.__dict__))
# 执行结果:
# # attr ： __dict__  Action：__getattribute__
# result:{'classname': 'num1', 'shuxing': 'age'}

# 属性存在  -> 直接 执行 __getattribute__ 方法
print("result:{}".format(insA.classname))
# attr ： classname  Action：__getattribute__
# result:num1

# 属性不存在；-> 1.也是先执行__getattribute__， 2.如果__getattribute__没有找到，也就是返回的是None
print("result:{}".format(insA.graden))
# attr ： graden  Action：__getattribute__

print(insA.shuxing)
# shuxing不可被访问


# # 5.2 __setattr__ 属性赋值拦截器
# # 原理：__setattr__()在属性赋值时被调用，并且将值存储到实例字典中，这个字典应该是self的__dict__属性。
# #  即：在类实例的每个属性进行赋值时，都会首先调用__setattr__()方法，并在__setattr__()方法中将属性名和属性值添加到类实例的__dict__属性中。
# # 参考：https://zhuanlan.zhihu.com/p/101004827?from_voters_page=true
# # 重点看最后例子：https://www.cnblogs.com/huchong/p/8287799.html
class Fun(object):
    def __init__(self):
        self.name = "Liu"
        self.age = 12
        self.male = True

    def __setattr__(self, key, value):
        # 这里还可以 做 添加键值对的日志处理
        print("*" * 50)
        print("setting:{},  with:{}".format(key, value))
        print("current __dict__ : {}".format(self.__dict__))
        # 属性注册,如果不注册，则赋值也就没有成功
        self.__dict__[key] = value
        # 效果同上，建议使用上面，因为super啥的有可能引起无限递归错误
        # super(Fun, self).__setattr__(key,value)
        # python3 super()等价于super(Fun, self)，为了监控，最好还是使用super(Fun, self)

    # del fun.name的时候调用
    def __delattr__(self, item):
        print('__delattr__被调用')

fun = Fun()
del fun.name



