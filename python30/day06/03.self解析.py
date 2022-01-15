class Student:
    '''
    这是一个学生类
    '''
    # self可以换成abc，但是规范不要改
    def study(self):
        '''
        :return:None
        '''
        # 其实这个self就是 s1 那个实例对象
        # s1调用这个study方法 self就是s1，s2调用这个self就是s2
        print(id(self)) # 2260659034576
        print("学习")

s1 = Student()
s1.name = "lpx"

s1.study()
print(id(s1))   # 2260659034576