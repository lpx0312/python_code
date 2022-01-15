# #  "D:\Users\Desktop\default"
# path = r"E:\Share\PythonCode\day03\open文件写入测试.txt"
# f = open(path,encoding="gbk",mode="w")
# f.write("测试\n")
# f.write("hah\n")
# f.writelines(["""怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。
# 三十功名尘与土，八千里路云和月。
# 莫等闲、白了少年头，空悲切。
# 靖康耻，犹未雪。臣子恨，何时灭。
# 驾长车，踏破贺兰山缺。
# 壮志饥餐胡虏肉，笑谈渴饮匈奴血。"""])
# # f.read()
# f.close()


# f = open(path,encoding="gbk",mode="r")
# for i in f :
#     print(i,end="")

# print(f.readline(1))
# print(f.readlines())

# with自动关闭f.close
# with open(path,encoding="gbk",mode="r") as f :
#     print(f.readlines())


# tell() seek()

# with open(path,mode="rb") as f :
#     # for i  in  f :
#     #     print(i.decode("gbk"),end="")
#     # print("\n")
#     # 注意使用for的生成器遍历每行内容tell()也会向后递加
#     print(f.tell()) # 223  # 0
#     print(f.read(4).decode("gbk"))
#     print(f.tell()) # 4
#     f.seek(2,1)     # 模式1 代表 从当前位置使光标偏移  默认0 ，从头开会偏移
#     print(f.tell()) # 6
#     f.seek(4)       #
#     print(f.tell(),end="") # 4
#     print(f.read(4).decode("gbk"))# ha


print("============================================")


# 元祖（） 不可变类型,也是序列
# 可以成为  不可变的列表

# tuple
t = (1,2,"ha","ss",True)
print(t)
print(t[0])
print(t[0:2])
print("ss" in t)

# 元祖的相+ *
k = t +  (1,2,3)    # (1, 2, 'ha', 'ss', True, 1, 2, 3)
h = t * 2   # (1, 2, 'ha', 'ss', True, 1, 2, 'ha', 'ss', True)
print(h)

#元祖的遍历
for i in t :
     print(i,"===============")

for i in enumerate(t):
     print(i)

# 元祖的内置方法
print(t.index("ss"))      # 1
print(t.count("s"))      #  如果没有 数量就是0

# 集合Set：特点：没有重复,无序的
# 默认是 可变类型，后面可能可变成  不可变类型
# 且集合中的值，必须是不可变类型的
s1 = {"s","kl","据了解",True,3.14}





























