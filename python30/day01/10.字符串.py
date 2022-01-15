
# python 不区分 单引号和双引号
s1 = "hello"
s2 = 'world'
print(s1,s2)  # hello world


# 转移: \
# 1.加上普通符号赋 予特定功能
print("OK\nhaha\nwawa") # \ 加上普通符号 n 变成了特性功能的换行
print("OK\thaha\twawa") # \t  制表符

# 2.加上特殊符号变成普通符号
# \ 加上特殊字符串的引号，把这个'变成纯粹的' 并不是结束的引号
print('I\'m lpx')
# 还可以使用r'' 将字符串内的\ 不作为转义符
# 注意 r针对于 \ 不能进行转义
print(r"I'm lpx")




#长字符串：''' 或者 """ 成对
#通常用于 引导选项
print('''
    hello 
    world
''')

print('''
    1.添加学生 
    2.删除学生
    3.查询学生
    4.修改学生信息
    5.退出程序
''')

#choice = input("请选择功能序号：")



# 格式化输出：注意和别的语言都不一样
# 方式1：%s 等方式 占位符方式
"""
%d、%i       转换为带符号的十进制整数
%o           转换为带符号的八进伟整数
%x、%X      转换为带符号的十六进制整数
%e          转化为科学计数法表示的浮点数（e小写）
%E          转化为科学计数法表示的浮点数（E大写）
%f、%F      转化为十进制浮点数
%g          智能选择使用%f或%e格式
%G          智能选择使用F或%E格式
%c          格式化字符及其ASCII码
%r          互使用repr）虽改将表达式转换为字符串
%s          使用Str（）函数将表达式转换为字符串
"""
name = "li"
age = 23
print("姓名：%s;年龄：%d"%(name,age))

money=3.1415956
print("money：%.2f"%(money))


#方式2：format方式， 【推荐】
#解释，"姓名：{};年龄：{}".format(name,age) 其中 format是字符串的内置方法，所以使用.来连接
# print("hi{0}".format("woca"))  #hiwoca  在pycharm中可以直接，"hi{0}".format("woca").print()回车得到前面代码
print("姓名：{};年龄：{}".format(name,age))   # "姓名：li;年龄：23"
print("姓名：{0};年龄：{1}".format(name,age)) #同上  "姓名：li;年龄：23"
print("姓名：{1};年龄：{0}".format(name,age)) #1是第二个占位符 0才是第一个 结果是"姓名：23;年龄：li"
print("姓名：{0};年龄：{1}！{1}".format(name,age)) #不需要多写因为一共就0 和1 连个参数
#高级玩法：使用 key-value 【最为推荐】 不存在 位置是否更换
print("key-value 姓名：{name};年龄：{age}".format(name=age,age=age))
print("key-value2 姓名：{a};年龄：{b}".format(a=age,b=age))  #{a}其实a是坑（占位符）的名称，a=age意思是 这个a坑里面是 age的值

#format格式化数组
grade = 97.556   # 浮点数取位数
print("money：{:.2f}".format(money))  # 3.14
print("money：{money:.2f}".format(money=money)) #3.14

# 字符串的小操作
# 拼接 +
x = "hello"
y = "world"
#字符串拼接  +  前提是两边必须是字符串，否则会报错，
# 因为python不能隐式转换，除了布尔值和0 1之间的转换。
print(x+y)

# 乘  *
print("*+*+"*10)
print("*"*30+"Welcome to Home"+"*"*30)

# 帮助手册查看
# print(help(str))  #太长了 所有的str帮助
print(help(str.upper))

#  https://blog.csdn.net/a1786742005/article/details/89388093
# 进阶
# 通过序列传入参数
# 在序列名前加一个*，就可以传入。
list1 = ["Hello","World"]
print("{} {}".format(*list1))   # 按照默认位置传入
print("{0} {1}".format(*list1))   # 按照指定位置传入
print("{1} {0}".format(*list1))   # 按照指定位置传入

# 进阶
# 通过字典传入
# 在字典前加两个*，就可以传入
kw = {"name":"小明","height":"180cm"}
print("{name}的身高是{height}".format(**kw)) # 小明的身高是180cm
# 如果不指定 坑的符号，也可以使用这一种，注意必须是*dict.values()
# 因为dict遍历，默认的是key而不是value
print("{}的身高是{}".format(*kw.values())) # 小明的身高是180cm
print("==========={}的身高是{}".format(*kw)) # name的身高是height

print("{1} {0}".format(*list1))


strvar = "忽一涛买了%-2d个风油精" % (3)
print(strvar)
