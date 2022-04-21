#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：01_paramiko模块封装.py
@Author  ：lipanxiang
@Date    ：2022/4/21 20:57 
'''
from distutils.log import warn as printf

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except Exception as e:
    pass


ip_list2=[
"10.0.0.111",
"10.0.0.112",
"10.0.0.113",
]
# 参考文章：https://blog.csdn.net/u014028063/article/details/81197431?utm_source=app&app_version=4.19.1&code=app_1562916241&uLinkId=usr1mkqgl919blen

# parammiko 简单使用：
# 一、基于用户名和密码的 sshclient 方式登录 【常用方法】
def send_pub_key():
    try:
        import paramiko
    except Exception as e:
        printf('paramiko module is not exsit')

    ssh = paramiko.SSHClient()
    try :
        # 创建SSH对象
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname='10.0.0.188', port=22, username='root', password='123456')
        # 执行命令
        creat_pubkey_cmd = '[ ! -f ~/.ssh/id_rsa ] && echo "is_rsa is not exsit" && ssh-keygen  -t rsa  -f ~/.ssh/id_rsa -C "root@ssh01_10.0.0.188"    -P  \'\'  &>/dev/null && echo "creat pub_key:OK"'
        # print creat_pubkey_cmd
        # creat_pubkey_cmd = 'df '
        printf('creat_pubkey_cmd',creat_pubkey_cmd)
        stdin, stdout, stderr = ssh.exec_command(creat_pubkey_cmd)
        printf("stdout", stdout.read())
        for ip in ip_list2:
            send_pubkey_cmd = 'sshpass -pLipanxiang1102 ssh-copy-id -i /root/.ssh/id_rsa.pub root@{0} "-o StrictHostKeyChecking=no" &>/dev/null  && echo "send pub_key :OK" '.format(ip)
            printf('send_pubkey_cmd',send_pubkey_cmd)
            stdin, stdout, stderr = ssh.exec_command(send_pubkey_cmd)
            printf("stdout",stdout.read())
    except Exception as e:
        printf('ssh Objece is abnormal exit ')
        ssh.close()
    ssh.close()


# send_pub_key()


# 二、基于用户名和密码的 transport 方式登录

'''
基于SSHClient是传统的连接服务器、执行命令、关闭的一个操作，
有时候需要登录上服务器执行多个操作，
比如执行命令、上传/下载文件，上面方法则无法实现，可以通过如下方式来操作
'''
def transport_ssh_test():
    #SSHClient 封装 Transport
    import paramiko
    # 实例化一个transport对象
    transport = paramiko.Transport(('10.0.0.188', 22))
    # 建立连接
    transport.connect(username='root', password='123456')
    # 将sshclient的对象的transport指定为以上的transport
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    # 执行命令，和传统方法一样
    stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd | grep root')
    print (stdout.read().decode())
    # 关闭连接
    transport.close()


# transport_ssh_test()


# 三、SSHClient基于秘钥验证
def ssh_client_pubkey():
    import paramiko
    from io import StringIO
    key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAuBeC0DLo+1oNK18nDgcwhK32Ph4MTLDGF1ThXXQ24jrNJOoS
56QN8Bt2e5OzkM8NYySsgGDTv48bQDLxTgse0dhp8h3WrMyz5cK7G2ZqfiTH+0zB
2mnhKBo6VnRBNTFtOaIJ39C8Anw8I7TAqBGrESjLNZtWFcRS4ETOC5FTVO9y1l/3
ev8OigSmEV6p4iLbIW5mZZpLsItjq3RfYiQtFd7nWgN0xy4QXi79kQOj0U4aPdNu
vFE3TOlasGCqDbqRLHLg1/uFMjDecCMeZGknVSaNOL0uFMzTH+hB5G4EBeTfDkqa
IjLX8CfLC4UYbVv/90nGnjbrpevYNl4ae10t7wIDAQABAoIBAGpiY91PXmZK7wte
bKJlszspkQDqum7jRUacbbRlAYaRNpYbkxs8KjXUmQ7nF0Ea9oCR5AI4coXj/HqI
NfzE3mWka+1YIwQvM9MWSqyV7frB5LOr8ub2gwB6z7XAbyJ/UsCYjJ5D8TJ6ewKj
ZSZ7N2GuMmjjQMdJch9ag7wZmo+c6LagjfEJzmqfcNp8I90TL4pY/Z32hQWqVKma
4GZ6PchM2E7dU4ZKKIwbESZzt4H7dp/NYvQsnG7HyaI8GGQsAdXD5CE1045rQbPQ
93iXtel2JpZFdYxeujaYy8Hs0ZnGxB01KGd+PoUeTHQuOqx+k96ZKoNP8ZAEKOof
h39Z3WkCgYEA7qMAnz6FUngjfc+wmcCauAibSlWWXxBl3jpL0BK1IPdt5pxkp35n
thSyD5/IVd5opYS5K8hdMB/1xBMpgN5MEF2ISJgguL2CiGzFXAnLfrOSnBXrleAI
RhygASA/TFftpFkj6KcBkSTpQF41qiFnLe93A/BGGdXcmC2nuO1lPZUCgYEAxXyF
biO5ZFRaTagxi46IuJQGdhXCillTWtFGICKwUkjww/0nmnnpSVpXhWJG/efYRxhX
yZxOff88aWL4pTnPuxU3YfGG0+qiZeP8BA8Cp523xEAiUty84baMkXSgd+up0i/K
3ne0/aJWYpcfBwxZLpmMtjLEaTQ6v1+B3p5PdHMCgYEAvUpdBvQf6x/S/0wMiJln
4M0q6Rbk1Xl7ZICXfHAqbwD1kzTA/r9c4uidqZkT31ExbwHNpDYl/TOMzkBo7ojm
iyC2JudNJV1lunOVRYGbgmBMzjTxD4yK45p3LQ14SEWDApeWzUgUDR7bSqywIsim
QKCvplckNAAZIDkuzpi4ctUCgYEAmWm9Qa1Q1MbOi+sv6ejk/vZG+q62vMDdhvxx
jH9GF/X/y1C61j8EYe5jdQO+gHn9wmT/tWfOdgS0Cm5PGBOL8xptNpHpGnD4jUyJ
NyHt/wX/ft4Pi+1ccb9c/ZXrHp2dA+IKp724hRv6HYamHNST5yZzcAqKF+vyAz6P
Zb/3m08CgYEAtp2lIxfI2fntnUoX1cvhppPQJAOywNAjCo6wE8TYCE0P0vnKN2dk
7MAbnL6DigU9MYvHMkk04S7PiY0sVYnmW+U1e2D4KWtx8DIkfr6d0r4OIEkHmWXL
awNP3/SmrwJ5Tf4kOgu318vNM9OHljKuHnZVB3lNiNY6YfByROEEyZM=
-----END RSA PRIVATE KEY-----"""
    private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
    # private_key = paramiko.RSAKey.from_private_key_file(r"C:\Users\lipanx\.ssh\self_id_rsa")
    # 创建SSH对象:
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='10.0.0.111', port=22, username='root', pkey=private_key)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('df')
    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    print(result.decode())
    # 关闭连接
    ssh.close()

ssh_client_pubkey()
# send_pub_key()
