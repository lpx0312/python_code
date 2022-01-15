

import socket


sock = socket.socket()
sock.bind(("127.0.0.1",8888))
sock.listen(5)

while 1:

	print("server is waiting...")
	conn,addr = sock.accept()
	data = conn.recv(1024)
	print("data:",data)

	# 打开文件，读取数据
	with open("index2.html", "rb") as f:
		html_bytes = f.read()
	conn.send(b"HTTP1.1 200 ok\r\n\r\n"+html_bytes)


