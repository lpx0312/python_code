
import subprocess
import json
import  struct


# total_num = str(len('李攀祥'.encode('utf8')))
# print('李攀祥'.encode('utf8'))
# print(len('李攀祥'.encode('utf8')))
# print(total_num)

cmd = 'ipconfig'
# 处理命令的流程
sendResult = subprocess.Popen(cmd, shell=True,
                              stdout=subprocess.PIPE,  # 标准输出
                              stderr=subprocess.PIPE  # 标准错误
                              )
stdout = sendResult.stdout.read()  # 这里返回的是 二进制
stderr = sendResult.stderr.read()  # 这里返回的是 二进制
#
# print('本机命令执行结果stdout{}'.format(stdout.decode('utf8')))
# print('本机命令执行结果stderr{}'.format(stderr.decode('utf8')))

# 如果使用utf8会报错
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc5 in position 13: invalid continuation byte
# 因为 windows下执行的命令，默认是gbk执行的
# print(stdout.decode('gbk'))
# 制作报头
header_dic = {
    'total_size': len(stderr) + len(stderr),
    'filename': None,
    'md5': None
}
header_json = json.dumps(header_dic)  # 将 dic 制作成 json字符串
header_bytes = header_json.encode('utf8')  # 将json字符串转化成 二进制 bytes类型（但是这个长度是可变的）

# 将长度可变的json字符串的二进制数字转化为固定长度的内容
print(header_bytes)
print(len(header_bytes))
pa = struct.pack('i',len(header_bytes))
print(pa)

print(struct.unpack('i',pa))
