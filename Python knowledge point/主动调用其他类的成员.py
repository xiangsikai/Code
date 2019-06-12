# by luffycity.com
""""""


"""
class Base(object):
    def f1(self):
        print('5个功能')
        
# obj = Base()
# Base.f1(obj)

obj = Base()
obj.f1()
         
"""


# ########### 方式一
# class Base(object):
#
#     def f1(self):
#         print('5个功能')
#
# class Foo(object):
#
#     def f1(self):
#         print('3个功能')
#         Base.f1(self)
#
# obj = Foo()
# obj.f1()


# ########### 方式二:按照类的继承顺序,找下一个.
"""
class Base(object):
    def f1(self):
        print('5个功能')

class Foo(Base):
    def f1(self):
        super().f1()
        print('3个功能')
        
obj = Foo()
obj.f1()
"""

# ########### 方式二:按照类的继承顺序,找下一个.
class Foo(object):
    def f1(self):
        super().f1()
        print('3个功能')

class Bar(object):
    def f1(self):
        print('6个功能')

class Info(Foo,Bar):
    pass

# obj = Foo()
# obj.f1()

obj = Info()
obj.f1()












