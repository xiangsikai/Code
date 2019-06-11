# by luffycity.com

# 带w的. 只要你操作了. 就会清空源文件
# 如果文件不存在. 会自动创建文件
# f = open("阿西吧", mode="w", encoding="utf-8")
# f.write("呀! 养狗了没有?\n")
# f.write("养狗四米大")
# f.flush()
# f.close()

# a模式
# 写的时候. 换行需要手动控制   \n
# f = open("阿西吧", mode="a", encoding="utf-8")
# f.write("四米大?")
# f.write("四米大")
# f.flush()
# f.close()

# rb, wb, ab, bytes如果处理的是非文本文件, mode里如果有b. encoding就不能给了
# f = open("c:/pdd.jpg", mode="rb") # 这里不能写encoding
# e = open("e:/pdd.jpg", mode="wb")
# for line in f: # 从c盘读取 line你是不知道读取了多少数据的
#     e.write(line)   # 写入到e盘
# f.close()
# e.flush()
# e.close()






















