#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：04_subprocess模块【推荐】.py
@Author  ：lipanxiang
@Date    ：2022/4/21 8:07 
'''


'''
Subprocess是一个功能强大的子进程管理模块，是替换os.system ,os.spawn* 等方法的一个模块。

'''

'''
subprocess模块是python从2.4版本开始引入的模块，也是系统自带的，不需要再额外安装了。
主要用来取代 一些旧的模块方法，如os.system、os.spawn*、os.popen*、commands.*等。
subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。

当执行命令的参数或者返回中包含了中文文字，那么建议使用subprocess。

如果命令是 字符串 必须设置 shell=True 
如果命令是 列表['ls', '-l']   可以不用设置shell 因为默认就是 False

参考: https://www.cnblogs.com/zhou2019/p/10582716.html#:~:text=subprocess%E6%A8%A1%E5%9D%97%20subprocess%E6%98%AFPython,2.4%E4%B8%AD%E6%96%B0%E5%A2%9E%E7%9A%84%E4%B8%80%E4%B8%AA%E6%A8%A1%E5%9D%97%EF%BC%8C%E5%AE%83%E5%85%81%E8%AE%B8%E4%BD%A0%E7%94%9F%E6%88%90%E6%96%B0%E7%9A%84%E8%BF%9B%E7%A8%8B%EF%BC%8C%E8%BF%9E%E6%8E%A5%E5%88%B0%E5%AE%83%E4%BB%AC%E7%9A%84%20input%2Foutput%2Ferror%20%E7%AE%A1%E9%81%93%EF%BC%8C%E5%B9%B6%E8%8E%B7%E5%8F%96%E5%AE%83%E4%BB%AC%E7%9A%84%E8%BF%94%E5%9B%9E%EF%BC%88%E7%8A%B6%E6%80%81%EF%BC%89%E7%A0%81%E3%80%82
'''

'''
总结:
那么我们到底该用哪个模块、哪个函数来执行命令与系统及系统进行交互呢？下面我们来做个总结：

首先应该知道的是，Python2.4版本引入了subprocess模块用来替换os.system()、os.popen()、os.spawn*()等函数以及commands模块；也就是说如果你使用的是Python 2.4及以上的版本就应该使用subprocess模块了。

如果你的应用使用的Python 2.4以上，但是是Python 3.5以下的版本，
Python官方给出的建议是使用subprocess.call()函数。Python 2.5中新增了一个subprocess.check_call()函数，
Python 2.7中新增了一个subprocess.check_output()函数，这两个函数也可以按照需求进行使用。

如果你的应用使用的是Python 3.5及以上的版本（目前应该还很少），
Python官方给出的建议是尽量使用subprocess.run()函数。

当subprocess.call()、subprocess.check_call()、subprocess.check_output()和subprocess.run()这些高级函数无法满足需求时，
我们可以使用subprocess.Popen类来实现我们需要的复杂功能。
'''


#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 推荐subprocess.Popen方法 【通用 推荐】

import subprocess
cmd = "sh ~/2.sh"
res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(res.stdout.read()) 这种也可以获取 屏幕输出
# print(res.stderr.read())
std_out, std_err = res.communicate()  # 推荐使用这种
if not std_err :
    print('成功')
    print('命令输出')
    print(std_out)
else:
    print("命令执行出错")


# subprocess.run  python3.5 之后使用
'''
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')
'''




# subprocess.call() 相当于 os.system() 命令的用法，它执行命令并将执行结果状态码返回。 # python 2.5 -3.5 之间使用
res=subprocess.call('cat /etc/hosts',shell=True)
'''
命令输出结果
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.0.0.30   gitlab.lpx.com
'''
print(res)
'''
0 命令执行结果
'''

# subprocess.getstatusoutput(cmd)  也是python3 之后才有这个功能，也不推荐
# 可以获取命令执行结果和命令执行输出（屏幕输出）
retcode, output = subprocess.getstatusoutput('ls -l /test')
print(retcode)
print(output)


# subprocess.check_call()：用法与subprocess.call()类似，区别是，当返回值不为0时，直接抛出异常，这里不再赘述了
# subprocess.check_output()：用法与上面两个方法类似，区别是，如果当返回值为0时，直接返回输出结果，如果返回值不为0，直接抛出异常。需要说明的是，该方法在python3.x中才有。









