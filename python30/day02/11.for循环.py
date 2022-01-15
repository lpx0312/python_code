
# python没有一般的 for循环 例如for(i=0;i<100;i++)这样的。
# 只有类似其他语言的  for in语言
# names = ["a","b","c","d"]

# for item in names:
#     print(item)

# 变量赋值，小技巧
# 分别赋值
# x,y = [12,23]
# print(x)
# print(y)

# x1,*y1 = [12,23,34,55]
# print(x1) # 12
# print(y1) # [23, 34, 55]

# enumerate(枚举)是一个内置函数,一般用于 获取索引列表
# enumerate(names) 返回的是 一个 元祖类新的数据(0, 'a') 其中第一个数据是 索引，第二个数据是 值，相当于其他语言的key和value
# for i in enumerate(names):
#     print(i)
# 然后把元祖(0, 'a') 赋值给 i,j ,则i就是索引，j就是值，
# for i,j in enumerate(names):
#     print(i,j)

dic = {"name":"lpx","age":23,"address":"汉阳区"}
# 这几种都是 可迭代的对象，可以使用for in循环
# print(dic.keys()) # dict_keys(['name', 'age', 'address'])
# print(dic.values()) # dict_values(['lpx', 23, '汉阳区'])
# print(dic.items()) # dict_items([('name', 'lpx'), ('age', 23), ('address', '汉阳区')])
# 遍历 keys 和 values 都是获取到一个值，
# 遍历 items 是直接获取到一个有两个数的元祖，需要两个值来接受



# for key in  dic.keys():  # 等同于 for key in  dic：因为默认dic循环的时候，就是dic.keys()
#     print(key)
# for value in  dic.values():
#     print(value)
# for key,value in  dic.items():
#     print(key,value)

# for key,value in  dic.items() 等同于下面的
#
for key in dic:
    print(key,dic[key])


# for循环的次数
# range 相当于次数了，range(100)等价于包含100个元素的列表[0,1,2,3,4......99]
# for i in range(100):
#     print(i)  # 打印 0到99

# range(1,100) ，定义起止位置: 1是起，止是100-1=99
# for i in range(1,100):
#     print(i) # 1-99
# for i in range(10,100):
#     print(i) # 10-99 ，

# print(range(1,100))       # range(1, 100)
# print(type(range(1,100))) # <class 'range'>

