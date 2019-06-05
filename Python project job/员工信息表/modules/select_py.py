#-*- coding:utf-8 -*-
#select name,age from staff_table where age > 22
#select  * from staff_table where dept = "IT"
#select  * from staff_table where enroll_date like "2013"
import os,sys
select_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(select_path)
from core import man


def select_run(cmd):
    """查询sql函数"""
    sql_value = man.sel_value(cmd)
    count = 0

    #打开文件取出员工信息表内容
    with open('%s\\db\\file.txt'%(select_path)) as files:
         for line in files:
            if not line.strip():
                continue
            lines = line.strip()
            sql_dict = man.sql_dict(lines)

            #判断Sql关键值
            select_flag = False
            if sql_value['motion'] == ">":
                select_flag = int(sql_dict[sql_value['fields']]) > int(sql_value['sum'])
            elif sql_value['motion'] == "=":
                select_flag = sql_dict[sql_value['fields']] == sql_value['sum']
            elif sql_value['motion'] == "<":
                select_flag = int(sql_dict[sql_value['fields']]) < int(sql_value['sum'])
            elif sql_value['motion'] == "like":
                select_flag = sql_value['sum'] in sql_dict[sql_value['fields']]

            #如果符合条件就处理
            if select_flag:
                count = count + 1
                if sql_value['keyword'] == "*":
                    print(sql_dict)
                else:
                    keyword = sql_value['keyword'].split(",")
                    temp_dict = dict()
                    for i in keyword:
                        temp_dict[i] = sql_dict[i]
                    print(temp_dict)
         print("匹配行数:%s行"%(count))

