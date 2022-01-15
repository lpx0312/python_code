# li = ["yuan", "alvin", "ritian", "barry", "stevin"]
# # 1)列表中追加元素"seven",并输出添加后的列表
# # 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# # 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# # 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# # 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# # 6)请删除列表中的元素"yuan",并输出添加后的列表
# # 7)请删除列表中的第2至4个元素，并输出删除元素后的列表
# # 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# # 9)请将列表所有得元素反转，并输出反转后的列表
# # 10)请计算出"yuan"元素在列表li中出现的次数,并输出该次数。
# # 11)numbe = [1,2,72,42,25,16] 排序 输入升序和倒序 后的列表


# 1)列表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)

# 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,"Tony")
# print(li)

# 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = "Kelly"
# print(li)

# 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)

# 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwer"
# li.extend(s)
# print(li)

# print(help(list))

# 6)请删除列表中的元素"yuan",并输出添加后的列表
# if "yuan" in li :
#     li.remove("yuan")
# print(li)

# # 7)请删除列表中的第2至4个元素，并输出删除元素后的列表【重点没做出来】
# li = ["yuan", "alvin", "ritian", "barry", "stevin"]
# # print(help(list.pop))
# del li[1:4]
# print(li)

# 8）请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# li = ["yuan", "alvin", "ritian", "barry", "stevin"]
# print(li[1])
# tmp =  li.pop(1)
# print(li)
# print(tmp)

# 9)请将列表所有得元素反转，并输出反转后的列表
# li = ["yuan", "alvin", "ritian", "barry", "stevin"]
# li.reverse()
# print(li)

# 10)请计算出"yuan"元素在列表li中出现的次数,并输出该次数。
# li = ["yuan", "alvin", "ritian", "yuan", "stevin"]
# print(li.count("yuan"))


# 11) numbe = [1,2,72,42,25,16] 排序 输入升序和倒序 后的列表
# numbe = [1,2,72,42,25,16]
# numbe.sort()
# print(numbe) # [1, 2, 16, 25, 42, 72]

# numbe.sort(reverse=True)
# print(numbe)  # [72, 42, 25, 16, 2, 1]
