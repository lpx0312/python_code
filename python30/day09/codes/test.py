 #coding:utf-8
 # # # #
 # # # #
 # # # # # class A(object):
 # # # # #
 # # # # #     def foo(self):
 # # # # #         print("foo功能！")
 # # # # #         return self
 # # # # #
 # # # # #     def bar(self):
 # # # # #         print("bar功能！")
 # # # # #         return self
 # # # # #     def a(self):
 # # # # #         print("a")
 # # # # #     def b(self):
 # # # # #         print("b")
 # # # # #
 # # # # # a = A()
 # # # # # a.foo().bar().a().b()
 # # # #
 # # # #
 # # # # # 面试题
 # # # # # print(a is b)
 # # # # # print(a == b)
 # # # #
 # # # # # def foo():
 # # # # #     count = 0
 # # # # #     while count<4:
 # # # # #         print("OK")
 # # # # #         yield count
 # # # # #         count+=1
 # # # # #
 # # # # # gen = foo()
 # # # # #
 # # # # #
 # # # # # print(list(gen))
 # # # #
 # # # # # for i in range(10):
 # # # # #     pass
 # # # # # print(i)
 # # # #
 # # # # # # 生成器函数：带有yield关键字的函数都是生成器函数
 # # # # # def  func():
 # # # # #     print(123)
 # # # # #     yield 1
 # # # # #     print(456)
 # # # # #     yield 2
 # # # # #
 # # # # # ret = func()  # 调用生成器函数并不会执行函数内任何代码，只会返回一个生成器
 # # # # # # print(ret)    # <generator object func at 0x000001EAD82305F0>
 # # # # # print('__iter__' in dir(ret) and '__next__' in dir(ret)) # True ，返回的生成器也是迭代器
 # # # # # n = ret.__next__() # 打印123  返回值的生成器开始调用__next__方法时，才开始执行函数内的语法，返回值就是第一个yield的值
 # # # # # print(n)  # 1
 # # # # # n2 = ret.__next__()  # 打印456
 # # # # # print(n2) # 2
 # # # #
 # # # # def cloth(num):
 # # # #     for i in range(num):
 # # # #         yield '校服{}'.format(i)
 # # # #
 # # # # g = cloth(10)
 # # # # print('--->',g.__next__()) ## ---> 校服0
 # # # # for i in g:
 # # # #     print(i)  # 校服1--9
 # # # #
 # # # # def func2():
 # # # #     print('-'*10)
 # # # #     n = yield 10
 # # # #     print('-'*n)
 # # # #     yield  20
 # # # #
 # # # # g = func2()  # 返回一个生成器
 # # # # ret = g.__next__()  # 执行生成器里面内容，返回值是yield的10
 # # # # print(ret)          # 打印ret值 ==10
 # # # #
 # # # # # 发送给2也就是把2 放到上一个yield处，也就是n=2，send还有个next的作用
 # # # # # 也就是继续执行到下一个yield处返回
 # # # # ret2 = g.send(2)
 # # # # print(ret2)
 # # #
 # # #
 # # # # import time
 # # # # def func():
 # # # #     with open('file','r') as f:
 # # # #         while True:
 # # # #             line = f.readline()
 # # # #             if line.strip():
 # # # #                 yield line.strip()
 # # # #             time.sleep(1)
 # # # #
 # # # # for i in func():
 # # # #     print(i)
 # # # #
 # # #
 # # # # 计算移动平均值，send用的比较少
 # # # # 平均收益
 # # # #  0.01 0.02  0.03
 # # # #
 # # #
 # # # # def cal_average():
 # # # #     sum_num = 0
 # # # #     count = 0
 # # # #     avg = 0
 # # # #     while True:
 # # # #         if  count == 0:
 # # # #             va1 = yield  avg
 # # # #         else:
 # # # #             avg = sum_num/count
 # # # #             va1 = yield avg
 # # # #         sum_num += va1
 # # # #         count += 1
 # # #
 # # #
 # # # # def cal_average():
 # # #
 # # # #     count,sum_num,avg = 0,0,0
 # # # #     while True:
 # # # #        avg =  avg if count == 0 else sum_num/count
 # # # #        sum_num += yield avg
 # # # #        count  += 1
 # # # #
 # # # #
 # # # # g = cal_average()
 # # # # ret = g.__next__()
 # # # # # print(ret)
 # # # #
 # # # # while True:
 # # # #     num = int(input('请输入>>>'))
 # # # #     ret = g.send(num)
 # # # #     print(ret)
 # # #
 # # #
 # # # # 30以内所有能被3整除的数
 # # # mul = [ i  for i in range(30) if i%3 == 0]
 # # # print(mul)
 # # #
 # # # # 30以内所有能被3整除的数的平方
 # # # mul2 = [ i**2 for i in range(30) if i%3 == 0]
 # # # print(mul2)
 # # #
 # # #
 # # # # 找到嵌套列表中名字含有两个‘e’的所有名字-
 # # # names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
 # # #          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
 # # #
 # # #
 # # # name1 = [ j for i in names for j in i if j.count('e')== 2]
 # # # print(name1)
 # # #
 # # #
 # # # mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
 # # # m1 = { i.lower():mcase.get(i.upper(),0) + mcase.get(i.lower(),0)   for i in mcase}
 # # # print(m1)
 # # #
 # # #
 # # #
 # # # squared = {x**2 for x in [1, -1, 2]}
 # # # print(squared)
 # # #
 # # #
 # # #
 # # # l=['（alex）','（铁成）','（俊熹）','（徐鹏）','（瑞芳）']#几万个名字
 # # # g = (i.strip('（）') for i in l )# 几万个名字
 # # # print(g) # <generator object <genexpr> at 0x000001A7F659F820>
 # # # for i in g:
 # # #     print(i)
 # # #
 # #
 # # # 列表迭代器
 # # l = [1,3,4,6,78,10]
 # # ret =  reversed(l)  # 内置函数reversed返回一个 迭代器，有next方法，第二次for循环无效
 # # print(ret)  # <list_reverseiterator object at 0x0000027B7C77B070>
 # # for i in ret:
 # #     print(i)  # 打印的结果是反序的
 # #
 # #
 # # # 字典迭代器
 # # dic = {"1":1,"2":2}
 # # ret = reversed(dic)
 # # print(ret) # <dict_reversekeyiterator object at 0x000001993D5BBB30>
 # # for i in ret:
 # #     print(i)
 # #
 # #
 # # l = [1,2,3,4,5,6,7,8]
 # # l.reverse()   # 这个是列表中的一个方法，没有返回值，直接修改列表本身
 # # print(l)  # [8, 7, 6, 5, 4, 3, 2, 1]
 # #
 #
 # # f = lambda x: x if x%3 ==0 else 0
 # # print(f(3))
 #
 # # l1 = [1,3,4,5,6,9,33,65]
 # # ret = map(lambda x:x**2,l1)
 # # print(ret)
# object at 0x000001A2697EB070> # 也是一个迭代器
 # # print(list(ret))  # [1, 9, 16, 25, 36, 81, 1089, 4225]
 #
 #
 # # def func(x):
 # #     ret =  x%10
 # #     return ret
 # # l1 = [1,3,4,5,6,9,33,65]
 # # ret = sorted(l1,key=func)
 # # print(ret)
 #
 #
 #
 # # import sys
 # # # 设置递归最大深度，python默认1000，但是一般不设置，
 # # # 因为能用递归的情况，一般都在1000以下就能完成
 # # sys.setrecursionlimit(3000)
 # #
 # # num = 0
 # # def func():
 # #     global num
 # #     num += 1
 # #     print(num)
 # #     func()
 # # func()
 #
 #
 # # 实现阶乘：
 #
 # # 循环实现阶乘
 # from io import TextIOWrapper
 #
 #
 # def func(num):
 #     sum = 1
 #     for i in range(num):
 #         sum *= i+1
 #     return sum
 # print(func(3))
 #
 #
 # # 递归求阶乘
 # def mul(n):
 #     if n == 1 :
 #         return  n
 #     else   :
 #         return n*mul(n-1)
 #
 # ret = mul(5)
 # print(ret)
 #
 #
 #
 #
 #
 #
 #
 #
 # # l =[2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
 # # print(l)
 # #
 # # def search(lst,aim,start=0,end=0):
 # #     end  = end if end else len(lst)-1
 # #     mid_index = start + ((end - start)//2)
 # #     # print(mid_index,lst[mid_index])
 # #     if lst[mid_index] >aim :
 # #        return search(lst,aim,start,mid_index-1)
 # #     elif  lst[mid_index] <aim  :
 # #        return search(lst,aim,mid_index+1,end)
 # #     elif  lst[mid_index] == aim :
 # #         return  mid_index
 # #
 # # ind = search(l,66)
 # # print(ind)
 # # print(l[17])
 #
 #
 #
 #
 # # def multipliers():
 # #     print()
 # #     return [lambda x:i*x for i in range(4)]
 # # # print([m(2) for m in multipliers()])
 # #
 # # print(list(multipliers()))
 #
 # # f = [lambda x:i*x for i in range(4)]
 # # print(f)
# # # # # # # #
# # # # # # # with open('file','r',encoding='utf-8' )  as f:
# # # # # # #     # 所以这里的f 也是一个迭代器
# # # # # # #     print('__iter__' in dir(f),'__next__' in  dir(f))
# # # # # # #
# # # # # # # '''
# # # # # # # ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__',
# # # # # # # '__dict__', '__dir__', '__doc__', '__enter__',
# # # # # # # '__eq__', '__exit__', '__format__', '__ge__',
# # # # # # # '__getattribute__', '__gt__', '__hash__',
# # # # # # # '__init__', '__init_subclass__', '__iter__',
# # # # # # #  '__le__', '__lt__', '__ne__', '__new__',
# # # # # # #  '__next__', '__reduce__', '__reduce_ex__',
# # # # # # #  '__repr__', '__setattr__', '__sizeof__',
# # # # # # #  '__str__', '__subclasshook__', '_checkClosed',
# # # # # # #   '_checkReadable', '_checkSeekable', '_checkWritable',
# # # # # # #    '_finalizing', 'buffer', 'close', 'closed', 'detach',
# # # # # # #     'encoding', 'errors', 'fileno', 'flush', 'isatty',
# # # # # # #     'line_buffering', 'mode', 'name', 'newlines', 'read',
# # # # # # #     'readable', 'readline', 'readlines', 'reconfigure', 'seek',
# # # # # # #     'seekable', 'tell', 'truncate', 'writable', 'write',
# # # # # # #     'write_through', 'writelines']
# # # # # # # '''
# # # # # # #
# # # # # # #
# # # # # # # # 计算[1, -1, 2 ]计算列表中的每个值平方，自带去重功能
# # # # # # # l1 = [1, -1, 2 ]
# # # # # # # f = { i**2 for i in l1}
# # # # # # # print(list(f))
# # # # # # #
# # # # # # # #  将字典的key value 对调
# # # # # # # macase={'a':10,'b':34}
# # # # # # # f1 = {macase[i]:i for  i in macase.keys()}
# # # # # # # print(f1)
# # # # # # #
# # # # # # # #
# # # # # # # mcase={'a':10,'b':34,'A':7,'Z':3}
# # # # # # # f = { i.lower():mcase.get(i.lower(),0)+mcase.get(i.upper(),0)  for i in mcase.keys()}
# # # # # # # print(f)
# # # # # # #
# # # # # # # # 去除前后空格
# # # # # # # str='   lpx  '
# # # # # # # ret = str.strip()
# # # # # # # print(ret)        # lpx
# # # # # # # print(' ' in ret) # False
# # # # # # #
# # # # # # # # 去除前后空格和() 括号，【重点】
# # # # # # # str='(   lpx  )'
# # # # # # # ret = str.strip('() ')
# # # # # # # print(ret)        # lpx
# # # # # # # print(' ' in ret) # False
# # # # # # #
# # # # # # # # 循环数据清洗
# # # # # # # l = ['(lpx )','( wy)','(xuc )']
# # # # # # # f = [i.strip('() ') for i in l]
# # # # # # # print(f) # ['lpx', 'wy', 'xuc']
# # # # # # #
# # # # # # # print(int('1'))
# # # # # #
# # # # # # a = 1
# # # # # # print(bool(a))
# # # # # # print(int(1.11))  # 1
# # # # # # print(int(2.56))  # 2
# # # # # # print(float(a))   # 1.0
# # # # # # print(complex(1)) # (1+0j) 不重要不用记
# # # # # #
# # # # # # v1 = bin(12)
# # # # # # print(v1)
# # # # # # print(type(v1)) # <class 'str'>
# # # # # #
# # # # # # v2 = int(v1,base=2)
# # # # # # print(v2)
# # # # # # print(type(v2)) # <class 'int'>
# # # # # #
# # # # # # print(0b101)        # 5
# # # # # # print(type(0b101))  # <class 'int'>
# # # # # # print(pow(2,3,3))
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # # #
# # # # # # l1 = [-10,2,-4,5]
# # # # # # print(max(l1))  # 5
# # # # # # print(min(l1))  # -10
# # # # # # # key代表每个迭代器中的每个元素，按照什么函数进行比较
# # # # # # print(max(l1,key=abs))  # -10
# # # # # # print(min(l1,key=abs))  #  2
# # # # # #
# # # # # #
# # # # # #
# # # # # # print(min(1,2,-3))
# # # # # #
# # # # # # #sum(iterable,start)
# # # # # # # print(sum({1:1,2:23}.values()))
# # # # # #
# # # # # # l1 = [1,2,-3,4]
# # # # # # print(sum(l1))     # 4
# # # # # # print(sum(l1,10))  # 14
# # # # # #
# # # # # #
# # # # # # print(max(1, -3, 2, key=abs))
# # # # # #
# # # # # # print(tuple([1,2,4]) )
# # # # # #
# # # # # # l1 = [2,1,4,7]
# # # # # # f = reversed(l1)
# # # # # # print(list(f))  # [7, 4, 1, 2]
# # # # # #
# # # # # # a = ("a", "b", "c", "d", "e", "f", "g", "h")
# # # # # # x = slice(0, 8, 3)
# # # # # # print(a[x])  # ('a', 'd', 'g')
# # # # #
# # # # # # l1 = [1,2,-3,4]
# # # # # # print(str(l1))
# # # # # # print(type(str(l1)))
# # # # # #
# # # # # # str1='False'
# # # # # # print(bool(str1))
# # # # #
# # # # #
# # # # #
# # # # # with open('file','rb') as f:
# # # # #     for line in f:
# # # # #         print(type(line)) #
# # # # #         print(line.decode('utf-8'))
# # # # #
# # # # #
# # # # # # 字符串编码
# # # # # print('升级'.encode('utf-8')) # b'\xe5\x8d\x87\xe7\xba\xa7'
# # # # # print(bytes('升级','utf-8'))  # b'\xe5\x8d\x87\xe7\xba\xa7'
# # # # # # 字符串，encode 编码
# # # # # # bytes.decode 解码
# # # # # print('升级'.encode('utf-8').decode('utf-8'))  #升级
# # # # #
# # # # # print(bytearray('升级', encoding='utf-8'))
# # # #
# # # # print(ord('a'))  # 97
# # # # print(chr(98))   # b
# # # # print(type(ascii('lpx')))
# # #
# # # a =  1
# # # b = 2
# # # print(locals())  # 局部在全局就是全局  a b
# # # print(globals()) # 全局  a b
# # # def func():
# # #      c = 3
# # #      d = 4
# # #      print(locals())    # 局部变量  c d
# # #      print(globals())   # 全局  a b ，不管在哪都是全局
# # #
# # #
# # # help()
# #
# #
# # # def add(n, i):
# # #     return n + i
# # # def test():
# # #     for i in range(4):
# # #         yield i
# # # g = test()
# # # for n in [1, 50]:
# # #     g = (add(n, i) for i in g)
# # # print(list(g))
# #
# # n = 1
# # g =  (n+i for i in (0,1,2,3))
# # n = 10
# # g = (n+i for i in g)
# # print(list(g))
# #
# #
# # def multipliers():
# #     return [lambda x:i*x for i in range(4)]
# # print([m(2) for m in [lambda x:i*x for i in range(4)] ])
# #
# # def num():
# #     sub = []
# #     for i in range(4):
# #         def num2(x):
# #             return x * i
# #         sub.append(num2)
# #     return sub
# # for m in  num():
# #     print(m(2))
# #
# # # print([m(2) for m in num()])
# #
# #
# # # sub=[]
# # # for i in [1,2,3,4]:
# # #     sub.append(i)
#
#
# # from datetime import datetime
# # d = datetime.now()
# # print(d.strftime('%Y-%m-%d %H:%M:%S'))
#
# path = '/home/lpx/pic'
# dir_list = [path]
# path = dir_list.pop()
# print(path)
#
#
#

# import re
# # findall是返回所有能匹配上的项，所组成的列表，如果匹配不到.group取值会报错
# ret = re.findall('\d{3}','akksjkdjsk123kkjhkjh1224khkj723')
# print(ret)  # ['123', '122', '723']
# ret = re.search('\d{3}','akksjkdjsk123kkjhkjh1224khkj723')
#
# # search永远只返回能匹配的第一项，需要.group取值，如果匹配不到.group取值会报错
# print(ret)  # <re.Match object; span=(10, 13), match='123'>
# print(ret.group())
#
# # match永远只会从头开始匹配,需要.group取值
# ret = re.match('\d{3}','akksjkdjsk123kkjhkjh1224khkj723')
# print(ret)   # None
# ret = re.match('\d{3}','123akksjkdjsk123kkjhkjh1224khkj723')
# print(ret)   # None
# print(ret.group()) # None
#
#
# # findall优先显示，优先显示括号分组内的内容
# ret = re.findall('\d(\d)','akksjkdjsk123kkjhkjh1224khkj723')
# print(ret)   # 匹配两个数，但会优先显示第二个 ['2', '2', '4', '2']
# ret = re.findall('\d(?:\d)','akksjkdjsk123kkjhkjh1224khkj723')
# print(ret)   # 在分组中使用?:取消，分组的优先显示 ['12', '12', '24', '72']
#


# 序列化的作用
    # 硬盘上的存储：存储在数据库里，文件里
    # 网络上的传输

# import json
# d = {"name":"李攀祥","age":(1,2),"hobby":None}
# # dumps序列化方法，
# print(json.dumps(d,ensure_ascii=False,indent=4))  # 和json格式是一样的，indent就是间隔，也就是json字符串的格式化，ensure_ascii=False表示开启utf-8
# with open('dic_test','w',encoding='utf-8') as f:
#     f.write(json.dumps(d,ensure_ascii=False,indent=4))
#
# '''
# {
#     "name": "李攀祥",
#     "age": 18,
#     "hobby": null
# }
# '''

# import json
# # loads反序列化
# with open('dic_test','r',encoding='utf-8') as f:
#     ret = f.read()
#
# dic = json.loads(ret)
# print(dic)  #  {'name': '张三', 'age': 18, 'hobby': None}
# import pickle
# import time
#
# ret = time.localtime()
# # <class 'time.struct_time'>
#
# dic = {"k":ret,"k2":1,"k3":'','name':'张三'}
#
# with open('file_test','wb') as f:
#     pickle.dump(dic,f)
#
#
# with open('file_test','rb') as f:
#    dict =  pickle.load(f)
# print(dict['k'][5])
#
#
#
#

#
# with open('dic_test','r',encoding='utf-8') as f:
#     dic = json.load(f)
# print(dic)

'''file
{"username":"张三","password":"1"}
{"username":"李四","password":"2"}
{"username":"王五","password":"3"}
{"username":"孙六","password":"4"}
'''


# import  json
# # 读取
# with open('file','r',encoding='utf-8') as f:
#     ret =  { i :json.loads(line)  for i,line in enumerate(f,1)}
#
# # 写入
# dict = {'username': '焊机', 'password': '5'}
# with open('file','a',encoding='utf-8') as f :
#     f.write(json.dumps(dict,ensure_ascii=False))
#


# def get_section(config,itemname):
#     '''
#     根据配置项名字，获取所在组section
#     :param config:ConfigParser的实例对象
#     :param itemname:配置项名
#     :return:返回所在组名的列表
#     '''
#     ret = []
#     for i in config:
#         if itemname in config[i]:
#             ret.append(i)
#     return ret

# import configparser
# config = configparser.ConfigParser()






# config.read('example.ini')
# print(get_section(config,'host port2'))
#
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w',encoding='utf-8') as f:
#    config.write(f)

# print(type(config))
# print(config.sections())   # 没有读取文件之前，section是空的
# print(dict(config))   # config读取文件后，类似于字典的形式，可以直接转化为字典，
# print(dict(config).keys())  #
# print(config.sections())   # 没有读取文件之前，section是空的 ,config的sections就相当于 ，dict字典的keys(),默认的config也是默认的
#
# print('bitbucket.org' in config)
# print('bitbucket.org' in dict(config))

# print(config['bitbucket.org']['user'])
# print(config['bitbucket.org']['user2']) # 如果值不存在会报错


# print(config['bitbucket.org'])          #<Section: bitbucket.org> section对象其实也是一个字典

# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)

# 同for循环,找到'bitbucket.org'下所有键，返回的是列表，
# print(config.options('bitbucket.org'))
# print(dict(dict(config)['bitbucket.org']).keys())


# config.remove_section('bitbucket.org')
# config.add_section()
# print(config)




# config.write(open('example.ini', "w"))


# def get_section(config,itemKey):
#     return  [ i for i in config.sections() if config.has_option(i,itemKey)]
#
#
# # 需要修改的配置项
# dict = {"upload_max_filesize":"200M","post_max_size":"200M"}
#
# import ConfigParser
# import sys
# conf =  ConfigParser.ConfigParser()
# conf.read('php.ini')
#
# for k,v in dict.items():
#     section = get_section(conf,k)
#     if section:
#         if len(section) == 1 :
#             value = conf.get(section[0],k)
#             if not value == v:
#                 conf.set(section[0],k,v)
#                 print '{}由{}更改为{}'.format(k,value,v)
#             else:
#                 print '{}无需更改'.format(v)
#         else:
#             print '指定的参数不明确，程序退出'
#             sys.exit()
#
# conf.write(open('php.ini','w'))

 # print conf.get('PHP','auto_append_file')

# 判断是否是迭代器
from collections import Iterator
# 判断是否是生成器
from inspect import isgenerator

f = open('php.ini','r')
l = [1,2]
l2 =( i  for i in range(10))
def foo():
    yield 1
    yield 2


print isinstance(f, Iterator)  # True  文件句柄是一个迭代器
print isinstance(l, Iterator)  # False l只是迭代器对象，迭代器和迭代对象是不一样的，

print isgenerator(f)         # False 说明f文件句柄，不是生成器
print isgenerator(l2)         # True
print isgenerator(foo)       # False 生成器函数不调用，不会返回生成器,只是一个变量指向一个特定的内存地址
print isgenerator(foo())      # True


import  yaml
