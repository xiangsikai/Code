# by luffycity.com
import time
import threading

lock = threading.Condition()

# ############## 方式一 ##############

def func(arg):
    print('线程进来了')
    lock.acquire()
    lock.wait() # 加锁

    print(arg)
    time.sleep(1)

    lock.release()


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()

while True:
    inp = int(input('>>>'))

    lock.acquire()
    lock.notify(inp)
    lock.release()


# ############## 方式二 ##############
"""
def xxxx():
    print('来执行函数了')
    input(">>>")
    # ct = threading.current_thread() # 获取当前线程
    # ct.getName()
    return True

def func(arg):
    print('线程进来了')
    lock.wait_for(xxxx)
    print(arg)
    time.sleep(1)

for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()

"""






















