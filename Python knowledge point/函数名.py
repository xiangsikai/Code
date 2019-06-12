# by luffycity.com

# a = 10
# b = a # 赋值操作
# print(b)

# def func():
#     print("我是一个小小的函数")
# a = func
# print(a)
#
# func()
# a()
#
# func = 3
# print(func)

# 函数名就是一个变量

# a = 10
# b = 20
# c = 30
# lst = [a, b, c]
# print(lst)

# def func1():
#     print("我是1")
# def func2():
#     print("我是2")
# def func3():
#     print("我是3")
#
# lst = [func1, func2, func3]
# for el in lst:
#     el()
# 函数名是变量名

# 函数名可以作为参数传递给函数
# def my():
#     print("我是my")
#
# def proxy(fn): # 代理模式. 装饰器
#     print("在处理之前")
#     fn()
#     print("在处理之后")
#
# proxy(my) # 把函数名作为参数传递给另一个函数


# def func1():
#     print("我是func1")
#
# def func2():
#     print("我是func2")
#
#
# def func(fn, gn): # 函数名可以作为参数进行传递
#     print("我是func")
#     fn()
#     gn()
#     print("哈哈哈")
# func(func1, func2)


# def func():
#     print("我是func")
#     a = 10 # 变量
#     def inner():
#         print("我是inner")
#     return inner
# # ret = func()
# # ret()
# func()() # 先运行func()  然后在返回值上加()

# def chi():
#     print("我要吃")
