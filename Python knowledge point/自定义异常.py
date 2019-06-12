# by luffycity.com


""""""

"""
class MyException(Exception):
    def __init__(self,code,msg):
        self.code = code
        self.msg = msg
try:
    raise MyException(1000,'操作异常')

except MyException as obj:
    print(obj.code,obj.msg)

"""


class MyException(Exception):
    def __init__(self,code,msg):
        self.code = code
        self.msg = msg
try:
    raise MyException(1000,'操作异常')

except KeyError as obj:
    print(obj,1111)
except MyException as obj:
    print(obj,2222)
except Exception as obj:
    print(obj,3333)
