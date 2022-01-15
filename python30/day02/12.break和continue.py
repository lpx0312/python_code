# break：退出整个while循环

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


# continue:退出当次循环，进入下一循环
counter = 0
while  counter < 100:
    counter += 1
    if  counter == 88 :
        continue
    print(counter)
