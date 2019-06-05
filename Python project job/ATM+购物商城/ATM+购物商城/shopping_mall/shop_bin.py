#!-*- coding:utf-8 -*-
import os,sys,json
shop_bin__path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(shop_bin__path)
from core import auth
from db import user_path
shopping_list =  "\033[31;1m丨-------\033[0m" \
                 "\033[35;1mS\033[0m" \
                 "\033[33;1mh\033[0m" \
                 "\033[36;1mo\033[0m" \
                 "\033[32;1mp\033[0m" \
                 "\033[34;1mp\033[0m" \
                 "\033[35;1mi\033[0m" \
                 "\033[33;1mn\033[0m" \
                 "\033[36;1mg\033[0m " \
                 "\033[32;1mL\033[0m" \
                 "\033[33;1mi\033[0m" \
                 "\033[34;1ms\033[0m" \
                 "\033[35;1mt\033[0m" \
                 "\033[31;1m-------丨\n\033[0m" \
                 "\033[32;1m/商品号-\033[0m     \033[33;1m-商品名-\033[0m     \033[36;1m-价钱\\\n\033[0m" \
                 "\033[34;1m< 1 >        皮带        1000\n\033[0m" \
                 "\033[35;1m< 2 >        皮鞋        2000\n\033[0m" \
                 "\033[33;1m< 3 >        西装        3000\n\033[0m" \
                 "\033[36;1m< 4 >        手表        4000\n\033[0m" \
                 "\033[32;1m< 5 >        手机        5000\n\033[0m"

shopping_price = {
        '1':{"name":"皮带","price":"1000"},
        '2':{"name":"皮鞋","price":"2000"},
        '3':{"name":"西装","price":"3000"},
        '4':{"name":"手表","price":"4000"},
        '5':{"name":"手机","price":"5000"},
        }

def shop_list():
    """主引导模块"""
    flag = True
    while flag:
        if not auth.login():
            print(shopping_list)
            shop_count = input("\033[30;1m输入购买的商品号>>\033[0m").strip()
            if shop_count in shopping_price:
                merchandise_price = shopping_price[shop_count]["price"]
                merchandise_name = shopping_price[shop_count]["name"]
                with open("%s\\user_account\\%s"%(user_path.path_list_db,auth.username),"r") as shop_r:
                    user_account = json.loads(shop_r.read())
                    user_cash = user_account[auth.username]["cash"]
                    user_deposit = user_account[auth.username]["deposit"]
                if int(merchandise_price) <= int(user_deposit):
                    new_deposit = int(user_deposit) - int(merchandise_price)
                    user_account[auth.username]["deposit"] = new_deposit
                    with open("%s\\user_account\\%s" %(user_path.path_list_db,auth.username),"w") as shop_w:
                        shop_w.write(json.dumps(user_account))
                        print("用户：%s    \n已购买:%s    花费：%s \n"
                            "账户余额：%s"%(auth.username,merchandise_name,merchandise_price,new_deposit))
                else:
                    print("您的账户余额不足")
            shop_acc = input("\n任意键继续，退出请按q\n"
                                 ">>").strip()
            if shop_acc == "q":
                print("\033[32;1m\n(•‾⌣‾•) 谢谢回顾！！！ \033[0m")
                flag = False

