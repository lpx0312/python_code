
# f = open("满江红",mode="r",encoding="utf8")

# tell ：返回当前光标的位置：
# seek ：光标移到某个位置

# print(f.tell())
# print(f.read(3))  # read是按照 mode=r 字符来读的
# print(f.tell())   # 9 但是tell是按照字节来走的  utf-8 一个中文字符=3个字节 所以tell走到了3*3=9
# print(f.read(3))  #
# print(f.tell())   # 18

# seek 默认是从0 开始偏移
# f.seek(9)           # utf8 9=移动9/3=3个字符
# print(f.read(3))    # 冠，凭
# f.seek(6)           # seek都是从头开始 读，并不会从上次光标位置移动。
# print(f.read(2))    # 冲冠


# # seek(偏移量，偏移模式)
# f.seek(3)  # 偏移模式默认是0，偏移模式1是当前位置开始偏移 偏移模式2：末尾位置开始便宜


# f = open("满江红",mode="r",encoding="utf8")
# # # 怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。
# print(f.read(9))       # 发冲冠，凭栏处、潇
# print(f.tell())        # 30
# f.seek(3,1)            # 再次偏移 但是会报错，因为seek的第二个参数，必须搭配mode=b或rb 二进制字节来使用
# print(f.tell())        #



#  seek和tell 对应的都是 字节，不管open的model是r还是rb
#  如果seek 要使用第二个参数，所以必须要使用open的model必须是rb
f = open("满江红",mode="rb")
# 怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。
f.seek(3)        # 1个字符
print(f.tell())   # 3
print(f.read(9).decode("utf8"))  # 因为是rb 字节模式，读取9/3=3个字符  发冲冠
print(f.tell())   # 12
f.seek(6,1)       # 1代表模式 代表从当前 位置继续偏移 6/3=2 则偏移2个字符
print(f.tell())   # 18
f.close()



