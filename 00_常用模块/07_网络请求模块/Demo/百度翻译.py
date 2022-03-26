# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def generate_sign(salt,appid,query,appkey):
    sign = make_md5(appid + query + str(salt) + appkey)
    return sign

def get_translate_result(query,from_lang,to_lang):
    # api_url
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # Set your own appid/appkey.
    '''
    APP ID：20220325001140672
    密钥：pLDVyE8sDb4yIKNAX32Z
    http://api.fanyi.baidu.com/manage/developer
    '''
    appid = '20220325001140672'
    appkey = 'pLDVyE8sDb4yIKNAX32Z'

    # 获取salt,sign
    salt = random.randint(32768, 65536)
    sign = generate_sign(salt,appid,query,appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    #Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__' :
    query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'
    get_translate_result(query, 'en', 'zh')