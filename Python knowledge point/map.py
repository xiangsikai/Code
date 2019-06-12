# by luffycity.com

# lst = [1,4,7,2,5,8]

# 计算列表中没个数字的平方
# ll = []
# for el in lst:
#     ll.append(el**2)

# def func(el):
#     return el**2
# m = map(lambda el: el**2, lst) # 把后面的可迭代对象中的每一个元素传递给function, 结果就是function的返回值
#
# print(list(m))

# print("__iter__" in dir(m))

# 分而治之
# map(func1, map(func2, map(func3 , lst)))

# lst1 = [1, 3, 5, 7]
# lst2 = [2, 4, 6, 8, 10]
# # 水桶效应, zip()
# m = map(lambda x, y, z: x + y+ z, lst1, lst2, [5,1,2,3,6])
# print(list(m))
