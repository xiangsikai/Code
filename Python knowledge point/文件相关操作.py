# by luffycity.com

# f = open("阿西吧", mode="r", encoding="utf-8")
# for line in f:
#     print(line.strip())
#
# f.seek(0) # 移动到开头
#
# for line in f:
#     print(line.strip())
#
# f.close()

# f = open("阿西吧", mode="r", encoding="utf-8")
# f.seek(3) # 3byte => 1中文
# s = f.read(1) # 读取一个字符
# print(f.tell()) # 光标在哪儿???
# f.close()

# seek(偏移量, 位置)
# seek(0) # 开头
# seek(0,2) # 在末尾的偏移量是0 末尾

f = open("啊同类个同同同", mode="w", encoding="utf-8")
f.write("哇哈哈哈哈压缩盖伦")
f.seek(9)
print(f.tell())
# 从文件开头截断到光标位置
# 如果给参数. 从头截断到参数位置
f.truncate(12)
f.close()
