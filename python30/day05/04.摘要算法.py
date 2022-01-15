#coding:utf-8
import hashlib  # hash库
# # 一、hashlib的基本概念
# '''
# 1、什么叫hash:hash是一种算法（不同的hash算法只是复杂度不一样）（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法），该算法接受传入的内容，经过运算得到一串hash值
# 2、hash值的特点是(hash值/产品有三大特性：)：
# 2.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
# 2.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码（只能有内容返回hash值）
# 2.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的(如从网上下载文件要进行hash校验，保证网络传输没有丢包)
# 基于2.1和2.3可以做文件下载一致性的校验
# 基于2.1和2.2可以对用户密码进行加密
# hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()
# 为工厂运送原材料），经过加工返回的产品就是hash值
# '''
#
# # 二、产生hash值的三个阶段
#
# ####   使用 sha256
# # # 1.造出hash工厂
# hash = hashlib.sha256('Hello '.encode('utf8'))      #同一种hash算法得到的长度是固定的
# # # 2.运送原材料
# hash.update('World'.encode('utf8'))                 #工厂传入的原材料都是bytes类型
# # # 3.产出hash值
# # print(hash.digest())  b'\xa5\x91\xa6\xd4\x0b\xf4 @J\x01\x173\xcf\xb7\xb1\x90\xd6,e\xbf\x0b\xcd\xa3+W\xb2w\xd9\xad\x9f\x14n'
# print(hash.hexdigest())         # a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
# print(len(hash.hexdigest()))    # 64位

# m=hashlib.md5()                               #括号内也可以传值，类型也要求是bytes类型
# m.update('你好呀！'.encode('utf-8'))
# print(m.hexdigest())                          #9e49eb8e75b9a87424e388b862ea5f83
#
#
# ## 与上述hash的结果一样 ##
# import hashlib
# m1=hashlib.md5('你'.encode('utf-8'))          # 括号内也可以传值，类型也要求是bytes类型
# m1.update('好呀！'.encode('utf-8'))
# print(m1.hexdigest())                        # 9e49eb8e75b9a87424e388b862ea5f83
#
#
# # # 三、校验文件的一致性  (如何保证下载的文件过程中不丢包，保证下载数据的完整性)
# m2 = hashlib.md5()
# with open(r'./资源/1.torrent','rb') as f :
#     for line in f :
#         m2.update(line)
# print(m2.hexdigest())     # ee87dd6cf9f1afc400c1f3c02e563425
#
# m3 = hashlib.md5()
# with open(r'./资源/2.torrent','rb') as f :
#     for line in f :
#         m3.update(line)
# print(m3.hexdigest())       #ee87dd6cf9f1afc400c1f3c02e563425
#

def hasString(path):
    import hashlib

    has = hashlib.md5()
    with open(path, 'rb') as f:
        for i in f:
            has.update(i)
    return  has.hexdigest()


#
# # # 四、对明文密码进行加密
#
#
# # # 应用：对明文密码进行加密（暴力破解-------用明文密码用一种算法算出一个hash值，与截取的hash值进行比对，比对成功说明明文密码一致，就可以破解用户的密码）
# # '''
# # 如用户在某网站进行注册信息，这个时候防止信息被恶意拦截获取，
# # 可以对用户明文密码进行加密，存成hash值得形式，
# # 这样用户每次登陆虽然输的是明文密码，校验hash值即可
# # '''
# #
# # password1=input('>>>>>:').strip()
# # m4=hashlib.md5()
# # m4.update(password1.encode('utf-8'))
# # print(m4.hexdigest())
# #
# #
# # # 对密码进行加盐（暗号）----------进一步加强密码的安全性
# # password2=input('>>>>>:').strip()
# # m5=hashlib.md5()  # 也可以直接在这里加盐，hashlib.md5('ABC123'.encode('utf-8')
# # m5.update('ABC123'.encode('utf-8'))         #对密码加盐
# # m5.update(password2.encode('utf-8'))
# # print(m5.hexdigest())
#
# # # 五、破解用户注册的密码
# # # 重点
# # '''模拟撞库破解密码'''
# # passwds=[                      #可以通过random实现对passwds中的内容
# #     'alex3714',
# #     'alex1313',
# #     'alex94139413',
# #     'alex123456',
# #     '123456alex',
# #     'a123lex',
# #     ]
# #
# # def make_passwd_dic(passwds):                #通过明文密码列表，造出与之对应的hash值得字典
# #     dic={}
# #     for passwd in passwds:
# #         m=hashlib.md5()                      #使用md5算法，造了一个工厂
# #         m.update(passwd.encode('utf-8'))     #给工厂运送原材料(即我们要加密的内容)
# #         dic[passwd]=m.hexdigest()            #产出hash值（即最终的产品），将其加入到我们事先造好的空字典中，字典形式:{密码：hash值}
# #     return dic
# #
# # def break_code(cryptograph,passwd_dic):      #判断拦截的hash值是否与字典中事先造好的hash值相等，相等则说明成功进行破解
# #     for k,v in passwd_dic.items():
# #         if v == cryptograph:
# #             print('密码是===>{}'.format(k))
# #
# # cryptograph='aee949757a2e698417463d47acac93df'     #我们拦截拿到的密码，经过加密的hash值
# # break_code(cryptograph,make_passwd_dic(passwds))   #将要破解的密码hash值，和事先造好的hash的字典当做函数的实参传给对应的形参


import hashlib

has = hashlib.md5("加盐".encode('utf8'))

has.update("hh".encode('utf8'))

print(has.hexdigest())