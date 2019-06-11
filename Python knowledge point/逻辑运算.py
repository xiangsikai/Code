# by luffycity.com

# 1. and 并且的含义. 左右两端同时为真. 结果才能是真.
# 2. or 或者的含义. 左右两端有一个是真. 结果就是真. 所有的条件都是假. 结果才是假
# 3. not 取反 非真既假, 非假既真
# 顺序: () => not => and => or  相同的运算. 从左往右算

# print(1>2 and 4<6 or 5>7)
# print(1 > 2 or 3 > 4)
# print(5>3 or 4<6)
# print(5>3 or 4>6)

# print(3>4 or 4<3  and  1==1) # False
# print(1 < 2  and  3 < 4 or 1>2 ) # True
# print(2 > 1  and  3 < 4 or 4 > 5 and  2 < 1) # True
# print(1 > 2  and  3 < 4 or 4 > 5 and  2 > 1  or 9 < 8) # False
# print(1 > 1  and  3 < 4 or 4 > 5 and  2 > 1  and  9 > 8 or 7 < 6) # False
# print(not  2 > 1  and 3 < 4  or 4 > 5  and 2 > 1  and 9 > 8  or 7 < 6) # False

# x or y 如果x是0 返回y, 如果x是非零, 返回x
# print(1 or 2) # 1
# print(1 or 0) # 1
# print(0 or 1) # 1
# print(0 or 2) # 2
# print(0 or 1 or 2 or 3)
# print(3 or 0 or 1 or 0 or 2)

# and和or相反. 不要去总结and.  记住or
# print(1 and 2) # 2
# print(0 and 2) # 0
# print(1 and 0) # 0
# print(0 and 1) # 0

# print(1 and 2 or 3)
# print(1 or 2 and 3)

# False: 0, True: 1(非零)
# print(1 and 2>3)
# print(2>3 and 1)
#
# print(1 > 2 or 0 and 3 < 6 or 5) # 先算and 后算or
print(2**32)

