# -*- coding:utf-8 -*-
import os,sys
core_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(core_path)
from conf import settings
from src import socket

class ftp_login(object):
    """FTP用户登陆类"""

    def login_acc(self,user,password):
        """匹配登陆用户"""
        with open(settings.user_file) as f:
            for i in f:
                uname,pas = i.split(",")
                pas.strip("\n")
                if uname == user and int(pas) == int(password):
                    return True

    def ftp_establist_home(self,user):
        """创建用户家目录"""
        user_mkdir = os.path.join(settings.data_path,user+"\\")
        if os.path.isdir(user_mkdir):
            pass
        else:
            os.mkdir(user_mkdir)

    def ftp_core(self):
        headline = "<FTP 登陆接口>\n"
        print(headline)
        flag = True
        while flag:
            user = input("用户名>>:").strip()
            password = input("密码>>:").strip()
            judeg = self.login_acc(user,password)
            if judeg:
                print("\n<选择类型>\n"
                      "1.server\n"
                      "2.client\n")
                while True:
                    mun = input("输入数字>>:").strip()
                    mun = int(mun)
                    if mun == int("1"):
                        print("Server启动成功--请启动Client ！！！")
                        self.ftp_establist_home(user)
                        username = ftp_run(user)
                        username.ftp_server(user)
                    elif mun == int("2"):
                        self.ftp_establist_home(user)
                        username = ftp_run(user)
                        username.ftp_client(user)
                    else:
                        print("只能输入 1 与 2")
                else:
                    print("用户名密码错误！！！")

class ftp_run(object):
    """执行视图类"""
    def __init__(self,user):
        self.user = user

    def ftp_view(self,user):
        mug = """
       \033[31;1m< 欢迎[%s] 登陆 F T P 管理平台>\033[0m
        |                                 |
        |    \033[29;1m下载>>:down 文件名\033[0m         |
        |    \033[33;1m上传>>:up 文件名\033[0m           |
        |    \033[35;1m退出平台>>: “q”\033[0m           |
        |                                 |
       ———————————————————
        """%(user)
        print(mug)

    def ftp_path(self,user):
        upath = os.listdir("%s%s\\"%(settings.data_path,user))
        count = 0
        for i in upath:
            count += 1
            print("家目录文件%s:[%s]"%(count,i))

    def ftp_server(self,user):
        sock = socket.ftp_socket(user)
        sock.socket_server(user)

    def ftp_client(self,user):
        self.ftp_view(user)
        sock = socket.ftp_socket(user)
        sock.socket_client(user)


