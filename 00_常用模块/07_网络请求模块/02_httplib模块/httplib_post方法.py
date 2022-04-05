#!/usr/bin/python
# coding=utf-8
# 参考文档：https://www.cnblogs.com/beard/p/11982673.html
# https://blog.csdn.net/xixihahalelehehe/article/details/105229074

import sys
import json

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except Exception as e :
    print('No python2')

try:
    # python2
    import httplib
except Exception as e:
    # python3
    import httplib3


# httplib的https的请求（POST）
import urllib
# port 可以省略
conn = httplib.HTTPSConnection(host='api.muxiaoguo.cn',port=443)
headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
data={'type':1,'city':'武汉','api_key':'3c9f233f0486b780'}
body=urllib.urlencode(data)
print body
conn.request(method='POST',url='/api/tianqi',body=body,headers=headers)
res = conn.getresponse()
print res.status
result = json.loads(res.read())
if result.get('data').get('cityname') == '武汉':
    print '武汉'
conn.close()



