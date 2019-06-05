#！-*- coding:utf-8 -*-
import os,sys,json
login_command_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(login_command_path)
from db import user_path


def login_initial(username,cash):
    """创建新用户的个人文件"""
    login_file = {
        username:{
            'cash':cash,
            'deposit':0
        }
    }
    with open("%s\\user_account\\%s" %(user_path.path_list_db,username),"w") as login_w:
        login_w.write(json.dumps(login_file))

