import  struct
import json
import  socket



sock =  socket.socket()
sock.connect(('192.168.0.113',8899))
print(sock.recv(1024).decode('utf8'))

while 1:
    # 发送消息
    try :
        cmd =  input('请输入需要查询的命令>>')
        if not cmd :continue
        sock.send(cmd.encode('utf8')) # 发送
        if cmd.encode('utf8') == 'quit':
            break
        # 先收报头长度
        # struct.unpack('i',sock.recv(4)) ==> (48,) 返回的是一个元祖
        headnum = struct.unpack('i',sock.recv(4))[0] # unpack获取 报头长度
        print('headnum::{}'.format(headnum))

        # 再收报头
        head_bytes = sock.recv(headnum) # 收过来的是 二进制 报头文件
        print('head_bytes::{}'.format(head_bytes))

        head_json = head_bytes.decode('utf8') # 转化为json字符串文件
        head_dic =  json.loads(head_json) # 将json字符串转化为python的字典 反序列化拿字典
        print('head_dic::{}'.format(head_dic))
        total_size =  head_dic['total_size'] # 拿到数据总长度
        print('total_size:::{}'.format(total_size))

        # 最后收数据
        recv_size =  0
        total_data = b''
        while recv_size<total_size: # 循环着收数据
            recv_data =  sock.recv(1024)  # 1024 只是每次收的最大限制
            recv_size += len(recv_data) # 有可能接受的不是1024，获取接受的比1024少呢
            total_data += recv_data
        # 必须是  gbk
        # 否则会报错 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc5 in position 13: invalid continuation byte
        print('返回的消息：{}'.format(total_data.decode('gbk')))
    except ConnectionError:
        print('服务端异常关闭，无发送信息到服务端，程序退出')
        break
sock.close()







