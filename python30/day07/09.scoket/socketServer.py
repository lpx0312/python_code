def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


#  网编三要素：
#  IP  端口  协议


import  socket
import time
# （1）创建socket套接字对象
# socket 的 def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
sock = socket.socket(family=-1,type=-1)  # family=-1 =>IPV4   type =  SOCK_STREAM 这两个都是默认的 可以不写

# （2）绑定:服务端的IP和端口
# 注意要绑定实际IP 不要绑定127.0.0.1 或localhost等，因为客户端找的是服务端的IP，
# 如果这里填写localhost或127.0.0.1 客户端会报错ConnectionRefusedError: [WinError 10061]
sock.bind((get_host_ip(),11111))

# （3）确定最大监听数
sock.listen(5)  # socket 是 一个一个连接，连接一个其余的及时等待，表示 listen正在等待排队的  不包括 已经连接的

# （4）等待连接
print('服务器等待连接')
# accept 返回了 return sock, addr
# sock（conn）是客户端的套接字对象 addr是客户端的IP和端口




# 服务端：先收后发
while 1:  # 这个循环用于，当一个用户连接端口后，接收下一个用户
    print('服务器开始等待连接：：')
    conn, addr = sock.accept()
    print('conn:{}\n'.format(conn),'addr:{}'.format(addr ))

    # conn: 发送消息send方法  接收数据recv方法
    # send(字节串)
    # date =  "欢迎连接本服务器".encode('utf8')
    # conn.send(date)

    while 1:
        try:
            msg = conn.recv(1024)
            print(msg.decode('utf8'))
        except ConnectionError:
            print('客户端已异常断开，无法将消息收到客户端消息')
            print('等待2s，重新等待客户端连接')
            time.sleep(2)
            break

        if msg.decode('utf8') == 'quit':
            break

        try:
            res = input('响应：>>>')
            conn.send(res.encode('utf8'))
        except ConnectionError:
            print('客户端已异常断开，无法将消息发送到客户端')
            print('等待2s，重新等待客户端连接')
            time.sleep(2)
            break

