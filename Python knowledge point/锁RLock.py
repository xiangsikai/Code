# by luffycity.com

import threading
import time

v = []
lock = threading.RLock()
def func(arg):
    lock.acquire()
    lock.acquire()

    v.append(arg)
    time.sleep(0.01)
    m = v[-1]
    print(arg,m)

    lock.release()
    lock.release()


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()