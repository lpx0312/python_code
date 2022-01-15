import socket
import  subprocess


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

sock =  socket.socket(family=-1,type=-1)

sock.bind((get_host_ip(),8899))

sock.listen(5)



while  1:

    conn,addr = sock.accept()
    print()
    conn.send('欢迎{}连接本服务器{}'.format(addr[0],get_host_ip()).encode())

    while 1:
        cmd = conn.recv(1024).decode()
        print('接收的命令是：{}'.format(cmd))
        sendResult =  subprocess.getoutput(cmd)
        print('已将结果返回客户端{}'.format(sendResult))
        total_num = str(len(sendResult.encode('utf8')))
        print('server_total_num:{}'.format(total_num))
        conn.send(total_num.encode('utf8'))

        if conn.recv(1024).decode('utf8') == 'ok' :
            conn.send(sendResult.encode('utf8'))
