# <!-- s30day02作业
#
# 1 列表操作
#
# ```python
# li = ["yuan", "alvin", "ritian", "barry", "stevin"]
# # 1)列表中追加元素"seven",并输出添加后的列表
# # 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# # 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# # 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# # 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# # 6)请删除列表中的元素"yuan",并输出添加后的列表
# # 7)请删除列表中的第2至4个元素，并输出删除元素后的列表
# # 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# # 9)请将列表所有得元素反转，并输出反转后的列表
# # 10)请计算出"yuan"元素在列表li中出现的次数,并输出该次数。
# ```
# li = ["yuan", "alvin", "ritian", "barry", "stevin"]

# li.append('seven')
# print(li)

# li.insert(0, 'tony')
# print(li)

# li[1] = 'Kelly'
# print(li)
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)

# s = "qwert"
# li.extend(s)
# li.remove('yuan')

# del li[1:4]
# print(li)

# li.reverse()
# li = li[::-1]
# print(li)
#
# print(li.count('yuan'))


#
#
#
#
#
#
# 2、
#
#  ```python
# 假设有下面这样的列表：
# names = [‘baicai’,‘zhurou’,‘fentiao’,‘fish’]
# 输出的结果为：‘I have baicai,zhurou,fentiao and fish’
#  ```
names = ["baicai","zhurou","fentiao","fish"]
# s = 'i have ' + ','.join(names[0:3]) + ' and ' + names[3]
# print(s)

# print('i have %s,%s,%s and %s'% (names[0], names[1], names[2], names[3]))
# print('i have {},{},{} and {}'.format(names[0], names[1], names[2], names[3]))
# print('i have {},{},{} and {}'.format(*names))
# print(names)
# print(*names)








# 3 基于列表和字典实现学生信息管理,学生信息,比如姓名.年龄,性别存在字典中,每一个学生字典存放在一个列表中,进而实现学生信息的增删改查:
#
# ```python
# ＋－－－－－－－－－－－－－－－－－－－－－－＋
# ｜　(1) 添加学生信息　　　　　　　　　　　　　｜
# ｜　(2) 显示所有学生的信息　　　　　　　　　　｜
# ｜　(3) 删除学生信息　　　　　　　　　　　　　｜
# ｜　(4) 修改学生信息　　　　　　　　　　　　　｜
# ｜  (5) 退出程序                            |
# ｜                                         ｜
# ＋－－－－－－－－－－－－－－－－－－－－－－＋
# ```


list_data = [
    {"user": '张开', 'age': 12},
    {"user": '李开', 'age': 12},
    {"user": '陈开', 'age': 12},
]


while True:
    cmd1 = input("""
{}
＋－－－－－－－－－－－－－－－－－－－－－－＋
｜　(1) 添加学生信息　　　　　　　　　　　　　｜
｜　(2) 显示所有学生的信息　　　　　　　　　　｜
｜　(3) 删除学生信息　　　　　　　　　　　　　｜
｜　(4) 修改学生信息　　　　　　　　　　　　　｜
｜  (5) 退出程序                        |
＋－－－－－－－－－－－－－－－－－－－－－－＋
输入序号选择操作:
    """.format('*' * 60)).strip()
    if cmd1.isdigit():
        cmd1 = int(cmd1)
        if cmd1 == 1:
            user, age = input('user: ').strip(), input('age: ').strip()
            list_data.append({'user': user, 'age': age})
            print('[{}] add successful!!'.format(user))
        elif cmd1 == 2:
            if list_data:
                for index, item in enumerate(list_data, 1):
                    print('{} {} {}'.format(index, item['user'], item['age']))
            else:
                print('empty!!!!')
        elif cmd1 == 3:
            if list_data:
                for index, item in enumerate(list_data, 1):
                    print('{} {} {}'.format(index, item['user'], item['age']))
                cmd2 = input('选择要删除学生的序号: ').strip()
                if cmd2.isdigit():
                    cmd2 = int(cmd2)
                    if 1 <= cmd2 <= len(list_data):  # 确认删除的学生学号是在合法范围内
                        tmp_user = list_data.pop(cmd2-1)
                        print('[{}] delete successful!!'.format(tmp_user['user']))
                    else:
                        print('删除的学生序号不合法！！')
                else:
                    print('请输入数字！！！')
            else:
                print('empty!!没有学生可删除')
        elif cmd1 == 4:
            if list_data:
                for index, item in enumerate(list_data, 1):
                    print('{} {} {}'.format(index, item['user'], item['age']))
                cmd3 = input('选择要修改学生的序号: ').strip()
                if cmd3.isdigit():
                    cmd3 = int(cmd3)
                    if 1 <= cmd3 <= len(list_data):  # 确认修改的学生学号是在合法范围内

                        old_dict = list_data[cmd3 - 1]  # 取出老的学生信息字典： {'user': '李开', 'age': 12}
                        # 获取更新后的值
                        new_user, new_age = input('new user: ').strip(), input('new age: ').strip()
                        # 如果不想修改其中某个值，就直接回车，不要输入内容，如果直接回车，表示不更新该值，就用原来的
                        new_user = new_user if new_user else old_dict['user']
                        new_age = int(new_age) if new_age else int(old_dict['age'])
                        # 组成一个新字典，用于替换原字典
                        new_dict = {"user": new_user, 'age': new_age}
                        # 进行替换
                        list_data[cmd3 - 1] = new_dict
                        print('old: {}\nnew: {}\nupdate successful!!'.format(old_dict, new_dict))
                    else:
                        print('删除的学生序号不合法！！')
                else:
                    print('请输入数字！！！')
            else:
                print('empty!!!')
        elif cmd1 == 5:
            # print('再来呦')
            # break
            exit('再来呦')
        else:
            print('请输入一个有效的数字！！')
    else:
        print('请输入数字！！')

# 4、求偶数元素的和[1,2,1,2,3,3,6,5,8]

# count = 0
# for i in [1,2,1,2,3,3,6,5,8]:
#     if i % 2 == 0:
#         count += i
# print(count)



# 5、写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
#  1 ~ 99
# count = 0
# for i in range(1, 100):
#     if i == 88:
#         continue
#     elif i % 2 == 0:
#         count -= i
#     else:
#         count += i
# print(count)

# 6 、
#
# ```
# 求1+2!+3!+4!+……+10!的和.
# ```
# 3!    1*2*3 = 6
"""
1*1
1*1*2
1*1*2*3
1*1*2*3*4
1*1*2*3*4*5
1*1*2*3*4*5*6
1*1*2*3*4*5*6*7
1*1*2*3*4*5*6*7*8
1*1*2*3*4*5*6*7*8*9
1*1*2*3*4*5*6*7*8*9*10
"""
# # 会算每一个数的阶乘
# count = 1
# for i in range(1, 4):   # 3的阶乘
#     count *= i   # count = count * i
# print(count)
"""
3 的阶乘   1 * 2 * 3

第一次循环
count = 1   i = 1   count = count * i     --> 1
第二次循环
count = 1   i = 2   count = count * i     --> 2
第3次循环
count = 2   i = 3   count = count * i     --> 6

"""
# sum1 = 0
# for k in range(1, 11):   # 为内部循环提供值，并存储该值的阶乘结果
#     count = 1
#     for i in range(1, k + 1):   # 计算给定值的阶乘     k=3   range(1, 3 +1)  --> 1, 2 ,3
#         count = count * i     # count *= i
#     sum1 = sum1 + count
#
# print(sum1)


# sum1 = 0
# count = 1
# for i in range(1, 11):
#     count = count * i
#     sum1 = sum1 + count
#     print(count, sum1)
# print(sum1)

# 7、
#
# ```
# 编写一个程序.要求用户输入今天是星期几.根据用户的输入判定是工作日还是周末,并显示合适的问候语.
# 1.如果输入的数字不在1~7之间,则显示"请输入位于1~7之间的数".
# 2.如果用户输入的数字为6或7,则显示"周末愉快!"
# 3.对于1~5之间的数字,则显示"工作日愉快!"
# ```
# while True:
#     week = input('week: ').strip()
#     if week.lower() == 'q':
#         break
#     if week.isdigit():
#         week = int(week)
#         if 1 <= week <= 5:
#             print("工作日愉快!")
#         elif 6 <= week <= 7:
#             print('周末愉快!')
#         else:
#             print('你输入的值不在1-7之间，我很不愉快！！！')
#     else:
#         print('输入数字')


# 8、
#
# ```
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21.....,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
# 计算索引为10的斐波那契数列对应的值
# ```

# a, b = 0, 1
#
# for i in range(10):
#     print('a', a, '-------', 'b', b)
#     a, b = b, a + b


# 9、猜数游戏
#
# ```
# 程序随机内置一个位于一定范围内的数字作为猜测的结果，由用户猜测此数字。用户每猜测一次，由系统提示猜测结果：太大了、太小了或者猜对了，直到用户猜对结果或者猜测次数用完导致失败。
# 设定一个理想数字比如：66，
# 让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果正确，退出循环。
# 最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。
#
# ```

# count = 0
# random_num = 66
# while count < 3:
#     choice = input('>>: ').strip()
#     if choice.isdigit():
#         choice = int(choice)
#         if choice < random_num:
#             print("结果小了")
#         elif choice > random_num:
#             print("结果大了")
#         else:
#             print('结果正确')
#             break
#     else:
#         print('输入数字')
#
#     count += 1
#     if count == 3:
#         print('都没猜对,继续努力')
#         break
#     else:
#         print('你还有{}次机会'.format(3 - count))

# 10、
#
# ```
# (选做题)打印菱形小星星
# '''
"""
     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *
"""
count = 1
range_num = 13
for i in range(1, range_num):
    if range_num / 2 > i:  # 当宽的一半小于 i 说明要从小到大，每次加两个*
        sign = "*" * count
        print(sign.center(range_num, ' '), '-----', 'count == ', count, 'i == ', i, '半数： ', range_num / 2)
        count += 2
    else:
        sign = "*" * count
        print(sign.center(range_num, ' '), '+++++++', 'count == ', count, 'i == ', i, '半数： ', range_num / 2)
        count -= 2





# print(sign.center(13, ' '))
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
#
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
#
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
# count += 2
# sign = "*" * count
# print(sign.center(13, ' '))
#
# sign = "*" * count
# print(sign.center(13, ' '))
# count -= 2
#
# sign = "*" * count
# print(sign.center(13, ' '))
# count -= 2
