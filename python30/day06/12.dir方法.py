class Student:
    # 类属性
    x = 100

    def __init__(self,name,score):
       # 实例属性
        self.name = name
        self.score = score

    def test(self):
        pass


lpx =  Student('lpx',100)
# dir(obj) 可以获取对象的所有属性（包含方法）列表
print('获取所有的属性列表')
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'score', 'x']
print(dir(lpx))


print('获取自定义属性字段')
# 对象.__dict__ == 只能获取  实例属性，并不能获取 类属性
print(lpx.__dict__) # {'name': 'lpx', 'score': 100}


