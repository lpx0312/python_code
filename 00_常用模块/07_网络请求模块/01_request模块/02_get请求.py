# 参考教程
# https://www.cnblogs.com/lanyinhao/p/9634742.html

# python的requests模块
import requests
import json
from urllib.parse import quote


# get请求有两种方式传入参数，
# 1.直接url接参数，这种如果遇到中文需要使用quote进行编码转换，
# 2.使用params参数字典方式 传入参数，这种不需要对中文进行转换。
# url="https://tianqiapi.com/free/day?appid=23035354&appsecret=8YvlPNrz&cityid=0&city={0}&ip=112.232.36.102&callback=0".format(quote('武汉'))
# print(url)

url="https://api.muxiaoguo.cn/api/tianqi"
params={
    "api_key": "3c9f233f0486b780",
    "city": "武汉",
    "type": "1"
}
headers={'Content-Type': 'application/json'}

ret = requests.get(url=url,params=params,headers=headers)
print(ret.json())
print(ret.headers)
print(type(ret.status_code))

if ret.status_code == 200 :
    print('返回成功')
    ret_result = ret.json()
    print('ret_result',ret_result)
    if ret_result.get('data').get('cityname') == '武汉' :
        print('武汉')







