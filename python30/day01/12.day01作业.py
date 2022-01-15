#0. 什么是解释器,什么是编译器,简述两者的区别


# 编译器--> b


import keyword
print(keyword.kwlist)

'''
2. 用print打印出下面内容：
文能提笔安天下,
武能上马定乾坤。
心存谋略何人胜,
古今英雄唯是君。
'''


# #方法1：
# print("文能提笔安天下,")
# print("武能上马定乾坤。")
# print("心存谋略何人胜,")
# print("古今英雄唯是君。")
# #方法2：
# print("文能提笔安天下,\n武能上马定乾坤。\n心存谋略何人胜,\n古今英雄唯是君。")
#
# print("""
# 文能提笔安天下,
# 武能上马定乾坤。
# 古今英雄唯是君。
# """)


"""
4. 分别使用%占位符以及format方法制作趣味模板程序需求：
等待用户输名字、地址、爱好，根据用户的名字和爱好进任意格式化输出 
如：敬爱可亲的xxx，最喜欢在xxx地方法xxx
"""
name = input("请输入如你的名字：>>>")
addr = input("请输入你的地址：>>>")
like = input("请输入你的爱好：>>>")
print("敬爱可亲的{name},最喜欢在{addr}地方玩{like}".format(name,addr,like))

# 心存谋略何人胜,


#
# print("请输入名字".center(20, "*"))
# name = input(">>>")
# print("请输入地址".center(20, "*"))
# address = input(">>>")
# print("请输入您的爱好".center(20, "*"))
# like = input(">>>")
#
# #占位符方式
# print("敬爱可爱的%s,最喜欢在%s的地方%s" % (name, address, like))
#
# #format的方式
# print("敬爱可爱的{name},最喜欢在{address}的地方{like}".format(name=name, address=address, like=like))


'''
5. 有 names = "  张三 李四 王五 赵六 "
   将names字符串中所有的名字放在一个列表中
'''

names = "  张三 李四 王五 赵六 "
# 必须先去除 前后的空格，在分隔
print(names.strip().split(" "))


'''
6. 查找字符串"  张三 李四 王五 赵六 "王五的索引位置
'''




print(names.find("王五"))
print(names.index("王五"))

'''
 7.将十进制1025分别转换为二进制,八进制以及十六进制
'''

print(bin(1025))
print(oct(1025))
print(hex(1025))

'''
8. 将"goods"与"food"以及"meat"拼接为完整路径,即"/goods/food/meat/"
'''









# s1 = "/{}/{}/{}".format("goods", "food", "meat")
# print(s1)
# s2 = "/%s/%s/%s" % ("goods", "food", "meat")
# print(s2)
# join
# s3 = "/" + "/".join(["goods", "food", "meat"])
# print(s3


