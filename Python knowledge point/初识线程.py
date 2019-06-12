# by luffycity.com
import time
import threading

def task(a1,a2,a3):
    time.sleep(2)
    print('拿快递')

def play():
    print('和女朋友去耍')


def wm():
    print('去拿外卖')


# 创建一个线程
# 让该线程去执行任务：函数
t1 = threading.Thread(target=task,args=(1,2,3,))
# 去执行吧
t1.start()


# 创建一个线程
# 让该线程去执行任务：函数
t2 = threading.Thread(target=play)
# 去执行吧
t2.start()


# 创建一个线程
# 让该线程去执行任务：函数
t3 = threading.Thread(target=wm)
# 去执行吧
t3.start()

print('玩扇子')
print('煽风点火')
print('耍贱...')