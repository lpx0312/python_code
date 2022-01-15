

list_date = [
    {"name": "张三", "age": 20, "gender": "男"},
    {"name": "李四", "age": 21, "gender": "男"},
    {"name": "王五", "age": 22, "gender": "男"}
]

def jugeNum(str):
    '''
    :param str: 传入需要判断是否是数字的字符串
    :return: 如果是能转成int类型的字符串，返回int(str),如果不能转成的，返回0
    '''
    if str.isdigit():
        return int(str)
    else:
        print("输入错误")
        return 0

def jugeGender(str):
    if str == "男" or str == "女" :
        return  str
    else:
        print("输入错误,请输入男或女")
        return  0

def jugeNameExist(name):
    '''
    判断用户是否存在
    :param name: 用户名
    :return: 存在返回(True,index)   不存在(False,index)
    '''
    for index,item in enumerate(list_date):
        for key,value in item.items():
            if name == value:
                return  (True,index)
    return (False,index)

def add_stu(list_date):
    print("*"*10,"添加学生","*"*10)
    if list_date:
        name = input("请输入需要添加的学生姓名：>>>")
        while True:
            age = jugeNum(input("请输入需要添加的学生年龄：>>>"))
            if age:
                break
        while True:
            gender = jugeGender(input("请输入需要添加的学生性别：>>>"))
            if gender:
                break
        list_date.append({"name": name, "age": age, "gender": gender})

def show_stu(list_date):
    print("*"*10,"显示所有学生","*"*10)
    for index, item in enumerate(list_date):
        print(index, item["name"], item["age"], item["gender"])



def del_stu(list_date):
    '''
    该函数，只适用于 name唯一的情况下
    :param list_date: 存储学生数据的列表
    :return: None：这里主要用户结束程序，跳出循环
    '''
    while True:
        name = input("请输入需要删除的学生姓名：>>>")
        for index, item in enumerate(list_date):
            if name == item["name"]:
                # print(index)
                list_date.pop(index) # 不能使用remove因为remover是删除 值，但是这个值是一个字典 不好删除
                print("name=[{}]的学生已经删除".format(name))
                return None
        print("输入的学生名字不存在")

def modify_stu(list_date):
    # print("*"*10,"修改学生信息","*"*10)
    while True:
        name = input("请输入需要修改的学生姓名：>>>")
        # 判断用户名是否存在
        if jugeNameExist(name)[0]:
            print("学生存在：")
            # 判断输入的学生年龄是否正确
            while True:
                age = jugeNum(input("请输入需要添加的学生年龄：>>>"))
                if age:
                    break
            # 判断输入的性别是否正确
            while True:
                gender = jugeGender(input("请输入需要添加的学生性别：>>>"))
                if gender:
                    break

            list_date[jugeNameExist(name)[1]].update({"name": name, "age": age, "gender": gender})
            break
        else:
            print("输入的姓名不存在")

def exitProgram(list_date):
    exit()

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
    {}
    请输入选择功能
    """.format("*"*30,"*"*30)).strip()
    ## 字典中放 函数
    func = {"1":add_stu,"2":show_stu,"3":del_stu,"4":modify_stu,"5":exitProgram}
    # print(func)
    if cmd1.isdigit():
        # func.get(cmd1) 获取字典中的函数名，如果想调用 还需要添加()括号 故为 func.get(cmd1)()
        func.get(cmd1)(list_date)
    else :
        print("输入错误,请输入功能序号")


# print(list_date)