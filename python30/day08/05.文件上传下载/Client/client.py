import  socket
import  struct
import  json
import  os
import  hashlib

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


def uploadfile(sock,filepath):
    # 上传之前应该确认 文件大小  文件名
    file_size = os.path.getsize(filepath) # 文件大小
    file_name =  os.path.split(filepath)[1]  # 文件名
    file_md5 =  get_md5(filepath)  #  加盐后的md5值

    file_dic = {
        'file_size' :file_size,
        'file_name' :file_name,
        'file_md5' : file_md5,
        'cmd_file' : 'put'
    }
    file_json =  json.dumps(file_dic) # 序列化获取json字符串
    file_bytes =  file_json.encode('utf8') # json字符串转化为二进制

    # print(struct.pack('i',len(file_bytes)))
    # print(struct.unpack('i',struct.pack('i',len(file_bytes))))

    # 先发送表头信息【4个字节】
    sock.send(struct.pack('i',len(file_bytes))) #
    sock.send(file_bytes)       # 发送表头数据

    # 发送文件数据
    with open(filepath,'rb') as f:
        for line in f:
            sock.send(line)

    # # 接收返回状态:
    # print(sock.recv(1024).decode('utf8'))


def downloadfile(sock,abspath,localpath):
    # filepath = os.path.split(filepath)[0]  # 文件的完整路径，可以是http://www.baidu.com/Base/image/1.txt
    print(abspath)
    file_dic = {
        'file_size' :None,
        'file_name' :abspath,
        'file_md5' : None,
        'cmd_file' : 'get'
    }
    file_json = json.dumps(file_dic)  # 序列化获取json字符串
    file_bytes = file_json.encode('utf8')  # json字符串转化为二进制
    sock.send(struct.pack('i',len(file_bytes))) #
    sock.send(file_bytes)       # 发送表头数据


    # 接收返回的文件数据
    head_length = struct.unpack('i', sock.recv(4))[0]  # 接收表头长度数据
    # print('head_length::{}'.format(head_length))
    json_bytes = sock.recv(head_length)  # 获取json二进制
    # print('json_bytes:::{}'.format(json_bytes))
    # json_str = json_bytes.decode('utf8','ignore')  # 获取json字符串
    json_dic = json.loads(json_bytes)  # 反序列化json获取python字典,loads参数可以是二进制也可以是str
    print(json_dic)
    file_name = json_dic['file_name']  # 文件名
    file_size = json_dic['file_size']  # 文件大小
    file_md5 = json_dic['file_md5']  # 文件加盐后的md5

    total_download_path =  localpath +'\\'+ file_name
    print('total_download_path',total_download_path)

    with open(total_download_path, "wb") as f:
        # 循环接收上传数据写入到文件中
        receive_len = 0
        while receive_len < file_size:
            print("receive_len", receive_len)
            temp = sock.recv(10000000)
            f.write(temp)
            receive_len += len(temp)
        # f.write('13s4131431435434'.encode('utf8')) #测试md5

    # print(total_download_path)

    # 如果不传入需要接收的长度，最好不传，因为容易被下次接收接了，【这里后面会报错】
    # if get_md5(total_download_path) == file_md5:
    #     print('md5值相同，文件完整')
    #     sock.send('{}文件上传的md5值相同，文件完整'.format(file_name).encode('utf8'))
    # else:
    #     print('md5值不相同，文件可能被更改过')
    #     sock.send('{}文件上传的md5值不相同，文件可能被更改过'.format(file_name).encode('utf8'))

def main():
    # 如果路径不存在，下载写入的时候会报错
    localpath = r"D:\download"
    s = socket.socket()
    remote_IP = (get_hostip(),9000)
    s.connect(remote_IP)
    print(s.recv(1024).decode('utf8'))

    while 1:
        inp = input('请输入命令>>>')
        # cmd,filepath =  inp.split(' ')
        cmd, filepath = inp.split()
        # print(cmd)
        # print(filepath)
        if cmd == 'put':
            uploadfile(s,filepath)
        elif cmd == 'get':
            downloadfile(s,filepath,localpath)
        else:
            print('输入的命令请重新输入')
            continue

if __name__ == '__main__':
    # filepath = r"D:\Users\Desktop\meinv.jpg"
    # uploadfile('sock', filepath)
    main()
    # print(get_hostip())
    # file_name = os.path.split(r"http://www.baidu.com/03 文件上传(yuan)/server/server.py")[1]
    # print(file_name)

