# by luffycity.com

# 引入模块
import os
import time

# 打开目标文件
# f1 = open("alex昨天干嘛去了", mode="r", encoding="utf-8")
with open("alex昨天又干嘛去了", mode="r", encoding="utf-8") as f1, \
    open("alex昨天又干嘛去了_副本", mode="w", encoding="utf-8") as f2:

    for line in f1:
        line = line.replace("alex", "sb")
        f2.write(line)

time.sleep(3)
# 删除文件
os.remove("alex昨天又干嘛去了")
time.sleep(3)
os.rename("alex昨天又干嘛去了_副本","alex昨天又干嘛去了")
