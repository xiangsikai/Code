# by luffycity.com

# s = 123
# for i in s:
#     print(i)
# print(dir(str)) #  dir查看xx类型的数据可以执行哪些方法, __iter__  iterable
# print(dir(list)) # __iter__
# print(dir(int)) # 没有__iter__
# 所有的带__iter__可以使用for循环的, 可迭代对象

# 可迭代对象可以使用__iter__()来获取到迭代器
# 迭代器里面有__next__()
# s = "石可心喜欢赵一宁"
# it = s.__iter__() # 获取迭代器
# print(dir(it)) # 迭代器里有__iter__ 还有__next__

# 1. 只能向前.
# 2. 几乎不占用内存, 节省内存(需要明天生成器)
# 3. for循环
# 4. 惰性机制 (面试题,难度系数比较高)

# print(it.__next__()) # 石
# print(it.__next__())    # 可
# print(it.__next__())# 心
# print(it.__next__())# 喜
# print(it.__next__())#欢
# print(it.__next__())#赵
# print(it.__next__())# 一
# print(it.__next__())# 宁


# 迭代器模拟for循环
# lst = ["赵一宁", "石可心", "朱奎峰", "姚明","潘长江"]
# # for el in lst: # 底层用的是迭代器
# #     print(el)
#
# it = lst.__iter__() # 获取迭代器
# while 1:
#     try:    # 尝试执行
#         el = it.__next__()  # 获取下一个元素
#         print(el)
#     except StopIteration:   # 处理错误
#         break

# lst = ["赵一宁为什么这么帅","我不信","你们信吗?"]
#
# it = lst.__iter__()

# 偏方
# print("__iter__" in dir(it))
# print("__next__" in dir(it))
# 可以通过dir来判断数据是否是可迭代的, 以及数据是否是迭代器

# 官方方案
# from collections import Iterable  # 可迭代对象
# from collections import Iterator    # 迭代器
#
# print(isinstance(lst, Iterable))
# print(isinstance(lst, Iterator))
#
# print(isinstance(it, Iterable))
# print(isinstance(it, Iterator))
#
lst = ["赵四","花生哥, 越来越皮", "天台见"]
it = lst.__iter__()

# it.__next__()
# it.__next__()
# list(参数)把参数进行循环迭代
s = list(it) # 在list中.一定存在for. 一定__next__()
print(s) # ["赵四","花生哥, 越来越皮", "天台见"]
