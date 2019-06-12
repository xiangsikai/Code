# by luffycity.com
import threading

print('666')

def func(arg):
    print(arg)


t = threading.Thread(target=func)
t.start()

print('end')



