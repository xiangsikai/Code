# by luffycity.com

# #### 讲解 & 练习题
from types import MethodType,FunctionType
def check(arg):
    """
    检查arg是方法还是函数？
    :param arg:
    :return:
    """
    if isinstance(arg,MethodType):
        print('arg是一个方法')
    elif isinstance(arg,FunctionType):
        print('arg是一个函数')
    else:
        print('不知道是什么')
#
# def func():
#     pass
#
# class Foo(object):
#     def detail(self):
#         pass
#     @staticmethod
#     def xxx():
#         pass
#
#
# check(func)
#
# obj = Foo()
# check(obj.detail)
# check(obj.xxx)

# #### 特点
"""
class Foo(object):

    def f1(self):
        pass

    def f2(self):
        pass

    def f3(self):
        pass

# obj = Foo()
# print(obj.f1)
# print(obj.f2)

obj = Foo()
Foo.f1(obj) # 把f1当做函数

obj = Foo()
obj.f1()    # 把f1当做方法，自动传self值
"""

# 练习1
"""
class Foo(object):

    def f1(self):
        pass

    def f2(self):
        pass

    def f3(self):
        pass

    list_display = [f1,f2]

    def __init__(self):
        pass


for item in Foo.list_display:
    item(123)
"""
# 练习2
# class Foo(object):
#
#     def f1(self):
#         pass
#
#     def f2(self):
#         pass
#
#     def f3(self):
#         pass
#
#     list_display = [f1,f2]
#
# obj = Foo()
# Foo.list_display.append(obj.f3)
#
# for item in Foo.list_display:
#     print(item)































