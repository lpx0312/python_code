
# 1.代码重复  2.耦合性

''' 函数的定义方式：
def 函数名(参数)：
    函数体
    return 返回值
'''

# 因为python是解释性语言，会逐行解释，所以函数必须写在，调用函数之前才能被加载到内存中
# 这一点适合其他 编译型语言的区别
# leijihe() 会报错

# def leijihe(start,end):
#     '''
#     :param start: 起始值
#     :param end: 结束值
#     :return: 返回累加和
#     :eg  1+2+3+..100 返回5050
#     '''
#     ret = 0
#     for i in range(start,end+1):
#         ret += i
#     # print(ret)
#     return  ret
#
# sumNumber = leijihe(1,100)
# print("sumNumber={}".format(sumNumber))

