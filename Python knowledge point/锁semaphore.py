# by luffycity.com
import time
import threading

lock = threading.BoundedSemaphore(3)
def func(arg):
    lock.acquire()
    print(arg)
    time.sleep(1)
    lock.release()


for i in range(20):
    t =threading.Thread(target=func,args=(i,))
    t.start()