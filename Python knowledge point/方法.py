# by luffycity.com

# ############### 没必要写实例方法 ##############
class Foo(object):

    def __init__(self,name):
        self.name = name

    def func(self):
        print('123')


obj = Foo('史雷')
obj.func()
# ############### 有必要写实例方法 ##############
"""
class Foo(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)


obj = Foo('史雷')
obj.func()
"""
# ############### 静态方法 ##############
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     # 实例方法
#     def func(self):
#         print(self.name)
#
#     # 静态方法,如果方法无需使用对象中封装的值,那么就可以使用静态方法
#     @staticmethod
#     def display(a1,a2):
#         return a1 + a2
#
# obj = Foo('史雷')
# obj.func()
#
# ret = Foo.display(1,3)
# print(ret)

# 总结
#   1. 编写时:
#        - 方法上方写 @staticmethod
#        - 方法参数可有可无
#   2. 调用时:
#       - 类.方法名()  *
#       - 对象.方法名()
#   3. 什么时写静态方法?
#       - 无需调用对象中已封装的值.


# ############### 类方法 ##############

class Foo(object):
    def __init__(self, name):
        self.name = name

    # 实例方法,self是对象
    def func(self):
        print(self.name)

    # 静态方法,如果方法无需使用对象中封装的值,那么就可以使用静态方法
    @staticmethod
    def display(a1,a2):
        return a1 + a2

    # 类方法,cls是类
    @classmethod
    def show(cls,x1,x2):
        print(cls,x1,x2)

# 执行类方法
Foo.show(1,8)

# 总结
#   1. 定义时:
#        - 方法上方写: @classmethod
#        - 方法的参数: 至少有一个cls参数
#   2. 执行时:
#        - 类名.方法名()  # 默认会将当前类传到参数中.
#   3. 什么时用?
#        - 如果在方法中会使用到当前类,那么就可以使用类方法.





























