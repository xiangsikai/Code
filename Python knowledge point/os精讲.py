# by luffycity.com
# os.system("bash command")  运行shell命令，直接显示
# os.popen("bash command).read()  运行shell命令，获取执行结果
# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
import os
# 统计文件的大小
# os.path.getsize('路径') # python的命令
# dir 路径 \C   # 操作系统的命令

# 帮助你显示当前路径下的所有文件和文件夹
# os.system('dir 路径')  # 使用python语言直接执行操作系统的命令
# os.listdir('路径')     # 使用python语言的os模块提供的方法 间接调用了操作系统命令

# 程序员 python开发的
# 和python代码打交道

# 学习python的人
    # web开发
    # 运维开发  : 运维功底  熟悉操作系统命令

# exec('字符串数据类型的python代码')
# eval('执行字符串数据类型的python代码')

# os.system('执行字符串数据类型的操作系统命令')
# os.popen('执行字符串数据类型的操作系统命令,并返回结果')

# 两周时间 - linux操作系统

# getcwd  # 获取当前执行命令的时候所在的目录
# chdir   # 修改当前执行命令的时候所在的目录

# ret = os.listdir('D:\sylar\s15')
# print(ret)

# os.chdir('D:\sylar\s15')
# print(os.popen('dir').read())

# os模块所做的事情
    # 定制了很多方法 间接的帮助你去调用操作系统的命令 获得结果
    # 然后帮助你分析整理成我们需要的数据类型的形态
# 你也可以os.popen/os.system直接取调用操作系统的命令 获得结果
    # 但是 分析和整理的工作需要你自己做
# 用os模块的方法本身能够完成的功能我们就用定制好的方法就够了
# 如果有一天 你发现os模块定制好的功能解决不了我们的问题了
    # 而刚好操作系统的命令能够很好地帮助我们解决问题
    # 这个时候就用os.popen/os.system
