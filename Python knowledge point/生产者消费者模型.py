# by luffycity.com
import time
import queue
import threading
q = queue.Queue() # 线程安全

def producer(id):
    """
    生产者
    :return:
    """
    while True:
        time.sleep(2)
        q.put('包子')
        print('厨师%s 生产了一个包子' %id )

for i in range(1,4):
    t = threading.Thread(target=producer,args=(i,))
    t.start()


def consumer(id):
    """
    消费者
    :return:
    """
    while True:
        time.sleep(1)
        v1 = q.get()
        print('顾客 %s 吃了一个包子' % id)

for i in range(1,3):
    t = threading.Thread(target=consumer,args=(i,))
    t.start()