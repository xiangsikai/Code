#-*- coding:utf-8 -*-
import os,sys,json
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_path)
from core import transaction
from conf import settiings
from core import auth
ATM_PRICE = {
        '1':transaction.deposit,
        '2':transaction.transfer_account,
        '3':transaction.enchashment,
        '4':transaction.account_inquiry,
        }
def main_main(username):
    """主引导模块"""
    flag = True
    while flag:
        print(settiings.ATM_LIST)
        main_count = input(">>>：").strip()
        if len(main_count) == 0 or not main_count.isdigit():
            print("请输入数字。\n")
            continue
        if 1 <= int(main_count) <= 4:
            ATM_PRICE[main_count](username)
        if int(main_count) == 5:
            break

def run():
    """执行模块"""
    auth.login()
    main_main(auth.username)



