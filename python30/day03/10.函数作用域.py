# python作用域遵循的标准 LEGB local->encloseing（嵌套） ->global->built-in（解释器）
# python能够划分作用域的只有函数和类， 流程控制语句不能划分作用域
# 其他语言 流程控制 是可以划分作用域的【重点区别】


# def foo():
#     x = 10
#
# # print(x) # 报错

# def foo():
#     print(x) # 查询去全局global找到了x 故打印100
# x = 100
# foo()  # 100


# # built it ：是解释器级别的
# x = 100     #global
# def foo():
#     x = 10     # enclose
#     def bar():
#         x =  5  # local
#         print(x) # 5 如果x =5 去掉 ，则直接打印 会打印10
#     bar()        # 必须调用 否则不会打印
# foo() # 也必须执行 否则里面的bar函数肯定不会执行


# # python流程控制语句，不能划分作用域
# # 和其他语言的区别，【重点重点】
# x = 100
# if True:
#     x = 10  # 流程控制语句中 也是全局
# print(x)  # x = 10

#
# for i in [1,2,3,4]:
#     pass
# print(i) # 4
# 因为python中if else for while不存在开辟作用域的能力
# 且i 最后赋的值是 4 所以 i = 4





