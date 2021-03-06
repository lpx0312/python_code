# x = 123
# 变量赋值=等号左右，可以有空格，也可没空格，建议=左右有个空格
# 1.变量的首个字符不能是数字，会报错
# 2.变量严格区分大小写，X和x是两个 变量，
# 3.x和_x都不会报错，可正常运行,但是_x在特定情况会有特殊意思，所以不建议使用_开头做变量
# 4.python可以使用中文做变量名，但是不建议，容易产生很大的坑。
# 5.变量名：遵循小驼峰，首字符小写，其余字符大写
# 这里的print一行代码，前面不能有空格，否则会报错：IndentationError  缩进错误，强缩进语言，所有代码必须顶头写
# print(x)

# 如果只写一个y ，会报错 “NameError:name'y'is not defined”，但是报错之前的代码打印x的123 却已经执行了，这就是解释性语言的特性，逐行解释，没报错就执行，报错才停止
# 特别注意：python是弱类型语言，可以不用声明变量类型，所有变量赋值不用担心，变量类型
# y = 20
# y = "hehe"
# y = True
#
# print(y)

# 思考
# x = 10
# x = 20
# y = x
# y = 30
# print(x)
# print(y)


# 多变量赋值
# Python允许你同时为多个变量赋值。例如：

# a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
# 您也可以为多个对象指定多个变量。例如：

# PEP8 ,逗号后面 一定要有空格，否则不规范
a, b, c = 1, 2, "runoob"

print(a, b, c)

x1,*y1 = [12,23,34,55]
print(x1) # 12
print(y1) # [23, 34, 55]

