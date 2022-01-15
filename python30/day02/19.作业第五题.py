# 5、写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？

# sumNumber = 0
# for i in range(1,100):
#     # print(i)
#     if   i%2 == 0 :
#         if i != 88:
#             sumNumber -= i
#     else:
#         sumNumber += i
#
# print(sumNumber)


count = 0
for i in range(1, 100):
    if i == 88:
        continue
    elif i % 2 == 0:
        count -= i
    else:
        count += i
print(count)