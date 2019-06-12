# by luffycity.com

class Base(object):
    pass

class Foo(Base):
    pass

class Bar(Foo):
    pass

print(issubclass(Bar,Base)) # 检查第一个参数是否是第二个参数的 子子孙孙类



