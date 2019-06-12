# by luffycity.com
import re
def atom_cal(exp):
    if '*' in exp:
        a,b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a, b = exp.split('/')
        return str(float(a) / float(b))

def format_exp(exp):
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('-+','-')
    exp = exp.replace('++','+')
    return exp

def mul_div(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)
        if ret:
            atom_exp = ret.group()
            res = atom_cal(atom_exp)
            exp = exp.replace(atom_exp,res)
        else:return exp

def add_sub(exp):
    ret = re.findall('[+-]?\d+(?:\.\d+)?', exp)
    exp_sum = 0
    for i in ret:
        exp_sum += float(i)
    return exp_sum

def cal(exp):
    exp = mul_div(exp)
    exp = format_exp(exp)
    exp_sum =  add_sub(exp)
    return exp_sum   # float

def main(exp):
    exp = exp.replace(' ','')
    while True:
        ret = re.search('\([^()]+\)',exp)
        if ret :
            inner_bracket = ret.group()
            res = str(cal(inner_bracket))
            exp = exp.replace(inner_bracket,res)
            exp = format_exp(exp)
        else:break
    return cal(exp)

# s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# ret = main(s)
# print(ret,type(ret))
if __name__ == '__main__':
    s = input('>>>')
    print(main(s))
