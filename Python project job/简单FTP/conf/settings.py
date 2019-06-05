# -*- coding:utf-8 -*-
import os,sys
COF_DIR = os.path.abspath(os.path.dirname(__file__))
USER_DIR = os.path.dirname(COF_DIR)
data_path = os.path.join(USER_DIR,'data\\')

#用户数据存放路径
user_file = os.path.join(data_path,'login_user')