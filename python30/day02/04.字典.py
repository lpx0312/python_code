#  字典类型
#  字典是不连续的，使用key-value通过键值hash指针来定位的
#  因为是不连续的内存空间 ，字典不属于 序列

# 字典特性：
# ①：键不可重复，创建时同一个键被赋值两次，后面一个值会被记住
# ②：键的数据类型：必须是不可变类型（整型，字符串，元祖，布尔）
#    值可以是任意类型
# ================================
# 字典的键可以使用布尔类型的，True 默认代表 1，False 默认代表 0，
# 如果包含 0 或 1 就无法使用布尔类型：
# >>> test = {0:"1", 1:"2", True:"3", False:"4"}
# >>> print(test)
# {0: '4', 1: '3'}
# 没有 0 或 1 的情况下：
#
# >>> test = {"a":"1", "b" :"2", True:"3", False:"4"}
# >>> print(test)
# {'a': '1', True: '3', 'b': '2', False: '4'}

# =================================
# 创建字典：
# 不可变类型作为字典的键(整形，字符串，元祖)
# 可变类型（列表，字典）
# 值：可以是任意类型
# dic = {"name":"lpx",1:"hehe1" }

# 如果创建的时候.键重复了，则后面会替换前面的
# dict1 = {'a': 1, 'b': 2, 'b': '3'}
# print(dict1 ) # {'a': 1, 'b': '3'}

# len(dic)  获取字典中元素数量
# print(len(dic))

# 访问字典
# print(dic["name"])
# print(dic[1]) # 这个方式取值，如果key不存在，会报错，所以不推荐


# print(dic["names"])  # 如果字典的键没有，就会报错。【但不推荐】
# 推荐使用:get方法：通过键取值的方法，如果键没有，则会返回，None ，并不会报错
# dic.get(key,errorValue)
# ->如果key存在返回dic[key]
# ->如果key不存在，返回errorValue(可以是 任何类型)
# print(dic.get("sss")) #None
# print(dic.get("name")) #ahaha
# print(type(None)) # <class 'NoneType'>
# print(dic.get("sss", ["hehe","hah"]))

# # 3、 setdefault 方法【可用于 获取和添加】
# # 如果 setdefault中key不存在，则是相当于，添加操作
# # 如果 setdefault中key存在，只是获取value，并不是修改
# dic = {"name": "lpx", 1: "hehe1"}
# # val 是 取到的值，
# val = dic.setdefault("height", "180")
# print("var:{}".format(val))
# print(dic)  # {'name': 'lpx', 1: 'hehe1', 'height': '180'}

#  get和setdefault 区别：
#  get如果其中的key不存在，会返回另一个值，但是并不会更改原字典的内容
#   但是setdefault如果key不在，也会返回一个默认值，但是会将其更改到原字典中

# 4、keys values items方法
# print(dic.keys())
# print(type(dic.keys())) # <class 'dict_keys'>
# print(dic.values())
# print(type(dic.values())) # <class 'dict_values'>
# print(dic.items())
# print(type(dic.items()))  # <class 'dict_items'>

#
# # 添加方法
# # 如果key不存在 则重新添加
# dic["height"]="180cm"
# print(dic)
# # 如果key存在，则是 修改
# dic["name"] = "lll"
# print(dic)

#
# # 删除方法 【特别注意：和别的语言不一样的点】
# # del  删除键值对（常用），删除dic字典（不建议）
#  python系统级方法删除 del
# del dic["name"]
# print(dic)
# # 直接删除 dic ，但是不建议，因为python有自己的垃圾回收机制，不用的时候，自动回回收。
# # del dic

# dic = {"name": "lpx", 1: "hehe1"}
# # 根据键删除
# dic.pop("name")  # 如果pop键没有，会报错
# print(dic)
#
# dic.popitem()# python3.6之前，字典是无序的，则popitem会随机删除
# python3.6之后，把字典变成了 有序的，则popitem会删除最后一个

# 清空字典
# dic.clear()
# print(dic)    # {}

# # 虽然 字典不是序列，是无序的，但是也有个in语法 【重点】
# # in  用来判断  键中是否存在 height
# print("height" in dic)


# 类似 列表中的 extend，但是extend不能更新或修改，只能扩展
# dic = {"name":"lpx",1:"hehe1" }
# dic2 = { 10:100,11:110,"shuzu":["h",2,3,4] }

# 没有重复的话
# dic.update(dic2)
# print(dic)  # {'name': 'lpx', 1: 'hehe1', 10: 100, 11: 110, 'shuzu': ['h', 2, 3, 4]}

# 如果有重复的
# key的name就会被更改，其余扩展
# {'name': 'haha', 1: 100, 11: 110, 'shuzu': ['h', 2, 3, 4]}
# dic = {"name":"lpx",1:"hehe1" }
# dic2 = { 1:100,11:110,"shuzu":["h",2,3,4],"name":"haha" }
# dic.update(dic2)
# print(dic)

# update 可以更改多个 value
# dic = {"name":"lpx","language":"chian","address":"Wuhan"}
# dic2 = {"name":"lipanx","address":"hanyang"}
# dic.update(dic2)
# print(dic)

dic = {"name": "lpx", "age": 23 }