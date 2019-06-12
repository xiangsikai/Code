
# lst = []
# for i in range(1, 16):
#     lst.append("python"+str(i))
# print(lst)

# 推导式: 用一句话来生成一个列表
# lst = ["python"+str(j) for j in range(1,16)]
# print(lst)

# 语法:  [结果  for循环 判断]

# lst = [i for i in range(100) if i%2==1]
# print(lst)

# 100以内能被3整除的数的平方
# lst = [i*i for i in range(100) if i%3==0]
# print(lst)

# 寻找名字中带有两个e的人的名字
# names = [['Tom', 'Billy', 'Jefferson' , 'Andrew' , 'Wesley' , 'Steven' ,'Joe'],
#          [ 'Alice', 'Jill' , 'Ana', 'Wendy', 'Jennifer', 'Sherry' , 1]]
#
# lst = [name for line in names for name in line if type(name) == str and name.count("e") == 2]
# print(lst)

# lst = []
# for line in names:
#     for name in line:
#         if name.count("e") == 2:
#             print(name)
#

# [11,22,33,44] => {0:11,1:22,2:33}
# lst = [11,22,33,44]
# dic = {i:lst[i] for i in range(len(lst)) if i < 2} # 字典推导式就一行
# print(dic)
# 语法:{k:v for循环 条件筛选}

# dic = {"jj": "林俊杰", "jay": "周杰伦", "zs": "赵四", "ln":"刘能"}
# d = {v : k for k,v in dic.items()}
# print(d)


# s = {i for i in range(100)} # 可去除重复
# print(s)

# 集合推导式
lst = [1, 1, 4, 6,7,4,2,2]
s = { el for el in lst }
print(s)

# s = set(lst)
# print(s)