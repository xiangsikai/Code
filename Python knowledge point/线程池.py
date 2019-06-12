# by luffycity.com
from concurrent.futures import ThreadPoolExecutor
import time

def task(a1,a2):
    time.sleep(2)
    print(a1,a2)

# 创建了一个线程池（最多5个线程）
pool = ThreadPoolExecutor(5)

for i in range(40):
    # 去线程池中申请一个线程，让线程执行task函数。
    pool.submit(task,i,8)