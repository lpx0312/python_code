





# #print是python内置的解释器中的函数
# # 可以使用Ctrl+点击 print可以查看源码
# # def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
print("OK1")
# print里面默认有个换行符号,如果不想换行，将参数end重新赋值为空
print("Ok2",end="")
print("OK3")



#输入函数（用于用户交互）
# input()是一个堵塞函数，等待用户输入
zhanghao = input("请输入账号：")
mima = input("请输入密码：")
# 字符串的连接符
# python的字符串连接符 不是 & 而是 +
print("账号：" +  zhanghao + "密码：" + mima)

# print如果使用,来连接，则是默认空格连接，但是如果使用+连接，则是直接连接，中间没有其他
# 这种，也只能print来使用，并不能单独使用
print("账号：",zhanghao, "密码：" , mima)

# 重赋值 原理：10这个数据在内存中开启一个空间，然后x指向这个空间的地址，
# 100又重新开辟一个内存空间，然后x将指向更改到了100的内存地址，那么10的内存空间就没有变量指向了，
# 所以10所在的内存空间就被python的垃圾处理机制给销毁了
x = 10
x = 100
print(x)


