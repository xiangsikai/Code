# by luffycity.com

# 如何使用 from import
# 需要从一个文件中使用哪个名字,就把这个名字导入进来
# from my_module import name

# from import的过程中仍然执行了这个被导入的文件

# from my_module import read1
# import谁就只能用谁
# read1()
# from my_module import read2
# read2()

# 当前文件命名空间和模块的命名空间的问题
# from my_module import read1
# def read1():
#     print('in my read1')
# read1()
#
# from my_module import read2
# read2()

# from import导入的过程中发生了什么事儿?
# 1.找到要被导入的模块
# 2.判断这个模块是否被导入过
# 3.如果这个模块没被导入过
    # 创建一个属于这个模块的命名空间
    # 执行这个文件
    # 找到你要导入的变量
    # 给你要导入的变量创建一个引用,指向要导入的变量
# from my_module import read1
# def read1():
#     print('in my read1')
# read1()
#
# from my_module import read2
# read2()

# 导入多个名字?
# from my_module import read1,read2
# read1()
# read2()

# 给导入的名字起别名
# from my_module import read1 as r1,read2 as r2
# def read1():
#     print('in my read1')
# r1()
# r2()
# read1()

# from my_module import * 在导入的过程中 内存的引用变化
# from my_module import *
# name = 'egon'
# print(name)   # egon
# read1()
# read2()       # alex

# * 和 __all__ __all__能够约束*导入的变量的内容
# from my_module import *
# print(name)
# read1()
# read2()

# from my_module import read1
# read1()



