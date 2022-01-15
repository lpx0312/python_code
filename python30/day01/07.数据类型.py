# 数据类型
# 1.基本数据类型：（所有语言都有的）  整形 字符串  布尔类型
#
x = 10
print(x)
print(type(x)) # <class 'int'> int 类型

# python 不分 长整型  短整型 等类型，
# 8字节 就是 2的8次方  256
# 1Byte字节 = 4 bit
y = 18000000000000000000000000000
print(y)
print(type(y)) # <class 'int'> int 类型


# 进制（逢几进一）
# 计算机只认识 二进制
# 0b 开头的代表 后面数字是 二进制的
print(0b0011)
# 0o 代表八进制
print(0o12)
# 0x 代表十六进制
print(0x101)


# 进制转化
#bin(num) 转化为2进制
print(bin(1024)) # 10进制转2进制
print(bin(0x777))  #16进制转2进制
# oct(num) 转化为8进制  注意大小写
print(oct(1024))
# hex(num)  转化为16进制
print(hex(0o7777))



# print(0b)


