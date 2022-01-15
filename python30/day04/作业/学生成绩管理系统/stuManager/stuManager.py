
def add_info(score_sheet):
    # print('score_sheet',score_sheet)

    """ 添加学生信息 """
    # 为了保证学号唯一，先获取所有学号
    tmp = []
    for i in score_sheet:
        tmp.append(i['学号'])
    while True:
        res1 = int(input('学号: ').strip())
        if res1 in tmp:
            print('该学号已存在')
            continue
        res2 = input('姓名: ').strip()  # 刘开 123 12 68 32 34
        res3 = int(input('年龄: ').strip())
        res4 = int(input('数学: ').strip())
        res5 = int(input('英语: ').strip())
        res6 = int(input('语文: ').strip())
        # print('姓名:res2:--'.format(res2))
        tmp_dict = {}
        tmp_dict['姓名'] = res2
        tmp_dict['学号'] = res1
        tmp_dict['年龄'] = res3
        tmp_dict['数学'] = res4
        tmp_dict['英语'] = res5
        tmp_dict['语文'] = res6
        # print('tmp_dict:--',tmp_dict)
        score_sheet.append(tmp_dict)
        del tmp_dict
        print('{}添加成功'.format(res2))
        break


def show_info(score_sheet):
    """ 根据学号查看学生信息 """
    while True:
        tmp = [i['学号'] for i in score_sheet]
        cmd = int(input('{}\n根据学号查看信息:  '.format(tmp)).strip())
        if cmd in tmp:
            for i in score_sheet:
                if i["学号"] == cmd:
                    print('姓名: {} 学号: {} 年龄: {} 语文成绩: {}  数学成绩: {} 英语成绩: {} 平均分: {:.2f}'.format(
                        i['姓名'], i['学号'], i['年龄'], i['语文'], i['数学'], i['英语'],
                        (i['语文'] + i['数学'] + i['英语']) / 3
                    ))
                    return
        else:
            print('查无学号')


def update_info(score_sheet):
    """ 根据学号更新学生信息 """
    while True:
        tmp = [i['学号'] for i in score_sheet]
        cmd = int(input('{}\n根据学号更新学生信息:  '.format(tmp)).strip())
        if cmd in tmp:
            for i in score_sheet:
                if i["学号"] == cmd:
                    # print(score_sheet.index(i), i)
                    # 学号唯一，所以，不允许修改
                    res1, res2, res3 = input('新的姓名: ').strip(), int(input('新的年龄: ').strip()), int(
                        input('新的语文成绩: ').strip())
                    res4, res5 = int(input('新的数学成绩: ').strip()), int(input('新的英语成绩: ').strip())
                    res1 = res1 if res1 else score_sheet[i]['姓名']
                    res2 = res2 if res2 else score_sheet[i]['年龄']
                    res3 = res3 if res3 else score_sheet[i]['语文']
                    res4 = res4 if res4 else score_sheet[i]['数学']
                    res5 = res5 if res5 else score_sheet[i]['英语']
                    current_index = score_sheet.index(i)
                    score_sheet[current_index] = new_dict = {
                        "姓名": res1,
                        "年龄": res2,
                        "语文": res3,
                        "数学": res4,
                        "英语": res5,
                        "学号": i['学号'],
                    }
                    # score_sheet[current_index] = new_dict
                    print('old_dict: {}\nnew_dict:{}\nupdate successful'.format(i, new_dict))
                    return


        else:
            print('查无学号')


def drop_info(score_sheet):
    """ 根据学号删除学生信息 """
    while True:
        tmp = [i['学号'] for i in score_sheet]
        cmd = int(input('{}\n根据学号删除学生信息:  '.format(tmp)).strip())
        if cmd in tmp:
            for i in score_sheet:
                if i["学号"] == cmd:
                    score_sheet.remove(i)
                    print('remove {} successful'.format(i['姓名']))
                    return
        else:
            print('查无学号')


def count_info(score_sheet):
    """ 统计信息：各学生的 平均成绩 成绩方差    班级各科及格率  平均成绩  """
    tmp_dict = {
        "考试总人数": 0,
        "语文成绩总分数": 0,
        "语文成绩及格人数": 0,
        "数学成绩总分数": 0,
        "数学成绩及格人数": 0,
        "英语成绩总分数": 0,
        "英语成绩及格人数": 0,
    }
    for i in score_sheet:
        print('{}的平均成绩: {:.2f} 成绩方差: {:.2f}'.format(
            i['姓名'],
            (i['语文'] + i['数学'] + i['英语']) / 3,
            (i['语文'] ** 2 + i['数学'] ** 2 + i['英语'] ** 2) / 3 - (((i['语文'] + i['数学'] + i['英语']) / 3) ** 2)
        ))
        tmp_dict["考试总人数"] += 1
        tmp_dict['语文成绩总分数'] += i['语文']
        tmp_dict['数学成绩总分数'] += i['数学']
        tmp_dict['英语成绩总分数'] += i['英语']
        if i['语文'] > 60:
            tmp_dict['语文成绩及格人数'] += 1
        if i['数学'] > 60:
            tmp_dict['数学成绩及格人数'] += 1
        if i['英语'] > 60:
            tmp_dict['英语成绩及格人数'] += 1
    print("""
班级各科情况汇总:
    考数学的总人数：{}  平均成绩:{:.2f}  及格率:{:.2f}%
    考语文的总人数：{}  平均成绩:{:.2f}  及格率:{:.2f}%
    考英语的总人数：{}  平均成绩:{:.2f}  及格率:{:.2f}%
    """.format(
        tmp_dict['考试总人数'], (tmp_dict["数学成绩总分数"] / tmp_dict['考试总人数']), (tmp_dict["数学成绩及格人数"] / tmp_dict['考试总人数'] * 100),
        tmp_dict['考试总人数'], (tmp_dict["语文成绩总分数"] / tmp_dict['考试总人数']), (tmp_dict["语文成绩及格人数"] / tmp_dict['考试总人数'] * 100),
        tmp_dict['考试总人数'], (tmp_dict["英语成绩总分数"] / tmp_dict['考试总人数']), (tmp_dict["英语成绩及格人数"] / tmp_dict['考试总人数'] * 100),
    ))

