# by luffycity.com
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def task(arg):
    time.sleep(2)
    print(arg)

if __name__ == '__main__':

    pool = ProcessPoolExecutor(5)
    for i in range(10):
        pool.submit(task,i)


