# by luffycity.com

# 普通的正常的函数
# def func(n):
#     return n * n
#
# # ret = func(9)
# # print(ret)
# #
# # # 匿名函数, 语法: lambda 参数: 返回值
# a = lambda n : n * n
# # ret = a(9)
# # print(ret)
# b = lambda x: x+1

# print(a(5)) # 函数的名字可以认为是a
#
# print(func.__name__) # 查看函数的名字
# print(a.__name__) # __name__的值都是<lambda>
# print(b.__name__)

# def func(a, b):
#     return a + b
#
# x = lambda a, b: a+b
#
# print(x(1,2))


# def func(x, y):
#     return x, y
#
# print(func(1,2))
# #           1,     2

# suiyi = lambda x, y : 1, 2   # 笔试题
# print(suiyi)
# print(suiyi(250,38))

# lambda 参数: 返回值

# 匿名函数, 给函数传递2给参数. 返回最大值
# fn = lambda *args: max(args) # 单行函数
#
# print(fn(1,2,5,2,3,4,156,3,2,2,4,5,56,34,34,34,34,88))
