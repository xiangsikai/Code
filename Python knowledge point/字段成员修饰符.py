# by luffycity.com
""""""

# ######################## 公有实例变量(字段) ########################
"""
class Foo:

    def __init__(self,name):
        self.name = name
        self.age = 123

    def func(self):
        print(self.name)


obj = Foo('张凯雄')
print(obj.name)
print(obj.age)
obj.func()
"""


# ######################## 私有实例变量(私有字段) ########################
"""
class Foo:

    def __init__(self,name):
        # 私有实例变量(私有字段)
        self.__name = name
        self.age = 123

    def func(self):
        print(self.__name)

obj = Foo('张凯雄')
print(obj.age)
#obj.__name # 无法访问
obj.func()  # 找一个内部人:func, 让func帮助你执行内部私有 __name
"""

# ######################## 类变量(静态字段) ########################
"""
class Foo:
    country = "中国"

    def __init__(self):
        pass

    def func(self):
        # 内部调用
        print(self.country)
        print(Foo.country) # 推荐


# 外部调用
print(Foo.country)

obj = Foo()
obj.func()
"""

# ######################## 私有类变量(私有静态字段) ########################
"""
class Foo:
    __country = "中国"

    def __init__(self):
        pass

    def func(self):
        # 内部调用
        print(self.__country)
        print(Foo.__country)  # 推荐

# 外部无法调用私有类变量
# print(Foo.country)

obj = Foo()
obj.func()
"""





