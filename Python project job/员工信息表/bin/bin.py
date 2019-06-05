#-*- coding:utf-8 -*-
#查询语句
#select name,age from staff_table where age > 22
#select  * from staff_table where dept = "IT"
#select  * from staff_table where enroll_date like "2013"
#创建新员工记录
#alter table file.txt add
#修改语法
#UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
#删除语法
#DELETE FROM Person WHERE ID = 1



import os,sys
bin_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin_path)
from modules import select_py
from modules import add_py
from modules import update_py
from modules import del_py

while True:
    if __name__ == '__main__':
        cmd = input('>>').strip()
        if cmd.startswith('select'):
            select_py.select_run(cmd)
        elif cmd.startswith('alter'):
            add_py.add_run(cmd)
        elif cmd.startswith('UPDATE'):
            update_py.update_run(cmd)
        elif cmd.startswith('DELETE'):
            del_py.delete_run(cmd)
        elif cmd == 'exit':
            exit()