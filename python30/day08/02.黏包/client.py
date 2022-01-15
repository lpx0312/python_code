# import  socket
#
#
#
#
# sock =  socket.socket(family=-1,type=-1)
#
# sock.connect(('192.168.0.113',8899))
#
# data = input('>>>')
#
# sock.send(data.encode('utf8'))
# sock.send(data.encode('utf8'))
# sock.send(data.encode('utf8'))
# sock.send(data.encode('utf8'))

import socket

sock = socket.socket()
sock.connect(('192.168.0.113',8899))
print(sock.recv(1024).decode())

while 1:
    data =  input('输入执行的命令>>>')
    sock.send(data.encode())

    total_num = sock.recv(1024).decode('utf8')
    sock.send('ok'.encode('utf8'))
    res = sock.recv(int(total_num))
    print('服务器响应：',res.decode())




