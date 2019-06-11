# by luffycity.com
# while 1:
#     print("打开手机")
#     print("打开陌陌")
#     print("搜索一下你心仪的对象")
#     print("走吧. 出去玩啊")
#     print("出发!")

# 定义了一个动作或者功能
# define
# def yue():
#     print("打开手机")
#     print("打开陌陌")
#     # 可以终止一个函数执行
#     return "大妈", "阿姨", "嫂子","姑娘"
#     print("搜索一下你心仪的对象")
#     print("走吧. 出去玩啊")
#     print("出发!")
#
# # 多个返回值接收到的是元组
# ret = yue()
# print(ret)
# yue()

# 写函数. 让用户输入a和b, 返回a+b的结果
# def sum():
#     a = int(input("请输入一个a:"))
#     b = int(input("请输入一个b:"))
#     c = a + b
#     return c
# ret = sum()
# print(ret)

# 在函数声明的位置的变量:形参
# def yue(tools): # tools就是个变量
#     print("打开手机")
#     print("打开%s" % tools)
#     print("搜索一下你心仪的对象")
#     print("走吧. 出去玩啊")
#     print("出发!")
#
# # 在函数调用的地方给的具体的值: 实参
# yue("探探")
# yue("微信")
# yue("陌陌")
# yue("alex")

# 吃
# 位置参数, 当函数的参数很多的时候, 必须要记住每一个位置是什么
# 关键字参数, 按照形参的名字给形参传值
# def chi(good_food, no_good_food, drink, ice_cream): # 形参位置参数
#     print(good_food, no_good_food, drink, ice_cream)
#
# # chi("大白梨", "法国大蜗牛", "卫龙辣条",  "哈根达斯")
# # chi(drink="神仙水", ice_cream="老冰棍", good_food="盖浇饭", no_good_food="锅包肉")
# chi("盖浇饭", "汉堡", ice_cream="巧乐兹", drink="营养快线") # 顺序:先位置后关键字


def regist(name, phone, gender="男"): # 默认值参数必须在参数列表的最后
    print(name, phone, gender)

regist("阿凡达", "10086")
regist("阿凡提", "10010")
regist("阿甘", "10000")
regist("女神","13315251","女")
