#-*- coding:utf-8 -*-
import os,sys
man_path = os.path.basename(os.path.basename(os.path.abspath(__name__)))
sys.path.append(man_path)

def sel_value(cmd):
    """取出sql中关键字"""
    select_list = cmd.split()
    select_keyword = select_list[1]
    select_fields = select_list[-3]
    select_motion = select_list[-2]
    select_sum = select_list[-1].strip('"')
    select_value = [select_keyword,select_fields,select_motion,select_sum]
    select_key = ['keyword','fields','motion','sum']
    select_dict = dict(zip(select_key,select_value))
    return select_dict

def sql_dict(cmd):
    """创建文件信息列表字典"""

    #分割文件求出列支
    lines = cmd.strip()
    file_name = cmd.split(',')
    file_key = ['id','name','age', 'phone','dept','enroll_date']

    #创建字典zip()将两个列表组合。
    info_dict = dict(zip(file_key,file_name))
    return info_dict

def sql_dict_value(cmd):
    """将字典转换为文件内的字符"""
    dict_resolve = list(cmd.values())
    dict_value = "%s,%s,%s,%s,%s,%s"%(dict_resolve[0],dict_resolve[1],dict_resolve[2],
                                      dict_resolve[3],dict_resolve[4],dict_resolve[5])
    return dict_value
