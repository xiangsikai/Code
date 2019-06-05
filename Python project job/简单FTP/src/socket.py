#_*_ coding:utf-8 _*_
import socket,os,sys
socket_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(socket_path)
from conf import settings
from core import core

class ftp_socket(object):
    """socket上传下载类"""
    def __init__(self,user):
        self.user = user

    def socket_client(self,user):
        """socket客户端"""
        while True:
            client = socket.socket()
            client.connect(('localhost',6969))
            home = core.ftp_run(user)
            home.ftp_path(user)
            msg = input(">>:").strip()
            if len(msg) == 0:continue
            elif msg == "q" :exit()
            client.send(msg.encode("utf-8"))
            acc,filename = msg.split()
            if acc == "down":
                    data = client.recv(10240000)
                    f = open(filename,"wb")
                    f.write(data)
                    print("下载成功！！！\n")
                    f.close()
            elif acc == "up":
                    f = open(filename,"rb")
                    data = f.read()
                    client.send(data)
                    print("上传成功！！！\n")
            client.close()

    def socket_server(self,user):
        """服务端"""
        while True:
            server = socket.socket()
            server.bind(('localhost',6969))
            server.listen()
            conn,addr = server.accept()
            msg = conn.recv(10240000)
            acc,filename = msg.split()
            filename = filename.decode()
            if acc.decode() == "down":
                print("%s%s/%s"%(settings.data_path,user,filename))
                f = open("%s%s/%s"%(settings.data_path,user,filename),"rb")
                data = f.read()
                conn.sendall(data)
            elif acc.decode() == "up":
                data = conn.recv(10240000)
                f = open("%s%s/%s"%(settings.data_path,user,filename),"wb")
                f.write(data)
                f.close()
            server.close()
