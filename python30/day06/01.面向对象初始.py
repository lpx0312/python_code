




'''
面向对象的核心概念： 类  对象
类：是比函数更高级的一种代码组织形式，将数据与该数据相关的函数，组织在一起
  ：抽象的概念

对象：属性+方法


一个对象就是一块独立的内存空间

'''

### class 类名：
### 类名  首字母大写
class Car:
    # 类 属性
    lunzi = 4

    # 实例属性
    color = 'red'
    brand = '特斯拉'

    # 类 方法
    def running(self):
        print("高速运行")


car2  = Car()
print(car2.lunzi)


# 声明一个类
class Student:
    '''
    这是一个学生类
    '''
    banji = 's30'
    def study(self):
        '''
        :return:None
        '''
        print("学习")

# 构建类的实例对象  类名()
# 只有两个类型能调用，一个是函数 一个是类
s1 = Student() # 等同于 java语言的  new Student()，因为python是去关键字，所以省略了new关键字，所以效果完全等效
s1.name= "lpx"

# 查询
print(s1.banji)
s1.study()
print(s1.name)


s2 =  Student()
# 每个实例化的对象  都是不一样的  都有完全独立的两个空间
print("id1:",id(s1)) # 2524927406144
print("id2:",id(s2)) # 2524927406672