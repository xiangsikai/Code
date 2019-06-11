# by luffycity.com

# 引入copy模块
import copy

lst1 = ["金毛狮王", "紫衫龙王", "青翼蝠王", "白眉鹰王",["张无忌","赵敏","周芷若"]]
# lst2 = lst1[:] # 浅拷贝
# lst2 = lst1.copy() # 浅拷贝
lst2 = copy.deepcopy(lst1)

# lst1[4].append("小昭")

print(lst1)
print(lst2)

print(id(lst1[4]))
print(id(lst2[4]))

# 1. 赋值操作. 没有创建新对象
# 2. 浅拷贝. 只拷贝第一层内容. [:]   copy()
# 3. 深拷贝. 把这个对象内部的内容全部拷贝一份. 引入copy模块. deepcopy()
