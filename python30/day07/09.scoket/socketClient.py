import socket
import sys

# 创建客户端的socket的套接字对象
sock = socket.socket(family=-1,type = -1)

# 连接服务器
sock.connect(('192.168.0.113',11111))


# # def recv(self, bufsize: int, flags: int = ...) -> bytes:
# # bufsize 接受的最大字节数 1024 就是 1k
# res  = sock.recv(1024)
# print(res.decode('utf8'))


# 客户端:先发在收
while  1:
    try :
        shuru = input('>>>')
        sock.send(shuru.encode('utf8'))
        if shuru == 'quit':
            break
    except ConnectionResetError:
        print('服务端异常关闭，无发送信息到服务端，程序退出')
        sys.exit(0)
    try:
        recv = sock.recv(1024)
        print(recv.decode('utf8'))
    except ConnectionResetError:
        print('服务端异常关闭，无法接受到服务端消息，程序退出')
        sys.exit(0)

# ConnectionRefusedError