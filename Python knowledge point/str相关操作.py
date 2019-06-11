# by luffycity.com

# s = "al1ex is a gay and Wu傻sir is A gay too"

# s1 = s.capitalize() # 把首字母变成大写
# print(s1)

# s2 = s.lower() # 小写
# print(s2)

# s3 = s.upper()  # 大写
# print(s3)

# s4 = s.swapcase() # 大小写互换
# print(s4)

# s2 = "БBß"  # 俄美德
# print(s2)
# print(s2.lower())
# print(s2.casefold())

# s5 = s.title() # 把每个单词的首字母大写
# print(s5)

# s = "sb"
# s1 = s.center(10, "*") # 强行使用*在原字符串左右两端进行拼接. 拼接成10个单位
# print(s1)

# s = "    alex    is    a   gay   "
# s1 = s.strip() # 默认去掉空格. 空白\t \n
# print(s1)

# username = input("请输入用户名:").strip()
# password = input("请输入密码:").strip()
# if username == 'alex' and password =="123":
#     print("成功")
# else:
#     print("失败")

# s = "sb alex wusir sb sb taibai taibai sb"
# print(s.strip("sb")) # 可以指定要去掉的内容

# s = "泰坦尼克号, 西虹市首富, 小猪佩奇, 冒险王"
# s1 = s.replace("冒险王", "西西里的美丽传说")
# s2 = s.replace("佩奇", "wusir")
# print(s2)
#
# s = "alex_wusir_taibai_ritian"
# s1 = s.replace("_","")
# print(s1)

# s8 = "sylar_alex_taibai_wusir_eggon"
# # s9 = s8.replace("i", "sb", 2) # 换两次
# # print(s9)
#
# lst = s8.split("taibai") # 切完的结果是一个列表. 列表中装的是字符串. 用什么切. 就会损失掉什么
# print(lst)

# s = """我家大门常打开
# 开放怀抱等你
# 后面是什么歌词
# 我忘了"""
# lst = s.split("\n")
# print(lst)

# s = "我今天下午要去吃饭饭"
# lst = s.split("我今天下午要去吃饭饭哈哈哈") # 没切
# print(lst)

# s = "我叫%s, 我今年%s了, 我喜欢%s" % ("周杰伦", "40", "昆凌")
# print(s)

# s = "我叫{}, 我今年{}了, 我喜欢{}".format("周杰伦", "40", "昆凌")
# print(s)

# s = "我叫{0}, 我今年{1}了, 我喜欢{2}".format("周杰伦", "40", "昆凌")
# print(s)

# s = "我叫{name}, 我今年{age}了, 我喜欢{hobby}".format(hobby="周杰伦", age="40", name="昆凌")
# print(s)

# s = "alex is a gay"
# print(s.startswith("tory")) # 以xxx开头
# print(s.endswith("girl")) # 以xxx结尾

# s = "I have a dream. I want to kill you!"
# 都可以进行索引范围
# print(s.count("dream")) # 计算a在字符串中出现的次数
# print(s.find("a")) # 查找xxx在字符串中出现的位置. 只找第一次出现的位置, 没有就返回-1
# print(s.index("z")) # 当字符串不存在的时候. 报错


# s = "abcdefg1@"
# print(s.isdigit()) # %d
# print(s.isalpha()) # 字母
# print(s.isalnum()) # 是否由数字和字母组成

# s = "壹仟贰佰五十六萬拾"
# print(s.isnumeric())

# 字符串长度, python的内置函数len(), int(), bool(), str(), type()
# s = "娃哈哈可口可乐"
# print(len(s)) # 字符串中的字符的个数


# s = "王小利刘能赵四"
# # # 对字符串进行遍历.
# n = 0
# while n < len(s):
#     print(s[n])
#     n = n + 1
#
# # 迭代
# for c in s: # charactor
#     print(c)




