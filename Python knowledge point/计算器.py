# by luffycity.com
# ret = 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# print(ret)

# s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# print(eval(s))

s = '1 - 2 * 12'
# 正则表达式 函数 循环

# 匹配内层不再有括号的子表达式
# 计算
    # 先计算乘除法
    # 再计算加减法
# 一个括号计算完毕
# 将结果和括号进行替换
# 如何处理符号

# 1.先把所有的空格去掉
    # 匹配 内层不再有括号的子表达式
    # 匹配乘除法
    # 匹配加减法
# 2.远离递归,如果要用递归,请考虑返回值的问题

