# by luffycity.com

import logging

logger = logging.basicConfig(filename='xxxxxxx.txt',
                             format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S',
                             level=30)

# logging.debug('x1') # 10
# logging.info('x2')  # 20
# logging.warning('x3') # 30
# logging.error('x4')    # 40
# logging.critical('x5') # 50
# logging.log(10,'x6')


import traceback

def func():
    try:
        a = a +1
    except Exception as e:
        # 获取当前错误的堆栈信息
        msg = traceback.format_exc()
        logging.error(msg)
func()