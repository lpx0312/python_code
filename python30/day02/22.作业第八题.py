# 8、
#
# ```
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21.....,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
# 计算索引为10的斐波那契数列对应的值
# ```


# 自己的做法
# first = 0
# second = 1
# value = 0
# m = 10
#
# for i in range(3,m+1):
#     if  i%2 == 0:
#         second = second + first
#         # print(second)
#     else:
#         first = first + second
#         # print(first)
#     if m%2 == 0 :
#         value = second
#     else:
#         value = first
#
# print(value)


# 待参考
a, b = 0, 1

for i in range(10):
    print('a', a, '-------', 'b', b)
    a, b = b, a + b