# __all__ =  ['x']
#
# x = 10
# y = 100


from  db import  fileOperation as myfile
from  stuManager import  stuManager as stuM


# 逻辑功能



def q(score_sheet):
    """ 退出系统 """
    myfile.save_data(score_sheet)
    exit('退出系统辣')


def start():
    """ 入口函数 """
    # 获取学生列表
    score_sheet = myfile.read_file()
    while True:
        # tmp_dict = {
        #     1: ['添加学生信息', add_info],
        #     2: ['根据学号查看学生信息', show_info],
        #     3: ['根据学号更新学生信息', update_info],
        #     4: ['根据学号删除学生信息', drop_info],
        #     5: ['统计信息', count_info],
        #     6: ['保存学生信息', save_file],
        #     7: ['退出系统', q],
        # }

        print("""
1: 添加学生信息
2: 根据学号查看学生信息
3: 根据学号更新学生信息
4: 根据学号删除学生信息
5: 统计信息
6: 保存学生信息
7: 退出系统
        """)
        cmd = input('\n根据序号选择操作: ').strip()
        if cmd.isdigit():
            cmd = int(cmd)
            if cmd == 1:
                stuM.add_info(score_sheet)
            elif cmd == 2:
                stuM.show_info(score_sheet)
            elif cmd == 3:
                stuM.update_info(score_sheet)
            elif cmd == 4:
                stuM.drop_info(score_sheet)
            elif cmd == 5:
                stuM.count_info(score_sheet)
            elif cmd == 6:
                myfile.save_file(score_sheet)
            elif cmd == 7:
                q(score_sheet)
            else:
                print('请输入一个合理的序号')
        else:
            print('请输入一个数字')

