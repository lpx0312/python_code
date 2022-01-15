import requests
import re
import json
import requests  # pip install requests

# res =  requests.get("https://movie.douban.com/top250?start=0&filter=")
# print(res)
# with  open("douban.html","w",encoding='utf8') as f:
#     f.write(res.text)


with  open("douban.html", "r", encoding='utf8') as f:
    context = f.read()


def parsePage(s):
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)

    ret = com.finditer(s)
    for i in ret:
        print(i.group())
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
        }


ret = parsePage(context)
print(ret)

reg = '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>' \
		'.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>'


f = open("move_info7", "a", encoding="utf8")

for obj in ret:
    # print(obj)
    data = json.dumps(obj, ensure_ascii=False,indent=4)
    f.write(data + "\n")



# reg = '<li>.*?<div class="item">.*?<div class="pic">.*?<em .*?>(\d+)</em>.*?<span class="title">(.*?)</span>.*?' \
#       '<span class="rating_num" .*?>(.*?)</span>.*?<span .*?>.*?</span>.*?<span>(.*?)人评价</span>'
# ret = re.findall(reg, context, re.S)
#
# print(ret)
# ll = []
# for yuanzu in ret:
#     dict = {}
#     dict["序号"] = yuanzu[0]
#     dict["片名"] = yuanzu[1]
#     dict["评分"] = yuanzu[2]
#     dict["评论数"] = int(yuanzu[3])
#     ll.append(dict)
# print(ll)
# # json.dumps(ll)
# with open("move_info8", "w", encoding='utf8') as f:
#     f.write(json.dumps(ll,ensure_ascii=False,indent=4))
