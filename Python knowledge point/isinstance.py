# by luffycity.com
"""


"""

class Base(object):
    pass

class Foo(Base):
    pass

obj1 = Foo()
print(isinstance(obj1,Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
print(isinstance(obj1,Base)) # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。


obj2 = Base()
print(isinstance(obj2,Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
print(isinstance(obj2,Base)) # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。



# #################### 练习
"""
给你一个参数，判断对象是不是由某一个指定类？ type                  --> type(obj) == Foo
给你一个参数，判断对象是不是由某一个指定类或其父类？ isinstance    --> instance(obj,Foo)
"""







