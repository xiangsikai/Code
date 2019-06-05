#-*- coding:utf-8 -*-
#修改语法
#UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
import os,sys
update_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(update_path)

from core import man

def update_run(cmd):
    '''sql修改用户信息'''

    while True:
        #截取sql关键词
        update_list = cmd.split()
        update_keylist = update_list[3]
        update_nature1,update_keyword1 = update_keylist.split("=")
        update_nature2 = update_list[-3]
        update_keyword2 = update_list[-1]

        #判断sql对应的key值是否相同
        if update_nature1 == update_nature2:
            values = []

            #读取文件
            with open("%s\\db\\file.txt"%(update_path),'r+') as update_file:
                for line in update_file:
                    if not line.strip():
                        continue
                    lines = line.strip()
                    update_dict = man.sql_dict(lines)
                    dict_value = man.sql_dict_value(update_dict)
                    if update_dict[update_nature1] == update_keyword1.strip('"'):
                        update_dict[update_nature2] = update_keyword2.strip('"')
                        dict_value = man.sql_dict_value(update_dict)
                        values.append(dict_value)
                    else:
                        values.append(dict_value)
            #写入文件
            with open("%s\\db\\file.txt"%(update_path),'w+') as update_file:
                for val in values:
                    update_file.write(val + "\n")
                print("OK")
            break