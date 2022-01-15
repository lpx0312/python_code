import socket
import struct
import json
import hashlib
import os
# import  re
# from urlparse import  *
from urllib.parse import urlparse
import nturl2path
from pathlib import Path


def get_hostip():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    IP = ""
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except:
        s.close()
    return IP

def url_get_local_path(url,html_base_dir):
    '''
    传入url和html家目录，返回请求服务器本地地址
    :param url:请求的网址
    :param html_base_dir:服务器本地的html所在的家目录
    :return:返回解析的状态和请求的地址
        exist = 1:代表 域名正确，且所需文件存在
        exist = 0：代表 域名正确,但所需文件不存在
        exist = -1：代表域名就有错误
    '''
    res = urlparse(url)
    status = -1
    request_local_path = ""
    if res.netloc == get_hostip():
        local_path= nturl2path.url2pathname(res.path) # 将uri地址更改为path
        total_path =  html_base_dir + local_path
        print(total_path)
        if os.path.exists(total_path):
            exist = 1
            request_local_path = total_path
        else:
            exist = 0
            request_local_path = total_path
    else:
        pass
    return {"exist": exist, "request_local_path": request_local_path}



# 返回给客户端的字典构造
# put类型需要返回的：
# filename   status   type    md5   message="请求文件，不存在"url

# get
# 需要返回：
    # 1.如果请求不存在   filename  status = 0， message = "请求的文件，不存在"  file_size = 101010  get
    # 2.如果请求存在：filename  status = 1, message = "文件已成功返回" file_size = 101010        get
def creat_client_headdic(type=None,file_name=None,file_size=None,file_md5=None,status=None,message=None):
    file_dic = {
        'type': type,
        'file_name': file_name,
        'file_size': file_size,
        'file_md5': file_md5,
        'status' : status,
        'message':message
    }
    return file_dic




import socket


def get_md5(filepath):
    has  =  hashlib.md5('加盐'.encode('utf8'))
    with open(filepath,'rb') as f:
        for line  in   f:
            has.update(line)
    return has.hexdigest()



class FTPServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    max_packet_size = 8192
    coding = 'utf8'



    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__listen = 5
        self.__upload_dir = r"D:\\"
        self.__html_base_dir = r'E:\\Foxmail 7.2'

    def bind(self,serverIP,serverPort):
        self.socket.bind((serverIP,serverPort))

    def setlinsten(self):
        self.socket.listen(self.listen)

    # 设置listen
    @property
    def listen(self):
        return  self.__listen
    @listen.setter
    def listen(self,listen):
        self.__listen = listen
        self.socket.listen(self.__listen)

    #设置upload的文件路径
    @property
    def upload_dir(self):
        return self.__upload_dir
    @upload_dir.setter
    def upload_dir(self,upload_dir):
        if Path(upload_dir).is_dir():
            print('{}目录存在，设置成功'.format(upload_dir))
            self.__upload_dir = upload_dir
        else:
            print('{}目录存在，设置失败'.format(upload_dir))

    # 设置html家目录位置
    @property
    def html_base_dir(self):
        return self.__html_base_dir
    @html_base_dir.setter
    def html_base_dir(self,html_base_dir):
        if Path(html_base_dir).is_dir():
            print('{}目录存在，设置成功'.format(html_base_dir))
            self.__html_base_dir = html_base_dir
        else:
            print('{}目录存在，设置失败'.format(html_base_dir))



    def accept(self):
       self.conn,self.addr= self.socket.accept()
       return self.conn,self.addr

    def client_close(self):
        self.socket.close()

    # 接收返回的dict
    def recv_head_dic(self):
        '''
        接收返回的dict
        :return:
        '''
        # 获取返回的head_lengh_struct
        head_lengh_struct = self.conn.recv(4)
        print(head_lengh_struct)
        # 获取返回的报头长度数据
        head_length = struct.unpack('i', head_lengh_struct)[0]
        # 获取json二进制
        json_bytes = self.conn.recv(head_length)
        # 反序列化json的二进制获取python的字典
        return_dic = json.loads(json_bytes)  # 反序列化json获取python字典,loads参数可以是二进制也可以是str
        return return_dic

        # dict转化为（报头长度，报头bytes）

    def head_dic_to_bytes(self, head_dic):
        '''
            将报头的python字典制作为固定长度的报头字节数和报头二进制文件
        :param head_dic: 报头的python字典
        :param encoding: json序列化的编码方式
        :return:pack加密的固定包头字节数，报头json序列化后的二进制文件
        '''
        # print(head_dic)
        head_json = json.dumps(head_dic)  # 序列化获取json字符串
        head_bytes = head_json.encode(self.coding)  # json字符串转化为二进制
        head_lengh_struct = struct.pack('i', len(head_bytes))
        return head_lengh_struct, head_bytes

        # 发送报头长度和报头bytes

    def send_head_dic(self, head_dic):
        '''
        上传数据：
        :param head_dic: 需要上传的报头字典文件
        :param abs_filepath:
        :return:
        '''
        # print(self.head_dic_to_bytes(head_dic)[0])
        try:
            # 先发送加密的报头固定长度文件，解密可以得到报头的长度
            self.conn.send(self.head_dic_to_bytes(head_dic)[0])
            # 再发送报头json的二进制文件
            self.conn.send(self.head_dic_to_bytes(head_dic)[1])
        except:
            self.client_close()

    # 服务端响应客户端的上传动作
    def put_file(self,return_dict):

        abs_file_path = os.path.normpath(os.path.join(
            self.upload_dir,
            return_dict['file_name']
        ))
        # print(abs_file_path)
        with open(abs_file_path, "wb") as f:
            receive_len = 0
            while receive_len < return_dict['file_size']:
                temp = self.conn.recv(FTPServer.max_packet_size)
                f.write(temp)
                receive_len += len(temp)

        file_md5 = get_md5(abs_file_path)
        status = -1
        message = ""
        file_size = ""
        if file_md5 == return_dict['file_md5']:
            file_md5 = 'OK'
            status = 1
            message = "上传的数据成功，md5值相同，文件完整"
            file_size = return_dict['file_size']
        else:
            file_md5 = 'NG'
            status = -1
            message = "文件上传失败，md5值不同，文件损坏"
            file_size = len(message.encode(self.coding))

        return_client_dict = creat_client_headdic(type='put',
                                                  file_size=file_size,
                                                  file_name=return_dict['file_name'],
                                                  file_md5=file_md5,
                                                  status=status,
                                                  message=message)
        self.send_head_dic(return_client_dict)

    # 服务端响应客户端的下载响应
    def get_file(self, url):
        res = url_get_local_path(url, self.html_base_dir)
        total_path = res['request_local_path']
        if res['exist'] == 1:
            # 文件存在
            return_client_dict = creat_client_headdic(type='get',file_size=os.path.getsize(total_path),
                                                      file_name=os.path.split(total_path)[1],
                                                      file_md5=get_md5(total_path),
                                                      status=1)
            # 发送文件名字和文件大小和md5
            self.send_head_dic(return_client_dict)

            # 发送文件数据
            with open(total_path, 'rb') as f:
                for line in f:
                    self.conn.send(line)

        else:
            message = "请求的地址不存在"
            return_client_dict = creat_client_headdic(type='get',file_name=os.path.split(total_path)[1],
                                                      status=-1,
                                                      message="请求的地址不存在",
                                                      file_size=len(message.encode(self.coding)))
            # 发送文件的内容
            self.send_head_dic(return_client_dict)
            print('请求的地址，不存在')


def  main():
    f =  FTPServer()
    f.bind(get_hostip(),9000)
    f.listen = 10
    # print(f.listen)
    while 1:
        print('等待用户连接>>>')
        conn,addr = f.accept()
        print('用户连接成功>>>')
        print(conn)
        print(addr)

        while 1:
            return_dic = f.recv_head_dic()
            print(return_dic)
            if return_dic['type'] == 'put':
                f.put_file(return_dic)
            elif return_dic['type'] == 'get':
                f.get_file(return_dic['url'])
                # print(return_dic)
            elif return_dic['type'] == 'quit':
                f.conn.close()
                print('客户端连接断开')
                break
            # pass

if __name__ == '__main__':
    main()










