# by luffycity.com
import os
import shutil

# py2 + win：报错
# os.rename('a.text','b.txt')

# py2+py3
shutil.move('c.txt','a.txt')

# shutil.rmtree('D:\sylar\s15\day30')