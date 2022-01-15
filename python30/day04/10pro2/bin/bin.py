
# 入口程序
import sys  # 解释器打交道的
# print(sys.path) #导包路径
# 路径就是：启动文件，所在的文件夹
import  os   # 操作系统打交道的
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print("bin",sys.path)
from  main  import main

if __name__ == '__main__':
    # print(__file__)  # 当前文件所在路径   # E:/Share/PythonCode/day04/10pro2/bin/bin.py  # 这里pycharm执行的是绝对路径，但是终端是相对路径，不准确不建议使用
    # print(os.path.abspath(__file__))    # E:\Share\PythonCode\day04\10pro2\bin\bin.py
    # print(os.path.dirname(os.path.abspath(__file__)))  # E:\Share\PythonCode\day04\10pro2\bin
    # main.run()
    main.run()