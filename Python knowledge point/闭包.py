# by luffycity.com
# 闭包. 在内层函数中访问外层函数的变量
# 闭包的作用:
#     1. 可以保护你的变量不收侵害
#     2. 可以让一个变量常驻内存
#  查看函数是否是闭包
# a = 10 # 不安全的
#
# def outer():
#     global a
#     a = 20
#
#
# def outer_2():
#     global a
#     a = 30
#
# outer_2()
# outer()
#
# print(a)

# def outer():
#     a = 10 # 常驻内存,  为了inner执行的时候有值.
#     def inner():
#         print(a)    #
#
#     return inner
#
# fn = outer()
# print("fdsafasd")
# print("fdsafasd")
# print("fdsafasd")
#
# fn() # 调用的时机是不定的.

# 超简易爬虫
# from urllib.request import urlopen
#
# def outer():
#     # 常驻内存
#     s = urlopen("http://www.xiaohua100.cn/index.html").read()
#     def getContent(): # 闭包
#         return s
#     return getContent
#
#
# print("爬取内容.....")
# pa = outer()
#
# ret = pa()
# print(ret)
#
# ret = pa()
# print(ret)
#
# ret = pa()
# print(ret)
#
# ret = pa()
# print(ret)

# def func():
#     a = 10
#     def inner():
#         print(a)
#     print(inner.__closure__) # 如n果的是Noe. 不是闭包. 如果不是None, 就是闭包打印
#
# func()

