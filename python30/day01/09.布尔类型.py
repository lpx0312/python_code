# 布尔类型
# 只有两种：True 和 False


# python大小写有区别，所有不能搞错
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>
print(4 < 6)
print(4 == 4)

# python 中会把 True当做 整形 1 使用
# 把False视为0
print(True)
print(False)
print(True+8)
print(False+8)
print(type(True+1))  # 这个就是 int类型

#python是强类型还是弱类型，
#弱类型的原因是：不用声明 变量的类型
#强类型的原因是：
# 如果语言支持隐式转换，则语言是弱类型语言，
# 但是python不支持隐式转换，则从这个角度，python就是强类型语言。
# print("23"+12)   #不会隐式转换。
