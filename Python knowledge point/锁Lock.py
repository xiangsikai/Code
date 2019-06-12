# by luffycity.com

import threading
import time

v = []
lock = threading.Lock()

def func(arg):
    lock.acquire()
    v.append(arg)
    time.sleep(0.01)
    m = v[-1]
    print(arg,m)
    lock.release()


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()