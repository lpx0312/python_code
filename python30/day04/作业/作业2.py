# 以2020/20/12 12:23 的方式打印三天后此刻的时间字符串。

import datetime

now = datetime.datetime.now()

threeAfter = datetime.timedelta(days=3) + now

geshihua =  threeAfter.strftime("%Y/%m/%d %H:%M")

print(geshihua)