

import  socket
import  os
import  hashlib
import struct
import json
import  sys
from pathlib import Path


# 获取本机IP
def get_hostip():
    s =  socket.socket(family = socket.AF_INET,type=socket.SOCK_DGRAM)
    try :
        s.connect(('8.8.8.8',80))
        IP =  s.getsockname()[0]
    except:
        s.close()
    return  IP

# 获取MD5值
def get_md5(filepath):
    has  =  hashlib.md5('加盐'.encode('utf8'))
    with open(filepath,'rb') as f:
        for line  in   f:
            has.update(line)
    return has.hexdigest()


'''
干什么？：上传数据：下载数据 的客户端

上传数据：包括上传数据 和 接收返回（是否成功的消息）
    传输的工具：socket：
        socket对象可以是该类的属性
        因为socket的创建，必须有网络类型socket.AF_INET 和 socket.SOCK_STREAM，
            因为该FTP是基于socket.AF_INET和socket.SOCK_STREAM的，所以可以设置为类方法
    能干什么：
        连接服务端：需要 服务端IP和端口，因为连接服务端的IP和端口可能会变，所以不能设置为类属性，
                  所以服务端IP和端口可以设置为实例属性，可以在init中实例化的时候设置，
                  也可以在其他实例方法中设置，比如在连接服务器的实例方法中创建
        断开服务器连接：
                  使用socket的实例对象.close()来断开
        上传数据：
            为了解决粘包的问题，需要在传输命令的时候，传输的时候，告诉服务端，需要上传的数据的大小，好让服务端来确认接收多少数据
            所以需要传：{
                    命令名称：put
                    需要上传的文件的大小 ：file_size   (解决粘包)
                    需要上传的文件名：file_name       （为了上传到服务端后的文件的保存）
                    md5值：file_md5                 (为了确认上传的文件是否有损坏)
                    }
            接收数据返回信息：
                接收服务端返回的信息，包含{
                        文件名：file_name
                        isMd5OK："OK"        #确认上传到服务器的文件是否有损坏
                        'status':'200'
                        }

        下载数据：
            需要传：{    
                     命令名称：get
                     文件的绝对路径：'http://172.21.95.231/data.json'
                   }
            如果文件不存在，返回错误信息
                
            如果文件存在，返回需要所需的文件数据，以及返回正常的信息


'''

# 发送给server的字典构造
def creat_server_headdic(file_name=None,file_size=None,file_md5=None,type=None,url=None):
    '''
    上传文件的报头字典的构建
    :param file_name: 文件名
    :param file_size: 文件大小
    :param file_md5: 文件的md5
    :param type: 操作的类型，'put' or 'get'
    :param url :请求文件的网址
    :return:
    '''
    file_dic = {
        'file_size': file_size,
        'file_name': file_name,
        'file_md5': file_md5,
        'type': type,
        'url':url
    }
    return file_dic

# 判断本地的目录是否存在，以及需要下载的文件在本地是否存在
def jugePathEsxit(path_dir,file_name):
     abs_file_path = os.path.normpath(os.path.join(
         path_dir,
         file_name
     ))
     if Path(path_dir).is_dir():
         # 指定的目录存在
         print('{}目录存在'.format(path_dir))
         if Path(abs_file_path).exists():
             print('{}文件存在'.format(file_name))
             return True
         else:
             print('{}文件不存在'.format(file_name))
             return False
     else:
         print('{}目录不存在'.format(path_dir))
         sys.exit()




class FTPClient(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    max_packet_size = 8192
    coding = 'utf8'

    # # 可以将连接服务器的操作，放到初始化__init__方法中去
    # def client_connect(self,server_address,server_port):
    #     '''
    #     根据服务端IP和端口，连接服务端
    #     :param server_address: 服务端IP
    #     :param server_port:    服务端端口
    #     :return:
    #     '''
    #     self.server_address = server_address
    #     self.server_port = server_port
    #     try:
    #         self.socket.connect((self.server_address,self.server_port))
    #     except:
    #         self.client_close()
    def __init__(self,server_address,server_port):
        '''
        初始化FTP这个类，并默认赋值
        '''
        # 每个实例对象独有的才设置为实例变量，每个对象都一样的设置为类对象
        # 实例对象可以获取实例对象的值，但是不能更改
        self.socket =  socket.socket(self.address_family,self.socket_type)
        self.server_address = server_address
        self.server_port = server_port
        self.__local_download_path =  'D:\download'
        try:
            self.socket.connect((self.server_address,self.server_port))
        except:
            self.client_close()


    @property
    def local_download_path(self):
        return self.__local_download_path

    # 更改本地下载目录
    @local_download_path.setter
    def local_download_path(self,path):
        self.__local_download_path = path



    def client_close(self):
        '''
        关闭服务器连接
        :return:
        '''
        self.socket.close()


    # dict转化为（报头长度，报头bytes）
    def head_dic_to_bytes(self,head_dic):
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
    def send_head_dic(self,head_dic):
        '''
        上传数据：
        :param head_dic: 需要上传的报头字典文件
        :param abs_filepath:
        :return:
        '''
        # print(self.head_dic_to_bytes(head_dic)[0])
        try:
            # 先发送加密的报头固定长度文件，解密可以得到报头的长度
            self.socket.send(self.head_dic_to_bytes(head_dic)[0])
            # 再发送报头json的二进制文件
            self.socket.send(self.head_dic_to_bytes(head_dic)[1])
        except:
            self.client_close()





    # 发送文件数据
    def  put_file(self, head_dic,abs_filepath):
        # self.send_head_dic(head_dic)
        # print(abs_filepath)
        # 再发送文件
        with open(abs_filepath, 'rb') as f:
            for line in f:
                self.socket.send(line)


    # 接收返回的dict
    def recv_head_dic(self):
        '''
        接收返回的dict
        :return:
        '''
        # 获取返回的head_lengh_struct
        head_lengh_struct = self.socket.recv(4)
        # 获取返回的报头长度数据
        head_length = struct.unpack('i', head_lengh_struct)[0]
        # 获取json二进制
        json_bytes = self.socket.recv(head_length)
        # 反序列化json的二进制获取python的字典
        return_dic = json.loads(json_bytes)  # 反序列化json获取python字典,loads参数可以是二进制也可以是str
        return  return_dic




    def get_file(self,return_dict):
        # 把目录和文件名合成一个路径
        abs_file_path = os.path.normpath(os.path.join(
            self.local_download_path,
            return_dict['file_name']
        ))
        if not jugePathEsxit(self.local_download_path,return_dict['file_name']):
            # 文件不存在
            # 将数据写入文件
            self.get_bytes_write_file(abs_file_path, return_dict['file_size'])
        else:
            print('文件已经存在')


    # 将接收到的数据，循环写入文件
    def get_bytes_write_file(self,abs_file_path,file_size):
        # 循环接收下载回来的数据
        with open(abs_file_path, "wb") as f:
            receive_len = 0
            while receive_len < file_size:
                # print("receive_len", receive_len)
                temp = self.socket.recv(self.max_packet_size)
                f.write(temp)
                receive_len += len(temp)

    # 接收服务返回的消息
    def recv_server_message(self,return_dict):
        abs_file_path = os.path.normpath(os.path.join(
            self.local_download_path,
            return_dict['file_name']
        ))
        message = ""
        if return_dict['type'] == 'get':
            if return_dict['status'] == 1:
                # 打印返回的消息，下载的文件是否完整
                if get_md5(abs_file_path) == return_dict['file_md5']:
                    message = '{}:::下载完成，md5值相同，文件完整'.format(return_dict['file_name'])
                else:
                    message = '{}:::下载完成，md5值不同，文件损坏'.format(return_dict['file_name'])
            elif return_dict['status'] == -1:
                message = '网址请求不成功：status:{},message={}'.format(return_dict['file_name'],return_dict['file_name'])
        else:
            if return_dict['status'] == 1:
                message = '{}:::上传成功且文件完整'.format(return_dict['file_name'])
            else:
                message = '{}:::上传失败，文件损坏'.format(return_dict['file_name'])
        return message

def main():
    f = FTPClient(get_hostip(),9000)
    # f.socket.recv(1024).decode('utf8')
    while 1:
        inp = input('请输入命令>>>')
        if not inp:
            continue
        cmd,filepath = None,None
        if inp =='quit':
            cmd = 'quit'
        else:
            try:
                cmd, filepath = inp.split()
                print('cmd{}'.format(cmd))
                print('filepath{}'.format(filepath))
            except ValueError:
                # 如果 可以用空格 分隔命令为 3个变量，就会执行这里
                # 所以 该程序 目前 的文件名或路径 不能含有空格
                print('输入错误，请重新输入')
                continue

        if cmd == 'put':
            send_dict = creat_server_headdic(file_size = os.path.getsize(filepath),
                file_name = os.path.split(filepath)[1],
                file_md5 = get_md5(filepath),type=cmd)

            # 上传head_dic
            f.send_head_dic(send_dict)
            # 上传文件数据
            f.put_file(send_dict,filepath)
            return_dict =  f.recv_head_dic()
            # 打印返回的信息
            print(f.recv_server_message(return_dict))
        elif cmd == 'get':
            # 重新设置保存文件的路径
            # f.local_download_path = r'E:\\'
            # 创建发送给服务端的字典
            # os.path.split(filepath)[1]
            send_dict = creat_server_headdic(file_name=os.path.split(filepath)[1],type=cmd, url= filepath)
            print('send_dict:::{}'.format(send_dict))
            # 发送表头
            f.send_head_dic(send_dict)

            # 获取服务端返回字典
            return_dict = f.recv_head_dic()
            if return_dict['status'] == 1:
                # 将数据写入到本地文件
                f.get_file(return_dict)
            print(f.recv_server_message(return_dict))




        elif cmd =='quit':
            send_dict = creat_server_headdic(type=cmd)
            f.send_head_dic(send_dict)
            break
        else:
            continue

if __name__ == '__main__':
    # filepath = r"D:\Users\Desktop\meinv.jpg"
    # uploadfile('sock', filepath)
    main()
    # print(get_hostip())
    # file_name = os.path.split(r"http://www.baidu.com/03 文件上传(yuan)/server/server.py")[1]
    # print(file_name)

