# by luffycity.com
"""
面向对象补充
"""

"""
class Foo(object):
    def __init__(self):
        self.info = {}

    def __setitem__(self, key, value):
        self.info[key] = value

    def __getitem__(self, item):
        return self.info.get(item)


obj = Foo()
obj['x'] = 123
print(obj['x'])
"""
from flask import globals
# class Foo(object):
#
#     def __init__(self):
#         object.__setattr__(self, 'info', {}) # 在对象中设置值的本质
#
#     def __setattr__(self, key, value):
#         self.info[key] = value
#
#     def __getattr__(self, item):
#         print(item)
#         return self.info[item]
#
# obj = Foo()
# obj.name = 'alex'
# print(obj.name)
v = []
for i in range(10000):
    v.append(i)

print(v)
