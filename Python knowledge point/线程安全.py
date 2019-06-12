# by luffycity.com
import threading

v = []
def func(arg):
    v.append(arg) # 线程安全
    print(v)
for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()