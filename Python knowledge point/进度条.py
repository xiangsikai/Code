# by luffycity.com
""""""
# 第一个知识点
"""
import time
print('\r80%',end='')
time.sleep(2)
print('\r90%',end='')
"""
# 第二个知识点
"""
tpl = "进度条目前是%s%%" %(90,)
print(tpl)
"""
import time

def func(size,total_size):
    val = int(size/total_size * 100)
    time.sleep(0.1)
    print('\r%s%%|%s' %(val,"#"*val,), end='')

for i in range(101):
    func(i,100)

