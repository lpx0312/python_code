

class Person:
    # 类 属性（类的成员变量）
    legs_num = 2 # legs腿


    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

    def running(self):
        print(self.name+' is running')

yuan = Person('lpx',18)
alvin = Person('zs',20)

# 实例对象调用类属性
print(yuan.legs_num)
print(alvin.legs_num)

# 类对象调用类属性
print(Person.legs_num) # 2


# 类对象修改属性
# Person.legs_num = 4  # 这个是直接修改 类的属性 而下面的是 在 实例yuan里面新建这个属性

# yuan.legs_num = 4 是赋值操作，并不是查找操作
# 如果是查找则是 先在自己空间查找，自己空间找不到 再到类空间去查找
# 但是如果是赋值，则会，如果自己的空间没有，则会直接在自己空间新建这个属性，并
# 并不是到类空间里去 修改类的 属性
# 这里是重点
yuan.legs_num = 4


print(yuan.legs_num) # 4
print(alvin.legs_num) # 2

# 实例对象调用实例方法
# 解释器会将实例对象作为第一个实参（也就是self），传递给实例方法
yuan.running()  # running


# 类对象 调用实例方法  【一般不这么用】
# 重点，这里必须传参
Person.running(yuan) # 等价于 yuan.running()
