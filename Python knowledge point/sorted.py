# by luffycity.com

# lst = [16, 18, 32, 54, 12, 9]

# lst.sort() # list的方法

# print(lst)
#  内置函数中提供了一个通用的排序方案, sorted()
# s = sorted(lst)
# print(s)
#       0       1          0          1         1        0      0
# lst = ["聊斋", "西游记", "三国演义", "葫芦娃", "水浒传", "年轮", "亮剑"]
#
# def func(s):
#     return len(s)%2
#
# ll = sorted(lst, key=func)
#
# print(ll)
# key: 排序方案, sorted函数内部会把可迭代对象中的每一个元素拿出来交给后面的key
# 后面的key计算出一个数字. 作为当前这个元素的权重, 整个函数根据权重进行排序


lst = [
    {'name':"汪峰","age":48},
    {"name":"章子怡",'age':38},
    {"name":"alex","age":39},
    {"name":"wusir","age":32},
    {"name":"赵一宁","age":28}
    ]



ll = sorted(lst, key=lambda el: len(el['name']), reverse=True)
print(ll)


