# by luffycity.com
import socket
import select

class Req(object):
    def __init__(self,sk,func):
        self.sock = sk
        self.func = func

    def fileno(self):
        return self.sock.fileno()


class Nb(object):

    def __init__(self):
        self.conn_list = []
        self.socket_list = []

    def add(self,url,func):
        client = socket.socket()
        client.setblocking(False)  # 非阻塞
        try:
            client.connect((url, 80))
        except BlockingIOError as e:
            pass
        obj = Req(client,func)
        self.conn_list.append(obj)
        self.socket_list.append(obj)

    def run(self):

        while True:
            rlist,wlist,elist = select.select(self.socket_list,self.conn_list,[],0.005)
            # wlist中表示已经连接成功的req对象
            for sk in wlist:
                # 发生变换的req对象
                sk.sock.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
                self.conn_list.remove(sk)
            for sk in rlist:
                chunk_list = []
                while True:
                    try:
                        chunk = sk.sock.recv(8096)
                        if not chunk:
                            break
                        chunk_list.append(chunk)
                    except BlockingIOError as e:
                        break
                body = b''.join(chunk_list)
                # print(body.decode('utf-8'))
                sk.func(body)
                sk.sock.close()
                self.socket_list.remove(sk)
            if not self.socket_list:
                break


def baidu_repsonse(body):
    print('百度下载结果：',body)

def sogou_repsonse(body):
    print('搜狗下载结果：', body)

def oldboyedu_repsonse(body):
    print('老男孩下载结果：', body)


t1 = Nb()
t1.add('www.baidu.com',baidu_repsonse)
t1.add('www.sogou.com',sogou_repsonse)
t1.add('www.oldboyedu.com',oldboyedu_repsonse)
t1.run()











#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# client1 = socket.socket()
# client1.setblocking(False) # 百度创建连接: 非阻塞
#
# try:
#     client1.connect(('www.baidu.com',80))
# except BlockingIOError as e:
#     pass
#
#
# client2 = socket.socket()
# client2.setblocking(False) # 百度创建连接: 非阻塞
# try:
#     client2.connect(('www.sogou.com',80))
# except BlockingIOError as e:
#     pass
#
#
# client3 = socket.socket()
# client3.setblocking(False) # 百度创建连接: 非阻塞
# try:
#     client3.connect(('www.oldboyedu.com',80))
# except BlockingIOError as e:
#     pass
#
# class Foo(object):
#     def __init__(self,sk):
#         self.sk = sk
#
#     def fileno(self):
#         return self.sk.fileno()
#
# """
# 1. select.select(socket_list,conn_list,[],0.005)
#     select监听的 socket_list/conn_list 内部会调用列表中每一个值的fileno方法，获取该返回值并去系统中检测。
#
# 2. 方式一：
#     select.select([client1,client2,client3],[client1,client2,client3],[],0.005)
# 3. 方式二：
#     select.select([Foo(client1),Foo(client2),(client3)],Foo(client1),Foo(client2),(client3),[],0.005)
# """
# socket_list = [Foo(client1),client2,client3] # client1.fileno
# conn_list = [client1,client2,client3]
#
# while True:
#     rlist,wlist,elist = select.select(socket_list,conn_list,[],0.005)
#     # wlist中表示已经连接成功的socket对象
#     for sk in wlist:
#         if sk == client1:
#             sk.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
#         elif sk==client2:
#             sk.sendall(b'GET /web?query=fdf HTTP/1.0\r\nhost:www.sogou.com\r\n\r\n')
#         else:
#             sk.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.oldboyedu.com\r\n\r\n')
#         conn_list.remove(sk)
#     for sk in rlist:
#         chunk_list = []
#         while True:
#             try:
#                 chunk = sk.recv(8096)
#                 if not chunk:
#                     break
#                 chunk_list.append(chunk)
#             except BlockingIOError as e:
#                 break
#         body = b''.join(chunk_list)
#         # print(body.decode('utf-8'))
#         print('------------>',body)
#         sk.close()
#         socket_list.remove(sk)
#     if not socket_list:
#         break

