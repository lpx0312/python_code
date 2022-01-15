# 9、猜数游戏
#
# ```
# 程序随机内置一个位于一定范围内的数字作为猜测的结果，由用户猜测此数字。用户每猜测一次，由系统提示猜测结果：太大了、太小了或者猜对了，直到用户猜对结果或者猜测次数用完导致失败。
# 设定一个理想数字比如：66，
# 让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果正确，退出循环。
# 最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。
# ```

number = 66

count = 0
while 1:
    cai = input("""请输入数字>>>""")
    # isdigit 方法：如果是-10 负数，则是False，“ss”也是False
    count += 1
    if cai.isdigit():
        cai = int(cai)
        if cai > number:
            print("太大了")
        elif cai < number:
            print("太小了")
        elif cai == number :
            print("猜对了")
            break
    else:
        print("输入的不是数字，请重新输入")

    if   count == 3:
        print("输入次数已用完")
        break



