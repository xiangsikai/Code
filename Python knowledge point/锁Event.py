# by luffycity.com
import time
import threading

lock = threading.Event()


def func(arg):
    print('线程来了')
    lock.wait() # 加锁：红灯
    print(arg)


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()

input(">>>>")
lock.set() # 绿灯


lock.clear() # 再次变红灯

for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()

input(">>>>")
lock.set()





















