#-*- coding:utf-8 -*-
import re
sum_count = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

def multiply_divide_acc(data):
    """判断是否停止计算乘除"""
    global flag_multiply_divide
    if '/' in data or '*' in data:
        flag_multiply_divide = True
    else:
        flag_multiply_divide = False

def multiply_divide(num):
    """计算乘除"""
    global flag_multiply_divide
    flag_multiply_divide = True
    while  True:
        if "*" in num or "/" in num:
            multiply_divide_num = re.search('\d+[\.]?\d*[\*\/]{1}[\-\+]?\d+[\.]?\d*',num).group()
            if re.split('[\-\+]?\d+[\.]?\d*',multiply_divide_num)[1] == '*':
                v1,v2 = multiply_divide_num.split('*')
                value = float(v1) * float(v2)
                va1,va2 = re.split('\d+[\.]?\d*[\*\/][\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                multiply_divide_acc(num)
                if not flag_multiply_divide:
                    return num
            elif re.split('[\-\+]?\d+[\.]?\d*',multiply_divide_num)[1] == '/':
                v1,v2 = multiply_divide_num.split('/')
                value = float(v1) / float(v2)
                va1,va2 = re.split('\d+[\.]?\d*[\*\/][\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                multiply_divide_acc(num)
                if not flag_multiply_divide:
                    return num
            else:
                break
        else:
            break

def add_update(data):
    """将多个正负号修改为单个加减符号"""
    num_update = re.split('\d+[\.]{0,1}\d*',data)
    if (int(data.count('-')) * 3 + int(data.count('+')) * 2) % 2 == 0:
        data_acc_a = data.replace(num_update[1],'+',2)
        return data_acc_a
    else:
        data_acc_a = data.replace(num_update[1],'-',2)
        return data_acc_a

def add_acc(data):
    """判断是否停止计算加减"""
    global flag_add
    add_acc = re.search('\d+[\.]?\d*[\+\-]*',data).group()
    if add_acc.endswith('+') or add_acc.endswith('-'):
        flag_add = True
    else:
        flag_add = False

def add_and_subtract(num):
    """计算加减法"""
    global flag_add
    flag_add = True
    while flag_add:
        num_add_and_subtract = re.search('\-?\d+[\.]?\d*[\-\+]*\d+[\.]?\d*',num).group()
        if '*' in num_add_and_subtract or '/' in num_add_and_subtract:
            break
        num_add_and_subtract = add_update(num_add_and_subtract)
        if '+' in re.split('\d+[\.]?\d*',num_add_and_subtract):
            if int(num_add_and_subtract.count('+')) == 1:
                v1,v2 = num_add_and_subtract.split('+')
                value = float(v1) + float(v2)
                va1,va2 = re.split('\-?\d+[\.]?\d*[\-\+]?[\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                add_acc(num)
                if not flag_add:
                    return num
            else:
                v1 = re.sub('[\+]?','',num_add_and_subtract,1)
                v2,v3 = v1.split('+')
                v4 = '-%s'%(v2)
                value = float(v4) - float(v3)
                va1,va2 = re.split('\-?\d+[\.]?\d*[\-\+]?[\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                add_acc(num)
                if not flag_add:
                    return num
        elif '-' in re.split('\d+[\.]?\d*',num_add_and_subtract):
            if int(num_add_and_subtract.count('-')) == 1:
                v1,v2 = num_add_and_subtract.split('-')
                value = float(v1) - float(v2)
                va1,va2 = re.split('\-?\d+[\.]?\d*[\-\+]?[\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                add_acc(num)
                if not flag_add:
                    return num
            else:
                v1 = re.sub('[\-]?','',num_add_and_subtract,1)
                v2,v3 = v1.split('-')
                v4 = '-%s'%(v2)
                value = float(v4) + float(v3)
                va1,va2 = re.split('\-?\d+[\.]?\d*[\-\+]?[\-\+]?\d+[\.]?\d*',num,1)
                num_new = '%s%s%s'%(va1,value,va2)
                num = num_new
                add_acc(num)
                if not flag_add:
                    return num
        else:
            break

def parenthesis_acc(num):
    """判断是否得出总结果，停止函数计算"""
    global flag_par
    par_acc = re.search('[\-\+]?\d+[\.]?\d*[\-\+\*\/]?',num).group()
    if par_acc.endswith('+') or par_acc.endswith('-') or par_acc.endswith('/') or par_acc.endswith('*'):
        flag_par = True
    else:
        flag_par = False

def parenthesis(num):
    """匹配括号并计算"""
    global flag_par
    while True:
        global num_par
        if '(' in list(num):
            num_parenthesis = re.search('\([^()]+\)',num).group()
            va1,va2 = re.split('\([^()]+\)',num,1)
            num_par = re.sub('(\(|\))',"",num_parenthesis)
            num_mul = multiply_divide(num_par)
            if not num_mul == None:
                num_par = num_mul
            num_add = add_and_subtract(num_par)
            if not num_add == None:
                num_par = num_add
            new = '%s%s%s'%(va1,num_par,va2)
            num = new
        else:
            num_mul = multiply_divide(num)
            if not num_mul == None:
                num = num_mul
            num_add = add_and_subtract(num)
            if not num_add == None:
                num = num_add
            parenthesis_acc(num)
            if not flag_par:
                return num

def run():
    """调用程序"""
    run_flag = True
    while run_flag:
        print("\n-------计算器-------")
        print('输入a：↓\n'
              '计算：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))')
        run_num = input('q退出>>>：').strip()
        if run_num == 'q':
            run_flag = False
        elif run_num == 'a':
            num_new = parenthesis(sum_count)
            print("eval计算结果：%s"%(eval(sum_count)))
            print('计算器运算结果：%s'%(num_new))
            run_flag = False
        else:
            num_new = parenthesis(run_num)
            print("eval计算结果：%s"%(eval(run_num)))
            print('计算器运算结果：%s'%(num_new))

run()