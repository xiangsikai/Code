#！-*- coding:utf-8 -*-
import os,sys
conf_auth_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(conf_auth_path)


ATM_LIST =  "\n--------ATM---------\n" \
            "丨 -1-    现金存款 |\n" \
            "丨 -2-    用户转账 |\n"\
            "丨 -3-    存款提现 |\n" \
            "丨 -4-    账户查询 |\n" \
            "丨 -5-    退出ATM  |\n"

ATM_ADMIN_LIST = "\n=----管理员页面-----=\n" \
                 "-    1.注册用户     -\n" \
                 "-    2.删除用户     -\n" \

ATM_LIST_ALL = "\n=-----ATM+购物车---=\n" \
               "-   1.ATM客户端    -\n" \
               "-   2.ATM管理端    -\n" \
               "-   3.购物车平台   -\n" \
               "-   4.退出该平台   -\n"




