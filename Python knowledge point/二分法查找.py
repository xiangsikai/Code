# by luffycity.com


# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101 , 238 , 345 , 456 , 567 , 678 , 789 ]
# n = 79

# for el in lst:
#     if el == n: # O(1)
#         print("找到了")
#         break
# else:
#     print("没有")


# 使用二分法可以提高效率, 前提条件:有序序列
# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101 , 238 , 345 , 456 , 567 , 678 , 789]
#
# n = 88
# #
# left = 0
# right = len(lst)-1
#
# while left <= right: # 边界, 当右边比左边还小的时候退出循环
#     mid = (left + right)//2 # 必须是整除. 因为索引没有小数
#     if lst[mid] > n:
#         right = mid - 1
#     if lst[mid] < n:
#         left = mid + 1
#     if lst[mid] == n:
#         print("找到了这个数")
#         break
# else:
#     print("没有这个数")


# 递归来完成二分法
lst = [22, 33, 44, 55, 66, 77, 88, 99, 101 , 238 , 345 , 456 , 567 , 678 , 789]
def func(n, left, right):
    if left <= right: # 边界
        print("哈哈")
        mid = (left + right)//2
        if n > lst[mid]:
            left = mid + 1
            return func(n, left, right) # 递归  递归的入口
        elif n < lst[mid]:
            right = mid - 1
            # 深坑. 函数的返回值返回给调用者
            return func(n, left, right)    # 递归
        elif n == lst[mid]:
            print("找到了")
            return mid
            # return  # 通过return返回. 终止递归
    else:
        print("没有这个数") # 递归的出口
        return -1 # 1, 索引+ 2, 什么都不返回, None
# 找66, 左边界:0,  右边界是:len(lst) - 1
ret = func(70, 0, len(lst) - 1)
print(ret) # 不是None







