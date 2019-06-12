# by luffycity.com
"""
pip3 install requests

"""
import threading
import requests
import uuid

url_list = [
    'https://www3.autoimg.cn/newsdfs/g28/M05/F9/98/120x90_0_autohomecar__ChsEnluQmUmARAhAAAFES6mpmTM281.jpg',
    'https://www2.autoimg.cn/newsdfs/g28/M09/FC/06/120x90_0_autohomecar__ChcCR1uQlD6AT4P3AAGRMJX7834274.jpg',
    'https://www2.autoimg.cn/newsdfs/g3/M00/C6/A9/120x90_0_autohomecar__ChsEkVuPsdqAQz3zAAEYvWuAspI061.jpg',
]

def task(url):
    """"""

    """
    1. DNS解析，根据域名解析出IP
    2. 创建socket客户端    sk = socket.socket()
    3. 向服务端发起连接请求 sk.connect()
    4. 发送数据（我要图片） sk.send(...)
    5. 接收数据            sk.recv(8096)

    接收到数据后写入文件。
    """
    ret = requests.get(url)
    file_name = str(uuid.uuid4()) + '.jpg'
    with open(file_name, mode='wb') as f:
        f.write(ret.content)

for url in url_list:

    t = threading.Thread(target=task,args=(url,))
    t.start()
