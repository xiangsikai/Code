#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#作者：项思凯 英文名：Kevin Xiang
#工资管理系统
#登陆注册，输错三次锁定账户。
#增加用户，删除用户，修改工资，查看用户信息。
#退出，打印列表。
import sys,time
def login_user():
    userall = {}    #空字典。
    count = 0       #建立变量0。
    print("\n《工资管理系统 |  登陆平台》") #输出文字。
    while count <3:    #创建死循环，count小于等于3停止。
        user_file = open("用户文件.txt")   #用户文件。
        login_name = input("请输入用户：")             #创建交互变量，输入用户名。
        login_password = input("请输入密码：")         #创建交互变量，输入密码。
        for i in user_file:     #for循环用户文件。
             userlist = i.strip()    #for循环打印去掉空格符
             userdata = userlist.split(",")                  #以“，”分割文件字符。
             user_name = userdata[0].strip()                 #切割打印，第一个字符。
             user_pass = userdata[1].strip()                 #切割打印，第二个字符。
             user_look = userdata[2].strip()
             userall[user_name] ={'username':user_name,'password':user_pass,"look":user_look} #创建字典。
        user_file.close()   #关闭文件。
        if  login_name in userall.keys():      #判断用户是否在用户列表内。
            if userall[login_name]["look"] == '1':         #判断用户是否在黑名单。
                print("\033[41;1m你的用户以被锁，请联系管理员\033[0m")      #输出文字。
                exit()  #关闭程序。
            if login_name == userall[login_name]['username'] and login_password == userall[login_name]['password']: #判用户件与密码。
                print('\033[32;1m欢迎登陆\033[0m'.center(50,"-"))         #输出文字。
                main_2()
            else:   #判断用户密码不匹配就执行下面。
                print("\033[31;1m您输入的密码错误，请重新输入\033[0m")
                count +=1   #count变量每循环一次就加1。
                if count ==3:   #判断如果count循环三次。
                    userall[login_name]["look"] = 1 #如果条件成立就更改look的值为1。
                    user_file2 = open('用户文件.txt','w+')  #开启文件的读写权限。
                    for n in userall.values():  #只循环。userall的值。
                        n_1 = [n["username"],n["password"],str(n['look'])]  #将值添加到对应列表。
                        n_2 = ','.join(n_1)     #以“，”分割将列表转换为字符串。
                        user_file2.write(n_2 + '\n')    #内容写入文件内覆盖内容。
                    user_file2.close()           #关闭文件。
                    print("\033[33;1m您的用户以被锁定\033[0m".center(50,"-"))    #输出文字。
                    main_1()
        else:   #判断如果输入用户错误就执行下面。
             print("\033[31;1m您输入的用户名错误\033[0m")  #输出内容。
def register_user():
    """注册用户"""
    username_pass_list = {}
    with open("用户文件.txt","r") as username_file:
        for i in username_file:
             userlist = i.strip()
             userdata = userlist.split(",")
             user_name1 = userdata[0].strip()
             user_pass1 = userdata[1].strip()
             user_look1 = userdata[2].strip()
             username_pass_list[user_name1] ={'username':user_name1,'password':user_pass1,"look":user_look1}
        flag = True
        while flag:
            user_name = input("输入注册的用户名:>>>").strip()
            user_pass = input("输入%s的密码:>>>" % (user_name)).strip()
            if user_name in username_pass_list:
                    print("用户已存在")
            else:
                username_pass_list.setdefault(user_name,{"username":user_name,"password":user_pass,"look":"0"})
                user_file2 = open('用户文件.txt','w+')
                flag1 = False
                for n in username_pass_list.values():  #只循环。userall的值。
                    flag1 = True
                    n_1 = [n["username"],n["password"],str(n['look'])]
                    n_2 = ','.join(n_1)
                    user_file2.write(n_2 + '\n')
                user_file2.close()
                if  flag1:
                    print("用户注册成功，正在跳转到登陆界面")
                    for i in range(30):
                        sys.stdout.write("-")
                        sys.stdout.flush()
                        time.sleep(0.1)
                    login_user()
                else:
                    print("注册失败")
def read_file_db():
    """读数据库"""
    temp_list = []
    with open("数据库.txt") as txt_file:
        for lines in txt_file:
            temp_dict = dict()
            temp_str = lines.strip().split()
            temp_dict[temp_str[0]] = {"salary":temp_str[1]}
            temp_list.append(temp_dict)

    return temp_list
def write_file_db(user_info_dic):
    """写数据库"""
    with open("数据库.txt","w") as user_info:
        for line in user_info_dic:
            username = list(line)[0]
            salary = line[username]["salary"]
            user_info.write("%s %s\n" % (username,salary))
        return "OK"
def add_user():
    """添加用户"""
    flag = True
    while flag:
        xinxi()
        user_info_dic = read_file_db()
        user_name = input("输入添加用户名|按q退出:>>>").strip()
        if user_name == "q" or user_name == "Q":
            flag = False
            continue
        salary = input("输入新添加的用户资金:>>>").strip()
        username_list = []
        if len(user_name) == 0 or len(salary) == 0 or not salary.isdigit():
            print("输入用户名或资金错误，重新输入")
            continue
        for user_info in user_info_dic:
            username = list(user_info.keys())[0]
            username_list.append(username)
        if user_name in username_list:
            print("用户已存在")
            continue
        else:
            temp_dict = dict()
            temp_dict[user_name] = {"salary":salary}
            user_info_dic.append(temp_dict)
        result = write_file_db(user_info_dic)
        if result == "OK":
            input("添加成功,按任意键继续:>>>")
def del_user():
    """删除用户"""
    flag = True
    while flag:
        xinxi()
        user_info_dic = read_file_db()
        user_name = input("输入要删除的用户名|按q退出:>>>").strip()
        if user_name == "Q" or user_name == "q":
            flag = False
            continue
        elif len(user_name) == 0:
            print("用户名信息不能为空")
            continue
        user_exit_flag = False
        count = 0
        for user_info in user_info_dic:
            username = list(user_info.keys())[0]
            if username == user_name:
                user_exit_flag = True
                del user_info_dic[count]
                write_file_db(user_info_dic)
            count += 1
        if user_exit_flag:
            input("用户已经删除,按任意键继续")
        else:
            input("未找到 %s" % user_name)
def update():
    user_info_dic = read_file_db()
    flag = True
    while flag:
        xinxi()
        user_name = input("输入用户需修改的用户名|按q退出:>>>").strip()
        if user_name == "q" or user_name == "Q":
            flag = False
            continue
        salary = input("输入用户修改的工资:>>>").strip()
        if len(salary) == 0 or not salary.isdigit():
            print("输入工资错误！！！")
            continue
        user_exit_flag2 = False
        count = 0
        for line4 in user_info_dic:
            username = list(line4.keys())[0]
            if user_name == username:
                user_exit_flag2 = True
                user_info_dic[count][username]["salary"] = salary
                write_file_db(user_info_dic)
            count += 1
        if user_exit_flag2:
            print("%s 用户修改资金为 %s 已修改成功！！！" % (user_name,salary))
        else:
            print("输入用户名错误请重新输入")
def search_user():
    user_info_dic = read_file_db()
    flag = True
    while flag:
        xinxi()
        user_name = input("输入查询用户名称|按q退出:>>>").strip()
        if user_name == "q" or user_name == "Q":
            flag = False
            continue
        elif len(user_name) == 0:
            print("请输入正确用户名")
            continue
        user_exit3 = False
        count = 0
        for line in user_info_dic:
            username = list(line.keys())[0]
            if username == user_name:
                user_exit3 = True
                salary = user_info_dic[count][username]["salary"]
                print("用户：%s\n资金：%s" % (username,salary))
            count += 1
        if  user_exit3:
            input("按任意键退出")
            break
        else:
            print("输入用户错误！！！")
def uhelp():
    """帮助信息"""
    with open("帮助信息.txt","r") as help_user:
        print(help_user.read())
        input("输入任意键退出:>>>")
def xinxi():
    """用户信息"""
    print("\n")
    print("↓----------------------↓")
    for xin in read_file_db():
        xin_1 = list(xin.keys())[0]
        print("    用户名:",xin_1)
def main_2():
    """主逻辑区"""
    list_1 =    {"1": ["添加账户", add_user],
                 "2": ["删除用户", del_user],
                 "3": ["查询用户", search_user],
                 "4": ["修改工资", update],
                 "5": ["帮助信息", uhelp]}
    flag = True
    while flag:
        print("\n#-+-+-+-+-+-+-+-+-+-#")
        print(1,"   ",list_1["1"][0].center(8,"-"))
        print(2,"   ",list_1["2"][0].center(8,"-"))
        print(3,"   ",list_1["3"][0].center(8,"-"))
        print(4,"   ",list_1["4"][0].center(8,"-"))
        print(5,"   ",list_1["5"][0].center(8,"-"))
        print("#-+-+-+-+-+-+-+-+-+-#")
        bianhao = input("输入操作编号|按q退出:>>>").strip()
        if bianhao == "q" or bianhao == "Q":
            exit()
            continue
        elif not bianhao.isdigit() or len(bianhao) == 0:
            print("输入数字序号1 ~ 5")
            continue
        else:
            if 0 < int(bianhao) < 7:
                list_1[bianhao][1]()
def main_1():
    list_1 = {"1": ["登陆账户", login_user],
              "2": ["账户注册", register_user]}
    flag = True
    while flag:
        print("\n《工资管理平台登陆系统》")
        print("#-+-+-+-+-+-+-+-+-+-#")
        print(1,"   ",list_1["1"][0].center(8,"-"))
        print(2,"   ",list_1["2"][0].center(8,"-"))
        print("#-+-+-+-+-+-+-+-+-+-#")
        bianhao = input("输入操作编号|按q退出:>>>").strip()
        if bianhao == "q" or bianhao == "Q":
            flag = False
            continue
        elif not bianhao.isdigit() or len(bianhao) == 0:
            print("输入数字序号1 ~ 2")
            continue
        else:
            if 0 < int(bianhao) < 3:
                list_1[bianhao][1]()

main_1()

