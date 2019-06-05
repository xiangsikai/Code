#！-*- coding:utf-8 -*-
import os,sys,json,logging
auth_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(auth_path)
from db import user
from db import user_path
from core import login_command
from log import loger

def auth_login(func):
    """检测用户登陆状态"""
    def auth():
        if func():
             print("\n-------登录成功-------")
             logging.info("User:%s Successful user login !!!"%(username))
    return auth

@auth_login
def login():
    """用户登陆"""
    flag = True
    while flag:
        print("-------登录接口-------\n")
        acc = False
        global username
        username = input("登录账户>>").strip()
        password = input("登录密码>>").strip()
        if len(username) == 0 or len(password) == 0:
            print("输入不能为空")
        if username == list(user.user_file["User"])[0] or password == user.user_file["User"][username]["password"]:
            if int(user.user_file["User"][username]["key"]) == 0:
                ufile = []
                user.user_file["User"][username]["key"] = 1
                ufile.append(user.user_file)
                with open("%s\\user.py" %user_path.path_list_db,"w") as w_key:
                    w_key.write("user_file = %s" %json.dumps(ufile[0]))
                cash = input("输入已拥有的现金>>").strip()
                login_command.login_initial(username,cash)
                continue
            else:
                with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"r") as r_user:
                    user_afile = json.loads(r_user.read())
                    print("账户名：%s   存款：%s     现金：%s"%(username,user_afile[username]["deposit"],user_afile[username]["cash"]))
                    acc = True
                    return acc
        else:
            print("用户名或密码错误")
