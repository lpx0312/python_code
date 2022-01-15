# 求1+2!+3!+4!+……+10!的和.
# eg：3！= 1*2*3

# sumNumber = 0
# for i in  range(1,11):
#     # print(i)
#     chengNumber = 1
#     for  j in range(1,i+1):
#         chengNumber *= j
#         # print("i={},j={},chengNumber={}".format(i,j,chengNumber))
#     sumNumber += chengNumber
# print(sumNumber)
#
#
# sum1 = 0
# for k in range(1, 11):   # 为内部循环提供值，并存储该值的阶乘结果
#     count = 1
#     for i in range(1, k + 1):   # 计算给定值的阶乘     k=3   range(1, 3 +1)  --> 1, 2 ,3
#         count = count * i     # count *= i
#     sum1 = sum1 + count
#
# print(sum1)


# 作业时  没想到
sum1 = 0
count = 1
for i in range(1, 11):
    count = count * i
    sum1 = sum1 + count
    print(count, sum1)
print(sum1)