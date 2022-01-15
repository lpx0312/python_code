

# # 其中查看 满江红 文件的编码格式是UTF-8 一个字符用3个字节来表示
# f = open("满江红")
# # <_io.TextIOWrapper name='满江红' mode='r' encoding='cp936'>
# # 其中 cp936代表，Windows系统的编码格式，
# # 也可以在Windows系统中，cmd中输入 chcp 来查看 Windows系统默认的 编码格式为,活动代码页: 936,
# # 936 就代表 GBK，一个字符用2个字节来表示。
# # 具体编码集：可查看 https://blog.csdn.net/zp357252539/article/details/79084480
# print(f)
# # 报错： UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 22: illegal multibyte sequence
# print(f.read())

# 满江红文件的文件编码格式是：UTF-8
# open方法，可以指定 windows操作系统 用什么格式来 解码文件，需要和文件的编码格式对齐。
# open 的model 默认是r ，r是默认读 字符


# open 语法格式
'''
def open(
    file: _OpenFile,                文件路径
    mode: str,                      mode: 可选，文件打开模式【可参考：https://www.runoob.com/python3/python3-file-methods.html】
    buffering: int = ...,           设置缓冲
    encoding: Optional[str] = ...,  编码格式
    errors: Optional[str] = ...,    报错级别
    newline: Optional[str] = ...,   区分换行符
    closefd: bool = ...,            传入的file参数类型
    opener: Optional[_Opener] = ...,设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
) -> IO[Any]: ...
'''

# open("满江红", encoding="utf-8",mode="b") 这样写会报错 一下，所以b是二进制写入，不能带encoding参数
# binary mode doesn't take an encoding argument 二进制模式不带编码参数


# f = open("满江红", encoding="utf-8", mode="r")
# print(f)
# 因为open的model是r，r是读取字符，所以这里读取2个字符，
# 如果model 是 rb，读取二进制，则read是读取2个字节b'\xe6\x80'
# print(f.read(2))

# f = open(r"D:\Users\Desktop\PxeServerCreat2.sh", encoding="utf-8")
# r"D:\Users\Desktop\PxeServerCreat2.sh" 等同于 "D:\\Users\\Desktop\\PxeServerCreat2.sh"

# f = open("满江红", mode="rb")
# # 不使用用open进行解码，
# # 我们可以适用rb模式，拿到字节，然后使用python来进行界面，并不是使用open方法，调用操作系统来解码
#
# data = f.read()  # b'\xe6\x80\x92\xe5\x8f\x91\xe5\x86\xb2\xe5\x86\xa0\xef\xbc\x8c\xe5\x87\xad\xe6\xa0\x8f\xe5\xa4\x84\xe3\x80\x81\xe6\xbd\x87\xe6\xbd\x87\xe9\x9b\xa8\xe6\xad\x87\xe3\x80\x82\xe6\x8a\xac\xe6\x9c\x9b\xe7\x9c\xbc\xe3\x80\x81\xe4\xbb\xb0\xe5\xa4\xa9\xe9\x95\xbf\xe5\x95\xb8\xef\xbc\x8c\xe5\xa3\xae\xe6\x80\x80\xe6\xbf\x80\xe7\x83\x88\xe3\x80\x82\r\n\xe4\xb8\x89\xe5\x8d\x81\xe5\x8a\x9f\xe5\x90\x8d\xe5\xb0\x98\xe4\xb8\x8e\xe5\x9c\x9f\xef\xbc\x8c\xe5\x85\xab\xe5\x8d\x83\xe9\x87\x8c\xe8\xb7\xaf\xe4\xba\x91\xe5\x92\x8c\xe6\x9c\x88\xe3\x80\x82\r\n\xe8\x8e\xab\xe7\xad\x89\xe9\x97\xb2\xe3\x80\x81\xe7\x99\xbd\xe4\xba\x86\xe5\xb0\x91\xe5\xb9\xb4\xe5\xa4\xb4\xef\xbc\x8c\xe7\xa9\xba\xe6\x82\xb2\xe5\x88\x87\xe3\x80\x82\r\n\xe9\x9d\x96\xe5\xba\xb7\xe8\x80\xbb\xef\xbc\x8c\xe7\x8a\xb9\xe6\x9c\xaa\xe9\x9b\xaa\xe3\x80\x82\xe8\x87\xa3\xe5\xad\x90\xe6\x81\xa8\xef\xbc\x8c\xe4\xbd\x95\xe6\x97\xb6\xe7\x81\xad\xe3\x80\x82\r\n\xe9\xa9\xbe\xe9\x95\xbf\xe8\xbd\xa6\xef\xbc\x8c\xe8\xb8\x8f\xe7\xa0\xb4\xe8\xb4\xba\xe5\x85\xb0\xe5\xb1\xb1\xe7\xbc\xba\xe3\x80\x82\r\n\xe5\xa3\xae\xe5\xbf\x97\xe9\xa5\xa5\xe9\xa4\x90\xe8\x83\xa1\xe8\x99\x8f\xe8\x82\x89\xef\xbc\x8c\xe7\xac\x91\xe8\xb0\x88\xe6\xb8\xb4\xe9\xa5\xae\xe5\x8c\x88\xe5\xa5\xb4\xe8\xa1\x80\xe3\x80\x82'
# # 然后将字节data ，使用decode解码为字符。解码的格式需要和文件本身的编码格式对应
# print(data.decode(encoding="utf-8"))
# print(type(data.decode(encoding="utf-8")))  #<class 'str'>

# f = open("满江红", mode="rb")
# # print(f.read(3))  # b'\xe6\x80\x92'
# # 怒 因为是rb是读取3个字节，utf-8 3个字节是一个字符，所以解码出来是一个字符
# # 但是如果 read(2)或read(4) 则会报错，因为多了或少了，解码不成完整的字符
# print(f.read(3).decode('utf-8'))
# # 等同于 下面，但是有是有 不相同，
# # 因为f.read(3)第一次读取到b'\xe6\x80\x92'，但是第二是读取f.read(3)就会读取 3-6的字节了
# print(b'\xe6\x80\x92'.decode('utf-8'))


f = open("满江红", encoding="utf-8", mode="r")

# 读取一行
# print(f.readline(2),end="") # 读取第一行 第1,2个字节，一般不这么用
# print(f.readline(2),end="") # 再次执行则 读取第一行 第 3,4个字节，一般不这么用

# print(f.readline(), end="") # 读取第一行 # 怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。
# print(f.readline(), end="") # 再次执行 读取第二行
# print(type(f.readline()), end="")    # <class 'str'>


# 读取所有行:不推荐使用，会将所有内容，存到内存中，会撑爆内存
# f.readlines()返回值是 列表
# 但是有个问题，如果前面有read()方法，则只会读取后面的所有，并不会读取全部。
# print(f.readlines())
# readlines() 读取所有行，存储在列表中，每行是一个元素
# 然后所有元素都加一个\n 换行(除了最后一个元素)
# ['怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。\n', '三十功名尘与土，八千里路云和月。\n', '莫等闲、白了少年头，空悲切。\n', '靖康耻，犹未雪。臣子恨，何时灭。\n', '驾长车，踏破贺兰山缺。\n', '壮志饥餐胡虏肉，笑谈渴饮匈奴血。']


# 故使用read和readline和readlines都是 读取之后，会接着读取后面，
# 故使用read等方法，最好读取依次，不要多次读取

# for  line in f.readlines():
#     print(line,end="")

# 循环遍历这个文件
# 使用生成器来 遍历【推荐使用这种】
# 因为内存中只存在一行的内容
# python2和python3 都是一样的 for  line in f: 都是这样的
for  line in f:
    print(line,end="")


# python2中默认的编解码方式，是ACSII码
# 所以python一般最上边需要添加 codeing = "utf8"
# print("会计师")  python如何没有说明 codeing = "utf8" 则默认ASCII码，就会乱码




# str.encode('utf-8') # 编码将字符串转化为字节
# b'\xe6\x80\x92'.decode('utf-8')  # 解码 将字节转化为  字符

# 还可以使用 bytes 进行编码
# a = bytes(s,'utf-8')
# ==》 得出的 a 的结果就是对应的字节