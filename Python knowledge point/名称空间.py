# by luffycity.com
# a = 10 # 全局名称空间中的内容
#
# def fn(): # fn也在全局名称空间
#     b = 20 # 局部名称空间
#     print(a)
# def gn():
#     print(a)
# fn()
# gn()

# 1. 内置, 2. 全局 , 3. 局部(函数调用)
# a = 110 # 全局
# def fn(): #
#     b = 20 # 局部
#     def gn(): # 局部
#         print(globals())  # 可以查看全局作用域中的内容
#         print(locals())  # 查看当前作用域中的内容
#     gn()
# fn()

# def outer():
#     print("哈哈")
#     def inner_1():
#         print("呵呵")
#         def inner_1_1():
#             print("嘻嘻")
#         inner_1_1()
#         print("吼吼")
#     def inner_2():
#         print("嘿嘿")
#     inner_2()
#     inner_1()
# outer()



