# by luffycity.com
"""
对文件描述的注释

"""

"""
class Foo(object):

    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    
    def __call__(self, *args, **kwargs):
        print(11111,args,kwargs)
        return 123

    def __getitem__(self, item):
        print(item)
        return 8

    def __setitem__(self, key, value):
        print(key,value,111111111)

    def __delitem__(self, key):
        print(key)

    def __add__(self, other):
        return self.a1 + other.a2

    def __enter__(self):
        print('1111')
        return 999

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('22222')
"""
# 1. 类名() 自动执行 __init__
# obj = Foo(1,2)

# 2. 对象() 自动执行 __call__
# ret = obj(6,4,2,k1=456)

# 3. 对象['xx']  自动执行 __getitem__
# ret = obj['yu']
# print(ret)

# 4. 对象['xx'] = 11  自动执行 __setitem__
# obj['k1'] = 123

# 5. del 对象[xx]     自动执行 __delitem__
# del obj['uuu']

# 6. 对象+对象         自动执行 __add__
# obj1 = Foo(1,2)
# obj2 = Foo(88,99)
# ret = obj2 + obj1
# print(ret)

# 7. with 对象        自动执行 __enter__ / __exit__
# obj = Foo(1,2)
# with obj as f:
#     print(f)
#     print('内部代码')

# 8. 真正的构造方法
# class Foo(object):
#     def __init__(self, a1, a2):     # 初始化方法
#         """
#         为空对象进行数据初始化
#         :param a1:
#         :param a2:
#         """
#         self.a1 = a1
#         self.a2 = a2
#
#     def __new__(cls, *args, **kwargs): # 构造方法
#         """
#         创建一个空对象
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         return object.__new__(cls) # Python内部创建一个当前类的对象(初创时内部是空的.).
#
# obj1 = Foo(1,2)
# print(obj1)
#
# obj2 = Foo(11,12)
# print(obj2)











