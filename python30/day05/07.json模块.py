
# 什么是JSON
# JSON中字符串只能是"" 双引号，但是python中'' 和"" 都可以表示字符串
# JSON中null-> python中的None
#

# JSON的序列化：将本语言支持的数据类型转化为json字符串的过程
# JSON的反序列化：将JSON字符串转化为本语言支持的数据对象类型


import json

s = 'hello world'
b = True
i = 100
l = [s,b,i]
d = {"name":"李攀祥","age":18,"hobby":None}

# print(repr(s))
# print(str(s))

# print(json.dumps(s))  # "hello world"
print(json.dumps(b))
# print(json.dumps(i))
# print(json.dumps(l))

# 重点的两个参数
# dumps和dump默认是中文，转化为Ascii的，数据中如果有中文，可以吧这个功能关闭，默认是打开的
# print(json.dumps(d,,indentensure_ascii=False=4))
# indent缩进，默认没有设置，转换后就是一行，不规范，可以添加indent=4来进行缩进，也就是成了我们所谓的标准的json格式

'''
def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):

json def dumps(obj: Any,
          *,
          skipkeys: bool = ...,
          ensure_ascii: bool = ...,    # 中文默认是使用Ascii，故中文转化不成功
          check_circular: bool = ...,
          allow_nan: bool = ...,
          cls: Optional[Type[JSONEncoder]] = ...,
          indent: Union[None, int, str] = ...,   # 缩进默认 没有设置，所以会一行显示，所以可以设置为indent=4
          separators: Optional[Tuple[str, str]] = ...,
          default: Optional[(Any) -> Any] = ...,
          sort_keys: bool = ...,
          **kwds: Any) -> str
'''


'''  https://blog.csdn.net/xc_zhou/article/details/80952314
因此 str() 与 repr() 的不同在于：

str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
'''

# # json.dumps之后的和python一点关系都没有，是JSON类型的字符串，所有语言都认识。
# print(repr(json.dumps(s)))  # '"hello world"'
# print(repr(json.dumps(b)))  # 'true'
# print(repr(json.dumps(i)))  # '100'
# print(repr(json.dumps(l)))  # '["hello world", true, 100]'
# print(repr(json.dumps(d)))  # '{"name": "lpx", "age": 18}'



# 应用一：将JSON字符串存储到文件中

# with open('json.txt','w',encoding='utf8') as f:
#     f.write(json.dumps(d))
# # json.txt : {"name": "lpx", "age": 18, "hobby": null}

# 应用二：反序列化：
with open('json.txt',"r",encoding='utf8') as f :
    json_str = f.read()

print(json_str) # {"name": "lpx", "age": 18, "hobby": null}
data = json.loads(json_str)
print(data)     # {'name': 'lpx', 'age': 18, 'hobby': None}
print(type(data))       # <class 'dict'>
print(type(json_str))   # <class 'str'>


# 思考1：
# 这种也能转换，因为我们自己写的字符串也是符合JSON格式，
# 只要是符合JSON字符串的字符串就可以使用json.loads来用来反序列化
#
json.loads()
data2 = json.loads('[{"k1":"v1"},{"name":null},{}]')
print(data2)        # [{'k1': 'v1'}, {'name': None}, {}]
print(type(data2))  # <class 'list'>





# JSON文件 反序列化：
with open(r"D:\Users\Desktop\data.json",'r',encoding="utf8") as f:
    data3 = json.load(f)
print(data3)
print(type(data3))

# JSON文件的序列化：
with open("json.txt",'w',encoding="utf8") as f:
    json.dump(data3,f)


# dumps和loads是对字符串进行序列化和反序列化
# dump和load是对文件进行序列化和反序列化，（不用管多少行）