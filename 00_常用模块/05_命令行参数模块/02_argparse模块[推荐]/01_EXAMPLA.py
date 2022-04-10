import argparse
import urllib
from pyquery import PyQuery as pq
def getArgs():
    parse=argparse.ArgumentParser()
    parse.add_argument('-u',type=str)
    parse.add_argument('-d',type=str)
    parse.add_argument('-o',type=str)
    args=parse.parse_args()
    return vars(args)
def urlAddQuery(url,query):
    query=query.replace(',','&')
    if '?' in url:
        return url.replace('?','?'+query+'&')
    else:
        return url+'?'+query
def getHref():
    args=getArgs()
    print(args)
    url=args['u']
    query=args['d'].strip("\'")
    fileName=args['o']
    doc=pq(url=url)
    with open(fileName,'w') as f:
        for a in doc('a'):
            a=pq(a)
            href=a.attr('href')
            if href:
                newurl=urlAddQuery(href,query)
                f.write(newurl+'\n')
if __name__=='__main__':
    print("开始程序")
    # python  EXAMPLA01.py -u http://www.sohu.com -d 'a=1,b=2,c=3' -o index.html

    '''
    有一道面试题：编写一个脚本main.py，使用方式如下：
    main.py -u http://www.sohu.com -d 'a=1,b=2,c=3' -o /tmp/index.html
    功能要求：打开-u指定的页面，将页面中所有的链接后面增加参数a=1&b=2&c=3(需要考虑链接中已经存在指定的参数的问题), 然后保存到-o指定的文件中。
    '''

    getHref()