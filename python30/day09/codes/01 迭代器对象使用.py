


# 迭代器(iterator)  生成器(generator)


# 一   可迭代对象(iterable) 迭代器:惰性查询
# 迭代的概念： 重复 以本次结果作为下次的初始值
# l=[1,2,3,4,5]
# index=0
# while index < len(l):
#     print(l[index])
#     index+=1
for i in  [1,2,3].__iter__():
    print(i)



# 可迭代对象(Iterable) : 对象类定义__iter__方法的对象称之为可迭代对象
# print([1,2,3].__iter__()) # <list_iterator object at 0x0000022AD4628F28>
# print({"name":"yuan"}.__iter__()) # <dict_keyiterator object at 0x00000204B218A688>s8F28>

# iter = [1,2,3,4].__iter__()
# print(iter.__next__()) # 将元素依次取出来
# print(iter.__next__()) # 将元素依次取出来
# print(iter.__next__()) # 将元素依次取出来
# print(iter.__next__()) # 将元素依次取出来
# print(iter.__next__()) # 将元素依次取出来

# iter2 = {11,22,33}.__iter__()
# print(iter2.__next__())  # 33
# print(iter2.__next__())  # 11
# print(iter2.__next__())  # 22


# 方式1
# count = 0
# while  count<len(l):
#     print(iter_l.__next__())
#     count+=1

# 方式2

# while 1:
#     try:
#         print(iter_l.__next__())
#     except StopIteration:
#         break

# 方式3：
'''
for 循环本质： 
iter = in后面的可迭代对象.__iter__()
while 1:
   try:
       i = iter.__next__()
   except:
       break
'''
# for i in 100:
#     print(i)









