import re
# re是干嘛的，是正则表达式
# https://cnblogs.com/yuanchenqi/articles/6766020.html#%20label5
# 用来做模糊匹配



#
# 完全匹配
ret = re.findall("python", "welcome to python world | python is nice!")
# print(ret)  # ['python', 'python']

# 元字符：. ^  $

# 1. *  通配符：除换行符的任意一个符号：.
print(re.findall(".oo.","room,zoom,zoo,home"))

# 2. ^ $
# ^ 开头   $结尾
print(re.findall("^welcom", "welcome to python world | python is nice!"))   # ['welcom']
print(re.findall("nice!$", "welcome to python world | python is nice!"))   # ['nice!']


# 3. * + ? {}
# * 重复0到无数次
print(re.findall("com*e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['coe', 'come', 'commme', 'commmmmmme']
# + 1到无数次，至少一个
print(re.findall("com+e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['come', 'commme', 'commmmmmme']
# ?  重复0-1次，最多一个
print(re.findall("com?e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['coe', 'come']
# {}:任意指定次数
print(re.findall("com{3}e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['commme']
# {n,}:大于等于n次的
print(re.findall("com{3,}e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['commme', 'commmmmmme']
# {,n}:小于等于n次的
print(re.findall("com{,3}e", "coe welcome welcommme to python world | python is nice! welcommmmmmme"))   # ['coe', 'come', 'commme']


#  4.\ []  () | - 
# \d 就代表一个0-9的数字
print(re.findall("\d", "12,45,67,89,yuan,alvin,100")) # ['1', '2', '4', '5', '6', '7', '8', '9', '1', '0', '0'
# \d+ 至少一个数字，
print(re.findall("\d+", "12,45,67,89,yuan,alvin,100")) # ['12', '45', '67', '89', '100']
#  \w  匹配任何字母数字字符；   它相当于类 [a-zA-Z0-9_]。
print(re.findall("\w+","12,45,67,0,yuan,alvin,100"))   #['12', '45', '67', '0', 'yuan', 'alvin', '100']

# [] 字符集 多选一
print(re.findall("a[bc]d", "abcd")) # []
print(re.findall("a[bc]d", "abd"))  # ['abd']
print(re.findall("a[b,c]d", "abd,acd,a,d,abcd"))  # ['abd', 'acd', 'a,d']
print(re.findall("[1-8]+", "12,45,67,0,1,89yuan,alvin,100")) # ['12', '45', '67', '1', '8', '1']

# [^]:^放在字符集中就是代表  取反
print(re.findall("c[^0-9]e","coe,c12e,c11e,cle,clle")) #['coe', 'cle']


# () 分组
print(re.findall("ad+","addddd")) #['addddd']
print(re.findall("ad+","ad adad adadadad lpx ")) #['ad', 'ad', 'ad']
# findall 遇到分组的时候，只取分组里的内容，并不会全部，例如这个结果，['baidu', 'jd']而不是www.baidu.com和www.jd.com
print(re.findall("(ad)+","ad adad adadadad lpx ")) # ['ad', 'ad', 'ad']
print(re.findall("www.(baidu|jd).com","www.baidu.com,www.jd.com,www.abc.com")) # ['baidu', 'jd']
print(re.findall("y(\d)+","y12n,y123h,yy"))  #['2', '3']

# findall 取消分组优先权：
print(re.findall("y(?:\d)+","y12n,y123h,yy")) #['y12', 'y123']









# 2.方法
# （1）  re.findall("规则","待匹配字符串")
#  (2)  re.search("规则","待匹配字符串")  # 只匹配一个
# ret3= re.search("www.(baidu|jd).com","www.baidu.com,www.jd.com,www.abc.com")
# print(type(ret3)) # <class 're.Match'>
# print(ret3.group())
# print(ret3.span())

#  (3)  re.match("规则","待匹配字符串")  # 只匹配第一个，且如果第一个匹配不成功，就直接返回None
# ret4= re.match("www.(baidu|jd).com","www.baidu.cwm,www.jd.com,www.abc.com")
# print(type(ret4)) # <class 're.Match'>
# print(ret4.group())
# print(ret4.span())


# 贪婪匹配：
# 匹配尽可能长的字符串，re默认采用的就是贪婪匹配
print(re.findall("a+", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa b c")) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print(re.findall("a.*c", "abcabcadc"))  #['abcabcadc']
# .*?  非常有用 规则不好定义的时候就使用.*?
# ？ 用于去掉 贪婪匹配，按最短的来匹配
print(re.findall("a.*?c", "abcabcadc"))  #['abc', 'abc', 'adc']


# 字符串的split方法，有局限性，不能按照多个分隔符来进行分割，只能按照固定的分割
print("hello,world alvin|lpx".split(",")) # ['hello', 'world alvin|lpx']
print(re.split("[, |]", "hello,world alvin|lpx")) # ['hello', 'world', 'alvin', 'lpx']

# 将规则编译成对象obj,下次调用直接用obj这个规则对象来使用
# 这样就是 规则编译一次，调用多次
obj = re.compile("\d{3}")
ret5 = obj.search("abc123eeee")
print(ret5.group()) # 123
ret6 = obj.search("jsijfdis4568")
print(ret6.group()) # 456

print(re.findall("\d{3}","jsijfdis4568"))

