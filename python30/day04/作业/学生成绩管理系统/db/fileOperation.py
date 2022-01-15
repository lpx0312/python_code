import os
PATH = os.path.dirname(os.path.abspath(__file__)) + r'\\info.txt'
score_sheet = [
    # {'姓名': '张开', '学号': 123, '年龄': 18, '数学': 35.0, '语文': 92.0, '英语': 88.0},
    # {'姓名': '李开', '学号': 234, '年龄': 18, '数学': 95.0, '语文': 22.0, '英语': 78.0},
    # {'姓名': '王开', '学号': 345, '年龄': 20, '数学': 66.0, '语文': 22.0, '英语': 8.0}
]


def read_file():
    print()
    with open(PATH, 'r', encoding='utf-8') as f:
        title = f.readline().strip().split(',')  # ['姓名', '学号', '年龄', '数学', '语文', '英语']
        # print(title)
        for line in f:
            line = line.strip().split(',')  # ['张开', '123', '18', '35', '92', '88']
            d = {
                title[0]: line[0],
                title[1]: int(line[1]),
                title[2]: int(line[2]),
                title[3]: int(line[3]),
                title[4]: int(line[4]),
                title[5]: int(line[5]),
            }
            score_sheet.append(d)
            # print(score_sheet)
    print(score_sheet)
    return  score_sheet

def save_data(score_sheet):
    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(','.join(score_sheet[0].keys()) + '\n')
        for item in score_sheet:
            f.write(','.join([str(i) for i in item.values()]) + '\n')


def save_file(score_sheet):
    print("{}:{}".format("save_file",score_sheet))
    """ 保存学生信息 """
    save_data(score_sheet)
    print('数据保存成功')


if __name__ == '__main__':
    # read_file()
    save_file(score_sheet)