# by luffycity.com
import time
import threading
import multiprocessing


lock = multiprocessing.RLock()

def task(arg):
    print('鬼子来了')
    lock.acquire()
    time.sleep(2)
    print(arg)
    lock.release()


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task,args=(1,))
    p1.start()

    p2 = multiprocessing.Process(target=task, args=(2,))
    p2.start()