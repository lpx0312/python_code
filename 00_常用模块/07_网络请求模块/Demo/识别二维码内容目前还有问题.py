import requests
import base64
import os

def tobase64(img_data_path):
    '''
    将图片转化为base64的字符串
    @param img_data_path: 图片路径
    @type img_data_path:  str
    @return: 图片的base64字符串
    @rtype: str
    '''
    with open(img_data_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


url="https://api.muxiaoguo.cn/api/QrcodeRT?api_key=2675e57e7fcf91f2"

#假设待上传文件与脚本在同一目录下
dir_path = os.path.abspath(os.path.dirname(__file__))
#待上传文件的路径，这里假设文件名为test.txt
file_path = os.path.join(dir_path, 'Qrcode.png')
img2base64 = tobase64(file_path)

print(img2base64)
data = {
    "file": img2base64,
}
print(data)

result_json = requests.post(url, data=data).content
print(result_json)


# files = open(r"D:\User\Desktop\Qrcode.png",'rb')
# files = {'file': open(r"D:\User\Desktop\Qrcode.png",'rb')}
# body={
#     'file':files
# }
#
# response = requests.post(url, files=files)
# print(response.text)

# import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder

# with open(r'Qrcode.png', 'rb') as f:
#     file = {"file": ("Qrcode.png", f)}
#     # encode_data = encode_multipart_formdata(file)
#     data = MultipartEncoder(fields=file)
#     print(data)
#     print(data.content_type)
#
#     # 按各自平台请求头要求拼接
#     url = "https://api.muxiaoguo.cn/api/QrcodeRT?api_key=2675e57e7fcf91f2"
#     header = {"Content-Type": data.content_type}
#
#     # 发起请求，注意了，血泪教训：请求与 with xxxxx要注意格式，如果与打开文件操作格式与本
#     # 博客不一致，那么文件关闭后是拿不到文件的数据的
#     respones = requests.post(url=url, headers=header, data=data)
#     print(respones.text)

# url="https://api.muxiaoguo.cn/api/QrcodeRT"
# body={"api_key":"2675e57e7fcf91f2"}
# files = {
#     "file": ("Qrcode.png", open("Qrcode.png", "rb"))
# }
# r = requests.post(url=url,files=files,data=body)
# print(r.text)
#

# https://www.cnblogs.com/Simple-Small/p/13217842.html 还是不管用呢

#'multipart/form-data'

# headers={
#     'Content-Type':'multipart/form-data'
# }
# import os
# #假设待上传文件与脚本在同一目录下
# dir_path = os.path.abspath(os.path.dirname(__file__))
# #待上传文件的路径，这里假设文件名为test.txt
# file_path = os.path.join(dir_path,'Qrcode.png')
# print(file_path)
#
# url="https://api.muxiaoguo.cn/api/QrcodeRT?api_key=2675e57e7fcf91f2"
# files = {
#     'file': ('Qrcode.jpg', open(file_path, 'rb'), 'application/octet-stream')
# }
#
# response = requests.post(url,files=files)
#
# print(response.text)