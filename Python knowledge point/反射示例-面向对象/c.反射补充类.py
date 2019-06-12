# by luffycity.com
"""
getattr # 根据字符串的形式，去对象中找成员。
hasattr # 根据字符串的形式，去判断对象中是否有成员。
setattr # 根据字符串的形式，去判断对象动态的设置一个成员（内存）
delattr # 根据字符串的形式，去判断对象动态的设置一个成员（内存）
"""

class Foo(object):

    def __init__(self,a1):
        self.a1 = a1
        self.a2 = None

obj = Foo(1)


v1 = getattr(obj,'a1')
print(v1)

setattr(obj,'a2',2)


v2 = getattr(obj,'a2')
print(v2)