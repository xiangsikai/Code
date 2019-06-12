# by luffycity.com
""""""
# ########################## 私有的实例方法 #######################
"""
class Foo(object):


    def __init__(self):
        pass


    def __display(self,arg):
        print('私有方法',arg)

    def func(self):
        self.__display(123)

obj = Foo()
# obj.__display(123) # 无法访问
obj.func()
"""
# ########################## 私有的静态方法 #######################
"""
class Foo(object):


    def __init__(self):
        pass

    @staticmethod
    def __display(arg):
        print('私有静态 方法',arg)

    def func(self):
        Foo.__display(123)

    @staticmethod
    def get_display():
        Foo.__display(888)

# Foo.__display(123) 报错

obj = Foo()
obj.func()

Foo.get_display()
"""








