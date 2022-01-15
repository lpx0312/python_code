# 3 基于列表和字典实现学生信息管理,学生信息,比如姓名.年龄,性别存在字典中,
# 每一个学生字典存放在一个列表中,进而实现学生信息的增删改查:
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

list_date = [
    {"name": "张三", "age": 20, "gender": "男"},
    {"name": "李四", "age": 21, "gender": "男"},
    {"name": "王五", "age": 22, "gender": "男"}
]



cmd1 = input("""
{}
＋－－－－－－－－－－－－－－－－－－－－－－＋
｜　(1) 添加学生信息　　　　　　　　　　　　　｜
｜　(2) 显示所有学生的信息　　　　　　　　　　｜
｜　(3) 删除学生信息　　　　　　　　　　　　　｜
｜　(4) 修改学生信息　　　　　　　　　　　　　｜
｜  (5) 退出程序                        |
｜                                     ｜
＋－－－－－－－－－－－－－－－－－－－－－－＋
{}
请输入选择功能
""".format("*"*30,"*"*30)).strip()
print(cmd1)
if  cmd1.isdigit():
    num1 = int(cmd1)
    if num1 == 1:   # 添加学生信息
        #添加学生之前，先显示所有用户
        for index, item in enumerate(list_date):
            print(index, item["name"], item["age"], item["gender"])

        name = input("""请输入name >>>""".strip())

        # 校验 年龄
        while 1:
            age = input("""请输入age >>>""".strip())
            if age.isdigit():
                age = int(age)
                break
            else:
                print("请重新输入正确的age")
        # 校验 性别
        while 1:
            gender = input("""请输入gender >>>""".strip())
            if  gender == "男" or gender == "女":
                break
            else:
                print("请输入正确的性别(男/女)")

        dict1 = {"name":name,"age":age,"gender":gender}
        list_date.append(dict1)
        print("[{}]已经添加成功".format(name))

    if num1 == 2:   # 显示所有学生的信息
        if list_date:
            for index, item in enumerate(list_date):
                print(index, item["name"], item["age"], item["gender"])
        else:
            print("没有学生")
    if num1 == 3:   # 删除学生信息
        if list_date:
            # 删除学生之前，先显示所有用户
            for index, item in enumerate(list_date):
                print(index, item["name"], item["age"], item["gender"])
            while 1:
                name = input("""请输入需要删除的name >>>""".strip())
                delindex = -1
                for index, item in enumerate(list_date):
                    if name == item["name"]:
                        delindex = index
                if delindex != -1:
                    del list_date[delindex]
                    print("[{}]已经删除]".format(name))
                    break
                else:
                    print("输入的名字不存在，不能删除，请重新输入")
        else:
            print("没有学生")

    if num1 == 4:   # 修改学生信息
        if list_date:
            # 修改学生之前，先显示所有用户
            for index, item in enumerate(list_date):
                print(index, item["name"], item["age"], item["gender"])
            while 1:
                name = input("""请输入需要修改的name >>>""".strip())
                delindex = -1
                for index, item in enumerate(list_date):
                    if name == item["name"]:
                        delindex = index
                if delindex != -1:
                    list_date[delindex]["name"] = input("""请输入需要修改后的name >>>""".strip())
                    list_date[delindex]["age"] = input("""请输入需要修改后的age >>>""".strip())
                    list_date[delindex]["gender"] = input("""请输入修改后的gender >>>""".strip())
                    print("[{}]信息已修改]".format(name).strip())
                    print("修改后数据为：{} {} {} ".format(list_date[delindex]["name"],list_date[delindex]["age"],list_date[delindex]["gender"]))
                    break
                else:
                    print("输入的名字不存在，不能修改，请重新输入")
        else:
            print("没有学生")
    if num1 == 5:   # 退出程序
        exit('再来呦')
else:
    "请输入正确数字"



print(list_date)

