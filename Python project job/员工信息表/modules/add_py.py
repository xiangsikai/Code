#-*- coding:utf-8 -*-
#alter table file.txt add
import os,sys
add_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(add_path)
from core import man

def add_run(cmd):
    """创建新的列"""
    while True:
        add_list = cmd.split()
        flag = True
        if os.path.exists("%s\\db\\%s"%(add_path,add_list[2])):
            add_name = input('name:>>').strip()
            add_age = input('age:>>').strip()
            add_phone = None
            while flag:
                add_phonev2 = input('phone:>>').strip()
                if len(add_phonev2) == 0:
                    print('必须输入:如182-xxxx-xxxx')
                    continue
                else:
                    add_phone = add_phonev2
                    flag = False
            add_dept = input('dept:>>').strip()
            add_enroll_date = input('enroll_date:>>').strip()

            #打开文件进行添加
            add_file = open("%s\\db\\%s"%(add_path,add_list[2]),'r+')
            count = 0
            for line in add_file:
                if not line.strip():
                    continue
                count = count + 1
            count = count + 1
            temp_add = "%s,%s,%s,%s,%s,%s\n"%(count,add_name,add_age,add_phone,add_dept,add_enroll_date)
            add_file.write(temp_add)
            add_file.close()
            print("OK!")
            break
