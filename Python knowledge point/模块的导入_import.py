# by luffycity.com

# 什么是模块 ? 已经写好的一组功能的集合
# 别人写好的函数 变量 方法 放在一个文件里 (这个文件可以被我们直接使用)这个文件就是个模块
# py dll文件 zip文件

# 如何自己写一个模块
# 创建一个py文件,给它起一个 符合变量名命名规则的名字,这个名字就是模块名

# import my_module   # pycharm认为你的模块导入不进来
# 在导入模块的过程中发生了什么?
# 导入一个模块就是执行一个模块

# 怎么使用my_module模块中的名字
# print(my_module.name)
# print(my_module.read1)
# my_module.read1()

# import的命名空间,模块和当前文件在不同的命名空间中
# name = 'egon'
# def read1():
#     print('main read1')
#
# print(name)
# print(my_module.name)

# 模块是否可以被重复导入
# import my_module
# import my_module
# 怎么判断这个模块已经被导入过了???
# import sys
# print(sys.modules)

# 模块导入的过程中发生了什么?
    # 找到这个模块
    # 判断这个模块是否被导入过了
    # 如果没有被导入过
        # 创建一个属于这个模块的命名空间
        # 让模块的名字 指向 这个空间
        # 执行这个模块中的代码

# name = 'egon'
# def read1():
#     print('main read1')
#
#
# print(name)
# print(my_module.name)
# my_module.read2()

# 给模块起别名,起了别名之后,使用这个模块就都使用别名引用变量了
# import my_module as m
# m.read1()

# json pickle
# dumps loads
# def func(dic,t = 'json'):
#     if t == 'json':
#         import json
#         return json.dumps(dic)
#     elif t == 'pickle':
#         import pickle
#         return pickle.dumps(dic)
#
# def func(dic, t='json'):
#     if t == 'json':
#         import json as aaa
#     elif t == 'pickle':
#         import pickle as aaa
#     return aaa.dumps(dic)

# 导入多个模块
# import os,time
# import os as o,time as t
# 规范建议 模块应该一个一个的导入 : 自定义模块,第三方模块,内置模块
# 内置模块
# 扩展(第三方)模块
# 自定义模块

# import os
#
# import django
#
# import my_module
