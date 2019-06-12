# by luffycity.com
"""
以后：Flask框架内部看到源码 上下文管理

"""

import time
import threading
INFO = {}
class Local(object):

    def __getattr__(self, item):
        ident = threading.get_ident()
        return INFO[ident][item]

    def __setattr__(self, key, value):
        ident = threading.get_ident()
        if ident in INFO:
            INFO[ident][key] = value
        else:
            INFO[ident] = {key:value}

obj = Local()

def func(arg):
    obj.phone = arg # 调用对象的 __setattr__方法（“phone”,1）
    time.sleep(2)
    print(obj.phone,arg)


for i in range(10):
    t =threading.Thread(target=func,args=(i,))
    t.start()

