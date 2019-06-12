# by luffycity.com
import time
import threading

DATA_DICT = {}

def func(arg):
    ident = threading.get_ident()
    DATA_DICT[ident] = arg
    time.sleep(1)
    print(DATA_DICT[ident],arg)


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()