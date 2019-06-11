lst = []

with open("2018-08-06.log", mode="r", encoding="utf-8") as f:
    first = f.readline().strip().split(",")
    for line in f:
        dic = {} # 每一行一个字典
        # 1,alex,10086,特斯拉
        ls = line.strip().split(",")
        for i in range(len(first)):
            dic[first[i]] = ls[i]

        lst.append(dic)

print(lst)

