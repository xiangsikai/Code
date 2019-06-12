# by luffycity.com
""""""
import logging


# 创建一个操作日志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger1 = logging.Logger('s1', level=logging.ERROR)
logger1.addHandler(file_handler)


logger1.error('123123123')



# 在创建一个操作日志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger2 = logging.Logger('s2', level=logging.ERROR)
logger2.addHandler(file_handler2)

logger2.error('666')