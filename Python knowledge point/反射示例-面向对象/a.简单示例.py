# by luffycity.com


class Foo(object):

    country = "中国"

    def func(self):
        pass


# v = getattr(Foo,'func') # Foo.func # 根据字符串为参数，去类中寻找与之同名的成员。
# print(v)

# obj = Foo()
# v = getattr(obj,"func") # obj.func # 根据字符串为参数，去对象中寻找与之同名的成员。
# print(v)