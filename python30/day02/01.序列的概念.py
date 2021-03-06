# 序列是什么？
# 序列是一个概念，并不是一种类型
# 序列是一串连续存储的空间
# 其中 字符串就属于序列


# 序列通过  索引取值
s = "sktill001.xyz"
print(s[::-1])
# 字符串可以作为 序列
print(s[0])  # 字符串也可以当做 一个 序列
print(s[-1])  # -->z  倒数第一个字符
# 索引是 从0开始算


# 切片：必须有两刀 有开头还有结尾
# 一刀是索引
# 切片原则：左闭右开
# s[0:8] 索引0取得到  索引8的没有取到
print(s[0:8])  # sktill00
print(s[0:9])  # sktill001   满足需求

# s[:10]  ==》等价于 s[0:10]
# s[10:] 缺省状态，默认取到结尾
# s[:] ==》 相当于从头取到尾，
# #需求：取得xyz
if s.find("xyz") != -1:  # 先判断s字符串中是否存在 xyz ,为什么不用index，因为如果不存在index会报错，不知如何判断，还没有学异常处理流程
    print(s[s.find("xyz"):])  # 如果存在则返回，
else:
    print("不存在xyz字符串")

# s="sktill001.xyz"
print(s[0:10:2])  # stl01

print(s[2::2])  # tl01xz

# s[start:end:step]
# start :开始索引  不写默认0
# end   :结束索引  不写默认到最后
# step  ：步长


# 序列的相乘和相加
print("*" * 3)  # =>  ***  为什么可以相乘 因为字符串也可以作为序列，可以进行相乘
print("*" * 3 + "haha")  # => ***haha
# 因为"*"可以作为序列，所以用乘法，因为是字符串 所以可以+ "字符串"
print(type("*" * 3))  # => <class 'str'>
print(["2", "3", "4"] * 2)  # => ['2', '3', '4', '2', '3', '4']
print(type(["2", "3", "4"] * 2))  # <class 'list'>
print([2, 3, 4] * 2)  # => [2, 3, 4, 2, 3, 4]
print(type([2, 3, 4] * 2))  # <class 'list'>
print(type([2, 3, 4]))  # <class 'list'>
# 序列*数量+序列（不能+其他类型，因为会报错）
print([2, 3, 4] * 2 + [3, 1])

# in 判断是否存在
print("张三" in "张三 李四 王五")  # True
print("张三" in "张 三 李四 王五")  # False
print("张三" in ["张三", "李四"])  # True
