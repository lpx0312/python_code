
import requests
import json
# requests 忽略https，并且使用verify=False
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url="https://api.muxiaoguo.cn/api/tianqi"
headers={'Content-Type': 'application/x-www-form-urlencoded'}
data={'type':1,'city':'武汉','api_key':'3c9f233f0486b780'}

res = requests.post(url,data=data,headers=headers,verify=False)
print(res.json())


