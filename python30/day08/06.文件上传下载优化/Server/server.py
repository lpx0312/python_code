import socket
import  struct
import  json
import  hashlib
import  os
import  re
# from urlparse import  *
from urllib.parse import urlparse
import nturl2path


def send_head_dic(head_dic,coding):
    '''
        将报头的python字典制作为固定长度的报头字节数和报头二进制文件
    :param head_dic: 报头的python字典
    :param encoding: json序列化的编码方式
    :return:pack加密的固定包头字节数，报头json序列化后的二进制文件
    '''
    file_json = json.dumps(head_dic)  # 序列化获取json字符串
    file_bytes = file_json.encode(coding)  # json字符串转化为二进制
    head_lengh_struct = struct.pack('i', len(file_bytes))
    return head_lengh_struct, file_bytes

def get_hostip():
    s =  socket.socket(family = socket.AF_INET,type=socket.SOCK_DGRAM)
    try :
        s.connect(('8.8.8.8',80))
        IP =  s.getsockname()[0]
    except:
        s.close()
    return  IP


def get_md5(filepath):
    has  =  hashlib.md5('加盐'.encode('utf8'))
    with open(filepath,'rb') as f:
        for line  in   f:
            has.update(line)
    return has.hexdigest()

def put_file(conn,file_size,file_name,file_md5):
    with open(file_name, "wb") as f:
        # 循环接收上传数据写入到文件中
        receive_len = 0
        while receive_len < file_size:
            # print("receive_len", receive_len)
            temp = conn.recv(10000000)
            f.write(temp)
            receive_len += len(temp)
        # f.write('13s4131431435434'.encode('utf8')) #测试md5


    # 最好不能这样，因为如果没有接收的长度，发过去容易出问题
    # 如果想返回，则需要要传发送的字符串长度过去
    # 或者返回固定长度的信息【不太准确】，我这里就是这么做的
    if get_md5(file_name) == file_md5:
        print('md5值相同，文件完整')

        s2 = send_head_dic({"file_name":file_name,"isMd5OK":"OK","status":"ok","type":"put"},'utf8')

        conn.send(s2[0])
        conn.send(s2[1])
    else:
        print('md5值不相同，文件可能被更改过')
        conn.send('文件上传完成，md5值不同，文件损坏'.format(file_name).encode('utf8'))


def jugeURL(url):
    Base_IP = r'E:\Apache24\htdocs'
    res = urlparse(url)
    print()
    if res[1] == get_hostip():
        print('主机名正确')
        # 主机名（域名）正确
        path_name = nturl2path.url2pathname(res[2]) # 将uri地址更改为path
        total_path =  Base_IP + path_name
        if os.path.exists(total_path):
            return total_path
        else:
            print('{}文件不存在'.format(total_path))
            return None
    else:
        print('主机名不正确')
        return None


def get_file(conn, file_name):
    total_path  =  jugeURL(file_name)
    print(total_path)
    if  total_path :
        # 上传之前应该确认 文件大小  文件名
        file_size = os.path.getsize(total_path)  # 文件大小
        file_name = os.path.split(total_path)[1]  # 文件名
        file_md5 = get_md5(total_path)  # 加盐后的md5值

        file_dic = {
            'file_size': file_size,
            'file_name': file_name,
            'file_md5': file_md5,
        }
        file_json = json.dumps(file_dic)  # 序列化获取json字符串
        file_bytes = file_json.encode('utf8')  # json字符串转化为二进制
        # # 先发送表头信息【4个字节】
        conn.send(struct.pack('i', len(file_bytes)))  #
        conn.send(file_bytes)  # 发送表头数据

        print(file_json)
        # 发送文件数据
        with open(total_path, 'rb') as f:
            for line in f:
                conn.send(line)
    else:
        print('文件不存在')

import sys
host_IP = (get_hostip(),9000)
# print(host_IP)
with  socket.socket() as s :
    s.bind(host_IP)
    s.listen(5)

    while 1:
        conn,addr = s.accept()
        # conn.send('欢迎{}连接本服务器{}'.format(addr[0],host_IP[0]).encode('utf8'))
        # file_name, file_md5 = recv_file(conn)

        while  1:
            head_length = struct.unpack('i', conn.recv(4))[0]  # 接收表头长度数据
            # print('堵塞了吗？')
            # print('head_length::{}'.format(head_length))
            json_bytes = conn.recv(head_length)  # 获取json二进制
            # print('json_bytes:::{}'.format(json_bytes))
            # json_str = json_bytes.decode('utf8','ignore')  # 获取json字符串
            # print(json_str)
            json_dic = json.loads(json_bytes)  # 反序列化json获取python字典,loads参数可以是二进制也可以是str
            print(json_dic)
            file_name = json_dic['file_name']  # 文件名
            file_size = json_dic['file_size']  # 文件大小
            file_md5 = json_dic['file_md5']  # 文件加盐后的md5
            type = json_dic['type']

            if type =='put':
                put_file(conn, file_size, file_name, file_md5)
            elif type =='get':
                get_file(conn, file_name)
                # sys.exit(0)





