# w 写入文件句柄
f = open("满江红2.txt",mode= "w")  # 操作系统用的是 gbk 打开的,所以创建的也是gbk编码的文件
f.write("怒发冲冠为红颜")            # 则写入的字符串 就是 gbk的编码
f.close()
# 上面这样写 会新建 满江红2.txt
# 但是内容会乱码 ŭ�����Ϊ����
# 因为pycharm打开这个满江红2.txt文件时，默认的解码是 utf-8的，不对齐，所以就会乱码

# 注意：ANSI在中文操作系统默认是gb2312
# 解决方法：有两种
# 1.使用默认打开文件模式是 GBK的，可以在资源管理器中 找到文件使用 notepad打开
# 2.创建文件时，就使用utf-8创建，则文件编码格式就是，utf-8，且pycharm默认打开是utf-8编码，就不会乱码了


# mode = w  覆盖写
f = open("满江红3.txt",mode= "w",encoding="utf8")
f.write("怒发冲冠为红颜\n")
f.write("怒发冲冠为红颜\n")
f.close()

# mode = a 是追加写
f = open("满江红3.txt",mode= "a",encoding="utf8")
f.write("是否是追加\n")
# writelines 使用的意义不大
f.writelines(["111\n","222"])
f.close()




