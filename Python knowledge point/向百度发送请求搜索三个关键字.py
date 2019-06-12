# by luffycity.com

import socket
import requests
# #################### 解决并发：单线程 ####################
# 方式一
key_list = ['alex','db','sb']
for item in key_list:
    ret = requests.get('https://www.baidu.com/s?wd=%s' %item)

# 方式二
def get_data(key):
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

key_list = ['alex','db','sb']
for item in key_list:
    get_data(item)


# #################### 解决并发：多线程 ####################
import threading

key_list = ['alex','db','sb']
for item in key_list:
    t = threading.Thread(target=get_data,args=(item,))
    t.start()

# #################### 解决并发：单线程+IO不等待 ####################
# IO请求？
# 数据回来了？