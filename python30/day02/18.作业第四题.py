# 4、求偶数元素的和[1,2,1,2,3,3,6,5,8]

list1 = [1,2,1,2,3,3,6,5,8]
sumNum = 0
for i in list1:
    #print(i)
    if  i%2 == 0:
        # print("{}是偶数".format(i))
        sumNum += i
    # else:
        # print("{}不是偶数".format(i))

print(sumNum)