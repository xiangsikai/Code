# by luffycity.com
import time
import threading

v = threading.local()

def func(arg):
    # 内部会为当前线程创建一个空间用于存储：phone=自己的值
    v.phone = arg
    time.sleep(2)
    print(v.phone,arg) # 去当前线程自己空间取值

for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()