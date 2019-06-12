# by luffycity.com

import os # os是和操作系统交互的模块

# os.makedirs('dir1/dir2')
# os.mkdir('dir3')
# os.mkdir('dir3/dir4')

# 只能删空文件夹
# os.rmdir('dir3/dir4')
# os.removedirs('dir3/dir4')
# os.removedirs('dir1/dir2')

# print(os.stat(r'D:\sylar\s15\day18\6.os模块.py'))

# exec/eval执行的是字符串数据类型的 python代码
# os.system和 os.popen是执行字符串数据类型的 命令行代码

# os.'system('dir')  # 执行操作系统的命令,没有返回值,实际的操作/删除一个文件 创建一个文件夹 exec
# 程序要处理这些路径
# ret = os.popen('dir) # 是和做查看类的操作
# s =ret.read()
# print(s)
# print(s.split('\n'))

# os.listdir / os.path.join
# file_lst = os.listdir('D:\sylar\s15')
# for path in file_lst:
#     print(os.path.join('D:\sylar\s15',path))

# print('-->',os.getcwd())  # current work dir 当前工作目录
# # 并不是指当前文件所在的目录
# # 当前文件是在哪个目录下执行的
# ret = os.popen('dir') # 是和做查看类的操作
# s =ret.read()
# print(s)

# os.chdir('D:\sylar\s15\day18')  # 切换当前的工作目录
# ret = os.popen('dir') # 是和做查看类的操作
# s =ret.read()
# print(s)


# 验证码
# 发红包
# 计算时间差 - 函数
# sys.argv 登录验证
# os模块:
    # 用户登录 ,登录之后 给这个用户创建一个属于他的文件夹 已用户名命名
    # 如果用户注销,删除这个文件夹