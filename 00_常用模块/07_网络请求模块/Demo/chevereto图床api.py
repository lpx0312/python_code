#coding=utf-8
import time,os,json
from tqdm import tqdm
import requests
import base64


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


def upload_img(img_data_path):
    '''
    上传单张图片
    @param img_data_path: 图片路径
    @type img_data_path:  str
    @return: None
    @rtype: None
    '''

    APIKey = "ad227380b9a4a8018f05bdf78dc83c1a" #在此修改apikey
    img2base64 = tobase64(img_data_path)
    data = {
            "source":img2base64,
            "action":"upload",
            "key":APIKey
            }
    url = "http://192.168.0.180:6002/api/1/upload"
    result_json = requests.post(url, data = data).content
    try:
        result_dict = json.loads(result_json.decode())
    except Exception as _:
        print('the result of the picture bed is not standard json.' )
    pic_url = result_dict.get('image',{}).get('url','')
    print('pic_url',pic_url)


def get_image_path_list(img_path):
    '''
    获取文件夹下的图片完整路径列表
    @param img_path:  图片的文件夹
    @type img_path:  str
    @return:  图片路径的列表
    @rtype:  list
    '''
    file_name = []
    for root,_,files in os.walk(img_path):
        print('root',root)
        print('files',files)
        files.sort()
        for file in files:
            if (file.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff', '.gif'))):
                file_name.append(os.path.join(root,file))
    return file_name


if __name__ == "__main__":
    current_path = os.getcwd()
    print(current_path)
    img_path = os.path.join(current_path, 'result')
    file_name_list = get_image_path_list(r"D:\User\Desktop\新建文件夹\images")
    print(file_name_list)
    for file_index in tqdm(range(len(file_name_list))):
        print('\nname:',file_name_list[file_index])
        upload_img(file_name_list[file_index])