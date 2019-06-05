import os,sys
list_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(list_path)
from conf import settiings
from core import auth_admin
from core import main
from shopping_mall import shop_bin
list_all = {"1":main.run,
            "2":auth_admin.login_admin,
            "3":shop_bin.shop_list}

def list():
    """总接口模块"""
    while True:
        print(settiings.ATM_LIST_ALL)
        admin_list = input(">>:").strip()
        if len(admin_list) == 0 or not admin_list.isdigit():
            print("输入错误")
        elif 1 <= int(admin_list) <= 3:
            list_all[admin_list]()
        elif int(admin_list) == 4:
            exit()

