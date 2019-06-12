# by luffycity.com


# # ######################## 线程 ###########################
# import time
# import threading
#
# def task(arg):
#     time.sleep(50)
#
# while True:
#     num = input('>>>')
#     t = threading.Thread(target=task,args=(num,))
#     t.start()

# ######################## 线程池 ###########################
# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def task(arg):
#     time.sleep(50)
#
# pool = ThreadPoolExecutor(20)
# while True:
#     num = input('>>>')
#     pool.submit(task,num)