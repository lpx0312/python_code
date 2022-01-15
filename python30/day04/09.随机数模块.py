import random

print(random.choice(["zhangsan","lisi",[1,2,3,43,4]]))

#
# # 0-1 随机浮点数
# # print(random.random())
# # 1-3 随机浮点型
# print(random.uniform(1,3))
#
# # 随机整数（自定义）
# # randint ：1-5 之间的 包含1 和5的 整数 双闭
# print(random.randint(1, 5))
# # randrange：1-5之间 1可以取  5取不到  左闭右开
# print(random.randrange(1, 5))
#
# # choice 从序列中随机选取一个值
# print(random.choice([1, 2, 4, 5, 6, 5, 56, 56]))
# print(random.choice(("sss","sdfs","hhh")))
# print(random.choice(["zhangsan","lisi",[1,2,3,43,4]]))
# print(random.choice([{"age":18,"height":"180cm"},{"age":20,"height":"170cm"}]))
#
# # sample 从序列中取多个
# print(random.sample([{"age":80,"height":"140cm"},{"age":18,"height":"180cm"},{"age":20,"height":"170cm"},{"age":50,"height":"150cm"}],3))
#
#
#
# # 打乱 列表
# l = [1,2,3442,3,5,2,52,34,2]
# random.shuffle(l)
# print(l)



# 案例：生成随机验证码
# 默认生成 5位 随机验证码

print(chr(65))  # A
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122)) # Z
print("abcdefghijklmnopqlszovwxyz".upper())
#
# def yanzhengma():
#     numberend = ""
#     for i in range(0,5):
#         randnum = str(random.randint(0,9))
#         strUpper = chr(random.randint(65,90))
#         strLower = chr(random.randint(97,122))
#         numberend += random.choice([randnum,strLower,strUpper])
#     return numberend
#
# print(yanzhengma())
# import random
# import string
# def get_verificate_code(count,lower=True,upper=True,digits=True):
#     '''
#     :param count: 验证码位数
#     :param lower: 是否含小写字符 默认包含
#     :param upper: 是否含大写字符 默认包含
#     :param digits: 是否含数字   默认包含
#     :return:
#     '''
#     ret = ""
#     if lower:
#         ret += string.ascii_lowercase
#     if upper:
#         ret += string.ascii_uppercase
#     if digits:
#         ret += string.digits
#
#     verificate_code = ""
#     for i in range(count):
#         #可以这么写，但是不太好看，string模块中把这些都定义了，直接使用就可以了
#         #random.choice("abcdefghijklmnopqlszovwxyzABCDEFGHIJKLMNOPQLSZOVWXYZ0123456789")
#         # ascii_letters 带表大小写字符，可以进去看一下 string.digits代表数组
#         verificate_code += random.choice(ret)
#     return verificate_code
# print(get_verificate_code(10,upper=False))

