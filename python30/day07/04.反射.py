class Person:
    leg_nums = 2
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person('lpx',27,'male')

# 实例对象的反射：：
# while 1 :
#     attr = input('p1的属性：>>>')
#
#     # 反射取值
#     # 可以把根据  属性字符串  和 实例对象，获取对象属性
#     # getattr(p1,attr) 获取属性：如果有值，取出值，如果没有报错
#     # hasattr(p1,attr) 判断属性是否存在，存在返回True，不存在返回False
#
#     if   hasattr(p1,attr):
#         attrValue = getattr(p1,attr)
#         print(attrValue)
#     else :
#         print('输入的属性，不存在')
#         couse = input('是否添加该属性[y/n]')
#         if  couse =='y':
#             val = input('%s的属性值设置为>>>'.format(attr))
#             # 反射的属性
#             setattr(p1,attr,val)
#
#     # attrValue = getattr(p1,'name')


# 类对象的反射
print(getattr(Person, 'leg_nums'))
print(hasattr(Person, 'leg_nums'))
setattr(Person,'lll',120)
print(getattr(Person, 'lll'))
print(Person.lll)


# delattr(obj,name) 删除对象的属性


# 经典案例
# 方法也是一种属性：

class FTP(object):

    def __init__(self):
        self.run()

    # 启动方法
    def run(self):
        print('''
           提示:
               上传:   put 路径/文件名称    put meinv.jpg
               下载:   get 路径/文件名称
       '''
              )
        while 1:
            input_str = input(">>>")
            action, params = input_str.split(" ")
            if hasattr(self, action):
                # getattr(self, action) 获取方法属性，然后() 调用方法
                getattr(self, action)()
            else:
                print("不存在该方法")

    def put(self):
        print("上传...")

    def get(self):
        print("下载...")


ftp = FTP()
ftp.run()


# getattr 函数
# 获取对象属性后返回值可直接使用：
class A(object):
    def set(self, a, b):
        x = a
        a = b
        b = x
        print(a,b)

a = A()
c = getattr(a, 'set')
c(a='1', b='2')
