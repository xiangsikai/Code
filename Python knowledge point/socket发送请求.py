# by luffycity.com

import socket
import requests

# 方式一
ret = requests.get('https://www.baidu.com/s?wd=alex')


# 方式二
client = socket.socket()

# 百度创建连接: 阻塞
client.connect(('www.baidu.com',80))

# 问百度我要什么？
client.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')

# 我等着接收百度给我的回复
chunk_list = []
while True:
    chunk = client.recv(8096)
    if not chunk:
        break
    chunk_list.append(chunk)

body = b''.join(chunk_list)
print(body.decode('utf-8'))

