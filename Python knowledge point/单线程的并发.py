# by luffycity.com
import socket
import select



client1 = socket.socket()
client1.setblocking(False) # 百度创建连接: 非阻塞

try:
    client1.connect(('www.baidu.com',80))
except BlockingIOError as e:
    pass


client2 = socket.socket()
client2.setblocking(False) # 百度创建连接: 非阻塞
try:
    client2.connect(('www.sogou.com',80))
except BlockingIOError as e:
    pass


client3 = socket.socket()
client3.setblocking(False) # 百度创建连接: 非阻塞
try:
    client3.connect(('www.oldboyedu.com',80))
except BlockingIOError as e:
    pass

socket_list = [client1,client2,client3]
conn_list = [client1,client2,client3]

while True:
    rlist,wlist,elist = select.select(socket_list,conn_list,[],0.005)
    # wlist中表示已经连接成功的socket对象
    for sk in wlist:
        if sk == client1:
            sk.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
        elif sk==client2:
            sk.sendall(b'GET /web?query=fdf HTTP/1.0\r\nhost:www.sogou.com\r\n\r\n')
        else:
            sk.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.oldboyedu.com\r\n\r\n')
        conn_list.remove(sk)
    for sk in rlist:
        chunk_list = []
        while True:
            try:
                chunk = sk.recv(8096)
                if not chunk:
                    break
                chunk_list.append(chunk)
            except BlockingIOError as e:
                break
        body = b''.join(chunk_list)
        # print(body.decode('utf-8'))
        print('------------>',body)
        sk.close()
        socket_list.remove(sk)
    if not socket_list:
        break

