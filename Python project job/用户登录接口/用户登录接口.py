#-*- coding:utf-8 -*-
'''
--------------------
输入用户密码
输入三次后锁定
认证后显示欢迎信息
--------------------
'''
#编写者：项思凯
#英文名：kevin Xiang
userall = {}    #空字典。
count = 0       #建立变量0。
print("Pytion用户登陆接口") #输出文字。
while count <3:    #创建死循环，count小于等于3停止。
        user_file = open("user.txt")   #用户文件。
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
                exit()   #关闭程序。
            else:   #判断用户密码不匹配就执行下面。
                print("\033[31;1m您输入的密码错误，请重新输入\033[0m")
                count +=1   #count变量每循环一次就加1。
                if count ==3:   #判断如果count循环三次。
                    userall[login_name]["look"] = 1 #如果条件成立就更改look的值为1。
                    user_file2 = open('user.txt','w+')  #开启文件的读写权限。
                    for n in userall.values():  #只循环。userall的值。
                        n_1 = [n["username"],n["password"],str(n['look'])]  #将值添加到对应列表。
                        n_2 = ','.join(n_1)     #以“，”分割将列表转换为字符串。
                        user_file2.write(n_2 + '\n')    #内容写入文件内覆盖内容。
                    user_file2.close()           #关闭文件。
                    print("\033[33;1m您的用户以被锁定\033[0m".center(50,"-"))    #输出文字。

        else:   #判断如果输入用户错误就执行下面。
             print("\033[31;1m您输入的用户名错误\033[0m")  #输出内容。