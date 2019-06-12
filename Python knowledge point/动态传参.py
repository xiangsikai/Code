# by luffycity.com
# def chi(good_food, no_good_food, drink, xx, xxx,ice_cream):
#     print(good_food, no_good_food, no_good_food, drink, ice_cream)
#
# chi("盖浇饭","馒头","腊肠", "橙汁","哈根达斯")
#  顺序: 位置参数=>*args(arguments) => 默认值参数
# * 在这里表示接收位置参数的动态传参, 接收到的是元组
# def chi(name,*food, location="北京"): # 参数名是food  *表示动态传参
#     print(location)
#     print(name+"要吃", food)
#
# chi("刘旺鑫","狗不理","大麻花","天津")
# # chi("刘旺鑫","大米饭","小米饭")
# # chi("刘旺鑫","馒头")

# 关键字的动态传参
# def chi(*foo2, **food): # 无敌传参
#     print(food)
#
# chi(good_food="狗不理", no_good_food="汉堡",drink="大白梨",ice_cream="巧乐兹")

# 顺序
# 位置参数, *args, 默认值参数, **kwargs
# 随以上参数可以意搭配使用

# 1. 实参:
#    位置参数
#     关键字参数
#     混合参数(位置, 关键字)
# 2. 形参:
#     位置参数
#     默认值参数
#     动态传参:
#         *args: 位置参数动态传参
#         **kwargs: 关键字参数动态传参
#     顺序: 位置, *args, 默认值, **kwargs
# def fun(a, *args, c="哈哈",  **kwargs):
#     print(a, args, c, kwargs)
# fun(1, 2, 3, 4,5, 6)

# 单行注释
'''多行注释'''
# 函数注释
# def func(a, b):
#     """
#     这个函数是用来计算a和b的和
#     :param a: 第一个数据
#     :param b: 第二个数据
#     :return: 返回的是两个数的和
#     """
#     return a + b
#
# print(func.__doc__) # document文档

# 接收所有参数
# def func(*args, **kwargs):# 无敌 *args相当于一个聚合的作用
#    print(args, kwargs)
#
# func(1,2,3,4,5,a=6,b=7,c=9)

# 形参: 聚合
# def func(*food): # 聚合, 位置参数
#     print(food)
# lst = ["鸡蛋","煎饼果子","猪蹄","滋滋冒油"]
# # 实参: 打散
# func(*lst) # 打散. 把list, tuple, set, str 进行迭代打散

# 聚合成关键字参数
# def func(**kwargs):
#     print(kwargs)
#
# dic = {"name":'alex', 'age':'18'}
# func(**dic) # 打散成关键字参数

