# by luffycity.com
# 执行一个py文件的方式:
    # 在cmd执行,在python执行 : 直接执行这个文件 - 以脚本的形式运行这个文件
    # 导入这个文件

# 都是py文件
    # 直接运行这个文件 这个文件就是一个脚本
    # 导入这个文件     这个文件就是一个模块

# import re
# import time
#
# import my_module
# import calculate
#
# ret = calculate.main('1*2+3')
# print(ret)

# 当一个py文件
    # 当做一个脚本的时候 : 能够独立的提供一个功能,能自主完成交互
    # 当成一个模块的时候 : 能够被导入这调用这个功能,不能自主交互

# 一个文件中的__name__变量
    # 当这个文件被当做脚本执行的时候 __name__ == '__main__'
    # 当这个文件被当做模块导入的时候 __name__ == '模块的名字'

import calculate
print(calculate.main('1+2'))