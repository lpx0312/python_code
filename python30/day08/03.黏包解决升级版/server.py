import socket
import  subprocess
import  json
import  struct
import time
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



# sock =  socket.socket(family=-1,type=-1)
#
# sock.bind((get_host_ip(),8899))
#
# sock.listen(5)

with  socket.socket(family=-1,type=-1) as s :
    s.bind((get_host_ip(),8899))
    s.listen(5)
    while  1: # 链接循环
        conn,addr = s.accept()  # 等待客户端连接
        # 给客户端发送信息，打印链接成功的信息
        conn.send('欢迎{}连接本服务器{}'.format(addr[0],get_host_ip()).encode('utf8'))
        while 1:    # 通讯循环
            try :
                # 接收客户端发来的执行
                cmd = conn.recv(1024).decode('utf8')
                print('接收的命令是：{}'.format(cmd))
                if cmd == 'quit':
                    break
                #处理命令的流程
                sendResult =  subprocess.Popen(cmd,shell=True,
                                               stdout = subprocess.PIPE,# 标准输出
                                               stderr = subprocess.PIPE # 标准错误
                                               )
                stdout = sendResult.stdout.read() # 这里返回的是 二进制
                stderr = sendResult.stderr.read() # 这里返回的是 二进制

                # print('本机命令执行结果stdout{}'.format(stdout.decode('gbk')))
                # print('本机命令执行结果stderr{}'.format(stderr.decode('gbk')))
                print("stdout:::{}".format(stdout))
                print('stderr>>>>'.format(stderr))
                print(len(stderr) + len(stderr))
                # 制作报头
                header_dic = {
                    'total_size':len(stdout) + len(stderr),
                    'filename':None,
                    'md5':None
                }
                print(header_dic)
                header_json = json.dumps(header_dic) # 将 dic 制作成 json字符串
                header_bytes =  header_json.encode('utf8') # 将json字符串转化成 二进制 bytes类型（但是这个长度是可变的）

                # 将长度可变的json字符串的二进制长度转化为固定长度的内容
                num_lenght =  struct.pack('i',len(header_bytes))
                print('num_lenght::{}'.format(num_lenght))
                # 先发报头长度
                conn.send(num_lenght)

                # 在发报头
                conn.send(header_bytes)
                print('header_bytes::{}'.format(header_bytes))

                # 最后发命令结果
                conn.send(stdout)
                print(stdout)
                conn.send(stderr)
            except ConnectionError:
                print('客户端已异常断开，无法将消息发送到客户端')
                print('等待2s，重新等待客户端连接')
                time.sleep(2)
                break
        conn.close()