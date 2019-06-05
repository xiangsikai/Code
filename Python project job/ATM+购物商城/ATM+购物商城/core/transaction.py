#！-*- coding:utf-8 -*-
import os,sys,json,logging
transaction_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(transaction_path)
from db import user_path
from db import user
from log import loger

def deposit(username):
    """现金存款"""
    while True:
        deposit_cash = input("输入需要存款的金额>>:").strip()
        if len(deposit_cash) == 0 or not deposit_cash.isdigit():
            print("请输入数字。\n")
        with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"r") as deposit_r:
            user_account = json.loads(deposit_r.read())
            user_cash = user_account[username]["cash"]
            user_deposit = user_account[username]["deposit"]
            if int(user_cash) >= int(deposit_cash):
                ucash = int(user_cash) - int(deposit_cash)
                udeposit = int(deposit_cash) + int(user_deposit)
                user_account[username]["cash"] = ucash
                user_account[username]["deposit"] = udeposit
                with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"w") as deposit_w:
                    deposit_w.write(json.dumps(user_account))
                print("\033[32;1m充值成功！\033[0m 用户:%s  存款：%s   现金：%s"%(username,udeposit,ucash))
                logging.info("User:%s   Deposit:%s"%(username,deposit_cash))
                break
            else:
                print("现金不足，您的现金余额为:%s "%(user_cash))

def transfer_account(username):
    """用户转账"""
    while True:
        transfer_user = input("输入转账用户>>：").strip()
        if transfer_user in list(user.user_file['User']):
            if user.user_file['User'][transfer_user]["key"] == 1:
                with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"r") as deposit_r_u1:
                    user_account_u1 = json.loads(deposit_r_u1.read())
                    user_deposit_u1 = user_account_u1[username]["deposit"]
                transfer_deposit = input("输入转账金额>>：").strip()
                if int(user_deposit_u1) >= int(transfer_deposit):
                    user_deposit_u1_transfer = int(user_deposit_u1) - int(transfer_deposit)
                    user_account_u1[username]["deposit"] = int(user_deposit_u1_transfer)
                    with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"w") as deposit_w_u1:
                        deposit_w_u1.write(json.dumps(user_account_u1))
                    with open("%s\\user_account\\%s"%(user_path.path_list_db,transfer_user),"r") as deposit_r_u2:
                        user_account_u2 = json.loads(deposit_r_u2.read())
                        user_deposit_u2 = user_account_u2[transfer_user]["deposit"]
                        user_deposit_u2_transfer = int(user_deposit_u2) + int(transfer_deposit)
                        user_account_u2[transfer_user]["deposit"] = user_deposit_u2_transfer
                    with open("%s\\user_account\\%s"%(user_path.path_list_db,transfer_user),"w") as deposit_w_u2:
                        deposit_w_u2.write(json.dumps(user_account_u2))
                    print("\033[32;1m\n转账成功！！！\033[0m "
                          "账户:%s    余额：%s   转账金额：%s"%(username,user_deposit_u1_transfer,transfer_deposit) )
                    logging.info("User:%s   Transfer_user:%s    Transfer_deposit:%s"%(username,transfer_user,transfer_deposit))
                    break
                else:
                    print("账户存款不足 存款余额：%s"%(user_deposit_u1))
            else:
                print("该用户已注册，未开通个人账户。\n")
        else:
                print("输入“%s”未注册用户"%(transfer_user))

def enchashment(username):
    """存款提现"""
    while True:
        with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"r") as cash_enchashment_r:
            user_account = json.loads(cash_enchashment_r.read())
            user_cash = user_account[username]["cash"]
            user_deposit = user_account[username]["deposit"]
        user_enchashment = input("请输入提现金额>>：").strip()
        if len(user_enchashment) == 0 or not user_enchashment.isdigit():
            print("请输入数字。\n")
            continue
        elif int(user_deposit) >= int(user_enchashment):
            service_charge = int(user_enchashment) * 0.05
            user_enchashment_deposit = int(user_deposit) - int(user_enchashment) - service_charge
            user_enchashment_cash = int(user_cash) + int(user_enchashment)
            user_account[username]["cash"] = user_enchashment_cash
            user_account[username]["deposit"] = user_enchashment_deposit
            with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"w") as cash_enchashment_w:
                cash_enchashment_w.write(json.dumps(user_account))
            print("\033[32;1m\n提现成功！！！\033[0m"
                  "账户:%s    现金：%s  存款：%s    \n"
                  "提取现金：%s      手续费：%s"%(username,user_enchashment_cash,int(user_enchashment_deposit),user_enchashment,service_charge))
            logging.info("User:%s   Enchashment:%s"%(username,user_enchashment))
            break
        else:
            print("存款余额不足 存款余额：%s"%(user_deposit))

def account_inquiry(username):
    """账户查询"""
    with open("%s\\user_account\\%s"%(user_path.path_list_db,username),"r") as account_inquiry_r:
            user_account = json.loads(account_inquiry_r.read())
            user_cash = user_account[username]["cash"]
            user_deposit = user_account[username]["deposit"]
    print("用户：%s\n现金：%s\n存款：%s"%(username,user_cash,user_deposit))
    logging.info("User:%s   Account_inquiry"%(username))
