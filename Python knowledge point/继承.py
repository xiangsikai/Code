# by luffycity.com
""""""


# ########################1. 基本使用 ###########################

# ##### 基本写法
"""
class SuperBase:
    def f3(self):
        print('f3')

class Base(SuperBase):  # 父类,基类
    def f2(self):
        print('f2')

class Foo(Base):        # 子类,派生类

    def f1(self):
        print('f1')

obj = Foo()
obj.f1()
obj.f2()
obj.f3()
# 原则:现在自己类中找,么有就去父类
"""

# ##### 为何有继承? 为了提高代码重用性
"""
class Base:
    def f1(self):
        pass

class Foo(Base):

    def f2(self):
        pass

class Bar(Base):

    def f3(self):
        pass
"""

# ########################2. 多继承 ###########################
"""
class Base1:
    def show(self):
        print('Base1.show')

class Base2:
    def show(self):
        print('Base2.show')

class Foo(Base1,Base2):
    pass

obj = Foo()
obj.show()
"""
# 左边更亲

# ############################### 练习题 #############################
###### 习题1

# class Base:
#     def f1(self):
#         print('base.f1')
#
# class Foo(Base):
#     def f2(self):
#         print('foo.f2')


# 1. 是否执行
# obj = Foo()
# obj.f2()
# obj.f1()

# 2. 是否执行
# obj = Base()
# obj.f1()
# obj.f2() # 错

##### 习题2:
"""
class Base:
    def f1(self):
        print('base.f1')

class Foo(Base):
    def f3(self):
        print('foo.f3')
    
    def f2(self):
        print('foo.f2')
        self.f3() # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
        
obj = Foo()
obj.f2() # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
"""

##### 习题3:
"""
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        print('foo.f3')

class Foo(Base):

    def f2(self):
        print('foo.f2')
        self.f3()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.


obj = Foo()
obj.f2()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
"""
##### 习题4:
"""
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1() # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
        print('foo.f3')

class Foo(Base):

    def f2(self):
        print('foo.f2')
        self.f3()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.


obj = Foo()
obj.f2()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
"""
##### 习题5:
"""
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1() # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
        print('base.f3')

class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.


obj = Foo()
obj.f2()  # obj是那一个类(Foo),那么执行方法时,就从该类开始找.
# foo.f2
# foo.f1
# base.f3

obj2 = Base()
obj2.f3()
# base.f1
# base.f3
"""
# 总结: self是那个类的对象,那么就从该类开始找(自己没有就找父类)

##### 习题6:

class Base1:
    def f1(self):
        print('base1.1')
    def f2(self):
        print('base1.f2')

class Base2:
    def f1(self):
        print('base2.f1')

    def f2(self):
        print('base2.f2')

    def f3(self):
        print('base2.f3')
        self.f1()

class Foo(Base1,Base2):

    def f0(self):
        print('foo.f0')
        self.f3()
# 1. 多继承先找左边
# 2. self到底是谁,self是那个类的对象,那么就从该类开始找(自己没有就找父类)
obj = Foo()
obj.f0()




























