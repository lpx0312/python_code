
# # 如果文件不在了，就会报错
# # with open('b.txt', 'r') as f:
# #     print(f.read())
#
# try:
#     with open('b.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     # Exception 代表 所有错误
#     # FileNotFoundError 代表 文件不存在
#     # KeyError 键不存在
#     # IndexError 数组索引错误
#     # except 后面不加任何东西，包含的错误太广了，有些不是错误，例如sys.exit()也会报错 所有不建议使用

#     print('文件不存在')
#     print('发生错误,%s'%e)


