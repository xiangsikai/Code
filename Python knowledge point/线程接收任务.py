# by luffycity.com
import time
import threading


def task(n):
    print('开始执行任务:',n)
    time.sleep(10)
    print('...')
    print('任务%s 执行完毕:'%n)

while True:
    name = input("请输入任务：")
    t = threading.Thread(target=task,args=(name,))
    t.start()