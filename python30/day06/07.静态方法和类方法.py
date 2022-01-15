

# # 一、
# # 对于计算器这种类，根本用不到self这个类的属性，所以现在想取消self这个参数
# class Cal:
#     def add(self,x,y):
#         return x+y
#     def mul(self,x,y):
#         return x*y
#
# cal = Cal()
# ret = cal.add(2,3)
# print(ret)


# # 二、
# # 这样不加self，但是会报错
# # 因为self只是一个形参，可以是任何名字，
# # 所以这里x默认充当了x的角色
# class Cal:
#     def add(x,y):
#         return x+y
#     def mul(x,y):
#         return x*y
#
# cal = Cal()
# ret = cal.add(2,3) # 2 变成了self的参数
# print(ret)

# # 三、
# # 静态方法的创建：加 @staticmethod装饰器
# class Cal:
#
#     # 加个@staticmethod装饰器，就是告诉解释器，不要穿self
#     @staticmethod
#     def add(x,y):
#         return x+y
#
#
#     @staticmethod
#     def mul(x,y):
#         return x*y
#
# # 实例对象调用静态方法
# cal = Cal()
# ret = cal.add(2,3)
# print(ret)
#
#
# # 类方法调用静态方法
# # 不需要在传入  对象，因为静态方法本身就取消了self参数
# print(Cal.add(3, 4))


# # 四、
# # 现在的需求，调用add_cls_number方法，让Student的类属性class_number的数量+1
# class Student:
#
#     # 类属性
#     class_number = 68
#
#     # 实例方法
#     def add_cls_number(self):
#         self.class_number+=1
#         print(self.class_number)
#
#
# s1 =  Student()
# print('s1.class_number:::{}'.format(s1.class_number))
# # 分析，s1这个实例对象调用.add_cls_number方法，其中self就是s1，s1和Student是不同对象，不同的存储空间。相当于
# '''
#     def add_cls_number(s1):
#         s1.class_number+=1      # 因为s1实例对象是Student创建的，也有class_number属性，则这里就把s1.class_number进行+1，并没有影响Student类中的class_number属性
#         print(s1.class_number)
# '''
# s1.add_cls_number()
# # 结论：实例对象 修改不了 类属性
# print('s1.class_number:::{}'.format(s1.class_number))
# print('Student.class_number:::{}'.format(Student.class_number))


# 五、
class Student:

    # 类属性
    class_number = 68

    # 类方法
    @classmethod
    # 和实例对象的self类似，cls代表类对象，而且和self一样，也是默认隐藏的
    def add_cls_number(cls):
        print('cls  ID:::{}'.format(id(cls)))
        # cls：当前类对象
        cls.class_number+=1
        print(cls.class_number)


# 调用add_cls_number方法，因为该方法是 @classmethod装饰的类方法
# 所以调用的时候，Student.add_cls_number()==》把Student类对象传递给了cls==>
# cls.class_number+=1 ==>Student.class_number+=1  所以这里直接更改了类属性
Student.add_cls_number()
print('Student ID:::{}'.format(id(Student)))
print('Student.class_number:::{}'.format(Student.class_number))
# 类对象调用类方法，进而更改了 类属性


