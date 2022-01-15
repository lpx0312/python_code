import socket
import time
import struct
import json

sock = socket.socket()
sock.bind(("127.0.0.1",9001))
sock.listen(5)

while 1:
    print("server is waiting....")
    client_sock,addr = sock.accept()
    print("客户端%s建立连接"%str(addr))
    while 1:
        msg_len = client_sock.recv(4)
        msg_len = struct.unpack("i",msg_len)[0]
        info = client_sock.recv(msg_len)
        info_dict = json.loads(info)
        cmd = info_dict.get("cmd")
        print(info_dict)
        if cmd == "put":
            filename = info_dict["filename"]
            filesize = info_dict["file_size"]

            with open(filename,"wb") as f:
                # 循环接收上传数据写入到文件中
                receive_len = 0
                while receive_len < filesize:
                    print("receive_len",receive_len)
                    temp = client_sock.recv(10000000)
                    f.write(temp)
                    receive_len += len(temp)






