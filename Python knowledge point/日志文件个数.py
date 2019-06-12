# by luffycity.com

import logging

logger1 = logging.basicConfig(filename='x1.txt',
                             format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S',
                             level=30)

logging.error('x4')
logging.error('x5')