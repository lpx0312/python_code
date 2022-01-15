class Student(object):
    def __init__(self,name,score,sex):
        self.__name = name
        self.score = score
        self.__sex = sex


    @property
    # 获取私有化属性的方法
    def name(self):
        return self.__name


    # @property
    def score(self):
        return self.score

    @score.setter
    def score(self, score):
        self.score = score
        # print(self.score)
    #
    # def haha(self):
    #     print(self.score)


s1 = Student("lpx",100,"m")
# 没有加 property属性之前，是当做函数来调用
# print(s1.name())
# 加了 property之后，将这个方法当做属性来调用，省略了()
print(s1.name)
# s1.score = 100
# print(s1.score)
# s1.haha()



'''
使用接口函数获取修改数据 和 使用点方法（alex.name = ‘yuan’ 或者print(yuan.name)）设置数据相比， 
点方法使用更方便，我们有什么方法达到 既能使用点方法，同时又能让点方法直接调用到我们的接口了，答案就是property属性装饰器：

```python
class Student(object):

    def __init__(self,name,score,sex):
        self.__name = name
        self.__score = score
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) > 1 :
            self.__name = name
        else:
            print("name的长度必须要大于1个长度")

    @property
    def score(self):
        return self.__score

    # @score.setter
    # def score(self, score):
    #     if score > 0 and score < 100:
    #         self.__score = score
    #     else:
    #         print("输入错误！")


yuan = Student('yuan',18,'male')

yuan.name = '苑浩'  #  调用了score(self, score)函数设置数据

print(yuan.name)   #  调用了score(self)函数获取数据

yuan.score = 199
print(yuan.score)
```

注意，使用 @property 装饰器时，接口名不必与属性名相同。

python提供了更加人性化的操作，可以通过限制方式完成只读、只写、读写、删除等各种操作

```python
class Person:
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    def __del_name(self):
        del self.__name
    # property()中定义了读取、赋值、删除的操作
    # name = property(__get_name, __set_name, __del_name)
    name = property(__get_name, __set_name)

yuan = Person("yuan")

print(yuan.name)   # 合法：调用__get_name
yuan.name = "苑浩"  # 合法：调用__set_name
print(yuan.name)

# property中没有添加__del_name函数，所以不能删除指定的属性
del p.name  # 错误：AttributeError: can't delete Attribute
```

`@property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


'''