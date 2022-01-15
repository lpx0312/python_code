import requests  # pip install requests
res =  requests.get("https://www.jd.com/")
print(res.text)
with  open("jd.html","w",encoding='utf8') as f:
    f.write(res.text)