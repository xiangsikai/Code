# by luffycity.com
from abc import ABCMeta,abstractmethod


class Base(metaclass=ABCMeta): # 抽象类

    def f1(self):
        print(123)


    @abstractmethod
    def f2(self):   # 抽象方法
        pass

class Foo(Base):

    def f2(self):
        print(666)


obj = Foo()
obj.f1()