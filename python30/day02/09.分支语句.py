# python没有switch case语句。和其他语言的区别

#语法：
'''
if  True :
    pass
elif False:
    pass
elif False:
    pass
else:
    pass
'''



# pass是个占位符  本身没有意义
#
# score =  input("请输入你的成绩>>>")
# print(score.isdigit()) # 如果是 -25 这个也是 False
#
# if  score.isdigit() :
#     score = int(score)
#     if score >= 90 and score <=100 :
#         print("A")
#     elif score >= 80 and score < 90 :
#         print("B")
#     elif score >= 70 and score < 80 :
#         print("C")
#     elif score >= 60 and score < 70 :
#         print("D")
#     # elif score>100 or score < 0:
#     #     print("输入的分数，有问题")
#     else:
#         print("不及格")
# else:
#     print("输入的不是分数")


# 循环输入
# 当输入q的时候退出
# while  1:
#     score =  input("请输入你的成绩>>>")
#     if score == "q" :
#         print("退出")
#         break
#     if  score.isdigit() :
#         score = int(score)
#         if score >= 90 and score <=100 :
#             print("A")
#         elif score >= 80 and score < 90 :
#             print("B")
#         elif score >= 70 and score < 80 :
#             print("C")
#         elif score >= 60 and score < 70 :
#             print("D")
#         else:
#             print("不及格")
#     else:
#         print("输入的不是分数")



# 最多连续循环录入10次，中途如果q退出，就退出，不退出就等到10次 自动退出。
# count = 0
# while  1:
#     score =  input("请输入你的成绩>>>")
#     if score == "q" :
#         print("退出")
#         break
#     if  score.isdigit() :
#         score = int(score)
#         if score >= 90 and score <=100 :
#             print("A")
#         elif score >= 80 and score < 90 :
#             print("B")
#         elif score >= 70 and score < 80 :
#             print("C")
#         elif score >= 60 and score < 70 :
#             print("D")
#         else:
#             print("不及格")
#     else:
#         print("输入的不是分数")
#     count += 1
#     if  count == 10 :
#         print("已经录入10次，程序停止")
#         break