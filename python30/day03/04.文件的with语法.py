
f = open("满江红")
f.close()


# with中语句执行完后，with会# 文件的with主要用于，忘记调用 f.close()自动调用 f.close方法帮你关闭
with open("满江红",encoding="utf-8") as f:
    print(f.read())



