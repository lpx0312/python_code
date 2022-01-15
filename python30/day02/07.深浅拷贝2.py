
# 数据类型： 可变类型和不可变类型
# 不可变类型：整型 字符串  布尔  元祖
# 可变类型： 列表  字典


# 浅拷贝
# a = [[1,2,3],20,30]
# b = a.copy()  # 同b=a[:]
# a[0][1] = 1000
# print(a) # [[1, 1000, 3], 20, 30]
# print(b) # [[1, 1000, 3], 20, 30]


# 浅拷贝：拷贝的是内存地址，并不是拷贝的值
# print(id(a[0][1]))
# print(id(b[0][1]))



# 使用copy的python方法，并不是 对象方法，必须使用copy模块
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象
a[2] = 333

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

# https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
