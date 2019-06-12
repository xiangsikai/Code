# by luffycity.com

# lst = ["张无忌", "张铁林", "赵一宁", "石可心","马大帅"]

# def func(el):
#     if el[0] == '张':
#         return False # 不想要的
#     else:
#         return True # 想要的

# 筛选,
# f = filter(lambda el: el[0]!="张", lst) # 将lst中的每一项传递给func, 所有返回True的都会保留, 所有返回False都会被过滤掉
#
# print("__iter__" in dir(f)) # 判断是否可以进行迭代
# for e in f:
#     print(e)


# lst = [
#     {"name":"汪峰", "score":48},
#     {"name":"章子怡", "score":39},
#     {"name":"赵一宁","score":97},
#     {"name":"石可心","score":90}
# ]
#
# f = filter(lambda el: el['score'] < 60 , lst) # 去16期的人
#
# print(list(f))


