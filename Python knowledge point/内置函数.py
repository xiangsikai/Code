# by luffycity.com
import os

# lst = ["白蛇传","骷髅叹","庄周闲游"]

# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(dir(str))
# it = iter(lst) # 内部封装的就是__iter__()
# print(it.__next__())
# print(next(it)) # 内部封装的是__next__()

# print("哈哈")

# lst = (1,2,3,4,5,6)
# print(id(lst))
#
# print(hash(lst)) # 目的是为了存储. 计算之后是一个数字. hash值尽量的不要重复(在某些特定环境下hash可能会重复)
#
# dic = {"jay":"周杰伦", "jj": "林俊杰"}

# print(dir(str)) # 所有方法名字
#
# print(help(str)) # 帮助文档

# def a():
#     pass
# # a() # 10不是函数 . 10不是可以被调用的
# print(callable(a)) # 是否可以被调用执行


#  根号下的内容都是正数
# i**2 == -1 # i 叫虚数
# 复数 = 实数+虚数  3+2i
# print(0.00125e3)

# print(bin(3)) #  5的二进制  0b二进制
# print(oct(8)) # 0o八进制
# print(hex(15)) # 0x十六进制  0123456789ABCDEF



# 注册, 实名认证, 银行卡, 风险评估
# 01      01       01     01
# 1111
# 1101


# print(abs(32)) # 绝对值 |绝对值| 取模
# print(divmod(10, 3)) # 计算商和余数
# print(round(4.51)) # 四舍五入
# print(pow(2, 4, 3)) # 求次幂, 第三个参数, 计算余数
# print(2**4)

# print(sum([1,2,3,4,5], 3))
#
# print(min([5,12,45,6,7,34])) # 最小值
# print(max([5,12,45,6,7,34])) # 最大值


# lst = ["马化腾", "马云", "马大帅", "马超"]
# ll = reversed(lst)  # reversed()翻转. 返回迭代器
# print(list(ll))

# lst = ["马化腾", "马云", "马大帅", "马超"]
# s = slice(1,3,2) #  切片
# print(lst[s])
# print(lst[1:3:2])


# s = "你好啊. 不要睡了. 我也困"
# print(memoryview(s.encode("utf-8"))) # 还不如id()


# print(ord('a')) # 查看字母a的编码位置 97
# print(ord("A")) # 65
# print(ord("中")) # 20013
#
# print(chr(20013))

'''
25105
29233
20320

print(ord("我")) #
print(ord("爱")) #
print(ord("你")) #


print(ascii("a"))
print(ascii("中")) # 
'''

# 周杰伦说:"昆凌特别难看"
# print('周杰伦说:"昆凌特别难看"')
#
# print("周杰伦说:\"昆凌特别难看\"") # \" 转义. 不让"作为字符串的开头或者结尾
# print("哈哈\\\呵呵") # \\ 表示的是一个\    \ 转义. \n换行 \t制表符 \", \', \\
# print(repr("周杰伦说:\n\t昆凌特别难看\t"))  # 对象的规范字符串表示形式???????
#
# print("")
# C: \在字符串中是转义字符,
# \n 换行
# \t 制表符
# \\ \
# \"  "
# \'  '

# print("\\\\\哈哈")

# 原样输出字符串
# print(repr("你好啊\n我不好")) # 还原回来了

# 今天吃\n什么 注入

# format

# s = "抽烟"
# print(s.center(20)) # 拉长到20 源字符串居中
#
# print(format(s,"^20")) # 居中
# print(format(s,">20")) # 右对齐
# print(format(s,"<20")) # 左对齐


# print(format(3, 'b'))   # 二进制 11
# print(format(97, 'c' ))   # 转换成unicode字符
# print(format(11, 'd' ))   # 十进制
# print(format(11, 'o' ))   # ⼋进制
# print(format(11, 'x' ))   # ⼗六进制(⼩写字⺟)
# print(format(11, 'X' ))   # ⼗六进制(⼤写字⺟)
# print(format(11, 'n' ))   # 和d⼀样
# print(format(11))   # 和d⼀样

# 浮点数
# print(format (123456789, 'e' ))   # 科学计数法. 默认保留6位⼩数
# print(format (123456789, '0.2e' ))   # 科学计数法. 保留2位⼩数(⼩写)
# print(format (123456789, '0.2E' ))   # 科学计数法. 保留2位⼩数(⼤写)
# print(format (1.23456789, 'f' ))   # ⼩数点计数法. 保留6位⼩数
# print(format (1.23456789, '0.2f' ))   # ⼩数点计数法. 保留2位⼩数
# print(format (1.23456789, '0.10f'))   # ⼩数点计数法. 保留10位⼩数
# print(format (1.23456789e+10000, 'F' ))   # ⼩数点计数法. INF 无穷大

# 原样输出
# print(r"你好啊\n 我不好\n\好不好\t, 他好我也好\", 到底谁好")

# s = {"爱情公寓", "爵迹", "妖猫传", "煎饼侠", "郭德纲的电影"}
#
# s.add("空天猎") # 可变, 不可哈希
# print(s)
# print(hash(s)) # 可变

# s = frozenset({"战狼2", "我不是药神", "西虹市首富", "捉妖记"})
# print(hash(s)) # 可哈希, 不可变

# lst = ["张国荣", "黄渤", "郭达森", "泰森", "甄子丹"]
#
# for el in lst:
#     print(el)
#
# for i in range(len(lst)):
#     print(i, lst[i])
#
# for i, el in enumerate(lst):
#     print(i, el)

# all() and
# print(all([True, 1, 1, 1]))
#
# # any() or
# print(any([1, 1, 0, 0]))
#
# # 所有的空 都是False

# zip() 压缩
# lst1 = ["甜蜜蜜", "往事只能回味", "难忘今宵", "分红的回忆", "十年"]
# lst2 = ["邓丽君", "韩宝仪", "李谷一", "王宝强", "陈奕迅"]
# lst3 = ["2000","3000","5","120","50000"]
# a = zip(lst1, lst2,lst3) # 水桶效应
# print("__iter__" in dir(a)) # 可迭代的
# for el in a:
#     print(el)


# s = "5 + 6"
# ret = eval(s) # 动态执行一个代码片段, 侧重点在返回上
# print(ret)
#
# a = "{'name':'汪峰', 'age':'48', 'wife':{'name':'国际章','age':'38'}}" # json. 像字典一样的东西
# d = eval(a) # 还原回字典,列表.
# print(d['name'])



# s = "a = 10"
# exec(s) # 执行代码
# print(a) # pycharm里的报错信息. 不一定是对的

# content = input("请输入你的代码:")
# exec(content)
# print(a)

# s = "for i in range(10): print(i)"
# c = compile(s, "", "exec")
# exec(c)
#
# s = "5+9"
# c = compile(s, "", "eval")
# ret = eval(c)
# print(ret)

# s = "content = input('请输入你的名字:')"
# c = compile(s, "", "single") 编译
#
# exec(c) 执行
# print(content)


# 编程大赛
# 收卷子. 最终效率决定了排名, 用运行时间.