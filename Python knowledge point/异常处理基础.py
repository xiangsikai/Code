# by luffycity.com
# 什么是异常
# IndexError [][1]
# KeyError {}['key']
# pickle.load() EOFError
# FileNotFoundError open('aa')
# ModuleNotFoundError import aaaaaaaaaaa
# ValueError int('sdjkhf')

# 语法错误 应该在写代码的时候就规避掉
# SyntaxError
# NameError name

# 什么时候最容易出异常
# 当你要处理的内容不确定的时候
    # 有用户参与
    # 有外界数据接入 : 从文件中读 从网络上获取


# 当有多行报错的时候是为什么?
# def func1():
#     name
#
# def func2():
#     func1()
#
# def main():
#     func2()
#
# main()
# 在嵌套调用的过程中,内部的代码出了问题,外部所有的调用的地方都成为报错追溯信息的一部分

# 怎么解决
# 从下往上找 首先找到你写的代码 出错的那一行
# 看看能不能看出问题
# 就把报错的最后一行 错误类型和详细提示贴到百度里,结合报错的那一行解决问题

# 单分支
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
#
# try:
#     num = int(input('num >>>'))
#     print(l[num - 1])
# except ValueError :      # except处理的异常必须和实际报错的异常是相同的
#     print('请输入一个数字')
# print(l[num - 1])

# 多分支
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
#
# try:
#     num = int(input('num >>>'))
#     print(l[num - 1])
# except ValueError :
#     # 从上向下报错的代码只要找到一个和报错类型相符的分支就执行这个分支中的代码,然后直接退出分支
#     print('请输入一个数字')
# except IndexError :
#     # 如果找不到能处理和报错类型相同的分支,会一直往下走,最后还是没有找到就会报错
#     print('只能输入1或2')

# 多分支合并
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
#
# try:
#     num = int(input('num >>>'))
#     print(l[num - 1])
# except (ValueError,IndexError) :
#     print('您输入的内容不合法')


# 万能异常
# def buy():
#     print('buy')
#     name
#
# def back():
#     print('back')
#     [][1]
#
# def show():
#     print('show')
#     1/0
#
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         num = int(input('num >>>'))
#         print(l[num - 1])
#         try:
#             func = l[num - 1][1]
#             func()
#         except Exception:
#             print('用户在选择了%s操作之后发生了不可知的异常' % l[num - 1][0])
#
# main()


# as语法  能够将具体错误信息打印出来
# def buy():
#     print('buy')
#     name
#
# def back():
#     print('back')
#     [][1]
#
# def show():
#     print('show')
#     1/0
#
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         num = int(input('num >>>'))
#         print(l[num - 1])
#         try:
#             func = l[num - 1][1]
#             func()
#         except Exception as e:
#             print(e)
#             #print(e.args,e.__traceback__.tb_lineno,e.__traceback__.tb_frame)
#             print('用户在选择了%s操作之后发生了不可知的异常' % l[num - 1][0])
#
# main()

# 万能异常,相当于except Exception
# try:
#     name
#     [][1]
#     int('aaa')
# except:
#     print(123)

# 多分支 + 万能异常 : 万能异常应该永远放在异常处理的最下面
# def buy():
#     print('buy')
#     name
#
# def back():
#     print('back')
#     [][1]
#
# def show():
#     print('show')
#     1/0
#
# def main():
#     l = [('购物',buy),('退货',back),('查看订单',show)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         try:
#             num = int(input('num >>>'))
#             print(l[num - 1])
#             func = l[num - 1][1]
#             func()
#         except (ValueError,IndexError) :
#             print('您输入的内容不合法')
#         except Exception as e:
#             print(e)
#             #print(e.args,e.__traceback__.tb_lineno,e.__traceback__.tb_frame)
#             print('用户在选择了%s操作之后发生了不可知的异常' % l[num - 1][0])
# main()

# try:
#     pass
# except (ValueError,IndexError):
#     print('针对性的处理')
# except Exception as e:
#     print(e)
#     print('通用性的处理')