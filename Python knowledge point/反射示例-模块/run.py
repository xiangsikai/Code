# by luffycity.com
from types import FunctionType
import handler

while True:
    print("""
    系统支持的函数有：
        1. f1
        2. f2
        3. f3
        4. f4
        5. f5
    """)
    val = input("请输入要执行的函数：") # val = "f1"

    # 错误
    # handler.val()
    if hasattr(handler,val):
        func_or_val = getattr(handler,val)     # 根据字符串为参数，去模块中寻找与之同名的成员。
        if isinstance(func_or_val,FunctionType):
            func_or_val()
        else:
            print(func_or_val)
    else:
        print('handler中不存在输入的属性名')

    # 正确方式
    """
    if val == 'f1':
        handler.f1()
    elif val == 'f2':
        handler.f2()
    elif val == 'f3':
        handler.f3()
    elif val == 'f4':
        handler.f4()
    elif val == 'f5':
        handler.f5()
    """