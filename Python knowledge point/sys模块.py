# by luffycity.com
import sys
# sys 是和Python解释器打交道的
# sys.argv
# print(sys.argv)  # argv的第一个参数 是python这个命令后面的值
# usr = input('username')
# pwd = input('password')
# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr == 'alex' and pwd == 'alex3714':
#     print('登录成功')
# else:
#     exit()

# 1. 程序员 运维人员  在命令行运行代码
# 2. 操作系统input事件 阻塞 退出了CPU的竞争

# sys.path
# print(sys.path)
# 模块是存在解释器里的么??? 不是
# 模块应该是存在硬盘上
# 但是我在使用的时候 import --> 这个模块才到内存中

# 一个模块能否被顺利的导入 全看sys.path下面有没有这个模块所在的
# 自定义模块的时候 导入模块的时候 还需要再关注 sys.path

import re
# sys.modules
# print(sys.modules)  # 是我们导入到内存中的所有模块的名字 : 这个模块的内存地址
# print(sys.modules['re'].findall('\d','abc126'))