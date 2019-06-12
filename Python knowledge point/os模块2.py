# by luffycity.com
import os
# 把路径中不符合规范的/改成操作系统默认的格式
# path = os.path.abspath('D:/sylar/s15/day19/4.os模块.py')
# print(path)
# 能够给能找到的相对路径改成绝对路径
# path = os.path.abspath('4.os模块.py')
# print(path)

# 就是把一个路径分成两段,第二段是一个文件/文件夹
# path= os.path.split('D:/sylar/s15/day19/4.os模块.py')
# print(path)
# path= os.path.split('D:/sylar/s15/day19')
# print(path)

# ret1 = os.path.dirname('D:/sylar/s15/day19/4.os模块.py')
# ret2 = os.path.basename('D:/sylar/s15/day19/4.os模块.py')
# print(ret1)
# print(ret2)

# 如果你两个值都需要 os.path.split
# 如果你只要一个值 os.path.dirname/os.path.basename

# 判断文件/文件夹是否存在
# res = os.path.exists(r'D:\sylar\s15\day19\4.os模块.py')
# print(res)

# res1 = os.path.isabs('4.os模块.py')
# res2 = os.path.isabs(r'D:\sylar\s15\day19\4.os模块.py')
# print(res1)
# print(res2)

# print(os.listdir('D:\sylar\s15'))

# print(os.path.isdir(r'D:\sylar\s15\aaa'))
# print(os.path.isfile(r'D:\sylar\s15\aaa'))
# print(os.path.isfile('D:\sylar\s15\day01'))
# print(os.path.isdir('D:\sylar\s15\day01'))

# path = os.path.join('D:\sylar\s15','bbb')
# print(path)

# size= os.path.getsize(r'D:\sylar\s15\day19\4.os模块.py')  # 查看文件大小
# print(size)

# ret1 = os.path.getsize('D:\sylar\s15\day19')
# ret2 = os.path.getsize('D:\sylar\s15\day18')
# ret3 = os.path.getsize('D:\sylar\s15\day17')
# ret4 = os.path.getsize('D:\sylar\s15')
# print(ret1,ret2,ret3,ret4)
# 所有的文件夹 都至少是4096个字节
# 8192
# 64字节 + 32字节/新文件

# 使用python代码统计一个文件夹中所有文件的总大小
# 你需要统计文件夹大小
# D:\sylar\s15\ 文件夹的大小
    # 拿到这个文件夹下所有的文件夹 和 文件
    # 是文件就取大小
    # 是文件夹 再打开这个文件夹 : 文件/文件夹
# 递归
def func(path):    # r'D:\sylar\s15'
    size_sum = 0
    name_lst = os.listdir(path)
    for name in name_lst:
        path_abs = os.path.join(path,name)
        if os.path.isdir(path_abs):
            size = func(path_abs)
            size_sum += size
        else:
            size_sum += os.path.getsize(path_abs)
    return size_sum

ret = func(r'D:\sylar\s15')
print(ret)

# def func(path):  # D:\sylar\s15
#     size_sum = 0 # 0
#     name_lst = os.listdir(path) #  ['day01','day02',...]
#     for name in name_lst:   # 'day01'  'day02'
#         path = os.path.join(path,name)   # 'D:\sylar\s15\day01'
#         if os.path.isdir(path):    # True
#             size = func(path)             # func('D:\sylar\s15\day01')
#             size_sum += size
#         else:
#             size_sum += os.path.getsize(path)
#     return size_sum
#
# def func(path):    # 'D:\sylar\s15\day02'
#     size_sum = 0   # sum = 0
#     name_lst = os.listdir(path)  # [first.py...]
#     for name in name_lst:        # first.py  100
#         path = os.path.join(path,name)
#         if os.path.isdir(path):
#             func(path)
#         else:                    # 文件
#             size_sum += os.path.getsize(path)   # sizesum += 100 = 100+100+100+100 = 500
#     return size_sum   # return 500


# 循环 # 堆栈思想
# 列表 满足一个顺序 先进来的后出去
lst = [r'D:\sylar\s15',]  # 列表的第一个目录就是我要统计的目录
size_sum = 0
while lst:   # [r'D:\sylar\s15',]  lst = ['D:\sylar\s15\day01','D:\sylar\s15\day01'..]
    path = lst.pop()  # path = 'D:\sylar\s15' lst = []
    path_list = os.listdir(path)  # path_list = ['day01',day02',aaa,day15.py]
    for name in path_list:  # name = day01
        abs_path = os.path.join(path,name)
        if os.path.isdir(abs_path):   # 文件夹的逻辑
            lst.append(abs_path)        # lst.append('D:\sylar\s15\day01')  lst = ['D:\sylar\s15\day01']
        else:
            size_sum += os.path.getsize(abs_path)
print(size_sum)










