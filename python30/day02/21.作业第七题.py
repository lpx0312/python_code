# 7、
#
# ```
# 编写一个程序.要求用户输入今天是星期几.根据用户的输入判定是工作日还是周末,并显示合适的问候语.
# 1.如果输入的数字不在1~7之间,则显示"请输入位于1~7之间的数".
# 2.如果用户输入的数字为6或7,则显示"周末愉快!"
# 3.对于1~5之间的数字,则显示"工作日愉快!"
#

while 1:
    xingqi = input("""
    {}
    请输入今天是星期几
    {}
    """.format("*"*30,"*"*30))
    if xingqi.isdigit():
        xingqi =  int(xingqi)
        if  1 <= xingqi <= 7 :
            if xingqi >=6 :
                print("周末快乐")
                break
            else:
                print("工作日愉快")
                break
        else:
            print("请输入位于1~7之间的数")
    else:
        print("请输入数字1-7")




# 建议使用这一种，少用一些 if，最多不要超过三层if
while True:
    week = input('week: ').strip()
    if week.lower() == 'q':
        break
    if week.isdigit():
        week = int(week)
        if 1 <= week <= 5:
            print("工作日愉快!")
        elif 6 <= week <= 7:
            print('周末愉快!')
        else:
            print('你输入的值不在1-7之间，我很不愉快！！！')
    else:
        print('输入数字')
