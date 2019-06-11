# by luffycity.com
# ==   比较   比较是值

# a = 'alex'
# b = 'alex'
# print(a == b)  True

# n = 10
# n1 = 10
# print(n == n1) True

# li1 = [1,2,3]
# li2 = [1,2,3]
# print(li1 == li2) True

# is 是  比较  比较的是内存地址

# a = 'alex'
# print(id(a))   # 36942544  内存地址

# n = 10
# print(id(n))     #1408197120

# li = [1,2,3]
# print(id(li))      #38922760

#字符串
# a = 'alex'
# b = 'alex'
# print(a is b)  #True
#数字
# n = 10
# n1 = 10
# print(n is n1)   #True

#========================================================

#小数据池

    # 数字小数据池的范围  -5 ~ 256
    # 字符串中如果有特殊字符他们的内存地址就不一样
    # 字符串中单个*20以内他们的内存地址一样,单个*21以上内存地址不一致

    # 黑框框 == 终端

# a = 'alex@'
# a1 = 'alex@'
# print(a is a1)    # Fales

# n = 5//2
# n1 = 2
# print(n is n1)    #True

# a = 'a'*21
# b = 'a'*21
# print(a is b)

# a = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# b = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# print(a is b)




# n = -6
# n1 = -6
# print(n is n1)  #False

# n = -5
# n1 = -5
# print(n is n1)    #True


# n = 257
# n1 = 257
# print(n is n1)     #True


#总结:

    # == 比较   比较的俩边的值

    # is   比较   比较的是内存地址   id()





#列表
# li =[1,2,3]
# li2 =[1,2,3]
# print(li is li2)  #False
#元组
# tu =(1,2,3)
# tu1 =(1,2,3)
# print(tu is tu1)   # False
#字典
# dic1 = {'name':'alex'}
# dic = {'name':'alex'}
# print(dic1 is dic)    #False