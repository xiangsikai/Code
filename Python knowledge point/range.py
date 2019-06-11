# by luffycity.com

# range()是一个可迭代对象
# 1. range(n)  0 -> n-1
# for i in range(10):
#     print(i)
# 2. range(m,n) m -> n-1
# for i in range(1,10):
#     print(i)
# 3. range(m,n,q) m -> n-1 每q个取一个
# for i in range(1,10,3):
#     print(i)

# for i in range(100, 90, -1):
#     print(i)
#       0        1      2         3            4        5
lst = ["砂锅", "馒头", "盖浇饭", "刀削面", "大麻花", "大煎饼"]
# 获取到列表的索引. 拿到索引之后. 可以拿到元素
for i in range(len(lst)):
    print(i)    # i就是lst的索引
    print(lst[i])
# for el in lst:
#     print(el)
