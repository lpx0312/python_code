#注释：就是解释器 不解释的内容，会绕过注释的内容


# 单行注释 使用"#"


# 这是一个向终端打印几个Helloworld字符串
print("Hello World!")


'''
多行注释
'''

#python 里面 单引号和双引号 完全没区别
#python 不支持 注释的嵌套
"""
多行双引注释
"""

"2"
"2"
"3"
"4"
"4"
"5"


# 不算是多行单引注释 还是双引注释，都只是一个字符串而已，但是字符串1.没赋给变量  2.没打印， 但 python还是加载了，但并没有输出，就过了，

#  使用#注释，python 就直接过了，不加载（解释）这一行。

#  这里 “”“ 占据一行，且最后有回车，所以会有一个空白行
print("""    
s
2
3
4
34
3


""")
