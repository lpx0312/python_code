# names1 = ["张三","李四","王五","王二麻子"]
#
# names1.sort()
# print(names1) #['张三', '李四', '王二麻子', '王五']


# names1 = ["b","a","d","c"]
# names1.sort()
# print(names1)   # ['a', 'b', 'c', 'd']
#
# names1.sort(reverse=True) #倒序
# print(names1)

#
# names1 = ["ba","ab","db","cd"]
# names1.sort()
# print(names1)   # ['ab', 'ba', 'cd', 'db']


# s = "sldfla"
# print(s[::-1])
# >>> alfdls


dic = {"name":"lpx"}
dic.setdefault("age",23)
print(dic)

# 如果只是 *dic 则默认会 key，并不是value
print("name:{}  age:{}".format(*dic.values()))