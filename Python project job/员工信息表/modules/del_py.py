#-*- coding:utf-8 -*-
#删除语法
#DELETE FROM Person WHERE ID = 1
import os,sys
del_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(del_path)
from core import man


def delete_run(cmd):
    """指定ID删除语句"""
    while True:
        del_list = cmd.split()
        del_num = del_list[-1]
        del_value = []

        #读取文件
        with open('%s\\db\\file.txt'%(del_path)) as del_file_r:
            for line in del_file_r:
                if not line.strip():
                    continue
                lines = line.strip()
                del_dict_value = man.sql_dict(lines)
                if int(del_dict_value['id']) == int(del_num):
                    continue
                value = man.sql_dict_value(del_dict_value)
                del_value.append(value)

        #写入文件
        with open('%s\\db\\file.txt'%(del_path),'w+') as del_file_w:
            for lines in del_value:
                del_file_w.write(lines + '\n')
            print("OK!")
        break
