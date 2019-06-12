# by luffycity.com
import multiprocessing
import threading




# ##################### 进程间的数据不共享 #####################
"""
data_list = []

def task(arg):
    data_list.append(arg)
    print(data_list)


def run():
    for i in range(10):
        p = multiprocessing.Process(target=task,args=(i,))
        # p = threading.Thread(target=task,args=(i,))
        p.start()

if __name__ == '__main__':
    run()
"""
# ##################### 进程常用功能 #####################
"""
import time
def task(arg):
    time.sleep(2)
    print(arg)


def run():
    print('111111111')
    p1 = multiprocessing.Process(target=task,args=(1,))
    p1.name = 'pp1'
    p1.start()
    print('222222222')

    p2 = multiprocessing.Process(target=task, args=(2,))
    p2.name = 'pp2'
    p2.start()
    print('333333333')

if __name__ == '__main__':
    run()
"""

# ##################### 通过继承方式创建进程 #####################

class MyProcess(multiprocessing.Process):

    def run(self):
        print('当前进程',multiprocessing.current_process())


def run():
    p1 = MyProcess()
    p1.start()

    p2 = MyProcess()
    p2.start()

if __name__ == '__main__':
    run()