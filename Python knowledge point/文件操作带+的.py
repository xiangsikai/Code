# by luffycity.com

# 不论你读取了多少内容.光标在哪儿,写入的时候都是在结尾写入, 除非上来就写入, 这时写入是在开头
# 最好用的读写同时存在的模式
# r+ 读写模式. 先读后写
# w+ 写读模式. 先写后读
# f = open("阿西吧", mode="r+", encoding="utf-8")
# s = f.read(3) # 读取三个字符
# print(s)
# f.write("不养了. 送人") # 在末尾写

# f.write("葫芦娃")
# s = f.read()
# print(s)
# s = f.read(2)
# print(s)
# f.write("还有何云伟")
# f.close()

# 很少用. 因为会清空文件中的内容
# f = open("阿西吧", mode="w+", encoding="utf-8")
# f.write("张云雷也要退出德云社") # 写完之后光标在最后. 读取是没有内容的
# f.seek(0) # 移动光标, 移动到开头
# s = f.read()
# print("读取的内容是",s)
# f.flush()
# f.close()

# a+
f = open("阿西吧", mode="a+", encoding="utf-8")
f.write("我要加入德云社")
f.seek(0)
s = f.read()
print(s)
f.flush()
f.close()