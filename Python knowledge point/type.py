# by luffycity.com
"""
 获取当前对象是由那个类创建。

"""

"""
class Foo(object):
    pass

obj = Foo()

print(obj,type(obj)) # 获取当前对象是由那个类创建。
if type(obj) == Foo:
    print('obj是Foo类型')
"""

# #### 练习题
"""
class Foo(object):
    pass

class Bar(object):
    pass

def func(*args):
    foo_counter =0
    bar_counter =0
    for item in args:
        if type(item) == Foo:
            foo_counter += 1
        elif type(item) == Bar:
            bar_counter += 1
    return foo_counter,bar_counter

# result = func(Foo(),Bar(),Foo())
# print(result)

v1,v2 = func(Foo(),Bar(),Foo())
print(v1,v2)
"""