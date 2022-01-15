import socket
import struct
import os
import json

ip_port=("127.0.0.1",9001)
sk=socket.socket()
sk.connect(ip_port)

while 1:
    msg = input("输入执行命令>>>") # put meinv.jpg
    # 拆解命令
    cmd,params = msg.split(" ")

    if cmd == "put":

        # 传文件名,文件大小
        f = open(params,mode="rb")
        # 文件名称
        filename = f.name
        # 文件大小
        file_size = os.path.getsize(params)
        data = {}
        data["filename"] = filename
        data["file_size"] = file_size
        data["cmd"] = "put"
        msg = json.dumps(data).encode()
        msg_len = struct.pack("i",len(msg))
        # 发送文件信息
        sk.send(msg_len)
        sk.send(msg)
        # 循环上传文件数据
        for line in f:
            sk.send(line)

        f.close()

        '''
        "xxxx{"filename":xx,filesize:423,"cmd":"put"}xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        
        
        '''
