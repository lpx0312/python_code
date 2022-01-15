# import  subprocess
#
# print(subprocess.getoutput('ipconfig'))


# 获取文件名
# import  os
# url = 'http://172.21.95.231/data.json'
# filepath = os.path.split(url)
# print(filepath)



# # 获取url中的域名和path
# from urllib.parse import urlparse
# # Python2 中的是urlparse 这个包，在 Python3 中都整合到 urllib 中了
# # url1='http://www.chenxm.cc/post/hhh/719.html'
# url1 = 'https://docs.google.com/spreadsheet/ccc?key=blah-blah-blah-blah#gid=1'
# res1 = urlparse(url1)
# print(res1)
# print('请求方式:::{}  域名或IP:::{}  URI:::{}'.format(res1.scheme,res1.netloc,res1.path))
#
# url2 = 'https://172.19.6.89/post/hhh/meinv.jpg'
# res2 =  urlparse(url2)
# print('请求方式:::{}  域名或IP:::{}  URI:::{}'.format(res2.scheme,res2.netloc,res2.path))
# print(res2[0])
# print(res2[1])
# print(res2[2])





# import nturl2path
# from urllib.parse import urlparse
# import os
# import socket

# def get_hostip():
#     s =  socket.socket(family = socket.AF_INET,type=socket.SOCK_DGRAM)
#     try :
#         s.connect(('8.8.8.8',80))
#         IP =  s.getsockname()[0]
#     except:
#         s.close()
#     return  IP
#
# def jugeURL(url):
#     Base_IP = r'E:\Apache24\htdocs'
#     res = urlparse(url)
#     if res[1] == get_hostip():
#         # 主机名（域名）正确
#         path_name = nturl2path.url2pathname(res[2]) # 将uri地址更改为path
#         total_path =  Base_IP + path_name
#         if os.path.exists(total_path):
#             print('{}文件存在'.format(total_path))
#         else:
#             print('{}文件不存在'.format(total_path))
#     else:
#         print('主机名不正确')
#


# if __name__ == '__main__':
#     # jugeURL('http://172.21.95.231/data.json')


# print(len('文件上传完成，md5值相同，文件完整'.encode('utf8')))

# from pathlib import  Path
# if Path("D:\download").is_dir():
#     # 指定的目录存在
#     print('目录存在')
#     if Path("D:\download\data.json").exists():
#         print('json存在')
#     else:
#         print('json不存在')

# inp = input('>>')
# cmd,filepath = inp.split()



# from urllib.parse import urlparse
# url='http://www.chenxm.cc/post/hhh/719.html'
# res1 = urlparse(url)
# uri = res1.path
#
# path =  nturl2path.url2pathname(uri)
# print(path)
#
# html_base_dir = r'D:\EHS_20210228_000001'
# abs_file_path = html_base_dir + path
# print(abs_file_path)
from urllib.parse import urlparse
import nturl2path
import os
import socket

# 获取本机IP
def get_hostip():
    s =  socket.socket(family = socket.AF_INET,type=socket.SOCK_DGRAM)
    try :
        s.connect(('8.8.8.8',80))
        IP =  s.getsockname()[0]
    except:
        s.close()
    return  IP



def url_get_local_path(url,html_base_dir):
    '''
    传入url和html家目录，返回请求服务器本地地址
    :param url:请求的网址
    :param html_base_dir:服务器本地的html所在的家目录
    :return:返回解析的状态和请求的地址
        status = 1:代表 域名正确，且所需文件存在
        status = 0：代表 域名正确,但所需文件不存在
        status = -1：代表域名就有错误
    '''
    res = urlparse(url)
    status = -1
    request_local_path = ""
    if res.netloc == get_hostip():
        local_path= nturl2path.url2pathname(res.path) # 将uri地址更改为path
        total_path =  html_base_dir + local_path
        # print(total_path)
        if os.path.exists(total_path):
            status = 1
            request_local_path = total_path
        else:
            status = 0
            request_local_path = total_path
    else:
        pass
    return {"status": status, "request_local_path": request_local_path}



res =  url_get_local_path('http://172.21.95.231/EHS_20210228_000001.dmp',r'D:\EHS_20210228_000001')
# print(res['request_local_path'])

print(os.path.split(res['request_local_path']))

print(len('请求的内容不存在'.encode('utf8')))