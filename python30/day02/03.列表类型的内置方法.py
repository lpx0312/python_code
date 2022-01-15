#列表的内置方法

# 添加方法
# ① append 追加 （从最后面追加）
# ② insert 插入
# ③ extend 扩展列表


# names = ["张三","李四","欧阳一枝花","王五","赵六"]

# append的方法  没有返回值，直接操作对象
# names.append("hah")
# print(names)
# print(len(names))

# names2 = ["haha","kjk",True]
# names.append(names2)
# print(names)
# print(len(names))

#extend  扩展列表:  names.extend(names3) 扩展names 直接操作列表，并没有返回值

names = ["张三","李四","欧阳一枝花","王五","赵六"]
names3 = ["haha","kjk",True]
names.extend(names3)  # names = ['张三', '李四', '欧阳一枝花', '王五', '赵六', 'haha', 'kjk', True]
print(names)

# 直接使用 使用+ 并不直接操作names，
# name4 = names + names3
# print(name4)     # names = ['张三', '李四', '欧阳一枝花', '王五', '赵六', 'haha', 'kjk', True]


# insert 插入列表
# 索引1的位置  插入数据
# names.insert(1, "插入的值")
# print(names)


# 删除方法
# ① pop 按照索引删除  不填参数默认删除最后一个元素
# ② remove  按元素值删除 前提必须有这个元素
# ③ clear
# names = ["张三", "李四", "欧阳一枝花", "王五", "赵六"]

# names.pop()
# print(names)
# names.pop(1)

# 如果删除的元素值不存在 会报错 list.remove(x): x not in list
# names.remove("zhang")

# str = "张三"
# if  str in names :
#     names.remove(str)
#     print(names)
# else:
#     print("元素不存在删除失败")

# 清空列表数据
# names.clear()
# print(names)


# # 更改方法：没有具体的方法，就是直接赋值 就是 更改
# names = ["张三", "李四", "欧阳一枝花", "王五", "赵六"]
# # 单元素更改
# names[0] = "zhang"
# print(names)
# # 多元素更改
# names[1:2]=["er","san"]
# print(names)

# 查询方法：
# index方法、count方法、len方法
# find 查询元素索引【只是 字符串 方法 列表不能使用】： 查询到 返回索引，查询不到返回 -1，只查询第一次出现的
# index 查询元素索引： 查询到 返回索引，查询不到会 报错，只查询第一次出现的
# count 查询元素在列表中的个数：
# len  查询元素个数
# names = ["张三", "张三", "欧阳一枝花", "王五", "赵六"]

# print(names.index("张三"))
# # print(names.find("s")) 报错:
# print(len(names))    # 5
# print(names.count("张三")) # 2


# sort 方法排序 (没有返回值) ,参数 reverse（翻转）是一个布尔值，默认False正序，True是 倒序
# nums = [12,334,115,78]
# # nums.sort()
# nums.sort(reverse=True)
# print(nums)


# reverse方法（没有返回值）：翻转列表 ：
# nums2 =  ["sss",1,"345",False]
# nums2.reverse()
# print(nums2)


# # list
# # 列表的复制 copy 有返回值
# names2 = names.copy()
# # 列表的扩展  extend 直接扩展本列表，没有返回值
# names.extend(names2)
# print(names)
# print(names2)


#









# list_iterator 列表迭代器
# print([1,2,3].__iter__()) # <list_iterator object at 0x000001BC2E563970>
# print({"name":"lpx"}.__iter__()) # <dict_keyiterator object at 0x000001FD657CAA40>

# [1,2,3]是可迭代对象
# 可迭代对象调用__iter__()方法，就生成该对象的迭代器

# 生成可迭代器
# iter1 = [1,2,3].__iter__()
# print(iter1.__next__()) # 将元素依次取出来
# print(iter1.__next__()) # 将元素依次取出来
# print(iter1.__next__()) # 将元素依次取出来
# print(iter1.__next__()) # 超过会报错

# 迭代器功能：主要是 用于内存优化，
# 比如:列表中的存1亿个数据，内存就崩溃了。
# 惰性查询：把列表做成迭代器，就不会存1亿个数据。








# LEB421011709
#
# 15871718721     ZHANG
























