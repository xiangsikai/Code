import os,sys,json
auth_admin_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(auth_admin_path)
from db import user
from db import user_path
from conf import settiings

def admin_add():
    """添加用户"""
    while True:
        username =input("输入要注册的用户名>>：").strip()
        if len(username) == 0:
            print("用户名不能为空")
        password_1 = input("输入创建密码>>：").strip()
        password_2 = input("请再次输入密码>>：").strip()
        if password_1 == password_2:
            admin_list = []
            user.user_file["User"].setdefault(username,{"password":password_1,"key":0})
            admin_list.append(user.user_file)
            with open("%s\\user.py" %user_path.path_list_db,"w") as add:
                add.write("user_file = %s" %json.dumps(admin_list[0]))
            print("注册成功")
            break
        else:
            print("密码确认错误，请重新输入")

def admin_del():
    """删除用户"""
    while True:
        username =input("输入要删除的用户>>：").strip()
        if len(username) == 0:
            print("用户名不能为空")
        if username in list(user.user_file["User"]):
            admin_list = []
            del user.user_file["User"][username]
            admin_list.append(user.user_file)
            with open("%s\\user.py" %user_path.path_list_db,"w") as del_user:
                del_user.write("user_file = %s" %json.dumps(admin_list[0]))
            print("删除成功")
            break

def login_admin():
    while True:
        print(settiings.ATM_ADMIN_LIST)
        admin_count = input(">>:").strip()
        if len(admin_count) == 0 or not admin_count.isdigit():
            print("输入错误")
        elif 1 <= int(admin_count) <= 2:
            admin_command[admin_count]()
            break

admin_command = {"1":admin_add,
                 "2":admin_del,}

