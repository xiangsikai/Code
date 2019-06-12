# by luffycity.com
import threading


# ###################### 1.线程的基本使用 #################
# def func(arg):
#     print(arg)
#
#
# t = threading.Thread(target=func,args=(11,))
# t.start()
#
#
# print(123)
# ###################### 2.主线程默认等子线程执行完毕 #################
# import time
# def func(arg):
#     time.sleep(arg)
#     print(arg)
#
#
# t1 = threading.Thread(target=func,args=(3,))
# t1.start()
#
# t2 = threading.Thread(target=func,args=(9,))
# t2.start()
#
# print(123)
# ###################### 3.主线程不再等，主线程终止则所有子线程终止 #################
# import time
# def func(arg):
#     time.sleep(2)
#     print(arg)
#
# t1 = threading.Thread(target=func,args=(3,))
# t1.setDaemon(True)
# t1.start()
#
# t2 = threading.Thread(target=func,args=(9,))
# t2.setDaemon(True)
# t2.start()
#
# print(123)

# ###################### 4.开发者可以控制主线程等待子线程（最多等待时间） #################
# import time
# def func(arg):
#     time.sleep(0.01)
#     print(arg)
#
# print('创建子线程t1')
# t1 = threading.Thread(target=func,args=(3,))
# t1.start()
# # 无参数，让主线程在这里等着，等到子线程t1执行完毕，才可以继续往下走。
# # 有参数，让主线程在这里最多等待n秒，无论是否执行完毕，会继续往下走。
# t1.join(2)
#
# print('创建子线程t2')
# t2 = threading.Thread(target=func,args=(9,))
# t2.start()
# t2.join(2) # 让主线程在这里等着，等到子线程t2执行完毕，才可以继续往下走。
#
# print(123)

# ###################### 4.线程名称 #################
# def func(arg):
#     # 获取当前执行该函数的线程的对象
#     t = threading.current_thread()
#     # 根据当前线程对象获取当前线程名称
#     name = t.getName()
#     print(name,arg)
#
# t1 = threading.Thread(target=func,args=(11,))
# t1.setName('侯明魏')
# t1.start()
#
# t2 = threading.Thread(target=func,args=(22,))
# t2.setName('刘宁钱')
# t2.start()
#
# print(123)

# ###################### 5.线程本质 #################
# 先打印：11？123？
# def func(arg):
#     print(arg)
#
# t1 = threading.Thread(target=func,args=(11,))
# t1.start()
# # start 是开始运行线程吗？不是
# # start 告诉cpu，我已经准备就绪，你可以调度我了。
# print(123)


# ###################### 6.补充：面向对象版本的多线程 #################
# 多线程方式：1 (常见)
# def func(arg):
#     print(arg)
#
# t1 = threading.Thread(target=func,args=(11,))
# t1.start()

# 多线程方式：2
# class MyThread(threading.Thread):
#
#     def run(self):
#         print(11111,self._args,self._kwargs)
#
# t1 = MyThread(args=(11,))
# t1.start()
#
# t2 = MyThread(args=(22,))
# t2.start()

print('end')