# by luffycity.com

def f1():
    print(11)
    yield
    print(22)
    yield
    print(33)

def f2():
    print(55)
    yield
    print(66)
    yield
    print(77)

v1 = f1()
v2 = f2()

next(v1) # v1.send(None)
next(v2) # v1.send(None)
next(v1) # v1.send(None)
next(v2) # v1.send(None)
next(v1) # v1.send(None)
next(v2) # v1.send(None)