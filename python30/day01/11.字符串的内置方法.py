


# # 可以视一切数据皆为对象    --》 对象.方法()
# # 同一类型的内置方法是相同的，
# #str 输入str 后 Ctrl+左键，可以查看所有的 字符串的方法
#
#
#
# # String字符串的内置方法
#
# # "hi".capitalize() 首字符大写
# result = "hi".capitalize()
# print(result)
# # "hello world".title()
# # 让每个单词的首字母大写，前提是每个单词用空格分开，否则python不知道是不是一个单词
# # .title() 以空格作为“分隔符”
# print("hello world".title())
#
#
# #"hi".upper() 所有字符大写
# print("hi".upper())
#
# #"hi".lower() 所有字符小写
# print("hi".lower())

# 大小写
"Hello World".capitalize()# 首字母大写
"Hello World".upper()     # 全部小写
"Hello World".lower()     # 全部小写
"Hello World".title()     # 各单词首字符大写
"Hello World".swapcase()  # 大小写互换

# 判断字符串中的字符类型
"hello World".startswith('a')   # 判断str是否以a开头
"hello World".endswith('a')     # 判断str是否以a结尾
'hello World'.isalnum()         # 判断是否全为字母或数字
'hello World'.isalpha()         # 是否全为字母
'hello World'.isdigit()         # 是否全为数字
'hello World'.islower()         # 是否全小写
'hello World'.isupper()         # 是否全大写
'hello World'.istitle()         # 是否首字母为大写
'hello World'.isspace()         # 判断字符是否为空格

# 字符串替换
'hello World'.replace('llo','new')          # 字符串替换
'hello World'.replace('llo','new',2)        # 替换指定次数

# 去空格
# 返回删除空格后的副本，原字符串并没有变化
'   hello World   '.strip()   # 去两边空格
'   hello World   '.lstrip()  # 去左边空格
'   hello World   '.rsplit()  # 去右边空格
print('   hello World   '.rstrip())


# 用指定符连接单个字符串：join操作列表，返回字符串
print('-'.join(['a', 'b', 'c']))  # a-b-c

# 用字符串中指定符分割字符串-->返回列表
'hello World'.split()               # 默认空格分割
# print('he-ll-o Wo-rld'.split('-'))  #['he', 'll', 'o Wo', 'rld']

# 搜索
'hello World'.find('ll')    #  2,搜索不到 返回 -1
'hello World'.index('ll')   #  2,搜索不到 会报错
'hello Worldll'.rfind('ll') #  11,从右边开始搜索
"hello World".count("l")   #  3  # 获取"l"在字符串中的个数




#
#
# #"  helloworld  ".strip() 取出首尾两端的空格【重点】
# print("  helloworld  ".strip())
# print("  helloworld  ".lstrip()) #去除左边空格
# print("  helloworld  ".rstrip()) #去除右边空格
#
# #"hello world".replace("world", "lpx") 替换字符串
# print("hello world".replace("world", "lpx"))  #hello lpx
# print("hello world".replace("worlds", "lpx"))  #hello world  没有找到old str则没有效果，也不会报错



# #判断是否是数字字符串
# #input所有输入 都会默认为 是字符串
# yourAge = input("年龄：")
# # #先去除前后空格
# totalAge = yourAge.strip()
# totalAge.isdigit(),判断这个"23"字符串是否能转化为数字 如果是则返回True
# isNumber = totalAge.isdigit()
#
# if  isNumber :
#     print(int(totalAge) > 30)
# else:
#     print("输入错误")
# # 全选 Ctrl+ /整体单行注释


# #int(str)将字符串强行转化为int整数，前提是字符串可以转成 整数，eg"sss"就不能转化为整数
#
# #"hello world".find("wor") 查询字符串，查到了返回这个首字符的索引 从0 开始算
# print("hello world".find("wor"))  #   6
# print("hello world".find("wors"))  # 找不到就返回  -1


# #判断开头结尾
# #str.startwith(substr),如果是以substr开头返回True，否则返回False
# print("root:lpx 123 ".startswith("ro"))
# print("root:lpx 123 ".startswith("lpx"))
#str.endwith(substr)以什么结束
# print("sdfsdhaha".endswith("haha", 1, 20)) #True


# #join 方法  拼接字符串【注意：和别的语言使用方法不太一样】
# names = ["li","px","李"]
# result = "|".join(names)  #使用| 来拼接"数组"(但python不是数组 叫什么后面解释)中的字符串，
# print(result) # "li|px|李"
# result = " ".join(names)  # 使用空格分隔后拼接 #
# print(result)
#
#
#
# # .encode() 很关键 后面再讲
# # "lisdd".encode()
# # isdecimal() 是不是decimal
# print("20".isdecimal()) #True
# print("20s".isdecimal()) #False
#
# print("11","22")
#

# str.split("str")
# print("Hello world".split(" "))#按照“ ”空格将str拆分成含有多个字符串的列表 结果['Hello', 'aworld']
# print("Hello world".split("sss")) #如果拆分需要 没有  则不会拆分，则结果依旧是一个列表，==》['Hello world']

















