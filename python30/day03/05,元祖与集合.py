
# # 字符串 整型 浮点型 布尔型 列表  字典  元祖  集合 None
#
# # 元祖： 只读列表
# #  元祖和列表的方法  几乎一样，只是不能更改
# #  不可变类型
#
# t = (1, 2, "wo","wo")
# print(t)
# print(type(t))  # <class 'tuple'>
#
# print(t[1])
# print(t[1:4])
#
# print('wo' in t)  # (2, 3)
#
# # 查看元素值在元祖中的索引
# print(t.index("wo"))
#
# # 查看元素值在元祖中的个数
# print(t.count("wo"))
#
# print("================")
# # 元祖的遍历
# for  i in  t:
#     print(i)
#
# print("======集合=======")


# 集合 ：无序的  类名 就是 set
# 集合中只能存放，不可变类型
# 但是结合本身【默认】是 可变类型
# 集合不支持重复，可用于集合类型来去重

#  {vaue1,value2 }=》集合
#  {key：valie,key1:value2} =>字典
#  [value1,value2]=>列表
#  (value1，value2，value3)  => 元祖

# s1 = {1,2,3,1,2,5,7,"1"}
# print(s1)       # {1, 2, 3, 5, 7, '1'}
# print(type(s1)) # <class 'set'>

# # 利用集合去重
# names = ["张三","李四","王五","张三"]
# # 集合 = set[列表]  将列表转化为集合
# s2 = set(names)
# # 但是 这是 无序的
# print(s2)  #{'张三', '王五', '李四'}

# # 列表 = list(集合) 将集合转化为 列表
# print(list(s2))
# # print(len(list(s2)))

# # 添加
# s2.add("添加")
# s2.add(("hehe","haha"))
# s2.update({"张三","李四","update"})

# # 删除
# # s2.remove("添加") # 删除没有的value，会报错
# # s2.pop() # 随机删除
# print(s2)
# s2.discard("张三2") # 删除没有的value不会报错，也没有动作
# print(s2)

# 集合操作:都有返回值，都是操作后，返回新的集合
s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
# 只有差集 s3对s4 和s4 对 s3 有问题，其余的都一样

# 交集 intersection
print(s4.intersection(s3))  # intersection 交集 {4, 5}
print(s3.intersection(s4))  # {4, 5}
# 并集  union
print(s4.union(s3)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s3.union(s4)) # {1, 2, 3, 4, 5, 6, 7, 8}
# 差集  difference
print(s3.difference(s4))  # {1, 2, 3}
print(s4.difference(s3))  # {8, 6, 7}
# 对称差集 symmetric_difference
print(s3.symmetric_difference(s4))  # {1, 2, 3, 6, 7, 8}
print(s4.symmetric_difference(s3))  # {1, 2, 3, 6, 7, 8}

