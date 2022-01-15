import  sys

# sys.exit("退出程序啦") # 退出程序
# print(help(sys.exit))

# sys.path：导包路径

# 解释器所在的平台，也就是操作系统
print(sys.platform) # win32

# python解释器版本
print(sys.version) # 3.8.6

# 启动时传入的参数， 比如 终端传参， python  '05.sys模块.py' 则sys.argv  默认是: ['05.sys模块.py']的列表
# python "05.sys模块.py" -u lpx  -m  123    ['05.sys模块.py', '-u', 'lpx', '-m', '123']
print(sys.argv)     #  ['E:/Share/PythonCode/day05/05.sys模块.py']
# sys.argv 第一个元素是程序本身路径
# python "05.sys模块.py" -u lpx  -m  123
for index,value  in enumerate(sys.argv):
    if value == '-u':
        print('用户名：{}'.format(sys.argv[index+1]))   # 用户名：lpx
    if value == '-m':
        print('密码：{}'.format(sys.argv[index + 1]))  # 密码：123
